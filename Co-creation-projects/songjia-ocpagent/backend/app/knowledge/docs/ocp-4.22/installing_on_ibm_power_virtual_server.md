---
title: "Installing on IBM Power Virtual Server"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power_virtual_server/index
retrieved_at: 2026-09-05T05:42:06.235958+00:00
---

# Installing on IBM Power Virtual Server

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on IBM Power Virtual Server

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139776231484048)

**Abstract**

This document describes how to install OpenShift Container Platform on IBM Power Virtual Server.

---

## [Chapter 1. Installation methods](#preparing-to-install-on-ibm-power-vs) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on IBM Power® Virtual Server, review the available installer-provisioned infrastructure methods and configure the Cloud Credential Operator utility.

### [1.1. Installing a cluster on installer-provisioned infrastructure](#installation-methods-ibm-power-vs_preparing-to-install-on-ibm-power-vs) Copy linkLink copied to clipboard!

Review the available installer-provisioned methods for installing a OpenShift Container Platform cluster on IBM Power® Virtual Server, including customized, VPC-based, private, and disconnected network options.

* **Installing a customized cluster on IBM Power® Virtual Server**: You can install a customized cluster on IBM Power® Virtual Server infrastructure that the installation program provisions. The installation program supports some customization at the installation stage. Many other customization options are available postinstallation.
* **Installing a cluster on IBM Power® Virtual Server into an existing VPC**: You can install OpenShift Container Platform on IBM Power® Virtual Server into an existing Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.
* **Installing a private cluster on IBM Power® Virtual Server**: You can install a private cluster on IBM Power® Virtual Server. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.
* **Installing a cluster on IBM Power® Virtual Server in a restricted network**: You can install OpenShift Container Platform on installer-provisioned IBM Power® Virtual Server infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components.

Note

Installing OpenShift Container Platform on IBM Power® Virtual Server using user-provisioned infrastructure is the same as for IBM Power®.

### [1.2. Configuring the Cloud Credential Operator utility](#cco-ccoctl-configuring_preparing-to-install-on-ibm-power-vs) Copy linkLink copied to clipboard!

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on IBM Power® Virtual Server, you must set the CCO to `manual` mode as part of the installation process.

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

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

## [Chapter 2. Configuring an IBM Cloud account](#installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on IBM Power® Virtual Server, you must configure an IBM Cloud® account with the correct quotas, DNS resolution, and IAM policies.

### [2.1. Prerequisites](#prerequisites) Copy linkLink copied to clipboard!

* You have an IBM Cloud® account with a subscription. You cannot install OpenShift Container Platform on a free or on a trial IBM Cloud® account.

### [2.2. Quotas and limits on IBM Power Virtual Server](#quotas-and-limits-ibm-power-vs_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

The OpenShift Container Platform cluster uses several IBM Cloud® and IBM Power® Virtual Server components. Default quotas and limits affect your ability to install clusters, so you might need to request additional resources for your IBM Cloud® account depending on your configuration, region, or number of clusters.

#### [2.2.1. Virtual private cloud](#virtual-private-cloud) Copy linkLink copied to clipboard!

Each OpenShift Container Platform cluster creates its own Virtual Private Cloud (VPC). The default quota of VPC instances per region is 10. If you have 10 VPC instances created, you must increase your quota before attempting an installation.

#### [2.2.2. Application load balancer](#application-load-balancer) Copy linkLink copied to clipboard!

By default, each cluster creates two application load balancers (ALBs):

* Internal load balancer for the control plane API server
* External load balancer for the control plane API server

You can create additional `LoadBalancer` service objects to create additional ALBs. The default quota of VPC ALBs are 50 per region. To have more than 50 ALBs, you must increase this quota.

VPC ALBs are supported. Classic ALBs are not supported for IBM Power® Virtual Server.

#### [2.2.3. Transit gateways](#transit-gateways) Copy linkLink copied to clipboard!

Each OpenShift Container Platform cluster creates its own transit gateway to enable communication with a VPC. The default quota of transit gateways per IBM Cloud® account is 10. If you have 10 transit gateways created, you must increase your quota before attempting an installation.

#### [2.2.4. Dynamic host configuration protocol (DHCP) service](#dynamic-host-configuration-protocol-dhcp-service) Copy linkLink copied to clipboard!

There is a limit of one Dynamic Host Configuration Protocol (DHCP) service per IBM Power® Virtual Server instance.

#### [2.2.5. Virtual server instances](#virtual-server-instances) Copy linkLink copied to clipboard!

By default, a cluster creates server instances with the following resources:

* 0.5 CPUs
* 32 GB RAM
* System Type: `s922`
* Processor Type: `uncapped`, `shared`
* Storage Tier: `Tier-3`

The installation program creates the following nodes:

* One bootstrap machine, which the installation process removes after the installation is complete
* Three control plane nodes
* Three compute nodes

### [2.3. Configuring DNS resolution](#configuring-dns-resolution-powervs_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

DNS resolution configuration for OpenShift Container Platform on IBM Power® Virtual Server depends on whether you are installing a public or private cluster. Public clusters use IBM Cloud® Internet Services (CIS) and private clusters use IBM Cloud® DNS Services.

* If you are installing a public cluster, you use IBM Cloud® Internet Services (CIS).
* If you are installing a private cluster, you use IBM Cloud® DNS Services (DNS Services).

### [2.4. Using IBM Cloud Internet Services for DNS resolution](#installation-cis-ibm-cloud_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

The installation program uses IBM Cloud® Internet Services (CIS) to configure cluster DNS resolution and provide name lookup for a public cluster.

Note

This offering does not support IPv6, so dual stack or IPv6 environments are not possible.

You must create a domain zone in CIS in the same account as your cluster. You must also ensure the zone is authoritative for the domain. You can do this using a root domain or subdomain.

**Prerequisites**

* You have installed the IBM Cloud® CLI. For more information, see "IBM Cloud® CLI".
* You have an existing domain and registrar. For more information, see the "IBM® DNS documentation".

**Procedure**

1. Create a CIS instance to use with your cluster:

   1. Install the CIS plugin:

      ```
      $ ibmcloud plugin install cis
      ```
   2. Log in to IBM Cloud® by using the CLI:

      ```
      $ ibmcloud login
      ```
   3. Create the CIS instance:

      ```
      $ ibmcloud cis instance-create <instance_name> standard-next
      ```

      At a minimum, you require a `Standard Next` plan for CIS to manage the cluster subdomain and its DNS records.

      Note

      After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect.
2. Connect an existing domain to your CIS instance:

   1. Set the context instance for CIS:

      ```
      $ ibmcloud cis instance-set <instance_CRN>
      ```

      Replace `<instance_CRN>` with the instance CRN (Cloud Resource Name). For example: `ibmcloud cis instance-set crn:v1:bluemix:public:power-iaas:osa21:a/65b64c1f1c29460d8c2e4bbfbd893c2c:c09233ac-48a5-4ccb-a051-d1cfb3fc7eb5::`
   2. Add the domain for CIS:

      ```
      $ ibmcloud cis domain-add <domain_name>
      ```

      Replace `<domain_name>` with the fully qualified domain name. You can use either the root domain or subdomain value as the domain name, depending on which you plan to configure.

      Note

      A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`.
3. Open the CIS web console, navigate to the **Overview** page, and note your CIS name servers. These name servers are used in the next step. For more information, see "CIS web console".
4. Configure the name servers for your domains or subdomains at the domain’s registrar or DNS provider. For more information, see the IBM Cloud® documentation for "Configuring name servers".

### [2.5. IBM Cloud IAM policies and API key](#installation-ibm-cloud-iam-policies-api-key_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

To install OpenShift Container Platform into your IBM Cloud® account, the installation program requires an IAM API key, which provides authentication and authorization to access IBM Cloud® service APIs. You can use an existing IAM API key that contains the required policies or create a new one.

For an IBM Cloud® IAM overview, see the "IBM Cloud® IAM overview" documentation.

#### [2.5.1. Prerequisite permissions](#pre-requisite-permissions-ibm-cloud_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

Expand

Table 2.1. Prerequisite permissions

| Role | Access |
| --- | --- |
| Viewer, Operator, Editor, Administrator, Reader, Writer, Manager | Internet Services service in <resource\_group> resource group |
| Viewer, Operator, Editor, Administrator, User API key creator, Service ID creator | IAM Identity Service service |
| Viewer, Operator, Administrator, Editor, Reader, Writer, Manager, Console Administrator | VPC Infrastructure Services service in <resource\_group> resource group |
| Viewer | Resource Group: Access to view the resource group itself. The resource type should equal `Resource group`, with a value of <your\_resource\_group\_name>. |

Show more

#### [2.5.2. Cluster-creation permissions](#cluster-creation-permissions-ibm-cloud_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

Expand

Table 2.2. Cluster-creation permissions

| Role | Access |
| --- | --- |
| Viewer | <resource\_group> (Resource Group Created for Your Team) |
| Viewer, Operator, Editor, Reader, Writer, Manager | All Identity and IAM enabled services in Default resource group |
| Viewer, Reader | Internet Services service |
| Viewer, Operator, Reader, Writer, Manager, Content Reader, Object Reader, Object Writer, Editor | Cloud Object Storage service |
| Viewer | Default resource group: The resource type should equal `Resource group`, with a value of `Default`. If your account administrator changed your account’s default resource group to something other than Default, use that value instead. |
| Viewer, Operator, Editor, Reader, Manager | Workspace for IBM Power® Virtual Server service in <resource\_group> resource group |
| Viewer, Operator, Editor, Reader, Writer, Manager, Administrator | Internet Services service in <resource\_group> resource group: CIS functional scope string equals reliability |
| Viewer, Operator, Editor | Transit Gateway service |
| Viewer, Operator, Editor, Administrator, Reader, Writer, Manager, Console Administrator | VPC Infrastructure Services service <resource\_group> resource group |

Show more

#### [2.5.3. Access policy assignment](#access-policy-assignment-ibm-cloud_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

In IBM Cloud® IAM, access policies can be attached to different subjects:

* Access group (Recommended)
* Service ID
* User

Note

The recommended method is to define IAM access policies in an access group. This helps organize all the access required for OpenShift Container Platform and enables you to onboard users and service IDs to this group. You can also assign access to users and service IDs directly, if desired.

For more information, see "Access groups" and "Users and service IDs".

#### [2.5.4. Creating an API key](#installation-ibm-cloud-creating-api-key_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

You must create a user API key or a service ID API key for your IBM Cloud® account.

**Prerequisites**

* You have assigned the required access policies to your IBM Cloud® account.
* You have attached your IAM access policies to an access group, or other appropriate resource.

**Procedure**

* Create an API key, depending on how you defined your IAM access policies.

  For example, if you assigned your access policies to a user, you must create a user API key. If you assigned your access policies to a service ID, you must create a service ID API key. If your access policies are assigned to an access group, you can use either API key type. For more information on IBM Cloud® API keys, see "User API key", "Service ID API key", and "Understanding API keys".

### [2.6. Supported IBM Power Virtual Server regions and zones](#installation-ibm-power-vs-regions_installing-ibm-cloud-account-power-vs) Copy linkLink copied to clipboard!

When installing OpenShift Container Platform, you must choose a supported region or zone for your cloud provider deployment.

You can deploy an OpenShift Container Platform cluster to the following regions:

* `tor` (Toronto, Canada)

  + `tor01`
* `dal` (Dallas, USA)

  + `dal10`
  + `dal12`
* `eu-de` (Frankfurt, Germany)

  + `eu-de-1`
  + `eu-de-2`
* `lon` (London, UK)

  + `lon04`
  + `lon06`
* `mad` (Madrid, Spain)

  + `mad02`
  + `mad04`
* `osa` (Osaka, Japan)

  + `osa21`
* `sao` (Sao Paulo, Brazil)

  + `sao01`
  + `sao04`
* `syd` (Sydney, Australia)

  + `syd04`
  + `syd05`
* `wdc` (Washington DC, USA)

  + `wdc06`
  + `wdc07`
* `us-east` (Washington DC, United States)

  + `us-east`
* `us-south` (Dallas, United States)

  + `us-south`

You might optionally specify the IBM Cloud® region in which the installation program creates any VPC components.

Note

If you do not specify the region, the installation program selects the region closest to IBM Power Virtual Server zone you are deploying to.

IBM Cloud® supports the following regions:

* `us-east`
* `us-south`
* `eu-de`
* `eu-es`
* `eu-gb`
* `jp-osa`
* `au-syd`
* `br-sao`
* `ca-tor`
* `jp-tok`

## [Chapter 3. Creating an IBM Power Virtual Server workspace](#creating-ibm-power-vs-workspace) Copy linkLink copied to clipboard!

To host your OpenShift Container Platform cluster on IBM Power® Virtual Server, you can create a dedicated workspace and retrieve its identifier for use during installation.

### [3.1. Creating an IBM Power Virtual Server workspace](#creating-ibm-power-vs-workspace-procedure_creating-ibm-power-vs-workspace) Copy linkLink copied to clipboard!

To set up the infrastructure needed for your OpenShift Container Platform cluster, you can create an IBM Power® Virtual Server workspace and retrieve its GUID for use during installation.

**Procedure**

1. To create an IBM Power® Virtual Server workspace, complete step 1 to step 5 from the IBM Cloud® documentation for [Creating an IBM Power® Virtual Server](https://cloud.ibm.com/docs/power-iaas?topic=power-iaas-creating-power-virtual-server).
2. After it has finished provisioning, retrieve the 32-character alphanumeric Globally Unique Identifier (GUID) of your new workspace by entering the following command:

   ```
   $ ibmcloud resource service-instance <workspace name>
   ```

## [Chapter 4. Installing a cluster on IBM Power Virtual Server with customizations](#installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

To install a customized OpenShift Container Platform cluster on IBM Power® Virtual Server, use installer-provisioned infrastructure and adjust the `install-config.yaml` parameters before you run the installation program.

### [4.1. Prerequisites](#prereqs-ibm-power-vs_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM Power® Virtual Server, complete the prerequisite tasks to configure your IBM Cloud® account, firewall, and credential utility.

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You configured an IBM Cloud® account to host the cluster.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
* You configured the `ccoctl` utility before you installed the cluster.

### [4.2. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [4.3. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.4. Obtaining the installation program](#installation-obtaining-installer_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.5. Exporting the API key](#installation-ibm-cloud-export-variables_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key.

**Prerequisites**

* You have created either a user API key or service ID API key for your IBM Cloud® account.

**Procedure**

* Export your API key for your account as a global variable:

  ```
  $ export IBMCLOUD_API_KEY=<api_key>
  ```

Important

You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.

### [4.6. Creating the installation configuration file](#installation-initializing_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

        Note

        Always delete the `~/.powervs` directory to avoid reusing a stale configuration. Run the following command:

        ```
        $ rm -rf ~/.powervs
        ```
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **powervs** as the platform to target.
      3. Select the region to deploy the cluster to.
      4. Select the zone to deploy the cluster to.
      5. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      6. Enter a descriptive name for your cluster.
2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.
3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [4.6.1. Sample customized install-config.yaml file for IBM Power Virtual Server](#installation-ibm-power-vs-config-yaml_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters.

Important

This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and change it.

```
apiVersion: v1
baseDomain: example.com
compute:
- architecture: ppc64le
  hyperthreading: Enabled
  name: worker
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
controlPlane:
  architecture: ppc64le
  hyperthreading: Enabled
  name: master
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
metadata:
  creationTimestamp: null
  name: example-cluster-name
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.0.0/24
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  powervs:
    userID: ibm-user-id
    region: powervs-region
    zone: powervs-zone
    powervsResourceGroup: "ibmcloud-resource-group"
    serviceInstanceGUID: "powervs-region-service-instance-guid"
    vpcRegion: vpc-region
publish: External
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
```

where:

`compute`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The first line of the `compute` section must begin with a hyphen, `-`. Although both sections currently define a single machine pool, it is possible that OpenShift Container Platform will support defining multiple compute pools during installation.

`compute.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

`compute.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the compute machines. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

`controlPlane`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used.

`controlPlane.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

    Important

    When multithreading (SMT) is disabled, each vCPU is equivalent to one physical core. Disable SMT only if you have specific requirements.

`controlPlane.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the control plane. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

    Note

    When simultaneous multithreading (SMT) is not enabled, one vCPU is equivalent to one physical core. When enabled, total vCPUs is computed as: (Thread(s) per core \* Core(s) per socket) \* Socket(s). The smtLevel controls the threads per core. Lower SMT levels may require additional assigned cores when deploying the cluster nodes. You can do this by setting the `'processors'` parameter in the `install-config.yaml` file to an appropriate value to meet the requirements for deploying OpenShift Container Platform successfully.

`networking.networkType`
:   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`platform.powervs.powervsResourceGroup`
:   Specifies the name of an existing resource group.

`pullSecret`
:   Specifies your pull secret. The installation program prompts you for this value. This value is required.

    Note

    For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

#### [4.6.2. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.7. Manually creating IAM](#manually-create-iam-ibm-cloud_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Cloud Credential Operator (CCO) must operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for your cloud provider.

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources.

**Prerequisites**

* You have configured the `ccoctl` binary.
* You have an existing `install-config.yaml` file.

**Procedure**

1. Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`.

   **Example `install-config.yaml` configuration file**

   ```
   apiVersion: v1
   baseDomain: cluster1.example.com
   credentialsMode: Manual
   compute:
   - architecture: ppc64le
     hyperthreading: Enabled
   ```

   where:

   `credentialsMode`
   :   Specifies the CCO credentials mode. Set the value to `Manual`.
2. To generate the manifests, run the following command from the directory that includes the installation program:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
3. From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
4. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

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
   :   Specifies that only the manifests that your specific cluster configuration requires are included.

   `--install-config`
   :   Specifies the location of the `install-config.yaml` file.

   `--to`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
         apiVersion: cloudcredential.openshift.io/v1
         kind: CredentialsRequest
         metadata:
           labels:
             controller-tools.k8s.io: "1.0"
           name: openshift-image-registry-ibmcos
           namespace: openshift-cloud-credential-operator
         spec:
           secretRef:
             name: installer-cloud-credentials
             namespace: openshift-image-registry
           providerSpec:
             apiVersion: cloudcredential.openshift.io/v1
             kind: IBMCloudProviderSpec
             policies:
             - attributes:
               - name: serviceName
                 value: cloud-object-storage
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
               - crn:v1:bluemix:public:iam::::role:Operator
               - crn:v1:bluemix:public:iam::::role:Editor
               - crn:v1:bluemix:public:iam::::serviceRole:Reader
               - crn:v1:bluemix:public:iam::::serviceRole:Writer
             - attributes:
               - name: resourceType
                 value: resource-group
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
       ```
5. Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret:

   ```
   $ ccoctl ibmcloud create-service-id \
     --credentials-requests-dir=<path_to_credential_requests_directory> \
     --name=<cluster_name> \
     --output-dir=<installation_directory> \
     --resource-group-name=<resource_group_name>
   ```

   where:

   `<path_to_credential_requests_directory>`
   :   Specifies the directory that has the files for the `CredentialsRequest` objects.

   `<cluster_name>`
   :   Specifies the name of the OpenShift Container Platform cluster.

   `<installation_directory>`
   :   Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands. This parameter is optional.

   `<resource_group_name>`
   :   Specifies the name of the resource group used for scoping the access policies. This parameter is optional.

       Note

       If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object.

       If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command:

       ```
       $ grep resourceGroup <installation_directory>/manifests/cluster-infrastructure-02-config.yml
       ```

**Verification**

* Check that the appropriate secrets exist in the `manifests` directory of your cluster.

### [4.8. Deploying the cluster](#installation-launching-installer_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

* In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ```
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  + For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
  + To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

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

### [4.9. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.10. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.11. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.12. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

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

### [4.13. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-ibm-power-vs-customizations) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

## [Chapter 5. Installing a cluster on IBM Power Virtual Server into an existing VPC](#installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

To install a OpenShift Container Platform cluster on IBM Power® Virtual Server into an existing Virtual Private Cloud (VPC), use installer-provisioned infrastructure. The installation program provisions the remaining required infrastructure, which you can then customize.

### [5.1. Prerequisites](#prereqs-ibm-power-vs_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM Power® Virtual Server, complete the prerequisite tasks to configure your IBM Cloud® account, firewall, and credential utility.

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You configured an IBM Cloud® account to host the cluster.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
* You configured the `ccoctl` utility before you installed the cluster.

### [5.2. About using a custom Virtual Private Cloud (VPC)](#installation-custom-ibm-powervs-vpc_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you can deploy a cluster using an existing IBM® Virtual Private Cloud (VPC).

Because the installation program cannot know what other components are in your existing subnets, it cannot choose subnet CIDRs and so forth. You must configure networking for the subnets to which you will install the cluster.

#### [5.2.1. Requirements for using your Virtual Private Cloud (VPC)](#installation-custom-ibm-power-vs-requirements_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create a VPC or VPC subnet in this scenario.

The installation program cannot:

* Subdivide network ranges for the cluster to use
* Set route tables for the subnets
* Set VPC options such as DHCP

Note

The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

#### [5.2.2. Virtual Private Cloud (VPC) validation](#installation-custom-ibm-power-vs-validation_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

The VPC and all of the subnets must be in an existing resource group. The cluster is deployed to this resource group.

As part of the installation, specify the following in the `install-config.yaml` file:

* The name of the resource group
* The name of VPC
* The name of the VPC subnet

To ensure that the subnets that you give are suitable, the installation program confirms that all of the subnets you specify exist.

Note

Subnet IDs are not supported.

#### [5.2.3. Isolation between clusters](#installation-custom-ibm-power-vs-isolation_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

If you deploy OpenShift Container Platform to an existing network, cluster service isolation decreases in the following ways:

* ICMP Ingress is allowed to the entire network.
* TCP port 22 Ingress (SSH) is allowed to the entire network.
* Control plane TCP 6443 Ingress (Kubernetes API) is allowed to the entire network.
* Control plane TCP 22623 Ingress (MCS) is allowed to the entire network.

### [5.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [5.4. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.5. Obtaining the installation program](#installation-obtaining-installer_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.6. Exporting the API key](#installation-ibm-cloud-export-variables_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key.

**Prerequisites**

* You have created either a user API key or service ID API key for your IBM Cloud® account.

**Procedure**

* Export your API key for your account as a global variable:

  ```
  $ export IBMCLOUD_API_KEY=<api_key>
  ```

Important

You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.

### [5.7. Creating the installation configuration file](#installation-initializing_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

        Note

        Always delete the `~/.powervs` directory to avoid reusing a stale configuration. Run the following command:

        ```
        $ rm -rf ~/.powervs
        ```
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **powervs** as the platform to target.
      3. Select the region to deploy the cluster to.
      4. Select the zone to deploy the cluster to.
      5. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      6. Enter a descriptive name for your cluster.
2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.
3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [5.7.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

#### [5.7.2. Sample customized install-config.yaml file for IBM Power Virtual Server](#installation-ibm-power-vs-config-yaml_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters.

Important

This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and change it.

```
apiVersion: v1
baseDomain: example.com
compute:
- architecture: ppc64le
  hyperthreading: Enabled
  name: worker
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
controlPlane:
  architecture: ppc64le
  hyperthreading: Enabled
  name: master
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
metadata:
  creationTimestamp: null
  name: example-cluster-existing-vpc
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.0.0/24
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  powervs:
    userID: ibm-user-id
    powervsResourceGroup: "ibmcloud-resource-group"
    region: powervs-region
    vpcRegion: vpc-region
    vpcName: name-of-existing-vpc
    zone: powervs-zone
    serviceInstanceGUID: "powervs-region-service-instance-guid"
credentialsMode: Manual
publish: External
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
```

where:

`compute`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The first line of the `compute` section must begin with a hyphen, `-`. Both sections currently define a single machine pool.

`compute.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

`compute.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the compute machines. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

`controlPlane`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used.

`controlPlane.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

    Important

    When multithreading (SMT) is disabled, each vCPU is equivalent to one physical core. Disable SMT only if you have specific requirements.

`controlPlane.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the control plane. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

    Note

    When simultaneous multithreading (SMT) is not enabled, one vCPU is equivalent to one physical core. When enabled, total vCPUs is computed as (Thread(s) per core \* Core(s) per socket) \* Socket(s). The smtLevel controls the threads per core. Lower SMT levels may require additional assigned cores when deploying the cluster nodes. You can do this by setting the `'processors'` parameter in the `install-config.yaml` file to an appropriate value to meet the requirements for deploying OpenShift Container Platform successfully.

`networking.clusterNetwork.cidr`
:   Specifies the CIDR. The machine CIDR must contain the subnets for the compute machines and control plane machines.

`networking.networkType`
:   Specifies the cluster network plugin for installation. The supported value is `OVNKubernetes`.

`platform.powervs.vpcName`
:   Specifies the name of an existing VPC.

`publish`
:   Specifies how to publish the user-facing endpoints of your cluster.

`pullSecret`
:   Specifies your pull secret. The installation program prompts you for this value. This value is required.

`sshKey`
:   Specifies the SSH key to use to access the machines in your cluster. This value is optional.

    Note

    For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

#### [5.7.3. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.8. Manually creating IAM](#manually-create-iam-ibm-cloud_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Cloud Credential Operator (CCO) must operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for your cloud provider.

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources.

**Prerequisites**

* You have configured the `ccoctl` binary.
* You have an existing `install-config.yaml` file.

**Procedure**

1. Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`.

   **Example `install-config.yaml` configuration file**

   ```
   apiVersion: v1
   baseDomain: cluster1.example.com
   credentialsMode: Manual
   compute:
   - architecture: ppc64le
     hyperthreading: Enabled
   ```

   where:

   `credentialsMode`
   :   Specifies the CCO credentials mode. Set the value to `Manual`.
2. To generate the manifests, run the following command from the directory that includes the installation program:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
3. From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
4. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

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
   :   Specifies that only the manifests that your specific cluster configuration requires are included.

   `--install-config`
   :   Specifies the location of the `install-config.yaml` file.

   `--to`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
         apiVersion: cloudcredential.openshift.io/v1
         kind: CredentialsRequest
         metadata:
           labels:
             controller-tools.k8s.io: "1.0"
           name: openshift-image-registry-ibmcos
           namespace: openshift-cloud-credential-operator
         spec:
           secretRef:
             name: installer-cloud-credentials
             namespace: openshift-image-registry
           providerSpec:
             apiVersion: cloudcredential.openshift.io/v1
             kind: IBMCloudProviderSpec
             policies:
             - attributes:
               - name: serviceName
                 value: cloud-object-storage
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
               - crn:v1:bluemix:public:iam::::role:Operator
               - crn:v1:bluemix:public:iam::::role:Editor
               - crn:v1:bluemix:public:iam::::serviceRole:Reader
               - crn:v1:bluemix:public:iam::::serviceRole:Writer
             - attributes:
               - name: resourceType
                 value: resource-group
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
       ```
5. Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret:

   ```
   $ ccoctl ibmcloud create-service-id \
     --credentials-requests-dir=<path_to_credential_requests_directory> \
     --name=<cluster_name> \
     --output-dir=<installation_directory> \
     --resource-group-name=<resource_group_name>
   ```

   where:

   `<path_to_credential_requests_directory>`
   :   Specifies the directory that has the files for the `CredentialsRequest` objects.

   `<cluster_name>`
   :   Specifies the name of the OpenShift Container Platform cluster.

   `<installation_directory>`
   :   Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands. This parameter is optional.

   `<resource_group_name>`
   :   Specifies the name of the resource group used for scoping the access policies. This parameter is optional.

       Note

       If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object.

       If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command:

       ```
       $ grep resourceGroup <installation_directory>/manifests/cluster-infrastructure-02-config.yml
       ```

**Verification**

* Check that the appropriate secrets exist in the `manifests` directory of your cluster.

### [5.9. Deploying the cluster](#installation-launching-installer_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

* In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ```
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  + For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
  + To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

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

### [5.10. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.11. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.12. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.13. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

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

### [5.14. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-ibm-powervs-vpc) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

## [Chapter 6. Installing a private cluster on IBM Power Virtual Server](#installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

To install a private OpenShift Container Platform cluster on IBM Power® Virtual Server, deploy into an existing Virtual Private Cloud (VPC) and workspace. The installation program provisions the remaining infrastructure, which you can then customize.

### [6.1. Prerequisites](#prereqs-ibm-power-vs_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM Power® Virtual Server, complete the prerequisite tasks to configure your IBM Cloud® account, firewall, and credential utility.

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You configured an IBM Cloud® account to host the cluster.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
* You configured the `ccoctl` utility before you installed the cluster.

### [6.2. Private clusters](#private-clusters-default_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

You can deploy a private OpenShift Container Platform cluster that does not expose external endpoints. Private clusters are accessible from only an internal network and are not visible to the internet.

By default, OpenShift Container Platform is provisioned to use publicly-accessible DNS and endpoints. A private cluster sets the DNS, Ingress Controller, and API server to private when you deploy your cluster. This means that the cluster resources are only accessible from your internal network and are not visible to the internet.

Important

If the cluster has any public subnets, load balancer services created by administrators might be publicly accessible. To ensure cluster security, verify that these services are explicitly annotated as private.

To deploy a private cluster, you must:

* Use existing networking that meets your requirements.
* Create a DNS zone using IBM Cloud® DNS Services and specify it as the base domain of the cluster. For more information, see "Using IBM Cloud® DNS Services to configure DNS resolution".
* Deploy from a machine that has access to:

  + The API services for the cloud to which you provision.
  + The hosts on the network that you provision.
  + The internet to obtain installation media.

### [6.3. Private clusters in IBM Power Virtual Server](#private-clusters-about-ibm-power-virtual-server_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

To create a private cluster on IBM Power® Virtual Server, you must provide an existing private Virtual Private Cloud (VPC) and subnets to host the cluster. The installation program must also be able to resolve the DNS records that the cluster requires. The installation program configures the Ingress Operator and API server for only internal traffic.

The cluster still requires access to internet to access the IBM Cloud® APIs.

The following items are not required or created when you install a private cluster:

* Public subnets
* Public network load balancers, which support public Ingress
* A public DNS zone that matches the `baseDomain` for the cluster

You will also need to create an IBM® DNS service containing a DNS zone that matches your `baseDomain`. Unlike standard deployments on Power VS which use IBM® CIS for DNS, you must use IBM® DNS for your DNS service.

#### [6.3.1. Limitations](#private-clusters-limitations-ibm-power-virtual-server_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

Private clusters on IBM Power® Virtual Server are subject only to the limitations associated with the existing VPC that was used for cluster deployment.

### [6.4. Requirements for using your Virtual Private Cloud (VPC)](#installation-custom-ibm-power-vs-requirements_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create a VPC or VPC subnet in this scenario.

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create a VPC or VPC subnet in this scenario.

The installation program cannot:

* Subdivide network ranges for the cluster to use
* Set route tables for the subnets
* Set VPC options such as DHCP

Note

The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

#### [6.4.1. Virtual Private Cloud (VPC) validation](#installation-custom-ibm-power-vs-validation_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

The VPC and all of the subnets must be in an existing resource group. The cluster is deployed to this resource group.

As part of the installation, specify the following in the `install-config.yaml` file:

* The name of the resource group
* The name of VPC
* The name of the VPC subnet

To ensure that the subnets that you give are suitable, the installation program confirms that all of the subnets you specify exist.

Note

Subnet IDs are not supported.

#### [6.4.2. Isolation between clusters](#installation-custom-ibm-power-vs-isolation_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

If you deploy OpenShift Container Platform to an existing network, cluster service isolation decreases in the following ways:

* ICMP Ingress is allowed to the entire network.
* TCP port 22 Ingress (SSH) is allowed to the entire network.
* Control plane TCP 6443 Ingress (Kubernetes API) is allowed to the entire network.
* Control plane TCP 22623 Ingress (MCS) is allowed to the entire network.

### [6.5. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [6.6. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.7. Obtaining the installation program](#installation-obtaining-installer_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.8. Exporting the API key](#installation-ibm-cloud-export-variables_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key.

**Prerequisites**

* You have created either a user API key or service ID API key for your IBM Cloud® account.

**Procedure**

* Export your API key for your account as a global variable:

  ```
  $ export IBMCLOUD_API_KEY=<api_key>
  ```

Important

You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.

### [6.9. Manually creating the installation configuration file](#installation-initializing-manual_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

#### [6.9.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 6.1. Minimum resource requirements

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

#### [6.9.2. Sample customized install-config.yaml file for IBM Power Virtual Server](#installation-ibm-power-vs-config-yaml_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters.

Important

This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and change it.

```
apiVersion: v1
baseDomain: example.com
compute:
- architecture: ppc64le
  hyperthreading: Enabled
  name: worker
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
controlPlane:
  architecture: ppc64le
  hyperthreading: Enabled
  name: master
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
metadata:
  creationTimestamp: null
  name: example-private-cluster-name
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.0.0/24
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  powervs:
    userID: ibm-user-id
    powervsResourceGroup: "ibmcloud-resource-group"
    region: powervs-region
    vpcName: name-of-existing-vpc
    vpcRegion: vpc-region
    zone: powervs-zone
    serviceInstanceGUID: "powervs-region-service-instance-guid"
publish: Internal
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
```

where:

`compute`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The first line of the `compute` section must begin with a hyphen, `-`. Both sections currently define a single machine pool.

`compute.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

`compute.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the compute machines. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

`controlPlane`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used.

`controlPlane.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

    Important

    When multithreading (SMT) is disabled, each vCPU is equivalent to one physical core. Disable SMT only if you have specific requirements.

`controlPlane.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the control plane. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

    Note

    When simultaneous multithreading (SMT) is not enabled, one vCPU is equivalent to one physical core. When enabled, total vCPUs is computed as (Thread(s) per core \* Core(s) per socket) \* Socket(s). The smtLevel controls the threads per core. Lower SMT levels may require additional assigned cores when deploying the cluster nodes. You can do this by setting the `'processors'` parameter in the `install-config.yaml` file to an appropriate value to meet the requirements for deploying OpenShift Container Platform successfully.

`networking.clusterNetwork.cidr`
:   Specifies the CIDR. The machine CIDR must contain the subnets for the compute machines and control plane machines.

`networking.networkType`
:   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`platform.powervs.vpcName`
:   Specifies the name of an existing VPC.

`publish`
:   Specifies how to publish the user-facing endpoints of your cluster. Set `publish` to `Internal` to deploy a private cluster.

`pullSecret`
:   Specifies your pull secret. The installation program prompts you for this value. This value is required.

`sshKey`
:   Specifies the SSH key to use to access the machines in your cluster. This value is optional.

    Note

    For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

#### [6.9.3. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.10. Manually creating IAM](#manually-create-iam-ibm-cloud_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Cloud Credential Operator (CCO) must operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for your cloud provider.

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources.

**Prerequisites**

* You have configured the `ccoctl` binary.
* You have an existing `install-config.yaml` file.

**Procedure**

1. Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`.

   **Example `install-config.yaml` configuration file**

   ```
   apiVersion: v1
   baseDomain: cluster1.example.com
   credentialsMode: Manual
   compute:
   - architecture: ppc64le
     hyperthreading: Enabled
   ```

   where:

   `credentialsMode`
   :   Specifies the CCO credentials mode. Set the value to `Manual`.
2. To generate the manifests, run the following command from the directory that includes the installation program:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
3. From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
4. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

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
   :   Specifies that only the manifests that your specific cluster configuration requires are included.

   `--install-config`
   :   Specifies the location of the `install-config.yaml` file.

   `--to`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
         apiVersion: cloudcredential.openshift.io/v1
         kind: CredentialsRequest
         metadata:
           labels:
             controller-tools.k8s.io: "1.0"
           name: openshift-image-registry-ibmcos
           namespace: openshift-cloud-credential-operator
         spec:
           secretRef:
             name: installer-cloud-credentials
             namespace: openshift-image-registry
           providerSpec:
             apiVersion: cloudcredential.openshift.io/v1
             kind: IBMCloudProviderSpec
             policies:
             - attributes:
               - name: serviceName
                 value: cloud-object-storage
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
               - crn:v1:bluemix:public:iam::::role:Operator
               - crn:v1:bluemix:public:iam::::role:Editor
               - crn:v1:bluemix:public:iam::::serviceRole:Reader
               - crn:v1:bluemix:public:iam::::serviceRole:Writer
             - attributes:
               - name: resourceType
                 value: resource-group
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
       ```
5. Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret:

   ```
   $ ccoctl ibmcloud create-service-id \
     --credentials-requests-dir=<path_to_credential_requests_directory> \
     --name=<cluster_name> \
     --output-dir=<installation_directory> \
     --resource-group-name=<resource_group_name>
   ```

   where:

   `<path_to_credential_requests_directory>`
   :   Specifies the directory that has the files for the `CredentialsRequest` objects.

   `<cluster_name>`
   :   Specifies the name of the OpenShift Container Platform cluster.

   `<installation_directory>`
   :   Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands. This parameter is optional.

   `<resource_group_name>`
   :   Specifies the name of the resource group used for scoping the access policies. This parameter is optional.

       Note

       If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object.

       If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command:

       ```
       $ grep resourceGroup <installation_directory>/manifests/cluster-infrastructure-02-config.yml
       ```

**Verification**

* Check that the appropriate secrets exist in the `manifests` directory of your cluster.

### [6.11. Deploying the cluster](#installation-launching-installer_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

* In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ```
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  + For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
  + To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

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

### [6.12. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.13. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.14. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.15. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

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

### [6.16. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-ibm-power-vs-private-cluster) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

## [Chapter 7. Installing a cluster on IBM Power Virtual Server in a disconnected environment](#installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

To install a OpenShift Container Platform cluster on IBM Power® Virtual Server in a disconnected environment, mirror the required release content and deploy into an existing Virtual Private Cloud (VPC) on IBM Cloud®.

### [7.1. Prerequisites](#prereqs-ibm-power-vs-disconnected_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM Power® Virtual Server in a restricted network, complete the prerequisite tasks to mirror images, configure an IBM Cloud® account, and prepare an existing Virtual Private Cloud (VPC).

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You configured an IBM Cloud® account to host the cluster.
* You mirrored the images for a disconnected installation to your registry and obtained the `imageContentSources` data for your version of OpenShift Container Platform.

  Important

  Because the installation media is on the mirror host, you can use that machine to complete all installation steps.
* You have an existing VPC in IBM Cloud®. When installing a cluster in a restricted network, you cannot use the installer-provisioned VPC. You must use a user-provisioned VPC that satisfies one of the following requirements:

  + Contains the mirror registry
  + Has firewall rules or a peering connection to access the mirror registry hosted elsewhere
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.
* You configured the `ccoctl` utility before you installed the cluster.

### [7.2. About installations in restricted networks](#installation-about-restricted-networks_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

You can install OpenShift Container Platform 4.22 in a restricted network without an active internet connection to obtain software components. Restricted network installations can use installer-provisioned or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, such as Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare-metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and has the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

#### [7.2.1. Additional limits](#installation-restricted-network-limits_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

Clusters in restricted networks have the following additional limitations and restrictions:

* The `ClusterVersion` status includes an `Unable to retrieve available updates` error.
* By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

### [7.3. About using a custom Virtual Private Cloud (VPC)](#installation-custom-ibm-powervs-vpc_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you can deploy a cluster into the subnets of an existing IBM® Virtual Private Cloud (VPC).

#### [7.3.1. Requirements for using your Virtual Private Cloud (VPC)](#installation-custom-ibm-power-vs-requirements_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create a VPC or VPC subnet in this scenario.

The installation program cannot:

* Subdivide network ranges for the cluster to use
* Set route tables for the subnets
* Set VPC options such as DHCP

Note

The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

#### [7.3.2. Virtual Private Cloud (VPC) validation](#installation-custom-ibm-power-vs-validation_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

The VPC and all of the subnets must be in an existing resource group. The cluster is deployed to this resource group.

As part of the installation, specify the following in the `install-config.yaml` file:

* The name of the resource group
* The name of VPC
* The name of the VPC subnet

To ensure that the subnets that you give are suitable, the installation program confirms that all of the subnets you specify exist.

Note

Subnet IDs are not supported.

#### [7.3.3. Isolation between clusters](#installation-custom-ibm-power-vs-isolation_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

If you deploy OpenShift Container Platform to an existing network, cluster service isolation decreases in the following ways:

* ICMP Ingress is allowed to the entire network.
* TCP port 22 Ingress (SSH) is allowed to the entire network.
* Control plane TCP 6443 Ingress (Kubernetes API) is allowed to the entire network.
* Control plane TCP 22623 Ingress (MCS) is allowed to the entire network.

### [7.4. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to obtain the images that are necessary to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

### [7.5. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [7.6. Exporting the API key](#installation-ibm-cloud-export-variables_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key.

**Prerequisites**

* You have created either a user API key or service ID API key for your IBM Cloud® account.

**Procedure**

* Export your API key for your account as a global variable:

  ```
  $ export IBMCLOUD_API_KEY=<api_key>
  ```

Important

You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.

### [7.7. Creating the installation configuration file](#installation-initializing_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host.
* You have the `imageContentSources` values that were generated during mirror registry creation.
* You have obtained the contents of the certificate for your mirror registry.
* You have retrieved a Red Hat Enterprise Linux CoreOS (RHCOS) image and uploaded it to an accessible location.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

        Note

        Always delete the `~/.powervs` directory to avoid reusing a stale configuration. Run the following command:

        ```
        $ rm -rf ~/.powervs
        ```
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **powervs** as the platform to target.
      3. Select the region to deploy the cluster to.
      4. Select the zone to deploy the cluster to.
      5. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      6. Enter a descriptive name for your cluster.
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
   3. Define the network for the VPC to install the cluster in under the parent `platform.powervs` field:

      ```
      vpcName: <existing_vpc>
      ```

      For `platform.powervs.vpcName`, specify the name for the existing IBM Cloud® VPC.
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

#### [7.7.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 7.1. Minimum resource requirements

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

#### [7.7.2. Sample customized install-config.yaml file for IBM Power Virtual Server](#installation-ibm-power-vs-config-yaml_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters.

Important

This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and change it.

```
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    powervs:
      smtLevel: 8
    ibmcloud: {}
  replicas: 3
metadata:
  name: example-restricted-cluster-name
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 192.168.0.0/24
platform:
  powervs:
    userid: ibm-user-id
    powervsResourceGroup: "ibmcloud-resource-group"
    region: "powervs-region"
    vpcRegion: "vpc-region"
    vpcName: name-of-existing-vpc
    zone: "powervs-zone"
    serviceInstanceID: "service-instance-id"
publish: Internal
credentialsMode: Manual
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
sshKey: ssh-ed25519 AAAA...
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
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
:   Specifies the base domain of the cluster. This value is required.

`metadata.name`
:   Specifies the name of the cluster. This value is required.

`compute`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The first line of the `compute` section must begin with a hyphen, `-`.

`compute.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

`compute.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the compute machines. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

`controlPlane`
:   Specifies parameters where, if you do not provide values, the installation program provides the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used.

`controlPlane.hyperthreading`
:   Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

    Important

    When multithreading (SMT) is disabled, each vCPU is equivalent to one physical core. Disable SMT only if you have specific requirements.

`controlPlane.platform.powervs.smtLevel`
:   Specifies the level of SMT to set to the control plane. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes.

    Note

    When simultaneous multithreading (SMT) is not enabled, one vCPU is equivalent to one physical core. When enabled, total vCPUs is computed as (Thread(s) per core \* Core(s) per socket) \* Socket(s). The smtLevel controls the threads per core. Lower SMT levels may require additional assigned cores when deploying the cluster nodes. You can do this by setting the `'processors'` parameter in the `install-config.yaml` file to an appropriate value to meet the requirements for deploying OpenShift Container Platform successfully.

`networking.clusterNetwork.cidr`
:   Specifies the CIDR. The machine CIDR must contain the subnets for the compute machines and control plane machines.

`networking.machineNetwork.cidr`
:   Specifies the CIDR. The CIDR must contain the subnets defined in `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`.

`networking.networkType`
:   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`platform.powervs.powervsResourceGroup`
:   Specifies the name of an existing resource group. The existing VPC and subnets should be in this resource group. The cluster is deployed to this resource group.

`platform.powervs.vpcName`
:   Specifies the name of an existing VPC.

`pullSecret`
:   Specifies the pull secret for your mirror registry. For `<local_registry>`, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, registry.example.com or registry.example.com:5000. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.

`sshKey`
:   Specifies the SSH key to use to access the machines in your cluster. This value is optional.

    Note

    For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

`additionalTrustBundle`
:   Specifies the contents of the certificate file that you used for your mirror registry.

`imageContentSources`
:   Specifies the `imageContentSources` section from the output of the command to mirror the repository.

#### [7.7.3. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [7.8. Manually creating IAM](#manually-create-iam-ibm-cloud_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Cloud Credential Operator (CCO) must operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for your cloud provider.

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources.

**Prerequisites**

* You have configured the `ccoctl` binary.
* You have an existing `install-config.yaml` file.

**Procedure**

1. Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`.

   **Example `install-config.yaml` configuration file**

   ```
   apiVersion: v1
   baseDomain: cluster1.example.com
   credentialsMode: Manual
   compute:
   - architecture: ppc64le
     hyperthreading: Enabled
   ```

   where:

   `credentialsMode`
   :   Specifies the CCO credentials mode. Set the value to `Manual`.
2. To generate the manifests, run the following command from the directory that includes the installation program:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
3. From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
4. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

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
   :   Specifies that only the manifests that your specific cluster configuration requires are included.

   `--install-config`
   :   Specifies the location of the `install-config.yaml` file.

   `--to`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
         apiVersion: cloudcredential.openshift.io/v1
         kind: CredentialsRequest
         metadata:
           labels:
             controller-tools.k8s.io: "1.0"
           name: openshift-image-registry-ibmcos
           namespace: openshift-cloud-credential-operator
         spec:
           secretRef:
             name: installer-cloud-credentials
             namespace: openshift-image-registry
           providerSpec:
             apiVersion: cloudcredential.openshift.io/v1
             kind: IBMCloudProviderSpec
             policies:
             - attributes:
               - name: serviceName
                 value: cloud-object-storage
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
               - crn:v1:bluemix:public:iam::::role:Operator
               - crn:v1:bluemix:public:iam::::role:Editor
               - crn:v1:bluemix:public:iam::::serviceRole:Reader
               - crn:v1:bluemix:public:iam::::serviceRole:Writer
             - attributes:
               - name: resourceType
                 value: resource-group
               roles:
               - crn:v1:bluemix:public:iam::::role:Viewer
       ```
5. Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret:

   ```
   $ ccoctl ibmcloud create-service-id \
     --credentials-requests-dir=<path_to_credential_requests_directory> \
     --name=<cluster_name> \
     --output-dir=<installation_directory> \
     --resource-group-name=<resource_group_name>
   ```

   where:

   `<path_to_credential_requests_directory>`
   :   Specifies the directory that has the files for the `CredentialsRequest` objects.

   `<cluster_name>`
   :   Specifies the name of the OpenShift Container Platform cluster.

   `<installation_directory>`
   :   Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands. This parameter is optional.

   `<resource_group_name>`
   :   Specifies the name of the resource group used for scoping the access policies. This parameter is optional.

       Note

       If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object.

       If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command:

       ```
       $ grep resourceGroup <installation_directory>/manifests/cluster-infrastructure-02-config.yml
       ```

**Verification**

* Check that the appropriate secrets exist in the `manifests` directory of your cluster.

### [7.9. Deploying the cluster](#installation-launching-installer_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

* In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ```
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  + For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
  + To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

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

### [7.10. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [7.11. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [7.12. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [7.13. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [7.14. Disabling the default software catalog sources](#olm-restricted-networks-operatorhub_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator.

**Procedure**

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ```
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  Tip

  Or, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

### [7.15. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-restricted-networks-ibm-power-vs) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

## [Chapter 8. Uninstalling a cluster on IBM Power Virtual Server](#uninstalling-cluster-ibm-power-vs) Copy linkLink copied to clipboard!

To remove a OpenShift Container Platform cluster that you deployed on IBM Power® Virtual Server, run the delete cluster command to remove all associated cloud resources.

### [8.1. Removing a cluster that uses installer-provisioned infrastructure](#installation-uninstall-clouds_uninstalling-cluster-ibm-power-vs) Copy linkLink copied to clipboard!

To remove an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, you can use the installation program and the installation files from your original deployment to uninstall the cluster from your cloud platform.

Note

After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource.

**Prerequisites**

* You have a copy of the installation program that you used to deploy the cluster.
* You have the files that the installation program generated when you created your cluster.
* You have configured the `ccoctl` binary.
* You have installed the IBM Cloud® CLI and installed or updated the VPC infrastructure service plugin. For more information see "Prerequisites" in the [IBM Cloud® CLI documentation](https://cloud.ibm.com/docs/vpc?topic=vpc-infrastructure-cli-plugin-vpc-reference&interface=ui#cli-ref-prereqs).

**Procedure**

1. If the following conditions are met, this step is required:

   * The installer created a resource group as part of the installation process.
   * You or one of your applications created persistent volume claims (PVCs) after the cluster was deployed.

     In which case, the PVCs are not removed when uninstalling the cluster, which might prevent the resource group from being successfully removed. To prevent a failure:

     1. Log in to the IBM Cloud® using the CLI.
     2. To list the PVCs, run the following command:

        ```
        $ ibmcloud is volumes --resource-group-name <infrastructure_id>
        ```

        For more information about listing volumes, see the [IBM Cloud® CLI documentation](https://cloud.ibm.com/docs/vpc?topic=vpc-infrastructure-cli-plugin-vpc-reference&interface=ui#volume-cli).
     3. To delete the PVCs, run the following command:

        ```
        $ ibmcloud is volume-delete --force <volume_id>
        ```

        For more information about deleting volumes, see the [IBM Cloud® CLI documentation](https://cloud.ibm.com/docs/vpc?topic=vpc-infrastructure-cli-plugin-vpc-reference&interface=ui#volume-delete).
2. Export the API key that was created as part of the installation process.

   ```
   $ export IBMCLOUD_API_KEY=<api_key>
   ```

   Note

   You must set the variable name exactly as specified. The installation program expects the variable name to be present to remove the service IDs that were created when the cluster was installed.
3. From the directory that has the installation program on the computer that you used to install the cluster, run the following command:

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

       * You must specify the directory that has the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster.
       * You might have to run the `openshift-install destroy` command up to three times to ensure a proper cleanup.
4. Remove the manual CCO credentials that were created for the cluster:

   ```
   $ ccoctl ibmcloud delete-service-id \
       --credentials-requests-dir <path_to_credential_requests_directory> \
       --name <cluster_name>
   ```

   Note

   If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
5. Optional: Delete the `<installation_directory>` directory and the OpenShift Container Platform installation program.

## [Chapter 9. Installation configuration parameters for IBM Power Virtual Server](#installation-config-parameters-ibm-power-vs) Copy linkLink copied to clipboard!

Before you deploy an OpenShift Container Platform cluster on IBM Power® Virtual Server, you supply parameters to customize your cluster and the platform that hosts it.

When you create the `install-config.yaml` file, you provide values for the required parameters through the command line. You can then modify the `install-config.yaml` file to customize your cluster further.

### [9.1. Available installation configuration parameters for IBM Power Virtual Server](#installation-configuration-parameters_installation-config-parameters-ibm-power-vs) Copy linkLink copied to clipboard!

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required, optional, and IBM Power Virtual Server-specific installation configuration parameters that you can set as part of the installation process.

Important

After installation, you cannot change these parameters in the `install-config.yaml` file.

#### [9.1.1. Required configuration parameters](#installation-configuration-parameters-required_installation-config-parameters-ibm-power-vs) Copy linkLink copied to clipboard!

Required installation configuration parameters are described in the following table:

Expand

Table 9.1. Required parameters

| Parameter | Description |
| --- | --- |
| ``` apiVersion: ``` | The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String |
| ``` baseDomain: ``` | The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`. |
| ``` metadata: ``` | Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object |
| ``` metadata:   name: ``` | The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`. |
| ``` platform: ``` | The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object |
| ``` pullSecret: ``` | Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:**  ``` {    "auths":{       "cloud.openshift.com":{          "auth":"b3Blb=",          "email":"you@example.com"       },       "quay.io":{          "auth":"b3Blb=",          "email":"you@example.com"       }    } } ``` |
| ``` platform:   powervs:     userID: ``` | The UserID is the login for the user’s IBM Cloud® account.  **Value:** String. For example, `existing_user_id`. |
| ``` platform:   powervs:     powervsResourceGroup: ``` | The PowerVSResourceGroup is the resource group in which IBM Power® Virtual Server resources are created. If using an existing VPC, the existing VPC and subnets should be in this resource group.  **Value:** String. For example, `existing_resource_group`. |
| ``` platform:   powervs:     region: ``` | Specifies the IBM Cloud® region where the cluster is created.  **Value:** String. For example, `existing_region`. |
| ``` platform:   powervs:     zone: ``` | Specifies the IBM Cloud® colo region where the cluster is created.  **Value:** String. For example, `existing_zone`. |

Show more

#### [9.1.2. Network configuration parameters](#installation-configuration-parameters-network_installation-config-parameters-ibm-power-vs) Copy linkLink copied to clipboard!

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults.

Only IPv4 addresses are supported.

Expand

Table 9.2. Network parameters

| Parameter | Description |
| --- | --- |
| ``` networking: ``` | The configuration for the cluster network.  **Value:** Object  Note  You cannot change parameters specified by the `networking` object after installation. |
| ``` networking:   networkType: ``` | The Red Hat OpenShift Networking network plugin to install.  **Value:** The default value is `OVNKubernetes`. |
| ``` networking:   clusterNetwork: ``` | The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  ``` networking:   clusterNetwork:   - cidr: 10.128.0.0/14     hostPrefix: 23 ``` |
| ``` networking:   clusterNetwork:     cidr: ``` | Required if you use `networking.clusterNetwork`. An IP address block.  An IPv4 network. |
| ``` networking:   clusterNetwork:     hostPrefix: ``` | The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  The default value is `23`. |
| ``` networking:   serviceNetwork: ``` | The IP address block for services. The default value is `172.30.0.0/16`.  **Value:** An array with an IP address block in CIDR format. For example:  ``` networking:   serviceNetwork:    - 172.30.0.0/16 ``` |
| ``` networking:   machineNetwork: ``` | The IP address blocks for machines.  **Value:** An array of objects. For example:  ``` networking:   machineNetwork:   - cidr: 10.0.0.0/16 ``` |
| ``` networking:   machineNetwork:     cidr: ``` | Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `192.168.0.0/24`.  Note  Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction:  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. * In both cases, you must provide an IPv4 CIDR entry. |
| ``` networking:   ovnKubernetesConfig:     ipv4:       internalJoinSubnet: ``` | Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`. |

Show more

#### [9.1.3. Optional configuration parameters](#installation-configuration-parameters-optional_installation-config-parameters-ibm-power-vs) Copy linkLink copied to clipboard!

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
| ``` compute:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, heterogeneous clusters are not supported, so all pools must specify the same architecture. The valid value is the default: `ppc64le`.  **Value:** String |
| ``` compute:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` compute:   smtLevel: ``` | The SMTLevel specifies the level of SMT to set to the control plane and compute machines. Valid values are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `off`, and `on`.  **Value:** String |
| ``` compute:   name: ``` | Required if you use `compute`. The name of the machine pool.  **Value:** `worker` |
| ``` compute:   platform: ``` | Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  Example usage, `compute.platform.powervs.sysType`. |
| ``` compute:   platform:     powervs:       sysType: ``` | Defines the system type for the instance.  **Value:** The available system types depend on the zone you want to target. Supported values are `e980`, `s922`, `e1080`, or `s1022`.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}` |
| ``` compute:   replicas: ``` | The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`. |
| ``` featureSet: ``` | Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`. |
| ``` controlPlane: ``` | The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects. |
| ``` controlPlane:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, heterogeneous clusters are not supported, so all pools must specify the same architecture. The valid value is the default: `ppc64le`.  **Value:** String |
| ``` controlPlane:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` controlPlane:   name: ``` | Required if you use `controlPlane`. The name of the machine pool.  **Value:** `master` |
| ``` controlPlane:   platform: ``` | Required if you use `controlPlane`. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the `compute.platform` parameter value.  Example usage, `controlPlane.platform.powervs.processors`. |
| ``` controlPlane:   platform:     powervs:       sysType: ``` | Defines the system type for the instance.  **Value:** The available system types depend on the zone you want to target. Supported values are `e980`, `s922`, `e1080`, or `s1022`.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}` |
| ``` controlPlane:   replicas: ``` | The number of control plane machines to provision.  **Value:** Supported values are `3`, or `1` when deploying single-node OpenShift. |
| ``` arbiter:     name: ``` | The OpenShift Container Platform cluster requires a name for arbiter nodes. For example, `arbiter`. |
| ``` arbiter:     replicas: ``` | The `replicas` parameter sets the number of arbiter nodes for the OpenShift Container Platform cluster. You cannot set this field to a value that is greater than 1. |
| ``` credentialsMode: ``` | The Cloud Credential Operator (CCO) mode. If no mode is specified, the CCO dynamically tries to determine the capabilities of the provided credentials, with a preference for mint mode on the platforms where multiple modes are supported.  Note  Not all CCO modes are supported for all cloud providers. For more information about CCO modes, see the "Managing cloud provider credentials" entry in the *Authentication and authorization* content.  **Value:** `Mint`, `Passthrough`, `Manual` or an empty string (`""`). |
| ``` imageContentSources: ``` | Sources and repositories for the release-image content.  **Value:** Array of objects. Includes a `source` and, optionally, `mirrors`, as described in the following rows of this table. |
| ``` imageContentSources:   source: ``` | Required if you use `imageContentSources`. Specify the repository that users refer to, for example, in image pull specifications.  **Value:** String |
| ``` imageContentSources:   mirrors: ``` | Specify one or more repositories that might also contain the same images.  **Value:** Array of strings |
| ``` osImageStream: ``` | Specifies the image stream that will be used for all machines in the cluster. `osImageStream` is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.  **Value:** String. Valid values are `rhel-9` or `rhel-10`. |
| ``` publish: ``` | How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.  **Value:**`Internal` or `External`. The default value is `External`.  Setting this field to `Internal` is not supported on non-cloud platforms. |
| ``` sshKey: ``` | The SSH key to authenticate access to your cluster machines.  Note  For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.  **Value:** For example, `sshKey: ssh-ed25519 AAAA..`. |
| ``` platform:   powervs:     vpcRegion: ``` | Specifies the IBM Cloud® region in which to create VPC resources.  **Value:** String. For example, `existing_vpc_region`. |
| ``` platform:   powervs:     vpcSubnets: ``` | Specifies existing subnets by name where cluster resources are created.  **Value:** String. For example, `powervs_region_example_subnet`. |
| ``` platform:   powervs:     vpcName: ``` | Specifies the IBM Cloud® name.  **Value:** String. For example, `existing_vpcName`. |
| ``` platform:   powervs:     serviceInstanceGUID: ``` | Specifies the ID of the Power IAAS instance created from the IBM Cloud® Catalog.  **Value:** String. For example, `existing_service_instance_GUID`. |
| ``` platform:   powervs:     clusterOSImage: ``` | Specifies a pre-created IBM Power® Virtual Server boot image that overrides the default image for cluster nodes.  **Value:** String. For example, `existing_cluster_os_image`. |
| ``` platform:   powervs:     defaultMachinePlatform: ``` | Specifies the default configuration used when installing on IBM Power® Virtual Server for machine pools that do not define their own platform configuration.  **Value:** String. For example, `existing_machine_platform`. |
| ``` platform:   powervs:     memoryGiB: ``` | Specifies the size of a virtual machine’s memory, in GB.  **Value:** The valid integer must be an integer number of GB that is at least `2` and no more than `64`, depending on the machine type. |
| ``` platform:   powervs:     procType: ``` | Defines the processor sharing model for the instance.  **Value:** The valid values are `Capped`, `Dedicated`, and `Shared`. |
| ``` platform:   powervs:     processors: ``` | Defines the processing units for the instance.  **Value:** The number of processors must be from `.5` to `32` cores. The processors must be in increments of `.25`. |
| ``` platform:   powervs:     tgName: ``` | Defines the name of an existing Transit Gateway.  **Value:** String. For example, `existing_tgName`. |

Show more

## [Legal Notice](#idm139776231484048) Copy linkLink copied to clipboard!

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
