---
title: "Edge computing"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/index
retrieved_at: 2026-09-05T05:41:46.680478+00:00
---

# Edge computing

---

OpenShift Container Platform 4.22

## Configure and deploy OpenShift Container Platform clusters at the network edge

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140244016352480)

**Abstract**

This document describes how to configure and deploy OpenShift Container Platform clusters at the network edge.

---

## [Chapter 1. Challenges of the network far edge](#ztp-deploying-far-edge-clusters-at-scale) Copy linkLink copied to clipboard!

Edge computing presents complex challenges when managing many sites in geographically displaced locations. Use GitOps Zero Touch Provisioning (ZTP) to provision and manage sites at the far edge of the network.

### [1.1. Overcoming the challenges of the network far edge](#ztp-challenges-of-far-edge-deployments_ztp-deploying-far-edge-clusters-at-scale) Copy linkLink copied to clipboard!

Today, service providers want to deploy their infrastructure at the edge of the network. This presents significant challenges:

* How do you handle deployments of many edge sites in parallel?
* What happens when you need to deploy sites in disconnected environments?
* How do you manage the lifecycle of large fleets of clusters?

GitOps Zero Touch Provisioning (ZTP) and *GitOps* meets these challenges by allowing you to provision remote edge sites at scale with declarative site definitions and configurations for bare-metal equipment. Template or overlay configurations install OpenShift Container Platform features that are required for CNF workloads. The full lifecycle of installation and upgrades is handled through the GitOps ZTP pipeline.

GitOps ZTP uses GitOps for infrastructure deployments. With GitOps, you use declarative YAML files and other defined patterns stored in Git repositories. Red Hat Advanced Cluster Management (RHACM) uses your Git repositories to drive the deployment of your infrastructure.

GitOps provides traceability, role-based access control (RBAC), and a single source of truth for the desired state of each site. Scalability issues are addressed by Git methodologies and event driven operations through webhooks.

You start the GitOps ZTP workflow by creating declarative site definition and configuration custom resources (CRs) that the GitOps ZTP pipeline delivers to the edge nodes.

The following diagram shows how GitOps ZTP works within the far edge framework.

### [1.2. Using GitOps ZTP to provision clusters at the network far edge](#about-ztp_ztp-deploying-far-edge-clusters-at-scale) Copy linkLink copied to clipboard!

Red Hat Advanced Cluster Management (RHACM) manages clusters in a hub-and-spoke architecture, where a single hub cluster manages many spoke clusters. Hub clusters running RHACM provision and deploy the managed clusters by using GitOps Zero Touch Provisioning (ZTP) and the assisted service that is deployed when you install RHACM.

The assisted service handles provisioning of OpenShift Container Platform on single node clusters, three-node clusters, or standard clusters running on bare metal.

A high-level overview of using GitOps ZTP to provision and maintain bare-metal hosts with OpenShift Container Platform is as follows:

* A hub cluster running RHACM manages an OpenShift image registry that mirrors the OpenShift Container Platform release images. RHACM uses the OpenShift image registry to provision the managed clusters.
* You manage the bare-metal hosts in a YAML format inventory file, versioned in a Git repository.
* You make the hosts ready for provisioning as managed clusters, and use RHACM and the assisted service to install the bare-metal hosts on site.

Installing and deploying the clusters is a two-stage process, involving an initial installation phase, and a subsequent configuration and deployment phase. The following diagram illustrates this workflow:

### [1.3. Installing managed clusters with ClusterInstance resources and RHACM](#ztp-creating-ztp-crs-for-multiple-managed-clusters_ztp-deploying-far-edge-clusters-at-scale) Copy linkLink copied to clipboard!

GitOps Zero Touch Provisioning (ZTP) uses `ClusterInstance` custom resources (CRs) in a Git repository to manage the processes that install OpenShift Container Platform clusters. The `ClusterInstance` CR contains cluster-specific parameters required for installation. It has options for applying select configuration CRs during installation including user defined extra manifests.

The GitOps ZTP plugin processes `ClusterInstance` CRs to generate a collection of CRs on the hub cluster. This triggers the assisted service in Red Hat Advanced Cluster Management (RHACM) to install OpenShift Container Platform on the bare-metal host. You can find installation status and error messages in these CRs on the hub cluster. You can provision single clusters manually or in batches with GitOps ZTP:

Provisioning a single cluster
:   Create a single `ClusterInstance` CR and related configuration CRs for the cluster, and apply them in the hub cluster to begin cluster provisioning. This is a good way to test your CRs before deploying on a larger scale.

Provisioning many clusters
:   Install managed clusters in batches of up to 500 by defining `ClusterInstance` and related CRs in a Git repository. ArgoCD uses the `ClusterInstance` CRs to deploy the clusters. The RHACM policy generator creates the manifests and applies them to the hub cluster. This starts the cluster provisioning process.

### [1.4. Configuring managed clusters with policies and PolicyGenerator resources](#ztp-configuring-cluster-policies_ztp-deploying-far-edge-clusters-at-scale) Copy linkLink copied to clipboard!

GitOps Zero Touch Provisioning (ZTP) uses Red Hat Advanced Cluster Management (RHACM) to configure clusters by using a policy-based governance approach to applying the configuration.

The policy generator is a plugin for the GitOps Operator that enables the creation of RHACM policies from a concise template. The tool can combine multiple CRs into a single policy, and you can generate multiple policies that apply to various subsets of clusters in your fleet.

Note

For scalability and to reduce the complexity of managing configurations across the fleet of clusters, use configuration CRs with as much commonality as possible.

* Where possible, apply configuration CRs using a fleet-wide common policy.
* The next preference is to create logical groupings of clusters to manage as much of the remaining configurations as possible under a group policy.
* When a configuration is unique to an individual site, use RHACM templating on the hub cluster to inject the site-specific data into a common or group policy. Alternatively, apply an individual site policy for the site.

The following diagram shows how the policy generator interacts with GitOps and RHACM in the configuration phase of cluster deployment.

For large fleets of clusters, it is typical for there to be a high-level of consistency in the configuration of those clusters.

The following recommended structuring of policies combines configuration CRs to meet several goals:

* Describe common configurations once and apply to the fleet.
* Minimize the number of maintained and managed policies.
* Support flexibility in common configurations for cluster variants.

Expand

Table 1.1. Recommended PolicyGenerator policy categories

| Policy category | Description |
| --- | --- |
| Common | A policy that exists in the common category is applied to all clusters in the fleet. Use common `PolicyGenerator` CRs to apply common installation settings across all cluster types. |
| Groups | A policy that exists in the groups category is applied to a group of clusters in the fleet. Use group `PolicyGenerator` CRs to manage specific aspects of single-node, three-node, and standard cluster installations. Cluster groups can also follow geographic region, hardware variant, etc. |
| Sites | A policy that exists in the sites category is applied to a specific cluster site. Any cluster can have its own specific policies maintained. |

Show more

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

## [Chapter 2. Preparing the hub cluster for GitOps ZTP](#ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

To use RHACM in a disconnected environment, create a mirror registry that mirrors the OpenShift Container Platform release images and Operator Lifecycle Manager (OLM) catalog that contains the required Operator images. OLM manages, installs, and upgrades Operators and their dependencies in the cluster. You can also use a disconnected mirror host to serve the RHCOS ISO and RootFS disk images that are used to provision the bare-metal hosts.

### [2.1. Telco RAN DU 4.22 validated software components](#ztp-telco-ran-software-versions_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

The Red Hat telco RAN DU 4.22 solution has been validated using the following Red Hat software products for OpenShift Container Platform managed clusters.

Expand

Table 2.1. Telco RAN DU managed cluster validated software components

| Component | Software version |
| --- | --- |
| OpenShift Container Platform | 4.22 |
| Cluster Logging Operator | 6.5 |
| Local Storage Operator | 4.22 |
| OpenShift API for Data Protection (OADP) | 1.6 |
| PTP Operator | 4.22 |
| SR-IOV Operator | 4.22 |
| SRIOV-FEC Operator | 2.12 |
| Lifecycle Agent Operator | 4.22 |

Show more

* Cluster Logging Operator will be updated to 6.6 when the aligned Cluster Logging Operator version is released.

### [2.2. Recommended hub cluster specifications and managed cluster limits for GitOps ZTP](#ztp-gitops-ztp-max-spoke-clusters_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

With GitOps Zero Touch Provisioning (ZTP), you can manage thousands of clusters in geographically dispersed regions and networks. The Red Hat Performance and Scale lab successfully created and managed 3500 virtual single-node OpenShift clusters with a reduced DU profile from a single Red Hat Advanced Cluster Management (RHACM) hub cluster in a lab environment.

In real-world situations, the scaling limits for the number of clusters that you can manage will vary depending on various factors affecting the hub cluster. For example:

Hub cluster resources
:   Available hub cluster host resources (CPU, memory, storage) are an important factor in determining how many clusters the hub cluster can manage. The more resources allocated to the hub cluster, the more managed clusters it can accommodate.

Hub cluster storage
:   The hub cluster host storage IOPS rating and whether the hub cluster hosts use NVMe storage can affect hub cluster performance and the number of clusters it can manage.

Network bandwidth and latency
:   Slow or high-latency network connections between the hub cluster and managed clusters can impact how the hub cluster manages multiple clusters.

Managed cluster size and complexity
:   The size and complexity of the managed clusters also affects the capacity of the hub cluster. Larger managed clusters with more nodes, namespaces, and resources require additional processing and management resources. Similarly, clusters with complex configurations such as the RAN DU profile or diverse workloads can require more resources from the hub cluster.

Number of managed policies
:   The number of policies managed by the hub cluster scaled over the number of managed clusters bound to those policies is an important factor that determines how many clusters can be managed.

Monitoring and management workloads
:   RHACM continuously monitors and manages the managed clusters. The number and complexity of monitoring and management workloads running on the hub cluster can affect its capacity. Intensive monitoring or frequent reconciliation operations can require additional resources, potentially limiting the number of manageable clusters.

RHACM version and configuration
:   Different versions of RHACM can have varying performance characteristics and resource requirements. Additionally, the configuration settings of RHACM, such as the number of concurrent reconciliations or the frequency of health checks, can affect the managed cluster capacity of the hub cluster.

Use the following representative configuration and network specifications to develop your own Hub cluster and network specifications.

Important

The following guidelines are based on internal lab benchmark testing only and do not represent complete bare-metal host specifications.

Expand

Table 2.2. Representative three-node hub cluster machine specifications

| Requirement | Description |
| --- | --- |
| Server hardware | 3 x Dell PowerEdge R650 rack servers |
| NVMe hard disks | * 50 GB disk for `/var/lib/etcd` * 2.9 TB disk for `/var/lib/containers` |
| SSD hard disks | * 1 SSD split into 15 200GB thin-provisioned logical volumes provisioned as `PV` CRs * 1 SSD serving as an extra large `PV` resource |
| Number of applied DU profile policies | 5 |

Show more

Important

The following network specifications are representative of a typical real-world RAN network and were applied to the scale lab environment during testing.

Expand

Table 2.3. Simulated lab environment network specifications

| Specification | Description |
| --- | --- |
| Round-trip time (RTT) latency | 50 ms |
| Packet loss | 0.02% packet loss |
| Network bandwidth limit | 20 Mbps |

Show more

### [2.3. Installing GitOps ZTP in a disconnected environment](#installing-disconnected-rhacm_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

Use Red Hat Advanced Cluster Management (RHACM), Red Hat OpenShift GitOps, and Topology Aware Lifecycle Manager (TALM) on the hub cluster in the disconnected environment to manage the deployment of multiple managed clusters.

**Prerequisites**

* You have installed the OpenShift Container Platform CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.
* You have configured a disconnected mirror registry for use in the cluster.

  Note

  The disconnected mirror registry that you create must contain a version of TALM backup and pre-cache images that matches the version of TALM running in the hub cluster. The spoke cluster must be able to resolve these images in the disconnected mirror registry.

**Procedure**

* Install RHACM in the hub cluster. See [Installing RHACM in a disconnected environment](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/install/installing#install-on-disconnected-networks).
* Install GitOps and TALM in the hub cluster.

### [2.4. Adding RHCOS ISO and RootFS images to the disconnected mirror host](#ztp-acm-adding-images-to-mirror-registry_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

Before you begin installing clusters in the disconnected environment with Red Hat Advanced Cluster Management (RHACM), you must first host Red Hat Enterprise Linux CoreOS (RHCOS) images for it to use. Use a disconnected mirror to host the RHCOS images.

**Prerequisites**

* Deploy and configure an HTTP server to host the RHCOS image resources on the network. You must be able to access the HTTP server from your computer, and from the machines that you create.

Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. You require ISO and RootFS images to install RHCOS on the hosts. RHCOS QCOW2 images are not supported for this installation type.

**Procedure**

1. Log in to the mirror host.
2. Obtain the RHCOS ISO and RootFS images from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/), for example:

   1. Export the required image names and OpenShift Container Platform version as environment variables:

      ```
      $ export ISO_IMAGE_NAME=<iso_image_name>
      ```

      ```
      $ export ROOTFS_IMAGE_NAME=<rootfs_image_name>
      ```

      ```
      $ export OCP_VERSION=<ocp_version>
      ```

      where:

      `<iso_image_name>`
      :   ISO image name, for example, `rhcos-4.22.1-x86_64-live.x86_64.iso`

      `<rootfs_image_name>`
      :   RootFS image name, for example, `rhcos-4.22.1-x86_64-live-rootfs.x86_64.img`

      `<ocp_version>`
      :   OpenShift Container Platform version, for example, `4.22.1`
   2. Download the required images:

      ```
      $ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.22/${OCP_VERSION}/${ISO_IMAGE_NAME} -O /var/www/html/${ISO_IMAGE_NAME}
      ```

      ```
      $ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.22/${OCP_VERSION}/${ROOTFS_IMAGE_NAME} -O /var/www/html/${ROOTFS_IMAGE_NAME}
      ```

**Verification**

* Verify that the images downloaded successfully and are being served on the disconnected mirror host, for example:

  ```
  $ wget http://$(hostname)/${ISO_IMAGE_NAME}
  ```

  Example output:

  ```
  Saving to: rhcos-4.22.1-x86_64-live.x86_64.iso
  rhcos-4.22.1-x86_64-live.x86_64.iso-  11%[====>    ]  10.01M  4.71MB/s
  ```

### [2.5. Enabling the assisted service](#enabling-assisted-installer-service-on-bare-metal_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

Red Hat Advanced Cluster Management (RHACM) uses the assisted service to deploy OpenShift Container Platform clusters. The assisted service is deployed automatically when you enable the MultiClusterHub Operator on Red Hat Advanced Cluster Management (RHACM). After that, you need to configure the `Provisioning` resource to watch all namespaces and to update the `AgentServiceConfig` custom resource (CR) with references to the ISO and RootFS images that are hosted on the mirror registry HTTP server.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have RHACM with `MultiClusterHub` enabled.

**Procedure**

1. Enable the `Provisioning` resource to watch all namespaces and configure mirrors for disconnected environments. For more information, see [Enabling the central infrastructure management service](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.9/html/clusters/cluster_mce_overview#enable-cim).
2. Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command:

   ```
   $ oc edit AgentServiceConfig
   ```
3. Update the `spec.osImages` field in the `AgentServiceConfig` CR:

   ```
   apiVersion: agent-install.openshift.io/v1beta1
   kind: AgentServiceConfig
   metadata:
    name: agent
   spec:
   # ...
     osImages:
       - cpuArchitecture: x86_64
         openshiftVersion: "4.22"
         rootFSUrl: https://<host>/<path>/rhcos-live-rootfs.x86_64.img
         url: https://<host>/<path>/rhcos-live.x86_64.iso
   ```

   where:

   `<host>`
   :   Specifies the fully qualified domain name (FQDN) for the target mirror registry HTTP server.

   `<path>`
   :   Specifies the path to the image on the target mirror registry.
4. Save and quit the editor to apply the changes.

### [2.6. Configuring the hub cluster to use a disconnected mirror registry](#ztp-configuring-the-cluster-for-a-disconnected-environment_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

You can configure the hub cluster to use a disconnected mirror registry for a disconnected environment.

**Prerequisites**

* You have a disconnected hub cluster installation with Red Hat Advanced Cluster Management (RHACM) 2.17 installed.
* You have hosted the `rootfs` and `iso` images on an HTTP server. See the *Additional resources* section for guidance about *Mirroring the OpenShift Container Platform image repository*.

Warning

If you enable TLS for the HTTP server, you must confirm the root certificate is signed by an authority trusted by the client and verify the trusted certificate chain between your OpenShift Container Platform hub and managed clusters and the HTTP server. Using a server configured with an untrusted certificate prevents the images from being downloaded to the image creation service. Using untrusted HTTPS servers is not supported.

**Procedure**

1. Create a `ConfigMap` containing the mirror registry config:

   ```
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: assisted-installer-mirror-config
     namespace: multicluster-engine
     labels:
       app: assisted-service
   data:
     ca-bundle.crt: |
       -----BEGIN CERTIFICATE-----
       <certificate_contents>
       -----END CERTIFICATE-----

     registries.conf: |
       unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

       [[registry]]
          prefix = ""
          location = "quay.io/example-repository"
          mirror-by-digest-only = true

          [[registry.mirror]]
          location = "mirror1.registry.corp.com:5000/example-repository"
   ```

   where:

   `namespace: multicluster-engine`
   :   The `ConfigMap` namespace must be set to `multicluster-engine`.

   `ca-bundle.crt`
   :   The mirror registry’s certificate that is used when creating the mirror registry.

   `registries.conf`
   :   The configuration file for the mirror registry. The mirror registry configuration adds mirror information to the `/etc/containers/registries.conf` file in the discovery image. The mirror information is stored in the `imageContentSources` section of the `install-config.yaml` file when the information is passed to the installation program. The Assisted Service pod that runs on the hub cluster fetches the container images from the configured mirror registry.

   `location = "quay.io/example-repository"`
   :   The URL of the mirror registry. You must use the URL from the `imageContentSources` section by running the `oc adm release mirror` command when you configure the mirror registry. For more information, see the *Mirroring the OpenShift Container Platform image repository* section.

   `location = "mirror1.registry.corp.com:5000/example-repository"`
   :   The registries defined in the `registries.conf` file must be scoped by repository, not by registry. In this example, both the `quay.io/example-repository` and the `mirror1.registry.corp.com:5000/example-repository` repositories are scoped by the `example-repository` repository.

   This updates `mirrorRegistryRef` in the `AgentServiceConfig` custom resource, as shown in this example output:

   ```
   apiVersion: agent-install.openshift.io/v1beta1
   kind: AgentServiceConfig
   metadata:
     name: agent
     namespace: multicluster-engine
   spec:
     databaseStorage:
       volumeName: <db_pv_name>
       accessModes:
       - ReadWriteOnce
       resources:
         requests:
           storage: <db_storage_size>
     filesystemStorage:
       volumeName: <fs_pv_name>
       accessModes:
       - ReadWriteOnce
       resources:
         requests:
           storage: <fs_storage_size>
     mirrorRegistryRef:
       name: assisted-installer-mirror-config
     osImages:
       - openshiftVersion: <ocp_version>
         url: <iso_url>
   ```

   where:

   `namespace: multicluster-engine`
   :   Set the `AgentServiceConfig` namespace to `multicluster-engine` to match the `ConfigMap` namespace.

   `assisted-installer-mirror-config`
   :   Set `mirrorRegistryRef.name` to match the definition specified in the related `ConfigMap` CR.

   `<ocp_version>`
   :   Set the OpenShift Container Platform version to either the x.y or x.y.z format.

   `<iso_url>`
   :   Set the URL for the ISO hosted on the `httpd` server.

   Important

   A valid NTP server is required during cluster installation. Ensure that a suitable NTP server is available and can be reached from the installed clusters through the disconnected network.

### [2.7. Configuring the hub cluster to use unauthenticated registries](#ztp-configuring-the-hub-cluster-to-use-unauthenticated-registries_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

You can configure the hub cluster to use unauthenticated registries. Unauthenticated registries does not require authentication to access and download images.

**Prerequisites**

* You have installed and configured a hub cluster and installed Red Hat Advanced Cluster Management (RHACM) on the hub cluster.
* You have installed the OpenShift Container Platform CLI (oc).
* You have logged in as a user with `cluster-admin` privileges.
* You have configured an unauthenticated registry for use with the hub cluster.

**Procedure**

1. Update the `AgentServiceConfig` custom resource (CR) by running the following command:

   ```
   $ oc edit AgentServiceConfig agent
   ```
2. Add the `unauthenticatedRegistries` field in the CR:

   ```
   apiVersion: agent-install.openshift.io/v1beta1
   kind: AgentServiceConfig
   metadata:
     name: agent
   spec:
     unauthenticatedRegistries:
     - example.registry.com
     - example.registry2.com
     ...
   ```

   Unauthenticated registries are listed under `spec.unauthenticatedRegistries` in the `AgentServiceConfig` resource. Any registry on this list is not required to have an entry in the pull secret used for the spoke cluster installation. `assisted-service` validates the pull secret by making sure it contains the authentication information for every image registry used for installation.

   Note

   Mirror registries are automatically added to the ignore list and do not need to be added under `spec.unauthenticatedRegistries`. Specifying the `PUBLIC_CONTAINER_REGISTRIES` environment variable in the `ConfigMap` overrides the default values with the specified value. The `PUBLIC_CONTAINER_REGISTRIES` defaults are [quay.io](https://quay.io) and [registry.svc.ci.openshift.org](https://registry.svc.ci.openshift.org).

**Verification**

Verify that you can access the newly added registry from the hub cluster by running the following commands:

1. Open a debug shell prompt to the hub cluster:

   ```
   $ oc debug node/<node_name>
   ```
2. Test access to the unauthenticated registry by running the following command:

   ```
   sh-4.4# podman login -u kubeadmin -p $(oc whoami -t) <unauthenticated_registry>
   ```

   where:

   <unauthenticated\_registry>
   :   Is the new registry, for example, `unauthenticated-image-registry.openshift-image-registry.svc:5000`.

   **Example output**

   ```
   Login Succeeded!
   ```

### [2.8. Configuring the hub cluster with ArgoCD](#ztp-configuring-hub-cluster-with-argocd_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

You can configure the hub cluster with a set of ArgoCD applications that generate the required installation and policy custom resources (CRs) for each site with GitOps Zero Touch Provisioning (ZTP).

Note

Red Hat Advanced Cluster Management (RHACM) uses `ClusterInstance` CRs to generate the Day 1 managed cluster installation CRs for ArgoCD. Each ArgoCD application can manage a maximum of 1000 `ClusterInstance` CRs.

**Prerequisites**

* You have a OpenShift Container Platform hub cluster with Red Hat Advanced Cluster Management (RHACM) and Red Hat OpenShift GitOps installed.
* You have extracted the reference deployment from the GitOps ZTP plugin container as described in the "Preparing the GitOps ZTP site configuration repository" section. Extracting the reference deployment creates the `out/argocd/deployment` directory referenced in the following procedure.

**Procedure**

1. Prepare the ArgoCD pipeline configuration:

   1. Create a Git repository with the directory structure similar to the example directory. For more information, see "Preparing the GitOps ZTP site configuration repository".
   2. Configure access to the repository using the ArgoCD UI. Under **Settings** configure the following:

      * **Repositories** - Add the connection information. The URL must end in `.git`, for example, `https://repo.example.com/repo.git` and credentials.
      * **Certificates** - Add the public certificate for the repository, if needed.
   3. Modify the two ArgoCD applications, `out/argocd/deployment/clusters-app.yaml` and `out/argocd/deployment/policies-app.yaml`, based on your Git repository:

      * Update the URL to point to the Git repository. The URL ends with `.git`, for example, `https://repo.example.com/repo.git`.
      * The `targetRevision` indicates which Git repository branch to monitor.
      * `path` specifies the path to the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs, respectively.

2. To install the GitOps ZTP plugin, patch the ArgoCD instance in the hub cluster with the relevant multicluster engine (MCE) subscription image. Customize the patch file that you previously extracted into the `out/argocd/deployment/` directory for your environment.

   1. Select the `multicluster-operators-subscription` image that matches your RHACM version.

      * For RHACM 2.8 and 2.9, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel8:v<rhacm_version>` image.
      * For RHACM 2.10 and later, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v<rhacm_version>` image.

      Important

      The version of the `multicluster-operators-subscription` image must match the RHACM version. Beginning with the MCE 2.10 release, RHEL 9 is the base image for `multicluster-operators-subscription` images.

      Click `[Expand for Operator list]` in the "Platform Aligned Operators" table in [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) to view the complete supported Operators matrix for OpenShift Container Platform.
   2. Modify the `out/argocd/deployment/argocd-openshift-gitops-patch.json` file with the `multicluster-operators-subscription` image that matches your RHACM version:

      ```
      {
        "args": [
          "-c",
          "mkdir -p /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator && cp /policy-generator/PolicyGenerator-not-fips-compliant /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator/PolicyGenerator"
        ],
        "command": [
          "/bin/bash"
        ],
        "image": "registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v2.10",
        "name": "policy-generator-install",
        "imagePullPolicy": "Always",
        "volumeMounts": [
          {
            "mountPath": "/.config",
            "name": "kustomize"
          }
        ]
      }
      ```

      * Optional: For RHEL 9 images, in the `args` field, change the executable path from `/policy-generator/PolicyGenerator-not-fips-compliant` to match the required universal executable for your ArgoCD version.
      * Match the `multicluster-operators-subscription` image to your RHACM version. In disconnected environments, replace the URL with the disconnected registry equivalent for your environment.
   3. Patch the ArgoCD instance. Run the following command:

      ```
      $ oc patch argocd openshift-gitops \
      -n openshift-gitops --type=merge \
      --patch-file out/argocd/deployment/argocd-openshift-gitops-patch.json
      ```
3. In RHACM 2.7 and later, the multicluster engine enables the `cluster-proxy-addon` feature by default. Apply the following patch to disable the `cluster-proxy-addon` feature and remove the relevant hub cluster and managed pods that are responsible for this add-on. Run the following command:

   ```
   $ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type=merge --patch-file out/argocd/deployment/disable-cluster-proxy-addon.json
   ```
4. Apply the pipeline configuration to your hub cluster by running the following command:

   ```
   $ oc apply -k out/argocd/deployment
   ```
5. Optional: If you have existing ArgoCD applications, verify that the `PrunePropagationPolicy=background` policy is set in the `Application` resource by running the following command:

   ```
   $ oc -n openshift-gitops get applications.argoproj.io  \
   clusters -o jsonpath='{.spec.syncPolicy.syncOptions}' |jq
   ```

   Example output for an existing policy:

   ```
   [
     "CreateNamespace=true",
     "PrunePropagationPolicy=background",
     "RespectIgnoreDifferences=true"
   ]
   ```

   1. If the `spec.syncPolicy.syncOption` field does not contain a `PrunePropagationPolicy` parameter or `PrunePropagationPolicy` is set to the `foreground` value, set the policy to `background` in the `Application` resource. See the following example:

      ```
      kind: Application
      spec:
        syncPolicy:
          syncOptions:
          - PrunePropagationPolicy=background
      ```

   Setting the `background` deletion policy ensures that the `ManagedCluster` CR and all its associated resources are deleted.

### [2.9. Preparing the GitOps ZTP site configuration repository](#ztp-preparing-the-ztp-git-repository_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

Before you can use the GitOps Zero Touch Provisioning (ZTP) pipeline, you need to prepare the Git repository to host the site configuration data.

**Prerequisites**

* You have configured the hub cluster GitOps applications for generating the required installation and policy custom resources (CRs).
* You have deployed the managed clusters using GitOps ZTP.

**Procedure**

1. Create a directory structure with separate paths for the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs.

   Note

   Keep `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` CRs in separate directories. Both the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` directories must contain a `kustomization.yaml` file that explicitly includes the files in that directory.
2. Export the `argocd` directory from the `ztp-site-generate` container image using the following commands:

   ```
   $ podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22
   ```

   ```
   $ mkdir -p ./out
   ```

   ```
   $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./out
   ```
3. Check that the `out` directory contains the following subdirectories:

   * `out/extra-manifest` contains the source CR files that you use to create extra manifest `ConfigMap` resources through the `configMapGenerator` in the `kustomization.yaml` file. The `ClusterInstance` CR references these `ConfigMap` resources using the `extraManifestsRefs` field.
   * `out/source-crs` contains the source CR files that `PolicyGenerator` uses to generate the Red Hat Advanced Cluster Management (RHACM) policies.
   * `out/argocd/deployment` contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure.
   * `out/argocd/example/clusterinstance` contains the examples for `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration.
4. Copy the `out/source-crs` folder and contents to the `PolicyGenerator` or `PolicyGentemplate` directory.
5. The out/extra-manifests directory contains the reference manifests for a RAN DU cluster. Copy the `out/extra-manifests` directory into the `ClusterInstance` folder. This directory should contain CRs from the `ztp-site-generate` container only. Do not add user-provided CRs here. If you want to work with user-provided CRs you must create another directory for that content. For example:

   ```
   example/
     ├── acmpolicygenerator
     │   ├── kustomization.yaml
     │   └── source-crs/
     ├── policygentemplates
     │   ├── kustomization.yaml
     │   └── source-crs/
     └── clusterinstance
           ├── extra-manifests
           └── kustomization.yaml
   ```

   Note

   Using `PolicyGenTemplate` CRs to manage and deploy policies to manage clusters will be deprecated in a future OpenShift Container Platform release. Equivalent and improved functionality is available by using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.
6. Commit the directory structure and the `kustomization.yaml` files and push to your Git repository. The initial push to Git should include the `kustomization.yaml` files.

   You can use the directory structure under `out/argocd/example` as a reference for the structure and content of your Git repository. That structure includes `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` reference CRs for single-node, three-node, and standard clusters. Remove references to cluster types that you are not using.

   For all cluster types, you must:

   * Add the `source-crs` subdirectory to the `acmpolicygenerator` or `policygentemplates` directory.
   * Add the `extra-manifests` directory to the `clusterinstance` directory.

     The following example describes a set of CRs for a network of single-node clusters:

     ```
     example/
       ├── acmpolicygenerator
       │   ├── acm-common-ranGen.yaml
       │   ├── acm-example-sno-site.yaml
       │   ├── acm-group-du-sno-ranGen.yaml
       │   ├── group-du-sno-validator-ranGen.yaml
       │   ├── kustomization.yaml
       │   ├── source-crs/
       │   └── ns.yaml
       └── clusterinstance
             ├── example-sno.yaml
             ├── extra-manifests/
             ├── custom-manifests/
             ├── KlusterletAddonConfigOverride.yaml
             └── kustomization.yaml
     ```

     where:

     `extra-manifests/`
     :   Contains reference manifests from the `ztp-container`.

     `custom-manifests/`
     :   Contains custom manifests.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

### [2.10. Preparing the GitOps ZTP site configuration repository for version independence](#ztp-preparing-the-ztp-git-repository-ver-ind_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

You can use GitOps ZTP to manage source custom resources (CRs) for managed clusters that are running different versions of OpenShift Container Platform. This means that the version of OpenShift Container Platform running on the hub cluster can be independent of the version running on the managed clusters.

Note

The following procedure assumes you are using `PolicyGenerator` resources instead of `PolicyGentemplate` resources for cluster policies management.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a directory structure with separate paths for the `ClusterInstance` and `PolicyGenerator` CRs.
2. Within the `PolicyGenerator` directory, create a directory for each OpenShift Container Platform version you want to make available. For each version, create the following resources:

   * `kustomization.yaml` file that explicitly includes the files in that directory
   * `source-crs` directory to contain reference CR configuration files from the `ztp-site-generate` container

     If you want to work with user-provided CRs, you must create a separate directory for them.
3. In the `/clusterinstance` directory, create a subdirectory for each OpenShift Container Platform version you want to make available. For each version, create at least one directory for reference CRs to be copied from the container. There is no restriction on the naming of directories or on the number of reference directories. If you want to work with custom manifests, you must create a separate directory for them.

   The following example describes a structure using user-provided manifests and CRs for different versions of OpenShift Container Platform:

   ```
   ├── acmpolicygenerator
   │   ├── kustomization.yaml
   │   ├── version_4.13
   │   │   ├── common-ranGen.yaml
   │   │   ├── group-du-sno-ranGen.yaml
   │   │   ├── group-du-sno-validator-ranGen.yaml
   │   │   ├── helix56-v413.yaml
   │   │   ├── kustomization.yaml
   │   │   ├── ns.yaml
   │   │   └── source-crs/
   │   │      └── reference-crs/
   │   │      └── custom-crs/
   │   └── version_4.14
   │       ├── common-ranGen.yaml
   │       ├── group-du-sno-ranGen.yaml
   │       ├── group-du-sno-validator-ranGen.yaml
   │       ├── helix56-v414.yaml
   │       ├── kustomization.yaml
   │       ├── ns.yaml
   │       └── source-crs/
   │         └── reference-crs/
   │         └── custom-crs/
   └── clusterinstance
       ├── kustomization.yaml
       ├── version_4.13
       │   ├── helix56-v413.yaml
       │   ├── kustomization.yaml
       │   ├── extra-manifest/
       │   └── custom-manifest/
       └── version_4.14
           ├── helix57-v414.yaml
           ├── kustomization.yaml
           ├── extra-manifest/
           └── custom-manifest/
   ```

   where:

   `kustomization.yaml` (top-level)
   :   Create a top-level `kustomization` YAML file.

   `version_4.13`, `version_4.14`
   :   Create the version-specific directories within the custom `/acmpolicygenerator` directory.

   `kustomization.yaml` (per-version)
   :   Create a `kustomization.yaml` file for each version.

   `source-crs/`
   :   Create a `source-crs` directory for each version to contain reference CRs from the `ztp-site-generate` container.

   `reference-crs/`
   :   Create the `reference-crs` directory for policy CRs that are extracted from the ZTP container.

   `custom-crs/`
   :   Optional: Create a `custom-crs` directory for user-provided CRs.

   `extra-manifest/`
   :   Create a directory within the custom `/clusterinstance` directory to contain extra manifests from the `ztp-site-generate` container.

   `custom-manifest/`
   :   Create a folder to hold user-provided manifests.

   Note

   In the example directory structure, each version subdirectory in the custom `/clusterinstance` directory contains two further subdirectories, one containing the reference manifests copied from the container, the other for custom manifests that you provide. The names assigned to those directories are examples.
4. Create ConfigMaps from the manifest directories and reference them in the `ClusterInstance` CR using the `extraManifestsRefs` field.

   Example `kustomization.yaml` with `configMapGenerator`:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization

   configMapGenerator:
   - name: extra-manifests-cm
     namespace: helix56-v413
     files:
     - extra-manifest/workload-partitioning.yaml
     - extra-manifest/enable-crun-master.yaml
     - custom-manifest/custom-config.yaml
     # ...

   generatorOptions:
     disableNameSuffixHash: true
   ```

   where:

   `extra-manifest/`
   :   Extra manifest files from the `ztp-site-generate` container.

   `custom-manifest/`
   :   User-provided custom manifest files.
5. Edit the `ClusterInstance` CR to reference the `ConfigMap` CR:

   Example `ClusterInstance` CR:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: helix56-v413
     namespace: helix56-v413
   spec:
     # ...
     extraManifestsRefs:
     - name: extra-manifests-cm
   ```

   The `extra-manifests-cm` value references the `ConfigMap` containing the extra manifests.
6. Edit the top-level `kustomization.yaml` file to control which OpenShift Container Platform versions are active. The following is an example of a `kustomization.yaml` file at the top level:

   ```
   resources:
   - version_4.13
   #- version_4.14
   ```

   where:

   `version_4.13`
   :   Activate version 4.13.

   `#- version_4.14`
   :   Use comments to deactivate a version.

### [2.11. Configuring the hub cluster for backup and restore](#ztp-configuring-the-hub-cluster-for-backup-and-restore_ztp-preparing-the-hub-cluster) Copy linkLink copied to clipboard!

You can use GitOps ZTP to configure a set of policies to back up `BareMetalHost` resources. This allows you to recover data from a failed hub cluster and deploy a replacement cluster using Red Hat Advanced Cluster Management (RHACM).

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a policy to add the `cluster.open-cluster-management.io/backup=cluster-activation` label to all `BareMetalHost` resources that have the `infraenvs.agent-install.openshift.io` label. Save the policy as `BareMetalHostBackupPolicy.yaml`.

   The following example adds the `cluster.open-cluster-management.io/backup` label to all `BareMetalHost` resources that have the `infraenvs.agent-install.openshift.io` label:

   **Example Policy**

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: Policy
   metadata:
     name: bmh-cluster-activation-label
     annotations:
       policy.open-cluster-management.io/description: Policy used to add the cluster.open-cluster-management.io/backup=cluster-activation label to all BareMetalHost resources
   spec:
     disabled: false
     policy-templates:
       - objectDefinition:
           apiVersion: policy.open-cluster-management.io/v1
           kind: ConfigurationPolicy
           metadata:
             name: set-bmh-backup-label
           spec:
             object-templates-raw: |
               {{- /* Set cluster-activation label on all BMH resources */ -}}
               {{- $infra_label := "infraenvs.agent-install.openshift.io" }}
               {{- range $bmh := (lookup "metal3.io/v1alpha1" "BareMetalHost" "" "" $infra_label).items }}
                   - complianceType: musthave
                     objectDefinition:
                       kind: BareMetalHost
                       apiVersion: metal3.io/v1alpha1
                       metadata:
                         name: {{ $bmh.metadata.name }}
                         namespace: {{ $bmh.metadata.namespace }}
                         labels:
                           cluster.open-cluster-management.io/backup: cluster-activation
               {{- end }}
             remediationAction: enforce
             severity: high
   ---
   apiVersion: cluster.open-cluster-management.io/v1beta1
   kind: Placement
   metadata:
     name: bmh-cluster-activation-label-pr
   spec:
     predicates:
       - requiredClusterSelector:
           labelSelector:
             matchExpressions:
               - key: name
                 operator: In
                 values:
                   - local-cluster
   ---
   apiVersion: policy.open-cluster-management.io/v1
   kind: PlacementBinding
   metadata:
     name: bmh-cluster-activation-label-binding
   placementRef:
     name: bmh-cluster-activation-label-pr
     apiGroup: cluster.open-cluster-management.io
     kind: Placement
   subjects:
     - name: bmh-cluster-activation-label
       apiGroup: policy.open-cluster-management.io
       kind: Policy
   ---
   apiVersion: cluster.open-cluster-management.io/v1beta2
   kind: ManagedClusterSetBinding
   metadata:
     name: default
     namespace: default
   spec:
     clusterSet: default
   ```

   If you apply the `cluster.open-cluster-management.io/backup: cluster-activation` label to `BareMetalHost` resources, the RHACM cluster backs up those resources. You can restore the `BareMetalHost` resources if the active cluster becomes unavailable, when restoring the hub activation resources.
2. Apply the policy by running the following command:

   ```
   $ oc apply -f BareMetalHostBackupPolicy.yaml
   ```

**Verification**

1. Find all `BareMetalHost` resources with the label `infraenvs.agent-install.openshift.io` by running the following command:

   ```
   $ oc get BareMetalHost -A -l infraenvs.agent-install.openshift.io
   ```

   **Example output**

   ```
   NAMESPACE      NAME             STATE   CONSUMER   ONLINE   ERROR   AGE
   baremetal-ns   baremetal-name                      false            50s
   ```
2. Verify that the policy has applied the label `cluster.open-cluster-management.io/backup=cluster-activation` to all these resources, by running the following command:

   ```
   $ oc get BareMetalHost -A -l infraenvs.agent-install.openshift.io,cluster.open-cluster-management.io/backup=cluster-activation
   ```

   **Example output**

   ```
   NAMESPACE      NAME             STATE   CONSUMER   ONLINE   ERROR   AGE
   baremetal-ns   baremetal-name                      false            50s
   ```

   The output must show the same list as in the previous step, which listed all `BareMetalHost` resources with the label `infraenvs.agent-install.openshift.io`. This confirms that all the `BareMetalHost` resources with the `infraenvs.agent-install.openshift.io` label also have the `cluster.open-cluster-management.io/backup: cluster-activation` label.

   The following example shows a `BareMetalHost` resource with the `infraenvs.agent-install.openshift.io` label. The resource must also have the `cluster.open-cluster-management.io/backup: cluster-activation` label, which was added by the policy created in step 1.

   ```
   apiVersion: metal3.io/v1alpha1
   kind: BareMetalHost
   metadata:
     labels:
       cluster.open-cluster-management.io/backup: cluster-activation
       infraenvs.agent-install.openshift.io: value
     name: baremetal-name
     namespace: baremetal-ns
   ```

You can now use Red Hat Advanced Cluster Management to restore a managed cluster.

Important

When you restore `BareMetalHost` resources as part of restoring the cluster activation data, you must restore the `BareMetalHost` status. The following RHACM `Restore` resource example restores activation resources, including `BareMetalHost`, and also restores the status for the `BareMetalHost` resources:

```
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Restore
metadata:
  name: restore-acm-bmh
  namespace: open-cluster-management-backup
spec:
  cleanupBeforeRestore: CleanupRestored
  veleroManagedClustersBackupName: latest
  veleroCredentialsBackupName: latest
  veleroResourcesBackupName: latest
  restoreStatus:
    includedResources:
      - BareMetalHosts
```

* Set `veleroManagedClustersBackupName: latest` to restore activation resources.
* Restores the status for `BareMetalHost` resources.

## [Chapter 3. Updating GitOps ZTP](#ztp-updating-gitops) Copy linkLink copied to clipboard!

You can update the GitOps Zero Touch Provisioning (ZTP) infrastructure independently from the hub cluster, Red Hat Advanced Cluster Management (RHACM), and the managed OpenShift Container Platform clusters.

Note

You can update the Red Hat OpenShift GitOps Operator when new versions become available. When updating the GitOps ZTP plugin, review the updated files in the reference configuration and ensure that the changes meet your requirements.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

### [3.1. Overview of the GitOps ZTP update process](#ztp-updating-gitops-ztp_ztp-updating-gitops) Copy linkLink copied to clipboard!

You can update GitOps Zero Touch Provisioning (ZTP) for a fully operational hub cluster running an earlier version of the GitOps ZTP infrastructure. The update process avoids impact on managed clusters.

Note

Any changes to policy settings, including adding recommended content, results in updated policies that must be rolled out to the managed clusters and reconciled.

At a high level, the strategy for updating the GitOps ZTP infrastructure is as follows:

1. Label all existing clusters with the `ztp-done` label.
2. Stop the ArgoCD applications.
3. Install the new GitOps ZTP tools.
4. Update required content and optional changes in the Git repository.
5. Enable pulling the ISO images for the desired OpenShift Container Platform version.
6. Update and restart the application configuration.

### [3.2. Preparing for the upgrade](#ztp-preparing-for-the-gitops-ztp-upgrade_ztp-updating-gitops) Copy linkLink copied to clipboard!

Use the following procedure to prepare your site for the GitOps Zero Touch Provisioning (ZTP) upgrade.

**Procedure**

1. Get the latest version of the GitOps ZTP container that has the custom resources (CRs) used to configure Red Hat OpenShift GitOps for use with GitOps ZTP.
2. Extract the `argocd/deployment` directory by using the following commands:

   ```
   $ mkdir -p ./update
   ```

   ```
   $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./update
   ```

   The `/update` directory contains the following subdirectories:

   * `update/extra-manifest`: contains the source CR files that you package into a `ConfigMap` and reference in the `ClusterInstance` CR using the `extraManifestsRefs` field.
   * `update/source-crs`: contains the source CR files that the `PolicyGenerator` or `PolicyGentemplate` CR uses to generate the Red Hat Advanced Cluster Management (RHACM) policies.
   * `update/argocd/deployment`: contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure.
   * `update/argocd/example`: contains example `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration.
3. Update the `clusters-app.yaml` and `policies-app.yaml` files to reflect the name of your applications and the URL, branch, and path for your Git repository.

   If the upgrade includes changes that results in obsolete policies, the obsolete policies should be removed prior to performing the upgrade.
4. Diff the changes between the configuration and deployment source CRs in the `/update` folder and Git repo where you manage your fleet site CRs. Apply and push the required changes to your site repository.

   Important

   When you update GitOps ZTP to the latest version, you must apply the changes from the `update/argocd/deployment` directory to your site repository. Do not use older versions of the `argocd/deployment/` files.

### [3.3. Labeling the existing clusters](#ztp-labeling-the-existing-clusters_ztp-updating-gitops) Copy linkLink copied to clipboard!

To ensure that existing clusters remain untouched by the tool updates, label all existing managed clusters with the `ztp-done` label.

Note

This procedure only applies when updating clusters that were not provisioned with Topology Aware Lifecycle Manager (TALM). Clusters that you provision with TALM are automatically labeled with `ztp-done`.

**Procedure**

1. Find a label selector that lists the managed clusters that were deployed with GitOps Zero Touch Provisioning (ZTP), such as `local-cluster!=true`:

   ```
   $ oc get managedcluster -l 'local-cluster!=true'
   ```
2. Ensure that the resulting list contains all the managed clusters that were deployed with GitOps ZTP, and then use that selector to add the `ztp-done` label:

   ```
   $ oc label managedcluster -l 'local-cluster!=true' ztp-done=
   ```

### [3.4. Stopping the existing GitOps ZTP applications](#ztp-stopping-the-existing-gitops-ztp-applications_ztp-updating-gitops) Copy linkLink copied to clipboard!

Removing the existing applications ensures that any changes to existing content in the Git repository are not rolled out until the new version of the tools is available.

Use the application files from the `deployment` directory. If you used custom names for the applications, update the names in these files first.

**Procedure**

1. Perform a non-cascaded delete on the `clusters` application to leave all generated resources in place:

   ```
   $ oc delete -f update/argocd/deployment/clusters-app.yaml
   ```
2. Perform a cascaded delete on the `policies` application to remove all previous policies:

   ```
   $ oc patch -f policies-app.yaml -p '{"metadata": {"finalizers": ["resources-finalizer.argocd.argoproj.io"]}}' --type merge
   ```

   ```
   $ oc delete -f update/argocd/deployment/policies-app.yaml
   ```

### [3.5. Required changes to the Git repository](#ztp-required-changes-to-the-git-repository_ztp-updating-gitops) Copy linkLink copied to clipboard!

When upgrading the `ztp-site-generate` container from an earlier release of GitOps Zero Touch Provisioning (ZTP) to 4.10 or later, there are additional requirements for the contents of the Git repository. Existing content in the repository must be updated to reflect these changes.

Note

The following procedure assumes you are using `PolicyGenerator` resources instead of `PolicyGentemplate` resources for cluster policies management.

* Make required changes to `PolicyGenerator` files:

  All `PolicyGenerator` files must be created in a `Namespace` prefixed with `ztp`. This ensures that the GitOps ZTP application is able to manage the policy CRs generated by GitOps ZTP without conflicting with the way Red Hat Advanced Cluster Management (RHACM) manages the policies internally.
* Add the `kustomization.yaml` file to the repository:

  All `ClusterInstance` and `PolicyGenerator` CRs must be included in a `kustomization.yaml` file under their respective directory trees. For example:

  ```
  ├── acmpolicygenerator
  │   ├── site1-ns.yaml
  │   ├── site1.yaml
  │   ├── site2-ns.yaml
  │   ├── site2.yaml
  │   ├── common-ns.yaml
  │   ├── common-ranGen.yaml
  │   ├── group-du-sno-ranGen-ns.yaml
  │   ├── group-du-sno-ranGen.yaml
  │   └── kustomization.yaml
  └── clusterinstance
      ├── site1.yaml
      ├── site2.yaml
      └── kustomization.yaml
  ```

  Note

  The files listed in the `generator` sections must contain either `ClusterInstance` or `{policy-gen-cr}` CRs only. If your existing YAML files contain other CRs, for example, `Namespace`, these other CRs must be pulled out into separate files and listed in the `resources` section.

  The `PolicyGenerator` kustomization file must contain all `PolicyGenerator` YAML files in the `generator` section and `Namespace` CRs in the `resources` section. For example:

  ```
  apiVersion: kustomize.config.k8s.io/v1beta1
  kind: Kustomization

  generators:
  - acm-common-ranGen.yaml
  - acm-group-du-sno-ranGen.yaml
  - site1.yaml
  - site2.yaml

  resources:
  - common-ns.yaml
  - acm-group-du-sno-ranGen-ns.yaml
  - site1-ns.yaml
  - site2-ns.yaml
  ```

  The `ClusterInstance` kustomization file must contain all `ClusterInstance` YAML files in the `generator` section and any other CRs in the resources:

  ```
  apiVersion: kustomize.config.k8s.io/v1beta1
  kind: Kustomization

  generators:
  - site1.yaml
  - site2.yaml
  ```
* Remove the `pre-sync.yaml` and `post-sync.yaml` files.

  In OpenShift Container Platform 4.10 and later, the `pre-sync.yaml` and `post-sync.yaml` files are no longer required. The `update/deployment/kustomization.yaml` CR manages the policies deployment on the hub cluster.

  Note

  There is a set of `pre-sync.yaml` and `post-sync.yaml` files under both the `ClusterInstance` and `{policy-gen-cr}` trees.
* Review and incorporate recommended changes

  Each release may include additional recommended changes to the configuration applied to deployed clusters. Typically these changes result in lower CPU use by the OpenShift platform, additional features, or improved tuning of the platform.

  Review the reference `ClusterInstance` and `PolicyGenerator` CRs applicable to the types of cluster in your network. These examples can be found in the `argocd/example` directory extracted from the GitOps ZTP container.

### [3.6. Installing the new GitOps ZTP applications](#ztp-installing-the-new-gitops-ztp-applications_ztp-updating-gitops) Copy linkLink copied to clipboard!

Using the extracted `argocd/deployment` directory, and after ensuring that the applications point to your site Git repository, apply the full contents of the deployment directory. Applying the full contents of the directory ensures that all necessary resources for the applications are correctly configured.

**Procedure**

1. To install the GitOps ZTP plugin, patch the ArgoCD instance in the hub cluster with the relevant multicluster engine (MCE) subscription image. Customize the patch file that you previously extracted into the `out/argocd/deployment/` directory for your environment.

   1. Select the `multicluster-operators-subscription` image that matches your RHACM version.

      * For RHACM 2.8 and 2.9, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel8:v<rhacm_version>` image.
      * For RHACM 2.10 and later, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v<rhacm_version>` image.

      Important

      The version of the `multicluster-operators-subscription` image must match the RHACM version. Beginning with the MCE 2.10 release, RHEL 9 is the base image for `multicluster-operators-subscription` images.

      Click `[Expand for Operator list]` in the "Platform Aligned Operators" table in [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) to view the complete supported Operators matrix for OpenShift Container Platform.
   2. Modify the `out/argocd/deployment/argocd-openshift-gitops-patch.json` file with the `multicluster-operators-subscription` image that matches your RHACM version:

      ```
      {
        "args": [
          "-c",
          "mkdir -p /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator && cp /policy-generator/PolicyGenerator-not-fips-compliant /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator/PolicyGenerator"
        ],
        "command": [
          "/bin/bash"
        ],
        "image": "registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v2.10",
        "name": "policy-generator-install",
        "imagePullPolicy": "Always",
        "volumeMounts": [
          {
            "mountPath": "/.config",
            "name": "kustomize"
          }
        ]
      }
      ```

      * Optional: For RHEL 9 images, in the `args` field, change the executable path from `/policy-generator/PolicyGenerator-not-fips-compliant` to match the required universal executable for your ArgoCD version.
      * Match the `multicluster-operators-subscription` image to your RHACM version. In disconnected environments, replace the URL with the disconnected registry equivalent for your environment.
   3. Patch the ArgoCD instance. Run the following command:

      ```
      $ oc patch argocd openshift-gitops \
      -n openshift-gitops --type=merge \
      --patch-file out/argocd/deployment/argocd-openshift-gitops-patch.json
      ```
2. In RHACM 2.7 and later, the multicluster engine enables the `cluster-proxy-addon` feature by default. Apply the following patch to disable the `cluster-proxy-addon` feature and remove the relevant hub cluster and managed pods that are responsible for this add-on. Run the following command:

   ```
   $ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type=merge --patch-file out/argocd/deployment/disable-cluster-proxy-addon.json
   ```
3. Apply the pipeline configuration to your hub cluster by running the following command:

   ```
   $ oc apply -k out/argocd/deployment
   ```

### [3.7. Pulling ISO images for the desired OpenShift Container Platform version](#ztp-pulling-ocp-images_ztp-updating-gitops) Copy linkLink copied to clipboard!

To pull ISO images for the desired OpenShift Container Platform version, update the `AgentServiceConfig` custom resource (CR) with references to the desired ISO and RootFS images that are hosted on the mirror registry HTTP server.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have RHACM with `MultiClusterHub` enabled.
* You have enabled the assisted service.

**Procedure**

1. Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command:

   ```
   $ oc edit AgentServiceConfig
   ```
2. Update the `spec.osImages` field in the `AgentServiceConfig` CR:

   ```
   apiVersion: agent-install.openshift.io/v1beta1
   kind: AgentServiceConfig
   metadata:
    name: agent
   spec:
   # ...
     osImages:
       - cpuArchitecture: x86_64
         openshiftVersion: "4.22"
         rootFSUrl: https://<host>/<path>/rhcos-live-rootfs.x86_64.img
         url: https://<host>/<path>/rhcos-live.x86_64.iso
   ```

   where:

   `<host>`
   :   Specifies the fully qualified domain name (FQDN) for the target mirror registry HTTP server.

   `<path>`
   :   Specifies the path to the image on the target mirror registry.
3. Save and quit the editor to apply the changes.

### [3.8. Rolling out the GitOps ZTP configuration changes](#ztp-roll-out-the-configuration-changes_ztp-updating-gitops) Copy linkLink copied to clipboard!

If any configuration changes were included in the upgrade due to implementing recommended changes, the upgrade process results in a set of policy CRs on the hub cluster in the `Non-Compliant` state. With the GitOps Zero Touch Provisioning (ZTP) version 4.10 and later `ztp-site-generate` container, these policies are set to `inform` mode and are not pushed to the managed clusters without an additional step by the user. This ensures that potentially disruptive changes to the clusters can be managed in terms of when the changes are made, for example, during a maintenance window, and how many clusters are updated concurrently.

To roll out the changes, create one or more `ClusterGroupUpgrade` CRs as detailed in the TALM documentation. The CR must contain the list of `Non-Compliant` policies that you want to push out to the managed clusters as well as a list or selector of which clusters should be included in the update.

## [Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources](#ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can provision OpenShift Container Platform clusters at scale with Red Hat Advanced Cluster Management (RHACM) using the assisted service and the GitOps plugin policy generator with core-reduction technology enabled. The GitOps Zero Touch Provisioning (ZTP) pipeline performs the cluster installations. GitOps ZTP can be used in a disconnected environment.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

### [4.1. GitOps ZTP and Topology Aware Lifecycle Manager](#ztp-talo-integration_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

GitOps Zero Touch Provisioning (ZTP) generates installation and configuration CRs from manifests stored in Git. These artifacts are applied to a centralized hub cluster where Red Hat Advanced Cluster Management (RHACM), the assisted service, and the Topology Aware Lifecycle Manager (TALM) use the CRs to install and configure the managed cluster. The configuration phase of the GitOps ZTP pipeline uses the TALM to orchestrate the application of the configuration CRs to the cluster. There are several key integration points between GitOps ZTP and the TALM.

Inform policies
:   By default, GitOps ZTP creates all policies with a remediation action of `inform`. These policies cause RHACM to report on compliance status of clusters relevant to the policies but does not apply the desired configuration. During the GitOps ZTP process, after OpenShift installation, the TALM steps through the created `inform` policies and enforces them on the target managed cluster(s). This applies the configuration to the managed cluster. Outside of the GitOps ZTP phase of the cluster lifecycle, this allows you to change policies without the risk of immediately rolling those changes out to affected managed clusters. You can control the timing and the set of remediated clusters by using TALM.

Automatic creation of ClusterGroupUpgrade CRs
:   To automate the initial configuration of newly deployed clusters, TALM monitors the state of all `ManagedCluster` CRs on the hub cluster. Any `ManagedCluster` CR that does not have a `ztp-done` label applied, including newly created `ManagedCluster` CRs, causes the TALM to automatically create a `ClusterGroupUpgrade` CR with the following characteristics:

    * The `ClusterGroupUpgrade` CR is created and enabled in the `ztp-install` namespace.
    * `ClusterGroupUpgrade` CR has the same name as the `ManagedCluster` CR.
    * The cluster selector includes only the cluster associated with that `ManagedCluster` CR.
    * The set of managed policies includes all policies that RHACM has bound to the cluster at the time the `ClusterGroupUpgrade` is created.
    * Pre-caching is disabled.
    * Timeout set to 4 hours (240 minutes).

    The automatic creation of an enabled `ClusterGroupUpgrade` ensures that initial zero-touch deployment of clusters proceeds without the need for user intervention. Additionally, the automatic creation of a `ClusterGroupUpgrade` CR for any `ManagedCluster` without the `ztp-done` label allows a failed GitOps ZTP installation to be restarted by simply deleting the `ClusterGroupUpgrade` CR for the cluster.

Waves
:   Each policy generated from a `PolicyGenerator` or `PolicyGentemplate` CR includes a `ztp-deploy-wave` annotation. This annotation is based on the same annotation from each CR which is included in that policy. The wave annotation is used to order the policies in the auto-generated `ClusterGroupUpgrade` CR. The wave annotation is not used other than for the auto-generated `ClusterGroupUpgrade` CR.

    Note

    All CRs in the same policy must have the same setting for the `ztp-deploy-wave` annotation. The default value of this annotation for each CR can be overridden in the `PolicyGenerator` or `PolicyGentemplate`. The wave annotation in the source CR is used for determining and setting the policy wave annotation. This annotation is removed from each built CR which is included in the generated policy at runtime.

    The TALM applies the configuration policies in the order specified by the wave annotations. The TALM waits for each policy to be compliant before moving to the next policy. It is important to ensure that the wave annotation for each CR takes into account any prerequisites for those CRs to be applied to the cluster. For example, an Operator must be installed before or concurrently with the configuration for the Operator. Similarly, the `CatalogSource` for an Operator must be installed in a wave before or concurrently with the Operator Subscription. The default wave value for each CR takes these prerequisites into account.

    Note

    Multiple CRs and policies can share the same wave number. Having fewer policies can result in faster deployments and lower CPU usage. It is a best practice to group many CRs into relatively few waves.

    To check the default wave value in each source CR, run the following command against the `out/source-crs` directory that is extracted from the `ztp-site-generate` container image:

    ```
    $ grep -r "ztp-deploy-wave" out/source-crs
    ```

Phase labels
:   The `ClusterGroupUpgrade` CR is automatically created and includes directives to annotate the `ManagedCluster` CR with labels at the start and end of the GitOps ZTP process.

    When GitOps ZTP configuration postinstallation commences, the `ManagedCluster` has the `ztp-running` label applied. When all policies are remediated to the cluster and are fully compliant, these directives cause the TALM to remove the `ztp-running` label and apply the `ztp-done` label.

    For deployments that make use of the `informDuValidator` policy, the `ztp-done` label is applied when the cluster is fully ready for deployment of applications. This includes all reconciliation and resulting effects of the GitOps ZTP applied configuration CRs. The `ztp-done` label affects automatic `ClusterGroupUpgrade` CR creation by TALM. Do not manipulate this label after the initial GitOps ZTP installation of the cluster.

Linked CRs
:   The automatically created `ClusterGroupUpgrade` CR has the owner reference set as the `ManagedCluster` from which it was derived. This reference ensures that deleting the `ManagedCluster` CR causes the instance of the `ClusterGroupUpgrade` to be deleted along with any supporting resources.

### [4.2. Overview of deploying managed clusters with GitOps ZTP](#ztp-ztp-building-blocks_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

Red Hat Advanced Cluster Management (RHACM) uses GitOps Zero Touch Provisioning (ZTP) to deploy single-node OpenShift Container Platform clusters, three-node clusters, and standard clusters. You manage site configuration data as OpenShift Container Platform custom resources (CRs) in a Git repository. GitOps ZTP uses a declarative GitOps approach for a develop once, deploy anywhere model to deploy the managed clusters.

The deployment of the clusters includes:

* Installing the host operating system (RHCOS) on a blank server
* Deploying OpenShift Container Platform
* Creating cluster policies and site subscriptions
* Making the necessary network configurations to the server operating system
* Deploying profile Operators and performing any needed software-related configuration, such as performance profile, PTP, and SR-IOV

Note

To deploy clusters with virtualized control planes running on OpenShift Virtualization VMs instead of physical servers, you can use KubeVirt Redfish to expose VMs as Redfish endpoints. For more information, see "Virtualized control planes".

### [4.3. Overview of the managed site installation process](#ztp-overview-managed-site-installation-process_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

After you apply the managed site custom resources (CRs) on the hub cluster, the following actions happen automatically:

1. A Discovery image ISO file is generated and booted on the target host.
2. When the ISO file successfully boots on the target host it reports the host hardware information to RHACM.
3. After all hosts are discovered, OpenShift Container Platform is installed.
4. When OpenShift Container Platform finishes installing, the hub installs the `klusterlet` service on the target cluster.
5. The requested add-on services are installed on the target cluster.

The Discovery image ISO process is complete when the `Agent` CR for the managed cluster is created on the hub cluster.

Important

The target bare-metal host must meet the networking, firmware. For more information, see "Recommended single-node OpenShift cluster configuration for vDU application workloads".

### [4.4. Creating the managed bare-metal host secrets](#ztp-creating-the-site-secrets_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the GitOps Zero Touch Provisioning (ZTP) pipeline to access the Baseboard Management Controller (BMC) and a secret for the assisted installer service to pull cluster installation images from the registry.

Note

The secrets are referenced from the `ClusterInstance` CR by name. The namespace must match the `ClusterInstance` namespace.

**Procedure**

1. Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators:

   1. Save the following YAML as the file `example-sno-secret.yaml`:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
        name: example-sno-bmc-secret
        namespace: example-sno
      data:
        password: <base64_password>
        username: <base64_username>
      type: Opaque
      ---
      apiVersion: v1
      kind: Secret
      metadata:
        name: pull-secret
        namespace: example-sno
      data:
        .dockerconfigjson: <pull_secret>
      type: kubernetes.io/dockerconfigjson
      ```

      where:

      `namespace`
      :   Must match the namespace configured in the related `ClusterInstance` CR.

      `password`, `username`
      :   Base64-encoded values for `password` and `username`.

      `.dockerconfigjson`
      :   Base64-encoded pull secret.
2. Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.

### [4.5. Configuring Discovery ISO kernel arguments for installations using GitOps ZTP](#setting-managed-bare-metal-host-kernel-arguments_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

The GitOps Zero Touch Provisioning (ZTP) workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements.

For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation.

Note

In OpenShift Container Platform 4.22, you can only add kernel arguments. You can not replace or delete kernel arguments.

**Prerequisites**

* You have installed the OpenShift CLI (oc).
* You have logged in to the hub cluster as a user with cluster-admin privileges.

**Procedure**

1. Create the `InfraEnv` CR and edit the `spec.kernelArguments` specification to configure kernel arguments.

   1. Save the following YAML in an `InfraEnv-example.yaml` file:

      Note

      The `InfraEnv` CR in this example uses template syntax such as `{{ .Cluster.ClusterName }}` that is populated based on values in the `ClusterInstance` CR. The `ClusterInstance` CR automatically populates values for these templates during deployment. Do not edit the templates manually.

      ```
      apiVersion: agent-install.openshift.io/v1beta1
      kind: InfraEnv
      metadata:
        annotations:
          argocd.argoproj.io/sync-wave: "1"
        name: "{{ .Cluster.ClusterName }}"
        namespace: "{{ .Cluster.ClusterName }}"
      spec:
        clusterRef:
          name: "{{ .Cluster.ClusterName }}"
          namespace: "{{ .Cluster.ClusterName }}"
        kernelArguments:
          - operation: append
            value: audit=0
          - operation: append
            value: trace=1
        sshAuthorizedKey: "{{ .Site.SshPublicKey }}"
        proxy: "{{ .Cluster.ProxySettings }}"
        pullSecretRef:
          name: "{{ .Site.PullSecretRef.Name }}"
        ignitionConfigOverride: "{{ .Cluster.IgnitionConfigOverride }}"
        nmStateConfigLabelSelector:
          matchLabels:
            nmstate-label: "{{ .Cluster.ClusterName }}"
        additionalNTPSources: "{{ .Cluster.AdditionalNTPSources }}"
      ```

      * `kernelArguments.operation` specifies the append operation to add a kernel argument.
      * `kernelArguments.value` specifies the kernel argument you want to configure. This example configures the `audit` kernel argument and the `trace` kernel argument.
2. Commit the `InfraEnv-example.yaml` file to your Git repository and push your changes. The following example shows a sample Git repository structure:

   ```
   ~/example-ztp/install
             └── site-install
                  ├── clusterinstance-example.yaml
                  ├── InfraEnv-example.yaml
                  └── kustomization.yaml
   ```
3. Update the `kustomization.yaml` file to use the `configMapGenerator` field to package the `InfraEnv` CR into a `ConfigMap`:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - clusterinstance-example.yaml
   configMapGenerator:
     - name: custom-infraenv-cm
       namespace: example-cluster
       files:
         - InfraEnv-example.yaml
   generatorOptions:
     disableNameSuffixHash: true
   ```

   * `clusterinstance-example.yaml` specifies the name of the `ClusterInstance` CR.
   * `configMapGenerator.name` specifies the name of the `ConfigMap` that contains the custom `InfraEnv` CR.
   * `configMapGenerator.namespace` must match the `ClusterInstance` namespace.
4. In your `ClusterInstance` CR, reference the `ConfigMap` in the `spec.templateRefs` field:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-cluster"
     namespace: "example-cluster"
   spec:
     clusterName: "example-cluster"
     templateRefs:
       - name: custom-infraenv-cm
         namespace: example-cluster
   # ...
   ```

   * `spec.templateRefs` specifies the `ConfigMap` CR that contains the custom `InfraEnv` CR template.
5. Commit the `ClusterInstance` CR and `kustomization.yaml` to your Git repository and push your changes.

   When the Argo CD pipeline syncs the changes, the SiteConfig Operator uses the custom `InfraEnv-example` CR from the generated `ConfigMap` to configure the infrastructure environment, including the custom kernel arguments.

**Verification**

To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file.

1. Begin an SSH session with the target host:

   ```
   $ ssh -i /path/to/privatekey core@<host_name>
   ```
2. View the system’s kernel arguments by using the following command:

   ```
   $ cat /proc/cmdline
   ```

### [4.6. Deploying a managed cluster with ClusterInstance and GitOps ZTP](#ztp-deploying-a-site_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

Use the following procedure to create a `ClusterInstance` custom resource (CR) and related files and initiate the GitOps Zero Touch Provisioning (ZTP) cluster deployment.

Note

You require Red Hat Advanced Cluster Management (RHACM) version 2.12 or later to install the SiteConfig Operator and use the `ClusterInstance` CR.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You installed the SiteConfig Operator in the hub cluster.
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You configured the hub cluster for generating the required installation and policy CRs.
* You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and you must configure it as a source repository for the ArgoCD application. See "Preparing the GitOps ZTP site configuration repository" for more information.

  Note

  When you create the source repository, ensure that you patch the ArgoCD application with the `argocd/deployment/argocd-openshift-gitops-patch.json` patch-file that you extract from the `ztp-site-generate` container. See "Configuring the hub cluster with ArgoCD".
* To be ready for provisioning managed clusters, you require the following for each bare-metal host:

  Network connectivity
  :   Your network requires DNS. Managed cluster hosts should be reachable from the hub cluster. Ensure that Layer 3 connectivity exists between the hub cluster and the managed cluster host.

  Baseboard Management Controller (BMC) details
  :   GitOps ZTP uses BMC username and password details to connect to the BMC during cluster installation. The GitOps ZTP plugin manages the `ManagedCluster` CRs on the hub cluster based on the `ClusterInstance` CR in your site Git repo. You create individual `BMCSecret` CRs for each host manually.

**Procedure**

1. Create the required managed cluster secrets on the hub cluster. These resources must be in a namespace with a name matching the cluster name. For example, in `out/argocd/example/clusterinstance/example-sno.yaml`, the cluster name and namespace is `example-sno`.

   1. Export the cluster namespace by running the following command:

      ```
      $ export CLUSTERNS=example-sno
      ```
   2. Create the namespace:

      ```
      $ oc create namespace $CLUSTERNS
      ```
2. Create pull secret and BMC `Secret` CRs for the managed cluster. The pull secret must contain all the credentials necessary for installing OpenShift Container Platform and all required Operators. See "Creating the managed bare-metal host secrets" for more information.

   Note

   The secrets are referenced from the `ClusterInstance` custom resource (CR) by name. The namespace must match the `ClusterInstance` namespace.
3. Create a `ClusterInstance` CR for your cluster in your local clone of the Git repository:

   1. Choose the appropriate example for your CR from the `out/argocd/example/clusterinstance/` folder. The folder includes example files for single node, three-node, and standard clusters:

      * `example-sno.yaml`
      * `example-3node.yaml`
      * `example-standard.yaml`
   2. Change the cluster and host details in the example file to match the type of cluster you want. For example:

      **Example single-node OpenShift ClusterInstance CR**

      ```
      # example-node1-bmh-secret & assisted-deployment-pull-secret need to be created under same namespace example-ai-sno
      ---
      apiVersion: siteconfig.open-cluster-management.io/v1alpha1
      kind: ClusterInstance
      metadata:
        name: "example-ai-sno"
        namespace: "example-ai-sno"
      spec:
        baseDomain: "example.com"
        pullSecretRef:
          name: "assisted-deployment-pull-secret"
        clusterImageSetNameRef: "openshift-4.22"
        sshPublicKey: "ssh-rsa AAAA..."
        clusterName: "example-ai-sno"
        networkType: "OVNKubernetes"
        # installConfigOverrides is a generic way of passing install-config
        # parameters through the siteConfig.  The 'capabilities' field configures
        # the composable openshift feature.  In this 'capabilities' setting, we
        # remove all the optional set of components.
        # Notes:
        # - OperatorLifecycleManager is needed for 4.15 and later
        # - NodeTuning is needed for 4.13 and later, not for 4.12 and earlier
        # - Ingress is needed for 4.16 and later
        installConfigOverrides: |
          {
            "capabilities": {
              "baselineCapabilitySet": "None",
              "additionalEnabledCapabilities": [
                "NodeTuning",
                "OperatorLifecycleManager",
                "Ingress"
              ]
            }
          }
        # Include references to extraManifest ConfigMaps.
        extraManifestsRefs:
          - name: sno-extra-manifest-configmap
        extraLabels:
          ManagedCluster:
            # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples
            du-profile: "latest"
            # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples in ../policygentemplates:
            # ../policygentemplates/common-ranGen.yaml will apply to all clusters with 'common: true'
            common: "true"
            # ../policygentemplates/group-du-sno-ranGen.yaml will apply to all clusters with 'group-du-sno: ""'
            group-du-sno: ""
            # ../policygentemplates/example-sno-site.yaml will apply to all clusters with 'sites: "example-sno"'
            # Normally this should match or contain the cluster name so it only applies to a single cluster
            sites : "example-sno"
        clusterNetwork:
          - cidr: 1001:1::/48
            hostPrefix: 64
        machineNetwork:
          - cidr: 1111:2222:3333:4444::/64
        serviceNetwork:
          - cidr: 1001:2::/112
        additionalNTPSources:
          - 1111:2222:3333:4444::2
        # Initiates the cluster for workload partitioning. Setting specific reserved/isolated CPUSets is done via PolicyTemplate
        # please see Workload Partitioning Feature for a complete guide.
        cpuPartitioningMode: AllNodes
        templateRefs:
          - name: ai-cluster-templates-v1
            namespace: open-cluster-management
        nodes:
          - hostName: "example-node1.example.com"
            role: "master"
            bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
            bmcCredentialsName:
              name: "example-node1-bmh-secret"
            bootMACAddress: "AA:BB:CC:DD:EE:11"
            # Use UEFISecureBoot to enable secure boot, UEFI to disable.
            bootMode: "UEFISecureBoot"
            rootDeviceHints:
              deviceName: "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0"
            # disk partition at `/var/lib/containers` with ignitionConfigOverride. Some values must be updated. See DiskPartitionContainer.md in argocd folder for more details
            ignitionConfigOverride: |
              {
                "ignition": {
                  "version": "3.2.0"
                },
                "storage": {
                  "disks": [
                    {
                      "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                      "partitions": [
                        {
                          "label": "var-lib-containers",
                          "sizeMiB": 0,
                          "startMiB": 250000
                        }
                      ],
                      "wipeTable": false
                    }
                  ],
                  "filesystems": [
                    {
                      "device": "/dev/disk/by-partlabel/var-lib-containers",
                      "format": "xfs",
                      "mountOptions": [
                        "defaults",
                        "prjquota"
                      ],
                      "path": "/var/lib/containers",
                      "wipeFilesystem": true
                    }
                  ]
                },
                "systemd": {
                  "units": [
                    {
                      "contents": "# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                      "enabled": true,
                      "name": "var-lib-containers.mount"
                    }
                  ]
                }
              }
            nodeNetwork:
              interfaces:
                - name: eno1
                  macAddress: "AA:BB:CC:DD:EE:11"
              config:
                interfaces:
                  - name: eno1
                    type: ethernet
                    state: up
                    ipv4:
                      enabled: false
                    ipv6:
                      enabled: true
                      address:
                      # For SNO sites with static IP addresses, the node-specific,
                      # API and Ingress IPs should all be the same and configured on
                      # the interface
                      - ip: 1111:2222:3333:4444::aaaa:1
                        prefix-length: 64
                dns-resolver:
                  config:
                    search:
                    - example.com
                    server:
                    - 1111:2222:3333:4444::2
                routes:
                  config:
                  - destination: ::/0
                    next-hop-interface: eno1
                    next-hop-address: 1111:2222:3333:4444::1
                    table-id: 254
            templateRefs:
              - name: ai-node-templates-v1
                namespace: open-cluster-management
      ```

      Note

      For more information about BMC addressing, see the "Additional resources" section. The `installConfigOverrides` and `ignitionConfigOverride` fields are expanded in the example for ease of readability.

      Note

      To override the default `BareMetalHost` CR for a node, create a custom node template in a `ConfigMap` and reference it in the node-level `spec.nodes.templateRefs` field in the `ClusterInstance` CR. Ensure that you set the `argocd.argoproj.io/sync-wave: "3"` annotation in your override `BareMetalHost` CR.
   3. You can inspect the default set of extra-manifest `MachineConfig` CRs in `out/argocd/extra-manifest`. It is automatically applied to the cluster when it is installed.
   4. Optional: To provision additional install-time manifests on the provisioned cluster, package your extra manifest CRs in a `ConfigMap` and reference it in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the GitOps ZTP pipeline".

      Important

      For optimal cluster performance, enable crun for master and worker nodes in single-node OpenShift, single-node OpenShift with additional worker nodes, three-node OpenShift, and standard clusters.

      Enable crun in a `ContainerRuntimeConfig` CR as an additional Day 0 install-time manifest to avoid the cluster having to reboot.

      The `enable-crun-master.yaml` and `enable-crun-worker.yaml` CR files are in the `out/source-crs/optional-extra-manifest/` folder that you can extract from the `ztp-site-generate` container.
4. Add the `ClusterInstance` CR to the `kustomization.yaml` file in the `generators` section, similar to the example shown in `out/argocd/example/clusterinstance/kustomization.yaml`.
5. Commit the `ClusterInstance` CR and associated `kustomization.yaml` changes in your Git repository and push the changes.

   The ArgoCD pipeline detects the changes and begins the managed cluster deployment.

**Verification**

* Verify that the custom roles and labels are applied after the node is deployed:

  ```
  $ oc describe node example-node.example.com
  ```

  The following example output shows the custom roles and labels:

  ```
  Name:   example-node.example.com
  Roles:  control-plane,example-label,master,worker
  Labels: beta.kubernetes.io/arch=amd64
          beta.kubernetes.io/os=linux
          custom-label/parameter1=true
          kubernetes.io/arch=amd64
          kubernetes.io/hostname=cnfdf03.telco5gran.eng.rdu2.redhat.com
          kubernetes.io/os=linux
          node-role.kubernetes.io/control-plane=
          node-role.kubernetes.io/example-label=
          node-role.kubernetes.io/master=
          node-role.kubernetes.io/worker=
          node.openshift.io/os_id=rhcos
  ```

  + `node-role.kubernetes.io/example-label=` shows the custom label applied to the node.

#### [4.6.1. Configuring IPsec encryption for single-node OpenShift clusters using GitOps ZTP and ClusterInstance resources](#ztp-configuring-ipsec-using-ztp-and-siteconfig_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can enable IPsec encryption in managed single-node OpenShift clusters that you install using GitOps ZTP and Red Hat Advanced Cluster Management (RHACM). You can encrypt traffic between the managed cluster and IPsec endpoints external to the managed cluster. All network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in Transport mode.

Important

You can also configure IPsec encryption for single-node OpenShift clusters with an additional worker node by following this procedure. It is recommended to use the `MachineConfig` custom resource (CR) to configure IPsec encryption for single-node OpenShift clusters and single-node OpenShift clusters with an additional worker node because of their low resource availability.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have installed the SiteConfig Operator in the hub cluster.
* You have configured RHACM and the hub cluster for generating the required installation and policy custom resources (CRs) for managed clusters.
* You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.
* You have installed the `butane` utility version 0.20.0 or later.
* You have a PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format.

**Procedure**

1. Extract the latest version of the `ztp-site-generate` container source and merge it with your repository where you manage your custom site configuration data.
2. Configure `optional-extra-manifest/ipsec/ipsec-endpoint-config.yaml` with the required values that configure IPsec in the cluster. For example:

   ```
   interfaces:
   - name: hosta_conn
     type: ipsec
     libreswan:
       left: '%defaultroute'
       leftid: '%fromcert'
       leftmodecfgclient: false
       leftcert: left_server
       leftrsasigkey: '%cert'
       right: <external_host>
       rightid: '%fromcert'
       rightrsasigkey: '%cert'
       rightsubnet: <external_address>
       ikev2: insist
       type: tunnel
   ```

   * `leftcert` must match the name of the certificate used on the remote system.
   * `right` is the external host IP address or DNS hostname.
   * `rightsubnet` is the IP subnet of the external host on the other side of the IPsec tunnel.
   * `ikev2: insist` uses the IKEv2 VPN encryption protocol only. Do not use IKEv1, which is deprecated.
3. Add the following certificates to the `optional-extra-manifest/ipsec` folder:

   * `left_server.p12`: The certificate bundle for the IPsec endpoints
   * `ca.pem`: The certificate authority that you signed your certificates with

     The certificate files are required for the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in later steps.
4. Open a shell prompt at the `optional-extra-manifest/ipsec` folder of the Git repository where you maintain your custom site configuration data.
5. Run the `optional-extra-manifest/ipsec/build.sh` script to generate the required Butane and `MachineConfig` CRs files.

   If the PKCS#12 certificate is protected with a password, set the `-W` argument.

   The following example shows the generated output directory structure:

   ```
   out
    └── argocd
         └── example
              └── optional-extra-manifest
                   └── ipsec
                        ├── 99-ipsec-master-endpoint-config.bu
                        ├── 99-ipsec-master-endpoint-config.yaml
                        ├── 99-ipsec-worker-endpoint-config.bu
                        ├── 99-ipsec-worker-endpoint-config.yaml
                        ├── build.sh
                        ├── ca.pem
                        ├── left_server.p12
                        ├── enable-ipsec.yaml
                        ├── ipsec-endpoint-config.yml
                        └── README.md
   ```

   * The `ipsec/build.sh` script generates the Butane and endpoint configuration CRs.
   * Add the `ca.pem` and `left_server.p12` certificate files that are relevant to your network.
6. Create an `ipsec-manifests/` folder in the repository where you manage your custom site configuration data. Add the `enable-ipsec.yaml` and `99-ipsec-*` YAML files to the directory. For example:

   ```
   site-configs/
     ├── hub-1/
     │   └── clusterinstance-site1-sno-du.yaml
     ├── ipsec-manifests/
     │   ├── enable-ipsec.yaml
     │   ├── 99-ipsec-worker-endpoint-config.yaml
     │   └── 99-ipsec-master-endpoint-config.yaml
     └── kustomization.yaml
   ```
7. Create a `kustomization.yaml` file that uses `configMapGenerator` to package your IPsec manifests into a `ConfigMap`:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - hub-1/clusterinstance-site1-sno-du.yaml
   configMapGenerator:
     - name: ipsec-manifests-cm
       namespace: site1-sno-du
       files:
         - ipsec-manifests/enable-ipsec.yaml
         - ipsec-manifests/99-ipsec-master-endpoint-config.yaml
         - ipsec-manifests/99-ipsec-worker-endpoint-config.yaml
   generatorOptions:
     disableNameSuffixHash: true
   ```

   * `namespace` must match the `ClusterInstance` namespace.
   * `disableNameSuffixHash: true` disables the hash suffix so the `ConfigMap` name is predictable.
8. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     clusterName: "site1-sno-du"
     networkType: "OVNKubernetes"
     extraManifestsRefs:
       - name: ipsec-manifests-cm
   # ...
   ```

   * `extraManifestsRefs.name` references the `ConfigMap` containing the IPsec manifests.

   Note

   If you have other extra manifests, you can either include them in the same `ConfigMap` or create multiple `ConfigMap` resources and reference each of those in the `extraManifestsRefs` field.
9. Commit the `ClusterInstance` CR, IPsec manifest files, and `kustomization.yaml` changes in your Git repository and push the changes to provision the managed cluster and configure IPsec encryption.

   The Argo CD pipeline detects the changes and begins the managed cluster deployment.

   During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests.

**Verification**

For information about verifying the IPsec encryption, see "Verifying the IPsec encryption".

#### [4.6.2. Configuring IPsec encryption for multi-node clusters using GitOps ZTP and ClusterInstance resources](#ztp-configuring-ipsec-using-ztp-and-siteconfig-for-mno_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can enable IPsec encryption in managed multi-node clusters that you install using GitOps ZTP and Red Hat Advanced Cluster Management (RHACM). You can encrypt traffic between the managed cluster and IPsec endpoints external to the managed cluster. All network traffic between nodes on the OVN-Kubernetes cluster network is encrypted with IPsec in Transport mode.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have installed the SiteConfig Operator in the hub cluster.
* You have configured RHACM and the hub cluster for generating the required installation and policy custom resources (CRs) for managed clusters.
* You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.
* You have installed the `butane` utility version 0.20.0 or later.
* You have a PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format.
* You have installed the NMState Operator.

**Procedure**

1. Extract the latest version of the `ztp-site-generate` container source and merge it with your repository where you manage your custom site configuration data.
2. Configure the `optional-extra-manifest/ipsec/ipsec-config-policy.yaml` file with the required values that configure IPsec in the cluster.

   **`ConfigurationPolicy` object for creating an IPsec configuration**

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: ConfigurationPolicy
   metadata:
     name: policy-config
   spec:
     namespaceSelector:
       include: ["default"]
       exclude: []
       matchExpressions: []
       matchLabels: {}
     remediationAction: inform
     severity: low
     evaluationInterval:
       compliant:
       noncompliant:
     object-templates-raw: |
       {{- range (lookup "v1" "Node" "" "").items }}
       - complianceType: musthave
         objectDefinition:
           kind: NodeNetworkConfigurationPolicy
           apiVersion: nmstate.io/v1
           metadata:
             name: {{ .metadata.name }}-ipsec-policy
           spec:
             nodeSelector:
               kubernetes.io/hostname: {{ .metadata.name }}
             desiredState:
               interfaces:
               - name: hosta_conn
                 type: ipsec
                 libreswan:
                   left: '%defaultroute'
                   leftid: '%fromcert'
                   leftmodecfgclient: false
                   leftcert: left_server
                   leftrsasigkey: '%cert'
                   right: <external_host>
                   rightid: '%fromcert'
                   rightrsasigkey: '%cert'
                   rightsubnet: <external_address>
                   ikev2: insist
                   type: tunnel
   ```

   * `leftcert` must match the name of the certificate used on the remote system.
   * `right` is the external host IP address or DNS hostname.
   * `rightsubnet` is the IP subnet of the external host on the other side of the IPsec tunnel.
   * `ikev2: insist` uses the IKEv2 VPN encryption protocol only. Do not use IKEv1, which is deprecated.
3. Add the following certificates to the `optional-extra-manifest/ipsec` folder:

   * `left_server.p12`: The certificate bundle for the IPsec endpoints
   * `ca.pem`: The certificate authority that you signed your certificates with

     The certificate files are required for the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in later steps.
4. Open a shell prompt at the `optional-extra-manifest/ipsec` folder of the Git repository where you maintain your custom site configuration data.
5. Run the `optional-extra-manifest/ipsec/import-certs.sh` script to generate the required Butane and `MachineConfig` CRs to import the external certs.

   If the PKCS#12 certificate is protected with a password, set the `-W` argument.

   The following example shows the generated output directory structure:

   ```
   out
    └── argocd
         └── example
              └── optional-extra-manifest
                   └── ipsec
                        ├── 99-ipsec-master-import-certs.bu
                        ├── 99-ipsec-master-import-certs.yaml
                        ├── 99-ipsec-worker-import-certs.bu
                        ├── 99-ipsec-worker-import-certs.yaml
                        ├── import-certs.sh
                        ├── ca.pem
                        ├── left_server.p12
                        ├── enable-ipsec.yaml
                        ├── ipsec-config-policy.yaml
                        └── README.md
   ```

   * The `ipsec/import-certs.sh` script generates the Butane and endpoint configuration CRs.
   * Add the `ca.pem` and `left_server.p12` certificate files that are relevant to your network.
6. Create an `ipsec-manifests/` folder in the repository where you manage your custom site configuration data and add the `enable-ipsec.yaml` and `99-ipsec-*` YAML files to the directory.

   **Example site configuration directory**

   ```
   site-configs/
     ├── hub-1/
     │   └── clusterinstance-site1-mno-du.yaml
     ├── ipsec-manifests/
     │   ├── enable-ipsec.yaml
     │   ├── 99-ipsec-master-import-certs.yaml
     │   └── 99-ipsec-worker-import-certs.yaml
     └── kustomization.yaml
   ```
7. Create a `kustomization.yaml` file that uses `configMapGenerator` to package your IPsec manifests into a `ConfigMap`:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - hub-1/clusterinstance-site1-mno-du.yaml
   configMapGenerator:
     - name: ipsec-manifests-cm
       namespace: site1-mno-du
       files:
         - ipsec-manifests/enable-ipsec.yaml
         - ipsec-manifests/99-ipsec-master-import-certs.yaml
         - ipsec-manifests/99-ipsec-worker-import-certs.yaml
   generatorOptions:
     disableNameSuffixHash: true
   ```

   * `namespace` must match the `ClusterInstance` namespace.
   * `disableNameSuffixHash: true` disables the hash suffix so the `ConfigMap` name is predictable.
8. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-mno-du"
     namespace: "site1-mno-du"
   spec:
     clusterName: "site1-mno-du"
     networkType: "OVNKubernetes"
     extraManifestsRefs:
       - name: ipsec-manifests-cm
   # ...
   ```

   * `extraManifestsRefs.name` references the `ConfigMap` containing the IPsec certificate import manifests.

   Note

   If you have other extra manifests, you can either include them in the same `ConfigMap` or create multiple `ConfigMap` resources and reference them all in `extraManifestsRefs`.
9. Include the `ipsec-config-policy.yaml` config policy file in the `source-crs` directory in GitOps and reference the file in one of the `PolicyGenerator` CRs.
10. Commit the `ClusterInstance` CR, IPsec manifest files, and `kustomization.yaml` changes in your Git repository and push the changes to provision the managed cluster and configure IPsec encryption.

    The Argo CD pipeline detects the changes and begins the managed cluster deployment.

    During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests. The IPsec configuration policy is applied as a Day 2 operation after the cluster is provisioned.

**Verification**

For information about verifying the IPsec encryption, see "Verifying the IPsec encryption".

#### [4.6.3. Verifying the IPsec encryption](#ztp-verifying-ipsec_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can verify that the IPsec encryption is successfully applied in a managed OpenShift Container Platform cluster.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have configured the IPsec encryption.

**Procedure**

1. Start a debug pod for the managed cluster by running the following command:

   ```
   $ oc debug node/<node_name>
   ```
2. Check that the IPsec policy is applied in the cluster node by running the following command:

   ```
   sh-5.1# ip xfrm policy
   ```

   The following example output shows the IPsec policy applied to the cluster node:

   ```
   src 172.16.123.0/24 dst 10.1.232.10/32
     dir out priority 1757377 ptype main
     tmpl src 10.1.28.190 dst 10.1.232.10
       proto esp reqid 16393 mode tunnel
   src 10.1.232.10/32 dst 172.16.123.0/24
     dir fwd priority 1757377 ptype main
     tmpl src 10.1.232.10 dst 10.1.28.190
       proto esp reqid 16393 mode tunnel
   src 10.1.232.10/32 dst 172.16.123.0/24
     dir in priority 1757377 ptype main
     tmpl src 10.1.232.10 dst 10.1.28.190
       proto esp reqid 16393 mode tunnel
   ```
3. Check that the IPsec tunnel is up and connected by running the following command:

   ```
   sh-5.1# ip xfrm state
   ```

   The following example output shows the IPsec tunnel is up and connected:

   ```
   src 10.1.232.10 dst 10.1.28.190
     proto esp spi 0xa62a05aa reqid 16393 mode tunnel
     replay-window 0 flag af-unspec esn
     auth-trunc hmac(sha1) 0x8c59f680c8ea1e667b665d8424e2ab749cec12dc 96
     enc cbc(aes) 0x2818a489fe84929c8ab72907e9ce2f0eac6f16f2258bd22240f4087e0326badb
     anti-replay esn context:
      seq-hi 0x0, seq 0x0, oseq-hi 0x0, oseq 0x0
      replay_window 128, bitmap-length 4
      00000000 00000000 00000000 00000000
   src 10.1.28.190 dst 10.1.232.10
     proto esp spi 0x8e96e9f9 reqid 16393 mode tunnel
     replay-window 0 flag af-unspec esn
     auth-trunc hmac(sha1) 0xd960ddc0a6baaccb343396a51295e08cfd8aaddd 96
     enc cbc(aes) 0x0273c02e05b4216d5e652de3fc9b3528fea94648bc2b88fa01139fdf0beb27ab
     anti-replay esn context:
      seq-hi 0x0, seq 0x0, oseq-hi 0x0, oseq 0x0
      replay_window 128, bitmap-length 4
      00000000 00000000 00000000 00000000
   ```
4. Ping a known IP in the external host subnet by running the following command: For example, ping an IP address in the `rightsubnet` range that you set in the `ipsec/ipsec-endpoint-config.yaml` file:

   ```
   sh-5.1# ping 172.16.110.8
   ```

   The following example output shows a successful ping response:

   ```
   PING 172.16.110.8 (172.16.110.8) 56(84) bytes of data.
   64 bytes from 172.16.110.8: icmp_seq=1 ttl=64 time=153 ms
   64 bytes from 172.16.110.8: icmp_seq=2 ttl=64 time=155 ms
   ```

#### [4.6.4. ClusterInstance CR installation reference](#ztp-clusterinstance-config-reference_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

For a detailed API reference for the `ClusterInstance` custom resource, see [ClusterInstance API](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/apis/index#clusterinstance-api) in the Red Hat Advanced Cluster Management (RHACM) documentation.

### [4.7. Managing host firmware settings with GitOps ZTP](#ztp-configuring-host-firmware-with-gitops-ztp_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

Hosts require the correct firmware configuration to ensure high performance and optimal efficiency. You can deploy custom host firmware configurations for managed clusters with GitOps ZTP.

Tune hosts with specific hardware profiles in your lab and ensure they are optimized for your requirements. When you have completed host tuning to your satisfaction, you extract the host profile and save it in your GitOps ZTP repository. Then, you use the host profile to configure firmware settings in the managed cluster hosts that you deploy with GitOps ZTP.

You specify the required hardware profiles by creating `HostFirmwareSettings` CRs, packaging them in `ConfigMap` resources, and referencing them in the `templateRefs` field of your `ClusterInstance` CR. The SiteConfig Operator generates the required `HostFirmwareSettings` and `BareMetalHost` CRs that are applied to the hub cluster.

Use the following best practices to manage your host firmware profiles.

Identify critical firmware settings with hardware vendors
:   Work with hardware vendors to identify and document critical host firmware settings required for optimal performance and compatibility with the deployed host platform.

Use common firmware configurations across similar hardware platforms
:   Where possible, use a standardized host firmware configuration across similar hardware platforms to reduce complexity and potential errors during deployment.

Test firmware configurations in a lab environment
:   Test host firmware configurations in a controlled lab environment before deploying in production to ensure that settings are compatible with hardware, firmware, and software.

Manage firmware profiles in source control
:   Manage host firmware profiles in Git repositories to track changes, ensure consistency, and facilitate collaboration with vendors.

#### [4.7.1. Retrieving the host firmware schema for a managed cluster](#ztp-retrieving-the-host-firmware-schema_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can discover the host firmware schema for managed clusters. The host firmware schema for bare-metal hosts is populated with information that the Ironic API returns. The API returns information about host firmware interfaces, including firmware setting types, allowable values, ranges, and flags.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have installed Red Hat Advanced Cluster Management (RHACM) and logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have provisioned a cluster that is managed by RHACM.

**Procedure**

* Discover the host firmware schema for the managed cluster. Run the following command:

  ```
  $ oc get firmwareschema -n <managed_cluster_namespace> -o yaml
  ```

  The following example output shows the host firmware schema:

  ```
  apiVersion: v1
  items:
  - apiVersion: metal3.io/v1alpha1
    kind: FirmwareSchema
    metadata:
      creationTimestamp: "2024-09-11T10:29:43Z"
      generation: 1
      name: schema-40562318
      namespace: compute-1
      ownerReferences:
      - apiVersion: metal3.io/v1alpha1
        kind: HostFirmwareSettings
        name: compute-1.example.com
        uid: 65d0e89b-1cd8-4317-966d-2fbbbe033fe9
      resourceVersion: "280057624"
      uid: 511ad25d-f1c9-457b-9a96-776605c7b887
    spec:
      schema:
        AccessControlService:
          allowable_values:
          - Enabled
          - Disabled
          attribute_type: Enumeration
          read_only: false
        # ...
  ```

#### [4.7.2. Retrieving the host firmware settings for a managed cluster](#ztp-retrieving-the-host-firmware-settings_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can retrieve the host firmware settings for managed clusters. This is useful when you have deployed changes to the host firmware and you want to monitor the changes and ensure that they are applied successfully.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have installed Red Hat Advanced Cluster Management (RHACM) and logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have provisioned a cluster that is managed by RHACM.

**Procedure**

1. Retrieve the host firmware settings for the managed cluster. Run the following command:

   ```
   $ oc get hostfirmwaresettings -n <cluster_namespace> <node_name> -o yaml
   ```

   The following example output shows the host firmware settings:

   ```
   apiVersion: v1
   items:
   - apiVersion: metal3.io/v1alpha1
     kind: HostFirmwareSettings
     metadata:
       creationTimestamp: "2024-09-11T10:29:43Z"
       generation: 1
       name: compute-1.example.com
       namespace: kni-qe-24
       ownerReferences:
       - apiVersion: metal3.io/v1alpha1
         blockOwnerDeletion: true
         controller: true
         kind: BareMetalHost
         name: compute-1.example.com
         uid: 0baddbb7-bb34-4224-8427-3d01d91c9287
       resourceVersion: "280057626"
       uid: 65d0e89b-1cd8-4317-966d-2fbbbe033fe9
     spec:
       settings: {}
     status:
       conditions:
       - lastTransitionTime: "2024-09-11T10:29:43Z"
         message: ""
         observedGeneration: 1
         reason: Success
         # Indicates that a change in the host firmware settings has been detected.
         status: "True"
         type: ChangeDetected
       - lastTransitionTime: "2024-09-11T10:29:43Z"
         message: Invalid BIOS setting
         observedGeneration: 1
         reason: ConfigurationError
         # Indicates that the host has an invalid firmware setting.
         status: "False"
         type: Valid
       lastUpdated: "2024-09-11T10:29:43Z"
       schema:
         name: schema-40562318
         namespace: compute-1
       # Contains the complete list of configured host firmware settings returned under the `status.settings` field.
       settings:
         AccessControlService: Enabled
         AcpiHpet: Enabled
         AcpiRootBridgePxm: Enabled
         # ...
   ```
2. Optional: Check the status of the `HostFirmwareSettings` (`hfs`) custom resource in the cluster:

   ```
   $ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="ChangeDetected")].status}'
   ```

   The following example output shows a detected change:

   ```
   True
   ```
3. Optional: Check for invalid firmware settings in the cluster host by running the following command:

   ```
   $ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
   ```

   The following example output shows an invalid firmware setting:

   ```
   False
   ```

#### [4.7.3. Deploying user-defined firmware to cluster hosts with GitOps ZTP](#ztp-deploying-user-defined-firmware-configuration-with-gitops-ztp_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can deploy user-defined firmware settings to cluster hosts by creating custom node templates that include `HostFirmwareSettings` CRs, and referencing them in the `ClusterInstance` CR. You can configure hardware profiles to apply to hosts in the following scenarios:

* All hosts in the cluster
* Individual hosts in the cluster

Important

You can configure host hardware profiles to be applied in a hierarchy. Node-level profiles override cluster-wide settings.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have installed Red Hat Advanced Cluster Management (RHACM) version 2.12 or later and logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have installed the SiteConfig Operator in the hub cluster.
* You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

**Procedure**

1. Create the `HostFirmwareSettings` CR that contains the firmware settings you want to apply. For example, create the following YAML file:

   **host-firmware-settings.yaml**

   ```
   apiVersion: metal3.io/v1alpha1
   kind: HostFirmwareSettings
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     settings:
       BootMode: "Uefi"
       LogicalProc: "Enabled"
       ProcVirtualization: "Enabled"
   ```
2. Save the `HostFirmwareSettings` CR file relative to the `kustomization.yaml` file that you use to provision the cluster. For example:

   ```
   site-configs/
     └── site1-sno-du/
           ├── clusterinstance-site1-sno-du.yaml
           ├── kustomization.yaml
           └── host-firmware-settings.yaml
   ```
3. Create a `ConfigMap` to store the `HostFirmwareSettings` CR. You can use a `kustomization.yaml` file with `configMapGenerator` to create the `ConfigMap`. For example:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - clusterinstance-site1-sno-du.yaml
   configMapGenerator:
     - name: host-firmware-settings-cm
       namespace: site1-sno-du
       files:
         - host-firmware-settings.yaml
   generatorOptions:
     disableNameSuffixHash: true
   ```

   * `namespace` must match the `ClusterInstance` namespace.
   * `host-firmware-settings.yaml` is the name of the `HostFirmwareSettings` CR.
4. To apply a hardware profile to all hosts in the cluster, reference the `ConfigMap` in the `spec.templateRefs` field of your `ClusterInstance` CR. For example:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     clusterName: "site1-sno-du"
     # ...
     templateRefs:
       - name: host-firmware-settings-cm
         namespace: site1-sno-du
     nodes:
       - hostName: "node1.example.com"
         # ...
   ```

   * `templateRefs` applies the firmware profile to all hosts in the cluster.
5. Optional: To apply a hardware profile to a specific host in the cluster, reference the `ConfigMap` in the `spec.nodes[].templateRefs` field. For example:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     clusterName: "site1-sno-du"
     # ...
     nodes:
       - hostName: "node1.example.com"
         # ...
         templateRefs:
           - name: host-firmware-node1-cm
             namespace: site1-sno-du
       - hostName: "node2.example.com"
         # ...
   ```

   * `nodes[].templateRefs` applies the firmware profile only to the `node1.example.com` host.

     Note

     Node-level `templateRefs` settings override cluster-level `templateRefs` settings.
6. Commit the `ClusterInstance` CR, `ConfigMap`, and associated `kustomization.yaml` changes in your Git repository and push the changes.

   The Argo CD pipeline detects the changes and begins the managed cluster deployment.

   Note

   Cluster deployment proceeds even if an invalid firmware setting is detected. To apply a correction using GitOps ZTP, re-deploy the cluster with the corrected hardware profile.

**Verification**

* Check that the firmware settings have been applied in the managed cluster host. For example, run the following command:

  ```
  $ oc get hfs -n <managed_cluster_namespace> <managed_cluster_name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
  ```
* `<managed_cluster_namespace>` is the namespace of the managed cluster and `<managed_cluster_name>` is the name of the managed cluster.

  The following example output shows valid firmware settings:

  ```
  True
  ```

### [4.8. Monitoring managed cluster installation progress](#ztp-monitoring-deployment-progress_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

The Argo CD pipeline syncs the `ClusterInstance` CR from the Git repository to the hub cluster. The SiteConfig Operator then processes the `ClusterInstance` CR and generates the required cluster configuration CRs. You can monitor the progress of the cluster installation from the RHACM dashboard or from the command line.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Monitor the progress of cluster installation by running the following commands:

   1. Export the cluster name:

      ```
      $ export CLUSTER=<clusterName>
      ```
   2. Query the `AgentClusterInstall` CR for the managed cluster:

      ```
      $ oc get agentclusterinstall -n $CLUSTER $CLUSTER -o jsonpath='{.status.conditions[?(@.type=="Completed")]}' | jq
      ```
   3. Get the installation events for the cluster:

      ```
      $ curl -sk $(oc get agentclusterinstall -n $CLUSTER $CLUSTER -o jsonpath='{.status.debugInfo.eventsURL}')  | jq '.[-2,-1]'
      ```

### [4.9. Troubleshooting GitOps ZTP by validating the installation CRs](#ztp-troubleshooting-ztp-gitops-installation-crs_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

The ArgoCD pipeline uses the `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` custom resources (CRs) to generate the cluster configuration CRs and Red Hat Advanced Cluster Management (RHACM) policies. Use the following steps to troubleshoot issues that might occur during this process.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Check that the installation CRs were created by using the following command:

   ```
   $ oc get AgentClusterInstall -n <cluster_name>
   ```

   If no object is returned, use the following steps to troubleshoot the ArgoCD pipeline flow from `ClusterInstance` files to the installation CRs.
2. Verify that the `ManagedCluster` CR was generated using the `ClusterInstance` CR on the hub cluster:

   ```
   $ oc get managedcluster
   ```
3. If the `ManagedCluster` is missing, check if the `clusters` application failed to synchronize the files from the Git repository to the hub cluster:

   ```
   $ oc get applications.argoproj.io -n openshift-gitops clusters -o yaml
   ```

### [4.10. Troubleshooting GitOps ZTP virtual media booting on SuperMicro servers](#ztp-troubleshooting-ztp-gitops-supermicro-tls_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

SuperMicro X11 servers do not support virtual media installations when the image is served using the `https` protocol. As a result, single-node OpenShift deployments for this environment fail to boot on the target node. To avoid this issue, log in to the hub cluster and disable Transport Layer Security (TLS) in the `Provisioning` resource. This ensures the image is not served with TLS even though the image address uses the `https` scheme.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Disable TLS in the `Provisioning` resource by running the following command:

   ```
   $ oc patch provisioning provisioning-configuration --type merge -p '{"spec":{"disableVirtualMediaTLS": true}}'
   ```
2. Continue the steps to deploy your single-node OpenShift cluster.

### [4.11. Removing a managed cluster site from the GitOps ZTP pipeline](#ztp-site-cleanup_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can remove a managed site and the associated installation and configuration policy CRs from the GitOps Zero Touch Provisioning (ZTP) pipeline.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Remove a site and the associated CRs by removing the associated `ClusterInstance` and `PolicyGenerator` or `PolicyGentemplate` files from the `kustomization.yaml` file.
2. Add the following `syncOptions` field to the ArgoCD application that manages the target site.

   ```
   kind: Application
   spec:
     syncPolicy:
       syncOptions:
       - PrunePropagationPolicy=background
   ```

   When you run the GitOps ZTP pipeline again, the generated CRs are removed.
3. Optional: If you want to permanently remove a site, you should also remove the `ClusterInstance` and site-specific `PolicyGenerator` or `PolicyGentemplate` files from the Git repository.
4. Optional: If you want to remove a site temporarily, for example when redeploying a site, you can leave the `ClusterInstance` and site-specific `PolicyGenerator` or `PolicyGentemplate` CRs in the Git repository.

### [4.12. Removing obsolete content from the GitOps ZTP pipeline](#ztp-removing-obsolete-content_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

If a change to the `PolicyGenerator` or `PolicyGentemplate` configuration results in obsolete policies, for example, if you rename policies, use the following procedure to remove the obsolete policies.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Remove the affected `PolicyGenerator` or `PolicyGentemplate` files from the Git repository, commit and push to the remote repository.
2. Wait for the changes to synchronize through the application and the affected policies to be removed from the hub cluster.
3. Add the updated `PolicyGenerator` or `PolicyGentemplate` files back to the Git repository, and then commit and push to the remote repository.

   Note

   Removing GitOps Zero Touch Provisioning (ZTP) policies from the Git repository, and as a result also removing them from the hub cluster, does not affect the configuration of the managed cluster. The policy and CRs managed by that policy remains in place on the managed cluster.
4. Optional: As an alternative, after making changes to `PolicyGenerator` or `PolicyGentemplate` CRs that result in obsolete policies, you can remove these policies from the hub cluster manually. You can delete policies from the RHACM console using the **Governance** tab or by running the following command:

   ```
   $ oc delete policy -n <namespace> <policy_name>
   ```

### [4.13. Tearing down the GitOps ZTP pipeline](#ztp-tearing-down-the-pipeline_ztp-deploying-far-edge-sites) Copy linkLink copied to clipboard!

You can remove the ArgoCD pipeline and all generated GitOps Zero Touch Provisioning (ZTP) artifacts.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Detach all clusters from Red Hat Advanced Cluster Management (RHACM) on the hub cluster.
2. Delete the `kustomization.yaml` file in the `deployment` directory using the following command:

   ```
   $ oc delete -k out/argocd/deployment
   ```
3. Commit and push your changes to the site repository.

## [Chapter 5. Manually installing a single-node OpenShift cluster with GitOps ZTP](#ztp-manual-install) Copy linkLink copied to clipboard!

You can deploy a managed single-node OpenShift cluster by using Red Hat Advanced Cluster Management (RHACM) and the assisted service.

Note

If you are creating multiple managed clusters, use the `ClusterInstance` method described in [Deploying far edge sites with ZTP](#ztp-deploying-far-edge-sites "Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources").

Important

The target bare-metal host must meet the networking, firmware, and hardware requirements listed in [Recommended cluster configuration for vDU application workloads](#sno-configure-for-vdu "Chapter 7. Recommended single-node OpenShift cluster configuration for vDU application workloads").

### [5.1. Extracting reference and example CRs from the ztp-site-generate container](#ztp-generating-install-and-config-crs-manually_ztp-manual-install) Copy linkLink copied to clipboard!

Use the `ztp-site-generate` container to extract reference custom resources (CRs) and example `ClusterInstance` CRs to prepare for cluster installation and Day 2 configuration.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You installed `podman`.

**Procedure**

1. Create an output folder by running the following command:

   ```
   $ mkdir -p ./out
   ```
2. Log in to the Ecosystem container registry with your credentials by running the following command:

   ```
   $ podman login registry.redhat.io
   ```
3. Extract the reference and example CRs from the `ztp-site-generate` container image by running the following command:

   ```
   $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 extract /home/ztp --tar | tar x -C ./out
   ```

   The `./out` directory contains the reference `PolicyGenerator` and `ClusterInstance` CRs in the `out/argocd/example/` folder.

   **Example output**

   ```
   out
    └── argocd
         └── example
              ├── acmpolicygenerator
              │     ├── {policy-prefix}common-ranGen.yaml
              │     ├── {policy-prefix}example-sno-site.yaml
              │     ├── {policy-prefix}group-du-sno-ranGen.yaml
              │     ├── ...
              │     ├── kustomization.yaml
              │     └── ns.yaml
              └── clusterinstance
                    ├── example-sno.yaml
                    ├── example-3node.yaml
                    ├── example-standard.yaml
                    └── ...
   ```
4. Create a `ClusterInstance` CR for your cluster.

   Use the example `ClusterInstance` CRs in the `out/argocd/example/clusterinstance/` folder that you previously extracted from the `ztp-site-generate` container as a reference. The folder includes example files for single node, three-node, and standard clusters:

   * `example-sno.yaml`
   * `example-3node.yaml`
   * `example-standard.yaml`

     Change the cluster and host details in the example file to match the type of cluster you want to install. For example:

     **Example single-node OpenShift ClusterInstance CR**

     ```
     # example-node1-bmh-secret & assisted-deployment-pull-secret need to be created under same namespace example-ai-sno
     ---
     apiVersion: siteconfig.open-cluster-management.io/v1alpha1
     kind: ClusterInstance
     metadata:
       name: "example-ai-sno"
       namespace: "example-ai-sno"
     spec:
       baseDomain: "example.com"
       pullSecretRef:
         name: "assisted-deployment-pull-secret"
       clusterImageSetNameRef: "openshift-4.22"
       sshPublicKey: "ssh-rsa AAAA..."
       clusterName: "example-ai-sno"
       networkType: "OVNKubernetes"
       # installConfigOverrides is a generic way of passing install-config
       # parameters through the siteConfig.  The 'capabilities' field configures
       # the composable openshift feature.  In this 'capabilities' setting, we
       # remove all the optional set of components.
       # Notes:
       # - OperatorLifecycleManager is needed for 4.15 and later
       # - NodeTuning is needed for 4.13 and later, not for 4.12 and earlier
       # - Ingress is needed for 4.16 and later
       installConfigOverrides: |
         {
           "capabilities": {
             "baselineCapabilitySet": "None",
             "additionalEnabledCapabilities": [
               "NodeTuning",
               "OperatorLifecycleManager",
               "Ingress"
             ]
           }
         }
       # Include references to extraManifest ConfigMaps.
       extraManifestsRefs:
         - name: sno-extra-manifest-configmap
       extraLabels:
         ManagedCluster:
           # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples
           du-profile: "latest"
           # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples in ../policygentemplates:
           # ../policygentemplates/common-ranGen.yaml will apply to all clusters with 'common: true'
           common: "true"
           # ../policygentemplates/group-du-sno-ranGen.yaml will apply to all clusters with 'group-du-sno: ""'
           group-du-sno: ""
           # ../policygentemplates/example-sno-site.yaml will apply to all clusters with 'sites: "example-sno"'
           # Normally this should match or contain the cluster name so it only applies to a single cluster
           sites : "example-sno"
       clusterNetwork:
         - cidr: 1001:1::/48
           hostPrefix: 64
       machineNetwork:
         - cidr: 1111:2222:3333:4444::/64
       serviceNetwork:
         - cidr: 1001:2::/112
       additionalNTPSources:
         - 1111:2222:3333:4444::2
       # Initiates the cluster for workload partitioning. Setting specific reserved/isolated CPUSets is done via PolicyTemplate
       # please see Workload Partitioning Feature for a complete guide.
       cpuPartitioningMode: AllNodes
       templateRefs:
         - name: ai-cluster-templates-v1
           namespace: open-cluster-management
       nodes:
         - hostName: "example-node1.example.com"
           role: "master"
           bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
           bmcCredentialsName:
             name: "example-node1-bmh-secret"
           bootMACAddress: "AA:BB:CC:DD:EE:11"
           # Use UEFISecureBoot to enable secure boot, UEFI to disable.
           bootMode: "UEFISecureBoot"
           rootDeviceHints:
             deviceName: "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0"
           # disk partition at `/var/lib/containers` with ignitionConfigOverride. Some values must be updated. See DiskPartitionContainer.md in argocd folder for more details
           ignitionConfigOverride: |
             {
               "ignition": {
                 "version": "3.2.0"
               },
               "storage": {
                 "disks": [
                   {
                     "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                     "partitions": [
                       {
                         "label": "var-lib-containers",
                         "sizeMiB": 0,
                         "startMiB": 250000
                       }
                     ],
                     "wipeTable": false
                   }
                 ],
                 "filesystems": [
                   {
                     "device": "/dev/disk/by-partlabel/var-lib-containers",
                     "format": "xfs",
                     "mountOptions": [
                       "defaults",
                       "prjquota"
                     ],
                     "path": "/var/lib/containers",
                     "wipeFilesystem": true
                   }
                 ]
               },
               "systemd": {
                 "units": [
                   {
                     "contents": "# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                     "enabled": true,
                     "name": "var-lib-containers.mount"
                   }
                 ]
               }
             }
           nodeNetwork:
             interfaces:
               - name: eno1
                 macAddress: "AA:BB:CC:DD:EE:11"
             config:
               interfaces:
                 - name: eno1
                   type: ethernet
                   state: up
                   ipv4:
                     enabled: false
                   ipv6:
                     enabled: true
                     address:
                     # For SNO sites with static IP addresses, the node-specific,
                     # API and Ingress IPs should all be the same and configured on
                     # the interface
                     - ip: 1111:2222:3333:4444::aaaa:1
                       prefix-length: 64
               dns-resolver:
                 config:
                   search:
                   - example.com
                   server:
                   - 1111:2222:3333:4444::2
               routes:
                 config:
                 - destination: ::/0
                   next-hop-interface: eno1
                   next-hop-address: 1111:2222:3333:4444::1
                   table-id: 254
           templateRefs:
             - name: ai-node-templates-v1
               namespace: open-cluster-management
     ```

     Note

     Optional: To provision additional install-time manifests on the provisioned cluster, create the extra manifest CRs and apply them to the hub cluster. Then reference them in the `extraManifestsRefs` field of the `ClusterInstance` CR. For more information, see "Customizing extra installation manifests in the GitOps ZTP pipeline".
5. Optional: Generate Day 2 configuration CRs from the reference `PolicyGenerator` CRs:

   1. Create an output folder for the configuration CRs by running the following command:

      ```
      $ mkdir -p ./ref
      ```
   2. Generate the configuration CRs by running the following command:

      ```
      $ podman run -it --rm -v `pwd`/out/argocd/example/policygentemplates:/resources:Z -v `pwd`/ref:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22 generator config -N . /output
      ```

      The command generates example group and cluster-specific configuration CRs in the `./ref` folder. You can apply these CRs to the cluster after installation is complete.

### [5.2. Creating the managed bare-metal host secrets](#ztp-creating-the-site-secrets_ztp-manual-install) Copy linkLink copied to clipboard!

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the GitOps Zero Touch Provisioning (ZTP) pipeline to access the Baseboard Management Controller (BMC) and a secret for the assisted installer service to pull cluster installation images from the registry.

Note

The secrets are referenced from the `ClusterInstance` CR by name. The namespace must match the `ClusterInstance` namespace.

**Procedure**

1. Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators:

   1. Save the following YAML as the file `example-sno-secret.yaml`:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
        name: example-sno-bmc-secret
        namespace: example-sno
      data:
        password: <base64_password>
        username: <base64_username>
      type: Opaque
      ---
      apiVersion: v1
      kind: Secret
      metadata:
        name: pull-secret
        namespace: example-sno
      data:
        .dockerconfigjson: <pull_secret>
      type: kubernetes.io/dockerconfigjson
      ```

      where:

      `namespace`
      :   Must match the namespace configured in the related `ClusterInstance` CR.

      `password`, `username`
      :   Base64-encoded values for `password` and `username`.

      `.dockerconfigjson`
      :   Base64-encoded pull secret.
2. Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.

### [5.3. Configuring Discovery ISO kernel arguments for manual installations using GitOps ZTP](#setting-managed-bare-metal-host-kernel-arguments_ztp-manual-install) Copy linkLink copied to clipboard!

The GitOps Zero Touch Provisioning (ZTP) workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements. For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation. In OpenShift Container Platform 4.22, you can only add kernel arguments. You can not replace or delete kernel arguments.

**Prerequisites**

* You have installed the OpenShift CLI (oc).
* You have logged in to the hub cluster as a user with cluster-admin privileges.
* You have applied a `ClusterInstance` CR to the hub cluster.

**Procedure**

1. Edit the `spec.kernelArguments` specification in the `InfraEnv` CR to configure kernel arguments:

   ```
   apiVersion: agent-install.openshift.io/v1beta1
   kind: InfraEnv
   metadata:
     name: <cluster_name>
     namespace: <cluster_name>
   spec:
     kernelArguments:
       - operation: append
         value: audit=0
       - operation: append
         value: trace=1
     clusterRef:
       name: <cluster_name>
       namespace: <cluster_name>
     pullSecretRef:
       name: pull-secret
   ```

   where:

   `operation`
   :   Specify the `append` operation to add a kernel argument.

   `value`
   :   Specify the kernel argument you want to configure. This example configures the `audit` kernel argument and the `trace` kernel argument.

   Note

   The `ClusterInstance` CR generates the `InfraEnv` resource as part of the day-0 installation CRs.

**Verification**

To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file.

1. Begin an SSH session with the target host:

   ```
   $ ssh -i /path/to/privatekey core@<host_name>
   ```
2. View the system’s kernel arguments by using the following command:

   ```
   $ cat /proc/cmdline
   ```

### [5.4. Installing a single managed cluster](#ztp-manually-install-a-single-managed-cluster_ztp-manual-install) Copy linkLink copied to clipboard!

You can manually deploy a single managed cluster using the assisted service and Red Hat Advanced Cluster Management (RHACM).

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have extracted the reference and example CRs from the `ztp-site-generate` container and you configured the `ClusterInstance` CR.
* You have created the baseboard management controller (BMC) `Secret` and the image pull-secret `Secret` custom resources (CRs). See "Creating the managed bare-metal host secrets" for details.
* Your target bare-metal host meets the networking and hardware requirements for managed clusters.

**Procedure**

1. Create a `ClusterImageSet` for each specific cluster version to be deployed, for example `clusterImageSet-4.22.yaml`. A `ClusterImageSet` has the following format:

   ```
   apiVersion: hive.openshift.io/v1
   kind: ClusterImageSet
   metadata:
     name: openshift-4.22.0
   spec:
      releaseImage: quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64
   ```

   where:

   `name`
   :   The descriptive version that you want to deploy.

   `releaseImage`
   :   Specifies the `releaseImage` to deploy and determines the operating system image version. The discovery ISO is based on the image version as set by `releaseImage`, or the latest version if the exact version is unavailable.
2. Apply the `clusterImageSet` CR:

   ```
   $ oc apply -f clusterImageSet-4.22.yaml
   ```
3. Create the `Namespace` CR in the `cluster-namespace.yaml` file:

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
        name: <cluster_name>
        labels:
           name: <cluster_name>
   ```

   where:

   `name`
   :   The name of the managed cluster to provision.
4. Apply the `Namespace` CR by running the following command:

   ```
   $ oc apply -f cluster-namespace.yaml
   ```
5. Apply the `ClusterInstance` CR that you configured to the hub cluster by running the following command:

   ```
   $ oc apply -f clusterinstance.yaml
   ```

   The SiteConfig Operator processes the `ClusterInstance` CR and automatically generates the required installation CRs, including `BareMetalHost`, `AgentClusterInstall`, `ClusterDeployment`, `InfraEnv`, and `NMStateConfig`. The assisted service then begins the cluster installation.

### [5.5. Late binding for bare-metal host pools in GitOps ZTP deployments](#ztp-late-binding-bare-metal-host-pools_ztp-manual-install) Copy linkLink copied to clipboard!

In the standard GitOps ZTP flow, the `InfraEnv` custom resource (CR) references a specific `ClusterDeployment` CR, and all discovered hosts are automatically associated with that cluster. Late binding separates host discovery from cluster assignment, so you can manage a pool of bare-metal hosts independently from cluster lifecycle.

With late binding, you create an `InfraEnv` CR without a `ClusterDeployment` reference, so that all hosts booted from the discovery ISO remain unbound and available for assignment to any cluster. You then use the `bmac.agent-install.openshift.io/cluster-reference` annotation on `BareMetalHost` resources to declaratively bind individual hosts to specific `ClusterDeployment` CRs. This annotation-based binding is compatible with GitOps workflows such as ArgoCD.

Late binding in the GitOps ZTP workflow is designed for environments where hardware provisioning and cluster creation happen independently. Common scenarios include:

* An infrastructure team boots a set of bare-metal servers from a single discovery ISO, and a platform team later assigns subsets of those hosts to different clusters as demand arises.
* Hardware provisioning and cluster creation are handled by different teams at different times.
* Spare bare metal capacity must be allocated to clusters as workload requirements change.

If you are deploying a single cluster where all discovered hosts belong to that cluster, use the standard GitOps ZTP flow with a `ClusterDeployment` reference in the `InfraEnv` CR.

### [5.6. Bind bare-metal hosts to clusters using the cluster-reference annotation in GitOps ZTP deployments](#ztp-binding-bmh-to-cluster-using-annotation_ztp-manual-install) Copy linkLink copied to clipboard!

In GitOps ZTP deployments, you can declaratively bind individual `BareMetalHost` resources from a shared `InfraEnv` pool to specific `ClusterDeployment` CRs by using the `bmac.agent-install.openshift.io/cluster-reference` annotation. This approach is compatible with GitOps workflows because the binding is managed through annotations on the `BareMetalHost` resource rather than by patching `Agent` CRs directly.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created an `InfraEnv` CR without a `clusterRef` field. If you use the SiteConfig Operator, verify that the generated `InfraEnv` does not include a `clusterRef` field.
* You have `BareMetalHost` resources that reference the shared `InfraEnv`. These resources are either generated automatically by the SiteConfig Operator from a `ClusterInstance` CR, or created manually with the `infraenvs.agent-install.openshift.io` label set to the name of the `InfraEnv` CR.
* You have booted the hosts from the discovery ISO and `Agent` CRs have been created automatically for the discovered hosts.
* You have created the target `ClusterDeployment` and `AgentClusterInstall` CRs for the cluster that you want to bind hosts to.

**Procedure**

1. Verify that the `InfraEnv` CR does not have a `clusterRef` field set:

   ```
   $ oc get infraenv <infraenv_name> -n <namespace> -o jsonpath='{.spec.clusterRef}'
   ```

   If the command returns an empty result, the `InfraEnv` is configured for late binding. If a `clusterRef` value is returned, the `BareMetalHost` cluster-reference annotation is ignored and you must use the standard binding flow.
2. Verify that the `Agent` CRs exist and are not bound to a cluster:

   ```
   $ oc get agents -n <namespace>
   ```

   **Example output**

   ```
   NAME                                   CLUSTER   APPROVED   ROLE          STAGE
   aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb             false      auto-assign
   cccccccc-4444-5555-6666-dddddddddddd             false      auto-assign
   ```

   Agents that are not bound to a cluster have an empty `CLUSTER` column.
3. Add the `bmac.agent-install.openshift.io/cluster-reference` annotation to the `BareMetalHost` resource to bind it to the target `ClusterDeployment` CR:

   ```
   $ oc annotate bmh <bmh_name> -n <namespace> \
       bmac.agent-install.openshift.io/cluster-reference=<cluster_namespace>/<cluster_name>
   ```

   Replace `<cluster_namespace>/<cluster_name>` with the namespace and name of the target `ClusterDeployment` CR.

   Alternatively, you can set the annotation declaratively in the `BareMetalHost` YAML manifest:

   ```
   apiVersion: metal3.io/v1alpha1
   kind: BareMetalHost
   metadata:
     name: worker-01
     namespace: my-infraenv-ns
     annotations:
       bmac.agent-install.openshift.io/cluster-reference: my-cluster-ns/my-cluster
     labels:
       infraenvs.agent-install.openshift.io: my-infraenv
   spec:
     online: true
     bootMACAddress: 00:00:5E:00:53:01
     bmc:
       address: redfish-virtualmedia://192.0.2.10/redfish/v1/Systems/1
       credentialsName: worker-01-bmc-secret
   ```

   The `bmac.agent-install.openshift.io/cluster-reference` annotation value uses the format `<namespace>/<name>`, referencing the target `ClusterDeployment`.
4. Verify that the `Agent` CR is bound to the correct `ClusterDeployment` CR by running the following command:

   ```
   $ oc get agents -n <namespace>
   ```

   **Example output**

   ```
   NAME                                   CLUSTER      APPROVED   ROLE          STAGE
   aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb   my-cluster   false      auto-assign
   ```

   The `CLUSTER` column shows the name of the target `ClusterDeployment`.
5. Verify the `Bound` condition on the `Agent` CR:

   ```
   $ oc get agent <agent_name> -n <namespace> \
       -o jsonpath='{.status.conditions[?(@.type=="Bound")]}'
   ```

   A successfully bound agent shows `status: "True"` and `reason: "Bound"` in the output.

   Note

   Agents discovered by using a `BareMetalHost` resource are automatically approved for installation when the `bootMACAddress` in the `BareMetalHost` matches a NIC in the inventory of the discovered host. You do not need to manually approve these agents.
6. Optional: To unbind a host from a cluster before installation starts, set the annotation value to an empty string:

   ```
   $ oc annotate bmh <bmh_name> -n <namespace> \
       bmac.agent-install.openshift.io/cluster-reference="" --overwrite
   ```

   The bare metal agent controller (BMAC) clears the `spec.clusterDeploymentName` field on the corresponding `Agent` CR, and the host returns to the unbound pool.

   Important

   You cannot unbind a host after cluster installation has started. If you try to unbind a host that is already installed or in an `error` or `canceled` state, the `Agent` CR `Bound` condition is set to `False` with the reason `UnbindingPendingUserAction`. For hosts discovered by using a `BareMetalHost` resource, the assisted controllers automatically use the `BareMetalHost` to boot the host back into the discovery ISO to complete the unbinding process. For hosts discovered without a `BareMetalHost` resource, you must manually reboot the host with the discovery ISO.

**Verification**

* Verify that all agents are approved and bound to the correct cluster:

  ```
  $ oc get agents -n <namespace> -o custom-columns=NAME:.metadata.name,CLUSTER:.spec.clusterDeploymentName.name,APPROVED:.spec.approved
  ```

### [5.7. BareMetalHost cluster-reference annotation](#ztp-bmh-cluster-reference-annotation-ref_ztp-manual-install) Copy linkLink copied to clipboard!

The `bmac.agent-install.openshift.io/cluster-reference` annotation on `BareMetalHost` resources controls the declarative binding of discovered hosts to `ClusterDeployment` CRs. You can use this annotation to bind, unbind, or leave hosts unchanged in a late binding workflow.

Expand

Table 5.1. Cluster-reference annotation states

| Annotation state | Value | Effect on Agent CR |
| --- | --- | --- |
| Set with cluster reference | `<namespace>/<name>` | Sets `spec.clusterDeploymentName` to the referenced `ClusterDeployment` CR. The `Agent` is bound to the specified cluster. |
| Set with empty string | `""` | Clears `spec.clusterDeploymentName`. The `Agent` is unbound from its current cluster and returns to the unbound pool. |
| Not set | N/A | No change to the `Agent` CR cluster reference. The host remains in its current state. |

Show more

Expand

Table 5.2. Constraints and precedence rules

| Constraint | Description |
| --- | --- |
| `InfraEnv` `clusterRef` takes precedence | If the `InfraEnv` CR has a `clusterRef` field set, the `BareMetalHost` cluster-reference annotation is ignored. The `InfraEnv` CR must not have a `clusterRef` for late binding to work. |
| Unbinding is blocked after installation starts | You can only unbind a host before cluster installation begins. After the installation starts, setting the annotation to an empty string results in an `UnbindingPendingUserAction` state on the `Agent` CR. |
| `ClusterDeployment` CR must exist | The `ClusterDeployment` CR referenced by the annotation must exist in the specified namespace. If the `ClusterDeployment` CR does not exist, the binding fails. |
| One `InfraEnv` CR per host | Each `BareMetalHost` CR is associated with a single `InfraEnv` CR through the `infraenvs.agent-install.openshift.io` label. |

Show more

Expand

Table 5.3. Related BareMetalHost bare metal agent controller (BMAC) annotations

| Annotation | Description |
| --- | --- |
| `bmac.agent-install.openshift.io/cluster-reference` | Binds the host to a specific `ClusterDeployment` CR. Value format: `<namespace>/<name>`. |
| `bmac.agent-install.openshift.io/hostname` | Sets the hostname for the agent during deployment. |
| `bmac.agent-install.openshift.io/role` | Sets the role of the host, such as `master` or `worker`. |
| `bmac.agent-install.openshift.io/installer-args` | Passes additional arguments to the OpenShift Container Platform installer. |
| `bmac.agent-install.openshift.io/ignition-config-overrides` | Provides ignition configuration overrides for the host. |

Show more

### [5.8. Monitoring the managed cluster installation status](#ztp-checking-the-managed-cluster-status_ztp-manual-install) Copy linkLink copied to clipboard!

Ensure that cluster provisioning was successful by checking the cluster status.

**Prerequisites**

* All of the custom resources have been configured and provisioned, and the `Agent` custom resource is created on the hub for the managed cluster.

**Procedure**

1. Check the status of the managed cluster:

   ```
   $ oc get managedcluster
   ```

   `True` indicates the managed cluster is ready.
2. Check the agent status:

   ```
   $ oc get agent -n <cluster_name>
   ```
3. Use the `describe` command to provide an in-depth description of the agent’s condition. Statuses to be aware of include `BackendError`, `InputError`, `ValidationsFailing`, `InstallationFailed`, and `AgentIsConnected`. These statuses are relevant to the `Agent` and `AgentClusterInstall` custom resources.

   ```
   $ oc describe agent -n <cluster_name>
   ```
4. Check the cluster provisioning status:

   ```
   $ oc get agentclusterinstall -n <cluster_name>
   ```
5. Use the `describe` command to provide an in-depth description of the cluster provisioning status:

   ```
   $ oc describe agentclusterinstall -n <cluster_name>
   ```
6. Check the status of the managed cluster’s add-on services:

   ```
   $ oc get managedclusteraddon -n <cluster_name>
   ```
7. Retrieve the authentication information of the `kubeconfig` file for the managed cluster:

   ```
   $ oc get secret -n <cluster_name> <cluster_name>-admin-kubeconfig -o jsonpath={.data.kubeconfig} | base64 -d > <directory>/<cluster_name>-kubeconfig
   ```

### [5.9. Troubleshooting the managed cluster](#ztp-troubleshooting-the-managed-cluster_ztp-manual-install) Copy linkLink copied to clipboard!

Use this procedure to diagnose any installation issues that might occur with the managed cluster.

**Procedure**

1. Check the status of the managed cluster:

   ```
   $ oc get managedcluster
   ```

   **Example output**

   ```
   NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
   SNO-cluster     true                                   True     True      2d19h
   ```

   If the status in the `AVAILABLE` column is `True`, the managed cluster is being managed by the hub.

   If the status in the `AVAILABLE` column is `Unknown`, the managed cluster is not being managed by the hub. Use the following steps to continue checking to get more information.
2. Check the `AgentClusterInstall` install status:

   ```
   $ oc get clusterdeployment -n <cluster_name>
   ```

   **Example output**

   ```
   NAME        PLATFORM            REGION   CLUSTERTYPE   INSTALLED    INFRAID    VERSION  POWERSTATE AGE
   Sno0026    agent-baremetal                               false                          Initialized
   2d14h
   ```

   If the status in the `INSTALLED` column is `false`, the installation was unsuccessful.
3. If the installation failed, enter the following command to review the status of the `AgentClusterInstall` resource:

   ```
   $ oc describe agentclusterinstall -n <cluster_name> <cluster_name>
   ```
4. Resolve the errors and reset the cluster:

   1. Remove the cluster’s managed cluster resource:

      ```
      $ oc delete managedcluster <cluster_name>
      ```
   2. Remove the cluster’s namespace:

      ```
      $ oc delete namespace <cluster_name>
      ```

      This deletes all of the namespace-scoped custom resources created for this cluster. You must wait for the `ManagedCluster` CR deletion to complete before proceeding.
   3. Recreate the custom resources for the managed cluster.

### [5.10. RHACM generated cluster installation CRs](#ztp-installation-crs_ztp-manual-install) Copy linkLink copied to clipboard!

Red Hat Advanced Cluster Management (RHACM) supports deploying OpenShift Container Platform on single-node clusters, three-node clusters, and standard clusters with a specific set of installation custom resources (CRs) that you generate by using `ClusterInstance` CRs for each cluster.

Note

Every managed cluster has its own namespace, and all of the installation CRs except for `ManagedCluster` and `ClusterImageSet` are under that namespace. `ManagedCluster` and `ClusterImageSet` are cluster-scoped, not namespace-scoped. The namespace and the CR names match the cluster name.

The following table lists the installation CRs that are automatically applied by the RHACM assisted service when it installs clusters using the `ClusterInstance` CRs that you configure.

Expand

Table 5.4. Cluster installation CRs generated by RHACM

| CR | Description | Usage |
| --- | --- | --- |
| `BareMetalHost` | Contains the connection information for the Baseboard Management Controller (BMC) of the target bare-metal host. In late binding scenarios where the `InfraEnv` CR is not bound to a `ClusterDeployment` CR, the optional `bmac.agent-install.openshift.io/cluster-reference` annotation on the `BareMetalHost` CR declaratively binds the host to a specific `ClusterDeployment` CR. | Provides access to the BMC to load and start the discovery image on the target server by using the Redfish protocol. |
| `InfraEnv` | Contains information for installing OpenShift Container Platform on the target bare-metal host. | Used with `ClusterDeployment` to generate the discovery ISO for the managed cluster. Can also be created without a `ClusterDeployment` reference to enable late binding, where hosts are bound to clusters individually by using the `BareMetalHost` cluster-reference annotation. |
| `AgentClusterInstall` | Specifies details of the managed cluster configuration such as networking and the number of control plane nodes. Displays the cluster `kubeconfig` and credentials when the installation is complete. | Specifies the managed cluster configuration information and provides status during the installation of the cluster. |
| `ClusterDeployment` | References the `AgentClusterInstall` CR to use. | Used with `InfraEnv` to generate the discovery ISO for the managed cluster. |
| `NMStateConfig` | Provides network configuration information such as `MAC` address to `IP` mapping, DNS server, default route, and other network settings. | Sets up a static IP address for the managed cluster’s Kube API server. |
| `Agent` | Contains hardware information about the target bare-metal host. | Created automatically on the hub when the target machine’s discovery image boots. |
| `ManagedCluster` | When a cluster is managed by the hub, it must be imported and known. This Kubernetes object provides that interface. | The hub uses this resource to manage and show the status of managed clusters. |
| `KlusterletAddonConfig` | Contains the list of services provided by the hub to be deployed to the `ManagedCluster` resource. | Tells the hub which add-on services to deploy to the `ManagedCluster` resource. |
| `Namespace` | Logical space for `ManagedCluster` resources existing on the hub. Unique per site. | Propagates resources to the `ManagedCluster`. |
| `Secret` | Two CRs are created: `BMC Secret` and `Image Pull Secret`. | * `BMC Secret` authenticates into the target bare-metal host using its username and password. * `Image Pull Secret` contains authentication information for the OpenShift Container Platform image installed on the target bare-metal host. |
| `ClusterImageSet` | Contains OpenShift Container Platform image information such as the repository and image name. | Passed into resources to provide OpenShift Container Platform images. |

Show more

## [Chapter 6. Migrating from SiteConfig CRs to ClusterInstance CRs](#ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

You can incrementally migrate single-node OpenShift clusters from `SiteConfig` custom resources (CRs) to `ClusterInstance` CRs. During migration, the existing and new pipelines run in parallel, so you can migrate one or more clusters at a time in a controlled and phased manner.

Important

* The `SiteConfig` CR is deprecated from OpenShift Container Platform version 4.18 and removed from OpenShift Container Platform 4.21.
* The `ClusterInstance` CR is available from Red Hat Advanced Cluster Management (RHACM) version 2.12 or later.

### [6.1. Overview of migrating from SiteConfig CRs to ClusterInstance CRs](#ztp-migrate-clusterinstance-overview_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

The `ClusterInstance` CR provides a more unified and generic approach to defining clusters and is the preferred method for managing cluster deployments in the GitOps ZTP workflow. The SiteConfig Operator, which manages the `ClusterInstance` custom resource (CR), is a fully developed controller shipped as an add-on within Red Hat Advanced Cluster Management (RHACM).

Important

The SiteConfig Operator only reconciles updates for `ClusterInstance` objects. The controller does not monitor or manage deprecated `SiteConfig` objects.

The migration from `SiteConfig` CRs to `ClusterInstance` CRs provides several improvements, such as enhanced scalability and a clear separation of cluster parameters from the cluster deployment method. For more information about these improvements, and the SiteConfig Operator, see [SiteConfig](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.12/html-single/multicluster_engine_operator_with_red_hat_advanced_cluster_management/index#siteconfig-intro).

The migration process involves the following high-level steps:

1. Set up the parallel pipeline by preparing a new Git folder structure in your repository and creating the corresponding Argo CD project and application.
2. To migrate the clusters incrementally, first remove the associated `SiteConfig` CR from the old pipeline. Then, add a corresponding `ClusterInstance` CR to the new pipeline.

   Note

   By using the `prune=false` sync policy in the initial Argo CD application, the resources managed by this pipeline remain intact even after you remove the target cluster from this application. This approach ensures that the existing cluster resources remain operational during the migration process.

   1. Optionally, use the `siteconfig-converter` tool to automatically convert existing `SiteConfig` CRs to `ClusterInstance` CRs.
3. When you complete the cluster migration, delete the original Argo project and application and clean up any related resources.

The following sections describe how to migrate an example cluster, `sno1`, from using a `SiteConfig` CR to a `ClusterInstance` CR.

The following Git repository folder structure is used as a basis for this example migration:

```
├── site-configs/
│   ├── kustomization.yaml
│   ├── hub-1/
│   │   └── kustomization.yaml
│   │   ├── sno1.yaml
│   │   ├── sno2.yaml
│   │   ├── sno3.yaml
│   │   ├── extra-manifest/
│   │   │   ├── enable-crun-master.yaml
│   │   │   └── enable-crun-worker.yaml
│   ├── pre-reqs/
│   │   ├── kustomization.yaml
│   │   ├── sno1/
│   │   │   ├── bmc-credentials.yaml
│   │   │   ├── kustomization.yaml
│   │   │   └── pull-secret.yaml
│   │   ├── sno2/
│   │   │   ├── bmc-credentials.yaml
│   │   │   ├── kustomization.yaml
│   │   │   └── pull-secret.yaml
│   │   └── sno3/
│   │       ├── bmc-credentials.yaml
│   │       ├── kustomization.yaml
│   │       └── pull-secret.yaml
│   ├── reference-manifest/
│   │   └── 4.22/
│   ├──resources/
│   │   ├── active-ocp-version.yaml
│   │   └── kustomization.yaml

└── site-policies/ #Policies and configurations implemented for the clusters
...
```

### [6.2. Preparing a parallel Argo CD pipeline for ClusterInstance CRs](#ztp-creating-argocd-clusterinstance_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

Create a parallel Argo CD project and application to manage the new `ClusterInstance` CRs and associated cluster resources.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have configured your GitOps ZTP environment successfully.
* You have installed and configured the Assisted Installer service successfully.
* You have access to the Git repository that contains your single-node OpenShift cluster configurations.

**Procedure**

1. Create YAML files for the parallel Argo project and application:

   1. Create a YAML file that defines the `AppProject` resource:

      **Example `ztp-app-project-v2.yaml` file**

      ```
      apiVersion: argoproj.io/v1alpha1
      kind: AppProject
      metadata:
        name: ztp-app-project
        namespace: openshift-gitops
        annotations:
          argocd.argoproj.io/sync-wave: "100"
      spec:
        clusterResourceWhitelist:
        - group: 'hive.openshift.io'
          kind: ClusterImageSet
        - group: 'cluster.open-cluster-management.io'
          kind: ManagedCluster
        - group: ''
          kind: Namespace
        destinations:
        - namespace: '*'
          server: '*'
        namespaceResourceWhitelist:
        - group: ''
          kind: ConfigMap
        - group: ''
          kind: Namespace
        - group: ''
          kind: Secret
        - group: 'extensions.hive.openshift.io'
          kind: ImageClusterInstall
        - group: 'metal3.io'
          kind: DataImage
        - group: 'siteconfig.open-cluster-management.io'
          kind: ClusterInstance
      ```

      1

      ```
        sourceRepos:
        - '*'
      ```

      [1](#CO1-1)
      :   The `ClusterInstance` CR manages the `siteconfig.open-cluster-management.io` object instead of the `SiteConfig` CR.
   2. Create a YAML file that defines the `Application` resource:

      **Example `clusters-v2.yaml` file**

      ```
      apiVersion: argoproj.io/v1alpha1
      kind: Application
      metadata:
        name: clusters-v2
        namespace: openshift-gitops
      spec:
        destination:
          namespace: clusters-sub
          server: https://kubernetes.default.svc
        ignoreDifferences:
        - group: cluster.open-cluster-management.io
          kind: ManagedCluster
          managedFieldsManagers:
          - controller
        project: ztp-app-project-v2
      ```

      1

      ```
        source:
          path: site-configs-v2
      ```

      2

      ```
          repoURL: http://infra.5g-deployment.lab:3000/student/ztp-repository.git
          targetRevision: main
        syncPolicy:
          syncOptions:
          - CreateNamespace=true
          - PrunePropagationPolicy=background
          - RespectIgnoreDifferences=true
      ```

      [1](#CO2-1)
      :   The `project` field must match the name of the `AppProject` resource created in the previous step.

      [2](#CO2-2)
      :   The `path` field must match the root folder in your Git repository that will contain the `ClusterInstance` CRs and associated resources.

      Note

      By default, `auto-sync` is enabled. However, synchronization only occurs when you push configuration data for the cluster to the new configuration folder, or in this example, the `site-configs-v2/` folder.
2. Create and commit a root folder in your Git repository that will contain the `ClusterInstance` CRs and associated resources, for example:

   ```
   $ mkdir site-configs-v2
   $ touch site-configs-v2/.gitkeep
   $ git commit -s -m “Creates cluster-instance folder”
   $ git push origin main
   ```

   * The `.gitkeep` file is a placeholder to ensure that the empty folder is tracked by Git.

     Note

     You only need to create and commit the root `site-configs-v2/` folder during pipeline setup. You will mirror the complete `site-configs/` folder structure into `site-configs-v2/` during the cluster migration procedure.
3. Apply the `AppProject` and `Application` resources to the hub cluster by running the following commands:

   ```
   $ oc apply -f ztp-app-project-v2.yaml
   $ oc apply -f clusters-v2.yaml
   ```

**Verification**

1. Verify that the original Argo CD project, `ztp-app-project`, and the new Argo CD project, `ztp-app-project-v2` are present on the hub cluster by running the following command:

   ```
   $ oc get appprojects -n openshift-gitops
   ```

   **Example output**

   ```
   NAME                 AGE
   default              46h
   policy-app-project   42h
   ztp-app-project      18h
   ztp-app-project-v2    14s
   ```
2. Verify that the original Argo CD application, `clusters`, and the new Argo CD application, `clusters-v2` are present on the hub cluster by running the following command:

   ```
   $ oc get application.argo -n openshift-gitops
   ```

   **Example output**

   ```
   NAME                       SYNC STATUS   HEALTH STATUS
   clusters                   Synced        Healthy
   clusters-v2                Synced        Healthy
   policies                   Synced        Healthy
   ```

### [6.3. Transitioning the active-ocp-version ClusterImageSet](#ztp-active-ocp-version_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

Optionally, the `active-ocp-version` `ClusterImageSet` is a GitOps Zero Touch Provisioning (ZTP) convention used in GitOps ZTP deployments. It provides a single, central definition of the OpenShift Container Platform release image to use when provisioning clusters. By default, this resource is synchronized to the hub cluster from the `site-config/resources/` folder.

If your deployment uses an `active-ocp-version` `ClusterImageSet` CR, you must migrate it to the `resources/` folder in the new directroy that contains `ClusterInstance` CRs. This prevents synchronization conflicts because both Argo CD applications cannot manage the same resource.

**Prerequisites**

* You have completed the procedure to create the parallel Argo CD pipeline for `ClusterInstance` CRs.
* The Argo CD application points to the folder in your Git repository that will contain the new `ClusterInstance` CRs and associated cluster resouces. In this example, the `site-configs-v2/` Argo CD application points to the `site-configs-v2/` folder.
* Your Git repository contains an `active-ocp-version.yaml` manifest in the `resources/` folder.

**Procedure**

1. Copy the `resources/` folder from the `site-configs/` directory into the new `site-configs-v2/` directory:

   ```
   $ cp -r site-configs/resources site-configs-v2/
   ```
2. Remove the reference to the `resources/` folder from the `site-configs/kustomization.yaml` file. This ensures that the old `clusters` Argo CD application no longer manages the `active-ocp-version` resource.

   **Example updated `site-configs/resources/kustomization.yaml` file**

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
      - pre-reqs/
      #- resources/
   generators:
      - hub-1/sno1.yaml
      - hub-1/sno2.yaml
      - hub-1/sno3.yaml
   ```
3. Add the `resources/` folder to the `site-configs-v2/kustomization.yaml` file. This step transfers ownership of the `ClusterImageSet` to the new `clusters-v2` application.

   **Example updated `site-configs-v2/kustomization.yaml` file**

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - resources/
   ```
4. Commit and push the changes to the Git repository.

**Verification**

1. In Argo CD, verify that the `clusters-v2` application is **Healthy** and **Synced**.
2. If the `active-ocp-version` `ClusterImageSet` resource in the `cluster` Argo application is out of sync, you can remove the Argo CD application label by running the following command:

   ```
   $ oc label clusterimageset active-ocp-version app.kubernetes.io/instance-
   ```

   **Example output**

   ```
   clusterimageset.hive.openshift.io/active-ocp-version unlabeled
   ```

### [6.4. Performing the migration from SiteConfig CR to ClusterInstance CR](#ztp-migrating-sno-clusterinstance_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

Migrate a single-node OpenShift cluster from using a `SiteConfig` CR to a `ClusterInstance` CR by removing the `SiteConfig` CR from the old pipeline, and adding a corresponding `ClusterInstance` CR to the new pipeline.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have set up the parallel Argo CD pipeline, including the Argo CD project and application, that will manage the cluster using the `ClusterInstance` CR.
* The Argo CD application managing the original `SiteConfig` CR pipeline is configured with the sync policy `prune=false`. This setting ensures that resources remain intact after you remove the target cluster from this application.
* You have access to the Git repository that contains your single-node OpenShift cluster configurations.
* You have Red Hat Advanced Cluster Management (RHACM) version 2.12 or later installed in the hub cluster.
* The SiteConfig Operator is installed and running in the hub cluster.
* You have installed Podman and you have access to the registry.redhat.io container image registry.

**Procedure**

1. Mirror the `site-configs` folder structure to the new `site-configs-v2` directory that will contain the `ClusterInstance` CRs, for example:

   ```
   site-configs-v2/
   ├── hub-1/
   ```

   1

   ```
   │   └── extra-manifest/
   ├── pre-reqs/
   │   └── sno1/
   ```

   2

   ```
   ├── reference-manifest/
   │   └── 4.22/
   └── resources/
   ```

   [1](#CO3-1)
   :   The `hub-1/` folder will contain the `ClusterInstance` CR for each cluster.

   [2](#CO3-2)
   :   Mirror the target cluster, in this example `sno1`, to include the required pre-requisite resources such as the image registry pull secret, the baseboard management controller credentials, and so on.
2. Remove the target cluster from the original Argo CD application by commenting out the resources in the related files in Git:

   1. Comment out the target cluster from the `site-configs/kustomization.yaml` file, for example:

      ```
      $ cat site-configs/kustomization.yaml
      ```

      **Example updated `site-configs/kustomization.yaml` file**

      ```
      apiVersion: kustomize.config.k8s.io/v1beta1
      kind: Kustomization
      resources:
         - pre-reqs/
         #- resources/
      generators:
         #- hub-1/sno1.yaml
         - hub-1/sno2.yaml
         - hub-1/sno3.yaml
      ```
   2. Comment out the target cluster from the `site-configs/pre-reqs/kustomization.yaml` file. This removes the `site-configs/pre-reqs/sno1` folder, which also requires migration and has resources such as the image registry pull secret, the baseboard management controller credentials, and so on, for example:

      ```
      $ cat site-configs/pre-reqs/kustomization.yaml
      ```

      **Example updated `site-configs/pre-reqs/kustomization.yaml` file**

      ```
      apiVersion: kustomize.config.k8s.io/v1beta1
      kind: Kustomization
      resources:
        #- sno1/
        - sno2/
        - sno3/
      ```
3. Commit the changes to the Git repository.

   Note

   After you commit the changes, the original Argo CD application reports an `OutOfSync` sync status because the Argo CD application still attempts to monitor the status of the taget cluster’s resources. However, because the sync policy is set to `prune=false`, the Argo CD application does not delete any resources.
4. To ensure that the original Argo CD application no longer manages the cluster resources, you can remove the Argo CD application label from the resources by running the following command:

   ```
   $ for cr in bmh,hfs,clusterdeployment,agentclusterinstall,infraenv,nmstateconfig,configmap,klusterletaddonconfig,secrets; do oc label $cr app.kubernetes.io/instance- --all -n sno1; done && oc label ns sno1 app.kubernetes.io/instance- && oc label managedclusters sno1 app.kubernetes.io/instance-
   ```

   The Argo CD application label is removed from all resources in the `sno1` namespace and the sync status returns to `Synced`.
5. Create the `ClusterInstance` CR for the target cluster by using the `siteconfig-converter` tool packaged with the `ztp-site-generate` container image:

   Note

   The siteconfig-converter tool cannot translate earlier versions of the `AgentClusterInstall` resource that uses the following deprecated fields in the `SiteConfig` CR:

   * `apiVIP`
   * `ingressVIP`
   * `manifestsConfigMapRef`

   To solve this issue, you can do one of the following options:

   * Create a custom cluster template that includes these fields. For more information about creating custom templates, see [Creating custom templates with the SiteConfig operator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html/multicluster_engine_operator_with_red_hat_advanced_cluster_management/siteconfig-intro#create-custom-templates)
   * Suppress the creation of the `AgentClusterInstall` resource by adding it to the `suppressedManifests` list in the `ClusterInstance` CR, or by using the `-s` flag in the `siteconfig-converter` tool. You must remove the resource from the `suppressedManifests` list when reinstalling the cluster.

   1. Pull the `ztp-site-generate` container image by running the following command:

      ```
      podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:4.22
      ```
   2. Run the `siteconfig-converter` tool interactively through the container by running the following command:

      ```
      $ podman run -v "${PWD}":/resources:Z,U -it registry.redhat.io/openshift4/ztp-site-generate-rhel8:{product-version} siteconfig-converter -d /resources/<output_folder> /resources/<path_to_siteconfig_resource>
      ```

      * Replace `<output_folder>` with the output directory for the generated files.
      * Replace `<path_to_siteconfig_resource>` with the path to the target `SiteConfig` CR file.

        **Example output**

        ```
        Successfully read SiteConfig: sno1/sno1
        Converted cluster 1 (sno1) to ClusterInstance: /resources/output/sno1.yaml
        WARNING: Added default extraManifest ConfigMap 'extra-manifests-cm' to extraManifestsRefs. This configmap is created automatically.
        Successfully converted 1 cluster(s) to ClusterInstance files in /resources/output: sno1.yaml
        Generating ConfigMap kustomization files...
        Using ConfigMap name: extra-manifests-cm, namespace: sno1, manifests directory: extra-manifests
        Generating ConfigMap kustomization files with name: extra-manifests-cm, namespace: sno1, manifests directory: extra-manifests
        Generating extraManifests for SiteConfig: /resources/sno1.yaml
        Successfully generated extra manifests in /resources/output/extra-manifests
        --- Kustomization.yaml Generator ---
        Scanning directory: /resources/output/extra-manifests
        Found and adding: extra-manifests/enable-crun-master.yaml
        Found and adding: extra-manifests/enable-crun-worker.yaml
        ------------------------------------
        kustomization-configMapGenerator-snippet.yaml generated successfully at: /resources/output/kustomization-configMapGenerator-snippet.yaml
        Content:
        apiVersion: kustomize.config.k8s.io/v1beta1
        kind: Kustomization
        configMapGenerator:
            - files:
                - extra-manifests/enable-crun-master.yaml
                - extra-manifests/enable-crun-worker.yaml
              name: extra-manifests-cm
              namespace: sno1
        generatorOptions:
            disableNameSuffixHash: true

        ------------------------------------
        ```

        Note

        The `ClusterInstance` CR requires the extra manifests to be defined in a `ConfigMap` resource.

        To meet this requirement, the `siteconfig-converter` tool generates a `kustomization.yaml` snippet. The generated snippet uses Kustomize’s `configMapGenerator` to automatically package your manifest files into the required `ConfigMap` resource. You must merge this snippet into your original `kustomization.yaml` file to ensure that the `ConfigMap` resource is created and managed alongside your other cluster resources.
6. Configure the new Argo CD application to manage the target cluster by referencing it in the new pipelines `Kustomization` files, for example:

   ```
   $ cat site-configs-v2/kustomization.yaml
   ```

   **Example updated `site-configs-v2/kustomization.yaml` file**

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - resources/
     - pre-reqs/
     - hub-1/sno1.yaml
   ```

   ```
   $ cat  site-configs-v2/pre-reqs/kustomization.yaml
   ```

   **Example updated `site-configs-v2/pre-reqs/kustomization.yaml` file**

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - sno1/
   ```
7. Commit the changes to the Git repository.

**Verification**

1. Verify that the `ClusterInstance` CR is successfully deployed and the provisioning status complete by running the following command:

   ```
   $ oc get clusterinstance -A
   ```

   **Example output**

   ```
   NAME                                                         PAUSED   PROVISIONSTATUS   PROVISIONDETAILS         AGE
   clusterinstance.siteconfig.open-cluster-management.io/sno1            Completed         Provisioning completed   27s
   ```

   At this point, the new Argo CD application that uses the `ClusterInstance` CR is managing the `sno1` cluster. You can continue to migrate one or more clusters at a time by repeating these steps until all target clusters are migrated to the new pipeline.
2. Verify the folder structure and files in the `site-configs-v2/` directory contain the migrated resources for the `sno1` cluster, for example:

   ```
   site-configs-v2/
   ├── hub-1/
   │   ├── sno1.yaml
   ```

   1

   ```
   ├── extra-manifest/
   │   ├── enable-crun-worker.yaml
   ```

   2

   ```
   │   └── enable-crun-master.yaml
   ├── kustomization.yaml
   ```

   3

   ```
   ├── pre-reqs/
   │   └── sno1/
   │       ├── bmc-credentials.yaml
   │       ├── namespace.yaml
   │       └── pull-secret.yaml
   ├── kustomization.yaml
   ├── reference-manifest/
   │   └── 4.22/
   └── resources/
       ├── active-ocp-version.yaml
       └── kustomization.yaml
   ```

   [1](#CO4-1)
   :   This `ClusterInstance` CR for the `sno1` cluster.

   [2](#CO4-2)
   :   The tool automatically generates the extra manifests referenced by the `ClusterInstance` CR.

   [3](#CO4-3)
   :   The tool generates a `kuztomization.yaml` file snippet to create the `ConfigMap` resources that specifies the extra manifests. You can merge the generated `kustomization` snippet with your original `kuztomization.yaml` file.

#### [6.4.1. Reference flags for the siteconfig-converter tool](#ztp-site_converter-ref_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

The following matrix describes the flags for the `siteconfig-converter` tool.

Expand

| Flag | Type | Description |
| --- | --- | --- |
| -d | string | Define the output directory for the converted `ClusterInstance` custom resources (CRs). This flag is required. |
| -t | string | Define a comma-separated list of template references for clusters in namespace/name format. The default value is `open-cluster-management/ai-cluster-templates-v1`. |
| -n | string | Define a comma-separated list of template references for nodes in namespace/name format. The default value is `open-cluster-management/ai-node-templates-v1`. |
| -m | string | Define a comma-separated list of `ConfigMap` names to use for extra manifests references. |
| -s | string | Define a comma-separated list of manifest names to suppress at the cluster level. |
| -w | boolean | Write conversion warnings as comments to the head of the converted YAML files. The default value is `false`. |
| -c | boolean | Copy comments from the original `SiteConfig` CRs to the converted `ClusterInstance` CRs. The default is false. |

Show more

### [6.5. Deleting the Argo CD pipeline post-migration](#ztp-clusterinstance-cleanup_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

After you migrate all single-node OpenShift clusters from using `SiteConfig` CRs to `ClusterInstance` CRs, you can delete the original Argo CD application and related resources that managed the `SiteConfig` CRs.

Note

Only delete the Argo CD application and related resources after you have confirmed that all clusters are successfully managed by the new Argo CD application that uses `ClusterInstance` CRs. Additionally, if the Argo CD project was only used for the migrated cluster’s Argo application, you can also delete this project.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* All single-node OpenShift clusters have been successfully migrated to use `ClusterInstance` CRs and are managed by another Argo CD application.

**Procedure**

1. Delete the original Argo CD application that managed the `SiteConfig` CRs:

   ```
   $ oc delete application.argo clusters -n openshift-gitops
   ```

   * Replace `clusters` with the name of your original Argo CD application.
2. Delete the original Argo CD project by running the following command:

   ```
   $ oc delete appproject ztp-app-project -n openshift-gitops
   ```

   * Replace `ztp-app-project` with the name of your original Argo CD project.

**Verification**

1. Confirm that the original Argo CD application is deleted by running the following command:

   ```
   $ oc get appproject -n openshift-gitops
   ```

   **Example output**

   ```
   NAME                 AGE
   default              6d20h
   policy-app-project   2d22h
   ztpv2-app-project    44h
   ```

   * The original Argo CD project in this example, `ztp-app-project` is not present in the output.
2. Confirm that the original Argo CD project is deleted by running the following command:

   ```
   oc get applications.argo -n openshift-gitops
   ```

   **Example output**

   ```
   NAME                       SYNC STATUS   HEALTH STATUS
   clusters-v2                Synced        Healthy
   policies                   Synced        Healthy
   ```

   * The original Argo CD application in this example, `clusters` is not present in the output.

### [6.6. Troubleshooting the migration to ClusterInstance CRs](#ztp-clusterinstance-troubleshooting_ztp-migrate-clusterinstance) Copy linkLink copied to clipboard!

Consider the following troubleshooting steps if you encounter issues during the migration from `SiteConfig` CRs to `ClusterInstance` CRs.

**Procedure**

* Verify that the SiteConfig Operator rendered all the required deployment resources by running the following command:

  ```
  $ oc -n <target_cluster> get clusterinstances <target_cluster> -ojson | jq .status.manifestsRendered
  ```

  **Example output**

  ```
  [
    {
      "apiGroup": "extensions.hive.openshift.io/v1beta1",
      "kind": "AgentClusterInstall",
      "lastAppliedTime": "2025-01-13T11:10:52Z",
      "name": "sno1",
      "namespace": "sno1",
      "status": "rendered",
      "syncWave": 1
    },
    {
      "apiGroup": "metal3.io/v1alpha1",
      "kind": "BareMetalHost",
      "lastAppliedTime": "2025-01-13T11:10:53Z",
      "name": "sno1.example.com",
      "namespace": "sno1",
      "status": "rendered",
      "syncWave": 1
    },
    {
      "apiGroup": "hive.openshift.io/v1",
      "kind": "ClusterDeployment",
      "lastAppliedTime": "2025-01-13T11:10:53Z",
      "name": "sno1",
      "namespace": "sno1",
      "status": "rendered",
      "syncWave": 1
    },
    {
      "apiGroup": "agent-install.openshift.io/v1beta1",
      "kind": "InfraEnv",
      "lastAppliedTime": "2025-01-13T11:10:53Z",
      "name": "sno1",
      "namespace": "sno1",
      "status": "rendered",
      "syncWave": 1
    },
    {
      "apiGroup": "agent-install.openshift.io/v1beta1",
      "kind": "NMStateConfig",
      "lastAppliedTime": "2025-01-13T11:10:53Z",
      "name": "sno1.example.com",
      "namespace": "sno1",
      "status": "rendered",
      "syncWave": 1
    },
    {
      "apiGroup": "agent.open-cluster-management.io/v1",
      "kind": "KlusterletAddonConfig",
      "lastAppliedTime": "2025-01-13T11:10:53Z",
      "name": "sno1",
      "namespace": "sno1",
      "status": "rendered",
      "syncWave": 2
    },
    {
      "apiGroup": "cluster.open-cluster-management.io/v1",
      "kind": "ManagedCluster",
      "lastAppliedTime": "2025-01-13T11:10:53Z",
      "name": "sno1",
      "status": "rendered",
      "syncWave": 2
    }
  ]
  ```

## [Chapter 7. Recommended single-node OpenShift cluster configuration for vDU application workloads](#sno-configure-for-vdu) Copy linkLink copied to clipboard!

Use the following reference information to understand the single-node OpenShift configurations required to deploy virtual distributed unit (vDU) applications in the cluster. Configurations include cluster optimizations for high performance workloads, enabling workload partitioning, and minimizing the number of reboots required postinstallation.

### [7.1. Running low latency applications on OpenShift Container Platform](#ztp-low-latency_sno-configure-for-vdu) Copy linkLink copied to clipboard!

OpenShift Container Platform enables low latency processing for applications running on commercial off-the-shelf (COTS) hardware by using several technologies and specialized hardware devices:

Real-time kernel for RHCOS
:   Ensures workloads are handled with a high degree of process determinism.

CPU isolation
:   Avoids CPU scheduling delays and ensures CPU capacity is available consistently.

NUMA-aware topology management
:   Aligns memory and huge pages with CPU and PCI devices to pin guaranteed container memory and huge pages to the non-uniform memory access (NUMA) node. Pod resources for all Quality of Service (QoS) classes stay on the same NUMA node. This decreases latency and improves performance of the node.

Huge pages memory management
:   Using huge page sizes improves system performance by reducing the amount of system resources required to access page tables.

Precision timing synchronization using PTP
:   Allows synchronization between nodes in the network with sub-microsecond accuracy.

### [7.2. Recommended cluster host requirements for vDU application workloads](#ztp-install-sno-hardware-reqs_sno-configure-for-vdu) Copy linkLink copied to clipboard!

Running vDU application workloads requires a bare-metal host with sufficient resources to run OpenShift Container Platform services and production workloads.

Expand

Table 7.1. Minimum resource requirements

| Profile | vCPU | Memory | Storage |
| --- | --- | --- | --- |
| Minimum | 4 vCPU | 32 GB of RAM | 120 GB |
| Recommended | 8 vCPU | 32 GB of RAM | 120 GB |

Show more

Important

Running single-node OpenShift on 4 vCPUs leaves very little headroom for vDU application workloads. With all cluster capabilities enabled, the platform alone can request over 2.5 vCPUs and consume over 2 vCPUs at idle, leaving minimal capacity for application workloads.

To run on 4 vCPUs, you must minimize the cluster resource footprint:

* Set `baselineCapabilitySet` to `None` in the `install-config.yaml` file and use `additionalEnabledCapabilities` to enable only the capabilities that your workload requires, such as `Storage`, `Console`, and `Ingress`. For more information, see "Cluster capabilities".
* Use a performance profile to partition CPU resources between cluster housekeeping duties and application workloads, ensuring that your vDU containers run on isolated CPUs with minimal interruption. For more information, see "Tuning nodes for low latency with the performance profile".

If your deployment does not require these optimizations, it is recommended to use at least 8 vCPUs..

Note

One vCPU equals one physical core. However, if you enable simultaneous multithreading (SMT), or Hyper-Threading, use the following formula to calculate the number of vCPUs that represent one physical core:

* (threads per core × cores) × sockets = vCPUs

Important

The server must have a Baseboard Management Controller (BMC) when booting with virtual media.

### [7.3. Configuring host firmware for low latency and high performance](#ztp-du-configuring-host-firmware-requirements_sno-configure-for-vdu) Copy linkLink copied to clipboard!

Bare-metal hosts require the firmware to be configured before the host can be provisioned. The firmware configuration is dependent on the specific hardware and the particular requirements of your installation.

**Procedure**

1. Set the **UEFI/BIOS Boot Mode** to `UEFI`.
2. In the host boot sequence order, set **Hard drive first**.
3. Apply the specific firmware configuration for your hardware. The following table describes a representative firmware configuration for an Intel Xeon Skylake server and later hardware generations, based on the Intel FlexRAN 4G and 5G baseband PHY reference design.

   Important

   The exact firmware configuration depends on your specific hardware and network requirements. The following sample configuration is for illustrative purposes only.

   Expand

   Table 7.2. Sample firmware configuration

   | Firmware setting | Configuration |
   | --- | --- |
   | CPU Power and Performance Policy | Performance |
   | Uncore Frequency Scaling | Disabled |
   | Performance P-limit | Disabled |
   | Enhanced Intel SpeedStep ® Tech | Enabled |
   | Intel Configurable TDP | Enabled |
   | Configurable TDP Level | Level 2 |
   | Intel® Turbo Boost Technology | Enabled |
   | Energy Efficient Turbo | Disabled |
   | Hardware P-States | Disabled |
   | Package C-State | C0/C1 state |
   | C1E | Disabled |
   | Processor C6 | Disabled |

   Show more

   Note

   Enable global SR-IOV and VT-d settings in the firmware for the host. These settings are relevant to bare-metal environments.

### [7.4. Connectivity prerequisites for managed cluster networks](#ztp-managed-cluster-network-prereqs_sno-configure-for-vdu) Copy linkLink copied to clipboard!

Before you can install and provision a managed cluster with the GitOps Zero Touch Provisioning (ZTP) pipeline, the managed cluster host must meet the following networking prerequisites:

* There must be bi-directional connectivity between the GitOps ZTP container in the hub cluster and the Baseboard Management Controller (BMC) of the target bare-metal host.
* The managed cluster must be able to resolve and reach the API hostname of the hub hostname and `*.apps` hostname. Here is an example of the API hostname of the hub and `*.apps` hostname:

  + `api.hub-cluster.internal.domain.com`
  + `console-openshift-console.apps.hub-cluster.internal.domain.com`
* The hub cluster must be able to resolve and reach the API and `*.apps` hostname of the managed cluster. Here is an example of the API hostname of the managed cluster and `*.apps` hostname:

  + `api.sno-managed-cluster-1.internal.domain.com`
  + `console-openshift-console.apps.sno-managed-cluster-1.internal.domain.com`

### [7.5. Workload partitioning in single-node OpenShift with GitOps ZTP](#ztp-workload-partitioning-sno_sno-configure-for-vdu) Copy linkLink copied to clipboard!

Workload partitioning configures OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved number of host CPUs.

To configure workload partitioning with GitOps Zero Touch Provisioning (ZTP), you configure a `cpuPartitioningMode` field in the `ClusterInstance` custom resource (CR) that you use to install the cluster and you apply a `PerformanceProfile` CR that configures the `isolated` and `reserved` CPUs on the host.

Configuring the `ClusterInstance` CR enables workload partitioning at cluster installation time and applying the `PerformanceProfile` CR configures the specific allocation of CPUs to reserved and isolated sets. Both of these steps happen at different points during cluster provisioning.

The workload partitioning configuration pins the OpenShift Container Platform infrastructure pods to the `reserved` CPU set. Platform services such as systemd, CRI-O, and kubelet run on the `reserved` CPU set. The `isolated` CPU sets are exclusively allocated to your container workloads. Isolating CPUs ensures that the workload has guaranteed access to the specified CPUs without contention from other applications running on the same node. All CPUs that are not isolated should be reserved.

Important

Ensure that `reserved` and `isolated` CPU sets do not overlap with each other.

### [7.6. Recommended cluster install manifests](#ztp-sno-install-time-cluster-config_sno-configure-for-vdu) Copy linkLink copied to clipboard!

The ZTP pipeline applies the following custom resources (CRs) during cluster installation. These configuration CRs ensure that the cluster meets the feature and performance requirements necessary for running a vDU application.

Note

When using the GitOps ZTP plugin and `ClusterInstance` CRs for cluster deployment, the following `MachineConfig` CRs are included by default.

Use the `ClusterInstance` `extraManifestRefs` to alter the CRs that are included by default. For more information, see "Advanced managed cluster configuration with ClusterInstance CRs".

#### [7.6.1. Reduced platform management footprint](#ztp-sno-du-configuring-the-container-mountspace_sno-configure-for-vdu) Copy linkLink copied to clipboard!

To reduce the overall management footprint of the platform, a `MachineConfig` custom resource (CR) is required that places all Kubernetes-specific mount points in a new namespace separate from the host operating system. The following base64-encoded example `MachineConfig` CR illustrates this configuration.

**Recommended container mount namespace configuration (`01-container-mount-ns-and-kubelet-conf-master.yaml`)**

```
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: container-mount-namespace-and-kubelet-conf-master
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
        - contents:
            source: data:text/plain;charset=utf-8;base64,IyEvYmluL2Jhc2gKCmRlYnVnKCkgewogIGVjaG8gJEAgPiYyCn0KCnVzYWdlKCkgewogIGVjaG8gVXNhZ2U6ICQoYmFzZW5hbWUgJDApIFVOSVQgW2VudmZpbGUgW3Zhcm5hbWVdXQogIGVjaG8KICBlY2hvIEV4dHJhY3QgdGhlIGNvbnRlbnRzIG9mIHRoZSBmaXJzdCBFeGVjU3RhcnQgc3RhbnphIGZyb20gdGhlIGdpdmVuIHN5c3RlbWQgdW5pdCBhbmQgcmV0dXJuIGl0IHRvIHN0ZG91dAogIGVjaG8KICBlY2hvICJJZiAnZW52ZmlsZScgaXMgcHJvdmlkZWQsIHB1dCBpdCBpbiB0aGVyZSBpbnN0ZWFkLCBhcyBhbiBlbnZpcm9ubWVudCB2YXJpYWJsZSBuYW1lZCAndmFybmFtZSciCiAgZWNobyAiRGVmYXVsdCAndmFybmFtZScgaXMgRVhFQ1NUQVJUIGlmIG5vdCBzcGVjaWZpZWQiCiAgZXhpdCAxCn0KClVOSVQ9JDEKRU5WRklMRT0kMgpWQVJOQU1FPSQzCmlmIFtbIC16ICRVTklUIHx8ICRVTklUID09ICItLWhlbHAiIHx8ICRVTklUID09ICItaCIgXV07IHRoZW4KICB1c2FnZQpmaQpkZWJ1ZyAiRXh0cmFjdGluZyBFeGVjU3RhcnQgZnJvbSAkVU5JVCIKRklMRT0kKHN5c3RlbWN0bCBjYXQgJFVOSVQgfCBoZWFkIC1uIDEpCkZJTEU9JHtGSUxFI1wjIH0KaWYgW1sgISAtZiAkRklMRSBdXTsgdGhlbgogIGRlYnVnICJGYWlsZWQgdG8gZmluZCByb290IGZpbGUgZm9yIHVuaXQgJFVOSVQgKCRGSUxFKSIKICBleGl0CmZpCmRlYnVnICJTZXJ2aWNlIGRlZmluaXRpb24gaXMgaW4gJEZJTEUiCkVYRUNTVEFSVD0kKHNlZCAtbiAtZSAnL15FeGVjU3RhcnQ9LipcXCQvLC9bXlxcXSQvIHsgcy9eRXhlY1N0YXJ0PS8vOyBwIH0nIC1lICcvXkV4ZWNTdGFydD0uKlteXFxdJC8geyBzL15FeGVjU3RhcnQ9Ly87IHAgfScgJEZJTEUpCgppZiBbWyAkRU5WRklMRSBdXTsgdGhlbgogIFZBUk5BTUU9JHtWQVJOQU1FOi1FWEVDU1RBUlR9CiAgZWNobyAiJHtWQVJOQU1FfT0ke0VYRUNTVEFSVH0iID4gJEVOVkZJTEUKZWxzZQogIGVjaG8gJEVYRUNTVEFSVApmaQo=
          mode: 493
          path: /usr/local/bin/extractExecStart
        - contents:
            source: data:text/plain;charset=utf-8;base64,IyEvYmluL2Jhc2gKbnNlbnRlciAtLW1vdW50PS9ydW4vY29udGFpbmVyLW1vdW50LW5hbWVzcGFjZS9tbnQgIiRAIgo=
          mode: 493
          path: /usr/local/bin/nsenterCmns
    systemd:
      units:
        - contents: |
            [Unit]
            Description=Manages a mount namespace that both kubelet and crio can use to share their container-specific mounts

            [Service]
            Type=oneshot
            RemainAfterExit=yes
            RuntimeDirectory=container-mount-namespace
            Environment=RUNTIME_DIRECTORY=%t/container-mount-namespace
            Environment=BIND_POINT=%t/container-mount-namespace/mnt
            ExecStartPre=bash -c "findmnt ${RUNTIME_DIRECTORY} || mount --make-unbindable --bind ${RUNTIME_DIRECTORY} ${RUNTIME_DIRECTORY}"
            ExecStartPre=touch ${BIND_POINT}
            ExecStart=unshare --mount=${BIND_POINT} --propagation slave mount --make-rshared /
            ExecStop=umount -R ${RUNTIME_DIRECTORY}
          name: container-mount-namespace.service
        - dropins:
            - contents: |
                [Unit]
                Wants=container-mount-namespace.service
                After=container-mount-namespace.service

                [Service]
                ExecStartPre=/usr/local/bin/extractExecStart %n /%t/%N-execstart.env ORIG_EXECSTART
                EnvironmentFile=-/%t/%N-execstart.env
                ExecStart=
                ExecStart=bash -c "nsenter --mount=%t/container-mount-namespace/mnt \
                    ${ORIG_EXECSTART}"
              name: 90-container-mount-namespace.conf
          name: crio.service
        - dropins:
            - contents: |
                [Unit]
                Wants=container-mount-namespace.service
                After=container-mount-namespace.service

                [Service]
                ExecStartPre=/usr/local/bin/extractExecStart %n /%t/%N-execstart.env ORIG_EXECSTART
                EnvironmentFile=-/%t/%N-execstart.env
                ExecStart=
                ExecStart=bash -c "nsenter --mount=%t/container-mount-namespace/mnt \
                    ${ORIG_EXECSTART} --housekeeping-interval=30s"
              name: 90-container-mount-namespace.conf
            - contents: |
                [Service]
                Environment="OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION=60s"
                Environment="OPENSHIFT_EVICTION_MONITORING_PERIOD_DURATION=30s"
              name: 30-kubelet-interval-tuning.conf
          name: kubelet.service
```

#### [7.6.2. SCTP](#ztp-sno-du-enabling-sctp_sno-configure-for-vdu) Copy linkLink copied to clipboard!

Stream Control Transmission Protocol (SCTP) is a key protocol used in RAN applications. This `MachineConfig` object adds the SCTP kernel module to the node to enable this protocol.

**Recommended control plane node SCTP configuration (`03-sctp-machine-config-master.yaml`)**

```
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: load-sctp-module-master
spec:
  config:
    ignition:
      version: 2.2.0
    storage:
      files:
        - contents:
            source: data:,
            verification: {}
          filesystem: root
          mode: 420
          path: /etc/modprobe.d/sctp-blacklist.conf
        - contents:
            source: data:text/plain;charset=utf-8,sctp
          filesystem: root
          mode: 420
          path: /etc/modules-load.d/sctp-load.conf
```

**Recommended worker node SCTP configuration (`03-sctp-machine-config-worker.yaml`)**

```
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: load-sctp-module-worker
spec:
  config:
    ignition:
      version: 2.2.0
    storage:
      files:
        - contents:
            source: data:,
            verification: {}
          filesystem: root
          mode: 420
          path: /etc/modprobe.d/sctp-blacklist.conf
        - contents:
            source: data:text/plain;charset=utf-8,sctp
          filesystem: root
          mode: 420
          path: /etc/modules-load.d/sctp-load.conf
```

#### [7.6.3. Setting rcu\_normal](#ztp-setting-rcu-normal_sno-configure-for-vdu) Copy linkLink copied to clipboard!

The following `MachineConfig` CR configures the system to set `rcu_normal` to 1 after the system has finished startup. This improves kernel latency for vDU applications.

**Recommended configuration for disabling `rcu_expedited` after the node has finished startup (`08-set-rcu-normal-master.yaml`)**

```
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 08-set-rcu-normal-master
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
        - contents:
            source: data:text/plain;charset=utf-8;base64,IyEvYmluL2Jhc2gKIwojIERpc2FibGUgcmN1X2V4cGVkaXRlZCBhZnRlciBub2RlIGhhcyBmaW5pc2hlZCBib290aW5nCiMKIyBUaGUgZGVmYXVsdHMgYmVsb3cgY2FuIGJlIG92ZXJyaWRkZW4gdmlhIGVudmlyb25tZW50IHZhcmlhYmxlcwojCgojIERlZmF1bHQgd2FpdCB0aW1lIGlzIDYwMHMgPSAxMG06Ck1BWElNVU1fV0FJVF9USU1FPSR7TUFYSU1VTV9XQUlUX1RJTUU6LTYwMH0KCiMgRGVmYXVsdCBzdGVhZHktc3RhdGUgdGhyZXNob2xkID0gMiUKIyBBbGxvd2VkIHZhbHVlczoKIyAgNCAgLSBhYnNvbHV0ZSBwb2QgY291bnQgKCsvLSkKIyAgNCUgLSBwZXJjZW50IGNoYW5nZSAoKy8tKQojICAtMSAtIGRpc2FibGUgdGhlIHN0ZWFkeS1zdGF0ZSBjaGVjawpTVEVBRFlfU1RBVEVfVEhSRVNIT0xEPSR7U1RFQURZX1NUQVRFX1RIUkVTSE9MRDotMiV9CgojIERlZmF1bHQgc3RlYWR5LXN0YXRlIHdpbmRvdyA9IDYwcwojIElmIHRoZSBydW5uaW5nIHBvZCBjb3VudCBzdGF5cyB3aXRoaW4gdGhlIGdpdmVuIHRocmVzaG9sZCBmb3IgdGhpcyB0aW1lCiMgcGVyaW9kLCByZXR1cm4gQ1BVIHV0aWxpemF0aW9uIHRvIG5vcm1hbCBiZWZvcmUgdGhlIG1heGltdW0gd2FpdCB0aW1lIGhhcwojIGV4cGlyZXMKU1RFQURZX1NUQVRFX1dJTkRPVz0ke1NURUFEWV9TVEFURV9XSU5ET1c6LTYwfQoKIyBEZWZhdWx0IHN0ZWFkeS1zdGF0ZSBhbGxvd3MgYW55IHBvZCBjb3VudCB0byBiZSAic3RlYWR5IHN0YXRlIgojIEluY3JlYXNpbmcgdGhpcyB3aWxsIHNraXAgYW55IHN0ZWFkeS1zdGF0ZSBjaGVja3MgdW50aWwgdGhlIGNvdW50IHJpc2VzIGFib3ZlCiMgdGhpcyBudW1iZXIgdG8gYXZvaWQgZmFsc2UgcG9zaXRpdmVzIGlmIHRoZXJlIGFyZSBzb21lIHBlcmlvZHMgd2hlcmUgdGhlCiMgY291bnQgZG9lc24ndCBpbmNyZWFzZSBidXQgd2Uga25vdyB3ZSBjYW4ndCBiZSBhdCBzdGVhZHktc3RhdGUgeWV0LgpTVEVBRFlfU1RBVEVfTUlOSU1VTT0ke1NURUFEWV9TVEFURV9NSU5JTVVNOi0wfQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKd2l0aGluKCkgewogIGxvY2FsIGxhc3Q9JDEgY3VycmVudD0kMiB0aHJlc2hvbGQ9JDMKICBsb2NhbCBkZWx0YT0wIHBjaGFuZ2UKICBkZWx0YT0kKCggY3VycmVudCAtIGxhc3QgKSkKICBpZiBbWyAkY3VycmVudCAtZXEgJGxhc3QgXV07IHRoZW4KICAgIHBjaGFuZ2U9MAogIGVsaWYgW1sgJGxhc3QgLWVxIDAgXV07IHRoZW4KICAgIHBjaGFuZ2U9MTAwMDAwMAogIGVsc2UKICAgIHBjaGFuZ2U9JCgoICggIiRkZWx0YSIgKiAxMDApIC8gbGFzdCApKQogIGZpCiAgZWNobyAtbiAibGFzdDokbGFzdCBjdXJyZW50OiRjdXJyZW50IGRlbHRhOiRkZWx0YSBwY2hhbmdlOiR7cGNoYW5nZX0lOiAiCiAgbG9jYWwgYWJzb2x1dGUgbGltaXQKICBjYXNlICR0aHJlc2hvbGQgaW4KICAgIColKQogICAgICBhYnNvbHV0ZT0ke3BjaGFuZ2UjIy19ICMgYWJzb2x1dGUgdmFsdWUKICAgICAgbGltaXQ9JHt0aHJlc2hvbGQlJSV9CiAgICAgIDs7CiAgICAqKQogICAgICBhYnNvbHV0ZT0ke2RlbHRhIyMtfSAjIGFic29sdXRlIHZhbHVlCiAgICAgIGxpbWl0PSR0aHJlc2hvbGQKICAgICAgOzsKICBlc2FjCiAgaWYgW1sgJGFic29sdXRlIC1sZSAkbGltaXQgXV07IHRoZW4KICAgIGVjaG8gIndpdGhpbiAoKy8tKSR0aHJlc2hvbGQiCiAgICByZXR1cm4gMAogIGVsc2UKICAgIGVjaG8gIm91dHNpZGUgKCsvLSkkdGhyZXNob2xkIgogICAgcmV0dXJuIDEKICBmaQp9CgpzdGVhZHlzdGF0ZSgpIHsKICBsb2NhbCBsYXN0PSQxIGN1cnJlbnQ9JDIKICBpZiBbWyAkbGFzdCAtbHQgJFNURUFEWV9TVEFURV9NSU5JTVVNIF1dOyB0aGVuCiAgICBlY2hvICJsYXN0OiRsYXN0IGN1cnJlbnQ6JGN1cnJlbnQgV2FpdGluZyB0byByZWFjaCAkU1RFQURZX1NUQVRFX01JTklNVU0gYmVmb3JlIGNoZWNraW5nIGZvciBzdGVhZHktc3RhdGUiCiAgICByZXR1cm4gMQogIGZpCiAgd2l0aGluICIkbGFzdCIgIiRjdXJyZW50IiAiJFNURUFEWV9TVEFURV9USFJFU0hPTEQiCn0KCndhaXRGb3JSZWFkeSgpIHsKICBsb2dnZXIgIlJlY292ZXJ5OiBXYWl0aW5nICR7TUFYSU1VTV9XQUlUX1RJTUV9cyBmb3IgdGhlIGluaXRpYWxpemF0aW9uIHRvIGNvbXBsZXRlIgogIGxvY2FsIHQ9MCBzPTEwCiAgbG9jYWwgbGFzdENjb3VudD0wIGNjb3VudD0wIHN0ZWFkeVN0YXRlVGltZT0wCiAgd2hpbGUgW1sgJHQgLWx0ICRNQVhJTVVNX1dBSVRfVElNRSBdXTsgZG8KICAgIHNsZWVwICRzCiAgICAoKHQgKz0gcykpCiAgICAjIERldGVjdCBzdGVhZHktc3RhdGUgcG9kIGNvdW50CiAgICBjY291bnQ9JChjcmljdGwgcHMgMj4vZGV2L251bGwgfCB3YyAtbCkKICAgIGlmIFtbICRjY291bnQgLWd0IDAgXV0gJiYgc3RlYWR5c3RhdGUgIiRsYXN0Q2NvdW50IiAiJGNjb3VudCI7IHRoZW4KICAgICAgKChzdGVhZHlTdGF0ZVRpbWUgKz0gcykpCiAgICAgIGVjaG8gIlN0ZWFkeS1zdGF0ZSBmb3IgJHtzdGVhZHlTdGF0ZVRpbWV9cy8ke1NURUFEWV9TVEFURV9XSU5ET1d9cyIKICAgICAgaWYgW1sgJHN0ZWFkeVN0YXRlVGltZSAtZ2UgJFNURUFEWV9TVEFURV9XSU5ET1cgXV07IHRoZW4KICAgICAgICBsb2dnZXIgIlJlY292ZXJ5OiBTdGVhZHktc3RhdGUgKCsvLSAkU1RFQURZX1NUQVRFX1RIUkVTSE9MRCkgZm9yICR7U1RFQURZX1NUQVRFX1dJTkRPV31zOiBEb25lIgogICAgICAgIHJldHVybiAwCiAgICAgIGZpCiAgICBlbHNlCiAgICAgIGlmIFtbICRzdGVhZHlTdGF0ZVRpbWUgLWd0IDAgXV07IHRoZW4KICAgICAgICBlY2hvICJSZXNldHRpbmcgc3RlYWR5LXN0YXRlIHRpbWVyIgogICAgICAgIHN0ZWFkeVN0YXRlVGltZT0wCiAgICAgIGZpCiAgICBmaQogICAgbGFzdENjb3VudD0kY2NvdW50CiAgZG9uZQogIGxvZ2dlciAiUmVjb3Zlcnk6IFJlY292ZXJ5IENvbXBsZXRlIFRpbWVvdXQiCn0KCnNldFJjdU5vcm1hbCgpIHsKICBlY2hvICJTZXR0aW5nIHJjdV9ub3JtYWwgdG8gMSIKICBlY2hvIDEgPiAvc3lzL2tlcm5lbC9yY3Vfbm9ybWFsCn0KCm1haW4oKSB7CiAgd2FpdEZvclJlYWR5CiAgZWNobyAiV2FpdGluZyBmb3Igc3RlYWR5IHN0YXRlIHRvb2s6ICQoYXdrICd7cHJpbnQgaW50KCQxLzM2MDApImgiLCBpbnQoKCQxJTM2MDApLzYwKSJtIiwgaW50KCQxJTYwKSJzIn0nIC9wcm9jL3VwdGltZSkiCiAgc2V0UmN1Tm9ybWFsCn0KCmlmIFtbICIke0JBU0hfU09VUkNFWzBdfSIgPSAiJHswfSIgXV07IHRoZW4KICBtYWluICIke0B9IgogIGV4aXQgJD8KZmkK
          mode: 493
          path: /usr/local/bin/set-rcu-normal.sh
    systemd:
      units:
        - contents: |
            [Unit]
            Description=Disable rcu_expedited after node has finished booting by setting rcu_normal to 1

            [Service]
            Type=simple
            ExecStart=/usr/local/bin/set-rcu-normal.sh

            # Maximum wait time is 600s = 10m:
            Environment=MAXIMUM_WAIT_TIME=600

            # Steady-state threshold = 2%
            # Allowed values:
            #  4  - absolute pod count (+/-)
            #  4% - percent change (+/-)
            #  -1 - disable the steady-state check
            # Note: '%' must be escaped as '%%' in systemd unit files
            Environment=STEADY_STATE_THRESHOLD=2%%

            # Steady-state window = 120s
            # If the running pod count stays within the given threshold for this time
            # period, return CPU utilization to normal before the maximum wait time has
            # expires
            Environment=STEADY_STATE_WINDOW=120

            # Steady-state minimum = 40
            # Increasing this will skip any steady-state checks until the count rises above
            # this number to avoid false positives if there are some periods where the
            # count doesn't increase but we know we can't be at steady-state yet.
            Environment=STEADY_STATE_MINIMUM=40

            [Install]
            WantedBy=multi-user.target
          enabled: true
          name: set-rcu-normal.service
```

#### [7.6.4. Automatic kernel crash dumps with kdump](#ztp-sno-du-enabling-kdump_sno-configure-for-vdu) Copy linkLink copied to clipboard!

`kdump` is a Linux kernel feature that creates a kernel crash dump when the kernel crashes. You can use the crash dump to debug and find the cause of the kernel crash. To enable `kdump`, you apply `MachineConfig` custom resources (CRs) that reserve memory for the crash kernel and enable the `kdump` systemd service. The `ztp-site-generate` container provides the following reference CRs for this configuration:

* `06-kdump-master.yaml` for control plane nodes
* `06-kdump-worker.yaml` for worker nodes

Note

Use the reference `MachineConfig` CRs from the `ztp-site-generate` container image as the source of truth for kdump configuration values. You can extract the CRs from the container image and find them in the `out/source-crs/extra-manifest/` folder.

#### [7.6.5. Disable automatic CRI-O cache wipe](#ztp-sno-du-disabling-crio-wipe_sno-configure-for-vdu) Copy linkLink copied to clipboard!

After an uncontrolled host shutdown or cluster reboot, CRI-O automatically deletes the entire CRI-O cache, causing all images to be pulled from the registry when the node reboots. This can result in unacceptably slow recovery times or recovery failures. To prevent this from happening in single-node OpenShift clusters that you install with GitOps ZTP, disable the CRI-O delete cache feature during cluster installation.

**Recommended `MachineConfig` CR to disable CRI-O cache wipe on control plane nodes (`99-crio-disable-wipe-master.yaml`)**

```
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-crio-disable-wipe-master
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
        - contents:
            source: data:text/plain;charset=utf-8;base64,W2NyaW9dCmNsZWFuX3NodXRkb3duX2ZpbGUgPSAiIgo=
          mode: 420
          path: /etc/crio/crio.conf.d/99-crio-disable-wipe.toml
```

**Recommended `MachineConfig` CR to disable CRI-O cache wipe on worker nodes (`99-crio-disable-wipe-worker.yaml`)**

```
# Automatically generated by extra-manifests-builder
# Do not make changes directly.
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-crio-disable-wipe-worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
        - contents:
            source: data:text/plain;charset=utf-8;base64,W2NyaW9dCmNsZWFuX3NodXRkb3duX2ZpbGUgPSAiIgo=
          mode: 420
          path: /etc/crio/crio.conf.d/99-crio-disable-wipe.toml
```

#### [7.6.6. Configuring crun as the default container runtime](#ztp-sno-du-configuring-crun-container-runtime_sno-configure-for-vdu) Copy linkLink copied to clipboard!

The following `ContainerRuntimeConfig` custom resources (CRs) configure crun as the default OCI container runtime for control plane and worker nodes. The crun container runtime is fast and lightweight and has a low memory footprint.

Important

For optimal performance, enable crun for control plane and worker nodes in single-node OpenShift, three-node OpenShift, and standard clusters. To avoid the cluster rebooting when the CR is applied, apply the change as a GitOps ZTP additional Day 0 install-time manifest.

**Recommended `ContainerRuntimeConfig` CR for control plane nodes (`enable-crun-master.yaml`)**

```
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
  name: enable-crun-master
spec:
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/master: ""
  containerRuntimeConfig:
    defaultRuntime: crun
```

**Recommended `ContainerRuntimeConfig` CR for worker nodes (`enable-crun-worker.yaml`)**

```
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
  name: enable-crun-worker
spec:
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: ""
  containerRuntimeConfig:
    defaultRuntime: crun
```

## [Chapter 8. Validating single-node OpenShift cluster tuning for vDU application workloads](#ztp-vdu-configuration-reference) Copy linkLink copied to clipboard!

Before you can deploy virtual distributed unit (vDU) applications, you need to tune and configure the cluster host firmware and various other cluster configuration settings. Use the following information to validate the cluster configuration to support vDU workloads.

### [8.1. Recommended firmware configuration for vDU cluster hosts](#ztp-du-firmware-config-reference_vdu-config-ref) Copy linkLink copied to clipboard!

Use the following table as the basis to configure the cluster host firmware for vDU applications running on OpenShift Container Platform 4.22.

Note

The following table is a general recommendation for vDU cluster host firmware configuration. Exact firmware settings will depend on your requirements and specific hardware platform. Automatic setting of firmware is not handled by the zero touch provisioning pipeline.

Expand

Table 8.1. Recommended cluster host firmware settings

| Firmware setting | Configuration | Description |
| --- | --- | --- |
| HyperTransport (HT) | Enabled | HyperTransport (HT) bus is a bus technology developed by AMD. HT provides a high-speed link between the components in the host memory and other system peripherals. |
| UEFI | Enabled | Enable booting from UEFI for the vDU host. |
| CPU Power and Performance Policy | Performance | Set CPU Power and Performance Policy to optimize the system for performance over energy efficiency. |
| Uncore Frequency Scaling | Disabled | Disable Uncore Frequency Scaling to prevent the voltage and frequency of non-core parts of the CPU from being set independently. |
| Uncore Frequency | Maximum | Sets the non-core parts of the CPU such as cache and memory controller to their maximum possible frequency of operation. |
| Performance P-limit | Disabled | Disable Performance P-limit to prevent the Uncore frequency coordination of processors. |
| Enhanced Intel® SpeedStep Tech | Enabled | Enable Enhanced Intel SpeedStep to allow the system to dynamically adjust processor voltage and core frequency that decreases power consumption and heat production in the host. |
| Intel® Turbo Boost Technology | Enabled | Enable Turbo Boost Technology for Intel-based CPUs to automatically allow processor cores to run faster than the rated operating frequency if they are operating below power, current, and temperature specification limits. |
| Intel Configurable TDP | Enabled | Enables Thermal Design Power (TDP) for the CPU. |
| Configurable TDP Level | Level 2 | TDP level sets the CPU power consumption required for a particular performance rating. TDP level 2 sets the CPU to the most stable performance level at the cost of power consumption. |
| Energy Efficient Turbo | Disabled | Disable Energy Efficient Turbo to prevent the processor from using an energy-efficiency based policy. |
| Hardware P-States | Enabled or Disabled | Enable OS-controlled P-States to allow power saving configurations. Disable `P-states` (performance states) to optimize the operating system and CPU for performance over power consumption. |
| Package C-State | C0/C1 state | Use C0 or C1 states to set the processor to a fully active state (C0) or to stop CPU internal clocks running in software (C1). |
| C1E | Disabled | CPU Enhanced Halt (C1E) is a power saving feature in Intel chips. Disabling C1E prevents the operating system from sending a halt command to the CPU when inactive. |
| Processor C6 | Disabled | C6 power-saving is a CPU feature that automatically disables idle CPU cores and cache. Disabling C6 improves system performance. |
| Sub-NUMA Clustering | Disabled | Sub-NUMA clustering divides the processor cores, cache, and memory into multiple NUMA domains. Disabling this option can increase performance for latency-sensitive workloads. |

Show more

Note

Enable global SR-IOV and VT-d settings in the firmware for the host. These settings are relevant to bare-metal environments.

Note

Enable both `C-states` and OS-controlled `P-States` to allow per pod power management.

### [8.2. Recommended cluster configurations to run vDU applications](#ztp-du-cluster-config-reference_vdu-config-ref) Copy linkLink copied to clipboard!

Clusters running virtualized distributed unit (vDU) applications require a highly tuned and optimized configuration. The following information describes the various elements that you require to support vDU workloads in OpenShift Container Platform 4.22 clusters.

#### [8.2.1. Recommended cluster MachineConfig CRs for single-node OpenShift clusters](#ztp-recommended-cluster-mc-crs_vdu-config-ref) Copy linkLink copied to clipboard!

Check that the `MachineConfig` custom resources (CRs) that you extract from the `ztp-site-generate` container are applied in the cluster. The CRs can be found in the extracted `out/source-crs/extra-manifest/` folder.

The following `MachineConfig` CRs from the `ztp-site-generate` container configure the cluster host:

Expand

Table 8.2. Recommended GitOps ZTP MachineConfig CRs

| MachineConfig CR | Description |
| --- | --- |
| `01-container-mount-ns-and-kubelet-conf-master.yaml`  `01-container-mount-ns-and-kubelet-conf-worker.yaml` | Configures the container mount namespace and kubelet configuration. |
| `03-sctp-machine-config-master.yaml`  `03-sctp-machine-config-worker.yaml` | Loads the SCTP kernel module. These `MachineConfig` CRs are optional and can be omitted if you do not require this kernel module. |
| `06-kdump-master.yaml`  `06-kdump-worker.yaml` | Configures kdump crash reporting for the cluster. |
| `07-sriov-related-kernel-args-master.yaml` | Configures SR-IOV kernel arguments in the cluster. |
| `08-set-rcu-normal-master.yaml`  `08-set-rcu-normal-worker.yaml` | Disables `rcu_expedited` mode after the cluster has rebooted. |
| `99-crio-disable-wipe-master.yaml`  `99-crio-disable-wipe-worker.yaml` | Disables the automatic CRI-O cache wipe following cluster reboot. |
| `99-sync-time-once-master.yaml`  `99-sync-time-once-worker.yaml` | Configures the one-time check and adjustment of the system clock by the Chrony service. |
| `enable-crun-master.yaml`  `enable-crun-worker.yaml` | Enables the `crun` OCI container runtime. |
| `extra-manifest/enable-cgroups-v1.yaml`  `source-crs/extra-manifest/enable-cgroups-v1.yaml` | Enables cgroups v1 during cluster installation and when generating RHACM cluster policies. |

Show more

Note

In OpenShift Container Platform 4.14 and later, you configure workload partitioning with the `cpuPartitioningMode` field in the `ClusterInstance` CR.

#### [8.2.2. Recommended cluster Operators](#ztp-recommended-cluster-operators_vdu-config-ref) Copy linkLink copied to clipboard!

The following Operators are required for clusters running virtualized distributed unit (vDU) applications and are a part of the baseline reference configuration:

* Node Tuning Operator (NTO). NTO packages functionality that was previously delivered with the Performance Addon Operator, which is now a part of NTO.
* PTP Operator
* SR-IOV Network Operator
* Red Hat OpenShift Logging Operator
* Local Storage Operator

#### [8.2.3. Recommended cluster kernel configuration](#ztp-recommended-cluster-kernel-config_vdu-config-ref) Copy linkLink copied to clipboard!

Always use the latest supported real-time kernel version in your cluster. Ensure that you apply the following configurations in the cluster:

1. Ensure that the following `additionalKernelArgs` are set in the cluster performance profile:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   # ...
   spec:
     additionalKernelArgs:
     - "rcupdate.rcu_normal_after_boot=0"
     - "efi=runtime"
     - "vfio_pci.enable_sriov=1"
     - "vfio_pci.disable_idle_d3=1"
     - "module_blacklist=irdma"

     # ...
   ```
2. Optional: Set the CPU frequency under the `hardwareTuning` field:

   You can use hardware tuning to tune CPU frequencies for reserved and isolated core CPUs. For FlexRAN like applications, hardware vendors recommend that you run CPU frequencies below the default provided frequencies. It is highly recommended that, before setting any frequencies, you refer to the hardware vendor’s guidelines for maximum frequency settings for your processor generation. This example sets the frequencies for reserved and isolated CPUs to 2500 MHz:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
     name: openshift-node-performance-profile
   spec:
         cpu:
           isolated: "2-19,22-39"
           reserved: "0-1,20-21"
         hugepages:
           defaultHugepagesSize: 1G
           pages:
             - size: 1G
               count: 32
         realTimeKernel:
             enabled: true
         hardwareTuning:
             isolatedCpuFreq: 2500000
             reservedCpuFreq: 2500000
   ```
3. Ensure that the `performance-patch` profile in the `Tuned` CR configures the correct CPU isolation set that matches the `isolated` CPU set in the related `PerformanceProfile` CR, for example:

   ```
   apiVersion: tuned.openshift.io/v1
   kind: Tuned
   metadata:
     name: performance-patch
     namespace: openshift-cluster-node-tuning-operator
     annotations:
       ran.openshift.io/ztp-deploy-wave: "10"
   spec:
     profile:
       - name: performance-patch
         # The 'include' line must match the associated PerformanceProfile name, for example:
         # include=openshift-node-performance-${PerformanceProfile.metadata.name}
         # When using the standard (non-realtime) kernel, remove the kernel.timer_migration override from the [sysctl] section
         data: |
           [main]
           summary=Configuration changes profile inherited from performance created tuned
           include=openshift-node-performance-openshift-node-performance-profile
           [scheduler]
           group.ice-ptp=0:f:10:*:ice-ptp.*
           group.ice-gnss=0:f:10:*:ice-gnss.*
           group.ice-dplls=0:f:10:*:ice-dplls.*
           [service]
           service.stalld=start,enable
           service.chronyd=stop,disable
   # ...
   ```

#### [8.2.4. Checking the realtime kernel version](#ztp-checking-kernel-rt-in-cluster_vdu-config-ref) Copy linkLink copied to clipboard!

Always use the latest version of the realtime kernel in your OpenShift Container Platform clusters. If you are unsure about the kernel version that is in use in the cluster, you can compare the current realtime kernel version to the release version with the following procedure.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You are logged in as a user with `cluster-admin` privileges.
* You have installed `podman`.

**Procedure**

1. Run the following command to get the cluster version:

   ```
   $ OCP_VERSION=$(oc get clusterversion version -o jsonpath='{.status.desired.version}{"\n"}')
   ```
2. Get the release image SHA number:

   ```
   $ DTK_IMAGE=$(oc adm release info --image-for=driver-toolkit quay.io/openshift-release-dev/ocp-release:$OCP_VERSION-x86_64)
   ```
3. Run the release image container and extract the kernel version that is packaged with cluster’s current release:

   ```
   $ podman run --rm $DTK_IMAGE rpm -qa | grep 'kernel-rt-core-' | sed 's#kernel-rt-core-##'
   ```

   **Example output**

   ```
   4.18.0-305.49.1.rt7.121.el8_4.x86_64
   ```

   This is the default realtime kernel version that ships with the release.

   Note

   The realtime kernel is denoted by the string `.rt` in the kernel version.

**Verification**

Check that the kernel version listed for the cluster’s current release matches actual realtime kernel that is running in the cluster. Run the following commands to check the running realtime kernel version:

1. Open a remote shell connection to the cluster node:

   ```
   $ oc debug node/<node_name>
   ```
2. Check the realtime kernel version:

   ```
   sh-4.4# uname -r
   ```

   **Example output**

   ```
   4.18.0-305.49.1.rt7.121.el8_4.x86_64
   ```

### [8.3. Checking that the recommended cluster configurations are applied](#ztp-checking-du-cluster-config_vdu-config-ref) Copy linkLink copied to clipboard!

You can check that clusters are running the correct configuration. The following procedure describes how to check the various configurations that you require to deploy a DU application in OpenShift Container Platform 4.22 clusters.

**Prerequisites**

* You have deployed a cluster and tuned it for vDU workloads.
* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Check that the default OperatorHub sources are disabled. Run the following command:

   ```
   $ oc get operatorhub cluster -o yaml
   ```

   The following example output shows that all default sources are disabled:

   ```
   spec:
       disableAllDefaultSources: true
   ```
2. Check that all required `CatalogSource` resources are annotated for workload partitioning (`PreferredDuringScheduling`) by running the following command:

   ```
   $ oc get catalogsource -A -o jsonpath='{range .items[*]}{.metadata.name}{" -- "}{.metadata.annotations.target\.workload\.openshift\.io/management}{"\n"}{end}'
   ```

   ```
   certified-operators -- {"effect": "PreferredDuringScheduling"}
   community-operators -- {"effect": "PreferredDuringScheduling"}
   ran-operators --
   redhat-marketplace -- {"effect": "PreferredDuringScheduling"}
   redhat-operators -- {"effect": "PreferredDuringScheduling"}
   ```

   In this output, `CatalogSource` resources that are not annotated are also returned. The `ran-operators` `CatalogSource` resource is not annotated and does not have the `PreferredDuringScheduling` annotation.

   Note

   In a properly configured vDU cluster, only a single annotated catalog source is listed.
3. Check that all applicable OpenShift Container Platform Operator namespaces are annotated for workload partitioning. This includes all Operators installed with core OpenShift Container Platform and the set of additional Operators included in the reference DU tuning configuration. Run the following command:

   ```
   $ oc get namespaces -A -o jsonpath='{range .items[*]}{.metadata.name}{" -- "}{.metadata.annotations.workload\.openshift\.io/allowed}{"\n"}{end}'
   ```

   ```
   default --
   openshift-apiserver -- management
   openshift-apiserver-operator -- management
   openshift-authentication -- management
   openshift-authentication-operator -- management
   ```

   Important

   Additional Operators must not be annotated for workload partitioning. In the output from the previous command, additional Operators should be listed without any value on the right side of the `--` separator.
4. Check that the `ClusterLogging` configuration is correct. Run the following commands:

   1. Validate that the appropriate input and output logs are configured:

      ```
      $ oc get -n openshift-logging ClusterLogForwarder instance -o yaml
      ```

      ```
      apiVersion: logging.openshift.io/v1
      kind: ClusterLogForwarder
      metadata:
        creationTimestamp: "2022-07-19T21:51:41Z"
        generation: 1
        name: instance
        namespace: openshift-logging
        resourceVersion: "1030342"
        uid: 8c1a842d-80c5-447a-9150-40350bdf40f0
      spec:
        inputs:
        - infrastructure: {}
          name: infra-logs
        outputs:
        - name: kafka-open
          type: kafka
          url: tcp://10.46.55.190:9092/test
        pipelines:
        - inputRefs:
          - audit
          name: audit-logs
          outputRefs:
          - kafka-open
        - inputRefs:
          - infrastructure
          name: infrastructure-logs
          outputRefs:
          - kafka-open
      ...
      ```
   2. Check that the curation schedule is appropriate for your application:

      ```
      $ oc get -n openshift-logging clusterloggings.logging.openshift.io instance -o yaml
      ```

      ```
      apiVersion: logging.openshift.io/v1
      kind: ClusterLogging
      metadata:
        creationTimestamp: "2022-07-07T18:22:56Z"
        generation: 1
        name: instance
        namespace: openshift-logging
        resourceVersion: "235796"
        uid: ef67b9b8-0e65-4a10-88ff-ec06922ea796
      spec:
        collection:
          logs:
            fluentd: {}
            type: fluentd
        curation:
          curator:
            schedule: 30 3 * * *
          type: curator
        managementState: Managed
      ...
      ```
5. Check that the web console is disabled (`managementState: Removed`) by running the following command:

   ```
   $ oc get consoles.operator.openshift.io cluster -o jsonpath="{ .spec.managementState }"
   ```

   ```
   Removed
   ```
6. Check that `chronyd` is disabled on the cluster node by running the following commands:

   ```
   $ oc debug node/<node_name>
   ```

   Check the status of `chronyd` on the node:

   ```
   sh-4.4# chroot /host
   ```

   ```
   sh-4.4# systemctl status chronyd
   ```

   ```
   ● chronyd.service - NTP client/server
       Loaded: loaded (/usr/lib/systemd/system/chronyd.service; disabled; vendor preset: enabled)
       Active: inactive (dead)
         Docs: man:chronyd(8)
               man:chrony.conf(5)
   ```
7. Check that the PTP interface is successfully synchronized to the primary clock using a remote shell connection to the `linuxptp-daemon` container and the PTP Management Client (`pmc`) tool:

   1. Set the `$PTP_POD_NAME` variable with the name of the `linuxptp-daemon` pod by running the following command:

      ```
      $ PTP_POD_NAME=$(oc get pods -n openshift-ptp -l app=linuxptp-daemon -o name)
      ```
   2. Run the following command to check the sync status of the PTP device:

      ```
      $ oc -n openshift-ptp rsh -c linuxptp-daemon-container ${PTP_POD_NAME} pmc -u -f /var/run/ptp4l.0.config -b 0 'GET PORT_DATA_SET'
      ```

      ```
      sending: GET PORT_DATA_SET
        3cecef.fffe.7a7020-1 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
          portIdentity            3cecef.fffe.7a7020-1
          portState               SLAVE
          logMinDelayReqInterval  -4
          peerMeanPathDelay       0
          logAnnounceInterval     1
          announceReceiptTimeout  3
          logSyncInterval         0
          delayMechanism          1
          logMinPdelayReqInterval 0
          versionNumber           2
        3cecef.fffe.7a7020-2 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
          portIdentity            3cecef.fffe.7a7020-2
          portState               LISTENING
          logMinDelayReqInterval  0
          peerMeanPathDelay       0
          logAnnounceInterval     1
          announceReceiptTimeout  3
          logSyncInterval         0
          delayMechanism          1
          logMinPdelayReqInterval 0
          versionNumber           2
      ```
   3. Run the following `pmc` command to check the PTP clock status:

      ```
      $ oc -n openshift-ptp rsh -c linuxptp-daemon-container ${PTP_POD_NAME} pmc -u -f /var/run/ptp4l.0.config -b 0 'GET TIME_STATUS_NP'
      ```

      ```
      sending: GET TIME_STATUS_NP
        3cecef.fffe.7a7020-0 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
          master_offset              10
          ingress_time               1657275432697400530
          cumulativeScaledRateOffset +0.000000000
          scaledLastGmPhaseChange    0
          gmTimeBaseIndicator        0
          lastGmPhaseChange          0x0000'0000000000000000.0000
          gmPresent                  true
          gmIdentity                 3c2c30.ffff.670e00
      ```

      In this output:

      * `master_offset` should be between -100 and 100 ns.
      * `gmPresent` indicates that the PTP clock is synchronized to a primary clock, and the local clock is not the grandmaster clock.
   4. Check that the expected `master offset` value corresponding to the value in `/var/run/ptp4l.0.config` is found in the `linuxptp-daemon-container` log:

      ```
      $ oc logs $PTP_POD_NAME -n openshift-ptp -c linuxptp-daemon-container
      ```

      ```
      phc2sys[56020.341]: [ptp4l.1.config] CLOCK_REALTIME phc offset  -1731092 s2 freq -1546242 delay    497
      ptp4l[56020.390]: [ptp4l.1.config] master offset         -2 s2 freq   -5863 path delay       541
      ptp4l[56020.390]: [ptp4l.0.config] master offset         -8 s2 freq  -10699 path delay       533
      ```
8. Check that the SR-IOV configuration is correct by running the following commands:

   1. Check that the `disableDrain` value in the `SriovOperatorConfig` resource is set to `true`:

      ```
      $ oc get sriovoperatorconfig -n openshift-sriov-network-operator default -o jsonpath="{.spec.disableDrain}{'\n'}"
      ```

      ```
      true
      ```
   2. Check that the `SriovNetworkNodeState` sync status is `Succeeded` by running the following command:

      ```
      $ oc get SriovNetworkNodeStates -n openshift-sriov-network-operator -o jsonpath="{.items[*].status.syncStatus}{'\n'}"
      ```

      ```
      Succeeded
      ```
   3. Verify that the expected number and configuration of virtual functions (`Vfs`) under each interface configured for SR-IOV is present and correct in the `.status.interfaces` field. For example:

      ```
      $ oc get SriovNetworkNodeStates -n openshift-sriov-network-operator -o yaml
      ```

      ```
      apiVersion: v1
      items:
      - apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetworkNodeState
      ...
        status:
          interfaces:
          ...
          - Vfs:
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.0
              vendor: "8086"
              vfID: 0
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.1
              vendor: "8086"
              vfID: 1
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.2
              vendor: "8086"
              vfID: 2
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.3
              vendor: "8086"
              vfID: 3
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.4
              vendor: "8086"
              vfID: 4
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.5
              vendor: "8086"
              vfID: 5
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.6
              vendor: "8086"
              vfID: 6
            - deviceID: 154c
              driver: vfio-pci
              pciAddress: 0000:3b:0a.7
              vendor: "8086"
              vfID: 7
      ```
9. Check that the cluster performance profile is correct. The `cpu` and `hugepages` sections will vary depending on your hardware configuration. Run the following command:

   ```
   $ oc get PerformanceProfile openshift-node-performance-profile -o yaml
   ```

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
     creationTimestamp: "2022-07-19T21:51:31Z"
     finalizers:
     - foreground-deletion
     generation: 1
     name: openshift-node-performance-profile
     resourceVersion: "33558"
     uid: 217958c0-9122-4c62-9d4d-fdc27c31118c
   spec:
     additionalKernelArgs:
     - idle=poll
     - rcupdate.rcu_normal_after_boot=0
     - efi=runtime
     cpu:
       isolated: 2-51,54-103
       reserved: 0-1,52-53
     hugepages:
       defaultHugepagesSize: 1G
       pages:
       - count: 32
         size: 1G
     machineConfigPoolSelector:
       pools.operator.machineconfiguration.openshift.io/master: ""
     net:
       userLevelNetworking: true
     nodeSelector:
       node-role.kubernetes.io/master: ""
     numa:
       topologyPolicy: restricted
     realTimeKernel:
       enabled: true
   status:
     conditions:
     - lastHeartbeatTime: "2022-07-19T21:51:31Z"
       lastTransitionTime: "2022-07-19T21:51:31Z"
       status: "True"
       type: Available
     - lastHeartbeatTime: "2022-07-19T21:51:31Z"
       lastTransitionTime: "2022-07-19T21:51:31Z"
       status: "True"
       type: Upgradeable
     - lastHeartbeatTime: "2022-07-19T21:51:31Z"
       lastTransitionTime: "2022-07-19T21:51:31Z"
       status: "False"
       type: Progressing
     - lastHeartbeatTime: "2022-07-19T21:51:31Z"
       lastTransitionTime: "2022-07-19T21:51:31Z"
       status: "False"
       type: Degraded
     runtimeClass: performance-openshift-node-performance-profile
     tuned: openshift-cluster-node-tuning-operator/openshift-node-performance-openshift-node-performance-profile
   ```

   Note

   CPU settings are dependent on the number of cores available on the server and should align with workload partitioning settings. `hugepages` configuration is server and application dependent.
10. Check that the `PerformanceProfile` was successfully applied to the cluster by running the following command:

    ```
    $ oc get performanceprofile openshift-node-performance-profile -o jsonpath="{range .status.conditions[*]}{ @.type }{' -- '}{@.status}{'\n'}{end}"
    ```

    ```
    Available -- True
    Upgradeable -- True
    Progressing -- False
    Degraded -- False
    ```
11. Check the `Tuned` performance patch settings by running the following command:

    ```
    $ oc get tuneds.tuned.openshift.io -n openshift-cluster-node-tuning-operator performance-patch -o yaml
    ```

    ```
    apiVersion: tuned.openshift.io/v1
    kind: Tuned
    metadata:
      creationTimestamp: "2022-07-18T10:33:52Z"
      generation: 1
      name: performance-patch
      namespace: openshift-cluster-node-tuning-operator
      resourceVersion: "34024"
      uid: f9799811-f744-4179-bf00-32d4436c08fd
    spec:
      profile:
      - data: |
          [main]
          summary=Configuration changes profile inherited from performance created tuned
          include=openshift-node-performance-openshift-node-performance-profile
          [bootloader]
          cmdline_crash=nohz_full=2-23,26-47
          [sysctl]
          kernel.timer_migration=1
          [scheduler]
          group.ice-ptp=0:f:10:*:ice-ptp.*
          [service]
          service.stalld=start,enable
          service.chronyd=stop,disable
        name: performance-patch
      recommend:
      - machineConfigLabels:
          machineconfiguration.openshift.io/role: master
        priority: 19
        profile: performance-patch
    ```

    The CPU list in `cmdline=nohz_full=` will vary based on your hardware configuration.
12. Check that cluster networking diagnostics are disabled by running the following command:

    ```
    $ oc get networks.operator.openshift.io cluster -o jsonpath='{.spec.disableNetworkDiagnostics}'
    ```

    ```
    true
    ```
13. Check that the `Kubelet` housekeeping interval is tuned to slower rate. This is set in the `containerMountNS` machine config. Run the following command:

    ```
    $ oc describe machineconfig container-mount-namespace-and-kubelet-conf-master | grep OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION
    ```

    ```
    Environment="OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION=60s"
    ```
14. Check that Grafana and `alertManagerMain` are disabled and that the Prometheus retention period is set to 24h by running the following command:

    ```
    $ oc get configmap cluster-monitoring-config -n openshift-monitoring -o jsonpath="{ .data.config\.yaml }"
    ```

    ```
    grafana:
      enabled: false
    alertmanagerMain:
      enabled: false
    prometheusK8s:
       retention: 24h
    ```

    1. Use the following commands to verify that Grafana and `alertManagerMain` routes are not found in the cluster:

       ```
       $ oc get route -n openshift-monitoring alertmanager-main
       ```

       ```
       $ oc get route -n openshift-monitoring grafana
       ```

       Both queries should return `Error from server (NotFound)` messages.
15. Check that there is a minimum of 4 CPUs allocated as `reserved` for each of the `PerformanceProfile`, `Tuned` performance-patch, workload partitioning, and kernel command-line arguments by running the following command:

    ```
    $ oc get performanceprofile -o jsonpath="{ .items[0].spec.cpu.reserved }"
    ```

    ```
    0-3
    ```

    Note

    Depending on your workload requirements, you might require additional reserved CPUs to be allocated.

## [Chapter 9. Advanced managed cluster configuration with ClusterInstance resources](#ztp-advanced-install-ztp) Copy linkLink copied to clipboard!

You can use `ClusterInstance` custom resources (CRs) to deploy custom functionality and configurations in your managed clusters at installation time.

### [9.1. Customizing extra installation manifests in the GitOps ZTP pipeline](#ztp-customizing-the-install-extra-manifests_ztp-advanced-install-ztp) Copy linkLink copied to clipboard!

You can define a set of extra manifests for inclusion in the installation phase of the GitOps Zero Touch Provisioning (ZTP) pipeline. These manifests are linked to the `ClusterInstance` custom resources (CRs) and are applied to the cluster during installation. Including `MachineConfig` CRs at install time makes the installation process more efficient.

Extra manifests must be packaged in `ConfigMap` resources and referenced in the `extraManifestsRefs` field of the `ClusterInstance` CR.

**Prerequisites**

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

**Procedure**

1. Create a set of extra manifest CRs that the GitOps ZTP pipeline uses to customize the cluster installs.
2. In your `/clusterinstance` directory, create a subdirectory with your extra manifests. The following example illustrates a sample folder structure:

   ```
   clusterinstance/
   ├── site1-sno-du.yaml
   ├── extra-manifest/
   │   ├── 01-example-machine-config.yaml
   │   ├── enable-crun-master.yaml
   │   └── enable-crun-worker.yaml
   └── kustomization.yaml
   ```
3. Create or update the `kustomization.yaml` file to use `configMapGenerator` to package your extra manifests into a `ConfigMap`:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - site1-sno-du.yaml
   configMapGenerator:
     - name: extra-manifests-cm
       namespace: site1-sno-du
       files:
         - extra-manifest/01-example-machine-config.yaml
         - extra-manifest/enable-crun-master.yaml
         - extra-manifest/enable-crun-worker.yaml
   generatorOptions:
     disableNameSuffixHash: true
   ```

   * The `configMapGenerator.namespace` value must match the `ClusterInstance` namespace.
   * Setting `generatorOptions.disableNameSuffixHash` to `true` disables the hash suffix so the `ConfigMap` name is predictable.
4. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     clusterName: "site1-sno-du"
     networkType: "OVNKubernetes"
     extraManifestsRefs:
       - name: extra-manifests-cm
     # ...
   ```

   * The `extraManifestsRefs` field references the `ConfigMap` containing the extra manifests.
5. Commit the `ClusterInstance` CR, extra manifest files, and `kustomization.yaml` to your Git repository and push the changes.

   During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests.

   Note

   You can reference multiple `ConfigMap` resources in `extraManifestsRefs` to organize your manifests logically. For example, you might have separate `ConfigMap` resources for crun configuration, custom `MachineConfig` CRs, and other Day 0 configurations.

### [9.2. Configuring cluster network MTU at installation time](#ztp-configuring-cluster-network-mtu_ztp-advanced-install-ztp) Copy linkLink copied to clipboard!

You can explicitly set the cluster network maximum transmission unit (MTU) during installation by including a `Network` custom resource (CR) as an extra manifest in the GitOps Zero Touch Provisioning (ZTP) pipeline.

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

* You have configured the hub cluster to provision managed clusters by using the GitOps ZTP pipeline.
* You have a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

**Procedure**

1. In your `ClusterInstance` CR, set the machine network MTU on the network interface for all nodes.

   The following example configures a VLAN interface with MTU `9100`:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     nodes:
       - hostName: "node1.example.com"
         nodeNetwork:
           interfaces:
             - name: "bond0.120"
               macAddress: "00:00:00:00:00:00"
           config:
             interfaces:
               - name: bond0.120
                 type: vlan
                 state: up
                 mtu: 9100
                 ipv4:
                   enabled: true
                   dhcp: false
                   address:
                     - ip: "192.168.120.15"
                       prefix-length: 25
                 vlan:
                   base-iface: bond0
                   id: 120
     # ...
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
3. In your `clusterinstance` directory, place the manifest file in an extra manifests subdirectory:

   ```
   clusterinstance/
   ├── site1-sno-du.yaml
   ├── extra-manifest/
   │   └── set-cluster-mtu.yaml
   └── kustomization.yaml
   ```
4. Create or update the `kustomization.yaml` file to package the extra manifest into a `ConfigMap`:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization
   resources:
     - site1-sno-du.yaml
   configMapGenerator:
     - name: cluster-mtu-extra-manifests
       namespace: site1-sno-du
       files:
         - extra-manifest/set-cluster-mtu.yaml
   generatorOptions:
     disableNameSuffixHash: true
   ```
5. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "site1-sno-du"
     namespace: "site1-sno-du"
   spec:
     clusterName: "site1-sno-du"
     networkType: "OVNKubernetes"
     extraManifestsRefs:
       - name: cluster-mtu-extra-manifests
     # ...
   ```
6. Commit the `ClusterInstance` CR, the `set-cluster-mtu.yaml` manifest, and the `kustomization.yaml` to your Git repository and push the changes.

   During cluster provisioning, the SiteConfig Operator applies the `Network` CR as an extra manifest, and the CNO uses the specified MTU value instead of auto-calculating it.

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

### [9.3. Deleting a node by using the ClusterInstance CR](#ztp-deleting-node-clusterinstance_ztp-advanced-install-ztp) Copy linkLink copied to clipboard!

By using a `ClusterInstance` custom resource (CR), you can delete and reprovision a node. This method is more efficient than manually deleting the node.

**Prerequisites**

* You have configured the hub cluster to generate the required installation and policy CRs.
* You have created a Git repository in which you can manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as the source repository for the Argo CD application.

**Procedure**

1. Update the `ClusterInstance` CR to add the `bmac.agent-install.openshift.io/remove-agent-and-node-on-delete=true` annotation to the `BareMetalHost` resource for the node, and push the changes to the Git repository:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-cluster"
     namespace: "example-cluster"
   spec:
     # ...
     nodes:
       - hostName: "worker-node2.example.com"
         role: "worker"
         extraAnnotations:
           BareMetalHost:
             bmac.agent-install.openshift.io/remove-agent-and-node-on-delete: "true"
   # ...
   ```
2. Verify that the `BareMetalHost` object is annotated by running the following command:

   ```
   $ oc get bmh -n <cluster_namespace> <bmh_name> -ojsonpath='{.metadata}' | jq -r '.annotations["bmac.agent-install.openshift.io/remove-agent-and-node-on-delete"]'
   ```

   **Example output**

   ```
   true
   ```
3. Delete the `BareMetalHost` CR by configuring the `pruneManifests` field in the `ClusterInstance` CR to remove the target `BareMetalHost` resource:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-cluster"
     namespace: "example-cluster"
   spec:
     # ...
     nodes:
       - hostName: "worker-node2.example.com"
         role: "worker"
         pruneManifests:
           - apiVersion: metal3.io/v1alpha1
             kind: BareMetalHost
   # ...
   ```
4. Push the changes to the Git repository and wait for deprovisioning to start. The status of the `BareMetalHost` CR should change to `deprovisioning`. Wait for the `BareMetalHost` to finish deprovisioning, and be fully deleted.

**Verification**

1. Verify that the `BareMetalHost` and `Agent` CRs for the worker node have been deleted from the hub cluster by running the following commands:

   ```
   $ oc get bmh -n <cluster_namespace>
   ```

   ```
   $ oc get agent -n <cluster_namespace>
   ```
2. Verify that the node record has been deleted from the spoke cluster by running the following command:

   ```
   $ oc get nodes
   ```

   Note

   If you are working with secrets, deleting a secret too early can cause an issue because ArgoCD needs the secret to complete resynchronization after deletion. Delete the secret only after the node cleanup, when the current ArgoCD synchronization is complete.
3. After the `BareMetalHost` object is successfully deleted, remove the worker node definition from the `spec.nodes` section in the `ClusterInstance` CR and push the changes to the Git repository.

**Next steps**

To reprovision a node, add the node definition back to the `spec.nodes` section in the `ClusterInstance` CR, push the changes to the Git repository, and wait for the synchronization to complete. This regenerates the `BareMetalHost` CR of the worker node and triggers the re-install of the node.

## [Chapter 10. Managing cluster policies with PolicyGenerator resources](#managing-cluster-policies-with-policygenerator-resources) Copy linkLink copied to clipboard!

### [10.1. Configuring managed cluster policies by using PolicyGenerator resources](#ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

You can customize how Red Hat Advanced Cluster Management (RHACM) uses `PolicyGenerator` CRs to generate `Policy` CRs that configure the managed clusters that you provision.

Using RHACM and `PolicyGenerator` CRs is the recommended approach for managing policies and deploying them to managed clusters. This replaces the use of `PolicyGenTemplate` CRs for this purpose. For more information about `PolicyGenerator` resources, see the RHACM [Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/governance/policy-deployment#integrate-policy-generator) documentation.

#### [10.1.1. Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

`PolicyGenerator` custom resources (CRs) and `PolicyGenTemplate` CRs can be used in GitOps ZTP to generate RHACM policies for managed clusters.

There are advantages to using `PolicyGenerator` CRs over `PolicyGenTemplate` CRs when it comes to patching OpenShift Container Platform resources with GitOps ZTP. Using the RHACM `PolicyGenerator` API provides a generic way of patching resources which is not possible with `PolicyGenTemplate` resources.

The `PolicyGenerator` API is a part of the [Open Cluster Management](https://open-cluster-management.io/) standard, while the `PolicyGenTemplate` API is not. A comparison of `PolicyGenerator` and `PolicyGenTemplate` resource patching and placement strategies are described in the following table.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

Expand

Table 10.1. Comparison of RHACM PolicyGenerator and PolicyGenTemplate patching

| PolicyGenerator patching | PolicyGenTemplate patching |
| --- | --- |
| Uses Kustomize strategic merges for merging resources. For more information see [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/). | Works by replacing variables with their values as defined by the patch. This is less flexible than Kustomize merge strategies. |
| Supports `ManagedClusterSet` and `Binding` resources. | Does not support `ManagedClusterSet` and `Binding` resources. |
| Relies only on patching, no embedded variable substitution is required. | Overwrites variable values defined in the patch. |
| Does not support merging lists in merge patches. Replacing a list in a merge patch is supported. | Merging and replacing lists is supported in a limited fashion - you can only merge one object in the list. |
| Does not currently support the [OpenAPI specification](https://spec.openapis.org/oas/latest.html) for resource patching. This means that additional directives are required in the patch to merge content that does not follow a schema, for example, `PtpConfig` resources. | Works by replacing fields and values with values as defined by the patch. |
| Requires additional directives, for example, `$patch: replace` in the patch to merge content that does not follow a schema. | Substitutes fields and values defined in the source CR with values defined in the patch, for example `$name`. |
| Can patch the `Name` and `Namespace` fields defined in the reference source CR, but only if the CR file has a single object. | Can patch the `Name` and `Namespace` fields defined in the reference source CR. |

Show more

#### [10.1.2. About the PolicyGenerator CRD](#ztp-the-policygentemplate_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

The `PolicyGenerator` custom resource definition (CRD) tells the `PolicyGen` policy generator what custom resources (CRs) to include in the cluster configuration, how to combine the CRs into the generated policies, and what items in those CRs need to be updated with overlay content.

The following example shows a `PolicyGenerator` CR (`acm-common-du-ranGen.yaml`) extracted from the `ztp-site-generate` reference container. The `acm-common-du-ranGen.yaml` file defines two Red Hat Advanced Cluster Management (RHACM) policies. The policies manage a collection of configuration CRs, one for each unique value of `policyName` in the CR. `acm-common-du-ranGen.yaml` creates a single placement binding and a placement rule to bind the policies to clusters based on the labels listed in the `policyDefaults.placement.labelSelector` section.

**Example PolicyGenerator CR - acm-common-ranGen.yaml**

```
apiVersion: policy.open-cluster-management.io/v1
kind: PolicyGenerator
metadata:
    name: common-latest
placementBindingDefaults:
    name: common-latest-placement-binding
policyDefaults:
    namespace: ztp-common
    placement:
        labelSelector:
            matchExpressions:
                - key: common
                  operator: In
                  values:
                    - "true"
                - key: du-profile
                  operator: In
                  values:
                    - latest
    remediationAction: inform
    severity: low
    namespaceSelector:
        exclude:
            - kube-*
        include:
            - '*'
    evaluationInterval:
        compliant: 10m
        noncompliant: 10s
policies:
    - name: common-latest-config-policy
      policyAnnotations:
        ran.openshift.io/ztp-deploy-wave: "1"
      manifests:
        - path: source-crs/ReduceMonitoringFootprint.yaml
        - path: source-crs/DefaultCatsrc.yaml
          patches:
            - metadata:
                name: redhat-operators-disconnected
              spec:
                displayName: disconnected-redhat-operators
                image: registry.example.com:5000/disconnected-redhat-operators/disconnected-redhat-operator-index:v4.9
        - path: source-crs/DisconnectedICSP.yaml
          patches:
            - spec:
                repositoryDigestMirrors:
                    - mirrors:
                        - registry.example.com:5000
                      source: registry.redhat.io
    - name: common-latest-subscriptions-policy
      policyAnnotations:
        ran.openshift.io/ztp-deploy-wave: "2"
      manifests:
        - path: source-crs/SriovSubscriptionNS.yaml
        - path: source-crs/SriovSubscriptionOperGroup.yaml
        - path: source-crs/SriovSubscription.yaml
        - path: source-crs/SriovOperatorStatus.yaml
        - path: source-crs/PtpSubscriptionNS.yaml
        - path: source-crs/PtpSubscriptionOperGroup.yaml
        - path: source-crs/PtpSubscription.yaml
        - path: source-crs/PtpOperatorStatus.yaml
        - path: source-crs/ClusterLogNS.yaml
        - path: source-crs/ClusterLogOperGroup.yaml
        - path: source-crs/ClusterLogSubscription.yaml
        - path: source-crs/ClusterLogOperatorStatus.yaml
        - path: source-crs/StorageNS.yaml
        - path: source-crs/StorageOperGroup.yaml
        - path: source-crs/StorageSubscription.yaml
        - path: source-crs/StorageOperatorStatus.yaml
```

where:

`name: common-latest-placement-binding`
:   Applies the policies to all clusters with this label.

`DefaultCatsrc.yaml`
:   The `DefaultCatsrc.yaml` file contains the catalog source for the disconnected registry and related registry configuration details.

`manifests`
:   Files listed under `policies.manifests` create the Operator policies for installed clusters.

A `PolicyGenerator` CR can be constructed with any number of included CRs. Apply the following example CR in the hub cluster to generate a policy containing a single CR:

```
apiVersion: policy.open-cluster-management.io/v1
kind: PolicyGenerator
metadata:
  name: group-du-sno
placementBindingDefaults:
  name: group-du-sno-placement-binding
policyDefaults:
  namespace: ztp-group
  placement:
    labelSelector:
      matchExpressions:
        - key: group-du-sno
          operator: Exists
  remediationAction: inform
  severity: low
  namespaceSelector:
    exclude:
      - kube-*
    include:
      - '*'
  evaluationInterval:
    compliant: 10m
    noncompliant: 10s
policies:
  - name: group-du-sno-config-policy
    policyAnnotations:
      ran.openshift.io/ztp-deploy-wave: '10'
    manifests:
      - path: source-crs/PtpConfigSlave-MCP-master.yaml
        patches:
          - metadata: null
            name: du-ptp-slave
            namespace: openshift-ptp
            annotations:
              ran.openshift.io/ztp-deploy-wave: '10'
            spec:
              profile:
                - name: slave
                  interface: $interface
                  ptp4lOpts: '-2 -s'
                  phc2sysOpts: '-a -r -n 24'
                  ptpSchedulingPolicy: SCHED_FIFO
                  ptpSchedulingPriority: 10
                  ptpSettings:
                    logReduce: 'true'
                  ptp4lConf: |
                    [global]
                    #
                    # Default Data Set
                    #
                    twoStepFlag 1
                    slaveOnly 1
                    priority1 128
                    priority2 128
                    domainNumber 24
                    #utc_offset 37
                    clockClass 255
                    clockAccuracy 0xFE
                    offsetScaledLogVariance 0xFFFF
                    free_running 0
                    freq_est_interval 1
                    dscp_event 0
                    dscp_general 0
                    dataset_comparison G.8275.x
                    G.8275.defaultDS.localPriority 128
                    #
                    # Port Data Set
                    #
                    logAnnounceInterval -3
                    logSyncInterval -4
                    logMinDelayReqInterval -4
                    logMinPdelayReqInterval -4
                    announceReceiptTimeout 3
                    syncReceiptTimeout 0
                    delayAsymmetry 0
                    fault_reset_interval -4
                    neighborPropDelayThresh 20000000
                    masterOnly 0
                    G.8275.portDS.localPriority 128
                    #
                    # Run time options
                    #
                    assume_two_step 0
                    logging_level 6
                    path_trace_enabled 0
                    follow_up_info 0
                    hybrid_e2e 0
                    inhibit_multicast_service 0
                    net_sync_monitor 0
                    tc_spanning_tree 0
                    tx_timestamp_timeout 50
                    unicast_listen 0
                    unicast_master_table 0
                    unicast_req_duration 3600
                    use_syslog 1
                    verbose 0
                    summary_interval 0
                    kernel_leap 1
                    check_fup_sync 0
                    clock_class_threshold 7
                    #
                    # Servo Options
                    #
                    pi_proportional_const 0.0
                    pi_integral_const 0.0
                    pi_proportional_scale 0.0
                    pi_proportional_exponent -0.3
                    pi_proportional_norm_max 0.7
                    pi_integral_scale 0.0
                    pi_integral_exponent 0.4
                    pi_integral_norm_max 0.3
                    step_threshold 2.0
                    first_step_threshold 0.00002
                    max_frequency 900000000
                    clock_servo pi
                    sanity_freq_limit 200000000
                    ntpshm_segment 0
                    #
                    # Transport options
                    #
                    transportSpecific 0x0
                    ptp_dst_mac 01:1B:19:00:00:00
                    p2p_dst_mac 01:80:C2:00:00:0E
                    udp_ttl 1
                    udp6_scope 0x0E
                    uds_address /var/run/ptp4l
                    #
                    # Default interface options
                    #
                    clock_type OC
                    network_transport L2
                    delay_mechanism E2E
                    time_stamping hardware
                    tsproc_mode filter
                    delay_filter moving_median
                    delay_filter_length 10
                    egressLatency 0
                    ingressLatency 0
                    boundary_clock_jbod 0
                    #
                    # Clock description
                    #
                    productDescription ;;
                    revisionData ;;
                    manufacturerIdentity 00:00:00
                    userDescription ;
                    timeSource 0xA0
              recommend:
                - profile: slave
                  priority: 4
                  match:
                    - nodeLabel: node-role.kubernetes.io/master
```

Using the source file `PtpConfigSlave.yaml` as an example, the file defines a `PtpConfig` CR. The generated policy for the `PtpConfigSlave` example is named `group-du-sno-config-policy`. The `PtpConfig` CR defined in the generated `group-du-sno-config-policy` is named `du-ptp-slave`. The `spec` defined in `PtpConfigSlave.yaml` is placed under `du-ptp-slave` along with the other `spec` items defined under the source file.

The following example shows the `group-du-sno-config-policy` CR:

```
---
apiVersion: policy.open-cluster-management.io/v1
kind: PolicyGenerator
metadata:
    name: du-upgrade
placementBindingDefaults:
    name: du-upgrade-placement-binding
policyDefaults:
    namespace: ztp-group-du-sno
    placement:
        labelSelector:
            matchExpressions:
                - key: group-du-sno
                  operator: Exists
    remediationAction: inform
    severity: low
    namespaceSelector:
        exclude:
            - kube-*
        include:
            - '*'
    evaluationInterval:
        compliant: 10m
        noncompliant: 10s
policies:
    - name: du-upgrade-operator-catsrc-policy
      policyAnnotations:
        ran.openshift.io/ztp-deploy-wave: "1"
      manifests:
        - path: source-crs/DefaultCatsrc.yaml
          patches:
            - metadata:
                name: redhat-operators
              spec:
                displayName: Red Hat Operators Catalog
                image: registry.example.com:5000/olm/redhat-operators:v4.14
                updateStrategy:
                    registryPoll:
                        interval: 1h
              status:
                connectionState:
                    lastObservedState: READY
```

#### [10.1.3. Recommendations when customizing PolicyGenerator CRs](#ztp-pgt-config-best-practices_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

Consider the following best practices when customizing site configuration `PolicyGenerator` custom resources (CRs):

* Use as few policies as are necessary. Using fewer policies requires less resources. Each additional policy creates increased CPU load for the hub cluster and the deployed managed cluster. CRs are combined into policies based on the `policyName` field in the `PolicyGenerator` CR. CRs in the same `PolicyGenerator` which have the same value for `policyName` are managed under a single policy.
* In disconnected environments, use a single catalog source for all Operators by configuring the registry as a single index containing all Operators. Each additional `CatalogSource` CR on the managed clusters increases CPU usage.
* Reduce the overall time taken until the cluster is ready to deploy applications by including `MachineConfig` CRs as extra manifests in the installation. To do this, package `MachineConfig` CRs in a `ConfigMap` CR. Reference the `ConfigMap` CRs in the `extraManifestsRefs` field in the `ClusterInstance` CR.
* `PolicyGenerator` CRs should override the channel field to explicitly identify the desired version. This ensures that changes in the source CR during upgrades does not update the generated subscription.
* The default setting for `policyDefaults.consolidateManifests` is `true`. This is the recommended setting for DU profile. Setting it to `false` might impact large scale deployments.
* The default setting for `policyDefaults.orderPolicies` is `false`. This is the recommended setting for DU profile. After the cluster installation is complete and a cluster becomes `Ready`, TALM creates a `ClusterGroupUpgrade` CR corresponding to this cluster. The `ClusterGroupUpgrade` CR contains a list of ordered policies defined by the `ran.openshift.io/ztp-deploy-wave` annotation. If you use the `PolicyGenerator` CR to change the order of the policies, conflicts might occur and the configuration might not be applied.

Note

When managing large numbers of spoke clusters on the hub cluster, minimize the number of policies to reduce resource consumption.

Grouping multiple configuration CRs into a single or limited number of policies is one way to reduce the overall number of policies on the hub cluster. When using the common, group, and site hierarchy of policies for managing site configuration, it is especially important to combine site-specific configuration into a single policy.

#### [10.1.4. PolicyGenerator CRs for RAN deployments](#ztp-policygentemplates-for-ran_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

Use `PolicyGenerator` custom resources (CRs) to customize the configuration applied to the cluster by using the GitOps Zero Touch Provisioning (ZTP) pipeline. The `PolicyGenerator` CR allows you to generate one or more policies to manage the set of configuration CRs on your fleet of clusters. The `PolicyGenerator` CR identifies the set of managed CRs, bundles them into policies, builds the policy wrapping around those CRs, and associates the policies with clusters by using label binding rules.

The reference configuration, obtained from the GitOps ZTP container, is designed to provide a set of critical features and node tuning settings that ensure the cluster can support the stringent performance and resource utilization constraints typical of RAN (Radio Access Network) Distributed Unit (DU) applications. Changes or omissions from the baseline configuration can affect feature availability, performance, and resource utilization. Use the reference `PolicyGenerator` CRs as the basis to create a hierarchy of configuration files tailored to your specific site requirements.

The baseline `PolicyGenerator` CRs that are defined for RAN DU cluster configuration can be extracted from the GitOps ZTP `ztp-site-generate` container. See "Preparing the GitOps ZTP site configuration repository" for further details.

The `PolicyGenerator` CRs can be found in the `./out/argocd/example/acmpolicygenerator/` folder. The reference architecture has common, group, and site-specific configuration CRs. Each `PolicyGenerator` CR refers to other CRs that can be found in the `./out/source-crs` folder.

The `PolicyGenerator` CRs relevant to RAN cluster configuration are described below. Variants are provided for the group `PolicyGenerator` CRs to account for differences in single-node, three-node compact, and standard cluster configurations. Similarly, site-specific configuration variants are provided for single-node clusters and multi-node (compact or standard) clusters. Use the group and site-specific configuration variants that are relevant for your deployment.

Expand

Table 10.2. PolicyGenerator CRs for RAN deployments

| PolicyGenerator CR | Description |
| --- | --- |
| `acm-example-multinode-site.yaml` | Contains a set of CRs that get applied to multi-node clusters. These CRs configure SR-IOV features typical for RAN installations. |
| `acm-example-sno-site.yaml` | Contains a set of CRs that get applied to single-node OpenShift clusters. These CRs configure SR-IOV features typical for RAN installations. |
| `acm-common-mno-ranGen.yaml` | Contains a set of common RAN policy configuration that get applied to multi-node clusters. |
| `acm-common-ranGen.yaml` | Contains a set of common RAN CRs that get applied to all clusters. These CRs subscribe to a set of operators providing cluster features typical for RAN as well as baseline cluster tuning. |
| `acm-group-du-3node-ranGen.yaml` | Contains the RAN policies for three-node clusters only. |
| `acm-group-du-sno-ranGen.yaml` | Contains the RAN policies for single-node clusters only. |
| `acm-group-du-standard-ranGen.yaml` | Contains the RAN policies for standard three control-plane clusters. |
| `acm-group-du-3node-validator-ranGen.yaml` | `PolicyGenerator` CR used to generate the various policies required for three-node clusters. |
| `acm-group-du-standard-validator-ranGen.yaml` | `PolicyGenerator` CR used to generate the various policies required for standard clusters. |
| `acm-group-du-sno-validator-ranGen.yaml` | `PolicyGenerator` CR used to generate the various policies required for single-node OpenShift clusters. |

Show more

#### [10.1.5. Customizing a managed cluster with PolicyGenerator CRs](#ztp-customizing-a-managed-site-using-pgt_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

Use the following procedure to customize the policies that get applied to the managed cluster that you provision using the GitOps Zero Touch Provisioning (ZTP) pipeline.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You configured the hub cluster for generating the required installation and policy CRs.
* You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

**Procedure**

1. Create a `PolicyGenerator` CR for site-specific configuration CRs.

   1. Choose the appropriate example for your CR from the `out/argocd/example/acmpolicygenerator/` folder, for example, `acm-example-sno-site.yaml` or `acm-example-multinode-site.yaml`.
   2. Change the `policyDefaults.placement.labelSelector` field in the example file to match the site-specific label included in the `ClusterInstance` CR. In the example `ClusterInstance` file, the site-specific label is `sites: example-sno`.

      Note

      Ensure that the labels defined in your `PolicyGenerator` `policyDefaults.placement.labelSelector` field correspond to the labels that are defined in the related managed clusters `ClusterInstance` CR.
   3. Change the content in the example file to match the desired configuration.
2. Optional: Create a `PolicyGenerator` CR for any common configuration CRs that apply to the entire fleet of clusters.

   1. Select the appropriate example for your CR from the `out/argocd/example/acmpolicygenerator/` folder, for example, `acm-common-ranGen.yaml`.
   2. Change the content in the example file to match the required configuration.
3. Optional: Create a `PolicyGenerator` CR for any group configuration CRs that apply to the certain groups of clusters in the fleet.

   Ensure that the content of the overlaid spec files matches your required end state. As a reference, the `out/source-crs` directory contains the full list of source-crs available to be included and overlaid by your PolicyGenerator templates.

   Note

   Depending on the specific requirements of your clusters, you might need more than a single group policy per cluster type, especially considering that the example group policies each have a single `PerformancePolicy.yaml` file that can only be shared across a set of clusters if those clusters consist of identical hardware configurations.

   1. Select the appropriate example for your CR from the `out/argocd/example/acmpolicygenerator/` folder, for example, `acm-group-du-sno-ranGen.yaml`.
   2. Change the content in the example file to match the required configuration.
4. Optional. Create a validator inform policy `PolicyGenerator` CR to signal when the GitOps ZTP installation and configuration of the deployed cluster is complete. For more information, see "Creating a validator inform policy".
5. Define all the policy namespaces in a YAML file similar to the example `out/argocd/example/acmpolicygenerator//ns.yaml` file.

   Important

   Do not include the `Namespace` CR in the same file with the `PolicyGenerator` CR.
6. Add the `PolicyGenerator` CRs and `Namespace` CR to the `kustomization.yaml` file in the generators section, similar to the example shown in `out/argocd/example/acmpolicygenerator/kustomization.yaml`.
7. Commit the `PolicyGenerator` CRs, `Namespace` CR, and associated `kustomization.yaml` file in your Git repository and push the changes.

   The ArgoCD pipeline detects the changes and begins the managed cluster deployment. You can push the changes to the `ClusterInstance` CR and the `PolicyGenerator` CR simultaneously.

#### [10.1.6. Monitoring managed cluster policy deployment progress](#ztp-monitoring-policy-deployment-progress_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

The ArgoCD pipeline uses `PolicyGenerator` CRs in Git to generate the RHACM policies and then sync them to the hub cluster. You can monitor the progress of the managed cluster policy synchronization after the assisted service installs OpenShift Container Platform on the managed cluster.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. The Topology Aware Lifecycle Manager (TALM) applies the configuration policies that are bound to the cluster.

   After the cluster installation is complete and the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR corresponding to this cluster, with a list of ordered policies defined by the `ran.openshift.io/ztp-deploy-wave annotations`, is automatically created by the TALM. The cluster’s policies are applied in the order listed in `ClusterGroupUpgrade` CR.

   You can monitor the high-level progress of configuration policy reconciliation by using the following commands:

   ```
   $ export CLUSTER=<clusterName>
   ```

   ```
   $ oc get clustergroupupgrades -n ztp-install $CLUSTER -o jsonpath='{.status.conditions[-1:]}' | jq
   ```

   **Example output**

   ```
   {
     "lastTransitionTime": "2022-11-09T07:28:09Z",
     "message": "Remediating non-compliant policies",
     "reason": "InProgress",
     "status": "True",
     "type": "Progressing"
   }
   ```
2. You can monitor the detailed cluster policy compliance status by using the RHACM dashboard or the command line.

   1. To check policy compliance by using `oc`, run the following command:

      ```
      $ oc get policies -n $CLUSTER
      ```

      **Example output**

      ```
      NAME                                                     REMEDIATION ACTION   COMPLIANCE STATE   AGE
      ztp-common.common-config-policy                          inform               Compliant          3h42m
      ztp-common.common-subscriptions-policy                   inform               NonCompliant       3h42m
      ztp-group.group-du-sno-config-policy                     inform               NonCompliant       3h42m
      ztp-group.group-du-sno-validator-du-policy               inform               NonCompliant       3h42m
      ztp-install.example1-common-config-policy-pjz9s          enforce              Compliant          167m
      ztp-install.example1-common-subscriptions-policy-zzd9k   enforce              NonCompliant       164m
      ztp-site.example1-config-policy                          inform               NonCompliant       3h42m
      ztp-site.example1-perf-policy                            inform               NonCompliant       3h42m
      ```
   2. To check policy status from the RHACM web console, perform the following actions:

      1. Click **Governance** → **Find policies**.
      2. Click on a cluster policy to check its status.

Note

When all of the cluster policies become compliant, GitOps ZTP installation and configuration for the cluster is complete. The `ztp-done` label is added to the cluster.

In the reference configuration, the final policy that becomes compliant is the one defined in the `*-du-validator-policy` policy. This policy, when compliant on a cluster, ensures that all cluster configuration, Operator installation, and Operator configuration is complete.

#### [10.1.7. Coordinating reboots for configuration changes](#ztp-coordinating-reboots-for-config-changes_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

You can use Topology Aware Lifecycle Manager (TALM) to coordinate reboots across a fleet of spoke clusters when configuration changes require a reboot, such as deferred tuning changes. TALM reboots all nodes in the targeted `MachineConfigPool` on the selected clusters when the reboot policy is applied.

Instead of rebooting nodes after each individual change, you can apply all configuration updates through policies and then trigger a single, coordinated reboot.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have deployed and configured TALM.

**Procedure**

1. Generate the configuration policies by creating a `PolicyGenerator` custom resource (CR). You can use one of the following sample manifests:

   * `out/argocd/example/acmpolicygenerator/acm-example-sno-reboot`
   * `out/argocd/example/acmpolicygenerator/acm-example-multinode-reboot`
2. Update the `policyDefaults.placement.labelSelector` field in the `PolicyGenerator` CR to target the clusters that you want to reboot. Modify other fields as necessary for your use case.

   If you are coordinating a reboot to apply a deferred tuning change, ensure the `MachineConfigPool` in the reboot policy matches the value specified in the `spec.recommend` field in the `Tuned` object.
3. Apply the `PolicyGenerator` CR to generate and apply the configuration policies. For detailed steps, see "Customizing a managed cluster with PolicyGenerator CRs".
4. After ArgoCD completes syncing the policies, create and apply the `ClusterGroupUpgrade` (CGU) CR.

   **Example CGU custom resource configuration**

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: reboot
     namespace: default
   spec:
     clusterLabelSelectors:
     - matchLabels:
   # ...
     enable: true
     managedPolicies:
     - example-reboot
     remediationStrategy:
       timeout: 300
       maxConcurrency: 10
   # ...
   ```

   where:

   `matchLabels`
   :   Configure the labels that match the clusters you want to reboot.

   `managedPolicies`
   :   Add all required configuration policies before the reboot policy. TALM applies the configuration changes as specified in the policies, in the order they are listed.

   `timeout`
   :   Specify the timeout in seconds for the entire upgrade across all selected clusters. Set this field by considering the worst-case scenario.
5. After you apply the CGU custom resource, TALM rolls out the configuration policies in order. Once all policies are compliant, it applies the reboot policy and triggers a reboot of all nodes in the specified `MachineConfigPool`.

**Verification**

1. Monitor the CGU rollout status.

   You can monitor the rollout of the CGU custom resource on the hub by checking the status. Verify the successful rollout of the reboot by running the following command:

   ```
   oc get cgu -A
   ```

   **Example output**

   ```
   NAMESPACE   NAME     AGE   STATE       DETAILS
   default     reboot   1d    Completed   All clusters are compliant with all the managed policies
   ```
2. Verify successful reboot on a specific node.

   To confirm that the reboot was successful on a specific node, check the status of the `MachineConfigPool` (MCP) for the node by running the following command:

   ```
   oc get mcp master
   ```

   **Example output**

   ```
   NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master   rendered-master-be5785c3b98eb7a1ec902fef2b81e865   True      False      False      3              3                   3                     0                      72d
   ```

#### [10.1.8. Validating the generation of configuration policy CRs](#ztp-validating-the-generation-of-configuration-policy-crs_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

`Policy` custom resources (CRs) are generated in the same namespace as the `PolicyGenerator` from which they are created. The same troubleshooting flow applies to all policy CRs generated from a `PolicyGenerator` regardless of whether they are `ztp-common`, `ztp-group`, or `ztp-site` based, as shown using the following commands:

```
$ export NS=<namespace>
```

```
$ oc get policy -n $NS
```

The expected set of policy-wrapped CRs should be displayed.

If the policies failed synchronization, use the following troubleshooting steps.

**Procedure**

1. To display detailed information about the policies, run the following command:

   ```
   $ oc describe -n openshift-gitops application policies
   ```
2. Check for `Status: Conditions:` to show the error logs. For example, setting an invalid `sourceFile` entry to `fileName:` generates the error shown below:

   ```
   Status:
     Conditions:
       Last Transition Time:  2021-11-26T17:21:39Z
       Message:               rpc error: code = Unknown desc = `kustomize build /tmp/https___git.com/ran-sites/policies/ --enable-alpha-plugins` failed exit status 1: 2021/11/26 17:21:40 Error could not find test.yaml under source-crs/: no such file or directory Error: failure in plugin configured via /tmp/kust-plugin-config-52463179; exit status 1: exit status 1
       Type:  ComparisonError
   ```
3. Check for `Status: Sync:`. If there are log errors at `Status: Conditions:`, the `Status: Sync:` shows `Unknown` or `Error`:

   ```
   Status:
     Sync:
       Compared To:
         Destination:
           Namespace:  policies-sub
           Server:     https://kubernetes.default.svc
         Source:
           Path:             policies
           Repo URL:         https://git.com/ran-sites/policies/.git
           Target Revision:  master
       Status:               Error
   ```
4. When Red Hat Advanced Cluster Management (RHACM) recognizes that policies apply to a `ManagedCluster` object, the policy CR objects are applied to the cluster namespace. Check to see if the policies were copied to the cluster namespace:

   ```
   $ oc get policy -n $CLUSTER
   ```

   **Example output**

   ```
   NAME                                         REMEDIATION ACTION   COMPLIANCE STATE   AGE
   ztp-common.common-config-policy              inform               Compliant          13d
   ztp-common.common-subscriptions-policy       inform               Compliant          13d
   ztp-group.group-du-sno-config-policy         inform               Compliant          13d
   ztp-group.group-du-sno-validator-du-policy   inform               Compliant          13d
   ztp-site.example-sno-config-policy           inform               Compliant          13d
   ```

   RHACM copies all applicable policies into the cluster namespace. The copied policy names have the format: `<PolicyGenerator.Namespace>.<PolicyGenerator.Name>-<policyName>`.
5. Check the placement rule for any policies not copied to the cluster namespace. The `matchSelector` in the `Placement` for those policies should match labels on the `ManagedCluster` object:

   ```
   $ oc get Placement -n $NS
   ```
6. Note the `Placement` name appropriate for the missing policy, common, group, or site, using the following command:

   ```
   $ oc get Placement -n $NS <placement_rule_name> -o yaml
   ```

   * The status-decisions should include your cluster name.
   * The key-value pair of the `matchSelector` in the spec must match the labels on your managed cluster.
7. Check the labels on the `ManagedCluster` object by using the following command:

   ```
   $ oc get ManagedCluster $CLUSTER -o jsonpath='{.metadata.labels}' | jq
   ```
8. Check to see what policies are compliant by using the following command:

   ```
   $ oc get policy -n $CLUSTER
   ```

   If the `Namespace`, `OperatorGroup`, and `Subscription` policies are compliant but the Operator configuration policies are not, it is likely that the Operators did not install on the managed cluster. This causes the Operator configuration policies to fail to apply because the CRD is not yet applied to the spoke.

#### [10.1.9. Restarting policy reconciliation](#ztp-restarting-policies-reconciliation_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

You can restart policy reconciliation when unexpected compliance issues occur, for example, when the `ClusterGroupUpgrade` custom resource (CR) has timed out.

**Procedure**

1. A `ClusterGroupUpgrade` CR is generated in the namespace `ztp-install` by the Topology Aware Lifecycle Manager after the managed cluster becomes `Ready`:

   ```
   $ export CLUSTER=<clusterName>
   ```

   ```
   $ oc get clustergroupupgrades -n ztp-install $CLUSTER
   ```
2. If there are unexpected issues and the policies fail to become complaint within the configured timeout (the default is 4 hours), the status of the `ClusterGroupUpgrade` CR shows `UpgradeTimedOut`:

   ```
   $ oc get clustergroupupgrades -n ztp-install $CLUSTER -o jsonpath='{.status.conditions[?(@.type=="Ready")]}'
   ```
3. A `ClusterGroupUpgrade` CR in the `UpgradeTimedOut` state automatically restarts its policy reconciliation every hour. If you have changed your policies, you can start a retry immediately by deleting the existing `ClusterGroupUpgrade` CR. This triggers the automatic creation of a new `ClusterGroupUpgrade` CR that begins reconciling the policies immediately:

   ```
   $ oc delete clustergroupupgrades -n ztp-install $CLUSTER
   ```

Note

When the `ClusterGroupUpgrade` CR completes with status `UpgradeCompleted` and the managed cluster has the label `ztp-done` applied, you can make additional configuration changes by using `PolicyGenerator`. Deleting the existing `ClusterGroupUpgrade` CR will not make the TALM generate a new CR.

At this point, GitOps ZTP has completed its interaction with the cluster and any further interactions should be treated as an update and a new `ClusterGroupUpgrade` CR created for remediation of the policies.

#### [10.1.10. Changing applied managed cluster CRs using policies](#ztp-removing-content-from-managed-clusters_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

You can remove content from a custom resource (CR) that is deployed in a managed cluster through a policy.

By default, all `Policy` CRs created from a `PolicyGenerator` CR have the `complianceType` field set to `musthave`. A `musthave` policy without the removed content is still compliant because the CR on the managed cluster has all the specified content. With this configuration, when you remove content from a CR, TALM removes the content from the policy but the content is not removed from the CR on the managed cluster.

With the `complianceType` field to `mustonlyhave`, the policy ensures that the CR on the cluster is an exact match of what is specified in the policy.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have deployed a managed cluster from a hub cluster running RHACM.
* You have installed Topology Aware Lifecycle Manager on the hub cluster.

**Procedure**

1. Remove the content that you no longer need from the affected CRs. In this example, the `disableDrain: false` line was removed from the `SriovOperatorConfig` CR.

   **Example CR**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovOperatorConfig
   metadata:
     name: default
     namespace: openshift-sriov-network-operator
   spec:
     configDaemonNodeSelector:
       "node-role.kubernetes.io/$mcp": ""
     disableDrain: true
     enableInjector: true
     enableOperatorWebhook: true
   ```
2. Change the `complianceType` of the affected policies to `mustonlyhave` in the `acm-group-du-sno-ranGen.yaml` file.

   **Example YAML**

   ```
   # ...
   policyDefaults:
     complianceType: "mustonlyhave"
   # ...
   policies:
     - name: config-policy
       policyAnnotations:
         ran.openshift.io/ztp-deploy-wave: ""
       manifests:
         - path: source-crs/SriovOperatorConfig.yaml
   ```
3. Create a `ClusterGroupUpdates` CR and specify the clusters that must receive the CR changes::

   **Example ClusterGroupUpdates CR**

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-remove
     namespace: default
   spec:
     managedPolicies:
       - ztp-group.group-du-sno-config-policy
     enable: false
     clusters:
     - spoke1
     - spoke2
     remediationStrategy:
       maxConcurrency: 2
       timeout: 240
     batchTimeoutAction:
   ```
4. Create the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc create -f cgu-remove.yaml
   ```
5. When you are ready to apply the changes, for example, during an appropriate maintenance window, change the value of the `spec.enable` field to `true` by running the following command:

   ```
   $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-remove \
   --patch '{"spec":{"enable":true}}' --type=merge
   ```

**Verification**

1. Check the status of the policies by running the following command:

   ```
   $ oc get <kind> <changed_cr_name>
   ```

   **Example output**

   ```
   NAMESPACE   NAME                                                   REMEDIATION ACTION   COMPLIANCE STATE   AGE
   default     cgu-ztp-group.group-du-sno-config-policy               enforce                                 17m
   default     ztp-group.group-du-sno-config-policy                   inform               NonCompliant       15h
   ```

   When the `COMPLIANCE STATE` of the policy is `Compliant`, it means that the CR is updated and the unwanted content is removed.
2. Check that the policies are removed from the targeted clusters by running the following command on the managed clusters:

   ```
   $ oc get <kind> <changed_cr_name>
   ```

   If there are no results, the CR is removed from the managed cluster.

#### [10.1.11. Indication of done for GitOps ZTP installations](#ztp-definition-of-done-for-ztp-installations_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

GitOps Zero Touch Provisioning (ZTP) simplifies the process of checking the GitOps ZTP installation status for a cluster. The GitOps ZTP status moves through three phases: cluster installation, cluster configuration, and GitOps ZTP done.

Cluster installation phase
:   The cluster installation phase is shown by the `ManagedClusterJoined` and `ManagedClusterAvailable` conditions in the `ManagedCluster` CR . If the `ManagedCluster` CR does not have these conditions, or the condition is set to `False`, the cluster is still in the installation phase. Additional details about installation are available from the `AgentClusterInstall` and `ClusterDeployment` CRs. For more information, see "Troubleshooting GitOps ZTP".

Cluster configuration phase
:   The cluster configuration phase is shown by a `ztp-running` label applied the `ManagedCluster` CR for the cluster.

GitOps ZTP done
:   Cluster installation and configuration is complete in the GitOps ZTP done phase. This is shown by the removal of the `ztp-running` label and addition of the `ztp-done` label to the `ManagedCluster` CR. The `ztp-done` label shows that the configuration has been applied and the baseline DU configuration has completed cluster tuning.

    The change to the GitOps ZTP done state is conditional on the compliant state of a Red Hat Advanced Cluster Management (RHACM) validator inform policy. This policy captures the existing criteria for a completed installation and validates that it moves to a compliant state only when GitOps ZTP provisioning of the managed cluster is complete.

    The validator inform policy ensures the configuration of the cluster is fully applied and Operators have completed their initialization. The policy validates the following:

    * The target `MachineConfigPool` contains the expected entries and has finished updating. All nodes are available and not degraded.
    * The SR-IOV Operator has completed initialization as indicated by at least one `SriovNetworkNodeState` with `syncStatus: Succeeded`.
    * The PTP Operator daemon set exists.

#### [10.1.12. Configuring an OpenAPI schema for patching list fields by using the PolicyGenerator CR](#ztp-configuring-open-api-schema-for-patching_ztp-configuring-managed-clusters-policygenerator) Copy linkLink copied to clipboard!

You can configure an OpenAPI schema in the `PolicyGenerator` custom resource (CR) to control how list fields are merged when patching non-core Kubernetes objects.

By default, patching list fields can replace entire lists when the resource does not define merge behavior. An OpenAPI schema defines how list items are uniquely identified and merged during policy generation.

**Prerequisites**

* You have created a `PolicyGenerator` CR.
* You have access to a running cluster if you need to generate a schema.

**Procedure**

1. Obtain an OpenAPI schema for the resources that you want to patch:

   1. If an OpenAPI schema is available for the custom resource that you want to patch, use that schema file.
   2. If a schema is not available, generate it from an active cluster by running the following command:

      ```
      kustomize openapi fetch
      ```
2. Edit the generated schema file to keep only the resource definitions that you need to patch.

   Removing unrelated definitions simplifies the schema and reduces maintenance effort.
3. Define merge behavior for list fields that you want to patch. For each list of objects that you want to patch, add fields that specify how list items are uniquely identified and merged. For example:

   ```
   "x-kubernetes-patch-merge-key": "name"
   "x-kubernetes-patch-strategy": "merge"
   ```

   * `x-kubernetes-patch-merge-key` specifies the field that uniquely identifies an object in the list. For example, setting this field to `name` uses the `name` field to identify list items.
   * `x-kubernetes-patch-strategy` specifies how the patch is applied to the identified list item. The following are the supported values:

     + `merge`: Merges the fields from the patch into the existing list item.
     + `replace`: Replaces the entire list item identified by the merge key with the patch content.
4. Save the schema file in the directory that contains the `kustomization.yaml` file.
5. Reference the OpenAPI schema in the `kustomization.yaml` file:

   ```
   openapi:
     path: schema.json
   ```
6. Configure the OpenAPI schema path in the `PolicyGenerator` CR:

   **Example `PolicyGenerator` CR for patching list fields by using an OpenAPI schema**

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: PolicyGenerator
   metadata:
     name: policy-generator-example
   policies:
     - name: myapp
       manifests:
         - path: input-kustomize/
           patches: []
           openapi:
             path: schema.json
   ```
7. Generate or apply the policies by using the policy generator.

   The policy generator passes the OpenAPI schema to Kustomize to control how list fields are patched.

### [10.2. Advanced managed cluster configuration with PolicyGenerator resources](#ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

You can use `PolicyGenerator` CRs to deploy custom functionality in your managed clusters. Using RHACM and `PolicyGenerator` CRs is the recommended approach for managing policies and deploying them to managed clusters. This replaces the use of `PolicyGenTemplate` CRs for this purpose. For more information about `PolicyGenerator` resources, see the RHACM [Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/governance/policy-deployment#integrate-policy-generator) documentation.

#### [10.2.1. Deploying additional changes to clusters](#ztp-deploying-additional-changes-to-clusters_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

If you require cluster configuration changes outside of the base GitOps Zero Touch Provisioning (ZTP) pipeline configuration, there are three options:

Apply the additional configuration after the GitOps ZTP pipeline is complete
:   When the GitOps ZTP pipeline deployment is complete, the deployed cluster is ready for application workloads. At this point, you can install additional Operators and apply configurations specific to your requirements. Ensure that additional configurations do not negatively affect the performance of the platform or allocated CPU budget.

Add content to the GitOps ZTP library
:   The base source custom resources (CRs) that you deploy with the GitOps ZTP pipeline can be augmented with custom content as required.

Create extra manifests for the cluster installation
:   Extra manifests are applied during installation and make the installation process more efficient.

Important

Providing additional source CRs or modifying existing source CRs can significantly impact the performance or CPU profile of OpenShift Container Platform.

#### [10.2.2. Using PolicyGenerator CRs to override source CRs content](#ztp-using-pgt-to-update-source-crs_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

`PolicyGenerator` custom resources (CRs) allow you to overlay additional configuration details on top of the base source CRs provided with the GitOps plugin in the `ztp-site-generate` container. You can think of `PolicyGenerator` CRs as a logical merge or patch to the base CR. Use `PolicyGenerator` CRs to update a single field of the base CR, or overlay the entire contents of the base CR. You can update values and insert fields that are not in the base CR.

The following example procedure describes how to update fields in the generated `PerformanceProfile` CR for the reference configuration based on the `PolicyGenerator` CR in the `acm-group-du-sno-ranGen.yaml` file. Use the procedure as a basis for modifying other parts of the `PolicyGenerator` based on your requirements.

**Prerequisites**

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for Argo CD.

**Procedure**

1. Review the baseline source CR for existing content. You can review the source CRs listed in the reference `PolicyGenerator` CRs by extracting them from the GitOps Zero Touch Provisioning (ZTP) container.

   1. Create an `/out` folder:

      ```
      $ mkdir -p ./out
      ```
   2. Extract the source CRs:

      ```
      $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22.1 extract /home/ztp --tar | tar x -C ./out
      ```
2. Review the baseline `PerformanceProfile` CR in `./out/source-crs/PerformanceProfile.yaml`:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
     name: $name
     annotations:
       ran.openshift.io/ztp-deploy-wave: "10"
   spec:
     additionalKernelArgs:
     - "idle=poll"
     - "rcupdate.rcu_normal_after_boot=0"
     cpu:
       isolated: $isolated
       reserved: $reserved
     hugepages:
       defaultHugepagesSize: $defaultHugepagesSize
       pages:
         - size: $size
           count: $count
           node: $node
     machineConfigPoolSelector:
       pools.operator.machineconfiguration.openshift.io/$mcp: ""
     net:
       userLevelNetworking: true
     nodeSelector:
       node-role.kubernetes.io/$mcp: ''
     numa:
       topologyPolicy: "restricted"
     realTimeKernel:
       enabled: true
   ```

   Note

   Any fields in the source CR which contain `$…​` are removed from the generated CR if they are not provided in the `PolicyGenerator` CR.
3. Update the `PolicyGenerator` entry for `PerformanceProfile` in the `acm-group-du-sno-ranGen.yaml` reference file. The following example `PolicyGenerator` CR stanza supplies appropriate CPU specifications, sets the `hugepages` configuration, and adds a new field that sets `globallyDisableIrqLoadBalancing` to false.

   ```
   - path: source-crs/PerformanceProfile.yaml
     patches:
       - spec:
           # These must be tailored for the specific hardware platform
           cpu:
             isolated: "2-19,22-39"
             reserved: "0-1,20-21"
           hugepages:
             defaultHugepagesSize: 1G
             pages:
             - size: 1G
               count: 10
           globallyDisableIrqLoadBalancing: false
   ```
4. Commit the `PolicyGenerator` change in Git, and then push to the Git repository being monitored by the GitOps ZTP argo CD application.

   The GitOps ZTP application generates an RHACM policy that contains the generated `PerformanceProfile` CR. The contents of that CR are derived by merging the `metadata` and `spec` contents from the `PerformanceProfile` entry in the `PolicyGenerator` onto the source CR. The resulting CR has the following content:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
       name: openshift-node-performance-profile
   spec:
       additionalKernelArgs:
           - idle=poll
           - rcupdate.rcu_normal_after_boot=0
       cpu:
           isolated: 2-19,22-39
           reserved: 0-1,20-21
       globallyDisableIrqLoadBalancing: false
       hugepages:
           defaultHugepagesSize: 1G
           pages:
               - count: 10
                 size: 1G
       machineConfigPoolSelector:
           pools.operator.machineconfiguration.openshift.io/master: ""
       net:
           userLevelNetworking: true
       nodeSelector:
           node-role.kubernetes.io/master: ""
       numa:
           topologyPolicy: restricted
       realTimeKernel:
           enabled: true
   ```

   Note

   In the `/source-crs` folder that you extract from the `ztp-site-generate` container, the `$` syntax is not used for template substitution as implied by the syntax. Rather, if the `policyGen` tool sees the `$` prefix for a string and you do not specify a value for that field in the related `PolicyGenerator` CR, the field is omitted from the output CR entirely.

   An exception to this is the `$mcp` variable in `/source-crs` YAML files that is substituted with the specified value for `mcp` from the `PolicyGenerator` CR. For example, in `example/acmpolicygenerator/acm-group-du-standard-ranGen.yaml`, the value for `mcp` is `worker`:

   ```
   spec:
     bindingRules:
       group-du-standard: ""
     mcp: "worker"
   ```

   The `policyGen` tool replace instances of `$mcp` with `worker` in the output CRs.

#### [10.2.3. Adding custom content to the GitOps ZTP pipeline](#ztp-adding-new-content-to-gitops-ztp_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Perform the following procedure to add new content to the GitOps ZTP pipeline.

**Procedure**

1. Create a subdirectory named `source-crs` in the directory that contains the `kustomization.yaml` file for the `PolicyGenerator` custom resource (CR).
2. Add your user-provided CRs to the `source-crs` subdirectory, as shown in the following example:

   ```
   example
   └── acmpolicygenerator
       ├── dev.yaml
       ├── kustomization.yaml
       ├── mec-edge-sno1.yaml
       ├── sno.yaml
       └── source-crs
           ├── PaoCatalogSource.yaml
           ├── PaoSubscription.yaml
           ├── custom-crs
           |   ├── apiserver-config.yaml
           |   └── disable-nic-lldp.yaml
           └── elasticsearch
               ├── ElasticsearchNS.yaml
               └── ElasticsearchOperatorGroup.yaml
   ```

   The `source-crs` subdirectory must be in the same directory as the `kustomization.yaml` file.
3. Update the required `PolicyGenerator` CRs to include references to the content you added in the `source-crs/custom-crs` and `source-crs/elasticsearch` directories. For example:

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: PolicyGenerator
   metadata:
       name: group-dev
   placementBindingDefaults:
       name: group-dev-placement-binding
   policyDefaults:
       namespace: ztp-clusters
       placement:
           labelSelector:
               matchExpressions:
                   - key: dev
                     operator: In
                     values:
                       - "true"
       remediationAction: inform
       severity: low
       namespaceSelector:
           exclude:
               - kube-*
           include:
               - '*'
       evaluationInterval:
           compliant: 10m
           noncompliant: 10s
   policies:
       - name: group-dev-group-dev-cluster-log-ns
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/ClusterLogNS.yaml
       - name: group-dev-group-dev-cluster-log-operator-group
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/ClusterLogOperGroup.yaml
       - name: group-dev-group-dev-cluster-log-sub
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/ClusterLogSubscription.yaml
       - name: group-dev-group-dev-lso-ns
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/StorageNS.yaml
       - name: group-dev-group-dev-lso-operator-group
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/StorageOperGroup.yaml
       - name: group-dev-group-dev-lso-sub
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/StorageSubscription.yaml
       - name: group-dev-group-dev-pao-cat-source
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "1"
         manifests:
           - path: source-crs/PaoSubscriptionCatalogSource.yaml
             patches:
               - spec:
                   image: <container_image_url>
       - name: group-dev-group-dev-pao-ns
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/PaoSubscriptionNS.yaml
       - name: group-dev-group-dev-pao-sub
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: source-crs/PaoSubscription.yaml
       - name: group-dev-group-dev-elasticsearch-ns
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: elasticsearch/ElasticsearchNS.yaml
       - name: group-dev-group-dev-elasticsearch-operator-group
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: elasticsearch/ElasticsearchOperatorGroup.yaml
       - name: group-dev-group-dev-apiserver-config
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: custom-crs/apiserver-config.yaml
       - name: group-dev-group-dev-disable-nic-lldp
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "2"
         manifests:
           - path: custom-crs/disable-nic-lldp.yaml
   ```

   Set `policies.manifests.path` to include the relative path to the file from the `/source-crs` parent directory.
4. Commit the `PolicyGenerator` change in Git, and then push to the Git repository that is monitored by the GitOps ZTP Argo CD policies application.
5. Update the `ClusterGroupUpgrade` CR to include the changed `PolicyGenerator` and save it as `cgu-test.yaml`. The following example shows a generated `cgu-test.yaml` file.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: custom-source-cr
     namespace: ztp-clusters
   spec:
     managedPolicies:
       - group-dev-config-policy
     enable: true
     clusters:
     - cluster1
     remediationStrategy:
       maxConcurrency: 2
       timeout: 240
   ```
6. Apply the updated `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc apply -f cgu-test.yaml
   ```

**Verification**

* Check that the updates have succeeded by running the following command:

  ```
  $ oc get cgu -A
  ```

  The following example shows the output:

  ```
  NAMESPACE     NAME               AGE   STATE        DETAILS
  ztp-clusters  custom-source-cr   6s    InProgress   Remediating non-compliant policies
  ztp-install   cluster1           19h   Completed    All clusters are compliant with all the managed policies
  ```

#### [10.2.4. Configuring policy compliance evaluation timeouts for PolicyGenerator CRs](#ztp-configuring-pgt-compliance-eval-timeouts_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Use Red Hat Advanced Cluster Management (RHACM) installed on a hub cluster to monitor and report on whether your managed clusters are compliant with applied policies. RHACM uses policy templates to apply predefined policy controllers and policies. Policy controllers are Kubernetes custom resource definition (CRD) instances.

You can override the default policy evaluation intervals with `PolicyGenerator` custom resources (CRs). You configure duration settings that define how long a `ConfigurationPolicy` CR can be in a state of policy compliance or non-compliance before RHACM re-evaluates the applied cluster policies.

The GitOps Zero Touch Provisioning (ZTP) policy generator generates `ConfigurationPolicy` CR policies with pre-defined policy evaluation intervals. The default value for the `noncompliant` state is 10 seconds. The default value for the `compliant` state is 10 minutes. To disable the evaluation interval, set the value to `never`.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data.

**Procedure**

1. To configure the evaluation interval for all policies in a `PolicyGenerator` CR, set appropriate `compliant` and `noncompliant` values for the `evaluationInterval` field. For example:

   ```
   policyDefaults:
     evaluationInterval:
       compliant: 30m
       noncompliant: 45s
   ```

   Note

   You can also set `compliant` and `noncompliant` fields to `never` to stop evaluating the policy after it reaches particular compliance state.
2. To configure the evaluation interval for an individual policy object in a `PolicyGenerator` CR, add the `evaluationInterval` field and set appropriate values. For example:

   ```
   policies:
     - name: "sriov-sub-policy"
       manifests:
         - path: "SriovSubscription.yaml"
           evaluationInterval:
             compliant: never
             noncompliant: 10s
   ```
3. Commit the `PolicyGenerator` CRs files in the Git repository and push your changes.

**Verification**

Check that the managed spoke cluster policies are monitored at the expected intervals.

1. Log in as a user with `cluster-admin` privileges on the managed cluster.
2. Get the pods that are running in the `open-cluster-management-agent-addon` namespace. Run the following command:

   ```
   $ oc get pods -n open-cluster-management-agent-addon
   ```

   The following example shows the output:

   ```
   NAME                                         READY   STATUS    RESTARTS        AGE
   config-policy-controller-858b894c68-v4xdb    1/1     Running   22 (5d8h ago)   10d
   ```
3. Check the applied policies are being evaluated at the expected interval in the logs for the `config-policy-controller` pod:

   ```
   $ oc logs -n open-cluster-management-agent-addon config-policy-controller-858b894c68-v4xdb
   ```

   The following example shows the output:

   ```
   2022-05-10T15:10:25.280Z       info   configuration-policy-controller controllers/configurationpolicy_controller.go:166      Skipping the policy evaluation due to the policy not reaching the evaluation interval  {"policy": "compute-1-config-policy-config"}
   2022-05-10T15:10:25.280Z       info   configuration-policy-controller controllers/configurationpolicy_controller.go:166      Skipping the policy evaluation due to the policy not reaching the evaluation interval  {"policy": "compute-1-common-compute-1-catalog-policy-config"}
   ```

#### [10.2.5. Signalling GitOps ZTP cluster deployment completion with validator inform policies](#ztp-creating-a-validator-inform-policy_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Create a validator inform policy that signals when the GitOps Zero Touch Provisioning (ZTP) installation and configuration of the deployed cluster is complete. This policy can be used for deployments of single-node OpenShift clusters, three-node clusters, and standard clusters.

**Procedure**

1. Create a standalone `PolicyGenerator` custom resource (CR) that contains the source file `validatorCRs/informDuValidator.yaml`. You only need one standalone `PolicyGenerator` CR for each cluster type. For example, this CR applies a validator inform policy for single-node OpenShift clusters:

   Example single-node cluster validator inform policy CR (acm-group-du-sno-validator-ranGen.yaml):

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: PolicyGenerator
   metadata:
       name: group-du-sno-validator-latest
   placementBindingDefaults:
       name: group-du-sno-validator-latest-placement-binding
   policyDefaults:
       namespace: ztp-group
       placement:
           labelSelector:
               matchExpressions:
                   - key: du-profile
                     operator: In
                     values:
                       - latest
                   - key: group-du-sno
                     operator: Exists
                   - key: ztp-done
                     operator: DoesNotExist
       remediationAction: inform
       severity: low
       namespaceSelector:
           exclude:
               - kube-*
           include:
               - '*'
       evaluationInterval:
           compliant: 10m
           noncompliant: 10s
   policies:
       - name: group-du-sno-validator-latest-du-policy
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "10000"
         evaluationInterval:
           compliant: 5s
         manifests:
           - path: source-crs/validatorCRs/informDuValidator-MCP-master.yaml
   ```
2. Commit the `PolicyGenerator` CR file in your Git repository and push the changes.

#### [10.2.6. Configuring power states using PolicyGenerator CRs](#ztp-using-pgt-to-configure-power-saving-states_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

For low latency and high-performance edge deployments, it is necessary to disable or limit C-states and P-states.

With this configuration, the CPU runs at a constant frequency, which is typically the maximum turbo frequency. This ensures that the CPU is always running at its maximum speed, which results in high performance and low latency. This leads to the best latency for workloads. However, this also leads to the highest power consumption, which might not be necessary for all workloads.

Workloads can be classified as critical or non-critical, with critical workloads requiring disabled C-state and P-state settings for high performance and low latency, while non-critical workloads use C-state and P-state settings for power savings at the expense of some latency and performance. You can configure the following three power states using GitOps Zero Touch Provisioning (ZTP):

* High-performance mode provides ultra low latency at the highest power consumption.
* Performance mode provides low latency at a relatively high power consumption.
* Power saving balances reduced power consumption with increased latency.

The default configuration is for a low latency, performance mode.

`PolicyGenerator` custom resources (CRs) allow you to overlay additional configuration details onto the base source CRs provided with the GitOps plugin in the `ztp-site-generate` container.

Configure the power states by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenerator` CR in the `acm-group-du-sno-ranGen.yaml`.

The following common prerequisites apply to configuring all three power states:

* You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for Argo CD.
* You have followed the procedure described in "Preparing the GitOps ZTP site configuration repository".

##### [10.2.6.1. Configuring performance mode using PolicyGenerator CRs](#ztp-using-pgt-to-configure-performance-mode_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Follow this example to set performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenerator` CR in the `acm-group-du-sno-ranGen.yaml`.

Performance mode provides low latency at a relatively high power consumption.

**Prerequisites**

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

**Procedure**

1. Update the `PolicyGenerator` entry for `PerformanceProfile` in the `acm-group-du-sno-ranGen.yaml` reference file in `out/argocd/example/acmpolicygenerator//` as follows to set performance mode.

   ```
   - path: source-crs/PerformanceProfile.yaml
     patches:
       - spec:
           workloadHints:
                realTime: true
                highPowerConsumption: false
                perPodPowerManagement: false
   ```
2. Commit the `PolicyGenerator` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

##### [10.2.6.2. Configuring high-performance mode using PolicyGenerator CRs](#ztp-using-pgt-to-configure-high-performance-mode_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Follow this example to set high performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenerator` CR in the `acm-group-du-sno-ranGen.yaml`.

High performance mode provides ultra low latency at the highest power consumption.

**Prerequisites**

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

**Procedure**

1. Update the `PolicyGenerator` entry for `PerformanceProfile` in the `acm-group-du-sno-ranGen.yaml` reference file in `out/argocd/example/acmpolicygenerator/` as follows to set high-performance mode.

   ```
   - path: source-crs/PerformanceProfile.yaml
     patches:
       - spec:
           workloadHints:
                realTime: true
                highPowerConsumption: true
                perPodPowerManagement: false
   ```
2. Commit the `PolicyGenerator` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

##### [10.2.6.3. Configuring power saving mode using PolicyGenerator CRs](#ztp-using-pgt-to-configure-power-saving-mode_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Follow this example to set power saving mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenerator` CR in the `acm-group-du-sno-ranGen.yaml`.

The power saving mode balances reduced power consumption with increased latency.

**Prerequisites**

* You enabled C-states and OS-controlled P-states in the BIOS.

**Procedure**

1. Update the `PolicyGenerator` entry for `PerformanceProfile` in the `acm-group-du-sno-ranGen.yaml` reference file in `out/argocd/example/acmpolicygenerator/` as follows to configure power saving mode. It is recommended to configure the CPU governor for the power saving mode through the additional kernel arguments object.

   ```
   - path: source-crs/PerformanceProfile.yaml
     patches:
       - spec:
           # ...
           workloadHints:
             realTime: true
             highPowerConsumption: false
             perPodPowerManagement: true
           # ...
           additionalKernelArgs:
             - # ...
             - "cpufreq.default_governor=schedutil"
   ```

   The `schedutil` governor is recommended, however, you can also use other governors, including `ondemand` and `powersave`.
2. Commit the `PolicyGenerator` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

**Verification**

1. Select a worker node in your deployed cluster from the list of nodes identified by using the following command:

   ```
   $ oc get nodes
   ```
2. Log in to the node by using the following command:

   ```
   $ oc debug node/<node-name>
   ```

   Replace `<node-name>` with the name of the node you want to verify the power state on.
3. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths as shown in the following example:

   ```
   # chroot /host
   ```
4. Run the following command to verify the applied power state:

   ```
   # cat /proc/cmdline
   ```

   For power saving mode, verify that the output includes `intel_pstate=passive`.

##### [10.2.6.4. Maximizing power savings](#ztp-using-pgt-to-maximize-power-savings-mode_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Limiting the maximum CPU frequency is recommended to achieve maximum power savings.

Enabling C-states on the non-critical workload CPUs without restricting the maximum CPU frequency negates much of the power savings by boosting the frequency of the critical CPUs.

Maximize power savings by updating the `sysfs` plugin fields, setting an appropriate value for `max_perf_pct` in the `TunedPerformancePatch` CR for the reference configuration. This example based on the `acm-group-du-sno-ranGen.yaml` describes the procedure to follow to restrict the maximum CPU frequency.

**Prerequisites**

* You have configured power savings mode as described in "Using PolicyGenerator CRs to configure power savings mode".

**Procedure**

1. Update the `PolicyGenerator` entry for `TunedPerformancePatch` in the `acm-group-du-sno-ranGen.yaml` reference file in `out/argocd/example/acmpolicygenerator/`. To maximize power savings, add `max_perf_pct` as shown in the following example:

   ```
   - path: source-crs/TunedPerformancePatch.yaml
     patches:
       - spec:
         profile:
           - name: performance-patch
             data: |
               # ...
               [sysfs]
               /sys/devices/system/cpu/intel_pstate/max_perf_pct=<x>
   ```

   The `max_perf_pct` controls the maximum frequency the `cpufreq` driver is allowed to set as a percentage of the maximum supported CPU frequency. This value applies to all CPUs. You can check the maximum supported frequency in `/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq`. As a starting point, you can use a percentage that caps all CPUs at the `All Cores Turbo` frequency. The `All Cores Turbo` frequency is the frequency that all cores run at when the cores are all fully occupied.

   Note

   To maximize power savings, set a lower value. Setting a lower value for `max_perf_pct` limits the maximum CPU frequency, thereby reducing power consumption, but also potentially impacting performance. Experiment with different values and monitor the system’s performance and power consumption to find the optimal setting for your use-case.
2. Commit the `PolicyGenerator` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

#### [10.2.7. Configuring LVM Storage using PolicyGenerator CRs](#ztp-provisioning-lvm-storage_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

You can configure Logical Volume Manager (LVM) Storage for managed clusters that you deploy with GitOps Zero Touch Provisioning (ZTP).

Note

You use LVM Storage to persist event subscriptions when you use PTP events or bare-metal hardware events with HTTP transport.

Use the Local Storage Operator for persistent storage that uses local volumes in distributed units.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.
* Create a Git repository where you manage your custom site configuration data.

**Procedure**

1. To configure LVM Storage for new managed clusters, add the following YAML to `policies.manifests` in the `acm-common-ranGen.yaml` file:

   ```
   - name: subscription-policies
     policyAnnotations:
       ran.openshift.io/ztp-deploy-wave: "2"
     manifests:
       - path: source-crs/StorageLVMOSubscriptionNS.yaml
       - path: source-crs/StorageLVMOSubscriptionOperGroup.yaml
       - path: source-crs/StorageLVMOSubscription.yaml
         spec:
           name: lvms-operator
           channel: stable-4.22
   ```

   Note

   The Storage LVMO subscription is deprecated. In future releases of OpenShift Container Platform, the storage LVMO subscription will not be available. Instead, you must use the Storage LVMS subscription.

   In OpenShift Container Platform 4.22, you can use the Storage LVMS subscription instead of the LVMO subscription. The LVMS subscription does not require manual overrides in the `acm-common-ranGen.yaml` file. Add the following YAML to `policies.manifests` in the `acm-common-ranGen.yaml` file to use the Storage LVMS subscription:

   ```
   - path: source-crs/StorageLVMSubscriptionNS.yaml
   - path: source-crs/StorageLVMSubscriptionOperGroup.yaml
   - path: source-crs/StorageLVMSubscription.yaml
   ```
2. Add the `LVMCluster` CR to `policies.manifests` in your specific group or individual site configuration file. For example, in the `acm-group-du-sno-ranGen.yaml` file, add the following:

   ```
   - fileName: StorageLVMCluster.yaml
     policyName: "lvms-config"
       metadata:
         name: "lvms-storage-cluster-config"
           spec:
             storage:
               deviceClasses:
               - name: vg1
                 thinPoolConfig:
                   name: thin-pool-1
                   sizePercent: 90
                   overprovisionRatio: 10
   ```

   This example configuration creates a volume group (`vg1`) with all the available devices, except the disk where OpenShift Container Platform is installed. A thin-pool logical volume is also created.
3. Merge any other required changes and files with your custom site repository.
4. Commit the `PolicyGenerator` changes in Git, and then push the changes to your site configuration repository to deploy LVM Storage to new sites using GitOps ZTP.

#### [10.2.8. Configuring PTP events with PolicyGenerator CRs](#ztp-advanced-policy-config-ptp_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

You can use the GitOps ZTP pipeline to configure PTP events that use HTTP transport.

##### [10.2.8.1. Configuring PTP events that use HTTP transport](#ztp-configuring-ptp-fast-events_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

You can configure PTP events that use HTTP transport on managed clusters that you deploy with the GitOps Zero Touch Provisioning (ZTP) pipeline.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data.

**Procedure**

1. Apply the following `PolicyGenerator` changes to `acm-group-du-3node-ranGen.yaml`, `acm-group-du-sno-ranGen.yaml`, or `acm-group-du-standard-ranGen.yaml` files according to your requirements:

   1. In `policies.manifests`, add the `PtpOperatorConfig` CR file that configures the transport host:

      ```
      - path: source-crs/PtpOperatorConfigForEvent.yaml
        patches:
        - metadata:
            name: default
            namespace: openshift-ptp
            annotations:
              ran.openshift.io/ztp-deploy-wave: "10"
          spec:
            daemonNodeSelector:
              node-role.kubernetes.io/$mcp: ""
            ptpEventConfig:
              enableEventPublisher: true
              transportHost: "http://ptp-event-publisher-service-NODE_NAME.openshift-ptp.svc.cluster.local:9043"
      ```

      Note

      In OpenShift Container Platform 4.13 or later, you do not need to set the `transportHost` field in the `PtpOperatorConfig` resource when you use HTTP transport with PTP events.
   2. Configure the `linuxptp` and `phc2sys` for the PTP clock type and interface. For example, add the following YAML into `policies.manifests`:

      ```
      - path: source-crs/PtpConfigSlave.yaml
        patches:
        - metadata:
            name: "du-ptp-slave"
          spec:
            recommend:
            - match:
              - nodeLabel: node-role.kubernetes.io/master
              priority: 4
              profile: slave
            profile:
            - name: "slave"
              # This interface must match the hardware in this group
              interface: "ens5f0"
              ptp4lOpts: "-2 -s --summary_interval -4"
              phc2sysOpts: "-a -r -n 24"
              ptpSchedulingPolicy: SCHED_FIFO
              ptpSchedulingPriority: 10
              ptpSettings:
                logReduce: "true"
              ptp4lConf: |
                [global]
                #
                # Default Data Set
                #
                twoStepFlag 1
                slaveOnly 1
                priority1 128
                priority2 128
                domainNumber 24
                #utc_offset 37
                clockClass 255
                clockAccuracy 0xFE
                offsetScaledLogVariance 0xFFFF
                free_running 0
                freq_est_interval 1
                dscp_event 0
                dscp_general 0
                dataset_comparison G.8275.x
                G.8275.defaultDS.localPriority 128
                #
                # Port Data Set
                #
                logAnnounceInterval -3
                logSyncInterval -4
                logMinDelayReqInterval -4
                logMinPdelayReqInterval -4
                announceReceiptTimeout 3
                syncReceiptTimeout 0
                delayAsymmetry 0
                fault_reset_interval -4
                neighborPropDelayThresh 20000000
                masterOnly 0
                G.8275.portDS.localPriority 128
                #
                # Run time options
                #
                assume_two_step 0
                logging_level 6
                path_trace_enabled 0
                follow_up_info 0
                hybrid_e2e 0
                inhibit_multicast_service 0
                net_sync_monitor 0
                tc_spanning_tree 0
                tx_timestamp_timeout 50
                unicast_listen 0
                unicast_master_table 0
                unicast_req_duration 3600
                use_syslog 1
                verbose 0
                summary_interval 0
                kernel_leap 1
                check_fup_sync 0
                clock_class_threshold 7
                #
                # Servo Options
                #
                pi_proportional_const 0.0
                pi_integral_const 0.0
                pi_proportional_scale 0.0
                pi_proportional_exponent -0.3
                pi_proportional_norm_max 0.7
                pi_integral_scale 0.0
                pi_integral_exponent 0.4
                pi_integral_norm_max 0.3
                step_threshold 2.0
                first_step_threshold 0.00002
                max_frequency 900000000
                clock_servo pi
                sanity_freq_limit 200000000
                ntpshm_segment 0
                #
                # Transport options
                #
                transportSpecific 0x0
                ptp_dst_mac 01:1B:19:00:00:00
                p2p_dst_mac 01:80:C2:00:00:0E
                udp_ttl 1
                udp6_scope 0x0E
                uds_address /var/run/ptp4l
                #
                # Default interface options
                #
                clock_type OC
                network_transport L2
                delay_mechanism E2E
                time_stamping hardware
                tsproc_mode filter
                delay_filter moving_median
                delay_filter_length 10
                egressLatency 0
                ingressLatency 0
                boundary_clock_jbod 0
                #
                # Clock description
                #
                productDescription ;;
                revisionData ;;
                manufacturerIdentity 00:00:00
                userDescription ;
                timeSource 0xA0
            ptpClockThreshold:
              holdOverTimeout: 30 # seconds
              maxOffsetThreshold: 100  # nano seconds
              minOffsetThreshold: -100
      ```

      where:

      `path`
      :   Specifies `PtpConfigMaster.yaml` or `PtpConfigSlave.yaml` depending on your requirements. For configurations based on `acm-group-du-sno-ranGen.yaml` or `acm-group-du-3node-ranGen.yaml`, use `PtpConfigSlave.yaml`.

      `patches.spec.profile.interface`
      :   Specifies the device specific interface name.

      `patches.spec.profile.ptp4lOpts`
      :   Specifies the ptp4l options. You must append the `--summary_interval -4` value to `ptp4lOpts` in `.spec.sourceFiles.spec.profile` to enable PTP fast events.

      `patches.spec.profile.phc2sysOpts`
      :   Specifies the required `phc2sysOpts` values. `-m` prints messages to `stdout`. The `linuxptp-daemon` `DaemonSet` parses the logs and generates Prometheus metrics.

      `patches.spec.ptpClockThreshold`
      :   Specifies the PTP clock threshold settings. Optional. If the `ptpClockThreshold` stanza is not present, default values are used for the `ptpClockThreshold` fields. The stanza shows default `ptpClockThreshold` values. The `ptpClockThreshold` values configure how long after the PTP master clock is disconnected before PTP events are triggered. `holdOverTimeout` is the time value in seconds before the PTP clock event state changes to `FREERUN` when the PTP master clock is disconnected. The `maxOffsetThreshold` and `minOffsetThreshold` settings configure offset values in nanoseconds that compare against the values for `CLOCK_REALTIME` (`phc2sys`) or master offset (`ptp4l`). When the `ptp4l` or `phc2sys` offset value is outside this range, the PTP clock state is set to `FREERUN`. When the offset value is within this range, the PTP clock state is set to `LOCKED`.
2. Merge any other required changes and files with your custom site repository.
3. Push the changes to your site configuration repository to deploy PTP fast events to new sites using GitOps ZTP.

#### [10.2.9. Configuring the Image Registry Operator for local caching of images](#ztp-add-local-reg-for-sno-duprofile_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

OpenShift Container Platform manages image caching using a local registry. In edge computing use cases, clusters are often subject to bandwidth restrictions when communicating with centralized image registries, which might result in long image download times.

Long download times are unavoidable during initial deployment. Over time, there is a risk that CRI-O will erase the `/var/lib/containers/storage` directory in the case of an unexpected shutdown. To address long image download times, you can create a local image registry on remote managed clusters using GitOps Zero Touch Provisioning (ZTP). This is useful in Edge computing scenarios where clusters are deployed at the far edge of the network.

Before you can set up the local image registry with GitOps ZTP, you need to configure disk partitioning in the `ClusterInstance` CR that you use to install the remote managed cluster. After installation, you configure the local image registry using a `PolicyGenerator` CR. Then, the GitOps ZTP pipeline creates Persistent Volume (PV) and Persistent Volume Claim (PVC) CRs and patches the `imageregistry` configuration.

Note

The local image registry can only be used for user application images and cannot be used for the OpenShift Container Platform or Operator Lifecycle Manager operator images.

##### [10.2.9.1. Configuring disk partitioning with ClusterInstance](#ztp-configuring-disk-partitioning_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Configure disk partitioning for a managed cluster using a `ClusterInstance` CR and GitOps Zero Touch Provisioning (ZTP). The disk partition details in the `ClusterInstance` CR must match the underlying disk.

Important

You must complete this procedure at installation time.

**Prerequisites**

* Install Butane.

**Procedure**

1. Create the `storage.bu` file.

   ```
   variant: fcos
   version: 1.3.0
   storage:
     disks:
     - device: /dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0
       wipe_table: false
       partitions:
       - label: var-lib-containers
         start_mib: <start_of_partition>
         size_mib: <partition_size>
     filesystems:
       - path: /var/lib/containers
         device: /dev/disk/by-partlabel/var-lib-containers
         format: xfs
         wipe_filesystem: true
         with_mount_unit: true
         mount_options:
           - defaults
           - prjquota
   ```

   where:

   `<device>`
   :   Specifies the root disk.

   `<start_of_partition>`
   :   Specifies the start of the partition in MiB. If the value is too small, the installation fails.

   `<partition_size>`
   :   Specifies the size of the partition. If the value is too small, the deployment fails.
2. Convert the `storage.bu` to an Ignition file by running the following command:

   ```
   $ butane storage.bu
   ```

   The following example shows the output:

   ```
   {"ignition":{"version":"3.2.0"},"storage":{"disks":[{"device":"/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0","partitions":[{"label":"var-lib-containers","sizeMiB":0,"startMiB":250000}],"wipeTable":false}],"filesystems":[{"device":"/dev/disk/by-partlabel/var-lib-containers","format":"xfs","mountOptions":["defaults","prjquota"],"path":"/var/lib/containers","wipeFilesystem":true}]},"systemd":{"units":[{"contents":"# # Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target","enabled":true,"name":"var-lib-containers.mount"}]}}
   ```
3. Use a tool such as [JSON Pretty Print](https://jsonformatter.org/json-pretty-print) to convert the output into JSON format.
4. Copy the output into the `spec.nodes[].ignitionConfigOverride` field in the `ClusterInstance` CR, as shown in the following example:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-sno"
     namespace: "example-sno"
   spec:
     # ...
     nodes:
       - hostName: "node1.example.com"
         role: "master"
         ignitionConfigOverride: |
             {
               "ignition": {
                 "version": "3.2.0"
               },
               "storage": {
                 "disks": [
                   {
                     "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                     "partitions": [
                       {
                         "label": "var-lib-containers",
                         "sizeMiB": 0,
                         "startMiB": 250000
                       }
                     ],
                     "wipeTable": false
                   }
                 ],
                 "filesystems": [
                   {
                     "device": "/dev/disk/by-partlabel/var-lib-containers",
                     "format": "xfs",
                     "mountOptions": [
                       "defaults",
                       "prjquota"
                     ],
                     "path": "/var/lib/containers",
                     "wipeFilesystem": true
                   }
                 ]
               },
               "systemd": {
                 "units": [
                   {
                     "contents": "# # Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                     "enabled": true,
                     "name": "var-lib-containers.mount"
                   }
                 ]
               }
             }
   ```

   Note

   If the `spec.nodes[].ignitionConfigOverride` field does not exist, create it.

**Verification**

1. During or after installation, verify on the hub cluster that the `BareMetalHost` object shows the annotation by running the following command:

   ```
   $ oc get bmh -n my-sno-ns my-sno -ojson | jq '.metadata.annotations["bmac.agent-install.openshift.io/ignition-config-overrides"]
   ```

   The following example shows the output:

   ```
   "{\"ignition\":{\"version\":\"3.2.0\"},\"storage\":{\"disks\":[{\"device\":\"/dev/disk/by-id/wwn-0x6b07b250ebb9d0002a33509f24af1f62\",\"partitions\":[{\"label\":\"var-lib-containers\",\"sizeMiB\":0,\"startMiB\":250000}],\"wipeTable\":false}],\"filesystems\":[{\"device\":\"/dev/disk/by-partlabel/var-lib-containers\",\"format\":\"xfs\",\"mountOptions\":[\"defaults\",\"prjquota\"],\"path\":\"/var/lib/containers\",\"wipeFilesystem\":true}]},\"systemd\":{\"units\":[{\"contents\":\"# Generated by Butane\\n[Unit]\\nRequires=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\nAfter=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\n\\n[Mount]\\nWhere=/var/lib/containers\\nWhat=/dev/disk/by-partlabel/var-lib-containers\\nType=xfs\\nOptions=defaults,prjquota\\n\\n[Install]\\nRequiredBy=local-fs.target\",\"enabled\":true,\"name\":\"var-lib-containers.mount\"}]}}"
   ```
2. After installation, check the single-node OpenShift disk status.

   1. Enter into a debug session on the single-node OpenShift node by running the following command. This step instantiates a debug pod called `<node_name>-debug`:

      ```
      $ oc debug node/my-sno-node
      ```
   2. Set `/host` as the root directory within the debug shell by running the following command. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths:

      ```
      # chroot /host
      ```
   3. List information about all available block devices by running the following command:

      ```
      # lsblk
      ```

      The following example shows the output:

      ```
      NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
      sda      8:0    0 446.6G  0 disk
      ├─sda1   8:1    0     1M  0 part
      ├─sda2   8:2    0   127M  0 part
      ├─sda3   8:3    0   384M  0 part /boot
      ├─sda4   8:4    0 243.6G  0 part /var
      │                                /sysroot/ostree/deploy/rhcos/var
      │                                /usr
      │                                /etc
      │                                /
      │                                /sysroot
      └─sda5   8:5    0 202.5G  0 part /var/lib/containers
      ```
   4. Display information about the file system disk space usage by running the following command:

      ```
      # df -h
      ```

      The following example shows the output:

      ```
      Filesystem      Size  Used Avail Use% Mounted on
      devtmpfs        4.0M     0  4.0M   0% /dev
      tmpfs           126G   84K  126G   1% /dev/shm
      tmpfs            51G   93M   51G   1% /run
      /dev/sda4       244G  5.2G  239G   3% /sysroot
      tmpfs           126G  4.0K  126G   1% /tmp
      /dev/sda5       203G  119G   85G  59% /var/lib/containers
      /dev/sda3       350M  110M  218M  34% /boot
      tmpfs            26G     0   26G   0% /run/user/1000
      ```

##### [10.2.9.2. Configuring the image registry using PolicyGenerator CRs](#ztp-configuring-pgt-image-registry_ztp-advanced-policygenerator-config) Copy linkLink copied to clipboard!

Use `PolicyGenerator` (PGT) CRs to apply the CRs required to configure the image registry and patch the `imageregistry` configuration.

**Prerequisites**

* You have configured a disk partition in the managed cluster.
* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data for use with GitOps Zero Touch Provisioning (ZTP).

**Procedure**

1. Configure the storage class, persistent volume claim, persistent volume, and image registry configuration in the appropriate `PolicyGenerator` CR. For example, to configure an individual site, add the following YAML to the file `acm-example-sno-site.yaml`:

   ```
   sourceFiles:
     # storage class
     - fileName: StorageClass.yaml
       policyName: "sc-for-image-registry"
       metadata:
         name: image-registry-sc
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
     # persistent volume claim
     - fileName: StoragePVC.yaml
       policyName: "pvc-for-image-registry"
       metadata:
         name: image-registry-pvc
         namespace: openshift-image-registry
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
       spec:
         accessModes:
           - ReadWriteMany
         resources:
           requests:
             storage: 100Gi
         storageClassName: image-registry-sc
         volumeMode: Filesystem
     # persistent volume
     - fileName: ImageRegistryPV.yaml
       policyName: "pv-for-image-registry"
       metadata:
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
     - fileName: ImageRegistryConfig.yaml
       policyName: "config-for-image-registry"
       complianceType: musthave
       metadata:
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
       spec:
         storage:
           pvc:
             claim: "image-registry-pvc"
   ```

   where:

   `ran.openshift.io/ztp-deploy-wave: "100"`
   :   Sets the appropriate value for `ztp-deploy-wave` depending on whether you are configuring image registries at the site, common, or group level. `ztp-deploy-wave: "100"` is suitable for development or testing because it allows you to group the referenced source files together.

   `ImageRegistryPV.yaml`
   :   In `ImageRegistryPV.yaml`, ensure that the `spec.local.path` field is set to `/var/imageregistry` to match the value set for the `mount_point` field in the `ClusterInstance` CR.

   Important

   Do not set `complianceType: mustonlyhave` for the `- fileName: ImageRegistryConfig.yaml` configuration. This can cause the registry pod deployment to fail.
2. Commit the `PolicyGenerator` change in Git, and then push to the Git repository being monitored by the GitOps ZTP ArgoCD application.

**Verification**

Use the following steps to troubleshoot errors with the local image registry on the managed clusters:

* Verify successful login to the registry while logged in to the managed cluster. Run the following commands:

  1. Export the managed cluster name:

     ```
     $ cluster=<managed_cluster_name>
     ```
  2. Get the managed cluster `kubeconfig` details:

     ```
     $ oc get secret -n $cluster $cluster-admin-password -o jsonpath='{.data.password}' | base64 -d > kubeadmin-password-$cluster
     ```
  3. Download and export the cluster `kubeconfig`:

     ```
     $ oc get secret -n $cluster $cluster-admin-kubeconfig -o jsonpath='{.data.kubeconfig}' | base64 -d > kubeconfig-$cluster && export KUBECONFIG=./kubeconfig-$cluster
     ```
  4. Verify access to the image registry from the managed cluster. See "Accessing the registry".
* Check that the `Config` CRD in the `imageregistry.operator.openshift.io` group instance is not reporting errors. Run the following command while logged in to the managed cluster:

  ```
  $ oc get image.config.openshift.io cluster -o yaml
  ```

  The following example shows the output:

  ```
  apiVersion: config.openshift.io/v1
  kind: Image
  metadata:
    annotations:
      include.release.openshift.io/ibm-cloud-managed: "true"
      include.release.openshift.io/self-managed-high-availability: "true"
      include.release.openshift.io/single-node-developer: "true"
      release.openshift.io/create-only: "true"
    creationTimestamp: "2021-10-08T19:02:39Z"
    generation: 5
    name: cluster
    resourceVersion: "688678648"
    uid: 0406521b-39c0-4cda-ba75-873697da75a4
  spec:
    additionalTrustedCA:
      name: acm-ice
  ```
* Check that the `PersistentVolumeClaim` on the managed cluster is populated with data. Run the following command while logged in to the managed cluster:

  ```
  $ oc get pv image-registry-sc
  ```
* Check that the `registry*` pod is running and is located under the `openshift-image-registry` namespace.

  ```
  $ oc get pods -n openshift-image-registry | grep registry*
  ```

  The following example shows the output:

  ```
  cluster-image-registry-operator-68f5c9c589-42cfg   1/1     Running     0          8d
  image-registry-5f8987879-6nx6h                     1/1     Running     0          8d
  ```
* Check that the disk partition on the managed cluster is correct:

  1. Open a debug shell to the managed cluster:

     ```
     $ oc debug node/sno-1.example.com
     ```
  2. Run `lsblk` to check the host disk partitions:

     ```
     sh-4.4# lsblk
     NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
     sda      8:0    0 446.6G  0 disk
       |-sda1   8:1    0     1M  0 part
       |-sda2   8:2    0   127M  0 part
       |-sda3   8:3    0   384M  0 part /boot
       |-sda4   8:4    0 336.3G  0 part /sysroot
       `-sda5   8:5    0 100.1G  0 part /var/imageregistry
     sdb      8:16   0 446.6G  0 disk
     sr0     11:0    1   104M  0 rom
     ```

     The `/var/imageregistry` mount point indicates that the disk is correctly partitioned.

### [10.3. Updating managed clusters in a disconnected environment with PolicyGenerator resources and TALM](#ztp-topology-aware-lifecycle-manager-pg) Copy linkLink copied to clipboard!

You can use the Topology Aware Lifecycle Manager (TALM) to manage the software lifecycle of managed clusters that you have deployed using GitOps Zero Touch Provisioning (ZTP) and Topology Aware Lifecycle Manager (TALM). TALM uses Red Hat Advanced Cluster Management (RHACM) PolicyGenerator policies to manage and control changes applied to target clusters.

#### [10.3.1. Setting up the disconnected environment](#talo-platform-prepare-for-update-env-setup_ztp-talm-pg) Copy linkLink copied to clipboard!

TALM can perform both platform and Operator updates.

You must mirror both the platform image and Operator images that you want to update to in your mirror registry before you can use TALM to update your disconnected clusters.

**Procedure**

* For platform updates, you must perform the following steps:

  1. Mirror the required OpenShift Container Platform image repository. Ensure that the required platform image is mirrored by following the "Mirroring the OpenShift Container Platform image repository" procedure linked in the Additional resources. Save the contents of the `imageContentSources` section in the `imageContentSources.yaml` file:

     The following is example output:

     ```
     imageContentSources:
      - mirrors:
        - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
        source: quay.io/openshift-release-dev/ocp-release
      - mirrors:
        - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
        source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
     ```
  2. Save the image signature of the required platform image that was mirrored. You must add the image signature to the `PolicyGenerator` CR for platform updates. To get the image signature, perform the following steps:

     1. Specify the required OpenShift Container Platform tag by running the following command:

        ```
        $ OCP_RELEASE_NUMBER=<release_version>
        ```
     2. Specify the architecture of the cluster by running the following command:

        ```
        $ ARCHITECTURE=<cluster_architecture>
        ```

        + `<cluster_architecture>` specifies the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`.
     3. Get the release image digest from Quay by running the following command

        ```
        $ DIGEST="$(oc adm release info quay.io/openshift-release-dev/ocp-release:${OCP_RELEASE_NUMBER}-${ARCHITECTURE} | sed -n 's/Pull From: .*@//p')"
        ```
     4. Set the digest algorithm by running the following command:

        ```
        $ DIGEST_ALGO="${DIGEST%%:*}"
        ```
     5. Set the digest signature by running the following command:

        ```
        $ DIGEST_ENCODED="${DIGEST#*:}"
        ```
     6. Get the image signature from the [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/) website by running the following command:

        ```
        $ SIGNATURE_BASE64=$(curl -s "https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/${DIGEST_ALGO}=${DIGEST_ENCODED}/signature-1" | base64 -w0 && echo)
        ```
     7. Save the image signature to the `checksum-<OCP_RELEASE_NUMBER>.yaml` file by running the following commands:

        ```
        $ cat >checksum-${OCP_RELEASE_NUMBER}.yaml <<EOF
        ```

        ```
        ${DIGEST_ALGO}-${DIGEST_ENCODED}: ${SIGNATURE_BASE64}
        EOF
        ```
  3. Prepare the update graph. You have two options to prepare the update graph:

     1. Use the OpenShift Update Service.

        For more information about how to set up the graph on the hub cluster, see [Deploy the operator for OpenShift Update Service](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.4/html/clusters/managing-your-clusters#deploy-the-operator-for-cincinnati) and [Build the graph data init container](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.4/html/clusters/managing-your-clusters#build-the-graph-data-init-container).
     2. Make a local copy of the upstream graph. Host the update graph on an `http` or `https` server in the disconnected environment that has access to the managed cluster. To download the update graph, use the following command:

        ```
        $ curl -s https://api.openshift.com/api/upgrades_info/v1/graph?channel=stable-4.22 -o ~/upgrade-graph_stable-4.22
        ```
* For Operator updates, you must perform the following task:

  + Mirror the Operator catalogs. Ensure that the required Operator images are mirrored by following the procedure in the "Mirroring Operator catalogs for use with disconnected clusters" section.

#### [10.3.2. Performing a platform update with PolicyGenerator CRs](#talo-platform-update-PolicyGenerator_ztp-talm-pg) Copy linkLink copied to clipboard!

You can perform a platform update with the TALM.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Update GitOps Zero Touch Provisioning (ZTP) to the latest version.
* Provision one or more managed clusters with GitOps ZTP.
* Mirror the required image repository.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Create a `PolicyGenerator` CR for the platform update:

   1. Save the following `PolicyGenerator` CR in the `du-upgrade.yaml` file:

      The following example shows the `PolicyGenerator` CR for platform update:

      ```
      apiVersion: policy.open-cluster-management.io/v1
      kind: PolicyGenerator
      metadata:
          name: du-upgrade
      placementBindingDefaults:
          name: du-upgrade-placement-binding
      policyDefaults:
          namespace: ztp-group-du-sno
          placement:
              labelSelector:
                  matchExpressions:
                      - key: group-du-sno
                        operator: Exists
          remediationAction: inform
          severity: low
          namespaceSelector:
              exclude:
                  - kube-*
              include:
                  - '*'
          evaluationInterval:
              compliant: 10m
              noncompliant: 10s
      policies:
          - name: du-upgrade-platform-upgrade
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "100"
            manifests:
              - path: source-crs/ClusterVersion.yaml
                patches:
                  - metadata:
                      name: version
                    spec:
                      channel: stable-4.22
                      desiredUpdate:
                          version: 4.22.4
                      upstream: http://upgrade.example.com/images/upgrade-graph_stable-4.22
                    status:
                      history:
                          - state: Completed
                            version: 4.22.4
          - name: du-upgrade-platform-upgrade-prep
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "1"
            manifests:
              - path: source-crs/ImageSignature.yaml
              - path: source-crs/DisconnectedICSP.yaml
                patches:
                  - metadata:
                      name: disconnected-internal-icsp-for-ocp
                    spec:
                      repositoryDigestMirrors:
                          - mirrors:
                              - quay-intern.example.com/ocp4/openshift-release-dev
                            source: quay.io/openshift-release-dev/ocp-release
                          - mirrors:
                              - quay-intern.example.com/ocp4/openshift-release-dev
                            source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
      ```

      * `source-crs/ClusterVersion.yaml` - Shows the `ClusterVersion` CR to trigger the update. The `channel`, `upstream`, and `desiredVersion` fields are all required for image precaching.
      * `source-crs/ImageSignature.yaml` - Contains the image signature of the required release image. The image signature is used to verify the image before applying the platform update.
      * `repositoryDigestMirrors` - Shows the mirror repository that contains the required OpenShift Container Platform image. Get the mirrors from the `imageContentSources.yaml` file that you saved when following the procedures in the "Setting up the environment" section.

      The `PolicyGenerator` CR generates two policies:

      * The `du-upgrade-platform-upgrade-prep` policy does the preparation work for the platform update. It creates the `ConfigMap` CR for the required release image signature, creates the image content source of the mirrored release image repository, and updates the cluster version with the required update channel and the update graph reachable by the managed cluster in the disconnected environment.
      * The `du-upgrade-platform-upgrade` policy is used to perform platform upgrade.
   2. Add the `du-upgrade.yaml` file contents to the `kustomization.yaml` file located in the GitOps ZTP Git repository for the `PolicyGenerator` CRs and push the changes to the Git repository.

      ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.
   3. Check the created policies by running the following command:

      ```
      $ oc get policies -A | grep platform-upgrade
      ```
2. Create the `ClusterGroupUpdate` CR for the platform update with the `spec.enable` field set to `false`.

   1. Save the content of the platform update `ClusterGroupUpdate` CR with the `du-upgrade-platform-upgrade-prep` and the `du-upgrade-platform-upgrade` policies and the target clusters to the `cgu-platform-upgrade.yml` file, as shown in the following example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-platform-upgrade
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-platform-upgrade-prep
        - du-upgrade-platform-upgrade
        preCaching: false
        clusters:
        - spoke1
        remediationStrategy:
          maxConcurrency: 1
        enable: false
      ```
   2. Apply the `ClusterGroupUpdate` CR to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-platform-upgrade.yml
      ```
3. Optional: Precache the images for the platform update.

   1. Enable precaching in the `ClusterGroupUpdate` CR by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
      --patch '{"spec":{"preCaching": true}}' --type=merge
      ```
   2. Monitor the update process and wait for the pre-caching to complete. Check the status of pre-caching by running the following command on the hub cluster:

      ```
      $ oc get cgu cgu-platform-upgrade -o jsonpath='{.status.precaching.status}'
      ```
4. Start the platform update:

   1. Enable the `cgu-platform-upgrade` policy and disable pre-caching by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
      --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
      ```
   2. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```

#### [10.3.3. Performing an Operator update with PolicyGenerator CRs](#talo-operator-update-PolicyGenerator_ztp-talm-pg) Copy linkLink copied to clipboard!

You can perform an Operator update with the TALM.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Update GitOps Zero Touch Provisioning (ZTP) to the latest version.
* Provision one or more managed clusters with GitOps ZTP.
* Mirror the required index image, bundle images, and all Operator images referenced in the bundle images.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Update the `PolicyGenerator` CR for the Operator update.

   1. Update the `du-upgrade` `PolicyGenerator` CR with the following additional contents in the `du-upgrade.yaml` file:

      ```
      apiVersion: policy.open-cluster-management.io/v1
      kind: PolicyGenerator
      metadata:
          name: du-upgrade
      placementBindingDefaults:
          name: du-upgrade-placement-binding
      policyDefaults:
          namespace: ztp-group-du-sno
          placement:
              labelSelector:
                  matchExpressions:
                      - key: group-du-sno
                        operator: Exists
          remediationAction: inform
          severity: low
          namespaceSelector:
              exclude:
                  - kube-*
              include:
                  - '*'
          evaluationInterval:
              compliant: 10m
              noncompliant: 10s
      policies:
          - name: du-upgrade-operator-catsrc-policy
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "1"
            manifests:
              - path: source-crs/DefaultCatsrc.yaml
                patches:
                  - metadata:
                      name: redhat-operators-disconnected
                    spec:
                      displayName: Red Hat Operators Catalog
                      image: registry.example.com:5000/olm/redhat-operators-disconnected:v4.22
                      updateStrategy:
                          registryPoll:
                              interval: 1h
                    status:
                      connectionState:
                          lastObservedState: READY
      ```

      * `image` - Contains the required Operator images. If the index images are always pushed to the same image name and tag, this change is not needed.
      * `updateStrategy` - Sets how frequently the Operator Lifecycle Manager (OLM) polls the index image for new Operator versions with the `registryPoll.interval` field. This change is not needed if a new index image tag is always pushed for y-stream and z-stream Operator updates. The `registryPoll.interval` field can be set to a shorter interval to expedite the update, however shorter intervals increase computational load. To counteract this, you can restore `registryPoll.interval` to the default value once the update is complete.
      * `lastObservedState` - Displays the observed state of the catalog connection. The `READY` value ensures that the `CatalogSource` policy is ready, indicating that the index pod is pulled and is running. This way, TALM upgrades the Operators based on up-to-date policy compliance states.
   2. This update generates one policy, `du-upgrade-operator-catsrc-policy`, to update the `redhat-operators-disconnected` catalog source with the new index images that contain the required Operators images.

      Note

      If you want to use the image precaching for Operators and there are Operators from a different catalog source other than `redhat-operators-disconnected`, you must perform the following tasks:

      * Prepare a separate catalog source policy with the new index image or registry poll interval update for the different catalog source.
      * Prepare a separate subscription policy for the required Operators that are from the different catalog source.

      For example, the required SRIOV-FEC Operator is available in the `certified-operators` catalog source. To update the catalog source and the Operator subscription, add the following contents to generate two policies, `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy`:

      ```
      apiVersion: policy.open-cluster-management.io/v1
      kind: PolicyGenerator
      metadata:
          name: du-upgrade
      placementBindingDefaults:
          name: du-upgrade-placement-binding
      policyDefaults:
          namespace: ztp-group-du-sno
          placement:
              labelSelector:
                  matchExpressions:
                      - key: group-du-sno
                        operator: Exists
          remediationAction: inform
          severity: low
          namespaceSelector:
              exclude:
                  - kube-*
              include:
                  - '*'
          evaluationInterval:
              compliant: 10m
              noncompliant: 10s
      policies:
          - name: du-upgrade-fec-catsrc-policy
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "1"
            manifests:
              - path: source-crs/DefaultCatsrc.yaml
                patches:
                  - metadata:
                      name: certified-operators
                    spec:
                      displayName: Intel SRIOV-FEC Operator
                      image: registry.example.com:5000/olm/far-edge-sriov-fec:v4.10
                      updateStrategy:
                          registryPoll:
                              interval: 10m
          - name: du-upgrade-subscriptions-fec-policy
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "2"
            manifests:
              - path: source-crs/AcceleratorsSubscription.yaml
                patches:
                  - spec:
                      channel: stable
                      source: certified-operators
      ```
   3. Remove the specified subscriptions channels in the common `PolicyGenerator` CR, if they exist. The default subscriptions channels from the GitOps ZTP image are used for the update.

      Note

      The default channel for the Operators applied through GitOps ZTP 4.22 is `stable`, except for the `performance-addon-operator`. As of OpenShift Container Platform 4.11, the `performance-addon-operator` functionality was moved to the `node-tuning-operator`. For the 4.10 release, the default channel for PAO is `v4.10`. You can also specify the default channels in the common `PolicyGenerator` CR.
   4. Push the `PolicyGenerator` CRs updates to the GitOps ZTP Git repository.

      ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.
   5. Check the created policies by running the following command:

      ```
      $ oc get policies -A | grep -E "catsrc-policy|subscription"
      ```
2. Apply the required catalog source updates before starting the Operator update.

   1. Save the content of the `ClusterGroupUpgrade` CR named `operator-upgrade-prep` with the catalog source policies and the target managed clusters to the `cgu-operator-upgrade-prep.yml` file:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-operator-upgrade-prep
        namespace: default
      spec:
        clusters:
        - spoke1
        enable: true
        managedPolicies:
        - du-upgrade-operator-catsrc-policy
        remediationStrategy:
          maxConcurrency: 1
      ```
   2. Apply the policy to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-operator-upgrade-prep.yml
      ```
   3. Monitor the update process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies -A | grep -E "catsrc-policy"
      ```
3. Create the `ClusterGroupUpgrade` CR for the Operator update with the `spec.enable` field set to `false`.

   1. Save the content of the Operator update `ClusterGroupUpgrade` CR with the `du-upgrade-operator-catsrc-policy` policy and the subscription policies created from the common `PolicyGenerator` and the target clusters to the `cgu-operator-upgrade.yml` file, as shown in the following example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-operator-upgrade
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-operator-catsrc-policy
        - common-subscriptions-policy
        preCaching: false
        clusters:
        - spoke1
        remediationStrategy:
          maxConcurrency: 1
        enable: false
      ```

      * `du-upgrade-operator-catsrc-policy` is needed by the image precaching feature to retrieve the Operator images from the catalog source.
      * `common-subscriptions-policy` contains Operator subscriptions. If you have followed the structure and content of the reference `PolicyGenTemplates`, all Operator subscriptions are grouped into the `common-subscriptions-policy` policy.

      Note

      One `ClusterGroupUpgrade` CR can only precache the images of the required Operators defined in the subscription policy from one catalog source included in the `ClusterGroupUpgrade` CR. If the required Operators are from different catalog sources, such as in the example of the SRIOV-FEC Operator, another `ClusterGroupUpgrade` CR must be created with `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy` policies for the SRIOV-FEC Operator images precaching and update.
   2. Apply the `ClusterGroupUpgrade` CR to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-operator-upgrade.yml
      ```
4. Optional: Precache the images for the Operator update.

   1. Before starting image precaching, verify the subscription policy is `NonCompliant` at this point by running the following command:

      ```
      $ oc get policy common-subscriptions-policy -n <policy_namespace>
      ```

      The following is example output:

      ```
      NAME                          REMEDIATION ACTION   COMPLIANCE STATE     AGE
      common-subscriptions-policy   inform               NonCompliant         27d
      ```
   2. Enable precaching in the `ClusterGroupUpgrade` CR by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
      --patch '{"spec":{"preCaching": true}}' --type=merge
      ```
   3. Monitor the process and wait for the precaching to complete. Check the status of precaching by running the following command on the managed cluster:

      ```
      $ oc get cgu cgu-operator-upgrade -o jsonpath='{.status.precaching.status}'
      ```
   4. Check if the precaching is completed before starting the update by running the following command:

      ```
      $ oc get cgu -n default cgu-operator-upgrade -ojsonpath='{.status.conditions}' | jq
      ```

      The following is example output:

      ```
      [
          {
            "lastTransitionTime": "2022-03-08T20:49:08.000Z",
            "message": "The ClusterGroupUpgrade CR is not enabled",
            "reason": "UpgradeNotStarted",
            "status": "False",
            "type": "Ready"
          },
          {
            "lastTransitionTime": "2022-03-08T20:55:30.000Z",
            "message": "Precaching is completed",
            "reason": "PrecachingCompleted",
            "status": "True",
            "type": "PrecachingDone"
          }
      ]
      ```
5. Start the Operator update.

   1. Enable the `cgu-operator-upgrade` `ClusterGroupUpgrade` CR and disable precaching to start the Operator update by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
      --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
      ```
   2. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```

#### [10.3.4. Troubleshooting missed Operator updates with PolicyGenerator CRs](#cnf-topology-aware-lifecycle-manager-operator-troubleshooting-PolicyGenerator_ztp-talm-pg) Copy linkLink copied to clipboard!

In some scenarios, Topology Aware Lifecycle Manager (TALM) might miss Operator updates due to an out-of-date policy compliance state.

After a catalog source update, it takes time for the Operator Lifecycle Manager (OLM) to update the subscription status. The status of the subscription policy might continue to show as compliant while TALM decides whether remediation is needed. As a result, the Operator specified in the subscription policy does not get upgraded.

To avoid this scenario, add another catalog source configuration to the `PolicyGenerator` and specify this configuration in the subscription for any Operators that require an update.

**Procedure**

1. Add a catalog source configuration in the `PolicyGenerator` resource:

   ```
   manifests:
   - path: source-crs/DefaultCatsrc.yaml
     patches:
       - metadata:
           name: redhat-operators-disconnected
         spec:
           displayName: Red Hat Operators Catalog
           image: registry.example.com:5000/olm/redhat-operators-disconnected:v{product-version}
           updateStrategy:
               registryPoll:
                   interval: 1h
         status:
           connectionState:
               lastObservedState: READY
   - path: source-crs/DefaultCatsrc.yaml
     patches:
       - metadata:
           name: redhat-operators-disconnected-v2
         spec:
           displayName: Red Hat Operators Catalog v2
           image: registry.example.com:5000/olm/redhat-operators-disconnected:<version>
           updateStrategy:
               registryPoll:
                   interval: 1h
         status:
           connectionState:
               lastObservedState: READY
   ```

   * `name` - Update the name for the new configuration.
   * `displayName` - Update the display name for the new configuration.
   * `image` - Update the index image URL. This `policies.manifests.patches.spec.image` field overrides any configuration in the `DefaultCatsrc.yaml` file.
2. Update the `Subscription` resource to point to the new configuration for Operators that require an update:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: operator-subscription
     namespace: operator-namspace
   # ...
   spec:
     source: redhat-operators-disconnected-v2
   # ...
   ```

   * `redhat-operators-disconnected-v2` specifies the name of the additional catalog source configuration that you defined in the `PolicyGenerator` resource.

#### [10.3.5. Performing a platform and an Operator update together](#talo-operator-and-platform-update_ztp-talm-pg) Copy linkLink copied to clipboard!

You can perform a platform and an Operator update at the same time.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Update GitOps Zero Touch Provisioning (ZTP) to the latest version.
* Provision one or more managed clusters with GitOps ZTP.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Create the `PolicyGenerator` CR for the updates by following the steps described in the "Performing a platform update" and "Performing an Operator update" sections.
2. Apply the prep work for the platform and the Operator update.

   1. Save the content of the `ClusterGroupUpgrade` CR with the policies for platform update preparation work, catalog source updates, and target clusters to the `cgu-platform-operator-upgrade-prep.yml` file, for example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-platform-operator-upgrade-prep
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-platform-upgrade-prep
        - du-upgrade-operator-catsrc-policy
        clusterSelector:
        - group-du-sno
        remediationStrategy:
          maxConcurrency: 10
        enable: true
      ```
   2. Apply the `cgu-platform-operator-upgrade-prep.yml` file to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-platform-operator-upgrade-prep.yml
      ```
   3. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```
3. Create the `ClusterGroupUpdate` CR for the platform and the Operator update with the `spec.enable` field set to `false`.

   1. Save the contents of the platform and Operator update `ClusterGroupUpdate` CR with the policies and the target clusters to the `cgu-platform-operator-upgrade.yml` file, as shown in the following example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-du-upgrade
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-platform-upgrade
        - du-upgrade-operator-catsrc-policy
        - common-subscriptions-policy
        preCaching: true
        clusterSelector:
        - group-du-sno
        remediationStrategy:
          maxConcurrency: 1
        enable: false
      ```

      * `du-upgrade-platform-upgrade` is the platform update policy.
      * `du-upgrade-operator-catsrc-policy` is the policy containing the catalog source information for the Operators to be updated. It is needed for the precaching feature to determine which Operator images to download to the managed cluster.
      * `common-subscriptions-policy` is the policy to update the Operators.
   2. Apply the `cgu-platform-operator-upgrade.yml` file to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-platform-operator-upgrade.yml
      ```
4. Optional: Precache the images for the platform and the Operator update.

   1. Enable precaching in the `ClusterGroupUpgrade` CR by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
      --patch '{"spec":{"preCaching": true}}' --type=merge
      ```
   2. Monitor the update process and wait for the precaching to complete. Check the status of precaching by running the following command on the managed cluster:

      ```
      $ oc get jobs,pods -n openshift-talm-pre-cache
      ```
   3. Check if the precaching is completed before starting the update by running the following command:

      ```
      $ oc get cgu cgu-du-upgrade -ojsonpath='{.status.conditions}'
      ```
5. Start the platform and Operator update.

   1. Enable the `cgu-du-upgrade` `ClusterGroupUpgrade` CR to start the platform and the Operator update by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
      --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
      ```
   2. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```

      Note

      The CRs for the platform and Operator updates can be created from the beginning by configuring the setting to `spec.enable: true`. In this case, the update starts immediately after precaching completes and there is no need to manually enable the CR.

      Both precaching and the update create extra resources, such as policies, placement bindings, placement rules, managed cluster actions, and managed cluster view, to help complete the procedures. Setting the `afterCompletion.deleteObjects` field to `true` deletes all these resources after the updates complete.

#### [10.3.6. Removing Performance Addon Operator subscriptions from deployed clusters with PolicyGenerator CRs](#talm-pao-update-PolicyGenerator_ztp-talm-pg) Copy linkLink copied to clipboard!

In earlier versions of OpenShift Container Platform, the Performance Addon Operator provided automatic, low latency performance tuning for applications. In OpenShift Container Platform 4.11 or later, these functions are part of the Node Tuning Operator.

Do not install the Performance Addon Operator on clusters running OpenShift Container Platform 4.11 or later. If you upgrade to OpenShift Container Platform 4.11 or later, the Node Tuning Operator automatically removes the Performance Addon Operator.

Note

You need to remove any policies that create Performance Addon Operator subscriptions to prevent a re-installation of the Operator.

The reference DU profile includes the Performance Addon Operator in the `PolicyGenerator` CR `acm-common-ranGen.yaml`. To remove the subscription from deployed managed clusters, you must update `acm-common-ranGen.yaml`.

Note

If you install Performance Addon Operator 4.10.3-5 or later on OpenShift Container Platform 4.11 or later, the Performance Addon Operator detects the cluster version and automatically hibernates to avoid interfering with the Node Tuning Operator functions. However, to ensure best performance, remove the Performance Addon Operator from your OpenShift Container Platform 4.11 clusters.

**Prerequisites**

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for ArgoCD.
* Update to OpenShift Container Platform 4.11 or later.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Change the `complianceType` to `mustnothave` for the Performance Addon Operator namespace, Operator group, and subscription in the `acm-common-ranGen.yaml` file.

   ```
   - name: group-du-sno-pg-subscriptions-policy
     policyAnnotations:
       ran.openshift.io/ztp-deploy-wave: "2"
     manifests:
       - path: source-crs/PaoSubscriptionNS.yaml
       - path: source-crs/PaoSubscriptionOperGroup.yaml
       - path: source-crs/PaoSubscription.yaml
   ```
2. Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The status of the `common-subscriptions-policy` policy changes to `Non-Compliant`.
3. Apply the change to your target clusters by using the Topology Aware Lifecycle Manager. For more information about rolling out configuration changes, see the "Additional resources" section.
4. Monitor the process. When the status of the `common-subscriptions-policy` policy for a target cluster is `Compliant`, the Performance Addon Operator has been removed from the cluster. Get the status of the `common-subscriptions-policy` by running the following command:

   ```
   $ oc get policy -n ztp-common common-subscriptions-policy
   ```
5. Delete the Performance Addon Operator namespace, Operator group and subscription CRs from `policies.manifests` in the `acm-common-ranGen.yaml` file.
6. Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The policy remains compliant.

#### [10.3.7. Precaching user-specified images with TALM on single-node OpenShift clusters](#talm-prechache-user-specified-images-concept_ztp-talm-pg) Copy linkLink copied to clipboard!

You can precache application-specific workload images on single-node OpenShift clusters before updating your applications.

You can specify the configuration options for the precaching jobs by using the following custom resources (CR):

* `PreCachingConfig` CR
* `ClusterGroupUpgrade` CR

TALM derives the platform image from the `ClusterVersion` object in the managed policies. TALM derives Operator index images from `CatalogSource` objects that the managed policies reference.

Note

All fields in the `PreCachingConfig` CR are optional.

The following example shows a `PreCachingConfig` CR:

```
apiVersion: ran.openshift.io/v1alpha1
kind: PreCachingConfig
metadata:
  name: exampleconfig
  namespace: exampleconfig-ns
spec:
  overrides:
    operatorsPackagesAndChannels:
      - local-storage-operator: stable
      - ptp-operator: stable
      - sriov-network-operator: stable
  spaceRequired: 30 Gi
  excludePrecachePatterns:
    - aws
    - vsphere
  additionalImages:
    - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
    - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
```

* `overrides` - Specifies Operator packages and channels to precache instead of the values that TALM derives from the managed policies. The only supported override is `operatorsPackagesAndChannels`. TALM ignores the deprecated `platformImage` and `operatorsIndexes` override fields if they are present.
* `spaceRequired` - Specifies the minimum required disk space on the cluster. If unspecified, TALM defines a default value for OpenShift Container Platform images. The disk space field must include an integer value and the storage unit. For example: `40 GiB`, `200 MB`, `1 TiB`.
* `excludePrecachePatterns` - Specifies the images to exclude from precaching based on image name matching.
* `additionalImages` - Specifies the list of additional images to precache.

The following example shows a `ClusterGroupUpgrade` CR with a `PreCachingConfig` CR reference:

```
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu
spec:
  preCaching: true
  preCachingConfigRef:
    name: exampleconfig
    namespace: exampleconfig-ns
```

* `preCaching` set to `true` enables the precaching job.
* `preCachingConfigRef.name` specifies the `PreCachingConfig` CR that you want to use.
* `preCachingConfigRef.namespace` specifies the namespace of the `PreCachingConfig` CR that you want to use.

##### [10.3.7.1. Creating the custom resources for precaching](#talm-prechache-user-specified-images-preparing-crs_ztp-talm-pg) Copy linkLink copied to clipboard!

You must create the `PreCachingConfig` CR before or concurrently with the `ClusterGroupUpgrade` CR.

**Procedure**

1. Create the `PreCachingConfig` CR with the list of additional images you want to precache.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: PreCachingConfig
   metadata:
     name: exampleconfig
     namespace: default
   spec:
   # ...
     spaceRequired: 30Gi
     additionalImages:
       - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
       - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
       - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
   ```

   * `namespace` must be accessible to the hub cluster.
   * `spaceRequired` - It is recommended to set the minimum disk space required field to ensure that there is sufficient storage space for the precached images.
2. Create a `ClusterGroupUpgrade` CR with the `preCaching` field set to `true` and specify the `PreCachingConfig` CR created in the previous step:

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu
     namespace: default
   spec:
     clusters:
     - sno1
     - sno2
     preCaching: true
     preCachingConfigRef:
     - name: exampleconfig
       namespace: default
     managedPolicies:
       - du-upgrade-platform-upgrade
       - du-upgrade-operator-catsrc-policy
       - common-subscriptions-policy
     remediationStrategy:
       timeout: 240
   ```

   Warning

   Once you install the images on the cluster, you cannot change or delete them.
3. When you want to start precaching the images, apply the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc apply -f cgu.yaml
   ```

   TALM verifies the `ClusterGroupUpgrade` CR. From this point, you can continue with the TALM precaching workflow.

   Note

   All sites are precached concurrently.

**Verification**

1. Check the precaching status on the hub cluster where the `ClusterGroupUpgrade` CR is applied by running the following command:

   ```
   $ oc get cgu <cgu_name> -n <cgu_namespace> -oyaml
   ```

   The following example shows the derived precaching specification. The `platformImage` and `operatorsIndexes` values come from the managed policies, not from `PreCachingConfig` overrides.

   ```
     precaching:
       spec:
         platformImage: quay.io/openshift-release-dev/ocp-release@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
         operatorsIndexes:
           - registry.example.com:5000/custom-redhat-operators:1.0.0
         operatorsPackagesAndChannels:
           - local-storage-operator: stable
           - ptp-operator: stable
           - sriov-network-operator: stable
         excludePrecachePatterns:
           - aws
           - vsphere
         additionalImages:
           - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
           - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
           - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
         spaceRequired: "30"
       status:
         sno1: Starting
         sno2: Starting
   ```

   The precaching configurations are validated by checking if the managed policies exist. Valid configurations of the `ClusterGroupUpgrade` and the `PreCachingConfig` CRs result in the following statuses:

   The following example shows the output of valid CRs:

   ```
   - lastTransitionTime: "2023-01-01T00:00:01Z"
     message: All selected clusters are valid
     reason: ClusterSelectionCompleted
     status: "True"
     type: ClusterSelected
   - lastTransitionTime: "2023-01-01T00:00:02Z"
     message: Completed validation
     reason: ValidationCompleted
     status: "True"
     type: Validated
   - lastTransitionTime: "2023-01-01T00:00:03Z"
     message: Precaching spec is valid and consistent
     reason: PrecacheSpecIsWellFormed
     status: "True"
     type: PrecacheSpecValid
   - lastTransitionTime: "2023-01-01T00:00:04Z"
     message: Precaching in progress for 1 clusters
     reason: InProgress
     status: "False"
     type: PrecachingSucceeded
   ```

   The following example shows an invalid `PreCachingConfig` CR:

   ```
   Type:    "PrecacheSpecValid"
   Status:  False,
   Reason:  "PrecacheSpecIncomplete"
   Message: "Precaching spec is incomplete: failed to get PreCachingConfig resource due to PreCachingConfig.ran.openshift.io "<precaching_cr_name>" not found"
   ```
2. You can find the precaching job by running the following command on the managed cluster:

   ```
   $ oc get jobs -n openshift-talo-pre-cache
   ```

   The following example shows a precaching job in progress:

   ```
   NAME        COMPLETIONS       DURATION      AGE
   pre-cache   0/1               1s            1s
   ```
3. You can check the status of the pod created for the precaching job by running the following command:

   ```
   $ oc describe pod pre-cache -n openshift-talo-pre-cache
   ```

   The following example shows a precaching job in progress:

   ```
   Type        Reason              Age    From              Message
   Normal      SuccesfulCreate     19s    job-controller    Created pod: pre-cache-abcd1
   ```
4. You can get live updates on the status of the job by running the following command:

   ```
   $ oc logs -f pre-cache-abcd1 -n openshift-talo-pre-cache
   ```
5. To verify the precache job is successfully completed, run the following command:

   ```
   $ oc describe pod pre-cache -n openshift-talo-pre-cache
   ```

   The following example shows a completed precache job:

   ```
   Type        Reason              Age    From              Message
   Normal      SuccesfulCreate     5m19s  job-controller    Created pod: pre-cache-abcd1
   Normal      Completed           19s    job-controller    Job completed
   ```
6. To verify that the images are successfully precached on the single-node OpenShift, do the following:

   1. Enter into the node in debug mode:

      ```
      $ oc debug node/cnfdf00.example.lab
      ```
   2. Change root to `host`:

      ```
      $ chroot /host/
      ```
   3. Search for the required images:

      ```
      $ sudo podman images | grep <operator_name>
      ```

#### [10.3.8. About the auto-created ClusterGroupUpgrade CR for GitOps ZTP](#talo-precache-autocreated-cgu-for-ztp_ztp-talm-pg) Copy linkLink copied to clipboard!

TALM has a controller called `ManagedClusterForCGU` that monitors the `Ready` state of the `ManagedCluster` CRs on the hub cluster and creates the `ClusterGroupUpgrade` CRs for GitOps Zero Touch Provisioning (ZTP).

For any managed cluster in the `Ready` state without a `ztp-done` label applied, the `ManagedClusterForCGU` controller automatically creates a `ClusterGroupUpgrade` CR in the `ztp-install` namespace with its associated RHACM policies that are created during the GitOps ZTP process. TALM then remediates the set of configuration policies that are listed in the auto-created `ClusterGroupUpgrade` CR to push the configuration CRs to the managed cluster.

If there are no policies for the managed cluster at the time when the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR with no policies is created. Upon completion of the `ClusterGroupUpgrade` the managed cluster is labeled as `ztp-done`. If there are policies that you want to apply for that managed cluster, manually create a `ClusterGroupUpgrade` as a Day 2 operation.

**Procedure**

* View the auto-created `ClusterGroupUpgrade` CR for GitOps ZTP:

  The following example shows an auto-created `ClusterGroupUpgrade` CR for GitOps ZTP:

  ```
  apiVersion: ran.openshift.io/v1alpha1
  kind: ClusterGroupUpgrade
  metadata:
    generation: 1
    name: spoke1
    namespace: ztp-install
    ownerReferences:
    - apiVersion: cluster.open-cluster-management.io/v1
      blockOwnerDeletion: true
      controller: true
      kind: ManagedCluster
      name: spoke1
      uid: 98fdb9b2-51ee-4ee7-8f57-a84f7f35b9d5
    resourceVersion: "46666836"
    uid: b8be9cd2-764f-4a62-87d6-6b767852c7da
  spec:
    actions:
      afterCompletion:
        addClusterLabels:
          ztp-done: ""
        deleteClusterLabels:
          ztp-running: ""
        deleteObjects: true
      beforeEnable:
        addClusterLabels:
          ztp-running: ""
    clusters:
    - spoke1
    enable: true
    managedPolicies:
    - common-spoke1-config-policy
    - common-spoke1-subscriptions-policy
    - group-spoke1-config-policy
    - spoke1-config-policy
    - group-spoke1-validator-du-policy
    preCaching: false
    remediationStrategy:
      maxConcurrency: 1
      timeout: 240
  ```

  + `ztp-done: ""` is applied to the managed cluster when TALM completes the cluster configuration.
  + `ztp-running: ""` is applied to the managed cluster when TALM starts deploying the configuration policies.

## [Chapter 11. Managing cluster policies with PolicyGenTemplate resources](#managing-cluster-policies-with-policygentemplate-resources) Copy linkLink copied to clipboard!

### [11.1. Configuring managed cluster policies by using PolicyGenTemplate resources](#ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

Applied `Policy` custom resources (CRs) configure the managed clusters that you provision. You can customize how Red Hat Advanced Cluster Management (RHACM) uses `PolicyGenTemplate` CRs to generate the applied `Policy` CRs.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

#### [11.1.1. About the PolicyGenTemplate CRD](#ztp-the-policygentemplate_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

The `PolicyGenTemplate` custom resource definition (CRD) tells the `PolicyGen` policy generator what custom resources (CRs) to include in the cluster configuration, how to combine the CRs into the generated policies, and what items in those CRs need to be updated with overlay content.

The following example shows a `PolicyGenTemplate` CR (`common-du-ranGen.yaml`) extracted from the `ztp-site-generate` reference container. The `common-du-ranGen.yaml` file defines two Red Hat Advanced Cluster Management (RHACM) policies. The policies manage a collection of configuration CRs, one for each unique value of `policyName` in the CR. `common-du-ranGen.yaml` creates a single placement binding and a placement rule to bind the policies to clusters based on the labels listed in the `spec.bindingRules` section.

**Example PolicyGenTemplate CR - common-ranGen.yaml**

```
apiVersion: ran.openshift.io/v1
kind: PolicyGenTemplate
metadata:
  name: "common-latest"
  namespace: "ztp-common"
spec:
  bindingRules:
    common: "true"
    du-profile: "latest"
  sourceFiles:
    - fileName: SriovSubscriptionNS.yaml
      policyName: "subscriptions-policy"
    - fileName: SriovSubscriptionOperGroup.yaml
      policyName: "subscriptions-policy"
    - fileName: SriovSubscription.yaml
      policyName: "subscriptions-policy"
    - fileName: SriovOperatorStatus.yaml
      policyName: "subscriptions-policy"
    - fileName: PtpSubscriptionNS.yaml
      policyName: "subscriptions-policy"
    - fileName: PtpSubscriptionOperGroup.yaml
      policyName: "subscriptions-policy"
    - fileName: PtpSubscription.yaml
      policyName: "subscriptions-policy"
    - fileName: PtpOperatorStatus.yaml
      policyName: "subscriptions-policy"
    - fileName: ClusterLogNS.yaml
      policyName: "subscriptions-policy"
    - fileName: ClusterLogOperGroup.yaml
      policyName: "subscriptions-policy"
    - fileName: ClusterLogSubscription.yaml
      policyName: "subscriptions-policy"
    - fileName: ClusterLogOperatorStatus.yaml
      policyName: "subscriptions-policy"
    - fileName: StorageNS.yaml
      policyName: "subscriptions-policy"
    - fileName: StorageOperGroup.yaml
      policyName: "subscriptions-policy"
    - fileName: StorageSubscription.yaml
      policyName: "subscriptions-policy"
    - fileName: StorageOperatorStatus.yaml
      policyName: "subscriptions-policy"
    - fileName: DefaultCatsrc.yaml
      policyName: "config-policy"
      metadata:
        name: redhat-operators-disconnected
      spec:
        displayName: disconnected-redhat-operators
        image: registry.example.com:5000/disconnected-redhat-operators/disconnected-redhat-operator-index:v4.9
    - fileName: DisconnectedICSP.yaml
      policyName: "config-policy"
      spec:
        repositoryDigestMirrors:
        - mirrors:
          - registry.example.com:5000
          source: registry.redhat.io
```

where:

`common: "true"`
:   Applies the policies to all clusters with this label.

`sourceFiles`
:   Files listed under `sourceFiles` create the Operator policies for installed clusters.

`DefaultCatsrc.yaml`
:   Configures the catalog source for the disconnected registry.

`policyName: "config-policy"`
:   Configures Operator subscriptions. The `OperatorHub` CR disables the default and this CR replaces `redhat-operators` with a `CatalogSource` CR that points to the disconnected registry.

A `PolicyGenTemplate` CR can be constructed with any number of included CRs. Apply the following example CR in the hub cluster to generate a policy containing a single CR:

```
apiVersion: ran.openshift.io/v1
kind: PolicyGenTemplate
metadata:
  name: "group-du-sno"
  namespace: "ztp-group"
spec:
  bindingRules:
    group-du-sno: ""
  mcp: "master"
  sourceFiles:
    - fileName: PtpConfigSlave.yaml
      policyName: "config-policy"
      metadata:
        name: "du-ptp-slave"
      spec:
        profile:
        - name: "slave"
          interface: "ens5f0"
          ptp4lOpts: "-2 -s --summary_interval -4"
          phc2sysOpts: "-a -r -n 24"
```

Using the source file `PtpConfigSlave.yaml` as an example, the file defines a `PtpConfig` CR. The generated policy for the `PtpConfigSlave` example is named `group-du-sno-config-policy`. The `PtpConfig` CR defined in the generated `group-du-sno-config-policy` is named `du-ptp-slave`. The `spec` defined in `PtpConfigSlave.yaml` is placed under `du-ptp-slave` along with the other `spec` items defined under the source file.

The following example shows the `group-du-sno-config-policy` CR:

```
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: group-du-ptp-config-policy
  namespace: groups-sub
  annotations:
    policy.open-cluster-management.io/categories: CM Configuration Management
    policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
    policy.open-cluster-management.io/standards: NIST SP 800-53
spec:
    remediationAction: inform
    disabled: false
    policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
                name: group-du-ptp-config-policy-config
            spec:
                remediationAction: inform
                severity: low
                namespaceselector:
                    exclude:
                        - kube-*
                    include:
                        - '*'
                object-templates:
                    - complianceType: musthave
                      objectDefinition:
                        apiVersion: ptp.openshift.io/v1
                        kind: PtpConfig
                        metadata:
                            name: du-ptp-slave
                            namespace: openshift-ptp
                        spec:
                            recommend:
                                - match:
                                - nodeLabel: node-role.kubernetes.io/worker-du
                                  priority: 4
                                  profile: slave
                            profile:
                                - interface: ens5f0
                                  name: slave
                                  phc2sysOpts: -a -r -n 24
                                  ptp4lConf: |
                                    [global]
                                    #
                                    # Default Data Set
                                    #
                                    twoStepFlag 1
                                    slaveOnly 0
                                    priority1 128
                                    priority2 128
                                    domainNumber 24
```

#### [11.1.2. Recommendations when customizing PolicyGenTemplate CRs](#ztp-pgt-config-best-practices_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

Consider the following best practices when customizing site configuration `PolicyGenTemplate` custom resources (CRs):

* Use as few policies as are necessary. Using fewer policies requires less resources. Each additional policy creates increased CPU load for the hub cluster and the deployed managed cluster. CRs are combined into policies based on the `policyName` field in the `PolicyGenTemplate` CR. CRs in the same `PolicyGenTemplate` which have the same value for `policyName` are managed under a single policy.
* In disconnected environments, use a single catalog source for all Operators by configuring the registry as a single index containing all Operators. Each additional `CatalogSource` CR on the managed clusters increases CPU usage.
* Reduce the overall time taken until the cluster is ready to deploy applications by including `MachineConfig` CRs as extra manifests in the installation. To do this, package `MachineConfig` CRs in a `ConfigMap` CR. Reference the `ConfigMap` CRs in the `extraManifestsRefs` field in the `ClusterInstance` CR.
* `PolicyGenTemplate` CRs should override the channel field to explicitly identify the desired version. This ensures that changes in the source CR during upgrades does not update the generated subscription.
* The default setting for `policyDefaults.consolidateManifests` is `true`. This is the recommended setting for DU profile. Setting it to `false` might impact large scale deployments.
* The default setting for `policyDefaults.orderPolicies` is `false`. This is the recommended setting for DU profile. After the cluster installation is complete and a cluster becomes `Ready`, TALM creates a `ClusterGroupUpgrade` CR corresponding to this cluster. The `ClusterGroupUpgrade` CR contains a list of ordered policies defined by the `ran.openshift.io/ztp-deploy-wave` annotation. If you use the `PolicyGenTemplate` CR to change the order of the policies, conflicts might occur and the configuration might not be applied.

Note

When managing large numbers of spoke clusters on the hub cluster, minimize the number of policies to reduce resource consumption.

Grouping multiple configuration CRs into a single or limited number of policies is one way to reduce the overall number of policies on the hub cluster. When using the common, group, and site hierarchy of policies for managing site configuration, it is especially important to combine site-specific configurations into a single policy.

#### [11.1.3. PolicyGenTemplate CRs for RAN deployments](#ztp-policygentemplates-for-ran_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

Use `PolicyGenTemplate` custom resources (CRs) to customize the configuration applied to the cluster by using the GitOps Zero Touch Provisioning (ZTP) pipeline. The `PolicyGenTemplate` CR allows you to generate one or more policies to manage the set of configuration CRs on your fleet of clusters. The `PolicyGenTemplate` CR identifies the set of managed CRs, bundles them into policies, builds the policy wrapping around those CRs, and associates the policies with clusters by using label binding rules.

The reference configuration, obtained from the GitOps ZTP container, is designed to provide a set of critical features and node tuning settings that ensure the cluster can support the stringent performance and resource utilization constraints typical of RAN (Radio Access Network) Distributed Unit (DU) applications. Changes or omissions from the baseline configuration can affect feature availability, performance, and resource utilization. Use the reference `PolicyGenTemplate` CRs as the basis to create a hierarchy of configuration files tailored to your specific site requirements.

The baseline `PolicyGenTemplate` CRs that are defined for RAN DU cluster configuration can be extracted from the GitOps ZTP `ztp-site-generate` container. See "Preparing the GitOps ZTP site configuration repository" for further details.

The `PolicyGenTemplate` CRs can be found in the `./out/argocd/example/policygentemplates` folder. The reference architecture has common, group, and site-specific configuration CRs. Each `PolicyGenTemplate` CR refers to other CRs that can be found in the `./out/source-crs` folder.

The `PolicyGenTemplate` CRs relevant to RAN cluster configuration are described below. Variants are provided for the group `PolicyGenTemplate` CRs to account for differences in single-node, three-node compact, and standard cluster configurations. Similarly, site-specific configuration variants are provided for single-node clusters and multi-node (compact or standard) clusters. Use the group and site-specific configuration variants that are relevant for your deployment.

Expand

Table 11.1. PolicyGenTemplate CRs for RAN deployments

| PolicyGenTemplate CR | Description |
| --- | --- |
| `example-multinode-site.yaml` | Contains a set of CRs that get applied to multi-node clusters. These CRs configure SR-IOV features typical for RAN installations. |
| `example-sno-site.yaml` | Contains a set of CRs that get applied to single-node OpenShift clusters. These CRs configure SR-IOV features typical for RAN installations. |
| `common-mno-ranGen.yaml` | Contains a set of common RAN policy configuration that get applied to multi-node clusters. |
| `common-ranGen.yaml` | Contains a set of common RAN CRs that get applied to all clusters. These CRs subscribe to a set of operators providing cluster features typical for RAN as well as baseline cluster tuning. |
| `group-du-3node-ranGen.yaml` | Contains the RAN policies for three-node clusters only. |
| `group-du-sno-ranGen.yaml` | Contains the RAN policies for single-node clusters only. |
| `group-du-standard-ranGen.yaml` | Contains the RAN policies for standard three control-plane clusters. |
| `group-du-3node-validator-ranGen.yaml` | `PolicyGenTemplate` CR used to generate the various policies required for three-node clusters. |
| `group-du-standard-validator-ranGen.yaml` | `PolicyGenTemplate` CR used to generate the various policies required for standard clusters. |
| `group-du-sno-validator-ranGen.yaml` | `PolicyGenTemplate` CR used to generate the various policies required for single-node OpenShift clusters. |

Show more

#### [11.1.4. Customizing a managed cluster with PolicyGenTemplate CRs](#ztp-customizing-a-managed-site-using-pgt_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

Use the following procedure to customize the policies that get applied to the managed cluster that you provision using the GitOps Zero Touch Provisioning (ZTP) pipeline.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You configured the hub cluster for generating the required installation and policy CRs.
* You created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

**Procedure**

1. Create a `PolicyGenTemplate` CR for site-specific configuration CRs.

   1. Choose the appropriate example for your CR from the `out/argocd/example/policygentemplates` folder, for example, `example-sno-site.yaml` or `example-multinode-site.yaml`.
   2. Change the `spec.bindingRules` field in the example file to match the site-specific label included in the `ClusterInstance` CR. In the example `ClusterInstance` file, the site-specific label is `sites: example-sno`.

      Note

      Ensure that the labels defined in your `PolicyGenTemplate` `spec.bindingRules` field correspond to the labels that are defined in the related managed clusters `ClusterInstance` CR.
   3. Change the content in the example file to match the desired configuration.
2. Optional: Create a `PolicyGenTemplate` CR for any common configuration CRs that apply to the entire fleet of clusters.

   1. Select the appropriate example for your CR from the `out/argocd/example/policygentemplates` folder, for example, `common-ranGen.yaml`.
   2. Change the content in the example file to match the required configuration.
3. Optional: Create a `PolicyGenTemplate` CR for any group configuration CRs that apply to the certain groups of clusters in the fleet.

   Ensure that the content of the overlaid spec files matches your required end state. As a reference, the `out/source-crs` directory contains the full list of source-crs available to be included and overlaid by your PolicyGenTemplate templates.

   Note

   Depending on the specific requirements of your clusters, you might need more than a single group policy per cluster type, especially considering that the example group policies each have a single `PerformancePolicy.yaml` file that can only be shared across a set of clusters if those clusters consist of identical hardware configurations.

   1. Select the appropriate example for your CR from the `out/argocd/example/policygentemplates` folder, for example, `group-du-sno-ranGen.yaml`.
   2. Change the content in the example file to match the required configuration.
4. Optional. Create a validator inform policy `PolicyGenTemplate` CR to signal when the GitOps ZTP installation and configuration of the deployed cluster is complete. For more information, see "Creating a validator inform policy".
5. Define all the policy namespaces in a YAML file similar to the example `out/argocd/example/policygentemplates/ns.yaml` file.

   Important

   Do not include the `Namespace` CR in the same file with the `PolicyGenTemplate` CR.
6. Add the `PolicyGenTemplate` CRs and `Namespace` CR to the `kustomization.yaml` file in the generators section, similar to the example shown in `out/argocd/example/policygentemplateskustomization.yaml`.
7. Commit the `PolicyGenTemplate` CRs, `Namespace` CR, and associated `kustomization.yaml` file in your Git repository and push the changes.

   The ArgoCD pipeline detects the changes and begins the managed cluster deployment. You can push the changes to the `ClusterInstance` CR and the `PolicyGenTemplate` CR simultaneously.

#### [11.1.5. Monitoring managed cluster policy deployment progress](#ztp-monitoring-policy-deployment-progress_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

The ArgoCD pipeline uses `PolicyGenTemplate` CRs in Git to generate the RHACM policies and then sync them to the hub cluster. You can monitor the progress of the managed cluster policy synchronization after the assisted service installs OpenShift Container Platform on the managed cluster.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. The Topology Aware Lifecycle Manager (TALM) applies the configuration policies that are bound to the cluster.

   After the cluster installation is complete and the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR corresponding to this cluster, with a list of ordered policies defined by the `ran.openshift.io/ztp-deploy-wave annotations`, is automatically created by the TALM. The cluster’s policies are applied in the order listed in `ClusterGroupUpgrade` CR.

   You can monitor the high-level progress of configuration policy reconciliation by using the following commands:

   ```
   $ export CLUSTER=<clusterName>
   ```

   ```
   $ oc get clustergroupupgrades -n ztp-install $CLUSTER -o jsonpath='{.status.conditions[-1:]}' | jq
   ```

   **Example output**

   ```
   {
     "lastTransitionTime": "2022-11-09T07:28:09Z",
     "message": "Remediating non-compliant policies",
     "reason": "InProgress",
     "status": "True",
     "type": "Progressing"
   }
   ```
2. You can monitor the detailed cluster policy compliance status by using the RHACM dashboard or the command line.

   1. To check policy compliance by using `oc`, run the following command:

      ```
      $ oc get policies -n $CLUSTER
      ```

      **Example output**

      ```
      NAME                                                     REMEDIATION ACTION   COMPLIANCE STATE   AGE
      ztp-common.common-config-policy                          inform               Compliant          3h42m
      ztp-common.common-subscriptions-policy                   inform               NonCompliant       3h42m
      ztp-group.group-du-sno-config-policy                     inform               NonCompliant       3h42m
      ztp-group.group-du-sno-validator-du-policy               inform               NonCompliant       3h42m
      ztp-install.example1-common-config-policy-pjz9s          enforce              Compliant          167m
      ztp-install.example1-common-subscriptions-policy-zzd9k   enforce              NonCompliant       164m
      ztp-site.example1-config-policy                          inform               NonCompliant       3h42m
      ztp-site.example1-perf-policy                            inform               NonCompliant       3h42m
      ```
   2. To check policy status from the RHACM web console, perform the following actions:

      1. Click **Governance** → **Find policies**.
      2. Click on a cluster policy to check its status.

Note

When all of the cluster policies become compliant, GitOps ZTP installation and configuration for the cluster is complete. The `ztp-done` label is added to the cluster.

In the reference configuration, the final policy that becomes compliant is the one defined in the `*-du-validator-policy` policy. This policy, when compliant on a cluster, ensures that all cluster configuration, Operator installation, and Operator configuration is complete.

#### [11.1.6. Validating the generation of configuration policy CRs](#ztp-validating-the-generation-of-configuration-policy-crs_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

`Policy` custom resources (CRs) are generated in the same namespace as the `PolicyGenTemplate` from which they are created. The same troubleshooting flow applies to all policy CRs generated from a `PolicyGenTemplate` regardless of whether they are `ztp-common`, `ztp-group`, or `ztp-site` based, as shown using the following commands:

```
$ export NS=<namespace>
```

```
$ oc get policy -n $NS
```

The expected set of policy-wrapped CRs should be displayed.

If the policies failed synchronization, use the following troubleshooting steps.

**Procedure**

1. To display detailed information about the policies, run the following command:

   ```
   $ oc describe -n openshift-gitops application policies
   ```
2. Check for `Status: Conditions:` to show the error logs. For example, setting an invalid `sourceFile` entry to `fileName:` generates the error shown below:

   ```
   Status:
     Conditions:
       Last Transition Time:  2021-11-26T17:21:39Z
       Message:               rpc error: code = Unknown desc = `kustomize build /tmp/https___git.com/ran-sites/policies/ --enable-alpha-plugins` failed exit status 1: 2021/11/26 17:21:40 Error could not find test.yaml under source-crs/: no such file or directory Error: failure in plugin configured via /tmp/kust-plugin-config-52463179; exit status 1: exit status 1
       Type:  ComparisonError
   ```
3. Check for `Status: Sync:`. If there are log errors at `Status: Conditions:`, the `Status: Sync:` shows `Unknown` or `Error`:

   ```
   Status:
     Sync:
       Compared To:
         Destination:
           Namespace:  policies-sub
           Server:     https://kubernetes.default.svc
         Source:
           Path:             policies
           Repo URL:         https://git.com/ran-sites/policies/.git
           Target Revision:  master
       Status:               Error
   ```
4. When Red Hat Advanced Cluster Management (RHACM) recognizes that policies apply to a `ManagedCluster` object, the policy CR objects are applied to the cluster namespace. Check to see if the policies were copied to the cluster namespace:

   ```
   $ oc get policy -n $CLUSTER
   ```

   **Example output**

   ```
   NAME                                         REMEDIATION ACTION   COMPLIANCE STATE   AGE
   ztp-common.common-config-policy              inform               Compliant          13d
   ztp-common.common-subscriptions-policy       inform               Compliant          13d
   ztp-group.group-du-sno-config-policy         inform               Compliant          13d
   ztp-group.group-du-sno-validator-du-policy   inform               Compliant          13d
   ztp-site.example-sno-config-policy           inform               Compliant          13d
   ```

   RHACM copies all applicable policies into the cluster namespace. The copied policy names have the format: `<PolicyGenTemplate.Namespace>.<PolicyGenTemplate.Name>-<policyName>`.
5. Check the placement rule for any policies not copied to the cluster namespace. The `matchSelector` in the `PlacementRule` for those policies should match labels on the `ManagedCluster` object:

   ```
   $ oc get PlacementRule -n $NS
   ```
6. Note the `PlacementRule` name appropriate for the missing policy, common, group, or site, using the following command:

   ```
   $ oc get PlacementRule -n $NS <placement_rule_name> -o yaml
   ```

   * The status-decisions should include your cluster name.
   * The key-value pair of the `matchSelector` in the spec must match the labels on your managed cluster.
7. Check the labels on the `ManagedCluster` object by using the following command:

   ```
   $ oc get ManagedCluster $CLUSTER -o jsonpath='{.metadata.labels}' | jq
   ```
8. Check to see what policies are compliant by using the following command:

   ```
   $ oc get policy -n $CLUSTER
   ```

   If the `Namespace`, `OperatorGroup`, and `Subscription` policies are compliant but the Operator configuration policies are not, it is likely that the Operators did not install on the managed cluster. This causes the Operator configuration policies to fail to apply because the CRD is not yet applied to the spoke.

#### [11.1.7. Restarting policy reconciliation](#ztp-restarting-policies-reconciliation_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

You can restart policy reconciliation when unexpected compliance issues occur, for example, when the `ClusterGroupUpgrade` custom resource (CR) has timed out.

**Procedure**

1. A `ClusterGroupUpgrade` CR is generated in the namespace `ztp-install` by the Topology Aware Lifecycle Manager after the managed cluster becomes `Ready`:

   ```
   $ export CLUSTER=<clusterName>
   ```

   ```
   $ oc get clustergroupupgrades -n ztp-install $CLUSTER
   ```
2. If there are unexpected issues and the policies fail to become complaint within the configured timeout (the default is 4 hours), the status of the `ClusterGroupUpgrade` CR shows `UpgradeTimedOut`:

   ```
   $ oc get clustergroupupgrades -n ztp-install $CLUSTER -o jsonpath='{.status.conditions[?(@.type=="Ready")]}'
   ```
3. A `ClusterGroupUpgrade` CR in the `UpgradeTimedOut` state automatically restarts its policy reconciliation every hour. If you have changed your policies, you can start a retry immediately by deleting the existing `ClusterGroupUpgrade` CR. This triggers the automatic creation of a new `ClusterGroupUpgrade` CR that begins reconciling the policies immediately:

   ```
   $ oc delete clustergroupupgrades -n ztp-install $CLUSTER
   ```

Note

When the `ClusterGroupUpgrade` CR completes with status `UpgradeCompleted` and the managed cluster has the label `ztp-done` applied, you can make additional configuration changes by using `PolicyGenTemplate`. Deleting the existing `ClusterGroupUpgrade` CR will not make the TALM generate a new CR.

At this point, GitOps ZTP has completed its interaction with the cluster and any further interactions should be treated as an update and a new `ClusterGroupUpgrade` CR created for remediation of the policies.

#### [11.1.8. Changing applied managed cluster CRs using policies](#ztp-removing-content-from-managed-clusters_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

You can remove content from a custom resource (CR) that is deployed in a managed cluster through a policy.

By default, all `Policy` CRs created from a `PolicyGenTemplate` CR have the `complianceType` field set to `musthave`. A `musthave` policy without the removed content is still compliant because the CR on the managed cluster has all the specified content. With this configuration, when you remove content from a CR, TALM removes the content from the policy but the content is not removed from the CR on the managed cluster.

With the `complianceType` field to `mustonlyhave`, the policy ensures that the CR on the cluster is an exact match of what is specified in the policy.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have deployed a managed cluster from a hub cluster running RHACM.
* You have installed Topology Aware Lifecycle Manager on the hub cluster.

**Procedure**

1. Remove the content that you no longer need from the affected CRs. In this example, the `disableDrain: false` line was removed from the `SriovOperatorConfig` CR.

   **Example CR**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovOperatorConfig
   metadata:
     name: default
     namespace: openshift-sriov-network-operator
   spec:
     configDaemonNodeSelector:
       "node-role.kubernetes.io/$mcp": ""
     disableDrain: true
     enableInjector: true
     enableOperatorWebhook: true
   ```
2. Change the `complianceType` of the affected policies to `mustonlyhave` in the `group-du-sno-ranGen.yaml` file.

   **Example YAML**

   ```
   - fileName: SriovOperatorConfig.yaml
     policyName: "config-policy"
     complianceType: mustonlyhave
   ```
3. Create a `ClusterGroupUpdates` CR and specify the clusters that must receive the CR changes::

   **Example ClusterGroupUpdates CR**

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-remove
     namespace: default
   spec:
     managedPolicies:
       - ztp-group.group-du-sno-config-policy
     enable: false
     clusters:
     - spoke1
     - spoke2
     remediationStrategy:
       maxConcurrency: 2
       timeout: 240
     batchTimeoutAction:
   ```
4. Create the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc create -f cgu-remove.yaml
   ```
5. When you are ready to apply the changes, for example, during an appropriate maintenance window, change the value of the `spec.enable` field to `true` by running the following command:

   ```
   $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-remove \
   --patch '{"spec":{"enable":true}}' --type=merge
   ```

**Verification**

1. Check the status of the policies by running the following command:

   ```
   $ oc get <kind> <changed_cr_name>
   ```

   **Example output**

   ```
   NAMESPACE   NAME                                                   REMEDIATION ACTION   COMPLIANCE STATE   AGE
   default     cgu-ztp-group.group-du-sno-config-policy               enforce                                 17m
   default     ztp-group.group-du-sno-config-policy                   inform               NonCompliant       15h
   ```

   When the `COMPLIANCE STATE` of the policy is `Compliant`, it means that the CR is updated and the unwanted content is removed.
2. Check that the policies are removed from the targeted clusters by running the following command on the managed clusters:

   ```
   $ oc get <kind> <changed_cr_name>
   ```

   If there are no results, the CR is removed from the managed cluster.

#### [11.1.9. Indication of done for GitOps ZTP installations](#ztp-definition-of-done-for-ztp-installations_ztp-configuring-managed-clusters-policies) Copy linkLink copied to clipboard!

GitOps Zero Touch Provisioning (ZTP) simplifies the process of checking the GitOps ZTP installation status for a cluster. The GitOps ZTP status moves through three phases: cluster installation, cluster configuration, and GitOps ZTP done.

Cluster installation phase
:   The cluster installation phase is shown by the `ManagedClusterJoined` and `ManagedClusterAvailable` conditions in the `ManagedCluster` CR . If the `ManagedCluster` CR does not have these conditions, or the condition is set to `False`, the cluster is still in the installation phase. Additional details about installation are available from the `AgentClusterInstall` and `ClusterDeployment` CRs. For more information, see "Troubleshooting GitOps ZTP".

Cluster configuration phase
:   The cluster configuration phase is shown by a `ztp-running` label applied the `ManagedCluster` CR for the cluster.

GitOps ZTP done
:   Cluster installation and configuration is complete in the GitOps ZTP done phase. This is shown by the removal of the `ztp-running` label and addition of the `ztp-done` label to the `ManagedCluster` CR. The `ztp-done` label shows that the configuration has been applied and the baseline DU configuration has completed cluster tuning.

    The change to the GitOps ZTP done state is conditional on the compliant state of a Red Hat Advanced Cluster Management (RHACM) validator inform policy. This policy captures the existing criteria for a completed installation and validates that it moves to a compliant state only when GitOps ZTP provisioning of the managed cluster is complete.

    The validator inform policy ensures the configuration of the cluster is fully applied and Operators have completed their initialization. The policy validates the following:

    * The target `MachineConfigPool` contains the expected entries and has finished updating. All nodes are available and not degraded.
    * The SR-IOV Operator has completed initialization as indicated by at least one `SriovNetworkNodeState` with `syncStatus: Succeeded`.
    * The PTP Operator daemon set exists.

### [11.2. Advanced managed cluster configuration with PolicyGenTemplate resources](#ztp-advanced-policy-config) Copy linkLink copied to clipboard!

You can use `PolicyGenTemplate` CRs to deploy custom functionality in your managed clusters.

Important

Using RHACM and `PolicyGenTemplate` CRs is the recommended approach for managing policies and deploying them to managed clusters. This replaces the use of `PolicyGenTemplate` CRs for this purpose. For more information about `PolicyGenTemplate` resources, see the RHACM [Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/governance/policy-deployment#integrate-policy-generator) documentation.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

#### [11.2.1. Deploying additional changes to clusters](#ztp-deploying-additional-changes-to-clusters_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

If you require cluster configuration changes outside of the base GitOps Zero Touch Provisioning (ZTP) pipeline configuration, there are three options:

Apply the additional configuration after the GitOps ZTP pipeline is complete
:   When the GitOps ZTP pipeline deployment is complete, the deployed cluster is ready for application workloads. At this point, you can install additional Operators and apply configurations specific to your requirements. Ensure that additional configurations do not negatively affect the performance of the platform or allocated CPU budget.

Add content to the GitOps ZTP library
:   The base source custom resources (CRs) that you deploy with the GitOps ZTP pipeline can be augmented with custom content as required.

Create extra manifests for the cluster installation
:   Extra manifests are applied during installation and make the installation process more efficient.

Important

Providing additional source CRs or modifying existing source CRs can significantly impact the performance or CPU profile of OpenShift Container Platform.

#### [11.2.2. Using PolicyGenTemplate CRs to override source CRs content](#ztp-using-pgt-to-update-source-crs_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

`PolicyGenTemplate` custom resources (CRs) allow you to overlay additional configuration details on top of the base source CRs provided with the GitOps plugin in the `ztp-site-generate` container. You can think of `PolicyGenTemplate` CRs as a logical merge or patch to the base CR. Use `PolicyGenTemplate` CRs to update a single field of the base CR, or overlay the entire contents of the base CR. You can update values and insert fields that are not in the base CR.

The following example procedure describes how to update fields in the generated `PerformanceProfile` CR for the reference configuration based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml` file. Use the procedure as a basis for modifying other parts of the `PolicyGenTemplate` based on your requirements.

**Prerequisites**

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for Argo CD.

**Procedure**

1. Review the baseline source CR for existing content. You can review the source CRs listed in the reference `PolicyGenTemplate` CRs by extracting them from the GitOps Zero Touch Provisioning (ZTP) container.

   1. Create an `/out` folder:

      ```
      $ mkdir -p ./out
      ```
   2. Extract the source CRs:

      ```
      $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.22.1 extract /home/ztp --tar | tar x -C ./out
      ```
2. Review the baseline `PerformanceProfile` CR in `./out/source-crs/PerformanceProfile.yaml`:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
     name: $name
     annotations:
       ran.openshift.io/ztp-deploy-wave: "10"
   spec:
     additionalKernelArgs:
     - "idle=poll"
     - "rcupdate.rcu_normal_after_boot=0"
     cpu:
       isolated: $isolated
       reserved: $reserved
     hugepages:
       defaultHugepagesSize: $defaultHugepagesSize
       pages:
         - size: $size
           count: $count
           node: $node
     machineConfigPoolSelector:
       pools.operator.machineconfiguration.openshift.io/$mcp: ""
     net:
       userLevelNetworking: true
     nodeSelector:
       node-role.kubernetes.io/$mcp: ''
     numa:
       topologyPolicy: "restricted"
     realTimeKernel:
       enabled: true
   ```

   Note

   Any fields in the source CR which contain `$…​` are removed from the generated CR if they are not provided in the `PolicyGenTemplate` CR.
3. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file. The following example `PolicyGenTemplate` CR stanza supplies appropriate CPU specifications, sets the `hugepages` configuration, and adds a new field that sets `globallyDisableIrqLoadBalancing` to false.

   ```
   - fileName: PerformanceProfile.yaml
     policyName: "config-policy"
     metadata:
       name: openshift-node-performance-profile
     spec:
       cpu:
         # These must be tailored for the specific hardware platform
         isolated: "2-19,22-39"
         reserved: "0-1,20-21"
       hugepages:
         defaultHugepagesSize: 1G
         pages:
           - size: 1G
             count: 10
       globallyDisableIrqLoadBalancing: false
   ```
4. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the GitOps ZTP argo CD application.

   The GitOps ZTP application generates an RHACM policy that contains the generated `PerformanceProfile` CR. The contents of that CR are derived by merging the `metadata` and `spec` contents from the `PerformanceProfile` entry in the `PolicyGenTemplate` onto the source CR. The resulting CR has the following content:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
       name: openshift-node-performance-profile
   spec:
       additionalKernelArgs:
           - idle=poll
           - rcupdate.rcu_normal_after_boot=0
       cpu:
           isolated: 2-19,22-39
           reserved: 0-1,20-21
       globallyDisableIrqLoadBalancing: false
       hugepages:
           defaultHugepagesSize: 1G
           pages:
               - count: 10
                 size: 1G
       machineConfigPoolSelector:
           pools.operator.machineconfiguration.openshift.io/master: ""
       net:
           userLevelNetworking: true
       nodeSelector:
           node-role.kubernetes.io/master: ""
       numa:
           topologyPolicy: restricted
       realTimeKernel:
           enabled: true
   ```

   Note

   In the `/source-crs` folder that you extract from the `ztp-site-generate` container, the `$` syntax is not used for template substitution as implied by the syntax. Rather, if the `policyGen` tool sees the `$` prefix for a string and you do not specify a value for that field in the related `PolicyGenTemplate` CR, the field is omitted from the output CR entirely.

   An exception to this is the `$mcp` variable in `/source-crs` YAML files that is substituted with the specified value for `mcp` from the `PolicyGenTemplate` CR. For example, in `example/policygentemplates/group-du-standard-ranGen.yaml`, the value for `mcp` is `worker`:

   ```
   spec:
     bindingRules:
       group-du-standard: ""
     mcp: "worker"
   ```

   The `policyGen` tool replace instances of `$mcp` with `worker` in the output CRs.

#### [11.2.3. Adding custom content to the GitOps ZTP pipeline](#ztp-adding-new-content-to-gitops-ztp_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Perform the following procedure to add new content to the GitOps ZTP pipeline.

**Procedure**

1. Create a subdirectory named `source-crs` in the directory that contains the `kustomization.yaml` file for the `PolicyGenTemplate` custom resource (CR).
2. Add your user-provided CRs to the `source-crs` subdirectory, as shown in the following example:

   ```
   example
   └── policygentemplates
       ├── dev.yaml
       ├── kustomization.yaml
       ├── mec-edge-sno1.yaml
       ├── sno.yaml
       └── source-crs
           ├── PaoCatalogSource.yaml
           ├── PaoSubscription.yaml
           ├── custom-crs
           |   ├── apiserver-config.yaml
           |   └── disable-nic-lldp.yaml
           └── elasticsearch
               ├── ElasticsearchNS.yaml
               └── ElasticsearchOperatorGroup.yaml
   ```

   The `source-crs` subdirectory must be in the same directory as the `kustomization.yaml` file.
3. Update the required `PolicyGenTemplate` CRs to include references to the content you added in the `source-crs/custom-crs` and `source-crs/elasticsearch` directories. For example:

   ```
   apiVersion: ran.openshift.io/v1
   kind: PolicyGenTemplate
   metadata:
     name: "group-dev"
     namespace: "ztp-clusters"
   spec:
     bindingRules:
       dev: "true"
     mcp: "master"
     sourceFiles:
       # These policies/CRs come from the internal container Image
       #Cluster Logging
       - fileName: ClusterLogNS.yaml
         remediationAction: inform
         policyName: "group-dev-cluster-log-ns"
       - fileName: ClusterLogOperGroup.yaml
         remediationAction: inform
         policyName: "group-dev-cluster-log-operator-group"
       - fileName: ClusterLogSubscription.yaml
         remediationAction: inform
         policyName: "group-dev-cluster-log-sub"
       #Local Storage Operator
       - fileName: StorageNS.yaml
         remediationAction: inform
         policyName: "group-dev-lso-ns"
       - fileName: StorageOperGroup.yaml
         remediationAction: inform
         policyName: "group-dev-lso-operator-group"
       - fileName: StorageSubscription.yaml
         remediationAction: inform
         policyName: "group-dev-lso-sub"
       #These are custom local policies that come from the source-crs directory in the git repo
       # Performance Addon Operator
       - fileName: PaoSubscriptionNS.yaml
         remediationAction: inform
         policyName: "group-dev-pao-ns"
       - fileName: PaoSubscriptionCatalogSource.yaml
         remediationAction: inform
         policyName: "group-dev-pao-cat-source"
         spec:
           image: <container_image_url>
       - fileName: PaoSubscription.yaml
         remediationAction: inform
         policyName: "group-dev-pao-sub"
       #Elasticsearch Operator
       - fileName: elasticsearch/ElasticsearchNS.yaml
         remediationAction: inform
         policyName: "group-dev-elasticsearch-ns"
       - fileName: elasticsearch/ElasticsearchOperatorGroup.yaml
         remediationAction: inform
         policyName: "group-dev-elasticsearch-operator-group"
       #Custom Resources
       - fileName: custom-crs/apiserver-config.yaml
         remediationAction: inform
         policyName: "group-dev-apiserver-config"
       - fileName: custom-crs/disable-nic-lldp.yaml
         remediationAction: inform
         policyName: "group-dev-disable-nic-lldp"
   ```

   Set `fileName` to include the relative path to the file from the `/source-crs` parent directory.
4. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository that is monitored by the GitOps ZTP Argo CD policies application.
5. Update the `ClusterGroupUpgrade` CR to include the changed `PolicyGenTemplate` and save it as `cgu-test.yaml`. The following example shows a generated `cgu-test.yaml` file.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: custom-source-cr
     namespace: ztp-clusters
   spec:
     managedPolicies:
       - group-dev-config-policy
     enable: true
     clusters:
     - cluster1
     remediationStrategy:
       maxConcurrency: 2
       timeout: 240
   ```
6. Apply the updated `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc apply -f cgu-test.yaml
   ```

**Verification**

* Check that the updates have succeeded by running the following command:

  ```
  $ oc get cgu -A
  ```

  The following example shows the output:

  ```
  NAMESPACE     NAME               AGE   STATE        DETAILS
  ztp-clusters  custom-source-cr   6s    InProgress   Remediating non-compliant policies
  ztp-install   cluster1           19h   Completed    All clusters are compliant with all the managed policies
  ```

#### [11.2.4. Configuring policy compliance evaluation timeouts for PolicyGenTemplate CRs](#ztp-configuring-pgt-compliance-eval-timeouts_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Use Red Hat Advanced Cluster Management (RHACM) installed on a hub cluster to monitor and report on whether your managed clusters are compliant with applied policies. RHACM uses policy templates to apply predefined policy controllers and policies. Policy controllers are Kubernetes custom resource definition (CRD) instances.

You can override the default policy evaluation intervals with `PolicyGenTemplate` custom resources (CRs). You configure duration settings that define how long a `ConfigurationPolicy` CR can be in a state of policy compliance or non-compliance before RHACM re-evaluates the applied cluster policies.

The GitOps Zero Touch Provisioning (ZTP) policy generator generates `ConfigurationPolicy` CR policies with pre-defined policy evaluation intervals. The default value for the `noncompliant` state is 10 seconds. The default value for the `compliant` state is 10 minutes. To disable the evaluation interval, set the value to `never`.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data.

**Procedure**

1. To configure the evaluation interval for all policies in a `PolicyGenTemplate` CR, set appropriate `compliant` and `noncompliant` values for the `evaluationInterval` field. For example:

   ```
   spec:
     evaluationInterval:
       compliant: 30m
       noncompliant: 20s
   ```

   Note

   You can also set `compliant` and `noncompliant` fields to `never` to stop evaluating the policy after it reaches particular compliance state.
2. To configure the evaluation interval for an individual policy object in a `PolicyGenTemplate` CR, add the `evaluationInterval` field and set appropriate values. For example:

   ```
   spec:
     sourceFiles:
       - fileName: SriovSubscription.yaml
         policyName: "sriov-sub-policy"
         evaluationInterval:
           compliant: never
           noncompliant: 10s
   ```
3. Commit the `PolicyGenTemplate` CRs files in the Git repository and push your changes.

**Verification**

Check that the managed spoke cluster policies are monitored at the expected intervals.

1. Log in as a user with `cluster-admin` privileges on the managed cluster.
2. Get the pods that are running in the `open-cluster-management-agent-addon` namespace. Run the following command:

   ```
   $ oc get pods -n open-cluster-management-agent-addon
   ```

   The following example shows the output:

   ```
   NAME                                         READY   STATUS    RESTARTS        AGE
   config-policy-controller-858b894c68-v4xdb    1/1     Running   22 (5d8h ago)   10d
   ```
3. Check the applied policies are being evaluated at the expected interval in the logs for the `config-policy-controller` pod:

   ```
   $ oc logs -n open-cluster-management-agent-addon config-policy-controller-858b894c68-v4xdb
   ```

   The following example shows the output:

   ```
   2022-05-10T15:10:25.280Z       info   configuration-policy-controller controllers/configurationpolicy_controller.go:166      Skipping the policy evaluation due to the policy not reaching the evaluation interval  {"policy": "compute-1-config-policy-config"}
   2022-05-10T15:10:25.280Z       info   configuration-policy-controller controllers/configurationpolicy_controller.go:166      Skipping the policy evaluation due to the policy not reaching the evaluation interval  {"policy": "compute-1-common-compute-1-catalog-policy-config"}
   ```

#### [11.2.5. Signalling GitOps ZTP cluster deployment completion with validator inform policies](#ztp-creating-a-validator-inform-policy_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Create a validator inform policy that signals when the GitOps Zero Touch Provisioning (ZTP) installation and configuration of the deployed cluster is complete. This policy can be used for deployments of single-node OpenShift clusters, three-node clusters, and standard clusters.

**Procedure**

1. Create a standalone `PolicyGenTemplate` custom resource (CR) that contains the source file `validatorCRs/informDuValidator.yaml`. You only need one standalone `PolicyGenTemplate` CR for each cluster type. For example, this CR applies a validator inform policy for single-node OpenShift clusters:

   Example single-node cluster validator inform policy CR (group-du-sno-validator-ranGen.yaml):

   ```
   apiVersion: ran.openshift.io/v1
   kind: PolicyGenTemplate
   metadata:
     name: "group-du-sno-validator"
     namespace: "ztp-group"
   spec:
     bindingRules:
       group-du-sno: ""
     bindingExcludedRules:
       ztp-done: ""
     mcp: "master"
     sourceFiles:
       - fileName: validatorCRs/informDuValidator.yaml
         remediationAction: inform
         policyName: "du-policy"
   ```

   where:

   `metadata.name`
   :   Specifies the name of the `{policy-gen-crs}` object. This name is also used as part of the names for the `placementBinding`, `placementRule`, and `policy` that are created in the requested `namespace`.

   `metadata.namespace`
   :   Specifies the namespace. This value should match the `namespace` used in the group `policy-gen-crs`.

   `spec.bindingRules`
   :   Specifies the binding rules. The `group-du-*` label defined in `bindingRules` must exist in the `ClusterInstance` files.

   `spec.bindingExcludedRules`
   :   Specifies the binding excluded rules. The label defined in `bindingExcludedRules` must be `ztp-done:`. The `ztp-done` label is used in coordination with the Topology Aware Lifecycle Manager.

   `spec.mcp`
   :   Specifies the `MachineConfigPool` object that is used in the source file `validatorCRs/informDuValidator.yaml`. It should be `master` for single node and three-node cluster deployments and `worker` for standard cluster deployments.

   `spec.sourceFiles.remediationAction`
   :   Specifies the remediation action. Optional. The default value is `inform`.

   `spec.sourceFiles.policyName`
   :   Specifies the name for the generated RHACM policy. The generated validator policy for the single node example is `group-du-sno-validator-du-policy`.
2. Commit the `PolicyGenTemplate` CR file in your Git repository and push the changes.

#### [11.2.6. Configuring power states using PolicyGenTemplate CRs](#ztp-using-pgt-to-configure-power-saving-states_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

For low latency and high-performance edge deployments, it is necessary to disable or limit C-states and P-states.

With this configuration, the CPU runs at a constant frequency, which is typically the maximum turbo frequency. This ensures that the CPU is always running at its maximum speed, which results in high performance and low latency. This leads to the best latency for workloads. However, this also leads to the highest power consumption, which might not be necessary for all workloads.

Workloads can be classified as critical or non-critical, with critical workloads requiring disabled C-state and P-state settings for high performance and low latency, while non-critical workloads use C-state and P-state settings for power savings at the expense of some latency and performance. You can configure the following three power states using GitOps Zero Touch Provisioning (ZTP):

* High-performance mode provides ultra low latency at the highest power consumption.
* Performance mode provides low latency at a relatively high power consumption.
* Power saving balances reduced power consumption with increased latency.

The default configuration is for a low latency, performance mode.

`PolicyGenTemplate` custom resources (CRs) allow you to overlay additional configuration details onto the base source CRs provided with the GitOps plugin in the `ztp-site-generate` container.

Configure the power states by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

The following common prerequisites apply to configuring all three power states:

* You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for Argo CD.
* You have followed the procedure described in "Preparing the GitOps ZTP site configuration repository".

##### [11.2.6.1. Configuring performance mode using PolicyGenTemplate CRs](#ztp-using-pgt-to-configure-performance-mode_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Follow this example to set performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

Performance mode provides low latency at a relatively high power consumption.

**Prerequisites**

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

**Procedure**

1. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates//` as follows to set performance mode.

   ```
   - fileName: PerformanceProfile.yaml
     policyName: "config-policy"
     metadata:
     # ...
     spec:
       # ...
       workloadHints:
            realTime: true
            highPowerConsumption: false
            perPodPowerManagement: false
   ```
2. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

##### [11.2.6.2. Configuring high-performance mode using PolicyGenTemplate CRs](#ztp-using-pgt-to-configure-high-performance-mode_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Follow this example to set high performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

High performance mode provides ultra low latency at the highest power consumption.

**Prerequisites**

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

**Procedure**

1. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates/` as follows to set high-performance mode.

   ```
   - fileName: PerformanceProfile.yaml
     policyName: "config-policy"
     metadata:
     #  ...
     spec:
     #  ...
       workloadHints:
            realTime: true
            highPowerConsumption: true
            perPodPowerManagement: false
   ```
2. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

* [Configuring host firmware for low latency and high performance](#ztp-du-configuring-host-firmware-requirements_sno-configure-for-vdu "7.3. Configuring host firmware for low latency and high performance")

##### [11.2.6.3. Configuring power saving mode using PolicyGenTemplate CRs](#ztp-using-pgt-to-configure-power-saving-mode_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Follow this example to set power saving mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

The power saving mode balances reduced power consumption with increased latency.

**Prerequisites**

* You enabled C-states and OS-controlled P-states in the BIOS.

**Procedure**

1. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates/` as follows to configure power saving mode. It is recommended to configure the CPU governor for the power saving mode through the additional kernel arguments object.

   ```
   - fileName: PerformanceProfile.yaml
     policyName: "config-policy"
     metadata:
     # ...
     spec:
       # ...
       workloadHints:
         realTime: true
         highPowerConsumption: false
         perPodPowerManagement: true
       # ...
       additionalKernelArgs:
         - # ...
         - "cpufreq.default_governor=schedutil"
   ```

   The `schedutil` governor is recommended, however, other governors that can be used include `ondemand` and `powersave`.
2. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

**Verification**

1. Select a worker node in your deployed cluster from the list of nodes identified by using the following command:

   ```
   $ oc get nodes
   ```
2. Log in to the node by using the following command:

   ```
   $ oc debug node/<node-name>
   ```

   Replace `<node-name>` with the name of the node you want to verify the power state on.
3. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths as shown in the following example:

   ```
   # chroot /host
   ```
4. Run the following command to verify the applied power state:

   ```
   # cat /proc/cmdline
   ```

   For power saving mode, verify that the output includes `intel_pstate=passive`.

##### [11.2.6.4. Maximizing power savings](#ztp-using-pgt-to-maximize-power-savings-mode_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Limiting the maximum CPU frequency is recommended to achieve maximum power savings.

Enabling C-states on the non-critical workload CPUs without restricting the maximum CPU frequency negates much of the power savings by boosting the frequency of the critical CPUs.

Maximize power savings by updating the `sysfs` plugin fields, setting an appropriate value for `max_perf_pct` in the `TunedPerformancePatch` CR for the reference configuration. This example based on the `group-du-sno-ranGen.yaml` describes the procedure to follow to restrict the maximum CPU frequency.

**Prerequisites**

* You have configured power savings mode as described in "Using PolicyGenTemplate CRs to configure power savings mode".

**Procedure**

1. Update the `PolicyGenTemplate` entry for `TunedPerformancePatch` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates/`. To maximize power savings, add `max_perf_pct` as shown in the following example:

   ```
   - fileName: TunedPerformancePatch.yaml
     policyName: "config-policy"
     spec:
       profile:
         - name: performance-patch
           data: |
             # ...
             [sysfs]
             /sys/devices/system/cpu/intel_pstate/max_perf_pct=<x>
   ```

   The `max_perf_pct` controls the maximum frequency the `cpufreq` driver is allowed to set as a percentage of the maximum supported CPU frequency. This value applies to all CPUs. You can check the maximum supported frequency in `/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq`. As a starting point, you can use a percentage that caps all CPUs at the `All Cores Turbo` frequency. The `All Cores Turbo` frequency is the frequency that all cores will run at when the cores are all fully occupied.

   Note

   To maximize power savings, set a lower value. Setting a lower value for `max_perf_pct` limits the maximum CPU frequency, thereby reducing power consumption, but also potentially impacting performance. Experiment with different values and monitor the system’s performance and power consumption to find the optimal setting for your use-case.
2. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the GitOps ZTP Argo CD application.

#### [11.2.7. Configuring LVM Storage using PolicyGenTemplate CRs](#ztp-provisioning-lvm-storage_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

You can configure Logical Volume Manager (LVM) Storage for managed clusters that you deploy with GitOps Zero Touch Provisioning (ZTP).

Note

You use LVM Storage to persist event subscriptions when you use PTP events or bare-metal hardware events with HTTP transport.

Use the Local Storage Operator for persistent storage that uses local volumes in distributed units.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.
* Create a Git repository where you manage your custom site configuration data.

**Procedure**

1. To configure LVM Storage for new managed clusters, add the following YAML to `spec.sourceFiles` in the `common-ranGen.yaml` file:

   ```
   - fileName: StorageLVMOSubscriptionNS.yaml
     policyName: subscription-policies
   - fileName: StorageLVMOSubscriptionOperGroup.yaml
     policyName: subscription-policies
   - fileName: StorageLVMOSubscription.yaml
     spec:
       name: lvms-operator
       channel: stable-4.22
     policyName: subscription-policies
   ```

   Note

   The Storage LVMO subscription is deprecated. In future releases of OpenShift Container Platform, the storage LVMO subscription will not be available. Instead, you must use the Storage LVMS subscription.

   In OpenShift Container Platform 4.22, you can use the Storage LVMS subscription instead of the LVMO subscription. The LVMS subscription does not require manual overrides in the `common-ranGen.yaml` file. Add the following YAML to `spec.sourceFiles` in the `common-ranGen.yaml` file to use the Storage LVMS subscription:

   ```
   - fileName: StorageLVMSubscriptionNS.yaml
     policyName: subscription-policies
   - fileName: StorageLVMSubscriptionOperGroup.yaml
     policyName: subscription-policies
   - fileName: StorageLVMSubscription.yaml
     policyName: subscription-policies
   ```
2. Add the `LVMCluster` CR to `spec.sourceFiles` in your specific group or individual site configuration file. For example, in the `group-du-sno-ranGen.yaml` file, add the following:

   ```
   - fileName: StorageLVMCluster.yaml
     policyName: "lvms-config"
     spec:
       storage:
         deviceClasses:
         - name: vg1
           thinPoolConfig:
             name: thin-pool-1
             sizePercent: 90
             overprovisionRatio: 10
   ```

   This example configuration creates a volume group (`vg1`) with all the available devices, except the disk where OpenShift Container Platform is installed. A thin-pool logical volume is also created.
3. Merge any other required changes and files with your custom site repository.
4. Commit the `PolicyGenTemplate` changes in Git, and then push the changes to your site configuration repository to deploy LVM Storage to new sites using GitOps ZTP.

#### [11.2.8. Configuring PTP events with PolicyGenTemplate CRs](#ztp-advanced-policy-config-ptp_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

You can use the GitOps ZTP pipeline to configure PTP events that use HTTP transport.

##### [11.2.8.1. Configuring PTP events that use HTTP transport](#ztp-configuring-ptp-fast-events_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

You can configure PTP events that use HTTP transport on managed clusters that you deploy with the GitOps Zero Touch Provisioning (ZTP) pipeline.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data.

**Procedure**

1. Apply the following `PolicyGenTemplate` changes to `group-du-3node-ranGen.yaml`, `group-du-sno-ranGen.yaml`, or `group-du-standard-ranGen.yaml` files according to your requirements:

   1. In `spec.sourceFiles`, add the `PtpOperatorConfig` CR file that configures the transport host:

      ```
      - fileName: PtpOperatorConfigForEvent.yaml
        policyName: "config-policy"
        spec:
          daemonNodeSelector: {}
          ptpEventConfig:
            enableEventPublisher: true
            transportHost: http://ptp-event-publisher-service-NODE_NAME.openshift-ptp.svc.cluster.local:9043
      ```

      Note

      In OpenShift Container Platform 4.13 or later, you do not need to set the `transportHost` field in the `PtpOperatorConfig` resource when you use HTTP transport with PTP events.
   2. Configure the `linuxptp` and `phc2sys` for the PTP clock type and interface. For example, add the following YAML into `spec.sourceFiles`:

      ```
      - fileName: PtpConfigSlave.yaml
        policyName: "config-policy"
        metadata:
          name: "du-ptp-slave"
        spec:
          profile:
          - name: "slave"
            interface: "ens5f1"
            ptp4lOpts: "-2 -s --summary_interval -4"
            phc2sysOpts: "-a -r -m -n 24 -N 8 -R 16"
          ptpClockThreshold:
            holdOverTimeout: 30 # seconds
            maxOffsetThreshold: 100  # nano seconds
            minOffsetThreshold: -100
      ```

      where:

      `fileName`
      :   Specifies `PtpConfigMaster.yaml` or `PtpConfigSlave.yaml` depending on your requirements. For configurations based on `group-du-sno-ranGen.yaml` or `group-du-3node-ranGen.yaml`, use `PtpConfigSlave.yaml`.

      `spec.profile.interface`
      :   Specifies the device specific interface name.

      `spec.profile.ptp4lOpts`
      :   Specifies the ptp4l options. You must append the `--summary_interval -4` value to `ptp4lOpts` in `.spec.sourceFiles.spec.profile` to enable PTP fast events.

      `spec.profile.phc2sysOpts`
      :   Specifies the required `phc2sysOpts` values. `-m` prints messages to `stdout`. The `linuxptp-daemon` `DaemonSet` parses the logs and generates Prometheus metrics.

      `spec.ptpClockThreshold`
      :   Specifies the PTP clock threshold settings. Optional. If the `ptpClockThreshold` stanza is not present, default values are used for the `ptpClockThreshold` fields. The stanza shows default `ptpClockThreshold` values. The `ptpClockThreshold` values configure how long after the PTP master clock is disconnected before PTP events are triggered. `holdOverTimeout` is the time value in seconds before the PTP clock event state changes to `FREERUN` when the PTP master clock is disconnected. The `maxOffsetThreshold` and `minOffsetThreshold` settings configure offset values in nanoseconds that compare against the values for `CLOCK_REALTIME` (`phc2sys`) or master offset (`ptp4l`). When the `ptp4l` or `phc2sys` offset value is outside this range, the PTP clock state is set to `FREERUN`. When the offset value is within this range, the PTP clock state is set to `LOCKED`.
2. Merge any other required changes and files with your custom site repository.
3. Push the changes to your site configuration repository to deploy PTP fast events to new sites using GitOps ZTP.

#### [11.2.9. Configuring the Image Registry Operator for local caching of images](#ztp-add-local-reg-for-sno-duprofile_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

OpenShift Container Platform manages image caching using a local registry. In edge computing use cases, clusters are often subject to bandwidth restrictions when communicating with centralized image registries, which might result in long image download times.

Long download times are unavoidable during initial deployment. Over time, there is a risk that CRI-O will erase the `/var/lib/containers/storage` directory in the case of an unexpected shutdown. To address long image download times, you can create a local image registry on remote managed clusters using GitOps Zero Touch Provisioning (ZTP). This is useful in Edge computing scenarios where clusters are deployed at the far edge of the network.

Before you can set up the local image registry with GitOps ZTP, you need to configure disk partitioning in the `ClusterInstance` CR that you use to install the remote managed cluster. After installation, you configure the local image registry using a `PolicyGenTemplate` CR. Then, the GitOps ZTP pipeline creates Persistent Volume (PV) and Persistent Volume Claim (PVC) CRs and patches the `imageregistry` configuration.

Note

The local image registry can only be used for user application images and cannot be used for the OpenShift Container Platform or Operator Lifecycle Manager operator images.

##### [11.2.9.1. Configuring disk partitioning with ClusterInstance](#ztp-configuring-disk-partitioning_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Configure disk partitioning for a managed cluster using a `ClusterInstance` CR and GitOps Zero Touch Provisioning (ZTP). The disk partition details in the `ClusterInstance` CR must match the underlying disk.

Important

You must complete this procedure at installation time.

**Prerequisites**

* Install Butane.

**Procedure**

1. Create the `storage.bu` file.

   ```
   variant: fcos
   version: 1.3.0
   storage:
     disks:
     - device: /dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0
       wipe_table: false
       partitions:
       - label: var-lib-containers
         start_mib: <start_of_partition>
         size_mib: <partition_size>
     filesystems:
       - path: /var/lib/containers
         device: /dev/disk/by-partlabel/var-lib-containers
         format: xfs
         wipe_filesystem: true
         with_mount_unit: true
         mount_options:
           - defaults
           - prjquota
   ```

   where:

   `<device>`
   :   Specifies the root disk.

   `<start_of_partition>`
   :   Specifies the start of the partition in MiB. If the value is too small, the installation fails.

   `<partition_size>`
   :   Specifies the size of the partition. If the value is too small, the deployment fails.
2. Convert the `storage.bu` to an Ignition file by running the following command:

   ```
   $ butane storage.bu
   ```

   The following example shows the output:

   ```
   {"ignition":{"version":"3.2.0"},"storage":{"disks":[{"device":"/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0","partitions":[{"label":"var-lib-containers","sizeMiB":0,"startMiB":250000}],"wipeTable":false}],"filesystems":[{"device":"/dev/disk/by-partlabel/var-lib-containers","format":"xfs","mountOptions":["defaults","prjquota"],"path":"/var/lib/containers","wipeFilesystem":true}]},"systemd":{"units":[{"contents":"# # Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target","enabled":true,"name":"var-lib-containers.mount"}]}}
   ```
3. Use a tool such as [JSON Pretty Print](https://jsonformatter.org/json-pretty-print) to convert the output into JSON format.
4. Copy the output into the `spec.nodes[].ignitionConfigOverride` field in the `ClusterInstance` CR, as shown in the following example:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-sno"
     namespace: "example-sno"
   spec:
     # ...
     nodes:
       - hostName: "node1.example.com"
         role: "master"
         ignitionConfigOverride: |
             {
               "ignition": {
                 "version": "3.2.0"
               },
               "storage": {
                 "disks": [
                   {
                     "device": "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0",
                     "partitions": [
                       {
                         "label": "var-lib-containers",
                         "sizeMiB": 0,
                         "startMiB": 250000
                       }
                     ],
                     "wipeTable": false
                   }
                 ],
                 "filesystems": [
                   {
                     "device": "/dev/disk/by-partlabel/var-lib-containers",
                     "format": "xfs",
                     "mountOptions": [
                       "defaults",
                       "prjquota"
                     ],
                     "path": "/var/lib/containers",
                     "wipeFilesystem": true
                   }
                 ]
               },
               "systemd": {
                 "units": [
                   {
                     "contents": "# # Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                     "enabled": true,
                     "name": "var-lib-containers.mount"
                   }
                 ]
               }
             }
   ```

   Note

   If the `spec.nodes[].ignitionConfigOverride` field does not exist, create it.

**Verification**

1. During or after installation, verify on the hub cluster that the `BareMetalHost` object shows the annotation by running the following command:

   ```
   $ oc get bmh -n my-sno-ns my-sno -ojson | jq '.metadata.annotations["bmac.agent-install.openshift.io/ignition-config-overrides"]
   ```

   The following example shows the output:

   ```
   "{\"ignition\":{\"version\":\"3.2.0\"},\"storage\":{\"disks\":[{\"device\":\"/dev/disk/by-id/wwn-0x6b07b250ebb9d0002a33509f24af1f62\",\"partitions\":[{\"label\":\"var-lib-containers\",\"sizeMiB\":0,\"startMiB\":250000}],\"wipeTable\":false}],\"filesystems\":[{\"device\":\"/dev/disk/by-partlabel/var-lib-containers\",\"format\":\"xfs\",\"mountOptions\":[\"defaults\",\"prjquota\"],\"path\":\"/var/lib/containers\",\"wipeFilesystem\":true}]},\"systemd\":{\"units\":[{\"contents\":\"# Generated by Butane\\n[Unit]\\nRequires=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\nAfter=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\n\\n[Mount]\\nWhere=/var/lib/containers\\nWhat=/dev/disk/by-partlabel/var-lib-containers\\nType=xfs\\nOptions=defaults,prjquota\\n\\n[Install]\\nRequiredBy=local-fs.target\",\"enabled\":true,\"name\":\"var-lib-containers.mount\"}]}}"
   ```
2. After installation, check the single-node OpenShift disk status.

   1. Enter into a debug session on the single-node OpenShift node by running the following command. This step instantiates a debug pod called `<node_name>-debug`:

      ```
      $ oc debug node/my-sno-node
      ```
   2. Set `/host` as the root directory within the debug shell by running the following command. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths:

      ```
      # chroot /host
      ```
   3. List information about all available block devices by running the following command:

      ```
      # lsblk
      ```

      The following example shows the output:

      ```
      NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
      sda      8:0    0 446.6G  0 disk
      ├─sda1   8:1    0     1M  0 part
      ├─sda2   8:2    0   127M  0 part
      ├─sda3   8:3    0   384M  0 part /boot
      ├─sda4   8:4    0 243.6G  0 part /var
      │                                /sysroot/ostree/deploy/rhcos/var
      │                                /usr
      │                                /etc
      │                                /
      │                                /sysroot
      └─sda5   8:5    0 202.5G  0 part /var/lib/containers
      ```
   4. Display information about the file system disk space usage by running the following command:

      ```
      # df -h
      ```

      The following example shows the output:

      ```
      Filesystem      Size  Used Avail Use% Mounted on
      devtmpfs        4.0M     0  4.0M   0% /dev
      tmpfs           126G   84K  126G   1% /dev/shm
      tmpfs            51G   93M   51G   1% /run
      /dev/sda4       244G  5.2G  239G   3% /sysroot
      tmpfs           126G  4.0K  126G   1% /tmp
      /dev/sda5       203G  119G   85G  59% /var/lib/containers
      /dev/sda3       350M  110M  218M  34% /boot
      tmpfs            26G     0   26G   0% /run/user/1000
      ```

##### [11.2.9.2. Configuring the image registry using PolicyGenTemplate CRs](#ztp-configuring-pgt-image-registry_ztp-advanced-policy-config) Copy linkLink copied to clipboard!

Use `PolicyGenTemplate` (PGT) CRs to apply the CRs required to configure the image registry and patch the `imageregistry` configuration.

**Prerequisites**

* You have configured a disk partition in the managed cluster.
* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data for use with GitOps Zero Touch Provisioning (ZTP).

**Procedure**

1. Configure the storage class, persistent volume claim, persistent volume, and image registry configuration in the appropriate `PolicyGenTemplate` CR. For example, to configure an individual site, add the following YAML to the file `example-sno-site.yaml`:

   ```
   sourceFiles:
     # storage class
     - fileName: StorageClass.yaml
       policyName: "sc-for-image-registry"
       metadata:
         name: image-registry-sc
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
     # persistent volume claim
     - fileName: StoragePVC.yaml
       policyName: "pvc-for-image-registry"
       metadata:
         name: image-registry-pvc
         namespace: openshift-image-registry
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
       spec:
         accessModes:
           - ReadWriteMany
         resources:
           requests:
             storage: 100Gi
         storageClassName: image-registry-sc
         volumeMode: Filesystem
     # persistent volume
     - fileName: ImageRegistryPV.yaml
       policyName: "pv-for-image-registry"
       metadata:
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
     - fileName: ImageRegistryConfig.yaml
       policyName: "config-for-image-registry"
       complianceType: musthave
       metadata:
         annotations:
           ran.openshift.io/ztp-deploy-wave: "100"
       spec:
         storage:
           pvc:
             claim: "image-registry-pvc"
   ```

   where:

   `ran.openshift.io/ztp-deploy-wave: "100"`
   :   Sets the appropriate value for `ztp-deploy-wave` depending on whether you are configuring image registries at the site, common, or group level. `ztp-deploy-wave: "100"` is suitable for development or testing because it allows you to group the referenced source files together.

   `ImageRegistryPV.yaml`
   :   In `ImageRegistryPV.yaml`, ensure that the `spec.local.path` field is set to `/var/imageregistry` to match the value set for the `mount_point` field in the `ClusterInstance` CR.

   Important

   Do not set `complianceType: mustonlyhave` for the `- fileName: ImageRegistryConfig.yaml` configuration. This can cause the registry pod deployment to fail.
2. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the GitOps ZTP ArgoCD application.

**Verification**

Use the following steps to troubleshoot errors with the local image registry on the managed clusters:

* Verify successful login to the registry while logged in to the managed cluster. Run the following commands:

  1. Export the managed cluster name:

     ```
     $ cluster=<managed_cluster_name>
     ```
  2. Get the managed cluster `kubeconfig` details:

     ```
     $ oc get secret -n $cluster $cluster-admin-password -o jsonpath='{.data.password}' | base64 -d > kubeadmin-password-$cluster
     ```
  3. Download and export the cluster `kubeconfig`:

     ```
     $ oc get secret -n $cluster $cluster-admin-kubeconfig -o jsonpath='{.data.kubeconfig}' | base64 -d > kubeconfig-$cluster && export KUBECONFIG=./kubeconfig-$cluster
     ```
  4. Verify access to the image registry from the managed cluster. See "Accessing the registry".
* Check that the `Config` CRD in the `imageregistry.operator.openshift.io` group instance is not reporting errors. Run the following command while logged in to the managed cluster:

  ```
  $ oc get image.config.openshift.io cluster -o yaml
  ```

  The following example shows the output:

  ```
  apiVersion: config.openshift.io/v1
  kind: Image
  metadata:
    annotations:
      include.release.openshift.io/ibm-cloud-managed: "true"
      include.release.openshift.io/self-managed-high-availability: "true"
      include.release.openshift.io/single-node-developer: "true"
      release.openshift.io/create-only: "true"
    creationTimestamp: "2021-10-08T19:02:39Z"
    generation: 5
    name: cluster
    resourceVersion: "688678648"
    uid: 0406521b-39c0-4cda-ba75-873697da75a4
  spec:
    additionalTrustedCA:
      name: acm-ice
  ```
* Check that the `PersistentVolumeClaim` on the managed cluster is populated with data. Run the following command while logged in to the managed cluster:

  ```
  $ oc get pv image-registry-sc
  ```
* Check that the `registry*` pod is running and is located under the `openshift-image-registry` namespace.

  ```
  $ oc get pods -n openshift-image-registry | grep registry*
  ```

  The following example shows the output:

  ```
  cluster-image-registry-operator-68f5c9c589-42cfg   1/1     Running     0          8d
  image-registry-5f8987879-6nx6h                     1/1     Running     0          8d
  ```
* Check that the disk partition on the managed cluster is correct:

  1. Open a debug shell to the managed cluster:

     ```
     $ oc debug node/sno-1.example.com
     ```
  2. Run `lsblk` to check the host disk partitions:

     ```
     sh-4.4# lsblk
     NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
     sda      8:0    0 446.6G  0 disk
       |-sda1   8:1    0     1M  0 part
       |-sda2   8:2    0   127M  0 part
       |-sda3   8:3    0   384M  0 part /boot
       |-sda4   8:4    0 336.3G  0 part /sysroot
       `-sda5   8:5    0 100.1G  0 part /var/imageregistry
     sdb      8:16   0 446.6G  0 disk
     sr0     11:0    1   104M  0 rom
     ```

     The `/var/imageregistry` mount point indicates that the disk is correctly partitioned.

### [11.3. Updating managed clusters in a disconnected environment with PolicyGenTemplate resources and TALM](#ztp-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

You can use the Topology Aware Lifecycle Manager (TALM) to manage the software lifecycle of managed clusters that you have deployed by using GitOps Zero Touch Provisioning (ZTP) and Topology Aware Lifecycle Manager (TALM). TALM uses Red Hat Advanced Cluster Management (RHACM) PolicyGenTemplate policies to manage and control changes applied to target clusters.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

#### [11.3.1. Setting up the disconnected environment](#talo-platform-prepare-for-update-env-setup_ztp-talm) Copy linkLink copied to clipboard!

TALM can perform both platform and Operator updates.

You must mirror both the platform image and Operator images that you want to update to in your mirror registry before you can use TALM to update your disconnected clusters.

**Procedure**

* For platform updates, you must perform the following steps:

  1. Mirror the required OpenShift Container Platform image repository. Ensure that the required platform image is mirrored by following the "Mirroring the OpenShift Container Platform image repository" procedure linked in the Additional resources. Save the contents of the `imageContentSources` section in the `imageContentSources.yaml` file:

     The following is example output:

     ```
     imageContentSources:
      - mirrors:
        - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
        source: quay.io/openshift-release-dev/ocp-release
      - mirrors:
        - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
        source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
     ```
  2. Save the image signature of the required platform image that was mirrored. You must add the image signature to the `PolicyGenTemplate` CR for platform updates. To get the image signature, perform the following steps:

     1. Specify the required OpenShift Container Platform tag by running the following command:

        ```
        $ OCP_RELEASE_NUMBER=<release_version>
        ```
     2. Specify the architecture of the cluster by running the following command:

        ```
        $ ARCHITECTURE=<cluster_architecture>
        ```

        + `<cluster_architecture>` specifies the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`.
     3. Get the release image digest from Quay by running the following command

        ```
        $ DIGEST="$(oc adm release info quay.io/openshift-release-dev/ocp-release:${OCP_RELEASE_NUMBER}-${ARCHITECTURE} | sed -n 's/Pull From: .*@//p')"
        ```
     4. Set the digest algorithm by running the following command:

        ```
        $ DIGEST_ALGO="${DIGEST%%:*}"
        ```
     5. Set the digest signature by running the following command:

        ```
        $ DIGEST_ENCODED="${DIGEST#*:}"
        ```
     6. Get the image signature from the [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/) website by running the following command:

        ```
        $ SIGNATURE_BASE64=$(curl -s "https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/${DIGEST_ALGO}=${DIGEST_ENCODED}/signature-1" | base64 -w0 && echo)
        ```
     7. Save the image signature to the `checksum-<OCP_RELEASE_NUMBER>.yaml` file by running the following commands:

        ```
        $ cat >checksum-${OCP_RELEASE_NUMBER}.yaml <<EOF
        ```

        ```
        ${DIGEST_ALGO}-${DIGEST_ENCODED}: ${SIGNATURE_BASE64}
        EOF
        ```
  3. Prepare the update graph. You have two options to prepare the update graph:

     1. Use the OpenShift Update Service.

        For more information about how to set up the graph on the hub cluster, see [Deploy the operator for OpenShift Update Service](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.4/html/clusters/managing-your-clusters#deploy-the-operator-for-cincinnati) and [Build the graph data init container](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.4/html/clusters/managing-your-clusters#build-the-graph-data-init-container).
     2. Make a local copy of the upstream graph. Host the update graph on an `http` or `https` server in the disconnected environment that has access to the managed cluster. To download the update graph, use the following command:

        ```
        $ curl -s https://api.openshift.com/api/upgrades_info/v1/graph?channel=stable-4.22 -o ~/upgrade-graph_stable-4.22
        ```
* For Operator updates, you must perform the following task:

  + Mirror the Operator catalogs. Ensure that the required Operator images are mirrored by following the procedure in the "Mirroring Operator catalogs for use with disconnected clusters" section.

#### [11.3.2. Performing a platform update with PolicyGenTemplate CRs](#talo-platform-update-PolicyGenTemplate_ztp-talm) Copy linkLink copied to clipboard!

You can perform a platform update with the TALM.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Update GitOps Zero Touch Provisioning (ZTP) to the latest version.
* Provision one or more managed clusters with GitOps ZTP.
* Mirror the required image repository.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Create a `PolicyGenTemplate` CR for the platform update:

   1. Save the following `PolicyGenTemplate` CR in the `du-upgrade.yaml` file:

      The following example shows the `PolicyGenTemplate` CR for platform update:

      ```
      apiVersion: ran.openshift.io/v1
      kind: PolicyGenTemplate
      metadata:
        name: "du-upgrade"
        namespace: "ztp-group-du-sno"
      spec:
        bindingRules:
          group-du-sno: ""
        mcp: "master"
        remediationAction: inform
        sourceFiles:
          - fileName: ImageSignature.yaml
            policyName: "platform-upgrade-prep"
            binaryData:
              ${DIGEST_ALGO}-${DIGEST_ENCODED}: ${SIGNATURE_BASE64}
          - fileName: DisconnectedICSP.yaml
            policyName: "platform-upgrade-prep"
            metadata:
              name: disconnected-internal-icsp-for-ocp
            spec:
              repositoryDigestMirrors:
                - mirrors:
                  - quay-intern.example.com/ocp4/openshift-release-dev
                  source: quay.io/openshift-release-dev/ocp-release
                - mirrors:
                  - quay-intern.example.com/ocp4/openshift-release-dev
                  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
          - fileName: ClusterVersion.yaml
            policyName: "platform-upgrade"
            metadata:
              name: version
            spec:
              channel: "stable-4.22"
              upstream: http://upgrade.example.com/images/upgrade-graph_stable-4.22
              desiredUpdate:
                version: 4.22.4
            status:
              history:
                - version: 4.22.4
                  state: "Completed"
      ```

      * `ImageSignature.yaml` - The `ConfigMap` CR contains the signature of the required release image to update to.
      * `${DIGEST_ALGO}-${DIGEST_ENCODED}: ${SIGNATURE_BASE64}` - Shows the image signature of the required OpenShift Container Platform release. Get the signature from the `checksum-${OCP_RELEASE_NUMBER}.yaml` file you saved when following the procedures in the "Setting up the environment" section.
      * `repositoryDigestMirrors` - Shows the mirror repository that contains the required OpenShift Container Platform image. Get the mirrors from the `imageContentSources.yaml` file that you saved when following the procedures in the "Setting up the environment" section.
      * `ClusterVersion.yaml` - Shows the `ClusterVersion` CR to trigger the update. The `channel`, `upstream`, and `desiredVersion` fields are all required for image precaching.

      The `PolicyGenTemplate` CR generates two policies:

      * The `du-upgrade-platform-upgrade-prep` policy does the preparation work for the platform update. It creates the `ConfigMap` CR for the required release image signature, creates the image content source of the mirrored release image repository, and updates the cluster version with the required update channel and the update graph reachable by the managed cluster in the disconnected environment.
      * The `du-upgrade-platform-upgrade` policy is used to perform platform upgrade.
   2. Add the `du-upgrade.yaml` file contents to the `kustomization.yaml` file located in the GitOps ZTP Git repository for the `PolicyGenTemplate` CRs and push the changes to the Git repository.

      ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.
   3. Check the created policies by running the following command:

      ```
      $ oc get policies -A | grep platform-upgrade
      ```
2. Create the `ClusterGroupUpdate` CR for the platform update with the `spec.enable` field set to `false`.

   1. Save the content of the platform update `ClusterGroupUpdate` CR with the `du-upgrade-platform-upgrade-prep` and the `du-upgrade-platform-upgrade` policies and the target clusters to the `cgu-platform-upgrade.yml` file, as shown in the following example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-platform-upgrade
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-platform-upgrade-prep
        - du-upgrade-platform-upgrade
        preCaching: false
        clusters:
        - spoke1
        remediationStrategy:
          maxConcurrency: 1
        enable: false
      ```
   2. Apply the `ClusterGroupUpdate` CR to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-platform-upgrade.yml
      ```
3. Optional: Precache the images for the platform update.

   1. Enable precaching in the `ClusterGroupUpdate` CR by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
      --patch '{"spec":{"preCaching": true}}' --type=merge
      ```
   2. Monitor the update process and wait for the pre-caching to complete. Check the status of pre-caching by running the following command on the hub cluster:

      ```
      $ oc get cgu cgu-platform-upgrade -o jsonpath='{.status.precaching.status}'
      ```
4. Start the platform update:

   1. Enable the `cgu-platform-upgrade` policy and disable pre-caching by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
      --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
      ```
   2. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```

#### [11.3.3. Performing an Operator update with PolicyGenTemplate CRs](#talo-operator-update-PolicyGenTemplate_ztp-talm) Copy linkLink copied to clipboard!

You can perform an Operator update with the TALM.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Update GitOps Zero Touch Provisioning (ZTP) to the latest version.
* Provision one or more managed clusters with GitOps ZTP.
* Mirror the required index image, bundle images, and all Operator images referenced in the bundle images.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Update the `PolicyGenTemplate` CR for the Operator update.

   1. Update the `du-upgrade` `PolicyGenTemplate` CR with the following additional contents in the `du-upgrade.yaml` file:

      ```
      apiVersion: ran.openshift.io/v1
      kind: PolicyGenTemplate
      metadata:
        name: "du-upgrade"
        namespace: "ztp-group-du-sno"
      spec:
        bindingRules:
          group-du-sno: ""
        mcp: "master"
        remediationAction: inform
        sourceFiles:
          - fileName: DefaultCatsrc.yaml
            remediationAction: inform
            policyName: "operator-catsrc-policy"
            metadata:
              name: redhat-operators-disconnected
            spec:
              displayName: Red Hat Operators Catalog
              image: registry.example.com:5000/olm/redhat-operators-disconnected:v4.22
              updateStrategy:
                registryPoll:
                  interval: 1h
            status:
              connectionState:
                  lastObservedState: READY
      ```

      * `image` - The index image URL contains the required Operator images. If the index images are always pushed to the same image name and tag, this change is not needed.
      * `updateStrategy` - Set how frequently the Operator Lifecycle Manager (OLM) polls the index image for new Operator versions with the `registryPoll.interval` field. This change is not needed if a new index image tag is always pushed for y-stream and z-stream Operator updates. The `registryPoll.interval` field can be set to a shorter interval to expedite the update, however shorter intervals increase computational load. To counteract this behavior, you can restore `registryPoll.interval` to the default value once the update is complete.
      * `lastObservedState` - Last observed state of the catalog connection. The `READY` value ensures that the `CatalogSource` policy is ready, indicating that the index pod is pulled and is running. This way, TALM upgrades the Operators based on up-to-date policy compliance states.
   2. This update generates one policy, `du-upgrade-operator-catsrc-policy`, to update the `redhat-operators-disconnected` catalog source with the new index images that contain the required Operators images.

      Note

      If you want to use the image precaching for Operators and there are Operators from a different catalog source other than `redhat-operators-disconnected`, you must perform the following tasks:

      * Prepare a separate catalog source policy with the new index image or registry poll interval update for the different catalog source.
      * Prepare a separate subscription policy for the required Operators that are from the different catalog source.

      For example, the required SRIOV-FEC Operator is available in the `certified-operators` catalog source. To update the catalog source and the Operator subscription, add the following contents to generate two policies, `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy`:

      ```
      apiVersion: ran.openshift.io/v1
      kind: PolicyGenTemplate
      metadata:
        name: "du-upgrade"
        namespace: "ztp-group-du-sno"
      spec:
        bindingRules:
          group-du-sno: ""
        mcp: "master"
        remediationAction: inform
        sourceFiles:
            # ...
          - fileName: DefaultCatsrc.yaml
            remediationAction: inform
            policyName: "fec-catsrc-policy"
            metadata:
              name: certified-operators
            spec:
              displayName: Intel SRIOV-FEC Operator
              image: registry.example.com:5000/olm/far-edge-sriov-fec:v4.10
              updateStrategy:
                registryPoll:
                  interval: 10m
          - fileName: AcceleratorsSubscription.yaml
            policyName: "subscriptions-fec-policy"
            spec:
              channel: "stable"
              source: certified-operators
      ```
   3. Remove the specified subscriptions channels in the common `PolicyGenTemplate` CR, if they exist. The default subscriptions channels from the GitOps ZTP image are used for the update.

      Note

      The default channel for the Operators applied through GitOps ZTP 4.22 is `stable`, except for the `performance-addon-operator`. As of OpenShift Container Platform 4.11, the `performance-addon-operator` functionality was moved to the `node-tuning-operator`. For the 4.10 release, the default channel for PAO is `v4.10`. You can also specify the default channels in the common `PolicyGenTemplate` CR.
   4. Push the `PolicyGenTemplate` CRs updates to the GitOps ZTP Git repository.

      ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.
   5. Check the created policies by running the following command:

      ```
      $ oc get policies -A | grep -E "catsrc-policy|subscription"
      ```
2. Apply the required catalog source updates before starting the Operator update.

   1. Save the content of the `ClusterGroupUpgrade` CR named `operator-upgrade-prep` with the catalog source policies and the target managed clusters to the `cgu-operator-upgrade-prep.yml` file:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-operator-upgrade-prep
        namespace: default
      spec:
        clusters:
        - spoke1
        enable: true
        managedPolicies:
        - du-upgrade-operator-catsrc-policy
        remediationStrategy:
          maxConcurrency: 1
      ```
   2. Apply the policy to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-operator-upgrade-prep.yml
      ```
   3. Monitor the update process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies -A | grep -E "catsrc-policy"
      ```
3. Create the `ClusterGroupUpgrade` CR for the Operator update with the `spec.enable` field set to `false`.

   1. Save the content of the Operator update `ClusterGroupUpgrade` CR with the `du-upgrade-operator-catsrc-policy` policy and the subscription policies created from the common `PolicyGenTemplate` and the target clusters to the `cgu-operator-upgrade.yml` file, as shown in the following example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-operator-upgrade
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-operator-catsrc-policy
        - common-subscriptions-policy
        preCaching: false
        clusters:
        - spoke1
        remediationStrategy:
          maxConcurrency: 1
        enable: false
      ```

      * `du-upgrade-operator-catsrc-policy` is needed by the image precaching feature to retrieve the Operator images from the catalog source.
      * `common-subscriptions-policy` contains Operator subscriptions. If you have followed the structure and content of the reference `PolicyGenTemplates`, all Operator subscriptions are grouped into the `common-subscriptions-policy` policy.

      Note

      One `ClusterGroupUpgrade` CR can only precache the images of the required Operators defined in the subscription policy from one catalog source included in the `ClusterGroupUpgrade` CR. If the required Operators are from different catalog sources, such as in the example of the SRIOV-FEC Operator, another `ClusterGroupUpgrade` CR must be created with `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy` policies for the SRIOV-FEC Operator images precaching and update.
   2. Apply the `ClusterGroupUpgrade` CR to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-operator-upgrade.yml
      ```
4. Optional: Precache the images for the Operator update.

   1. Before starting image precaching, verify the subscription policy is `NonCompliant` at this point by running the following command:

      ```
      $ oc get policy common-subscriptions-policy -n <policy_namespace>
      ```

      The following is example output:

      ```
      NAME                          REMEDIATION ACTION   COMPLIANCE STATE     AGE
      common-subscriptions-policy   inform               NonCompliant         27d
      ```
   2. Enable precaching in the `ClusterGroupUpgrade` CR by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
      --patch '{"spec":{"preCaching": true}}' --type=merge
      ```
   3. Monitor the process and wait for the precaching to complete. Check the status of precaching by running the following command on the managed cluster:

      ```
      $ oc get cgu cgu-operator-upgrade -o jsonpath='{.status.precaching.status}'
      ```
   4. Check if the precaching is completed before starting the update by running the following command:

      ```
      $ oc get cgu -n default cgu-operator-upgrade -ojsonpath='{.status.conditions}' | jq
      ```

      The following is example output:

      ```
      [
          {
            "lastTransitionTime": "2022-03-08T20:49:08.000Z",
            "message": "The ClusterGroupUpgrade CR is not enabled",
            "reason": "UpgradeNotStarted",
            "status": "False",
            "type": "Ready"
          },
          {
            "lastTransitionTime": "2022-03-08T20:55:30.000Z",
            "message": "Precaching is completed",
            "reason": "PrecachingCompleted",
            "status": "True",
            "type": "PrecachingDone"
          }
      ]
      ```
5. Start the Operator update.

   1. Enable the `cgu-operator-upgrade` `ClusterGroupUpgrade` CR and disable precaching to start the Operator update by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
      --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
      ```
   2. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```

#### [11.3.4. Troubleshooting missed Operator updates with PolicyGenTemplate CRs](#cnf-topology-aware-lifecycle-manager-operator-troubleshooting-PolicyGenTemplate_ztp-talm) Copy linkLink copied to clipboard!

In some scenarios, Topology Aware Lifecycle Manager (TALM) might miss Operator updates due to an out-of-date policy compliance state.

After a catalog source update, it takes time for the Operator Lifecycle Manager (OLM) to update the subscription status. The status of the subscription policy might continue to show as compliant while TALM decides whether remediation is needed. As a result, the Operator specified in the subscription policy does not get upgraded.

To avoid this scenario, add another catalog source configuration to the `PolicyGenTemplate` and specify this configuration in the subscription for any Operators that require an update.

**Procedure**

1. Add a catalog source configuration in the `PolicyGenTemplate` resource:

   ```
   - fileName: DefaultCatsrc.yaml
         remediationAction: inform
         policyName: "operator-catsrc-policy"
         metadata:
           name: redhat-operators-disconnected
         spec:
           displayName: Red Hat Operators Catalog
           image: registry.example.com:5000/olm/redhat-operators-disconnected:v{product-version}
           updateStrategy:
             registryPoll:
               interval: 1h
         status:
           connectionState:
               lastObservedState: READY
   - fileName: DefaultCatsrc.yaml
         remediationAction: inform
         policyName: "operator-catsrc-policy"
         metadata:
           name: redhat-operators-disconnected-v2
         spec:
           displayName: Red Hat Operators Catalog v2
           image: registry.example.com:5000/olm/redhat-operators-disconnected:<version>
           updateStrategy:
             registryPoll:
               interval: 1h
         status:
           connectionState:
               lastObservedState: READY
   ```

   * `name` - Update the name for the new configuration.
   * `displayName` - Update the display name for the new configuration.
   * `image` - Update the index image URL. This `fileName.spec.image` field overrides any configuration in the `DefaultCatsrc.yaml` file.
2. Update the `Subscription` resource to point to the new configuration for Operators that require an update:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: operator-subscription
     namespace: operator-namspace
   # ...
   spec:
     source: redhat-operators-disconnected-v2
   # ...
   ```

   * `redhat-operators-disconnected-v2` specifies the name of the additional catalog source configuration that you defined in the `PolicyGenTemplate` resource.

#### [11.3.5. Performing a platform and an Operator update together](#talo-operator-and-platform-update_ztp-talm) Copy linkLink copied to clipboard!

You can perform a platform and an Operator update at the same time.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Update GitOps Zero Touch Provisioning (ZTP) to the latest version.
* Provision one or more managed clusters with GitOps ZTP.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Create the `PolicyGenTemplate` CR for the updates by following the steps described in the "Performing a platform update" and "Performing an Operator update" sections.
2. Apply the prep work for the platform and the Operator update.

   1. Save the content of the `ClusterGroupUpgrade` CR with the policies for platform update preparation work, catalog source updates, and target clusters to the `cgu-platform-operator-upgrade-prep.yml` file, for example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-platform-operator-upgrade-prep
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-platform-upgrade-prep
        - du-upgrade-operator-catsrc-policy
        clusterSelector:
        - group-du-sno
        remediationStrategy:
          maxConcurrency: 10
        enable: true
      ```
   2. Apply the `cgu-platform-operator-upgrade-prep.yml` file to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-platform-operator-upgrade-prep.yml
      ```
   3. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```
3. Create the `ClusterGroupUpdate` CR for the platform and the Operator update with the `spec.enable` field set to `false`.

   1. Save the contents of the platform and Operator update `ClusterGroupUpdate` CR with the policies and the target clusters to the `cgu-platform-operator-upgrade.yml` file, as shown in the following example:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: cgu-du-upgrade
        namespace: default
      spec:
        managedPolicies:
        - du-upgrade-platform-upgrade
        - du-upgrade-operator-catsrc-policy
        - common-subscriptions-policy
        preCaching: true
        clusterSelector:
        - group-du-sno
        remediationStrategy:
          maxConcurrency: 1
        enable: false
      ```

      * `du-upgrade-platform-upgrade` is the platform update policy.
      * `du-upgrade-operator-catsrc-policy` is the policy containing the catalog source information for the Operators to be updated. It is needed for the precaching feature to determine which Operator images to download to the managed cluster.
      * `common-subscriptions-policy` is the policy to update the Operators.
   2. Apply the `cgu-platform-operator-upgrade.yml` file to the hub cluster by running the following command:

      ```
      $ oc apply -f cgu-platform-operator-upgrade.yml
      ```
4. Optional: Precache the images for the platform and the Operator update.

   1. Enable precaching in the `ClusterGroupUpgrade` CR by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
      --patch '{"spec":{"preCaching": true}}' --type=merge
      ```
   2. Monitor the update process and wait for the precaching to complete. Check the status of precaching by running the following command on the managed cluster:

      ```
      $ oc get jobs,pods -n openshift-talm-pre-cache
      ```
   3. Check if the precaching is completed before starting the update by running the following command:

      ```
      $ oc get cgu cgu-du-upgrade -ojsonpath='{.status.conditions}'
      ```
5. Start the platform and Operator update.

   1. Enable the `cgu-du-upgrade` `ClusterGroupUpgrade` CR to start the platform and the Operator update by running the following command:

      ```
      $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
      --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
      ```
   2. Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

      ```
      $ oc get policies --all-namespaces
      ```

      Note

      The CRs for the platform and Operator updates can be created from the beginning by configuring the setting to `spec.enable: true`. In this case, the update starts immediately after precaching completes and there is no need to manually enable the CR.

      Both precaching and the update create extra resources, such as policies, placement bindings, placement rules, managed cluster actions, and managed cluster view, to help complete the procedures. Setting the `afterCompletion.deleteObjects` field to `true` deletes all these resources after the updates complete.

#### [11.3.6. Removing Performance Addon Operator subscriptions from deployed clusters with PolicyGenTemplate CRs](#talm-pao-update-PolicyGenTemplate_ztp-talm) Copy linkLink copied to clipboard!

In earlier versions of OpenShift Container Platform, the Performance Addon Operator provided automatic, low latency performance tuning for applications. In OpenShift Container Platform 4.11 or later, these functions are part of the Node Tuning Operator.

Do not install the Performance Addon Operator on clusters running OpenShift Container Platform 4.11 or later. If you upgrade to OpenShift Container Platform 4.11 or later, the Node Tuning Operator automatically removes the Performance Addon Operator.

Note

You need to remove any policies that create Performance Addon Operator subscriptions to prevent a re-installation of the Operator.

The reference DU profile includes the Performance Addon Operator in the `PolicyGenTemplate` CR `common-ranGen.yaml`. To remove the subscription from deployed managed clusters, you must update `common-ranGen.yaml`.

Note

If you install Performance Addon Operator 4.10.3-5 or later on OpenShift Container Platform 4.11 or later, the Performance Addon Operator detects the cluster version and automatically hibernates to avoid interfering with the Node Tuning Operator functions. However, to ensure best performance, remove the Performance Addon Operator from your OpenShift Container Platform 4.11 clusters.

**Prerequisites**

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for ArgoCD.
* Update to OpenShift Container Platform 4.11 or later.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Change the `complianceType` to `mustnothave` for the Performance Addon Operator namespace, Operator group, and subscription in the `common-ranGen.yaml` file.

   ```
   - fileName: PaoSubscriptionNS.yaml
     policyName: "subscriptions-policy"
     complianceType: mustnothave
   - fileName: PaoSubscriptionOperGroup.yaml
     policyName: "subscriptions-policy"
     complianceType: mustnothave
   - fileName: PaoSubscription.yaml
     policyName: "subscriptions-policy"
     complianceType: mustnothave
   ```
2. Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The status of the `common-subscriptions-policy` policy changes to `Non-Compliant`.
3. Apply the change to your target clusters by using the Topology Aware Lifecycle Manager. For more information about rolling out configuration changes, see the "Additional resources" section.
4. Monitor the process. When the status of the `common-subscriptions-policy` policy for a target cluster is `Compliant`, the Performance Addon Operator has been removed from the cluster. Get the status of the `common-subscriptions-policy` by running the following command:

   ```
   $ oc get policy -n ztp-common common-subscriptions-policy
   ```
5. Delete the Performance Addon Operator namespace, Operator group and subscription CRs from `spec.sourceFiles` in the `common-ranGen.yaml` file.
6. Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The policy remains compliant.

#### [11.3.7. Precaching user-specified images with TALM on single-node OpenShift clusters](#talm-prechache-user-specified-images-concept_ztp-talm) Copy linkLink copied to clipboard!

You can precache application-specific workload images on single-node OpenShift clusters before updating your applications.

You can specify the configuration options for the precaching jobs by using the following custom resources (CR):

* `PreCachingConfig` CR
* `ClusterGroupUpgrade` CR

TALM derives the platform image from the `ClusterVersion` object in the managed policies. TALM derives Operator index images from `CatalogSource` objects that the managed policies reference.

Note

All fields in the `PreCachingConfig` CR are optional.

The following example shows a `PreCachingConfig` CR:

```
apiVersion: ran.openshift.io/v1alpha1
kind: PreCachingConfig
metadata:
  name: exampleconfig
  namespace: exampleconfig-ns
spec:
  overrides:
    operatorsPackagesAndChannels:
      - local-storage-operator: stable
      - ptp-operator: stable
      - sriov-network-operator: stable
  spaceRequired: 30 Gi
  excludePrecachePatterns:
    - aws
    - vsphere
  additionalImages:
    - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
    - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
```

* `overrides` - Specifies Operator packages and channels to precache instead of the values that TALM derives from the managed policies. The only supported override is `operatorsPackagesAndChannels`. TALM ignores the deprecated `platformImage` and `operatorsIndexes` override fields if they are present.
* `spaceRequired` - Specifies the minimum required disk space on the cluster. If unspecified, TALM defines a default value for OpenShift Container Platform images. The disk space field must include an integer value and the storage unit. For example: `40 GiB`, `200 MB`, `1 TiB`.
* `excludePrecachePatterns` - Specifies the images to exclude from precaching based on image name matching.
* `additionalImages` - Specifies the list of additional images to precache.

The following example shows a `ClusterGroupUpgrade` CR with a `PreCachingConfig` CR reference:

```
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu
spec:
  preCaching: true
  preCachingConfigRef:
    name: exampleconfig
    namespace: exampleconfig-ns
```

* `preCaching` set to `true` enables the precaching job.
* `preCachingConfigRef.name` specifies the `PreCachingConfig` CR that you want to use.
* `preCachingConfigRef.namespace` specifies the namespace of the `PreCachingConfig` CR that you want to use.

##### [11.3.7.1. Creating the custom resources for precaching](#talm-prechache-user-specified-images-preparing-crs_ztp-talm) Copy linkLink copied to clipboard!

You must create the `PreCachingConfig` CR before or concurrently with the `ClusterGroupUpgrade` CR.

**Procedure**

1. Create the `PreCachingConfig` CR with the list of additional images you want to precache.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: PreCachingConfig
   metadata:
     name: exampleconfig
     namespace: default
   spec:
   # ...
     spaceRequired: 30Gi
     additionalImages:
       - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
       - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
       - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
   ```

   * `namespace` must be accessible to the hub cluster.
   * `spaceRequired` - It is recommended to set the minimum disk space required field to ensure that there is sufficient storage space for the precached images.
2. Create a `ClusterGroupUpgrade` CR with the `preCaching` field set to `true` and specify the `PreCachingConfig` CR created in the previous step:

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu
     namespace: default
   spec:
     clusters:
     - sno1
     - sno2
     preCaching: true
     preCachingConfigRef:
     - name: exampleconfig
       namespace: default
     managedPolicies:
       - du-upgrade-platform-upgrade
       - du-upgrade-operator-catsrc-policy
       - common-subscriptions-policy
     remediationStrategy:
       timeout: 240
   ```

   Warning

   Once you install the images on the cluster, you cannot change or delete them.
3. When you want to start precaching the images, apply the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc apply -f cgu.yaml
   ```

   TALM verifies the `ClusterGroupUpgrade` CR. From this point, you can continue with the TALM precaching workflow.

   Note

   All sites are precached concurrently.

**Verification**

1. Check the precaching status on the hub cluster where the `ClusterGroupUpgrade` CR is applied by running the following command:

   ```
   $ oc get cgu <cgu_name> -n <cgu_namespace> -oyaml
   ```

   The following example shows the derived precaching specification. The `platformImage` and `operatorsIndexes` values come from the managed policies, not from `PreCachingConfig` overrides.

   ```
     precaching:
       spec:
         platformImage: quay.io/openshift-release-dev/ocp-release@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
         operatorsIndexes:
           - registry.example.com:5000/custom-redhat-operators:1.0.0
         operatorsPackagesAndChannels:
           - local-storage-operator: stable
           - ptp-operator: stable
           - sriov-network-operator: stable
         excludePrecachePatterns:
           - aws
           - vsphere
         additionalImages:
           - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
           - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
           - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
         spaceRequired: "30"
       status:
         sno1: Starting
         sno2: Starting
   ```

   The precaching configurations are validated by checking if the managed policies exist. Valid configurations of the `ClusterGroupUpgrade` and the `PreCachingConfig` CRs result in the following statuses:

   The following example shows the output of valid CRs:

   ```
   - lastTransitionTime: "2023-01-01T00:00:01Z"
     message: All selected clusters are valid
     reason: ClusterSelectionCompleted
     status: "True"
     type: ClusterSelected
   - lastTransitionTime: "2023-01-01T00:00:02Z"
     message: Completed validation
     reason: ValidationCompleted
     status: "True"
     type: Validated
   - lastTransitionTime: "2023-01-01T00:00:03Z"
     message: Precaching spec is valid and consistent
     reason: PrecacheSpecIsWellFormed
     status: "True"
     type: PrecacheSpecValid
   - lastTransitionTime: "2023-01-01T00:00:04Z"
     message: Precaching in progress for 1 clusters
     reason: InProgress
     status: "False"
     type: PrecachingSucceeded
   ```

   The following example shows an invalid `PreCachingConfig` CR:

   ```
   Type:    "PrecacheSpecValid"
   Status:  False,
   Reason:  "PrecacheSpecIncomplete"
   Message: "Precaching spec is incomplete: failed to get PreCachingConfig resource due to PreCachingConfig.ran.openshift.io "<precaching_cr_name>" not found"
   ```
2. You can find the precaching job by running the following command on the managed cluster:

   ```
   $ oc get jobs -n openshift-talo-pre-cache
   ```

   The following example shows a precaching job in progress:

   ```
   NAME        COMPLETIONS       DURATION      AGE
   pre-cache   0/1               1s            1s
   ```
3. You can check the status of the pod created for the precaching job by running the following command:

   ```
   $ oc describe pod pre-cache -n openshift-talo-pre-cache
   ```

   The following example shows a precaching job in progress:

   ```
   Type        Reason              Age    From              Message
   Normal      SuccesfulCreate     19s    job-controller    Created pod: pre-cache-abcd1
   ```
4. You can get live updates on the status of the job by running the following command:

   ```
   $ oc logs -f pre-cache-abcd1 -n openshift-talo-pre-cache
   ```
5. To verify the precache job is successfully completed, run the following command:

   ```
   $ oc describe pod pre-cache -n openshift-talo-pre-cache
   ```

   The following example shows a completed precache job:

   ```
   Type        Reason              Age    From              Message
   Normal      SuccesfulCreate     5m19s  job-controller    Created pod: pre-cache-abcd1
   Normal      Completed           19s    job-controller    Job completed
   ```
6. To verify that the images are successfully precached on the single-node OpenShift, do the following:

   1. Enter into the node in debug mode:

      ```
      $ oc debug node/cnfdf00.example.lab
      ```
   2. Change root to `host`:

      ```
      $ chroot /host/
      ```
   3. Search for the required images:

      ```
      $ sudo podman images | grep <operator_name>
      ```

#### [11.3.8. About the auto-created ClusterGroupUpgrade CR for GitOps ZTP](#talo-precache-autocreated-cgu-for-ztp_ztp-talm) Copy linkLink copied to clipboard!

TALM has a controller called `ManagedClusterForCGU` that monitors the `Ready` state of the `ManagedCluster` CRs on the hub cluster and creates the `ClusterGroupUpgrade` CRs for GitOps Zero Touch Provisioning (ZTP).

For any managed cluster in the `Ready` state without a `ztp-done` label applied, the `ManagedClusterForCGU` controller automatically creates a `ClusterGroupUpgrade` CR in the `ztp-install` namespace with its associated RHACM policies that are created during the GitOps ZTP process. TALM then remediates the set of configuration policies that are listed in the auto-created `ClusterGroupUpgrade` CR to push the configuration CRs to the managed cluster.

If there are no policies for the managed cluster at the time when the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR with no policies is created. Upon completion of the `ClusterGroupUpgrade` the managed cluster is labeled as `ztp-done`. If there are policies that you want to apply for that managed cluster, manually create a `ClusterGroupUpgrade` as a Day 2 operation.

**Procedure**

* View the auto-created `ClusterGroupUpgrade` CR for GitOps ZTP:

  The following example shows an auto-created `ClusterGroupUpgrade` CR for GitOps ZTP:

  ```
  apiVersion: ran.openshift.io/v1alpha1
  kind: ClusterGroupUpgrade
  metadata:
    generation: 1
    name: spoke1
    namespace: ztp-install
    ownerReferences:
    - apiVersion: cluster.open-cluster-management.io/v1
      blockOwnerDeletion: true
      controller: true
      kind: ManagedCluster
      name: spoke1
      uid: 98fdb9b2-51ee-4ee7-8f57-a84f7f35b9d5
    resourceVersion: "46666836"
    uid: b8be9cd2-764f-4a62-87d6-6b767852c7da
  spec:
    actions:
      afterCompletion:
        addClusterLabels:
          ztp-done: ""
        deleteClusterLabels:
          ztp-running: ""
        deleteObjects: true
      beforeEnable:
        addClusterLabels:
          ztp-running: ""
    clusters:
    - spoke1
    enable: true
    managedPolicies:
    - common-spoke1-config-policy
    - common-spoke1-subscriptions-policy
    - group-spoke1-config-policy
    - spoke1-config-policy
    - group-spoke1-validator-du-policy
    preCaching: false
    remediationStrategy:
      maxConcurrency: 1
      timeout: 240
  ```

  + `ztp-done: ""` is applied to the managed cluster when TALM completes the cluster configuration.
  + `ztp-running: ""` is applied to the managed cluster when TALM starts deploying the configuration policies.

## [Chapter 12. Using hub templates in PolicyGenerator or PolicyGenTemplate CRs](#ztp-using-hub-cluster-templates-pgt) Copy linkLink copied to clipboard!

Topology Aware Lifecycle Manager supports Red Hat Advanced Cluster Management (RHACM) hub cluster template functions in configuration policies used with GitOps Zero Touch Provisioning (ZTP).

Hub-side cluster templates allow you to define configuration policies that can be dynamically customized to the target clusters. This reduces the need to create separate policies for many clusters with similar configurations but with different values.

Important

Policy templates are restricted to the same namespace as the namespace where the policy is defined. This means you must create the objects referenced in the hub template in the same namespace where the policy is created.

Important

Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#integrate-policy-generator) documentation.

### [12.1. Specifying group and site configurations in group PolicyGenerator or PolicyGentemplate CRs](#ztp-specifying-nics-in-pgt-crs-with-hub-cluster-templates_hub-cluster-templates-pgt) Copy linkLink copied to clipboard!

You can manage the configuration of fleets of clusters with `ConfigMap` CRs by using hub templates to populate the group and site values in the generated policies that get applied to the managed clusters. Using hub templates in site `PolicyGenerator` or `PolicyGentemplate` CRs means that you do not need to create a policy CR for each site.

You can group the clusters in a fleet in various categories, depending on the use case, for example hardware type or region. Each cluster should have a label corresponding to the group or groups that the cluster is in. If you manage the configuration values for each group in different `ConfigMap` CRs, then you require only one group policy CR to apply the changes to all the clusters in the group by using hub templates.

The following example shows you how to use three `ConfigMap` CRs and one `PolicyGenerator` CR to apply both site and group configuration to clusters grouped by hardware type and region.

Note

There is a [1 MiB size limit](https://kubernetes.io/docs/concepts/configuration/configmap/#motivation) (Kubernetes documentation) for `ConfigMap` CRs. The effective size for the `ConfigMap` CRs is further limited by the `last-applied-configuration` annotation. To avoid the `last-applied-configuration` limitation, add the following annotation to the template `ConfigMap`:

```
argocd.argoproj.io/sync-options: Replace=true
```

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the GitOps ZTP ArgoCD application.

**Procedure**

1. Create three `ConfigMap` CRs that contain the group and site configuration:

   1. Create a `ConfigMap` CR named `group-hardware-types-configmap` to hold the hardware-specific configuration. For example:

      ```
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: group-hardware-types-configmap
        namespace: ztp-group
        annotations:
          argocd.argoproj.io/sync-options: Replace=true
      data:
        # SriovNetworkNodePolicy.yaml
        hardware-type-1-sriov-node-policy-pfNames-1: "[\"ens5f0\"]"
        hardware-type-1-sriov-node-policy-pfNames-2: "[\"ens7f0\"]"
        # PerformanceProfile.yaml
        hardware-type-1-cpu-isolated: "2-31,34-63"
        hardware-type-1-cpu-reserved: "0-1,32-33"
        hardware-type-1-hugepages-default: "1G"
        hardware-type-1-hugepages-size: "1G"
        hardware-type-1-hugepages-count: "32"
      ```

      where:

      `argocd.argoproj.io/sync-options`
      :   The `argocd.argoproj.io/sync-options` annotation is required only if the `ConfigMap` is larger than 1 MiB in size.
   2. Create a `ConfigMap` CR named `group-zones-configmap` to hold the regional configuration. For example:

      ```
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: group-zones-configmap
        namespace: ztp-group
      data:
        # ClusterLogForwarder.yaml
        zone-1-cluster-log-fwd-outputs: "[{\"type\":\"kafka\", \"name\":\"kafka-open\", \"url\":\"tcp://10.46.55.190:9092/test\"}]"
        zone-1-cluster-log-fwd-pipelines: "[{\"inputRefs\":[\"audit\", \"infrastructure\"], \"labels\": {\"label1\": \"test1\", \"label2\": \"test2\", \"label3\": \"test3\", \"label4\": \"test4\"}, \"name\": \"all-to-default\", \"outputRefs\": [\"kafka-open\"]}]"
      ```
   3. Create a `ConfigMap` CR named `site-data-configmap` to hold the site-specific configuration. For example:

      ```
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: site-data-configmap
        namespace: ztp-group
      data:
        # SriovNetwork.yaml
        du-sno-1-zone-1-sriov-network-vlan-1: "140"
        du-sno-1-zone-1-sriov-network-vlan-2: "150"
      ```

   Note

   Each `ConfigMap` CR must be in the same namespace as the policy to be generated from the group `PolicyGenerator` CR.
2. Commit the `ConfigMap` CRs in Git, and then push to the Git repository being monitored by the Argo CD application.
3. Apply the hardware type and region labels to the clusters. The following command applies to a single cluster named `du-sno-1-zone-1` and the labels chosen are `"hardware-type": "hardware-type-1"` and `"group-du-sno-zone": "zone-1"`:

   ```
   $ oc patch managedclusters.cluster.open-cluster-management.io/du-sno-1-zone-1 --type merge -p '{"metadata":{"labels":{"hardware-type": "hardware-type-1", "group-du-sno-zone": "zone-1"}}}'
   ```
4. Depending on your requirements, Create a group `PolicyGenerator` or `PolicyGentemplate` CR that uses hub templates to obtain the required data from the `ConfigMap` objects:

   1. Create a group `PolicyGenerator` CR. This example `PolicyGenerator` CR configures logging, VLAN IDs, NICs and Performance Profile for the clusters that match the labels listed the under `policyDefaults.placement` field:

      ```
      ---
      apiVersion: policy.open-cluster-management.io/v1
      kind: PolicyGenerator
      metadata:
          name: group-du-sno-pgt
      placementBindingDefaults:
          name: group-du-sno-pgt-placement-binding
      policyDefaults:
          placement:
              labelSelector:
                  matchExpressions:
                      - key: group-du-sno-zone
                        operator: In
                        values:
                          - zone-1
                      - key: hardware-type
                        operator: In
                        values:
                          - hardware-type-1
          remediationAction: inform
          severity: low
          namespaceSelector:
              exclude:
                  - kube-*
              include:
                  - '*'
          evaluationInterval:
              compliant: 10m
              noncompliant: 10s
      policies:
          - name: group-du-sno-pgt-group-du-sno-cfg-policy
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "10"
            manifests:
              - path: source-crs/ClusterLogForwarder.yaml
                patches:
                  - spec:
                      outputs: '{{hub fromConfigMap "" "group-zones-configmap" (printf "%s-cluster-log-fwd-outputs" (index .ManagedClusterLabels "group-du-sno-zone")) | toLiteral hub}}'
                      pipelines: '{{hub fromConfigMap "" "group-zones-configmap" (printf "%s-cluster-log-fwd-pipelines" (index .ManagedClusterLabels "group-du-sno-zone")) | toLiteral hub}}'
              - path: source-crs/PerformanceProfile-MCP-master.yaml
                patches:
                  - metadata:
                      name: openshift-node-performance-profile
                    spec:
                      additionalKernelArgs:
                          - rcupdate.rcu_normal_after_boot=0
                          - vfio_pci.enable_sriov=1
                          - vfio_pci.disable_idle_d3=1
                          - efi=runtime
                      cpu:
                          isolated: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-cpu-isolated" (index .ManagedClusterLabels "hardware-type")) hub}}'
                          reserved: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-cpu-reserved" (index .ManagedClusterLabels "hardware-type")) hub}}'
                      hugepages:
                          defaultHugepagesSize: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-hugepages-default" (index .ManagedClusterLabels "hardware-type")) hub}}'
                          pages:
                              - count: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-hugepages-count" (index .ManagedClusterLabels "hardware-type")) | toInt hub}}'
                                size: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-hugepages-size" (index .ManagedClusterLabels "hardware-type")) hub}}'
                      realTimeKernel:
                          enabled: true
          - name: group-du-sno-pgt-group-du-sno-sriov-policy
            policyAnnotations:
              ran.openshift.io/ztp-deploy-wave: "100"
            manifests:
              - path: source-crs/SriovNetwork.yaml
                patches:
                  - metadata:
                      name: sriov-nw-du-fh
                    spec:
                      resourceName: du_fh
                      vlan: '{{hub fromConfigMap "" "site-data-configmap" (printf "%s-sriov-network-vlan-1" .ManagedClusterName) | toInt hub}}'
              - path: source-crs/SriovNetworkNodePolicy-MCP-master.yaml
                patches:
                  - metadata:
                      name: sriov-nnp-du-fh
                    spec:
                      deviceType: netdevice
                      isRdma: false
                      nicSelector:
                          pfNames: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-sriov-node-policy-pfNames-1" (index .ManagedClusterLabels "hardware-type")) | toLiteral hub}}'
                      numVfs: 8
                      priority: 10
                      resourceName: du_fh
              - path: source-crs/SriovNetwork.yaml
                patches:
                  - metadata:
                      name: sriov-nw-du-mh
                    spec:
                      resourceName: du_mh
                      vlan: '{{hub fromConfigMap "" "site-data-configmap" (printf "%s-sriov-network-vlan-2" .ManagedClusterName) | toInt hub}}'
              - path: source-crs/SriovNetworkNodePolicy-MCP-master.yaml
                patches:
                  - metadata:
                      name: sriov-nw-du-fh
                    spec:
                      deviceType: netdevice
                      isRdma: false
                      nicSelector:
                          pfNames: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-sriov-node-policy-pfNames-2" (index .ManagedClusterLabels "hardware-type")) | toLiteral hub}}'
                      numVfs: 8
                      priority: 10
                      resourceName: du_fh
      ```
   2. Create a group `PolicyGenTemplate` CR. This example `PolicyGenTemplate` CR configures logging, VLAN IDs, NICs and Performance Profile for the clusters that match the labels listed under `spec.bindingRules`:

      ```
      apiVersion: ran.openshift.io/v1
      kind: PolicyGenTemplate
      metadata:
        name: group-du-sno-pgt
        namespace: ztp-group
      spec:
        bindingRules:
          # These policies will correspond to all clusters with these labels
          group-du-sno-zone: "zone-1"
          hardware-type: "hardware-type-1"
        mcp: "master"
        sourceFiles:
          - fileName: ClusterLogForwarder.yaml # wave 10
            policyName: "group-du-sno-cfg-policy"
            spec:
              outputs: '{{hub fromConfigMap "" "group-zones-configmap" (printf "%s-cluster-log-fwd-outputs" (index .ManagedClusterLabels "group-du-sno-zone")) | toLiteral hub}}'
              pipelines: '{{hub fromConfigMap "" "group-zones-configmap" (printf "%s-cluster-log-fwd-pipelines" (index .ManagedClusterLabels "group-du-sno-zone")) | toLiteral hub}}'

          - fileName: PerformanceProfile.yaml # wave 10
            policyName: "group-du-sno-cfg-policy"
            metadata:
              name: openshift-node-performance-profile
            spec:
              additionalKernelArgs:
              - rcupdate.rcu_normal_after_boot=0
              - vfio_pci.enable_sriov=1
              - vfio_pci.disable_idle_d3=1
              - efi=runtime
              cpu:
                isolated: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-cpu-isolated" (index .ManagedClusterLabels "hardware-type")) hub}}'
                reserved: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-cpu-reserved" (index .ManagedClusterLabels "hardware-type")) hub}}'
              hugepages:
                defaultHugepagesSize: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-hugepages-default" (index .ManagedClusterLabels "hardware-type")) hub}}'
                pages:
                  - size: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-hugepages-size" (index .ManagedClusterLabels "hardware-type")) hub}}'
                    count: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-hugepages-count" (index .ManagedClusterLabels "hardware-type")) | toInt hub}}'
              realTimeKernel:
                enabled: true

          - fileName: SriovNetwork.yaml # wave 100
            policyName: "group-du-sno-sriov-policy"
            metadata:
              name: sriov-nw-du-fh
            spec:
              resourceName: du_fh
              vlan: '{{hub fromConfigMap "" "site-data-configmap" (printf "%s-sriov-network-vlan-1" .ManagedClusterName) | toInt hub}}'

          - fileName: SriovNetworkNodePolicy.yaml # wave 100
            policyName: "group-du-sno-sriov-policy"
            metadata:
              name: sriov-nnp-du-fh
            spec:
              deviceType: netdevice
              isRdma: false
              nicSelector:
                pfNames: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-sriov-node-policy-pfNames-1" (index .ManagedClusterLabels "hardware-type")) | toLiteral hub}}'
              numVfs: 8
              priority: 10
              resourceName: du_fh

          - fileName: SriovNetwork.yaml # wave 100
            policyName: "group-du-sno-sriov-policy"
            metadata:
              name: sriov-nw-du-mh
            spec:
              resourceName: du_mh
              vlan: '{{hub fromConfigMap "" "site-data-configmap" (printf "%s-sriov-network-vlan-2" .ManagedClusterName) | toInt hub}}'

          - fileName: SriovNetworkNodePolicy.yaml # wave 100
            policyName: "group-du-sno-sriov-policy"
            metadata:
              name: sriov-nw-du-fh
            spec:
              deviceType: netdevice
              isRdma: false
              nicSelector:
                pfNames: '{{hub fromConfigMap "" "group-hardware-types-configmap" (printf "%s-sriov-node-policy-pfNames-2" (index .ManagedClusterLabels "hardware-type")) | toLiteral hub}}'
              numVfs: 8
              priority: 10
              resourceName: du_fh
      ```

   Note

   To retrieve site-specific configuration values, use the `.ManagedClusterName` field. This is a template context value set to the name of the target managed cluster.

   To retrieve group-specific configuration, use the `.ManagedClusterLabels` field. This is a template context value set to the value of the managed cluster’s labels.
5. Commit the site `PolicyGenerator` or `PolicyGentemplate` CR in Git and push to the Git repository that is monitored by the ArgoCD application.

   Note

   Subsequent changes to the referenced `ConfigMap` CR are not automatically synced to the applied policies. You need to manually sync the new `ConfigMap` changes to update existing `PolicyGenerator` CRs. See "Syncing new ConfigMap changes to existing PolicyGenerator or PolicyGenTemplate CRs".

   You can use the same `PolicyGenerator` or `PolicyGentemplate` CR for multiple clusters. If there is a configuration change, then the only modifications you need to make are to the `ConfigMap` objects that hold the configuration for each cluster and the labels of the managed clusters.

### [12.2. Syncing new ConfigMap changes to existing PolicyGenerator or PolicyGentemplate CRs](#ztp-syncing-new-configmap-changes-to-existing-pgt-crs_hub-cluster-templates-pgt) Copy linkLink copied to clipboard!

You can sync updated `ConfigMap` CR changes to existing `PolicyGenerator` or `PolicyGentemplate` CRs deployed on the hub cluster.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created a `PolicyGenerator` or `PolicyGentemplate` CR that pulls information from a `ConfigMap` CR using hub cluster templates.

**Procedure**

1. Update the contents of your `ConfigMap` CR, and apply the changes in the hub cluster.
2. To sync the contents of the updated `ConfigMap` CR to the deployed policy, do either of the following:

   1. Option 1: Delete the existing policy. ArgoCD uses the `PolicyGenerator` or `PolicyGentemplate` CR to immediately recreate the deleted policy. For example, run the following command:

      ```
      $ oc delete policy <policy_name> -n <policy_namespace>
      ```
   2. Option 2: Apply a special annotation `policy.open-cluster-management.io/trigger-update` to the policy with a different value every time when you update the `ConfigMap`. For example:

      ```
      $ oc annotate policy <policy_name> -n <policy_namespace> policy.open-cluster-management.io/trigger-update="1"
      ```

      Note

      You must apply the updated policy for the changes to take effect. For more information, see [Special annotation for reprocessing](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.6/html-single/governance/index#special-annotation-processing).
3. Optional: If it exists, delete the `ClusterGroupUpdate` CR that contains the policy. For example:

   ```
   $ oc delete clustergroupupgrade <cgu_name> -n <cgu_namespace>
   ```

   1. Create a new `ClusterGroupUpdate` CR that includes the policy to apply with the updated `ConfigMap` changes. For example, add the following YAML to the file `cgr-example.yaml`:

      ```
      apiVersion: ran.openshift.io/v1alpha1
      kind: ClusterGroupUpgrade
      metadata:
        name: <cgr_name>
        namespace: <policy_namespace>
      spec:
        managedPolicies:
          - <managed_policy>
        enable: true
        clusters:
        - <managed_cluster_1>
        - <managed_cluster_2>
        remediationStrategy:
          maxConcurrency: 2
          timeout: 240
      ```
   2. Apply the updated policy:

      ```
      $ oc apply -f cgr-example.yaml
      ```

## [Chapter 13. Updating managed clusters with the Topology Aware Lifecycle Manager](#cnf-talm-for-cluster-updates) Copy linkLink copied to clipboard!

You can use the Topology Aware Lifecycle Manager (TALM) to manage the software lifecycle of multiple clusters. TALM uses Red Hat Advanced Cluster Management (RHACM) policies to perform changes on the target clusters.

Using RHACM and `PolicyGenerator` CRs is the recommended approach for managing policies and deploying them to managed clusters. This replaces the use of `PolicyGenTemplate` CRs for this purpose. For more information about `PolicyGenerator` resources, see the RHACM [Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/governance/policy-deployment#integrate-policy-generator) documentation.

### [13.1. About the Topology Aware Lifecycle Manager configuration](#cnf-about-topology-aware-lifecycle-manager-config_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

The Topology Aware Lifecycle Manager (TALM) manages the deployment of Red Hat Advanced Cluster Management (RHACM) policies for one or more OpenShift Container Platform clusters. Using TALM in a large network of clusters allows the phased rollout of policies to the clusters in limited batches. This helps to minimize possible service disruptions when updating. With TALM, you can control the following actions:

* The timing of the update
* The number of RHACM-managed clusters
* The subset of managed clusters to apply the policies to
* The update order of the clusters
* The set of policies remediated to the cluster
* The order of policies remediated to the cluster
* The assignment of a canary cluster

For single-node OpenShift, the Topology Aware Lifecycle Manager (TALM) offers pre-caching images for clusters with limited bandwidth.

TALM supports the orchestration of the OpenShift Container Platform y-stream and z-stream updates, and day-two operations on y-streams and z-streams.

### [13.2. About managed policies used with Topology Aware Lifecycle Manager](#cnf-about-topology-aware-lifecycle-manager-about-policies_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

The Topology Aware Lifecycle Manager (TALM) uses RHACM policies for cluster updates.

TALM can be used to manage the rollout of any policy CR where the `remediationAction` field is set to `inform`. Supported use cases include the following:

* Manual user creation of policy CRs
* Automatically generated policies from the `PolicyGenerator` or `PolicyGentemplate` custom resource definition (CRD)

Note

Using the `PolicyGentemplate` CRD is the recommended method for automatic policy generation.

For policies that update an Operator subscription with manual approval, TALM provides additional functionality that approves the installation of the updated Operator.

For more information about managed policies, see [Policy Overview](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#policy-overview) in the RHACM documentation.

### [13.3. Installing the Topology Aware Lifecycle Manager by using the web console](#installing-topology-aware-lifecycle-manager-using-web-console_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

You can use the OpenShift Container Platform web console to install the Topology Aware Lifecycle Manager.

**Prerequisites**

* Install the latest version of the RHACM Operator.
* TALM requires RHACM 2.9 or later.
* Set up a hub cluster with a disconnected registry.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. In the OpenShift Container Platform web console, navigate to **Ecosystem** → **Software Catalog**.
2. Search for the **Topology Aware Lifecycle Manager** from the list of available Operators, and then click **Install**.
3. Keep the default selection of **Installation mode** ["All namespaces on the cluster (default)"] and **Installed Namespace** ("openshift-operators") to ensure that the Operator is installed properly.
4. Click **Install**.

**Verification**

To confirm that the installation is successful:

1. Navigate to the **Ecosystem** → **Installed Operators** page.
2. Check that the Operator is installed in the `All Namespaces` namespace and its status is `Succeeded`.

If the Operator is not installed successfully:

1. Navigate to the **Ecosystem** → **Installed Operators** page and inspect the `Status` column for any errors or failures.
2. Navigate to the **Workloads** → **Pods** page and check the logs in any containers in the `cluster-group-upgrades-controller-manager` pod that are reporting issues.

### [13.4. Installing the Topology Aware Lifecycle Manager by using the CLI](#installing-topology-aware-lifecycle-manager-using-cli_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to install the Topology Aware Lifecycle Manager (TALM).

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Install the latest version of the RHACM Operator.
* TALM requires RHACM 2.9 or later.
* Set up a hub cluster with disconnected registry.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a `Subscription` CR:

   1. Define the `Subscription` CR and save the YAML file, for example, `talm-subscription.yaml`:

      ```
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: openshift-topology-aware-lifecycle-manager-subscription
        namespace: openshift-operators
      spec:
        channel: "stable"
        name: topology-aware-lifecycle-manager
        source: redhat-operators
        sourceNamespace: openshift-marketplace
      ```
   2. Create the `Subscription` CR by running the following command:

      ```
      $ oc create -f talm-subscription.yaml
      ```

**Verification**

1. Verify that the installation succeeded by inspecting the CSV resource:

   ```
   $ oc get csv -n openshift-operators
   ```

   **Example output**

   ```
   NAME                                                   DISPLAY                            VERSION               REPLACES                           PHASE
   topology-aware-lifecycle-manager.4.22.x   Topology Aware Lifecycle Manager   4.22.x                                      Succeeded
   ```
2. Verify that the TALM is up and running:

   ```
   $ oc get deploy -n openshift-operators
   ```

   **Example output**

   ```
   NAMESPACE                                          NAME                                             READY   UP-TO-DATE   AVAILABLE   AGE
   openshift-operators                                cluster-group-upgrades-controller-manager        1/1     1            1           14s
   ```

### [13.5. About the ClusterGroupUpgrade CR](#talo-about-cgu-crs_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

The Topology Aware Lifecycle Manager (TALM) builds the remediation plan from the `ClusterGroupUpgrade` CR for a group of clusters. You can define the following specifications in a `ClusterGroupUpgrade` CR:

* Clusters in the group
* Blocking `ClusterGroupUpgrade` CRs
* Applicable list of managed policies
* Number of concurrent updates
* Applicable canary updates
* Actions to perform before and after the update
* Update timing

You can control the start time of an update using the `enable` field in the `ClusterGroupUpgrade` CR. For example, if you have a scheduled maintenance window of four hours, you can prepare a `ClusterGroupUpgrade` CR with the `enable` field set to `false`.

You can set the timeout by configuring the `spec.remediationStrategy.timeout` setting as follows:

```
spec
  remediationStrategy:
          maxConcurrency: 1
          timeout: 240
```

You can use the `batchTimeoutAction` to determine what happens if an update fails for a cluster. You can specify `continue` to skip the failing cluster and continue to upgrade other clusters, or `abort` to stop policy remediation for all clusters. Once the timeout elapses, TALM removes all `enforce` policies to ensure that no further updates are made to clusters.

To apply the changes, you set the `enabled` field to `true`.

For more information see the "Applying update policies to managed clusters" section.

As TALM works through remediation of the policies to the specified clusters, the `ClusterGroupUpgrade` CR can report true or false statuses for a number of conditions.

Note

After TALM completes a cluster update, the cluster does not update again under the control of the same `ClusterGroupUpgrade` CR. You must create a new `ClusterGroupUpgrade` CR in the following cases:

* When you need to update the cluster again
* When the cluster changes to non-compliant with the `inform` policy after being updated

#### [13.5.1. Selecting clusters](#selecting_clusters_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

TALM builds a remediation plan and selects clusters based on the following fields:

* The `clusterLabelSelector` field specifies the labels of the clusters that you want to update. This consists of a list of the standard label selectors from `k8s.io/apimachinery/pkg/apis/meta/v1`. Each selector in the list uses either label value pairs or label expressions. Matches from each selector are added to the final list of clusters along with the matches from the `clusterSelector` field and the `cluster` field.
* The `clusters` field specifies a list of clusters to update.
* The `canaries` field specifies the clusters for canary updates.
* The `maxConcurrency` field specifies the number of clusters to update in a batch.
* The `actions` field specifies `beforeEnable` actions that TALM takes as it begins the update process, and `afterCompletion` actions that TALM takes as it completes policy remediation for each cluster.

You can use the `clusters`, `clusterLabelSelector`, and `clusterSelector` fields together to create a combined list of clusters.

The remediation plan starts with the clusters listed in the `canaries` field. Each canary cluster forms a single-cluster batch.

**Sample `ClusterGroupUpgrade` CR with the enabled `field` set to `false`**

```
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  creationTimestamp: '2022-11-18T16:27:15Z'
  finalizers:
    - ran.openshift.io/cleanup-finalizer
  generation: 1
  name: talm-cgu
  namespace: talm-namespace
  resourceVersion: '40451823'
  uid: cca245a5-4bca-45fa-89c0-aa6af81a596c
Spec:
  actions:
    afterCompletion:
      addClusterLabels:
        upgrade-done: ""
      deleteClusterLabels:
        upgrade-running: ""
      deleteObjects: true
    beforeEnable:
      addClusterLabels:
        upgrade-running: ""
  clusters:
    - spoke1
  enable: false
  managedPolicies:
    - talm-policy
  preCaching: false
  remediationStrategy:
    canaries:
        - spoke1
    maxConcurrency: 2
    timeout: 240
  clusterLabelSelectors:
    - matchExpressions:
      - key: label1
      operator: In
      values:
        - value1a
        - value1b
  batchTimeoutAction:
status:
    computedMaxConcurrency: 2
    conditions:
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: All selected clusters are valid
        reason: ClusterSelectionCompleted
        status: 'True'
        type: ClustersSelected
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: Completed validation
        reason: ValidationCompleted
        status: 'True'
        type: Validated
      - lastTransitionTime: '2022-11-18T16:37:16Z'
        message: Not enabled
        reason: NotEnabled
        status: 'False'
        type: Progressing
    managedPoliciesForUpgrade:
      - name: talm-policy
        namespace: talm-namespace
    managedPoliciesNs:
      talm-policy: talm-namespace
    remediationPlan:
      - - spoke1
      - - spoke2
        - spoke3
    status:
```

* `Spec.actions.afterCompletion` specifies the action that TALM takes when it completes policy remediation for each cluster.
* `Spec.actions.beforeEnable` specifies the action that TALM takes as it begins the update process.
* `Spec.clusters` defines the list of clusters to update.
* `Spec.enable` the `enable` field is set to `false`.
* `Spec.managedPolicies` lists the user-defined set of policies to remediate.
* `Spec.remediationStrategy` defines the specifics of the cluster updates.
* `Spec.preCaching.canaries` defines the clusters for canary updates.
* `Spec.preCaching.maxConcurrency` defines the maximum number of concurrent updates in a batch. The number of remediation batches is the number of canary clusters, plus the number of clusters, except the canary clusters, divided by the `maxConcurrency` value. The clusters that are already compliant with all the managed policies are excluded from the remediation plan.
* `Spec.clusterLabelSelectors` displays the parameters for selecting clusters.
* `Spec.batchTimeoutAction` controls what happens if a batch times out. Possible values are `abort` or `continue`. If unspecified, the default is `continue`.
* `status` displays information about the status of the updates.
* `Spec.preCaching.conditions.type` the `ClustersSelected` condition shows that all selected clusters are valid.
* `Spec.preCaching.conditions.type` the `Validated` condition shows that all selected clusters have been validated.

Note

Any failures during the update of a canary cluster stops the update process.

When the remediation plan is successfully created, you can you set the `enable` field to `true` and TALM starts to update the non-compliant clusters with the specified managed policies.

Note

You can only make changes to the `spec` fields if the `enable` field of the `ClusterGroupUpgrade` CR is set to `false`.

#### [13.5.2. Validating](#validating_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

TALM checks that all specified managed policies are available and correct, and uses the `Validated` condition to report the status and reasons as follows:

* `true`

  Validation is completed.
* `false`

  Policies are missing or invalid, or an invalid platform image has been specified.

#### [13.5.3. Pre-caching](#precaching_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

Clusters might have limited bandwidth to access the container image registry, which can cause a timeout before the updates are completed. On single-node OpenShift clusters, you can use pre-caching to avoid this. The container image pre-caching starts when you create a `ClusterGroupUpgrade` CR with the `preCaching` field set to `true`. TALM compares the available disk space with the estimated OpenShift Container Platform image size to ensure that there is enough space. If a cluster has insufficient space, TALM cancels pre-caching for that cluster and does not remediate policies on it.

TALM uses the `PrecacheSpecValid` condition to report status information as follows:

* `true`

  The pre-caching spec is valid and consistent.
* `false`

  The pre-caching spec is incomplete.

TALM uses the `PrecachingSucceeded` condition to report status information as follows:

* `true`

  TALM has concluded the pre-caching process. If pre-caching fails for any cluster, the update fails for that cluster but proceeds for all other clusters. A message informs you if pre-caching has failed for any clusters.
* `false`

  Pre-caching is still in progress for one or more clusters or has failed for all clusters.

For more information see the "Using the container image pre-cache feature" section.

#### [13.5.4. Updating clusters](#updating_clusters_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

TALM enforces the policies following the remediation plan. Enforcing the policies for subsequent batches starts immediately after all the clusters of the current batch are compliant with all the managed policies. If the batch times out, TALM moves on to the next batch. The timeout value of a batch is the `spec.timeout` field divided by the number of batches in the remediation plan.

TALM uses the `Progressing` condition to report the status and reasons as follows:

* `true`

  TALM is remediating non-compliant policies.
* `false`

  The update is not in progress. Possible reasons for this are:

  + All clusters are compliant with all the managed policies.
  + The update timed out as policy remediation took too long.
  + Blocking CRs are missing from the system or have not yet completed.
  + The `ClusterGroupUpgrade` CR is not enabled.

Note

The managed policies apply in the order that they are listed in the `managedPolicies` field in the `ClusterGroupUpgrade` CR. One managed policy is applied to the specified clusters at a time. When a cluster complies with the current policy, the next managed policy is applied to it.

**Sample `ClusterGroupUpgrade` CR in the `Progressing` state**

```
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  creationTimestamp: '2022-11-18T16:27:15Z'
  finalizers:
    - ran.openshift.io/cleanup-finalizer
  generation: 1
  name: talm-cgu
  namespace: talm-namespace
  resourceVersion: '40451823'
  uid: cca245a5-4bca-45fa-89c0-aa6af81a596c
Spec:
  actions:
    afterCompletion:
      deleteObjects: true
    beforeEnable: {}
  clusters:
    - spoke1
  enable: true
  managedPolicies:
    - talm-policy
  preCaching: true
  remediationStrategy:
    canaries:
        - spoke1
    maxConcurrency: 2
    timeout: 240
  clusterLabelSelectors:
    - matchExpressions:
      - key: label1
      operator: In
      values:
        - value1a
        - value1b
  batchTimeoutAction:
status:
    clusters:
      - name: spoke1
        state: complete
    computedMaxConcurrency: 2
    conditions:
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: All selected clusters are valid
        reason: ClusterSelectionCompleted
        status: 'True'
        type: ClustersSelected
      - lastTransitionTime: '2022-11-18T16:27:15Z'
        message: Completed validation
        reason: ValidationCompleted
        status: 'True'
        type: Validated
      - lastTransitionTime: '2022-11-18T16:37:16Z'
        message: Remediating non-compliant policies
        reason: InProgress
        status: 'True'
        type: Progressing
    managedPoliciesForUpgrade:
      - name: talm-policy
        namespace: talm-namespace
    managedPoliciesNs:
      talm-policy: talm-namespace
    remediationPlan:
      - - spoke1
      - - spoke2
        - spoke3
    status:
      currentBatch: 2
      currentBatchRemediationProgress:
        spoke2:
          state: Completed
        spoke3:
          policyIndex: 0
          state: InProgress
      currentBatchStartedAt: '2022-11-18T16:27:16Z'
      startedAt: '2022-11-18T16:27:15Z'
```

The `Progressing` fields show that TALM is in the process of remediating policies.

#### [13.5.5. Update status](#update_status_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

TALM uses the `Succeeded` condition to report the status and reasons as follows:

* `true`

  All clusters are compliant with the specified managed policies.
* `false`

  Policy remediation failed as there were no clusters available for remediation, or because policy remediation took too long for one of the following reasons:

  + The current batch contains canary updates and the cluster in the batch does not comply with all the managed policies within the batch timeout.
  + Clusters did not comply with the managed policies within the `timeout` value specified in the `remediationStrategy` field.

**Sample `ClusterGroupUpgrade` CR in the `Succeeded` state**

```
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: cgu-upgrade-complete
      namespace: default
    spec:
      clusters:
      - spoke1
      - spoke4
      enable: true
      managedPolicies:
      - policy1-common-cluster-version-policy
      - policy2-common-pao-sub-policy
      remediationStrategy:
        maxConcurrency: 1
        timeout: 240
    status:
      clusters:
        - name: spoke1
          state: complete
        - name: spoke4
          state: complete
      conditions:
      - message: All selected clusters are valid
        reason: ClusterSelectionCompleted
        status: "True"
        type: ClustersSelected
      - message: Completed validation
        reason: ValidationCompleted
        status: "True"
        type: Validated
      - message: All clusters are compliant with all the managed policies
        reason: Completed
        status: "False"
        type: Progressing
      - message: All clusters are compliant with all the managed policies
        reason: Completed
        status: "True"
        type: Succeeded
      managedPoliciesForUpgrade:
      - name: policy1-common-cluster-version-policy
        namespace: default
      - name: policy2-common-pao-sub-policy
        namespace: default
      remediationPlan:
      - - spoke1
      - - spoke4
      status:
        completedAt: '2022-11-18T16:27:16Z'
        startedAt: '2022-11-18T16:27:15Z'
```

* `spec.conditions.type` in the `Progressing` fields, the status is `false` as the update has completed; clusters are compliant with all the managed policies.
* `spec.conditions.type` the `Succeeded` fields show that the validations completed successfully.
* `status` the `status` field includes a list of clusters and their respective statuses. The status of a cluster can be `complete` or `timedout`.

**Sample `ClusterGroupUpgrade` CR in the `timedout` state**

```
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  creationTimestamp: '2022-11-18T16:27:15Z'
  finalizers:
    - ran.openshift.io/cleanup-finalizer
  generation: 1
  name: talm-cgu
  namespace: talm-namespace
  resourceVersion: '40451823'
  uid: cca245a5-4bca-45fa-89c0-aa6af81a596c
spec:
  actions:
    afterCompletion:
      deleteObjects: true
    beforeEnable: {}
  clusters:
    - spoke1
    - spoke2
  enable: true
  managedPolicies:
    - talm-policy
  preCaching: false
  remediationStrategy:
    maxConcurrency: 2
    timeout: 240
status:
  clusters:
    - name: spoke1
      state: complete
    - currentPolicy:
        name: talm-policy
        status: NonCompliant
      name: spoke2
      state: timedout
  computedMaxConcurrency: 2
  conditions:
    - lastTransitionTime: '2022-11-18T16:27:15Z'
      message: All selected clusters are valid
      reason: ClusterSelectionCompleted
      status: 'True'
      type: ClustersSelected
    - lastTransitionTime: '2022-11-18T16:27:15Z'
      message: Completed validation
      reason: ValidationCompleted
      status: 'True'
      type: Validated
    - lastTransitionTime: '2022-11-18T16:37:16Z'
      message: Policy remediation took too long
      reason: TimedOut
      status: 'False'
      type: Progressing
    - lastTransitionTime: '2022-11-18T16:37:16Z'
      message: Policy remediation took too long
      reason: TimedOut
      status: 'False'
      type: Succeeded
  managedPoliciesForUpgrade:
    - name: talm-policy
      namespace: talm-namespace
  managedPoliciesNs:
    talm-policy: talm-namespace
  remediationPlan:
    - - spoke1
      - spoke2
  status:
        startedAt: '2022-11-18T16:27:15Z'
        completedAt: '2022-11-18T20:27:15Z'
```

* `status.clusters.currentPolicy` if a cluster’s state is `timedout`, the `currentPolicy` field shows the name of the policy and the policy status.
* `status.conditions.type` the status for `succeeded` is `false` and the message indicates that policy remediation took too long.

#### [13.5.6. Blocking ClusterGroupUpgrade CRs](#cnf-about-topology-aware-lifecycle-manager-blocking-crs_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

You can create multiple `ClusterGroupUpgrade` CRs and control their order of application.

For example, if you create `ClusterGroupUpgrade` CR C that blocks the start of `ClusterGroupUpgrade` CR A, then `ClusterGroupUpgrade` CR A cannot start until the status of `ClusterGroupUpgrade` CR C becomes `UpgradeComplete`.

One `ClusterGroupUpgrade` CR can have multiple blocking CRs. In this case, all the blocking CRs must complete before the upgrade for the current CR can start.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Provision one or more managed clusters.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Save the content of the `ClusterGroupUpgrade` CRs in the `cgu-a.yaml`, `cgu-b.yaml`, and `cgu-c.yaml` files.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-a
     namespace: default
   spec:
     blockingCRs:
     - name: cgu-c
       namespace: default
     clusters:
     - spoke1
     - spoke2
     - spoke3
     enable: false
     managedPolicies:
     - policy1-common-cluster-version-policy
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     remediationStrategy:
       canaries:
       - spoke1
       maxConcurrency: 2
       timeout: 240
   status:
     conditions:
     - message: The ClusterGroupUpgrade CR is not enabled
       reason: UpgradeNotStarted
       status: "False"
       type: Ready
     managedPoliciesForUpgrade:
     - name: policy1-common-cluster-version-policy
       namespace: default
     - name: policy2-common-pao-sub-policy
       namespace: default
     - name: policy3-common-ptp-sub-policy
       namespace: default
     placementBindings:
     - cgu-a-policy1-common-cluster-version-policy
     - cgu-a-policy2-common-pao-sub-policy
     - cgu-a-policy3-common-ptp-sub-policy
     placementRules:
     - cgu-a-policy1-common-cluster-version-policy
     - cgu-a-policy2-common-pao-sub-policy
     - cgu-a-policy3-common-ptp-sub-policy
     remediationPlan:
     - - spoke1
     - - spoke2
   ```

   * `spec.blockingCRs.name` defines the blocking CRs. The `cgu-a` update cannot start until `cgu-c` is complete.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-b
     namespace: default
   spec:
     blockingCRs:
     - name: cgu-a
       namespace: default
     clusters:
     - spoke4
     - spoke5
     enable: false
     managedPolicies:
     - policy1-common-cluster-version-policy
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     - policy4-common-sriov-sub-policy
     remediationStrategy:
       maxConcurrency: 1
       timeout: 240
   status:
     conditions:
     - message: The ClusterGroupUpgrade CR is not enabled
       reason: UpgradeNotStarted
       status: "False"
       type: Ready
     managedPoliciesForUpgrade:
     - name: policy1-common-cluster-version-policy
       namespace: default
     - name: policy2-common-pao-sub-policy
       namespace: default
     - name: policy3-common-ptp-sub-policy
       namespace: default
     - name: policy4-common-sriov-sub-policy
       namespace: default
     placementBindings:
     - cgu-b-policy1-common-cluster-version-policy
     - cgu-b-policy2-common-pao-sub-policy
     - cgu-b-policy3-common-ptp-sub-policy
     - cgu-b-policy4-common-sriov-sub-policy
     placementRules:
     - cgu-b-policy1-common-cluster-version-policy
     - cgu-b-policy2-common-pao-sub-policy
     - cgu-b-policy3-common-ptp-sub-policy
     - cgu-b-policy4-common-sriov-sub-policy
     remediationPlan:
     - - spoke4
     - - spoke5
     status: {}
   ```

   The `cgu-b` update cannot start until `cgu-a` is complete.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-c
     namespace: default
   spec:
     clusters:
     - spoke6
     enable: false
     managedPolicies:
     - policy1-common-cluster-version-policy
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     - policy4-common-sriov-sub-policy
     remediationStrategy:
       maxConcurrency: 1
       timeout: 240
   status:
     conditions:
     - message: The ClusterGroupUpgrade CR is not enabled
       reason: UpgradeNotStarted
       status: "False"
       type: Ready
     managedPoliciesCompliantBeforeUpgrade:
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     managedPoliciesForUpgrade:
     - name: policy1-common-cluster-version-policy
       namespace: default
     - name: policy4-common-sriov-sub-policy
       namespace: default
     placementBindings:
     - cgu-c-policy1-common-cluster-version-policy
     - cgu-c-policy4-common-sriov-sub-policy
     placementRules:
     - cgu-c-policy1-common-cluster-version-policy
     - cgu-c-policy4-common-sriov-sub-policy
     remediationPlan:
     - - spoke6
     status: {}
   ```

   The `cgu-c` update does not have any blocking CRs. TALM starts the `cgu-c` update when the `enable` field is set to `true`.
2. Create the `ClusterGroupUpgrade` CRs by running the following command for each relevant CR:

   ```
   $ oc apply -f <name>.yaml
   ```
3. Start the update process by running the following command for each relevant CR:

   ```
   $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/<name> \
   --type merge -p '{"spec":{"enable":true}}'
   ```

   The following examples show `ClusterGroupUpgrade` CRs where the `enable` field is set to `true`:

   Example for `cgu-a` with blocking CRs:

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-a
     namespace: default
   spec:
     blockingCRs:
     - name: cgu-c
       namespace: default
     clusters:
     - spoke1
     - spoke2
     - spoke3
     enable: true
     managedPolicies:
     - policy1-common-cluster-version-policy
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     remediationStrategy:
       canaries:
       - spoke1
       maxConcurrency: 2
       timeout: 240
   status:
     conditions:
     - message: 'The ClusterGroupUpgrade CR is blocked by other CRs that have not yet
         completed: [cgu-c]'
       reason: UpgradeCannotStart
       status: "False"
       type: Ready
     managedPoliciesForUpgrade:
     - name: policy1-common-cluster-version-policy
       namespace: default
     - name: policy2-common-pao-sub-policy
       namespace: default
     - name: policy3-common-ptp-sub-policy
       namespace: default
     placementBindings:
     - cgu-a-policy1-common-cluster-version-policy
     - cgu-a-policy2-common-pao-sub-policy
     - cgu-a-policy3-common-ptp-sub-policy
     placementRules:
     - cgu-a-policy1-common-cluster-version-policy
     - cgu-a-policy2-common-pao-sub-policy
     - cgu-a-policy3-common-ptp-sub-policy
     remediationPlan:
     - - spoke1
     - - spoke2
     status: {}
   ```

   Shows the list of blocking CRs.

   Example for `cgu-b` with blocking CRs:

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-b
     namespace: default
   spec:
     blockingCRs:
     - name: cgu-a
       namespace: default
     clusters:
     - spoke4
     - spoke5
     enable: true
     managedPolicies:
     - policy1-common-cluster-version-policy
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     - policy4-common-sriov-sub-policy
     remediationStrategy:
       maxConcurrency: 1
       timeout: 240
   status:
     conditions:
     - message: 'The ClusterGroupUpgrade CR is blocked by other CRs that have not yet
         completed: [cgu-a]'
       reason: UpgradeCannotStart
       status: "False"
       type: Ready
     managedPoliciesForUpgrade:
     - name: policy1-common-cluster-version-policy
       namespace: default
     - name: policy2-common-pao-sub-policy
       namespace: default
     - name: policy3-common-ptp-sub-policy
       namespace: default
     - name: policy4-common-sriov-sub-policy
       namespace: default
     placementBindings:
     - cgu-b-policy1-common-cluster-version-policy
     - cgu-b-policy2-common-pao-sub-policy
     - cgu-b-policy3-common-ptp-sub-policy
     - cgu-b-policy4-common-sriov-sub-policy
     placementRules:
     - cgu-b-policy1-common-cluster-version-policy
     - cgu-b-policy2-common-pao-sub-policy
     - cgu-b-policy3-common-ptp-sub-policy
     - cgu-b-policy4-common-sriov-sub-policy
     remediationPlan:
     - - spoke4
     - - spoke5
     status: {}
   ```

   Shows the list of blocking CRs.

   Example for `cgu-c` with blocking CRs:

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-c
     namespace: default
   spec:
     clusters:
     - spoke6
     enable: true
     managedPolicies:
     - policy1-common-cluster-version-policy
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     - policy4-common-sriov-sub-policy
     remediationStrategy:
       maxConcurrency: 1
       timeout: 240
   status:
     conditions:
     - message: The ClusterGroupUpgrade CR has upgrade policies that are still non compliant
       reason: UpgradeNotCompleted
       status: "False"
       type: Ready
     managedPoliciesCompliantBeforeUpgrade:
     - policy2-common-pao-sub-policy
     - policy3-common-ptp-sub-policy
     managedPoliciesForUpgrade:
     - name: policy1-common-cluster-version-policy
       namespace: default
     - name: policy4-common-sriov-sub-policy
       namespace: default
     placementBindings:
     - cgu-c-policy1-common-cluster-version-policy
     - cgu-c-policy4-common-sriov-sub-policy
     placementRules:
     - cgu-c-policy1-common-cluster-version-policy
     - cgu-c-policy4-common-sriov-sub-policy
     remediationPlan:
     - - spoke6
     status:
       currentBatch: 1
       remediationPlanForBatch:
         spoke6: 0
   ```

   The `cgu-c` update does not have any blocking CRs.

### [13.6. Update policies on managed clusters](#talo-policies-concept_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

The Topology Aware Lifecycle Manager (TALM) remediates a set of `inform` policies for the clusters specified in the `ClusterGroupUpgrade` custom resource (CR). TALM remediates `inform` policies by controlling the `remediationAction` specification in a `Policy` CR through the `bindingOverrides.remediationAction` and `subFilter` specifications in the `PlacementBinding` CR. Each policy has its own corresponding RHACM placement rule and RHACM placement binding.

One by one, TALM adds each cluster from the current batch to the placement rule that corresponds with the applicable managed policy. If a cluster is already compliant with a policy, TALM skips applying that policy on the compliant cluster. TALM then moves on to applying the next policy to the non-compliant cluster. After TALM completes the updates in a batch, all clusters are removed from the placement rules associated with the policies. Then, the update of the next batch starts.

If a spoke cluster does not report any compliant state to RHACM, the managed policies on the hub cluster can be missing status information that TALM needs. TALM handles these cases in the following ways:

* If a policy’s `status.compliant` field is missing, TALM ignores the policy and adds a log entry. Then, TALM continues looking at the policy’s `status.status` field.
* If a policy’s `status.status` is missing, TALM produces an error.
* If a cluster’s compliance status is missing in the policy’s `status.status` field, TALM considers that cluster to be non-compliant with that policy.

The `ClusterGroupUpgrade` CR’s `batchTimeoutAction` determines what happens if an upgrade fails for a cluster. You can specify `continue` to skip the failing cluster and continue to upgrade other clusters, or specify `abort` to stop the policy remediation for all clusters. Once the timeout elapses, TALM removes all the resources it created to ensure that no further updates are made to clusters.

**Example upgrade policy**

```
apiVersion: policy.open-cluster-management.io/v1
kind: Policy
metadata:
  name: ocp-4.4.22.4
  namespace: platform-upgrade
spec:
  disabled: false
  policy-templates:
  - objectDefinition:
      apiVersion: policy.open-cluster-management.io/v1
      kind: ConfigurationPolicy
      metadata:
        name: upgrade
      spec:
        namespaceselector:
          exclude:
          - kube-*
          include:
          - '*'
        object-templates:
        - complianceType: musthave
          objectDefinition:
            apiVersion: config.openshift.io/v1
            kind: ClusterVersion
            metadata:
              name: version
            spec:
              channel: stable-4.22
              desiredUpdate:
                version: 4.4.22.4
              upstream: https://api.openshift.com/api/upgrades_info/v1/graph
            status:
              history:
                - state: Completed
                  version: 4.4.22.4
        remediationAction: inform
        severity: low
  remediationAction: inform
```

For more information about RHACM policies, see [Policy overview](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/governance/index#policy-overview).

#### [13.6.1. Configuring Operator subscriptions for managed clusters that you install with TALM](#talo-about-subscription-crs_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

Topology Aware Lifecycle Manager (TALM) can only approve the install plan for an Operator if the `Subscription` custom resource (CR) of the Operator contains the `status.state.AtLatestKnown` field.

**Procedure**

1. Add the `status.state.AtLatestKnown` field to the `Subscription` CR of the Operator:

   **Example Subscription CR**

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: cluster-logging
     namespace: openshift-logging
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
   spec:
     channel: "stable-6.2"
     name: cluster-logging
     source: redhat-operators-disconnected
     sourceNamespace: openshift-marketplace
     installPlanApproval: Manual
   status:
     state: AtLatestKnown
   ```

   The `status.state: AtLatestKnown` field is used for the latest Operator version available from the Operator catalog.

   Note

   When a new version of the Operator is available in the registry, the associated policy becomes non-compliant.
2. Apply the changed `Subscription` policy to your managed clusters with a `ClusterGroupUpgrade` CR.

#### [13.6.2. Applying update policies to managed clusters](#talo-apply-policies_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

You can update your managed clusters by applying your policies.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* TALM requires RHACM 2.9 or later.
* Provision one or more managed clusters.
* Log in as a user with `cluster-admin` privileges.
* Create RHACM policies in the hub cluster.

**Procedure**

1. Save the contents of the `ClusterGroupUpgrade` CR in the `cgu-1.yaml` file.

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: cgu-1
     namespace: default
   spec:
     managedPolicies:
       - policy1-common-cluster-version-policy
       - policy2-common-nto-sub-policy
       - policy3-common-ptp-sub-policy
       - policy4-common-sriov-sub-policy
     enable: false
     clusters:
     - spoke1
     - spoke2
     - spoke5
     - spoke6
     remediationStrategy:
       maxConcurrency: 2
       timeout: 240
     batchTimeoutAction:
   ```

   * `spec.managedPolicies` the name of the policies to apply.
   * `spec.clusters` the list of clusters to update.
   * `spec.remediationStrategy.maxConcurrency` the `maxConcurrency` field signifies the number of clusters updated at the same time.
   * `spec.remediationStrategy.timeout` the update timeout in minutes.
   * `spec.batchTimeoutAction` controls what happens if a batch times out. Possible values are `abort` or `continue`. If unspecified, the default is `continue`.
2. Create the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc create -f cgu-1.yaml
   ```

   1. Check if the `ClusterGroupUpgrade` CR was created in the hub cluster by running the following command:

      ```
      $ oc get cgu --all-namespaces
      ```

      **Example output**

      ```
      NAMESPACE   NAME  AGE  STATE      DETAILS
      default     cgu-1 8m55 NotEnabled Not Enabled
      ```
   2. Check the status of the update by running the following command:

      ```
      $ oc get cgu -n default cgu-1 -ojsonpath='{.status}' | jq
      ```

      **Example output**

      ```
      {
        "computedMaxConcurrency": 2,
        "conditions": [
          {
            "lastTransitionTime": "2022-02-25T15:34:07Z",
            "message": "Not enabled",
            "reason": "NotEnabled",
            "status": "False",
            "type": "Progressing"
          }
        ],
        "managedPoliciesContent": {
          "policy1-common-cluster-version-policy": "null",
          "policy2-common-nto-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"node-tuning-operator\",\"namespace\":\"openshift-cluster-node-tuning-operator\"}]",
          "policy3-common-ptp-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"ptp-operator-subscription\",\"namespace\":\"openshift-ptp\"}]",
          "policy4-common-sriov-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"sriov-network-operator-subscription\",\"namespace\":\"openshift-sriov-network-operator\"}]"
        },
        "managedPoliciesForUpgrade": [
          {
            "name": "policy1-common-cluster-version-policy",
            "namespace": "default"
          },
          {
            "name": "policy2-common-nto-sub-policy",
            "namespace": "default"
          },
          {
            "name": "policy3-common-ptp-sub-policy",
            "namespace": "default"
          },
          {
            "name": "policy4-common-sriov-sub-policy",
            "namespace": "default"
          }
        ],
        "managedPoliciesNs": {
          "policy1-common-cluster-version-policy": "default",
          "policy2-common-nto-sub-policy": "default",
          "policy3-common-ptp-sub-policy": "default",
          "policy4-common-sriov-sub-policy": "default"
        },
        "placementBindings": [
          "cgu-policy1-common-cluster-version-policy",
          "cgu-policy2-common-nto-sub-policy",
          "cgu-policy3-common-ptp-sub-policy",
          "cgu-policy4-common-sriov-sub-policy"
        ],
        "placementRules": [
          "cgu-policy1-common-cluster-version-policy",
          "cgu-policy2-common-nto-sub-policy",
          "cgu-policy3-common-ptp-sub-policy",
          "cgu-policy4-common-sriov-sub-policy"
        ],
        "remediationPlan": [
          [
            "spoke1",
            "spoke2"
          ],
          [
            "spoke5",
            "spoke6"
          ]
        ],
        "status": {}
      }
      ```

      The `spec.enable` field in the `ClusterGroupUpgrade` CR is set to `false`.
3. Change the value of the `spec.enable` field to `true` by running the following command:

   ```
   $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-1 \
   --patch '{"spec":{"enable":true}}' --type=merge
   ```

**Verification**

1. Check the status of the update by running the following command:

   ```
   $ oc get cgu -n default cgu-1 -ojsonpath='{.status}' | jq
   ```

   **Example output**

   ```
   {
     "computedMaxConcurrency": 2,
     "conditions": [
       {
         "lastTransitionTime": "2022-02-25T15:33:07Z",
         "message": "All selected clusters are valid",
         "reason": "ClusterSelectionCompleted",
         "status": "True",
         "type": "ClustersSelected"
       },
       {
         "lastTransitionTime": "2022-02-25T15:33:07Z",
         "message": "Completed validation",
         "reason": "ValidationCompleted",
         "status": "True",
         "type": "Validated"
       },
       {
         "lastTransitionTime": "2022-02-25T15:34:07Z",
         "message": "Remediating non-compliant policies",
         "reason": "InProgress",
         "status": "True",
         "type": "Progressing"
       }
     ],
     "managedPoliciesContent": {
       "policy1-common-cluster-version-policy": "null",
       "policy2-common-nto-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"node-tuning-operator\",\"namespace\":\"openshift-cluster-node-tuning-operator\"}]",
       "policy3-common-ptp-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"ptp-operator-subscription\",\"namespace\":\"openshift-ptp\"}]",
       "policy4-common-sriov-sub-policy": "[{\"kind\":\"Subscription\",\"name\":\"sriov-network-operator-subscription\",\"namespace\":\"openshift-sriov-network-operator\"}]"
     },
     "managedPoliciesForUpgrade": [
       {
         "name": "policy1-common-cluster-version-policy",
         "namespace": "default"
       },
       {
         "name": "policy2-common-nto-sub-policy",
         "namespace": "default"
       },
       {
         "name": "policy3-common-ptp-sub-policy",
         "namespace": "default"
       },
       {
         "name": "policy4-common-sriov-sub-policy",
         "namespace": "default"
       }
     ],
     "managedPoliciesNs": {
       "policy1-common-cluster-version-policy": "default",
       "policy2-common-nto-sub-policy": "default",
       "policy3-common-ptp-sub-policy": "default",
       "policy4-common-sriov-sub-policy": "default"
     },
     "placementBindings": [
       "cgu-policy1-common-cluster-version-policy",
       "cgu-policy2-common-nto-sub-policy",
       "cgu-policy3-common-ptp-sub-policy",
       "cgu-policy4-common-sriov-sub-policy"
     ],
     "placementRules": [
       "cgu-policy1-common-cluster-version-policy",
       "cgu-policy2-common-nto-sub-policy",
       "cgu-policy3-common-ptp-sub-policy",
       "cgu-policy4-common-sriov-sub-policy"
     ],
     "remediationPlan": [
       [
         "spoke1",
         "spoke2"
       ],
       [
         "spoke5",
         "spoke6"
       ]
     ],
     "status": {
       "currentBatch": 1,
       "currentBatchRemediationProgress": {
          "spoke1": {
             "policyIndex": 1,
             "state": "InProgress"
          },
          "spoke2": {
             "policyIndex": 1,
             "state": "InProgress"
          }
       },
       "currentBatchStartedAt": "2022-02-25T15:54:16Z",
       "startedAt": "2022-02-25T15:54:16Z"
     }
   }
   ```

   Reflects the update progress of the current batch. Run this command again to receive updated information about the progress.
2. Check the status of the policies by running the following command:

   ```
   oc get policies -A
   ```

   **Example output**

   ```
   NAMESPACE   NAME                                        REMEDIATION ACTION    COMPLIANCE STATE     AGE
   spoke1    default.policy1-common-cluster-version-policy enforce               Compliant            18m
   spoke1    default.policy2-common-nto-sub-policy         enforce               NonCompliant         18m
   spoke2    default.policy1-common-cluster-version-policy enforce               Compliant            18m
   spoke2    default.policy2-common-nto-sub-policy         enforce               NonCompliant         18m
   spoke5    default.policy3-common-ptp-sub-policy         inform                NonCompliant         18m
   spoke5    default.policy4-common-sriov-sub-policy       inform                NonCompliant         18m
   spoke6    default.policy3-common-ptp-sub-policy         inform                NonCompliant         18m
   spoke6    default.policy4-common-sriov-sub-policy       inform                NonCompliant         18m
   default   policy1-common-ptp-sub-policy                 inform                Compliant            18m
   default   policy2-common-sriov-sub-policy               inform                NonCompliant         18m
   default   policy3-common-ptp-sub-policy                 inform                NonCompliant         18m
   default   policy4-common-sriov-sub-policy               inform                NonCompliant         18m
   ```

   * The `spec.remediationAction` value changes to `enforce` for the child policies applied to the clusters from the current batch.
   * The `spec.remedationAction` value remains `inform` for the child policies in the rest of the clusters.
   * After the batch is complete, the `spec.remediationAction` value changes back to `inform` for the enforced child policies.
3. If the policies include Operator subscriptions, you can check the installation progress directly on the single-node cluster.

   1. Export the `KUBECONFIG` file of the single-node cluster you want to check the installation progress for by running the following command:

      ```
      $ export KUBECONFIG=<cluster_kubeconfig_absolute_path>
      ```
   2. Check all the subscriptions present on the single-node cluster and look for the one in the policy you are trying to install through the `ClusterGroupUpgrade` CR by running the following command:

      ```
      $ oc get subs -A | grep -i <subscription_name>
      ```

      **Example output for `cluster-logging` policy**

      ```
      NAMESPACE                              NAME                         PACKAGE                      SOURCE             CHANNEL
      openshift-logging                      cluster-logging              cluster-logging              redhat-operators   stable
      ```
4. If one of the managed policies includes a `ClusterVersion` CR, check the status of platform updates in the current batch by running the following command against the spoke cluster:

   ```
   $ oc get clusterversion
   ```

   **Example output**

   ```
   NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
   version   4.4.22.5     True        True          43s     Working towards 4.4.22.7: 71 of 735 done (9% complete)
   ```
5. Check the Operator subscription by running the following command:

   ```
   $ oc get subs -n <operator-namespace> <operator-subscription> -ojsonpath="{.status}"
   ```
6. Check the install plans present on the single-node cluster that is associated with the desired subscription by running the following command:

   ```
   $ oc get installplan -n <subscription_namespace>
   ```

   **Example output for `cluster-logging` Operator**

   ```
   NAMESPACE                              NAME            CSV                                 APPROVAL   APPROVED
   openshift-logging                      install-6khtw   cluster-logging.5.3.3-4             Manual     true
   ```

   The install plans have their `Approval` field set to `Manual` and their `Approved` field changes from `false` to `true` after TALM approves the install plan.

   Note

   When TALM is remediating a policy containing a subscription, it automatically approves any install plans attached to that subscription. Where multiple install plans are needed to get the operator to the latest known version, TALM might approve multiple install plans, upgrading through one or more intermediate versions to get to the final version.
7. Check if the cluster service version for the Operator of the policy that the `ClusterGroupUpgrade` is installing reached the `Succeeded` phase by running the following command:

   ```
   $ oc get csv -n <operator_namespace>
   ```

   **Example output for OpenShift Logging Operator**

   ```
   NAME                    DISPLAY                     VERSION   REPLACES   PHASE
   cluster-logging.v6.2.1  Red Hat OpenShift Logging   6.2.1                Succeeded
   ```

### [13.7. Using the container image pre-cache feature](#talo-precache-feature-concept_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

Single-node OpenShift clusters might have limited bandwidth to access the container image registry, which can cause a timeout before the updates are completed.

Note

The time of the update is not set by TALM. You can apply the `ClusterGroupUpgrade` CR at the beginning of the update by manual application or by external automation.

The container image pre-caching starts when the `preCaching` field is set to `true` in the `ClusterGroupUpgrade` CR.

TALM uses the `PrecacheSpecValid` condition to report status information as follows:

* `true`

  The pre-caching spec is valid and consistent.
* `false`

  The pre-caching spec is incomplete.

TALM uses the `PrecachingSucceeded` condition to report status information as follows:

* `true`

  TALM has concluded the pre-caching process. If pre-caching fails for any cluster, the update fails for that cluster but proceeds for all other clusters. A message informs you if pre-caching has failed for any clusters.
* `false`

  Pre-caching is still in progress for one or more clusters or has failed for all clusters.

After a successful pre-caching process, you can start remediating policies. The remediation actions start when the `enable` field is set to `true`. If there is a pre-caching failure on a cluster, the upgrade fails for that cluster. The upgrade process continues for all other clusters that have a successful pre-cache.

The pre-caching process can be in the following statuses:

* `NotStarted`

  This is the initial state all clusters are automatically assigned to on the first reconciliation pass of the `ClusterGroupUpgrade` CR. In this state, TALM deletes any pre-caching namespace and hub view resources of spoke clusters that remain from previous incomplete updates. TALM then creates a new `ManagedClusterView` resource for the spoke pre-caching namespace to verify its deletion in the `PrecachePreparing` state.
* `PreparingToStart`

  Cleaning up any remaining resources from previous incomplete updates is in progress.
* `Starting`

  Pre-caching job prerequisites and the job are created.
* `Active`

  The job is in "Active" state.
* `Succeeded`

  The pre-cache job succeeded.
* `PrecacheTimeout`

  The artifact pre-caching is partially done.
* `UnrecoverableError`

  The job ends with a non-zero exit code.

#### [13.7.1. Using the container image pre-cache filter](#talo-precache-feature-image-filter_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

The pre-cache feature typically downloads more images than a cluster needs for an update. You can control which pre-cache images are downloaded to a cluster. This decreases download time, and saves bandwidth and storage.

You can see a list of all images to be downloaded using the following command:

```
$ oc adm release info <ocp-version>
```

The following `ConfigMap` example shows how you can exclude images using the `excludePrecachePatterns` field.

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-group-upgrade-overrides
data:
  excludePrecachePatterns: |
    azure
    aws
    vsphere
    alibaba
```

TALM excludes all images with names that include any of the patterns listed here.

#### [13.7.2. Creating a ClusterGroupUpgrade CR with pre-caching](#talo-precache-start_and_update_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

For single-node OpenShift, the pre-cache feature allows the required container images to be present on the spoke cluster before the update starts.

Note

For pre-caching, TALM uses the `spec.remediationStrategy.timeout` value from the `ClusterGroupUpgrade` CR. You must set a `timeout` value that allows sufficient time for the pre-caching job to complete. When you enable the `ClusterGroupUpgrade` CR after pre-caching has completed, you can change the `timeout` value to a duration that is appropriate for the update.

**Prerequisites**

* Install the Topology Aware Lifecycle Manager (TALM).
* Provision one or more managed clusters.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Save the contents of the `ClusterGroupUpgrade` CR with the `preCaching` field set to `true` in the `clustergroupupgrades-group-du.yaml` file:

   ```
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: du-upgrade-4918
     namespace: ztp-group-du-sno
   spec:
     preCaching: true
     clusters:
     - cnfdb1
     - cnfdb2
     enable: false
     managedPolicies:
     - du-upgrade-platform-upgrade
     remediationStrategy:
       maxConcurrency: 2
       timeout: 240
   ```

   The `preCaching` field is set to `true`, which enables TALM to pull the container images before starting the update.
2. When you want to start pre-caching, apply the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc apply -f clustergroupupgrades-group-du.yaml
   ```

**Verification**

1. Check if the `ClusterGroupUpgrade` CR exists in the hub cluster by running the following command:

   ```
   $ oc get cgu -A
   ```

   Example output:

   ```
   NAMESPACE          NAME              AGE   STATE        DETAILS
   ztp-group-du-sno   du-upgrade-4918   10s   InProgress   Precaching is required and not done
   ```

   The CR is created.
2. Check the status of the pre-caching task by running the following command:

   ```
   $ oc get cgu -n ztp-group-du-sno du-upgrade-4918 -o jsonpath='{.status}'
   ```

   Example output:

   ```
   {
     "conditions": [
       {
         "lastTransitionTime": "2022-01-27T19:07:24Z",
         "message": "Precaching is required and not done",
         "reason": "InProgress",
         "status": "False",
         "type": "PrecachingSucceeded"
       },
       {
         "lastTransitionTime": "2022-01-27T19:07:34Z",
         "message": "Pre-caching spec is valid and consistent",
         "reason": "PrecacheSpecIsWellFormed",
         "status": "True",
         "type": "PrecacheSpecValid"
       }
     ],
     "precaching": {
       "clusters": [
         "cnfdb1"
         "cnfdb2"
       ],
       "spec": {
         "platformImage": "image.example.io"},
       "status": {
         "cnfdb1": "Active"
         "cnfdb2": "Succeeded"}
       }
   }
   ```

   The output lists the identified clusters. The `platformImage` value in `status.precaching.spec` is derived by TALM from the `ClusterVersion` object in the managed policies.
3. Check the status of the pre-caching job by running the following command on the spoke cluster:

   ```
   $ oc get jobs,pods -n openshift-talo-pre-cache
   ```

   Example output:

   ```
   NAME                  COMPLETIONS   DURATION   AGE
   job.batch/pre-cache   0/1           3m10s      3m10s

   NAME                     READY   STATUS    RESTARTS   AGE
   pod/pre-cache--1-9bmlr   1/1     Running   0          3m10s
   ```
4. Check the status of the `ClusterGroupUpgrade` CR by running the following command:

   ```
   $ oc get cgu -n ztp-group-du-sno du-upgrade-4918 -o jsonpath='{.status}'
   ```

   Example output:

   ```
   "conditions": [
       {
         "lastTransitionTime": "2022-01-27T19:30:41Z",
         "message": "The ClusterGroupUpgrade CR has all clusters compliant with all the managed policies",
         "reason": "UpgradeCompleted",
         "status": "True",
         "type": "Ready"
       },
       {
         "lastTransitionTime": "2022-01-27T19:28:57Z",
         "message": "Precaching is completed",
         "reason": "PrecachingCompleted",
         "status": "True",
         "type": "PrecachingSucceeded"
       }
   ```

The pre-cache tasks are done.

### [13.8. Troubleshooting the Topology Aware Lifecycle Manager](#talo-troubleshooting_cnf-topology-aware-lifecycle-manager) Copy linkLink copied to clipboard!

The Topology Aware Lifecycle Manager (TALM) is an OpenShift Container Platform Operator that remediates RHACM policies. When issues occur, use the `oc adm must-gather` command to gather details and logs and to take steps in debugging the issues.

For more information about related topics, see the following documentation:

* [Red Hat Advanced Cluster Management for Kubernetes 2.4 Support Matrix](https://access.redhat.com/articles/6218901)
* [Red Hat Advanced Cluster Management Troubleshooting](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.0/html/troubleshooting/troubleshooting)
* The "Troubleshooting Operator issues" section

**General troubleshooting**

You can determine the cause of the problem by reviewing the following questions:

* Is the configuration that you are applying supported?

  + Are the RHACM and the OpenShift Container Platform versions compatible?
  + Are the TALM and RHACM versions compatible?
* Which of the following components is causing the problem?

  + [Cannot modify the ClusterUpgradeGroup CR](#talo-troubleshooting-modify-cgu_cnf-topology-aware-lifecycle-manager)
  + [Managed policies](#talo-troubleshooting-managed-policies_cnf-topology-aware-lifecycle-manager)
  + [Clusters](#talo-troubleshooting-clusters_cnf-topology-aware-lifecycle-manager)
  + [Remediation Strategy](#talo-troubleshooting-remediation-strategy_cnf-topology-aware-lifecycle-manager)
  + [Topology Aware Lifecycle Manager](#talo-troubleshooting-remediation-talo_cnf-topology-aware-lifecycle-manager)

**Cannot modify the ClusterUpgradeGroup CR**

Issue
:   You cannot edit the `ClusterUpgradeGroup` CR after enabling the update.

Resolution
:   Restart the procedure by performing the following steps:

    1. Remove the old `ClusterGroupUpgrade` CR by running the following command:

       ```
       $ oc delete cgu -n <ClusterGroupUpgradeCR_namespace> <ClusterGroupUpgradeCR_name>
       ```
    2. Check and fix the existing issues with the managed clusters and policies.

       1. Ensure that all the clusters are managed clusters and available.
       2. Ensure that all the policies exist and have the `spec.remediationAction` field set to `inform`.
    3. Create a new `ClusterGroupUpgrade` CR with the correct configurations.

       ```
       $ oc apply -f <ClusterGroupUpgradeCR_YAML>
       ```

**Managed policies**

**Checking managed policies on the system**

Issue
:   You want to check if you have the correct managed policies on the system.

Resolution
:   Run the following command:

    ```
    $ oc get cgu lab-upgrade -ojsonpath='{.spec.managedPolicies}'
    ```

    Example output:

    ```
    ["group-du-sno-validator-du-validator-policy", "policy2-common-nto-sub-policy", "policy3-common-ptp-sub-policy"]
    ```

**Checking remediationAction mode**

Issue
:   You want to check if the `remediationAction` field is set to `inform` in the `spec` of the managed policies.

Resolution
:   Run the following command:

    ```
    $ oc get policies --all-namespaces
    ```

    Example output:

    ```
    NAMESPACE   NAME                                                 REMEDIATION ACTION   COMPLIANCE STATE   AGE
    default     policy1-common-cluster-version-policy                inform               NonCompliant       5d21h
    default     policy2-common-nto-sub-policy                        inform               Compliant          5d21h
    default     policy3-common-ptp-sub-policy                        inform               NonCompliant       5d21h
    default     policy4-common-sriov-sub-policy                      inform               NonCompliant       5d21h
    ```

**Checking policy compliance state**

Issue
:   You want to check the compliance state of policies.

Resolution
:   Run the following command:

    ```
    $ oc get policies --all-namespaces
    ```

    Example output:

    ```
    NAMESPACE   NAME                                                 REMEDIATION ACTION   COMPLIANCE STATE   AGE
    default     policy1-common-cluster-version-policy                inform               NonCompliant       5d21h
    default     policy2-common-nto-sub-policy                        inform               Compliant          5d21h
    default     policy3-common-ptp-sub-policy                        inform               NonCompliant       5d21h
    default     policy4-common-sriov-sub-policy                      inform               NonCompliant       5d21h
    ```

**Clusters**

**Checking if managed clusters are present**

Issue
:   You want to check if the clusters in the `ClusterGroupUpgrade` CR are managed clusters.

Resolution
:   Run the following command:

    ```
    $ oc get managedclusters
    ```

    Example output:

    ```
    NAME            HUB ACCEPTED   MANAGED CLUSTER URLS                    JOINED   AVAILABLE   AGE
    local-cluster   true           https://api.hub.example.com:6443        True     Unknown     13d
    spoke1          true           https://api.spoke1.example.com:6443     True     True        13d
    spoke3          true           https://api.spoke3.example.com:6443     True     True        27h
    ```

    1. Alternatively, check the TALM manager logs:

       1. Get the name of the TALM manager by running the following command:

          ```
          $ oc get pod -n openshift-operators
          ```

          Example output:

          ```
          NAME                                                         READY   STATUS    RESTARTS   AGE
          cluster-group-upgrades-controller-manager-75bcc7484d-8k8xp   2/2     Running   0          45m
          ```
       2. Check the TALM manager logs by running the following command:

          ```
          $ oc logs -n openshift-operators \
          cluster-group-upgrades-controller-manager-75bcc7484d-8k8xp -c manager
          ```

          Example output:

          ```
          ERROR	controller-runtime.manager.controller.clustergroupupgrade	Reconciler error	{"reconciler group": "ran.openshift.io", "reconciler kind": "ClusterGroupUpgrade", "name": "lab-upgrade", "namespace": "default", "error": "Cluster spoke5555 is not a ManagedCluster"}
          sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
          ```

The error message shows that the cluster is not a managed cluster.

**Checking if managed clusters are available**

Issue
:   You want to check if the managed clusters specified in the `ClusterGroupUpgrade` CR are available.

Resolution
:   Run the following command:

    ```
    $ oc get managedclusters
    ```

    Example output:

    ```
    NAME            HUB ACCEPTED   MANAGED CLUSTER URLS                    JOINED   AVAILABLE   AGE
    local-cluster   true           https://api.hub.testlab.com:6443        True     Unknown     13d
    spoke1          true           https://api.spoke1.testlab.com:6443     True     True        13d
    spoke3          true           https://api.spoke3.testlab.com:6443     True     True        27h
    ```

The value of the `AVAILABLE` field is `True` for the managed clusters.

**Checking clusterLabelSelector**

Issue
:   You want to check if the `clusterLabelSelector` field specified in the `ClusterGroupUpgrade` CR matches at least one of the managed clusters.

Resolution
:   Run the following command:

    ```
    $ oc get managedcluster --selector=upgrade=true
    ```

The label for the clusters you want to update is `upgrade:true`.

Example output:

```
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS                     JOINED    AVAILABLE   AGE
spoke1          true           https://api.spoke1.testlab.com:6443      True     True        13d
spoke3          true           https://api.spoke3.testlab.com:6443      True     True        27h
```

**Checking if canary clusters are present**

Issue
:   You want to check if the canary clusters are present in the list of clusters.

    Example `ClusterGroupUpgrade` CR:

```
spec:
    remediationStrategy:
        canaries:
        - spoke3
        maxConcurrency: 2
        timeout: 240
    clusterLabelSelectors:
      - matchLabels:
          upgrade: true
```

Resolution
:   Run the following commands:

    ```
    $ oc get cgu lab-upgrade -ojsonpath='{.spec.clusters}'
    ```

    Example output:

    ```
    ["spoke1", "spoke3"]
    ```

    1. Check if the canary clusters are present in the list of clusters that match `clusterLabelSelector` labels by running the following command:

       ```
       $ oc get managedcluster --selector=upgrade=true
       ```

       Example output:

       ```
       NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED    AVAILABLE   AGE
       spoke1          true           https://api.spoke1.testlab.com:6443   True     True        13d
       spoke3          true           https://api.spoke3.testlab.com:6443   True     True        27h
       ```

Note

A cluster can be present in `spec.clusters` and also be matched by the `spec.clusterLabelSelector` label.

**Checking the pre-caching status on spoke clusters**

1. Check the status of pre-caching by running the following command on the spoke cluster:

   ```
   $ oc get jobs,pods -n openshift-talo-pre-cache
   ```

**Remediation Strategy**

**Checking if remediationStrategy is present in the ClusterGroupUpgrade CR**

Issue
:   You want to check if the `remediationStrategy` is present in the `ClusterGroupUpgrade` CR.

Resolution
:   Run the following command:

    ```
    $ oc get cgu lab-upgrade -ojsonpath='{.spec.remediationStrategy}'
    ```

    Example output:

    ```
    {"maxConcurrency":2, "timeout":240}
    ```

**Checking if maxConcurrency is specified in the ClusterGroupUpgrade CR**

Issue
:   You want to check if the `maxConcurrency` is specified in the `ClusterGroupUpgrade` CR.

Resolution
:   Run the following command:

    ```
    $ oc get cgu lab-upgrade -ojsonpath='{.spec.remediationStrategy.maxConcurrency}'
    ```

    Example output:

    ```
    2
    ```

**Topology Aware Lifecycle Manager**

**Checking condition message and status in the ClusterGroupUpgrade CR**

Issue
:   You want to check the value of the `status.conditions` field in the `ClusterGroupUpgrade` CR.

Resolution
:   Run the following command:

    ```
    $ oc get cgu lab-upgrade -ojsonpath='{.status.conditions}'
    ```

    Example output:

    ```
    {"lastTransitionTime":"2022-02-17T22:25:28Z", "message":"Missing managed policies:[policyList]", "reason":"NotAllManagedPoliciesExist", "status":"False", "type":"Validated"}
    ```

**Checking if status.remediationPlan was computed**

Issue
:   You want to check if `status.remediationPlan` is computed.

Resolution
:   Run the following command:

    ```
    $ oc get cgu lab-upgrade -ojsonpath='{.status.remediationPlan}'
    ```

    Example output:

    ```
    [["spoke2", "spoke3"]]
    ```

**Errors in the TALM manager container**

Issue
:   You want to check the logs of the manager container of TALM.

Resolution
:   Run the following command:

    ```
    $ oc logs -n openshift-operators \
    cluster-group-upgrades-controller-manager-75bcc7484d-8k8xp -c manager
    ```

    Example output:

    ```
    ERROR	controller-runtime.manager.controller.clustergroupupgrade	Reconciler error	{"reconciler group": "ran.openshift.io", "reconciler kind": "ClusterGroupUpgrade", "name": "lab-upgrade", "namespace": "default", "error": "Cluster spoke5555 is not a ManagedCluster"}
    sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
    ```

Displays the error.

**Clusters are not compliant to some policies after a `ClusterGroupUpgrade` CR has completed**

Issue
:   The policy compliance status that TALM uses to decide if remediation is needed has not yet fully updated for all clusters. This may be because:

    * The CGU was run too soon after a policy was created or updated.
    * The remediation of a policy affects the compliance of subsequent policies in the `ClusterGroupUpgrade` CR.

Resolution
:   Create and apply a new `ClusterGroupUpdate` CR with the same specification.

**Auto-created `ClusterGroupUpgrade` CR in the GitOps ZTP workflow has no managed policies**

Issue
:   If there are no policies for the managed cluster when the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR with no policies is auto-created. Upon completion of the `ClusterGroupUpgrade` CR, the managed cluster is labeled as `ztp-done`. If the `PolicyGenerator` or `PolicyGenTemplate` CRs were not pushed to the Git repository within the required time after `ClusterInstance` resources were pushed, this might result in no policies being available for the target cluster when the cluster became `Ready`.

Resolution
:   Verify that the policies you want to apply are available on the hub cluster, then create a `ClusterGroupUpgrade` CR with the required policies.

You can either manually create the `ClusterGroupUpgrade` CR or trigger auto-creation again. To trigger auto-creation of the `ClusterGroupUpgrade` CR, remove the `ztp-done` label from the cluster and delete the empty `ClusterGroupUpgrade` CR that was previously created in the `zip-install` namespace.

**Pre-caching has failed**

Issue
:   Pre-caching might fail for one of the following reasons:

    * There is not enough free space on the node.
    * For a disconnected environment, the pre-cache image has not been properly mirrored.
    * There was an issue when creating the pod.

Resolution
:   1. To check if pre-caching has failed due to insufficient space, check the log of the pre-caching pod in the node.

       1. Find the name of the pod using the following command:

          ```
          $ oc get pods -n openshift-talo-pre-cache
          ```
       2. Check the logs to see if the error is related to insufficient space using the following command:

          ```
          $ oc logs -n openshift-talo-pre-cache <pod name>
          ```
    2. If there is no log, check the pod status using the following command:

       ```
       $ oc describe pod -n openshift-talo-pre-cache <pod name>
       ```
    3. If the pod does not exist, check the job status to see why it could not create a pod using the following command:

       ```
       $ oc describe job -n openshift-talo-pre-cache pre-cache
       ```

**Matching policies and `ManagedCluster` CRs before the managed cluster is available**

Issue
:   You want RHACM to match policies and managed clusters before the managed clusters become available.

Resolution
:   To ensure that TALM correctly applies the RHACM policies specified in the `spec.managedPolicies` field of the `ClusterGroupUpgrade` (CGU) CR, TALM needs to match these policies to the managed cluster before the managed cluster is available. The RHACM `PolicyGenerator` uses the generated `Placement` CR to do this automatically. By default, this `Placement` CR includes the necessary tolerations to ensure proper TALM behavior.

    The expected `spec.tolerations` settings in the `Placement` CR are as follows:

    ```
    #…​
      tolerations:
        - key: cluster.open-cluster-management.io/unavailable
         operator: Exists
        - key: cluster.open-cluster-management.io/unreachable
         operator: Exists
    #…​
    ```

    If you use a custom `Placement` CR instead of the one generated by the RHACM `PolicyGenerator`, include these tolerations in that `Placement` CR.

    For more information on placements in RHACM, see [Placement overview](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html-single/clusters/index#placement-overview).

    For more information on tolerations in RHACM, see [Placing managed clusters by using taints and tolerations](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html-single/clusters/index#taints-tolerations-managed).

To ensure that the `ClusterGroupUpgrade` configuration is functional, you can do the following:

**Procedure**

1. Create the `ClusterGroupUpgrade` CR with the `spec.enable` field set to `false`.
2. Wait for the status to be updated and go through the troubleshooting questions.
3. If everything looks as expected, set the `spec.enable` field to `true` in the `ClusterGroupUpgrade` CR.

   Warning

   After you set the `spec.enable` field to `true` in the `ClusterUpgradeGroup` CR, the update procedure starts and you cannot edit the CR’s `spec` fields anymore.

## [Chapter 14. Expanding single-node OpenShift clusters with GitOps ZTP](#ztp-sno-additional-worker-node) Copy linkLink copied to clipboard!

You can expand single-node OpenShift clusters with GitOps Zero Touch Provisioning (ZTP). When you add a worker node to single-node OpenShift clusters, the original single-node OpenShift cluster retains the control plane node role. Adding a worker node does not require any downtime for the existing single-node OpenShift cluster.

Note

You can only expand a single-node OpenShift cluster with one additional worker node. It is not recommended to expand a single-node OpenShift cluster with more than one worker node.

If you require workload partitioning on the worker node, you must deploy and remediate the managed cluster policies on the hub cluster before installing the node. This way, the workload partitioning `MachineConfig` objects are rendered and associated with the `worker` machine config pool before the GitOps ZTP workflow applies the `MachineConfig` ignition file to the worker node.

It is recommended that you first remediate the policies, and then install the worker node. If you create the workload partitioning manifests after installing the worker node, you must drain the node manually and delete all the pods managed by daemon sets. When the managing daemon sets create the new pods, the new pods undergo the workload partitioning process.

Important

Adding a worker node to single-node OpenShift clusters with GitOps ZTP is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

### [14.1. Applying profiles to the worker node with PolicyGenerator or PolicyGenTemplate resources](#ztp-additional-worker-apply-du-profile_sno-additional-worker) Copy linkLink copied to clipboard!

You can configure the additional worker node with a DU profile.

You can apply a RAN distributed unit (DU) profile to the worker node cluster using the GitOps Zero Touch Provisioning (ZTP) common, group, and site-specific `PolicyGenerator` or `PolicyGenTemplate` resources. The GitOps ZTP pipeline that is linked to the ArgoCD `policies` application includes the following CRs that you can find in the relevant `out/argocd/example` folder when you extract the `ztp-site-generate` container:

/acmpolicygenerator resources
:   * `acm-common-ranGen.yaml`
    * `acm-group-du-sno-ranGen.yaml`
    * `acm-example-sno-site.yaml`
    * `ns.yaml`
    * `kustomization.yaml`

/policygentemplates resources
:   * `common-ranGen.yaml`
    * `group-du-sno-ranGen.yaml`
    * `example-sno-site.yaml`
    * `ns.yaml`
    * `kustomization.yaml`

Configuring the DU profile on the worker node is considered an upgrade. To initiate the upgrade flow, you must update the existing policies or create additional ones. Then, you must create a `ClusterGroupUpgrade` CR to reconcile the policies in the group of clusters.

### [14.2. Ensuring PTP and SR-IOV daemon selector compatibility](#ztp-additional-worker-daemon-selector-comp_sno-additional-worker) Copy linkLink copied to clipboard!

If the DU profile was deployed using the GitOps Zero Touch Provisioning (ZTP) plugin version 4.11 or earlier, the PTP and SR-IOV Operators might be configured to place the daemons only on nodes labeled as `master`. This configuration prevents the PTP and SR-IOV daemons from operating on the worker node. If the PTP and SR-IOV daemon node selectors are incorrectly configured on your system, you must change the daemons before proceeding with the worker DU profile configuration.

**Procedure**

1. Check the daemon node selector settings of the PTP Operator on one of the spoke clusters:

   ```
   $ oc get ptpoperatorconfig/default -n openshift-ptp -ojsonpath='{.spec}' | jq
   ```

   The following is example output for the PTP Operator:

   ```
   {"daemonNodeSelector":{"node-role.kubernetes.io/master":""}}
   ```

   * If the node selector is set to `master`, the spoke was deployed with the version of the GitOps ZTP plugin that requires changes.
2. Check the daemon node selector settings of the SR-IOV Operator on one of the spoke clusters:

   ```
   $  oc get sriovoperatorconfig/default -n \
   openshift-sriov-network-operator -ojsonpath='{.spec}' | jq
   ```

   The following is example output for the SR-IOV Operator:

   ```
   {"configDaemonNodeSelector":{"node-role.kubernetes.io/worker":""},"disableDrain":false,"enableInjector":true,"enableOperatorWebhook":true}
   ```

   * If the node selector is set to `master`, the spoke was deployed with the version of the GitOps ZTP plugin that requires changes.
3. In the group policy, add the following `complianceType` and `spec` entries:

   ```
   spec:
       - fileName: PtpOperatorConfig.yaml
         policyName: "config-policy"
         complianceType: mustonlyhave
         spec:
           daemonNodeSelector:
             node-role.kubernetes.io/worker: ""
       - fileName: SriovOperatorConfig.yaml
         policyName: "config-policy"
         complianceType: mustonlyhave
         spec:
           configDaemonNodeSelector:
             node-role.kubernetes.io/worker: ""
   ```

   Important

   Changing the `daemonNodeSelector` field causes temporary PTP synchronization loss and SR-IOV connectivity loss.
4. Commit the changes in Git, and then push to the Git repository being monitored by the GitOps ZTP ArgoCD application.

### [14.3. PTP and SR-IOV node selector compatibility](#ztp-additional-worker-node-selector-comp_sno-additional-worker) Copy linkLink copied to clipboard!

The PTP configuration resources and SR-IOV network node policies use `node-role.kubernetes.io/master: ""` as the node selector. If the additional worker node has the same NIC configuration as the control plane node, the policies used to configure the control plane node can be reused for the worker node. However, the node selector must be changed to select both node types, for example with the `"node-role.kubernetes.io/worker"` label.

### [14.4. Using PolicyGenerator CRs to apply worker node policies to the worker node](#ztp-additional-worker-policies-PolicyGenerator_sno-additional-worker) Copy linkLink copied to clipboard!

You can create policies for the additional worker node by using `PolicyGenerator` CRs.

**Procedure**

1. Create the following `PolicyGenerator` CR:

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: PolicyGenerator
   metadata:
       name: example-sno-workers
   placementBindingDefaults:
       name: example-sno-workers-placement-binding
   policyDefaults:
       namespace: example-sno
       placement:
           labelSelector:
               matchExpressions:
                   - key: sites
                     operator: In
                     values:
                       - example-sno
       remediationAction: inform
       severity: low
       namespaceSelector:
           exclude:
               - kube-*
           include:
               - '*'
       evaluationInterval:
           compliant: 10m
           noncompliant: 10s
   policies:
       - name: example-sno-workers-config-policy
         policyAnnotations:
           ran.openshift.io/ztp-deploy-wave: "10"
         manifests:
           - path: source-crs/PerformanceProfile-MCP-worker.yaml
             patches:
               - metadata:
                   name: openshift-worker-node-performance-profile
                 spec:
                   cpu:
                       isolated: 4-47
                       reserved: 0-3
                   hugepages:
                       defaultHugepagesSize: 1G
                       pages:
                           - count: 32
                             size: 1G
                   realTimeKernel:
                       enabled: true
           - path: source-crs/TunedPerformancePatch-MCP-worker.yaml
             patches:
               - metadata:
                   name: performance-patch-worker
                 spec:
                   profile:
                       - data: |
                         [main]
                         summary=Configuration changes profile inherited from performance created tuned
                         include=openshift-node-performance-openshift-worker-node-performance-profile
                         [bootloader]
                         cmdline_crash=nohz_full=4-47
                         [sysctl]
                         kernel.timer_migration=1
                         [scheduler]
                         group.ice-ptp=0:f:10:*:ice-ptp.*
                         [service]
                         service.stalld=start,enable
                         service.chronyd=stop,disable
                         name: performance-patch-worker
                   recommend:
                       - profile: performance-patch-worker
   ```

   * `policyDefaults.placement.labelSelector.matchExpressions` — The policies are applied to all clusters with this label.
   * `spec.cpu.isolated` and `spec.cpu.reserved` in the `PerformanceProfile-MCP-worker.yaml` manifest — These fields must be configured for each specific hardware platform.
   * `cmdline_crash` in the `TunedPerformancePatch-MCP-worker.yaml` manifest — The `nohz_full` CPU set must match the `cpu.isolated` set in the `PerformanceProfile` section.

   You can generate the content of `crio` and `kubelet` configuration files.
2. Add the created policy template to the Git repository monitored by the ArgoCD `policies` application.
3. Add the policy in the `kustomization.yaml` file.
4. Commit the changes in Git, and then push to the Git repository being monitored by the GitOps ZTP ArgoCD application.
5. To remediate the new policies to your spoke cluster, create a TALM custom resource:

   ```
   $ cat <<EOF | oc apply -f -
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: example-sno-worker-policies
     namespace: default
   spec:
     backup: false
     clusters:
     - example-sno
     enable: true
     managedPolicies:
     - group-du-sno-config-policy
     - example-sno-workers-config-policy
     - example-sno-config-policy
     preCaching: false
     remediationStrategy:
       maxConcurrency: 1
   EOF
   ```

### [14.5. Using PolicyGenTemplate CRs to apply worker node policies to the worker node](#ztp-additional-worker-policies-PolicyGenTemplate_sno-additional-worker) Copy linkLink copied to clipboard!

You can create policies for the additional worker node by using `PolicyGenTemplate` CRs.

**Procedure**

1. Create the following `PolicyGenTemplate` CR:

   ```
   apiVersion: ran.openshift.io/v1
   kind: PolicyGenTemplate
   metadata:
     name: "example-sno-workers"
     namespace: "example-sno"
   spec:
     bindingRules:
       sites: "example-sno"
     mcp: "worker"
     sourceFiles:
       - fileName: MachineConfigGeneric.yaml
         policyName: "config-policy"
         metadata:
           labels:
             machineconfiguration.openshift.io/role: worker
           name: enable-workload-partitioning
         spec:
           config:
             storage:
               files:
               - contents:
                   source: data:text/plain;charset=utf-8;base64,W2NyaW8ucnVudGltZS53b3JrbG9hZHMubWFuYWdlbWVudF0KYWN0aXZhdGlvbl9hbm5vdGF0aW9uID0gInRhcmdldC53b3JrbG9hZC5vcGVuc2hpZnQuaW8vbWFuYWdlbWVudCIKYW5ub3RhdGlvbl9wcmVmaXggPSAicmVzb3VyY2VzLndvcmtsb2FkLm9wZW5zaGlmdC5pbyIKcmVzb3VyY2VzID0geyAiY3B1c2hhcmVzIiA9IDAsICJjcHVzZXQiID0gIjAtMyIgfQo=
                 mode: 420
                 overwrite: true
                 path: /etc/crio/crio.conf.d/01-workload-partitioning
                 user:
                   name: root
               - contents:
                   source: data:text/plain;charset=utf-8;base64,ewogICJtYW5hZ2VtZW50IjogewogICAgImNwdXNldCI6ICIwLTMiCiAgfQp9Cg==
                 mode: 420
                 overwrite: true
                 path: /etc/kubernetes/openshift-workload-pinning
                 user:
                   name: root
       - fileName: PerformanceProfile.yaml
         policyName: "config-policy"
         metadata:
           name: openshift-worker-node-performance-profile
         spec:
           cpu:
             isolated: "4-47"
             reserved: "0-3"
           hugepages:
             defaultHugepagesSize: 1G
             pages:
               - size: 1G
                 count: 32
           realTimeKernel:
             enabled: true
       - fileName: TunedPerformancePatch.yaml
         policyName: "config-policy"
         metadata:
           name: performance-patch-worker
         spec:
           profile:
             - name: performance-patch-worker
               data: |
                 [main]
                 summary=Configuration changes profile inherited from performance created tuned
                 include=openshift-node-performance-openshift-worker-node-performance-profile
                 [bootloader]
                 cmdline_crash=nohz_full=4-47
                 [sysctl]
                 kernel.timer_migration=1
                 [scheduler]
                 group.ice-ptp=0:f:10:*:ice-ptp.*
                 [service]
                 service.stalld=start,enable
                 service.chronyd=stop,disable
           recommend:
           - profile: performance-patch-worker
   ```

   * `spec.bindingRules.sites` — The policies are applied to all clusters with this label.
   * `spec.mcp` — The `MCP` field must be set to `worker`.
   * `MachineConfigGeneric.yaml` in `spec.sourceFiles` — This generic `MachineConfig` CR is used to configure workload partitioning on the worker node.
   * `spec.cpu.isolated` and `spec.cpu.reserved` in the `PerformanceProfile.yaml` manifest — These fields must be configured for each particular hardware platform.
   * `cmdline_crash` in the `TunedPerformancePatch.yaml` manifest — The `nohz_full` CPU set must match the `cpu.isolated` set in the `PerformanceProfile` section.

   You can generate the content of `crio` and `kubelet` configuration files.
2. Add the created policy template to the Git repository monitored by the ArgoCD `policies` application.
3. Add the policy in the `kustomization.yaml` file.
4. Commit the changes in Git, and then push to the Git repository being monitored by the GitOps ZTP ArgoCD application.
5. To remediate the new policies to your spoke cluster, create a TALM custom resource:

   ```
   $ cat <<EOF | oc apply -f -
   apiVersion: ran.openshift.io/v1alpha1
   kind: ClusterGroupUpgrade
   metadata:
     name: example-sno-worker-policies
     namespace: default
   spec:
     backup: false
     clusters:
     - example-sno
     enable: true
     managedPolicies:
     - group-du-sno-config-policy
     - example-sno-workers-config-policy
     - example-sno-config-policy
     preCaching: false
     remediationStrategy:
       maxConcurrency: 1
   EOF
   ```

### [14.6. Adding an additional worker node single-node OpenShift clusters with GitOps ZTP](#ztp-additional-worker-sno-proc_sno-additional-worker) Copy linkLink copied to clipboard!

You can add an additional worker node to existing single-node OpenShift clusters to increase available CPU resources in the cluster.

**Prerequisites**

* Install and configure RHACM 2.12 or later in an OpenShift Container Platform 4.11 or later bare-metal hub cluster
* Install Topology Aware Lifecycle Manager in the hub cluster
* Install Red Hat OpenShift GitOps in the hub cluster
* Use the GitOps ZTP `ztp-site-generate` container image version 4.12 or later
* Deploy a managed single-node OpenShift cluster with GitOps ZTP
* Configure the Central Infrastructure Management as described in the RHACM documentation
* Configure the DNS serving the cluster to resolve the internal API endpoint `api-int.<cluster_name>.<base_domain>`

**Procedure**

1. If you deployed your cluster by using the `example-sno.yaml` `ClusterInstance` CR, add your new worker node to the `spec.nodes` list:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-sno"
     namespace: "example-sno"
   spec:
     # ... existing cluster configuration ...
     nodes:
         - hostName: "example-sno.example.com"
           role: "master"
           # ... existing master node configuration ...
         - hostName: "example-node2.example.com"
           role: "worker"
           bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
           bmcCredentialsName:
             name: "example-node2-bmh-secret"
           bootMACAddress: "AA:BB:CC:DD:EE:11"
           bootMode: "UEFI"
           nodeNetwork:
             interfaces:
               - name: eno1
                 macAddress: "AA:BB:CC:DD:EE:11"
             config:
               interfaces:
                 - name: eno1
                   type: ethernet
                   state: up
                   macAddress: "AA:BB:CC:DD:EE:11"
                   ipv4:
                     enabled: false
                   ipv6:
                     enabled: true
                     address:
                     - ip: 1111:2222:3333:4444::1
                       prefix-length: 64
               dns-resolver:
                 config:
                   search:
                   - example.com
                   server:
                   - 1111:2222:3333:4444::2
               routes:
                 config:
                 - destination: ::/0
                   next-hop-interface: eno1
                   next-hop-address: 1111:2222:3333:4444::1
                   table-id: 254
   ```
2. Create a BMC authentication secret for the new host, as referenced by the `bmcCredentialsName` field in the `spec.nodes` section of your `ClusterInstance` CR:

   ```
   apiVersion: v1
   data:
     password: "password"
     username: "username"
   kind: Secret
   metadata:
     name: "example-node2-bmh-secret"
     namespace: example-sno
   type: Opaque
   ```
3. Commit the changes in Git, and then push to the Git repository that is being monitored by the GitOps ZTP ArgoCD application.

   When the ArgoCD `cluster` application synchronizes, two new manifests appear on the hub cluster generated by the SiteConfig Operator:

   * `BareMetalHost`
   * `NMStateConfig`

     Important

     The `cpuset` field should not be configured for the worker node. Workload partitioning for the worker node is added through management policies after the node installation is complete.

**Verification**

You can monitor the installation process in several ways.

* Check if the preprovisioning images are created by running the following command:

  ```
  $ oc get ppimg -n example-sno
  ```

  The following is example output:

  ```
  NAMESPACE       NAME            READY   REASON
  example-sno     example-sno     True    ImageCreated
  example-sno     example-node2   True    ImageCreated
  ```
* Check the state of the bare-metal hosts:

  ```
  $ oc get bmh -n example-sno
  ```

  The following is example output:

  ```
  NAME            STATE          CONSUMER   ONLINE   ERROR   AGE
  example-sno     provisioned               true             69m
  example-node2   provisioning              true             4m50s
  ```

  + The `provisioning` state indicates that node booting from the installation media is in progress.
* Continuously monitor the installation process:

  1. Watch the agent install process by running the following command:

     ```
     $ oc get agent -n example-sno --watch
     ```

     The following is example output:

     ```
     NAME                                   CLUSTER   APPROVED   ROLE     STAGE
     671bc05d-5358-8940-ec12-d9ad22804faa   example-sno   true       master   Done
     [...]
     14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Starting installation
     14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Installing
     14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Writing image to disk
     [...]
     14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Waiting for control plane
     [...]
     14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Rebooting
     14fd821b-a35d-9cba-7978-00ddf535ff37   example-sno   true       worker   Done
     ```
  2. When the worker node installation is finished, the worker node certificates are approved automatically. At this point, the worker appears in the `ManagedClusterInfo` status. Run the following command to see the status:

     ```
     $ oc get managedclusterinfo/example-sno -n example-sno -o \
     jsonpath='{range .status.nodeList[*]}{.name}{"\t"}{.conditions}{"\t"}{.labels}{"\n"}{end}'
     ```

     The following is example output:

     ```
     example-sno	[{"status":"True","type":"Ready"}]	{"node-role.kubernetes.io/master":"","node-role.kubernetes.io/worker":""}
     example-node2	[{"status":"True","type":"Ready"}]	{"node-role.kubernetes.io/worker":""}
     ```

## [Chapter 15. Pre-caching images for single-node OpenShift deployments](#ztp-pre-staging-tool) Copy linkLink copied to clipboard!

In environments with limited bandwidth where you use the GitOps Zero Touch Provisioning (ZTP) solution to deploy a large number of clusters, you want to avoid downloading all the images that are required for bootstrapping and installing OpenShift Container Platform. The limited bandwidth at remote single-node OpenShift sites can cause long deployment times. The factory-precaching-cli tool allows you to pre-stage servers before shipping them to the remote site for ZTP provisioning.

The factory-precaching-cli tool does the following:

* Downloads the RHCOS rootfs image that is required by the minimal ISO to boot.
* Creates a partition from the installation disk labelled as `data`.
* Formats the disk in xfs.
* Creates a GUID Partition Table (GPT) data partition at the end of the disk, where the size of the partition is configurable by the tool.
* Copies the container images required to install OpenShift Container Platform.
* Copies the container images required by ZTP to install OpenShift Container Platform.
* Optional: Copies Day-2 Operators to the partition.

Important

The factory-precaching-cli tool is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

### [15.1. Getting the factory-precaching-cli tool](#ztp-getting-tool_pre-caching) Copy linkLink copied to clipboard!

The factory-precaching-cli tool Go binary is publicly available in [the {rds-first} tools container image](https://quay.io/openshift-kni/telco-ran-tools:latest). The factory-precaching-cli tool Go binary in the container image is executed on the server running an RHCOS live image using `podman`. If you are working in a disconnected environment or have a private registry, you need to copy the image there so you can download the image to the server.

**Procedure**

* Pull the factory-precaching-cli tool image by running the following command:

  ```
  # podman pull quay.io/openshift-kni/telco-ran-tools:latest
  ```

**Verification**

* To check that the tool is available, query the current version of the factory-precaching-cli tool Go binary:

  ```
  # podman run quay.io/openshift-kni/telco-ran-tools:latest -- factory-precaching-cli -v
  ```

  The following is example output:

  ```
  factory-precaching-cli version 20221018.120852+main.feecf17
  ```

### [15.2. Booting from a live operating system image](#ztp-booting-from-live-os_pre-caching) Copy linkLink copied to clipboard!

You can use the factory-precaching-cli tool to boot servers where only one disk is available and an external disk drive cannot be attached to the server.

Warning

RHCOS requires the disk to not be in use when the disk is about to be written with an RHCOS image.

Depending on the server hardware, you can mount the RHCOS live ISO on the blank server using one of the following methods:

* Using the Dell RACADM tool on a Dell server.
* Using the HPONCFG tool on a HP server.
* Using the Redfish BMC API.

It is recommended to automate the mounting procedure. To automate the procedure, you need to pull the required images and host them on a local HTTP server.

**Prerequisites**

* You powered up the host.
* You have network connectivity to the host.

The following example procedure uses the Redfish BMC API to mount the RHCOS live ISO.

**Procedure**

1. Mount the RHCOS live ISO:

   1. Check virtual media status:

      ```
      $ curl --globoff -H "Content-Type: application/json" -H \
      "Accept: application/json" -k -X GET --user ${username_password} \
      https://$BMC_ADDRESS/redfish/v1/Managers/Self/VirtualMedia/1 | python -m json.tool
      ```
   2. Mount the ISO file as a virtual media:

      ```
      $ curl --globoff -L -w "%{http_code} %{url_effective}\\n" -ku ${username_password} -H "Content-Type: application/json" -H "Accept: application/json" -d '{"Image": "http://[$HTTPd_IP]/RHCOS-live.iso"}' -X POST https://$BMC_ADDRESS/redfish/v1/Managers/Self/VirtualMedia/1/Actions/VirtualMedia.InsertMedia
      ```
   3. Set the boot order to boot from the virtual media once:

      ```
      $ curl --globoff  -L -w "%{http_code} %{url_effective}\\n"  -ku ${username_password}  -H "Content-Type: application/json" -H "Accept: application/json" -d '{"Boot":{ "BootSourceOverrideEnabled": "Once", "BootSourceOverrideTarget": "Cd", "BootSourceOverrideMode": "UEFI"}}' -X PATCH https://$BMC_ADDRESS/redfish/v1/Systems/Self
      ```
2. Reboot and ensure that the server is booting from virtual media.

### [15.3. Partitioning the disk](#ztp-partitioning_pre-caching) Copy linkLink copied to clipboard!

To run the full pre-caching process, you have to boot from a live ISO and use the factory-precaching-cli tool from a container image to partition and pre-cache all the artifacts required.

A live ISO or RHCOS live ISO is required because the disk must not be in use when the operating system (RHCOS) is written to the device during the provisioning. Single-disk servers can also be enabled with this procedure.

**Prerequisites**

* You have a disk that is not partitioned.
* You have access to the `quay.io/openshift-kni/telco-ran-tools:latest` image.
* You have enough storage to install OpenShift Container Platform and pre-cache the required images.
* The container must run as `privileged` due to formatting host devices.
* You have to mount the `/dev` folder so that the process can be executed inside the container.

**Procedure**

1. Verify that the disk is cleared:

   ```
   # lsblk
   ```

   The following is example output:

   ```
   NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   loop0     7:0    0  93.8G  0 loop /run/ephemeral
   loop1     7:1    0 897.3M  1 loop /sysroot
   sr0      11:0    1   999M  0 rom  /run/media/iso
   nvme0n1 259:1    0   1.5T  0 disk
   ```
2. Erase any file system, RAID or partition table signatures from the device:

   ```
   # wipefs -a /dev/nvme0n1
   ```

   The following is example output:

   ```
   /dev/nvme0n1: 8 bytes were erased at offset 0x00000200 (gpt): 45 46 49 20 50 41 52 54
   /dev/nvme0n1: 8 bytes were erased at offset 0x1749a955e00 (gpt): 45 46 49 20 50 41 52 54
   /dev/nvme0n1: 2 bytes were erased at offset 0x000001fe (PMBR): 55 aa
   ```

   Important

   The tool fails if the disk is not empty because it uses partition number 1 of the device for pre-caching the artifacts.

   Create a single partition and a GPT partition table. The partition is automatically labelled as `data` and created at the end of the device. Otherwise, the partition will be overridden by the `coreos-installer`.

   Important

   The `coreos-installer` requires the partition to be created at the end of the device and to be labelled as `data`. Both requirements are necessary to save the partition when writing the RHCOS image to the disk.
3. Run the container as `privileged` and partition the disk. In the following example, the size of the partition is 250 GiB to allow pre-caching the DU profile for Day 2 Operators:

   ```
   # podman run -v /dev:/dev --privileged \
   --rm quay.io/openshift-kni/telco-ran-tools:latest -- \
   factory-precaching-cli partition \
   -d /dev/nvme0n1 \
   -s 250
   ```

   Where:

   * `factory-precaching-cli partition` specifies the partitioning function of the factory-precaching-cli tool.
   * `-d /dev/nvme0n1` defines the root directory on the disk.
   * `-s 250` defines the size of the disk in GB.
4. Check the storage information:

   ```
   # lsblk
   ```

   The following is example output:

   ```
   NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   loop0         7:0    0  93.8G  0 loop /run/ephemeral
   loop1         7:1    0 897.3M  1 loop /sysroot
   sr0          11:0    1   999M  0 rom  /run/media/iso
   nvme0n1     259:1    0   1.5T  0 disk
   └─nvme0n1p1 259:3    0   250G  0 part
   ```

   After verifying that the disk is partitioned correctly, mount the device into `/mnt`.

   Important

   It is recommended to mount the device into `/mnt` because that mounting point is used during GitOps ZTP preparation.
5. Verify that the partition is formatted as `xfs`:

   ```
   # lsblk -f /dev/nvme0n1
   ```

   The following is example output:

   ```
   NAME        FSTYPE LABEL UUID                                 MOUNTPOINT
   nvme0n1
   └─nvme0n1p1 xfs          1bee8ea4-d6cf-4339-b690-a76594794071
   ```
6. Mount the partition:

   ```
   # mount /dev/nvme0n1p1 /mnt/
   ```

**Verification**

* Verify that the device has a GPT partition table, the partition uses the latest sectors of the device, and the partition is correctly labeled as `data`. Query the disk status to verify that the disk is partitioned as expected:

  ```
  # gdisk -l /dev/nvme0n1
  ```

  The following is example output:

  ```
  GPT fdisk (gdisk) version 1.0.3

  Partition table scan:
    MBR: protective
    BSD: not present
    APM: not present
    GPT: present

  Found valid GPT with protective MBR; using GPT.
  Disk /dev/nvme0n1: 3125627568 sectors, 1.5 TiB
  Model: Dell Express Flash PM1725b 1.6TB SFF
  Sector size (logical/physical): 512/512 bytes
  Disk identifier (GUID): CB5A9D44-9B3C-4174-A5C1-C64957910B61
  Partition table holds up to 128 entries
  Main partition table begins at sector 2 and ends at sector 33
  First usable sector is 34, last usable sector is 3125627534
  Partitions will be aligned on 2048-sector boundaries
  Total free space is 2601338846 sectors (1.2 TiB)

  Number  Start (sector)    End (sector)  Size       Code  Name
     1      2601338880      3125627534   250.0 GiB   8300  data
  ```
* Check that the partition is mounted:

  ```
  # lsblk
  ```

  The following is example output:

  ```
  NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
  loop0         7:0    0  93.8G  0 loop /run/ephemeral
  loop1         7:1    0 897.3M  1 loop /sysroot
  sr0          11:0    1   999M  0 rom  /run/media/iso
  nvme0n1     259:1    0   1.5T  0 disk
  └─nvme0n1p1 259:2    0   250G  0 part /var/mnt
  ```

  The mount point is `/var/mnt` because the `/mnt` folder in RHCOS is a link to `/var/mnt`.

### [15.4. Downloading the images](#ztp-downloading-images_pre-caching) Copy linkLink copied to clipboard!

The factory-precaching-cli tool allows you to download the following images to your partitioned server:

* OpenShift Container Platform images
* Operator images that are included in the distributed unit (DU) profile for 5G RAN sites
* Operator images from disconnected registries

Note

The list of available Operator images can vary in different OpenShift Container Platform releases.

The factory-precaching-cli tool uses parallel workers to download multiple images simultaneously. You can configure the number of workers with the `--parallel` or `-p` option. The default number is set to 80% of the available CPUs to the server.

Note

Your login shell may be restricted to a subset of CPUs, which reduces the CPUs available to the container. To remove this restriction, you can precede your commands with `taskset 0xffffffff`, for example:

```
# taskset 0xffffffff podman run --rm quay.io/openshift-kni/telco-ran-tools:latest factory-precaching-cli download --help
```

#### [15.4.1. Preparing to download the OpenShift Container Platform images](#ztp-preparing-ocp-images_pre-caching) Copy linkLink copied to clipboard!

To download OpenShift Container Platform container images, you need to know the multicluster engine version. When you use the `--du-profile` flag, you also need to specify the Red Hat Advanced Cluster Management (RHACM) version running in the hub cluster that is going to provision the single-node OpenShift.

**Prerequisites**

* You have RHACM and the multicluster engine Operator installed.
* You partitioned the storage device.
* You have enough space for the images on the partitioned device.
* You connected the bare-metal server to the Internet.
* You have a valid pull secret.

**Procedure**

1. Check the RHACM version and the multicluster engine version by running the following commands in the hub cluster:

   ```
   $ oc get csv -A | grep -i advanced-cluster-management
   ```

   The following is example output:

   ```
   open-cluster-management                            advanced-cluster-management.v2.6.3           Advanced Cluster Management for Kubernetes   2.6.3                 advanced-cluster-management.v2.6.3                Succeeded
   ```

   ```
   $ oc get csv -A | grep -i multicluster-engine
   ```

   The following is example output:

   ```
   multicluster-engine                                cluster-group-upgrades-operator.v0.0.3       cluster-group-upgrades-operator              0.0.3                                                                   Pending
   multicluster-engine                                multicluster-engine.v2.1.4                   multicluster engine for Kubernetes           2.1.4                 multicluster-engine.v2.0.3                        Succeeded
   multicluster-engine                                openshift-gitops-operator.v1.5.7             Red Hat OpenShift GitOps                     1.5.7                 openshift-gitops-operator.v1.5.6-0.1664915551.p   Succeeded
   multicluster-engine                                openshift-pipelines-operator-rh.v1.6.4       Red Hat OpenShift Pipelines                  1.6.4                 openshift-pipelines-operator-rh.v1.6.3            Succeeded
   ```
2. To access the container registry, copy a valid pull secret on the server to be installed:

   1. Create the `.docker` folder:

      ```
      $ mkdir /root/.docker
      ```
   2. Copy the valid pull in the `config.json` file to the previously created `.docker/` folder:

      ```
      $ cp config.json /root/.docker/config.json
      ```

      `/root/.docker/config.json` is the default path where `podman` checks for the login credentials for the registry.

   Note

   If you use a different registry to pull the required artifacts, you need to copy the proper pull secret. If the local registry uses TLS, you need to include the certificates from the registry as well.

#### [15.4.2. Downloading the OpenShift Container Platform images](#ztp-downloading-ocp-images_pre-caching) Copy linkLink copied to clipboard!

The factory-precaching-cli tool allows you to pre-cache all the container images required to provision a specific OpenShift Container Platform release.

**Procedure**

* Pre-cache the release by running the following command:

  ```
  # podman run -v /mnt:/mnt -v /root/.docker:/root/.docker --privileged --rm quay.io/openshift-kni/telco-ran-tools -- \
     factory-precaching-cli download \
     -r 4.22.0 \
     --acm-version 2.6.3 \
     --mce-version 2.1.4 \
     -f /mnt \
     --img quay.io/custom/repository
  ```

  Where:

  + `factory-precaching-cli download` specifies the downloading function of the factory-precaching-cli tool.
  + `-r 4.22.0` specifies the OpenShift Container Platform release version.
  + `--acm-version 2.6.3` specifies the RHACM version.
  + `--mce-version 2.1.4` specifies the multicluster engine version.
  + `-f /mnt` specifies the folder where you want to download the images on the disk.
  + `--img quay.io/custom/repository` is optional and specifies the repository where you store your additional images. These images are downloaded and pre-cached on the disk.

    The following is example output:

    ```
    Generated /mnt/imageset.yaml
    Generating list of pre-cached artifacts...
    Processing artifact [1/176]: ocp-v4.0-art-dev@sha256_6ac2b96bf4899c01a87366fd0feae9f57b1b61878e3b5823da0c3f34f707fbf5
    Processing artifact [2/176]: ocp-v4.0-art-dev@sha256_f48b68d5960ba903a0d018a10544ae08db5802e21c2fa5615a14fc58b1c1657c
    Processing artifact [3/176]: ocp-v4.0-art-dev@sha256_a480390e91b1c07e10091c3da2257180654f6b2a735a4ad4c3b69dbdb77bbc06
    Processing artifact [4/176]: ocp-v4.0-art-dev@sha256_ecc5d8dbd77e326dba6594ff8c2d091eefbc4d90c963a9a85b0b2f0e6155f995
    Processing artifact [5/176]: ocp-v4.0-art-dev@sha256_274b6d561558a2f54db08ea96df9892315bb773fc203b1dbcea418d20f4c7ad1
    Processing artifact [6/176]: ocp-v4.0-art-dev@sha256_e142bf5020f5ca0d1bdda0026bf97f89b72d21a97c9cc2dc71bf85050e822bbf
    ...
    Processing artifact [175/176]: ocp-v4.0-art-dev@sha256_16cd7eda26f0fb0fc965a589e1e96ff8577e560fcd14f06b5fda1643036ed6c8
    Processing artifact [176/176]: ocp-v4.0-art-dev@sha256_cf4d862b4a4170d4f611b39d06c31c97658e309724f9788e155999ae51e7188f
    ...
    Summary:

    Release:                            4.22.0
    Hub Version:                        2.6.3
    ACM Version:                        2.6.3
    MCE Version:                        2.1.4
    Include DU Profile:                 No
    Workers:                            83
    ```

**Verification**

* Check that all the images are compressed in the target folder of the server. It is recommended that you pre-cache the images in the `/mnt` folder:

  ```
  $ ls -l /mnt
  ```

  The following is example output:

  ```
  -rw-r--r--. 1 root root  136352323 Oct 31 15:19 ocp-v4.0-art-dev@sha256_edec37e7cd8b1611d0031d45e7958361c65e2005f145b471a8108f1b54316c07.tgz
  -rw-r--r--. 1 root root  156092894 Oct 31 15:33 ocp-v4.0-art-dev@sha256_ee51b062b9c3c9f4fe77bd5b3cc9a3b12355d040119a1434425a824f137c61a9.tgz
  -rw-r--r--. 1 root root  172297800 Oct 31 15:29 ocp-v4.0-art-dev@sha256_ef23d9057c367a36e4a5c4877d23ee097a731e1186ed28a26c8d21501cd82718.tgz
  -rw-r--r--. 1 root root  171539614 Oct 31 15:23 ocp-v4.0-art-dev@sha256_f0497bb63ef6834a619d4208be9da459510df697596b891c0c633da144dbb025.tgz
  -rw-r--r--. 1 root root  160399150 Oct 31 15:20 ocp-v4.0-art-dev@sha256_f0c339da117cde44c9aae8d0bd054bceb6f19fdb191928f6912a703182330ac2.tgz
  -rw-r--r--. 1 root root  175962005 Oct 31 15:17 ocp-v4.0-art-dev@sha256_f19dd2e80fb41ef31d62bb8c08b339c50d193fdb10fc39cc15b353cbbfeb9b24.tgz
  -rw-r--r--. 1 root root  174942008 Oct 31 15:33 ocp-v4.0-art-dev@sha256_f1dbb81fa1aa724e96dd2b296b855ff52a565fbef003d08030d63590ae6454df.tgz
  -rw-r--r--. 1 root root  246693315 Oct 31 15:31 ocp-v4.0-art-dev@sha256_f44dcf2c94e4fd843cbbf9b11128df2ba856cd813786e42e3da1fdfb0f6ddd01.tgz
  -rw-r--r--. 1 root root  170148293 Oct 31 15:00 ocp-v4.0-art-dev@sha256_f48b68d5960ba903a0d018a10544ae08db5802e21c2fa5615a14fc58b1c1657c.tgz
  -rw-r--r--. 1 root root  168899617 Oct 31 15:16 ocp-v4.0-art-dev@sha256_f5099b0989120a8d08a963601214b5c5cb23417a707a8624b7eb52ab788a7f75.tgz
  -rw-r--r--. 1 root root  176592362 Oct 31 15:05 ocp-v4.0-art-dev@sha256_f68c0e6f5e17b0b0f7ab2d4c39559ea89f900751e64b97cb42311a478338d9c3.tgz
  -rw-r--r--. 1 root root  157937478 Oct 31 15:37 ocp-v4.0-art-dev@sha256_f7ba33a6a9db9cfc4b0ab0f368569e19b9fa08f4c01a0d5f6a243d61ab781bd8.tgz
  -rw-r--r--. 1 root root  145535253 Oct 31 15:26 ocp-v4.0-art-dev@sha256_f8f098911d670287826e9499806553f7a1dd3e2b5332abbec740008c36e84de5.tgz
  -rw-r--r--. 1 root root  158048761 Oct 31 15:40 ocp-v4.0-art-dev@sha256_f914228ddbb99120986262168a705903a9f49724ffa958bb4bf12b2ec1d7fb47.tgz
  -rw-r--r--. 1 root root  167914526 Oct 31 15:37 ocp-v4.0-art-dev@sha256_fa3ca9401c7a9efda0502240aeb8d3ae2d239d38890454f17fe5158b62305010.tgz
  -rw-r--r--. 1 root root  164432422 Oct 31 15:24 ocp-v4.0-art-dev@sha256_fc4783b446c70df30b3120685254b40ce13ba6a2b0bf8fb1645f116cf6a392f1.tgz
  -rw-r--r--. 1 root root  306643814 Oct 31 15:11 troubleshoot@sha256_b86b8aea29a818a9c22944fd18243fa0347c7a2bf1ad8864113ff2bb2d8e0726.tgz
  ```

#### [15.4.3. Downloading the Operator images](#ztp-downloading-operator-images_pre-caching) Copy linkLink copied to clipboard!

You can also pre-cache Day-2 Operators used in the 5G Radio Access Network (RAN) Distributed Unit (DU) cluster configuration. The Day-2 Operators depend on the installed OpenShift Container Platform version.

Important

You need to include the RHACM hub and multicluster engine Operator versions by using the `--acm-version` and `--mce-version` flags so the factory-precaching-cli tool can pre-cache the appropriate containers images for RHACM and the multicluster engine Operator.

**Procedure**

* Pre-cache the Operator images:

  ```
  # podman run -v /mnt:/mnt -v /root/.docker:/root/.docker --privileged --rm quay.io/openshift-kni/telco-ran-tools:latest -- factory-precaching-cli download \
     -r 4.22.0 \
     --acm-version 2.6.3 \
     --mce-version 2.1.4 \
     -f /mnt \
     --img quay.io/custom/repository \
     --du-profile -s
  ```

  Where:

  + `factory-precaching-cli download` specifies the downloading function of the factory-precaching-cli tool.
  + `-r 4.22.0` specifies the OpenShift Container Platform release version.
  + `--acm-version 2.6.3` specifies the RHACM version.
  + `--mce-version 2.1.4` specifies the multicluster engine version.
  + `-f /mnt` specifies the folder where you want to download the images on the disk.
  + `--img quay.io/custom/repository` is optional and specifies the repository where you store your additional images. These images are downloaded and pre-cached on the disk.
  + `--du-profile -s` specifies pre-caching the Operators included in the DU configuration.

    The following is example output:

    ```
    Generated /mnt/imageset.yaml
    Generating list of pre-cached artifacts...
    Processing artifact [1/379]: ocp-v4.0-art-dev@sha256_7753a8d9dd5974be8c90649aadd7c914a3d8a1f1e016774c7ac7c9422e9f9958
    Processing artifact [2/379]: ose-kube-rbac-proxy@sha256_c27a7c01e5968aff16b6bb6670423f992d1a1de1a16e7e260d12908d3322431c
    Processing artifact [3/379]: ocp-v4.0-art-dev@sha256_370e47a14c798ca3f8707a38b28cfc28114f492bb35fe1112e55d1eb51022c99
    ...
    Processing artifact [378/379]: ose-local-storage-operator@sha256_0c81c2b79f79307305e51ce9d3837657cf9ba5866194e464b4d1b299f85034d0
    Processing artifact [379/379]: multicluster-operators-channel-rhel8@sha256_c10f6bbb84fe36e05816e873a72188018856ad6aac6cc16271a1b3966f73ceb3
    ...
    Summary:

    Release:                            4.22.0
    Hub Version:                        2.6.3
    ACM Version:                        2.6.3
    MCE Version:                        2.1.4
    Include DU Profile:                 Yes
    Workers:                            83
    ```

#### [15.4.4. Pre-caching custom images in disconnected environments](#ztp-custom-pre-caching-in-disconnected-environment_pre-caching) Copy linkLink copied to clipboard!

The `--generate-imageset` argument stops the factory-precaching-cli tool after the `ImageSetConfiguration` custom resource (CR) is generated. This allows you to customize the `ImageSetConfiguration` CR before downloading any images. After you customized the CR, you can use the `--skip-imageset` argument to download the images that you specified in the `ImageSetConfiguration` CR.

You can customize the `ImageSetConfiguration` CR in the following ways:

* Add Operators and additional images
* Remove Operators and additional images
* Change Operator and catalog sources to local or disconnected registries

**Procedure**

1. Pre-cache the images:

   ```
   # podman run -v /mnt:/mnt -v /root/.docker:/root/.docker --privileged --rm quay.io/openshift-kni/telco-ran-tools:latest -- factory-precaching-cli download \
      -r 4.22.0 \
      --acm-version 2.6.3 \
      --mce-version 2.1.4 \
      -f /mnt \
      --img quay.io/custom/repository \
      --du-profile -s \
      --generate-imageset
   ```

   Where:

   * `factory-precaching-cli download` specifies the downloading function of the factory-precaching-cli tool.
   * `-r 4.22.0` specifies the OpenShift Container Platform release version.
   * `--acm-version 2.6.3` specifies the RHACM version.
   * `--mce-version 2.1.4` specifies the multicluster engine version.
   * `-f /mnt` specifies the folder where you want to download the images on the disk.
   * `--img quay.io/custom/repository` is optional and specifies the repository where you store your additional images. These images are downloaded and pre-cached on the disk.
   * `--du-profile -s` specifies pre-caching the Operators included in the DU configuration.
   * `--generate-imageset` generates the `ImageSetConfiguration` CR only, which allows you to customize the CR.

     The following is example output:

     ```
     Generated /mnt/imageset.yaml
     ```

     The following example shows the `ImageSetConfiguration` CR:

     ```
     apiVersion: mirror.openshift.io/v1alpha2
     kind: ImageSetConfiguration
     mirror:
       platform:
         channels:
         - name: stable-4.22
           minVersion: 4.22.0
           maxVersion: 4.22.0
       additionalImages:
         - name: quay.io/custom/repository
       operators:
         - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.22
           packages:
             - name: advanced-cluster-management
               channels:
                  - name: 'release-2.6'
                    minVersion: 2.6.3
                    maxVersion: 2.6.3
             - name: multicluster-engine
               channels:
                  - name: 'stable-2.1'
                    minVersion: 2.1.4
                    maxVersion: 2.1.4
             - name: local-storage-operator
               channels:
                 - name: 'stable'
             - name: ptp-operator
               channels:
                 - name: 'stable'
             - name: sriov-network-operator
               channels:
                 - name: 'stable'
             - name: cluster-logging
               channels:
                 - name: 'stable'
             - name: lvms-operator
               channels:
                 - name: 'stable-4.22'
             - name: amq7-interconnect-operator
               channels:
                 - name: '1.10.x'
             - name: bare-metal-event-relay
               channels:
                 - name: 'stable'
         - catalog: registry.redhat.io/redhat/certified-operator-index:v4.22
           packages:
             - name: sriov-fec
               channels:
                 - name: 'stable'
     ```

     Where:
   * `mirror.platform.channels.minVersion`, `mirror.platform.channels.maxVersion` — Specifies the platform versions that match the versions passed to the tool.
   * `mirror.operators.packages.name: advanced-cluster-management`, `mirror.operators.packages.name: multicluster-engine` — Specifies the versions of RHACM and the multicluster engine Operator that match the versions passed to the tool.
   * `mirror.operators.packages.name: local-storage-operator`, `mirror.operators.packages.name: ptp-operator`, `mirror.operators.packages.name: sriov-network-operator`, `mirror.operators.packages.name: cluster-logging`, `mirror.operators.packages.name: lvms-operator`, `mirror.operators.packages.name: amq7-interconnect-operator`, `mirror.operators.packages.name: bare-metal-event-relay`, `mirror.operators.packages.name: sriov-fec` — Specifies the CR contains all the specified DU Operators.
2. Customize the catalog resource in the CR:

   ```
   apiVersion: mirror.openshift.io/v1alpha2
   kind: ImageSetConfiguration
   mirror:
     platform:
   [...]
     operators:
       - catalog: eko4.cloud.lab.eng.bos.redhat.com:8443/redhat/certified-operator-index:v4.22
         packages:
           - name: sriov-fec
             channels:
               - name: 'stable'
   ```

   When you download images by using a local or disconnected registry, you have to first add certificates for the registries that you want to pull the content from.
3. To avoid any errors, copy the registry certificate into your server:

   ```
   # cp /tmp/eko4-ca.crt /etc/pki/ca-trust/source/anchors/.
   ```
4. Then, update the certificates truststore:

   ```
   # update-ca-trust
   ```
5. Mount the host `/etc/pki` folder into the factory-cli image:

   ```
   # podman run -v /mnt:/mnt -v /root/.docker:/root/.docker -v /etc/pki:/etc/pki --privileged --rm quay.io/openshift-kni/telco-ran-tools:latest -- \
   factory-precaching-cli download \
      -r 4.22.0 \
      --acm-version 2.6.3 \
      --mce-version 2.1.4 \
      -f /mnt \
      --img quay.io/custom/repository \
      --du-profile -s \
      --skip-imageset
   ```

   Where:

   * `factory-precaching-cli download` specifies the downloading function of the factory-precaching-cli tool.
   * `-r 4.22.0` specifies the OpenShift Container Platform release version.
   * `--acm-version 2.6.3` specifies the RHACM version.
   * `--mce-version 2.1.4` specifies the multicluster engine version.
   * `-f /mnt` specifies the folder where you want to download the images on the disk.
   * `--img quay.io/custom/repository` is optional and specifies the repository where you store your additional images. These images are downloaded and pre-cached on the disk.
   * `--du-profile -s` specifies pre-caching the Operators included in the DU configuration.
   * `--skip-imageset` specifies to download the images in your customized `ImageSetConfiguration` CR.
6. Download the images without generating a new `imageSetConfiguration` CR:

   ```
   # podman run -v /mnt:/mnt -v /root/.docker:/root/.docker --privileged --rm quay.io/openshift-kni/telco-ran-tools:latest -- factory-precaching-cli download -r 4.22.0 \
   --acm-version 2.6.3 --mce-version 2.1.4 -f /mnt \
   --img quay.io/custom/repository \
   --du-profile -s \
   --skip-imageset
   ```

### [15.5. Pre-caching images in GitOps ZTP](#ztp-pre-caching-config-con_pre-caching) Copy linkLink copied to clipboard!

The `ClusterInstance` manifest defines the installation and configuration parameters for an OpenShift Container Platform cluster. In the GitOps Zero Touch Provisioning (ZTP) provisioning workflow, the factory-precaching-cli tool uses the following fields in the `ClusterInstance` manifest to load the pre-cached images:

* `spec.ignitionConfigOverride`
* `spec.nodes[].ignitionConfigOverride`
* `spec.nodes[].installerArgs`

The following example shows the `ClusterInstance` CR with the pre-caching fields:

```
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "sno-worker-0"
  namespace: "sno-worker-0"
spec:
  baseDomain: "example.domain.redhat.com"
  pullSecretRef:
    name: "assisted-deployment-pull-secret"
  clusterImageSetNameRef: "openshift-{product-version}"
  sshPublicKey: "ssh-rsa ..."
  clusterName: "sno-worker-0"
  extraLabels:
    ManagedCluster:
      group-du-sno: ""
      common-411: "true"
      sites: "example-5g-lab"
      vendor: "OpenShift"
  clusterNetwork:
    - cidr: 10.128.0.0/14
      hostPrefix: 23
  machineNetwork:
    - cidr: 10.19.32.192/26
  serviceNetwork:
    - cidr: 172.30.0.0/16
  networkType: "OVNKubernetes"
  additionalNTPSources:
    - 1111:2222:3333:4444::2
  templateRefs:
    - name: ai-cluster-templates-v1
      namespace: siteconfig-system
  ignitionConfigOverride: |
    {
      "ignition": {
        "version": "3.2.0"
      },
      "systemd": {
        "units": [
          {
            "name": "var-mnt.mount",
            "enabled": true,
            "contents": "[Unit]\nDescription=Mount partition with artifacts\nBefore=precache-images.service\nBindsTo=precache-images.service\nStopWhenUnneeded=true\n\n[Mount]\nWhat=/dev/disk/by-partlabel/data\nWhere=/var/mnt\nType=xfs\nTimeoutSec=30\n\n[Install]\nRequiredBy=precache-images.service"
          },
          {
            "name": "precache-images.service",
            "enabled": true,
            "contents": "[Unit]\nDescription=Extracts the precached images in discovery stage\nAfter=var-mnt.mount\nBefore=agent.service\n\n[Service]\nType=oneshot\nUser=root\nWorkingDirectory=/var/mnt\nExecStart=bash /usr/local/bin/extract-ai.sh\n\n[Install]\nWantedBy=multi-user.target default.target\nWantedBy=agent.service"
          }
        ]
      },
      "storage": {
        "files": [
          {
            "overwrite": true,
            "path": "/usr/local/bin/extract-ai.sh",
            "mode": 755,
            "user": {
              "name": "root"
            },
            "contents": {
              "source": "data:,%23%21%2Fbin%2Fbash%0A%0AFOLDER%3D%22%24%7BFOLDER%3A-%24%28pwd%29%7D%22%0AOCP_RELEASE_LIST%3D%22%24%7BOCP_RELEASE_LIST%3A-ai-images.txt%7D%22%0ABINARY_FOLDER%3D%2Fvar%2Fmnt%0A%0Apushd%20%24FOLDER%0A%0Atotal_copies%3D%24%28sort%20-u%20%24BINARY_FOLDER%2F%24OCP_RELEASE_LIST%20%7C%20wc%20-l%29%20%20%23%20Required%20to%20keep%20track%20of%20the%20pull%20task%20vs%20total%0Acurrent_copy%3D1%0A%0Awhile%20read%20-r%20line%3B%0Ado%0A%20%20uri%3D%24%28echo%20%22%24line%22%20%7C%20awk%20%27%7Bprint%241%7D%27%29%0A%20%20%23tar%3D%24%28echo%20%22%24line%22%20%7C%20awk%20%27%7Bprint%242%7D%27%29%0A%20%20podman%20image%20exists%20%24uri%0A%20%20if%20%5B%5B%20%24%3F%20-eq%200%20%5D%5D%3B%20then%0A%20%20%20%20%20%20echo%20%22Skipping%20existing%20image%20%24tar%22%0A%20%20%20%20%20%20echo%20%22Copying%20%24%7Buri%7D%20%5B%24%7Bcurrent_copy%7D%2F%24%7Btotal_copies%7D%5D%22%0A%20%20%20%20%20%20current_copy%3D%24%28%28current_copy%20%2B%201%29%29%0A%20%20%20%20%20%20continue%0A%20%20fi%0A%20%20tar%3D%24%28echo%20%22%24uri%22%20%7C%20%20rev%20%7C%20cut%20-d%20%22%2F%22%20-f1%20%7C%20rev%20%7C%20tr%20%22%3A%22%20%22_%22%29%0A%20%20tar%20zxvf%20%24%7Btar%7D.tgz%0A%20%20if%20%5B%20%24%3F%20-eq%200%20%5D%3B%20then%20rm%20-f%20%24%7Btar%7D.gz%3B%20fi%0A%20%20echo%20%22Copying%20%24%7Buri%7D%20%5B%24%7Bcurrent_copy%7D%2F%24%7Btotal_copies%7D%5D%22%0A%20%20skopeo%20copy%20dir%3A%2F%2F%24%28pwd%29%2F%24%7Btar%7D%20containers-storage%3A%24%7Buri%7D%0A%20%20if%20%5B%20%24%3F%20-eq%200%20%5D%3B%20then%20rm%20-rf%20%24%7Btar%7D%3B%20current_copy%3D%24%28%28current_copy%20%2B%201%29%29%3B%20fi%0Adone%20%3C%20%24%7BBINARY_FOLDER%7D%2F%24%7BOCP_RELEASE_LIST%7D%0A%0A%23%20workaround%20while%20https%3A%2F%2Fgithub.com%2Fopenshift%2Fassisted-service%2Fpull%2F3546%0A%23cp%20%2Fvar%2Fmnt%2Fmodified-rhcos-4.10.3-x86_64-metal.x86_64.raw.gz%20%2Fvar%2Ftmp%2F.%0A%0Aexit%200"
            }
          },
          {
            "overwrite": true,
            "path": "/usr/local/bin/agent-fix-bz1964591",
            "mode": 755,
            "user": {
              "name": "root"
            },
            "contents": {
              "source": "data:,%23%21%2Fusr%2Fbin%2Fsh%0A%0A%23%20This%20script%20is%20a%20workaround%20for%20bugzilla%201964591%20where%20symlinks%20inside%20%2Fvar%2Flib%2Fcontainers%2F%20get%0A%23%20corrupted%20under%20some%20circumstances.%0A%23%0A%23%20In%20order%20to%20let%20agent.service%20start%20correctly%20we%20are%20checking%20here%20whether%20the%20requested%0A%23%20container%20image%20exists%20and%20in%20case%20%22podman%20images%22%20returns%20an%20error%20we%20try%20removing%20the%20faulty%0A%23%20image.%0A%23%0A%23%20In%20such%20a%20scenario%20agent.service%20will%20detect%20the%20image%20is%20not%20present%20and%20pull%20it%20again.%20In%20case%0A%23%20the%20image%20is%20present%20and%20can%20be%20detected%20correctly%2C%20no%20any%20action%20is%20required.%0A%0AIMAGE%3D%24%28echo%20%241%20%7C%20sed%20%27s%2F%3A.%2A%2F%2F%27%29%0Apodman%20image%20exists%20%24IMAGE%20%7C%7C%20echo%20%22already%20loaded%22%20%7C%7C%20echo%20%22need%20to%20be%20pulled%22%0A%23podman%20images%20%7C%20grep%20%24IMAGE%20%7C%7C%20podman%20rmi%20--force%20%241%20%7C%7C%20true"
            }
          }
        ]
      }
    }
  nodes:
    - hostName: "snonode.sno-worker-0.example.domain.redhat.com"
      role: "master"
      bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
      bmcCredentialsName:
        name: "worker0-bmh-secret"
      bootMACAddress: "AA:BB:CC:DD:EE:11"
      bootMode: "UEFI"
      rootDeviceHints:
        deviceName: /dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0
      installerArgs: '["--save-partlabel", "data"]'
      ignitionConfigOverride: |
        {
          "ignition": {
            "version": "3.2.0"
          },
          "systemd": {
            "units": [
              {
                "name": "var-mnt.mount",
                "enabled": true,
                "contents": "[Unit]\nDescription=Mount partition with artifacts\nBefore=precache-ocp-images.service\nBindsTo=precache-ocp-images.service\nStopWhenUnneeded=true\n\n[Mount]\nWhat=/dev/disk/by-partlabel/data\nWhere=/var/mnt\nType=xfs\nTimeoutSec=30\n\n[Install]\nRequiredBy=precache-ocp-images.service"
              },
              {
                "name": "precache-ocp-images.service",
                "enabled": true,
                "contents": "[Unit]\nDescription=Extracts the precached OCP images into containers storage\nAfter=var-mnt.mount\nBefore=machine-config-daemon-pull.service nodeip-configuration.service\n\n[Service]\nType=oneshot\nUser=root\nWorkingDirectory=/var/mnt\nExecStart=bash /usr/local/bin/extract-ocp.sh\nTimeoutStopSec=60\n\n[Install]\nWantedBy=multi-user.target"
              }
            ]
          },
          "storage": {
            "files": [
              {
                "overwrite": true,
                "path": "/usr/local/bin/extract-ocp.sh",
                "mode": 755,
                "user": {
                  "name": "root"
                },
                "contents": {
                  "source": "data:,%23%21%2Fbin%2Fbash%0A%0AFOLDER%3D%22%24%7BFOLDER%3A-%24%28pwd%29%7D%22%0AOCP_RELEASE_LIST%3D%22%24%7BOCP_RELEASE_LIST%3A-ocp-images.txt%7D%22%0ABINARY_FOLDER%3D%2Fvar%2Fmnt%0A%0Apushd%20%24FOLDER%0A%0Atotal_copies%3D%24%28sort%20-u%20%24BINARY_FOLDER%2F%24OCP_RELEASE_LIST%20%7C%20wc%20-l%29%20%20%23%20Required%20to%20keep%20track%20of%20the%20pull%20task%20vs%20total%0Acurrent_copy%3D1%0A%0Awhile%20read%20-r%20line%3B%0Ado%0A%20%20uri%3D%24%28echo%20%22%24line%22%20%7C%20awk%20%27%7Bprint%241%7D%27%29%0A%20%20%23tar%3D%24%28echo%20%22%24line%22%20%7C%20awk%20%27%7Bprint%242%7D%27%29%0A%20%20podman%20image%20exists%20%24uri%0A%20%20if%20%5B%5B%20%24%3F%20-eq%200%20%5D%5D%3B%20then%0A%20%20%20%20%20%20echo%20%22Skipping%20existing%20image%20%24tar%22%0A%20%20%20%20%20%20echo%20%22Copying%20%24%7Buri%7D%20%5B%24%7Bcurrent_copy%7D%2F%24%7Btotal_copies%7D%5D%22%0A%20%20%20%20%20%20current_copy%3D%24%28%28current_copy%20%2B%201%29%29%0A%20%20%20%20%20%20continue%0A%20%20fi%0A%20%20tar%3D%24%28echo%20%22%24uri%22%20%7C%20%20rev%20%7C%20cut%20-d%20%22%2F%22%20-f1%20%7C%20rev%20%7C%20tr%20%22%3A%22%20%22_%22%29%0A%20%20tar%20zxvf%20%24%7Btar%7D.tgz%0A%20%20if%20%5B%20%24%3F%20-eq%200%20%5D%3B%20then%20rm%20-f%20%24%7Btar%7D.gz%3B%20fi%0A%20%20echo%20%22Copying%20%24%7Buri%7D%20%5B%24%7Bcurrent_copy%7D%2F%24%7Btotal_copies%7D%5D%22%0A%20%20skopeo%20copy%20dir%3A%2F%2F%24%28pwd%29%2F%24%7Btar%7D%20containers-storage%3A%24%7Buri%7D%0A%20%20if%20%5B%20%24%3F%20-eq%200%20%5D%3B%20then%20rm%20-rf%20%24%7Btar%7D%3B%20current_copy%3D%24%28%28current_copy%20%2B%201%29%29%3B%20fi%0Adone%20%3C%20%24%7BBINARY_FOLDER%7D%2F%24%7BOCP_RELEASE_LIST%7D%0A%0Aexit%200"
                }
              }
            ]
          }
        }
      nodeNetwork:
        interfaces:
          - name: "ens1f0"
            macAddress: "AA:BB:CC:11:22:33"
        config:
          interfaces:
            - name: ens1f0
              type: ethernet
              state: up
              macAddress: "AA:BB:CC:11:22:33"
              ipv4:
                enabled: true
                dhcp: true
              ipv6:
                enabled: false
      templateRefs:
        - name: ai-node-templates-v1
          namespace: siteconfig-system
```

Where:

`spec.clusterImageSetNameRef`
:   Specifies the cluster image set used for deployment.

`spec.ignitionConfigOverride`
:   Configures the cluster-level ignition config override for the discovery stage.

`spec.nodes[].installerArgs`
:   Specifies the installation program arguments to preserve the data partition.

`spec.nodes[].ignitionConfigOverride`
:   Configures the node-level ignition config override for the installation stage.

#### [15.5.1. Understanding the spec.ignitionConfigOverride field](#ztp-pre-caching-config-spec-ignitionconfigoverride_pre-caching) Copy linkLink copied to clipboard!

The `spec.ignitionConfigOverride` field adds a configuration in Ignition format during the GitOps ZTP discovery stage. The configuration includes `systemd` services in the ISO mounted in virtual media. This way, the scripts are part of the discovery RHCOS live ISO and they can be used to load the Assisted Installer (AI) images.

`systemd` services
:   The `systemd` services are `var-mnt.mount` and `precache-images.services`. The `precache-images.service` depends on the disk partition to be mounted in `/var/mnt` by the `var-mnt.mount` unit. The service calls a script called `extract-ai.sh`.

`extract-ai.sh`
:   The `extract-ai.sh` script extracts and loads the required images from the disk partition to the local container storage. When the script finishes successfully, you can use the images locally.

`agent-fix-bz1964591`
:   The `agent-fix-bz1964591` script is a workaround for an AI issue. To prevent AI from removing the images, which can force the `agent.service` to pull the images again from the registry, the `agent-fix-bz1964591` script checks if the requested container images exist.

#### [15.5.2. Understanding the spec.nodes[].installerArgs field](#ztp-pre-caching-config-spec-nodes-installerargs_pre-caching) Copy linkLink copied to clipboard!

The `spec.nodes[].installerArgs` field allows you to configure how the `coreos-installer` utility writes the RHCOS live ISO to disk. You need to indicate to save the disk partition labeled as `data` because the artifacts saved in the `data` partition are needed during the OpenShift Container Platform installation stage.

The extra parameters are passed directly to the `coreos-installer` utility that writes the live RHCOS to disk. On the next reboot, the operating system starts from the disk.

You can pass several options to the `coreos-installer` utility:

```
OPTIONS:
...
    -u, --image-url <URL>
            Manually specify the image URL

    -f, --image-file <path>
            Manually specify a local image file

    -i, --ignition-file <path>
            Embed an Ignition config from a file

    -I, --ignition-url <URL>
            Embed an Ignition config from a URL
...
        --save-partlabel <lx>...
            Save partitions with this label glob

        --save-partindex <id>...
            Save partitions with this number or range
...
        --insecure-ignition
            Allow Ignition URL without HTTPS or hash
```

#### [15.5.3. Understanding the spec.nodes[].ignitionConfigOverride field](#ztp-pre-caching-config-spec-nodes-ignitionconfigoverride_pre-caching) Copy linkLink copied to clipboard!

Similarly to `spec.ignitionConfigOverride`, the `spec.nodes[].ignitionConfigOverride` field allows the addition of configurations in Ignition format to the `coreos-installer` utility, but at the OpenShift Container Platform installation stage. When the RHCOS is written to disk, the extra configuration included in the GitOps ZTP discovery ISO is no longer available. During the discovery stage, the extra configuration is stored in the memory of the live OS.

Note

At this stage, the number of container images extracted and loaded is bigger than in the discovery stage. Depending on the OpenShift Container Platform release and whether you install the Day-2 Operators, the installation time can vary.

At the installation stage, the `var-mnt.mount` and `precache-ocp.services` `systemd` services are used.

`precache-ocp.service`
:   The `precache-ocp.service` depends on the disk partition to be mounted in `/var/mnt` by the `var-mnt.mount` unit. The `precache-ocp.service` service calls a script called `extract-ocp.sh`.

    Important

    To extract all the images before the OpenShift Container Platform installation, you must execute `precache-ocp.service` before executing the `machine-config-daemon-pull.service` and `nodeip-configuration.service` services.

`extract-ocp.sh`
:   The `extract-ocp.sh` script extracts and loads the required images from the disk partition to the local container storage.

When you commit the `ClusterInstance` and optional `PolicyGenerator` or `PolicyGenTemplate` custom resources (CRs) to the Git repo that Argo CD is monitoring, you can start the GitOps ZTP workflow by syncing the CRs with the hub cluster.

### [15.6. Troubleshooting a "Rendered catalog is invalid" error](#ztp-pre-staging-troubleshooting_pre-caching) Copy linkLink copied to clipboard!

When you download images by using a local or disconnected registry, you might see the `The rendered catalog is invalid` error. This means that you are missing certificates of the new registry you want to pull content from.

Note

The factory-precaching-cli tool image is built on a UBI RHEL image. Certificate paths and locations are the same on RHCOS.

The following example shows the error output:

```
Generating list of pre-cached artifacts...
error: unable to run command oc-mirror -c /mnt/imageset.yaml file:///tmp/fp-cli-3218002584/mirror --ignore-history --dry-run: Creating directory: /tmp/fp-cli-3218002584/mirror/oc-mirror-workspace/src/publish
Creating directory: /tmp/fp-cli-3218002584/mirror/oc-mirror-workspace/src/v2
Creating directory: /tmp/fp-cli-3218002584/mirror/oc-mirror-workspace/src/charts
Creating directory: /tmp/fp-cli-3218002584/mirror/oc-mirror-workspace/src/release-signatures
backend is not configured in /mnt/imageset.yaml, using stateless mode
backend is not configured in /mnt/imageset.yaml, using stateless mode
No metadata detected, creating new workspace
level=info msg=trying next host error=failed to do request: Head "https://eko4.cloud.lab.eng.bos.redhat.com:8443/v2/redhat/redhat-operator-index/manifests/v4.11": x509: certificate signed by unknown authority host=eko4.cloud.lab.eng.bos.redhat.com:8443

The rendered catalog is invalid.

Run "oc-mirror list operators --catalog CATALOG-NAME --package PACKAGE-NAME" for more information.

error: error rendering new refs: render reference "eko4.cloud.lab.eng.bos.redhat.com:8443/redhat/redhat-operator-index:v4.11": error resolving name : failed to do request: Head "https://eko4.cloud.lab.eng.bos.redhat.com:8443/v2/redhat/redhat-operator-index/manifests/v4.11": x509: certificate signed by unknown authority
```

**Procedure**

1. Copy the registry certificate into your server:

   ```
   # cp /tmp/eko4-ca.crt /etc/pki/ca-trust/source/anchors/.
   ```
2. Update the certificates truststore:

   ```
   # update-ca-trust
   ```
3. Mount the host `/etc/pki` folder into the factory-cli image:

   ```
   # podman run -v /mnt:/mnt -v /root/.docker:/root/.docker -v /etc/pki:/etc/pki --privileged -it --rm quay.io/openshift-kni/telco-ran-tools:latest -- \
   factory-precaching-cli download -r 4.22.0 --acm-version 2.5.4 \
      --mce-version 2.0.4 -f /mnt \--img quay.io/custom/repository
      --du-profile -s --skip-imageset
   ```

## [Chapter 16. Image-based upgrade for single-node OpenShift clusters](#image-based-upgrade-for-single-node-openshift-clusters) Copy linkLink copied to clipboard!

### [16.1. Understanding the image-based upgrade for single-node OpenShift clusters](#cnf-understanding-image-based-upgrade) Copy linkLink copied to clipboard!

From OpenShift Container Platform 4.14.13, the Lifecycle Agent provides you with an alternative way to upgrade the platform version of a single-node OpenShift cluster. The image-based upgrade is faster than the standard upgrade method and allows you to directly upgrade from OpenShift Container Platform <4.y> to <4.y+2>, and <4.y.z> to <4.y.z+n>.

This upgrade method utilizes a generated OCI image from a dedicated seed cluster that is installed on the target single-node OpenShift cluster as a new `ostree` stateroot. A seed cluster is a single-node OpenShift cluster deployed with the target OpenShift Container Platform version, Day 2 Operators, and configurations that are common to all target clusters.

You can use the seed image, which is generated from the seed cluster, to upgrade the platform version on any single-node OpenShift cluster that has the same combination of hardware, Day 2 Operators, and cluster configuration as the seed cluster.

Important

The image-based upgrade uses custom images that are specific to the hardware platform that the clusters are running on. Each different hardware platform requires a separate seed image.

The Lifecycle Agent uses two custom resources (CRs) on the participating clusters to orchestrate the upgrade:

* On the seed cluster, the `SeedGenerator` CR allows for the seed image generation. This CR specifies the repository to push the seed image to.
* On the target cluster, the `ImageBasedUpgrade` CR specifies the seed image for the upgrade of the target cluster and the backup configurations for your workloads.

**Example SeedGenerator CR**

```
apiVersion: lca.openshift.io/v1
kind: SeedGenerator
metadata:
  name: seedimage
spec:
  seedImage: <seed_image>
```

**Example ImageBasedUpgrade CR**

```
apiVersion: lca.openshift.io/v1
kind: ImageBasedUpgrade
metadata:
  name: upgrade
spec:
  stage: Idle
  seedImageRef:
    version: <target_version>
    image: <seed_container_image>
    pullSecretRef:
      name: <seed_pull_secret>
  autoRollbackOnFailure: {}
  extraManifests:
  - name: example-extra-manifests
    namespace: openshift-lifecycle-agent
  # List of ConfigMap resources that contain the OADP Backup and Restore CRs.
  oadpContent:
  - name: oadp-cm-example
    namespace: openshift-adp
```

where

`spec.stage`
:   Defines the stage of the `ImageBasedUpgrade` CR. The value can be `Idle`, `Prep`, `Upgrade`, or `Rollback`.

`spec.seedImageRef`
:   Defines the seed image to be used, the target platform version, and the secret required to access the image.

`initMonitorTimeoutSeconds`
:   Optionally defines the time frame in seconds to roll back when the upgrade does not complete within that time frame after the first reboot. If not defined or set to `0`, the default value of `1800` seconds (30 minutes) is used.

`spec.extraManifests`
:   Optionally defines the list of `ConfigMap` resources that contain your custom catalog sources to retain after the upgrade, and your extra manifests to apply to the target cluster that are not part of the seed image.

`spec.oadpContent`
:   Defines the list of `ConfigMap` resources that contain the OADP `Backup` and `Restore` CRs.

#### [16.1.1. Stages of the image-based upgrade](#cnf-image-based-upgrade_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The image-based upgrade consists of four stages that you control by setting the `spec.stage` field in the `ImageBasedUpgrade` CR: Idle, Prep, Upgrade, and Rollback.

After generating the seed image on the seed cluster, you can move through the stages on the target cluster by setting the `spec.stage` field to one of the following values in the `ImageBasedUpgrade` CR:

* `Idle`
* `Prep`
* `Upgrade`
* `Rollback` (Optional)

**Figure 16.1. Stages of the image-based upgrade**

##### [16.1.1.1. Idle stage](#cnf-image-based-upgrade-concept-idle_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The Lifecycle Agent creates an `ImageBasedUpgrade` CR set to `stage: Idle` when the Operator is first deployed. This is the default stage. There is no ongoing upgrade and the cluster is ready to move to the `Prep` stage.

**Figure 16.2. Transition from Idle stage**

You also move to the `Idle` stage to do one of the following steps:

* Finalize a successful upgrade
* Finalize a rollback
* Cancel an ongoing upgrade until the pre-pivot phase in the `Upgrade` stage

Moving to the `Idle` stage ensures that the Lifecycle Agent cleans up resources, so that the cluster is ready for upgrades again.

**Figure 16.3. Transitions to Idle stage**

Important

If using RHACM when you cancel an upgrade, you must remove the `import.open-cluster-management.io/disable-auto-import` annotation from the target managed cluster to re-enable the automatic import of the cluster.

##### [16.1.1.2. Prep stage](#cnf-image-based-upgrade-concept-prep_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

Note

You can complete this stage before a scheduled maintenance window.

For the `Prep` stage, you specify the following upgrade details in the `ImageBasedUpgrade` CR:

* seed image to use
* resources to back up
* extra manifests to apply and custom catalog sources to retain after the upgrade, if any

Then, based on what you specify, the Lifecycle Agent prepares for the upgrade without impacting the current running version. During this stage, the Lifecycle Agent ensures that the target cluster is ready to proceed to the `Upgrade` stage by checking if it meets certain conditions. The Operator pulls the seed image to the target cluster with additional container images specified in the seed image. The Lifecycle Agent checks if there is enough space on the container storage disk and if necessary, the Operator deletes unpinned images until the disk usage is below the specified threshold. For more information about how to configure or disable the cleaning up of the container storage disk, see "Configuring the automatic image cleanup of the container storage disk".

You also prepare backup resources with the OADP Operator’s `Backup` and `Restore` CRs. These CRs are used in the `Upgrade` stage to reconfigure the cluster, register the cluster with RHACM, and restore application artifacts.

In addition to the OADP Operator, the Lifecycle Agent uses the `ostree` versioning system to create a backup, which allows complete cluster reconfiguration after both upgrade and rollback.

After the `Prep` stage finishes, you can cancel the upgrade process by moving to the `Idle` stage or you can start the upgrade by moving to the `Upgrade` stage in the `ImageBasedUpgrade` CR. If you cancel the upgrade, the Operator performs cleanup operations.

**Figure 16.4. Transition from Prep stage**

##### [16.1.1.3. Upgrade stage](#cnf-image-based-upgrade-concept-upgrade_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The `Upgrade` stage consists of two phases:

pre-pivot
:   Just before pivoting to the new stateroot, the Lifecycle Agent collects the required cluster specific artifacts and stores them in the new stateroot. The backup of your cluster resources specified in the `Prep` stage are created on a compatible Object storage solution. The Lifecycle Agent exports CRs specified in the `extraManifests` field in the `ImageBasedUpgrade` CR or the CRs described in the ZTP policies that are bound to the target cluster. After pre-pivot phase has completed, the Lifecycle Agent sets the new stateroot deployment as the default boot entry and reboots the node.

post-pivot
:   After booting from the new stateroot, the Lifecycle Agent also regenerates the seed image’s cluster cryptography. This ensures that each single-node OpenShift cluster upgraded with the same seed image has unique and valid cryptographic objects. The Operator then reconfigures the cluster by applying cluster-specific artifacts that were collected in the pre-pivot phase. The Operator applies all saved CRs, and restores the backups.

After the upgrade has completed and you are satisfied with the changes, you can finalize the upgrade by moving to the `Idle` stage.

Important

When you finalize the upgrade, you cannot roll back to the original release.

**Figure 16.5. Transitions from Upgrade stage**

If you want to cancel the upgrade, you can do so until the pre-pivot phase of the `Upgrade` stage. If you encounter issues after the upgrade, you can move to the `Rollback` stage for a manual rollback.

##### [16.1.1.4. Rollback stage](#cnf-image-based-upgrade-concept-rollback_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The `Rollback` stage can be initiated manually or automatically upon failure. During the `Rollback` stage, the Lifecycle Agent sets the original `ostree` stateroot deployment as default. Then, the node reboots with the previous release of OpenShift Container Platform and application configurations.

Warning

If you move to the `Idle` stage after a rollback, the Lifecycle Agent cleans up resources that can be used to troubleshoot a failed upgrade.

The Lifecycle Agent initiates an automatic rollback if the upgrade does not complete within a specified time limit. For more information about the automatic rollback, see the "Moving to the Rollback stage with Lifecycle Agent" or "Moving to the Rollback stage with Lifecycle Agent and GitOps ZTP" sections.

**Figure 16.6. Transition from Rollback stage**

#### [16.1.2. Guidelines for the image-based upgrade](#cnf-image-based-upgrade-guidelines_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

Your deployments must meet specific requirements for a successful image-based upgrade, which can be performed using either GitOps ZTP or non-GitOps deployment methods.

For a successful image-based upgrade, your deployments must meet certain requirements.

There are different deployment methods in which you can perform the image-based upgrade:

GitOps ZTP
:   You use the GitOps Zero Touch Provisioning (ZTP) to deploy and configure your clusters.

Non-GitOps
:   You manually deploy and configure your clusters.

You can perform an image-based upgrade in disconnected environments. For more information about how to mirror images for a disconnected environment, see "Mirroring images for a disconnected installation".

##### [16.1.2.1. Minimum software version of components](#cnf-image-based-upgrade-cluster-validated-software_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The image-based upgrade requires specific minimum software versions for various components depending on your deployment method.

Depending on your deployment method, the image-based upgrade requires the following minimum software versions.

Expand

Table 16.1. Minimum software version of components

| Component | Software version | Required |
| --- | --- | --- |
| Lifecycle Agent | 4.16 | Yes |
| OADP Operator | 1.4.1 | Yes |
| Managed cluster version | 4.14.13 | Yes |
| Hub cluster version | 4.16 | No |
| RHACM | 2.10.2 | No |
| GitOps ZTP plugin | 4.16 | Only for GitOps ZTP deployment method |
| Red Hat OpenShift GitOps | 1.12 | Only for GitOps ZTP deployment method |
| Topology Aware Lifecycle Manager (TALM) | 4.16 | Only for GitOps ZTP deployment method |
| Local Storage Operator [1] | 4.14 | Yes |
| Logical Volume Manager (LVM) Storage [1] | 4.14.2 | Yes |

Show more

1. The persistent storage must be provided by either the LVM Storage or the Local Storage Operator, not both.

##### [16.1.2.2. Hub cluster guidelines](#ztp-image-based-upgrade-hub-cluster-guide_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

When using RHACM, the hub cluster must meet specific conditions including disabling optional add-ons and upgrading to at least the target version.

If you are using Red Hat Advanced Cluster Management (RHACM), your hub cluster needs to meet the following conditions:

* To avoid including any RHACM resources in your seed image, you need to disable all optional RHACM add-ons before generating the seed image.
* Your hub cluster must be upgraded to at least the target version before performing an image-based upgrade on a target single-node OpenShift cluster.

##### [16.1.2.3. Seed image guidelines](#cnf-image-based-upgrade-seed-image-guide_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The seed image targets single-node OpenShift clusters with matching hardware and configuration, requiring the seed cluster to match specific aspects of the target clusters.

The seed image targets a set of single-node OpenShift clusters with the same hardware and similar configuration. This means that the seed cluster must match the configuration of the target clusters for the following items:

* CPU topology

  + Number of CPU cores
  + Tuned performance configuration, such as number of reserved CPUs
* `MachineConfig` resources for the target cluster
* IP version configuration, either IPv4, IPv6, or dual-stack networking
* Set of Day 2 Operators, including the Lifecycle Agent and the OADP Operator
* Disconnected registry
* FIPS configuration

The following configurations only have to partially match on the participating clusters:

* If the target cluster has a proxy configuration, the seed cluster must have a proxy configuration too but the configuration does not have to be the same.
* A dedicated partition on the primary disk for container storage is required on all participating clusters. However, the size and start of the partition does not have to be the same. Only the `spec.config.storage.disks.partitions.label: varlibcontainers` label in the `MachineConfig` CR must match on both the seed and target clusters. For more information about how to create the disk partition, see "Configuring a shared container partition between ostree stateroots" or "Configuring a shared container partition between ostree stateroots when using GitOps ZTP".

For more information about what to include in the seed image, see "Seed image configuration" and "Seed image configuration using the RAN DU profile".

##### [16.1.2.4. OADP backup and restore guidelines](#ztp-image-based-upgrade-backup-guide_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

Use the OADP Operator to back up and restore applications during the image-based upgrade by creating `Backup` and `Restore` custom resources (CRs) wrapped in `ConfigMap` objects.

With the OADP Operator, you can back up and restore your applications on your target clusters by using `Backup` and `Restore` CRs wrapped in `ConfigMap` objects. The application must work on the current and the target OpenShift Container Platform versions so that they can be restored after the upgrade. The backups must include resources that were initially created.

The following resources must be excluded from the backup:

* `pods`
* `endpoints`
* `controllerrevision`
* `podmetrics`
* `packagemanifest`
* `replicaset`
* `localvolume`, if using Local Storage Operator (LSO)

There are two local storage implementations for single-node OpenShift:

Local Storage Operator (LSO)
:   The Lifecycle Agent automatically backs up and restores the required artifacts, including `LocalVolume` resources and their associated `StorageClass` resources. You must exclude the `persistentvolumes` resource in the application `Backup` CR. The image-based upgrade does not support the `LocalVolumeSet` and `LocalVolumeDiscovery` CRs. If you use these CRs, the Lifecycle Agent does not restore them. Only persistent volumes that a `LocalVolume` CR created are preserved and available after the upgrade.

LVM Storage
:   You must create the `Backup` and `Restore` CRs for LVM Storage artifacts. You must include the `persistentVolumes` resource in the application `Backup` CR.

For the image-based upgrade, only one Operator is supported on a given target cluster.

Important

For both Operators, you must not apply the Operator CRs as extra manifests through the `ImageBasedUpgrade` CR.

The persistent volume contents are preserved and used after the pivot. When you are configuring the `DataProtectionApplication` CR, you must ensure that the `.spec.configuration.restic.enable` is set to `false` for an image-based upgrade. This disables Container Storage Interface integration.

##### [16.1.2.4.1. lca.openshift.io/apply-wave guidelines](#ztp-image-based-upgrade-apply-wave-guide_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

The `lca.openshift.io/apply-wave` annotation determines the apply order of `Backup` or `Restore` CRs. The value of the annotation must be a string number. If you define the `lca.openshift.io/apply-wave` annotation in the `Backup` or `Restore` CRs, they are applied in increasing order based on the annotation value. If you do not define the annotation, they are applied together.

The `lca.openshift.io/apply-wave` annotation must be numerically lower in your platform `Restore` CRs, for example RHACM and LVM Storage artifacts, than that of the application. This way, the platform artifacts are restored before your applications.

If your application includes cluster-scoped resources, you must create separate `Backup` and `Restore` CRs to scope the backup to the specific cluster-scoped resources created by the application. The `Restore` CR for the cluster-scoped resources must be restored before the remaining application `Restore` CR(s).

##### [16.1.2.4.2. lca.openshift.io/apply-label guidelines](#ztp-image-based-upgrade-apply-label-guide_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

You can back up specific resources exclusively with the `lca.openshift.io/apply-label` annotation. Based on which resources you define in the annotation, the Lifecycle Agent applies the `lca.openshift.io/backup: <backup_name>` label and adds the `labelSelector.matchLabels.lca.openshift.io/backup: <backup_name>` label selector to the specified resources when creating the `Backup` CRs.

To use the `lca.openshift.io/apply-label` annotation for backing up specific resources, the resources listed in the annotation must also be included in the `spec` section. If the `lca.openshift.io/apply-label` annotation is used in the `Backup` CR, only the resources listed in the annotation are backed up, even if other resource types are specified in the `spec` section or not.

**Example CR**

```
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: acm-klusterlet
  namespace: openshift-adp
  annotations:
    lca.openshift.io/apply-label: rbac.authorization.k8s.io/v1/clusterroles/klusterlet,apps/v1/deployments/open-cluster-management-agent/klusterlet
  labels:
    velero.io/storage-location: default
spec:
  includedNamespaces:
   - open-cluster-management-agent
  includedClusterScopedResources:
   - clusterroles
  includedNamespaceScopedResources:
   - deployments
```

* The `metadata.annotations.lca.openshift.io/apply-label` value must be a list of comma-separated objects in `group/version/resource/name` format for cluster-scoped resources or `group/version/resource/namespace/name` format for namespace-scoped resources, and it must be attached to the related `Backup` CR.

##### [16.1.2.5. Extra manifest guidelines](#cnf-image-based-upgrade-extra-manifests-guide_understanding-image-based-upgrade) Copy linkLink copied to clipboard!

Extra manifests enable the Lifecycle Agent to restore cluster-specific configurations after the upgrade pivot but before restoring application artifacts.

The Lifecycle Agent uses extra manifests to restore your target clusters after rebooting with the new stateroot deployment and before restoring application artifacts.

Different deployment methods require a different way to apply the extra manifests:

GitOps ZTP
:   You use the `lca.openshift.io/target-ocp-version: <target_ocp_version>` label to mark the extra manifests that the Lifecycle Agent must extract and apply after the pivot. You can specify the number of manifests labeled with `lca.openshift.io/target-ocp-version` by using the `lca.openshift.io/target-ocp-version-manifest-count` annotation in the `ImageBasedUpgrade` CR. If specified, the Lifecycle Agent verifies that the number of manifests extracted from policies matches the number provided in the annotation during the prep and upgrade stages.

    **Example for the lca.openshift.io/target-ocp-version-manifest-count annotation**

    ```
    apiVersion: lca.openshift.io/v1
    kind: ImageBasedUpgrade
    metadata:
      annotations:
        lca.openshift.io/target-ocp-version-manifest-count: "5"
      name: upgrade
    ```

Non-Gitops
:   You mark your extra manifests with the `lca.openshift.io/apply-wave` annotation to determine the apply order. The labeled extra manifests are wrapped in `ConfigMap` objects and referenced in the `ImageBasedUpgrade` CR that the Lifecycle Agent uses after the pivot.

If the target cluster uses custom catalog sources, you must include them as extra manifests that point to the correct release version.

Important

You cannot apply the following items as extra manifests:

* `MachineConfig` objects
* OLM Operator subscriptions

### [16.2. Preparing for an image-based upgrade for single-node OpenShift clusters](#preparing-for-an-image-based-upgrade-for-single-node-openshift-clusters) Copy linkLink copied to clipboard!

#### [16.2.1. Configuring a shared container partition for the image-based upgrade](#cnf-image-based-upgrade-shared-container-partition) Copy linkLink copied to clipboard!

Your single-node OpenShift clusters need to have a shared `/var/lib/containers` partition for the image-based upgrade. You can do this at install time.

##### [16.2.1.1. Configuring a shared container partition between ostree stateroots](#cnf-image-based-upgrade-shared-container-partition_shared-container-partition) Copy linkLink copied to clipboard!

Apply a `MachineConfig` to both the seed and the target clusters during installation time to create a separate partition and share the `/var/lib/containers` partition between the two `ostree` stateroots that will be used during the upgrade process.

Important

You must complete this procedure at installation time.

**Procedure**

* Apply a `MachineConfig` to create a separate partition:

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfig
  metadata:
    labels:
      machineconfiguration.openshift.io/role: master
    name: 98-var-lib-containers-partitioned
  spec:
    config:
      ignition:
        version: 3.2.0
      storage:
        disks:
          - device: /dev/disk/by-path/<root_disk>
            partitions:
              - label: var-lib-containers
                startMiB: <start_of_partition>
                sizeMiB: <partition_size>
        filesystems:
          - device: /dev/disk/by-partlabel/var-lib-containers
            format: xfs
            mountOptions:
              - defaults
              - prjquota
            path: /var/lib/containers
            wipeFilesystem: true
      systemd:
        units:
          - contents: |-
              # Generated by Butane
              [Unit]
              Before=local-fs.target
              Requires=systemd-fsck@dev-disk-by\x2dpartlabel-var\x2dlib\x2dcontainers.service
              After=systemd-fsck@dev-disk-by\x2dpartlabel-var\x2dlib\x2dcontainers.service

              [Mount]
              Where=/var/lib/containers
              What=/dev/disk/by-partlabel/var-lib-containers
              Type=xfs
              Options=defaults,prjquota

              [Install]
              RequiredBy=local-fs.target
            enabled: true
            name: var-lib-containers.mount
  ```

  where:

  `<root_disk>`
  :   Specifies the root disk, for example `pci-0000:01:00.0-scsi-0:2:0:0`.

  `<start_of_partition>`
  :   Specifies the start of the partition in MiB. If the value is too small, the installation will fail.

  `<partition_size>`
  :   Specifies a minimum size for the partition of 500 GB (512000 MiB) to ensure adequate disk space for precached images. If the value is too small, the deployments after installation will fail.

##### [16.2.1.2. Configuring a shared container directory between ostree stateroots when using GitOps ZTP](#ztp-image-based-upgrade-shared-container-partition_shared-container-partition) Copy linkLink copied to clipboard!

When you are using the GitOps Zero Touch Provisioning (ZTP) workflow, you do the following procedure to create a separate disk partition on both the seed and target cluster and to share the `/var/lib/containers` partition.

Important

You must complete this procedure at installation time.

**Prerequisites**

* You have installed Butane. For more information, see "Installing Butane".

**Procedure**

1. Create the `storage.bu` file:

   ```
   variant: fcos
   version: 1.3.0
   storage:
     disks:
     - device: /dev/disk/by-path/pci-<root_disk>
       wipe_table: false
       partitions:
       - label: var-lib-containers
         start_mib: <start_of_partition>
         size_mib: <partition_size>
     filesystems:
       - path: /var/lib/containers
         device: /dev/disk/by-partlabel/var-lib-containers
         format: xfs
         wipe_filesystem: true
         with_mount_unit: true
         mount_options:
           - defaults
           - prjquota
   ```

   where:

   `<root_disk>`
   :   Specifies the root disk.

   `<start_of_partition>`
   :   Specifies the start of the partition in MiB. If the value is too small, the installation will fail.

   `<partition_size>`
   :   Specifies a minimum size for the partition of 500 GB to ensure adequate disk space for precached images. If the value is too small, the deployments after installation will fail.
2. Convert the `storage.bu` to an Ignition file by running the following command:

   ```
   $ butane storage.bu
   ```

   Example output:

   ```
   {"ignition":{"version":"3.2.0"},"storage":{"disks":[{"device":"/dev/disk/by-path/pci-0000:00:17.0-ata-1.0","partitions":[{"label":"var-lib-containers","sizeMiB":0,"startMiB":250000}],"wipeTable":false}],"filesystems":[{"device":"/dev/disk/by-partlabel/var-lib-containers","format":"xfs","mountOptions":["defaults","prjquota"],"path":"/var/lib/containers","wipeFilesystem":true}]},"systemd":{"units":[{"contents":"# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target","enabled":true,"name":"var-lib-containers.mount"}]}}
   ```
3. Copy the output into the `spec.nodes[].ignitionConfigOverride` field in the `ClusterInstance` CR:

   ```
   apiVersion: siteconfig.open-cluster-management.io/v1alpha1
   kind: ClusterInstance
   metadata:
     name: "example-sno"
     namespace: "example-sno"
   spec:
     # ...
     nodes:
       - hostName: "node1.example.com"
         role: "master"
             ignitionConfigOverride: '{"ignition":{"version":"3.2.0"},"storage":{"disks":[{"device":"/dev/disk/by-path/pci-0000:00:17.0-ata-1.0","partitions":[{"label":"var-lib-containers","sizeMiB":0,"startMiB":250000}],"wipeTable":false}],"filesystems":[{"device":"/dev/disk/by-partlabel/var-lib-containers","format":"xfs","mountOptions":["defaults","prjquota"],"path":"/var/lib/containers","wipeFilesystem":true}]},"systemd":{"units":[{"contents":"# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target","enabled":true,"name":"var-lib-containers.mount"}]}}'
   ```

**Verification**

1. During or after installation, verify on the hub cluster that the `BareMetalHost` object shows the annotation by running the following command:

   ```
   $ oc get bmh -n my-sno-ns my-sno -ojson | jq '.metadata.annotations["bmac.agent-install.openshift.io/ignition-config-overrides"]'
   ```

   Example output:

   ```
   "{\"ignition\":{\"version\":\"3.2.0\"},\"storage\":{\"disks\":[{\"device\":\"/dev/disk/by-path/pci-0000:00:17.0-ata-1.0\",\"partitions\":[{\"label\":\"var-lib-containers\",\"sizeMiB\":0,\"startMiB\":250000}],\"wipeTable\":false}],\"filesystems\":[{\"device\":\"/dev/disk/by-partlabel/var-lib-containers\",\"format\":\"xfs\",\"mountOptions\":[\"defaults\",\"prjquota\"],\"path\":\"/var/lib/containers\",\"wipeFilesystem\":true}]},\"systemd\":{\"units\":[{\"contents\":\"# Generated by Butane\\n[Unit]\\nRequires=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\nAfter=systemd-fsck@dev-disk-by\\\\x2dpartlabel-var\\\\x2dlib\\\\x2dcontainers.service\\n\\n[Mount]\\nWhere=/var/lib/containers\\nWhat=/dev/disk/by-partlabel/var-lib-containers\\nType=xfs\\nOptions=defaults,prjquota\\n\\n[Install]\\nRequiredBy=local-fs.target\",\"enabled\":true,\"name\":\"var-lib-containers.mount\"}]}}"
   ```
2. After installation, check the single-node OpenShift disk status by running the following commands:

   ```
   # lsblk
   ```

   Example output:

   ```
   NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
   sda      8:0    0 446.6G  0 disk
   ├─sda1   8:1    0     1M  0 part
   ├─sda2   8:2    0   127M  0 part
   ├─sda3   8:3    0   384M  0 part /boot
   ├─sda4   8:4    0 243.6G  0 part /var
   │                                /sysroot/ostree/deploy/rhcos/var
   │                                /usr
   │                                /etc
   │                                /
   │                                /sysroot
   └─sda5   8:5    0 202.5G  0 part /var/lib/containers
   ```

   ```
   # df -h
   ```

   Example output:

   ```
   Filesystem      Size  Used Avail Use% Mounted on
   devtmpfs        4.0M     0  4.0M   0% /dev
   tmpfs           126G   84K  126G   1% /dev/shm
   tmpfs            51G   93M   51G   1% /run
   /dev/sda4       244G  5.2G  239G   3% /sysroot
   tmpfs           126G  4.0K  126G   1% /tmp
   /dev/sda5       203G  119G   85G  59% /var/lib/containers
   /dev/sda3       350M  110M  218M  34% /boot
   tmpfs            26G     0   26G   0% /run/user/1000
   ```

#### [16.2.2. Installing Operators for the image-based upgrade](#cnf-image-based-upgrade-install-operators) Copy linkLink copied to clipboard!

Prepare your clusters for the upgrade by installing the Lifecycle Agent and the OADP Operator.

To install the OADP Operator with the non-GitOps method, see "Installing the OADP Operator".

##### [16.2.2.1. Installing the Lifecycle Agent by using the CLI](#cnf-image-based-upgrade-installing-lifecycle-agent-using-cli_install-operators) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to install the Lifecycle Agent.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a `Namespace` object YAML file for the Lifecycle Agent:

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     name: openshift-lifecycle-agent
     annotations:
       workload.openshift.io/allowed: management
   ```

   1. Create the `Namespace` CR by running the following command:

      ```
      $ oc create -f <namespace_filename>.yaml
      ```
2. Create an `OperatorGroup` object YAML file for the Lifecycle Agent:

   ```
   apiVersion: operators.coreos.com/v1
   kind: OperatorGroup
   metadata:
     name: openshift-lifecycle-agent
     namespace: openshift-lifecycle-agent
   spec:
     targetNamespaces:
     - openshift-lifecycle-agent
   ```

   1. Create the `OperatorGroup` CR by running the following command:

      ```
      $ oc create -f <operatorgroup_filename>.yaml
      ```
3. Create a `Subscription` CR for the Lifecycle Agent:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: openshift-lifecycle-agent-subscription
     namespace: openshift-lifecycle-agent
   spec:
     channel: "stable"
     name: lifecycle-agent
     source: redhat-operators
     sourceNamespace: openshift-marketplace
   ```

   1. Create the `Subscription` CR by running the following command:

      ```
      $ oc create -f <subscription_filename>.yaml
      ```

**Verification**

1. To verify that the installation succeeded, inspect the CSV resource by running the following command:

   ```
   $ oc get csv -n openshift-lifecycle-agent
   ```

   Example output:

```
NAME                              DISPLAY                     VERSION               REPLACES                           PHASE
lifecycle-agent.v{product-version}.0           Openshift Lifecycle Agent   {product-version}.0                Succeeded
```

1. Verify that the Lifecycle Agent is up and running by running the following command:

   ```
   $ oc get deploy -n openshift-lifecycle-agent
   ```

   Example output:

```
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
lifecycle-agent-controller-manager   1/1     1            1           14s
```

##### [16.2.2.2. Installing the Lifecycle Agent by using the web console](#cnf-image-based-upgrade-installing-lifecycle-agent-using-web-console_install-operators) Copy linkLink copied to clipboard!

You can use the OpenShift Container Platform web console to install the Lifecycle Agent.

**Prerequisites**

* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. In the OpenShift Container Platform web console, navigate to **Ecosystem** → **Software Catalog**.
2. Search for the **Lifecycle Agent** from the list of available Operators, and then click **Install**.
3. On the **Install Operator** page, under **A specific namespace on the cluster** select **openshift-lifecycle-agent**.
4. Click **Install**.

**Verification**

1. To confirm that the installation is successful:

   1. Click **Ecosystem** → **Installed Operators**.
   2. Ensure that the Lifecycle Agent is listed in the **openshift-lifecycle-agent** project with a **Status** of **InstallSucceeded**.

      Note

      During installation an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message.

If the Operator is not installed successfully:

1. Click **Ecosystem** → **Installed Operators**, and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**.
2. Click **Workloads** → **Pods**, and check the logs for pods in the **openshift-lifecycle-agent** project.

##### [16.2.2.3. Installing the Lifecycle Agent with GitOps ZTP](#ztp-image-based-upgrade-installing-lcao-with-gitops_install-operators) Copy linkLink copied to clipboard!

Install the Lifecycle Agent with GitOps Zero Touch Provisioning (ZTP) to do an image-based upgrade.

**Procedure**

1. Extract the following CRs from the `ztp-site-generate` container image and push them to the `source-cr` directory:

   Example `LcaSubscriptionNS.yaml` file:

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     name: openshift-lifecycle-agent
     annotations:
       workload.openshift.io/allowed: management
       ran.openshift.io/ztp-deploy-wave: "2"
     labels:
       kubernetes.io/metadata.name: openshift-lifecycle-agent
   ```

   Example `LcaSubscriptionOperGroup.yaml` file:

   ```
   apiVersion: operators.coreos.com/v1
   kind: OperatorGroup
   metadata:
     name: lifecycle-agent-operatorgroup
     namespace: openshift-lifecycle-agent
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
   spec:
     targetNamespaces:
       - openshift-lifecycle-agent
   ```

   Example `LcaSubscription.yaml` file:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: lifecycle-agent
     namespace: openshift-lifecycle-agent
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
   spec:
     channel: "stable"
     name: lifecycle-agent
     source: redhat-operators
     sourceNamespace: openshift-marketplace
     installPlanApproval: Manual
   status:
     state: AtLatestKnown
   ```

   Example directory structure:

   ```
   ├── kustomization.yaml
   ├── sno
   │   ├── example-cnf.yaml
   │   ├── common-ranGen.yaml
   │   ├── group-du-sno-ranGen.yaml
   │   ├── group-du-sno-validator-ranGen.yaml
   │   └── ns.yaml
   ├── source-crs
   │   ├── LcaSubscriptionNS.yaml
   │   ├── LcaSubscriptionOperGroup.yaml
   │   ├── LcaSubscription.yaml
   ```
2. Add the CRs to your common PolicyGenerator:

   ```
   apiVersion: policy.open-cluster-management.io/v1
   kind: PolicyGenerator
   metadata:
     name: common-latest
   placementBindingDefaults:
     name: common-placement-binding
   policyDefaults:
     namespace: ztp-common
     placement:
       labelSelector:
         common: "true"
         du-profile: "latest"
     remediationAction: inform
     severity: low
     namespaceSelector:
       exclude:
         - kube-*
       include:
         - '*'
     evaluationInterval:
       compliant: 10m
       noncompliant: 10s
   policies:
   - name: common-latest-subscriptions-policy
     policyAnnotations:
       ran.openshift.io/ztp-deploy-wave: "2"
     manifests:
       - path: source-crs/LcaSubscriptionNS.yaml
       - path: source-crs/LcaSubscriptionOperGroup.yaml
       - path: source-crs/LcaSubscription.yaml
   [...]
   ```

##### [16.2.2.4. Installing and configuring the OADP Operator with GitOps ZTP](#ztp-image-based-upgrade-installing-oadp_install-operators) Copy linkLink copied to clipboard!

Install and configure the OADP Operator with GitOps ZTP before starting the upgrade.

**Procedure**

1. Extract the following CRs from the `ztp-site-generate` container image and push them to the `source-cr` directory:

   Example `OadpSubscriptionNS.yaml` file:

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     name: openshift-adp
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
     labels:
       kubernetes.io/metadata.name: openshift-adp
   ```

   Example `OadpSubscriptionOperGroup.yaml` file:

   ```
   apiVersion: operators.coreos.com/v1
   kind: OperatorGroup
   metadata:
     name: redhat-oadp-operator
     namespace: openshift-adp
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
   spec:
     targetNamespaces:
     - openshift-adp
   ```

   Example `OadpSubscription.yaml` file:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: redhat-oadp-operator
     namespace: openshift-adp
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
   spec:
     channel: stable-1.4
     name: redhat-oadp-operator
     source: redhat-operators
     sourceNamespace: openshift-marketplace
     installPlanApproval: Manual
   status:
     state: AtLatestKnown
   ```

   Example `OadpOperatorStatus.yaml` file:

   ```
   apiVersion: operators.coreos.com/v1
   kind: Operator
   metadata:
     name: redhat-oadp-operator.openshift-adp
     annotations:
       ran.openshift.io/ztp-deploy-wave: "2"
   status:
     components:
       refs:
       - kind: Subscription
         namespace: openshift-adp
         conditions:
         - type: CatalogSourcesUnhealthy
           status: "False"
       - kind: InstallPlan
         namespace: openshift-adp
         conditions:
         - type: Installed
           status: "True"
       - kind: ClusterServiceVersion
         namespace: openshift-adp
         conditions:
         - type: Succeeded
           status: "True"
           reason: InstallSucceeded
   ```

   Example directory structure:

   ```
   ├── kustomization.yaml
   ├── sno
   │   ├── example-cnf.yaml
   │   ├── common-ranGen.yaml
   │   ├── group-du-sno-ranGen.yaml
   │   ├── group-du-sno-validator-ranGen.yaml
   │   └── ns.yaml
   ├── source-crs
   │   ├── OadpSubscriptionNS.yaml
   │   ├── OadpSubscriptionOperGroup.yaml
   │   ├── OadpSubscription.yaml
   │   ├── OadpOperatorStatus.yaml
   ```
2. Add the CRs to your common `PolicyGenTemplate`:

   ```
   apiVersion: ran.openshift.io/v1
   kind: PolicyGenTemplate
   metadata:
     name: "example-common-latest"
     namespace: "ztp-common"
   spec:
     bindingRules:
       common: "true"
       du-profile: "latest"
     sourceFiles:
       - fileName: OadpSubscriptionNS.yaml
         policyName: "subscriptions-policy"
       - fileName: OadpSubscriptionOperGroup.yaml
         policyName: "subscriptions-policy"
       - fileName: OadpSubscription.yaml
         policyName: "subscriptions-policy"
       - fileName: OadpOperatorStatus.yaml
         policyName: "subscriptions-policy"
   [...]
   ```
3. Create the `DataProtectionApplication` CR and the S3 secret only for the target cluster:

   1. Extract the following CRs from the `ztp-site-generate` container image and push them to the `source-cr` directory:

      Example `OadpDataProtectionApplication.yaml` file:

      ```
      apiVersion: oadp.openshift.io/v1alpha1
      kind: DataProtectionApplication
      metadata:
        name: dataprotectionapplication
        namespace: openshift-adp
        annotations:
          ran.openshift.io/ztp-deploy-wave: "100"
      spec:
        configuration:
          restic:
            enable: false
          velero:
            defaultPlugins:
              - aws
              - openshift
            resourceTimeout: 10m
        backupLocations:
          - velero:
              config:
                profile: "default"
                region: minio
                s3Url: $url
                insecureSkipTLSVerify: "true"
                s3ForcePathStyle: "true"
              provider: aws
              default: true
              credential:
                key: cloud
                name: cloud-credentials
              objectStorage:
                bucket: $bucketName
                prefix: $prefixName
      status:
        conditions:
        - reason: Complete
          status: "True"
          type: Reconciled
      ```

      * `spec.configuration.restic.enable` must be set to `false` for an image-based upgrade because persistent volume contents are retained and reused after the upgrade.
      * `bucket` defines the bucket name created in S3 backend. `prefix` defines the name of the subdirectory that will be automatically created in the bucket. The combination of bucket and prefix must be unique for each target cluster to avoid interference between them. To ensure a unique storage directory for each target cluster, you can use the Red Hat Advanced Cluster Management hub template function, for example, `prefix: {{hub .ManagedClusterName hub}}`.

      Example `OadpSecret.yaml` file:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
        name: cloud-credentials
        namespace: openshift-adp
        annotations:
          ran.openshift.io/ztp-deploy-wave: "100"
      type: Opaque
      ```

      Example `OadpBackupStorageLocationStatus.yaml` file:

      ```
      apiVersion: velero.io/v1
      kind: BackupStorageLocation
      metadata:
        name: dataprotectionapplication-1
        namespace: openshift-adp
        annotations:
          ran.openshift.io/ztp-deploy-wave: "100"
      status:
        phase: Available
      ```

      The `name` value in the `BackupStorageLocation` resource must follow a specific naming convention that aligns with the corresponding `DataProtectionApplication` resource.

      * The name must use the `<DataProtectionApplication.metadata.name>-<index>` pattern.
      * The `<index>` represents the position of the corresponding entry in the `spec.backupLocations` field in the `DataProtectionApplication` resource. The position starts at `1`.
      * If you change the `metadata.name` value of the `DataProtectionApplication` resource in the `OadpDataProtectionApplication.yaml` file, you must also update the `metadata.name` field in the `BackupStorageLocation` resource to match the new value.

      The `OadpBackupStorageLocationStatus.yaml` CR verifies the availability of backup storage locations created by OADP.
   2. Add the CRs to your site `PolicyGenTemplate` with overrides:

      ```
      apiVersion: ran.openshift.io/v1
      kind: PolicyGenTemplate
      metadata:
        name: "example-cnf"
        namespace: "ztp-site"
      spec:
        bindingRules:
          sites: "example-cnf"
          du-profile: "latest"
        mcp: "master"
        sourceFiles:
          ...
          - fileName: OadpSecret.yaml
            policyName: "config-policy"
            data:
              cloud: <your_credentials>
          - fileName: OadpDataProtectionApplication.yaml
            policyName: "config-policy"
            spec:
              backupLocations:
                - velero:
                    config:
                      region: minio
                      s3Url: <your_S3_URL>
                      profile: "default"
                      insecureSkipTLSVerify: "true"
                      s3ForcePathStyle: "true"
                    provider: aws
                    default: true
                    credential:
                      key: cloud
                      name: cloud-credentials
                    objectStorage:
                      bucket: <your_bucket_name>
                      prefix: <cluster_name>
          - fileName: OadpBackupStorageLocationStatus.yaml
            policyName: "config-policy"
      ```

where:

`your_credentials`
:   Specifies your credentials for your S3 storage backend.

`OadpDataProtectionApplication.yaml`
:   If more than one `backupLocations` entries are defined in the `OadpDataProtectionApplication` CR, ensure that each location has a corresponding `OadpBackupStorageLocation` CR added for status tracking. Ensure that the name of each additional `OadpBackupStorageLocation` CR is overridden with the correct index as described in the example `OadpBackupStorageLocationStatus.yaml` file.

`your_S3_URL`
:   Specifies the URL for your S3-compatible bucket.

`bucket` and `prefix`
:   The `bucket` defines the bucket name that is created in S3 backend. The `prefix` defines the name of the subdirectory that will be automatically created in the `bucket`. The combination of `bucket` and `prefix` must be unique for each target cluster to avoid interference between them. To ensure a unique storage directory for each target cluster, you can use the Red Hat Advanced Cluster Management hub template function, for example, `prefix: {{hub .ManagedClusterName hub}}`.

#### [16.2.3. Generating a seed image for the image-based upgrade with the Lifecycle Agent](#cnf-image-based-upgrade-generate-seed-image) Copy linkLink copied to clipboard!

Use the Lifecycle Agent to generate the seed image with the `SeedGenerator` custom resource (CR).

##### [16.2.3.1. Seed image configuration](#cnf-image-based-upgrade-seed-image-config_generate-seed) Copy linkLink copied to clipboard!

The seed image targets a set of single-node OpenShift clusters with the same hardware and similar configuration. This means that the seed image must have all of the components and configuration that the seed cluster shares with the target clusters. Therefore, the seed image generated from the seed cluster cannot contain any cluster-specific configuration.

The following table lists the components, resources, and configurations that you must and must not include in your seed image:

Expand

Table 16.2. Seed image configuration

| Cluster configuration | Include in seed image |
| --- | --- |
| Performance profile | Yes |
| `MachineConfig` resources for the target cluster | Yes |
| IP version configuration, either IPv4, IPv6, or dual-stack networking | Yes |
| Set of Day 2 Operators, including the Lifecycle Agent and the OADP Operator | Yes |
| Disconnected registry configuration [2] | Yes |
| Valid proxy configuration [3] | Yes |
| FIPS configuration | Yes |
| Dedicated partition on the primary disk for container storage that matches the size of the target clusters | Yes |
| Local volumes  * `StorageClass` used in `LocalVolume` for LSO * `LocalVolume` for LSO * `LVMCluster` CR for LVMS | No |
| OADP `DataProtectionApplication` CR | No |

Show more

1. If the seed cluster is installed in a disconnected environment, the target clusters must also be installed in a disconnected environment.
2. The proxy configuration must be either enabled or disabled in both the seed and target clusters. However, the proxy servers configured on the clusters does not have to match.

##### [16.2.3.1.1. Seed image configuration using the RAN DU profile](#ztp-image-based-upgrade-seed-image-config-ran_generate-seed) Copy linkLink copied to clipboard!

The following table lists the components, resources, and configurations that you must and must not include in the seed image when using the RAN DU profile:

Expand

Table 16.3. Seed image configuration with RAN DU profile

| Resource | Include in seed image |
| --- | --- |
| All extra manifests that are applied as part of Day 0 installation | Yes |
| All Day 2 Operator subscriptions | Yes |
| `DisableOLMPprof.yaml` | Yes |
| `TunedPerformancePatch.yaml` | Yes |
| `PerformanceProfile.yaml` | Yes |
| `SriovOperatorConfig.yaml` | Yes |
| `DisableSnoNetworkDiag.yaml` | Yes |
| `StorageClass.yaml` | No, if it is used in `StorageLV.yaml` |
| `StorageLV.yaml` | No |
| `StorageLVMCluster.yaml` | No |
| `SriovFecClusterConfig.yaml` | No |
| `SriovVrbClusterConfig.yaml` | No |

Show more

Expand

Table 16.4. Seed image configuration with RAN DU profile for extra manifests

| Resource | Apply as extra manifest |
| --- | --- |
| `ClusterLogForwarder.yaml` | Yes  Note  The DU profile includes the Cluster Logging Operator, but the profile does not configure or apply any Cluster Logging Operator CRs. To enable log forwarding, include the `ClusterLogForwarder.yaml` CR as an extra manifest. The extra manifest is applied to the target single-node OpenShift cluster during the image-based upgrade process. |
| `ReduceMonitoringFootprint.yaml` | Yes |
| `PtpOperatorConfigForEvent.yaml` | Yes |
| `DefaultCatsrc.yaml` | Yes |
| `PtpConfig.yaml` | If the interfaces of the target cluster are common with the seed cluster, you can include them in the seed image. Otherwise, apply it as extra manifests. |
| `SriovNetwork.yaml``SriovNetworkNodePolicy.yaml` | If the configuration, including namespaces, is exactly the same on both the seed and target cluster, you can include them in the seed image. Otherwise, apply them as extra manifests. |

Show more

##### [16.2.3.2. Generating a seed image with the Lifecycle Agent](#cnf-image-based-upgrade-generate-seed-image_generate-seed) Copy linkLink copied to clipboard!

Use the Lifecycle Agent to generate a seed image from a managed cluster. The Operator checks for required system configurations, performs any necessary system cleanup before generating the seed image, and launches the image generation. The seed image generation includes the following tasks:

* Stopping cluster Operators
* Preparing the seed image configuration
* Generating and pushing the seed image to the image repository specified in the `SeedGenerator` CR
* Restoring cluster Operators
* Expiring seed cluster certificates
* Generating new certificates for the seed cluster
* Restoring and updating the `SeedGenerator` CR on the seed cluster

**Prerequisites**

* RHACM and multicluster engine for Kubernetes Operator are not installed on the seed cluster.
* You have configured a shared container directory on the seed cluster.
* You have installed the minimum version of the OADP Operator and the Lifecycle Agent on the seed cluster.
* Ensure that persistent volumes are not configured on the seed cluster.
* Ensure that the `LocalVolume` CR does not exist on the seed cluster if the Local Storage Operator is used.
* Ensure that the `LVMCluster` CR does not exist on the seed cluster if LVM Storage is used.
* Ensure that the `DataProtectionApplication` CR does not exist on the seed cluster if OADP is used.

**Procedure**

1. Detach the managed cluster from the hub to delete any RHACM-specific resources from the seed cluster that must not be in the seed image:

   1. Manually detach the seed cluster by running the following command:

      ```
      $ oc delete managedcluster sno-worker-example
      ```

      1. Wait until the managed cluster is removed. After the cluster is removed, create the proper `SeedGenerator` CR. The Lifecycle Agent cleans up the RHACM artifacts.
   2. If you are using GitOps ZTP, detach your cluster by removing the seed cluster’s `ClusterInstance` CR from the `kustomization.yaml`.

      1. If you have a `kustomization.yaml` file that references multiple `ClusterInstance` CRs, remove your seed cluster’s `ClusterInstance` CR from the `kustomization.yaml`:

         ```
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization

         resources:
         #- clusterinstance-seed-sno1.yaml
         - clusterinstance-target-sno2.yaml
         - clusterinstance-target-sno3.yaml
         ```
      2. If you have a `kustomization.yaml` that references one `ClusterInstance` CR, remove your seed cluster’s `ClusterInstance` CR from the `kustomization.yaml` and add the `resources: []` line:

         ```
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization

         resources: []
         ```
      3. Commit the `kustomization.yaml` changes in your Git repository and push the changes to your repository.

         The ArgoCD pipeline detects the changes and removes the managed cluster.
2. Create the `Secret` object so that you can push the seed image to your registry.

   1. Create the authentication file by running the following commands:

      ```
      $ MY_USER=myuserid
      ```

      ```
      $ AUTHFILE=/tmp/my-auth.json
      ```

      ```
      $ podman login --authfile ${AUTHFILE} -u ${MY_USER} quay.io/${MY_USER}
      ```

      ```
      $ base64 -w 0 ${AUTHFILE} ; echo
      ```
   2. Copy the output into the `seedAuth` field in the `Secret` YAML file named `seedgen` in the `openshift-lifecycle-agent` namespace:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
        name: <secret_name>
        namespace: openshift-lifecycle-agent
      type: Opaque
      data:
        seedAuth: <encoded_authfile>
      ```

      where:

      `<secret_name>`
      :   Specifies the name of the `Secret` resource. The value must be `seedgen`.

      `<encoded_authfile>`
      :   Specifies a base64-encoded authfile for write-access to the registry for pushing the generated seed images.
   3. Apply the `Secret` by running the following command:

      ```
      $ oc apply -f secretseedgenerator.yaml
      ```
3. Create the `SeedGenerator` CR:

   ```
   apiVersion: lca.openshift.io/v1
   kind: SeedGenerator
   metadata:
     name: <seedgenerator_name>
   spec:
     seedImage: <seed_container_image>
   ```

   where:

   `<seedgenerator_name>`
   :   Specifies the name of the `SeedGenerator` CR. The value must be `seedimage`.

   `<seed_container_image>`
   :   Specifies the container image URL, for example, `quay.io/example/seed-container-image:<tag>`. It is recommended to use the `<seed_cluster_name>:<ocp_version>` format.
4. Generate the seed image by running the following command:

   ```
   $ oc apply -f seedgenerator.yaml
   ```

   Important

   The cluster reboots and loses API capabilities while the Lifecycle Agent generates the seed image. Applying the `SeedGenerator` CR stops the `kubelet` and the CRI-O operations, then it starts the image generation.

**Verification**

* After the cluster recovers and it is available, you can check the status of the `SeedGenerator` CR by running the following command:

  ```
  $ oc get seedgenerator -o yaml
  ```

  The following example shows the output when the seed image generation is complete:

  ```
  status:
    conditions:
    - lastTransitionTime: "2024-02-13T21:24:26Z"
      message: Seed Generation completed
      observedGeneration: 1
      reason: Completed
      status: "False"
      type: SeedGenInProgress
    - lastTransitionTime: "2024-02-13T21:24:26Z"
      message: Seed Generation completed
      observedGeneration: 1
      reason: Completed
      status: "True"
      type: SeedGenCompleted
    observedGeneration: 1
  ```

  The `SeedGenCompleted` type indicates that the seed image generation is complete.

  Important

  After the seed image generation completes, do not use the seed cluster. Do not continue to run `oc` commands against the seed cluster or use it to manage managed clusters.

  If you access the seed cluster after generating the seed image, you can meet TLS certificate validation errors because the seed cluster certificates expire during seed image generation. If you need to generate another seed image, provision a new seed cluster.

#### [16.2.4. Creating ConfigMap objects for the image-based upgrade with the Lifecycle Agent](#cnf-image-based-upgrade-prep-resources) Copy linkLink copied to clipboard!

The Lifecycle Agent needs all your OADP resources, extra manifests, and custom catalog sources wrapped in a `ConfigMap` object to process them for the image-based upgrade.

##### [16.2.4.1. Creating OADP ConfigMap objects for the image-based upgrade with Lifecycle Agent](#cnf-image-based-upgrade-prep-oadp_cnf-non-gitops) Copy linkLink copied to clipboard!

Create your OADP resources that are used to back up and restore your resources during the upgrade.

**Prerequisites**

* You have generated a seed image from a compatible seed cluster.
* You have created OADP backup and restore resources.
* You have created a separate partition on the target cluster for the container images that is shared between stateroots. For more information, see "Configuring a shared container partition for the image-based upgrade".
* You have deployed a version of Lifecycle Agent that is compatible with the version used with the seed image.
* You have installed the OADP Operator, the `DataProtectionApplication` CR, and its secret on the target cluster.
* You have created an S3-compatible storage solution and a ready-to-use bucket with proper credentials configured. For more information, see "About installing OADP".

**Procedure**

1. Create the OADP `Backup` and `Restore` CRs for platform artifacts in the same namespace where the OADP Operator is installed, which is `openshift-adp`.

   1. If the target cluster is managed by RHACM, add the following `PlatformBackupRestore.yaml` file for backing up and restoring RHACM artifacts:

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        name: acm-klusterlet
        annotations:
          lca.openshift.io/apply-label: "apps/v1/deployments/open-cluster-management-agent/klusterlet,v1/secrets/open-cluster-management-agent/bootstrap-hub-kubeconfig,rbac.authorization.k8s.io/v1/clusterroles/klusterlet,v1/serviceaccounts/open-cluster-management-agent/klusterlet,scheduling.k8s.io/v1/priorityclasses/klusterlet-critical,rbac.authorization.k8s.io/v1/clusterroles/open-cluster-management:klusterlet-admin-aggregate-clusterrole,rbac.authorization.k8s.io/v1/clusterrolebindings/klusterlet,operator.open-cluster-management.io/v1/klusterlets/klusterlet,apiextensions.k8s.io/v1/customresourcedefinitions/klusterlets.operator.open-cluster-management.io,v1/secrets/open-cluster-management-agent/open-cluster-management-image-pull-credentials"
        labels:
          velero.io/storage-location: default
        namespace: openshift-adp
      spec:
        includedNamespaces:
        - open-cluster-management-agent
        includedClusterScopedResources:
        - klusterlets.operator.open-cluster-management.io
        - clusterroles.rbac.authorization.k8s.io
        - clusterrolebindings.rbac.authorization.k8s.io
        - priorityclasses.scheduling.k8s.io
        includedNamespaceScopedResources:
        - deployments
        - serviceaccounts
        - secrets
        excludedNamespaceScopedResources: []
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: acm-klusterlet
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "1"
      spec:
        backupName:
          acm-klusterlet
      ```

      Note

      If your `multiclusterHub` CR does not have `.spec.imagePullSecret` defined and the secret does not exist on the `open-cluster-management-agent` namespace in your hub cluster, remove `v1/secrets/open-cluster-management-agent/open-cluster-management-image-pull-credentials` from the `lca.openshift.io/apply-label` annotation.
   2. If you created persistent volumes on your cluster through LVM Storage, add the following `PlatformBackupRestoreLvms.yaml` file for LVM Storage artifacts:

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        labels:
          velero.io/storage-location: default
        name: lvmcluster
        namespace: openshift-adp
      spec:
        includedNamespaces:
          - openshift-storage
        includedNamespaceScopedResources:
          - lvmclusters
          - lvmvolumegroups
          - lvmvolumegroupnodestatuses
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: lvmcluster
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "2"
      spec:
        backupName:
          lvmcluster
      ```

      * The `lca.openshift.io/apply-wave` value must be lower than the values specified in the application `Restore` CRs.
2. If you need to restore applications after the upgrade, create the OADP `Backup` and `Restore` CRs for your application in the `openshift-adp` namespace.

   1. Create the OADP CRs for cluster-scoped application artifacts in the `openshift-adp` namespace, for example:

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        annotations:
          lca.openshift.io/apply-label: "apiextensions.k8s.io/v1/customresourcedefinitions/test.example.com,security.openshift.io/v1/securitycontextconstraints/test,rbac.authorization.k8s.io/v1/clusterroles/test-role,rbac.authorization.k8s.io/v1/clusterrolebindings/system:openshift:scc:test"
        name: backup-app-cluster-resources
        labels:
          velero.io/storage-location: default
        namespace: openshift-adp
      spec:
        includedClusterScopedResources:
        - customresourcedefinitions
        - securitycontextconstraints
        - clusterrolebindings
        - clusterroles
        excludedClusterScopedResources:
        - Namespace
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: test-app-cluster-resources
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "3"
      spec:
        backupName:
          backup-app-cluster-resources
      ```

      * Replace the example resource names in the `lca.openshift.io/apply-label` field with your actual resources.
      * The value in the `lca.openshift.io/apply-wave` field must be higher than the value in the platform `Restore` CRs and lower than the value in the application namespace-scoped `Restore` CR.
   2. Create the OADP CRs for your namespace-scoped application artifacts.

      When using LSO, see the following example OADP CRs:

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        labels:
          velero.io/storage-location: default
        name: backup-app
        namespace: openshift-adp
      spec:
        includedNamespaces:
        - test
        includedNamespaceScopedResources:
        - secrets
        - persistentvolumeclaims
        - deployments
        - statefulsets
        - configmaps
        - cronjobs
        - services
        - job
        - poddisruptionbudgets
        - <application_custom_resources>
        excludedClusterScopedResources:
        - persistentVolumes
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: test-app
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "4"
      spec:
        backupName:
          backup-app
      ```

      * Define custom resources for your application in the `includedNamespaceScopedResources` field.

      When using LVM Storage, see the following example OADP CRs:

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        labels:
          velero.io/storage-location: default
        name: backup-app
        namespace: openshift-adp
      spec:
        includedNamespaces:
        - test
        includedNamespaceScopedResources:
        - secrets
        - persistentvolumeclaims
        - deployments
        - statefulsets
        - configmaps
        - cronjobs
        - services
        - job
        - poddisruptionbudgets
        - <application_custom_resources>
        includedClusterScopedResources:
        - persistentVolumes
        - logicalvolumes.topolvm.io
        - volumesnapshotcontents
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: test-app
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "4"
      spec:
        backupName:
          backup-app
        restorePVs: true
        restoreStatus:
          includedResources:
          - logicalvolumes
      ```

      where:

      * `<application_custom_resources>`: Define custom resources for your application.
      * `persistentVolumes`: Required field.
      * `logicalvolumes.topolvm.io`: Required field.
      * `volumesnapshotcontents`: Optional if you use LVM Storage volume snapshots.
      * `restoreStatus.includedResources`: Required field for restoring logical volumes.

      Important

      The same version of the applications must function on both the current and the target release of OpenShift Container Platform.
3. Create the `ConfigMap` object for your OADP CRs by running the following command:

   ```
   $ oc create configmap oadp-cm-example --from-file=example-oadp-resources.yaml=<path_to_oadp_crs> -n openshift-adp
   ```
4. Patch the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade \
     -p='{"spec": {"oadpContent": [{"name": "oadp-cm-example", "namespace": "openshift-adp"}]}}' \
     --type=merge -n openshift-lifecycle-agent
   ```

##### [16.2.4.2. Creating ConfigMap objects of extra manifests for the image-based upgrade with Lifecycle Agent](#cnf-image-based-upgrade-prep-extramanifests_cnf-non-gitops) Copy linkLink copied to clipboard!

Create additional manifests that you want to apply to the target cluster.

Note

If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.

**Procedure**

1. Create a YAML file that contains your extra manifests, such as SR-IOV.

   **Example SR-IOV resources**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: "example-sriov-node-policy"
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: vfio-pci
     isRdma: false
     nicSelector:
       pfNames: [ens1f0]
     nodeSelector:
       node-role.kubernetes.io/master: ""
     mtu: 1500
     numVfs: 8
     priority: 99
     resourceName: example-sriov-node-policy
   ---
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: "example-sriov-network"
     namespace: openshift-sriov-network-operator
   spec:
     ipam: |-
       {
       }
     linkState: auto
     networkNamespace: sriov-namespace
     resourceName: example-sriov-node-policy
     spoofChk: "on"
     trust: "off"
   ```
2. Create the `ConfigMap` object by running the following command:

   ```
   $ oc create configmap example-extra-manifests-cm --from-file=example-extra-manifests.yaml=<path_to_extramanifest> -n openshift-lifecycle-agent
   ```
3. Patch the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade \
     -p='{"spec": {"extraManifests": [{"name": "example-extra-manifests-cm", "namespace": "openshift-lifecycle-agent"}]}}' \
     --type=merge -n openshift-lifecycle-agent
   ```

##### [16.2.4.3. Creating ConfigMap objects of custom catalog sources for the image-based upgrade with Lifecycle Agent](#cnf-image-based-upgrade-prep-catalogsources_cnf-non-gitops) Copy linkLink copied to clipboard!

You can keep your custom catalog sources after the upgrade by generating a `ConfigMap` object for your catalog sources and adding them to the `spec.extraManifest` field in the `ImageBasedUpgrade` CR. For more information about catalog sources, see "Catalog source".

**Procedure**

1. Create a YAML file that contains the `CatalogSource` CR:

   ```
   apiVersion: operators.coreos.com/v1
   kind: CatalogSource
   metadata:
     name: example-catalogsources
     namespace: openshift-marketplace
   spec:
     sourceType: grpc
     displayName: disconnected-redhat-operators
     image: quay.io/example-org/example-catalog:v1
   ```
2. Create the `ConfigMap` object by running the following command:

   ```
   $ oc create configmap example-catalogsources-cm --from-file=example-catalogsources.yaml=<path_to_catalogsource_cr> -n openshift-lifecycle-agent
   ```
3. Patch the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade \
     -p='{"spec": {"extraManifests": [{"name": "example-catalogsources-cm", "namespace": "openshift-lifecycle-agent"}]}}' \
     --type=merge -n openshift-lifecycle-agent
   ```

#### [16.2.5. Creating ConfigMap objects for the image-based upgrade with the Lifecycle Agent using GitOps ZTP](#ztp-image-based-upgrade-prep-resources) Copy linkLink copied to clipboard!

Create your OADP resources, extra manifests, and custom catalog sources wrapped in a `ConfigMap` object to prepare for the image-based upgrade.

##### [16.2.5.1. Creating OADP resources for the image-based upgrade with GitOps ZTP](#ztp-image-based-upgrade-prep-oadp_ztp-gitops) Copy linkLink copied to clipboard!

Prepare your OADP resources to restore your application after an upgrade.

**Prerequisites**

* You have provisioned one or more managed clusters with GitOps ZTP.
* You have logged in as a user with `cluster-admin` privileges.
* You have generated a seed image from a compatible seed cluster.
* You have created a separate partition on the target cluster for the container images that is shared between stateroots. For more information, see "Configuring a shared container partition between ostree stateroots when using GitOps ZTP".
* You have deployed a version of Lifecycle Agent that is compatible with the version used with the seed image.
* You have installed the OADP Operator, the `DataProtectionApplication` CR, and its secret on the target cluster.
* You have created an S3-compatible storage solution and a ready-to-use bucket with proper credentials configured. For more information, see "Installing and configuring the OADP Operator with GitOps ZTP".
* The `openshift-adp` namespace for the OADP `ConfigMap` object must exist on all managed clusters and the hub for the OADP `ConfigMap` to be generated and copied to the clusters.

**Procedure**

1. Ensure that your Git repository that you use with the ArgoCD policies application contains the following directory structure:

   ```
   ├── source-crs/
   │   ├── ibu/
   │   │    ├── ImageBasedUpgrade.yaml
   │   │    ├── PlatformBackupRestore.yaml
   │   │    ├── PlatformBackupRestoreLvms.yaml
   │   │    ├── PlatformBackupRestoreWithIBGU.yaml
   ├── ...
   ├── kustomization.yaml
   ```

   The `source-crs/ibu/PlatformBackupRestoreWithIBGU.yaml` file is provided in the ZTP container image.

   **PlatformBackupRestoreWithIBGU.yaml**

   ```
   apiVersion: velero.io/v1
   kind: Backup
   metadata:
     name: acm-klusterlet
     annotations:
       lca.openshift.io/apply-label: "apps/v1/deployments/open-cluster-management-agent/klusterlet,v1/secrets/open-cluster-management-agent/bootstrap-hub-kubeconfig,rbac.authorization.k8s.io/v1/clusterroles/klusterlet,v1/serviceaccounts/open-cluster-management-agent/klusterlet,scheduling.k8s.io/v1/priorityclasses/klusterlet-critical,rbac.authorization.k8s.io/v1/clusterroles/open-cluster-management:klusterlet-work:ibu-role,rbac.authorization.k8s.io/v1/clusterroles/open-cluster-management:klusterlet-admin-aggregate-clusterrole,rbac.authorization.k8s.io/v1/clusterrolebindings/klusterlet,operator.open-cluster-management.io/v1/klusterlets/klusterlet,apiextensions.k8s.io/v1/customresourcedefinitions/klusterlets.operator.open-cluster-management.io,v1/secrets/open-cluster-management-agent/open-cluster-management-image-pull-credentials"
     labels:
       velero.io/storage-location: default
     namespace: openshift-adp
   spec:
     includedNamespaces:
     - open-cluster-management-agent
     includedClusterScopedResources:
     - klusterlets.operator.open-cluster-management.io
     - clusterroles.rbac.authorization.k8s.io
     - clusterrolebindings.rbac.authorization.k8s.io
     - priorityclasses.scheduling.k8s.io
     includedNamespaceScopedResources:
     - deployments
     - serviceaccounts
     - secrets
     excludedNamespaceScopedResources: []
   ---
   apiVersion: velero.io/v1
   kind: Restore
   metadata:
     name: acm-klusterlet
     namespace: openshift-adp
     labels:
       velero.io/storage-location: default
     annotations:
       lca.openshift.io/apply-wave: "1"
   spec:
     backupName:
       acm-klusterlet
   ```

   Note

   If your `multiclusterHub` CR does not have `.spec.imagePullSecret` defined and the secret does not exist on the `open-cluster-management-agent` namespace in your hub cluster, remove `v1/secrets/open-cluster-management-agent/open-cluster-management-image-pull-credentials` from the `metadata.annotations.lca.openshift.io/apply-label` value in the `acm-klusterlet` `Backup` CR.

   Note

   If you perform the image-based upgrade directly on managed clusters, use the `PlatformBackupRestore.yaml` file.

   If you use LVM Storage to create persistent volumes, you can use the `source-crs/ibu/PlatformBackupRestoreLvms.yaml` provided in the ZTP container image to back up your LVM Storage resources.

   **PlatformBackupRestoreLvms.yaml**

   ```
   apiVersion: velero.io/v1
   kind: Backup
   metadata:
     labels:
       velero.io/storage-location: default
     name: lvmcluster
     namespace: openshift-adp
   spec:
     includedNamespaces:
       - openshift-storage
     includedNamespaceScopedResources:
       - lvmclusters
       - lvmvolumegroups
       - lvmvolumegroupnodestatuses
   ---
   apiVersion: velero.io/v1
   kind: Restore
   metadata:
     name: lvmcluster
     namespace: openshift-adp
     labels:
       velero.io/storage-location: default
     annotations:
       lca.openshift.io/apply-wave: "2"
   spec:
     backupName:
       lvmcluster
   ```

   * The `lca.openshift.io/apply-wave` value must be lower than the values specified in the application `Restore` CRs.
2. If you need to restore applications after the upgrade, create the OADP `Backup` and `Restore` CRs for your application in the `openshift-adp` namespace:

   1. Create the OADP CRs for cluster-scoped application artifacts in the `openshift-adp` namespace:

      **Example OADP CRs for cluster-scoped application artifacts for LSO and LVM Storage**

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        annotations:
          lca.openshift.io/apply-label: "apiextensions.k8s.io/v1/customresourcedefinitions/test.example.com,security.openshift.io/v1/securitycontextconstraints/test,rbac.authorization.k8s.io/v1/clusterroles/test-role,rbac.authorization.k8s.io/v1/clusterrolebindings/system:openshift:scc:test"
        name: backup-app-cluster-resources
        labels:
          velero.io/storage-location: default
        namespace: openshift-adp
      spec:
        includedClusterScopedResources:
        - customresourcedefinitions
        - securitycontextconstraints
        - clusterrolebindings
        - clusterroles
        excludedClusterScopedResources:
        - Namespace
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: test-app-cluster-resources
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "3"
      spec:
        backupName:
          backup-app-cluster-resources
      ```

      * Replace the example resource names in the `lca.openshift.io/apply-label` field with your actual resources.
      * The value in the `lca.openshift.io/apply-wave` field must be higher than the value in the platform `Restore` CRs and lower than the value in the application namespace-scoped `Restore` CR.
   2. Create the OADP CRs for your namespace-scoped application artifacts in the `source-crs/custom-crs` directory:

      **Example OADP CRs namespace-scoped application artifacts when LSO is used**

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        labels:
          velero.io/storage-location: default
        name: backup-app
        namespace: openshift-adp
      spec:
        includedNamespaces:
        - test
        includedNamespaceScopedResources:
        - secrets
        - persistentvolumeclaims
        - deployments
        - statefulsets
        - configmaps
        - cronjobs
        - services
        - job
        - poddisruptionbudgets
        - <application_custom_resources>
        excludedClusterScopedResources:
        - persistentVolumes
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: test-app
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "4"
      spec:
        backupName:
          backup-app
      ```

      * Define custom resources for your application in the `includedNamespaceScopedResources` field.

      **Example OADP CRs namespace-scoped application artifacts when LVM Storage is used**

      ```
      apiVersion: velero.io/v1
      kind: Backup
      metadata:
        labels:
          velero.io/storage-location: default
        name: backup-app
        namespace: openshift-adp
      spec:
        includedNamespaces:
        - test
        includedNamespaceScopedResources:
        - secrets
        - persistentvolumeclaims
        - deployments
        - statefulsets
        - configmaps
        - cronjobs
        - services
        - job
        - poddisruptionbudgets
        - <application_custom_resources>
        includedClusterScopedResources:
        - persistentVolumes
        - logicalvolumes.topolvm.io
        - volumesnapshotcontents
      ---
      apiVersion: velero.io/v1
      kind: Restore
      metadata:
        name: test-app
        namespace: openshift-adp
        labels:
          velero.io/storage-location: default
        annotations:
          lca.openshift.io/apply-wave: "4"
      spec:
        backupName:
          backup-app
        restorePVs: true
        restoreStatus:
          includedResources:
          - logicalvolumes
      ```

      where:

      * `<application_custom_resources>`: Define custom resources for your application.
      * `persistentVolumes`: Required field.
      * `logicalvolumes.topolvm.io`: Required field.
      * `volumesnapshotcontents`: Optional if you use LVM Storage volume snapshots.
      * `restoreStatus.includedResources`: Required field for restoring logical volumes.

      Important

      The same version of the applications must function on both the current and the target release of OpenShift Container Platform.
3. Create a `kustomization.yaml` with the following content:

   ```
   apiVersion: kustomize.config.k8s.io/v1beta1
   kind: Kustomization

   configMapGenerator:
   - files:
     - source-crs/ibu/PlatformBackupRestoreWithIBGU.yaml
     #- source-crs/custom-crs/ApplicationClusterScopedBackupRestore.yaml
     #- source-crs/custom-crs/ApplicationApplicationBackupRestoreLso.yaml
     name: oadp-cm
     namespace: openshift-adp
   generatorOptions:
     disableNameSuffixHash: true
   ```

   where:

   `configMapGenerator`
   :   Creates the `oadp-cm` `ConfigMap` object on the hub cluster with `Backup` and `Restore` CRs.

   `namespace: openshift-adp`
   :   The namespace must exist on all managed clusters and the hub for the OADP `ConfigMap` to be generated and copied to the clusters.
4. Push the changes to your Git repository.

##### [16.2.5.2. Labeling extra manifests for the image-based upgrade with GitOps ZTP](#ztp-image-based-upgrade-prep-label-extramanifests_ztp-gitops) Copy linkLink copied to clipboard!

Label your extra manifests so that the Lifecycle Agent can extract resources that are labeled with the `lca.openshift.io/target-ocp-version: <target_version>` label.

**Prerequisites**

* You have provisioned one or more managed clusters with GitOps ZTP.
* You have logged in as a user with `cluster-admin` privileges.
* You have generated a seed image from a compatible seed cluster.
* You have created a separate partition on the target cluster for the container images that is shared between stateroots. For more information, see "Configuring a shared container directory between ostree stateroots when using GitOps ZTP".
* You have deployed a version of Lifecycle Agent that is compatible with the version used with the seed image.

**Procedure**

1. Label your required extra manifests with the `lca.openshift.io/target-ocp-version: <target_version>` label in your existing site `PolicyGenTemplate` CR:

   ```
   apiVersion: ran.openshift.io/v1
   kind: PolicyGenTemplate
   metadata:
     name: example-sno
   spec:
     bindingRules:
       sites: "example-sno"
       du-profile: "4.15"
     mcp: "master"
     sourceFiles:
       - fileName: SriovNetwork.yaml
         policyName: "config-policy"
         metadata:
           name: "sriov-nw-du-fh"
           labels:
             lca.openshift.io/target-ocp-version: "4.15"
         spec:
           resourceName: du_fh
           vlan: 140
       - fileName: SriovNetworkNodePolicy.yaml
         policyName: "config-policy"
         metadata:
           name: "sriov-nnp-du-fh"
           labels:
             lca.openshift.io/target-ocp-version: "4.15"
         spec:
           deviceType: netdevice
           isRdma: false
           nicSelector:
             pfNames: ["ens5f0"]
           numVfs: 8
           priority: 10
           resourceName: du_fh
       - fileName: SriovNetwork.yaml
         policyName: "config-policy"
         metadata:
           name: "sriov-nw-du-mh"
           labels:
             lca.openshift.io/target-ocp-version: "4.15"
         spec:
           resourceName: du_mh
           vlan: 150
       - fileName: SriovNetworkNodePolicy.yaml
         policyName: "config-policy"
         metadata:
           name: "sriov-nnp-du-mh"
           labels:
             lca.openshift.io/target-ocp-version: "4.15"
         spec:
           deviceType: vfio-pci
           isRdma: false
           nicSelector:
             pfNames: ["ens7f0"]
           numVfs: 8
           priority: 10
           resourceName: du_mh
       - fileName: DefaultCatsrc.yaml
         policyName: "config-policy"
         metadata:
           name: default-cat-source
           namespace: openshift-marketplace
           labels:
               lca.openshift.io/target-ocp-version: "4.15"
         spec:
             displayName: default-cat-source
             image: quay.io/example-org/example-catalog:v1
   ```

   where:

   `lca.openshift.io/target-ocp-version`
   :   Ensure that this label matches either the y-stream or the z-stream of the target OpenShift Container Platform version that is specified in the `spec.seedImageRef.version` field of the `ImageBasedUpgrade` CR. The Lifecycle Agent only applies the CRs that match the specified version.

   `DefaultCatsrc.yaml`
   :   If you do not want to use custom catalog sources, remove this entry.
2. Push the changes to your Git repository.

#### [16.2.6. Configuring the automatic image cleanup of the container storage disk](#cnf-image-based-upgrade-configure-auto-image-cleanup) Copy linkLink copied to clipboard!

Configure when the Lifecycle Agent cleans up unpinned images in the `Prep` stage by setting a minimum threshold for available storage space through annotations. The default container storage disk usage threshold is 50%.

The Lifecycle Agent does not delete images that are pinned in CRI-O or are currently used. The Operator selects the images for deletion by starting with dangling images and then sorting the images from oldest to newest that is determined by the image `Created` timestamp.

##### [16.2.6.1. Configuring the automatic image cleanup of the container storage disk](#ztp-image-based-upgrade-configure-threshold_auto-cleanup) Copy linkLink copied to clipboard!

Configure the minimum threshold for available storage space through annotations.

**Prerequisites**

* You have created an `ImageBasedUpgrade` CR.

**Procedure**

1. Increase the threshold to 65% by running the following command:

   ```
   $ oc -n openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/disk-usage-threshold-percent='65'
   ```
2. (Optional) Remove the threshold override by running the following command:

   ```
   $ oc -n  openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/disk-usage-threshold-percent-
   ```

##### [16.2.6.2. Disable the automatic image cleanup of the container storage disk](#ztp-image-based-upgrade-disable-container-storage-image-cleanup_auto-cleanup) Copy linkLink copied to clipboard!

Disable the automatic image cleanup threshold.

**Procedure**

1. Disable the automatic image cleanup by running the following command:

   ```
   $ oc -n openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/on-prep='Disabled'
   ```
2. (Optional) Enable automatic image cleanup again by running the following command:

   ```
   $ oc -n  openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/on-prep-
   ```

### [16.3. Performing an image-based upgrade for single-node OpenShift clusters with the Lifecycle Agent](#cnf-image-based-upgrade) Copy linkLink copied to clipboard!

You can use the Lifecycle Agent to do a manual image-based upgrade of a single-node OpenShift cluster.

When you deploy the Lifecycle Agent on a cluster, an `ImageBasedUpgrade` CR is automatically created. You update this CR to specify the image repository of the seed image and to move through the different stages.

#### [16.3.1. Moving to the Prep stage of the image-based upgrade with Lifecycle Agent](#ztp-image-based-upgrade-prep_cnf-non-gitops) Copy linkLink copied to clipboard!

When you deploy the Lifecycle Agent on a cluster, the Lifecycle Agent automatically creates an `ImageBasedUpgrade` custom resource (CR).

After you create all the resources that you need during the upgrade, you can move on to the `Prep` stage. For more information, see the "Creating ConfigMap objects for the image-based upgrade with Lifecycle Agent" section.

Note

In a disconnected environment, if the seed cluster’s release image registry is different from the target cluster’s release image registry, you must create an `ImageDigestMirrorSet` (IDMS) resource to configure alternative mirrored repository locations. For more information, see "Configuring image registry repository mirroring".

You can retrieve the release registry used in the seed image by running the following command:

```
$ skopeo inspect docker://<imagename> | jq -r '.Labels."com.openshift.lifecycle-agent.seed_cluster_info" | fromjson | .release_registry'
```

**Prerequisites**

* You have created resources to back up and restore your clusters.

**Procedure**

1. Check that you have patched your `ImageBasedUpgrade` CR:

   ```
   apiVersion: lca.openshift.io/v1
   kind: ImageBasedUpgrade
   metadata:
     name: upgrade
   spec:
     stage: Idle
     seedImageRef:
       version: <target_version>
       image: <seed_container_image>
       pullSecretRef: <seed_pull_secret>
     autoRollbackOnFailure: {}
       initMonitorTimeoutSeconds: <initMonitorTimeoutSeconds>
     extraManifests:
     - name: example-extra-manifests-cm
       namespace: openshift-lifecycle-agent
     - name: example-catalogsources-cm
       namespace: openshift-lifecycle-agent
     oadpContent:
     - name: oadp-cm-example
       namespace: openshift-adp
   ```

   where:

   `<target_version>`
   :   Target platform version. The value must match the version of the seed image.

   `<seed_container_image>`
   :   Repository where the target cluster can pull the seed image from.

   `<seed_pull_secret>`
   :   Reference to a secret with credentials to pull container images if the images are in a private registry.

   `<initMonitorTimeoutSeconds>`
   :   Optional: Time frame in seconds to roll back if the upgrade does not complete within that time frame after the first reboot. If not defined or set to `0`, the Lifecycle Agent uses the default value of `1800` seconds (30 minutes).

   `extraManifests`
   :   Optional: List of `ConfigMap` resources. These resources contain your custom catalog sources to retain after the upgrade and any extra manifests that the seed image does not include.

   `oadpContent`
   :   List of `ConfigMap` resources that contain the OADP `Backup` and `Restore` CRs.
2. To start the `Prep` stage, change the value of the `stage` field to `Prep` in the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade -p='{"spec": {"stage": "Prep"}}' --type=merge -n openshift-lifecycle-agent
   ```

   If you include `ConfigMap` objects for OADP resources and extra manifests, Lifecycle Agent validates the specified `ConfigMap` objects during the `Prep` stage.

   The following issues might occur:

   * Validation warnings or errors if the Lifecycle Agent detects any issues with the `extraManifests` parameters.
   * Validation errors if the Lifecycle Agent detects any issues with the `oadpContent` parameters.

   Validation warnings do not block the `Upgrade` stage but you must decide if it is safe to proceed with the upgrade. These warnings, for example missing custom resource definitions (CRDs), namespaces, or dry run failures, update the `status.conditions` for the `Prep` stage and `annotation` fields in the `ImageBasedUpgrade` CR with details about the warning. The following example shows these details:

   ```
   # ...
   metadata:
   annotations:
     extra-manifest.lca.openshift.io/validation-warning: '...'
   # ...
   ```

   However, validation errors, such as adding `MachineConfig` or Operator manifests to extra manifests, cause the `Prep` stage to fail and block the `Upgrade` stage.

   When the validations pass, the cluster creates a new `ostree` stateroot, which involves pulling and unpacking the seed image, and running host-level commands. Finally, the Lifecycle Agent precaches all the required images on the target cluster.

**Verification**

* Check the status of the `ImageBasedUpgrade` CR by running the following command:

  ```
  $ oc get ibu -o yaml
  ```

  The following example shows a successful `Prep` stage:

  ```
    conditions:
    - lastTransitionTime: "2024-01-01T09:00:00Z"
      message: In progress
      observedGeneration: 13
      reason: InProgress
      status: "False"
      type: Idle
    - lastTransitionTime: "2024-01-01T09:00:00Z"
      message: Prep completed
      observedGeneration: 13
      reason: Completed
      status: "False"
      type: PrepInProgress
    - lastTransitionTime: "2024-01-01T09:00:00Z"
      message: Prep stage completed successfully
      observedGeneration: 13
      reason: Completed
      status: "True"
      type: PrepCompleted
    observedGeneration: 13
    validNextStages:
    - Idle
    - Upgrade
  ```

#### [16.3.2. Moving to the Upgrade stage of the image-based upgrade with Lifecycle Agent](#cnf-image-based-upgrade-with-backup_cnf-non-gitops) Copy linkLink copied to clipboard!

After you generate the seed image and complete the `Prep` stage, you can upgrade the target cluster. During the upgrade process, the OADP Operator creates a backup of the artifacts specified in the OADP custom resources (CRs), then the Lifecycle Agent upgrades the cluster.

If the upgrade fails or stops, the Lifecycle Agent initiates an automatic rollback. If you have an issue after the upgrade, you can perform a manual rollback. For more information about manual rollback, see "Moving to the Rollback stage of the image-based upgrade with Lifecycle Agent".

**Prerequisites**

* You have completed the `Prep` stage.

**Procedure**

1. To move to the `Upgrade` stage, change the value of the `stage` field to `Upgrade` in the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade -p='{"spec": {"stage": "Upgrade"}}' --type=merge
   ```
2. Check the status of the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc get ibu -o yaml
   ```

   The following example shows an upgrade in progress:

   ```
   status:
     conditions:
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: In progress
       observedGeneration: 5
       reason: InProgress
       status: "False"
       type: Idle
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: Prep completed
       observedGeneration: 5
       reason: Completed
       status: "False"
       type: PrepInProgress
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: Prep completed successfully
       observedGeneration: 5
       reason: Completed
       status: "True"
       type: PrepCompleted
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: |-
         Waiting for system to stabilize: one or more health checks failed
           - one or more ClusterOperators not yet ready: authentication
           - one or more MachineConfigPools not yet ready: master
           - one or more ClusterServiceVersions not yet ready: sriov-fec.v2.8.0
       observedGeneration: 1
       reason: InProgress
       status: "True"
       type: UpgradeInProgress
     observedGeneration: 1
     rollbackAvailabilityExpiration: "2024-05-19T14:01:52Z"
     validNextStages:
     - Rollback
   ```

   The OADP Operator creates a backup of the data specified in the OADP `Backup` and `Restore` CRs and the target cluster reboots.
3. Monitor the status of the CR by running the following command:

   ```
   $ oc get ibu -o yaml
   ```
4. After the upgrade, complete the changes by patching the value of the `stage` field to `Idle` in the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade -p='{"spec": {"stage": "Idle"}}' --type=merge
   ```

   Important

   You cannot roll back the changes once you move to the `Idle` stage after an upgrade.

   The Lifecycle Agent deletes all resources created during the upgrade process.
5. You can remove the OADP Operator and its configuration files after a successful upgrade. For more information, see "Deleting Operators from a cluster".

**Verification**

1. Check the status of the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc get ibu -o yaml
   ```

   The following example shows a completed upgrade:

   ```
   status:
     conditions:
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: In progress
       observedGeneration: 5
       reason: InProgress
       status: "False"
       type: Idle
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: Prep completed
       observedGeneration: 5
       reason: Completed
       status: "False"
       type: PrepInProgress
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: Prep completed successfully
       observedGeneration: 5
       reason: Completed
       status: "True"
       type: PrepCompleted
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: Upgrade completed
       observedGeneration: 1
       reason: Completed
       status: "False"
       type: UpgradeInProgress
     - lastTransitionTime: "2024-01-01T09:00:00Z"
       message: Upgrade completed
       observedGeneration: 1
       reason: Completed
       status: "True"
       type: UpgradeCompleted
     observedGeneration: 1
     rollbackAvailabilityExpiration: "2024-01-01T09:00:00Z"
     validNextStages:
     - Idle
     - Rollback
   ```
2. Check the status of the cluster restoration by running the following command:

   ```
   $ oc get restores -n openshift-adp -o custom-columns=NAME:.metadata.name,Status:.status.phase,Reason:.status.failureReason
   ```

   The following example shows completed restores:

   ```
   NAME             Status      Reason
   acm-klusterlet   Completed   <none>
   apache-app       Completed   <none>
   localvolume      Completed   <none>
   ```

   Note

   The `acm-klusterlet` is specific to RHACM environments only.

#### [16.3.3. Moving to the Rollback stage of the image-based upgrade with Lifecycle Agent](#cnf-image-based-upgrade-rollback_cnf-non-gitops) Copy linkLink copied to clipboard!

The Lifecycle Agent initiates an automatic rollback if the upgrade does not complete within the time frame specified in the `initMonitorTimeoutSeconds` field after rebooting, as shown in the following example:

```
apiVersion: lca.openshift.io/v1
kind: ImageBasedUpgrade
metadata:
  name: upgrade
spec:
  stage: Idle
  seedImageRef:
    version: 4.15.2
    image: <seed_container_image>
  autoRollbackOnFailure: {}
#    initMonitorTimeoutSeconds: <initMonitorTimeoutSeconds>
# ...
```

where:

`<initMonitorTimeoutSeconds>`
:   Optional: The time frame in seconds to roll back if the upgrade does not complete within that time frame after the first reboot. If not defined or set to `0`, the Lifecycle Agent uses the default value of `1800` seconds (30 minutes).

You can manually roll back the changes if you see unresolvable issues after an upgrade.

**Prerequisites**

* You have logged into the hub cluster as a user with `cluster-admin` privileges.
* You ensured that the control plane certificates on the original stateroot are valid. If the certificates expired, see "Recovering from expired control plane certificates".

Warning

If you choose to upgrade a recently installed single-node OpenShift cluster for example, for testing purposes, you have a limited rollback time frame of 24 hours or less. You can verify the rollback time by checking the `rollbackAvailabilityExpiration` field of the `ImageBasedUpgrade` custom resource.

**Procedure**

1. To move to the rollback stage, patch the value of the `stage` field to `Rollback` in the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade -p='{"spec": {"stage": "Rollback"}}' --type=merge
   ```

   The Lifecycle Agent reboots the cluster with the previously installed version of OpenShift Container Platform and restores the applications.
2. After reviewing the changes, complete the rollback by patching the value of the `stage` field to `Idle` in the `ImageBasedUpgrade` CR by running the following command:

   ```
   $ oc patch imagebasedupgrades.lca.openshift.io upgrade -p='{"spec": {"stage": "Idle"}}' --type=merge -n openshift-lifecycle-agent
   ```

   Warning

   If you move to the `Idle` stage after a rollback, the Lifecycle Agent cleans up resources that you can use to troubleshoot a failed upgrade.

#### [16.3.4. Troubleshooting image-based upgrades with Lifecycle Agent](#cnf-image-based-upgrade-troubleshooting_cnf-non-gitops) Copy linkLink copied to clipboard!

Perform troubleshooting steps on the managed clusters to resolve any issues.

Important

If you are using the `ImageBasedGroupUpgrade` CR to upgrade your clusters, ensure that you update the `lcm.openshift.io/ibgu-<stage>-completed` or `lcm.openshift.io/ibgu-<stage>-failed` cluster labels properly after performing troubleshooting or recovery steps on the managed clusters. This ensures that the TALM continues to manage the image-based upgrade for the cluster.

##### [16.3.4.1. Collecting logs](#cnf-image-based-upgrade-troubleshooting-must-gather_cnf-non-gitops) Copy linkLink copied to clipboard!

You can use the `oc adm must-gather` CLI to collect information for debugging and troubleshooting.

To collect data about the Operators, run the following command:

```
$  oc adm must-gather \
  --dest-dir=must-gather/tmp \
  --image=$(oc -n openshift-lifecycle-agent get deployment.apps/lifecycle-agent-controller-manager -o jsonpath='{.spec.template.spec.containers[?(@.name == "manager")].image}') \
  --image=quay.io/konveyor/oadp-must-gather:latest \//
  --image=quay.io/openshift/origin-must-gather:latest
```

+ Where:

+ \* `--image=quay.io/konveyor/oadp-must-gather:latest`: Optional: Add this option if you need to gather more information from the OADP Operator. \* `--image=quay.io/openshift/origin-must-gather:latest`: Optional: Add this option if you need to gather more information from the SR-IOV Operator.

##### [16.3.4.2. AbortFailed or FinalizeFailed error](#cnf-image-based-upgrade-troubleshooting-manual-cleanup_cnf-non-gitops) Copy linkLink copied to clipboard!

Issue
:   During the finalization stage or when you stop the process at the `Prep` stage, Lifecycle Agent cleans up the following resources:

    * Stateroot that is no longer required
    * Precaching resources
    * OADP CRs
    * `ImageBasedUpgrade` CR

    If the Lifecycle Agent fails to clean up these resources, it transitions to the `AbortFailed` or `FinalizeFailed` states. The condition message and log show the steps that failed, as shown in the following example:

    Example error message:

    ```
    message: failed to delete all the backup CRs. Perform cleanup manually then add 'lca.openshift.io/manual-cleanup-done' annotation to ibu CR to transition back to Idle
          observedGeneration: 5
          reason: AbortFailed
          status: "False"
          type: Idle
    ```

Resolution
:   1. Inspect the logs to find the reason for failure.
    2. To prompt Lifecycle Agent to retry the cleanup, add the `lca.openshift.io/manual-cleanup-done` annotation to the `ImageBasedUpgrade` CR.

       After observing this annotation, Lifecycle Agent retries the cleanup and, if it is successful, the `ImageBasedUpgrade` stage transitions to `Idle`.

       If the cleanup fails again, you can manually clean up the resources.

##### [16.3.4.3. Cleaning up stateroot manually](#cnf-image-based-upgrade-troubleshooting-stateroot_cnf-non-gitops) Copy linkLink copied to clipboard!

Issue
:   Stopping at the `Prep` stage, Lifecycle Agent cleans up the new stateroot. When finalizing after a successful upgrade or a rollback, Lifecycle Agent cleans up the old stateroot. If this step fails, you must inspect the logs to decide why the failure occurred.

Resolution
:   1. Check if there are any existing deployments in the stateroot by running the following command:

       ```
       $ ostree admin status
       ```
    2. If there are any, clean up the existing deployment by running the following command:

       ```
       $ ostree admin undeploy <index_of_deployment>
       ```
    3. After cleaning up all the deployments of the stateroot, wipe the stateroot directory by running the following commands:

       Warning

       Ensure that the booted deployment is not in this stateroot.

       ```
       $ stateroot="<stateroot_to_delete>"
       ```

       ```
       $ unshare -m /bin/sh -c "mount -o remount,rw /sysroot && rm -rf /sysroot/ostree/deploy/${stateroot}"
       ```

##### [16.3.4.4. Cleaning up OADP resources manually](#cnf-image-based-upgrade-troubleshooting-oadp-resources_cnf-non-gitops) Copy linkLink copied to clipboard!

Issue
:   Automatic cleanup of OADP resources can fail due to connection issues between Lifecycle Agent and the S3 backend. By restoring the connection and adding the `lca.openshift.io/manual-cleanup-done` annotation, the Lifecycle Agent can successfully cleanup backup resources.

Resolution

1. Check the backend connectivity by running the following command:

   ```
   $ oc get backupstoragelocations.velero.io -n openshift-adp
   ```

   The following example shows successful backend connectivity:

   ```
   NAME                          PHASE       LAST VALIDATED   AGE   DEFAULT
   dataprotectionapplication-1   Available   33s              8d    true
   ```
2. Remove all backup resources and then add the `lca.openshift.io/manual-cleanup-done` annotation to the `ImageBasedUpgrade` CR.

##### [16.3.4.5. LVM Storage volume contents not restored](#cnf-image-based-upgrade-troubleshooting-lvms_cnf-non-gitops) Copy linkLink copied to clipboard!

When you use LVM Storage to configure dynamic persistent volume storage, LVM Storage might not restore the persistent volume contents if you have configured it incorrectly.

##### [16.3.4.6. Missing LVM Storage-related fields in Backup CR](#cnf-image-based-upgrade-troubleshooting-lvms-backup_cnf-non-gitops) Copy linkLink copied to clipboard!

Issue
:   Your `Backup` CRs might be missing fields that you need to restore your persistent volumes. You can check for events in your application pod to decide if you have this issue by running the following:

    ```
    $ oc describe pod <your_app_name>
    ```

    The following example output shows a pod failing due to missing LVM Storage-related fields in the `Backup` CR:

    ```
    Events:
      Type     Reason            Age                From               Message
      ----     ------            ----               ----               -------
      Warning  FailedScheduling  58s (x2 over 66s)  default-scheduler  0/1 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/1 nodes are available: 1 Preemption is not helpful for scheduling..
      Normal   Scheduled         56s                default-scheduler  Successfully assigned default/db-1234 to sno1.example.lab
      Warning  FailedMount       24s (x7 over 55s)  kubelet            MountVolume.SetUp failed for volume "pvc-1234" : rpc error: code = Unknown desc = VolumeID is not found
    ```

Resolution
:   You must include `logicalvolumes.topolvm.io` in the application `Backup` CR. Without this resource, the application restores its persistent volume claims and persistent volume manifests correctly, however, the `logicalvolume` associated with this persistent volume is not restored properly after pivot. The following example shows a correctly configured `Backup` CR:

    ```
    apiVersion: velero.io/v1
    kind: Backup
    metadata:
      labels:
        velero.io/storage-location: default
      name: small-app
      namespace: openshift-adp
    spec:
      includedNamespaces:
      - test
      includedNamespaceScopedResources:
      - secrets
      - persistentvolumeclaims
      - deployments
      - statefulsets
      includedClusterScopedResources:
      - persistentVolumes
      - volumesnapshotcontents
      - logicalvolumes.topolvm.io
    ```

    To restore the persistent volumes for your application, you must configure the `includedClusterScopedResources` section as shown.

##### [16.3.4.7. Missing LVM Storage-related fields in Restore CR](#cnf-image-based-upgrade-troubleshooting-lvms-restore_cnf-non-gitops) Copy linkLink copied to clipboard!

Issue
:   LVM Storage restores the expected resources for the applications but it does not preserve the persistent volume contents after upgrading.

    1. List the persistent volumes for you applications by running the following command before pivot:

       ```
       $ oc get pv,pvc,logicalvolumes.topolvm.io -A
       ```

       The following shows the output before pivot:

       ```
       NAME                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM            STORAGECLASS   REASON   AGE
       persistentvolume/pvc-1234   1Gi        RWO            Retain           Bound    default/pvc-db   lvms-vg1                4h45m

       NAMESPACE   NAME                           STATUS   VOLUME     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
       default     persistentvolumeclaim/pvc-db   Bound    pvc-1234   1Gi        RWO            lvms-vg1       4h45m

       NAMESPACE   NAME                                AGE
                   logicalvolume.topolvm.io/pvc-1234   4h45m
       ```
    2. List the persistent volumes for you applications by running the following command after pivot:

       ```
       $ oc get pv,pvc,logicalvolumes.topolvm.io -A
       ```

       The following shows the output after pivot:

       ```
       NAME                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM            STORAGECLASS   REASON   AGE
       persistentvolume/pvc-1234   1Gi        RWO            Delete           Bound    default/pvc-db   lvms-vg1                19s

       NAMESPACE   NAME                           STATUS   VOLUME     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
       default     persistentvolumeclaim/pvc-db   Bound    pvc-1234   1Gi        RWO            lvms-vg1       19s

       NAMESPACE   NAME                                AGE
                   logicalvolume.topolvm.io/pvc-1234   18s
       ```

Resolution
:   The reason for this issue is that the `logicalvolume` status is not preserved in the `Restore` CR. This status is important because Velero requires this status to reference the volumes that you must preserve after pivoting. You must include the following fields in the application `Restore` CR, as shown in the following example:

    ```
    apiVersion: velero.io/v1
    kind: Restore
    metadata:
      name: sample-vote-app
      namespace: openshift-adp
      labels:
        velero.io/storage-location: default
      annotations:
        lca.openshift.io/apply-wave: "3"
    spec:
      backupName:
        sample-vote-app
      restorePVs: <restore_pvs>
      restoreStatus:
        includedResources:
          - logicalvolumes
    ```

    where:

`<restore_pvs>`
:   To preserve the persistent volumes for your application, you must set `restorePVs` to `true`.

`restoreStatus`
:   To preserve the persistent volumes for your application, you must configure this field as shown.

##### [16.3.4.8. Debugging failed Backup and Restore CRs](#cnf-image-based-upgrade-troubleshooting-debugging-oadp-crs_cnf-non-gitops) Copy linkLink copied to clipboard!

Issue
:   The backup or restoration of artifacts failed.

Resolution
:   You can debug `Backup` and `Restore` CRs and retrieve logs with the OADP CLI. The OADP CLI offers more detailed information than the OpenShift CLI tool.

    1. Describe the `Backup` CR that has errors by running the following command:

       ```
       $ oc oadp backup describe backup-acm-klusterlet -n openshift-adp --details
       ```
    2. Describe the `Restore` CR that has errors by running the following command:

       ```
       $ oc oadp restore describe restore-acm-klusterlet -n openshift-adp --details
       ```
    3. Download the backed up resources to a local directory by running the following command:

       ```
       $ oc oadp backup download backup-acm-klusterlet -n openshift-adp -o ~/backup-acm-klusterlet.tar.gz
       ```

### [16.4. Performing an image-based upgrade for single-node OpenShift clusters using GitOps ZTP](#ztp-image-based-upgrade) Copy linkLink copied to clipboard!

You can use a single resource on the hub cluster, the `ImageBasedGroupUpgrade` custom resource (CR), to manage an imaged-based upgrade on a selected group of managed clusters through all stages. Topology Aware Lifecycle Manager (TALM) reconciles the `ImageBasedGroupUpgrade` CR and creates the underlying resources to complete the defined stage transitions, either in a manually controlled or a fully automated upgrade flow.

For more information about the image-based upgrade, see "Understanding the image-based upgrade for single-node OpenShift clusters".

#### [16.4.1. Managing the image-based upgrade at scale using the ImageBasedGroupUpgrade CR on the hub](#ztp-image-based-upgrade-concept_ztp-gitops) Copy linkLink copied to clipboard!

The `ImageBasedGroupUpgrade` CR combines the `ImageBasedUpgrade` and `ClusterGroupUpgrade` APIs. For example, you can define the cluster selection and rollout strategy with the `ImageBasedGroupUpgrade` API in the same way as the `ClusterGroupUpgrade` API. The stage transitions are different from the `ImageBasedUpgrade` API. You can use the `ImageBasedGroupUpgrade` API to combine several stage transitions, also called actions, into one step that share one rollout strategy.

**Example 16.1. Example `ImageBasedGroupUpgrade.yaml`**

```
apiVersion: lcm.openshift.io/v1alpha1
kind: ImageBasedGroupUpgrade
metadata:
  name: <filename>
  namespace: default
spec:
  clusterLabelSelectors:
    - matchExpressions:
      - key: name
        operator: In
        values:
        - spoke1
        - spoke4
        - spoke6
  ibuSpec:
    seedImageRef:
      image: quay.io/seed/image:4.22.0
      version: 4.22.0
      pullSecretRef:
        name: "<seed_pull_secret>"
    extraManifests:
      - name: example-extra-manifests
        namespace: openshift-lifecycle-agent
    oadpContent:
      - name: oadp-cm
        namespace: openshift-adp
  plan:
    - actions: ["Prep", "Upgrade", "FinalizeUpgrade"]
      rolloutStrategy:
        maxConcurrency: 200
        timeout: 2400
```

Where:

* `clusterLabelSelectors`: Clusters to upgrade.
* `seedImageRef`: Target platform version, the seed image, and the secret required to access the image.

If you add the seed image pull secret in the hub cluster, in the same namespace as the `ImageBasedGroupUpgrade` resource, the secret is added to the manifest list for the `Prep` stage. The secret is recreated in each spoke cluster in the `openshift-lifecycle-agent` namespace.

* `extraManifests`: Optional: Applies additional manifests, which are not in the seed image, to the target cluster. Also applies `ConfigMap` objects for custom catalog sources.
* `oadpContent`: `ConfigMap` resources that contain the OADP `Backup` and `Restore` CRs.
* `plan`: Upgrade plan details.
* `maxConcurrency`: Number of clusters to update in a batch.
* `timeout`: Timeout limit to complete the action in minutes.

##### [16.4.1.1. Supported action combinations](#ztp-image-based-upgrade-supported-combinations_ztp-gitops) Copy linkLink copied to clipboard!

Actions are the list of stage transitions that TALM completes in the steps of an upgrade plan for the selected group of clusters. Each `action` entry in the `ImageBasedGroupUpgrade` CR is a separate step and a step has one or several actions that share the same rollout strategy. You can achieve more control over the rollout strategy for each action by separating actions into steps.

You can combine these actions differently in your upgrade plan and you can add the next steps later. Wait until the earlier steps either complete or fail before adding a step to your plan. The first action of an added step for clusters that failed a earlier steps must be either `Abort` or `Rollback`.

Important

You cannot remove actions or steps from an ongoing plan.

The following table shows example plans for different levels of control over the rollout strategy:

Expand

Table 16.5. Example upgrade plans

| Example plan | Description |
| --- | --- |
| ``` plan: - actions: ["Prep", "Upgrade", "FinalizeUpgrade"]   rolloutStrategy:     maxConcurrency: 200     timeout: 60 ``` | All actions share the same strategy |
| ``` plan: - actions: ["Prep", "Upgrade"]   rolloutStrategy:     maxConcurrency: 200     timeout: 60 - actions: ["FinalizeUpgrade"]   rolloutStrategy:     maxConcurrency: 500     timeout: 10 ``` | Some actions share the same strategy |
| ``` plan: - actions: ["Prep"]   rolloutStrategy:     maxConcurrency: 200     timeout: 60 - actions: ["Upgrade"]   rolloutStrategy:     maxConcurrency: 200     timeout: 20 - actions: ["FinalizeUpgrade"]   rolloutStrategy:     maxConcurrency: 500     timeout: 10 ``` | All actions have different strategies |

Show more

Important

Clusters that fail one of the actions will skip the remaining actions in the same step.

The `ImageBasedGroupUpgrade` API accepts the following actions:

`Prep`
:   Start preparing the upgrade resources by moving to the `Prep` stage.

`Upgrade`
:   Start the upgrade by moving to the `Upgrade` stage.

`FinalizeUpgrade`
:   Complete the upgrade on selected clusters that completed the `Upgrade` action by moving to the `Idle` stage.

`Rollback`
:   Start a rollback only on successfully upgraded clusters by moving to the `Rollback` stage.

`FinalizeRollback`
:   Complete the rollback by moving to the `Idle` stage.

`AbortOnFailure`
:   Cancel the upgrade on selected clusters that failed the `Prep` or `Upgrade` actions by moving to the `Idle` stage.

`Abort`
:   Cancel an ongoing upgrade only on clusters that are not yet upgraded by moving to the `Idle` stage.

The following action combinations are supported. A pair of brackets signifies one step in the `plan` section:

* `["Prep"]`, `["Abort"]`
* `["Prep", "Upgrade", "FinalizeUpgrade"]`
* `["Prep"]`, `["AbortOnFailure"]`, `["Upgrade"]`, `["AbortOnFailure"]`, `["FinalizeUpgrade"]`
* `["Rollback", "FinalizeRollback"]`

Use one of the following combinations when you need to resume or cancel an ongoing upgrade from a completely new `ImageBasedGroupUpgrade` CR:

* `["Upgrade","FinalizeUpgrade"]`
* `["FinalizeUpgrade"]`
* `["FinalizeRollback"]`
* `["Abort"]`
* `["AbortOnFailure"]`

##### [16.4.1.2. Labeling for cluster selection](#ztp-image-based-upgrade-cluster-labeling_ztp-gitops) Copy linkLink copied to clipboard!

Use the `spec.clusterLabelSelectors` field for initial cluster selection. In addition, TALM labels the managed clusters according to the results of their last stage transition.

When a stage completes or fails, TALM marks the relevant clusters with the following labels:

* `lcm.openshift.io/ibgu-<stage>-completed`
* `lcm.openshift.io/ibgu-<stage>-failed`

Use these cluster labels to cancel or roll back an upgrade on a group of clusters after troubleshooting the issues.

Important

If you are using the `ImageBasedGroupUpgrade` CR to upgrade your clusters, ensure that you update the `lcm.openshift.io/ibgu-<stage>-completed` or `lcm.openshift.io/ibgu-<stage>-failed` cluster labels properly after performing troubleshooting or recovery steps on the managed clusters. This ensures that the TALM continues to manage the image-based upgrade for the cluster.

For example, if you want to cancel the upgrade for all managed clusters except for clusters that successfully completed the upgrade, you can add an `Abort` action to your plan. The `Abort` action moves back the `ImageBasedUpgrade` CR to the `Idle` stage, which cancels the upgrade on clusters that are not yet upgraded. Adding a separate `Abort` action ensures that the TALM does not perform the `Abort` action on clusters that have the `lcm.openshift.io/ibgu-upgrade-completed` label.

The TALM removes the cluster labels after successfully canceling or finalizing the upgrade.

##### [16.4.1.3. Status monitoring](#ztp-image-based-upgrade-status-monitoring_ztp-gitops) Copy linkLink copied to clipboard!

The `ImageBasedGroupUpgrade` CR ensures a better monitoring experience by aggregating status reporting for all clusters in one place. You can monitor the following actions:

`status.clusters.completedActions`
:   Shows all completed actions defined in the `plan` section.

`status.clusters.currentAction`
:   Shows all actions that are currently in progress.

`status.clusters.failedActions`
:   Shows all failed actions along with a detailed error message.

#### [16.4.2. Performing an image-based upgrade on managed clusters at scale in several steps](#ztp-image-based-upgrade-procedure-steps_ztp-gitops) Copy linkLink copied to clipboard!

For use cases when you need better control of when the upgrade interrupts your service, you can upgrade a set of your managed clusters by using the `ImageBasedGroupUpgrade` CR. You can use the `ImageBasedGroupUpgrade` CR to add actions after the earlier step is complete. After evaluating the results of the earlier steps, you can move to the next upgrade stage or troubleshoot any failed steps throughout the procedure.

Important

Only certain action combinations are supported and listed in *Supported action combinations*.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created policies and `ConfigMap` objects for resources used in the image-based upgrade.
* You have installed the Lifecycle Agent and OADP Operators on all managed clusters through the hub cluster.

**Procedure**

1. Create a YAML file on the hub cluster that has the `ImageBasedGroupUpgrade` CR:

   ```
   apiVersion: lcm.openshift.io/v1alpha1
   kind: ImageBasedGroupUpgrade
   metadata:
     name: <filename>
     namespace: default
   spec:
     clusterLabelSelectors:
       - matchExpressions:
         - key: name
           operator: In
           values:
           - spoke1
           - spoke4
           - spoke6
     ibuSpec:
       seedImageRef:
         image: quay.io/seed/image:4.16.0-rc.1
         version: 4.16.0-rc.1
         pullSecretRef:
           name: "<seed_pull_secret>"
       extraManifests:
         - name: example-extra-manifests
           namespace: openshift-lifecycle-agent
       oadpContent:
         - name: oadp-cm
           namespace: openshift-adp
     plan:
       - actions: ["Prep"]
         rolloutStrategy:
           maxConcurrency: 2
           timeout: 2400
   ```

   Where:

   * `clusterLabelSelectors`: Clusters to upgrade.
   * `seedImageRef`: Target platform version, the seed image, and the secret required to access the image.

   Note

   If you add the seed image pull secret in the hub cluster, in the same namespace as the `ImageBasedGroupUpgrade` resource, the {lco} adds the secret to the manifest list for the `Prep` stage. The {lco} recreates the secret in each spoke cluster in the `openshift-lifecycle-agent` namespace.

   * `extraManifests`: Optional: Applies additional manifests, which are not in the seed image, to the target cluster. Also applies `ConfigMap` objects for custom catalog sources.
   * `oadpContent`: List of `ConfigMap` resources that contain the OADP `Backup` and `Restore` CRs.
   * `plan`: Upgrade plan details.
2. Apply the created file by running the following command on the hub cluster:

   ```
   $ oc apply -f <filename>.yaml
   ```
3. Monitor the status updates by running the following command on the hub cluster:

   ```
   $ oc get ibgu -o yaml
   ```

   **Example output**

   ```
   # ...
   status:
     clusters:
     - completedActions:
       - action: Prep
       name: spoke1
     - completedActions:
       - action: Prep
       name: spoke4
     - failedActions:
       - action: Prep
       name: spoke6
   # ...
   ```

   The earlier output of an example plan starts with the `Prep` stage only and you add actions to the plan based on the results of the earlier step. The TALM adds a label to the clusters to mark if the upgrade succeeded or failed. For example, the TALM applies the `lcm.openshift.io/ibgu-prep-failed` label to clusters that failed the `Prep` stage.

   After investigating the failure, you can add the `AbortOnFailure` step to your upgrade plan. It moves the clusters labeled with `lcm.openshift.io/ibgu-<action>-failed` back to the `Idle` stage. The TALM deletes the resources that are related to the upgrade on the selected clusters.
4. Optional: Add the `AbortOnFailure` action to your existing `ImageBasedGroupUpgrade` CR by running the following command:

   ```
   $ oc patch ibgu <filename> --type=json -p \
   '[{"op": "add", "path": "/spec/plan/-", "value": {"actions": ["AbortOnFailure"], "rolloutStrategy": {"maxConcurrency": 5, "timeout": 10}}}]'
   ```

   1. Continue monitoring the status updates by running the following command:

      ```
      $ oc get ibgu -o yaml
      ```
5. Add the action to your existing `ImageBasedGroupUpgrade` CR by running the following command:

   ```
   $ oc patch ibgu <filename> --type=json -p \
   '[{"op": "add", "path": "/spec/plan/-", "value": {"actions": ["Upgrade"], "rolloutStrategy": {"maxConcurrency": 2, "timeout": 30}}}]'
   ```
6. Optional: Add the `AbortOnFailure` action to your existing `ImageBasedGroupUpgrade` CR by running the following command:

   ```
   $ oc patch ibgu <filename> --type=json -p \
   '[{"op": "add", "path": "/spec/plan/-", "value": {"actions": ["AbortOnFailure"], "rolloutStrategy": {"maxConcurrency": 5, "timeout": 10}}}]'
   ```

   1. Continue monitoring the status updates by running the following command:

      ```
      $ oc get ibgu -o yaml
      ```
7. Add the action to your existing `ImageBasedGroupUpgrade` CR by running the following command:

   ```
   $ oc patch ibgu <filename> --type=json -p \
   '[{"op": "add", "path": "/spec/plan/-", "value": {"actions": ["FinalizeUpgrade"], "rolloutStrategy": {"maxConcurrency": 10, "timeout": 3}}}]'
   ```

**Verification**

* Monitor the status updates by running the following command:

  ```
  $ oc get ibgu -o yaml
  ```

  **Example output**

  ```
  # ...
  status:
    clusters:
    - completedActions:
      - action: Prep
      - action: AbortOnFailure
      failedActions:
      - action: Upgrade
      name: spoke1
    - completedActions:
      - action: Prep
      - action: Upgrade
      - action: FinalizeUpgrade
      name: spoke4
    - completedActions:
      - action: AbortOnFailure
      failedActions:
      - action: Prep
      name: spoke6
  # ...
  ```

#### [16.4.3. Performing an image-based upgrade on managed clusters at scale in one step](#ztp-image-based-upgrade-procedure-one-step_ztp-gitops) Copy linkLink copied to clipboard!

For use cases when service interruption is not a concern, you can upgrade a set of your managed clusters by using the `ImageBasedGroupUpgrade` custom resource (CR). You can use the `ImageBasedGroupUpgrade` CR to combine several actions in one step with one rollout strategy. With one rollout strategy, you can reduce the upgrade time but you can only troubleshoot failed clusters after the upgrade plan is complete.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.
* You have created policies and `ConfigMap` objects for resources used in the image-based upgrade.
* You have installed the Lifecycle Agent and OADP Operators on all managed clusters through the hub cluster.

**Procedure**

1. Create a YAML file on the hub cluster that has the `ImageBasedGroupUpgrade` CR:

   ```
   apiVersion: lcm.openshift.io/v1alpha1
   kind: ImageBasedGroupUpgrade
   metadata:
     name: <filename>
     namespace: default
   spec:
     clusterLabelSelectors:
       - matchExpressions:
         - key: name
           operator: In
           values:
           - spoke1
           - spoke4
           - spoke6
     ibuSpec:
       seedImageRef:
         image: quay.io/seed/image:4.22.0
         version: 4.22.0
         pullSecretRef:
           name: "<seed_pull_secret>"
       extraManifests:
         - name: example-extra-manifests
           namespace: openshift-lifecycle-agent
       oadpContent:
         - name: oadp-cm
           namespace: openshift-adp
     plan:
       - actions: ["Prep", "Upgrade", "FinalizeUpgrade"]
         rolloutStrategy:
           maxConcurrency: 200
           timeout: 2400
   ```

   Where:

   * `clusterLabelSelectors`: Clusters to upgrade.
   * `seedImageRef`: Target platform version, the seed image, and the secret required to access the image.

   Note

   If you add the seed image pull secret in the hub cluster, in the same namespace as the `ImageBasedGroupUpgrade` resource, the secret is added to the manifest list for the `Prep` stage. The secret is recreated in each spoke cluster in the `openshift-lifecycle-agent` namespace.

   * `extraManifests`: Optional: Applies additional manifests, which are not in the seed image, to the target cluster. Also applies `ConfigMap` objects for custom catalog sources.
   * `oadpContent`: `ConfigMap` resources that contain the OADP `Backup` and `Restore` CRs.
   * `plan`: Upgrade plan details.
   * `maxConcurrency`: Number of clusters to update in a batch.
   * `timeout`: Timeout limit to complete the action in minutes.
2. Apply the created file by running the following command on the hub cluster:

   ```
   $ oc apply -f <filename>.yaml
   ```

**Verification**

* Monitor the status updates by running the following command:

  ```
  $ oc get ibgu -o yaml
  ```

  **Example output**

  ```
  # ...
  status:
    clusters:
    - completedActions:
      - action: Prep
      failedActions:
      - action: Upgrade
      name: spoke1
    - completedActions:
      - action: Prep
      - action: Upgrade
      - action: FinalizeUpgrade
      name: spoke4
    - failedActions:
      - action: Prep
      name: spoke6
  # ...
  ```

#### [16.4.4. Canceling an image-based upgrade on managed clusters at scale](#ztp-image-based-upgrade-procedure-cancel_ztp-gitops) Copy linkLink copied to clipboard!

You can cancel the upgrade on a set of managed clusters that completed the `Prep` stage.

Important

Only certain action combinations are supported and listed in *Supported action combinations*.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Create a separate YAML file on the hub cluster that has the `ImageBasedGroupUpgrade` CR:

   ```
   apiVersion: lcm.openshift.io/v1alpha1
   kind: ImageBasedGroupUpgrade
   metadata:
     name: <filename>
     namespace: default
   spec:
     clusterLabelSelectors:
       - matchExpressions:
         - key: name
           operator: In
           values:
           - spoke4
     ibuSpec:
       seedImageRef:
         image: quay.io/seed/image:4.16.0-rc.1
         version: 4.16.0-rc.1
         pullSecretRef:
           name: "<seed_pull_secret>"
       extraManifests:
         - name: example-extra-manifests
           namespace: openshift-lifecycle-agent
       oadpContent:
         - name: oadp-cm
           namespace: openshift-adp
     plan:
       - actions: ["Abort"]
         rolloutStrategy:
           maxConcurrency: 5
           timeout: 10
   ```

   All managed clusters that completed the `Prep` stage move back to the `Idle` stage.
2. Apply the created file by running the following command on the hub cluster:

   ```
   $ oc apply -f <filename>.yaml
   ```

**Verification**

* Monitor the status updates by running the following command:

  ```
  $ oc get ibgu -o yaml
  ```

  **Example output**

  ```
  # ...
  status:
    clusters:
    - completedActions:
      - action: Prep
      currentActions:
      - action: Abort
      name: spoke4
  # ...
  ```

#### [16.4.5. Rolling back an image-based upgrade on managed clusters at scale](#ztp-image-based-upgrade-procedure-rollback_ztp-gitops) Copy linkLink copied to clipboard!

Roll back the changes on a set of managed clusters if you find unresolvable issues after a successful upgrade. You need to create a separate `ImageBasedGroupUpgrade` CR and define the set of managed clusters that you want to roll back.

Important

Only certain action combinations are supported and listed in *Supported action combinations*.

**Prerequisites**

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

**Procedure**

1. Create a separate YAML file on the hub cluster that has the `ImageBasedGroupUpgrade` CR:

   ```
   apiVersion: lcm.openshift.io/v1alpha1
   kind: ImageBasedGroupUpgrade
   metadata:
     name: <filename>
     namespace: default
   spec:
     clusterLabelSelectors:
       - matchExpressions:
         - key: name
           operator: In
           values:
           - spoke4
     ibuSpec:
       seedImageRef:
         image: quay.io/seed/image:4.22.0-rc.1
         version: 4.22.0-rc.1
         pullSecretRef:
           name: "<seed_pull_secret>"
       extraManifests:
         - name: example-extra-manifests
           namespace: openshift-lifecycle-agent
       oadpContent:
         - name: oadp-cm
           namespace: openshift-adp
     plan:
       - actions: ["Rollback", "FinalizeRollback"]
         rolloutStrategy:
           maxConcurrency: 200
           timeout: 2400
   ```
2. Apply the created file by running the following command on the hub cluster:

   ```
   $ oc apply -f <filename>.yaml
   ```

   All managed clusters that match the defined labels move back to the `Rollback` and then the `Idle` stages to complete the rollback.

**Verification**

* Monitor the status updates by running the following command:

  ```
  $ oc get ibgu -o yaml
  ```

  **Example output**

  ```
  # ...
  status:
    clusters:
    - completedActions:
      - action: Rollback
      - action: FinalizeRollback
      name: spoke4
  # ...
  ```

#### [16.4.6. Troubleshooting image-based upgrades with Lifecycle Agent](#cnf-image-based-upgrade-troubleshooting_ztp-gitops) Copy linkLink copied to clipboard!

Perform troubleshooting steps on the managed clusters to resolve any issues.

Important

If you are using the `ImageBasedGroupUpgrade` CR to upgrade your clusters, ensure that you update the `lcm.openshift.io/ibgu-<stage>-completed` or `lcm.openshift.io/ibgu-<stage>-failed` cluster labels properly after performing troubleshooting or recovery steps on the managed clusters. This ensures that the TALM continues to manage the image-based upgrade for the cluster.

##### [16.4.6.1. Collecting logs](#cnf-image-based-upgrade-troubleshooting-must-gather_ztp-gitops) Copy linkLink copied to clipboard!

You can use the `oc adm must-gather` CLI to collect information for debugging and troubleshooting.

To collect data about the Operators, run the following command:

```
$  oc adm must-gather \
  --dest-dir=must-gather/tmp \
  --image=$(oc -n openshift-lifecycle-agent get deployment.apps/lifecycle-agent-controller-manager -o jsonpath='{.spec.template.spec.containers[?(@.name == "manager")].image}') \
  --image=quay.io/konveyor/oadp-must-gather:latest \//
  --image=quay.io/openshift/origin-must-gather:latest
```

+ Where:

+ \* `--image=quay.io/konveyor/oadp-must-gather:latest`: Optional: Add this option if you need to gather more information from the OADP Operator. \* `--image=quay.io/openshift/origin-must-gather:latest`: Optional: Add this option if you need to gather more information from the SR-IOV Operator.

##### [16.4.6.2. AbortFailed or FinalizeFailed error](#cnf-image-based-upgrade-troubleshooting-manual-cleanup_ztp-gitops) Copy linkLink copied to clipboard!

Issue
:   During the finalization stage or when you stop the process at the `Prep` stage, Lifecycle Agent cleans up the following resources:

    * Stateroot that is no longer required
    * Precaching resources
    * OADP CRs
    * `ImageBasedUpgrade` CR

    If the Lifecycle Agent fails to clean up these resources, it transitions to the `AbortFailed` or `FinalizeFailed` states. The condition message and log show the steps that failed, as shown in the following example:

    Example error message:

    ```
    message: failed to delete all the backup CRs. Perform cleanup manually then add 'lca.openshift.io/manual-cleanup-done' annotation to ibu CR to transition back to Idle
          observedGeneration: 5
          reason: AbortFailed
          status: "False"
          type: Idle
    ```

Resolution
:   1. Inspect the logs to find the reason for failure.
    2. To prompt Lifecycle Agent to retry the cleanup, add the `lca.openshift.io/manual-cleanup-done` annotation to the `ImageBasedUpgrade` CR.

       After observing this annotation, Lifecycle Agent retries the cleanup and, if it is successful, the `ImageBasedUpgrade` stage transitions to `Idle`.

       If the cleanup fails again, you can manually clean up the resources.

##### [16.4.6.3. Cleaning up stateroot manually](#cnf-image-based-upgrade-troubleshooting-stateroot_ztp-gitops) Copy linkLink copied to clipboard!

Issue
:   Stopping at the `Prep` stage, Lifecycle Agent cleans up the new stateroot. When finalizing after a successful upgrade or a rollback, Lifecycle Agent cleans up the old stateroot. If this step fails, you must inspect the logs to decide why the failure occurred.

Resolution
:   1. Check if there are any existing deployments in the stateroot by running the following command:

       ```
       $ ostree admin status
       ```
    2. If there are any, clean up the existing deployment by running the following command:

       ```
       $ ostree admin undeploy <index_of_deployment>
       ```
    3. After cleaning up all the deployments of the stateroot, wipe the stateroot directory by running the following commands:

       Warning

       Ensure that the booted deployment is not in this stateroot.

       ```
       $ stateroot="<stateroot_to_delete>"
       ```

       ```
       $ unshare -m /bin/sh -c "mount -o remount,rw /sysroot && rm -rf /sysroot/ostree/deploy/${stateroot}"
       ```

##### [16.4.6.4. Cleaning up OADP resources manually](#cnf-image-based-upgrade-troubleshooting-oadp-resources_ztp-gitops) Copy linkLink copied to clipboard!

Issue
:   Automatic cleanup of OADP resources can fail due to connection issues between Lifecycle Agent and the S3 backend. By restoring the connection and adding the `lca.openshift.io/manual-cleanup-done` annotation, the Lifecycle Agent can successfully cleanup backup resources.

Resolution

1. Check the backend connectivity by running the following command:

   ```
   $ oc get backupstoragelocations.velero.io -n openshift-adp
   ```

   The following example shows successful backend connectivity:

   ```
   NAME                          PHASE       LAST VALIDATED   AGE   DEFAULT
   dataprotectionapplication-1   Available   33s              8d    true
   ```
2. Remove all backup resources and then add the `lca.openshift.io/manual-cleanup-done` annotation to the `ImageBasedUpgrade` CR.

##### [16.4.6.5. LVM Storage volume contents not restored](#cnf-image-based-upgrade-troubleshooting-lvms_ztp-gitops) Copy linkLink copied to clipboard!

When you use LVM Storage to configure dynamic persistent volume storage, LVM Storage might not restore the persistent volume contents if you have configured it incorrectly.

##### [16.4.6.6. Missing LVM Storage-related fields in Backup CR](#cnf-image-based-upgrade-troubleshooting-lvms-backup_ztp-gitops) Copy linkLink copied to clipboard!

Issue
:   Your `Backup` CRs might be missing fields that you need to restore your persistent volumes. You can check for events in your application pod to decide if you have this issue by running the following:

    ```
    $ oc describe pod <your_app_name>
    ```

    The following example output shows a pod failing due to missing LVM Storage-related fields in the `Backup` CR:

    ```
    Events:
      Type     Reason            Age                From               Message
      ----     ------            ----               ----               -------
      Warning  FailedScheduling  58s (x2 over 66s)  default-scheduler  0/1 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/1 nodes are available: 1 Preemption is not helpful for scheduling..
      Normal   Scheduled         56s                default-scheduler  Successfully assigned default/db-1234 to sno1.example.lab
      Warning  FailedMount       24s (x7 over 55s)  kubelet            MountVolume.SetUp failed for volume "pvc-1234" : rpc error: code = Unknown desc = VolumeID is not found
    ```

Resolution
:   You must include `logicalvolumes.topolvm.io` in the application `Backup` CR. Without this resource, the application restores its persistent volume claims and persistent volume manifests correctly, however, the `logicalvolume` associated with this persistent volume is not restored properly after pivot. The following example shows a correctly configured `Backup` CR:

    ```
    apiVersion: velero.io/v1
    kind: Backup
    metadata:
      labels:
        velero.io/storage-location: default
      name: small-app
      namespace: openshift-adp
    spec:
      includedNamespaces:
      - test
      includedNamespaceScopedResources:
      - secrets
      - persistentvolumeclaims
      - deployments
      - statefulsets
      includedClusterScopedResources:
      - persistentVolumes
      - volumesnapshotcontents
      - logicalvolumes.topolvm.io
    ```

    To restore the persistent volumes for your application, you must configure the `includedClusterScopedResources` section as shown.

##### [16.4.6.7. Missing LVM Storage-related fields in Restore CR](#cnf-image-based-upgrade-troubleshooting-lvms-restore_ztp-gitops) Copy linkLink copied to clipboard!

Issue
:   LVM Storage restores the expected resources for the applications but it does not preserve the persistent volume contents after upgrading.

    1. List the persistent volumes for you applications by running the following command before pivot:

       ```
       $ oc get pv,pvc,logicalvolumes.topolvm.io -A
       ```

       The following shows the output before pivot:

       ```
       NAME                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM            STORAGECLASS   REASON   AGE
       persistentvolume/pvc-1234   1Gi        RWO            Retain           Bound    default/pvc-db   lvms-vg1                4h45m

       NAMESPACE   NAME                           STATUS   VOLUME     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
       default     persistentvolumeclaim/pvc-db   Bound    pvc-1234   1Gi        RWO            lvms-vg1       4h45m

       NAMESPACE   NAME                                AGE
                   logicalvolume.topolvm.io/pvc-1234   4h45m
       ```
    2. List the persistent volumes for you applications by running the following command after pivot:

       ```
       $ oc get pv,pvc,logicalvolumes.topolvm.io -A
       ```

       The following shows the output after pivot:

       ```
       NAME                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM            STORAGECLASS   REASON   AGE
       persistentvolume/pvc-1234   1Gi        RWO            Delete           Bound    default/pvc-db   lvms-vg1                19s

       NAMESPACE   NAME                           STATUS   VOLUME     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
       default     persistentvolumeclaim/pvc-db   Bound    pvc-1234   1Gi        RWO            lvms-vg1       19s

       NAMESPACE   NAME                                AGE
                   logicalvolume.topolvm.io/pvc-1234   18s
       ```

Resolution
:   The reason for this issue is that the `logicalvolume` status is not preserved in the `Restore` CR. This status is important because Velero requires this status to reference the volumes that you must preserve after pivoting. You must include the following fields in the application `Restore` CR, as shown in the following example:

    ```
    apiVersion: velero.io/v1
    kind: Restore
    metadata:
      name: sample-vote-app
      namespace: openshift-adp
      labels:
        velero.io/storage-location: default
      annotations:
        lca.openshift.io/apply-wave: "3"
    spec:
      backupName:
        sample-vote-app
      restorePVs: <restore_pvs>
      restoreStatus:
        includedResources:
          - logicalvolumes
    ```

    where:

`<restore_pvs>`
:   To preserve the persistent volumes for your application, you must set `restorePVs` to `true`.

`restoreStatus`
:   To preserve the persistent volumes for your application, you must configure this field as shown.

##### [16.4.6.8. Debugging failed Backup and Restore CRs](#cnf-image-based-upgrade-troubleshooting-debugging-oadp-crs_ztp-gitops) Copy linkLink copied to clipboard!

Issue
:   The backup or restoration of artifacts failed.

Resolution
:   You can debug `Backup` and `Restore` CRs and retrieve logs with the OADP CLI. The OADP CLI offers more detailed information than the OpenShift CLI tool.

    1. Describe the `Backup` CR that has errors by running the following command:

       ```
       $ oc oadp backup describe backup-acm-klusterlet -n openshift-adp --details
       ```
    2. Describe the `Restore` CR that has errors by running the following command:

       ```
       $ oc oadp restore describe restore-acm-klusterlet -n openshift-adp --details
       ```
    3. Download the backed up resources to a local directory by running the following command:

       ```
       $ oc oadp backup download backup-acm-klusterlet -n openshift-adp -o ~/backup-acm-klusterlet.tar.gz
       ```

## [Chapter 17. Image-based installation for single-node OpenShift](#image-based-installation-for-single-node-openshift) Copy linkLink copied to clipboard!

### [17.1. Understanding image-based installation and deployment for single-node OpenShift](#ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

Image-based installations significantly reduce the deployment time of single-node OpenShift clusters by streamlining the installation process.

This approach enables the preinstallation of configured and validated instances of single-node OpenShift on target hosts. These preinstalled hosts can be rapidly reconfigured and deployed at the far edge of the network, including in disconnected environments, with minimal intervention.

Note

To deploy a managed cluster using an imaged-based approach in combination with GitOps Zero Touch Provisioning (ZTP), you can use the SiteConfig operator.

#### [17.1.1. Overview of image-based installation and deployment for single-node OpenShift clusters](#ibi-installation-deployment-overview_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

Deploying infrastructure at the far edge of the network presents challenges for service providers with low bandwidth, high latency, and disconnected environments. It is also costly and time-consuming to install and deploy single-node OpenShift clusters.

An image-based approach to installing and deploying single-node OpenShift clusters at the far edge of the network overcomes these challenges by separating the installation and deployment stages.

**Figure 17.1. Overview of an image-based installation and deployment for managed single-node OpenShift clusters**

Imaged-based installation
:   Preinstall multiple hosts with single-node OpenShift at a central site, such as a service depot or a factory. Then, validate the base configuration for these hosts and leverage the image-based approach to perform reproducible factory installs at scale by using a single live installation ISO.

Image-based deployment
:   Ship the preinstalled and validated hosts to a remote site and rapidly reconfigure and deploy the clusters in a matter of minutes by using a configuration ISO.

You can choose from two methods to preinstall and configure your SNO clusters.

Using the `openshift-install` program
:   For a single-node OpenShift cluster, use the `openshift-install` program only to manually create the live installation ISO that is common to all hosts. Then, use the program again to create the configuration ISO which ensures that the host is unique. For more information, see “Deploying managed single-node OpenShift using the openshift-install program”.

Using the IBI Operator
:   For managed single-node OpenShift clusters, you can use the `openshift-install` with the Image Based Install (IBI) Operator to scale up the operations. The program creates the live installation ISO and then the IBI Operator creates one configuration ISO for each host. For more information, see "Deploying single-node OpenShift using the IBI Operator".

##### [17.1.1.1. Image-based installation for single-node OpenShift clusters](#ibi-image-based-installation-overview_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

Using the Lifecycle Agent, you can generate an OCI container image that encapsulates an instance of a single-node OpenShift cluster.

This image is derived from a dedicated cluster that you can configure with the target OpenShift Container Platform version.

You can reference this image in a live installation ISO to consistently preinstall configured and validated instances of single-node OpenShift to multiple hosts. This approach enables the preparation of hosts at a central location, for example in a factory or service depot, before shipping the preinstalled hosts to a remote site for rapid reconfiguration and deployment. The instructions for preinstalling a host are the same whether you deploy the host by using only the `openshift-install` program or using the program with the IBI Operator.

The following is a high-level overview of the image-based installation process:

1. Generate an image from a single-node OpenShift cluster.
2. Use the `openshift-install` program to embed the seed image URL, and other installation artifacts, in a live installation ISO.
3. Start the host using the live installation ISO to preinstall the host.

   During this process, the `openshift-install` program installs Red Hat Enterprise Linux CoreOS (RHCOS) to the disk, pulls the image you generated, and precaches release container images to the disk.
4. When the installation completes, the host is ready to ship to the remote site for rapid reconfiguration and deployment.

##### [17.1.1.2. Image-based deployment for single-node OpenShift clusters](#ibi-image-based-deployment-overview_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

You can use the `openshift-install` program or the IBI Operator to configure and deploy a host that you preinstalled with an image-based installation.

Single-node OpenShift cluster deployment
:   To configure the target host with site-specific details by using the `openshift-install` program, you must create the following resources:

    * The `install-config.yaml` installation manifest
    * The `image-based-config.yaml` manifest

    The `openshift-install` program uses these resources to generate a configuration ISO that you attach to the preinstalled target host to complete the deployment.

Managed single-node OpenShift cluster deployment
:   Red Hat Advanced Cluster Management (RHACM) and the multicluster engine for Kubernetes Operator (MCE) use a hub-and-spoke architecture to manage and deploy single-node OpenShift clusters across multiple sites. Using this approach, the hub cluster serves as a central control plane that manages the spoke clusters, which are often remote single-node OpenShift clusters deployed at the far edge of the network.

    You can define the site-specific configuration resources for an image-based deployment in the hub cluster. The IBI Operator uses these configuration resources to reconfigure the preinstalled host at the remote site and deploy the host as a managed single-node OpenShift cluster. This approach is especially beneficial for telecommunications providers and other service providers with extensive, distributed infrastructures, where an end-to-end installation at the remote site would be time-consuming and costly.

    The following is a high-level overview of the image-based deployment process for hosts preinstalled with an imaged-based installation:

    * Define the site-specific configuration resources for the preinstalled host in the hub cluster.
    * Apply these resources in the hub cluster. This initiates the deployment process.
    * The IBI Operator creates a configuration ISO.
    * The IBI Operator boots the target preinstalled host with the configuration ISO attached.
    * The host mounts the configuration ISO and begins the reconfiguration process.
    * When the reconfiguration completes, the single-node OpenShift cluster is ready.

    As the host is already preinstalled using an image-based installation, a technician can reconfigure and deploy the host in a matter of minutes.

#### [17.1.2. Image-based installation and deployment components](#ibi-installation-deployment-components_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

The following content describes the components in an image-based installation and deployment.

Seed image
:   OCI container image generated from a dedicated cluster with the target OpenShift Container Platform version.

Seed cluster
:   Dedicated single-node OpenShift cluster that you use to create a seed image and is deployed with the target OpenShift Container Platform version.

Lifecycle Agent
:   Generates the seed image.

Image Based Install (IBI) Operator
:   When you deploy managed clusters, the IBI Operator creates a configuration ISO from the site-specific resources you define in the hub cluster, and attaches the configuration ISO to the preinstalled host by using a bare-metal provisioning service.

`openshift-install` program
:   Creates the installation and configuration ISO, and embeds the seed image URL in the live installation ISO. If the IBI Operator is not used, you must manually attach the configuration ISO to a preinstalled host to complete the deployment.

#### [17.1.3. Cluster guidelines for image-based installation and deployment](#ibi-image-based-install-cluster-guide_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

For a successful image-based installation and deployment, see the following guidelines.

##### [17.1.3.1. Cluster guidelines](#ibi-cluster-guidelines_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

* If you are using Red Hat Advanced Cluster Management (RHACM), to avoid including any RHACM resources in your seed image, you need to disable all optional RHACM add-ons before generating the seed image.
* In a deployed cluster, the `clusterversion` resource shows a `creationTimestamp` that reflects the creation date of the seed cluster, not the deployment date of the new cluster. To determine the deployment date of a new cluster, check the `creationTimestamp` field for the `Node` resource instead.

##### [17.1.3.2. Seed cluster guidelines](#ibi-seed-cluster-guidelines_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

* If your cluster deployment at the edge of the network requires a proxy configuration, you must create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
* The `clusterNetwork` and `serviceNetwork` network configurations in the seed cluster persist to the deployed cluster. The Lifecycle Agent embeds these settings in the seed image. You cannot change these settings later in the image-based installation and deployment process.
* If you set a maximum transmission unit (MTU) in the seed cluster, you must set the same MTU value in the static network configuration for the image-based configuration ISO.
* Your single-node OpenShift seed cluster must have a shared `/var/lib/containers` directory for precaching images during an image-based installation. For more information see "Configuring a shared container partition between ostree stateroots".
* Create a seed image from a single-node OpenShift cluster that uses the same hardware as your target bare-metal host. The seed cluster must reflect your target cluster configuration for the following items:

  + CPU topology

    - CPU architecture
    - Number of CPU cores
    - Tuned performance configuration, such as number of reserved CPUs
  + IP version configuration, either IPv4, IPv6, or dual-stack networking
  + Disconnected registry

    Note

    If the target cluster uses a disconnected registry, your seed cluster must use a disconnected registry. The registries do not have to be the same.
  + FIPS configuration

#### [17.1.4. Software prerequisites for an image-based installation and deployment](#ztp-image-based-upgrade-prereqs_ibi-understanding-image-based-install) Copy linkLink copied to clipboard!

An image-based installation and deployment requires the following minimum software versions for these required components.

Expand

Table 17.1. Minimum software requirements

| Component | Software version |
| --- | --- |
| Managed cluster version | 4.17 |
| Hub cluster version | 4.16 |
| Red Hat Advanced Cluster Management (RHACM) | 2.12 |
| Lifecycle Agent | 4.16 or later |
| Image Based Install Operator | 4.17 |
| `openshift-install` program | 4.17 |

Show more

### [17.2. Preparing for image-based installation for single-node OpenShift clusters](#ibi-preparing-for-image-based-install) Copy linkLink copied to clipboard!

To prepare for an image-based installation for single-node OpenShift clusters, you must complete the following tasks:

* Create a seed image by using the Lifecycle Agent.
* Verify that all software components meet the required versions. For further information, see "Software prerequisites for an image-based installation and deployment".

#### [17.2.1. Installing the Lifecycle Agent](#installing-the-lifecycle-agent) Copy linkLink copied to clipboard!

Use the Lifecycle Agent to generate a seed image from a seed cluster. You can install the Lifecycle Agent using the OpenShift CLI (`oc`) or the web console.

##### [17.2.1.1. Installing the Lifecycle Agent by using the CLI](#cnf-image-based-upgrade-installing-lifecycle-agent-using-cli_ibi-preparing-image-based-install) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to install the Lifecycle Agent.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a `Namespace` object YAML file for the Lifecycle Agent:

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     name: openshift-lifecycle-agent
     annotations:
       workload.openshift.io/allowed: management
   ```

   1. Create the `Namespace` CR by running the following command:

      ```
      $ oc create -f <namespace_filename>.yaml
      ```
2. Create an `OperatorGroup` object YAML file for the Lifecycle Agent:

   ```
   apiVersion: operators.coreos.com/v1
   kind: OperatorGroup
   metadata:
     name: openshift-lifecycle-agent
     namespace: openshift-lifecycle-agent
   spec:
     targetNamespaces:
     - openshift-lifecycle-agent
   ```

   1. Create the `OperatorGroup` CR by running the following command:

      ```
      $ oc create -f <operatorgroup_filename>.yaml
      ```
3. Create a `Subscription` CR for the Lifecycle Agent:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: openshift-lifecycle-agent-subscription
     namespace: openshift-lifecycle-agent
   spec:
     channel: "stable"
     name: lifecycle-agent
     source: redhat-operators
     sourceNamespace: openshift-marketplace
   ```

   1. Create the `Subscription` CR by running the following command:

      ```
      $ oc create -f <subscription_filename>.yaml
      ```

**Verification**

1. To verify that the installation succeeded, inspect the CSV resource by running the following command:

   ```
   $ oc get csv -n openshift-lifecycle-agent
   ```

   Example output:

```
NAME                              DISPLAY                     VERSION               REPLACES                           PHASE
lifecycle-agent.v{product-version}.0           Openshift Lifecycle Agent   {product-version}.0                Succeeded
```

1. Verify that the Lifecycle Agent is up and running by running the following command:

   ```
   $ oc get deploy -n openshift-lifecycle-agent
   ```

   Example output:

```
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
lifecycle-agent-controller-manager   1/1     1            1           14s
```

##### [17.2.1.2. Installing the Lifecycle Agent by using the web console](#cnf-image-based-upgrade-installing-lifecycle-agent-using-web-console_ibi-preparing-image-based-install) Copy linkLink copied to clipboard!

You can use the OpenShift Container Platform web console to install the Lifecycle Agent.

**Prerequisites**

* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. In the OpenShift Container Platform web console, navigate to **Ecosystem** → **Software Catalog**.
2. Search for the **Lifecycle Agent** from the list of available Operators, and then click **Install**.
3. On the **Install Operator** page, under **A specific namespace on the cluster** select **openshift-lifecycle-agent**.
4. Click **Install**.

**Verification**

1. To confirm that the installation is successful:

   1. Click **Ecosystem** → **Installed Operators**.
   2. Ensure that the Lifecycle Agent is listed in the **openshift-lifecycle-agent** project with a **Status** of **InstallSucceeded**.

      Note

      During installation an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message.

If the Operator is not installed successfully:

1. Click **Ecosystem** → **Installed Operators**, and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**.
2. Click **Workloads** → **Pods**, and check the logs for pods in the **openshift-lifecycle-agent** project.

#### [17.2.2. Configuring a shared container partition between ostree stateroots](#cnf-image-based-upgrade-shared-container-partition_ibi-preparing-image-based-install) Copy linkLink copied to clipboard!

Important

You must complete this procedure at installation time.

Apply a `MachineConfig` to the seed cluster to create a separate partition and share the `/var/lib/containers` partition between the two `ostree` stateroots that will be used during the preinstall process.

**Procedure**

* Apply a `MachineConfig` to create a separate partition:

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfig
  metadata:
    labels:
      machineconfiguration.openshift.io/role: master
    name: 98-var-lib-containers-partitioned
  spec:
    config:
      ignition:
        version: 3.2.0
      storage:
        disks:
          - device: /dev/disk/by-path/<root_disk>
            partitions:
              - label: var-lib-containers
                startMiB: <start_of_partition>
                sizeMiB: <partition_size>
        filesystems:
          - device: /dev/disk/by-partlabel/var-lib-containers
            format: xfs
            mountOptions:
              - defaults
              - prjquota
            path: /var/lib/containers
            wipeFilesystem: true
      systemd:
        units:
          - contents: |-
              # Generated by Butane
              [Unit]
              Before=local-fs.target
              Requires=systemd-fsck@dev-disk-by\x2dpartlabel-var\x2dlib\x2dcontainers.service
              After=systemd-fsck@dev-disk-by\x2dpartlabel-var\x2dlib\x2dcontainers.service

              [Mount]
              Where=/var/lib/containers
              What=/dev/disk/by-partlabel/var-lib-containers
              Type=xfs
              Options=defaults,prjquota

              [Install]
              RequiredBy=local-fs.target
            enabled: true
            name: var-lib-containers.mount
  ```

  where:

  `<root_disk>`
  :   Specifies the root disk, for example `pci-0000:01:00.0-scsi-0:2:0:0`.

  `<start_of_partition>`
  :   Specifies the start of the partition in MiB. If the value is too small, the installation will fail.

  `<partition_size>`
  :   Specifies a minimum size for the partition of 500 GB (512000 MiB) to ensure adequate disk space for precached images. If the value is too small, the deployments after installation will fail.

#### [17.2.3. Seed image configuration](#cnf-image-based-upgrade-seed-image-config_ibi-preparing-image-based-install) Copy linkLink copied to clipboard!

You can create a seed image from a single-node OpenShift cluster with the same hardware as your bare-metal host, and with a similar target cluster configuration. However, the seed image generated from the seed cluster cannot contain any cluster-specific configuration.

The following table lists the components, resources, and configurations that you must and must not include in your seed image:

Expand

Table 17.2. Seed image configuration

| Cluster configuration | Include in seed image |
| --- | --- |
| Performance profile | Yes |
| `MachineConfig` resources for the target cluster | Yes |
| IP version configuration, either IPv4, IPv6, or dual-stack networking | Yes |
| Set of Day 2 Operators, including the Lifecycle Agent and the OADP Operator | Yes |
| Disconnected registry configuration [2] | Yes |
| Valid proxy configuration [3] | Yes |
| FIPS configuration | Yes |
| Dedicated partition on the primary disk for container storage that matches the size of the target clusters | Yes |
| Local volumes  * `StorageClass` used in `LocalVolume` for LSO * `LocalVolume` for LSO * `LVMCluster` CR for LVMS | No |

Show more

1. If the seed cluster is installed in a disconnected environment, the target clusters must also be installed in a disconnected environment.
2. The proxy configuration must be either enabled or disabled in both the seed and target clusters. However, the proxy servers configured on the clusters does not have to match.

##### [17.2.3.1. Seed image configuration using the RAN DU profile](#ztp-image-based-upgrade-seed-image-config-ran_ibi-preparing-image-based-install) Copy linkLink copied to clipboard!

The following table lists the components, resources, and configurations that you must and must not include in the seed image when using the RAN DU profile:

Expand

Table 17.3. Seed image configuration with RAN DU profile

| Resource | Include in seed image |
| --- | --- |
| All extra manifests that are applied as part of Day 0 installation | Yes |
| All Day 2 Operator subscriptions | Yes |
| `DisableOLMPprof.yaml` | Yes |
| `TunedPerformancePatch.yaml` | Yes |
| `PerformanceProfile.yaml` | Yes |
| `SriovOperatorConfig.yaml` | Yes |
| `DisableSnoNetworkDiag.yaml` | Yes |
| `StorageClass.yaml` | No, if it is used in `StorageLV.yaml` |
| `StorageLV.yaml` | No |
| `StorageLVMCluster.yaml` | No |
| `SriovFecClusterConfig.yaml` | No |
| `SriovVrbClusterConfig.yaml` | No |

Show more

The following list of resources and configurations can be applied as extra manifests or by using RHACM policies:

* `ClusterLogForwarder.yaml`
* `ReduceMonitoringFootprint.yaml`
* `PtpOperatorConfigForEvent.yaml`
* `DefaultCatsrc.yaml`
* `PtpConfig.yaml`
* `SriovNetwork.yaml`

Important

If you are using GitOps ZTP, enable these resources by using RHACM policies to ensure configuration changes can be applied throughout the cluster lifecycle.

#### [17.2.4. Generating a seed image with the Lifecycle Agent](#cnf-image-based-upgrade-generate-seed-image_ibi-preparing-image-based-install) Copy linkLink copied to clipboard!

Use the Lifecycle Agent to generate a seed image from a managed cluster. The Operator checks for required system configurations, performs any necessary system cleanup before generating the seed image, and launches the image generation. The seed image generation includes the following tasks:

* Stopping cluster Operators
* Preparing the seed image configuration
* Generating and pushing the seed image to the image repository specified in the `SeedGenerator` CR
* Restoring cluster Operators
* Expiring seed cluster certificates
* Generating new certificates for the seed cluster
* Restoring and updating the `SeedGenerator` CR on the seed cluster

**Prerequisites**

* RHACM and multicluster engine for Kubernetes Operator are not installed on the seed cluster.
* You have configured a shared container directory on the seed cluster.
* You have installed the minimum version of the OADP Operator and the Lifecycle Agent on the seed cluster.
* Ensure that persistent volumes are not configured on the seed cluster.
* Ensure that the `LocalVolume` CR does not exist on the seed cluster if the Local Storage Operator is used.
* Ensure that the `LVMCluster` CR does not exist on the seed cluster if LVM Storage is used.
* Ensure that the `DataProtectionApplication` CR does not exist on the seed cluster if OADP is used.

**Procedure**

1. Detach the managed cluster from the hub to delete any RHACM-specific resources from the seed cluster that must not be in the seed image:

   1. Manually detach the seed cluster by running the following command:

      ```
      $ oc delete managedcluster sno-worker-example
      ```

      1. Wait until the managed cluster is removed. After the cluster is removed, create the proper `SeedGenerator` CR. The Lifecycle Agent cleans up the RHACM artifacts.
   2. If you are using GitOps ZTP, detach your cluster by removing the seed cluster’s `ClusterInstance` CR from the `kustomization.yaml`.

      1. If you have a `kustomization.yaml` file that references multiple `ClusterInstance` CRs, remove your seed cluster’s `ClusterInstance` CR from the `kustomization.yaml`:

         ```
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization

         resources:
         #- clusterinstance-seed-sno1.yaml
         - clusterinstance-target-sno2.yaml
         - clusterinstance-target-sno3.yaml
         ```
      2. If you have a `kustomization.yaml` that references one `ClusterInstance` CR, remove your seed cluster’s `ClusterInstance` CR from the `kustomization.yaml` and add the `resources: []` line:

         ```
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization

         resources: []
         ```
      3. Commit the `kustomization.yaml` changes in your Git repository and push the changes to your repository.

         The ArgoCD pipeline detects the changes and removes the managed cluster.
2. Create the `Secret` object so that you can push the seed image to your registry.

   1. Create the authentication file by running the following commands:

      ```
      $ MY_USER=myuserid
      ```

      ```
      $ AUTHFILE=/tmp/my-auth.json
      ```

      ```
      $ podman login --authfile ${AUTHFILE} -u ${MY_USER} quay.io/${MY_USER}
      ```

      ```
      $ base64 -w 0 ${AUTHFILE} ; echo
      ```
   2. Copy the output into the `seedAuth` field in the `Secret` YAML file named `seedgen` in the `openshift-lifecycle-agent` namespace:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
        name: <secret_name>
        namespace: openshift-lifecycle-agent
      type: Opaque
      data:
        seedAuth: <encoded_authfile>
      ```

      where:

      `<secret_name>`
      :   Specifies the name of the `Secret` resource. The value must be `seedgen`.

      `<encoded_authfile>`
      :   Specifies a base64-encoded authfile for write-access to the registry for pushing the generated seed images.
   3. Apply the `Secret` by running the following command:

      ```
      $ oc apply -f secretseedgenerator.yaml
      ```
3. Create the `SeedGenerator` CR:

   ```
   apiVersion: lca.openshift.io/v1
   kind: SeedGenerator
   metadata:
     name: <seedgenerator_name>
   spec:
     seedImage: <seed_container_image>
   ```

   where:

   `<seedgenerator_name>`
   :   Specifies the name of the `SeedGenerator` CR. The value must be `seedimage`.

   `<seed_container_image>`
   :   Specifies the container image URL, for example, `quay.io/example/seed-container-image:<tag>`. It is recommended to use the `<seed_cluster_name>:<ocp_version>` format.
4. Generate the seed image by running the following command:

   ```
   $ oc apply -f seedgenerator.yaml
   ```

   Important

   The cluster reboots and loses API capabilities while the Lifecycle Agent generates the seed image. Applying the `SeedGenerator` CR stops the `kubelet` and the CRI-O operations, then it starts the image generation.

**Verification**

* After the cluster recovers and it is available, you can check the status of the `SeedGenerator` CR by running the following command:

  ```
  $ oc get seedgenerator -o yaml
  ```

  The following example shows the output when the seed image generation is complete:

  ```
  status:
    conditions:
    - lastTransitionTime: "2024-02-13T21:24:26Z"
      message: Seed Generation completed
      observedGeneration: 1
      reason: Completed
      status: "False"
      type: SeedGenInProgress
    - lastTransitionTime: "2024-02-13T21:24:26Z"
      message: Seed Generation completed
      observedGeneration: 1
      reason: Completed
      status: "True"
      type: SeedGenCompleted
    observedGeneration: 1
  ```

  The `SeedGenCompleted` type indicates that the seed image generation is complete.

  Important

  After the seed image generation completes, do not use the seed cluster. Do not continue to run `oc` commands against the seed cluster or use it to manage managed clusters.

  If you access the seed cluster after generating the seed image, you can meet TLS certificate validation errors because the seed cluster certificates expire during seed image generation. If you need to generate another seed image, provision a new seed cluster.

### [17.3. Preinstalling single-node OpenShift using an image-based installation](#ibi-factory-image-based-install) Copy linkLink copied to clipboard!

Use the `openshift-install` program to create a live installation ISO for preinstalling single-node OpenShift on bare-metal hosts. For more information about downloading the installation program, see "Installation process" in the "Additional resources" section.

The installation program takes a seed image URL and other inputs, such as the release version of the seed image and the disk to use for the installation process, and creates a live installation ISO. You can then start the host using the live installation ISO to begin preinstallation. When preinstallation is complete, the host is ready to ship to a remote site for the final site-specific configuration and deployment.

The following are the high-level steps to preinstall a single-node OpenShift cluster using an image-based installation:

* Generate a seed image.
* Create a live installation ISO using the `openshift-install` installation program.
* Boot the host using the live installation ISO to preinstall the host.

#### [17.3.1. Creating a live installation ISO for a single-node OpenShift image-based installation](#ibi-create-iso-for-bmh_ibi-factory-image-based-install) Copy linkLink copied to clipboard!

You can embed your single-node OpenShift seed image URL, and other installation artifacts, in a live installation ISO by using the `openshift-install` program.

Note

For more information about the specification for the `image-based-installation-config.yaml` manifest, see the section "Reference specifications for the `image-based-installation-config.yaml` manifest".

**Prerequisites**

* You generated a seed image from a single-node OpenShift seed cluster.
* You downloaded the `openshift-install` program. The version of the `openshift-install` program must match the OpenShift Container Platform version in your seed image.
* The target host has network access to the seed image URL and all other installation artifacts.
* If you require static networking, you must install the `nmstatectl` library on the host that creates the live installation ISO.

**Procedure**

1. Create a live installation ISO and embed your single-node OpenShift seed image URL and other installation artifacts:

   1. Create a working directory by running the following:

      ```
      $ mkdir <working_directory>
      ```

      where `<working_directory>` is the name of your working directory, for example `ibi-iso-workdir`.
   2. Optional. Create an installation configuration template to use as a reference when configuring the `ImageBasedInstallationConfig` resource:

      ```
      $ openshift-install image-based create image-config-template --dir <working_directory>
      ```

      where `<working_directory>` is the name of your working directory, for example `ibi-iso-workdir`. If you do not specify a working directory, the command uses the current directory.

      Example output:

```
INFO Image-Config-Template created in: ibi-iso-workdir
```

+ The command creates the `image-based-installation-config.yaml` installation configuration template in your target directory:

+

```
#
# Note: This is a sample ImageBasedInstallationConfig file showing
# which fields are available to aid you in creating your
# own image-based-installation-config.yaml file.
#
apiVersion: v1beta1
kind: ImageBasedInstallationConfig
metadata:
  name: example-image-based-installation-config
# The following fields are required
seedImage: quay.io/openshift-kni/seed-image:4.22.0
seedVersion: 4.22.0
installationDisk: /dev/vda
pullSecret: '<your_pull_secret>'
# networkConfig is optional and contains the network configuration for the host in NMState format.
# See https://nmstate.io/examples.html for examples.
# networkConfig:
#   interfaces:
#     - name: eth0
#       type: ethernet
#       state: up
#       mac-address: 00:00:00:00:00:00
#       ipv4:
#         enabled: true
#         address:
#           - ip: 192.168.122.2
#             prefix-length: 23
#         dhcp: false
```

1. Edit your installation configuration file:

   Example `image-based-installation-config.yaml` file:

```
apiVersion: v1beta1
kind: ImageBasedInstallationConfig
metadata:
  name: example-image-based-installation-config
seedImage: quay.io/repo-id/seed:latest
seedVersion: "4.22.0"
extraPartitionStart: "-240G"
installationDisk: /dev/disk/by-id/wwn-0x62c...
sshKey: 'ssh-ed25519 AAAA...'
pullSecret: '{"auths": ...}'
networkConfig:
    interfaces:
      - name: ens1f0
        type: ethernet
        state: up
        ipv4:
          enabled: true
          dhcp: false
          auto-dns: false
          address:
            - ip: 192.168.200.25
              prefix-length: 24
        ipv6:
          enabled: false
    dns-resolver:
      config:
        server:
          - 192.168.15.47
          - 192.168.15.48
    routes:
      config:
      - destination: 0.0.0.0/0
        metric: 150
        next-hop-address: 192.168.200.254
        next-hop-interface: ens1f0
```

1. Create the live installation ISO by running the following command:

   ```
   $ openshift-install image-based create image --dir ibi-iso-workdir
   ```

   Example output:

```
INFO Consuming Image-based Installation ISO Config from target directory
INFO Creating Image-based Installation ISO with embedded ignition
```

**Verification**

* View the output in the working directory:

  ```
  ibi-iso-workdir/
    └── rhcos-ibi.iso
  ```

##### [17.3.1.1. Configuring additional partitions on the target host](#ibi-extra-partition-ibi-install-iso_ibi-factory-image-based-install) Copy linkLink copied to clipboard!

The installation ISO creates a partition for the `/var/lib/containers` directory as part of the image-based installation process.

You can create additional partitions by using the `coreosInstallerArgs` specification. For example, in hard disks with adequate storage, you might need an additional partition for storage options, such as Logical Volume Manager (LVM) Storage.

Note

The `/var/lib/containers` partition requires at least 500 GB to ensure adequate disk space for precached images. You must create additional partitions with a starting position larger than the partition for `/var/lib/containers`.

**Procedure**

1. Edit the `image-based-installation-config.yaml` file to configure additional partitions:

   Example `image-based-installation-config.yaml` file:

```
apiVersion: v1beta1
kind: ImageBasedInstallationConfig
metadata:
  name: example-extra-partition
seedImage: quay.io/repo-id/seed:latest
seedVersion: "4.22.0"
installationDisk: /dev/sda
pullSecret: '{"auths": ...}'
# ...
skipDiskCleanup: <skip_disk_cleanup>
coreosInstallerArgs:
   - "--save-partindex"
   - "<partition_index>"
ignitionConfigOverride: |
  {
    "ignition": {
      "version": "3.2.0"
    },
    "storage": {
      "disks": [
        {
          "device": "<installation_disk>",
          "partitions": [
            {
              "label": "<partition_label>",
              "number": <partition_number>,
              "sizeMiB": <partition_size>,
              "startMiB": <starting_position>
            }
          ]
        }
      ]
    }
  }
```

+ where:

+ `<skip_disk_cleanup>`:: Specifies whether to skip disk formatting during the installation process. Set to `true` to skip. `"--save-partindex"`:: Specifies the argument to preserve a partition. `<partition_index>`:: Specifies the additional partition to preserve. The live installation ISO requires five partitions. Set a number greater than five, for example `6`. `<installation_disk>`:: Specifies the installation disk on the target host, for example `/dev/sda`. `<partition_label>`:: Specifies the label for the partition, for example `storage`. `<partition_number>`:: Specifies the number for the partition, for example `6`. `<partition_size>`:: Specifies the size of partition in MiB, for example `380000`. `<starting_position>`:: Specifies the starting position on the disk in MiB for the additional partition. You must specify a starting point larger than the partition for `/var/lib/containers`, for example `500000`.

**Verification**

* When you complete the preinstallation of the host with the live installation ISO, login to the target host and run the following command to view the partitions:

  ```
  $ lsblk
  ```

  Example output:

```
sda    8:0    0  140G  0 disk
├─sda1 8:1    0    1M  0 part
├─sda2 8:2    0  127M  0 part
├─sda3 8:3    0  384M  0 part /var/mnt/boot
├─sda4 8:4    0  120G  0 part /var/mnt
├─sda5 8:5    0  500G  0 part /var/lib/containers
└─sda6 8:6    0  380G  0 part
```

#### [17.3.2. Provisioning the live installation ISO to a host](#ibi-provision-install-iso-to-bmh_ibi-factory-image-based-install) Copy linkLink copied to clipboard!

You can provision a live installation ISO to a bare-metal host to preinstall single-node OpenShift.

**Procedure**

* Using your preferred method, boot the target bare-metal host from the `rhcos-ibi.iso` live installation ISO to preinstall single-node OpenShift.

**Verification**

1. Login to the target host.
2. View the system logs by running the following command:

   ```
   $ journalctl -b
   ```

   Example output:

```
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13T17:01:44Z" level=info msg="All the precaching threads have finished."
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13T17:01:44Z" level=info msg="Total Images: 125"
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13T17:01:44Z" level=info msg="Images Pulled Successfully: 125"
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13T17:01:44Z" level=info msg="Images Failed to Pull: 0"
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13T17:01:44Z" level=info msg="Completed executing pre-caching"
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13T17:01:44Z" level=info msg="Pre-cached images successfully."
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13 17:01:44" level=info msg="Skipping shutdown"
Aug 13 17:01:44 10.46.26.129 install-rhcos-and-restore-seed.sh[2876]: time="2024-08-13 17:01:44" level=info msg="IBI preparation process finished successfully!"
Aug 13 17:01:44 10.46.26.129 systemd[1]: var-lib-containers-storage-overlay.mount: Deactivated successfully.
Aug 13 17:01:44 10.46.26.129 systemd[1]: Finished SNO Image-based Installation.
Aug 13 17:01:44 10.46.26.129 systemd[1]: Reached target Multi-User System.
Aug 13 17:01:44 10.46.26.129 systemd[1]: Reached target Graphical Interface.
```

#### [17.3.3. Reference specifications for the image-based-installation-config.yaml manifest](#ibi-installer-installation-config_ibi-factory-image-based-install) Copy linkLink copied to clipboard!

The following content describes the specifications for the `image-based-installation-config.yaml` manifest.

The `openshift-install` program uses the `image-based-installation-config.yaml` manifest to create a live installation ISO for image-based installations of single-node OpenShift.

Expand

Table 17.4. Required specifications

| Specification | Type | Description |
| --- | --- | --- |
| `seedImage` | `string` | Specifies the seed image to use in the ISO generation process. |
| `seedVersion` | `string` | Specifies the OpenShift Container Platform release version of the seed image. The release version in the seed image must match the release version that you specify in the `seedVersion` field. |
| `installationDisk` | `string` | Specifies the disk that will be used for the installation process.  Because the disk discovery order is not guaranteed, the kernel name of the disk can change across booting options for machines with multiple disks. For example, `/dev/sda` becomes `/dev/sdb` and vice versa. To avoid this issue, you must use a persistent disk attribute, such as the disk World Wide Name (WWN), for example: `/dev/disk/by-id/wwn-<disk-id>`. |
| `pullSecret` | `string` | Specifies the pull secret to use during the precache process. The pull secret contains authentication credentials for pulling the release payload images from the container registry.  If the seed image requires a separate private registry authentication, add the authentication details to the pull secret. |

Show more

Expand

Table 17.5. Optional specifications

| Specification | Type | Description |
| --- | --- | --- |
| `shutdown` | `boolean` | Specifies if the host shuts down after the installation process completes. The default value is `false`. |
| `extraPartitionStart` | `string` | Specifies the start of the extra partition used for `/var/lib/containers`. The default value is `-40G`, which means that the partition will be exactly 40GiB in size and uses the space 40GiB from the end of the disk. If you specify a positive value, the partition will start at that position of the disk and extend to the end of the disk. |
| `extraPartitionLabel` | `string` | The label of the extra partition you use for `/var/lib/containers`. The default partition label is `var-lib-containers`.  Note  You must ensure that the partition label in the installation ISO matches the partition label set in the machine configuration for the seed image. If the partition labels are different, the partition mount fails during installation on the host. For more information, see "Configuring a shared container partition between ostree stateroots". |
| `extraPartitionNumber` | `unsigned integer` | The number of the extra partition you use for `/var/lib/containers`. The default number is `5`. |
| `skipDiskCleanup` | `boolean` | The installation process formats the disk on the host. Set this specification to 'true' to skip this step. The default is `false`. |
| `networkConfig` | `string` | Specifies networking configurations for the host, for example:  ``` networkConfig:     interfaces:       - name: ens1f0         type: ethernet         state: up         ... ```  If you require static networking, you must install the `nmstatectl` library on the host that creates the live installation ISO. For further information about defining network configurations by using `nmstate`, see [nmstate.io](https://nmstate.io/).  Important  The name of the interface must match the actual NIC name as shown in the operating system. |
| `proxy` | `string` | Specifies proxy settings to use during the installation ISO generation, for example:  ``` proxy:   httpProxy: "http://proxy.example.com:8080"   httpsProxy: "http://proxy.example.com:8080"   noProxy: "no_proxy.example.com" ``` |
| `imageDigestSources` | `string` | Specifies the sources or repositories for the release-image content, for example:  ``` imageDigestSources:   - mirrors:       - "registry.example.com:5000/ocp4/openshift4"     source: "quay.io/openshift-release-dev/ocp-release" ``` |
| `additionalTrustBundle` | `string` | Specifies the PEM-encoded X.509 certificate bundle. The installation program adds this to the `/etc/pki/ca-trust/source/anchors/` directory in the installation ISO.  ``` additionalTrustBundle: |   -----BEGIN CERTIFICATE-----   MTICLDCCAdKgAwfBAgIBAGAKBggqhkjOPQRDAjB9MQswCQYRVEQGE   ...   l2wOuDwKQa+upc4GftXE7C//4mKBNBC6Ty01gUaTIpo=   -----END CERTIFICATE----- ``` |
| `sshKey` | `string` | Specifies the SSH key to authenticate access to the host. |
| `ignitionConfigOverride` | `string` | Specifies a JSON string containing the user overrides for the Ignition config. The configuration merges with the Ignition config file generated by the installation program. This feature requires Ignition version is 3.2 or later. |
| `coreosInstallerArgs` | `string` | Specifies custom arguments for the `coreos-install` command that you can use to configure kernel arguments and disk partitioning options. |

Show more

### [17.4. Deploying single-node OpenShift clusters](#deploying-single-node-openshift-clusters) Copy linkLink copied to clipboard!

#### [17.4.1. About image-based deployments for managed single-node OpenShift](#ibi-edge-image-based-install) Copy linkLink copied to clipboard!

When a host preinstalled with single-node OpenShift using an image-based installation arrives at a remote site, a technician can easily reconfigure and deploy the host in a matter of minutes.

For clusters with a hub-and-spoke architecture, to complete the deployment of a preinstalled host, you must first define site-specific configuration resources on the hub cluster for each host. These resources contain configuration information such as the properties of the bare-metal host, authentication details, and other deployment and networking information.

The Image Based Install (IBI) Operator creates a configuration ISO from these resources, and then boots the host with the configuration ISO attached. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the single-node OpenShift cluster is ready.

Note

You must create distinct configuration resources for each bare-metal host.

See the following high-level steps to deploy a preinstalled host in a cluster with a hub-and-spoke architecture:

1. Install the IBI Operator on the hub cluster.
2. Create site-specific configuration resources in the hub cluster for each host.
3. The IBI Operator creates a configuration ISO from these resources and boots the target host with the configuration ISO attached.
4. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the single-node OpenShift cluster is ready.

Note

Alternatively, you can manually deploy a preinstalled host for a cluster without using a hub cluster. You must define an `ImageBasedConfig` resource and an installation manifest, and provide these as inputs to the `openshift-install` installation program. For more information, see "Deploying a single-node OpenShift cluster using the `openshift-install` program".

##### [17.4.1.1. Installing the Image Based Install Operator](#ibi-install-ibi-operator_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

The Image Based Install (IBI) Operator is part of the image-based deployment workflow for preinstalled single-node OpenShift on bare-metal hosts.

Note

The IBI Operator is part of the multicluster engine for Kubernetes Operator from MCE version 2.7.

**Prerequisites**

* You logged in as a user with `cluster-admin` privileges.
* You deployed a Red Hat Advanced Cluster Management (RHACM) hub cluster or you deployed the multicluster engine for Kubernetes Operator.
* You reviewed the required versions of software components in the section "Software prerequisites for an image-based installation".

**Procedure**

* Set the `enabled` specification to `true` for the `image-based-install-operator` component in the `MultiClusterEngine` resource by running the following command:

  ```
  $ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type json \
  --patch '[{"op": "add", "path":"/spec/overrides/components/-", "value": {"name":"image-based-install-operator","enabled": true}}]'
  ```

**Verification**

* Check that the Image Based Install Operator pod is running by running the following command:

  ```
  $ oc get pods -A | grep image-based
  ```

  Example output:

  ```
  multicluster-engine             image-based-install-operator-57fb8sc423-bxdj8             2/2     Running     0               5m
  ```

##### [17.4.1.2. Deploying a managed single-node OpenShift cluster using the IBI Operator](#ibi-create-config-iso_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

Create the site-specific configuration resources in the hub cluster to initiate the image-based deployment of a preinstalled host.

When you create these configuration resources in the hub cluster, the Image Based Install (IBI) Operator generates a configuration ISO and attaches it to the target host to begin the site-specific configuration process. When the configuration process completes, the single-node OpenShift cluster is ready.

Note

For more information about the configuration resources that you must configure in the hub cluster, see "Cluster configuration resources for deploying a preinstalled host".

**Prerequisites**

* You preinstalled a host with single-node OpenShift using an image-based installation.
* You logged in as a user with `cluster-admin` privileges.
* You deployed a Red Hat Advanced Cluster Management (RHACM) hub cluster or you deployed the multicluster engine for Kubernetes operator (MCE).
* You installed the IBI Operator on the hub cluster.
* You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets".

**Procedure**

1. Create the `ibi-ns` namespace by running the following command:

   ```
   $ oc create namespace ibi-ns
   ```
2. Create the `Secret` resource for your image registry:

   1. Create a YAML file that defines the `Secret` resource for your image registry:

      Example `secret-image-registry.yaml` file:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
        name: ibi-image-pull-secret
        namespace: ibi-ns
      stringData:
        .dockerconfigjson: <base64_docker_auth_code>
      type: kubernetes.io/dockerconfigjson
      ```

      where:

      `<base64_docker_auth_code>`
      :   Specifies base64-encoded credential details. See the "Additional resources" section for more information about using image pull secrets.
   2. Create the `Secret` resource for your image registry by running the following command:

      ```
      $ oc create -f secret-image-registry.yaml
      ```
3. Optional: Configure static networking for the host:

   1. Create a `Secret` resource containing the static network configuration in `nmstate` format:

      Example `host-network-config-secret.yaml` file:

      ```
      apiVersion: v1
      kind: Secret
      metadata:
       name: <network_secret_name>
       namespace: ibi-ns
      type: Opaque
      stringData:
       nmstate: |
        interfaces:
          - name: <interface_name>
            type: ethernet
            state: up
            ipv4:
              enabled: true
              address:
                - ip: 192.168.200.25
                  prefix-length: 24
              dhcp: false
            ipv6:
              enabled: false
        dns-resolver:
          config:
            server:
              - <dns_server_1>
              - 192.168.15.48
        routes:
          config:
            - destination: 0.0.0.0/0
              metric: 150
              next-hop-address: 192.168.200.254
              next-hop-interface: <interface_name>
              table-id: 254
      ```

      where:

      `<network_secret_name>`
      :   Specifies the name for the `Secret` resource, for example `host-network-config-secret`.

      `nmstate`
      :   Specifies the static network configuration in `nmstate` format.

      `<interface_name>`
      :   Specifies the name of the interface on the host, for example `ens1f0`. The name of the interface must match the actual NIC name as shown in the operating system. To use your MAC address for NIC matching, set the `identifier` field to `mac-address`.

      `dhcp: false`
      :   Specifies that DHCP is disabled to ensure `nmstate` assigns the static IP address to the interface.

      `<dns_server_1>`
      :   Specifies one or more DNS servers that the system will use to resolve domain names, for example `192.168.15.47`.

      `config`
      :   Specifies the default route through the `ens1f0` interface to the next hop IP address `192.168.200.254`.
4. Create the `BareMetalHost` and `Secret` resources:

   1. Create a YAML file that defines the `BareMetalHost` and `Secret` resources:

      Example `ibi-bmh.yaml` file:

      ```
      apiVersion: metal3.io/v1alpha1
      kind: BareMetalHost
      metadata:
        name: <baremetalhost_name>
        namespace: ibi-ns
      spec:
        online: <online_status>
        bootMACAddress: <boot_mac_address>
        bmc:
          address: <bmc_address>
          credentialsName: <bmh_secret_name>
        preprovisioningNetworkDataName: <network_secret_name>
        automatedCleaningMode: disabled
        externallyProvisioned: true
      ---
      apiVersion: v1
      kind: Secret
      metadata:
        name: <bmh_secret_name>
        namespace: ibi-ns
      type: Opaque
      data:
        username: <username>
        password: <password>
      ```

      where:

      `<baremetalhost_name>`
      :   Specifies the name for the `BareMetalHost` resource, for example `ibi-bmh`.

      `<online_status>`
      :   Specifies if the host should be online, for example `false`.

      `<boot_mac_address>`
      :   Specifies the host boot MAC address, for example `00:a5:12:55:62:64`.

      `<bmc_address>`
      :   Specifies the BMC address, for example `redfish-virtualmedia+http://192.168.111.1:8000/redfish/v1/Systems/8a5babac-94d0-4c20-b282-50dc3a0a32b5`. You can only use bare-metal host drivers that support virtual media networking booting, for example redfish-virtualmedia and idrac-virtualmedia.

      `<bmh_secret_name>`
      :   Specifies the name of the bare-metal host `Secret` resource, for example `ibi-bmh-bmc-secret`.

      `<network_secret_name>`
      :   (Optional) Specifies the name of the `Secret` resource containing the static network configuration for the host, for example `host-network-config-secret`.

      `automatedCleaningMode: disabled`
      :   Specifies that automated cleaning is disabled to prevent the provisioning service from deleting all preinstallation artifacts, such as the seed image, during disk inspection.

      `externallyProvisioned: true`
      :   Specifies that the host is externally provisioned to enable it to boot from the preinstalled disk, instead of the configuration ISO.

      `<username>`
      :   Specifies the username for BMC authentication.

      `<password>`
      :   Specifies the password for BMC authentication.
   2. Create the `BareMetalHost` and `Secret` resources by running the following command:

      ```
      $ oc create -f ibi-bmh.yaml
      ```
5. Create the `ClusterImageSet` resource:

   1. Create a YAML file that defines the `ClusterImageSet` resource:

      Example `ibi-cluster-image-set.yaml` file:

      ```
      apiVersion: hive.openshift.io/v1
      kind: ClusterImageSet
      metadata:
        name: <clusterimageset_name>
      spec:
        releaseImage: <release_image>
      ```

      where:

      `<clusterimageset_name>`
      :   Specifies the name for the `ClusterImageSet` resource, for example `ibi-img-version-arch`.

      `<release_image>`
      :   Specifies the address for the release image to use for the deployment, for example `ibi.example.com:path/to/release/images:version-arch`. If you use a different image registry compared to the image registry used during seed image generation, ensure that the OpenShift Container Platform version for the release image remains the same.
   2. Create the `ClusterImageSet` resource by running the following command:

      ```
      $ oc apply -f ibi-cluster-image-set.yaml
      ```
6. Create the `ImageClusterInstall` resource:

   1. Create a YAML file that defines the `ImageClusterInstall` resource:

      Example `ibi-image-cluster-install.yaml` file:

      ```
      apiVersion: extensions.hive.openshift.io/v1alpha1
      kind: ImageClusterInstall
      metadata:
        name: <imageclusterinstall_name>
        namespace: ibi-ns
      spec:
        bareMetalHostRef:
          name: <baremetalhost_name>
          namespace: ibi-ns
        clusterDeploymentRef:
          name: <clusterdeployment_name>
        hostname: <cluster_hostname>
        imageSetRef:
          name: <clusterimageset_name>
        machineNetworks:
        - cidr: 10.0.0.0/24
        #- cidr: fd01::/64
        proxy:
          httpProxy: "http://proxy.example.com:8080"
          #httpsProxy: "http://proxy.example.com:8080"
          #noProxy: "no_proxy.example.com"
      ```

      where:

      `<imageclusterinstall_name>`
      :   Specifies the name for the `ImageClusterInstall` resource, for example `ibi-image-install`.

      `<baremetalhost_name>`
      :   Specifies the `BareMetalHost` resource that you want to target for the image-based installation, for example `ibi-bmh`.

      `<clusterdeployment_name>`
      :   Specifies the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host, for example `ibi-cluster-deployment`.

      `<cluster_hostname>`
      :   Specifies the hostname for the cluster, for example `ibi-host`.

      `<clusterimageset_name>`
      :   Specifies the name of the `ClusterImageSet` resource you used to define the container release images to use for deployment, for example `ibi-img-version-arch`.

      `machineNetworks`
      :   Specifies the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.

      `proxy`
      :   (Optional) Specifies a proxy to use for the cluster deployment.

          Important

          If your cluster deployment requires a proxy configuration, you must do the following:

          * Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
          * Configure the `machineNetwork` field in your installation manifest.
   2. Create the `ImageClusterInstall` resource by running the following command:

      ```
      $ oc create -f ibi-image-cluster-install.yaml
      ```
7. Create the `ClusterDeployment` resource:

   1. Create a YAML file that defines the `ClusterDeployment` resource:

      Example `ibi-cluster-deployment.yaml` file:

      ```
      apiVersion: hive.openshift.io/v1
      kind: ClusterDeployment
      metadata:
        name: <clusterdeployment_name>
        namespace: <namespace>
      spec:
        baseDomain: <base_domain>
        clusterInstallRef:
          group: extensions.hive.openshift.io
          kind: ImageClusterInstall
          name: <imageclusterinstall_name>
          version: v1alpha1
        clusterName: <cluster_name>
        platform:
          none: {}
        pullSecretRef:
          name: <pull_secret_name>
      ```

      where:

      `<clusterdeployment_name>`
      :   Specifies the name for the `ClusterDeployment` resource, for example `ibi-cluster-deployment`.

      `<namespace>`
      :   Specifies the namespace for the `ClusterDeployment` resource, for example `ibi-ns`.

      `<base_domain>`
      :   Specifies the base domain that the cluster should belong to, for example `example.com`.

      `<imageclusterinstall_name>`
      :   Specifies the name of the `ImageClusterInstall` in which you defined the container images to use for the image-based installation of the target host, for example `ibi-image-install`.

      `<cluster_name>`
      :   Specifies a name for the cluster, for example `ibi-cluster`.

      `<pull_secret_name>`
      :   Specifies the secret to use for pulling images from your image registry, for example `ibi-image-pull-secret`.
   2. Create the `ClusterDeployment` resource by running the following command:

      ```
      $ oc apply -f ibi-cluster-deployment.yaml
      ```
8. Create the `ManagedCluster` resource:

   1. Create a YAML file that defines the `ManagedCluster` resource:

      Example `ibi-managed.yaml` file:

      ```
      apiVersion: cluster.open-cluster-management.io/v1
      kind: ManagedCluster
      metadata:
        name: <managedcluster_name>
      spec:
        hubAcceptsClient: <hub_accepts_client>
      ```

      where:

      `<managedcluster_name>`
      :   Specifies the name for the `ManagedCluster` resource, for example `sno-ibi`.

      `<hub_accepts_client>`
      :   Specifies whether RHACM manages the cluster. Set to `true` to enable management.
   2. Create the `ManagedCluster` resource by running the following command:

      ```
      $ oc apply -f ibi-managed.yaml
      ```

**Verification**

1. Check the status of the `ImageClusterInstall` in the hub cluster to monitor the progress of the target host installation by running the following command:

   ```
   $ oc get imageclusterinstall
   ```

   Example output:

   ```
   NAME       REQUIREMENTSMET           COMPLETED                     BAREMETALHOSTREF
   target-0   HostValidationSucceeded   ClusterInstallationSucceeded  ibi-bmh
   ```

   Warning

   If the `ImageClusterInstall` resource is deleted, the IBI Operator reattaches the `BareMetalHost` resource and reboots the machine.
2. When the installation completes, you can retrieve the `kubeconfig` secret to log in to the managed cluster by running the following command:

   ```
   $ oc extract secret/<cluster_name>-admin-kubeconfig -n <cluster_namespace>  --to - > <directory>/<cluster_name>-kubeconfig
   ```

   where:

   `<cluster_name>`
   :   Specifies the name of the cluster.

   `<cluster_namespace>`
   :   Specifies the namespace of the cluster.

   `<directory>`
   :   Specifies the directory in which to create the file.

##### [17.4.1.2.1. Cluster configuration resources for deploying a preinstalled host](#ibi-managed-cluster-config-resources_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

To complete a deployment for a preinstalled host at a remote site, you must configure the following site-specifc cluster configuration resources in the hub cluster for each bare-metal host.

Expand

Table 17.6. Cluster configuration resources reference

| Resource | Description |
| --- | --- |
| `Namespace` | Namespace for the managed single-node OpenShift cluster. |
| `BareMetalHost` | Describes the physical host and its properties, such as the provisioning and hardware configuration. |
| `Secret` for the bare-metal host | Credentials for the host BMC. |
| `Secret` for the bare-metal host static network configuration | Optional: Describes static network configuration for the target host. |
| `Secret` for the image registry | Credentials for the image registry. The secret for the image registry must be of type `kubernetes.io/dockerconfigjson`. |
| `ImageClusterInstall` | References the bare-metal host, deployment, and image set resources. |
| `ClusterImageSet` | Describes the release images to use for the cluster. |
| `ClusterDeployment` | Describes networking, authentication, and platform-specific settings. |
| `ManagedCluster` | Describes cluster details to enable Red Hat Advanced Cluster Management (RHACM) to register and manage. |
| `ConfigMap` | Optional: Describes additional configurations for the cluster deployment, such as adding a bundle of trusted certificates for the host to ensure trusted communications for cluster services. |

Show more

##### [17.4.1.2.2. ImageClusterInstall resource API specifications](#ibi-image-cluster-install-api-spec_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

The following content describes the API specifications for the `ImageClusterInstall` resource. This resource is the endpoint for the Image Based Install Operator.

Expand

Table 17.7. Required specifications

| Specification | Type | Description |
| --- | --- | --- |
| `imageSetRef` | `string` | Specify the name of the `ClusterImageSet` resource that defines the release images for the deployment. |
| `hostname` | `string` | Specify the hostname for the cluster. |
| `sshKey` | `string` | Specify your SSH key to provide SSH access to the target host. |

Show more

Expand

Table 17.8. Optional specifications

| Specification | Type | Description |
| --- | --- | --- |
| `clusterDeploymentRef` | `string` | Specify the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host. |
| `clusterMetadata` | `string` | After the deployment completes, this specification is automatically populated with metadata information about the cluster, including the `cluster-admin` kubeconfig credentials for logging in to the cluster. |
| `imageDigestSources` | `string` | Specifies the sources or repositories for the release-image content, for example:  ``` imageDigestSources:   - mirrors:       - "registry.example.com:5000/ocp4/openshift4"     source: "quay.io/openshift-release-dev/ocp-release" ``` |
| `extraManifestsRefs` | `string` | Specify a `ConfigMap` resource containing additional manifests to be applied to the target cluster. |
| `bareMetalHostRef` | `string` | Specify the `bareMetalHost` resource to use for the cluster deployment |
| `machineNetworks` | `string` | Specify the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster. |
| `proxy` | `string` | Specifies proxy settings for the cluster, for example:  ``` proxy:   httpProxy: "http://proxy.example.com:8080"   httpsProxy: "http://proxy.example.com:8080"   noProxy: "no_proxy.example.com" ``` |
| `caBundleRef` | `string` | Specify a `ConfigMap` resource containing the new bundle of trusted certificates for the host. |

Show more

##### [17.4.1.3. ConfigMap resources for extra manifests](#ibi-extra-manifests-configmap_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

You can optionally create a `ConfigMap` resource to define additional manifests in an image-based deployment for managed single-node OpenShift clusters.

After you create the `ConfigMap` resource, reference it in the `ImageClusterInstall` resource. During deployment, the IBI Operator includes the extra manifests in the deployment.

##### [17.4.1.3.1. Creating a ConfigMap resource to add extra manifests in an image-based deployment](#ibi-create-extra-manifest-configmap_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

You can use a `ConfigMap` resource to add extra manifests to the image-based deployment for single-node OpenShift clusters.

The following example adds an single-root I/O virtualization (SR-IOV) network to the deployment.

Note

Filenames for extra manifests must not exceed 30 characters. Longer filenames might cause deployment failures.

Before you begin, ensure that:

* You preinstalled a host with single-node OpenShift using an image-based installation.
* You logged in as a user with `cluster-admin` privileges.

To create the `ConfigMap` resource, complete the following steps:

1. Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources:

   1. Create a YAML file that defines the resources, as in the following example:

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetworkNodePolicy
      metadata:
        name: "example-sriov-node-policy"
        namespace: openshift-sriov-network-operator
      spec:
        deviceType: vfio-pci
        isRdma: false
        nicSelector:
          pfNames: [ens1f0]
        nodeSelector:
          node-role.kubernetes.io/master: ""
        mtu: 1500
        numVfs: 8
        priority: 99
        resourceName: example-sriov-node-policy
      ---
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetwork
      metadata:
        name: "example-sriov-network"
        namespace: openshift-sriov-network-operator
      spec:
        ipam: |-
          {
          }
        linkState: auto
        networkNamespace: sriov-namespace
        resourceName: example-sriov-node-policy
        spoofChk: "on"
        trust: "off"
      ```
   2. Create the `ConfigMap` resource by running the following command:

      ```
      $ oc create configmap sr-iov-extra-manifest --from-file=sriov-extra-manifest.yaml -n <namespace>
      ```

      where:

      `<namespace>`
      :   Specifies the namespace that has the `ImageClusterInstall` resource, for example `ibi-ns`.

          Example output:

          ```
          configmap/sr-iov-extra-manifest created
          ```

          Note

          If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.
2. Reference the `ConfigMap` resource in the `spec.extraManifestsRefs` field of the `ImageClusterInstall` resource:

   ```
   #...
     spec:
       extraManifestsRefs:
       - name: sr-iov-extra-manifest
   #...
   ```

##### [17.4.1.3.2. Creating a ConfigMap resource to add a CA bundle in an image-based deployment](#ibi-create-ca-extra-manifest-configmap_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

You can use a `ConfigMap` resource to add a certificate authority (CA) bundle to the host to ensure trusted communications for cluster services.

After you create the `ConfigMap` resource, reference it in the `spec.caBundleRef` field of the `ImageClusterInstall` resource.

Before you begin, ensure that:

* You preinstalled a host with single-node OpenShift using an image-based installation.
* You logged in as a user with `cluster-admin` privileges.

To create the CA bundle `ConfigMap` resource, complete the following steps:

1. Create a CA bundle file called `tls-ca-bundle.pem`, as in the following example:

   ```
   -----BEGIN CERTIFICATE-----
   MIIDXTCCAkWgAwIBAgIJAKmjYKJbIyz3MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
   ...Custom CA certificate bundle...
   4WPl0Qb27Sb1xZyAsy1ww6MYb98EovazUSfjYr2EVF6ThcAPu4/sMxUV7He2J6Jd
   cA8SMRwpUbz3LXY=
   -----END CERTIFICATE-----
   ```
2. Create the `ConfigMap` object by running the following command:

   ```
   $ oc create configmap custom-ca --from-file=tls-ca-bundle.pem -n ibi-ns
   ```

   where:

   `custom-ca`
   :   Specifies the name for the `ConfigMap` resource.

   `tls-ca-bundle.pem`
   :   Specifies the key for the `data` entry in the `ConfigMap` resource. You must include a `data` entry with the `tls-ca-bundle.pem` key.

   `ibi-ns`
   :   Specifies the namespace that has the `ImageClusterInstall` resource.

       Example output:

       ```
       configmap/custom-ca created
       ```
3. Reference the `ConfigMap` resource in the `spec.caBundleRef` field of the `ImageClusterInstall` resource:

   ```
   #...
     spec:
       caBundleRef:
         name: custom-ca
   #...
   ```

#### [17.4.2. About image-based deployments for single-node OpenShift](#ibi-image-based-install-standalone) Copy linkLink copied to clipboard!

You can manually generate a configuration ISO by using the `openshift-install` program. Attach the configuration ISO to your preinstalled target host to complete the deployment.

##### [17.4.2.1. Deploying a single-node OpenShift cluster using the openshift-install program](#create-standalone-config-iso_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

You can use the `openshift-install` program to configure and deploy a host that you preinstalled with an image-based installation. To configure the target host with site-specific details, you must create the following resources:

* The `install-config.yaml` installation manifest
* The `image-based-config.yaml` manifest

The `openshift-install` program uses these resources to generate a configuration ISO that you attach to the preinstalled target host to complete the deployment.

Note

For more information about the specifications for the `image-based-config.yaml` manifest, see "Reference specifications for the image-based-config.yaml manifest".

**Prerequisites**

* You preinstalled a host with single-node OpenShift using an image-based installation.
* You downloaded the latest version of the `openshift-install` program.
* You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets".

**Procedure**

1. Create a working directory by running the following:

   ```
   $ mkdir <working_directory>
   ```

   where `<working_directory>` is the name of your working directory, for example `ibi-config-iso-workdir`.
2. Create the installation manifest:

   1. Create a YAML file that defines the `install-config` manifest, as in the following example:

      ```
      apiVersion: v1
      metadata:
        name: sno-cluster-name
      baseDomain: host.example.com
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
      networking:
        machineNetwork:
        - cidr: 192.168.200.0/24
        #- cidr: fd01::/64
      platform:
        none: {}
      fips: false
      cpuPartitioningMode: "AllNodes"
      pullSecret: '{"auths":{"<your_pull_secret>"}}}'
      sshKey: 'ssh-rsa <your_ssh_pub_key>'
      ```

      + For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format in the `machineNetwork` field. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.

      Important

      If your cluster deployment requires a proxy configuration, you must do the following:

      * Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
      * Configure the `machineNetwork` field in your installation manifest.
   2. Save the file in your working directory.
3. Optional. Create a configuration template in your working directory by running the following command:

   ```
   $ openshift-install image-based create config-template --dir ibi-config-iso-workdir/
   ```

   Example output:

   ```
   INFO Config-Template created in: ibi-config-iso-workdir
   ```

   The command creates the `image-based-config.yaml` configuration template in your working directory:

   ```
   #
   # Note: This is a sample ImageBasedConfig file showing
   # which fields are available to aid you in creating your
   # own image-based-config.yaml file.
   #
   apiVersion: v1beta1
   kind: ImageBasedConfig
   metadata:
     name: example-image-based-config
   additionalNTPSources:
     - 0.rhel.pool.ntp.org
     - 1.rhel.pool.ntp.org
   hostname: change-to-hostname
   releaseRegistry: quay.io
   # networkConfig contains the network configuration for the host in NMState format.
   # See https://nmstate.io/examples.html for examples.
   networkConfig:
     interfaces:
       - name: eth0
         type: ethernet
         state: up
         mac-address: 00:00:00:00:00:00
         ipv4:
           enabled: true
           address:
             - ip: 192.168.122.2
               prefix-length: 23
           dhcp: false
   ```
4. Edit your configuration file:

   Example `image-based-config.yaml` file:

   ```
   #
   # Note: This is a sample ImageBasedConfig file showing
   # which fields are available to aid you in creating your
   # own image-based-config.yaml file.
   #
   apiVersion: v1beta1
   kind: ImageBasedConfig
   metadata:
     name: sno-cluster-name
   additionalNTPSources:
     - 0.rhel.pool.ntp.org
     - 1.rhel.pool.ntp.org
   hostname: host.example.com
   releaseRegistry: quay.io
   # networkConfig contains the network configuration for the host in NMState format.
   # See https://nmstate.io/examples.html for examples.
   networkConfig:
       interfaces:
         - name: ens1f0
           type: ethernet
           state: up
           ipv4:
             enabled: true
             dhcp: false
             auto-dns: false
             address:
               - ip: 192.168.200.25
                 prefix-length: 24
           ipv6:
             enabled: false
       dns-resolver:
         config:
           server:
             - 192.168.15.47
             - 192.168.15.48
       routes:
         config:
         - destination: 0.0.0.0/0
           metric: 150
           next-hop-address: 192.168.200.254
           next-hop-interface: ens1f0
   ```
5. Create the configuration ISO in your working directory by running the following command:

   ```
   $ openshift-install image-based create config-image --dir ibi-config-iso-workdir/
   ```

   Example output:

   ```
   INFO Adding NMConnection file <ens1f0.nmconnection>
   INFO Consuming Install Config from target directory
   INFO Consuming Image-based Config ISO configuration from target directory
   INFO Config-Image created in: ibi-config-iso-workdir/auth
   ```

   View the output in the working directory:

   Example output:

   ```
   ibi-config-iso-workdir/
   ├── auth
   │   ├── kubeadmin-password
   │   └── kubeconfig
   └── imagebasedconfig.iso
   ```
6. Attach the `imagebasedconfig.iso` to the preinstalled host using your preferred method and restart the host to complete the configuration process and deploy the cluster.

**Verification**

When the configuration process completes on the host, access the cluster to verify its status.

1. Export the `kubeconfig` environment variable to your kubeconfig file by running the following command:

   ```
   $ export KUBECONFIG=ibi-config-iso-workdir/auth/kubeconfig
   ```
2. Verify that the cluster is responding by running the following command:

   ```
   $ oc get nodes
   ```

   Example output:

   ```
   NAME                                         STATUS   ROLES                  AGE     VERSION
   node/sno-cluster-name.host.example.com       Ready    control-plane,master   5h15m   v1.35.4
   ```

##### [17.4.2.1.1. Reference specifications for the image-based-config.yaml manifest](#ibi-installer-configuration-config_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

The following content describes the specifications for the `image-based-config.yaml` manifest.

The `openshift-install` program uses the `image-based-config.yaml` manifest to create a site-specific configuration ISO for image-based deployments of single-node OpenShift.

Expand

Table 17.9. Required specifications

| Specification | Type | Description |
| --- | --- | --- |
| `hostname` | `string` | Define the name of the node for the single-node OpenShift cluster. |

Show more

Expand

Table 17.10. Optional specifications

| Specification | Type | Description |
| --- | --- | --- |
| `networkConfig` | `string` | Specifies networking configurations for the host, for example:  ``` networkConfig:     interfaces:       - name: ens1f0         type: ethernet         state: up         ... ```  If you require static networking, you must install the `nmstatectl` library on the host that creates the live installation ISO. For further information about defining network configurations by using `nmstate`, see [nmstate.io](https://nmstate.io/).  Important  The name of the interface must match the actual NIC name as shown in the operating system. |
| `additionalNTPSources` | `string` | Specifies a list of NTP sources for all cluster hosts. These NTP sources are added to any existing NTP sources in the cluster. You can use the hostname or IP address for the NTP source. |
| `releaseRegistry` | `string` | Specifies the container image registry that you used for the release image of the seed cluster. |
| `nodeLabels` | `map[string]string` | Specifies custom node labels for the single-node OpenShift node, for example:  ``` nodeLabels:   node-role.kubernetes.io/edge: true   environment: production ``` |

Show more

##### [17.4.2.2. Configuring resources for extra manifests](#ibi-extra-manifest-standalone_ibi-edge-image-based-install) Copy linkLink copied to clipboard!

You can optionally define additional resources in an image-based deployment for single-node OpenShift clusters.

Create the additional resources in an `extra-manifests` folder in the same working directory that has the `install-config.yaml` and `image-based-config.yaml` manifests.

Note

Filenames for additional resources in the `extra-manifests` directory must not exceed 30 characters. Longer filenames might cause deployment failures.

The following example shows how to create a resource in the `extra-manifests` folder of your working directory to add an single-root I/O virtualization (SR-IOV) network to the deployment.

Note

If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.

**Prerequisites**

* You created a working directory with the `install-config.yaml` and `image-based-config.yaml` manifests

**Procedure**

1. Go to your working directory and create the `extra-manifests` folder by running the following command:

   ```
   $ mkdir extra-manifests
   ```
2. Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources in the `extra-manifests` folder:

   1. Create a YAML file that defines the resources, as shown in the following example:

      Note

      If the cluster nodes include Intel vRAN Boost (VRB1 or VRB2) hardware, you can include a `SriovVrbClusterConfig` resource in the extra manifests to configure the hardware.

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetworkNodePolicy
      metadata:
        name: "example-sriov-node-policy"
        namespace: openshift-sriov-network-operator
      spec:
        deviceType: vfio-pci
        isRdma: false
        nicSelector:
          pfNames: [ens1f0]
        nodeSelector:
          node-role.kubernetes.io/master: ""
        mtu: 1500
        numVfs: 8
        priority: 99
        resourceName: example-sriov-node-policy
      ---
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetwork
      metadata:
        name: "example-sriov-network"
        namespace: openshift-sriov-network-operator
      spec:
        ipam: |-
          {
          }
        linkState: auto
        networkNamespace: sriov-namespace
        resourceName: example-sriov-node-policy
        spoofChk: "on"
        trust: "off"
      ---
      apiVersion: sriovvrb.intel.com/v1
      kind: SriovVrbClusterConfig
      metadata:
        name: config
        namespace: vran-acceleration-operators
      spec:
        priority: 1
        nodeSelector:
          kubernetes.io/hostname: worker-node
        acceleratorSelector:
          pciAddress: 0000:07:00.0
        drainSkip: true
        physicalFunction:
          pfDriver: vfio-pci
          vfDriver: vfio-pci
          vfAmount: 2
          bbDevConfig:
            vrb2:
              pfMode: false
              numVfBundles: 2
              maxQueueSize: 1024
              downlink4G:
                aqDepthLog2: 4
                numAqsPerGroups: 16
                numQueueGroups: 0
              uplink4G:
                aqDepthLog2: 4
                numAqsPerGroups: 16
                numQueueGroups: 0
              downlink5G:
                aqDepthLog2: 4
                numAqsPerGroups: 16
                numQueueGroups: 4
              uplink5G:
                aqDepthLog2: 4
                numAqsPerGroups: 16
                numQueueGroups: 4
              qfft:
                aqDepthLog2: 4
                numAqsPerGroups: 16
                numQueueGroups: 4
              qmld:
                aqDepthLog2: 4
                numAqsPerGroups: 64
                numQueueGroups: 4
      ```

**Verification**

* When you create the configuration ISO, you can view the reference to the extra manifests in the `.openshift_install_state.json` file in your working directory:

  ```
   "*configimage.ExtraManifests": {
          "FileList": [
              {
                  "Filename": "extra-manifests/sriov-extra-manifest.yaml",
                  "Data": "YXBFDFFD..."
              }
          ]
      }
  ```

## [Chapter 18. Network reconfiguration for single-node OpenShift](#network-reconfiguration-for-single-node-openshift) Copy linkLink copied to clipboard!

### [18.1. Understand single-node OpenShift network reconfiguration](#cnf-understanding-sno-ip-configuration) Copy linkLink copied to clipboard!

Use the Lifecycle Agent to change the network configuration of a single-node OpenShift cluster without performing a full redeployment. This is critical for many edge computing use cases such as disaster recovery and network rehoming.

#### [18.1.1. Use cases for single-node OpenShift network reconfiguration](#cnf-sno-ip-configuration-use-cases_understanding-sno-ip-configuration) Copy linkLink copied to clipboard!

At the network far edge, changing a single-node OpenShift cluster’s core networking is an essential operation in many scenarios. For example, during disaster recovery, mobile deployments, or network migrations, you might need to change node IP addresses, gateways, DNS servers, or VLAN settings. However, these operations are high-risk because a misconfiguration can make the cluster unreachable and require a full redeployment.

The Lifecycle Agent uses the `IPConfig` custom resource (CR) to provide a declarative, stage-driven workflow that performs these changes safely and without a full cluster redeployment.

The following use cases highlight key scenarios for single-node OpenShift network reconfiguration:

Disaster recovery
:   After a site outage or major connectivity change, a single-node OpenShift cluster might need to move to a different uplink network. For example, you can reconfigure a cluster to use an IPv4 satellite connection as a backup if a primary 5G IPv6 network goes down.

Temporary and mobile deployments
:   Mobile infrastructure, such as cell-on-wheels units or new cell sites, often relies on temporary network connections. You can reconfigure these clusters as they move between uplink networks.

IoT network transitions
:   IoT gateway clusters at remote sites can be reconfigured when the underlying network infrastructure changes, such as switching ISPs or migrating to new IP address ranges across a facility.

Network consolidation and equipment upgrades
:   During network consolidation or infrastructure upgrades, you can migrate single-node OpenShift clusters to a new L2 or L3 environment with a deterministic, reversible process and minimal downtime.

#### [18.1.2. Workflow for single-node OpenShift network reconfiguration](#cnf-sno-ip-configuration-overview_understanding-sno-ip-configuration) Copy linkLink copied to clipboard!

The Lifecycle Agent uses a stage-driven workflow controlled through the `spec.stage` field in the `IPConfig` CR. The workflow consists of three stages.

**Figure 18.1. single-node OpenShift network reconfiguration stages**

Idle stage
:   The initial and final stage. In this stage, the Lifecycle Agent runs health checks, performs cleanup operations, and prepares the cluster for configuration changes. Transitioning to Idle after a successful configuration is the finalization point that removes rollback capability.

Config stage
:   Executes the network reconfiguration in two phases. The pre-pivot phase prepares a new stateroot, which is a bootable system state that has the updated network configuration, and reboots into it. The post-pivot phase applies the network changes, regenerates certificates, and waits for cluster stabilization.

Rollback stage
:   Reboots into the earlier stateroot. You can trigger a rollback manually or configure automatic rollback on failure.

    The network reconfiguration flow preserves the currently booted stateroot as a rollback target while preparing the new configuration in a new stateroot. This approach means the original configuration remains available for rollback until you finalize the change, only one reboot is required for the IP change, and the rollback process is fast because the earlier stateroot is already prepared.

#### [18.1.3. Supported network property changes](#cnf-sno-ip-configuration-supported-changes_understanding-sno-ip-configuration) Copy linkLink copied to clipboard!

The `IPConfig` CR supports the following network property changes:

* IPv4 and IPv6 address changes for single-stack or dual-stack clusters
* Machine network CIDR changes
* Default gateway changes
* DNS server list updates
* Optional VLAN ID changes on the `br-ex` uplink path
* Optional DNS response filtering changes on dual-stack clusters to filter IPv4 or IPv6

#### [18.1.4. Requirements and limitations for network reconfiguration](#cnf-sno-ip-configuration-requirements_understanding-sno-ip-configuration) Copy linkLink copied to clipboard!

Network reconfiguration by using the `IPConfig` CR has the following requirements:

* The cluster must be a single-node OpenShift cluster.
* The Lifecycle Agent must be installed.
* A baseline dnsmasq `MachineConfig` resource must exist, which is automatically installed by any single-node OpenShift installed directly or indirectly by the Assisted Installer, including Agent-based Installer (ABI), multicluster engine (MCE), and Red Hat Advanced Cluster Management (RHACM).
* All cluster operators must be available before starting a network reconfiguration.

Network reconfiguration by using the `IPConfig` CR has the following limitations:

* For dual-stack clusters, exactly one IPv4 address and one IPv6 address are supported per node.
* Only one NIC is supported. No bonding or link aggregation.
* You can configure a maximum of one VLAN ID on the `br-ex` uplink path.
* You must configure static networking on the host network. DHCP is not supported.
* You cannot add a VLAN to a cluster that does not already have VLAN configuration.
* Changing gateway or machine network without changing the address is not supported.
* Changing DNS servers without changing at least one IP address is not supported.
* You cannot set `spec.ipv4` on an IPv6-only cluster or `spec.ipv6` on an IPv4-only cluster.
* The resulting routing table must not have routes that overlap or conflict with the default route through the configured gateways.
* The cluster must not have a proxy network configuration.
* You cannot perform an image-based upgrade and a network reconfiguration at the same time.

### [18.2. Perform single-node OpenShift network reconfiguration](#cnf-configuring-sno-ip-configuration) Copy linkLink copied to clipboard!

You can perform a network reconfiguration on a single-node OpenShift cluster by editing the `IPConfig` custom resource (CR) and transitioning through the configuration stages.

#### [18.2.1. Perform a single-node OpenShift network reconfiguration](#cnf-changing-sno-ip-configuration_configuring-sno-ip-configuration) Copy linkLink copied to clipboard!

You can change the network configuration of a single-node OpenShift cluster by editing the `IPConfig` custom resource (CR) and transitioning through the configuration stages.

**Prerequisites**

* You have a single-node OpenShift cluster.
* You have installed the Lifecycle Agent.
* You have the new network configuration details, including IP addresses, gateways, and DNS servers.
* You have cluster administrator privileges.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Verify that the `IPConfig` CR exists and check its current state by running the following command:

   ```
   $ oc get ipc ipconfig -o yaml
   ```

   If the CR does not exist, verify that you installed the Lifecycle Agent.
2. Verify that the `spec.stage` field is set to `Idle`, the `Idle` status condition is set to `true`, and review the current network configuration in the `status` fields.

   Note

   You can only modify spec fields when the CR is in the `Idle` stage.
3. Edit the `IPConfig` CR to specify the new network configuration by running the following command:

   ```
   $ oc edit ipc ipconfig
   ```
4. Update the spec fields with your new network configuration. The following example shows a dual-stack configuration with VLAN and DNS settings:

   ```
   apiVersion: lca.openshift.io/v1
   kind: IPConfig
   metadata:
     name: ipconfig
   spec:
     stage: Idle
     ipv4:
       address: 192.0.2.10
       machineNetwork: 192.0.2.0/24
       gateway: 192.0.2.1
     ipv6:
       address: 2001:db8::10
       machineNetwork: 2001:db8::/64
       gateway: 2001:db8::1
     dnsServers:
     - 192.0.2.53
     - 2001:4860:4860::8888
     vlanID: 100
     dnsFilterOutFamily: none
     autoRollbackOnFailure:
       initMonitorTimeoutSeconds: 1800
   ```

   where:

   `spec.stage`
   :   Set this field to `Config` when you are ready to apply the new network settings.

   `spec.ipv4.address`
   :   Specifies the target IPv4 address. Must be within the machine network CIDR.

   `spec.ipv4.machineNetwork`
   :   Specifies the target machine network CIDR.

   `spec.ipv4.gateway`
   :   Specifies the target default gateway.

   `spec.dnsServers`
   :   Specifies an ordered list of DNS servers. The first server in the list is used as the primary DNS server. Use a maximum of two servers.

   `spec.vlanID`
   :   Specifies an optional VLAN ID. Only specify if the cluster already has VLAN configuration.

   `spec.dnsFilterOutFamily`
   :   Specifies optional DNS filtering for dual-stack clusters. Set to `ipv4` or `ipv6` to filter out A or AAAA records respectively.

   `spec.autoRollbackOnFailure.initMonitorTimeoutSeconds`
   :   Specifies the timeout in seconds for automatic rollback if the configuration does not complete. The default value is 1800 seconds, or 30 minutes.
5. After saving the configuration, change the stage to `Config` to start the network reconfiguration by running the following command:

   ```
   $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Config"}}'
   ```

   Note

   After triggering the network reconfiguration, update your external DNS servers to resolve the cluster’s new API and ingress endpoints.
6. Monitor the progress of the configuration by running the following command:

   ```
   $ oc get ipc ipconfig -o yaml
   ```

   Watch for the following progression:

   * The controller sets the `ConfigInProgress` condition
   * The pre-pivot phase runs and triggers a reboot
   * After reboot, the post-pivot phase applies the network changes
   * The controller waits for cluster stabilization
   * The `ConfigCompleted` condition is set when successful
7. After the configuration completes successfully, verify that the `status.validNextStages` field includes `Idle` and `Rollback`.
8. Verify the new network configuration by running the following command:

   ```
   $ oc get nodes -o wide
   ```
9. Verify cluster health by running the following command:

   ```
   $ oc get clusteroperators
   ```
10. When you are satisfied with the new configuration, finalize the change by setting the stage to `Idle`. Run the following command:

    ```
    $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Idle"}}'
    ```

    Important

    After you finalize the configuration by transitioning to `Idle`, you cannot roll back to the previous network configuration. The old stateroot is removed during `Idle` state cleanup.

#### [18.2.2. Roll back a network reconfiguration](#cnf-rollback-sno-ip-configuration_configuring-sno-ip-configuration) Copy linkLink copied to clipboard!

If you see issues after a network reconfiguration, you can roll back to an earlier network configuration. The rollback reboots the node into an earlier stateroot with the original network settings.

**Prerequisites**

* You have completed a network reconfiguration that has not been finalized.
* The `status.validNextStages` field in the `IPConfig` customer resource (CR) includes `Rollback`.
* You have cluster administrator privileges.

**Procedure**

1. Verify that rollback stage is available by checking the `IPConfig` CR. Run the following command:

   ```
   $ oc get ipc ipconfig -o jsonpath='{.status.validNextStages}'
   ```

   Verify that the output includes `Rollback`.
2. Check the rollback availability expiration timestamp by running the following command:

   ```
   $ oc get ipc ipconfig -o jsonpath='{.status.rollbackAvailabilityExpiration}'
   ```

   Note

   Plan your rollback before this timestamp. After this timestamp, rolling back requires manual recovery because of expired control plane or kubelet certificates in the rollback stateroot.
3. Trigger the rollback by setting the stage to `Rollback` by running the following command:

   ```
   $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Rollback"}}'
   ```

   The Lifecycle Agent reboots the node into the earlier stateroot.
4. After the node reboots, monitor the rollback progress by running the following command:

   ```
   $ oc get ipc ipconfig -o yaml
   ```

   Wait for the `RollbackCompleted` condition to be set.
5. Verify the node is using the original network configuration by running the following command:

   ```
   $ oc get nodes -o wide
   ```
6. Finalize the rollback by setting the stage to `Idle` by running the following command:

   ```
   $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Idle"}}'
   ```

#### [18.2.3. Automatic rollback mechanisms for network reconfiguration](#cnf-automatic-rollback-sno-ip-configuration_configuring-sno-ip-configuration) Copy linkLink copied to clipboard!

Network reconfiguration includes many automatic rollback safety mechanisms that help protect your cluster from failed configuration changes.

Automatic rollback on post-pivot failure
:   If network configuration or certificate regeneration fails after the reboot, the system automatically triggers a rollback to the earlier stateroot.

Init-monitor timeout rollback
:   If the network reconfiguration does not complete within the configured timeout, the system automatically triggers a rollback. The default timeout is 1800 seconds, 30 minutes. You can configure this timeout by using the `spec.autoRollbackOnFailure.initMonitorTimeoutSeconds` field in the `IPConfig` CR. Setting the value to `0` uses the default timeout.

#### [18.2.4. IPConfig reference specifications](#cnf-ipconfig-cr-reference_configuring-sno-ip-configuration) Copy linkLink copied to clipboard!

The `IPConfig` custom resource (CR) is a cluster-scoped CR that controls the IP configuration workflow for single-node OpenShift clusters using the Lifecycle Agent.

Note

The CR name must be `ipconfig`.

Expand

Table 18.1. IPConfig spec fields

| Field | Type | Description |
| --- | --- | --- |
| `spec.stage` | String | Controls the current stage of the IP configuration workflow. Valid values are `Idle`, `Config`, and `Rollback`. You can only change the stage to a value listed in `status.validNextStages`. |
| `spec.ipv4.address` | String | The IPv4 node address without CIDR notation, for example `192.0.2.10`. Required if the `ipv4` object is present. Omit the entire `ipv4` object for IPv6-only clusters. |
| `spec.ipv4.machineNetwork` | String | The machine network CIDR, for example `192.0.2.0/24`. The address must be within this CIDR. |
| `spec.ipv4.gateway` | String | The IPv4 default gateway address, used to create the default route for IPv4 traffic. Must be within the machine network CIDR. |
| `spec.ipv6.address` | String | The IPv6 node address without CIDR notation, for example `2001:db8::10`. Required if the `ipv6` object is present. Omit the entire `ipv6` object for IPv4-only clusters. |
| `spec.ipv6.machineNetwork` | String | The IPv6 machine network CIDR, for example `2001:db8::/64`. The address must be within this CIDR. |
| `spec.ipv6.gateway` | String | The IPv6 default gateway, used to create the default route for IPv6 traffic. You can use link-local gateways. |
| `spec.dnsServers` | Array of strings | Ordered list of DNS server IP addresses. The first server in the list is used as the primary DNS server. Must match cluster IP families. Maximum of 2 servers. |
| `spec.vlanID` | Integer | The VLAN ID to configure. Valid values are 1-4094. You can only set this field if the cluster already has VLAN configuration. |
| `spec.dnsFilterOutFamily` | String | DNS response filtering for dual-stack clusters only. Set to `ipv4` to filter out A records, `ipv6` to filter out AAAA records, or `none` to disable filtering. You can only configure this field to `ipv4` or `ipv6` when the cluster uses a dual-stack configuration. |
| `spec.autoRollbackOnFailure.initMonitorTimeoutSeconds` | Integer | Timeout in seconds for the init-monitor watchdog. Set to `0` or leave unset to use the default of 1800 seconds. |

Show more

### [18.3. Troubleshoot single-node OpenShift network reconfiguration](#cnf-troubleshooting-sno-ip-configuration) Copy linkLink copied to clipboard!

Use the following information to diagnose and resolve network reconfiguration issues on single-node OpenShift clusters.

#### [18.3.1. Gather diagnostic information for network reconfiguration issues](#cnf-gathering-sno-ip-configuration-diagnostics_troubleshooting-sno-ip-configuration) Copy linkLink copied to clipboard!

You can gather diagnostic information to help troubleshoot network reconfiguration issues on single-node OpenShift clusters.

**Procedure**

1. Inspect the `IPConfig` custom resource (CR) status by running the following command:

   ```
   $ oc get ipc ipconfig -o yaml
   ```

   Review the `status.conditions` field for the current state, reason, and message. Check `status.validNextStages` for possible stage transitions, and `status.history` for timestamps of stage progression.
2. View the Lifecycle Agent controller logs by running the following command:

   ```
   $ oc logs -n openshift-lifecycle-agent deployment/lifecycle-agent-controller-manager -c manager
   ```
3. Create a debug session on the target node by running the following command:

   ```
   $ oc debug node/<node_name>
   # chroot /host
   ```

   * Replace `<node_name>` with the name of your single-node OpenShift node.
4. View the relevant service logs depending on which phase you are troubleshooting by running one of the following commands:

   * View the logs for pre-pivot issues by running the following command:

     ```
     $ sudo journalctl -u lca-ipconfig-pre-pivot -b --no-pager
     ```
   * View the logs for post-pivot issues by running the following command:

     ```
     $ sudo journalctl -u ip-configuration.service -b --no-pager
     ```
   * View the logs for `init-monitor` watchdog issues by running the following command:

     ```
     $ sudo journalctl -u lca-init-monitor.service -b --no-pager
     ```
   * View the logs for rollback issues by running the following command:

     ```
     $ sudo journalctl -u lca-ipconfig-rollback -b --no-pager
     ```

#### [18.3.2. Network reconfiguration troubleshooting reference](#cnf-troubleshooting-sno-ip-configuration_troubleshooting-sno-ip-configuration) Copy linkLink copied to clipboard!

Use the following reference information to help diagnose and resolve network reconfiguration issues on single-node OpenShift clusters.

Expand

Table 18.2. On-node artifacts for troubleshooting

| File | Description |
| --- | --- |
| `/var/lib/lca/workspace/ip-config-pre-pivot.json` | Pre-pivot configuration data |
| `/var/lib/lca/workspace/ip-config-post-pivot.json` | Post-pivot configuration data |
| `/var/lib/lca/workspace/nmstate.yaml` | Generated `nmstate` configuration for network changes |
| `/var/lib/lca/workspace/recert_config.json` | Configuration for certificate regeneration |
| `/var/lib/lca/workspace/ip-config-autorollback-config.json` | Auto-rollback configuration |
| `/var/lib/lca/workspace/recert-pull-secret.json` | Pull secret for the recert image, if a custom pull secret was specified |
| `/var/lib/lca/ipc.json` | Persistence file that stores `IPConfig` state for rollback and status continuity across restarts |

Show more

Expand

Table 18.3. Common failure patterns

| Issue | Cause | Solution |
| --- | --- | --- |
| Stage transition rejected | You attempted to transition to a stage not in `status.validNextStages`. | Check `status.validNextStages` and only transition to an allowed stage. |
| Specification fields cannot be changed | You attempted to modify `spec` fields while the CR is not in the `Idle` stage. | Wait for the current operation to complete and the CR to return to `Idle`. |
| Health checks never pass | Cluster health blockers are preventing progress. | Investigate cluster health issues. |
| Post-pivot phase failed | An error occurred during network configuration or certificate regeneration. | Review the post-pivot service logs. If auto-rollback is enabled, the node automatically reverts. Otherwise, manually trigger rollback by setting `spec.stage: Rollback`. |
| Pods not receiving new IP family | Pre-existing pods might not automatically receive an IP address from the new family because of CNI behavior. | Delete and re-create the affected pods to obtain addresses from the new IP family. |
| Configuration stuck in disconnected environment | The Lifecycle Agent or recert container might be attempting to pull images not available in the disconnected registry. | Ensure all required images are mirrored to your disconnected registry before starting. Verify the `lca.openshift.io/recert-pull-secret` annotation references a valid pull secret. |

Show more

## [Legal Notice](#idm140244016352480) Copy linkLink copied to clipboard!

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
