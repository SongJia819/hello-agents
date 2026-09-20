---
title: "Installing on IBM PowerVC"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_powervc/index
retrieved_at: 2026-09-05T05:42:06.391012+00:00
---

# Installing on IBM PowerVC

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on IBM PowerVC

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140489807525120)

**Abstract**

This document describes how to install OpenShift Container Platform on IBM PowerVC.

---

## [Chapter 1. Installation methods](#installation-methods-ibm-powervc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on IBM PowerVC, use the installer-provisioned infrastructure method, which lets the installation program provision the underlying cluster infrastructure for you.

### [1.1. Installing a cluster on installer-provisioned infrastructure](#installation-methods-ibm-powervc_installation-methods-ibm-powervc) Copy linkLink copied to clipboard!

You can install a OpenShift Container Platform cluster on IBM PowerVC using installer-provisioned infrastructure. The installation program provisions the required infrastructure and supports customization at installation time, with additional options available postinstallation.

* **Installing a cluster on IBM PowerVC with customizations**: You can install a customized cluster on IBM PowerVC. The installation program supports some customization at the installation stage. Many other customization options are available postinstallation.

## [Chapter 2. Installing a cluster on IBM PowerVC with customizations](#installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

To install a customized OpenShift Container Platform cluster on IBM PowerVC, change the parameters in the `install-config.yaml` file before you run the installation program.

### [2.1. Prerequisites for installing a cluster on IBM(R) Power(R) Virtualization Center](#prereqs-ibm-powervc_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM PowerVC, verify that you have a load balancer and a DHCP server available on the target network.

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You have a load balancing service you can use with the IBM PowerVC network you intend to use.
* You have a DHCP server backing the IBM PowerVC network you intend to use.

### [2.2. Infrastructure requirements for installing OpenShift Container Platform on IBM PowerVC](#installation-ibm-powervc-infra-requirements_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

To support an OpenShift Container Platform installation by using the installation program, you need to prepare your IBM PowerVC environment.

#### [2.2.1. IBM PowerVC account privilege requirements](#installation-ibm-powervc-infra-requirements-account_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

When installing OpenShift Container Platform on IBM PowerVC by using the installation program, you must use an administrative account to ensure that you have all required permissions.

#### [2.2.2. IBM PowerVC image requirements](#installation-ibm-powervc-infra-requirements-image_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

You must import a Red Hat Enterprise Linux CoreOS (RHCOS) image. This can be found by using the installation program.

```
$ openshift-install coreos print-stream-json | jq -r '.architectures.ppc64le.artifacts.openstack' | jq -r '.formats."qcow2.gz".disk.location'
```

After downloading the image from the resultant URL, you can import the image into IBM PowerVC by using the `powervc-image-import` tool.

#### [2.2.3. Networking requirements](#installation-ibm-powervc-infra-requirements-networking_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

#### [2.2.4. IBM PowerVC network](#ibm-powervc-network) Copy linkLink copied to clipboard!

Installation requires at least one PowerVC network. Ideally the network should be dedicated to your OpenShift Container Platform cluster and not shared with other workloads.

IBM recommends that the network is set as a DHCP network in IBM PowerVC. You must have a DHCP server set up to assign addresses for this network. When using this type of network, IBM PowerVC is not aware of the IP address that is assigned to the created servers.

#### [2.2.5. DNS records](#dns-records) Copy linkLink copied to clipboard!

DNS records pointing to a `LoadBalancer` service are required for installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

Expand

Table 2.1. Required DNS records

| Component | Record | Description |
| --- | --- | --- |
| API VIP | `api.<cluster_name>.<base_domain>.` | This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the cluster. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| API VIP | `api-int.<cluster_name>.<base_domain>.` | This DNS A/AAAA or CNAME (Canonical Name) record must point to the load balancer for the cluster. This record must be resolvable by all the nodes within the cluster. |
| Ingress VIP | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the machines that run the Ingress router pods, which are the compute nodes by default. This record must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |

Show more

### [2.3. Resource guidelines for installing OpenShift Container Platform on IBM PowerVC](#installation-ibm-powervc-default-deployment_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

To support an OpenShift Container Platform installation, it is recommended that your IBM PowerVC has room for the following resources available:

Expand

Table 2.2. Recommended resources for a default OpenShift Container Platform cluster on IBM PowerVC

| Resource | Value |
| --- | --- |
| Subnets | 1 |
| RAM | 88 GB |
| vCPUs | 22 |
| Volume storage | 275 GB |
| Instances | 7 |

Show more

A cluster might function with fewer than recommended resources.

#### [2.3.1. Load balancing requirements for user-provisioned infrastructure](#installation-load-balancing-user-infra_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

Table 2.3. Application Ingress load balancer

| Port | Back-end machines (pool members) | Internal | External | Description |
| --- | --- | --- | --- | --- |
| `443` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTPS traffic |
| `80` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTP traffic |

Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

##### [2.3.1.1. Example load balancer configuration for user-provisioned clusters](#installation-load-balancing-user-infra-example_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.4. Obtaining the installation program](#installation-obtaining-installer_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.5. Creating the installation configuration file](#installation-initializing_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on IBM PowerVC.

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
      * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Enter a descriptive name for your cluster.
2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.
3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [2.5.1. Installation configuration for a cluster on IBM PowerVC with a user-managed load balancer](#install-powervc-standard-config_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

The `install-config.yaml` parameters required to deploy an OpenShift Container Platform cluster on IBM PowerVC using an external, user-managed load balancer help you configure networking, compute, and platform settings for this setup.

The following example `install-config.yaml` file demonstrates this configuration.

Important

This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program.

```
apiVersion: v1
baseDomain: mydomain.test
compute:
- architecture: ppc64le
  hyperthreading: Enabled
  name: worker
  platform:
    powervc:
      zones:
        - powervc-sample-project
  replicas: 3
controlPlane:
  architecture: ppc64le
  name: master
  platform:
    powervc:
      zones:
        - s1122
  replicas: 3
metadata:
  creationTimestamp: null
  name: ocp-on-powervc
networking:
  clusterNetwork:
  - cidr: 10.100.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.100.32.0/20
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  powervc:
    apiVIPs:
    - 10.20.188.52
    cloud: powervc
    clusterOSImage: my-rhcos-image
    defaultMachinePlatform:
      type: my-powervc-project
    ingressVIPs:
    - 10.20.188.52
    controlPlanePort:
      fixedIPs:
        - subnet:
            id: ae643a65-d0fc-4408-90c6-a820340bfade
```

* `apiVIPs`: Specifies the address of the user-managed load balancer.
* `ingressVIPs`: Specifies the address of the user-managed load balancer.
* `controlPlanePort.fixedIPs.subnet.id`: Specifies the subnet that is served by the user-managed DHCP server.

### [2.6. Deploying the cluster](#installation-launching-installer_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.7. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.8. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.9. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.10. Verifying cluster status](#installation-osp-verifying-cluster-status_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

You can verify your OpenShift Container Platform cluster’s status during or after installation.

**Procedure**

1. In the cluster environment, export the administrator’s kubeconfig file by entering the following command:

   ```
   $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
   ```

   * For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

     The `kubeconfig` file contains information about the cluster that is used by the CLI to connect a client to the correct cluster and API server.
2. View the control plane and compute machines created after a deployment by entering the following command:

   ```
   $ oc get nodes
   ```
3. View the version of your cluster by entering the following command:

   ```
   $ oc get clusterversion
   ```
4. View the status of the cluster Operators by entering the following command:

   ```
   $ oc get clusteroperator
   ```
5. View all running pods in the cluster by entering the following command:

   ```
   $ oc get pods -A
   ```

### [2.11. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

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

### [2.12. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-ibm-powervc-installer-custom) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

## [Chapter 3. Installation configuration parameters for IBM PowerVC](#installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

Before you deploy an OpenShift Container Platform cluster on IBM® Power® Virtualization Center, you provide parameters to customize your cluster and the platform that hosts it. When you create the `install-config.yaml` file, you provide values for the required parameters through the command line. You can then modify the `install-config.yaml` file to customize your cluster further.

### [3.1. Available installation configuration parameters for IBM PowerVC](#installation-configuration-parameters_installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required, optional, and IBM PowerVC-specific installation configuration parameters that you can set as part of the installation process.

Important

After installation, you cannot change these parameters in the `install-config.yaml` file.

#### [3.1.1. Required configuration parameters](#installation-configuration-parameters-required_installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

Required installation configuration parameters are described in the following table:

Expand

Table 3.1. Required parameters

| Parameter | Description |
| --- | --- |
| ``` apiVersion: ``` | The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String |
| ``` baseDomain: ``` | The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`. |
| ``` metadata: ``` | Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object |
| ``` metadata:   name: ``` | The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`. |
| ``` platform: ``` | The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object |
| ``` pullSecret: ``` | Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:**  ``` {    "auths":{       "cloud.openshift.com":{          "auth":"b3Blb=",          "email":"you@example.com"       },       "quay.io":{          "auth":"b3Blb=",          "email":"you@example.com"       }    } } ``` |

Show more

#### [3.1.2. Additional IBM PowerVC configuration parameters](#installation-configuration-parameters-additional-powervc_installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

Additional IBM PowerVC configuration parameters are described in the following table:

Expand

Table 3.2. Additional IBM PowerVC parameters

| Parameter | Description |
| --- | --- |
| ``` platform:   powervc:     cloud: ``` | The name of the IBM PowerVC cloud to use from the list of clouds in the `clouds.yaml` file.  In the cloud configuration in the `clouds.yaml` file, if possible, use application credentials rather than a user name and password combination. Using application credentials avoids disruptions from secret propagation that follow user name and password rotation.  **Value:** String, for example `MyCloud`. |

Show more

#### [3.1.3. Optional IBM PowerVC configuration parameters](#installation-configuration-parameters-optional-ibm-power-vc_installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

Optional IBM PowerVC configuration parameters are described in the following table:

Expand

Table 3.3. Optional IBM PowerVC parameters

| Parameter | Description |
| --- | --- |
| ``` compute:   platform:     powervc:       zones: ``` | IBM PowerVC Compute availability zones to install machines on. If this parameter is not set, the installation program relies on the default settings that the IBM PowerVC administrator configured.  **Value:** A list of strings. For example, `["zone-1", "zone-2"]`. |
| ``` controlPlane:   platform:     powervc:       zones: ``` | IBM PowerVC Compute availability zones to install machines on. If this parameter is not set, the installation program relies on the default settings that the IBM PowerVC administrator configured.  **Value:** A list of strings. For example, `["zone-1", "zone-2"]`. |
| ``` platform:   powervc:     clusterOSImage: ``` | The name of the existing IBM PowerVC image.  **Value:** the name of an existing IBM PowerVC image, for example `my-rhcos`. |
| ``` platform:   powervc:     controlPlanePort:       fixedIPs: ``` | Subnets for the machines to use.  **Value:** A list of subnet names or UUIDs to use in cluster installation. |
| ``` platform:   powervc:     controlPlanePort:       network: ``` | A network for the machines to use.  **Value:** The UUID or name of an IBM PowerVC network to use in cluster installation. |
| ``` platform:   powervc:     defaultMachinePlatform: ``` | The default machine pool platform configuration.  **Value:**  ``` {    "type": "my-compute-template", } ``` |
| ``` platform:   powervc:     externalDNS: ``` | IP addresses for external DNS servers that cluster instances use for DNS resolution.  **Value:** A list of IP addresses as strings. For example, `["8.8.8.8", "192.168.1.12"]`. |
| ``` platform:   powervc:     loadbalancer: ``` | Whether or not to use the default, internal load balancer. If the value is set to `UserManaged`, this default load balancer is disabled so that you can deploy a cluster that uses an external, user-managed load balancer. If the parameter is not set, or if the value is `OpenShiftManagedDefault`, the cluster uses the default load balancer.  **Value:** `UserManaged` or `OpenShiftManagedDefault`. |
| ``` platform:   powervc:     apiVIPs: ``` | Virtual IP (VIP) addresses that you configured for control plane API access.  **Value:** A list of IP addresses as strings. For example, `["10.0.0.30", "10.0.0.31"]` |
| ``` platform:   powervc:     ingressVIPs: ``` | Virtual IP (VIP) addresses that you configured for cluster ingress.  **Value:** A list of IP addresses as strings. For example, `["10.0.0.32", "10.0.0.33"]` |

Show more

#### [3.1.4. Network configuration parameters](#installation-configuration-parameters-network_installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults.

Only IPv4 addresses are supported.

Expand

Table 3.4. Network parameters

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

#### [3.1.5. Optional configuration parameters](#installation-configuration-parameters-optional_installation-config-parameters-ibm-powervc) Copy linkLink copied to clipboard!

Optional installation configuration parameters are described in the following table:

Expand

Table 3.5. Optional parameters

| Parameter | Description |
| --- | --- |
| ``` additionalTrustBundle: ``` | A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.  **Value:** String |
| ``` capabilities: ``` | Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in *Installing*.  **Value:** String array |
| ``` capabilities:   baselineCapabilitySet: ``` | Selects an initial set of optional capabilities to enable. Valid values are `None`, `v4.11`, `v4.12` and `vCurrent`. The default value is `vCurrent`.  **Value:** String |
| ``` capabilities:   additionalEnabledCapabilities: ``` | Extends the set of optional capabilities beyond what you specify in `baselineCapabilitySet`. You can specify multiple capabilities in this parameter.  **Value:** String array |
| ``` cpuPartitioningMode: ``` | Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the *Workload partitioning* page in the *Scalability and Performance* section.  **Value:** `None` or `AllNodes`. `None` is the default value. |
| ``` compute: ``` | The configuration for the machines that comprise the compute nodes.  **Value:** Array of `MachinePool` objects. |
| ``` compute:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64` (the default).  **Value:** String |
| ``` compute:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` compute:   name: ``` | Required if you use `compute`. The name of the machine pool.  **Value:** `worker` |
| ``` compute:   platform: ``` | Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}` |
| ``` compute:   replicas: ``` | The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`. |
| ``` featureSet: ``` | Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`. |
| ``` controlPlane: ``` | The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects. |
| ``` controlPlane:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64` (the default).  **Value:** String |
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

## [Chapter 4. Uninstalling a cluster on IBM PowerVC](#uninstalling-cluster-ibm-powervc) Copy linkLink copied to clipboard!

You can remove a cluster that you deployed to IBM PowerVC using the installation program.

### [4.1. Removing a cluster that uses installer-provisioned infrastructure](#installation-uninstall-clouds_uninstalling-cluster-ibm-powervc) Copy linkLink copied to clipboard!

To remove an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, you can use the installation program and the installation files from your original deployment to uninstall the cluster from your cloud platform.

Note

After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource.

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

## [Legal Notice](#idm140489807525120) Copy linkLink copied to clipboard!

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
