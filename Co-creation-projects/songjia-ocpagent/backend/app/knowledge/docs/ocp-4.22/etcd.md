---
title: "etcd"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/index
retrieved_at: 2026-09-05T05:41:47.113690+00:00
---

# etcd

---

OpenShift Container Platform 4.22

## Providing redundancy with etcd

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140035064915376)

**Abstract**

This document provides instructions for using etcd, which ensures a reliable approach to cluster configuration and resiliency in OpenShift Container Platform.

---

## [Chapter 1. Overview of etcd](#etcd-overview) Copy linkLink copied to clipboard!

etcd is the primary Kubernetes data store on OpenShift Container Platform. Knowing how disk, network, and consensus latency affect etcd helps you keep the control plane reliable.

etcd (pronounced et-see-dee) is a consistent, distributed key-value store that stores small amounts of data across a cluster of machines that can fit entirely in memory. As the core component of many projects, etcd is also the primary data store for Kubernetes, which is the standard system for container orchestration.

By using etcd, you can benefit in several ways:

* Support consistent uptime for your cloud-native applications, and keep them working even if individual servers fail
* Store and replicate all cluster states for Kubernetes
* Distribute configuration data to offer redundancy and resiliency for the configuration of nodes

Important

The default etcd configuration optimizes container orchestration. Use it as designed for the best results.

### [1.1. How etcd works](#how-etcd-works_etcd-overview) Copy linkLink copied to clipboard!

The etcd Operator deploys and manages the etcd cluster for the OpenShift Container Platform control plane by observing state, analyzing differences, and correcting drift.

To ensure a reliable approach to cluster configuration and management, etcd uses the etcd Operator. The Operator simplifies the use of etcd on a Kubernetes container platform such as OpenShift Container Platform.

Additionally, you can use the etcd Operator to deploy and manage the etcd cluster for the OpenShift Container Platform control plane. The etcd Operator manages the cluster state in the following ways:

* Observes the cluster state by using the Kubernetes API
* Analyzes differences between the current state and the required state
* Corrects the differences through the etcd cluster management APIs, the Kubernetes API, or both

Note

etcd holds the cluster state, which is constantly updated. This state is continuously persisted, which leads to a high number of small changes at high frequency. As a result, it is critical to back up the etcd cluster member with fast, low-latency I/O. For more information about best practices for etcd, see "Recommended etcd practices".

### [1.2. Factors that affect etcd performance](#understand-etcd-performance_etcd-overview) Copy linkLink copied to clipboard!

Disk latency, network latency and jitter, consensus delay, database size, and Kubernetes API transaction rate all influence etcd reliability on OpenShift Container Platform.

As a consistent distributed key-value store operating as a cluster of replicated nodes, etcd follows the Raft algorithm by electing one node as the leader and the others as followers. The leader maintains the current state of the system current state and ensures that the followers are up-to-date.

The leader node is responsible for log replication. It handles incoming write transactions from the client and writes a Raft log entry that it then broadcasts to the followers.

When an etcd client such as `kube-apiserver` connects to an etcd member that is requesting an action that requires a quorum, such as writing a value, if the etcd member is a follower, it returns a message indicating that the transaction needs to go to the leader.

When the etcd client requests an action from the leader that requires a quorum, such as writing a value, the leader maintains the client connection open while it writes the local Raft log, broadcasts the log to the followers, and waits for the majority of the followers to acknowledge to have committed the log without failures. The leader sends the acknowledgment to the etcd client and closes the session. If failure notifications are received from the followers and a consensus is not met, the leader returns the error message to the client and closes the session.

OpenShift Container Platform maintains etcd timers that are optimized for each platform. OpenShift Container Platform has prescribed validated values that are optimized for each platform provider. The default `etcd timers` parameters with `platform=none` or `platform=metal` values are as follows:

**OpenShift Container Platform timer conditions for etcd**

```
- name: ETCD_ELECTION_TIMEOUT
  value: "1000"
  ...
- name: ETCD_HEARTBEAT_INTERVAL
  value: "100"
```

* `ETCD_ELECTION_TIMEOUT` specifies how long a follower node waits without hearing a heartbeat before it attempts to become the leader.
* `ETCD_HEARTBEAT_INTERVAL` specifies the frequency that the leader notifies followers that it is still the leader.

These parameters do not provide all of the information for the control plane or for etcd. An etcd cluster is sensitive to disk latencies. Because etcd must persist proposals to its log, disk activity from other processes might cause long `fsync` latencies. The consequence is that etcd might miss heartbeats, causing request timeouts and temporary leader loss. During a leader loss and reelection, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.

#### [1.2.1. Effects of disk latency on etcd](#etcd-perf-disk-latency_etcd-overview) Copy linkLink copied to clipboard!

An etcd cluster is sensitive to disk latencies. To understand the disk latency that etcd experiences by etcd in your control plane environment, run the Flexible I/O Tester (fio) tests or suite, to check etcd disk performance in OpenShift Container Platform.

Important

Use only the `fio` test to measure disk latency at a specific point in time. This test does not account for long-term disk behavior and other disk workloads that occur with etcd in a production environment.

Ensure that the final report classifies the disk as appropriate for etcd, as shown in the following example:

```
...
99th percentile of fsync is 5865472 ns
99th percentile of the fsync is within the suggested threshold: - 20 ms, the disk can be used to host etcd
```

When a high latency disk is used, a message states that the disk is not suggested for etcd, as shown in the following example:

```
...
99th percentile of fsync is 15865472 ns
99th percentile of the fsync is greater than the suggested value which is 20 ms, faster disks are suggested to host etcd for better performance
```

When your cluster deployments span many data centers that are using disks for etcd that do not meet the suggested latency, service-affecting failures can occur. In addition, the network latency that the control plane can sustain is dramatically reduced.

#### [1.2.2. Effects of network latency and jitter on etcd](#etcd-perf-network-latency-jitter_etcd-overview) Copy linkLink copied to clipboard!

Use the tools that are described in the maximum transmission unit (MTU) discovery and validation section to obtain the average and maximum network latency.

The value of the heartbeat interval should be approximately the maximum of the average round-trip time (RTT) between members, normally around 1.5 times the round-trip time. With the OpenShift Container Platform default heartbeat interval of 100 ms, the suggested RTT between control plane nodes is less than 33 ms, with a maximum of less than 66 ms (66 ms x 1.5 = 99 ms). Any network latency that is larger might cause service-affecting events and cluster instability.

The network latency is determined by factors that include the technology of the transport networks, such as copper, fiber, wireless, or satellite, the number and quality of the network devices in the transport network, and other factors.

Consider network latency with network jitter for exact calculations. *Network jitter* is the variance in network latency or the variation in the delay of received packets. In efficient network conditions, the jitter should be zero. Network jitter affects the network latency calculations for etcd because the actual network latency over time will be the RTT plus or minus Jitter.

For example, a network with a maximum latency of 80 ms and jitter of 30 ms will experience latencies of 110 ms, which means etcd will miss heartbeats. This condition results in request timeouts and temporary leader loss. During a leader loss and re-election, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.

#### [1.2.3. Effects of consensus latency on etcd](#etcd-perf-consensus-latency_etcd-overview) Copy linkLink copied to clipboard!

The procedure can run only on an active cluster. The disk or network test should be completed while you plan a cluster deployment. That test validates and monitors cluster health after a deployment.

By using the `etcdctl` CLI, you can watch the latency for reaching consensus as experienced by etcd. You must identify one of the etcd pods and then retrieve the endpoint health.

#### [1.2.4. etcd peer round-trip time impacts on performance](#etcd-perf-rtt_etcd-overview) Copy linkLink copied to clipboard!

The etcd peer round- trip time (RTT) is not the same as the network RTT. This calculation is an end-to-end test metric about how quickly replication can occur among members.

The etcd peer RTT is the metric that shows the latency of etcd to finish replicating a client request among all the etcd members. The OpenShift Container Platform console provides dashboards to visualize the various etcd metrics. In the console, click **Observe** → **Dashboards**. From the dropdown list, select **etcd**.

A plot that summarizes the etcd peer RTT is near the end of the etcd **Dashboard** page.

#### [1.2.5. Effects of database size on etcd](#etcd-perf-db-size_etcd-overview) Copy linkLink copied to clipboard!

The etcd database size has a direct impact on the time to complete the etcd defragmentation process. OpenShift Container Platform automatically runs the etcd defragmentation on one etcd member at a time when it detects at least 45% fragmentation. During the defragmentation process, the etcd member cannot process any requests. On small etcd databases, the defragmentation process happens in less than a second. With larger etcd databases, the disk latency directly impacts the fragmentation time, causing additional latency, as operations are blocked while defragmentation happens.

The size of the etcd database is a factor to consider when network partitions isolate a control plane node for a period of time, and the control plane needs to sync after communication is re-established.

Minimal options exist for controlling the size of the etcd database, because it depends on the Operators and applications in the system. When you consider the latency range where the system operates, account for the effects of synchronization or defragmentation per size of the etcd database.

The magnitude of the effects is specific to the deployment. The time to complete a defragmentation will cause degradation in the transaction rate, as the etcd member cannot accept updates during the defragmentation process. Similarly, the time for the etcd re-synchronization for large databases with high change rate affects the transaction rate and transaction latency on the system. Consider the following two examples for the type of impacts to plan for.

The first example of the effect of etcd defragmentation based on database size is that writing an etcd database of 1 GB to a slow 7200 RPMs disk at 80 Mb per second takes about 1 minute and 40 seconds. In such a scenario, the defragmentation process takes at least this long, to complete the defragmentation.

The second example of the effect of database size on etcd synchronization is that if there is a change of 10% of the etcd database during disconnection of one of the control plane nodes, the sync needs to transfer at least 100 MB. Transferring 100 MB over a 1 Gbps link takes 800 ms. On clusters with regular transactions with the Kubernetes API, the larger the etcd database size, the more network instabilities will cause control plane instabilities.

In OpenShift Container Platform, the etcd dashboard has a plot that reports the size of the etcd database. Alternatively, you can obtain the database size from the CLI by using the `etcdctl` tool.

```
# oc get pods -n openshift-etcd -l app=etcd
```

**Example output**

```
NAME      READY   STATUS    RESTARTS   AGE
etcd-m0   4/4     Running   4          22h
etcd-m1   4/4     Running   4          22h
etcd-m2   4/4     Running   4          22h
```

```
# oc exec -t etcd-m0 -- etcdctl endpoint status -w simple | cut -d, -f 1,3,4
```

**Example output**

```
https://198.18.111.12:2379, 3.5.6, 1.1 GB
https://198.18.111.13:2379, 3.5.6, 1.1 GB
https://198.18.111.14:2379, 3.5.6, 1.1 GB
```

#### [1.2.6. Effects of the Kubernetes API transaction rate on etcd](#etcd-perf-kube-api_etcd-overview) Copy linkLink copied to clipboard!

When you are using a stretched control plane, the Kubernetes API transaction rate depends on the characteristics of the particular deployment. It depends on the combination of the etcd disk latency, the etcd RTT, and the size of objects that are written to the API. As a result, when you use stretched control planes, the cluster administrators need to test the environment to determine the sustained transaction rate that is possible for their environment. The `kube-burner` tool can be used for this purpose.

You cannot determine the transaction rate of the Kubernetes API without measuring it. One of the tools that is used for load testing the control plane is `kube-burner`. The binary provides a OpenShift Container Platform wrapper for testing OpenShift Container Platform clusters. It is used to test cluster or node density. For testing the control plane, `kube-burner ocp` has three workload profiles: `cluster-density`, `cluster-density-v2`, and `cluster-density-ms`. Each workload profile creates a series of resources designed to load the control.

## [Chapter 2. Recommended etcd practices](#etcd-practices) Copy linkLink copied to clipboard!

Follow storage, latency, and hardware validation guidance for etcd to reduce leader elections, API timeouts, and control plane instability on OpenShift Container Platform.

### [2.1. Storage practices for etcd](#recommended-etcd-practices_etcd-practices) Copy linkLink copied to clipboard!

Because etcd writes data to disk and persists proposals on disk, its performance depends on disk performance.

Although etcd is not particularly I/O intensive, it requires a low latency block device for optimal performance and stability. Because the consensus protocol for etcd depends on persistently storing metadata to a log (WAL), etcd is sensitive to disk-write latency. Slow disks and disk activity from other processes can cause long fsync latencies.

Those latencies can cause etcd to miss heartbeats, not commit new proposals to the disk on time, and ultimately experience request timeouts and temporary leader loss. High write latencies also lead to an OpenShift API slowness, which affects cluster performance. Because of these reasons, avoid colocating other workloads on the control-plane nodes that are I/O sensitive or intensive and share the same underlying I/O infrastructure.

Run etcd on a block device that can write at least 50 IOPS of 8KB sequentially, including fdatasync, in under 10ms. For heavy loaded clusters, sequential 500 IOPS of 8000 bytes (2 ms) are recommended. To measure those numbers, you can use a benchmarking tool, such as the `fio` command.

To achieve such performance, run etcd on machines that are backed by SSD or NVMe disks with low latency and high throughput. Consider single-level cell (SLC) solid-state drives (SSDs), which provide 1 bit per memory cell, are durable and reliable, and are ideal for write-intensive workloads.

Note

The load on etcd arises from static factors, such as the number of nodes and pods, and dynamic factors, including changes in endpoints due to pod autoscaling, pod restarts, job executions, and other workload-related events. To accurately size your etcd setup, you must analyze the specific requirements of your workload. Consider the number of nodes, pods, and other relevant factors that impact the load on etcd.

The following hard drive practices provide optimal etcd performance:

* Use dedicated etcd drives. Avoid drives that communicate over the network, such as iSCSI. Do not place log files or other heavy workloads on etcd drives.
* Prefer drives with low latency to support fast read and write operations.
* Prefer high-bandwidth writes for faster compactions and defragmentation.
* Prefer high-bandwidth reads for faster recovery from failures.
* Use solid state drives as a minimum selection. Prefer NVMe drives for production environments.
* Use server-grade hardware for increased reliability.
* Avoid NAS or SAN setups and spinning drives. Ceph Rados Block Device (RBD) and other types of network-attached storage can result in unpredictable network latency. To provide fast storage to etcd nodes at scale, use PCI passthrough to pass NVM devices directly to the nodes.
* Always benchmark by using utilities such as `fio`. You can use such utilities to continuously monitor the cluster performance as it increases.
* Avoid using the Network File System (NFS) protocol or other network based file systems.

Some key metrics to monitor on a deployed OpenShift Container Platform cluster are p99 of etcd disk write ahead log duration and the number of etcd leader changes. Use Prometheus to track these metrics.

Note

The etcd member database sizes can vary in a cluster during normal operations. This difference does not affect cluster upgrades, even if the leader size is different from the other members.

### [2.2. Cluster latency requirements for etcd](#recommended-cluster-latency-etcd_etcd-practices) Copy linkLink copied to clipboard!

etcd requires low network and disk I/O latency so that Raft consensus can commit changes quickly and recover from leader failures without destabilizing the cluster.

Address two constraints to provide a low-latency, high-availability network for etcd:

* network I/O latency
* disk I/O latency

etcd uses the Raft consensus algorithm, and every change must replicate to a majority of cluster members before it commits. This process is highly sensitive to network and disk performance. The minimum time for an etcd request is the round-trip time (RTT) between members, plus the time required to write data to permanent storage.

To achieve high availability, etcd must detect and recover from a leader failure quickly. This depends on two key tuning parameters:

Heartbeat Interval
:   The frequency that the leader sends a heartbeat to followers. This value should be close to the average RTT between members.

Election Timeout
:   The time a follower waits without hearing a heartbeat before it attempts to become the new leader. This should be at least 10 times the RTT value to account for network variance.

In a healthy cluster, the round-trip time between members should be less than 50 ms to eensure stability and avoid frequent leader elections. For this reason, etcd clusters are often deployed within a single data center or availability zone to minimize physical distance and network latency.

To support a low-latency, high-availability network, especially during the leader election process, an arbiter site should be located where it provides an RTT latency of less than 10 ms. The arbiter component of a network maintains consistency and availability in a distributed system.

### [2.3. Validating the hardware for etcd](#etcd-verify-hardware_etcd-practices) Copy linkLink copied to clipboard!

Validate control plane disk performance with `fio` before or after you create the OpenShift Container Platform cluster so that you can confirm that storage meets etcd latency requirements.

The output of the following procedure reports whether the disk is fast enough to host etcd by comparing the 99th percentile of the fsync metric captured from the run to see if it is less than 10 ms.

A few of the most important etcd metrics that might affected by I/O performance are as follows:

* `etcd_disk_wal_fsync_duration_seconds_bucket` reports the etcd WAL fsync duration.
* `etcd_disk_backend_commit_duration_seconds_bucket` reports the etcd backend commit latency duration.
* `etcd_server_leader_changes_seen_total` reports the leader changes.

Because etcd replicates the requests among all the members, its performance strongly depends on network input/output (I/O) latency. High network latencies result in etcd heartbeats taking longer than the election timeout, which results in leader elections that are disruptive to the cluster. A key metric to monitor on a deployed OpenShift Container Platform cluster is the 99th percentile of etcd network peer latency on each etcd cluster member. Use Prometheus to track the metric.

The `histogram_quantile(0.99, rate(etcd_network_peer_round_trip_time_seconds_bucket[2m]))` metric reports the round trip time for etcd to finish replicating the client requests between the members. Ensure that it is less than 50 ms.

**Prerequisites**

* A container runtime, such as Podman or Docker, is installed on the machine that you are testing.
* The `/var/lib/etcd` path is available for writing test data.

**Procedure**

* Run `fio` and analyze the results:

  + If you use Podman, run the following command:

    ```
    $ sudo podman run --volume /var/lib/etcd:/var/lib/etcd:Z quay.io/cloud-bulldozer/etcd-perf
    ```
  + If you use Docker, run the following command:

    ```
    $ sudo docker run --volume /var/lib/etcd:/var/lib/etcd:Z quay.io/cloud-bulldozer/etcd-perf
    ```

**Verification**

* Confirm that the 99th percentile of the fsync metric from the run is less than 10 ms.
* Confirm that the report indicates that the disk is fast enough to host etcd.

## [Chapter 3. Ensuring reliable etcd performance and scalability](#etcd-performance) Copy linkLink copied to clipboard!

Optimize etcd reliability and scalability by understanding hardware, network, and cluster factors that affect control plane performance, from storage latency to API transaction rates.

### [3.1. Leader election and log replication of etcd](#etcd-leader-election-log-replication_etcd-performance) Copy linkLink copied to clipboard!

etcd uses Raft leader election and log replication so the cluster stays consistent during writes. Understanding how the leader handles quorum requests helps you diagnose control plane latency and write failures.

etcd is a consistent, distributed key-value store that operates as a cluster of replicated nodes. Following the Raft algorithm, etcd operates by electing one node as the leader and the others as followers. The leader maintains the system’s current state and ensures that the followers are up-to-date.

The leader node is responsible for log replication. It handles incoming write transactions from the client and writes a Raft log entry that it then broadcasts to the followers.

When an etcd client such as `kube-apiserver` connects to an etcd member that is requesting an action that requires a quorum, such as writing a value, if the etcd member is a follower, it returns a message indicating the transaction should be sent to the leader.

When the etcd client requests an action that requires a quorum from the leader, the leader keeps the client connection open while it writes the local Raft log, broadcasts the log to the followers, and waits for the majority of the followers to acknowledge to have committed the log without failures. Only then does the leader send the acknowledgment to the etcd client and close the session. If failure notifications are received from the followers and the majority fails to reach a consensus, the leader returns the error message to the client and closes the session.

### [3.2. Node scaling for etcd](#etcd-node-scaling_etcd-performance) Copy linkLink copied to clipboard!

In general, clusters must have 3 control plane nodes. However, if your cluster is installed on a bare metal platform, it can have up to 5 control plane nodes. If your bare-metal cluster has fewer than 5 control plane nodes, you can scale up the cluster as a postinstallation task.

For example, to scale from 3 to 4 control plane nodes after installation, you can add a host and install it as a control plane node. Then, the etcd Operator scales accordingly to account for the additional control plane node.

Scaling a cluster to 4 or 5 control plane nodes is available only on bare metal platforms.

For more information about how to scale control plane nodes by using the Assisted Installer, see "Adding hosts" and "Replacing a control plane node in a healthy cluster".

Note

While adding control plane nodes can increase reliability and availability, it can decrease throughput and increase latency, affecting performance.

The following table shows failure tolerance for clusters of different sizes:

Expand

Table 3.1. Failure tolerances by cluster size

| Cluster size | Majority | Failure tolerance |
| --- | --- | --- |
| 1 node | 1 | 0 |
| 3 nodes | 2 | 1 |
| 4 nodes | 3 | 1 |
| 5 nodes | 3 | 2 |

Show more

For more information about recovering from quorum loss, see "Restoring to an earlier cluster state".

### [3.3. Managing etcd size by limiting the duration of Kubernetes events](#etcd-customize-ttl_etcd-performance) Copy linkLink copied to clipboard!

To manage etcd size, you can set the maximum time that Kubernetes events are stored in the etcd database of the Kubernetes API server. By specifying the `eventTTLMinutes` property, you can control how long events are stored in the etcd database before they are purged.

The `eventTTLMinutes` property is managed through the `KubeAPIServer` custom resource, which is maintained by the Kube API Server Operator.

**Procedure**

1. Edit the `KubeAPIServer` custom resource by entering the following command:

   ```
   $ oc patch kubeapiserver/cluster -p='{"spec": {"eventTTLMinutes": 5 }}' --type=merge
   ```

   The value for the `eventTTLMinutes` property specifies how many minutes events are stored in the etcd database. Valid values are `5` - `180`.
2. Save the changes to the `KubeAPIServer` custom resource.

   The Kube API Server Operator automatically reconciles the change, which involves rolling out new configurations to the Kube API Server pods.
3. Wait for the rollout to finish by entering the following command:

   ```
   $ oc adm wait-for-stable-cluster
   ```

   The following example shows the output that is displayed during that process:

   ```
   ...
   clusteroperators/kube-apiserver is still progressing after 10s
   ...
   clusteroperators/kube-apiserver stabilized at 2025-11-12T12:02:40+01:00 after 9m0s
   ```

**Verification**

* To verify that the configuration was applied, enter the following command:

  ```
  $ oc get cm config -n openshift-kube-apiserver -ojsonpath='{.data.config\.yaml}' | jq -r ".apiServerArguments[\"event-ttl\"][0]"
  ```

  The output shows the configured duration, which is 5m in the following example:

  ```
  5m
  ```

  Note

  Only newly created events are written to etcd by using the new value for the `eventTTLMinutes` property. Older, existing events are not updated and will expire according to any previously specified TTL values.
* To manually verify that a given event was written with a shorter lease, examine the lease directly on etcd by entering the following command:

  ```
  $ oc exec -it pods/<etcd_pod_name> -n openshift-etcd -c etcdctl -- sh
  ```

  The output of the command looks similar to the following example:

  ```
  sh-5.1h# $ etcdctl lease list | xargs -I {} etcdctl lease timetolive {}
  lease 1e6e9a77a71d8235 granted with TTL(15s), remaining(1s)
  lease 1e6e9a77a71d8247 granted with TTL(15s), remaining(3s)
  lease 1e6e9a77a71d8252 granted with TTL(15s), remaining(3s)
  lease 1e6e9a77a71d8310 granted with TTL(15s), remaining(11s)
  lease 1e6e9a77a71d8332 granted with TTL(15s), remaining(12s)
  lease 1e6e9a77a71d833e granted with TTL(15s), remaining(13s)
  lease 086e9a77a31f0776 granted with TTL(315s), remaining(177s)
  lease 086e9a779dcd8245 granted with TTL(10860s), remaining(8369s)
  lease 086e9a779dcd8fdf granted with TTL(10860s), remaining(8369s)
  ```

  Note

  Other API objects can also have leases.
* To inspect the attached keys, filter for the key prefix of the event by entering the following command:

  ```
  $ etcdctl lease list | xargs -I {} etcdctl lease timetolive --keys {} | grep "/kubernetes.io/events"
  ```

  The output looks similar to the following example:

  ```
  lease 0f009a77a48509ac granted with TTL(315s), remaining(74s), attached keys([/kubernetes.io/events/openshift-marketplace/redhat-operators-rrq79.18773e905b3e29a8 /kubernetes.io/events/openshift-marketplace/community-operators-csds7.18773e91b1e551a3])
  ...
  ...
  lease 1e6e9a77a71d3df1 granted with TTL(10860s), remaining(9478s), attached keys([/kubernetes.io/events/openshift-kube-apiserver/kube-apiserver-guard-ci-ln-pbkb71t-72292-dwp9h-master-2.18773c38ef4dcc03])
  ```

  In the example, the TTL value is 5 minutes (`300s`), but the output shows `315s` because a lease buffer reuse of 5% is added.

  Note

  If a lease can be reused, etcd reuses it. Instead of creating a unique etcd lease for every resource that requires a `TTL` property, which would force the API server to track thousands of separate objects, the system reuses a smaller pool of existing leases. When a new object needs a lease for a specific duration, the manager checks for an existing lease that still has enough remaining life to cover that duration, plus a small safety buffer of 5%. If a match is found, the new object uses that existing lease. If not, a new lease is created and added to the pool for others to share.

### [3.4. Effects of disk latency on etcd](#etcd-disk-latency_etcd-performance) Copy linkLink copied to clipboard!

etcd performance depends heavily on disk latency for fsync operations. Validate storage with `fio` before deployment so you avoid instability, failed writes, and service-affecting control plane events.

An etcd cluster is sensitive to disk latencies. To understand the disk latency that is experienced by etcd in your control plane environment, run the `fio` tests or suite.

Ensure that the final report classifies the disk as appropriate for etcd, as shown in the following example:

```
...
99th percentile of fsync is 5865472 ns
99th percentile of the fsync is within the recommended threshold: - 20 ms, the disk can be used to host etcd
```

When a high latency disk is used, a message states that the disk is not recommended for etcd, as shown in the following example:

```
...
99th percentile of fsync is 15865472 ns
99th percentile of the fsync is greater than the recommended value which is 20 ms, faster disks are recommended to host etcd for better performance
```

When you use cluster deployments that span multiple data centers that are using disks for etcd that do not meet the recommended latency, it increases the chances of service-affecting failures and dramatically reduces the network latency that the control plane can sustain.

### [3.5. Monitoring consensus latency for etcd](#etcd-consensus-latency_etcd-performance) Copy linkLink copied to clipboard!

Use the `etcdctl` command-line interface (CLI) to check endpoint health and consensus latency on a running cluster. Regular monitoring helps you spot delays before they cause leader elections and Kubernetes API instability.

By using the `etcdctl` CLI, you can monitor the latency for reaching consensus as experienced by etcd. You must identify one of the etcd pods and then retrieve the endpoint health.

This procedure, which validates and monitors cluster health, can be run only on an active cluster.

**Prerequisites**

* During planning for cluster deployment, you completed the disk and network tests.

**Procedure**

1. Enter the following command:

   ```
   # oc get pods -n openshift-etcd -l app=etcd
   ```

   **Example output**

   ```
   NAME      READY   STATUS    RESTARTS   AGE
   etcd-m0   4/4     Running   4          8h
   etcd-m1   4/4     Running   4          8h
   etcd-m2   4/4     Running   4          8h
   ```
2. Enter the following command. To better understand the etcd latency for consensus, run this command on a precise watch cycle for a few minutes. Observe that the numbers remain below the ~66 ms threshold. The closer the consensus time is to 100 ms, the more likely the cluster experiences service-affecting events and instability.

   ```
   # oc exec -ti etcd-m0 -- etcdctl endpoint health -w table
   ```

   **Example output**

   ```
   +----------------------------+--------+-------------+-------+
   |          ENDPOINT          | HEALTH |    TOOK     | ERROR |
   +----------------------------+--------+-------------+-------+
   | https://198.18.111.12:2379 |   true |  3.798349ms |       |
   | https://198.18.111.14:2379 |   true |  7.389608ms |       |
   | https://198.18.111.13:2379 |   true |  6.263117ms |       |
   +----------------------------+--------+-------------+-------+
   ```
3. Enter the following command:

   ```
   # oc exec -ti etcd-m0 -- watch -dp -c etcdctl endpoint health -w table
   ```

   **Example output**

   ```
   +----------------------------+--------+-------------+-------+
   |          ENDPOINT          | HEALTH |    TOOK     | ERROR |
   +----------------------------+--------+-------------+-------+
   | https://198.18.111.12:2379 |   true |  9.533405ms |       |
   | https://198.18.111.13:2379 |   true |  4.628054ms |       |
   | https://198.18.111.14:2379 |   true |  5.803378ms |       |
   +----------------------------+--------+-------------+-------+
   ```

### [3.6. Moving etcd to a different disk](#move-etcd-different-disk_etcd-performance) Copy linkLink copied to clipboard!

Move etcd data from a shared disk to a dedicated disk to resolve or prevent performance problems. Isolating etcd storage reduces latency from competing I/O on the control plane.

You can move etcd from a shared disk to a separate disk to prevent or resolve performance issues.

The Machine Config Operator (MCO) is responsible for mounting a secondary disk for OpenShift Container Platform 4.22 container storage.

Note

This encoded script only supports device names for the following device types:

* SCSI or SATA: `/dev/sd*`
* Virtual device: `/dev/vd*`
* NVMe: `/dev/nvme*[0-9]*n*`

When the new disk is attached to the cluster, the etcd database is part of the root mount. It is not part of the secondary disk or the intended disk when the primary node is recreated. As a result, the primary node does not create a separate `/var/lib/etcd` mount.

**Prerequisites**

* You have a backup of your cluster’s etcd data.
* You have installed the OpenShift CLI (`oc`).
* You have access to the cluster with `cluster-admin` privileges.
* You have attached additional disks before uploading the machine configuration.
* The `MachineConfigPool` matches `metadata.labels[machineconfiguration.openshift.io/role]`. This applies to a controller, worker, or a custom pool.

Note

This procedure does not move parts of the root file system, such as `/var/`, to another disk or partition on an installed node.

Important

This procedure is not supported when using control plane machine sets.

**Procedure**

1. Attach the new disk to the cluster and verify that the disk is detected in the node by running the `lsblk` command in a debug shell:

   ```
   $ oc debug node/<node_name>
   ```

   ```
   # lsblk
   ```

   Note the device name of the new disk reported by the `lsblk` command.
2. Create the following script and name it `etcd-find-secondary-device.sh`:

   ```
   #!/bin/bash
   set -uo pipefail

   for device in <device_type_glob>; do
   /usr/sbin/blkid "${device}" &> /dev/null
    if [ $? == 2  ]; then
       echo "secondary device found ${device}"
       echo "creating filesystem for etcd mount"
       mkfs.xfs -L var-lib-etcd -f "${device}" &> /dev/null
       udevadm settle
       touch /etc/var-lib-etcd-mount
       exit
    fi
   done
   echo "Couldn't find secondary block device!" >&2
   exit 77
   ```

   Replace `<device_type_glob>` with a shell glob for your block device type. For SCSI or SATA drives, use `/dev/sd*`; for virtual drives, use `/dev/vd*`; for NVMe drives, use `/dev/nvme*[0-9]*n*`.
3. Create a base64-encoded string from the `etcd-find-secondary-device.sh` script and note its contents:

   ```
   $ base64 -w0 etcd-find-secondary-device.sh
   ```
4. Create a `MachineConfig` YAML file named `etcd-mc.yml` with contents such as the following example:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: master
     name: 98-var-lib-etcd
   spec:
     config:
       ignition:
         version: 3.5.0
       storage:
         files:
           - path: /etc/find-secondary-device
             mode: 0755
             contents:
               source: data:text/plain;charset=utf-8;base64,<encoded_etcd_find_secondary_device_script>
       systemd:
         units:
           - name: find-secondary-device.service
             enabled: true
             contents: |
               [Unit]
               Description=Find secondary device
               DefaultDependencies=false
               After=systemd-udev-settle.service
               Before=local-fs-pre.target
               ConditionPathExists=!/etc/var-lib-etcd-mount

               [Service]
               RemainAfterExit=yes
               ExecStart=/etc/find-secondary-device

               RestartForceExitStatus=77

               [Install]
               WantedBy=multi-user.target
           - name: var-lib-etcd.mount
             enabled: true
             contents: |
               [Unit]
               Before=local-fs.target

               [Mount]
               What=/dev/disk/by-label/var-lib-etcd
               Where=/var/lib/etcd
               Type=xfs
               TimeoutSec=120s

               [Install]
               RequiredBy=local-fs.target
           - name: sync-var-lib-etcd-to-etcd.service
             enabled: true
             contents: |
               [Unit]
               Description=Sync etcd data if new mount is empty
               DefaultDependencies=no
               After=var-lib-etcd.mount var.mount
               Before=crio.service

               [Service]
               Type=oneshot
               RemainAfterExit=yes
               ExecCondition=/usr/bin/test ! -d /var/lib/etcd/member
               ExecStart=/usr/sbin/setsebool -P rsync_full_access 1
               ExecStart=/bin/rsync -ar /sysroot/ostree/deploy/rhcos/var/lib/etcd/ /var/lib/etcd/
               ExecStart=/usr/sbin/semanage fcontext -a -t container_var_lib_t '/var/lib/etcd(/.*)?'
               ExecStart=/usr/sbin/setsebool -P rsync_full_access 0
               TimeoutSec=0

               [Install]
               WantedBy=multi-user.target graphical.target
           - name: restorecon-var-lib-etcd.service
             enabled: true
             contents: |
               [Unit]
               Description=Restore recursive SELinux security contexts
               DefaultDependencies=no
               After=var-lib-etcd.mount
               Before=crio.service

               [Service]
               Type=oneshot
               RemainAfterExit=yes
               ExecStart=/sbin/restorecon -R /var/lib/etcd/
               TimeoutSec=0

               [Install]
               WantedBy=multi-user.target graphical.target
   ```

   Replace `<encoded_etcd_find_secondary_device_script>` with the encoded script contents that you noted.
5. Apply the created `MachineConfig` YAML file:

   ```
   $ oc create -f etcd-mc.yml
   ```

**Verification**

* Run the `grep /var/lib/etcd /proc/mounts` command in a debug shell for the node to ensure that the disk is mounted:

  ```
  $ oc debug node/<node_name>
  ```

  ```
  # grep -w "/var/lib/etcd" /proc/mounts
  ```

  **Example output**

  ```
  /dev/sdb /var/lib/etcd xfs rw,seclabel,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota 0 0
  ```

### [3.7. Data defragmentation for etcd](#etcd-defrag_etcd-performance) Copy linkLink copied to clipboard!

To prevent etcd performance degradation and cluster-wide maintenance alarms on large clusters, monitor etcd database metrics and defragment the data store when the keyspace grows too large.

For large and dense clusters, etcd can suffer from poor performance if the keyspace grows too large and exceeds the space quota. Periodically maintain and defragment etcd to free up space in the data store. Monitor Prometheus for etcd metrics and defragment it when required. Otherwise, etcd can raise a cluster-wide alarm that puts the cluster into a maintenance mode, which accepts only key reads and deletes.

Monitor these key metrics:

* `etcd_server_quota_backend_bytes`, which is the current quota limit
* `etcd_mvcc_db_total_size_in_use_in_bytes`, which indicates the actual database usage after a history compaction
* `etcd_mvcc_db_total_size_in_bytes`, which shows the database size, including free space waiting for defragmentation

Defragment etcd data to reclaim disk space after events that cause disk fragmentation, such as etcd history compaction.

History compaction is performed automatically every five minutes and leaves gaps in the back-end database. This fragmented space is available for use by etcd, but is not available to the host file system. You must defragment etcd to make this space available to the host file system.

Defragmentation occurs automatically, but you can also trigger it manually.

#### [3.7.1. Automatic defragmentation](#automatic-defrag-etcd-data_etcd-performance) Copy linkLink copied to clipboard!

When etcd database growth affects performance, the etcd Operator can automatically defragment member disks based on cluster metrics.

Note

Automatic defragmentation works well in most cases because the etcd Operator uses cluster metrics to choose the most efficient defragmentation approach.

The etcd Operator automatically defragments disks. No manual intervention is needed.

Verify that defragmentation succeeded by checking one of these logs:

* etcd logs
* cluster-etcd-operator pod
* operator status error log

Warning

Automatic defragmentation can cause leader election failure in various OpenShift Container Platform core components, such as the Kubernetes controller manager, which triggers a restart of the failing component. The restart is harmless and either triggers failover to the next running instance or the component resumes work again after the restart.

The following is example log output for successful defragmentation:

```
etcd member has been defragmented: <member_name>, memberID: <member_id>
```

The following is example log output for unsuccessful defragmentation:

```
failed defrag on member: <member_name>, memberID: <member_id>: <error_message>
```

#### [3.7.2. Manually defragmenting etcd data](#manual-defrag-etcd-data_etcd-performance) Copy linkLink copied to clipboard!

When automatic etcd defragmentation cannot reclaim enough space, manually defragment etcd on each member to restore disk availability and normal cluster operation.

A Prometheus alert indicates when you need to use manual defragmentation. The alert is displayed in two cases:

* When etcd uses more than 50% of its available space for more than 10 minutes
* When etcd is actively using less than 50% of its total database size for more than 10 minutes

You can also determine whether defragmentation is needed by checking the etcd database size in MB that will be freed by defragmentation with the PromQL expression: `(etcd_mvcc_db_total_size_in_bytes - etcd_mvcc_db_total_size_in_use_in_bytes)/1024/1024`

Warning

Defragmenting etcd is a blocking action. The etcd member does not respond until defragmentation is complete. For this reason, wait at least one minute between defragmentation actions on each of the pods to allow the cluster to recover.

Follow this procedure to defragment etcd data on each etcd member.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Determine which etcd member is the leader, because the leader should be defragmented last.

   1. Get the list of etcd pods:

      ```
      $ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
      ```

      The following is example output:

      ```
      etcd-ip-10-0-159-225.example.redhat.com                3/3     Running     0          175m   10.0.159.225   ip-10-0-159-225.example.redhat.com   <none>           <none>
      etcd-ip-10-0-191-37.example.redhat.com                 3/3     Running     0          173m   10.0.191.37    ip-10-0-191-37.example.redhat.com    <none>           <none>
      etcd-ip-10-0-199-170.example.redhat.com                3/3     Running     0          176m   10.0.199.170   ip-10-0-199-170.example.redhat.com   <none>           <none>
      ```
   2. Choose a pod and run the following command to determine which etcd member is the leader:

      ```
      $ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com etcdctl endpoint status --cluster -w table
      ```

      The following is example output:

      ```
      Defaulting container name to etcdctl.
      Use 'oc describe pod/etcd-ip-10-0-159-225.example.redhat.com -n openshift-etcd' to see all of the containers in this pod.
      +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
      |         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
      +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
      |  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
      | https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
      | https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
      +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
      ```

      Based on the `IS LEADER` column of this output, the `https://10.0.199.170:2379` endpoint is the leader. Matching this endpoint with the output of the previous step, the pod name of the leader is `etcd-ip-10-0-199-170.example.redhat.com`.
2. Defragment an etcd member.

   1. Connect to the running etcd container, passing in the name of a pod that is *not* the leader:

      ```
      $ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com
      ```
   2. Unset the `ETCDCTL_ENDPOINTS` environment variable:

      ```
      sh-4.4# unset ETCDCTL_ENDPOINTS
      ```
   3. Defragment the etcd member:

      ```
      sh-4.4# etcdctl --command-timeout=30s --endpoints=https://localhost:2379 defrag
      ```

      The following is example output:

      ```
      Finished defragmenting etcd member[https://localhost:2379]
      ```

      If a timeout error occurs, increase the value for `--command-timeout` until the command succeeds.
   4. Verify that the database size was reduced:

      ```
      sh-4.4# etcdctl endpoint status -w table --cluster
      ```

      The following is example output:

      ```
      +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
      |         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
      +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
      |  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
      | https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |   41 MB |     false |      false |         7 |      91624 |              91624 |        |
      ```

      1

      ```
      | https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
      +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
      ```

      This example shows that the database size for this etcd member is now 41 MB as opposed to the starting size of 104 MB.
   5. Repeat these steps to connect to each of the other etcd members and defragment them. Always defragment the leader last.

      Wait at least one minute between defragmentation actions to allow the etcd pod to recover. Until the etcd pod recovers, the etcd member does not respond.
3. If any `NOSPACE` alarms were triggered due to the space quota being exceeded, clear them.

   1. Check if there are any `NOSPACE` alarms:

      ```
      sh-4.4# etcdctl alarm list
      ```

      The following is example output:

      ```
      memberID:12345678912345678912 alarm:NOSPACE
      ```
   2. Clear the alarms:

      ```
      sh-4.4# etcdctl alarm disarm
      ```

### [3.8. Setting tuning parameters for etcd](#etcd-tuning-parameters_etcd-performance) Copy linkLink copied to clipboard!

Configure the control plane hardware speed setting for etcd to match your environment’s latency.

You can set the control plane hardware speed to `"Standard"` or `"Slower"`, or use the default, which is `""`.

The default setting allows the system to decide the speed to use. This value enables upgrades from versions where this feature does not exist, as the system can select values from previous versions.

By selecting one of the other values, you are overriding the default. If you see many leader elections due to timeouts or missed heartbeats, and your system is set to `""` or `"Standard"`, set the hardware speed to `"Slower"`. This change makes the system more tolerant to the increased latency.

**Procedure**

1. Check to see what the current value is by entering the following command:

   ```
   $ oc describe etcd/cluster | grep "Control Plane Hardware Speed"
   ```

   **Example output**

   ```
   Control Plane Hardware Speed:  <VALUE>
   ```

   Note

   If the output is empty, the field has not been set and should be considered as the default ("").
2. Change the value by entering the following command. Replace `<value>` with one of the valid values: `""`, `"Standard"`, or `"Slower"`:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"controlPlaneHardwareSpeed": "<value>"}}'
   ```

   The following table indicates the heartbeat interval and leader election timeout for each profile. These values are subject to change.

   Expand

   Table 3.2. Heartbeat interval and leader election timeout by hardware speed profile

   |  |  |  |
   | --- | --- | --- |
   | Profile | ETCD\_HEARTBEAT\_INTERVAL | ETCD\_LEADER\_ELECTION\_TIMEOUT |
   | `""` | Varies depending on platform | Varies depending on platform |
   | `Standard` | 100 | 1000 |
   | `Slower` | 500 | 2500 |

   Show more
3. Review the output:

   **Example output**

   ```
   etcd.operator.openshift.io/cluster patched
   ```

   If you enter any value besides the valid values, error output is displayed. For example, if you entered `"Faster"` as the value, the output is as follows:

   **Example output**

   ```
   The Etcd "cluster" is invalid: spec.controlPlaneHardwareSpeed: Unsupported value: "Faster": supported values: "", "Standard", "Slower"
   ```
4. Verify that the value was changed by entering the following command:

   ```
   $ oc describe etcd/cluster | grep "Control Plane Hardware Speed"
   ```

   **Example output**

   ```
   Control Plane Hardware Speed:  ""
   ```
5. Wait for etcd pods to roll out:

   ```
   $ oc get pods -n openshift-etcd -w
   ```

   The following output shows the expected entries for the `main-0` control plane node. Before you continue, wait until all control plane nodes show a status of `4/4 Running`.

   **Example output**

   ```
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Pending             0          0s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Pending             0          0s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     ContainerCreating   0          0s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     ContainerCreating   0          1s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           1/1     Running             0          2s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          34s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          36s
   installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          36s
   etcd-guard-ci-ln-qkgs94t-72292-9clnd-main-0            0/1     Running             0          26m
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Terminating         0          11m
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Terminating         0          11m
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Pending             0          0s
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Init:1/3            0          1s
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Init:2/3            0          2s
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     PodInitializing     0          3s
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  3/4     Running             0          4s
   etcd-guard-ci-ln-qkgs94t-72292-9clnd-main-0            1/1     Running             0          26m
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  3/4     Running             0          20s
   etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Running             0          20s
   ```
6. Enter the following command to review to the values:

   ```
   $ oc describe -n openshift-etcd pod/<ETCD_PODNAME> | grep -e HEARTBEAT_INTERVAL -e ELECTION_TIMEOUT
   ```

   Note

   These values might not have changed from the default.

### [3.9. OpenShift Container Platform timer tunables for etcd](#etcd-timer-tunables_etcd-performance) Copy linkLink copied to clipboard!

OpenShift Container Platform sets platform-specific etcd election timeout and heartbeat interval values. Knowing these tunables helps you align network and disk requirements with expected cluster behavior.

OpenShift Container Platform maintains etcd timers that are optimized for each platform. OpenShift Container Platform has prescribed validated values that are optimized for each platform provider. The default etcd timers with `platform=none` or `platform=metal` are as follows:

```
- name: ETCD_ELECTION_TIMEOUT
  value: "1000"
  ...
- name: ETCD_HEARTBEAT_INTERVAL
  value: "100"
```

From an etcd perspective, the two key values are election timeout and heartbeat interval:

Heartbeat interval
:   The frequency with which the leader notifies followers that it is still the leader.

Election timeout
:   This timeout is how long a follower node will go without hearing a heartbeat before it attempts to become leader itself.

These values do not provide the whole story for the control plane or even etcd. An etcd cluster is sensitive to disk latencies. Because etcd must persist proposals to its log, disk activity from other processes might cause long fsync latencies. The consequence is that etcd might miss heartbeats, causing request timeouts and temporary leader loss. During a leader loss and reelection, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.

### [3.10. Determining the size of the etcd database and understanding its effects](#etcd-database-size_etcd-performance) Copy linkLink copied to clipboard!

etcd database size affects defragmentation duration, resync time after network partitions, and transaction rates. Plan capacity so maintenance and recovery do not degrade cluster stability.

The size of the etcd database has a direct impact on the time to complete the etcd defragmentation process. OpenShift Container Platform automatically runs the etcd defragmentation on one etcd member at a time when it detects at least 45% fragmentation. During the defragmentation process, the etcd member cannot process any requests. On small etcd databases, the defragmentation process happens in less than a second. With larger etcd databases, the disk latency directly impacts the fragmentation time, causing additional latency, as operations are blocked while defragmentation happens.

The size of the etcd database is a factor to consider when network partitions isolate a control plane node for a period and the control plane needs to resync after communication is re-established.

Minimal options exist for controlling the size of the etcd database, as it depends on the operators and applications in the system. When you consider the latency range under which the system will operate, account for the effects of synchronization or defragmentation per size of the etcd database.

The magnitude of the effects is specific to the deployment. The time to complete a defragmentation will cause degradation in the transaction rate, as the etcd member cannot accept updates during the defragmentation process. Similarly, the time for the etcd re-synchronization for large databases with high change rate affects the transaction rate and transaction latency on the system.

Consider the following two examples for the type of impacts to plan for.

Example of the effect of etcd defragmentation based on database size
:   Writing an etcd database of 1 GB to a slow 7200 RPMs disk at 80 Mbits/sec takes about 1 minute and 40 seconds. In such a scenario, the defragmentation process takes at least this long, if not longer, to complete the defragmentation.

Example of the effect of database size on etcd synchronization
:   If there is a change of 10% of the etcd database during the disconnection of one of the control plane nodes, the resync needs to transfer at least 100 MB. Transferring 100 MB over a 1 Gbps link takes 800 ms. On clusters with regular transactions with the Kubernetes API, the larger the etcd database size, the more network instabilities will cause control plane instabilities.

You can determine the size of an etcd database by using the OpenShift Container Platform console or by running commands in the `etcdctl` tool.

**Procedure**

* To find the database size in the OpenShift Container Platform console, go to the **etcd** dashboard to view a plot that reports the size of the etcd database.
* To find the database size by using the `etcdctl` tool, enter the following commands:

  1. Enter the following command to list the pods:

     ```
     # oc get pods -n openshift-etcd -l app=etcd
     ```

     **Example output**

     ```
     NAME      READY   STATUS    RESTARTS   AGE
     etcd-m0   4/4     Running   4          22h
     etcd-m1   4/4     Running   4          22h
     etcd-m2   4/4     Running   4          22h
     ```
  2. Enter the following command and view the database size in the output:

     ```
     # oc exec -t etcd-m0 -- etcdctl endpoint status -w simple | cut -d, -f 1,3,4
     ```

     **Example output**

     ```
     https://198.18.111.12:2379, 3.5.6, 1.1 GB
     https://198.18.111.13:2379, 3.5.6, 1.1 GB
     https://198.18.111.14:2379, 3.5.6, 1.1 GB
     ```

### [3.11. Increasing the database size for etcd](#etcd-increase-db_etcd-performance) Copy linkLink copied to clipboard!

Increase the etcd disk quota when low space or excessive growth alerts appear. Expanding the quota before etcd runs out of space prevents write failures and cluster instability.

You can set the disk quota in gibibytes (GiB) for each etcd instance. If you set a disk quota for your etcd instance, you can specify integer values from 8 to 32. The default value is 8. You can specify only increasing values.

You might want to increase the disk quota if you encounter a `low space` alert. This alert indicates that the cluster is too large to fit in etcd despite automatic compaction and defragmentation. If you see this alert, you need to increase the disk quota immediately because after etcd runs out of space, writes fail.

Another scenario where you might want to increase the disk quota is if you encounter an `excessive database growth` alert. This alert is a warning that the database might grow too large in the next four hours. In this scenario, consider increasing the disk quota so that you do not eventually encounter a `low space` alert and possible write fails.

If you increase the disk quota, the disk space that you specify is not immediately reserved. Instead, etcd can grow to that size if needed. Ensure that etcd is running on a dedicated disk that is larger than the value that you specify for the disk quota.

For large etcd databases, the control plane nodes must have additional memory and storage. Because you must account for the API server cache, the minimum memory required is at least three times the configured size of the etcd database.

Important

Increasing the database size for etcd is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Procedure**

1. Check the current value of the disk quota for each etcd instance by entering the following command:

   ```
   $ oc describe etcd/cluster | grep "Backend Quota"
   ```

   **Example output**

   ```
   Backend Quota Gi B: <value>
   ```
2. Change the value of the disk quota by entering the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": <value>}}'
   ```

   **Example output**

   ```
   etcd.operator.openshift.io/cluster patched
   ```

**Verification**

1. Verify that the new value for the disk quota is set by entering the following command:

   ```
   $ oc describe etcd/cluster | grep "Backend Quota"
   ```

   The etcd Operator automatically rolls out the etcd instances with the new values.
2. Verify that the etcd pods are up and running by entering the following command:

   ```
   $ oc get pods -n openshift-etcd
   ```

   The following output shows the expected entries.

   **Example output**

   ```
   NAME                                                   READY   STATUS      RESTARTS   AGE
   etcd-ci-ln-b6kfsw2-72292-mzwbq-master-0                4/4     Running     0          39m
   etcd-ci-ln-b6kfsw2-72292-mzwbq-master-1                4/4     Running     0          37m
   etcd-ci-ln-b6kfsw2-72292-mzwbq-master-2                4/4     Running     0          41m
   etcd-guard-ci-ln-b6kfsw2-72292-mzwbq-master-0          1/1     Running     0          51m
   etcd-guard-ci-ln-b6kfsw2-72292-mzwbq-master-1          1/1     Running     0          49m
   etcd-guard-ci-ln-b6kfsw2-72292-mzwbq-master-2          1/1     Running     0          54m
   installer-5-ci-ln-b6kfsw2-72292-mzwbq-master-1         0/1     Completed   0          51m
   installer-7-ci-ln-b6kfsw2-72292-mzwbq-master-0         0/1     Completed   0          46m
   installer-7-ci-ln-b6kfsw2-72292-mzwbq-master-1         0/1     Completed   0          44m
   installer-7-ci-ln-b6kfsw2-72292-mzwbq-master-2         0/1     Completed   0          49m
   installer-8-ci-ln-b6kfsw2-72292-mzwbq-master-0         0/1     Completed   0          40m
   installer-8-ci-ln-b6kfsw2-72292-mzwbq-master-1         0/1     Completed   0          38m
   installer-8-ci-ln-b6kfsw2-72292-mzwbq-master-2         0/1     Completed   0          42m
   revision-pruner-7-ci-ln-b6kfsw2-72292-mzwbq-master-0   0/1     Completed   0          43m
   revision-pruner-7-ci-ln-b6kfsw2-72292-mzwbq-master-1   0/1     Completed   0          43m
   revision-pruner-7-ci-ln-b6kfsw2-72292-mzwbq-master-2   0/1     Completed   0          43m
   revision-pruner-8-ci-ln-b6kfsw2-72292-mzwbq-master-0   0/1     Completed   0          42m
   revision-pruner-8-ci-ln-b6kfsw2-72292-mzwbq-master-1   0/1     Completed   0          42m
   revision-pruner-8-ci-ln-b6kfsw2-72292-mzwbq-master-2   0/1     Completed   0          42m
   ```
3. Verify that the disk quota value is updated for the etcd pod by entering the following command:

   ```
   $ oc describe -n openshift-etcd pod/<etcd_podname> | grep "ETCD_QUOTA_BACKEND_BYTES"
   ```

   The value might not have changed from the default value of `8`.

   **Example output**

   ```
   ETCD_QUOTA_BACKEND_BYTES:                               8589934592
   ```

   Note

   While the value that you set is an integer in GiB, the value shown in the output is converted to bytes.

### [3.12. Troubleshooting etcd database size increases](#etcd-increase-db-troubleshooting_etcd-performance) Copy linkLink copied to clipboard!

Resolve common errors when increasing the etcd disk quota, including values that are too small, too large, or lower than the current setting.

If you encounter issues when you try to increase the database size for etcd, the following examples might help.

#### [3.12.1. Value is too small](#etcd-ts-db-small_etcd-performance) Copy linkLink copied to clipboard!

If the value that you specify is less than `8`, you see an error message. For example, if you enter the following command:

```
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 5}}'
```

The following error message is displayed:

**Example error message**

```
The Etcd "cluster" is invalid:
* spec.backendQuotaGiB: Invalid value: 5: spec.backendQuotaGiB in body should be greater than or equal to 8
* spec.backendQuotaGiB: Invalid value: "integer": etcd backendQuotaGiB may not be decreased
```

To resolve this issue, specify an integer between `8` and `32`.

#### [3.12.2. Value is too large](#etcd-ts-db-large_etcd-performance) Copy linkLink copied to clipboard!

If the value that you specify is greater than `32`, you see an error message. For example, if you enter the following command:

```
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 64}}'
```

The following error message is displayed:

**Example error message**

```
The Etcd "cluster" is invalid: spec.backendQuotaGiB: Invalid value: 64: spec.backendQuotaGiB in body should be less than or equal to 32
```

To resolve this issue, specify an integer between `8` and `32`.

#### [3.12.3. Value is decreasing](#etcd-ts-db-decrease_etcd-performance) Copy linkLink copied to clipboard!

If the value is set to a valid value between `8` and `32`, you cannot decrease the value. Otherwise, you see an error message.

For example, check the current value by entering the following command:

```
$ oc describe etcd/cluster | grep "Backend Quota"
```

**Example output**

```
Backend Quota Gi B: 10
```

If you decrease the disk quota value by entering the following command, an error message is displayed.

```
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 8}}'
```

**Example error message**

```
The Etcd "cluster" is invalid: spec.backendQuotaGiB: Invalid value: "integer": etcd backendQuotaGiB may not be decreased
```

To resolve this issue, specify an integer greater than `10`.

### [3.13. Measuring network jitter between control plane nodes](#etcd-network-latency-jitter_etcd-performance) Copy linkLink copied to clipboard!

Measure network jitter between control plane nodes to validate latency for etcd heartbeats. High jitter causes missed heartbeats, leader loss, and Kubernetes API request failures.

The value of the heartbeat interval should be around the maximum of the average round-trip time (RTT) between members, normally around 1.5 times the RTT. With the OpenShift Container Platform default heartbeat interval of 100 ms, the recommended RTT between control plane nodes is less than approximately 33 ms. The maximum RTT should be less than 66 ms (66 ms multiplied by 1.5 equals 99 ms). For more information, see "Setting tuning parameters for etcd". Any network latency that is higher might cause service-affecting events and cluster instability.

The network latency is influenced by many factors, including but not limited to the following factors:

* The technology of the transport networks, such as copper, fiber, wireless, or satellite
* The number and quality of the network devices in the transport network

A good evaluation reference is the comparison of the network latency in the organization with the commercial latencies that are published by telecommunications providers, such as monthly IP latency statistics.

Consider network latency with network jitter for more accurate calculations. *Network jitter* is the variance in network latency or, more specifically, the variation in the delay of received packets. On ideal network conditions, the jitter is as close to zero as possible. Network jitter affects the network latency calculations for etcd because the actual network latency over time will be the RTT plus or minus jitter. For example, a network with a maximum latency of 80 ms and jitter of 30 ms will experience latencies of 110 ms, which means etcd is missing heartbeats, causing request timeouts and temporary leader loss. During a leader loss and reelection, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.

It is important to measure the network jitter among all control plane nodes. To do so, you can use the `iPerf3` tool in UDP mode.

**Prerequisite**

* You built your own `iPerf` image. For more information, see the following Red Hat Knowledgebase articles:

  + [Testing Network Bandwidth in OpenShift using iPerf Container](https://access.redhat.com/articles/5233541)
  + [How to run iPerf network performance test in OpenShift 4](https://access.redhat.com/solutions/6129701)

**Procedure**

1. Connect to one of the control plane nodes and run the `iPerf` container as `iPerf` server in host network mode. When you are running in server mode, the tool accepts TCP and UDP tests. Enter the following command, being careful to replace `<iperf_image>` with your `iPerf` image:

   ```
   # podman run -ti --rm --net host <iperf_image> iperf3 -s
   ```
2. Connect to another control plane node and run the `iPerf3` tool in UDP client mode by entering the following command:

   ```
   # podman run -ti --rm --net host <iperf_image> iperf3 -u -c <node_iperf_server> -t 300
   ```

   The default test runs for 10 seconds, and at the end, the client output shows the average jitter from the client perspective.
3. Run the debug node mode by entering the following command:

   ```
   # oc debug node/m1
   ```

   **Example output**

   ```
   Starting pod/m1-debug ...
   To use host binaries, run `chroot /host`
   Pod IP: 198.18.111.13
   If you do not see a command prompt, try pressing Enter.
   ```
4. Enter the following commands:

   ```
   sh-4.4# chroot /host
   ```

   ```
   sh-4.4# podman run -ti --rm --net host <iperf_image> iperf3 -u -c m0
   ```

   **Example output**

   ```
   Connecting to host m0, port 5201
   [  5] local 198.18.111.13 port 60878 connected to 198.18.111.12 port 5201
   [ ID] Interval           Transfer     Bitrate         Total Datagrams
   [  5]   0.00-1.00   sec   129 KBytes  1.05 Mbits/sec  91
   [  5]   1.00-2.00   sec   127 KBytes  1.04 Mbits/sec  90
   [  5]   2.00-3.00   sec   129 KBytes  1.05 Mbits/sec  91
   [  5]   3.00-4.00   sec   129 KBytes  1.05 Mbits/sec  91
   [  5]   4.00-5.00   sec   127 KBytes  1.04 Mbits/sec  90
   [  5]   5.00-6.00   sec   129 KBytes  1.05 Mbits/sec  91
   [  5]   6.00-7.00   sec   127 KBytes  1.04 Mbits/sec  90
   [  5]   7.00-8.00   sec   129 KBytes  1.05 Mbits/sec  91
   [  5]   8.00-9.00   sec   127 KBytes  1.04 Mbits/sec  90
   [  5]   9.00-10.00  sec   129 KBytes  1.05 Mbits/sec  91
   - - - - - - - - - - - - - - - - - - - - - - - - -
   [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
   [  5]   0.00-10.00  sec  1.25 MBytes  1.05 Mbits/sec  0.000 ms  0/906 (0%)  sender
   [  5]   0.00-10.04  sec  1.25 MBytes  1.05 Mbits/sec  1.074 ms  0/906 (0%)  receiver

   iperf Done.
   ```
5. On the `iPerf` server, the output shows the jitter on every second interval. The average is shown at the end. For the purpose of this test, you want to identify the maximum jitter that is experienced during the test, ignoring the output of the first second as it might contain an invalid measurement. Enter the following command:

   ```
   # oc debug node/m0
   ```

   **Example output**

   ```
   Starting pod/m0-debug ...
   To use host binaries, run `chroot /host`
   Pod IP: 198.18.111.12
   If you do not see a command prompt, try pressing Enter.
   ```
6. Enter the following commands:

   ```
   sh-4.4# chroot /host
   ```

   ```
   sh-4.4# podman run -ti --rm --net host <iperf_image> iperf3 -s
   ```

   **Example output**

   ```
   -----------------------------------------------------------
   Server listening on 5201
   -----------------------------------------------------------
   Accepted connection from 198.18.111.13, port 44136
   [  5] local 198.18.111.12 port 5201 connected to 198.18.111.13 port 60878
   [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
   [  5]   0.00-1.00   sec   124 KBytes  1.02 Mbits/sec  4.763 ms  0/88 (0%)
   [  5]   1.00-2.00   sec   127 KBytes  1.04 Mbits/sec  4.735 ms  0/90 (0%)
   [  5]   2.00-3.00   sec   129 KBytes  1.05 Mbits/sec  0.568 ms  0/91 (0%)
   [  5]   3.00-4.00   sec   127 KBytes  1.04 Mbits/sec  2.443 ms  0/90 (0%)
   [  5]   4.00-5.00   sec   129 KBytes  1.05 Mbits/sec  1.372 ms  0/91 (0%)
   [  5]   5.00-6.00   sec   127 KBytes  1.04 Mbits/sec  2.769 ms  0/90 (0%)
   [  5]   6.00-7.00   sec   129 KBytes  1.05 Mbits/sec  2.393 ms  0/91 (0%)
   [  5]   7.00-8.00   sec   127 KBytes  1.04 Mbits/sec  0.883 ms  0/90 (0%)
   [  5]   8.00-9.00   sec   129 KBytes  1.05 Mbits/sec  0.594 ms  0/91 (0%)
   [  5]   9.00-10.00  sec   127 KBytes  1.04 Mbits/sec  0.953 ms  0/90 (0%)
   [  5]  10.00-10.04  sec  5.66 KBytes  1.30 Mbits/sec  1.074 ms  0/4 (0%)
   - - - - - - - - - - - - - - - - - - - - - - - - -
   [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
   [  5]   0.00-10.04  sec  1.25 MBytes  1.05 Mbits/sec  1.074 ms  0/906 (0%)  receiver
   -----------------------------------------------------------
   Server listening on 5201
   -----------------------------------------------------------
   ```
7. Add the calculated jitter as a penalty to the network latency. For example, if the network latency is 80 ms and the jitter is 30 ms, consider an effective network latency of 110 ms for the purposes of the control plane. In this example, that value goes above the 100 ms threshold, and the system will miss heartbeats.
8. When you calculate the network latency for etcd, use the effective network latency, which is the sum of the following equation:

   RTT + jitter

   You might be able to use the average jitter value to calculate the penalty, but the cluster can sporadically miss heartbeats if the etcd heartbeat timer is lower than the sum of the following equation:

   RTT + max(jitter)

   Instead, consider using the 99th percentile or max jitter value for a more resilient deployment:

   Effective Network Latency = RTT + max(jitter)

### [3.14. How etcd peer round-trip time affects performance](#etcd-peer-round-trip_etcd-performance) Copy linkLink copied to clipboard!

The etcd peer round-trip time (RTT) metric shows replication latency across members, beyond raw network RTT. Monitor it to detect control plane slowdowns before they affect cluster operations.

The etcd peer RTT is an end-to-end test metric on how quickly something can be replicated among members. It shows the latency of etcd to finish replicating a client request among all the etcd members. The etcd peer RTT is not the same thing as the network RTT.

You can monitor various etcd metrics on dashboards in the OpenShift Container Platform console. In the console, click **Observe** → **Dashboards** and from the dropdown list, select **etcd**.

Near the end of the **etcd** dashboard, you can find a plot that summarizes the etcd peer RTT.

Note

These etcd metrics are collected by the OpenShift Container Platform metrics system in Prometheus. You can access them from the CLI by using a Prometheus query. For more information, see the Red Hat Knowledgebase solution, "How to query from the command line Prometheus statistics".

```
# Get token to connect to Prometheus
SECRET=$(oc get secret -n openshift-user-workload-monitoring | grep  prometheus-user-workload-token | head -n 1 | awk '{print $1 }')
export TOKEN=$(oc get secret $SECRET -n openshift-user-workload-monitoring -o json | jq -r '.data.token' | base64 -d)
export THANOS_QUERIER_HOST=$(oc get route thanos-querier -n openshift-monitoring -o json | jq -r '.spec.host')
```

Queries must be URL-encoded. The following example shows how to retrieve the metrics that are reporting the RTT (in seconds) for etcd to finish replicating the client requests among the members:

```
# prometheus query
query="histogram_quantile(0.99, rate(etcd_network_peer_round_trip_time_seconds_bucket[5m]))"

# urlencoded query
encoded_query=$(printf "%s" $query |jq -sRr @uri)

# querying the metrics service
curl -s -X GET -k -H "Authorization: Bearer $TOKEN" "https://$THANOS_QUERIER_HOST/api/v1/query?query=$encoded_query" | jq '.data.result[] | .metric.pod,.value[1]'

"etcd-m2"
"0.09318400000000004"   # example ~93ms
"etcd-m0"
"0.050688"              # example ~51ms
"etcd-m1"
"0.050688"              # example ~51ms
```

The following metrics are also relevant to understanding etcd performance:

`etcd_disk_wal_fsync_duration_seconds_bucket`
:   Reports the etcd write-ahead log (WAL) fsync duration.

`etcd_disk_backend_commit_duration_seconds_bucket`
:   Reports the etcd backend commit latency duration.

`etcd_server_leader_changes_seen_total`
:   Reports the leader changes.

### [3.15. Determining Kubernetes API transaction rate for your environment](#etcd-determine-kube-api-transaction-rate_etcd-performance) Copy linkLink copied to clipboard!

Test sustained Kubernetes API transaction rates for stretched control plane deployments by using `kube-burner-ocp` density profiles. Validate limits before production workloads exceed etcd capacity.

When you are using stretched control planes, the Kubernetes API transaction rate depends on the characteristics of the particular deployment. Specifically, it depends on the following combined factors:

* The etcd disk latency
* The etcd round trip time
* The size of objects that are being written to the API

As a result, when you use stretched control planes, cluster administrators must test the environment to determine the sustained transaction rate that is possible for the environment. The `kube-burner` tool is useful for that purpose. The binary includes a wrapper for testing OpenShift clusters: `kube-burner-ocp`. You can use `kube-burner-ocp` to test cluster or node density.

To test the control plane, `kube-burner-ocp` has three workload profiles: `cluster-density`, `cluster-density-v2`, and `cluster-density-ms`. Each workload profile creates a series of resources that are designed to load the control plane. For more information about each profile, see the `kube-burner-ocp` workload documentation.

**Procedure**

1. Enter a command to create and delete resources. The following example shows a command that creates and deletes resources within 20 minutes:

   ```
   # kube-burner ocp cluster-density-ms --churn-duration 20m --churn-delay 0s --iterations 10 --timeout 30m
   ```
2. The OpenShift Container Platform console provides a dashboard with all the relevant API performance information. To access API performance information, click **Observe** → **Dashboards**. From the **Dashboards** menu, click **API Performance**.
3. During the run, observe the API performance dashboard in the OpenShift Container Platform console by clicking **Observe** → **Dashboards**. From the **Dashboards** menu, click **API Performance**.

   On the dashboard, notice how the control plane responds during load and the 99th percentile transaction rate it can achieve for the execution of various verbs and request rates by read and write. Use this information and the knowledge of your organization’s workload to determine the load that the organization can put in the clusters for the specific stretched control plane deployment.

## [Chapter 4. Backing up and restoring etcd data](#backing-up-and-restoring-etcd-data) Copy linkLink copied to clipboard!

### [4.1. Backing up and restoring etcd data](#etcd-backup) Copy linkLink copied to clipboard!

Back up etcd data regularly and store it in a secure location so you can restore your cluster to a previous state, using a snapshot from the same z-stream release.

As the key-value store for OpenShift Container Platform, etcd persists the state of all resource objects.

Back up the etcd data for your cluster regularly and store it in a secure location, ideally outside the OpenShift Container Platform environment. Do not take an etcd backup before the first certificate rotation completes, which occurs 24 hours after installation, otherwise the backup will contain expired certificates. It is also recommended to take etcd backups during non-peak usage hours because the etcd snapshot has a high I/O cost.

Be sure to take an etcd backup before you update your cluster. Taking a backup before you update is important because when you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.17.5 cluster must use an etcd backup that was taken from 4.17.5.

Important

Back up your cluster’s etcd data by performing a single invocation of the backup script on a control plane host. Do not take a backup for each control plane host.

After you have an etcd backup, you can restore to a previous cluster state.

#### [4.1.1. Backing up etcd data](#backing-up-etcd-data_etcd-backup) Copy linkLink copied to clipboard!

You can back up etcd data by creating an etcd snapshot and saving the static pod resources on a control plane host. This backup preserves the cluster state and provides the resources required to restore etcd at a later time.

Important

Only save a backup from a single control plane host. Do not take a backup from each control plane host in the cluster.

For a Two-Node with Fencing (TNF) setup, follow the steps to back up etcd data on only one node in the cluster. The cluster restore process is driven by data from a single node, so you can perform the etcd backup steps on only one node.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have verified whether the cluster-wide proxy is enabled.

  Tip

  You can check whether the proxy is enabled by reviewing the output of `oc get proxy cluster -o yaml`. The proxy is enabled if the `httpProxy`, `httpsProxy`, and `noProxy` fields have values set.

**Procedure**

1. Start a debug session as root for a control plane node:

   ```
   $ oc debug --as-root node/<node_name>
   ```
2. Change your root directory to `/host` in the debug shell:

   ```
   sh-4.4# chroot /host
   ```
3. If the cluster-wide proxy is enabled, export the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` environment variables by running the following commands:

   ```
   $ export HTTP_PROXY=http://<your_proxy.example.com>:8080
   ```

   ```
   $ export HTTPS_PROXY=https://<your_proxy.example.com>:8080
   ```

   ```
   $ export NO_PROXY=<example.com>
   ```
4. Run the `cluster-backup.sh` script with the path to the directory where you want to save the backup:

   Tip

   The `cluster-backup.sh` script is maintained as a component of the etcd Cluster Operator and is a wrapper around the `etcdctl snapshot save` command.

   ```
   sh-4.4# /usr/local/bin/cluster-backup.sh /home/core/assets/backup
   ```

   **Example script output**

   ```
   found latest kube-apiserver: /etc/kubernetes/static-pod-resources/kube-apiserver-pod-6
   found latest kube-controller-manager: /etc/kubernetes/static-pod-resources/kube-controller-manager-pod-7
   found latest kube-scheduler: /etc/kubernetes/static-pod-resources/kube-scheduler-pod-6
   found latest etcd: /etc/kubernetes/static-pod-resources/etcd-pod-3
   ede95fe6b88b87ba86a03c15e669fb4aa5bf0991c180d3c6895ce72eaade54a1
   etcdctl version: 3.4.14
   API version: 3.4
   {"level":"info","ts":1624647639.0188997,"caller":"snapshot/v3_snapshot.go:119","msg":"created temporary db file","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db.part"}
   {"level":"info","ts":"2021-06-25T19:00:39.030Z","caller":"clientv3/maintenance.go:200","msg":"opened snapshot stream; downloading"}
   {"level":"info","ts":1624647639.0301006,"caller":"snapshot/v3_snapshot.go:127","msg":"fetching snapshot","endpoint":"https://10.0.0.5:2379"}
   {"level":"info","ts":"2021-06-25T19:00:40.215Z","caller":"clientv3/maintenance.go:208","msg":"completed snapshot read; closing"}
   {"level":"info","ts":1624647640.6032252,"caller":"snapshot/v3_snapshot.go:142","msg":"fetched snapshot","endpoint":"https://10.0.0.5:2379","size":"114 MB","took":1.584090459}
   {"level":"info","ts":1624647640.6047094,"caller":"snapshot/v3_snapshot.go:152","msg":"saved","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db"}
   Snapshot saved at /home/core/assets/backup/snapshot_2021-06-25_190035.db
   {"hash":3866667823,"revision":31407,"totalKey":12828,"totalSize":114446336}
   snapshot db and kube resources are successfully saved to /home/core/assets/backup
   ```

   In this example, two files are created in the `/home/core/assets/backup/` directory on the control plane host:

   * `snapshot_<datetimestamp>.db`: This file is the etcd snapshot. The `cluster-backup.sh` script confirms the validity of the snapshot.
   * `static_kuberesources_<datetimestamp>.tar.gz`: This file contains the resources for the static pods. If etcd encryption is enabled, it also contains the encryption keys for the etcd snapshot.

     Note

     If etcd encryption is enabled, store this second file separately from the etcd snapshot for security reasons. However, this file is required to restore from the etcd snapshot.

     The etcd encryption only encrypts values, not keys. This means that resource types, namespaces, and object names are not encrypted.

#### [4.1.2. Creating automated etcd backups](#creating-automated-etcd-backups_etcd-backup) Copy linkLink copied to clipboard!

You can enable automated etcd backups for your cluster by applying a `FeatureGate` and backup custom resources (CRs).

Important

Automating etcd backups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Warning

Enabling the `TechPreviewNoUpgrade` feature set on your cluster prevents minor version updates. The `TechPreviewNoUpgrade` feature set cannot be disabled. Do not enable this feature set on production clusters.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

**Procedure**

1. Create a `FeatureGate` custom resource (CR) file named `enable-tech-preview-no-upgrade.yaml` with the following contents:

   ```
   apiVersion: config.openshift.io/v1
   kind: FeatureGate
   metadata:
     name: cluster
   spec:
     featureSet: TechPreviewNoUpgrade
   ```
2. Apply the CR by running the following command:

   ```
   $ oc apply -f enable-tech-preview-no-upgrade.yaml
   ```

   Applying the `FeatureGate` enables the automated backup APIs. It takes time for the related APIs to become available.
3. Verify that the custom resource definition (CRD) was created by running the following command:

   ```
   $ oc get crd | grep backup
   ```

   **Example output**

   ```
   backups.config.openshift.io 2023-10-25T13:32:43Z
   etcdbackups.operator.openshift.io 2023-10-25T13:32:04Z
   ```

##### [4.1.2.1. Creating a single automated etcd backup](#creating-single-etcd-backup_etcd-backup) Copy linkLink copied to clipboard!

You can create a single automated etcd backup by applying an `EtcdBackup` custom resource (CR). Backup data is stored on either dynamically-provisioned or local storage.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

**Procedure**

1. If dynamically-provisioned storage is available, complete the following steps to create a single automated etcd backup:

   1. Create a persistent volume claim (PVC) named `etcd-backup-pvc.yaml` with contents such as the following example:

      ```
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: etcd-backup-pvc
        namespace: openshift-etcd
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: <storage_amount>
        volumeMode: Filesystem
      ```

      where:

      `<storage_amount>`
      :   Specifies the amount of storage available to the PVC. Adjust this value for your requirements, such as `200Gi`.
   2. Apply the PVC by running the following command:

      ```
      $ oc apply -f etcd-backup-pvc.yaml
      ```
   3. Verify that the PVC was created by running the following command:

      ```
      $ oc get pvc
      ```

      **Example output**

      ```
      NAME              STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
      etcd-backup-pvc   Bound                                                       51s
      ```

      Note

      Dynamic PVCs stay in the `Pending` state until they are mounted.
   4. Create a CR file named `etcd-single-backup.yaml` with contents such as the following example:

      ```
      apiVersion: operator.openshift.io/v1alpha1
      kind: EtcdBackup
      metadata:
        name: etcd-single-backup
        namespace: openshift-etcd
      spec:
        pvcName: <pvc_name>
      ```

      where:

      `<pvc_name>`
      :   Specifies the name of the PVC to save the backup to. Adjust this value according to your environment, such as `etcd-backup-pvc`.
   5. Apply the CR to start a single backup by running the following command:

      ```
      $ oc apply -f etcd-single-backup.yaml
      ```
2. If dynamically-provisioned storage is not available, complete the following steps to create a single automated etcd backup:

   1. Create a `StorageClass` CR file named `etcd-backup-local-storage.yaml` with the following contents:

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
        name: etcd-backup-local-storage
      provisioner: kubernetes.io/no-provisioner
      volumeBindingMode: Immediate
      ```
   2. Apply the `StorageClass` CR by running the following command:

      ```
      $ oc apply -f etcd-backup-local-storage.yaml
      ```
   3. Create a PV named `etcd-backup-pv-fs.yaml` with contents such as the following example:

      ```
      apiVersion: v1
      kind: PersistentVolume
      metadata:
        name: etcd-backup-pv-fs
      spec:
        capacity:
          storage: <storage_amount>
        volumeMode: Filesystem
        accessModes:
        - ReadWriteOnce
        persistentVolumeReclaimPolicy: Retain
        storageClassName: etcd-backup-local-storage
        local:
          path: /mnt
        nodeAffinity:
          required:
            nodeSelectorTerms:
            - matchExpressions:
            - key: kubernetes.io/hostname
               operator: In
               values:
               - <node_name>
      ```

      where:

      `<storage_amount>`
      :   Specifies the amount of storage available to the PV. Adjust this value for your requirements, such as `100Gi`.

      `<node_name>`
      :   Specifies the control plane node to attach this PV to. Replace with the actual node name.
   4. Verify that the PV was created by running the following command:

      ```
      $ oc get pv
      ```

      **Example output**

      ```
      NAME                    CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS                REASON   AGE
      etcd-backup-pv-fs       100Gi      RWO            Retain           Available           etcd-backup-local-storage            10s
      ```
   5. Create a PVC named `etcd-backup-pvc.yaml` with contents such as the following example:

      ```
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: etcd-backup-pvc
        namespace: openshift-etcd
      spec:
        accessModes:
        - ReadWriteOnce
        volumeMode: Filesystem
        resources:
          requests:
            storage: <storage_amount>
      ```

      where:

      `<storage_amount>`
      :   Specifies the amount of storage available to the PVC. Adjust this value for your requirements, such as `10Gi`.
   6. Apply the PVC by running the following command:

      ```
      $ oc apply -f etcd-backup-pvc.yaml
      ```
   7. Create a CR file named `etcd-single-backup.yaml` with contents such as the following example:

      ```
      apiVersion: operator.openshift.io/v1alpha1
      kind: EtcdBackup
      metadata:
        name: etcd-single-backup
        namespace: openshift-etcd
      spec:
        pvcName: <pvc_name>
      ```

      where:

      `<pvc_name>`
      :   Specifies the name of the PVC to save the backup to. Adjust this value according to your environment, such as `etcd-backup-pvc`.
   8. Apply the CR to start a single backup by running the following command:

      ```
      $ oc apply -f etcd-single-backup.yaml
      ```

##### [4.1.2.2. Creating recurring automated etcd backups](#creating-recurring-etcd-backups_etcd-backup) Copy linkLink copied to clipboard!

You can create recurring automated etcd backups by applying a custom resource (CR) that defines a backup schedule and retention policy. Backup data is stored on either dynamically-provisioned or local storage.

Use dynamically-provisioned storage to keep the created etcd backup data in a safe, external location if possible. If dynamically-provisioned storage is not available, consider storing the backup data on an NFS share to make backup recovery more accessible.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

**Procedure**

1. If dynamically-provisioned storage is available, complete the following steps to create automated recurring backups:

   1. Create a persistent volume claim (PVC) named `etcd-backup-pvc.yaml` with contents such as the following example:

      ```
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: etcd-backup-pvc
        namespace: openshift-etcd
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 200Gi
        volumeMode: Filesystem
        storageClassName: etcd-backup-local-storage
      ```

      where:

      `spec.resources.requests.storage`
      :   Specifies the amount of storage available to the PVC. Adjust this value for your requirements.

          Note

          Each of the following providers requires changes to the `accessModes` and `storageClassName` keys:

          Expand

          | Provider | `accessModes` value | `storageClassName` value |
          | --- | --- | --- |
          | AWS with the `versioned-installer-efc_operator-ci` profile | `- ReadWriteMany` | `efs-sc` |
          | Google Cloud | `- ReadWriteMany` | `filestore-csi` |
          | Microsoft Azure | `- ReadWriteMany` | `azurefile-csi` |

          Show more
   2. Apply the PVC by running the following command:

      ```
      $ oc apply -f etcd-backup-pvc.yaml
      ```
   3. Verify that the PVC was created by running the following command:

      ```
      $ oc get pvc
      ```

      **Example output**

      ```
      NAME              STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
      etcd-backup-pvc   Bound                                                       51s
      ```

      Note

      Dynamic PVCs stay in the `Pending` state until they are mounted.
2. If dynamically-provisioned storage is unavailable, create a local storage PVC by completing the following steps:

   Warning

   If you delete or otherwise lose access to the node that contains the stored backup data, you can lose data.

   1. Create a `StorageClass` CR file named `etcd-backup-local-storage.yaml` with the following contents:

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
        name: etcd-backup-local-storage
      provisioner: kubernetes.io/no-provisioner
      volumeBindingMode: Immediate
      ```
   2. Apply the `StorageClass` CR by running the following command:

      ```
      $ oc apply -f etcd-backup-local-storage.yaml
      ```
   3. Create a PV named `etcd-backup-pv-fs.yaml` from the applied `StorageClass` with contents such as the following example:

      ```
      apiVersion: v1
      kind: PersistentVolume
      metadata:
        name: etcd-backup-pv-fs
      spec:
        capacity:
          storage: 100Gi
        volumeMode: Filesystem
        accessModes:
        - ReadWriteMany
        persistentVolumeReclaimPolicy: Delete
        storageClassName: etcd-backup-local-storage
        local:
          path: /mnt/
        nodeAffinity:
          required:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/hostname
                operator: In
                values:
                - <example_control_plane_node>
      ```

      where:

      `spec.capacity.storage`
      :   Specifies the amount of storage available to the PV. Adjust this value for your requirements.

      `spec.nodeAffinity.required.nodeSelectorTerms.matchExpressions.values`
      :   Specifies the control plane node to attach this PV to. Replace with the actual node name.

          Tip

          List the available nodes by running the following command:

          ```
          $ oc get nodes
          ```
   4. Verify that the PV was created by running the following command:

      ```
      $ oc get pv
      ```

      **Example output**

      ```
      NAME                    CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS                REASON   AGE
      etcd-backup-pv-fs       100Gi      RWX            Delete           Available           etcd-backup-local-storage            10s
      ```
   5. Create a PVC named `etcd-backup-pvc.yaml` with contents such as the following example:

      ```
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: etcd-backup-pvc
      spec:
        accessModes:
        - ReadWriteMany
        volumeMode: Filesystem
        resources:
          requests:
            storage: 10Gi
        storageClassName: etcd-backup-local-storage
      ```

      where:

      `spec.resources.requests.storage`
      :   Specifies the amount of storage available to the PVC. Adjust this value for your requirements.
   6. Apply the PVC by running the following command:

      ```
      $ oc apply -f etcd-backup-pvc.yaml
      ```
3. Create a CR file named `etcd-recurring-backups.yaml`. The contents of the CR define the schedule and retention type of automated backups.

   * For the default retention type of `RetentionNumber` with 15 retained backups, use contents such as the following example:

     ```
     apiVersion: config.openshift.io/v1alpha1
     kind: Backup
     metadata:
       name: etcd-recurring-backup
     spec:
       etcd:
         schedule: "20 4 * * *"
         timeZone: "UTC"
         pvcName: etcd-backup-pvc
     ```

     where:

     `spec.etcd.schedule`
     :   Specifies the `CronTab` schedule for recurring backups. Adjust this value for your needs.

         1. To use retention based on the maximum number of backups, add the following key-value pairs to the `etcd` key:

            ```
            spec:
              etcd:
                retentionPolicy:
                  retentionType: RetentionNumber
                  retentionNumber:
                    maxNumberOfBackups: 5
            ```

            where:

     `spec.etcd.retentionPolicy.retentionType`
     :   Specifies the retention type. Defaults to `RetentionNumber` if unspecified.

     `spec.etcd.retentionPolicy.retentionNumber.maxNumberOfBackups`
     :   Specifies the maximum number of backups to retain. Adjust this value for your needs. Defaults to 15 backups if unspecified.

         Warning

         A known issue causes the number of retained backups to be one greater than the configured value.

         1. For retention based on the file size of backups, use the following:

            ```
            spec:
              etcd:
                retentionPolicy:
                  retentionType: RetentionSize
                  retentionSize:
                    maxSizeOfBackupsGb: 20
            ```

            where:

     `spec.etcd.retentionPolicy.retentionSize.maxSizeOfBackupsGb`
     :   Specifies the maximum file size of the retained backups in gigabytes. Adjust this value for your needs. Defaults to 10 GB if unspecified.

         Warning

         A known issue causes the maximum size of retained backups to be up to 10 GB greater than the configured value.
4. Create the cron job defined by the CRD by running the following command:

   ```
   $ oc create -f etcd-recurring-backup.yaml
   ```
5. To find the created cron job, run the following command:

   ```
   $ oc get cronjob -n openshift-etcd
   ```

### [4.2. Replacing a healthy etcd member](#replacing-a-healthy-etcd-member) Copy linkLink copied to clipboard!

You might need to replace a healthy etcd member for planned hardware maintenance, hardware upgrades, or migration to new infrastructure.

#### [4.2.1. About replacing a healthy etcd member](#replace-healthy-etcd-about_replace-healthy-etcd-member) Copy linkLink copied to clipboard!

To replace a control plane node without disrupting etcd, remove a healthy member and add a replacement while the cluster remains operational. The procedure you follow depends on how your cluster was installed and whether it uses the Machine API and a control plane machine set.

Note

If the etcd member is unhealthy because the machine is not running, the node is not ready, or the etcd pod is crashlooping, see "Replacing an unhealthy etcd member".

If you have lost the majority of your control plane hosts, see "Restoring to an earlier cluster state".

#### [4.2.2. Replacing a healthy etcd member](#replace-healthy-etcd-procedures-about_replace-healthy-etcd-member) Copy linkLink copied to clipboard!

To replace a healthy etcd member without disrupting cluster operations, choose the procedure that matches your control plane configuration. You can use a control plane machine set, the Machine API, or scale up and scale down control plane nodes.

Important

Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur. For more information, see "Backing up etcd data".

Depending on your cluster configuration, use one of the following procedures:

* Replacing a healthy etcd member with a control plane machine set
* Replacing a healthy etcd member with the Machine API
* Replacing a healthy etcd member by scaling up and scaling down

For clusters that were installed by using the Assisted Installer, see "Replacing a control plane node in a healthy cluster" in the Assisted Installer documentation.

#### [4.2.3. Determining how to replace a healthy etcd member](#determining-replace-healthy-etcd-member_replace-healthy-etcd-member) Copy linkLink copied to clipboard!

To choose the correct procedure for replacing a healthy etcd member, check whether your cluster uses the Assisted Installer, a control plane machine set, or the Machine API. Use the OpenShift CLI (`oc`) to identify your cluster configuration and follow the matching replacement procedure.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in to `oc` as a user with the `cluster-admin` role.

**Procedure**

1. Check whether the cluster was installed by using the Assisted Installer by running the following command:

   ```
   $ oc get agentclusterinstall -A
   ```

   * If the command returns one or more `AgentClusterInstall` resources, follow the procedure in "Replacing a control plane node in a healthy cluster" in the Assisted Installer documentation.
   * If the command returns no resources, continue with the following steps.
2. Check whether the cluster has a control plane machine set by running the following command:

   ```
   $ oc -n openshift-machine-api get controlplanemachineset
   ```

   * If the command returns a `ControlPlaneMachineSet` resource, follow the procedure in "Replacing a healthy etcd member with a control plane machine set".
   * If the command returns no resources, continue to the next step.
3. Check whether the cluster has control plane `Machine` objects by running the following command:

   ```
   $ oc get machines -l machine.openshift.io/cluster-api-machine-role=master -n openshift-machine-api
   ```

   * If `Machine` objects exist, follow the procedure in "Replacing a healthy etcd member with the Machine API".
   * If there are no `Machine` objects, follow the procedure in "Replacing a healthy etcd member by scaling up and scaling down".

#### [4.2.4. Replacing a healthy etcd member with a control plane machine set](#replacing-healthy-etcd-member-cpms_replace-healthy-etcd-member) Copy linkLink copied to clipboard!

On clusters that use a control plane machine set, you can replace a healthy control plane machine by deleting the corresponding `Machine` object.

The control plane machine set creates a replacement machine, and the etcd Operator uses machine lifecycle hooks to protect etcd quorum during the replacement.

For more information about how quorum protection works during control plane machine deletion, see "Quorum protection with machine lifecycle hooks".

**Prerequisites**

* The cluster has a `ControlPlaneMachineSet` resource.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup. For more information, see "Backing up etcd data".

  Important

  Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur.

**Procedure**

1. List the control plane machines in your cluster by running the following command:

   ```
   $ oc get machines \
     -l machine.openshift.io/cluster-api-machine-role=master \
     -n openshift-machine-api
   ```
2. Identify the control plane machine that corresponds to the node that you want to replace.
3. Optional. If you are performing planned maintenance, cordon the node by running the following command:

   ```
   $ oc adm cordon <node_name>
   ```

   Replace `<node_name>` with the name of the node that you are replacing.

   Important

   Delete only one control plane machine at a time. Deleting multiple control plane machines at the same time can cause etcd quorum loss.
4. Delete the control plane machine by running the following command:

   ```
   $ oc delete machine <control_plane_machine_name> -n openshift-machine-api
   ```

   Replace `<control_plane_machine_name>` with the name of the control plane machine to delete.

   Note

   If you delete multiple control plane machines, the control plane machine set replaces them according to the configured update strategy:

   * For clusters that use the default `RollingUpdate` update strategy, the Operator replaces one machine at a time until each machine is replaced.
   * For clusters that are configured to use the `OnDelete` update strategy, the Operator creates all of the required replacement machines simultaneously.

   Both strategies maintain etcd health during control plane machine replacement.
5. Monitor the replacement by running the following commands:

   1. Verify that a new control plane machine is created:

      ```
      $ oc get machines \
        -l machine.openshift.io/cluster-api-machine-role=master \
        -n openshift-machine-api -o wide
      ```
   2. Verify that the etcd cluster Operator reports `Available=True` and `Degraded=False`:

      ```
      $ oc get clusteroperator etcd
      ```

      Note

      During the replacement `Progressing=True` is expected and transitions to `False` once the new member is fully reconciled.
   3. Verify that all control plane nodes are in the `Ready` state:

      ```
      $ oc get nodes -l node-role.kubernetes.io/control-plane
      ```

**Verification**

1. Verify etcd health by running the following commands:

   1. Open a remote shell session to a control plane etcd pod:

      ```
      $ oc rsh -n openshift-etcd <etcd_pod_name>
      ```

      Replace `<etcd_pod_name>` with the name of a running etcd pod.
   2. Check endpoint health:

      ```
      sh-4.2# etcdctl endpoint health
      ```

      Expected output shows `is healthy` for each endpoint.
   3. List etcd members and verify that the cluster has three members:

      ```
      sh-4.2# etcdctl member list -w table
      ```
2. Verify that all cluster Operators are available by running the following command:

   ```
   $ oc get clusteroperators
   ```

#### [4.2.5. Replacing a healthy etcd member with the Machine API](#replacing-healthy-etcd-member-machine-api_replace-healthy-etcd-member) Copy linkLink copied to clipboard!

On clusters that access the Machine API but do not use a control plane machine set, you can replace a healthy control plane machine by deleting the corresponding `Machine` object. The Machine API provisions a replacement machine, and the etcd cluster Operator adds the new node as an etcd member.

**Prerequisites**

* The cluster has access to the Machine API.
* The cluster does not have a `ControlPlaneMachineSet` resource.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup. For more information, see "Backing up etcd data".

  Important

  Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur.

**Procedure**

1. List the control plane machines in your cluster by running the following command:

   ```
   $ oc get machines \
     -l machine.openshift.io/cluster-api-machine-role=master \
     -n openshift-machine-api -o wide
   ```
2. Identify the control plane machine that corresponds to the node that you want to replace.
3. Optional. If you are performing planned maintenance, cordon the node by running the following command:

   ```
   $ oc adm cordon <node_name>
   ```

   Replace `<node_name>` with the name of the node that you are replacing.
4. Delete the control plane machine by running the following command:

   ```
   $ oc delete machine <control_plane_machine_name> -n openshift-machine-api
   ```

   Replace `<control_plane_machine_name>` with the name of the control plane machine to delete.

   Important

   Delete only one control plane machine at a time. Deleting multiple control plane machines at the same time can cause etcd quorum loss.

   A new machine is automatically provisioned after you delete the control plane machine.
5. Monitor the replacement by running the following commands until the new machine reaches the `Running` phase:

   ```
   $ oc get machines \
     -l machine.openshift.io/cluster-api-machine-role=master \
     -n openshift-machine-api -o wide
   ```

   ```
   $ oc get clusteroperator etcd
   ```

   ```
   $ oc get nodes -l node-role.kubernetes.io/control-plane
   ```

**Verification**

1. Verify etcd health by running the following commands:

   1. Open a remote shell session to a control plane etcd pod:

      ```
      $ oc rsh -n openshift-etcd <etcd_pod_name>
      ```

      Replace `<etcd_pod_name>` with the name of a running etcd pod.
   2. Check endpoint health:

      ```
      sh-4.2# etcdctl endpoint health
      ```

      Expected output shows `is healthy` for each endpoint.
   3. List etcd members and verify that the cluster has three members:

      ```
      sh-4.2# etcdctl member list -w table
      ```
2. Verify that all cluster Operators are available by running the following command:

   ```
   $ oc get clusteroperators
   ```

#### [4.2.6. Replacing a healthy etcd member by scaling up and scaling down](#replacing-healthy-etcd-member-scale-up-down_replace-healthy-etcd-member) Copy linkLink copied to clipboard!

On bare-metal clusters that do not use a control plane machine set, replace a healthy control plane node by temporarily scaling the control plane to four nodes, and then removing the node that you want to replace.

Important

Red Hat supports a cluster that has 4 or 5 control plane nodes only on bare-metal infrastructure.

**Prerequisites**

* The cluster does not have a `ControlPlaneMachineSet` resource.
* The cluster is installed on bare-metal infrastructure.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have taken an etcd backup. For more information, see "Backing up etcd data".
* You have created a single control plane node that you intend to add to your cluster as a postinstallation task.

  Important

  Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur.

**Procedure**

1. Add the new control plane node to your cluster by following the steps in "Adding a control plane node to your cluster".
2. Verify that the new control plane node is in the `Ready` state and that etcd has four members by running the following commands:

   ```
   $ oc get nodes -l node-role.kubernetes.io/control-plane
   ```

   ```
   $ oc rsh -n openshift-etcd <etcd_pod_name>
   ```

   Replace `<etcd_pod_name>` with the name of a running etcd pod.

   ```
   sh-4.2# etcdctl member list -w table
   ```

   ```
   sh-4.2# etcdctl endpoint health
   ```

   Expected output shows four etcd members and `is healthy` for each endpoint.
3. Remove the control plane node that you want to replace.

   1. Optional. If you are performing planned maintenance, cordon the node by running the following command:

      ```
      $ oc adm cordon <node_name>
      ```

      Replace `<node_name>` with the name of the node that you are replacing.
   2. Delete the `BareMetalHost` object for the control plane node that you want to replace by running the following command:

      ```
      $ oc delete bmh <node_name> -n openshift-machine-api
      ```

      Replace `<node_name>` with the name of the node that you are replacing.
   3. Delete the `Machine` object for the control plane node that you want to replace by running the following command:

      ```
      $ oc delete machine <machine_name> -n openshift-machine-api
      ```

      Replace `<machine_name>` with the name of the machine that is associated with the node that you are replacing.

      Note

      After you remove the `BareMetalHost` and `Machine` objects, the machine controller automatically deletes the `Node` object.
4. Monitor the cluster until the control plane returns to three nodes and etcd is healthy by running the following commands:

   ```
   $ oc get nodes -l node-role.kubernetes.io/control-plane
   ```

   ```
   $ oc get clusteroperator etcd
   ```

**Verification**

1. Verify etcd health by running the following commands:

   1. Open a remote shell session to a control plane etcd pod:

      ```
      $ oc rsh -n openshift-etcd <etcd_pod_name>
      ```
   2. Check endpoint health:

      ```
      sh-4.2# etcdctl endpoint health
      ```

      Expected output shows `is healthy` for each endpoint.
   3. List etcd members and verify that the cluster has three members:

      ```
      sh-4.2# etcdctl member list -w table
      ```
2. Verify that all cluster Operators are available by running the following command:

   ```
   $ oc get clusteroperators
   ```

### [4.3. Replacing an unhealthy etcd member](#replace-unhealthy-etcd-member) Copy linkLink copied to clipboard!

To restore etcd quorum when a single member is unhealthy, identify the member and determine whether its machine is stopped, its node is not ready, or its pod is crashlooping. You can then follow the replacement procedure that matches that state.

Note

If you have lost the majority of your control plane hosts, follow the steps in "Restoring to an earlier cluster state" instead of this procedure.

If the control plane certificates are not valid on the member being replaced, then you must follow the steps in "Recovering from expired control plane certificates" instead of this procedure.

If a control plane node is lost and a new one is created, the etcd cluster Operator handles generating the new TLS certificates and adding the node as an etcd member.

#### [4.3.1. Identifying an unhealthy etcd member](#restore-identify-unhealthy-etcd-member_replace-unhealthy-etcd-member) Copy linkLink copied to clipboard!

You can identify an unhealthy etcd member by checking the `EtcdMembersAvailable` status condition to see how many members are available and which member is unhealthy.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You created an etcd backup.

**Procedure**

* Check the status of the `EtcdMembersAvailable` status condition by running the following command:

  ```
  $ oc get etcd -o=jsonpath='{range .items[0].status.conditions[?(@.type=="EtcdMembersAvailable")]}{.message}{"\n"}{end}'
  ```

  **Example output**

  ```
  2 of 3 members are available, ip-10-0-131-183.ec2.internal is unhealthy
  ```

#### [4.3.2. Determining the state of the unhealthy etcd member](#restore-determine-state-etcd-member_replace-unhealthy-etcd-member) Copy linkLink copied to clipboard!

Determine whether the unhealthy etcd member has a stopped machine, an unready node, or a crashlooping etcd pod. Knowing the failure state enables you to follow the correct replacement procedure.

Depending on the state of your unhealthy etcd member, use one of the following procedures:

* Machine not running or node not ready. For more information, see "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready".
* Bare-metal machine not running or node not ready on installer-provisioned bare metal. For more information, see "Replacing an unhealthy bare metal etcd member whose machine is not running or whose node is not ready".
* Crashlooping etcd pod. For more information, see "Replacing an unhealthy etcd member whose etcd pod is crashlooping".

Note

If the machine is not running or the node is not ready, you might expect either to recover soon. In that case, you do not need to replace the etcd member. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

**Prerequisites**

* You confirmed access to the cluster as a user with the `cluster-admin` role.
* You identified an unhealthy etcd member.

**Procedure**

1. Determine if the machine is not running by running the following command:

   ```
   $ oc get machines -A -ojsonpath='{range .items[*]}{@.status.nodeRef.name}{"\t"}{@.status.providerStatus.instanceState}{"\n"}' | grep -v running
   ```

   **Example output**

   ```
   ip-10-0-131-183.ec2.internal  stopped
   ```

   This output lists the node and the status of the machine of the node. If the status is anything other than `running`, then the machine is not running.
2. Determine if the status of the node is `NotReady`.

   If either of the following scenarios are true, then the node is not ready.

   1. If the machine is running, then check whether the node has an `unreachable` taint by running the following command:

      ```
      $ oc get nodes -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{"\t"}{range .spec.taints[*]}{.key}{" "}' | grep unreachable
      ```

      **Example output**

      ```
      ip-10-0-131-183.ec2.internal	node-role.kubernetes.io/master node.kubernetes.io/unreachable node.kubernetes.io/unreachable
      ```

      If the node is listed with an `unreachable` taint, then the node is not ready.
   2. If the node is still reachable, then check whether the node is listed as `NotReady` by running the following command:

      ```
      $ oc get nodes -l node-role.kubernetes.io/master | grep "NotReady"
      ```

      **Example output**

      ```
      ip-10-0-131-183.ec2.internal   NotReady   master   122m   v1.35.4
      ```

      If the node is listed as `NotReady`, then the node is not ready.

      If the **node is not ready**, then follow the "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready" procedure.
3. Determine if the etcd pod is crashlooping.

   If the machine is running and the node status is `Ready`, check the status of the etcd pod.

   1. Verify that all control plane nodes are listed as `Ready` by running the following command:

      ```
      $ oc get nodes -l node-role.kubernetes.io/master
      ```

      **Example output**

      ```
      NAME                           STATUS   ROLES    AGE     VERSION
      ip-10-0-131-183.ec2.internal   Ready    master   6h13m   v1.35.4
      ip-10-0-164-97.ec2.internal    Ready    master   6h13m   v1.35.4
      ip-10-0-154-204.ec2.internal   Ready    master   6h13m   v1.35.4
      ```
   2. Check whether the status of an etcd pod is either `Error` or `CrashloopBackoff` by running the following command:

      ```
      $ oc -n openshift-etcd get pods -l k8s-app=etcd
      ```

      **Example output**

      ```
      etcd-ip-10-0-131-183.ec2.internal                2/3     Error       7          6h9m
      etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          6h6m
      etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          6h6m
      ```

      The etcd pod crashloops because the `etcd-ip-10-0-131-183.ec2.internal` is `Error`.

      If the **etcd pod is crashlooping**, then follow the steps in "Replacing an unhealthy etcd member whose etcd pod is crashlooping".

##### [4.3.2.1. Replacing an unhealthy etcd member whose machine is not running or whose node is not ready](#restore-replace-stopped-etcd-member_replace-unhealthy-etcd-member) Copy linkLink copied to clipboard!

Replace an unhealthy etcd member when the member machine is stopped or the node is not ready. Restoring the member returns the control plane to a healthy state.

Note

If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in "Troubleshooting the control plane machine set" for an etcd recovery procedure.

**Prerequisites**

* You identified the unhealthy etcd member.
* You verified that either the machine is not running or the node is not ready.
* Do not power on other control plane nodes until the unhealthy etcd member replacement is complete.
* You confirmed access to the cluster as a user with the `cluster-admin` role.
* You created an etcd backup before replacing the unhealthy etcd member.

  Important

  Without a recent etcd backup, you might not be able to restore the cluster if replacement fails.

**Procedure**

1. Remove the unhealthy member.

   1. List etcd pods and choose one that is not on the affected node by running the following command:

      ```
      $ oc -n openshift-etcd get pods -l k8s-app=etcd
      ```

      **Example output**

      ```
      etcd-ip-10-0-131-183.ec2.internal                3/3     Running     0          123m
      etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          123m
      etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          124m
      ```

      From the output, note a pod that is not on the affected node. In this example, the unhealthy member is `ip-10-0-131-183.ec2.internal`, so you could use `etcd-ip-10-0-154-204.ec2.internal`.
   2. Connect to the running etcd container on the pod you chose by running the following command:

      ```
      $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
      ```
   3. View the member list by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      | 6fc1e7c9db35841d | started | ip-10-0-131-183.ec2.internal | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
      | 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
      | ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      ```

      Take note of the ID and the name of the unhealthy etcd member because you need these values later in the procedure. The `etcdctl endpoint health` command continues to list the removed member until replacement is complete and a new member is added.
   4. Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command by running the following command:

      ```
      sh-4.2# etcdctl member remove <etcd_member_id>
      ```

      **Example output**

      ```
      Member 6fc1e7c9db35841d removed from cluster ead669ce1fbfb346
      ```
   5. View the member list again and verify that the member was removed by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      | 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
      | ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      ```

      You can now exit the node shell.
2. Turn off the quorum guard by running the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
   ```

   This command ensures that you can successfully re-create secrets and roll out the static pods.

   Important

   After you turn off the quorum guard, the cluster might be unreachable for a short period of time while the remaining etcd instances reboot to reflect the configuration change.

   Note

   etcd cannot tolerate any additional member failure when running with two members. Restarting either remaining member breaks the quorum and causes downtime in your cluster. The quorum guard protects etcd from restarts due to configuration changes that could cause downtime, so it must be disabled to complete this procedure.
3. Delete the affected node by running the following command:

   ```
   $ oc delete node <node_name>
   ```

   **Example command**

   ```
   $ oc delete node ip-10-0-131-183.ec2.internal
   ```
4. Remove the old secrets for the unhealthy etcd member that was removed.

   1. List the secrets for the unhealthy etcd member that was removed by running the following command:

      ```
      $ oc get secrets -n openshift-etcd | grep ip-10-0-131-183.ec2.internal
      ```

      Replace `ip-10-0-131-183.ec2.internal` in the command with the name of the unhealthy etcd member that you noted earlier in this procedure.

      There is a peer, serving, and metrics secret as shown in the following output:

      **Example output**

      ```
      etcd-peer-ip-10-0-131-183.ec2.internal              kubernetes.io/tls                     2      47m
      etcd-serving-ip-10-0-131-183.ec2.internal           kubernetes.io/tls                     2      47m
      etcd-serving-metrics-ip-10-0-131-183.ec2.internal   kubernetes.io/tls                     2      47m
      ```
   2. Delete the peer secret by running the following command:

      ```
      $ oc delete secret -n openshift-etcd etcd-peer-ip-10-0-131-183.ec2.internal
      ```
   3. Delete the serving secret by running the following command:

      ```
      $ oc delete secret -n openshift-etcd etcd-serving-ip-10-0-131-183.ec2.internal
      ```
   4. Delete the metrics secret by running the following command:

      ```
      $ oc delete secret -n openshift-etcd etcd-serving-metrics-ip-10-0-131-183.ec2.internal
      ```
5. Check whether a control plane machine set exists by running the following command:

   ```
   $ oc -n openshift-machine-api get controlplanemachineset
   ```

   If the control plane machine set exists, delete and re-create the control plane machine. After this machine is re-created, a new revision is forced and etcd scales up automatically. For more information, see "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready".

   If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps. Otherwise, you must create the new control plane by using the same method that was used to originally create it.

   1. Obtain the machine for the unhealthy member by running the following command.

      ```
      $ oc get machines -n openshift-machine-api -o wide
      ```

      **Example output**

      ```
      NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
      clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped
      clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
      clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
      clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
      clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
      clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
      ```

      In the example output, `clustername-8qw5l-master-0` is the control plane machine for the unhealthy node `ip-10-0-131-183.ec2.internal`. Its `STATE` is `stopped`.
   2. Delete the machine of the unhealthy member by running the following command:

      ```
      $ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0
      ```

      Replace `clustername-8qw5l-master-0` with the name of the control plane machine for the unhealthy node.

      A new machine is automatically provisioned after deleting the machine of the unhealthy member.
   3. Verify that a new machine was created by running the following command:

      ```
      $ oc get machines -n openshift-machine-api -o wide
      ```

      **Example output**

      ```
      NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
      clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
      clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
      clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-133-53.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8   running
      clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
      clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
      clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
      ```

      In the example output, `clustername-8qw5l-master-3` is the new control plane machine. The machine is ready when the `PHASE` changes from `Provisioning` to `Running`.

      It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

      Note

      Verify the subnet IDs that you are using for your machine sets to ensure that they end up in the correct availability zone.

      If the control plane machine set does not exist, delete and re-create the control plane machine. After this machine is re-created, a new revision is forced and etcd scales up automatically.

      If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps. Otherwise, you must create the new control plane by using the same method that was used to originally create it.
   4. Obtain the machine for the unhealthy member by running the following command:

      ```
      $ oc get machines -n openshift-machine-api -o wide
      ```

      **Example output**

      ```
      NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
      clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped
      clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
      clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
      clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
      clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
      clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
      ```

      In the example output, `clustername-8qw5l-master-0` is the control plane machine for the unhealthy node `ip-10-0-131-183.ec2.internal`. Its `STATE` is `stopped`.
   5. Save the machine configuration to a file on your file system by running the following command:

      ```
      $ oc get machine clustername-8qw5l-master-0 \
          -n openshift-machine-api \
          -o yaml \
          > new-master-machine.yaml
      ```

      Replace `clustername-8qw5l-master-0` with the name of the control plane machine for the unhealthy node.
6. Edit the `new-master-machine.yaml` file that was created in the previous step to assign a new name and remove unnecessary fields:

   1. Remove the entire `status` section:

      ```
      status:
        addresses:
        - address: 10.0.131.183
          type: InternalIP
        - address: ip-10-0-131-183.ec2.internal
          type: InternalDNS
        - address: ip-10-0-131-183.ec2.internal
          type: Hostname
        lastUpdated: "2020-04-20T17:44:29Z"
        nodeRef:
          kind: Node
          name: ip-10-0-131-183.ec2.internal
          uid: acca4411-af0d-4387-b73e-52b2484295ad
        phase: Running
        providerStatus:
          apiVersion: awsproviderconfig.openshift.io/v1beta1
          conditions:
          - lastProbeTime: "2020-04-20T16:53:50Z"
            lastTransitionTime: "2020-04-20T16:53:50Z"
            message: machine successfully created
            reason: MachineCreationSucceeded
            status: "True"
            type: MachineCreation
          instanceId: i-0fdb85790d76d0c3f
          instanceState: stopped
          kind: AWSMachineProviderStatus
      ```
   2. Change the `metadata.name` field to a new name.

      For example:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: Machine
      metadata:
        ...
        name: clustername-8qw5l-master-3
        ...
      ```

      Keep the same base name as the old machine and change the ending number to the next available number. In this example, `clustername-8qw5l-master-0` is changed to `clustername-8qw5l-master-3`
   3. Remove the `spec.providerID` field:

      ```
        providerID: aws:///us-east-1a/i-0fdb85790d76d0c3f
      ```
7. Delete the machine of the unhealthy member by running the following command:

   ```
   $ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0
   ```

   In the command, replace `clustername-8qw5l-master-0` with the control plane machine name for the unhealthy node that you identified in the example output above.
8. Verify that the machine was deleted by running the following command:

   ```
   $ oc get machines -n openshift-machine-api -o wide
   ```

   **Example output**

   ```
   NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
   clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
   clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
   clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
   clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
   clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
   ```
9. Create the new machine by using the `new-master-machine.yaml` file by running the following command:

   ```
   $ oc apply -f new-master-machine.yaml
   ```
10. Verify that the new machine was created by running the following command:

    ```
    $ oc get machines -n openshift-machine-api -o wide
    ```

    **Example output**

    ```
    NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
    clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
    clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
    clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-133-53.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8   running
    clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
    clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
    clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
    ```

    In the example output, `clustername-8qw5l-master-3` is the new control plane machine. The machine is ready when the `PHASE` changes from `Provisioning` to `Running`.

    It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.
11. Turn the quorum guard back on by running the following command:

    ```
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
    ```
12. You can verify that the `unsupportedConfigOverrides` section is removed from the object by running the following command:

    ```
    $ oc get etcd/cluster -oyaml
    ```
13. If you are using single-node OpenShift, restart the node. Otherwise, you might experience the following error in the etcd cluster Operator:

    **Example output**

    ```
    EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
    ```

**Verification**

1. Verify that all etcd pods are running properly by running the following command:

   ```
   $ oc -n openshift-etcd get pods -l k8s-app=etcd
   ```

   **Example output**

   ```
   etcd-ip-10-0-133-53.ec2.internal                 3/3     Running     0          7m49s
   etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          123m
   etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          124m
   ```
2. If the output from the previous command lists only two pods, force an etcd redeployment by running the following command:

   ```
   $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
   ```

   The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended in the example.
3. Verify that there are exactly three etcd members.

   1. Connect to the running etcd container, passing in the name of a pod that was not on the affected node by running the following command:

      ```
      $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
      ```
   2. View the member list by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      | 5eb0d6b8ca24730c | started |  ip-10-0-133-53.ec2.internal |  https://10.0.133.53:2380 |  https://10.0.133.53:2379 |
      | 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
      | ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      ```

      If the output from the previous command lists more than three etcd members, you must carefully remove the unwanted member.

      Warning

      Be sure to remove the correct etcd member; removing a good etcd member might lead to quorum loss.

##### [4.3.2.2. Replacing an unhealthy etcd member whose etcd pod is crashlooping](#restore-replace-crashlooping-etcd-member_replace-unhealthy-etcd-member) Copy linkLink copied to clipboard!

Replace an unhealthy etcd member when the etcd pod is crashlooping. Restoring the member returns the control plane to a healthy state.

**Prerequisites**

* You identified the unhealthy etcd member.
* You verified that the etcd pod is crashlooping.
* You confirmed access to the cluster as a user with the `cluster-admin` role.
* You created an etcd backup before replacing the unhealthy etcd member.

  Important

  It is important to take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues.

**Procedure**

1. Stop the crashlooping etcd pod.

   1. Debug the node that is crashlooping by running the following command:

      ```
      $ oc debug node/<unhealthy_node>
      ```

      Replace `<unhealthy_node>` with the name of the unhealthy etcd member.
   2. Change your root directory to `/host` by running the following command:

      ```
      sh-4.2# chroot /host
      ```
   3. Create a backup directory by running the following command:

      ```
      sh-4.2# mkdir /var/lib/etcd-backup
      ```
2. Move the existing etcd pod file out of the kubelet manifest directory by running the following commands:

   ```
   sh-4.2# mv /etc/kubernetes/manifests/etcd-pod.yaml /var/lib/etcd-backup/
   ```

   1. Move the etcd data directory to a different location by running the following command:

      ```
      sh-4.2# mv /var/lib/etcd/ /tmp
      ```

      You can now exit the node shell.
3. Remove the unhealthy member.

   1. Choose a pod that is *not* on the affected node by running the following command:

      ```
      $ oc -n openshift-etcd get pods -l k8s-app=etcd
      ```

      **Example output**

      ```
      etcd-ip-10-0-131-183.ec2.internal                2/3     Error       7          6h9m
      etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          6h6m
      etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          6h6m
      ```
   2. Connect to the running etcd container, passing in the name of a pod that is not on the affected node by running the following command:

      ```
      $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
      ```
   3. View the member list by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      | 62bcf33650a7170a | started | ip-10-0-131-183.ec2.internal | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
      | b78e2856655bc2eb | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
      | d022e10b498760d5 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      ```

      Take note of the ID and the name of the unhealthy etcd member, because these values are needed later in the procedure.
   4. Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:

      ```
      sh-4.2# etcdctl member remove 62bcf33650a7170a
      ```

      **Example output**

      ```
      Member 62bcf33650a7170a removed from cluster ead669ce1fbfb346
      ```
   5. View the member list again and verify that the member was removed by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      | b78e2856655bc2eb | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
      | d022e10b498760d5 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
      +------------------+---------+------------------------------+---------------------------+---------------------------+
      ```

      You can now exit the node shell.
4. Turn off the quorum guard by running the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
   ```

   This command ensures that you can successfully re-create secrets and roll out the static pods.
5. Remove the old secrets for the unhealthy etcd member that was removed.

   1. List the secrets for the unhealthy etcd member that was removed by running the following command:

      ```
      $ oc get secrets -n openshift-etcd | grep <unhealthy_node>
      ```

      Replace `<unhealthy_node>` in the command with the name of the unhealthy etcd member that you noted earlier in this procedure.

      There is a peer, serving, and metrics secret as shown in the following output:

      **Example output**

      ```
      etcd-peer-ip-10-0-131-183.ec2.internal              kubernetes.io/tls                     2      47m
      etcd-serving-ip-10-0-131-183.ec2.internal           kubernetes.io/tls                     2      47m
      etcd-serving-metrics-ip-10-0-131-183.ec2.internal   kubernetes.io/tls                     2      47m
      ```
   2. Delete the peer secret for the unhealthy etcd member that was removed by running the following command:

      ```
      $ oc delete secret -n openshift-etcd etcd-peer-ip-10-0-131-183.ec2.internal
      ```
   3. Delete the serving secret by running the following command:

      ```
      $ oc delete secret -n openshift-etcd etcd-serving-ip-10-0-131-183.ec2.internal
      ```
   4. Delete the metrics secret by running the following command:

      ```
      $ oc delete secret -n openshift-etcd etcd-serving-metrics-ip-10-0-131-183.ec2.internal
      ```
6. Force etcd redeployment by running the following command:

   ```
   $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "single-master-recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
   ```

   The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.

   When the etcd cluster Operator performs a redeployment, it ensures that all control plane nodes have a functioning etcd pod.
7. Turn the quorum guard back on by running the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
   ```
8. Verify that the `unsupportedConfigOverrides` section is removed from the object by running the following command:

   ```
   $ oc get etcd/cluster -oyaml
   ```
9. If you are using single-node OpenShift, restart the node. Otherwise, you might encounter the following error in the etcd cluster Operator:

   **Example output**

   ```
   EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
   ```

**Verification**

* Verify that the new member is available and healthy.

  + Connect to the running etcd container by running the following command:

    ```
    $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
    ```
  + Verify that all members are healthy by running the following command:

    ```
    sh-4.2# etcdctl endpoint health
    ```

    **Example output**

    ```
    https://10.0.131.183:2379 is healthy: successfully committed proposal: took = 16.671434ms
    https://10.0.154.204:2379 is healthy: successfully committed proposal: took = 16.698331ms
    https://10.0.164.97:2379 is healthy: successfully committed proposal: took = 16.621645ms
    ```

##### [4.3.2.3. Replacing an unhealthy bare metal etcd member whose machine is not running or whose node is not ready](#restore-replace-stopped-baremetal-etcd-member_replace-unhealthy-etcd-member) Copy linkLink copied to clipboard!

Replace an unhealthy bare metal etcd member when the machine is not running or the node is not ready. Restoring the member returns the control plane to a healthy state.

If you are running installer-provisioned infrastructure or you used the Machine API to create your machines, follow these steps. Otherwise you must create the new control plane node using the same method that was used to originally create it.

**Prerequisites**

* You identified the unhealthy bare metal etcd member.
* You verified that either the machine is not running or the node is not ready.
* You confirmed access to the cluster as a user with the `cluster-admin` role.
* You created an etcd backup.

  Important

  You must take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues.

**Procedure**

1. Verify and remove the unhealthy member.

   1. Choose a pod that is not on the affected node by running the following command:

      ```
      $ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
      ```

      **Example output**

      ```
      etcd-openshift-control-plane-0   5/5   Running   11   3h56m   192.168.10.9   openshift-control-plane-0  <none>           <none>
      etcd-openshift-control-plane-1   5/5   Running   0    3h54m   192.168.10.10   openshift-control-plane-1   <none>           <none>
      etcd-openshift-control-plane-2   5/5   Running   0    3h58m   192.168.10.11   openshift-control-plane-2   <none>           <none>
      ```
   2. Connect to the running etcd container, passing in the name of a pod that is not on the affected node by running the following command:

      ```
      $ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
      ```
   3. View the member list by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
      | ID               | STATUS  | NAME                      | PEER ADDRS                  | CLIENT ADDRS                | IS LEARNER |
      +------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
      | 7a8197040a5126c8 | started | openshift-control-plane-2 | https://192.168.10.11:2380/ | https://192.168.10.11:2379/ | false |
      | 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380/ | https://192.168.10.10:2379/ | false |
      | cc3830a72fc357f9 | started | openshift-control-plane-0 | https://192.168.10.9:2380/ | https://192.168.10.9:2379/   | false |
      +------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
      ```

      Take note of the ID and the name of the unhealthy etcd member, because these values are required later in the procedure. The `etcdctl endpoint health` command lists the removed member until the replacement procedure is completed and the new member is added.

      Warning

      Be sure to remove the correct etcd member. Removing a good etcd member might lead to quorum loss.
   4. Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:

      ```
      sh-4.2# etcdctl member remove 7a8197040a5126c8
      ```

      **Example output**

      ```
      Member 7a8197040a5126c8 removed from cluster b23536c33f2cdd1b
      ```
   5. View the member list again and verify that the member was removed by running the following command:

      ```
      sh-4.2# etcdctl member list -w table
      ```

      **Example output**

      ```
      +------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
      | ID               | STATUS  | NAME                      | PEER ADDRS                  | CLIENT ADDRS                | IS LEARNER |
      +------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
      | cc3830a72fc357f9 | started | openshift-control-plane-2 | https://192.168.10.11:2380/ | https://192.168.10.11:2379/ | false |
      | 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380/ | https://192.168.10.10:2379/ | false |
      +------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
      ```

      You can now exit the node shell.

      Important

      After you remove the member, the cluster might be unreachable for a short time while the remaining etcd instances reboot.
2. Turn off the quorum guard by running the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
   ```

   This command ensures that you can successfully re-create secrets and roll out the static pods.
3. Remove the old secrets for the unhealthy etcd member that was removed.

   1. List the secrets for the unhealthy etcd member that was removed by running the following command:

      ```
      $ oc get secrets -n openshift-etcd | grep openshift-control-plane-2
      ```

      Pass in the name of the unhealthy etcd member that you took note of earlier in this procedure.

      There is a peer, serving, and metrics secret as shown in the following output:

      ```
      etcd-peer-openshift-control-plane-2             kubernetes.io/tls   2   134m
      etcd-serving-metrics-openshift-control-plane-2  kubernetes.io/tls   2   134m
      etcd-serving-openshift-control-plane-2          kubernetes.io/tls   2   134m
      ```
   2. Delete the secrets for the unhealthy etcd member by running the following command:

      ```
      $ oc delete secret etcd-peer-openshift-control-plane-2 -n openshift-etcd
      ```

      **Example output**

      ```
      secret "etcd-peer-openshift-control-plane-2" deleted
      ```
   3. Delete the serving secret by running the following command:

      ```
      $ oc delete secret etcd-serving-metrics-openshift-control-plane-2 -n openshift-etcd
      ```

      **Example output**

      ```
      secret "etcd-serving-metrics-openshift-control-plane-2" deleted
      ```
   4. Delete the metrics secret by running the following command:

      ```
      $ oc delete secret etcd-serving-openshift-control-plane-2 -n openshift-etcd
      ```

      **Example output**

      ```
      secret "etcd-serving-openshift-control-plane-2" deleted
      ```
4. Obtain the machine for the unhealthy member by running the following command:

   ```
   $ oc get machines -n openshift-machine-api -o wide
   ```

   **Example output**

   ```
   NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                               PROVIDERID                                                                                              STATE
   examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
   examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
   examplecluster-control-plane-2    Running                          3h11m   openshift-control-plane-2   baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135   externally provisioned
   examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
   examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
   ```

   `examplecluster-control-plane-2` is the control plane machine for the unhealthy node `openshift-control-plane-2`.
5. Ensure that the Bare Metal Operator is available by running the following command:

   ```
   $ oc get clusteroperator baremetal
   ```

   **Example output**

   ```
   NAME        VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
   baremetal   4.22.0    True        False         False      3d15h
   ```
6. Remove the old `BareMetalHost` object by running the following command:

   ```
   $ oc delete bmh openshift-control-plane-2 -n openshift-machine-api
   ```

   **Example output**

   ```
   baremetalhost.metal3.io "openshift-control-plane-2" deleted
   ```
7. Delete the machine of the unhealthy member by running the following command:

   ```
   $ oc delete machine -n openshift-machine-api examplecluster-control-plane-2
   ```

   After you remove the `BareMetalHost` and `Machine` objects, then the `Machine` controller automatically deletes the `Node` object.

   If deletion of the machine is delayed for any reason or the command is obstructed and delayed, you can force deletion by removing the machine object finalizer field.

   Important

   Do not interrupt machine deletion by pressing `Ctrl+c`. You must allow the command to proceed to completion. Open a new terminal window to edit and delete the finalizer fields.

   A new machine is automatically provisioned after deleting the machine of the unhealthy member.

   1. Edit the machine configuration by running the following command:

      ```
      $ oc edit machine -n openshift-machine-api examplecluster-control-plane-2
      ```
   2. Delete the following fields in the `Machine` custom resource, and then save the updated file:

      ```
      finalizers:
      - machine.machine.openshift.io
      ```

      **Example output**

      ```
      machine.machine.openshift.io/examplecluster-control-plane-2 edited
      ```
8. Verify that the machine was deleted by running the following command:

   ```
   $ oc get machines -n openshift-machine-api -o wide
   ```

   **Example output**

   ```
   NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                                 PROVIDERID                                                                                       STATE
   examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
   examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
   examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
   examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
   ```
9. Verify that the node has been deleted by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                     STATUS ROLES   AGE   VERSION
   openshift-control-plane-0 Ready master 3h24m v1.35.4
   openshift-control-plane-1 Ready master 3h24m v1.35.4
   openshift-compute-0       Ready worker 176m v1.35.4
   openshift-compute-1       Ready worker 176m v1.35.4
   ```
10. Create the new `BareMetalHost` object and the secret to store the Baseboard Management Controller (BMC) credentials by running the following command:

    ```
    $ cat <<EOF | oc apply -f -
    apiVersion: v1
    kind: Secret
    metadata:
      name: openshift-control-plane-2-bmc-secret
      namespace: openshift-machine-api
    data:
      password: <password>
      username: <username>
    type: Opaque
    ---
    apiVersion: metal3.io/v1alpha1
    kind: BareMetalHost
    metadata:
      name: openshift-control-plane-2
      namespace: openshift-machine-api
    spec:
      automatedCleaningMode: disabled
      bmc:
        address: redfish://10.46.61.18:443/redfish/v1/Systems/1
        credentialsName: openshift-control-plane-2-bmc-secret
        disableCertificateVerification: true
      bootMACAddress: 48:df:37:b0:8a:a0
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

    Note

    The username and password can be found from the secrets of the other bare-metal host. The protocol to use in `bmc:address` can be taken from other bmh objects.

    Important

    If you reuse the `BareMetalHost` object definition from an existing control plane host, do not leave the `externallyProvisioned` field set to `true`.

    Existing control plane `BareMetalHost` objects may have the `externallyProvisioned` flag set to `true` if they were provisioned by the OpenShift Container Platform installation program.

    After the inspection is complete, the `BareMetalHost` object is created and available to be provisioned.
11. Verify the creation process using available `BareMetalHost` objects by running the following command:

    ```
    $ oc get bmh -n openshift-machine-api
    ```

    **Example output**

    ```
    NAME                      STATE                  CONSUMER                      ONLINE ERROR   AGE
    openshift-control-plane-0 externally provisioned examplecluster-control-plane-0 true         4h48m
    openshift-control-plane-1 externally provisioned examplecluster-control-plane-1 true         4h48m
    openshift-control-plane-2 available              examplecluster-control-plane-3 true         47m
    openshift-compute-0       provisioned            examplecluster-compute-0       true         4h48m
    openshift-compute-1       provisioned            examplecluster-compute-1       true         4h48m
    ```

    1. Verify that a new machine has been created by running the following command:

       ```
       $ oc get machines -n openshift-machine-api -o wide
       ```

       **Example output**

       ```
       NAME                                   PHASE     TYPE   REGION   ZONE   AGE     NODE                              PROVIDERID                                                                                            STATE
       examplecluster-control-plane-0         Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
       examplecluster-control-plane-1         Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
       examplecluster-control-plane-2         Running                          3h11m   openshift-control-plane-2   baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135   externally provisioned
       examplecluster-compute-0               Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
       examplecluster-compute-1               Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
       ```

       The new machine is ready when the phase changes from `Provisioning` to `Running`.

       It should take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.
    2. Verify that the bare metal host becomes provisioned and no error reported by running the following command:

       ```
       $ oc get bmh -n openshift-machine-api
       ```

       **Example output**

       ```
       NAME                      STATE                  CONSUMER                       ONLINE ERROR AGE
       openshift-control-plane-0 externally provisioned examplecluster-control-plane-0 true         4h48m
       openshift-control-plane-1 externally provisioned examplecluster-control-plane-1 true         4h48m
       openshift-control-plane-2 provisioned            examplecluster-control-plane-3 true          47m
       openshift-compute-0       provisioned            examplecluster-compute-0       true         4h48m
       openshift-compute-1       provisioned            examplecluster-compute-1       true         4h48m
       ```
    3. Verify that the new node is added and in a ready state by running the following command:

       ```
       $ oc get nodes
       ```

       **Example output**

       ```
       NAME                     STATUS ROLES   AGE   VERSION
       openshift-control-plane-0 Ready master 4h26m v1.35.4
       openshift-control-plane-1 Ready master 4h26m v1.35.4
       openshift-control-plane-2 Ready master 12m   v1.35.4
       openshift-compute-0       Ready worker 3h58m v1.35.4
       openshift-compute-1       Ready worker 3h58m v1.35.4
       ```
12. Turn the quorum guard back on by running the following command:

    ```
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
    ```
13. You can verify that the `unsupportedConfigOverrides` section is removed from the object by running the following command:

    ```
    $ oc get etcd/cluster -oyaml
    ```
14. If you are using single-node OpenShift, restart the node. Otherwise, you might encounter the following error in the etcd cluster Operator:

    **Example output**

    ```
    EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
    ```

**Verification**

1. Verify that all etcd pods are running properly by running the following command:

   ```
   $ oc -n openshift-etcd get pods -l k8s-app=etcd
   ```

   **Example output**

   ```
   etcd-openshift-control-plane-0      5/5     Running     0     105m
   etcd-openshift-control-plane-1      5/5     Running     0     107m
   etcd-openshift-control-plane-2      5/5     Running     0     103m
   ```

   If the output from the previous command only lists two pods, you can manually force an etcd redeployment. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:

   ```
   $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
   ```

   The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.

   To verify there are exactly three etcd members, connect to the running etcd container, passing in the name of a pod that was not on the affected node. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:

   ```
   $ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
   ```
2. View the member list by running the following command:

   ```
   sh-4.2# etcdctl member list -w table
   ```

   **Example output**

   ```
   +------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
   |        ID        | STATUS  |        NAME        |        PEER ADDRS         |       CLIENT ADDRS        |    IS LEARNER    |
   +------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
   | 7a8197040a5126c8 | started | openshift-control-plane-2 | https://192.168.10.11:2380 | https://192.168.10.11:2379 |   false |
   | 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380 | https://192.168.10.10:2379 |   false |
   | cc3830a72fc357f9 | started | openshift-control-plane-0 | https://192.168.10.9:2380 | https://192.168.10.9:2379 |     false |
   +------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
   ```

   Note

   If the output from the previous command lists more than three etcd members, you must carefully remove the unwanted member.
3. Verify that all etcd members are healthy by running the following command:

   ```
   # etcdctl endpoint health --cluster
   ```

   **Example output**

   ```
   https://192.168.10.10:2379 is healthy: successfully committed proposal: took = 8.973065ms
   https://192.168.10.9:2379 is healthy: successfully committed proposal: took = 11.559829ms
   https://192.168.10.11:2379 is healthy: successfully committed proposal: took = 11.665203ms
   ```
4. Validate that all nodes are at the latest revision by running the following command:

   ```
   $ oc get etcd -o=jsonpath='{range.items[0].status.conditions[?(@.type=="NodeInstallerProgressing")]}{.reason}{"\n"}{.message}{"\n"}'
   ```

   ```
   AllNodesAtLatestRevision
   ```

### [4.4. Disaster recovery](#etcd-disaster-recovery) Copy linkLink copied to clipboard!

To return your cluster to a working state after quorum loss, control plane failure, or expired certificates, follow the disaster recovery procedures for your situation. You can restore etcd quorum, restore the cluster from an etcd snapshot, or recover from expired control plane certificates.

Important

Disaster recovery requires you to have at least one healthy control plane host.

#### [4.4.1. Restoring etcd quorum for high availability clusters](#dr-restoring-etcd-quorum-ha_etcd-disaster-recovery) Copy linkLink copied to clipboard!

You can restore etcd quorum on high availability (HA) clusters by running the `quorum-restore.sh` script on a recovery host. Restored quorum returns the OpenShift Container Platform API to read/write mode when quorum loss takes the cluster offline.

The `quorum-restore.sh` script creates a new single-member etcd cluster from the local data directory on the recovery host. No prior backup is required.

For high availability (HA) clusters, a three-node HA cluster requires you to shut down etcd on two hosts to avoid a cluster split. On four-node and five-node HA clusters, you must shut down three hosts. Quorum requires a majority of nodes. The minimum number of nodes required for quorum on a three-node HA cluster is two. On four-node and five-node HA clusters, the minimum number of nodes required for quorum is three. If you start a new cluster from backup on your recovery host, the other etcd members might still be able to form quorum and continue service.

Warning

You might experience data loss if the host that runs the restoration does not have all data replicated to it.

Important

Quorum restoration should not be used to decrease the number of nodes outside of the restoration process. Decreasing the number of nodes results in an unsupported cluster configuration.

**Prerequisites**

* You have SSH access to the node used to restore quorum.

**Procedure**

1. Select a control plane host to use as the recovery host. You run the restore operation on this host.

   1. List the running etcd pods by running the following command:

      ```
      $ oc get pods -n openshift-etcd -l app=etcd --field-selector="status.phase==Running"
      ```
   2. Choose a pod and run the following command to obtain its IP address:

      ```
      $ oc exec -n openshift-etcd <etcd-pod> -c etcdctl -- etcdctl endpoint status -w table
      ```

      Note the IP address of a member that is not a learner and has the highest Raft index.
   3. List nodes by running the following command:

      ```
      $ oc get nodes -o jsonpath='{range .items[*]}[{.metadata.name},{.status.addresses[?(@.type=="InternalIP")].address}]{end}'
      ```

      Note the node name that corresponds to the IP address of the chosen etcd member.
2. Using SSH, connect to the chosen recovery node and run the following command to restore etcd quorum:

   ```
   $ sudo -E /usr/local/bin/quorum-restore.sh
   ```

   After a few minutes, the nodes that went down are automatically synchronized with the node that the recovery script was run on. Any remaining online nodes automatically rejoin the new etcd cluster created by the `quorum-restore.sh` script. This process takes a few minutes.
3. Exit the SSH session.
4. Return to a three-node configuration if any nodes are offline. Repeat the following steps for each node that is offline to delete and re-create them. After the machines are re-created, a new revision is forced and etcd automatically scales up.

   * If you use a user-provisioned bare-metal installation, you can re-create a control plane machine by using the same method that you used to originally create it. For more information, see "Installing a user-provisioned cluster on bare metal".

     Warning

     Do not delete and re-create the machine for the recovery host.
   * If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps:

     Warning

     Do not delete and re-create the machine for the recovery host.

     For bare-metal installations on installer-provisioned infrastructure, control plane machines are not re-created. For more information, see "Replacing a bare-metal control plane node".

     1. In a terminal that has access to the cluster as a `cluster-admin` user, obtain the machine for one of the offline nodes by running the following command:

        ```
        $ oc get machines -n openshift-machine-api -o wide
        ```

        **Example output**

        ```
        NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
        clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped
        clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-143-125.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
        clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-154-194.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba  running
        clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
        clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
        clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
        ```

        In the example output, `clustername-8qw5l-master-0` is the control plane machine for the offline node, `ip-10-0-131-183.ec2.internal`.
     2. Delete the machine of the offline node by running the following command:

        ```
        $ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0
        ```

        Specify the name of the control plane machine for the offline node.

        A new machine is automatically provisioned after deleting the machine of the offline node.
5. Verify that a new machine has been created by running the following command:

   ```
   $ oc get machines -n openshift-machine-api -o wide
   ```

   **Example output**

   ```
   NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
   clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-143-125.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
   clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-154-194.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba  running
   clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-173-171.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8  running
   clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
   clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
   clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
   ```

   In the example output, `clustername-8qw5l-master-3` is being created and is ready after the phase changes from `Provisioning` to `Running`.

   It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically synchronizes when the machine or node returns to a healthy state.
6. For each node that is offline, repeat the previous steps to delete and re-create the node.
7. Wait until the control plane recovers by running the following command:

   ```
   $ oc adm wait-for-stable-cluster
   ```

   Note

   It can take up to 15 minutes for the control plane to recover.

**Troubleshooting**

* If you see no progress rolling out the etcd static pods, you can force redeployment from the etcd cluster Operator by running the following command:

  ```
  $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
  ```

#### [4.4.2. About restoring to an earlier cluster state](#dr-scenario-2-restoring-cluster-state-about_etcd-disaster-recovery) Copy linkLink copied to clipboard!

To assess restore risks before you choose rollback as a last resort, review how an etcd snapshot restore affects your OpenShift Container Platform cluster, including Operators, workloads, and persistent storage.

You can use an etcd backup to restore your cluster to an earlier state. This can be used to recover from the following situations:

* The cluster has lost the majority of control plane hosts and quorum.
* An administrator has deleted something critical and must restore to recover the cluster.

If applicable, you might also need to recover from expired control plane certificates.

Warning

Restoring to an earlier cluster state is a destructive and destabilizing action to take on a running cluster. This should only be used as a last resort.

If you cannot retrieve data using the Kubernetes API server, then etcd is available and you should not restore using an etcd backup.

Restoring etcd effectively takes a cluster back in time and all clients experience a conflicting, parallel history. This can impact the behavior of watching components like kubelets, Kubernetes controller managers, persistent volume controllers, and OpenShift Container Platform Operators, including the network Operator.

It can cause Operator churn when the content in etcd does not match the actual content on disk, causing Operators for the Kubernetes API server, Kubernetes controller manager, Kubernetes scheduler, and etcd to get stuck when files on disk conflict with content in etcd. This can require manual actions to resolve the issues.

In extreme cases, the cluster can lose track of persistent volumes, delete critical workloads that no longer exist, reimage machines, and rewrite CA bundles with expired certificates.

#### [4.4.3. Restoring to an earlier cluster state for a single node](#dr-restoring-cluster-state-sno_etcd-disaster-recovery) Copy linkLink copied to clipboard!

To restore your OpenShift Container Platform cluster on a single node, use a saved etcd snapshot to roll back to an earlier state after quorum loss or critical data deletion.

Important

When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.22.2 cluster must use an etcd backup that was taken from 4.22.2.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file.
* You have SSH access to control plane hosts.
* You have a backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.

**Procedure**

1. Use SSH to connect to the single node and copy the etcd backup to the `/home/core` directory by running the following command:

   ```
   $ cp <etcd_backup_directory> /home/core
   ```
2. To restore the cluster from an earlier backup on the single node, run the following command:

   ```
   $ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd_backup_directory>
   ```
3. Exit the SSH session.
4. Monitor the recovery progress of the control plane by running the following command:

   ```
   $ oc adm wait-for-stable-cluster
   ```

   Note

   It can take up to 15 minutes for the control plane to recover.

#### [4.4.4. Restoring to an earlier cluster state for more than one node](#dr-scenario-2-restoring-cluster-state_etcd-disaster-recovery) Copy linkLink copied to clipboard!

To restore your OpenShift Container Platform cluster with more than one control plane node to an earlier state, use a saved etcd snapshot after quorum loss or critical data deletion.

For a Two-Node with Fencing (TNF) setup, a single surviving node can continue to operate in degraded mode. Use a saved etcd backup to restore an earlier cluster state if only one node is operational, or when both nodes have failed and you need to restart the cluster from a known safe state. In both cases, perform the restore procedure on a single node. The peer node automatically synchronizes data with the restored node when it rejoins the cluster.

Before you restore from backup on the recovery host, shut down etcd on enough control plane nodes so the remaining members cannot form a quorum:

* Shut down etcd on 2 hosts in a 3-node cluster.
* Shut down etcd on 3 hosts in a 4-node or 5-node cluster.

If too few hosts are shut down, the other etcd members might still form a quorum and continue service while you restore.

Note

If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in the control plane machine set troubleshooting topic for an etcd recovery procedure. For OpenShift Container Platform on a single node, follow the procedure to restore to an earlier cluster state for a single node.

Important

When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.22.2 cluster must use an etcd backup that was taken from 4.22.2.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file, like the one that was used during installation.
* You have a healthy control plane host to use as the recovery host.
* You have SSH access to control plane hosts.
* You have a backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.
* Control plane nodes are accessible or bootable.

Important

For non-recovery control plane nodes, it is not required to establish SSH connectivity or to stop the static pods. You can delete and re-create other non-recovery, control plane machines, one by one.

**Procedure**

1. Select a control plane host to use as the recovery host. This is the host that you run the restore operation on.
2. Establish SSH connectivity to each of the control plane nodes, including the recovery host.

   `kube-apiserver` becomes inaccessible after the restore process starts, so you cannot access the control plane nodes. Establish SSH connectivity to each control plane host in a separate terminal.

   Important

   If you do not complete this step, you cannot access the control plane hosts to complete the restore procedure, and you cannot recover your cluster from this state.
3. Using SSH, connect to each control plane node to disable etcd by running the following command:

   ```
   $ sudo -E /usr/local/bin/disable-etcd.sh
   ```
4. Copy the etcd backup directory to the recovery control plane host.

   This procedure assumes that you copied the `backup` directory containing the etcd snapshot and the resources for the static pods to the `/home/core/` directory of your recovery control plane host.
5. Use SSH to connect to the recovery host. Restore the cluster from an earlier backup by running the following command:

   ```
   $ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd-backup-directory>
   ```
6. Exit the SSH session.
7. When the API responds, turn off the etcd Operator quorum guard by running the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
   ```

   Important

   For a TNF setup, do not:

   * Change the etcd Operator quorum setting.
   * Turn the etcd Operator quorum off.
   * Turn the etcd Operator quorum back on.
8. Monitor the recovery progress of the control plane by running the following command:

   ```
   $ oc adm wait-for-stable-cluster
   ```

   Note

   It can take up to 15 minutes for the control plane to recover. Wait for the control plane to recover before using the next step.
9. Enable the quorum guard by running the following command:

   ```
   $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
   ```

**Troubleshooting**

If the etcd static pods do not roll out, you can manually force an etcd redeployment from the `cluster-etcd-operator` by running the following command:

```
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
```

#### [4.4.5. Issues and workarounds for restoring a persistent storage state](#dr-scenario-cluster-state-issues_etcd-disaster-recovery) Copy linkLink copied to clipboard!

To restore workloads safely after an etcd snapshot restore, identify and resolve outdated persistent storage references, including volumes, credentials, attachments, and devices on your OpenShift Container Platform cluster.

If your OpenShift Container Platform cluster uses persistent storage of any form, a state of the cluster is typically stored outside etcd. When you restore from an etcd backup, the status of the workloads in OpenShift Container Platform is also restored. However, if the etcd snapshot is old, the status might be invalid or outdated.

Important

The contents of persistent volumes (PVs) are never part of the etcd snapshot. When you restore an OpenShift Container Platform cluster from an etcd snapshot, non-critical workloads might gain access to critical data, or vice-versa.

The following are some example scenarios that produce an out-of-date status:

* MySQL database is running in a pod backed up by a PV object. Restoring OpenShift Container Platform from an etcd snapshot does not bring back the volume on the storage provider, and does not produce a running MySQL pod, despite the pod repeatedly attempting to start. You must manually restore this pod by restoring the volume on the storage provider, and then editing the PV to point to the new volume.
* Pod P1 is using volume A, which is attached to node X. If the etcd snapshot is taken while another pod uses the same volume on node Y, then when the etcd restore is performed, pod P1 might not be able to start correctly due to the volume still being attached to node Y. OpenShift Container Platform is not aware of the attachment, and does not automatically detach it. When this occurs, the volume must be manually detached from node Y so that the volume can attach on node X, and then pod P1 can start.
* Cloud provider or storage provider credentials were updated after the etcd snapshot was taken. This causes any CSI drivers or Operators that depend on those credentials to not work. You might have to manually update the credentials required by those drivers or Operators.
* A device is removed or renamed from OpenShift Container Platform nodes after the etcd snapshot is taken. The Local Storage Operator creates symlinks for each PV that it manages from `/dev/disk/by-id` or `/dev` directories. This situation might cause the local PVs to refer to devices that no longer exist.

  To fix this problem, an administrator must:

  1. Manually remove the PVs with invalid devices.
  2. Remove symlinks from respective nodes.
  3. Delete `LocalVolume` or `LocalVolumeSet` objects. For more information, see "Deleting the Local Storage Operator resources".

#### [4.4.6. Recovering from expired control plane certificates](#dr-scenario-3-recovering-expired-certs_etcd-disaster-recovery) Copy linkLink copied to clipboard!

You can restore kubelet certificates by manually approving pending `node-bootstrapper` certificate signing requests (CSRs) and, on user-provisioned installations, kubelet serving CSRs. Approved CSRs return nodes to a healthy state after control plane certificates expire.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

**Procedure**

1. Get the list of current CSRs by running the following command:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE    SIGNERNAME                                    REQUESTOR                                                                   CONDITION
   csr-2s94x   8m3s   kubernetes.io/kubelet-serving                 system:node:<node_name>                                                     Pending
   csr-4bd6t   8m3s   kubernetes.io/kubelet-serving                 system:node:<node_name>                                                     Pending
   csr-4hl85   13m    kubernetes.io/kube-apiserver-client-kubelet   system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   csr-zhhhp   3m8s   kubernetes.io/kube-apiserver-client-kubelet   system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   ...
   ```

   In the example output, CSRs with a `SIGNERNAME` of `kubernetes.io/kubelet-serving` are kubelet serving CSRs. You see this CSR type on user-provisioned installations. CSRs with a `SIGNERNAME` of `kubernetes.io/kube-apiserver-client-kubelet` and a `node-bootstrapper` requestor are `node-bootstrapper` CSRs that you must approve to restore kubelet certificates.
2. Review the details of a CSR to verify that it is valid by running the following command:

   ```
   $ oc describe csr <csr_name>
   ```

   `<csr_name>` is the name of a CSR from the list of current CSRs.
3. Approve each valid `node-bootstrapper` CSR by running the following command:

   ```
   $ oc adm certificate approve <csr_name>
   ```
4. For user-provisioned installations, approve each valid kubelet serving CSR by running the following command:

   ```
   $ oc adm certificate approve <csr_name>
   ```

#### [4.4.7. Testing restore procedures](#dr-testing-restore-procedures_etcd-disaster-recovery) Copy linkLink copied to clipboard!

You can test your cluster restore workflow by simulating etcd failure on nonrecovery nodes and restoring from backup. Use this test to confirm that your etcd backup and restore process works as expected.

Warning

You must have SSH access to the cluster. Without SSH access, you cannot disable etcd or manage the `kubelet` service on nonrecovery nodes.

**Prerequisites**

* You have SSH access to control plane hosts.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Use SSH to connect to each of your nonrecovery nodes to disable etcd and the `kubelet` service:

   1. Disable etcd by running the following command:

      ```
      $ sudo /usr/local/bin/disable-etcd.sh
      ```
   2. Delete variable data for etcd by running the following command:

      ```
      $ sudo rm -rf /var/lib/etcd
      ```
   3. Disable the `kubelet` service by running the following command:

      ```
      $ sudo systemctl disable kubelet.service
      ```
2. Exit every SSH session.
3. Ensure that your nonrecovery nodes are in a `NOT READY` state by running the following command:

   ```
   $ oc get nodes
   ```
4. Restore your cluster to an earlier cluster state using an etcd backup. For more information, see "Restoring to an earlier cluster state".
5. After you restore the cluster and the API responds, use SSH to connect to each nonrecovery node and enable the `kubelet` service by running the following command:

   ```
   $ sudo systemctl enable kubelet.service
   ```
6. Exit every SSH session.
7. Verify that your nodes return to the `READY` state by running the following command:

   ```
   $ oc get nodes
   ```
8. Verify that etcd is available by running the following command:

   ```
   $ oc get pods -n openshift-etcd
   ```

## [Chapter 5. Enabling etcd encryption](#etcd-encrypt) Copy linkLink copied to clipboard!

Encrypt and decrypt etcd data in OpenShift Container Platform to protect sensitive cluster resources such as secrets, config maps, and OAuth tokens.

### [5.1. etcd encryption](#about-etcd_etcd-encrypt) Copy linkLink copied to clipboard!

You can encrypt sensitive resource data in etcd to provide an additional layer of protection if an etcd backup or storage data is exposed.

By default, etcd data is not encrypted in OpenShift Container Platform. You can enable etcd encryption for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties.

When you enable etcd encryption, the following OpenShift API server and Kubernetes API server resources are encrypted:

* Secrets
* Config maps
* Routes
* OAuth access tokens
* OAuth authorize tokens

When you enable etcd encryption, encryption keys are created. You must have these keys to restore from an etcd backup.

Note

etcd encryption only encrypts values, not keys. Resource types, namespaces, and object names are unencrypted.

If etcd encryption is enabled during a backup, the `static_kuberesources_<datetimestamp>.tar.gz` file contains the encryption keys for the etcd snapshot. For security reasons, store this file separately from the etcd snapshot. However, this file is required to restore a previous state of etcd from the respective etcd snapshot.

### [5.2. Supported encryption types](#etcd-encryption-types_etcd-encrypt) Copy linkLink copied to clipboard!

OpenShift Container Platform supports AES-CBC and AES-GCM encryption types to protect etcd data at rest.

The following encryption types are supported for encrypting etcd data in OpenShift Container Platform:

AES-CBC
:   Uses AES-CBC with PKCS#7 padding and a 32-byte key to perform the encryption.

AES-GCM
:   Uses AES-GCM with a random nonce and a 32-byte key to perform the encryption.

The etcd encryption keys are rotated every 7 days. Up to 10 historical encryption keys are preserved after rotation to help decrypt older backups and provide an extra layer of data recovery safety.

### [5.3. Enabling etcd encryption](#enabling-etcd-encryption_etcd-encrypt) Copy linkLink copied to clipboard!

Enable etcd encryption to protect sensitive cluster resources such as secrets, config maps, routes, and OAuth tokens at rest.

Warning

Do not back up etcd resources until the initial encryption process is completed. If the encryption process is not completed, the backup might be only partially encrypted.

After you enable etcd encryption, several changes can occur:

* The etcd encryption might affect the memory consumption of a few resources.
* You might notice a transient effect on backup performance because the leader must serve the backup.
* A disk I/O can affect the node that receives the backup state.

You can encrypt the etcd database in either AES-GCM or AES-CBC encryption.

Note

To migrate your etcd database from one encryption type to the other, you can modify the API server’s `spec.encryption.type` field. Migration of the etcd data to the new encryption type occurs automatically.

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Modify the `APIServer` object:

   ```
   $ oc edit apiserver
   ```
2. Set the `spec.encryption.type` field to `aesgcm` or `aescbc`:

   ```
   spec:
     encryption:
       type: aesgcm
   ```

   * The `aesgcm` value specifies AES-GCM encryption. Alternatively, set the `type` field to `aescbc` for AES-CBC encryption.
3. Save the file to apply the changes.

   The encryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of the etcd database.

**Verification**

* Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully encrypted:

  ```
  $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
  ```

  The output shows `EncryptionCompleted` upon successful encryption:

  ```
  EncryptionCompleted
  All resources encrypted: routes.route.openshift.io
  ```

  If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.
* Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully encrypted:

  ```
  $ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
  ```

  The output shows `EncryptionCompleted` upon successful encryption:

  ```
  EncryptionCompleted
  All resources encrypted: secrets, configmaps
  ```

  If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.
* Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully encrypted:

  ```
  $ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
  ```

  The output shows `EncryptionCompleted` upon successful encryption:

  ```
  EncryptionCompleted
  All resources encrypted: oauthaccesstokens.oauth.openshift.io, oauthauthorizetokens.oauth.openshift.io
  ```

  If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

### [5.4. Disabling etcd encryption](#disabling-etcd-encryption_etcd-encrypt) Copy linkLink copied to clipboard!

Disable etcd encryption when you no longer need to encrypt sensitive cluster resources at rest.

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Modify the `APIServer` object:

   ```
   $ oc edit apiserver
   ```
2. Set the `encryption` field type to `identity`:

   ```
   spec:
     encryption:
       type: identity
   ```

   The `identity` value specifies that no encryption is performed. This is the default value.
3. Save the file to apply the changes.

   The decryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of your cluster.

**Verification**

* Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully decrypted:

  ```
  $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
  ```

  The output shows `DecryptionCompleted` upon successful decryption:

  ```
  DecryptionCompleted
  Encryption mode set to identity and everything is decrypted
  ```

  If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.
* Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully decrypted:

  ```
  $ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
  ```

  The output shows `DecryptionCompleted` upon successful decryption:

  ```
  DecryptionCompleted
  Encryption mode set to identity and everything is decrypted
  ```

  If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.
* Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully decrypted:

  ```
  $ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
  ```

  The output shows `DecryptionCompleted` upon successful decryption:

  ```
  DecryptionCompleted
  Encryption mode set to identity and everything is decrypted
  ```

  If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

## [Chapter 6. External encryption key management](#external-encryption-key-management) Copy linkLink copied to clipboard!

### [6.1. Kubernetes Key Management Service (KMS) v2 on OpenShift Container Platform](#kms_v2_index) Copy linkLink copied to clipboard!

You can configure Kubernetes Key Management Service (KMS) v2 on OpenShift Container Platform to centralize encryption key management and meet regulatory compliance requirements.

Important

Kubernetes KMS v2 is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [6.1.1. About Kubernetes KMS v2 encryption](#kms-about_kms-v2-index) Copy linkLink copied to clipboard!

Kubernetes KMS v2 uses external Key Management Services to encrypt etcd data and centralize key management.

Kubernetes KMS v2 provides:

* Customer-managed encryption keys that never leave the external KMS
* Centralized key management and auditing
* Regulatory compliance support

##### [6.1.1.1. Encrypted resources](#kms-encrypted-resources_kms-v2-index) Copy linkLink copied to clipboard!

When you enable KMS encryption, OpenShift Container Platform encrypts the following sensitive resources in etcd:

* Secrets
* ConfigMaps
* Routes
* OAuth access tokens
* OAuth authorize tokens

Note

Resource types, namespaces, and object names are not encrypted.

#### [6.1.2. KMS Technology Preview limitations](#kms-technology-preview-phases_kms-v2-index) Copy linkLink copied to clipboard!

Review the current limitations of Kubernetes KMS v2 to plan deployments and avoid unsupported configurations in OpenShift Container Platform 4.21 or later.

##### [6.1.2.1. Current limitations](#kms-current-limitations_kms-v2-index) Copy linkLink copied to clipboard!

* Plugins require manual installation on each control plane node
* Plugins must listen at `unix:///var/run/kmsplugin/kms.sock`
* Only one KMS plugin can run at a time
* KMS-to-KMS migration requires intermediate migration to `identity` or `aescbc`

### [6.2. Configuring Kubernetes KMS v2](#kms-configuring) Copy linkLink copied to clipboard!

You can configure external KMS encryption for etcd to centralize key management and meet regulatory compliance requirements.

Important

Kubernetes KMS v2 is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [6.2.1. Enable KMS encryption](#kms-configuring_kms-configuring) Copy linkLink copied to clipboard!

You can enable external Key Management Service (KMS) encryption for etcd data to centralize key management and meet compliance requirements.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have enabled the `TechPreviewNoUpgrade` feature set to enable the `KMSEncryption` feature gate.
* You have a `HashiCorp Vault Enterprise` instance accessible from your control plane nodes. Vault Community Edition is not available.
* Your control plane nodes have network access to the Vault server.
* You have configured your Vault instance with:

  + Transit secrets engine enabled at the default `transit/` mount path
  + Encryption key created with type `aes256-gcm96` (recommended for FIPS 140-3 compliance)
  + Vault policy allowing the Kubernetes KMS v2 plugin to encrypt, decrypt, and read key information
  + Authentication method (token, `AppRole`, or `userpass`) configured with the policy attached

The Kubernetes KMS v2 plugin requires a Vault policy with the following capabilities:

```
path "transit/encrypt/kms-key" {
  capabilities = ["update"]
}

path "transit/decrypt/kms-key" {
  capabilities = ["update"]
}

path "transit/keys/kms-key" {
  capabilities = ["read"]
}

path "auth/token/lookup-self" {
  capabilities = ["read"]
}
```

Replace `kms-key` with your Vault Transit key name if using a different name.

Important

Create an etcd backup before enabling KMS encryption.

**Procedure**

1. Deploy the KMS plugin on each control plane host as a static pod:

   * Configure the plugin to listen at `unix:///var/run/kmsplugin/kms.sock`
   * For your static pod, mount `/var/run/kmsplugin` as `hostPath`
   * Configure KMS provider connection details and authentication credentials

   The following steps show how to deploy the `HashiCorp` Vault KMS plugin as a static pod.
2. Create a static pod manifest file:

   ```
   $ cat > /tmp/vault-kms-plugin.yaml <<'EOF'
   apiVersion: v1
   kind: Pod
   metadata:
     name: vault-kms-plugin
     namespace: kube-system
     labels:
       app: vault-kms-plugin
       tier: control-plane
   spec:
     priorityClassName: system-node-critical
     hostNetwork: true
     containers:
     - name: vault-kms-plugin
       image: quay.io/redhat-isv-containers/698df066f8d1ddf179c15ef9:<version>
       command:
       - /vault-kubernetes-kms
       - -vault-address=<https://vault.example.com:8200>
       - -<vault_namespace>=admin
       - -auth-method=userpass
       - -userpass-username=<vault_username>
       - -userpass-password=<vault_password>
       - -transit-mount=transit
       - -transit-key=kms-key
       - -socket=unix:///var/run/kmsplugin/kms.sock
       volumeMounts:
       - name: kmsplugin
         mountPath: /var/run/kmsplugin
       resources:
         requests:
           cpu: 100m
           memory: 128Mi
         limits:
           cpu: 500m
           memory: 512Mi
       securityContext:
         privileged: true
     volumes:
     - name: kmsplugin
       hostPath:
         path: /var/run/kmsplugin
         type: DirectoryOrCreate
   EOF
   ```

   Replace the following values to match your environment:

   <version>
   :   The Vault KMS plugin image version tag. Use `0.1.0-beta-ubi`.

   <vault\_username>
   :   Your Vault username for authentication.

   <vault\_password>
   :   Your Vault password for authentication.

   <https://vault.example.com:8200>
   :   The Vault address. Update this field to match your Vault server URL.

   <vault\_namespace>
   :   Optional field.

       The manifest uses the Red Hat certified container image from Quay.io (`quay.io/redhat-isv-containers/698df066f8d1ddf179c15ef9`), which is the recommended image for OpenShift Container Platform.

       Note

       Alternatively, you can use the [HashiCorp image from Docker Hub](https://hub.docker.com/r/hashicorp/vault-kube-kms) by replacing the image field with `docker.io/hashicorp/vault-kube-kms:0.1.0-beta-ubi`.
3. Deploy the static pod manifest to each control plane node by running the following commands:

   ```
   $ MANIFEST=$(cat /tmp/vault-kms-plugin.yaml | base64)
   $ for node in $(oc get nodes --selector=node-role.kubernetes.io/master -o name | cut -d/ -f2); do
       echo "Deploying to $node..."
       oc debug node/$node -- chroot /host bash -c \
         "echo '$MANIFEST' | base64 -d > /etc/kubernetes/manifests/vault-kms-plugin.yaml"
     done
   ```

   The kubelet automatically detects and starts static pods from `/etc/kubernetes/manifests/`.
4. Verify the static pods are running by entering the following command:

   ```
   $ oc get pods -n kube-system -o wide | grep vault-kms
   ```

   **Example output**

   ```
   vault-kms-plugin-ip-10-0-16-7.compute.internal    1/1  Running  0  2m  10.0.16.7
   vault-kms-plugin-ip-10-0-32-93.compute.internal   1/1  Running  0  2m  10.0.32.93
   vault-kms-plugin-ip-10-0-69-106.compute.internal  1/1  Running  0  2m  10.0.69.106
   ```

   Static pod names include the node name as a suffix. You should see one pod per control plane node.
5. Verify the socket exists on a control plane node by entering the following command:

   ```
   $ oc debug node/<node_name> -- chroot /host ls -la /var/run/kmsplugin/kms.sock
   ```

   **Example output**

   ```
   srwxr-xr-x. 1 root root 0 <timestamp> /var/run/kmsplugin/kms.sock
   ```

   Note

   Static pods are managed by kubelet on each node and cannot be deleted with `oc delete pod`. To remove a static pod, delete the manifest file from `/etc/kubernetes/manifests/` on each control plane node.
6. Edit the `APIServer` custom resource by entering the following command:

   ```
   $ oc edit apiserver cluster
   ```
7. Add the KMS configuration to the `spec.encryption` section:

   ```
   apiVersion: config.openshift.io/v1
   kind: APIServer
   metadata:
     name: cluster
   spec:
     encryption:
       type: KMS
   ```
8. Save and exit.

   Migration begins automatically. The `kube-apiserver`, `openshift-apiserver` and `oauth-apiserver` Operators will restart and roll out new revisions.

   Note

   The `openshift-apiserver` and `authentication` operators typically complete migration in 5-10 minutes. The `kube-apiserver` operator uses a conservative rollout strategy, updating one control plane node at a time and waiting for health checks before proceeding to the next node. This process can take 30 minutes or longer depending on cluster load.

**Verification**

1. Verify the encryption type by entering the following command:

   ```
   $ oc get apiserver cluster -o jsonpath='{.spec.encryption.type}'
   ```

   Output should show `KMS`.
2. Monitor the `kube-apiserver` rollout progress by entering the following command:

   ```
   $ oc get kubeapiserver cluster -o jsonpath='{.status.nodeStatuses}' | jq -r '.[] | "\(.nodeName | split(".")[0]): current=\(.currentRevision) target=\(.targetRevision)"'
   ```

   **Example output during rollout**

   ```
   ip-10-0-16-166: current=10 target=0
   ip-10-0-32-93: current=9 target=10
   ip-10-0-69-106: current=9 target=0
   ```

   The operator rolls out one node at a time. When all nodes show the same `current` revision and `target` is `0`, the rollout is complete.
3. Check the encryption migration status by entering the following command:

   ```
   $ oc get kubeapiserver cluster -o jsonpath='{.status.conditions[?(@.type=="Encrypted")]}' | jq .
   ```

   **Example output when complete**

   ```
   {
     "lastTransitionTime": "2026-05-15T17:39:02Z",
     "message": "All resources encrypted: secrets, configmaps",
     "reason": "EncryptionCompleted",
     "status": "True",
     "type": "Encrypted"
   }
   ```

   Wait for `reason` to show `EncryptionCompleted` before proceeding to verify encryption in etcd.
4. Verify secrets are encrypted in etcd:

   Warning

   Wait for the `kube-apiserver` rollout to complete on all control plane nodes before verifying encryption. During the rollout, API requests are distributed across nodes, and secrets created while some nodes are still on an earlier revision will not be encrypted with Kubernetes KMS v2.

   1. Create a test secret by entering the following command:

      ```
      $ oc create secret generic test-secret --from-literal=key=value -n default
      ```
   2. Get an etcd pod name by entering the following command:

      ```
      $ oc get pods -n openshift-etcd -l app=etcd -o name | head -1
      ```
   3. Check the secret data in etcd by entering the following command:

      ```
      $ oc exec -n openshift-etcd <etcd_pod_name> -- etcdctl get /kubernetes.io/secrets/default/test-secret --print-value-only | hexdump -C | head -1
      ```

      Output should begin with `k8s:enc:kms:v2:` followed by encrypted binary data.
   4. Delete the test secret by entering the following command:

      ```
      $ oc delete secret test-secret -n default
      ```

#### [6.2.2. Rotate the Vault encryption key](#kms-rotating-encryption-key_kms-configuring) Copy linkLink copied to clipboard!

You can rotate your Vault Transit encryption key to generate a new key version while maintaining access to data encrypted with earlier versions.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to your Vault instance with permissions to rotate keys.
* Kubernetes KMS v2 encryption is enabled and functioning.

**Procedure**

1. Rotate the Vault encryption key by entering the following command:

   ```
   $ vault write -f transit/keys/kms-key/rotate
   ```

   Vault creates a new key version while maintaining earlier versions for decryption. The API server automatically uses the correct key version for each secret.
2. Verify the new key version by entering the following command:

   ```
   $ vault read transit/keys/kms-key
   ```

   The `latest_version` field shows the current key version number.

**Verification**

* Verify that existing secrets remain accessible by entering the following command:

  ```
  $ oc get secret -A
  ```

All secrets should be readable without errors.

Note

Existing encrypted secrets do not need re-encryption. Vault maintains all key versions and automatically uses the appropriate version for decryption.

#### [6.2.3. Migrate from local encryption to KMS encryption](#kms-migrating-from-local-encryption_kms-configuring) Copy linkLink copied to clipboard!

You can migrate from local etcd encryption to external KMS encryption to centralize key management and improve compliance.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have enabled the `TechPreviewNoUpgrade` feature set to enable the `KMSEncryption` feature gate.
* Your cluster is currently using `aescbc` or `aesgcm` encryption.
* You have deployed the KMS plugin on all control plane nodes.
* Control plane nodes have network access to the KMS provider.

Important

Create an etcd backup before migrating.

**Procedure**

1. Back up the current etcd encryption configuration by entering the following command:

   ```
   $ oc get apiserver cluster -o yaml > apiserver-backup.yaml
   ```
2. Edit the APIServer custom resource by entering the following command:

   ```
   $ oc edit apiserver cluster
   ```
3. Change the encryption type from `aescbc` or `aesgcm` to `KMS`:

   ```
   apiVersion: config.openshift.io/v1
   kind: APIServer
   metadata:
     name: cluster
   spec:
     encryption:
       type: KMS
   ```
4. Save and exit.

   Migration starts automatically and typically takes several minutes.
5. Verify migration completion for all API servers by running the following commands:

   ```
   $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{end}'
   ```

   ```
   $ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{end}'
   ```

   ```
   $ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{end}'
   ```

   All outputs should show `EncryptionCompleted`.

#### [6.2.4. Monitor KMS encryption status](#kms-monitoring-status_kms-configuring) Copy linkLink copied to clipboard!

You can monitor KMS encryption status by using Operator and API server logs to verify successful configuration and detect issues.

**Procedure**

1. Check the kube-apiserver operator logs for KMS-related events by entering the following command:

   ```
   $ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i kms
   ```
2. View API server logs for KMS-related events by entering the following command:

   ```
   $ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=100 | grep -i kms
   ```
3. Verify the KMS encryption configuration by entering the following command:

   ```
   $ oc get apiserver cluster -o jsonpath='{.spec.encryption}' | jq
   ```

#### [6.2.5. KMS encryption troubleshooting](#kms-troubleshooting_kms-configuring) Copy linkLink copied to clipboard!

You can diagnose and resolve common KMS encryption issues to maintain secure key management and cluster availability.

##### [6.2.5.1. Invalid KMS configuration](#kms-invalid-configuration_kms-configuring) Copy linkLink copied to clipboard!

**Symptom:** APIServer resource shows validation errors during KMS encryption configuration.

**Diagnosis:** Check kube-apiserver Operator logs:

```
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i "kms\|validation\|error"
```

**Solutions:**

* Verify plugin configuration follows provider requirements
* Ensure all required fields are specified
* Verify plugin is running on all control plane nodes:

  ```
  $ oc debug node/<node_name> -- chroot /host ls -la /var/run/kmsplugin/kms.sock
  ```

##### [6.2.5.2. KMS permissions errors](#kms-permissions-errors_kms-configuring) Copy linkLink copied to clipboard!

**Symptom:** Encryption migration fails with permission errors.

**Diagnosis:** Check Operator and plugin logs:

```
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i "kms\|permission\|access denied"
```

```
$ oc debug node/<node_name> -- chroot /host journalctl -u kms-plugin
```

**Solutions:**

* Verify plugin has valid authentication credentials
* Check if credentials have expired
* Ensure plugin principal has encrypt and decrypt permissions
* Verify KMS provider key policy allows plugin access
* Confirm encryption key is enabled and not scheduled for deletion

##### [6.2.5.3. Expired or deleted KMS key](#kms-expired-deleted-key_kms-configuring) Copy linkLink copied to clipboard!

**Symptom:** API server cannot decrypt secrets when accessing encrypted resources.

**Diagnosis:** Check logs and verify key status:

```
$ oc logs -n openshift-kube-apiserver -l apiserver=true | grep -i "decrypt\|kms.*error"
```

```
$ oc debug node/<node_name> -- chroot /host journalctl -u kms-plugin | grep -i "key\|error"
```

**Solutions:**

* Re-enable the encryption key if disabled
* Restore from backup if key was permanently deleted
* Cancel key deletion if scheduled
* Ensure KMS provider maintains access to previous key versions

Warning

Deleted KMS keys prevent data recovery. Align key retention with backup policies.

##### [6.2.5.4. API server degraded or unavailable](#kms-api-server-degraded_kms-configuring) Copy linkLink copied to clipboard!

**Symptom:** API server becomes degraded or unresponsive after enabling KMS encryption.

**Diagnosis:** Check Operator status and logs:

```
$ oc get clusteroperator kube-apiserver
```

```
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=200 | grep -i kms
```

**Solutions:**

* Check network connectivity between control plane and KMS provider
* Verify network policies, firewalls, and routes allow communication
* Monitor KMS provider rate limits and request increases if needed
* Verify DNS resolution and TLS certificate validation
* Confirm plugin is running on all control plane nodes:

  ```
  $ oc debug node/<node_name> -- chroot /host systemctl status kms-plugin
  ```

##### [6.2.5.5. Encryption migration stuck or slow](#kms-migration-stuck-slow_kms-configuring) Copy linkLink copied to clipboard!

**Symptom:** KMS encryption migration takes unusually long or becomes stuck.

**Diagnosis:** Check Operator status and migration logs:

```
$ oc get clusteroperator kube-apiserver
```

```
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i migration
```

**Solutions:**

* Migration time depends on data size; monitor progress
* Monitor KMS provider audit logs for rate limiting or throttling events
* Check network performance between control plane and KMS provider

##### [6.2.5.6. Collecting debug information](#kms-collecting-debug-info_kms-configuring) Copy linkLink copied to clipboard!

Collect cluster logs:

```
$ oc adm must-gather
```

```
$ oc get apiserver cluster -o yaml > apiserver.yaml
```

```
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator > kube-apiserver-operator.log
```

```
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=500 > kube-apiserver.log
```

Collect KMS provider information:

* KMS plugin logs from control plane nodes
* KMS provider audit logs
* KMS provider key policy and permissions
* Authentication credentials status
* Network connectivity test results

Note

Redact credentials, tokens, and sensitive data before sharing logs.

### [6.3. Disabling Kubernetes KMS v2](#kms-disabling) Copy linkLink copied to clipboard!

You can disable KMS encryption and migrate to local etcd encryption to simplify operations or resolve external KMS connectivity issues.

Important

Kubernetes KMS v2 is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [6.3.1. Disable KMS encryption](#kms-disabling-encryption_kms-disabling) Copy linkLink copied to clipboard!

You can disable external KMS encryption and migrate to local encryption to simplify operations or resolve KMS connectivity issues.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have created an etcd backup.

Warning

Re-encryption of all etcd data will occur.

**Procedure**

1. Edit the `APIServer` custom resource by entering the following command:

   ```
   $ oc edit apiserver cluster
   ```
2. Change the encryption configuration:

   ```
   apiVersion: config.openshift.io/v1
   kind: APIServer
   metadata:
     name: cluster
   spec:
     encryption:
       type: <encryption>
   ```

   Replace `<encryption>` with `aescbc`, `aesgcm`, or `identity`.
3. Save and exit.

   OpenShift Container Platform automatically migrates etcd data. Migration time depends on etcd size and secret count.
4. Monitor the migration progress by entering the following command:

   ```
   $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}{end}'
   ```

   Wait until the output shows `EncryptionCompleted`.
5. Verify kube-apiserver pods rolled out by entering the following command:

   ```
   $ oc get pods -n openshift-kube-apiserver -l app=openshift-kube-apiserver
   ```
6. Remove the static pod manifest from each control plane node by running the following command:

   ```
   $ for node in $(oc get nodes --selector=node-role.kubernetes.io/master -o name | cut -d/ -f2); do
       echo "Removing static pod from $node..."
       oc debug node/$node -- chroot /host \
         rm -f /etc/kubernetes/manifests/vault-kms-plugin.yaml
     done
   ```

   The kubelet automatically stops static pods when their manifest is removed from `/etc/kubernetes/manifests/`.
7. Clean up the socket directory by running the following command:

   ```
   $ for node in $(oc get nodes --selector=node-role.kubernetes.io/master -o name | cut -d/ -f2); do
       oc debug node/$node -- chroot /host rm -rf /var/run/kmsplugin
     done
   ```
8. After backup retention period passes, decommission the KMS key.

**Verification**

1. Verify the encryption type by entering the following command:

   ```
   $ oc get apiserver cluster -o jsonpath='{.spec.encryption.type}'
   ```
2. Verify that a test secret uses the new encryption type:

   1. Create a test secret by entering the following command:

      ```
      $ oc create secret generic encryption-test --from-literal=key=value -n default
      ```
   2. Get an etcd pod name by entering the following command:

      ```
      $ oc get pods -n openshift-etcd -l app=etcd -o name | head -1
      ```
   3. Check the encryption prefix by entering the following command:

      ```
      $ oc exec -n openshift-etcd <etcd_pod_name> -- etcdctl get /kubernetes.io/secrets/default/encryption-test --print-value-only | hexdump -C | head -1
      ```

      Output should begin with `k8s:enc:aescbc:v1:`, `k8s:enc:aesgcm:v1:`, or show readable JSON for `identity`.
   4. Delete the test secret by entering the following command:

      ```
      $ oc delete secret encryption-test -n default
      ```

Note

Do not delete the KMS key until migration completes successfully.

## [Chapter 7. Guidance for clusters that span data centers](#etcd-guidance-span) Copy linkLink copied to clipboard!

Evaluate considerations and metrics for OpenShift Container Platform clusters that span data centers so you can design supported, resilient multisite deployments.

Red Hat strongly recommends a deployment model where OpenShift Container Platform clusters are deployed within a data center, but also acknowledges that there can be scenarios where a provider can use a deployment model where a cluster can span across data centers. This guidance outlines considerations when exploring the use of cluster deployments that span many data centers and describes important metrics that affect the supportability of such deployments. The design of such deployments must adhere to these guidelines for the product to function optimally and to ensure the highest quality of support with the appropriate product support subscriptions.

Warning

A cluster deployment that spans many data centers extends the cluster as a single failure domain across locations and must not be considered a replacement for a disaster recovery plan.

Clusters that span many data centers follow standard Red Hat OpenShift Container Platform support guidance. Review the "Red Hat OpenShift Container Platform Lifecycle" and "Red Hat Production Support Scope of Coverage" for more information.

Do not deploy an OpenShift Container Platform cluster that spans many sites. If you need presence in many data centers or regions, deploy one cluster per region or site, and use tools such as Red Hat Advanced Cluster Management to manage those clusters and deployments.

Some OpenShift Container Platform platforms support many data center deployments. Check the platform-specific product documentation and release notes for details. Other platforms can span data centers, depending on the quality of the network connectivity between nodes. For more information, see "Ensuring reliable etcd performance and scalability".

When you implement a cluster deployment that spans many data centers, implement the practices in "Red Hat High Availability, and Recommended Practices". An alternative to multisite deployments is to deploy one OpenShift Container Platform cluster per site, managed by Red Hat Advanced Cluster Management.

### [7.1. Deployment caveats for spanned clusters](#deployment-caveats-span_etcd-guidance-span) Copy linkLink copied to clipboard!

Review the guidance about the general aspects of a cluster deployment that spans data centers.

Some caveats to remember:

* Although the designs for deployments that span data centers are not bound by any special support requirements, these clusters do have additional inherent complexities that can require additional consideration or support involvement (time to identify, remediate and resolve issues) when compared to a standard single-site cluster.
* Applications might not work well or not work at all in clusters with high Kube API latency or low transaction rates.
* Layered products, such as storage providers, have lower latency requirements. In those cases, the latency limits are dictated by the architectures that are supported by the layered product.
* The failure scenarios are amplified with stretched control planes, and the way they are affected is specific to the deployment. Because of this, before using a deployment that spans data centers on a production environment, the organization should test and document the behavior of the cluster during disruptions such as:

  + When there is a network partition leaving one, two, or all control plane nodes isolated
  + When there are maximum transmission unit (MTU) mismatches on the transport network among the control plane nodes
  + When there is a sustained spike in latency as a Day 2 event towards one or more of the control plane nodes
  + When there is a considerable change in jitter due to network congestion, misconfiguration, or lack of QoS, an intermediate network device causing packet errors, and others
* Clusters deployed across many sites, network infrastructures, storage infrastructures, or other components inherently have a higher number of points of failure. Network disruptions or splits become a larger threat to such clusters especially, putting the nodes at risk of losing contact with each other. These multisite clusters must be designed with the potential for such failures in mind. Organizations deploying multisite clusters should extensively test failure scenarios, and should consider whether the cluster has protection from all points of failure. Consult with Red Hat Support for help to consider the important aspects of a resilient High Availability cluster design.
* In some cases, geographic (GEO) awareness is a requirement or issue that must be solved to minimize latency, so a proper implementation of a Global Service Load Balancing (GSLB) method must be available.

### [7.2. Infrastructure as a Service (IaaS) and cloud provider considerations](#iaas-cloud-provider-considerations-span_etcd-guidance-span) Copy linkLink copied to clipboard!

Review infrastructure and cloud provider constraints for multisite OpenShift Container Platform control planes so you can plan maximum transmission unit (MTU), latency, and storage requirements.

This guidance applies to any infrastructure provider for which OpenShift Container Platform control plane nodes are supported by the user-provisioned infrastructure installer (platform=none) or the agent-based installer (platform=metal) using the ”User Managed Network” option.

Installer-provisioned infrastructure installers are not covered by these guidelines, however, where possible, installer-provisioned infrastructure deployments will span zones or availability zones on cloud or IaaS providers if possible by following these or similar guidelines. This means infrastructure provider-specific integrations will not be available; for example, integration with cloud provider services such as storage services and load balancers. Provider-specific services might still be used as external services.

Using different infrastructure platform providers for control plane nodes is discouraged; for example, mixing nodes across IaaS, cloud, and bare metal as control plane nodes. Consider the following guidelines when such combinations are needed:

* The minimum effective MTU across the infrastructure should be the maximum MTU used for the deployment. Using a lower MTU is acceptable. See "Understanding and Validating MTU setting with OpenShift Container Platform 4.x" for more information.
* The combined disk and network latency and jitter must keep an etcd peer round-trip time (RTT) of less than 100 ms. This is not the same as the network RTT.
* Layered products might have lower latency requirements. In those cases, the latency limits are dictated by the requirements of the architecture supported by the layered product. For example, OpenShift Container Platform cluster deployments that span data centers with Red Hat OpenShift Data Foundation must have a latency requirement of less than 10 ms RTT. For those cases, follow the specific product guidance.
* For guidance on cluster deployments that span data centers using OpenShift Data Foundation as the storage provider, see "Configuring OpenShift Data Foundation Disaster Recovery for OpenShift Workloads".

### [7.3. Site recommendations for multisite clusters](#site-recommendations-span_etcd-guidance-span) Copy linkLink copied to clipboard!

Plan control plane placement across data centers so your cluster maintains quorum when one site becomes unavailable.

Assuming that each site gets one control plane member, you theoretically define three sites, which is what Red Hat recommends. As a result, one data center can go into an inactive state and the cluster still maintains quorum and operational consistency.

When this assumption is not met, give attention to the needed and actual fault tolerance state of the cluster, as it often outlines or dictates the uptime and stability of the deployment.

### [7.4. Requirements for etcd, networking, and storage](#requirements-etcd-hardware-span_etcd-guidance-span) Copy linkLink copied to clipboard!

Apply etcd, networking, and storage requirements for multisite clusters so etcd stays healthy and workloads remain reachable across sites.

Consider the following requirements for clusters that span data centers.

#### [7.4.1. etcd requirements](#etcd-reqs-span_etcd-guidance-span) Copy linkLink copied to clipboard!

There is a large list of factors and considerations that go into planning an etcd cluster deployment. When planning an OpenShift Container Platform cluster that spans data centers, you need to plan for situations that will likely stress or push etcd to the edge of its operational limits.

See "Ensuring reliable etcd performance and scalability" for more details on how to maintain operational capabilities and reduce service-affecting events and instability of the cluster.

#### [7.4.2. Network requirements](#etcd-network-reqs-span_etcd-guidance-span) Copy linkLink copied to clipboard!

The chosen network topology must yield direct IP connectivity between nodes. The lowest effective maximum transmission unit (MTU) across the infrastructure should be the maximum MTU used for the deployment. Using a lower MTU is acceptable.

For more information, see "Understanding and Validating MTU setting with OpenShift Container Platform 4.x". The latency needs are ultimately defined by the services that use the network. See the sections related to etcd and storage for more details on requirements.

In addition to the base networking requirements, you need to think about how applications will be accessed. A top-level Global Service Load Balancing (GSLB) method will be needed outside of OpenShift Container Platform to enable external traffic to connect to the OpenShift Container Platform control plane services and ingress controllers.

#### [7.4.3. Storage requirements](#etcd-storage-reqs-span_etcd-guidance-span) Copy linkLink copied to clipboard!

When you plan a cluster deployment that spans data centers, consider the selected storage integration to ensure that it also meets multisite requirements, as it pertains to accessibility from all sites, fault tolerance, high availability, and so on.

An object storage solution should be used for the registry, and this storage solution needs to be in addition to any PV storage integration used for application volumes or workloads. This object storage solution should also have the same special considerations given to accessibility from all sites, fault tolerance, high availability, and so on.

Because disk I/O is a critical factor in the health of etcd database, it is required that they are deployed on a high speed, low latency media. See etcd guidance on "How etcd peer round trip time affects performance" and "Determining the size of the etcd database and understanding its effects" for more details on the exact requirements to meet.

### [7.5. Workload placement considerations](#workload-placement-considerations-span_etcd-guidance-span) Copy linkLink copied to clipboard!

Place critical workloads across sites in a multisite cluster so you avoid single points of failure during a data center outage.

With multisite clusters, administrators and developers must take special considerations into account to ensure that critical workloads are scheduled or placed based on the proper hardware or hosts within the topology of the cluster. This planning ensures that the applications and services are highly available and fault-tolerant based on the topology of the cluster deployment.

Without this planning, OpenShift Container Platform might schedule workloads on hosts within the cluster so that a single point of failure (SPoF) exists for OpenShift Container Platform infrastructure services and other application services if a data center outage occurs.

## [Legal Notice](#idm140035064915376) Copy linkLink copied to clipboard!

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
