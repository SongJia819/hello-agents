---
title: "Installing IBM Cloud Bare Metal (Classic)"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_ibm_cloud_bare_metal_classic/index
retrieved_at: 2026-09-05T05:41:55.808398+00:00
---

# Installing IBM Cloud Bare Metal (Classic)

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on IBM Cloud Bare Metal (Classic)

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140240355386496)

**Abstract**

This document describes how to install OpenShift Container Platform on IBM Cloud Bare Metal (Classic).

---

## [Chapter 1. Prerequisites for installing a cluster on {ibm-cloud-bm}](#install-ibm-cloud-prerequisites) Copy linkLink copied to clipboard!

You can use installer-provisioned installation to install OpenShift Container Platform on IBM Cloud® Bare Metal (Classic) nodes. Review the prerequisites and requirements before you begin an installer-provisioned installation on IBM Cloud® nodes.

Important

Red Hat supports Intelligent Platform Management Interface (IPMI) and PXE on the provisioning network only. Red Hat has not tested Red Fish, virtual media, or other complementary technologies such as Secure Boot on IBM Cloud® deployments. You must configure a provisioning network.

Installer-provisioned installation of OpenShift Container Platform requires:

* One node with Red Hat Enterprise Linux CoreOS (RHCOS) 8.x installed, for running the provisioner
* Three control plane nodes
* One routable network
* One provisioning network

### [1.1. About setting up IBM Cloud Bare Metal (Classic) infrastructure](#setting-up-ibm-cloud-infrastructure_install-ibm-cloud) Copy linkLink copied to clipboard!

To deploy an OpenShift Container Platform cluster on IBM Cloud® Bare Metal (Classic) infrastructure, you must provision the IBM Cloud® nodes and configure the supporting infrastructure. This includes setting up virtual networking and creating the bare-metal servers that make up the cluster.

Important

Red Hat supports Intelligent Platform Management Interface (IPMI) and PXE on the `provisioning` network only. Red Hat has not tested Red Fish, virtual media, or other complementary technologies such as Secure Boot on IBM Cloud® deployments. You must configure a `provisioning` network.

You can customize IBM Cloud® nodes by using the IBM Cloud® API. When creating IBM Cloud® nodes, you must consider the following requirements.

#### [1.1.1. Use one data center per cluster](#use-one-data-center-per-cluster) Copy linkLink copied to clipboard!

All nodes in the OpenShift Container Platform cluster must run in the same IBM Cloud® data center.

#### [1.1.2. Create public and private VLANs](#create-public-and-private-vlans) Copy linkLink copied to clipboard!

Create all nodes with a single public virtual LAN (VLAN) and a single private VLAN.

#### [1.1.3. Ensure subnets have enough IP addresses](#ensure-subnets-have-enough-ip-addresses) Copy linkLink copied to clipboard!

IBM Cloud® public VLAN subnets use a `/28` prefix by default, which provides 16 IP addresses. That is enough for a cluster consisting of three control plane nodes, four compute nodes, and two IP addresses for the API virtual IP (VIP) and Ingress VIP on the `baremetal` network. For larger clusters, you might need a smaller prefix.

IBM Cloud® private VLAN subnets use a `/26` prefix by default, which provides 64 IP addresses. IBM Cloud® Bare Metal (Classic) uses private network IP addresses to access the Baseboard Management Controller (BMC) of each node. OpenShift Container Platform creates an additional subnet for the `provisioning` network. Network traffic for the `provisioning` network subnet routes through the private VLAN. For larger clusters, you might need a smaller prefix.

Expand

Table 1.1. IP addresses per prefix

| IP addresses | Prefix |
| --- | --- |
| 32 | `/27` |
| 64 | `/26` |
| 128 | `/25` |
| 256 | `/24` |

Show more

#### [1.1.4. Configuring NICs](#configuring-nics) Copy linkLink copied to clipboard!

OpenShift Container Platform deploys with two networks:

* `provisioning`: The `provisioning` network is a non-routable network used for provisioning the underlying operating system on each node that is a part of the OpenShift Container Platform cluster.
* `baremetal`: The `baremetal` network is a routable network. You can use any NIC order to interface with the `baremetal` network, provided it is not the NIC specified in the `provisioningNetworkInterface` configuration setting or the NIC associated to a node’s `bootMACAddress` configuration setting for the `provisioning` network.

While the cluster nodes can contain more than two NICs, the installation process only focuses on the first two NICs. For example:

Expand

| NIC | Network | VLAN |
| --- | --- | --- |
| NIC1 | `provisioning` | <provisioning\_vlan> |
| NIC2 | `baremetal` | <baremetal\_vlan> |

Show more

In the earlier example, NIC1 on all control plane and worker nodes connects to the non-routable network (`provisioning`) that is only used for the installation of the OpenShift Container Platform cluster. NIC2 on all control plane and worker nodes connects to the `baremetal` network.

Expand

| PXE | Boot order |
| --- | --- |
| NIC1 PXE-enabled `provisioning` network | 1 |
| NIC2 `baremetal` network. | 2 |

Show more

Note

Enable PXE on the NIC used for the `provisioning` network and disable it on all other NICs.

#### [1.1.5. Configure canonical names](#configure-canonical-names) Copy linkLink copied to clipboard!

Clients access the OpenShift Container Platform cluster nodes over the `baremetal` network. Configure IBM Cloud® subdomains or subzones where the canonical name extension is the cluster name.

```
<cluster_name>.<domain>
```

For example:

```
test-cluster.example.com
```

#### [1.1.6. Create DNS entries](#create-dns-entries) Copy linkLink copied to clipboard!

You must create DNS `A` record entries resolving to unused IP addresses on the public subnet for the following:

Expand

| Usage | Hostname | IP |
| --- | --- | --- |
| API | api.<cluster\_name>.<domain> | <ip> |
| Ingress LB (apps) | \*.apps.<cluster\_name>.<domain> | <ip> |

Show more

Control plane and worker nodes already have DNS entries after provisioning.

The following table provides an example of fully qualified domain names. The API and name server addresses begin with canonical name extensions. The hostnames of the control plane and worker nodes are examples, so you can use any host naming convention you prefer.

Expand

| Usage | Hostname | IP |
| --- | --- | --- |
| API | api.<cluster\_name>.<domain> | <ip> |
| Ingress LB (apps) | \*.apps.<cluster\_name>.<domain> | <ip> |
| Provisioner node | provisioner.<cluster\_name>.<domain> | <ip> |
| Control plane 0 | openshift-control-0.<cluster\_name>.<domain> | <ip> |
| Control plane 1 | openshift-control-1.<cluster\_name>.<domain> | <ip> |
| Control plane 2 | openshift-control-2.<cluster\_name>.<domain> | <ip> |
| Compute 0 | openshift-compute-0.<cluster\_name>.<domain> | <ip> |
| Compute 1 | openshift-compute-1.<cluster\_name>.<domain> | <ip> |
| Compute n | openshift-compute-n.<cluster\_name>.<domain> | <ip> |

Show more

OpenShift Container Platform includes functionality that uses cluster membership information to generate `A` records. This resolves the node names to their IP addresses. After the nodes register with the API, the cluster can disperse node information without using CoreDNS-mDNS. This eliminates the network traffic associated with multicast DNS.

Important

After provisioning the IBM Cloud® nodes, you must create a DNS entry for the `api.<cluster_name>.<domain>` domain name on the external DNS because removing CoreDNS causes the local entry to disappear. Failure to create a DNS record for the `api.<cluster_name>.<domain>` domain name in the external DNS server prevents worker nodes from joining the cluster.

#### [1.1.7. Network Time Protocol (NTP)](#network-time-protocol-ntp) Copy linkLink copied to clipboard!

Each OpenShift Container Platform node in the cluster must have access to an NTP server. OpenShift Container Platform nodes use NTP to synchronize their clocks. For example, cluster nodes use SSL/TLS certificates that require validation, which might fail if the date and time between the nodes are not in sync.

Important

Define a consistent clock date and time format in each cluster node’s firmware settings, or installation might fail.

#### [1.1.8. Configure a DHCP server](#configure-a-dhcp-server) Copy linkLink copied to clipboard!

IBM Cloud® Bare Metal (Classic) does not run DHCP on the public or private VLANs. After provisioning IBM Cloud® nodes, you must set up a DHCP server for the public VLAN, which corresponds to OpenShift Container Platform’s `baremetal` network.

Note

The IP addresses allocated to each node do not need to match the IP addresses allocated by the IBM Cloud® Bare Metal (Classic) provisioning system.

See the "Configuring the public subnet" section for details.

#### [1.1.9. Ensure BMC access privileges](#ensure-bmc-access-privileges) Copy linkLink copied to clipboard!

The **Remote management** page for each node on the dashboard has the node’s IPMI credentials. The default IPMI privileges prevent the user from making certain boot target changes. You must change the privilege level to `OPERATOR` so that Ironic can make those changes.

In the `install-config.yaml` file, add the `privilegelevel` parameter to the URLs used to configure each BMC. See the "Configuring the install-config.yaml file" section for additional details. For example:

```
ipmi://<IP>:<port>?privilegelevel=OPERATOR
```

Contact IBM Cloud® support to request that they increase the IPMI privileges to `ADMINISTRATOR` for each node.

#### [1.1.10. Create bare-metal servers](#create-bare-metal-servers) Copy linkLink copied to clipboard!

Create bare-metal servers in the IBM Cloud® dashboard by navigating to **Create resource** → **Bare Metal Servers for Classic**.

You can also create bare-metal servers with the `ibmcloud` CLI utility. For example:

```
$ ibmcloud sl hardware create --hostname <SERVERNAME> \
                            --domain <DOMAIN> \
                            --size <SIZE> \
                            --os <OS-TYPE> \
                            --datacenter <DC-NAME> \
                            --port-speed <SPEED> \
                            --billing <BILLING>
```

Note

IBM Cloud® servers might take 3-5 hours to become available.

## [Chapter 2. Setting up the environment for an OpenShift Container Platform installation on IBM Cloud(R) Bare Metal (Classic)](#install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

After you complete the prerequisites, set up the environment for an OpenShift Container Platform installation on IBM Cloud® Bare Metal (Classic) by preparing the provisioner node, configuring the network, and deploying the cluster.

### [2.1. Preparing the provisioner node on IBM Cloud(R) Bare Metal (Classic) infrastructure](#preparing-the-provisioner-node-for-openshift-install-on-ibm-cloud_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on IBM Cloud® Bare Metal (Classic) infrastructure, prepare the provisioner node by creating a non-root user, configuring network bridges, registering the node, installing required packages, and downloading the pull secret.

**Procedure**

1. Log in to the provisioner node via `ssh`.
2. Create a non-root user (`kni`) and give that user `sudo` privileges:

   ```
   # useradd kni
   ```

   ```
   # passwd kni
   ```

   ```
   # echo "kni ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/kni
   ```

   ```
   # chmod 0440 /etc/sudoers.d/kni
   ```
3. Create an `ssh` key for the new user:

   ```
   # su - kni -c "ssh-keygen -f /home/kni/.ssh/id_rsa -N ''"
   ```
4. Log in as the new user on the provisioner node:

   ```
   # su - kni
   ```
5. Use Red Hat Subscription Manager to register the provisioner node:

   ```
   $ sudo subscription-manager register --username=<user> --password=<pass> --auto-attach
   ```

   ```
   $ sudo subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms \
                                     --enable=rhel-8-for-x86_64-baseos-rpms
   ```

   Note

   For more information about Red Hat Subscription Manager, see [Registering a RHEL system with command-line tools](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/basic-reg-rhel-cli).
6. Install the following packages:

   ```
   $ sudo dnf install -y libvirt qemu-kvm mkisofs python3-devel jq ipmitool
   ```
7. Change the user to add the `libvirt` group to the newly created user:

   ```
   $ sudo usermod --append --groups libvirt kni
   ```
8. Start `firewalld`:

   ```
   $ sudo systemctl start firewalld
   ```
9. Enable `firewalld`:

   ```
   $ sudo systemctl enable firewalld
   ```
10. Start the `http` service:

    ```
    $ sudo firewall-cmd --zone=public --add-service=http --permanent
    ```

    ```
    $ sudo firewall-cmd --reload
    ```
11. Start and enable the `libvirtd` service:

    ```
    $ sudo systemctl enable libvirtd --now
    ```
12. Set the ID of the provisioner node:

    ```
    $ PRVN_HOST_ID=<ID>
    ```

    You can view the ID with the following `ibmcloud` command:

    ```
    $ ibmcloud sl hardware list
    ```
13. Set the ID of the public subnet:

    ```
    $ PUBLICSUBNETID=<ID>
    ```

    You can view the ID with the following `ibmcloud` command:

    ```
    $ ibmcloud sl subnet list
    ```
14. Set the ID of the private subnet:

    ```
    $ PRIVSUBNETID=<ID>
    ```

    You can view the ID with the following `ibmcloud` command:

    ```
    $ ibmcloud sl subnet list
    ```
15. Set the provisioner node public IP address:

    ```
    $ PRVN_PUB_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | jq .primaryIpAddress -r)
    ```
16. Set the CIDR for the public network:

    ```
    $ PUBLICCIDR=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .cidr)
    ```
17. Set the IP address and CIDR for the public network:

    ```
    $ PUB_IP_CIDR=$PRVN_PUB_IP/$PUBLICCIDR
    ```
18. Set the gateway for the public network:

    ```
    $ PUB_GATEWAY=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .gateway -r)
    ```
19. Set the private IP address of the provisioner node:

    ```
    $ PRVN_PRIV_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | \
                     jq .primaryBackendIpAddress -r)
    ```
20. Set the CIDR for the private network:

    ```
    $ PRIVCIDR=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .cidr)
    ```
21. Set the IP address and CIDR for the private network:

    ```
    $ PRIV_IP_CIDR=$PRVN_PRIV_IP/$PRIVCIDR
    ```
22. Set the gateway for the private network:

    ```
    $ PRIV_GATEWAY=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .gateway -r)
    ```
23. Set up the bridges for the `baremetal` and `provisioning` networks:

    ```
    $ sudo nohup bash -c "
        nmcli --get-values UUID con show | xargs -n 1 nmcli con delete
        nmcli connection add ifname provisioning type bridge con-name provisioning
        nmcli con add type bridge-slave ifname eth1 master provisioning
        nmcli connection add ifname baremetal type bridge con-name baremetal
        nmcli con add type bridge-slave ifname eth2 master baremetal
        nmcli connection modify baremetal ipv4.addresses $PUB_IP_CIDR ipv4.method manual ipv4.gateway $PUB_GATEWAY
        nmcli connection modify provisioning ipv4.addresses 172.22.0.1/24,$PRIV_IP_CIDR ipv4.method manual
        nmcli connection modify provisioning +ipv4.routes \"10.0.0.0/8 $PRIV_GATEWAY\"
        nmcli con down baremetal
        nmcli con up baremetal
        nmcli con down provisioning
        nmcli con up provisioning
        init 6
    "
    ```

    Note

    For `eth1` and `eth2`, substitute the appropriate interface name, as needed.
24. If required, SSH back into the `provisioner` node:

    ```
    # ssh kni@provisioner.<cluster_name>.<domain>
    ```
25. Verify the connection bridges have been properly created:

    ```
    $ sudo nmcli con show
    ```

    **Example output**

    ```
    NAME               UUID                                  TYPE      DEVICE
    baremetal          4d5133a5-8351-4bb9-bfd4-3af264801530  bridge    baremetal
    provisioning       43942805-017f-4d7d-a2c2-7cb3324482ed  bridge    provisioning
    virbr0             d9bca40f-eee1-410b-8879-a2d4bb0465e7  bridge    virbr0
    bridge-slave-eth1  76a8ed50-c7e5-4999-b4f6-6d9014dd0812  ethernet  eth1
    bridge-slave-eth2  f31c3353-54b7-48de-893a-02d2b34c4736  ethernet  eth2
    ```
26. Create a `pull-secret.txt` file:

    ```
    $ vim pull-secret.txt
    ```

    Go to [Install on Bare Metal with user-provisioned infrastructure](https://console.redhat.com/openshift/install/metal/user-provisioned). In step 1, click **Download pull secret**. Paste the contents into the `pull-secret.txt` file and save the contents in the `kni` user’s home directory.

### [2.2. Configuring the public subnet](#configuring-the-public-subnet_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

To offer DHCP services for OpenShift Container Platform cluster nodes on the public subnet in IBM Cloud® Bare Metal (Classic), you can install and configure `dnsmasq` on the provisioner node.

All of the OpenShift Container Platform cluster nodes must be on the public subnet. IBM Cloud® Bare Metal (Classic) does not offer a DHCP server on the subnet. Set it up separately on the provisioner node.

You must reset the BASH variables defined when preparing the provisioner node. Rebooting the provisioner node after preparing it will delete the BASH variables set before.

**Procedure**

1. Install `dnsmasq`:

   ```
   $ sudo dnf install dnsmasq
   ```
2. Open the `dnsmasq` configuration file:

   ```
   $ sudo vi /etc/dnsmasq.conf
   ```
3. Add the following configuration to the `dnsmasq` configuration file:

   ```
   interface=baremetal
   except-interface=lo
   bind-dynamic
   log-dhcp

   dhcp-range=<ip_addr>,<ip_addr>,<pub_cidr>
   dhcp-option=baremetal,121,0.0.0.0/0,<pub_gateway>,<prvn_priv_ip>,<prvn_pub_ip>

   dhcp-hostsfile=/var/lib/dnsmasq/dnsmasq.hostsfile
   ```

   where:

   `dhcp-range`
   :   Specifies the DHCP range for the `baremetal` network. Replace both instances of `<ip_addr>` with one unused IP address from the public subnet so that the range begins and ends with the same IP address. Replace `<pub_cidr>` with the CIDR of the public subnet.

   `dhcp-option`
   :   Specifies the DHCP option for the `baremetal` network. Replace `<pub_gateway>` with the IP address of the gateway for the `baremetal` network. Replace `<prvn_priv_ip>` with the private IP address of the provisioner node on the `provisioning` network. Replace `<prvn_pub_ip>` with the public IP address of the provisioner node on the `baremetal` network.

       1. To retrieve the value for `<pub_cidr>`, run the following command:

          ```
          $ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .cidr
          ```

          Replace `<publicsubnetid>` with the ID of the public subnet.
       2. To retrieve the value for `<pub_gateway>`, run the following command:

          ```
          $ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .gateway -r
          ```

          Replace `<publicsubnetid>` with the ID of the public subnet.
       3. To retrieve the value for `<prvn_priv_ip>`, run the following command:

          ```
          $ ibmcloud  sl hardware detail <id> --output JSON | \
                      jq .primaryBackendIpAddress -r
          ```

          Replace `<id>` with the ID of the provisioner node.
       4. To retrieve the value for `<prvn_pub_ip>`, run the following command:

          ```
          $ ibmcloud sl hardware detail <id> --output JSON | jq .primaryIpAddress -r
          ```

          Replace `<id>` with the ID of the provisioner node.
4. Obtain the list of hardware for the cluster:

   ```
   $ ibmcloud sl hardware list
   ```
5. Obtain the MAC addresses and IP addresses for each node:

   ```
   $ ibmcloud sl hardware detail <id> --output JSON | \
     jq '.networkComponents[] | \
     "\(.primaryIpAddress) \(.macAddress)"' | grep -v null
   ```

   Replace `<id>` with the ID of the node.

   **Example output**

   ```
   "10.196.130.144 00:e0:ed:6a:ca:b4"
   "141.125.65.215 00:e0:ed:6a:ca:b5"
   ```

   Make a note of the MAC address and IP address of the public network. Make a separate note of the MAC address of the private network, which you will use later in the `install-config.yaml` file. Repeat this procedure for each node until you have all the public MAC and IP addresses for the public `baremetal` network, and the MAC addresses of the private `provisioning` network.
6. Add the MAC and IP address pair of the public `baremetal` network for each node into the `dnsmasq.hostsfile` file:

   ```
   $ sudo vim /var/lib/dnsmasq/dnsmasq.hostsfile
   ```

   **Example input**

   ```
   00:e0:ed:6a:ca:b5,141.125.65.215,master-0
   <mac>,<ip>,master-1
   <mac>,<ip>,master-2
   <mac>,<ip>,worker-0
   <mac>,<ip>,worker-1
   ...
   ```

   Replace `<mac>,<ip>` with the public MAC address and public IP address of the corresponding node name.
7. Start `dnsmasq`:

   ```
   $ sudo systemctl start dnsmasq
   ```
8. Enable `dnsmasq` so that it starts when booting the node:

   ```
   $ sudo systemctl enable dnsmasq
   ```
9. Verify `dnsmasq` is running:

   ```
   $ sudo systemctl status dnsmasq
   ```

   **Example output**

   ```
   ● dnsmasq.service - DNS caching server.
   Loaded: loaded (/usr/lib/systemd/system/dnsmasq.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2021-10-05 05:04:14 CDT; 49s ago
   Main PID: 3101 (dnsmasq)
   Tasks: 1 (limit: 204038)
   Memory: 732.0K
   CGroup: /system.slice/dnsmasq.service
   └─3101 /usr/sbin/dnsmasq -k
   ```
10. Open ports `53` and `67` with UDP protocol:

    ```
    $ sudo firewall-cmd --add-port 53/udp --permanent
    ```

    ```
    $ sudo firewall-cmd --add-port 67/udp --permanent
    ```
11. Add `provisioning` to the external zone with masquerade:

    ```
    $ sudo firewall-cmd --change-zone=provisioning --zone=external --permanent
    ```

    This step ensures network address translation for IPMI calls to the management subnet.
12. Reload the `firewalld` configuration:

    ```
    $ sudo firewall-cmd --reload
    ```

### [2.3. Retrieving the OpenShift Container Platform installer](#retrieving-the-openshift-installer_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

Use the `stable-4.x` version of the installation program and your selected architecture to deploy the generally available stable version of OpenShift Container Platform.

**Procedure**

* Retrieve the installation program by running one of the following commands:

  ```
  $ export VERSION=stable-4.22
  ```

  ```
  $ export RELEASE_ARCH=<architecture>
  ```

  ```
  $ export RELEASE_IMAGE=$(curl -s https://mirror.openshift.com/pub/openshift-v4/$RELEASE_ARCH/clients/ocp/$VERSION/release.txt | grep 'Pull From: quay.io' | awk -F ' ' '{print $3}')
  ```

### [2.4. Extracting the OpenShift Container Platform installer](#extracting-the-openshift-installer_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

Extract the OpenShift Container Platform installer after retrieving it to prepare for the installation of the cluster.

**Procedure**

1. Set the environment variables:

   ```
   $ export cmd=openshift-baremetal-install
   ```

   ```
   $ export pullsecret_file=~/pull-secret.txt
   ```

   ```
   $ export extract_dir=$(pwd)
   ```
2. Get the `oc` binary:

   ```
   $ curl -s https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$VERSION/openshift-client-linux.tar.gz | tar zxvf - oc
   ```
3. Extract the installer:

   ```
   $ sudo cp oc /usr/local/bin
   ```

   ```
   $ oc adm release extract --registry-config "${pullsecret_file}" --command=$cmd --to "${extract_dir}" ${RELEASE_IMAGE}
   ```

   ```
   $ sudo cp openshift-baremetal-install /usr/local/bin
   ```

### [2.5. Configuring the install-config.yaml file](#configuring-the-install-config-file_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

To configure OpenShift Container Platform for IBM Cloud® Bare Metal (Classic) infrastructure, you can edit the `install-config.yaml` file to set the required IPMI privilege level and hardware parameters for your bare-metal nodes.

The `install-config.yaml` file requires some additional details. Most of the information is teaching the installation program and the resulting cluster enough about the available IBM Cloud® Bare Metal (Classic) hardware so that it is able to fully manage it. The material difference between installing on bare metal and installing on IBM Cloud® Bare Metal (Classic) is that you must explicitly set the privilege level for IPMI in the BMC section of the `install-config.yaml` file.

**Procedure**

1. Configure `install-config.yaml`. Change the appropriate variables to match the environment, including `pullSecret` and `sshKey`.

   ```
   apiVersion: v1
   baseDomain: <domain>
   metadata:
     name: <cluster_name>
   networking:
     machineNetwork:
     - cidr: <public-cidr>
     networkType: OVNKubernetes
   compute:
   - name: worker
     replicas: 2
   controlPlane:
     name: master
     replicas: 3
     platform:
       baremetal: {}
   platform:
     baremetal:
       apiVIP: <api_ip>
       ingressVIP: <wildcard_ip>
       provisioningNetworkInterface: <NIC1>
       provisioningNetworkCIDR: <CIDR>
       hosts:
         - name: openshift-master-0
           role: master
           bmc:
             address: ipmi://10.196.130.145?privilegelevel=OPERATOR
             username: root
             password: <password>
           bootMACAddress: 00:e0:ed:6a:ca:b4
           rootDeviceHints:
             deviceName: "/dev/sda"
         - name: openshift-worker-0
           role: worker
           bmc:
             address: ipmi://<out-of-band-ip>?privilegelevel=OPERATOR
             username: <user>
             password: <password>
           bootMACAddress: <NIC1_mac_address>
           rootDeviceHints:
             deviceName: "/dev/sda"
   pullSecret: '<pull_secret>'
   sshKey: '<ssh_pub_key>'
   ```

   where:

   `bmc.address`
   :   Specifies the IPMI address with `privilegelevel=OPERATOR`. IBM Cloud® Bare Metal (Classic) infrastructure requires this privilege level.

   `bootMACAddress`
   :   Specifies the MAC address of the private `provisioning` network NIC for the corresponding node.

       Note

       You can use the `ibmcloud` command-line utility to retrieve the password.

       ```
       $ ibmcloud sl hardware detail <id> --output JSON | \
         jq '"(.networkManagementIpAddress) (.remoteManagementAccounts[0].password)"'
       ```

       Replace `<id>` with the ID of the node.
2. Create a directory to store the cluster configuration:

   ```
   $ mkdir ~/clusterconfigs
   ```
3. Copy the `install-config.yaml` file into the directory:

   ```
   $ cp install-config.yaml ~/clusterconfigs
   ```
4. Power off all bare-metal nodes before installing the OpenShift Container Platform cluster:

   ```
   $ ipmitool -I lanplus -U <user> -P <password> -H <management_server_ip> power off
   ```
5. Remove old bootstrap resources if any remain from an earlier deployment try:

   ```
   for i in $(sudo virsh list | tail -n +3 | grep bootstrap | awk {'print $2'});
   do
     sudo virsh destroy $i;
     sudo virsh undefine $i;
     sudo virsh vol-delete $i --pool $i;
     sudo virsh vol-delete $i.ign --pool $i;
     sudo virsh pool-destroy $i;
     sudo virsh pool-undefine $i;
   done
   ```

### [2.6. Additional installation configuration parameters](#additional-install-config-parameters_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

Some parameters, such as the cluster domain name, are required in the `install-config.yaml` file when installing a cluster on bare metal. Others, such as the provisioning network CIDR, are optional.

Expand

Table 2.1. Required parameters

| Parameters | Default | Description |
| --- | --- | --- |
| `baseDomain` |  | The domain name for the cluster. For example, `example.com`. |
| `bootMode` | `UEFI` | The boot mode for a node. Options are `legacy`, `UEFI`, and `UEFISecureBoot`. If `bootMode` is not set, Ironic sets it while inspecting the node.  Note  For hardware that implements `BootMode` read-only, such as HP or Cisco, do not leave this parameter blank. You must manually set the system to UEFI mode before installation and explicitly set this parameter to UEFI. |
| ``` platform:   baremetal:     bootstrapExternalStaticDNS ``` |  | The static network DNS of the bootstrap node. You must set this value when deploying a cluster with static IP addresses when there is no Dynamic Host Configuration Protocol (DHCP) server on the bare-metal network. If you do not set this value, the installation program will use the value from `bootstrapExternalStaticGateway`, which causes problems when the IP address values of the gateway and DNS are different. |
| ``` platform:   baremetal:     bootstrapExternalStaticIP ``` |  | The static IP address for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare metal network. |
| ``` platform:   baremetal:     bootstrapExternalStaticGateway ``` |  | The static IP address of the gateway for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare metal network. |
| `sshKey` |  | The `sshKey` parameter sets the key in the `~/.ssh/id_rsa.pub` file required to access the control plane nodes and compute nodes. Typically, this key is from the `provisioner` node. |
| `pullSecret` |  | The `pullSecret` parameter sets a copy of the pull secret downloaded from the [Install OpenShift on Bare Metal](https://console.redhat.com/openshift/install/metal/user-provisioned) page when preparing the provisioner node. |
| ``` metadata:     name: ``` |  | The OpenShift Container Platform cluster name. For example, `openshift`. |
| ``` networking:     machineNetwork:     - cidr: ``` |  | The public CIDR (Classless Inter-Domain Routing) of the external network. For example, `10.0.0.0/24`. |
| ``` compute:   - name: worker ``` |  | The OpenShift Container Platform cluster requires a name for each compute node even if there are zero nodes. |
| ``` compute:     replicas: 2 ``` |  | Replicas sets the number of compute nodes in the OpenShift Container Platform cluster. |
| ``` controlPlane:     name: master ``` |  | The OpenShift Container Platform cluster requires a name for control plane nodes. |
| ``` controlPlane:     replicas: 3 ``` |  | Replicas sets the number of control plane nodes included as part of the OpenShift Container Platform cluster. |
| `provisioningNetworkInterface` |  | The name of the network interface on nodes connected to the provisioning network. For OpenShift Container Platform 4.9 and later releases, use the `bootMACAddress` parameter to enable Ironic to identify the IP address of the NIC instead of using the `provisioningNetworkInterface` parameter to identify the name of the NIC. |
| `defaultMachinePlatform` |  | The default configuration used for machine pools without a platform configuration. |
| `apiVIPs` |  | (Optional) The virtual IP address for Kubernetes API communication.  You must either provide this setting in the `install-config.yaml` file as a reserved IP from the `MachineNetwork` parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the `apiVIPs` configuration setting in the `install-config.yaml` file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses `api.<cluster_name>.<base_domain>` to derive the IP address from the DNS.  Note  Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the `apiVIP` parameter. From OpenShift Container Platform 4.12 or later, the `apiVIP` parameter is deprecated. Instead, use a list format for the `apiVIPs` parameter to specify an IPv4 address, an IPv6 address or both IP address formats. |
| `bmcCACert` |  | `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses when using self-signed certificates with `disableCertificateVerification` set to `False`. |
| `ingressVIPs` |  | (Optional) The virtual IP address for ingress traffic.  You must either provide this setting in the `install-config.yaml` file as a reserved IP from the `MachineNetwork` parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the `ingressVIPs` configuration setting in the `install-config.yaml` file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses `test.apps.<cluster_name>.<base_domain>` to derive the IP address from the DNS.  Note  Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the `ingressVIP` parameter. In OpenShift Container Platform 4.12 and later, the `ingressVIP` parameter is deprecated. Instead, use a list format for the `ingressVIPs` parameter to specify an IPv4 addresses, an IPv6 addresses or both IP address formats. |

Show more

Expand

Table 2.2. Optional Parameters

| Parameters | Default | Description |
| --- | --- | --- |
| ``` platform:   baremetal:     additionalNTPServers:     - <ip_address_or_domain_name> ``` |  | An optional list of additional NTP servers to add to each host. You can use an IP address or a domain name to specify each NTP server. Additional NTP servers are user-defined NTP servers that enable preinstallation clock synchronization when the cluster host clocks are out of synchronization. |
| `provisioningDHCPRange` | `172.22.0.10,172.22.0.100` | Defines the IP range for nodes on the provisioning network. |
| `provisioningNetworkCIDR` | `172.22.0.0/24` | The CIDR for the network to use for provisioning. When not using the default address range on the provisioning network, you must set this configuration parameter. |
| `clusterProvisioningIP` | The third IP address of the `provisioningNetworkCIDR`. | The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, `172.22.0.3`. |
| `bootstrapProvisioningIP` | The second IP address of the `provisioningNetworkCIDR`. | The IP address on the bootstrap VM where the provisioning services run while the installation program is deploying the control plane nodes. Defaults to the second IP address of the provisioning subnet. For example, `172.22.0.2` or `2620:52:0:1307::2`. |
| `externalBridge` | `baremetal` | The name of the bare metal bridge of the hypervisor attached to the bare metal network. |
| `provisioningBridge` | `provisioning` | The name of the provisioning bridge on the `provisioner` host attached to the provisioning network. |
| `architecture` |  | Defines the host architecture for your cluster. Valid values are `amd64` or `arm64`. |
| `defaultMachinePlatform` |  | The default configuration used for machine pools without a platform configuration. |
| `bootstrapOSImage` |  | A URL to override the default operating system image for the bootstrap node. The URL must contain a SHA-256 hash of the image. For example: `https://mirror.openshift.com/rhcos-<version>-qemu.qcow2.gz?sha256=<uncompressed_sha256>`. |
| `provisioningNetwork` |  | The `provisioningNetwork` parameter determines whether the cluster uses the provisioning network. If it does, the parameter also determines if the cluster manages the network.  `Disabled`: Set this parameter to `Disabled` to disable the requirement for a provisioning network. When set to `Disabled`, you must only use virtual media based provisioning, or install the cluster by using the Assisted Installer. If `Disabled` and using power management, BMCs must be accessible from the bare metal network. If `Disabled`, you must provide two IP addresses on the bare metal network for the provisioning services to use.  `Managed`: Set this parameter to `Managed`, which is the default, to fully manage the provisioning network, including DHCP, TFTP, and so on.  `Unmanaged`: Set this parameter to `Unmanaged` to enable the provisioning network but take care of manual configuration of DHCP. Virtual media provisioning is recommended but PXE is still available if required. |
| `httpProxy` |  | Set this parameter to the appropriate HTTP proxy used within your environment. |
| `httpsProxy` |  | Set this parameter to the appropriate HTTPS proxy used within your environment. |
| `noProxy` |  | Set this parameter to the appropriate list of exclusions for proxy usage within your environment. |

Show more

#### [2.6.1. Hosts](#hosts) Copy linkLink copied to clipboard!

The `hosts` parameter is a list of separate bare metal assets used to build the cluster.

Expand

Table 2.3. Hosts

| Name | Default | Description |
| --- | --- | --- |
| `name` |  | The name of the `BareMetalHost` resource to associate with the details. For example, `openshift-master-0`. |
| `role` |  | The role of the bare metal node. Either `master` (control plane node) or `worker` (compute node). |
| `bmc` |  | Connection details for the baseboard management controller. See the BMC addressing section for additional details. |
| ``` bmc:     address: ``` |  | The protocol and address of the BMC as a URL. |
| ``` bmc:     username: ``` |  | The username of the BMC. |
| ``` bmc:     password: ``` |  | The password of the BMC. |
| ``` bmc:     disableCertificateVerification: ``` | `False` | `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses. For OpenShift Container Platform 4.16 and earlier, the value should be `True` when using a self-signed certificate. OpenShift Container Platform supports self-signed certificates with certificate verification when used with the `bmcVerifyCA` parameter. |
| ``` platform:   baremetal:     bmcVerifyCA: ``` |  | A local or self-signed CA certificate that the installation program will use to secure communication with the BMC. If you specify your own CA certificate, ensure that `disableCertificateVerification` is set to `False` so that the user-provided CA certificate is validated. |
| `bootMACAddress` |  | The MAC address of the NIC that the host uses for the provisioning network. Ironic retrieves the IP address by using the `bootMACAddress` parameter. Then, it binds to the host.  Note  You must provide a valid MAC address from the host if you disabled the provisioning network. |
| `networkConfig` |  | Set this optional parameter to configure the network interface of a host. See "(Optional) Configuring host network interfaces" for additional details. |

Show more

### [2.7. Root device hints](#root-device-hints_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

The `rootDeviceHints` parameter enables the installer to provision the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installer examines the devices in the order it discovers them, and compares the discovered values with the hint values. The installer uses the first discovered device that matches the hint value. The configuration can combine multiple hints, but a device must match all hints for the installer to select it.

Expand

Table 2.4. Subfields

| Subfield | Description |
| --- | --- |
| `deviceName` | A string containing a Linux device name such as `/dev/vda` or `/dev/disk/by-path/`.  Note  It is recommended to use the `/dev/disk/by-path/<device_path>` link to the storage location.  The hint must match the actual value exactly. |
| `hctl` | A string containing a SCSI bus address like `0:0:0:0`. The hint must match the actual value exactly. |
| `model` | A string containing a vendor-specific device identifier. The hint can be a substring of the actual value. |
| `vendor` | A string containing the name of the vendor or manufacturer of the device. The hint can be a sub-string of the actual value. |
| `serialNumber` | A string containing the device serial number. The hint must match the actual value exactly. |
| `minSizeGigabytes` | An integer representing the minimum size of the device in gigabytes. |
| `wwn` | A string containing the unique storage identifier. The hint must match the actual value exactly. |
| `wwnWithExtension` | A string containing the unique storage identifier with the vendor extension appended. The hint must match the actual value exactly. |
| `wwnVendorExtension` | A string containing the unique vendor storage identifier. The hint must match the actual value exactly. |
| `rotational` | A boolean indicating whether the device should be a rotating disk (true) or not (false). |

Show more

**Example usage**

```
     - name: master-0
       role: master
       bmc:
         address: ipmi://10.10.0.3:6203
         username: admin
         password: redhat
       bootMACAddress: de:ad:be:ef:00:40
       rootDeviceHints:
         deviceName: "/dev/sda"
```

### [2.8. Creating the OpenShift Container Platform manifests](#creating-the-openshift-manifests_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

Create manifest files to begin customizing your cluster installation.

**Procedure**

* Create the OpenShift Container Platform manifests by running the following command:

  ```
  $ ./openshift-baremetal-install --dir ~/clusterconfigs create manifests
  ```

  **Example output**

  ```
  INFO Consuming Install Config from target directory
  WARNING Making control-plane schedulable by setting MastersSchedulable to true for Scheduler cluster settings
  WARNING Discarding the OpenShift Manifest that was provided in the target directory because its dependencies are dirty and it needs to be regenerated
  ```

### [2.9. Deploying the cluster via the OpenShift Container Platform installer](#deploying-the-cluster-via-the-openshift-installer_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

You can deploy the cluster by running the OpenShift Container Platform installer.

**Procedure**

* Run the OpenShift Container Platform installer:

  ```
  $ ./openshift-baremetal-install --dir ~/clusterconfigs --log-level debug create cluster
  ```

### [2.10. Following the progress of the installation](#ipi-install-following-the-progress-of-the-installation_install-ibm-cloud-installation-workflow) Copy linkLink copied to clipboard!

During the deployment process, you can check the installation’s overall status by issuing the `tail` command to the `.openshift_install.log` log file in the install directory folder.

**Procedure**

* Track installation progress by running the following command:

  ```
  $ tail -f /path/to/install-dir/.openshift_install.log
  ```

## [Legal Notice](#idm140240355386496) Copy linkLink copied to clipboard!

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
