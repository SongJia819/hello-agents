---
title: "Installation configuration"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/index
retrieved_at: 2026-09-05T05:41:54.610130+00:00
---

# Installation configuration

---

OpenShift Container Platform 4.22

## Cluster-wide configuration during installations

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140014192642752)

**Abstract**

This document describes how to perform initial OpenShift Container Platform cluster configuration.

---

## [Chapter 1. Customizing nodes](#installing-customizing) Copy linkLink copied to clipboard!

You can customize nodes both cluster-wide and per-machine configuration through Ignition, which allows arbitrary partitioning and file content changes to the operating system.

If a configuration file is documented in Red Hat Enterprise Linux (RHEL), you can modify the file through Ignition.

There are two ways to deploy machine config changes:

* Creating machine configs that are included in manifest files to start up a cluster during `openshift-install`.
* Creating machine configs that are passed to running OpenShift Container Platform nodes through the Machine Config Operator.

Additionally, modifying the reference config, such as the Ignition config that is passed to `coreos-installer` when installing bare-metal nodes allows per-machine configuration. The Machine Config Operator cannot yet see these changes.

The following sections describe features that you might want to configure on your nodes.

### [1.1. Creating machine configs with Butane](#installation-special-config-butane_installing-customizing) Copy linkLink copied to clipboard!

Machine configs are used to configure control plane and compute machines by instructing machines how to create users and file systems, set up the network, install systemd units, and more.

Because modifying machine configs can be difficult, you can use Butane configs to create machine configs for you, thereby making node configuration much easier.

#### [1.1.1. About Butane](#installation-special-config-butane-about_installing-customizing) Copy linkLink copied to clipboard!

Butane is a command-line utility that OpenShift Container Platform uses to provide convenient, short-hand syntax for writing machine configs, and for performing additional validation of machine configs. The format of the Butane config file that Butane accepts is defined in the Butane config specification.

#### [1.1.2. Installing Butane](#installation-special-config-butane-install_installing-customizing) Copy linkLink copied to clipboard!

You can install the Butane tool (`butane`) to create OpenShift Container Platform machine configs from a command-line interface. You can install `butane` on Linux, Windows, or macOS by downloading the corresponding binary file.

Tip

Butane releases are backwards-compatible with older releases and with the Fedora CoreOS Config Transpiler (FCCT).

**Procedure**

1. Navigate to the Butane image download page at <https://mirror.openshift.com/pub/openshift-v4/clients/butane/>.
2. Get the `butane` binary:

   1. To save the latest version of Butane, save the `butane` image to your current directory:

      ```
      $ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane --output butane
      ```
   2. Optional: For a specific architecture, such as aarch64 or ppc64le, indicate the appropriate URL:

      ```
      $ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-aarch64 --output butane
      ```
3. Make the downloaded binary file executable:

   ```
   $ chmod +x butane
   ```
4. Move the `butane` binary file to a directory on your `PATH`.

   To check your `PATH`, open a terminal and execute the following command:

   ```
   $ echo $PATH
   ```

**Verification**

* You can now use the Butane tool by running the `butane` command:

  ```
  $ butane <butane_file>
  ```

#### [1.1.3. Creating a MachineConfig object by using Butane](#installation-special-config-butane-create_installing-customizing) Copy linkLink copied to clipboard!

You can use Butane to produce a `MachineConfig` object so that you can configure compute or control plane nodes at installation time or through the Machine Config Operator.

**Prerequisites**

* You have installed the `butane` utility.

**Procedure**

1. Create a Butane config file. The following example creates a file named `99-worker-custom.bu` that configures kernel debug messages and specifies custom settings for the chrony time service:

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 99-worker-custom
     labels:
       machineconfiguration.openshift.io/role: worker
   openshift:
     kernel_arguments:
       - loglevel=7
   storage:
     files:
       - path: /etc/chrony.conf
         mode: 0644
         overwrite: true
         contents:
           inline: |
             pool 0.rhel.pool.ntp.org iburst
             driftfile /var/lib/chrony/drift
             makestep 1.0 3
             rtcsync
             logdir /var/log/chrony
   ```

   Note

   The `99-worker-custom.bu` file is set to create a machine config for compute nodes. To deploy on control plane nodes, change the role from `worker` to `master`. To configure both node types, repeat the procedure and specify different file names and roles for each node type.
2. Create a `MachineConfig` object by giving Butane the file that you created in the previous step:

   ```
   $ butane 99-worker-custom.bu -o ./99-worker-custom.yaml
   ```

   A `MachineConfig` object YAML file is created for you to finish configuring your machines.
3. Save the Butane config in case you need to update the `MachineConfig` object in the future.
4. Choose one of the following options:

   * If the cluster is not running yet, generate manifest files and add the `MachineConfig` object YAML file to the `openshift` directory.
   * If the cluster is already running, apply the file as follows:

     ```
     $ oc create -f 99-worker-custom.yaml
     ```

### [1.3. Adding day-1 kernel arguments](#installation-special-config-kargs_installing-customizing) Copy linkLink copied to clipboard!

You can add kernel arguments to all control plane and compute nodes during initial cluster installation. This approach ensures the arguments take effect before the first boot operation of the system. You can also modify kernel arguments as a day-2 activity.

The following list details reasons why you might want to add kernel arguments during cluster installation:

* You need to do some low-level network configuration before the systems start.
* You want to disable a feature, such as SELinux, so it has no impact on the systems when they first come up.

Warning

Disabling SELinux on RHCOS in production is not supported. Re-provision any node with disabled SELinux before including the node in a production cluster.

To add kernel arguments to control plane or compute nodes, you can create a `MachineConfig` object. You can then inject the object into the set of manifest files used by Ignition during cluster setup.

For a listing of arguments you can pass to a RHEL 8 kernel at boot time, see "Kernel.org kernel parameters" in the *Additional resources* section. Add kernel arguments before installation only if they are required to complete the initial OpenShift Container Platform installation.

**Procedure**

1. Change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
2. Determine if you want to add kernel arguments to compute or control plane nodes, or both.
3. In the `openshift` directory, create a file, such as `99-openshift-machineconfig-master-kargs.yaml`, to define a `MachineConfig` object. Add the kernel settings to this file. The example adds a `loglevel=7` kernel argument to control plane nodes.

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: master
     name: 99-openshift-machineconfig-master-kargs
   spec:
     kernelArguments:
       - loglevel=7
   # ...
   ```

   You can change `master` to `worker` to add kernel arguments to compute nodes instead. Create a separate YAML file to add to both control plane and compute nodes.

### [1.4. The addition of kernel modules to nodes](#installation-special-config-kmod_installing-customizing) Copy linkLink copied to clipboard!

For most common hardware, the Linux kernel includes the device driver modules needed to use that hardware when the computer starts up. For some hardware, however, modules are not available in Linux. You must find a way to provide those modules to each host computer.

A subsequent procedure describes how to provide modules for nodes in an OpenShift Container Platform cluster.

When a kernel module is first deployed by following these instructions, the module is made available for the current kernel. If a new kernel is installed, the `kmods-via-containers` software rebuilds and deploys the module so a compatible version of that module is available with the new kernel.

The way that this feature is able to keep the module up to date on each node is by:

* Adding a systemd service to each node that starts at boot time to detect if a new kernel has been installed and
* If a new kernel is detected, the service rebuilds the module and installs it to the kernel

For information on the software needed for this procedure, see "kmods-via-containers".

The following list details some important items before you start the procedure:

* Software tools and examples are not yet available in official RPM form and can only be obtained for now from unofficial `github.com` sites noted in the procedure.
* Third-party kernel modules you might add through these procedures are not supported by Red Hat.
* The software needed to build your kernel modules is deployed in a RHEL 8 container. Remember that modules are rebuilt automatically on each node when that node gets a new kernel. For that reason, each node needs access to a `yum` repository that contains the kernel and related packages needed to rebuild the module. That content is best provided with a valid RHEL subscription.

### [1.5. Building and testing the kernel module container](#building-testing-kernel-module-container_installing-customizing) Copy linkLink copied to clipboard!

Before deploying kernel modules to your OpenShift Container Platform cluster, you can test the process on a separate RHEL system.

Before testing the process, gather the source code for the kernal module, the KVC framework, and the `kmod-via-containers` software. You can then build and test a module on a RHEL system.

**Procedure**

1. Register a RHEL 8 system:

   ```
   # subscription-manager register
   ```
2. Attach a subscription to the RHEL 8 system:

   ```
   # subscription-manager attach --auto
   ```
3. Install software that is required to build the software and container:

   ```
   # yum install podman make git -y
   ```
4. Clone the `kmod-via-containers` repository.

   1. Create a folder for the repository:

      ```
      $ mkdir kmods; cd kmods
      ```
   2. Clone the repository:

      ```
      $ git clone https://github.com/kmods-via-containers/kmods-via-containers
      ```
5. Install a KVC framework instance on your RHEL 8 build host to test the module. This adds a `kmods-via-container` systemd service and loads it:

   1. Change to the `kmod-via-containers` directory:

      ```
      $ cd kmods-via-containers/
      ```
   2. Install the KVC framework instance:

      ```
      $ sudo make install
      ```
   3. Reload the systemd manager configuration:

      ```
      $ sudo systemctl daemon-reload
      ```
6. Get the kernel module source code. The source code might be used to build a third-party module that you do not have control over, but is supplied by others. You will need content similar to the content shown in the `kvc-simple-kmod` example that can be cloned to your system as follows:

   ```
   $ cd .. ; git clone https://github.com/kmods-via-containers/kvc-simple-kmod
   ```
7. Edit the configuration file, `simple-kmod.conf` file, in this example, and change the name of the Dockerfile to `Dockerfile.rhel`:

   1. Change to the `kvc-simple-kmod` directory:

      ```
      $ cd kvc-simple-kmod
      ```
   2. Rename the Dockerfile:

      ```
      $ cat simple-kmod.conf
      ```

      **Example Dockerfile**

      ```
      KMOD_CONTAINER_BUILD_CONTEXT="https://github.com/kmods-via-containers/kvc-simple-kmod.git"
      KMOD_CONTAINER_BUILD_FILE=Dockerfile.rhel
      KMOD_SOFTWARE_VERSION=dd1a7d4
      KMOD_NAMES="simple-kmod simple-procfs-kmod"
      ```
8. Create an instance of `kmods-via-containers@.service` for your kernel module, `simple-kmod` in this example:

   ```
   $ sudo make install
   ```
9. Enable the `kmods-via-containers@.service` instance:

   ```
   $ sudo kmods-via-containers build simple-kmod $(uname -r)
   ```
10. Enable and start the systemd service:

    ```
    $ sudo systemctl enable kmods-via-containers@simple-kmod.service --now
    ```

    1. Review the service status:

       ```
       $ sudo systemctl status kmods-via-containers@simple-kmod.service
       ```

       **Example output**

       ```
       ● kmods-via-containers@simple-kmod.service - Kmods Via Containers - simple-kmod
          Loaded: loaded (/etc/systemd/system/kmods-via-containers@.service;
                 enabled; vendor preset: disabled)
          Active: active (exited) since Sun 2020-01-12 23:49:49 EST; 5s ago...
       ```
11. To confirm that the kernel modules are loaded, use the `lsmod` command to list the modules:

    ```
    $ lsmod | grep simple_
    ```

    **Example output**

    ```
    simple_procfs_kmod     16384  0
    simple_kmod            16384  0
    ```
12. Optional. Use other methods to check that the `simple-kmod` example is working.

    * Look for a "Hello world" message in the kernel ring buffer with `dmesg`:

      ```
      $ dmesg | grep 'Hello world'
      ```

      **Example output**

      ```
      [ 6420.761332] Hello world from simple_kmod.
      ```
    * Check the value of `simple-procfs-kmod` in `/proc`:

      ```
      $ sudo cat /proc/simple-procfs-kmod
      ```

      **Example output**

      ```
      simple-procfs-kmod number = 0
      ```
    * Run the `spkut` command to get more information from the module:

      ```
      $ sudo spkut 44
      ```

      **Example output**

      ```
      KVC: wrapper simple-kmod for 4.22.0-147.3.1.el8_1.x86_64
      Running userspace wrapper using the kernel module container...
      + podman run -i --rm --privileged
         simple-kmod-dd1a7d4:4.22.0-147.3.1.el8_1.x86_64 spkut 44
      simple-procfs-kmod number = 0
      simple-procfs-kmod number = 44
      ```

**Results**

After the system boots, the service checks if a new kernel is running. If there is a new kernel, the service builds a new version of the kernel module and then loads it. If the module is already built, it will just load it.

### [1.6. Provisioning a kernel module to OpenShift Container Platform](#provisioning-kernel-module-to-ocp_installing-customizing) Copy linkLink copied to clipboard!

Depending on whether or not you must have the kernel module in place when OpenShift Container Platform cluster first boots, you can set up the kernel modules to be deployed in one of two ways.

These two ways are listed as follows:

* Provision kernel modules at cluster install time (day-1): You can create the content as a `MachineConfig` object and provide it to `openshift-install` by including it with a set of manifest files.
* Provision kernel modules via Machine Config Operator (day-2): Deploy the kernel module software by using the Machine Config Operator (MCO) after the cluster is running.

Regardless of the provisioning method, each node must be able to obtain the kernel packages and related software packages when a new kernel is detected. You can configure each node to obtain this content in one of the following ways:

* Provide RHEL entitlements to each node.
* Copy RHEL entitlements from the `/etc/pki/entitlement` directory on an existing RHEL host to the same location as the other files. These other files were provided when you built your Ignition config. when you build your Ignition config.
* Add pointers to a `yum` repository containing the kernel and other packages in the Docker file. The pointer must include new kernel packages as they are needed to match newly installed kernels.

#### [1.6.1. Provisioning kernel modules by using a MachineConfig object](#provision-kernel-modules-via-machineconfig_installing-customizing) Copy linkLink copied to clipboard!

Package kernel module software with a `MachineConfig` object to deliver that software to compute or control plane nodes at installation time or through the Machine Config Operator (MCO).

**Procedure**

1. Register a RHEL 8 system:

   ```
   # subscription-manager register
   ```
2. Attach a subscription to the RHEL 8 system:

   ```
   # subscription-manager attach --auto
   ```
3. Install software needed to build the software:

   ```
   # yum install podman make git -y
   ```
4. Create a directory to host the kernel module and tooling:

   ```
   $ mkdir kmods; cd kmods
   ```
5. Get the `kmods-via-containers` software:

   1. Clone the `kmods-via-containers` repository:

      ```
      $ git clone https://github.com/kmods-via-containers/kmods-via-containers
      ```
   2. Clone the `kvc-simple-kmod` repository:

      ```
      $ git clone https://github.com/kmods-via-containers/kvc-simple-kmod
      ```
6. Get your module software. In this example, `kvc-simple-kmod` is used.
7. Create a fakeroot directory and populate it with files that you want to deliver through Ignition, using the repositories cloned earlier:

   1. Create the directory:

      ```
      $ FAKEROOT=$(mktemp -d)
      ```
   2. Change to the `kmod-via-containers` directory:

      ```
      $ cd kmods-via-containers
      ```
   3. Install the KVC framework instance:

      ```
      $ make install DESTDIR=${FAKEROOT}/usr/local CONFDIR=${FAKEROOT}/etc/
      ```
   4. Change to the `kvc-simple-kmod` directory:

      ```
      $ cd ../kvc-simple-kmod
      ```
   5. Create the instance:

      ```
      $ make install DESTDIR=${FAKEROOT}/usr/local CONFDIR=${FAKEROOT}/etc/
      ```
8. Clone the fakeroot directory, replacing any symbolic links with copies of their targets, by running the following command:

   ```
   $ cd .. && rm -rf kmod-tree && cp -Lpr ${FAKEROOT} kmod-tree
   ```
9. Create a Butane config file, `99-simple-kmod.bu`, that embeds the kernel module tree and enables the systemd service.

   Note

   See "Creating machine configs with Butane" for information about Butane.

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 99-simple-kmod
     labels:
       machineconfiguration.openshift.io/role: worker
   storage:
     trees:
       - local: kmod-tree
   systemd:
     units:
       - name: kmods-via-containers@simple-kmod.service
         enabled: true
   ```

   `metadata.labels.machineconfiguration.openshift.io/role`: Specifies the node role. To deploy on control plane nodes, change `worker` to `master`. To deploy on both control plane and compute nodes, perform the remainder of these instructions once for each node type.
10. Use Butane to generate a machine config YAML file, `99-simple-kmod.yaml`, containing the files and configuration to be delivered:

    ```
    $ butane 99-simple-kmod.bu --files-dir . -o 99-simple-kmod.yaml
    ```
11. If the cluster is not up yet, generate manifest files and add this file to the `openshift` directory. If the cluster is already running, apply the file as follows:

    ```
    $ oc create -f 99-simple-kmod.yaml
    ```

    Your nodes will start the `kmods-via-containers@simple-kmod.service` service and the kernel modules will be loaded.
12. To confirm that the kernel modules are loaded, list the modules by running the following command:

    ```
    $ lsmod | grep simple_
    ```

    **Example output**

    ```
    simple_procfs_kmod     16384  0
    simple_kmod            16384  0
    ```

    Note

    You can log in to a node running the `` oc debug node/<openshift-node>`command and then the `chroot /host `` command.

### [1.7. Boot disk encryption and mirroring during installation](#installation-special-config-storage_installing-customizing) Copy linkLink copied to clipboard!

You can configure the OpenShift Container Platform installation to enable boot disk encryption and mirroring on the cluster nodes.

OpenShift Container Platform supports the Trusted Platform Module (TPM) v2 and Tang encryption modes.

TPM v2
:   This is the preferred mode. TPM v2 stores passphrases in a secure cryptoprocessor on the server. You can use this mode to prevent decryption of the boot disk data on a cluster node if the disk is removed from the server.

Tang
:   Tang and Clevis are server and client components that enable network-bound disk encryption (NBDE). You can bind the boot disk data on your cluster nodes to one or more Tang servers. This prevents decryption of the data unless the nodes are on a secure network where the Tang servers are accessible. Clevis is an automated decryption framework used to implement decryption on the client side.

Important

The use of the Tang encryption mode to encrypt your disks is only supported for bare metal and vSphere installations on user-provisioned infrastructure.

In earlier versions of Red Hat Enterprise Linux CoreOS (RHCOS), disk encryption was configured by specifying `/etc/clevis.json` in the Ignition config. The file is not supported in clusters created with OpenShift Container Platform 4.7 or later.

When the TPM v2 or Tang encryption modes are enabled, the RHCOS boot disks are encrypted using the LUKS2 format.

Note the following points about the boot disk encryption and mirroring feature:

* Is available for installer-provisioned infrastructure, user-provisioned infrastructure, and Assisted Installer deployments
* For Assisted Installer deployments:

  + Each cluster can only have a single encryption method, Tang or TPM
  + Encryption can be enabled on some or all nodes
  + There is no Tang threshold; all servers must be valid and operational
  + Encryption applies to the installation disks only, not to the workload disks
* Is supported on Red Hat Enterprise Linux CoreOS (RHCOS) systems only
* Sets up disk encryption during the manifest installation phase, encrypting all data written to disk, from first boot forward
* Requires no user intervention for providing passphrases
* Uses AES-256-XTS encryption

#### [1.7.1. Configuring an encryption threshold](#installation-special-config-encryption-threshold_installing-customizing) Copy linkLink copied to clipboard!

In OpenShift Container Platform, you can specify a requirement for more than one Tang server. You can also configure the TPM v2 and Tang encryption modes simultaneously. Configuring both modes enables boot disk data decryption only if the TPM secure cryptoprocessor is present and the Tang servers are accessible over a secure network.

You can use the `threshold` attribute in your Butane configuration to define the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur.

The threshold is met when the stated value is reached through any combination of the declared conditions. In the case of offline provisioning, the offline server is accessed by using an included advertisement, and only uses that supplied advertisement if the number of online servers does not meet the set threshold.

**Procedure**

* Create the Butane configuration file and define a disk encryption configuration in the file. For example, the `threshold` value of `2` in the following configuration can be reached by accessing two Tang servers, where the offline server is available as a backup, or by accessing the TPM secure cryptoprocessor and one of the Tang servers.

  **Example Butane configuration for disk encryption**

  ```
  variant: openshift
  version: 4.22.0
  metadata:
    name: worker-storage
    labels:
      machineconfiguration.openshift.io/role: worker
  boot_device:
    layout: x86_64
    luks:
      tpm2: true
      tang:
        - url: http://tang1.example.com:7500
          thumbprint: jwGN5tRFK-kF6pIX89ssF3khxxX
        - url: http://tang2.example.com:7500
          thumbprint: VCJsvZFjBSIHSldw78rOrq7h2ZF
        - url: http://tang3.example.com:7500
          thumbprint: PLjNyRdGw03zlRoGjQYMahSZGu9
          advertisement: "{\"payload\": \"...\", \"protected\": \"...\", \"signature\": \"...\"}"
      threshold: 2
  openshift:
    fips: true
  ```

  where:

  `boot_device.layout`
  :   Specifies the instruction set architecture of the cluster nodes. Some examples include, `x86_64`, `aarch64`, or `ppc64le`.

  `boot_device.luks.tpm2`
  :   When `true`, specifies that you want to use a Trusted Platform Module (TPM) to encrypt the root file system.

  `boot_device.luks.tang`
  :   Specifies that you want to use the listed Tang servers.

  `boot_device.luks.tang.advertisement`
  :   Optional parameter. Specifies offline provisioning. Ignition provisions the Tang server binding rather than fetching the advertisement from the server at runtime. This lets the server be unavailable at provisioning time.

  `boot_device.luks.threshold`
  :   Specifies the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur.

      Important

      The default `threshold` value is `1`. If you include multiple encryption conditions in your configuration but do not specify a threshold, decryption can occur if any of the conditions are met.

      Note

      If you require TPM v2 *and* Tang for decryption, the value of the `threshold` attribute must equal the total number of stated Tang servers plus one. If the `threshold` value is lower, you can reach the threshold value by using a single encryption mode.

      For example, if you set `tpm2` to `true` and specify two Tang servers, a threshold of `2` can be met by accessing the two Tang servers, even if the TPM secure cryptoprocessor is not available.

### [1.8. About disk mirroring](#installation-special-config-mirrored-disk_installing-customizing) Copy linkLink copied to clipboard!

During OpenShift Container Platform installation on control plane and compute nodes, you can enable mirroring of the boot and other disks to two or more redundant storage devices. A node continues to function after storage device failure if one device remains available.

Mirroring does not support replacement of a failed disk. To restore the mirror to a pristine and non-degraded state, you must reprovision the node.

Note

For user-provisioned infrastructure deployments, mirroring is available only on RHCOS systems. Mirroring is available on `x86_64` nodes booted with BIOS or UEFI and on `ppc64le` nodes.

#### [1.8.1. Configuring disk encryption and mirroring](#installation-special-config-storage-procedure_installing-customizing) Copy linkLink copied to clipboard!

You can enable and configure encryption and mirroring before an OpenShift Container Platform installation.

**Prerequisites**

* You have downloaded the OpenShift Container Platform installation program on your installation node.
* You installed Butane on your installation node.

  Note

  Butane is a command-line utility for writing and validating machine configs with convenient, short-hand syntax. For more information, see "Creating machine configs with Butane".
* You have access to a Red Hat Enterprise Linux (RHEL) 8 machine that can be used to generate a thumbprint of the Tang exchange key.

**Procedure**

1. If you want to use TPM v2 to encrypt your cluster, check to see if TPM v2 encryption needs to be enabled in the host firmware for each node. This is required on most Dell systems. Check the manual for your specific system.
2. If you want to use Tang to encrypt your cluster, complete the following tasks:

   1. Set up a Tang server or access an existing one. See "Network-bound disk encryption" in the *Additional resources* for instructions.
   2. Install the `clevis` package on a RHEL 8 machine, if the package is not already installed:

      ```
      $ sudo yum install clevis
      ```
   3. On the RHEL 8 machine, run the following command to generate a thumbprint of the exchange key. Replace `http://tang1.example.com:7500` with the URL of your Tang server:

      ```
      $ clevis-encrypt-tang '{"url":"http://tang1.example.com:7500"}' < /dev/null > /dev/null
      ```

      In this example, `tangd.socket` is listening on port `7500` on the Tang server.

      Note

      The `clevis-encrypt-tang` command generates a thumbprint of the exchange key. No data passes to the encryption command during this step; `/dev/null` exists here as an input instead of plain text. The encrypted output is also sent to `/dev/null`, because it is not required for this procedure.

      **Example output**

      ```
      The advertisement contains the following signing keys:

      PLjNyRdGw03zlRoGjQYMahSZGu9
      ```

      `PLjNyRdGw03zlRoGjQYMahSZGu9`: The thumbprint of the exchange key.

      When the `Do you wish to trust these keys? [ynYN]` prompt displays, type `Y`.
   4. Optional: For offline Tang provisioning:

      1. Obtain the advertisement from the server using the `curl` command. Replace `http://tang2.example.com:7500` with the URL of your Tang server:

         ```
         $ curl -f http://tang2.example.com:7500/adv > adv.jws && cat adv.jws
         ```

         **Expected output**

         ```
         {"payload": "eyJrZXlzIjogW3siYWxnIjogIkV", "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI", "signature": "ADLgk7fZdE3Yt4FyYsm0pHiau7Q"}
         ```
      2. Provide the advertisement file to Clevis for encryption:

         ```
         $ clevis-encrypt-tang '{"url":"http://tang2.example.com:7500","adv":"adv.jws"}' < /dev/null > /dev/null
         ```
   5. If the nodes are configured with static IP addressing, run `coreos-installer iso customize --dest-karg-append` or use the `coreos-installer` `--append-karg` option when installing RHCOS nodes to set the IP address of the installed system. Append the `ip=` and other arguments needed for your network.

      Important

      Some methods for configuring static IPs do not affect the initramfs after the first boot and will not work with Tang encryption. These include the `coreos-installer` `--copy-network` option, the `coreos-installer iso customize` `--network-keyfile` option, and the `coreos-installer pxe customize` `--network-keyfile` option, as well as adding `ip=` arguments to the kernel command line of the live ISO or PXE image during installation. Incorrect static IP configuration causes the second boot of the node to fail.
3. On your installation node, change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   Replace `<installation_directory>` with the path to the directory that you want to store the installation files in.
4. Create a Butane config that configures disk encryption, mirroring, or both. For example, to configure storage for compute nodes, create a `$HOME/clusterconfig/worker-storage.bu` file.

   **Butane config example for a boot device**

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: worker-storage
     labels:
       machineconfiguration.openshift.io/role: worker
   boot_device:
     layout: x86_64
     luks:
       tpm2: true
       tang:
         - url: http://tang1.example.com:7500
           thumbprint: PLjNyRdGw03zlRoGjQYMahSZGu9
         - url: http://tang2.example.com:7500
           thumbprint: VCJsvZFjBSIHSldw78rOrq7h2ZF
           advertisement: "{"payload": "eyJrZXlzIjogW3siYWxnIjogIkV", "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI", "signature": "ADLgk7fZdE3Yt4FyYsm0pHiau7Q"}"
       threshold: 1
     mirror:
       devices:
         - /dev/sda
         - /dev/sdb
   openshift:
     fips: true
   ```

   where:

   `metadata.name`
   :   For control plane configurations, replace `worker` with `master` in both of these locations.

   `boot_device.layout`
   :   Specifies the instruction set architecture of the cluster nodes. Some examples include, `x86_64`, `aarch64`, or `ppc64le`.

   `boot_device.luks`
   :   Specifies encrypting the root file system. For more details, see "About disk encryption".

   `boot_device.luks.tpm2`
   :   When `true`, specifies that you want to use a Trusted Platform Module (TPM) to encrypt the root file system.

   `boot_device.luks.tang`
   :   Specifies that you want to use the listed Tang servers.

   `boot_device.luks.tang.url`
   :   Specifies the URL of a Tang server. In this example, `tangd.socket` is listening on port `7500` on the Tang server.

   `boot_device.luks.tang.thumbprint`
   :   Specifies the exchange key thumbprint, which was generated in a preceding step.

   `boot_device.luks.tang.advertisement`
   :   Optional parameter. Specifies offline provisioning. Ignition provisions the Tang server binding rather than fetching the advertisement from the server at runtime. This lets the server be unavailable at provisioning time.

   `boot_device.luks.threshold`
   :   Specifies the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur.

       The default value is `1`. For more information about this topic, see "About disk encryption".

   `boot_device.mirror`
   :   Specify the parameter if you want to mirror the boot disk. For more details, see "About disk mirroring".

   `boot_device.mirror.devices`
   :   List all disk devices that should be included in the boot disk mirror, including the disk that RHCOS will be installed onto.

   `openshift.fips`
   :   Specifies enabling FIPS mode on your cluster.

       Important

       To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see "Installing the system in FIPS mode" in the *Additional resources* section.

       If you are configuring nodes to use both disk encryption and mirroring, both features must be configured in the same Butane configuration file.

       If you are configuring disk encryption on a node with FIPS mode enabled, you must include the `fips` directive in the same Butane configuration file, even if FIPS mode is also enabled in a separate manifest.
5. Create a control plane or compute node manifest from the corresponding Butane configuration file and save it to the `<installation_directory>/openshift` directory. For example, to create a manifest for the compute nodes, run the following command:

   ```
   $ butane $HOME/clusterconfig/worker-storage.bu -o <installation_directory>/openshift/99-worker-storage.yaml
   ```

   Repeat this step for each node type that requires disk encryption or mirroring.
6. If you enable encryption, edit the manifest that was produced by the previous step and replace the cipher `aes-cbc-essiv:sha256` with `aes-xts-plain64`. The following excerpt shows a sample encryption configuration after this change:

   ```
   # ...
           luks:
   # ...
             options:
               - --cipher
               - aes-xts-plain64
   ```
7. Save the Butane configuration file in case you need to update the manifests in the future.
8. Continue with the remainder of the OpenShift Container Platform installation.

   Tip

   You can monitor the console log on the RHCOS nodes during installation for error messages relating to disk encryption or mirroring.

   Important

   If you configure additional data partitions, they will not be encrypted unless encryption is explicitly requested.

**Verification**

After installing OpenShift Container Platform, you can verify if boot disk encryption or mirroring is enabled on the cluster nodes.

1. From the installation host, access a cluster node by using a debug pod:

   1. Start a debug pod for the node, for example:

      ```
      $ oc debug node/compute-1
      ```
   2. Set `/host` as the root directory within the debug shell. The debug pod mounts the root file system of the node in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the executable paths on the node:

      ```
      # chroot /host
      ```

      Note

      OpenShift Container Platform cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes using SSH is not recommended.

      However, if the OpenShift Container Platform API is not available, or `kubelet` is not properly functioning on the target node, `oc` operations will be impacted.

      In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
2. If you configured boot disk encryption, verify if it is enabled:

   1. From the debug shell, review the status of the root mapping on the node:

      ```
      # cryptsetup status root
      ```

      **Example output**

      ```
      /dev/mapper/root is active and is in use.
        type:    LUKS2
        cipher:  aes-xts-plain64
        keysize: 512 bits
        key location: keyring
        device:  /dev/sda4
        sector size:  512
        offset:  32768 sectors
        size:    15683456 sectors
        mode:    read/write
      ```

      where:

      `type`
      :   Specifies the encryption format. When the TPM v2 or Tang encryption mode is enabled, the RHCOS boot disks are encrypted using the LUKS2 format.

      `cipher`
      :   Specifies the encryption algorithm used to encrypt the LUKS2 volume.

      `device`
      :   Specifies the device that contains the encrypted LUKS2 volume. If mirroring is enabled, the value will represent a software mirror device, for example `/dev/md126`.
   2. List the Clevis plugins that are bound to the encrypted device:

      ```
      # clevis luks list -d /dev/sda4
      ```

      Replace `/dev/sda4` with the device that is listed in the `device` field in the output of the preceding step.

      **Example output**

      ```
      1: sss '{"t":1,"pins":{"tang":[{"url":"http://tang.example.com:7500"}]}}'
      ```

      In the example output, the Tang plugin is used by the Shamir’s Secret Sharing (SSS) Clevis plugin for the `/dev/sda4` device.
3. If you configured mirroring, verify if it is enabled:

   1. From the debug shell, list the software RAID devices on the node:

      ```
      # cat /proc/mdstat
      ```

      **Example output**

      ```
      Personalities : [raid1]
      md126 : active raid1 sdb3[1] sda3[0]
      	  393152 blocks super 1.0 [2/2] [UU]

      md127 : active raid1 sda4[0] sdb4[1]
      	  51869632 blocks super 1.2 [2/2] [UU]

      unused devices: <none>
      ```

      `md126`: Specifies the `/dev/md126` software RAID mirror device that uses the `/dev/sda3` and `/dev/sdb3` disk devices on the cluster node. `md127`: Specifies the `/dev/md127` software RAID mirror device that uses the `/dev/sda4` and `/dev/sdb4` disk devices on the cluster node.
   2. Review the details of each of the software RAID devices listed in the output of the preceding command. The following example lists the details of the `/dev/md126` device:

      ```
      # mdadm --detail /dev/md126
      ```

      **Example output**

      ```
      /dev/md126:
                 Version : 1.0
           Creation Time : Wed Jul  7 11:07:36 2021
              Raid Level : raid1
              Array Size : 393152 (383.94 MiB 402.59 MB)
           Used Dev Size : 393152 (383.94 MiB 402.59 MB)
            Raid Devices : 2
           Total Devices : 2
             Persistence : Superblock is persistent

             Update Time : Wed Jul  7 11:18:24 2021
                   State : clean
          Active Devices : 2
         Working Devices : 2
          Failed Devices : 0
           Spare Devices : 0

      Consistency Policy : resync

                    Name : any:md-boot
                    UUID : ccfa3801:c520e0b5:2bee2755:69043055
                  Events : 19

          Number   Major   Minor   RaidDevice State
             0     252        3        0      active sync   /dev/sda3
             1     252       19        1      active sync   /dev/sdb3
      ```

      where:

      `Raid Level`
      :   Specifies the RAID level of the device. `raid1` indicates RAID 1 disk mirroring.

      `State`
      :   Specifies the state of the RAID device.

      `Active Devices/Working Devices`
      :   Specifies the number of underlying disk devices that are active and working.

      `Failed Devices`
      :   Specifies the number of underlying disk devices that are in a failed state.

      `Name`
      :   Specifies the name of the software RAID device.

      `/dev/sda3`
      :   Provides information about the underlying disk devices used by the software RAID device.
   3. List the file systems mounted on the software RAID devices:

      ```
      # mount | grep /dev/md
      ```

      **Example output**

      ```
      /dev/md127 on / type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /etc type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /usr type xfs (ro,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /sysroot type xfs (ro,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var/lib/containers/storage/overlay type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/1 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/2 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/3 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/4 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md127 on /var/lib/kubelet/pods/e5054ed5-f882-4d14-b599-99c050d4e0c0/volume-subpaths/etc/tuned/5 type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota)
      /dev/md126 on /boot type ext4 (rw,relatime,seclabel)
      ```

      In the example output, the `/boot` file system is mounted on the `/dev/md126` software RAID device and the root file system is mounted on `/dev/md127`.
4. Repeat the verification steps for each OpenShift Container Platform node type.

### [1.10. Configuring a RAID-enabled data volume](#installation-special-config-raid_installing-customizing) Copy linkLink copied to clipboard!

You can enable software Redundant Array of Independent Disks (RAID) partitioning to provide an external data volume.

OpenShift Container Platform supports RAID 0, RAID 1, RAID 4, RAID 5, RAID 6, and RAID 10 for data protection and fault tolerance. See "About disk mirroring" for more details.

Note

OpenShift Container Platform 4.22 supports manually configuring a hybrid RAID on an installation drive. For a manually configured example, see "Configuring an Intel® Virtual RAID on CPU (VROC) data volume".

**Prerequisites**

* You have downloaded the OpenShift Container Platform installation program on your installation node.
* You have installed Butane on your installation node.

  Note

  Butane is a command-line utility that OpenShift Container Platform uses to write machine configs. The utility provides convenient, short-hand syntax for writing machine configs and for performing additional validation of machine configs. For more information, see the *Creating machine configs with Butane* section.

**Procedure**

1. Create a Butane config that configures a data volume by using software RAID.

   * To configure a data volume with RAID 1 on the same disks that are used for a mirrored boot disk, create a `$HOME/clusterconfig/raid1-storage.bu` file:

     **Example configuration for RAID 1 on a mirrored boot disk**

     ```
     variant: openshift
     version: 4.22.0
     metadata:
       name: raid1-storage
       labels:
         machineconfiguration.openshift.io/role: worker
     boot_device:
       mirror:
         devices:
           - /dev/disk/by-id/scsi-3600508b400105e210000900000490000
           - /dev/disk/by-id/scsi-SSEAGATE_ST373453LW_3HW1RHM6
     storage:
       disks:
         - device: /dev/disk/by-id/scsi-3600508b400105e210000900000490000
           partitions:
             - label: root-1
               size_mib: 25000
             - label: var-1
         - device: /dev/disk/by-id/scsi-SSEAGATE_ST373453LW_3HW1RHM6
           partitions:
             - label: root-2
               size_mib: 25000
             - label: var-2
       raid:
         - name: md-var
           level: raid1
           devices:
             - /dev/disk/by-partlabel/var-1
             - /dev/disk/by-partlabel/var-2
       filesystems:
         - device: /dev/md/md-var
           path: /var
           format: xfs
           wipe_filesystem: true
           with_mount_unit: true
     # ...
     ```

     The `size_mib` field adds a data partition to the boot disk. A minimum value of 25000 mebibytes is recommended. If no value is specified or the specified value is smaller than the recommended minimum, the resulting root file system will be too small. Future reinstalls of RHCOS might overwrite the beginning of the data partition.
   * To configure a data volume with RAID 1 on secondary disks, create a `$HOME/clusterconfig/raid1-alt-storage.bu` file:

     **Example configuration for RAID 1 on secondary disks**

     ```
     variant: openshift
     version: 4.22.0
     metadata:
       name: raid1-alt-storage
       labels:
         machineconfiguration.openshift.io/role: worker
     storage:
       disks:
         - device: /dev/sdc
           wipe_table: true
           partitions:
             - label: data-1
         - device: /dev/sdd
           wipe_table: true
           partitions:
             - label: data-2
       raid:
         - name: md-var-lib-containers
           level: raid1
           devices:
             - /dev/disk/by-partlabel/data-1
             - /dev/disk/by-partlabel/data-2
       filesystems:
         - device: /dev/md/md-var-lib-containers
           path: /var/lib/containers
           format: xfs
           wipe_filesystem: true
           with_mount_unit: true
     # ...
     ```
2. Create a RAID manifest from the Butane config. Save the config to the `<installation_directory>/openshift` directory. For example, to create a manifest for the compute nodes, run the following command:

   ```
   $ butane $HOME/clusterconfig/<butane_config>.bu -o <installation_directory>/openshift/<manifest_name>.yaml
   ```

   Replace the `<manifest_name>` and `<butane_config>` values with the file names from a previous step. For example, `raid1-alt-storage.bu` and `raid1-alt-storage.yaml` for secondary disks.
3. Save the Butane config in case you need to update the manifest in the future.
4. Continue with the remainder of the OpenShift Container Platform installation.

### [1.11. Configuring an Intel® Virtual RAID on CPU (VROC) data volume](#installation-special-config-raid-intel-vroc_installing-customizing) Copy linkLink copied to clipboard!

Intel® VROC is a type of hybrid RAID, where some of the maintenance is offloaded to the hardware, but shows as software RAID to the operating system. You can configure an Intel® Virtual RAID on CPU (VROC) data volume to deliver direct-to-CPU NVMe throughput for data-intensive workloads.

The following procedure configures an Intel® VROC-enabled RAID1.

**Prerequisites**

* You have a system with Intel® Volume Management Device (VMD) enabled.

**Procedure**

1. Create the Intel® Matrix Storage Manager (IMSM) RAID container by running the following command:

   ```
   $ mdadm -CR /dev/md/imsm0 -e \
     imsm -n2 /dev/nvme0n1 /dev/nvme1n1
   ```

   The RAID device names. In this example, there are two devices listed. If you provide more than two device names, you must adjust the `-n` flag. For example, listing three devices would use the flag `-n3`.
2. Create the RAID1 storage inside the container:

   1. Create a dummy RAID0 volume in front of the real RAID1 volume by running the following command:

      ```
      $ mdadm -CR /dev/md/dummy -l0 -n2 /dev/md/imsm0 -z10M --assume-clean
      ```
   2. Create the real RAID1 array by running the following command:

      ```
      $ mdadm -CR /dev/md/coreos -l1 -n2 /dev/md/imsm0
      ```
   3. Stop both RAID0 and RAID1 member arrays and delete the dummy RAID0 array with the following commands:

      ```
      $ mdadm -S /dev/md/dummy \
        mdadm -S /dev/md/coreos \
        mdadm --kill-subarray=0 /dev/md/imsm0
      ```
   4. Restart the RAID1 arrays by running the following command:

      ```
      $ mdadm -A /dev/md/coreos /dev/md/imsm0
      ```
3. Install RHCOS on the RAID1 device:

   1. Get the UUID of the IMSM container by running the following command:

      ```
      $ mdadm --detail --export /dev/md/imsm0
      ```
   2. Install RHCOS and include the `rd.md.uuid` kernel argument by running the following command:

      ```
      $ coreos-installer install /dev/md/coreos \
        --append-karg rd.md.uuid=<md_UUID>
        ...
      ```

      Replace `<md_UUID>` with the UUID of the IMSM container.

      Include any additional `coreos-installer` arguments you need to install RHCOS.

### [1.12. Configuring chrony time service](#installation-special-config-chrony_installing-customizing) Copy linkLink copied to clipboard!

You can set the time server and related settings used by the chrony time service (`chronyd`) by modifying the contents of the `chrony.conf` file and passing those contents to your nodes as a machine config.

For more information on chrony best practices, see the following resources:

* [Configuring chrony (Red Hat Knowledgebase article)](https://access.redhat.com/solutions/3073261)
* [Best practices for NTP (Red Hat Knowledgebase article)](https://access.redhat.com/solutions/778603)
* [Basic chrony NTP troubleshooting (Red Hat Ceph Storage documentation)](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/troubleshooting_guide/basic-chrony-NTP-troubleshooting_diag#basic-chrony-NTP-troubleshooting_diag)

**Procedure**

1. Create a Butane config including the contents of the `chrony.conf` file. For example, to configure chrony on worker nodes, create a `99-worker-chrony.bu` file.

   Note

   The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane.

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 99-worker-chrony
     labels:
       machineconfiguration.openshift.io/role: worker
   storage:
     files:
     - path: /etc/chrony.conf
       mode: 0644
       overwrite: true
       contents:
         inline: |
           pool 0.rhel.pool.ntp.org iburst
           driftfile /var/lib/chrony/drift
           makestep 1.0 3
           rtcsync
           logdir /var/log/chrony
   ```

   * `name: 99-worker-chrony` - Specify a name for the machine config file. On control plane nodes, substitute `master` for `worker`.
   * `machineconfiguration.openshift.io/role: worker` - On control plane nodes, substitute `master` for `worker`.
   * `mode: 0644` - Specify an octal value mode for the `mode` field in the machine config file. After creating the file and applying the changes, the `mode` is converted to a decimal value. You can check the YAML file with the command `oc get mc <mc-name> -o yaml`.
   * `pool 0.rhel.pool.ntp.org iburst` - Specify any valid, reachable time source, such as the one provided by your DHCP server.

   Note

   For all-machine to all-machine communication, the Network Time Protocol (NTP) on UDP is port `123`. If an external NTP time server is configured, you must open UDP port `123`.

   Alternatively, you can specify any of the following NTP servers: `1.rhel.pool.ntp.org`, `2.rhel.pool.ntp.org`, or `3.rhel.pool.ntp.org`. When you use NTP with your DHCP server, you must set the `sourcedir /run/chrony-dhcp` parameter in the `chrony.conf` file.
2. Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, containing the configuration to be delivered to the nodes:

   ```
   $ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
   ```
3. Apply the configurations in one of two ways:

   * If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
   * If the cluster is already running, apply the file:

     ```
     $ oc apply -f ./99-worker-chrony.yaml
     ```

## [Chapter 2. Configuring your firewall](#configuring-firewall) Copy linkLink copied to clipboard!

If you use a firewall, you must configure your allowlist for the firewall to ensure OpenShift Container Platform has access to the URLs it requires to pull container images and access Red Hat services. Additional URLs are required for features such as Telemetry, Red Hat Lightspeed, cloud provider integrations, or certain build strategies.

### [2.1. Configuring your firewall for OpenShift Container Platform](#configuring-firewall-module_configuring-firewall) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires.

There are no special configuration considerations for services running on only controller nodes compared to compute nodes.

Note

If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster.

**Procedure**

1. Allowlist the following container registry URLs for cluster installation and upgrades:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `registry.redhat.io` | 443 | Provides core container images |
   | `access.redhat.com` | 443 | Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist. |
   | `registry.access.redhat.com` | 443 | Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images. |
   | `quay.io` | 443 | Provides core container images |
   | `cdn.quay.io` | 443 | Provides core container images |
   | `cdn01.quay.io` | 443 | Provides core container images |
   | `cdn02.quay.io` | 443 | Provides core container images |
   | `cdn03.quay.io` | 443 | Provides core container images |
   | `cdn04.quay.io` | 443 | Provides core container images |
   | `cdn05.quay.io` | 443 | Provides core container images |
   | `cdn06.quay.io` | 443 | Provides core container images |
   | `icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |
   | `cp.icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |

   Show more

   * You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist.
   * You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed.
   * When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`.
2. Allowlist the following URLs to enable cluster access, authentication, and updates:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `*.apps.<cluster_name>.<base_domain>` | 443 | Allowlist these URLs to enable cluster access, authentication, and updates. |
   | `api.openshift.com` | 443 | API endpoint for cluster tokens and update checks. |
   | `console.redhat.com` | 443 | Authentication service for cluster tokens. |
   | `sso.redhat.com` | 443 | The `https://console.redhat.com` site uses authentication from `sso.redhat.com` |

   Show more

   For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes:

   * `oauth-openshift.apps.<cluster_name>.<base_domain>`
   * `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`
   * `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname that is specified in the `spec.route.hostname` field of the `consoles.operator/cluster` object if the field is not empty.
3. Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `mirror.openshift.com` | 443 | Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |
   | `quayio-production-s3.s3.amazonaws.com` | 443 | Required to access Quay image content in AWS. |
   | `rhcos.mirror.openshift.com` | 443 | Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images. |
   | `storage.googleapis.com/openshift-release` | 443 | A source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |

   Show more
4. Set your firewall’s allowlist to include any site that provides resources for a language or framework that your builds require.
5. If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and Red Hat Lightspeed:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `cert-api.access.redhat.com` | 443 | Required for Telemetry |
   | `api.access.redhat.com` | 443 | Required for Telemetry |
   | `infogw.api.openshift.com` | 443 | Required for Telemetry |
   | `console.redhat.com` | 443 | Required for Telemetry and for `insights-operator` |

   Show more
6. If you use Alibaba Cloud, Amazon Web Services (AWS), Microsoft Azure, or Google Cloud to host your cluster, you must grant access to the URLs that offer the cloud provider API and DNS for that cloud:

   Expand

   | Cloud | URL | Port | Function |
   | --- | --- | --- | --- |
   | Alibaba | `*.aliyuncs.com` | 443 | Required to access Alibaba Cloud services and resources. Review the [Alibaba endpoints\_config.go file](https://github.com/aliyun/alibaba-cloud-sdk-go/blob/master/sdk/endpoints/endpoints_config.go?spm=a2c4g.11186623.0.0.47875873ciGnC8&file=endpoints_config.go) to find the exact endpoints to allow for the regions that you use. |
   | AWS | `aws.amazon.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `*.amazonaws.com`  Alternatively, if you choose to not use a wildcard for AWS APIs, you must include the following URLs in your allowlist: | 443 | Required to access AWS services and resources. Review the [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the AWS documentation to find the exact endpoints to allow for the regions that you use. |
   | `ec2.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `ec2.us-east-1.amazonaws.com` | 443 | Used to get the list of available regions when interactively generating the `install-config.yaml` file. |
   | `events.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `iam.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `route53.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `*.s3.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `*.s3.<aws_region>.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `*.s3.dualstack.<aws_region>.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `sts.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `sts.<aws_region>.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `tagging.us-east-1.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. This endpoint is always `us-east-1`, regardless of the region the cluster is deployed in. |
   | `ec2.<aws_region>.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `elasticloadbalancing.<aws_region>.amazonaws.com` | 443 | Used to install and manage clusters in an AWS environment. |
   | `servicequotas.<aws_region>.amazonaws.com` | 443 | Required. Used to confirm quotas for deploying the service. |
   | `tagging.<aws_region>.amazonaws.com` | 443 | Allows the assignment of metadata about AWS resources in the form of tags. |
   | `*.cloudfront.net` | 443 | Used to provide access to CloudFront. If you use the AWS Security Token Service (STS) and the private S3 bucket, you must provide access to CloudFront. | GCP |
   | `*.googleapis.com` | 443 | Required to access Google Cloud services and resources. Review [Cloud Endpoints](https://cloud.google.com/endpoints/) in the Google Cloud documentation to find the endpoints to allow for your APIs. |
   | `accounts.google.com` | 443 | Required to access your Google Cloud account. | Microsoft Azure |
   | `management.azure.com` | 443 | Required to access Microsoft Azure services and resources. Review the [Microsoft Azure REST API reference](https://docs.microsoft.com/en-us/rest/api/azure/) in the Microsoft Azure documentation to find the endpoints to allow for your APIs. |
   | `*.blob.core.windows.net` | 443 | Required to download Ignition files. |

   Show more
7. Allowlist the following URL for optional third-party content:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `registry.connect.redhat.com` | 443 | Required for all third-party images and certified operators. |

   Show more
8. If you use a default Red Hat Network Time Protocol (NTP) server, allow the following URLs. NTP operates on User Datagram Protocol (UDP) port 123, so this port must be opened on the firewall.

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `1.rhel.pool.ntp.org` | 123 | Provides NTP services for time synchronization. |
   | `2.rhel.pool.ntp.org` | 123 | Provides NTP services for time synchronization. |
   | `3.rhel.pool.ntp.org` | 123 | Provides NTP services for time synchronization. |

   Show more

   Note

   If you do not use a default Red Hat NTP server, verify the NTP server for your platform and allow it in your firewall.

### [2.2. OpenShift Container Platform network flow matrix](#network-flow-matrix_configuring-firewall) Copy linkLink copied to clipboard!

You can use the information in the appropriate network flow matrix to manage ingress traffic for your specific environment. You can restrict ingress traffic to essential flows to improve network security.

The following network flow matrixes describe the ingress flows to OpenShift Container Platform services for the following environments:

* OpenShift Container Platform on bare metal
* Single-node OpenShift with other platforms
* OpenShift Container Platform on Amazon Web Services (AWS)
* Single-node OpenShift on AWS

Note

You can use the `commatrix` plugin for the `oc` command to generate local network flow data for your cluster. For more information see "Generating ingress network flow data using the `commatrix` plugin".

Additionally, consider the following dynamic port ranges when managing ingress traffic for both bare metal and cloud environments:

* `9000-9999`: Reserved for internal OpenShift Container Platform components. Do not assign user workloads or services to ports in this range.
* `30000-32767`: Kubernetes `NodePort` service ports. These ports are required only if you expose services by using the `NodePort` service type. If `NodePort` services are not used, you can block this port range.

To view or download the complete raw CSV content for an environment, see the following resources:

* [OpenShift Container Platform on bare metal](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/bm.csv)
* [Single-node OpenShift with other platforms](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/none-sno.csv)
* [OpenShift Container Platform on AWS](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/aws.csv)
* [Single-node OpenShift on AWS](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.22/docs/stable/raw/aws-sno.csv)

Note

The network flow matrixes describe ingress traffic flows for a base OpenShift Container Platform or single-node OpenShift installation. The matrixes do not apply for hosted control planes, Red Hat build of MicroShift, or standalone clusters.

#### [2.2.1. Base network flows](#network-flow-matrix-common_configuring-firewall) Copy linkLink copied to clipboard!

The following matrixes describe the base ingress flows to OpenShift Container Platform services.

Note

For base ingress flows to single-node OpenShift clusters, see the *Control plane node base flows* matrix only.

Expand

Table 2.1. Control plane node base flows

| Direction | Protocol | Port | Namespace | Service | Pod | Container | Node Role | Optional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingress | TCP | 22 | Host system service | sshd |  |  | master | TRUE |
| Ingress | TCP | 111 | Host system service | rpcbind |  |  | master | TRUE |
| Ingress | TCP | 2379 | openshift-etcd | etcd | etcd | etcdctl | master | FALSE |
| Ingress | TCP | 2380 | openshift-etcd | healthz | etcd | etcd | master | FALSE |
| Ingress | TCP | 6080 | openshift-kube-apiserver |  | kube-apiserver | kube-apiserver-insecure-readyz | master | FALSE |
| Ingress | TCP | 6443 | openshift-kube-apiserver | apiserver | kube-apiserver | kube-apiserver | master | FALSE |
| Ingress | TCP | 8798 | openshift-machine-config-operator | machine-config-daemon | machine-config-daemon | machine-config-daemon | master | FALSE |
| Ingress | TCP | 9001 | openshift-machine-config-operator | machine-config-daemon | machine-config-daemon | kube-rbac-proxy | master | FALSE |
| Ingress | TCP | 9099 | openshift-cluster-version | cluster-version-operator | cluster-version-operator | cluster-version-operator | master | FALSE |
| Ingress | TCP | 9100 | openshift-monitoring | node-exporter | node-exporter | kube-rbac-proxy | master | FALSE |
| Ingress | TCP | 9103 | openshift-ovn-kubernetes | ovn-kubernetes-node | ovnkube-node | kube-rbac-proxy-node | master | FALSE |
| Ingress | TCP | 9104 | openshift-network-operator | metrics | network-operator | network-operator | master | FALSE |
| Ingress | TCP | 9105 | openshift-ovn-kubernetes | ovn-kubernetes-node | ovnkube-node | kube-rbac-proxy-ovn-metrics | master | FALSE |
| Ingress | TCP | 9107 | openshift-ovn-kubernetes | egressip-node-healthcheck | ovnkube-node | ovnkube-controller | master | FALSE |
| Ingress | TCP | 9108 | openshift-ovn-kubernetes | ovn-kubernetes-control-plane | ovnkube-control-plane | kube-rbac-proxy | master | FALSE |
| Ingress | TCP | 9192 | openshift-cluster-machine-approver | machine-approver | machine-approver | kube-rbac-proxy | master | FALSE |
| Ingress | TCP | 9258 | openshift-cloud-controller-manager-operator | machine-approver | cluster-cloud-controller-manager | cluster-cloud-controller-manager | master | FALSE |
| Ingress | TCP | 9443 | openshift-cloud-controller-manager-operator | cloud-controller-manager-operator | cluster-cloud-controller-manager-operator | cluster-cloud-controller-manager | master | FALSE |
| Ingress | TCP | 9637 | openshift-machine-config-operator | kube-rbac-proxy-crio | kube-rbac-proxy-crio | kube-rbac-proxy-crio | master | FALSE |
| Ingress | TCP | 9978 | openshift-etcd | etcd | etcd | etcd-metrics | master | FALSE |
| Ingress | TCP | 9979 | openshift-etcd | etcd | etcd | etcd-metrics | master | FALSE |
| Ingress | TCP | 9980 | openshift-etcd | etcd | etcd | etcd | master | FALSE |
| Ingress | TCP | 10250 | Host system service | kubelet |  |  | master | FALSE |
| Ingress | TCP | 10256 | openshift-ovn-kubernetes | ovnkube | ovnkube | ovnkube-controller | master | FALSE |
| Ingress | TCP | 10257 | openshift-kube-controller-manager | kube-controller-manager | kube-controller-manager | kube-controller-manager | master | FALSE |
| Ingress | TCP | 10259 | openshift-kube-scheduler | scheduler | openshift-kube-scheduler | kube-scheduler | master | FALSE |
| Ingress | TCP | 17697 | openshift-kube-apiserver | openshift-kube-apiserver-healthz | kube-apiserver | kube-apiserver-check-endpoints | master | FALSE |
| Ingress | TCP | 22623 | openshift-machine-config-operator | machine-config-server | machine-config-server | machine-config-server | master | FALSE |
| Ingress | TCP | 22624 | openshift-machine-config-operator | machine-config-server | machine-config-server | machine-config-server | master | FALSE |
| Ingress | UDP | 111 | Host system service | rpcbind |  |  | master | TRUE |

Show more

Expand

Table 2.2. Worker node base flows

| Direction | Protocol | Port | Namespace | Service | Pod | Container | Node Role | Optional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingress | TCP | 22 | Host system service | sshd |  |  | worker | TRUE |
| Ingress | TCP | 111 | Host system service | rpcbind |  |  | worker | TRUE |
| Ingress | TCP | 8798 | openshift-machine-config-operator | machine-config-daemon | machine-config-daemon | machine-config-daemon | worker | FALSE |
| Ingress | TCP | 9001 | openshift-machine-config-operator | machine-config-daemon | machine-config-daemon | kube-rbac-proxy | worker | FALSE |
| Ingress | TCP | 9100 | openshift-monitoring | node-exporter | node-exporter | kube-rbac-proxy | worker | FALSE |
| Ingress | TCP | 9103 | openshift-ovn-kubernetes | ovn-kubernetes-node | ovnkube-node | kube-rbac-proxy-node | worker | FALSE |
| Ingress | TCP | 9105 | openshift-ovn-kubernetes | ovn-kubernetes-node | ovnkube-node | kube-rbac-proxy-ovn-metrics | worker | FALSE |
| Ingress | TCP | 9107 | openshift-ovn-kubernetes | egressip-node-healthcheck | ovnkube-node | ovnkube-controller | worker | FALSE |
| Ingress | TCP | 9637 | openshift-machine-config-operator | kube-rbac-proxy-crio | kube-rbac-proxy-crio | kube-rbac-proxy-crio | worker | FALSE |
| Ingress | TCP | 10250 | Host system service | kubelet |  |  | worker | FALSE |
| Ingress | TCP | 10256 | openshift-ovn-kubernetes | ovnkube | ovnkube | ovnkube-controller | worker | FALSE |
| Ingress | UDP | 111 | Host system service | rpcbind |  |  | worker | TRUE |

Show more

#### [2.2.2. Additional network flows for OpenShift Container Platform on bare metal](#network-flow-matrix-bm_configuring-firewall) Copy linkLink copied to clipboard!

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on bare metal.

Expand

Table 2.3. OpenShift Container Platform on bare metal

| Direction | Protocol | Port | Namespace | Service | Pod | Container | Node Role | Optional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingress | TCP | 53 | openshift-dns | dns-default | dns-default | dns | master | FALSE |
| Ingress | TCP | 6180 | openshift-machine-api | metal3-state | metal3 | metal3-httpd | master | FALSE |
| Ingress | TCP | 6183 | openshift-machine-api | metal3-state | metal3 | metal3-httpd | master | FALSE |
| Ingress | TCP | 6385 | openshift-machine-api | metal3-state | metal3 | metal3-httpd | master | FALSE |
| Ingress | TCP | 6388 | openshift-machine-api | metal3-state | metal3 | metal3-httpd | master | FALSE |
| Ingress | TCP | 9444 | openshift-kni-infra |  | haproxy | haproxy | master | FALSE |
| Ingress | TCP | 9445 | openshift-kni-infra |  | haproxy | haproxy | master | FALSE |
| Ingress | TCP | 9454 | openshift-kni-infra |  | haproxy | haproxy | master | FALSE |
| Ingress | TCP | 18080 | openshift-kni-infra |  | coredns | coredns | master | FALSE |
| Ingress | UDP | 53 | openshift-dns | dns-default | dns-default | dns | master | FALSE |
| Ingress | UDP | 6081 | openshift-ovn-kubernetes | ovn-kubernetes geneve |  |  | master | FALSE |
| Ingress | TCP | 53 | openshift-dns | dns-default | dns-default | dns | worker | FALSE |
| Ingress | TCP | 80 | openshift-ingress | router-internal-default | router-default | router | worker | FALSE |
| Ingress | TCP | 443 | openshift-ingress | router-internal-default | router-default | router | worker | FALSE |
| Ingress | TCP | 1936 | openshift-ingress | router-internal-default | router-default | router | worker | FALSE |
| Ingress | TCP | 18080 | openshift-kni-infra |  | coredns | coredns | worker | FALSE |
| Ingress | UDP | 53 | openshift-dns | dns-default | dns-default | dns | worker | FALSE |
| Ingress | UDP | 6081 | openshift-ovn-kubernetes | ovn-kubernetes geneve |  |  | worker | FALSE |

Show more

#### [2.2.3. Additional network flows for single-node OpenShift with other platforms](#network-flow-matrix-sno_configuring-firewall) Copy linkLink copied to clipboard!

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to single-node OpenShift configured with `platform: none` in the installation manifest.

Expand

Table 2.4. Single-node OpenShift with other platforms

| Direction | Protocol | Port | Namespace | Service | Pod | Container | Node Role | Optional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingress | TCP | 80 | openshift-ingress | router-internal-default | router-default | router | master | FALSE |
| Ingress | TCP | 443 | openshift-ingress | router-internal-default | router-default | router | master | FALSE |
| Ingress | TCP | 1936 | openshift-ingress | router-internal-default | router-default | router | master | FALSE |

Show more

#### [2.2.4. Additional network flows for OpenShift Container Platform on AWS](#network-flow-matrix-aws_configuring-firewall) Copy linkLink copied to clipboard!

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on AWS.

Expand

Table 2.5. OpenShift Container Platform on AWS

| Direction | Protocol | Port | Namespace | Service | Pod | Container | Node Role | Optional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingress | TCP | 10258 | openshift-cloud-controller-manager-operator | cloud-controller | cloud-controller-manager | cloud-controller-manager | master | FALSE |
| Ingress | TCP | 80 | openshift-ingress | router-default | router-default | router | worker | FALSE |
| Ingress | TCP | 443 | openshift-ingress | router-default | router-default | router | worker | FALSE |
| Ingress | UDP | 6081 | openshift-ovn-kubernetes | ovn-kubernetes geneve |  |  | worker | FALSE |

Show more

#### [2.2.5. Additional network flows for single-node OpenShift on AWS](#network-flow-matrix-aws-sno_configuring-firewall) Copy linkLink copied to clipboard!

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to single-node OpenShift on AWS.

Expand

Table 2.6. Single-node OpenShift on AWS

| Direction | Protocol | Port | Namespace | Service | Pod | Container | Node Role | Optional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ingress | TCP | 80 | openshift-ingress | router-default | router-default | router | master | FALSE |
| Ingress | TCP | 443 | openshift-ingress | router-default | router-default | router | master | FALSE |
| Ingress | TCP | 10258 | openshift-cloud-controller-manager-operator | cloud-controller | cloud-controller-manager | cloud-controller-manager | master | FALSE |

Show more

### [2.3. Ingress network flow management with the commatrix plugin](#network-commatrix-plugin-intro_configuring-firewall) Copy linkLink copied to clipboard!

Use the `commatrix` plugin for the `oc` command to analyze ingress network traffic and generate firewall rules for live clusters.

For ingress network analysis, the plugin reads the services deployed in a target cluster and generates a communication matrix of expected ingress flows. You can export the data in formats such as CSV, JSON, or YAML for audits, documentation, or configuring external firewalls.

For firewall configuration, the plugin generates `nftables` rules in Butane format that restrict ingress traffic to only the flows required by your cluster. The plugin also generates a `NodeDisruptionPolicy` patch to apply updates without triggering node reboots.

The communication matrix uses `EndpointSlice` objects to discover exposed ports. Kubernetes automatically creates `EndpointSlice` objects for each `Service` object. Starting with OpenShift Container Platform 4.22, the matrix fully covers all core OpenShift Container Platform ports. However, non-core Operators or other software that expose ports without a corresponding `Service` object do not appear in the matrix, such as host-level services, monitoring agents, or third-party software.

To discover all listening ports on cluster nodes, use the `--host-open-ports` flag. This flag captures ports that are open on the hosts but are not defined through `Service` or `EndpointSlice` objects. You can compare this output with the declared ports by using the diff file generated by the plugin, which shows the differences between the intended and actual state.

### [2.4. Installing the commatrix plugin](#network-commatrix-plugin-install_configuring-firewall) Copy linkLink copied to clipboard!

You can install the `commatrix` plugin from the Red Hat Ecosystem Catalog.

Note

* You can also install the `commatrix` plugin by using Krew. For more information, see "CLI Manager Operator overview".
* The communication matrix does not include ports from non-core Operators or other software that do not expose a `Service` object. For a complete view of listening ports, run the `generate` command with the `--host-open-ports` flag.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You installed Podman.

**Procedure**

1. Log in to the Red Hat Ecosystem Catalog registry by running the following command and entering your credentials:

   ```
   $ podman login registry.redhat.io
   ```
2. Extract the `commatrix` binary from the plugin image by running the following commands:

   ```
   $ podman create --name oc-commatrix registry.redhat.io/openshift-kni/commatrix:v4.22
   $ podman cp oc-commatrix:/oc-commatrix .
   $ podman rm oc-commatrix
   ```
3. Move the extracted binary to a directory in your system `PATH`, such as `/usr/local/bin/`, by running the following command:

   ```
   sudo mv oc-commatrix /usr/local/bin/
   ```

**Verification**

* Run the following command to verify that the plugin is available locally:

  ```
  $ oc commatrix
  ```

  ```
  Generate an up-to-date communication flows matrix for all ingress flows of openshift (multi-node and single-node in OpenShift) and Operators.

   Optionally, generate a host open ports matrix and the difference with the communication matrix.

   For additional details, please refer to the communication matrix documentation(https://github.com/openshift-kni/commatrix/blob/main/README.md).

  Usage:
    commatrix [command]

  Available Commands:
    completion  Generate the autocompletion script for the specified shell
    generate    Generate an up-to-date communication flows matrix for all ingress flows.
    help        Help about any command

  Flags:
    -h, --help   help for commatrix

  Use "commatrix [command] --help" for more information about a command.
  ```

### [2.5. Generate ingress network flow data using the commatrix plugin](#network-commatrix-plugin-generate_configuring-firewall) Copy linkLink copied to clipboard!

Use the `commatrix` plugin for the `oc` command to generate ingress network flow data from your cluster and identify any differences between open ports on the host and expected ingress flows for your environment.

The plugin generates ingress flows to OpenShift Container Platform services for the following environments:

* OpenShift Container Platform on bare metal
* Single-node OpenShift with other platforms
* OpenShift Container Platform on Amazon Web Services (AWS)
* Single-node OpenShift on AWS

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You installed Podman.
* You installed the `commatrix` plugin.

**Procedure**

1. Generate network flow data by running the following command:

   ```
   $ oc commatrix generate
   ```

   Note

   By default, the plugin generates the network flow data in CSV format in a `communication-matrix` directory in your current working directory.

**Verification**

* View the generated network flow data in the `communication-matrix` directory by running the following command:

  ```
  $ cat communication-matrix/communication-matrix.csv
  ```

  ```
  Direction,Protocol,Port,Namespace,Service,Pod,Container,Node Role,Optional
  Ingress,TCP,4194,kube-system,kubelet,konnectivity-agent,,,false
  Ingress,TCP,9100,openshift-monitoring,node-exporter,node-exporter,kube-rbac-proxy,,false
  Ingress,TCP,9103,openshift-ovn-kubernetes,ovn-kubernetes-node,ovnkube-node,kube-rbac-proxy-node,,false

  ...
  ```

### [2.6. Ingress traffic configuration with the commatrix plugin](#commatrix-restricting-ingress-traffic_configuring-firewall) Copy linkLink copied to clipboard!

You can use the `commatrix` plugin to generate `nftables` rules that configure the firewall on cluster nodes to permit only the ingress traffic defined in the communication matrix.

`nftables` is the packet filtering framework in the Linux kernel that replaces `iptables`. OpenShift Container Platform cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) use `nftables` for packet filtering. The `commatrix` plugin generates `nftables` rules and packages them as `MachineConfig` resources that the Machine Config Operator applies to your nodes.

When you generate firewall rules with the `commatrix` plugin in Butane format, the plugin also generates a `NodeDisruptionPolicy` patch. This patch enables the Machine Config Operator to apply `nftables` rule updates without triggering a full node reboot, minimizing disruption to running workloads.

Important

When operators or components are installed, enabled, uninstalled, or disabled, you must regenerate the firewall rules to reflect the new configuration. Failure to regenerate and apply firewall rules in this scenario might have the following consequences:

* Unnecessary ports might remain open, which increases the attack surface of your cluster.
* Services might fail to function correctly if required ports remain blocked by outdated firewall rules.

### [2.7. Generate nftables firewall rules in Butane format](#commatrix-generate-butane_configuring-firewall) Copy linkLink copied to clipboard!

You can generate `nftables` firewall rules in Butane format by using the `commatrix` plugin. The generated Butane configs contain `nftables` rules that allow the ingress flows defined in the communication matrix and block all other ingress flows.

Warning

Errors in `nftables` rules can block legitimate traffic and isolate nodes from the cluster. Review all generated rules before applying them.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You installed Podman.
* You installed the `commatrix` plugin.
* You installed the `butane` CLI.
* For custom node groups, you need an existing machine config pool that you can target using node label selectors.

**Procedure**

1. Generate firewall rules in Butane format by running the following command:

   ```
   $ oc commatrix generate --format butane
   ```

   By default, the plugin writes the output files to the `communication-matrix` directory in your current working directory.

   The plugin generates one Butane config file per node pool, named `butane-<pool_name>.yaml`, and a `node-disruption-policy.yaml` patch file, for example:

   ```
   communication-matrix/
   ├── butane-master.yaml
   ├── butane-worker.yaml
   └── node-disruption-policy.yaml
   ```
2. Review the generated Butane config files by running the following command:

   ```
   $ cat communication-matrix/butane-<pool_name>.yaml
   ```

   See the following example of the `butane-master.yaml` file.

   Note

   You can adjust the generated firewall rules in your YAML file to suit your network environment.

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 98-nftables-commatrix-master
     labels:
       machineconfiguration.openshift.io/role: master
   systemd:
     units:
       - name: "nftables.service"
         enabled: true
         contents: |
           # ... systemd unit configuration ...
   storage:
     files:
       - path: /etc/sysconfig/nftables.conf
         mode: 0600
         overwrite: true
         contents:
           inline: |
             table inet openshift_filter {
                 chain OPENSHIFT {
                     type filter hook input priority 1; policy accept;

                     # Allow loopback traffic
                     iif lo accept

                     # Allow established and related traffic
                     ct state established,related accept

                     # Allow ICMP on ipv4
                     ip protocol icmp accept
                     ip6 nexthdr ipv6-icmp accept

                     # Allow specific TCP and UDP ports
                     tcp dport { 22, 6443, 9100, 10250, 30000-60999 } accept
                     udp dport { 6081, 30000-60999 } accept

                     # Drop broadcast traffic with rate-limited logging
                     ip daddr 255.255.255.255 jump { limit rate 1/minute log prefix "firewall "; drop; }

                     # Rate-limited logging and default drop
                     jump { limit rate 1/minute log prefix "firewall "; drop; }
                 }
             }
   ```
3. Review the generated `NodeDisruptionPolicy` patch by running the following command:

   ```
   $ cat communication-matrix/node-disruption-policy.yaml
   ```
4. Check whether your cluster already defines `NodeDisruptionPolicy` entries by running the following command:

   ```
   $ oc get -o yaml machineconfiguration cluster
   ```
5. Apply the `NodeDisruptionPolicy` patch:

   1. If the `MachineConfiguration` resource does not define any `nodeDisruptionPolicy` entries, run the following command:

      ```
      $ oc patch machineconfiguration cluster --type=merge --patch-file=communication-matrix/node-disruption-policy.yaml
      ```
   2. If the `MachineConfiguration` resource already contains `nodeDisruptionPolicy` entries, manually add the entries from `node-disruption-policy.yaml` to the existing `.spec.nodeDisruptionPolicy.units` and `.spec.nodeDisruptionPolicy.files` lists by running the following command:

      ```
      $ oc edit machineconfiguration cluster
      ```
6. Convert each Butane config to a `MachineConfig` resource by running the following command:

   ```
   $ butane --strict -o mc-<pool_name>.yaml communication-matrix/butane-<pool_name>.yaml
   ```

   * `<pool_name>` is the name of the target node pool.
7. Apply the `MachineConfig` resources by running the following command for each node pool:

   Important

   You must apply the `NodeDisruptionPolicy` patch before applying `MachineConfig` resources. If you apply `MachineConfig` resources without the `NodeDisruptionPolicy` in place, the Machine Config Operator triggers a full node reboot.

   ```
   $ oc apply -f mc-<pool_name>.yaml
   ```

   The plugin generates `MachineConfig` resources with the naming pattern `98-nftables-commatrix-<pool_name>`.

**Verification**

1. Open a debug shell on a target node by running the following commands:

   ```
   $ oc debug node/<node_name>
   sh-5.1# chroot /host
   ```

   * `<node_name>` is the name of a cluster node.
   * `chroot /host` accesses the host filesystem.
2. Verify that the `nftables` rules are active on a node by running the following command:

   ```
   sh-5.1# nft list ruleset
   ```

   ```
   ...
   table inet openshift_filter {
   	chain OPENSHIFT {
   		type filter hook input priority filter + 1; policy accept;
   		iif "lo" accept
   		ct state established,related accept
   		ip protocol icmp accept
   		ip6 nexthdr ipv6-icmp accept
   		tcp dport { 22, 111, 2379-2380, 6080, 6443, 9001, 9099-9100, 9103-9105, 9107-9108, 9192, 9258, 9443, 9637, 9978-9980, 10250, 10256-10259, 17697, 22623-22624, 30000-60999 } accept
   		udp dport { 111, 6081, 30000-60999 } accept
   		ip daddr 255.255.255.255 jump {
   			limit rate 1/minute burst 5 packets log prefix "firewall "
   			drop
   		}
   		jump {
   			limit rate 1/minute burst 5 packets log prefix "firewall "
   			drop
   		}
   	}
   }
   ...
   ```
3. Verify that denied traffic is logged with rate limiting by checking the node journal:

   ```
   $ oc debug node/<node_name> -- chroot /host journalctl -k --grep firewall
   ```

   Denied packets are logged, but log entries are rate-limited to one per minute with an initial burst of five entries.

### [2.8. Revert nftables firewall rules generated by the commatrix plugin](#commatrix-revert-nftables_configuring-firewall) Copy linkLink copied to clipboard!

If you need to remove the `nftables` firewall rules from your cluster nodes, delete the `MachineConfig` resources, and then clean up the `NodeDisruptionPolicy` entries.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You applied `nftables` firewall rules generated by the `commatrix` plugin.

**Procedure**

1. Identify the `MachineConfig` resources created by the `commatrix` plugin by running the following command:

   ```
   $ oc get machineconfig | grep nftables
   ```
2. Delete the `MachineConfig` resource for each node pool by running the following command:

   ```
   $ oc delete machineconfig 98-nftables-commatrix-<pool_name>
   ```
3. Wait for all `MachineConfigPool` resources to return to the `UPDATED` state:

   ```
   $ oc get mcp
   ```

   **Example output showing pools in `UPDATED` state**

   ```
   NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master   rendered-master-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6   True      False      False      1              1                   1                     0                      160d
   worker   rendered-worker-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6   True      False      False      0              0                   0                     0                      160d
   ```
4. Open a debug shell on a target node by running the following commands:

   ```
   $ oc debug node/<node_name>
   sh-5.1# chroot /host
   ```

   * `<node_name>` is the name of a cluster node.
   * `chroot /host` accesses the host filesystem.
5. Verify that the custom `nftables` rules were removed by running the following command:

   ```
   sh-5.1# nft list ruleset 2>&1 | grep -q openshift_filter || echo "Custom rules removed"
   ```
6. Remove the related `nftables` rules from the `NodeDisruptionPolicy` entries by editing the `MachineConfiguration` resource:

   ```
   $ oc edit machineconfiguration cluster
   ```

   Remove the `nftables.service` entry from `.spec.nodeDisruptionPolicy.units` and the `/etc/sysconfig/nftables.conf` entry from `.spec.nodeDisruptionPolicy.files`.

### [2.9. Reference flags for the commatrix plugin](#commatrix-plugin-reference_configuring-firewall) Copy linkLink copied to clipboard!

The following table describes the flags for the `commatrix` plugin.

Expand

| Flag | Type | Description |
| --- | --- | --- |
| `--customEntriesFormat` | string | Define the format of a custom entries file. The plugin appends the entries in this file to the generated data. Supported values are `json`, `yaml`, or `csv`. |
| `--customEntriesPath` | string | Define the file path to a custom entries file. The plugin appends the entries in this file to the generated data. |
| `--debug` | boolean | Enable verbose logging for debugging. The default value is `false`. |
| `--destDir` | string | Define the directory for output files. The default value is `communication-matrix`. |
| `--custom-node-group` | string | Assign nodes matching a label selector to a custom group for separate firewall rule generation. Specify in `<group_name>=<label_selector>` format. You can specify this flag multiple times to define multiple custom groups. This flag applies only to `nft`, `butane`, and `mc` output formats. A `MachineConfigPool` custom group matching the custom group name must exist before you apply the generated `MachineConfig` resources. |
| `--format` | string | Define the output format. Supported values are `json`, `yaml`, `csv`, `nft`, `butane`, or `mc`. The `butane` format generates Butane YAML configs containing nftables firewall rules. The `mc` format generates `MachineConfig` custom resources containing nftables firewall rules. The default value is `csv`. |
| `--host-open-ports` | boolean | Generate the expected communication data for the cluster environment. Identify the actual open ports on the cluster node to compare the difference between the expected open ports and the actual open ports. You can view the differences in the generated `matrix-diff-ss` file in the destination directory. For `nft`, `butane`, and `mc` formats, host open ports are merged into the communication matrix instead of generating a separate diff file. |
| `-h` | boolean | Display the plugin help information. |

Show more

## [Chapter 3. Installation configuration parameters](#installation-config-parameters-generic) Copy linkLink copied to clipboard!

Before you deploy an OpenShift Container Platform cluster, you create the `install-config.yaml` file and provide parameters to customize your cluster and the platform that hosts it. You can then modify the `install-config.yaml` file to customize your cluster further.

### [3.1. Available installation configuration parameters](#installation-configuration-parameters_installation-config-parameters-generic) Copy linkLink copied to clipboard!

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required, network, and optional installation configuration parameters that you can set as part of the installation process.

#### [3.1.1. Required configuration parameters](#installation-configuration-parameters-required_installation-config-parameters-generic) Copy linkLink copied to clipboard!

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

#### [3.1.2. Network configuration parameters](#installation-configuration-parameters-network_installation-config-parameters-generic) Copy linkLink copied to clipboard!

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults.

Only IPv4 addresses are supported.

Expand

Table 3.2. Network parameters

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

#### [3.1.3. Optional configuration parameters](#installation-configuration-parameters-optional_installation-config-parameters-generic) Copy linkLink copied to clipboard!

Optional installation configuration parameters are described in the following table:

Expand

Table 3.3. Optional parameters

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

## [Legal Notice](#idm140014192642752) Copy linkLink copied to clipboard!

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
