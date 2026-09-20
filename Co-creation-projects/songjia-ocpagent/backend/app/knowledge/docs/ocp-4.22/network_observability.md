---
title: "Network Observability"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_observability/index
retrieved_at: 2026-09-05T05:42:31.281179+00:00
---

# Network Observability

---

OpenShift Container Platform 4.22

## Configuring and using the Network Observability Operator in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140486421059392)

**Abstract**

Use the Network Observability Operator to observe and analyze network traffic flows for OpenShift Container Platform clusters.

---

## [Chapter 1. Network Observability Operator release notes](#network-observability-operator-release-notes) Copy linkLink copied to clipboard!

Review new features, enhancements, fixed issues, and known issues for the Network Observability Operator. These release notes provide information to help you understand changes and security advisories in the latest Operator release.

The Network Observability Operator enables administrators to observe and analyze network traffic flows for OpenShift Container Platform clusters.

These release notes track the development of the Network Observability Operator in the OpenShift Container Platform. It follows a rolling-stream release methodology, and customers are expected to continuously upgrade to new versions as they become available on the cluster.

Some referenced tickets are not linked. This means that the ticket is not accessible without Red Hat credentials.

### [1.1. Network Observability Operator 1.12.2 advisory](#network-observability-operator-release-notes-1-12-2-advisory_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

Network Observability Operator 1.12.2 includes a product enhancement advisory.

* [RHEA-2026:56870 Network Observability Operator 1.12.2](https://access.redhat.com/errata/RHEA-2026:56870)

### [1.2. Network Observability Operator 1.12.2 fixed issues](#network-observability-operator-release-notes-1-12-2-fixed-issues_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

The Network Observability Operator 1.12.2 release contains several fixed issues that improve system status reporting and user experience.

Narrowed Operator ClusterRole to least-privilege RBAC permissions
:   Before this update, the Network Observability Operator’s generated `ClusterRole` granted cluster-wide write access to core resources such as secrets and namespaces, and allowed creating `SecurityContextConstraints` and `ClusterRoleBindings` without resource-name scoping. As a consequence, the Network Observability Operator service account held broader permissions than required to manage its operands.

    With this release, the Network Observability Operator’s RBAC permissions are scoped to only the namespaces it manages, the `securitycontextconstraints` rule is restricted by resource name, and `ClusterRoleBinding` permissions are constrained to the specific bindings the Operator creates. As a result, the Operator follows the principle of least privilege and reduces the attack surface of the service account.

    After upgrading to Network Observability Operator 1.12.2, you must manually grant RBAC permissions if any of the following conditions apply:

    * You configured `spec.namespace` in the `FlowCollector` resource to a namespace other than `netobserv`.
    * You configured the `FlowCollector` resource with `spec.deploymentModel: Kafka` and TLS or mTLS enabled.
    * You use the Loki Operator with `LokiStack` installed in a namespace other than `netobserv`.

      For instructions, see "Granting permissions for custom namespace and secret access".

Inherited scheduling configuration for the console plugin static deployment
:   Before this update, the `netobserv-plugin-static` deployment in the `openshift-netobserv-operator` namespace did not inherit `nodeSelector` and `tolerations` settings from the Operator Subscription. As a consequence, you could not schedule the static console plugin pod onto infrastructure nodes alongside the controller manager.

    With this release, the `netobserv-plugin-static` deployment inherits the scheduling configuration set on the Operator Subscription. As a result, node placement for the static console plugin is consistent with the controller manager.

    [NETOBSERV-2575](https://redhat.atlassian.net/browse/NETOBSERV-2575)

Resolved Operator startup failure with custom console logos
:   Before this update, the Network Observability Operator failed to start when the `Console.operator.openshift.io` resource had the `spec.customization.logos` field configured. The Operator incorrectly reported a validation conflict between `logos` and the deprecated `customLogoFile` field, even when only `logos` was set.

    With this release, the Network Observability Operator correctly handles web console configurations that use the `spec.customization.logos` field. As a result, the Operator starts successfully on clusters with custom console branding.

    [NETOBSERV-2767](https://redhat.atlassian.net/browse/NETOBSERV-2767)

Fixed controller crash when FlowCollector is on hold and ServiceAccount is absent
:   Before this update, the Operator controller panicked with a nil pointer dereference when the `FlowCollector` resource was in `OnHold` mode and the eBPF agent `ServiceAccount` did not exist. As a consequence, the controller manager pod entered a `CrashLoopBackOff` state and all reconciliation stopped.

    With this release, the Network Observability Operator gracefully skips the deletion step when the `ServiceAccount` is absent during an `OnHold` reconciliation. As a result, the controller manager no longer crashes in this scenario.

    [NETOBSERV-2839](https://redhat.atlassian.net/browse/NETOBSERV-2839)

### [1.3. Network Observability Operator 1.12.1 advisory](#network-observability-operator-release-notes-1-12-1-advisory_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

Network Observability Operator 1.12.1 includes a product enhancement advisory.

* [RHEA-2026:40244 Network Observability Operator 1.12.1](https://access.redhat.com/errata/RHEA-2026:40244)

### [1.4. Network Observability Operator 1.12 advisory](#network-observability-operator-release-notes_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

You can review the advisory for Network Observability Operator 1.12 release.

* [RHSA-2026:24473 Network Observability Operator 1.12](https://access.redhat.com/errata/RHSA-2026:24473)

### [1.5. Network Observability Operator 1.12 new features and enhancements](#network-observability-operator-release-notes-1-12-new-features-enhancements_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

The Network Observability Operator 1.12 release introduces non-decrypting TLS metadata tracking, Kafka message compression options, automated secondary network indexing, and expanded web console compatibility for OpenShift Container Platform clusters.

Transport Layer Security traffic metadata tracking
:   The Network Observability Operator can now capture and analyze Transport Layer Security (TLS) metadata from network flows without decrypting traffic. By extracting handshake details from `ClientHello` and `ServerHello` messages, the Operator provides visibility into encryption protocols while maintaining data privacy.

    The following key benefits include:

    * Security risk detection: Identify workloads using deprecated TLS versions (1.0, 1.1) or weak cipher suites.
    * Compliance auditing: Audit TLS configurations to meet regulatory requirements through metric aggregation and dashboard visualization.
    * Security posture assessment: Visualize encrypted network traffic with lock icons in the **Topology** view and identify unencrypted communications across your cluster.
    * Configure Prometheus alerts to automatically report insecure or non-compliant TLS configurations.

      To use this feature, enable `TLSTracking` in the `spec.agent.ebpf.features` list of the `FlowCollector` custom resource (CR).

Support for Kafka compression
:   Message compression configuration is now available when using Kafka to scale network flow collection. Enabling compression reduces the network bandwidth required to transport flows and decreases the storage footprint on Kafka brokers.

    The following key benefits include:

    * Reduced network load: Compressing flow data minimizes the traffic volume between the eBPF agent or flowlogs-pipeline and your Kafka cluster.
    * Storage efficiency: Smaller message sizes lead to improved disk space utilization on Kafka brokers.
    * Tunable performance: Choose from several compression algorithms, such as `gzip`, `snappy`, `lz4`, or `zstd`, to balance CPU usage with compression ratios.

      To enable this feature, configure the `spec.kafka.compression` and `spec.exporters.kafka.compression` fields in the `FlowCollector` custom resource.

Simplified secondary network indexing
:   The configuration process for secondary network indexing is now simplified.

    The `name` field in the `spec.processor.advanced.secondaryNetworks` list is deprecated and ignored. The Network Observability Operator automatically evaluates all secondary networks regardless of their assigned names, removing the requirement for manual name-matching entries in the `FlowCollector` CR.

OpenShift Container Platform web console compatibility
:   The Network Observability web console plugin is updated to support OpenShift Container Platform 4.22 and later. Backward compatibility is maintained for OpenShift Container Platform versions 4.14 through 4.21.

### [1.6. Network Observability Operator 1.12 fixed issues](#network-observability-operator-release-notes-1-12-fixed-issues_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

The Network Observability Operator 1.12 release contains several fixed issues that improve performance, system status reporting, and user experience.

Consistent FlowCollector pipeline status
:   Before this update, changes to the sampling field caused an inconsistency in the `FlowCollector` resource status. As a consequence, you could see conflicting statuses across pipeline components.

    With this release, status reporting is made consistent across all components. As a result, the reliability of the pipeline status indicator is improved.

    [NETOBSERV-2375](https://issues.redhat.com/browse/NETOBSERV-2375)

Fixed `--help` flag processing in netobserv-cli
:   Before this update, the `--help` flag was ignored when placed after other command flags in the Network Observability CLI. As a consequence, running commands such as `oc netobserv flows --interfaces=br-ex --max-time=10s --help` executed the flow collection instead of displaying the help page.

    With this release, the `--help` flag is recognized regardless of its position in the command. As a result, you can now display help information by placing the `--help` flag anywhere in your command arguments.

    [NETOBSERV-2617](https://issues.redhat.com/browse/NETOBSERV-2617)

Improved visibility of DNS names warning messages
:   Before this update, the **DNS names** graph repeatedly displayed a warning message on every refresh when running in a Prometheus-only configuration. As a consequence, the persistent warning message covered other dashboard elements.

    With this release, the warning message is only displayed during the initial data load and does not overlay other content. As a result, interface clarity is improved when navigating the dashboard.

    [NETOBSERV-2618](https://issues.redhat.com/browse/NETOBSERV-2618)

Prometheus enabled by default in FlowCollector configurations
:   Before this update, the default setting for Prometheus metrics was unassigned during `FlowCollector` custom resource creation. As a consequence, you had to manually ensure that metrics collection was active to query accurate flow data.

    With this release, the default value for Prometheus metrics collection in the `FlowCollector` configuration is set to `true`. As a result, the deployment process is simplified and flow metrics are collected automatically.

    [NETOBSERV-2620](https://issues.redhat.com/browse/NETOBSERV-2620)

Usage examples added to CLI subcommand help text
:   Before this update, the `help` subcommands for the Network Observability CLI lacked syntax examples. As a consequence, understanding how to construct complex filtering and capture commands required additional research.

    With this release, clear examples are included in the subcommand help outputs. As a result, the usability and discoverability of the CLI features are enhanced.

    [NETOBSERV-2646](https://issues.redhat.com/browse/NETOBSERV-2646)

Corrected latency formatting for values above one second
:   Before this update, flow durations and network latencies greater than one second were improperly formatted as milliseconds. As a consequence, donut graphs and latency metrics displayed confusing or inaccurate time designations.

    With this release, the duration formatting function handles values greater than one millisecond accurately using decimal seconds. As a result, you can view precise network latency values in console charts.

    [NETOBSERV-2669](https://issues.redhat.com/browse/NETOBSERV-2669)

Improved FlowCollector status reporting when eBPF pods are absent
:   Before this update, the `FlowCollector` resource reported a status of `Ready` even when a restrictive `nodeSelector` prevented any eBPF agent pods from deploying. As a consequence, the system status misrepresented the health of the agent layer.

    With this release, the Operator checks for a zero-pod deployment count. As a result, the `FlowCollector` CR now correctly identifies when zero eBPF pods are active, improving cluster error diagnostics.

    [NETOBSERV-2674](https://issues.redhat.com/browse/NETOBSERV-2674)

Optimized field exports for OpenTelemetry exporters
:   Before this update, the OpenTelemetry exporter processed missing or null keys as non-null data. As a consequence, unpopulated `metadata` fields were exported to log streams, which increased storage usage and cluttered telemetry files.

    With this release, the OpenTelemetry exporter filters out null or unrelated fields, exporting only keys that belong to explicitly enabled features. As a result, exported log sizes are reduced and data efficiency is improved.

    [NETOBSERV-2705](https://issues.redhat.com/browse/NETOBSERV-2705)

Added sampling probability fields to IPFIX exports
:   Before this update, Internet Protocol Flow Information Export (IPFIX) record exports omitted per-flow sampling information. As a consequence, data exports failed to comply with the standard IPFIX specifications for `samplingProbability` usage.

    With this release, the exporter includes sampling probability details within the IPFIX packet metadata. As a result, exported OpenTelemetry data matches industry compliance standards.

    [NETOBSERV-2706](https://issues.redhat.com/browse/NETOBSERV-2706)

Fixed TLS volume name conflicts on OpenTelemetry exporters
:   Before this update, configuring TLS certificates on OpenTelemetry exporters generated an invalid volume name format. As a consequence, the `apiserver` rejected the underlying Flow-logs Pipeline deployment specification, causing the pipeline pod to fail during initialization.

    With this release, the Operator ensures valid volume names are generated when handling TLS attributes. As a result, enabling TLS on your OpenTelemetry exporters no longer interferes with pipeline pod lifecycles.

    [NETOBSERV-2707](https://issues.redhat.com/browse/NETOBSERV-2707)

Improved pod-to-pod flow filter rule matching for asymmetric CIDR rules
:   Before this update, the default flow filter action was not enforced when a network flow failed to match both a CIDR rule and its corresponding `peerCIDR` rule identically. As a consequence, unexpected acknowledgment-only, `ACK`, flows bypass filtering restrictions inside the pod network.

    With this release, when a network flow matches a designated CIDR rule but fails the `peerCIDR` pairing, the default filtering action is correctly applied. As a result, traffic blocking and network rule isolation are handled more securely.

    [NETOBSERV-2755](https://issues.redhat.com/browse/NETOBSERV-2755)

### [1.7. Network Observability Operator 1.12 known issues](#network-observability-operator-release-notes-1-12-known-issues_network-observability-operator-release-notes) Copy linkLink copied to clipboard!

The following known issues affect the Network Observability Operator 1.12 release.

Operator fails to start when custom web console logos are configured
:   When you configure custom product logos in the `Console.operator.openshift.io` resource using the `spec.customization.logos` field, the Network Observability Operator pod fails to start during installation. The Operator incorrectly reports a validation error indicating that both `logos` and the deprecated `customLogoFile` fields are set, even though only `logos` is configured.

    To work around this problem, manually enable the Network Observability Operator OpenShift Container Platform web console plugin by adding `netobserv-plugin-static` to the `spec.plugins` list in the `Console` cluster resource, or by enabling the plugin through the web console under **Administration** → **Cluster Settings** → **Configuration** → **Console** → **Console plugins**.

    [NETOBSERV-2767](https://issues.redhat.com/browse/NETOBSERV-2767)

## [Chapter 2. About network observability](#network-observability-overview) Copy linkLink copied to clipboard!

Use the Network Observability Operator to observe network traffic via `eBPF` technology, providing troubleshooting insights through Prometheus metrics and Loki logs.

You can view and analyze this stored information in the OpenShift Container Platform console for further insight and troubleshooting.

### [2.1. Network Observability Operator](#network-observability-operator_network-observability-overview) Copy linkLink copied to clipboard!

The Network Observability Operator provides the cluster-scoped `FlowCollector` API custom resource, which manages a pipeline of eBPF agents and services that collect, enrich, and store network flows in Loki or Prometheus.

A `FlowCollector` instance deploys pods and services that form a monitoring pipeline.

The `eBPF` agent is deployed as a `daemonset` object and creates the network flows. The pipeline collects and enriches network flows with Kubernetes metadata before storing them in Loki or generating Prometheus metrics.

### [2.2. Optional dependencies of the Network Observability Operator](#network-observability-dependency-network-observability-operator_network-observability-overview) Copy linkLink copied to clipboard!

Integrate the Network Observability Operator with optional dependencies, such as the Loki Operator for flow storage and AMQ Streams (Kafka) for resilient, large-scale data handling and scalability.

Supported optional dependencies include the Loki Operator for flow storage, and AMQ Streams for large-scale data handling with Kafka.

Loki Operator
:   You can use Loki as the backend to store all collected flows with a maximal level of details. It is recommended to use the Red Hat supported Loki Operator to install Loki. You can also choose to use network observability without Loki, but you need to consider some factors. For more information, see "Network observability without Loki".

AMQ Streams Operator
:   Kafka provides scalability, resiliency and high availability in the OpenShift Container Platform cluster for large scale deployments.

    Note

    If you choose to use Kafka, it is recommended to use Red Hat supported AMQ Streams Operator.

### [2.3. OpenShift Container Platform console integration](#network-observability-openshift-console-integration_network-observability-overview) Copy linkLink copied to clipboard!

The Network Observability Operator integrates with the OpenShift Container Platform console, providing an overview, topology view, and traffic flow tables.

The Network observability metrics dashboards in **Observe** → **Dashboards** are available only to users with administrator access.

Note

To enable multi-tenancy for developer access and for administrators with limited access to namespaces, you must specify permissions by defining roles. For more information, see "Enabling multi-tenancy in network observability".

#### [2.3.1. Network observability metrics dashboards](#network-observability-dashboards_network-observability-overview) Copy linkLink copied to clipboard!

Review the network observability metrics dashboards in the OpenShift Container Platform console, which provide overall traffic flow aggregation, filtering options, and dedicated dashboards for monitoring operator health.

In the OpenShift Container Platform console on the **Overview** tab, you can view the overall aggregated metrics of the network traffic flow on the cluster. You can choose to display the information by cluster, node, namespace, owner, pod, and service. Filters and display options can further refine the metrics. For more information, see "Observing the network traffic from the Overview view".

In **Observe** → **Dashboards**, the **Netobserv** dashboards provide a quick overview of the network flows in your OpenShift Container Platform cluster. The **Netobserv/Health** dashboard provides metrics about the health of the Operator. For more information, see "Network observability metrics" and "Viewing health information".

#### [2.3.2. Network observability topology views](#network-observability-topology-views_network-observability-overview) Copy linkLink copied to clipboard!

The network observability topology view in the OpenShift Container Platform console displays a graphical representation of traffic flow between components, which you can refine using various filters and display options.

The OpenShift Container Platform console offers the **Topology** tab which represents traffic between the OpenShift Container Platform components as a network graph. You can refine the graph by using the filters and display options. You can access the information for cluster, zone, udn, node, namespace, owner, pod, and service.

#### [2.3.3. Traffic flow tables](#traffic-flow-tables_network-observability-overview) Copy linkLink copied to clipboard!

The **Traffic flow** tables in the OpenShift Container Platform web console provide a detailed view of raw network flows, offering powerful filtering options and configurable columns for in-depth analysis.

The **Traffic flows** tab in the OpenShift Container Platform web console displays the data of the network flows and the amount of traffic.

### [2.4. Network Observability CLI](#network-observability-cli_network-observability-overview) Copy linkLink copied to clipboard!

The Network Observability CLI (`oc netobserv`) is a lightweight tool that streams flow and packet data for quick, live insight into networking issues without requiring the full Network Observability Operator installation.

The Network Observability CLI is a flow and packet visualization tool that relies on eBPF agents to stream collected data to an ephemeral collector pod. It requires no persistent storage during the capture. After the run, the output is transferred to your local machine. This enables quick, live insight into packets and flow data without installing the Network Observability Operator.

## [Chapter 3. Installing the Network Observability Operator](#installing-network-observability-operators) Copy linkLink copied to clipboard!

Installing the Loki Operator is recommended before using the Network Observability Operator. You can use network observability without Loki, but special considerations apply if you only need metrics or external exporters.

The Loki Operator integrates a gateway that implements multi-tenancy and authentication with Loki for data flow storage. The `LokiStack` resource manages Loki, which is a scalable, highly-available, multi-tenant log aggregation system, and a web proxy with OpenShift Container Platform authentication. The `LokiStack` proxy uses OpenShift Container Platform authentication to enforce multi-tenancy and facilitate the saving and indexing of data in Loki log stores.

### [3.1. Network observability without Loki](#network-observability-without-loki_network_observability) Copy linkLink copied to clipboard!

Compare the features available with network observability with and without installing the Loki Operator.

If you only want to export flows to a Kafka consumer or IPFIX collector, or you only need dashboard metrics, then you do not need to install Loki or provide storage for Loki. The following table compares available features with and without Loki.

Expand

Table 3.1. Comparison of feature availability with and without Loki

|  | **With Loki** | **Without Loki** |
| --- | --- | --- |
| **Exporters** | X | X |
| **Multi-tenancy** | X | X |
| **Complete filtering and aggregations capabilities** [1] | X |  |
| **Partial filtering and aggregations capabilities** [2] | X | X |
| **Flow-based metrics and dashboards** | X | X |
| **Traffic flows view overview** [3] | X | X |
| **Traffic flows view table** | X |  |
| **Topology view** | X | X |
| **OpenShift Container Platform console Network Traffic tab integration** | X | X |

Show more

1. Such as per pod.
2. Such as per workload or namespace.
3. Statistics on packet drops are only available with Loki.

### [3.2. Installing the Loki Operator](#network-observability-loki-installation_network_observability) Copy linkLink copied to clipboard!

Install the supported Loki Operator version from the software catalog to enable the secure `LokiStack` instance, which provides automatic in-cluster authentication and authorization for network observability.

The [Loki Operator versions 6.0+](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel9-operator/64479927e1820602a81cdf13) are the supported Loki Operator versions for network observability; these versions provide the ability to create a `LokiStack` instance using the `openshift-network` tenant configuration mode and provide fully-automatic, in-cluster authentication and authorization support for network observability.

**Prerequisites**

* You have administrator permissions.
* You have access to the OpenShift Container Platform web console.
* You have access to a supported object store. For example: AWS S3, Google Cloud Storage, Azure, Swift, Minio, or OpenShift Data Foundation.

**Procedure**

1. In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.
2. Choose **Loki Operator** from the list of available Operators, and click **Install**.
3. Under **Installation Mode**, select **All namespaces on the cluster**.

**Verification**

1. Verify that you installed the Loki Operator. Visit the **Ecosystem** → **Installed Operators** page and look for **Loki Operator**.
2. Verify that **Loki Operator** is listed with **Status** as **Succeeded** in all the projects.

Important

To uninstall Loki, refer to the uninstallation process that corresponds with the method you used to install Loki. You might have remaining `ClusterRoles` and `ClusterRoleBindings`, data stored in object store, and persistent volume that must be removed.

#### [3.2.1. Creating a secret for Loki storage](#network-observability-loki-secret_network_observability) Copy linkLink copied to clipboard!

Create a secret with cloud storage credentials, such as for Amazon Web Services (AWS), to allow the Loki Operator to access the necessary object store for log persistence.

The Loki Operator supports a few log storage options, such as AWS S3, Google Cloud Storage, Azure, Swift, Minio, OpenShift Data Foundation. The following example shows how to create a secret for AWS S3 storage. The secret created in this example, `loki-s3`, is referenced in "Creating a LokiStack custom resource". You can create this secret in the web console or CLI.

**Procedure**

1. Using the web console, navigate to the **Project** → **All Projects** dropdown and select **Create Project**.
2. Name the project `netobserv-loki` and click **Create**.
3. Navigate to the Import icon, **+**, in the top right corner. Paste your YAML file into the editor.

   The following shows an example secret YAML file for S3 storage:

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: loki-s3
     namespace: netobserv-loki
   stringData:
     access_key_id: QUtJQUlPU0ZPRE5ON0VYQU1QTEUK
     access_key_secret: d0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQo=
     bucketnames: s3-bucket-name
     endpoint: https://s3.eu-central-1.amazonaws.com
     region: eu-central-1
   ```

   where:

   `metadata.namespace`
   :   Specifies the namespace for the Loki S3 secret. While this example uses `netobserv-loki`, you can use a different namespace for different components.

   `stringData.access_key_id`
   :   Specifies the access key ID for the S3 bucket.

   `stringData.access_key_secret`
   :   Specifies the secret access key for the S3 bucket.

   `stringData.bucketnames`
   :   Specifies the name of the S3 bucket.

   `stringData.endpoint`
   :   Specifies the endpoint URL for the S3 service.

   `stringData.region`
   :   Specifies the AWS region where the bucket is located.

**Verification**

* After you create the secret, you view the secret listed under **Workloads** → **Secrets** in the web console.

#### [3.2.2. Creating a LokiStack custom resource](#network-observability-lokistack-create_network_observability) Copy linkLink copied to clipboard!

Deploy the `LokiStack` custom resource using the web console or OpenShift CLI (`oc`), ensuring you configure the correct namespace, deployment size, and secret name for Loki object storage.

You can deploy a `LokiStack` custom resource (CR) to create a namespace or new project.

**Procedure**

1. Navigate to **Ecosystem** → **Installed Operators**, viewing **All projects** from the **Project** dropdown.
2. Look for **Loki Operator**. In the details, under **Provided APIs**, select **LokiStack**.
3. Click **Create LokiStack**.
4. Ensure the following fields are specified in either **Form View** or **YAML view**:

   ```
   apiVersion: loki.grafana.com/v1
   kind: LokiStack
   metadata:
     name: loki
     namespace: netobserv-loki
   spec:
     size: 1x.small
     storage:
       schemas:
       - version: v13
         effectiveDate: '2022-06-01'
       secret:
         name: loki-s3
         type: s3
     storageClassName: gp3
     tenants:
       mode: openshift-network
   ```

   where:

   `metadata.namespace`
   :   Specifies the namespace for the `LokiStack` resource. While this example uses `netobserv-loki`, you can use a different namespace for different components.

   `spec.size`
   :   Specifies the deployment size. In Loki Operator 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`.

       Important

       It is not possible to change the number `1x` for the deployment size.

   `spec.storageClassName`
   :   Specifies a storage class name that is available on the cluster for `ReadWriteOnce` access mode. For best performance, specify a storage class that allocates block storage. Use the `oc get storageclasses` command to see available storage classes on your cluster.

       Important

       You must not reuse the same `LokiStack` custom resource that is used for logging.
5. Click **Create**.

#### [3.2.3. Role-based access control for Loki logs](#network-observability-role-based-access-control-for-loki-logs_network_observability) Copy linkLink copied to clipboard!

Configure role-based access control to grant users permission to view application, infrastructure, or audit logs in Loki.

By default, logging 5.8 and later does not grant users access to logs. You must configure role-based access control to grant users permission to view specific log types.

For more information on access control for Loki logs, see: "Fine grained access for Loki logs" in the Red Hat OpenShift Logging Operator documentation.

##### [3.2.3.1. Grant non-admin users cluster-wide log access](#grant-non-admin-users-cluster-wide-log-access_network_observability) Copy linkLink copied to clipboard!

Add users to a custom admin group to grant cluster-wide log access without making them cluster administrators. This is useful for senior engineers who need full log visibility but should not have cluster modification privileges.

Users who are members of any group specified in the `adminGroups` field of the `LokiStack` custom resource (CR) have the same read access to logs as administrators.

**Example LokiStack CR**

```
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: loki
  namespace: netobserv-loki
spec:
  tenants:
    mode: openshift-network
    openshift:
      adminGroups:
      - cluster-admin
      - custom-admin-group
```

where:

`spec.tenants.mode`
:   Specifies the tenant mode. Must be `openshift-network` for network observability.

`spec.tenants.openshift.adminGroups`
:   Specifies the list of groups whose members have cluster-wide log access. Defaults to `system:cluster-admins`, `cluster-admin`, and `dedicated-admin`. Set to `[]` to disable.

#### [3.2.4. LokiStack ingestion limits and health alerts](#network-observability-lokistack-configuring-ingestion_network_observability) Copy linkLink copied to clipboard!

The `LokiStack` instance includes default ingestion and query limits that can be overridden by administrators to manage performance and prevent system alerts or errors.

Note

You might want to update the ingestion and query limits if you get Loki errors showing up in the Console plugin, or in `flowlogs-pipeline` logs.

Here is an example of configured limits:

```
spec:
  limits:
    global:
      ingestion:
        ingestionBurstSize: 40
        ingestionRate: 20
        maxGlobalStreamsPerTenant: 25000
      queries:
        maxChunksPerQuery: 2000000
        maxEntriesLimitPerQuery: 10000
        maxQuerySeries: 3000
```

For more information about these settings, see "LokiStack API reference".

### [3.3. Installing the Network Observability Operator](#network-observability-operator-installation_network_observability) Copy linkLink copied to clipboard!

Install the Network Observability Operator and use the setup wizard to create the `FlowCollector` custom resource definition (CRD) to complete the initial configuration.

You can set specifications in the web console when you create the `FlowCollector`.

Important

The actual memory consumption of the Operator depends on your cluster size and the number of resources deployed. Memory consumption might need to be adjusted accordingly. For more information refer to "Network Observability controller manager pod runs out of memory" in the "Important Flow Collector configuration considerations" section.

**Prerequisites**

* If you choose to use Loki, install the [Loki Operator version 5.7+](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel8-operator/622b46bcae289285d6fcda39).
* You must have `cluster-admin` privileges.
* One of the following supported architectures is required: `amd64`, `ppc64le`, `arm64`, or `s390x`.
* Any CPU supported by Red Hat Enterprise Linux (RHEL) 9.
* Must be configured with OVN-Kubernetes as the main network plugin, and optionally using secondary interfaces with Multus and SR-IOV.

Note

Additionally, this installation example uses the `netobserv` namespace, which is used across all components. You can optionally use a different namespace.

**Procedure**

1. In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.
2. Choose **Network Observability Operator** from the list of available Operators in the software catalog, and click **Install**.
3. Select the checkbox `Enable Operator recommended cluster monitoring on this Namespace`.
4. Navigate to **Operators** → **Installed Operators**. Under Provided APIs for Network Observability, select the **Flow Collector** link.
5. Follow the **Network Observability FlowCollector setup** wizard.
6. Click **Create**.

**Verification**

To confirm this was successful, when you navigate to **Observe** you should see **Network Traffic** listed in the options.

In the absence of **Application Traffic** within the OpenShift Container Platform cluster, default filters might show that there are "No results", which results in no visual flow. Beside the filter selections, select **Clear all filters** to see the flow.

#### [3.3.1. Important FlowCollector configuration considerations](#network-observability-important-flowcollector-configuration-considerations_network_observability) Copy linkLink copied to clipboard!

Review essential `FlowCollector` configuration options before initial deployment to avoid pod disruptions caused by later reconfiguration. Key settings include Kafka integration, enriched flow data exports, SR-IOV traffic monitoring, and advanced tracking for DNS and packet drops.

Once you create the `FlowCollector` instance, you can reconfigure it, but the pods are terminated and recreated again, which can be disruptive.

Therefore, you can consider configuring the following options when creating the `FlowCollector` for the first time.

### [3.4. Migrating removed stored versions of the FlowCollector CRD](#network-observability-updating-migrating_network_observability) Copy linkLink copied to clipboard!

Manually remove the deprecated `v1alpha1` version from the `FlowCollector` custom resource definition (CRD) `storedVersion` list to prevent upgrade errors and successfully migrate to Network Observability Operator 1.6.

There are two options to remove stored versions:

1. Use the Storage Version Migrator Operator.
2. Uninstall and reinstall the Network Observability Operator, ensuring that the installation is in a clean state.

**Prerequisites**

* You have an older version of the Operator installed, and you want to prepare your cluster to install the latest version of the Operator. Or you have attempted to install the Network Observability Operator 1.6 and run into the error: `Failed risk of data loss updating "flowcollectors.flows.netobserv.io": new CRD removes version v1alpha1 that is listed as a stored version on the existing CRD`.

**Procedure**

1. Verify that the old `FlowCollector` CRD version is still referenced in the `storedVersion`:

   ```
   $ oc get crd flowcollectors.flows.netobserv.io -ojsonpath='{.status.storedVersions}'
   ```
2. If `v1alpha1` appears in the list of results, proceed with **Step a** to use the Kubernetes Storage Version Migrator or **Step b** to uninstall and reinstall the CRD and the Operator.

   1. **Option 1: Kubernetes Storage Version Migrator**: Create a YAML to define the `StorageVersionMigration` object, for example `migrate-flowcollector-v1alpha1.yaml`:

      ```
      apiVersion: migration.k8s.io/v1alpha1
      kind: StorageVersionMigration
      metadata:
        name: migrate-flowcollector-v1alpha1
      spec:
        resource:
          group: flows.netobserv.io
          resource: flowcollectors
          version: v1alpha1
      ```

      1. Save the file.
      2. Apply the `StorageVersionMigration` by running the following command:

         ```
         $ oc apply -f migrate-flowcollector-v1alpha1.yaml
         ```
      3. Update the `FlowCollector` CRD to manually remove `v1alpha1` from the `storedVersion`:

         ```
         $ oc edit crd flowcollectors.flows.netobserv.io
         ```
   2. **Option 2: Reinstall**: Save the Network Observability Operator 1.5 version of the `FlowCollector` CR to a file, for example `flowcollector-1.5.yaml`.

      ```
      $ oc get flowcollector cluster -o yaml > flowcollector-1.5.yaml
      ```

      1. Follow the steps in "Uninstalling the Network Observability Operator", which uninstalls the Operator and removes the existing `FlowCollector` CRD.
      2. Install the Network Observability Operator latest version, 1.6.0.
      3. Create the `FlowCollector` using backup that was saved in Step b.

**Verification**

* Run the following command:

  ```
  $ oc get crd flowcollectors.flows.netobserv.io -ojsonpath='{.status.storedVersions}'
  ```

  The list of results should no longer show `v1alpha1` and only show the latest version, `v1beta1`.

### [3.5. Enabling multi-tenancy in network observability](#network-observability-multi-tenancy_network_observability) Copy linkLink copied to clipboard!

Enable multi-tenancy in network observability by configuring cluster roles and namespace roles to grant project administrators and developers granular, restricted access to flows and metrics in Loki and Prometheus.

Access is enabled for project administrators. Project administrators who have limited access to some namespaces can access flows for only those namespaces.

For Developers, multi-tenancy is available for both Loki and Prometheus but requires different access rights.

**Prerequisite**

* If you are using Loki, you have installed at least [Loki Operator version 5.7](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel8-operator/622b46bcae289285d6fcda39).
* You must be logged in as a project administrator.

**Procedure**

* For per-tenant access, you must have the `netobserv-loki-reader` cluster role and the `netobserv-metrics-reader` namespace role to use the developer perspective. Run the following commands for this level of access:

  ```
  $ oc adm policy add-cluster-role-to-user netobserv-loki-reader <user_group_or_name>
  ```

  ```
  $ oc adm policy add-role-to-user netobserv-metrics-reader <user_group_or_name> -n <namespace>
  ```
* For cluster-wide access, non-cluster-administrators must have the `netobserv-loki-reader`, `cluster-monitoring-view`, and `netobserv-metrics-reader` cluster roles. In this scenario, you can use either the admin perspective or the developer perspective. Run the following commands for this level of access:

  ```
  $ oc adm policy add-cluster-role-to-user netobserv-loki-reader <user_group_or_name>
  ```

  ```
  $ oc adm policy add-cluster-role-to-user cluster-monitoring-view <user_group_or_name>
  ```

  ```
  $ oc adm policy add-cluster-role-to-user netobserv-metrics-reader <user_group_or_name>
  ```

### [3.6. Uninstalling the Network Observability Operator](#network-observability-operator-uninstall_network_observability) Copy linkLink copied to clipboard!

Uninstall the Network Observability Operator using the OpenShift Container Platform web console Operator Hub, working in the **Ecosystem** → **Installed Operators** area.

**Procedure**

1. Remove the `FlowCollector` custom resource.

   1. Click **Flow Collector**, which is next to the **Network Observability Operator** in the **Provided APIs** column.
   2. Click the Options menu
      for the **cluster** and select **Delete FlowCollector**.
2. Uninstall the Network Observability Operator.

   1. Navigate back to the **Ecosystem** → **Installed Operators** area.
   2. Click the Options menu
      next to the **Network Observability Operator** and select **Uninstall Operator**.
   3. **Home** → **Projects** and select `openshift-netobserv-operator`
   4. Navigate to **Actions** and select **Delete Project**
3. Remove the `FlowCollector` custom resource definition (CRD).

   1. Navigate to **Administration** → **CustomResourceDefinitions**.
   2. Look for **FlowCollector** and click the Options menu
      .
   3. Select **Delete CustomResourceDefinition**.

      Important

      The Loki Operator and Kafka remain if they were installed and must be removed separately. Additionally, you might have remaining data stored in an object store, and a persistent volume that must be removed.

## [Chapter 4. Scaling network flow collection with Kafka](#network-observability-kafka-operator-scaling-network-flow-collection) Copy linkLink copied to clipboard!

Scale your network flow collection by using the Kafka Operator to manage high-volume telemetry. Configure compression to reduce network bandwidth while balancing CPU overhead in large-scale cluster environments.

### [4.1. Kafka deployment scenarios for network flows](#network-observability-kafka-for-large-scale-environments_network-observability-kafka-operator-scaling-network-flow-collection) Copy linkLink copied to clipboard!

The Kafka Operator manages high-throughput and low-latency data feeds for network flow forwarding. This architecture provides a resilient and scalable solution for handling telemetry data in large-scale cluster environments.

#### [4.1.1. When to use Kafka for network flow collection](#when-to-use-kafka-for-network-flow-collection_network-observability-kafka-operator-scaling-network-flow-collection) Copy linkLink copied to clipboard!

Consider using Kafka to manage your network flow data when you experience the following circumstances:

* High flow volumes that overwhelm the default flowlogs-pipeline buffer
* Need for data persistence and replay capabilities
* Multiple consumers requiring access to the same flow data
* Requirements for horizontal scaling across multiple processing nodes

For smaller deployments with moderate flow volumes, the default configuration without Kafka is typically sufficient.

You can install the Kafka Operator as Red Hat AMQ Streams from the Operator Hub. See "Red Hat AMQ Streams".

Note

To uninstall Kafka, refer to the uninstallation process that corresponds with the method you used to install.

### [4.2. Reducing network bandwidth for flow telemetry](#network-observability-kafka-compression-benefits_network-observability-kafka-operator-scaling-network-flow-collection) Copy linkLink copied to clipboard!

Enable Kafka compression for flow records to optimize network traffic. This configuration reduces network bandwidth consumption while increasing the CPU load on the eBPF agent.

By default, the Network Observability Operator sends network flow records to Kafka without compression. This minimizes CPU overhead but can consume significant network bandwidth in clusters with high traffic volumes.

Enabling compression reduces the amount of data transmitted over the network, which is beneficial when the following cases are true:

* Network bandwidth is constrained or expensive
* Flow volumes are high and impacting network performance
* Kafka brokers are located on different nodes or in remote data centers

The trade-off is increased CPU usage on the eBPF agent pods, which run as a `DaemonSet` on every node. Each of the different compression algorithms provide the following balances between compression ratio and CPU cost:

* `lz4`: Very low CPU cost with 2 to 3 times compression. Best for most deployments.
* `zstd`: Moderate CPU cost with 3 to 5 times compression. Good for bandwidth-constrained environments.
* `snappy`: Similar to lz4 with slightly lower compression ratio.
* `gzip`: High CPU cost with 3 to 5 times compression. Maximum compression at highest CPU expense.
* `none`: No compression. Use when CPU is the bottleneck.

Flow records contain many repeated fields (IP addresses, namespaces, node names) and compress efficiently, often reaching the higher end of these compression ratios.

### [4.3. Configure Kafka compression](#network-observability-configuring-kafka-compression_network-observability-kafka-operator-scaling-network-flow-collection) Copy linkLink copied to clipboard!

Configure the compression algorithm for network flow records exported to Kafka to optimize bandwidth and storage. This helps manage the data footprint of high-volume network telemetry.

**Prerequisites**

* The Network Observability Operator is installed.
* The `FlowCollector` custom resource (CR) is configured to export data to a Kafka topic.
* You have `cluster-admin` permissions to edit the `FlowCollector` CR.

**Procedure**

1. Open the `FlowCollector` custom resource for editing by running the following command:

   ```
   $ oc edit flowcollector cluster
   ```
2. Navigate to the `spec.kafka` section and add the `compression` parameter:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     deploymentModel: Kafka
     kafka:
       address: "kafka-cluster-kafka-bootstrap.netobserv:9093"
       topic: "network-flows"
       compression: "lz4"
   ```

   where:

   `spec.kafka.compression`
   :   Specifies the compression algorithm. Accepted values: `gzip`, `snappy`, `lz4`, `zstd`, `none`. Default is `none`.
3. Save and apply the changes.

**Verification**

1. Confirm that the eBPF agent pods are running in the cluster by running the following command:

   ```
   $ oc get pods -A -l app=netobserv-ebpf-agent
   ```
2. Verify that Kafka compression is active by running the following command:

   ```
   $ oc logs -n <namespace> <pod_name> | grep "KafkaCompression"
   ```

   The output shows the compression configuration attribute in the eBPF agent pod logs.

### [4.4. Kafka compression codec reference](#network-observability-kafka-compression-codec-reference_network-observability-kafka-operator-scaling-network-flow-collection) Copy linkLink copied to clipboard!

Compare Kafka compression codecs to choose the optimal algorithm for your environment.

This reference applies to compression configured in both `spec.kafka.compression` for flow collection and `spec.exporters` for flow export.

Expand

Table 4.1. Kafka compression codec comparison

| Codec | Compression ratio | CPU cost (producer) | Decompression cost | Notes |
| --- | --- | --- | --- | --- |
| `none` | 1x | N/A | N/A | No overhead. Use when CPU is the bottleneck. |
| `lz4` | 2:1 to 3:1 | Very low | Very low | **Recommended default.** Best latency-to-compression ratio trade-off. |
| `snappy` | 2:1 to 3:1 | Very low | Very low | Similar to `lz4`, with a slightly lower compression ratio. |
| `zstd` | 3:1 to 5:1 | Moderate | Low | Higher compression ratio. Good for high-throughput clusters. |
| `gzip` | 3:1 to 5:1 | High | Moderate | Maximum compression ratio but incurs a significant CPU cost. |

Show more

Note

The compression ratios and CPU cost estimates are approximate values derived from upstream benchmarks, not from Network Observability-specific measurements. Actual results vary depending on flow record characteristics and batch sizes.

## [Chapter 5. Network Observability Operator in OpenShift Container Platform](#nw-network-observability-operator) Copy linkLink copied to clipboard!

The Network Observability Operator for OpenShift Container Platform deploys a monitoring pipeline. This pipeline collects and enriches network traffic flows generated by the `eBPF agent`.

### [5.1. Viewing statuses](#nw-network-observability-operator_nw-network-observability-operator) Copy linkLink copied to clipboard!

View the operational status of the Network Observability Operator by using the `oc get` command to check the `FlowCollector` resource status, as well as the status of the `eBPF agent`, `flowlogs-pipeline`, and console plugin Pods.

The Network Observability Operator provides the Flow Collector API. When a Flow Collector resource is created, it deploys pods and services to create and store network flows in the Loki log store, as well as to display dashboards, metrics, and flows in the OpenShift Container Platform web console.

**Procedure**

1. Run the following command to view the state of `FlowCollector`:

   ```
   $ oc get flowcollector/cluster
   ```

   **Example output**

   ```
   NAME      AGENT   SAMPLING (EBPF)   DEPLOYMENT MODEL   STATUS
   cluster   EBPF    50                DIRECT             Ready
   ```
2. Check the status of pods running in the `netobserv` namespace by entering the following command:

   ```
   $ oc get pods -n netobserv
   ```

   **Example output**

   ```
   NAME                              READY   STATUS    RESTARTS   AGE
   flowlogs-pipeline-56hbp           1/1     Running   0          147m
   flowlogs-pipeline-9plvv           1/1     Running   0          147m
   flowlogs-pipeline-h5gkb           1/1     Running   0          147m
   flowlogs-pipeline-hh6kf           1/1     Running   0          147m
   flowlogs-pipeline-w7vv5           1/1     Running   0          147m
   netobserv-plugin-cdd7dc6c-j8ggp   1/1     Running   0          147m
   ```

   The `flowlogs-pipeline` pods collect flows, enriches the collected flows, then send flows to the Loki storage. `netobserv-plugin` pods create a visualization plugin for the OpenShift Container Platform Console.
3. Check the status of pods running in the namespace `netobserv-privileged` by entering the following command:

   ```
   $ oc get pods -n netobserv-privileged
   ```

   **Example output**

   ```
   NAME                         READY   STATUS    RESTARTS   AGE
   netobserv-ebpf-agent-4lpp6   1/1     Running   0          151m
   netobserv-ebpf-agent-6gbrk   1/1     Running   0          151m
   netobserv-ebpf-agent-klpl9   1/1     Running   0          151m
   netobserv-ebpf-agent-vrcnf   1/1     Running   0          151m
   netobserv-ebpf-agent-xf5jh   1/1     Running   0          151m
   ```

   The `netobserv-ebpf-agent` pods monitor network interfaces of the nodes to get flows and send them to `flowlogs-pipeline` pods.
4. If you are using the Loki Operator, check the status of the `component` pods of `LokiStack` custom resource in the `netobserv` namespace by entering the following command:

   ```
   $ oc get pods -n netobserv
   ```

   **Example output**

   ```
   NAME                                                READY   STATUS    RESTARTS   AGE
   lokistack-compactor-0                               1/1     Running   0          18h
   lokistack-distributor-654f87c5bc-qhkhv              1/1     Running   0          18h
   lokistack-distributor-654f87c5bc-skxgm              1/1     Running   0          18h
   lokistack-gateway-796dc6ff7-c54gz                   2/2     Running   0          18h
   lokistack-index-gateway-0                           1/1     Running   0          18h
   lokistack-index-gateway-1                           1/1     Running   0          18h
   lokistack-ingester-0                                1/1     Running   0          18h
   lokistack-ingester-1                                1/1     Running   0          18h
   lokistack-ingester-2                                1/1     Running   0          18h
   lokistack-querier-66747dc666-6vh5x                  1/1     Running   0          18h
   lokistack-querier-66747dc666-cjr45                  1/1     Running   0          18h
   lokistack-querier-66747dc666-xh8rq                  1/1     Running   0          18h
   lokistack-query-frontend-85c6db4fbd-b2xfb           1/1     Running   0          18h
   lokistack-query-frontend-85c6db4fbd-jm94f           1/1     Running   0          18h
   ```

### [5.2. Network Observablity Operator architecture](#network-observability-architecture_nw-network-observability-operator) Copy linkLink copied to clipboard!

Review the Network Observability Operator architecture, detailing how the `FlowCollector` resource manages the `eBPF agent`, which collects and enriches flows, sending the data to Loki for storage or Prometheus for metrics.

The Network Observability Operator provides the `FlowCollector` API, which is instantiated at installation and configured to reconcile the `eBPF agent`, the `flowlogs-pipeline`, and the `netobserv-plugin` components. Only a single `FlowCollector` per cluster is supported.

The `eBPF agent` runs on each cluster node with some privileges to collect network flows. The `flowlogs-pipeline` receives the network flows data and enriches the data with Kubernetes identifiers. If you choose to use Loki, the `flowlogs-pipeline` sends flow logs data to Loki for storing and indexing. The `netobserv-plugin`, which is a dynamic OpenShift Container Platform web console plugin, queries Loki to fetch network flows data. Cluster-admins can view the data in the web console.

If you do not use Loki, you can generate metrics with Prometheus. Those metrics and their related dashboards are accessible in the web console. For more information, see "Network Observability without Loki".

There are three deployment model options for the Network Observability Operator.

Note

The Network Observability Operator does not manage Loki or other data stores. You must install Loki separately by using the Loki Operator. If you use Kafka, you must install it separately by using the Kafka Operator.

Service deployment model
:   When the `spec.deploymentModel` field in the `FlowCollector` resource is set to `Service`, agents are deployed per node as daemon sets. The `flowlogs-pipeline` is a standard deployment with a service. You can scale the `flowlogs-pipeline` component by using the `spec.processor.consumerReplicas` field.

Direct deployment model
:   When the `spec.deploymentModel` field is set to `Direct`, agents and the `flowlogs-pipeline` are both deployed per node as daemon sets. This model is suitable for technology assessments and small clusters. However, it is less memory-efficient in large clusters because each instance of `flowlogs-pipeline` caches the same cluster information.

Kafka deployment model (optional)
:   If you use the Kafka option, the `eBPF agent` sends the network flow data to Kafka. You can scale the `flowlogs-pipeline` component by using the `spec.processor.consumerReplicas` field. The `flowlogs-pipeline` component reads from the Kafka topic before sending data to Loki, as shown in the following diagram.

### [5.3. Viewing Network Observability Operator status and configuration](#nw-status-configuration-network-observability-operator_nw-network-observability-operator) Copy linkLink copied to clipboard!

Inspect the current status, configuration details, and generated resources of the Network Observability Operator by using the `oc describe flowcollector/cluster` command.

**Procedure**

1. Run the following command to view the status and configuration of the Network Observability Operator:

   ```
   $ oc describe flowcollector/cluster
   ```

## [Chapter 6. Configuring the Network Observability Operator](#configuring-network-observability-operators) Copy linkLink copied to clipboard!

Configure the Network Observability Operator by updating the cluster-wide `FlowCollector` API resource (cluster) to manage component configurations and flow collection settings.

The `FlowCollector` is explicitly created during installation. Since this resource operates cluster-wide, only a single `FlowCollector` is allowed, and it must be named `cluster`. For more information, see the "FlowCollector API reference".

### [6.1. View the FlowCollector resource](#network-observability-flowcollector-view_network_observability) Copy linkLink copied to clipboard!

View and modify the `FlowCollector` resource in the OpenShift Container Platform web console through the integrated setup, advanced form, or by editing the YAML directly to configure the Network Observability Operator.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab. There, you can modify the `FlowCollector` resource to configure the Network Observability Operator.

#### [6.1.1. Example of a FlowCollector resource](#network-observability-flowcollector-example_network_observability) Copy linkLink copied to clipboard!

Review a comprehensive, annotated example of the `FlowCollector` custom resource that demonstrates configurations for `eBPF` sampling, conversation tracking, Loki integration, and console quick filters.

##### [6.1.1.1. Sample FlowCollector resource](#network-observability-flowcollector-configuring-about-sample_network_observability) Copy linkLink copied to clipboard!

```
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  networkPolicy:
    enable: true
  agent:
    type: eBPF
    ebpf:
      sampling: 50
      privileged: false
      features: []
  processor:
    addZone: false
    subnetLabels:
      openShiftAutoDetect: true
      customLabels: []
    consumerReplicas: 3
  loki:
    enable: true
    mode: LokiStack
    lokiStack:
      name: loki
      namespace: netobserv-loki
  consolePlugin:
    enable: true
  exporters: []
```

where:

`spec.agent.type`
:   Must be `eBPF` as eBPF is the only OpenShift Container Platform supported option.

`spec.agent.ebpf.sampling`
:   Specifies the sampling interval. By default, eBPF sampling is set to `50`, so a packet has a 1 in 50 chance of being sampled. A lower sampling interval value requires more computational, memory, and storage resources. A value of `0` or `1` means all packets are sampled. It is recommended to start with the default value and refine it empirically to determine the optimal setting for your cluster.

`spec.agent.ebpf.privileged`
:   Specifies if the eBPF agent pods should run as privileged. Running as privileged is required for several features, such as monitoring non-default networks and tracking packet drops. For security, in accordance with the principle of least privilege, it should only be enabled when some of those features are desired. A warning will be displayed if you enabled a feature requiring privileged mode without setting it to true explicitly.

`spec.processor.addZone`
:   Used to inject cloud availability zones in network flows.

`spec.processor.subnetLabels`
:   Specifies a list of customized labels to inject in network flows, based on CIDR matching.

`spec.processor.consumerReplicas`
:   Specifies the number of replicas for the processor pods (flowlogs-pipeline). Refer to the Resource management and performance considerations section for recommendations based on the cluster size.

`spec.loki.mode`
:   Specifies how to configure the connection to Loki, depending on its installation mode. If you use the install paths described in "Installing the Loki Operator", the mode must be set to `LokiStack`, and `spec.loki.lokiStack` should refer to the installed `LokiStack` resource name and namespace.

`spec.loki.lokistack.namespace`
:   Specifies the namespace for the `LokiStack` resource. This value must match the `metadata.namespace` defined in the `LokiStack` custom resource. While this example uses `netobserv-loki`, you can use a different namespace for different components.

### [6.2. Grant permissions for custom namespace and secret access](#network-observability-grant-permissions-custom-namespace-and-secret-access_network_observability) Copy linkLink copied to clipboard!

Grant RBAC permissions to allow the Network Observability Operator to access secrets across custom or non-default namespaces.

For security, the Network Observability Operator does not have cluster-wide permissions to read secrets. You must explicitly grant the required permissions when any of the following conditions apply:

* You configured `spec.namespace` in the `FlowCollector` resource to a namespace other than `netobserv`.
* You configured the `FlowCollector` resource with `spec.deploymentModel: Kafka` and TLS or mTLS enabled.
* You use the Loki Operator with `LokiStack` installed in a namespace other than `netobserv`.

Complete only the procedures that apply to your configuration. If you do not meet any of these conditions, no additional permissions are required.

#### [6.2.1. Create cluster role bindings for a custom namespace](#network-observability-create-cluster-role-bindings-custom-namespace_network_observability) Copy linkLink copied to clipboard!

Create cluster role bindings for the Network Observability Operator service accounts when you deploy in a namespace other than the default `netobserv` namespace.

Important

Do not modify the existing default bindings. They are overwritten during Operator upgrades. Create new bindings as shown.

**Prerequisites**

* The Network Observability Operator is installed.
* You have `cluster-admin` privileges.
* You configured `spec.namespace` in the `FlowCollector` resource to a namespace other than `netobserv`.

**Procedure**

1. Replace `<namespace>` with the namespace you configured in `spec.namespace` of the `FlowCollector` resource.

   1. Create the `netobserv-informers-custom` cluster role binding by running the following command:

      ```
      $ oc create clusterrolebinding netobserv-informers-custom \
        --clusterrole=netobserv-informers \
        --serviceaccount=<namespace>:flowlogs-pipeline \
        --serviceaccount=<namespace>:flowlogs-pipeline-transformer
      ```
   2. Create the `netobserv-lokiwriter-custom` cluster role binding by running the following command:

      ```
      $ oc create clusterrolebinding netobserv-lokiwriter-custom \
        --clusterrole=netobserv-loki-writer \
        --serviceaccount=<namespace>:flowlogs-pipeline \
        --serviceaccount=<namespace>:flowlogs-pipeline-transformer
      ```
   3. Create the `netobserv-hostnetwork-custom` cluster role binding by running the following command:

      ```
      $ oc create clusterrolebinding netobserv-hostnetwork-custom \
        --clusterrole=netobserv-hostnetwork \
        --serviceaccount=<namespace>:flowlogs-pipeline
      ```
   4. Create the token review cluster role binding by running the following command:

      ```
      $ oc create clusterrolebinding netobserv-tokenreview-custom \
        --clusterrole=netobserv-token-review \
        --serviceaccount=<namespace>:netobserv-plugin
      ```

**Verification**

1. Check the `FlowCollector` status for errors by running the following command:

   ```
   $ oc get flowcollector cluster -o jsonpath='{.status.conditions}'
   ```
2. Verify that no conditions report permission-related errors.

   Note

   If the `FlowCollector` status continues to show permission errors after you grant the required permissions, restart the Network Observability Operator pod for faster reconciliation:

   ```
   $ oc delete pods -n openshift-netobserv-operator -l app=netobserv-operator
   ```

#### [6.2.2. Grant access to Kafka secrets](#network-observability-grant-access-kafka-secrets_network_observability) Copy linkLink copied to clipboard!

Grant the Network Observability Operator permission to access Kafka secrets when you use the Kafka deployment model with TLS or mTLS enabled.

**Prerequisites**

* The Network Observability Operator is installed.
* You have `cluster-admin` privileges.
* You configured the `FlowCollector` resource with `spec.deploymentModel: Kafka` and TLS or mTLS enabled.

**Procedure**

1. Replace `<namespace>` with the namespace configured in `spec.namespace` of the `FlowCollector` resource. The default value is `netobserv`.

   1. If Kafka is installed in the same namespace as the Network Observability components, create the secret watcher role binding by running the following command:

      ```
      $ oc create rolebinding secret-watcher \
        -n <namespace> \
        --clusterrole=netobserv-secret-watcher \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```
   2. Create the secret creator role binding in the privileged namespace by running the following command:

      ```
      $ oc create rolebinding secret-creator \
        -n <namespace>-privileged \
        --clusterrole=netobserv-secret-creator \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```
2. If Kafka is installed in a different namespace, create the secret watcher role binding in the Kafka namespace.

   1. Replace `<kafka_namespace>` with the namespace where Kafka is installed by running the following command:

      ```
      $ oc create rolebinding secret-watcher \
        -n <kafka_namespace> \
        --clusterrole=netobserv-secret-watcher \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```
   2. Create the secret creator role binding by running the following command:

      ```
      $ oc create rolebinding secret-creator \
        -n <namespace> \
        --clusterrole=netobserv-secret-creator \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```
   3. Create the secret creator role binding in the privileged namespace by running the following command:

      ```
      $ oc create rolebinding secret-creator \
        -n <namespace>-privileged \
        --clusterrole=netobserv-secret-creator \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```

**Verification**

1. Check the `FlowCollector` status for errors by running the following command:

   ```
   $ oc get flowcollector cluster -o jsonpath='{.status.conditions}'
   ```
2. Verify that no conditions report permission-related errors.

   Note

   If the `FlowCollector` status continues to show permission errors after you grant the required permissions, restart the Network Observability Operator pod for faster reconciliation:

   ```
   $ oc delete pods -n openshift-netobserv-operator -l app=netobserv-operator
   ```

#### [6.2.3. Grant access to LokiStack secrets](#network-observability-grant-access-lokistack-secrets_network_observability) Copy linkLink copied to clipboard!

Grant the Network Observability Operator permission to access the `LokiStack` secret when `LokiStack` is installed in a namespace other than `netobserv`.

**Prerequisites**

* The Network Observability Operator is installed.
* You have `cluster-admin` privileges.
* You use the Loki Operator with `LokiStack` installed in a namespace other than `netobserv`.

**Procedure**

1. Replace `<lokistack_namespace>` with the namespace where `LokiStack` is installed and `<namespace>` with the namespace configured in `spec.namespace` of the `FlowCollector` resource.

   1. Create the `secret-watcher` role binding in the LokiStack namespace by running the following command:

      ```
      $ oc create rolebinding secret-watcher \
        -n <lokistack_namespace> \
        --clusterrole=netobserv-secret-watcher \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```
   2. Create the `secret-creator` role binding by running the following command:

      ```
      $ oc create rolebinding secret-creator \
        -n <namespace> \
        --clusterrole=netobserv-secret-creator \
        --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
      ```

**Verification**

1. Check the `FlowCollector` status for errors by running the following command:

   ```
   $ oc get flowcollector cluster -o jsonpath='{.status.conditions}'
   ```
2. Verify that no conditions report permission-related errors.

   Note

   If the `FlowCollector` status continues to show permission errors after you grant the required permissions, restart the Network Observability Operator pod for faster reconciliation:

   ```
   $ oc delete pods -n openshift-netobserv-operator -l app=netobserv-operator
   ```

### [6.3. Configuring the FlowCollector resource with Kafka](#network-observability-flowcollector-kafka-config_network_observability) Copy linkLink copied to clipboard!

Configure the `FlowCollector` resource to use Kafka for high-throughput and low-latency data feeds.

You must have a running Kafka instance and create a Kafka topic in that instance dedicated to OpenShift Container Platform Network Observability. For more information, see [Kafka documentation with AMQ Streams](https://access.redhat.com/documentation/en-us/red_hat_amq/7.7/html/using_amq_streams_on_openshift/using-the-topic-operator-str).

**Prerequisites**

* You have installed Kafka. Red Hat supports Kafka with AMQ Streams Operator.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the Network Observability Operator, select **Flow Collector**.
3. Select the cluster and then click the **YAML** tab.
4. Change the `FlowCollector` resource for OpenShift Container Platform Network Observability Operator to use Kafka, as shown in the following sample YAML:

   **Sample Kafka configuration in `FlowCollector` resource**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     deploymentModel: Kafka
     kafka:
       address: "kafka-cluster-kafka-bootstrap.netobserv"
       topic: network-flows
       tls:
         enable: false
   ```

   where:

   `spec.deploymentModel`
   :   Specifies the deployment model. Set to `Kafka` instead of `Service` to enable the Kafka deployment model.

   `spec.kafka.address`
   :   Specifies the Kafka bootstrap server address. You can specify a port if needed, for instance `kafka-cluster-kafka-bootstrap.netobserv:9093` for using TLS on port 9093.

   `spec.kafka.topic`
   :   Specifies the name of the topic created in Kafka. It should match the name of a topic created in Kafka.

   `spec.kafka.tls`
   :   Specifies communication encryption. Use this setting to encrypt all communications to and from Kafka with TLS or mTLS. When enabled, the Kafka CA certificate must be available as a ConfigMap or a Secret in both namespaces: the namespace where you deploy the `flowlogs-pipeline` processor component (default: `netobserv`) and the namespace where you deploy the eBPF agents (default: `netobserv-privileged`). Reference the certificate by using `spec.kafka.tls.caCert`. When you use mTLS, make the client secrets available in these namespaces as well. You can generate the secrets by using the Red Hat AMQ Streams User Operator. Reference the secrets by using `spec.kafka.tls.userCert`.

### [6.4. Export enriched network flow data](#network-observability-enriched-flows_network_observability) Copy linkLink copied to clipboard!

Configure the `FlowCollector` resource to export enriched network flow data simultaneously to Kafka, IPFIX, or an OpenTelemetry endpoint for external consumption by tools like Splunk or Prometheus.

For Kafka or IPFIX, any processor or storage that supports those inputs, such as Splunk, Elasticsearch, or Fluentd, can consume the enriched network flow data.

For OpenTelemetry, network flow data and metrics can be exported to a compatible OpenTelemetry endpoint, such as Red Hat build of OpenTelemetry or Prometheus.

After configuration, network flows data can be sent to an available output. For more information, see "Network flows format reference".

**Prerequisites**

* Your Kafka, IPFIX, or OpenTelemetry collector endpoints are available from Network Observability `flowlogs-pipeline` pods.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** and then select the **YAML** tab.
4. Edit the `FlowCollector` to configure `spec.exporters` as follows:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     exporters:
     - type: Kafka
         kafka:
           address: "kafka-cluster-kafka-bootstrap.netobserv"
           topic: netobserv-flows-export
           tls:
             enable: false
     - type: IPFIX
         ipfix:
           targetHost: "ipfix-collector.ipfix.svc.cluster.local"
           targetPort: 4739
           transport: tcp
    -  type: OpenTelemetry
         openTelemetry:
           targetHost: my-otelcol-collector-headless.otlp.svc
           targetPort: 4317
           type: grpc
           logs:
             enable: true
           metrics:
             enable: true
             prefix: netobserv
             pushTimeInterval: 20s
             expiryTime: 2m
      #    fieldsMapping:
      #      input: SrcAddr
      #      output: source.address
   ```

   where:

   `spec.exporters.type`
   :   Specifies the export type. You can export flows to `IPFIX`, `OpenTelemetry`, and `Kafka` individually or concurrently.

   `spec.exporters.kafka.topic`
   :   Specifies the Kafka topic where the Network Observability Operator exports all flows.

   `spec.exporters.kafka.tls.enable`
   :   Specifies whether to encrypt communications to and from Kafka with SSL/TLS or mTLS. When enabled, the Kafka CA certificate must be available as a `ConfigMap` or a `Secret` in the namespace where the `flowlogs-pipeline` processor component is deployed (default: `netobserv`). Reference the certificate with `spec.exporters.tls.caCert`. For mTLS, client secrets must also be available in these namespaces and referenced with `spec.exporters.tls.userCert`.

   `spec.exporters.ipfix.transport`
   :   Specifies the transport protocol. The default value is `tcp`, but you can also specify `udp`.

   `spec.exporters.openTelemetry.type`
   :   Specifies the OpenTelemetry connection protocol. The available options are `http` and `grpc`.

   `spec.exporters.openTelemetry.logs`
   :   Specifies the OpenTelemetry configuration for exporting logs, which are identical to the logs created for Loki.

   `spec.exporters.openTelemetry.metrics`
   :   Specifies the OpenTelemetry configuration for exporting metrics, which are identical to the metrics created for Prometheus. These are defined in the `spec.processor.metrics.includeList` parameter of the `FlowCollector` resource or via the `FlowMetrics` resource.

   `spec.exporters.openTelemetry.metrics.pushTimeInterval`
   :   Specifies the time interval for sending metrics to the OpenTelemetry collector.

   `spec.exporters.openTelemetry.fieldsMapping`
   :   Specifies an optional mapping to customize the OpenTelemetry format output. Network Observability flow formats are automatically renamed to an OpenTelemetry-compliant format, but this parameter allows for custom overrides. For example in the YAML sample, `SrcAddr` is the Network Observability input field, and it is being renamed to `source.address` in OpenTelemetry output. You can see both Network Observability and OpenTelemetry formats in the "Network flows format reference".

### [6.5. Updating the FlowCollector resource](#network-observability-config-FLP-sampling_network_observability) Copy linkLink copied to clipboard!

As an alternative to using the web console, use the `oc patch` command with the `flowcollector` custom resource to quickly update specific specifications, such as eBPF sampling

**Procedure**

1. Run the following command to patch the `flowcollector` CR and update the `spec.agent.ebpf.sampling` value:

   ```
   $ oc patch flowcollector cluster --type=json -p "[{"op": "replace", "path": "/spec/agent/ebpf/sampling", "value": <new value>}] -n netobserv"
   ```

### [6.6. Filter network flows at ingestion](#network-observability-filter-network-flows-at-ingestion_network_observability) Copy linkLink copied to clipboard!

Create filters to reduce the number of generated network flows. Filtering network flows can reduce the resource usage of the network observability components.

You can configure two kinds of filters:

* eBPF agent filters
* Flowlogs-pipeline filters

#### [6.6.1. eBPF agent filters](#ebpf-agent-filters_network_observability) Copy linkLink copied to clipboard!

eBPF agent filters maximize performance because they take effect at the earliest stage of the network flows collection process.

To configure eBPF agent filters with the Network Observability Operator, see "Filtering eBPF flow data using multiple rules".

#### [6.6.2. Flowlogs-pipeline filters](#flowlogs-pipeline-filters_network_observability) Copy linkLink copied to clipboard!

Flowlogs-pipeline filters provide greater control over traffic selection because they take effect later in the network flows collection process. They are primarily used to improve data storage.

Flowlogs-pipeline filters use a simple query language to filter network flow, as shown in the following example:

```
(srcnamespace="netobserv" OR (srcnamespace="ingress" AND dstnamespace="netobserv")) AND srckind!="service"
```

The query language uses the following syntax:

Expand

Table 6.1. Query language syntax

| Category | Operators |
| --- | --- |
| Logical boolean operators (not case-sensitive) | `and`, `or` |
| Comparison operators | `=` (equals),  `!=` (not equals),  `=~` (matches regexp),  `!~` (not matches regexp),  `<` / `<=` (less than or equal to),  `>` / `>=` (greater than or equal to) |
| Unary operations | `with(field)` (field is present),  `without(field)` (field is absent) |

Show more

You can configure flowlogs-pipeline filters in the `spec.processor.filters` section of the `FlowCollector` resource. For example:

**Example YAML Flowlogs-pipeline filter**

```
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  agent:
  processor:
    filters:
      - query: |
          (SrcK8S_Namespace="netobserv" OR (SrcK8S_Namespace="openshift-ingress" AND DstK8S_Namespace="netobserv"))
        outputTarget: Loki
        sampling: 10
```

where:

`spec.processor.filters.outputTarget`
:   Specifies the output destination for matching flows, such as `Loki`, `Prometheus`, or an external system. If you omit this parameter, the system sends the flows to all configured outputs.

`spec.processor.filters.sampling`
:   Specifies an optional sampling interval to limit the number of matching flows stored or exported. For example, a value of `10` means there is a 1 in 10 chance that a flow is kept.

### [6.7. Configuring quick filters](#network-observability-config-quick-filters_network_observability) Copy linkLink copied to clipboard!

Use the list of available source, destination, and universal filter keys to modify quick filters within the `FlowCollector` resource.

Exact matches are possible using double-quotes around values. Otherwise, partial matches are used for textual values. The bang (!) character, placed at the end of a key, means negation. See the sample `FlowCollector` resource for more context about modifying the YAML.

Note

The filter matching types "all of" or "any of" is a UI setting that the users can modify from the query options. It is not part of this resource configuration.

Here is a list of all available filter keys:

Expand

Table 6.2. Filter keys

| Universal\* | Source | Destination | Description |
| --- | --- | --- | --- |
| namespace | `src_namespace` | `dst_namespace` | Filter traffic related to a specific namespace. |
| name | `src_name` | `dst_name` | Filter traffic related to a given leaf resource name, such as a specific pod, service, or node (for host-network traffic). |
| kind | `src_kind` | `dst_kind` | Filter traffic related to a given resource kind. The resource kinds include the leaf resource (Pod, Service or Node), or the owner resource (Deployment and StatefulSet). |
| owner\_name | `src_owner_name` | `dst_owner_name` | Filter traffic related to a given resource owner; that is, a workload or a set of pods. For example, it can be a Deployment name, a StatefulSet name, etc. |
| resource | `src_resource` | `dst_resource` | Filter traffic related to a specific resource that is denoted by its canonical name, that identifies it uniquely. The canonical notation is `kind.namespace.name` for namespaced kinds, or `node.name` for nodes. For example, `Deployment.my-namespace.my-web-server`. |
| address | `src_address` | `dst_address` | Filter traffic related to an IP address. IPv4 and IPv6 are supported. CIDR ranges are also supported. |
| mac | `src_mac` | `dst_mac` | Filter traffic related to a MAC address. |
| port | `src_port` | `dst_port` | Filter traffic related to a specific port. |
| host\_address | `src_host_address` | `dst_host_address` | Filter traffic related to the host IP address where the pods are running. |
| protocol | N/A | N/A | Filter traffic related to a protocol, such as TCP or UDP. |

Show more

* Universal keys filter for any of source or destination. For example, filtering `name: 'my-pod'` means all traffic from `my-pod` and all traffic to `my-pod`, regardless of the matching type used, whether **Match all** or **Match any**.

### [6.8. Resource management and performance considerations](#network-observability-resource-recommendations_network_observability) Copy linkLink copied to clipboard!

Review the key configuration settings, including eBPF sampling, feature enablement, and resource limits, necessary to manage performance criteria and optimize resource consumption for network observability.

The amount of resources required by network observability depends on the size of your cluster and your requirements for the cluster to ingest and store observability data. To manage resources and set performance criteria for your cluster, consider configuring the following settings. Configuring these settings might meet your optimal setup and observability needs.

The following settings can help you manage resources and performance from the outset:

eBPF Sampling
:   You can set the Sampling specification, `spec.agent.ebpf.sampling`, to manage resources. By default, eBPF sampling is set to `50`, so a flow has a 1 in 50 chance of being sampled. A lower sampling interval value requires more computational, memory, and storage resources. A value of `0` or `1` means all flows are sampled. It is recommended to start with the default value and refine it empirically to determine the optimal setting for your cluster.

eBPF features
:   The more features that are enabled, the more CPU and memory are impacted. See "Observing the network traffic" for a complete list of these features.

Without Loki
:   You can reduce the amount of resources that network observability requires by not using Loki and instead relying on Prometheus. For example, when network observability is configured without Loki, the total savings of memory usage are in the 20-65% range and CPU utilization is lower by 10-30%, depending upon the sampling interval value. See "Network observability without Loki" for more information.

Restricting or excluding interfaces
:   Reduce the overall observed traffic by setting the values for `spec.agent.ebpf.interfaces` and `spec.agent.ebpf.excludeInterfaces`. By default, the agent fetches all the interfaces in the system, except the ones listed in `excludeInterfaces` and `lo` (local interface). Note that the interface names might vary according to the Container Network Interface (CNI) used.

Performance fine-tuning
:   The following settings can be used to fine-tune performance after the Network Observability has been running for a while:

    * **Resource requirements and limits**: Adapt the resource requirements and limits to the load and memory usage you expect on your cluster by using the `spec.agent.ebpf.resources` and `spec.processor.resources` specifications. The default limits of 800MB might be sufficient for most medium-sized clusters.
    * **Cache max flows timeout**: Control how often flows are reported by the agents by using the eBPF agent’s `spec.agent.ebpf.cacheMaxFlows` and `spec.agent.ebpf.cacheActiveTimeout` specifications. A larger value results in less traffic being generated by the agents, which correlates with a lower CPU load. However, a larger value leads to a slightly higher memory consumption, and might generate more latency in the flow collection.

#### [6.8.1. Resource considerations](#network-observability-resources-table_network_observability) Copy linkLink copied to clipboard!

The Network Observability Operator configuration can be adjusted based on the cluster workload size. Use the following baseline examples to determine the appropriate resource limits and configuration settings for the environment.

The examples outlined in the table demonstrate scenarios that are tailored to specific workloads. Consider each example only as a baseline from which adjustments can be made to accommodate your workload needs.

The test beds used for these recommendations are:

* Extra small: 10-node cluster, 4 vCPUs and 16 GiB memory per worker, `LokiStack` size `1x.extra-small`, tested on AWS M6i instances.
* Small: 25-node cluster, 16 vCPUs and 64 GiB memory per worker, `LokiStack` size `1x.small`, tested on AWS M6i instances.
* Large: 250-node cluster, 16 vCPUs and 64 GiB memory per worker, `LokiStack` size `1x.medium`, tested on AWS M6i instances. In addition to the worker and controller nodes, three infrastructure nodes (size `M6i.12xlarge`) and one workload node (size `M6i.8xlarge`) were tested.

Expand

Table 6.3. Resource recommendations for cluster sizes

| Criterion | Extra small (10 nodes) | Small (25 nodes) | Large (250 nodes) |
| --- | --- | --- | --- |
| **Operator memory limit: `Subscription` `spec.config.resources`** | `400Mi` (default) | `400Mi` (default) | `400Mi` (default) |
| **eBPF agent sampling interval: `FlowCollector` `spec.agent.ebpf.sampling`** | `50` (default) | `50` (default) | `50` (default) |
| **eBPF agent memory limit: `FlowCollector` `spec.agent.ebpf.resources`** | `800Mi` (default) | `800Mi` (default) | `1600Mi` |
| **eBPF agent cache size: `FlowCollector` `spec.agent.ebpf.cacheMaxSize`** | `50,000` | `120,000` (default) | `120,000` (default) |
| **Processor memory limit: `FlowCollector` `spec.processor.resources`** | `800Mi` (default) | `800Mi` (default) | `800Mi` (default) |
| **Processor replicas: `FlowCollector` `spec.processor.consumerReplicas`** | `3` (default) | `6` | `18` |
| **Deployment model: `FlowCollector` `spec.deploymentModel`** | `Service` (default) | `Kafka` | `Kafka` |
| **Kafka partitions: Kafka installation** | N/A | `48` | `48` |
| **Kafka brokers: Kafka installation** | N/A | `3` (default) | `3` (default) |

Show more

#### [6.8.2. Total average memory and CPU usage](#network-observability-total-resource-usage-table_network_observability) Copy linkLink copied to clipboard!

Review the table detailing the total average CPU and memory usage for network observability components under two distinct traffic scenarios (`Test 1` and `Test 2`) at different eBPF sampling values.

The following table outlines averages of total resource usage for clusters with a sampling value of `1` and `50` for two different tests: `Test 1` and `Test 2`. The tests differ in the following ways:

* `Test 1` takes into account high ingress traffic volume in addition to the total number of namespace, pods and services in an OpenShift Container Platform cluster, places load on the eBPF agent, and represents use cases with a high number of workloads for a given cluster size. For example, `Test 1` consists of 76 Namespaces, 5153 Pods, and 2305 Services with a network traffic scale of ~350 MB/s.
* `Test 2` takes into account high ingress traffic volume in addition to the total number of namespace, pods and services in an OpenShift Container Platform cluster and represents use cases with a high number of workloads for a given cluster size. For example, `Test 2` consists of 553 Namespaces, 6998 Pods, and 2508 Services with a network traffic scale of ~950 MB/s.

Since different types of cluster use cases are exemplified in the different tests, the numbers in this table do not scale linearly when compared side-by-side. Instead, they are intended to be used as a benchmark for evaluating your personal cluster usage. The examples outlined in the table demonstrate scenarios that are tailored to specific workloads. Consider each example only as a baseline from which adjustments can be made to accommodate your workload needs.

Note

Metrics exported to Prometheus can impact the resource usage. Cardinality values for the metrics can help determine how much resources are impacted. For more information, see "Network Flows format" in the Additional resources section.

Expand

Table 6.4. Total average resource usage

| Sampling value | Resources used | Test 1 (25 nodes) | Test 2 (250 nodes) |
| --- | --- | --- | --- |
| **Sampling = 50** | Total NetObserv CPU Usage | 1.35 | 5.39 |
| Total NetObserv RSS (Memory) Usage | 16 GB | 63 GB |
| **Sampling = 1** | Total NetObserv CPU Usage | 1.82 | 11.99 |
| Total NetObserv RSS (Memory) Usage | 22 GB | 87 GB |

Show more

Summary: This table shows average total resource usage of Network Observability, which includes Agents, FLP, Kafka, and Loki with all features enabled. For details about what features are enabled, see the features covered in "Observing the network traffic", which comprises all the features that are enabled for this testing.

## [Chapter 7. Network observability per-tenant model](#network-observability-per-tenant-model_network_observability) Copy linkLink copied to clipboard!

Use the `FlowCollectorSlice` resource to delegate network traffic analysis management to project administrators while maintaining global cluster governance.

### [7.1. Per-tenant hierarchical governance and tenant autonomy](#network-observability-per-tenant-hierarchical-governance-and-tenant-autonomy_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Cluster administrators can maintain global governance while allowing project administrators to manage network traffic observability within their specific namespaces.

The Network Observability Operator uses a hierarchical configuration model to support multitenancy. This architecture is beneficial for large-scale deployments and hosted control planes environments where individual teams require self-service visibility without cluster administrator intervention.

The hierarchical model consists of the following components:

Global governance
:   The cluster administrator manages the global `FlowCollector` resource. This resource defines the observability infrastructure and determines if per-tenant configuration is permitted.

Tenant autonomy
:   The project administrator manages the `FlowCollectorSlice` resource. This namespace-scoped custom resource (CR) allows teams to define specific observability settings for their workloads.

### [7.2. FlowCollectorSlice resource for granular flow collection](#network-observability-per-tenant-flowcollector-slice-granular-flow-collection_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

The `FlowCollectorSlice` is a custom resource definition (CRD) that enables granular, multi-tenant network flow collection. By defining logical slices based on namespaces or subnets, you can selectively collect traffic and apply custom sampling to specific workloads rather than the entire cluster.

It complements the existing `FlowCollector` custom resource by enabling granular, selective, and multi-tenant-aware flow collection, instead of a single global configuration that applies uniformly to all traffic.

When slice-based collection is enabled, only traffic that matches at least one `FlowCollectorSlice` is collected, allowing administrators to precisely control which network flows are observed.

#### [7.2.1. Benefits of FlowCollectorSlice](#benefits-of-flowcollector-slice_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

By default, network flow collection applies uniformly to all traffic in the cluster. This can result in excessive data volume and limited flexibility.

Using `FlowCollectorSlice` provides the following benefits:

* Enables selective flow collection for specific namespaces or workloads.
* Supports multi-tenant and environment-based observability.
* Reduces storage and processing costs by filtering irrelevant traffic.
* Preserves backward compatibility through opt-in configuration.

#### [7.2.2. Relationship between FlowCollector and FlowCollectorSlice](#relationship-flowcollector-flowcollector-slice_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

While the `FlowCollector` resource defines global flow collection behavior for the cluster, the `FlowCollectorSlice` resource defines which traffic is eligible for collection when slice-based filtering is enabled.

The `FlowCollector.spec.slicesConfig` field controls how slice definitions are applied.

#### [7.2.3. Collection modes](#collection-modes_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Slice behavior is governed by the `FlowCollector.spec.slicesConfig.collectionMode` field. Set the field to one of the following collection modes:

AlwaysCollect
:   * Collects network flows from all cluster namespaces.
    * Applies the subnet and sampling configurations defined in `FlowCollectorSlice` resources.
    * Ignores the namespace selection logic in `FlowCollectorSlice` resources.
    * Maintains the default collection behavior for backward compatibility.

AllowList
:   * Collects only traffic that matches at least one `FlowCollectorSlice` resource.
    * An optional namespace allow list includes selected namespaces in the collection.

#### [7.2.4. FlowCollectorSlice status](#flowcollector-slice-status_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Each `FlowCollectorSlice` resource exposes a `status` subresource that reports:

* Validation results.
* Reconciliation state.
* Whether the slice is successfully applied.

This status allows administrators to verify that slice definitions are active and functioning as expected.

### [7.3. Enable the Network Observability Operator FlowCollectorSlice](#network-observability-per-tenant-flowcollector-slice-enable_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Enabling the `FlowCollectorSlice` feature in the `FlowCollector` resource allows cluster administrators to delegate flow collection and data enrichment management to specific namespaces.

Before project administrators can manage their own settings, a cluster administrator must enable the `FlowCollector` custom resource to watch for the `FlowCollectorSlice` custom resource.

**Prerequisites**

* The Network Observability Operator is installed.
* A `FlowCollector` custom resource exists in the cluster.
* You have `cluster-admin` privileges.

**Procedure**

1. Edit the `FlowCollector` custom resource by running the following command:

   ```
   $ oc edit flowcollector cluster
   ```
2. Configure the `spec.processor.slicesConfig` field to define which namespaces are permitted to use slices:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     processor:
       slicesConfig:
         enable: true
         collectionMode: AllowList
         namespacesAllowList:
          - /openshift-.*|netobserv.*/
   ```

   where:

   `spec.processor.sliceConfig.enable`
   :   Specifies if the `FlowCollectorSlice` feature is enabled. If not, all resources of kind `FlowCollectorSlice` are ignored.

   `spec.processor.sliceConfig.collectionMode`
   :   Specifies how the `FlowCollectorSlice` custom resources impacts the flow collection process. When set to `AlwaysCollect`, all flows are collected regardless of the presence of `FlowCollectorSlice`. When set to `AllowList`, only the flows related to namespaces where a `FlowCollectorSlice` resource is present, or configured via the global `namespacesAllowList`, are collected.

   `spec.processor.sliceConfig.namespacesAllowList`
   :   Specifies a list of namespaces for which flows are always collected, regardless of the presence of `FlowCollectorSlice` in those namespaces.

       Note

       The `namespacesAllowList` field supports regular expressions, such as `/openshift-.*/` to capture multiple namespaces, or strict equality, such as `netobserv`, to match a specific namespace.
3. Save the changes and exit the editor.

**Verification**

* Verify that only network flows from the `netobserv` namespace and namespaces starting with `openshift-` are displayed in the **Network Traffic** page of the web console.

#### [7.3.1. Disable the Network Observability Operator FlowCollectorSlice](#network-observability-per-tenant-flowcollector-slice-disable_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Disable slice-based filtering in the Network Observability Operator to resume global flow collection while preserving existing `FlowCollectorSlice` resources.

**Procedure**

1. Edit the `FlowCollector` resource by running the following command:

   ```
   $ oc edit flowcollector cluster
   ```
2. Set the `spec.processor.slicesConfig.collectionMode` field to `AlwaysCollect`:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     processor:
       slicesConfig:
         enable: true
         collectionMode: AlwaysCollect
         ...
   ```
3. Save the changes.

   Flow collection resumes for all traffic, and existing `FlowCollectorSlice` resources remain available for future use.

### [7.4. Configure the FlowCollectorSlice as a project administrator](#network-observability-per-tenant-flowcollector-slice-configure-project-administrator_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Project administrators can manage flow collection and data enrichment within their own namespaces by configuring a `FlowCollectorSlice` custom resource for decentralized network traffic analysis.

**Prerequisites**

* The Network Observability Operator is installed.
* You have `project-admin` permissions for the namespace.

**Procedure**

1. Create a YAML file named `flowCollectorSlice.yaml`:

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowCollectorSlice
   metadata:
     name: flowcollectorslice-sample
     namespace: my-app
   spec:
     sampling: 1
     subnetLabels:
       - name: EXT:Database
         cidrs:
           - 192.168.50.0/24
   ```
2. Apply the configuration by running the following command:

   ```
   $ oc apply -f flowCollectorSlice.yaml
   ```

**Verification**

1. In the OpenShift Container Platform console, navigate to **Observe** → **Network Traffic**.
2. Ensure flows to `192.168.50.0/24` subnet are observed with the `EXT:Database` label.

### [7.5. FlowCollectorSlice [flows.netobserv.io/v1alpha1]](#flowcollectorslice-flows-netobserv-io-v1alpha1_network-observability-per-tenant-configuration) Copy linkLink copied to clipboard!

Description
:   FlowCollectorSlice is the API allowing to decentralize some of the FlowCollector configuration per namespace tenant.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and might reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers might infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | `object` | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | FlowCollectorSliceSpec defines the desired state of FlowCollectorSlice |

Show more

#### [7.5.1. .metadata](#metadata) Copy linkLink copied to clipboard!

Description
:   Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>

Type
:   `object`

#### [7.5.2. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   FlowCollectorSliceSpec defines the desired state of FlowCollectorSlice

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `sampling` | `integer` | `sampling` is an optional sampling interval to apply to this slice. For example, a value of `50` means that 1 matching flow in 50 is sampled. |
| `subnetLabels` | `array` | `subnetLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided.  Beware that the subnet labels configured in FlowCollectorSlice are not limited to the flows of the related namespace: any flow in the whole cluster can be labeled using this configuration. However, subnet labels defined in the cluster-scoped FlowCollector take precedence in case of conflicting rules. |

Show more

#### [7.5.3. .spec.subnetLabels](#spec-subnetlabels) Copy linkLink copied to clipboard!

Description
:   `subnetLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided.

    Beware that the subnet labels configured in FlowCollectorSlice are not limited to the flows of the related namespace: any flow in the whole cluster can be labeled using this configuration. However, subnet labels defined in the cluster-scoped FlowCollector take precedence in case of conflicting rules.

Type
:   `array`

#### [7.5.4. .spec.subnetLabels[]](#spec-subnetlabels-2) Copy linkLink copied to clipboard!

Description
:   SubnetLabel allows to label subnets and IPs, such as to identify cluster-external workloads or web services.

Type
:   `object`

Required
:   * `cidrs`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cidrs` | `array (string)` | List of CIDRs, such as `["1.2.3.4/32"]`. |
| `name` | `string` | Label name, used to flag matching flows. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided. |

Show more

## [Chapter 8. Network Policy](#network-observability-network-policy) Copy linkLink copied to clipboard!

As an administrator, you can create a network policy for the `netobserv` namespace. This policy secures inbound and outbound access to the Network Observability Operator.

### [8.1. Configuring network policy by using the FlowCollector custom resource](#network-observability-deploy-network-policy_network_observability) Copy linkLink copied to clipboard!

You can set up ingress and egress network policies to control pod traffic. This enhances security and collects only the network flow data you need. This reduces noise, supports compliance, and improves visibility into network communication.

You can configure the `FlowCollector` custom resource (CR) to deploy an egress and ingress network policy for network observability. By default, the `spec.NetworkPolicy.enable` specification is set to `true`.

If you have installed Loki, Kafka or any exporter in a different namespace that also has a network policy, you must ensure that the network observability components can communicate with them. Consider the following about your setup:

* Connection to Loki (as defined in the `FlowCollector` CR `spec.loki` parameter)
* Connection to Kafka (as defined in the `FlowCollector` CR `spec.kafka` parameter)
* Connection to any exporter (as defined in FlowCollector CR `spec.exporters` parameter)
* If you are using Loki and including it in the policy target, connection to an external object storage (as defined in your `LokiStack` related secret)

**Procedure**

1. In the web console, go to **Ecosystem** → **Installed Operators** page.
2. Under the **Provided APIs** heading for **Network Observability**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab.
4. Configure the `FlowCollector` CR. A sample configuration is as follows:

   **Example `FlowCollector` CR for network policy**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     networkPolicy:
       enable: true
       additionalNamespaces: ["openshift-console", "openshift-monitoring"]
   # ...
   ```

   where:

   `spec.networkPolicy.enable`
   :   Specifies whether to enable network policy management. The default value is `true`.

   `spec.networkPolicy.additionalNamespaces`
   :   Specifies the namespaces to include in the network policy. The default values are `["openshift-console", "openshift-monitoring"]`.

## [Chapter 9. Network observability DNS resolution analysis](#network-observability-dns-resolution-analysis_network_observability) Copy linkLink copied to clipboard!

Learn how DNS resolution analysis uses eBPF-based decoding to identify service discovery issues and follow the steps to enable DNS tracking in the FlowCollector resource to enrich network flow records with domain names.

### [9.1. Strategic benefits of DNS resolution analysis](#network-observability-dns-resolution-analysis-strategic-benefits_network-observability-dns-decoding) Copy linkLink copied to clipboard!

Use DNS resolution analysis to differentiate between network transport failures and service discovery issues by enriching eBPF flow records with domain names and status codes.

Standard flow logs only show that traffic occurred on port 53. DNS resolution analysis allows you to complete the following tasks:

* Reduced Mean time to identify (Mtti): Distinguish immediately between a network routing failure and a DNS resolution failure, such as an `NXDOMAIN` error.
* Measure internal service latency: Track the time it takes for CoreDNS to respond to specific internal lookups (e.g., `my-service.namespace.svc.cluster.local`).
* Audit external dependencies: Audit which external APIs or third-party domains your workloads are communicating with without requiring sidecars or manual packet captures.
* Improved security posture: Detect potential data exfiltration or Command and Control (C2) activity by auditing the Fully Qualified Domain Names (FQDNs) queried by internal workloads.

#### [9.1.1. DNS flow enrichment](#dns-flow-enrichment_network-observability-dns-decoding) Copy linkLink copied to clipboard!

When this feature is active, the eBPF agent enriches the flow records. This metadata allows you to group and filter traffic by the intent of the connection (the domain) rather than just the source IP.

Enhanced DNS decoding allows the eBPF agent to inspect UDP and TCP DNS traffic on port 53 along with the query names for the DNS request.

### [9.2. Configure DNS domain tracking for network observability](#network-observability-dns-resolution-analysis-configure_network-observability-dns-decoding) Copy linkLink copied to clipboard!

Enable DNS tracking in the Network Observability Operator to monitor DNS query names, response codes, and latency for network flows within the cluster.

**Prerequisites**

* The Network Observability Operator is installed.
* You have `cluster-admin` privileges.
* You are familiar with the `FlowCollector` custom resource.

**Procedure**

1. Edit the `FlowCollector` resource by running the following command:

   ```
   $ oc edit flowcollector cluster
   ```
2. Configure the eBPF agent to enable the DNS tracking feature:

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     agent:
       type: eBPF
       ebpf:
         features:
           - DNSTracking
   ```

   where:

   `spec.agent.type.ebpf.features`
   :   Specifies the list of features to enable for the eBPF agent. To enable DNS tracking, add `DNSTracking` to this list.
3. Save and exit the editor.

**Verification**

1. In the OpenShift Container Platform web console, navigate to **Observe** → **Network Traffic**.
2. In the **Traffic Flows** view, click the **Manage columns** icon.
3. Ensure that the **DNS Query Name**, **DNS Response Code**, and **DNS Latency** columns are selected.
4. Filter the results by setting **Port** to `53`.
5. Confirm that the flow table columns are populated with domain names and DNS metadata.

### [9.3. DNS flow enrichment and analysis reference](#network-observability-dns-resolution-analysis-reference_network-observability-dns-decoding) Copy linkLink copied to clipboard!

Identify metadata added to network flows, leverage DNS data for network optimization, and understand the performance and storage impacts on the cluster.

The following table describes the metadata fields added to network flows when DNS tracking is enabled.

Note

Query names might be missing or truncated because of compression pointers or cache limitations.

Expand

Table 9.1. DNS flow metadata

| Field | Description | Example |
| --- | --- | --- |
| `dns_query_name` | The Fully Qualified Domain Name (FQDN) being queried. | `example.com` |
| `dns_response_code` | The status code returned by the DNS server. | `NoError`, `NXDomain` |
| `dns_id` | The transaction ID used to match queries with responses. | `45213` |

Show more

#### [9.3.1. Leverage DNS data for network optimization](#leverage-dns-data-optimization_network-observability-dns-decoding) Copy linkLink copied to clipboard!

Use the captured DNS metadata for the following operational outcomes:

* Audit external dependencies: Ensure workloads are not reaching out to unauthorized external APIs or high-risk domains.
* Performance tuning: Monitor `DNS Latency` to identify if `CoreDNS` pods require additional scaling or if upstream DNS providers are lagging.

#### [9.3.2. Identify misconfiguration errors](#identify-misconfiguration-errors_network-observability-dns-decoding) Copy linkLink copied to clipboard!

A high frequency of `NXDOMAIN` responses typically indicates service discovery errors in application code or stale environment variables.

`NXDOMAIN` errors can be frequent in Kubernetes because of DNS searches on services and pods. While these results do not necessarily indicate a misconfiguration or broken URL, they can negatively impact performance.

When `NXDOMAIN` errors are returned despite an apparently valid Service or Pod host name, such as `my-svc.my-namespace.svc`, the resolver is likely configured to query DNS for different suffixes. You can optimize this by adding a trailing dot to fully qualified domain names to tell the resolver that the name is unambiguous.

For example, instead of `https://my-svc.my-namespace.svc`, use `https://my-svc.my-namespace.svc.cluster.local.` with a trailing dot.

#### [9.3.3. Loki storage considerations](#loki-storage-considerations_network-observability-dns-decoding) Copy linkLink copied to clipboard!

DNS tracking increases the number of labels and the amount of metadata per flow. Ensure that the Loki storage is sized to accommodate the increased log volume.

## [Chapter 10. Observing the network traffic](#nw-observe-network-traffic) Copy linkLink copied to clipboard!

As an administrator, you can observe the network traffic in the OpenShift Container Platform web console for detailed troubleshooting and analysis. This feature helps you get insights from different graphical representations of traffic flow.

### [10.1. Observing the network traffic from the Overview view](#network-observability-network-traffic-overview-view_nw-observe-network-traffic) Copy linkLink copied to clipboard!

The Network Traffic **Overview** view provides aggregated flow metrics and visual insights into application communications. Administrators can use the metrics to monitor data volume, troubleshoot connectivity, and detect unusual traffic patterns across the cluster.

The **Overview** view shows aggregate network traffic in your OpenShift Container Platform cluster, allowing you to see which applications are communicating and the volume of data being transferred. It provides detailed insights by source, destination, and flow type, along with the top traffic flows and average byte rates.

As an administrator, you can troubleshoot connectivity issues, detect unusual traffic patterns, and optimize application performance. It provides a quick overview of network behavior, making it easier to prioritize actions and ensure efficient resource usage.

#### [10.1.1. Working with the Overview view](#network-observability-working-with-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Navigate to the network traffic **Overview** view in the OpenShift Container Platform console to see graphical representations of flow rate statistics and configure the display scope using available options.

**Prerequisite**

* Access to the cluster with administrator rights.

**Procedure**

1. Navigate to **Observe** → **Network Traffic**.
2. In the **Network Traffic** page, click the **Overview** tab.
3. Click the menu icon to configure the scope of each flow rate data.

#### [10.1.2. Configuring advanced options for the Overview view](#network-observability-configuring-options-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Customize the network traffic **Overview** view by configuring advanced options, such as graph scope, label truncation, and panel management, to refine the display of flow rate statistics and traffic data.

To access the advanced options, click **Show advanced options**. You can configure the details in the graph by using the **Display options** drop-down menu. The options available are as follows:

* **Scope**: Select to view the components that network traffic flows between. You can set the scope to **Node**, **Namespace**, **Owner**, **Zones**, **Cluster** or **Resource**. **Owner** is an aggregation of resources. **Resource** can be a pod, service, node, in case of host-network traffic, or an unknown IP address. The default value is **Namespace**.
* **Truncate labels**: Select the required width of the label from the drop-down list. The default value is **M**.

##### [10.1.2.1. Managing panels and display](#network-observability-cao-managing-panels-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

You can select the required panels to be displayed, reorder them, and focus on a specific panel. To add or remove panels, click **Manage panels**.

The following panels are shown by default:

* **Top X average bytes rates**
* **Top X bytes rates stacked with total**

Other panels can be added in **Manage panels**:

* **Top X average packets rates**
* **Top X packets rates stacked with total**

**Query options** allows you to choose whether to show the **Top 5**, **Top 10**, or **Top 15** rates.

#### [10.1.3. Packet drop tracking](#network-observability-pktdrop-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Monitor and analyze network packet loss by using eBPF-based packet drop tracking, which identifies drop locations, detects host or OVS-specific drop reasons, and provides dedicated graphical panels in the **Overview** view.

You can configure graphical representation of network flow records with packet loss in the **Overview** view. By employing eBPF tracepoint hooks, you can gain valuable insights into packet drops for TCP, UDP, SCTP, ICMPv4, and ICMPv6 protocols, which can result in the following actions:

* Identification: Pinpoint the exact locations and network paths where packet drops are occurring. Determine whether specific devices, interfaces, or routes are more prone to drops.
* Root cause analysis: Examine the data collected by the eBPF program to understand the causes of packet drops. For example, are they a result of congestion, buffer issues, or specific network events?
* Performance optimization: With a clearer picture of packet drops, you can take steps to optimize network performance, such as adjust buffer sizes, reconfigure routing paths, or implement Quality of Service (QoS) measures.

When packet drop tracking is enabled, you can see the following panels in the **Overview** by default:

* **Top X packet dropped state stacked with total**
* **Top X packet dropped cause stacked with total**
* **Top X average dropped packets rates**
* **Top X dropped packets rates stacked with total**

Other packet drop panels are available to add in **Manage panels**:

* **Top X average dropped bytes rates**
* **Top X dropped bytes rates stacked with total**

##### [10.1.3.1. Types of packet drops](#types-of-packet-drops) Copy linkLink copied to clipboard!

Two kinds of packet drops are detected by network observability: host drops and OVS drops. Host drops are prefixed with `SKB_DROP` and OVS drops are prefixed with `OVS_DROP`. Dropped flows are shown in the side panel of the **Traffic flows** table along with a link to a description of each drop type. Examples of host drop reasons are as follows:

* `SKB_DROP_REASON_NO_SOCKET`: the packet dropped due to a missing socket.
* `SKB_DROP_REASON_TCP_CSUM`: the packet dropped due to a TCP checksum error.

Examples of OVS drops reasons are as follows:

* `OVS_DROP_LAST_ACTION`: OVS packets dropped due to an implicit drop action, for example due to a configured network policy.
* `OVS_DROP_IP_TTL`: OVS packets dropped due to an expired IP TTL.

See the *Additional resources* of this section for more information about enabling and working with packet drop tracking.

#### [10.1.4. Working with packet drops](#network-observability-packet-drops_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Enable packet drop tracking in the Network Observability Operator by configuring the `FlowCollector` resource to monitor and visualize network data loss in the web console.

Packet loss occurs when one or more packets of network flow data fail to reach their destination. You can track these drops by editing the `FlowCollector` to the specifications in the following YAML example.

Important

CPU and memory usage increases when this feature is enabled.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster**, and then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource for packet drops, for example:

   **Example `FlowCollector` configuration**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     agent:
       type: eBPF
       ebpf:
         features:
          - PacketDrop
         privileged: true
   ```

   where:

   `spec.agent.ebpf.features`
   :   Specifies the features to enable. Include `PacketDrop` to start reporting packet drops for each network flow.

   `spec.agent.ebpf.privileged`
   :   Specifies whether privileged mode is enabled. Must be set to `true` for packet drop tracking.

**Verification**

* When you refresh the **Network Traffic** page, the **Overview**, **Traffic Flow**, and **Topology** views display new information about packet drops:

  1. Select new choices in **Manage panels** to choose which graphical visualizations of packet drops to display in the **Overview**.
  2. Select new choices in **Manage columns** to choose which packet drop information to display in the **Traffic flows** table.

     1. In the **Traffic Flows** view, you can also expand the side panel to view more information about packet drops. Host drops are prefixed with `SKB_DROP` and OVS drops are prefixed with `OVS_DROP`.
  3. In the **Topology** view, red lines are displayed where drops are present.

#### [10.1.5. DNS tracking](#network-observability-dns-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Monitor DNS activity by using eBPF-based DNS tracking to gain insights into query patterns, detect security threats, and troubleshoot latency issues through dedicated graphical panels in the **Overview** view.

You can configure graphical representation of Domain Name System (DNS) tracking of network flows in the **Overview** view. Using DNS tracking with extended Berkeley Packet Filter (eBPF) tracepoint hooks can serve various purposes:

* Network Monitoring: Gain insights into DNS queries and responses, helping network administrators identify unusual patterns, potential bottlenecks, or performance issues.
* Security Analysis: Detect suspicious DNS activities, such as domain name generation algorithms (DGA) used by malware, or identify unauthorized DNS resolutions that might indicate a security breach.
* Troubleshooting: Debug DNS-related issues by tracing DNS resolution steps, tracking latency, and identifying misconfigurations.

By default, when DNS tracking is enabled, you can see the following non-empty metrics represented in a donut or line chart in the **Overview**:

* Top X DNS Response Code
* Top X average DNS latencies with overall
* Top X 90th percentile DNS latencies

Other DNS tracking panels can be added in **Manage panels**:

* Bottom X minimum DNS latencies
* Top X maximum DNS latencies
* Top X 99th percentile DNS latencies

This feature is supported for IPv4 and IPv6 UDP and TCP protocols.

See the *Additional resources* in this section for more information about enabling and working with this view.

#### [10.1.6. Working with DNS tracking](#network-observability-dns-tracking_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Configure the `FlowCollector` custom resource to enable DNS tracking for monitoring network performance, security analysis, and DNS troubleshooting in the web console.

You can track DNS by editing the `FlowCollector` to the specifications in the following YAML example.

Important

CPU and memory usage increases are observed in the eBPF agent when this feature is enabled.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for **Network Observability**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource. A sample configuration is as follows:

   **Configure `FlowCollector` for DNS tracking**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     agent:
       type: eBPF
       ebpf:
         features:
          - DNSTracking
         sampling: 1
   ```

   * You can set the `spec.agent.ebpf.features` parameter list to enable DNS tracking of each network flow in the web console.
   * You can set `sampling` to a value of `1` for more accurate metrics and to capture **DNS latency**. For a `sampling` value greater than 1, you can observe flows with **DNS Response Code** and **DNS Id**, and it is unlikely that **DNS Latency** can be observed.
5. When you refresh the **Network Traffic** page, there are new DNS representations you can choose to view in the **Overview** and **Traffic Flow** views and new filters you can apply.

   1. Select new DNS choices in **Manage panels** to display graphical visualizations and DNS metrics in the **Overview**.
   2. Select new choices in **Manage columns** to add DNS columns to the **Traffic Flows** view.
   3. Filter on specific DNS metrics, such as **DNS Id**, **DNS Error** **DNS Latency** and **DNS Response Code**, and see more information from the side panel. The **DNS Latency** and **DNS Response Code** columns are shown by default.

      Note

      TCP handshake packets do not have DNS headers. TCP protocol flows without DNS headers are shown in the traffic flow data with **DNS Latency**, **ID**, and **Response code** values of "n/a". You can filter out flow data to view only flows that have DNS headers using the **Common** filter "DNSError" equal to "0".

#### [10.1.7. Round-Trip Time](#network-observability-RTT-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Analyze network flow latencies by using TCP Round-Trip Time (RTT) metrics, which use eBPF hookpoints to identify performance bottlenecks and troubleshoot TCP-related issues through dedicated panels in the Overview view.

You can use TCP smoothed Round-Trip Time (sRTT) to analyze network flow latencies. You can use RTT captured from the `fentry/tcp_rcv_established` eBPF hookpoint to read sRTT from the TCP socket to help with the following:

* Network Monitoring: Gain insights into TCP latencies, helping network administrators identify unusual patterns, potential bottlenecks, or performance issues.
* Troubleshooting: Debug TCP-related issues by tracking latency and identifying misconfigurations.

By default, when RTT is enabled, you can see the following TCP RTT metrics represented in the **Overview**:

* Top X 90th percentile TCP Round Trip Time with overall
* Top X average TCP Round Trip Time with overall
* Bottom X minimum TCP Round Trip Time with overall

Other RTT panels can be added in **Manage panels**:

* Top X maximum TCP Round Trip Time with overall
* Top X 99th percentile TCP Round Trip Time with overall

See the *Additional resources* in this section for more information about enabling and working with this view.

#### [10.1.8. Working with RTT tracing](#network-observability-RTT_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Enable Round Trip Time (RTT) tracing by configuring the `FlowCollector` custom resource to monitor and analyze network latency across your cluster by using the web console.

You can track RTT by editing the `FlowCollector` to the specifications in the following YAML example.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster**, and then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource for RTT tracing, for example:

   **Example `FlowCollector` configuration**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     agent:
       type: eBPF
       ebpf:
         features:
          - FlowRTT
   ```

   where:

   `spec.agent.ebpf.features`
   :   Specifies the list of eBPF features to enable. Add `FlowRTT` to this list to start tracing Round-trip time (RTT) network flows.

**Verification**

After the **Network Traffic** page is refreshed, the **Overview**, **Traffic flows**, and **Topology** views display RTT information.

1. In the **Overview** view, click **Manage panels** to select the RTT graphical visualizations to display.
2. In the **Traffic flows** table, verify that the **Flow RTT** column is visible by default. To manage columns, click **Manage columns**.
3. In the **Traffic flows** view, expand the side panel to view RTT metadata:

   1. Filter the flow data for the **TCP** protocol by entering `protocol=TCP` in the filter search bar.
   2. Verify that all TCP filtered flows have **FlowRTT** values greater than `0`.
   3. Filter for **FlowRTT** values greater than `10,000,000` nanoseconds (10 ms) by entering `time_flow_rtt>=10000000` in the filter search bar.
   4. Remove the filters.
4. In the **Topology** view, click the **Display** option drop-down menu. In the **Edge labels** list, select **RTT**.

#### [10.1.9. eBPF flow rule filter](#network-observability-ebpf-flow-rule-filter_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Control packet capture volume by using eBPF flow rule filtering to specify capture criteria based on ports and CIDR notation, while monitoring filter performance through dedicated health dashboards and Prometheus metrics.

You can use rule-based filtering to control the volume of packets cached in the eBPF flow table. For example, a filter can specify that only packets coming from port 100 should be captured. Then only the packets that match the filter are captured and the rest are dropped.

You can apply multiple filter rules.

##### [10.1.9.1. Ingress and egress traffic filtering](#ingress-and-egress-traffic-filtering_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Classless Inter-Domain Routing (CIDR) notation efficiently represents IP address ranges by combining the base IP address with a prefix length. For both ingress and egress traffic, the source IP address is first used to match filter rules configured with CIDR notation. If there is a match, then the filtering proceeds. If there is no match, then the destination IP is used to match filter rules configured with CIDR notation.

After matching either the source IP or the destination IP CIDR, you can pinpoint specific endpoints using the `peerIP` to differentiate the destination IP address of the packet. Based on the provisioned action, the flow data is either cached in the eBPF flow table or not cached.

##### [10.1.9.2. Dashboard and metrics integrations](#dashboard-and-metrics-integrations_nw-observe-network-traffic) Copy linkLink copied to clipboard!

When this option is enabled, the **Netobserv/Health** dashboard for **eBPF agent statistics** now has the **Filtered flows rate** view. Additionally, in **Observe** → **Metrics** you can query `netobserv_agent_filtered_flows_total` to observe metrics with the reason in **FlowFilterAcceptCounter**, **FlowFilterNoMatchCounter** or **FlowFilterRecjectCounter**.

##### [10.1.9.3. Flow filter configuration parameters](#network-observability-flowcollector-flowfilter-parameters_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Reference the required and optional parameters for configuring flow filter rules in the `FlowCollector` resource, including CIDR ranges, filter actions, protocols, and specific port configurations.

Expand

Table 10.1. Required configuration parameters

| Parameter | Description |
| --- | --- |
| `enable` | Set `enable` to `true` to enable the eBPF flow filtering feature. |
| `cidr` | Provides the IP address and CIDR mask for the flow filter rule. Supports both IPv4 and IPv6 address format. If you want to match against any IP, you can use `0.0.0.0/0` for IPv4 or `::/0` for IPv6. |
| `action` | Describes the action that is taken for the flow filter rule. The possible values are `Accept` or `Reject`.  * For the `Accept` action matching rule, the flow data is cached in the eBPF table and updated with the global metric, `FlowFilterAcceptCounter`. * For the `Reject` action matching rule, the flow data is dropped and not cached in the eBPF table. The flow data is updated with the global metric, `FlowFilterRejectCounter`. * If the rule is not matched, the flow is cached in the eBPF table and updated with the global metric, `FlowFilterNoMatchCounter`. |

Show more

Expand

Table 10.2. Optional configuration parameters

| Parameter | Description |
| --- | --- |
| `direction` | Defines the direction of the flow filter rule. Possible values are `Ingress` or `Egress`. |
| `protocol` | Defines the protocol of the flow filter rule. Possible values are `TCP`, `UDP`, `SCTP`, `ICMP`, and `ICMPv6`. |
| `tcpFlags` | Defines the TCP flags to filter flows. Possible values are `SYN`, `SYN-ACK`, `ACK`, `FIN`, `RST`, `PSH`, `URG`, `ECE`, `CWR`, `FIN-ACK`, and `RST-ACK`. |
| `ports` | Defines the ports to use for filtering flows. It can be used for either source or destination ports. To filter a single port, set a single port as an integer value. For example `ports: 80`. To filter a range of ports, use a "start-end" range in string format. For example `ports: "80-100"` |
| `sourcePorts` | Defines the source port to use for filtering flows. To filter a single port, set a single port as an integer value, for example `sourcePorts: 80`. To filter a range of ports, use a "start-end" range, string format, for example `sourcePorts: "80-100"`. |
| `destPorts` | DestPorts defines the destination ports to use for filtering flows. To filter a single port, set a single port as an integer value, for example `destPorts: 80`. To filter a range of ports, use a "start-end" range in string format, for example `destPorts: "80-100"`. |
| `icmpType` | Defines the ICMP type to use for filtering flows. |
| `icmpCode` | Defines the ICMP code to use for filtering flows. |
| `peerIP` | Defines the IP address to use for filtering flows, for example: `10.10.10.10`. |

Show more

#### [10.1.10. Filtering eBPF flow data using multiple rules](#network-observability-filtering-ebpf-rule_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Configure multiple filtering rules in the `FlowCollector` custom resource to refine network traffic data collection by accepting or rejecting specific eBPF flows based on IP addresses and packet conditions.

Important

* You cannot use duplicate Classless Inter-Domain Routing (CIDRs) in filter rules.
* When an IP address matches multiple filter rules, the rule with the most specific CIDR prefix (longest prefix) takes precedence.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for **Network Observability**, select **Flow Collector**.
3. Select **cluster**, then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource.

#### [10.1.11. eBPF flow data filtering examples](#network-observability-ebpf-flow-data-filtering-examples_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Use these `FlowCollector` custom resource examples to filter eBPF flows using multiple rules to control the flow of packets cached in the eBPF flow table.

##### [10.1.11.1. Example YAML to sample all North-South traffic, and 1:50 East-West traffic](#example-yaml-sample-all-north-south-traffic_nw-observe-network-traffic) Copy linkLink copied to clipboard!

By default, all other flows are rejected.

```
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  agent:
    type: eBPF
    ebpf:
      flowFilter:
        enable: true
        rules:
         - action: Accept
           cidr: 0.0.0.0/0
           sampling: 1
         - action: Accept
           cidr: 10.128.0.0/14
           peerCIDR: 10.128.0.0/14
         - action: Accept
           cidr: 172.30.0.0/16
           peerCIDR: 10.128.0.0/14
           sampling: 50
```

where:

`spec.agent.ebpf.flowFilter.enable`
:   Specifies whether to enable `eBPF` flow filtering. Set to `true` to enable flow filtering.

`spec.agent.ebpf.flowFilter.rules.action`
:   Specifies the action for the flow filter rule. Valid values are `Accept` or `Reject`.

`spec.agent.ebpf.flowFilter.rules.cidr`
:   Specifies the IP address and `CIDR` mask for the flow filter rule. This parameter supports both `IPv4` and `IPv6` address formats. Use `0.0.0.0/0` for `IPv4` or `::/0` for `IPv6` to match any IP address.

`spec.agent.ebpf.flowFilter.rules.peerCIDR`
:   Specifies the Peer IP `CIDR` used to filter flows.

`spec.agent.ebpf.flowFilter.rules.sampling`
:   Specifies the sampling interval for matched flows. This value overrides the global sampling setting defined in `spec.agent.ebpf.sampling`.

##### [10.1.11.2. Example YAML to filter flows with packet drops](#example-yaml-filter-flows-with-packet-drops_nw-observe-network-traffic) Copy linkLink copied to clipboard!

By default, all other flows are rejected.

```
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  namespace: netobserv
  deploymentModel: Service
  agent:
    type: eBPF
    ebpf:
      privileged: true
      features:
        - PacketDrop
      flowFilter:
        enable: true
        rules:
        - action: Accept
          cidr: 172.30.0.0/16
          pktDrops: true
```

where:

`spec.agent.ebpf.privileged`
:   Specifies whether to enable privileged mode, which is required for reporting packet drops.

`spec.agent.ebpf.features`
:   Specifies the list of eBPF features to enable. Adding the `PacketDrop` value to this list reports packet drops for each network flow.

`spec.agent.ebpf.flowFilter.enable`
:   Specifies whether to enable `eBPF` flow filtering.

`spec.agent.ebpf.flowFilter.rules.action`
:   Specifies the action for the flow filter rule. Valid values are `Accept` or `Reject`.

`spec.agent.ebpf.flowFilter.rules.pktDrops`
:   Specifies whether to filter for flows that contain packet drops.

#### [10.1.12. User-defined networks](#network-observability-user-defined-networks_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Understand how you can use user-defined networks (UDN) for flexible network segmentation and leverage the Network Observability Operator to monitor these segments through dedicated labels and name filters in the traffic flow table.

User-defined networks (UDN) improve the flexibility and segmentation capabilities of the default Layer 3 topology for a Kubernetes pod network by enabling custom Layer 2 and Layer 3 network segments, where all these segments are isolated by default. These segments act as primary or secondary networks for container pods and virtual machines that use the default OVN-Kubernetes CNI plugin.

UDNs enable a wide range of network architectures and topologies, enhancing network flexibility, security, and performance.

When the `UDNMapping` feature is enabled with Network Observability, the **Traffic** flow table has a **UDN labels** column. You can filter on **Source Network Name** and **Destination Network Name**.

#### [10.1.13. Working with user-defined networks](#network-observability-working-with-udn_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Configure the `FlowCollector` custom resource to enable user-defined network (UDN) mapping, providing visibility into traffic across custom network interfaces within the web console.

You can enable user-defined networks (UDN) in network observability resources. The following example shows the configuration for the `FlowCollector` resource.

**Prerequisite**

* You have configured UDN in Red Hat OpenShift Networking. For more information, see "Creating a UserDefinedNetwork by using the CLI" or "Creating a UserDefinedNetwork by using the web console."

**Procedure**

1. Edit the network observability `FlowCollector` resource by running the following command:

   ```
   $ oc edit flowcollector
   ```
2. Configure the `ebpf` section of the `FlowCollector` resource:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     agent:
       ebpf:
         sampling: 1
         privileged: true
         features:
         - UDNMapping
   ```

   where:

   `spec.agent.ebpf.sampling`
   :   Specifies sampling rate for network events. Set to a value of `1` to capture all network events. If sampling `1` is too resource heavy, set sampling to something more appropriate for your needs.

   `spec.agent.ebpf.privileged`
   :   Specifies whether privileged mode is enabled. Must be set to `true` for user-defined network mapping.

**Verification**

* Refresh the **Network Traffic** page to view updated UDN information in the **Traffic Flow** and **Topology** views:

  + In **Network Traffic** > **Traffic flows**, you can view UDNs under the `SrcK8S_NetworkName` and `DstK8S_NetworkName` fields.
  + In the **Topology** view, you can set **Network** as **Scope** or **Group**.

#### [10.1.14. OVN-Kubernetes networking events](#network-observability-networking-events-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Use OVN-Kubernetes network event tracking to monitor and audit network policies, admin network policies, and egress firewall rules in your cluster.

Important

OVN-Kubernetes networking events tracking is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You can use the insights from tracking network events to help with the following tasks:

* Network monitoring: Monitor allowed and blocked traffic, detecting whether packets are allowed or blocked based on network policies and admin network policies.
* Network security: You can track outbound traffic and see whether it adheres to egress firewall rules. Detect unauthorized outbound connections and flag outbound traffic that violates egress rules.

See the *Additional resources* in this section for more information about enabling and working with this view.

#### [10.1.15. Viewing network events](#network-observability-viewing-network-events_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Configure the `FlowCollector` custom resource to enable network event tracking for auditing how security policies, firewalls, and isolation rules affect traffic flows in the web console.

Important

OVN-Kubernetes networking events tracking is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You can edit the `FlowCollector` to view information about network traffic events, such as network flows that are dropped or allowed by the following resources:

* `NetworkPolicy`
* `AdminNetworkPolicy`
* `BaselineNetworkPolicy`
* `EgressFirewall`
* `UserDefinedNetwork` isolation
* Multicast ACLs

**Prerequisites**

* You must have `OVNObservability` enabled by setting the `TechPreviewNoUpgrade` feature set in the `FeatureGate` custom resource (CR) named `cluster`. For more information, see "Enabling feature sets using the CLI" and "Checking OVN-Kubernetes network traffic with OVS sampling using the CLI".
* You have created at least one of the following network APIs: `NetworkPolicy`, `AdminNetworkPolicy`, `BaselineNetworkPolicy`, `UserDefinedNetwork` isolation, multicast, or `EgressFirewall`.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster**, and then select the **YAML** tab.
4. Configure the `FlowCollector` CR to enable viewing `NetworkEvents`, for example:

   **Example `FlowCollector` configuration**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
      agent:
       type: eBPF
       ebpf:
     #   sampling: 1
         privileged: true
         features:
          - "NetworkEvents"
   ```

   where:

   `spec.agent.ebpf.sampling`
   :   Specifies the sampling rate for network events. Set to a value of `1` to capture all network events. If the sampling `1` is too resource heavy, set sampling to something more appropriate for your needs. This value is optional.

   `spec.agent.ebpf.privileged`
   :   Specifies whether the eBPF agent runs in privileged mode. Set to `true` because the OVN observability library needs to access local Open vSwitch (OVS) socket and Open Virtual Network (OVN) databases.

**Verification**

1. Navigate to the **Network Traffic** view and select the **Traffic flows** table.
2. You should see the new column, **Network Events**, where you can view information about impacts of one of the following network APIs you have enabled: `NetworkPolicy`, `AdminNetworkPolicy`, `BaselineNetworkPolicy`, `UserDefinedNetwork` isolation, multicast, or egress firewalls.

   An example of the kind of events you could see in this column is as follows:

   **Example of Network Events output**

   ```
   <Dropped_or_Allowed> by <network_event_and_event_name>, direction <Ingress_or_Egress>
   ```

### [10.2. Observing the network traffic from the Traffic flows view](#network-observability-trafficflow_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Use the **Traffic flows** view to monitor real-time and historical network communication between cluster components. By analyzing granular flow data collected via eBPF, you can audit network traffic, validate network policies, and export data for external reporting and analysis.

The **Traffic flows** view in the Network Observability Operator provides a granular, tabular representation of network activity across a OpenShift Container Platform cluster. By leveraging eBPF technology to collect flow data, this view allows administrators to monitor real-time and historical communication between pods, services, and nodes. This visibility is essential for auditing network traffic, validating network policies, and identifying unexpected communication patterns within the cluster infrastructure.

In the **Traffic flows** interface, you can analyze specific connection details by interacting with individual rows to retrieve detailed flow information. The view supports advanced customization through the **Display options** menu, where you can adjust row density and manage columns. By selecting and reordering specific columns, you can tailor the table to highlight the most relevant data points for your environment, such as source and destination endpoints or traffic volume.

To support external analysis and reporting, the **Traffic flows** view includes data export capabilities. You can export the entire dataset or select specific fields to generate a targeted report of network activity. This functionality ensures that network flow data is accessible for long-term auditing or for use in third-party monitoring tools, providing a flexible way to document and analyze the network health of your OpenShift Container Platform environment.

#### [10.2.1. Working with the Traffic flows view](#network-observability-working-with-trafficflow_nw-observe-network-traffic) Copy linkLink copied to clipboard!

View and analyze detailed network flow information by using the **Traffic flows** table.

As an administrator, you can navigate to **Traffic flows** table to see network flow information.

**Prerequisite**

* You have administrator access.

**Procedure**

1. Navigate to **Observe** → **Network Traffic**.
2. In the **Network Traffic** page, click the **Traffic flows** tab.
3. Click on each row to get the corresponding flow information.

#### [10.2.2. Traffic flow display settings](#network-observability-configuring-options-trafficflow_nw-observe-network-traffic) Copy linkLink copied to clipboard!

The **Traffic flows** view contains settings to customize the display density, data columns, and data export options.

##### [10.2.2.1. Display options](#display-options_nw-observe-network-traffic) Copy linkLink copied to clipboard!

The following elements are available in the **Traffic flows** view:

**Show advanced options**
:   Specifies a menu to customize and export the current view.

**Display options** drop-down
:   Specifies the row size for the data table. The default value is **Normal**.

**Manage columns**
:   Specifies a dialog to select and reorder the columns displayed in the **Traffic flows** table.

#### [10.2.3. Exporting traffic flow data](#network-observability-exporting-traffic-flow-data_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Export network flow data from the **Traffic flows** view to a CSV file for external analysis or reporting.

**Procedure**

1. Click **Export data**.
2. In the window, select the **Export all data** checkbox to export all the data, and clear the checkbox to select the required fields to be exported.
3. Click **Export**.

#### [10.2.4. Configuring IPsec with the FlowCollector custom resource](#network-observability-configuring-ipsec-with-flow-collector-resource_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Enable IPsec tracking in the `FlowCollector` resource to monitor encrypted traffic, adding an IPsec status column to the traffic flow view and generating a dedicated encryption dashboard.

In OpenShift Container Platform, IPsec is disabled by default. You can enable IPsec by following the instructions in "Configuring IPsec encryption".

**Prerequisite**

* You have enabled IPsec encryption on OpenShift Container Platform.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource for IPsec:

   **Example configuration of `FlowCollector` for IPsec**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     agent:
       type: eBPF
       ebpf:
         features:
         - "IPSec"
   ```

**Verification**

When IPsec is enabled:

* A new column named **IPsec Status** is displayed in the network observability **Traffic flows** view to show whether a flow was successfully IPsec-encrypted or if there was an error during encryption/decryption.
* A new dashboard showing the percent of encrypted traffic is generated.

#### [10.2.5. Working with conversation tracking](#network-observability-working-with-conversations_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Configure the `FlowCollector` custom resource to enable conversation tracking for grouping and analyzing related network flows in the web console.

As an administrator, you can group network flows that are part of the same conversation. A conversation is defined as a grouping of peers that are identified by their IP addresses, ports, and protocols, resulting in an unique **Conversation Id**. You can query conversation events in the web console. These events are represented in the web console as follows:

* **Conversation start**: This event happens when a connection is starting or TCP flag intercepted
* **Conversation tick**: This event happens at each specified interval defined in the `FlowCollector` `spec.processor.conversationHeartbeatInterval` parameter while the connection is active.
* **Conversation end**: This event happens when the `FlowCollector` `spec.processor.conversationEndTimeout` parameter is reached or the TCP flag is intercepted.
* **Flow**: This is the network traffic flow that occurs within the specified interval.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource so that `spec.processor.logTypes`, `conversationEndTimeout`, and `conversationHeartbeatInterval` parameters are set according to your observation needs. A sample configuration is as follows:

   **Configure `FlowCollector` for conversation tracking**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
    processor:
     logTypes: Flows
     advanced:
      conversationEndTimeout: 10s
      conversationHeartbeatInterval: 30s
   ```

   where:

   `spec.processor.logTypes`
   :   Specifies the types of events to export. When set to `Flows`, only the Flow event is exported. When set to `All`, both conversation and flow events are exported and visible in the **Network Traffic** page. To focus only on conversation events, specify `Conversations` to export **Conversation start**, **Conversation tick**, and **Conversation end** events. To export only the **Conversation end** events, specify `EndedConversations`. Storage requirements are highest for `All` and lowest for `EndedConversations`.

   `spec.processor.advanced.conversationEndTimeout`
   :   Specifies the duration at which a **Conversation end** event is triggered once the timeout is reached or a TCP flag is intercepted.

   `spec.processor.advanced.conversationHeartbeatInterval`
   :   Specifies the interval for the **Conversation tick** event while the network connection is active.

       Note

       If you update the `logType` option, the flows from the previous selection do not clear from the console plugin. For example, if you initially set `logType` to `Conversations` for a span of time until 10 AM and then move to `EndedConversations`, the console plugin shows all conversation events before 10 AM and only ended conversations after 10 AM.
5. Refresh the **Network Traffic** page on the **Traffic flows** tab. Notice there are two new columns, **Event/Type** and **Conversation Id**. All the **Event/Type** fields are `Flow` when **Flow** is the selected query option.
6. Select **Query Options** and choose the **Log Type**, **Conversation**. Now the **Event/Type** shows all of the desired conversation events.
7. Next you can filter on a specific conversation ID or switch between the **Conversation** and **Flow** log type options from the side panel.

#### [10.2.6. Working with the eBPF Manager Operator](#network-observability-ebpf-manager-operator_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Integrate the eBPF Manager Operator with Network Observability to manage eBPF programs and reduce the need for privileged agent permissions.

The eBPF Manager Operator reduces the attack surface and ensures compliance, security, and conflict prevention by managing all eBPF programs. Network observability can use the eBPF Manager Operator to load hooks. As a result, you no longer need to provide the eBPF Agent with privileged mode or additional Linux capabilities such as `CAP_BPF` and `CAP_PERFMON`. The eBPF Manager Operator with network observability is only supported on 64-bit AMD architecture.

Important

eBPF Manager Operator with network observability is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Operator Hub**.
2. Install **eBPF Manager**.
3. Check **Workloads** → **Pods** in the `bpfman` namespace to make sure they are all up and running.
4. Configure the `FlowCollector` custom resource to use the eBPF Manager Operator:

   **Example `FlowCollector` configuration**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     agent:
       ebpf:
         features:
           - EbpfManager
   ```

**Verification**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Click **eBPF Manager Operator** → **All instances** tab.

   For each node, verify that a `BpfApplication` named `netobserv` and a pair of `BpfProgram` objects, one for Traffic Control (TCx) ingress and another for TCx egress, exist. If you enable other eBPF Agent features, you might have more objects.

#### [10.2.7. Using the histogram](#network-observability-histogram-trafficflow_nw-observe-network-traffic) Copy linkLink copied to clipboard!

The histogram provides a visualization of network flow logs that you can use to analyze traffic volume trends and filter flow data by specific time intervals.

You can click **Show histogram** to display a toolbar view for visualizing the history of flows as a bar chart. The histogram shows the number of logs over time. You can select a part of the histogram to filter the network flow data in the table that follows the toolbar.

#### [10.2.8. Working with availability zones](#network-observability-zones_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Configure the `FlowCollector` custom resource to collect availability zone data, enabling the visualization and analysis of network traffic across different cluster zones in the web console.

You can configure the `FlowCollector` to collect information about the cluster availability zones. This allows you to enrich network flow data with the [`topology.kubernetes.io/zone`](https://kubernetes.io/docs/reference/labels-annotations-taints/#topologykubernetesiozone) label value applied to the nodes.

**Procedure**

1. In the web console, go to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource so that the `spec.processor.addZone` parameter is set to `true`. A sample configuration is as follows:

   **Configure `FlowCollector` for availability zones collection**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
   # ...
    processor:
      addZone: true
   # ...
   ```

**Verification**

When you refresh the **Network Traffic** page, the **Overview**, **Traffic Flow**, and **Topology** views display new information about availability zones:

1. In the **Overview** tab, you can see **Zones** as an available **Scope**.
2. In **Network Traffic** → **Traffic flows**, **Zones** are viewable under the SrcK8S\_Zone and DstK8S\_Zone fields.
3. In the **Topology** view, you can set **Zones** as **Scope** or **Group**.

#### [10.2.9. Endpoint translation (xlat)](#network-observability-packet-translation-overview_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Endpoint translation (xlat) uses eBPF to enrich network flow logs with translated pod-level metadata, providing visibility into the specific backend pods serving traffic behind services or load balancers.

You can gain visibility into the endpoints serving traffic in a consolidated view using network observability and extended Berkeley Packet Filter (eBPF). Typically, when traffic flows through a service, egressIP, or load balancer, the traffic flow information is abstracted as it is routed to one of the available pods. If you try to get information about the traffic, you can only view service related info, such as service IP and port, and not information about the specific pod that is serving the request. Often the information for both the service traffic and the virtual service endpoint is captured as two separate flows, which complicates troubleshooting.

To solve this, endpoint xlat can help in the following ways:

* Capture the network flows at the kernel level, which has a minimal impact on performance.
* Enrich the network flows with translated endpoint information, showing not only the service but also the specific backend pod, so you can see which pod served a request.

As network packets are processed, the eBPF hook enriches flow logs with metadata about the translated endpoint that includes the following pieces of information that you can view in the **Network Traffic** page in a single row:

* Source Pod IP
* Source Port
* Destination Pod IP
* Destination Port
* Conntrack Zone ID

#### [10.2.10. Working with endpoint translation (xlat)](#network-observability-packet-translation_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Enable endpoint translation (xlat) in the `FlowCollector` resource to enrich network flows with translated packet information. You can use this information to identify the specific pods and objects serving service traffic through dedicated xlat columns.

You can use network observability and eBPF to enrich network flows from a Kubernetes service with translated endpoint information, gaining insight into the endpoints serving traffic.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster**, and then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource for `PacketTranslation`, for example:

   **Example `FlowCollector` configuration**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     agent:
       type: eBPF
       ebpf:
         features:
          - PacketTranslation
   ```

   * You can start enriching network flows with translated packet information by listing the `PacketTranslation` parameter in the `spec.agent.ebpf.features` specification list.
5. Refresh the **Network Traffic** page to filter for information about translated packets:

   1. Filter the network flow data based on **Destination kind: Service**.
   2. You can see the **xlat** column, which distinguishes where translated information is displayed, and the following default columns:

      * **Xlat Zone ID**
      * **Xlat Src Kubernetes Object**
      * **Xlat Dst Kubernetes Object**
   3. You can manage the display of additional **xlat** columns in **Manage columns**.

### [10.3. Observing the network traffic from the Topology view](#network-observability-topology_nw-observe-network-traffic) Copy linkLink copied to clipboard!

The **Topology** view in the **Network Traffic** page provides a graphical representation of network flows and traffic volume across your OpenShift Container Platform cluster. As an administrator, you can use this view to monitor application traffic data and visualize the relationships between various network components.

The visualization represents network entities as nodes and traffic flows as edges. By selecting individual components within the graph, you can access a side panel containing specific metrics and health details for that resource. This interactive approach allows for rapid identification of traffic patterns and connectivity issues within the cluster.

To manage complex environments, the **Topology** view includes advanced configuration options that allow you to customize the layout and data density. You can adjust the **Scope** of the view, apply **Groups** to represent resource ownership, and choose different **Layout** algorithms to optimize the graphical display. Additionally, you can enable **Edge labels** to show real-time measurements, such as the average byte rate, directly on the flow lines.

For reporting or external analysis, the **Topology** view provides an export feature. You can download the current graphical representation as a PNG image or generate a direct link to the specific view configuration to share with other administrators. These tools ensure that network insights are both accessible and easily documented.

#### [10.3.1. Working with the Topology view](#network-observability-working-with-topology_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Access the **Topology** view to visually inspect cluster network relationships and select individual components to view detailed traffic metrics and metadata.

As an administrator, you can navigate to the **Topology** view to see the details and metrics of the component.

**Prerequisites**

* You have administrator access.

**Procedure**

1. Navigate to **Observe** → **Network Traffic**.
2. In the **Network Traffic** page, click the **Topology** tab.
3. Click each component in the **Topology** tab to view its details and metrics.

#### [10.3.2. Configuring the advanced options for the Topology view](#network-observability-configuring-options-topology_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Review the available advanced options in the **Topology** view to customize display settings, configure component grouping and layouts, and export the network graph as an image.

You can customize and export the view by using **Show advanced options**. The advanced options view has the following features:

* **Find in view**: To search the required components in the view.
* **Display options**: To configure the following options:

  + **Edge labels**: To show the specified measurements as edge labels. The default is to show the **Average rate** in **Bytes**.
  + **Scope**: To select the scope of components between which the network traffic flows. The default value is **Namespace**.
  + **Groups**: To enhance the understanding of ownership by grouping the components. The default value is **None**.
  + **Layout**: To select the layout of the graphical representation. The default value is **ColaNoForce**.
  + **Show**: To select the details that need to be displayed. All the options are checked by default. The options available are: **Edges**, **Edges label**, and **Badges**.
  + **Truncate labels**: To select the required width of the label from the drop-down list. The default value is **M**.
  + **Collapse groups**: To expand or collapse the groups. The groups are expanded by default. This option is disabled if **Groups** has the value of **None**.

##### [10.3.2.1. Exporting the topology view](#network-observability-cao-export-topology_nw-observe-network-traffic) Copy linkLink copied to clipboard!

To export the view, click **Export topology view**. The view is downloaded in PNG format.

### [10.4. Filtering the network traffic](#network-observability-quickfilter_nw-observe-network-traffic) Copy linkLink copied to clipboard!

Review the available query options and filtering parameters in the **Network Traffic** view to optimize data searches, analyze specific log types, and manage directional traffic visibility.

By default, the **Network Traffic** page displays the traffic flow data in the cluster based on the default filters configured in the `FlowCollector` instance. You can use the filter options to observe the required data by changing the preset filter.

Alternatively, you can access the traffic flow data in the **Network Traffic** tab of the **Namespaces**, **Services**, **Routes**, **Nodes**, and **Workloads** pages which provide the filtered data of the corresponding aggregations.

Query Options
:   You can use **Query Options** to optimize the search results, as listed below:

    * **Log Type**: The available options **Conversation** and **Flows** provide the ability to query flows by log type, such as flow log, new conversation, completed conversation, and a heartbeat, which is a periodic record with updates for long conversations. A conversation is an aggregation of flows between the same peers.
    * **Match filters**: You can determine the relation between different filter parameters selected in the advanced filter. The available options are **Match all** and **Match any**. **Match all** provides results that match all the values, and **Match any** provides results that match any of the values entered. The default value is **Match all**.
    * **Datasource**: You can choose the datasource to use for queries: **Loki**, **Prometheus**, or **Auto**. Notable performance improvements can be realized when using Prometheus as a datasource rather than Loki, but Prometheus supports a limited set of filters and aggregations. The default datasource is **Auto**, which uses Prometheus on supported queries or uses Loki if the query does not support Prometheus.
    * **Drops filter**: You can view different levels of dropped packets with the following query options:

      + **Fully dropped** shows flow records with fully dropped packets.
      + **Containing drops** shows flow records that contain drops but can be sent.
      + **Without drops** shows records that contain sent packets.
      + **All** shows all the aforementioned records.
    * **Limit**: The data limit for internal backend queries. Depending upon the matching and the filter settings, the number of traffic flow data is displayed within the specified limit.

Quick filters
:   The default values in **Quick filters** drop-down menu are defined in the `FlowCollector` configuration. You can modify the options from console.

Advanced filters
:   You can set the advanced filters, **Common**, **Source**, or **Destination**, by selecting the parameter to be filtered from the dropdown list. The flow data is filtered based on the selection. To enable or disable the applied filter, you can click on the applied filter listed below the filter options.

You can toggle between
**One way** and

**Back and forth** filtering. The
**One way** filter shows only **Source** and **Destination** traffic according to your filter selections. You can use **Swap** to change the directional view of the **Source** and **Destination** traffic. The

**Back and forth** filter includes return traffic with the **Source** and **Destination** filters. The directional flow of network traffic is shown in the **Direction** column in the Traffic flows table as `` Ingress`or `Egress `` for inter-node traffic and `Inner`for traffic inside a single node.

You can click **Reset defaults** to remove the existing filters, and apply the filter defined in `FlowCollector` configuration.

Note

To understand the rules of specifying the text value, click **Learn More**.

## [Chapter 11. Network observability health rules](#network-observability-health-rules) Copy linkLink copied to clipboard!

The Network Observability Operator provides alerts by using built-in metrics and the OpenShift Container Platform monitoring stack to report cluster network health.

Important

Network observability health alerts require OpenShift Container Platform 4.16 or later.

### [11.1. Identifying network issues with automated health rules](#network-observability-health-rules-and-performance_network-observability-health-rules) Copy linkLink copied to clipboard!

Network observability identifies network issues by using automated health rules to monitor metrics. These rules trigger alerts when anomalies occur, which assists in maintaining connectivity and responding to network degradation.

The Network Observability Operator manages a system of Prometheus-based rules that detect network problems, and converts these rules into `PrometheusRule` resources. It supports the following rule types:

Alerting rules
:   Trigger notifications through the Prometheus `Alertmanager` when network anomalies or infrastructure failures are detected.

Recording rules
:   Pre-compute complex Prometheus Query Language (PromQL) expressions into new time series to improve dashboard performance.

#### [11.1.1. Importance of network health monitoring](#importance-of-network-health-monitoring_network-observability-health-rules) Copy linkLink copied to clipboard!

Maintaining reliable and secure network connectivity is critical for cluster administrators and security teams. Unresolved network issues can result in the following consequences:

* Application downtime caused by packet drops or DNS failures.
* Security risks from undetected network policy violations.
* Performance degradation caused by latency spikes or bandwidth saturation.
* Compliance issues from unmonitored network traffic.

Early detection of these issues allows for resolution before service level objectives (SLOs) are affected.

#### [11.1.2. Automated health monitoring](#detection-of-network-issues_network-observability-health-rules) Copy linkLink copied to clipboard!

The Network Observability Operator provides automated health monitoring through the following features:

* Pre-configured health rules: Detect common network problems by using default thresholds.
* Automated alerting: Integrates with the OpenShift Container Platform monitoring stack.
* Health dashboards: Displays health status for clusters, nodes, namespaces, and workloads.
* Custom rules: Supports the creation of organization-specific monitoring rules.

Health rules monitor network flow metrics and trigger alerts when defined thresholds are exceeded. For example, the `PacketDropsByKernel` rule reports an alert when kernel packet drop rates exceed defined levels.

#### [11.1.3. Network health monitoring workflow](#network-health-monitoring-workflow_network-observability-health-rules) Copy linkLink copied to clipboard!

Monitoring network health involves the following phases:

* Configuring the Network Observability Operator to collect required network health data for monitoring, such as packet drops or DNS tracking.
* Reviewing and customizing default health rules and thresholds in the `FlowCollector` custom resource.
* Monitoring alerts in the OpenShift Container Platform web console in the **Observe** → **Alerting** and **Observe** → **Network Health** views.
* Creating custom health rules for specific requirements.
* Configuring recording rules to optimize performance for large-scale deployments.

The `PrometheusRule` resource in the `netobserv` namespace can be viewed by running the following command:

```
$ oc get prometheusrules -n netobserv -o yaml
```

#### [11.1.4. Detecting network issues with automated health rules](#network-observability-health-rules-monitoring-and-alerting_network-observability-health-rules) Copy linkLink copied to clipboard!

The Network Observability Operator includes a rule-based system to detect network anomalies and infrastructure failures. By converting configurations into alerting rules, the Operator provides automated monitoring and troubleshooting through the OpenShift Container Platform web console.

##### [11.1.4.1. Monitoring outcomes](#network-observability-health-outcomes_network-observability-health-rules) Copy linkLink copied to clipboard!

The Network Observability Operator displays network status in the following views:

**Alerting** UI
:   Specific alerts appear in **Observe** → **Alerting**. Notifications are managed through the Prometheus `Alertmanager`.

**Network Health** dashboard
:   A specialized dashboard in **Observe** → **Network Health** provides a summary of cluster network status.

The **Network Health** dashboard categorizes violations into tabs to isolate the scope of an issue:

* **Global**: Aggregate health of the cluster.
* **Nodes**: Violations specific to infrastructure nodes.
* **Namespaces**: Violations specific to individual namespaces.
* **Workloads**: Violations specific to resources, such as `Deployments` or `DaemonSets`.

##### [11.1.4.2. Predefined health rules](#network-observability-default-rules_network-observability-health-rules) Copy linkLink copied to clipboard!

The Network Observability Operator provides default rules for common networking scenarios. These rules are active only if the corresponding feature is enabled in the `FlowCollector` custom resource (CR).

The following list contains a subset of available default rules:

`PacketDropsByDevice`
:   Reports a high percentage of packet drops from network devices. This rule is based on node-exporter metrics and does not require the `PacketDrop` agent feature.

`PacketDropsByKernel`
:   Reports a high percentage of packet drops by the kernel. This rule requires the `PacketDrop` agent feature.

`IPsecErrors`
:   Reports IPsec encryption errors. This rule requires the `IPSec` agent feature.

`NetpolDenied`
:   Reports traffic denied by network policies. This rule requires the `NetworkEvents` agent feature.

`LatencyHighTrend`
:   Reports a significant increase in TCP latency. This rule requires the `FlowRTT` agent feature.

`DNSErrors`
:   Reports DNS errors. This rule requires the `DNSTracking` agent feature.

The following operational alerts apply to the Network Observability Operator:

`NetObservNoFlows`
:   Reports when the pipeline is active but no flows are observed.

`NetObservLokiError`
:   Reports when flows are dropped because of Loki errors.

For a complete list of rules and runbooks, see the [Network Observability Operator runbooks](https://github.com/openshift/runbooks/tree/master/alerts/network-observability-operator).

##### [11.1.4.3. Enabling features for health monitoring](#network-observability-enabling-features-for-health-monitoring_network-observability-health-rules) Copy linkLink copied to clipboard!

The Network Observability Operator creates rules based on the features enabled in the `FlowCollector` CR.

For example, packet drop rules are created only if the `PacketDrop` agent feature is enabled. Rules depend on metrics; if the required metrics are unavailable, configuration warnings might appear. Configure metrics in the `spec.processor.metrics.includeList` field of the `FlowCollector` resource.

### [11.2. Health rule threshold and grouping customization](#network-observability-health-rule-customization_network-observability-health-rules) Copy linkLink copied to clipboard!

Health rules in the Network Observability Operator are defined by using rule templates and variants in the `spec.processor.metrics.healthRules` field of the `FlowCollector` custom resource (CR). Customizing these templates allows for flexible, fine-grained alerting tailored to specific environment needs.

For each template, a list of variants can be defined, each with distinct thresholds and grouping configurations.

The following example shows a `FlowCollector` configuration with custom health rules:

```
apiVersion: flows.netobserv.io/v1beta1
kind: FlowCollector
metadata:
  name: flow-collector
spec:
  processor:
    metrics:
      healthRules:
      - template: PacketDropsByKernel
        mode: Alert # or Recording
        variants:
        # Triggered when aggregate cluster traffic reaches 10% drops
        - thresholds:
            critical: "10"
        # Triggered per-node with increasing severity levels
        - thresholds:
            critical: "15"
            warning: "10"
            info: "5"
          groupBy: Node
```

`spec.processor.metrics.healthRules.template`
:   Specifies the name of the predefined rule template.

`spec.processor.metrics.healthRules.mode`
:   Specifies whether the rule functions as an `Alert` or a `Recording` rule.

`spec.processor.metrics.healthRules.variants.thresholds`
:   Specifies the numerical values that trigger the rule. Multiple severity levels, such as `critical`, `warning`, or `info`, can be defined within a single variant.

`spec.processor.metrics.healthRules.variants.groupBy`
:   Specifies the dimension used to aggregate the metric, such as `Node` or `Namespace`.

Note

Customizing a rule replaces the default configuration for that template. To retain default configurations, the default settings must be manually included in the custom resource.

#### [11.2.1. Health rule query and metadata reference](#network-observability-health-rules-promql-expressions-metadata_network-observability-health-rules) Copy linkLink copied to clipboard!

The `FlowCollector` health rule API maps to the Prometheus Operator to generate `PrometheusRule` objects. Use these base Prometheus Query Language (PromQL) patterns and metadata configurations to create custom health rules for network observability.

The `PrometheusRule` resource in the `netobserv` namespace can be viewed by running the following command:

```
$ oc get prometheusrules -n netobserv -o yaml
```

##### [11.2.1.1. Customizing alert logic with PromQL: Incoming traffic surge](#example-query-surge-incoming-traffic_network-observability-health-rules) Copy linkLink copied to clipboard!

The following PromQL query calculates the byte rate from the `openshift-ingress` namespace to any workload namespace over a 30-minute interval:

```
sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace)
```

Queries can be customized to filter low-bandwidth data, compare time periods, and establish thresholds.

Data filtering
:   Appending `> 1000` to the query removes rates lower than `1 KB/s` to filter low-bandwidth traffic.

    `(sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace) > 1000)`

    Note

    The byte rate is relative to the sampling interval in the `FlowCollector` CR. Normalizing byte rates with the `netobserv_agent_sampling_rate` metric decouples the PromQL expression from the sampling configuration.

Time comparison
:   The `offset` modifier compares data across different time periods. For example, `offset 1d` retrieves data from the previous day.

    `sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace))`

Threshold application
:   A final threshold filters increases below a specific percentage. For example, `> 100` removes increases lower than 100%.

The following example shows a complete PromQL expression for a `PrometheusRule`:

```
expr: |-
  (100 *
    (
      (sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace) > 1000)
      - sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace)
    )
    / sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace))
  > 100
```

##### [11.2.1.2. Alert metadata fields](#alert-metadata-fields_network-observability-health-rules) Copy linkLink copied to clipboard!

Rule definitions require specific metadata for the Prometheus `Alertmanager` service and the **Network Health** dashboard. The following example shows an `AlertingRule` resource with configured metadata:

```
apiVersion: monitoring.openshift.io/v1
kind: AlertingRule
metadata:
  name: netobserv-alerts
  namespace: openshift-monitoring
spec:
  groups:
  - name: NetObservAlerts
    rules:
    - alert: NetObservIncomingBandwidth
      annotations:
        netobserv_io_network_health: '{"namespaceLabels":["DstK8S_Namespace"],"threshold":"100","unit":"%","upperBound":"500"}'
        message: |-
          Surge of incoming traffic detected: current traffic to {{ $labels.DstK8S_Namespace }} increased by more than 100% since yesterday.
        summary: "Surge in incoming traffic"
      expr: |-
        # ... (PromQL expression)
      for: 1m
      labels:
        app: netobserv
        netobserv: "true"
        severity: warning
```

`spec.groups.rules.alert.labels.netobserv`
:   Specifies that the **Network Health** dashboard must detect the alert when set to `true`.

`spec.groups.rules.alert.labels.severity`
:   Specifies the alert severity. Valid values are `critical`, `warning`, or `info`.

##### [11.2.1.3. netobserv\_io\_network\_health annotation fields](#netobserv-io-network-health-annotation_network-observability-health-rules) Copy linkLink copied to clipboard!

The optional `netobserv_io_network_health` annotation is a JSON string that controls how the alert renders on the **Network Health** page.

Expand

Table 11.1. Fields for the netobserv\_io\_network\_health annotation

| Field | Type | Description |
| --- | --- | --- |
| `namespaceLabels` | List of strings | One or more labels containing namespaces. Alerts appear under the **Namespaces** tab. |
| `nodeLabels` | List of strings | One or more labels containing node names. Alerts appear under the **Nodes** tab. |
| `workloadLabels` | List of strings | One or more labels containing owner or workload names. Alerts appear under the **Owners** tab when `kindLabels` is also provided. |
| `threshold` | String | The alert threshold. This value should match the threshold in the PromQL expression. |
| `unit` | String | The data unit for display purposes. |
| `upperBound` | String | An upper bound value used to calculate scores on a closed scale. Metric values exceeding this bound are clamped. |

Show more

Note

The `namespaceLabels` and `nodeLabels` fields are mutually exclusive. If neither is provided, the alert appears under the **Global** tab.

#### [11.2.2. Configuring custom health rules](#network-observability-configuring-custom-health-rules_network-observability-health-rules) Copy linkLink copied to clipboard!

Create custom health rules by using Prometheus Query Language (PromQL) to define an `AlertingRule` resource. These rules trigger alerts based on specific network metrics, such as traffic surges.

**Prerequisites**

* Access to the cluster with `cluster-admin` privileges.
* The Network Observability Operator is installed.
* OpenShift Container Platform 4.16 or later is installed.
* Familiarity with PromQL.

Important

Custom `PrometheusRule` resources are not owned by the `FlowCollector` resource. Custom rules created in the `netobserv` namespace might be deleted if the Network Observability Operator is uninstalled. To prevent data loss, create custom rules in a different namespace, such as `openshift-monitoring`, and maintain a backup in version control.

**Procedure**

1. Define an `AlertingRule` resource in a YAML file, for example, `custom-alert.yaml`.
2. Apply the custom alert rule by running the following command:

   ```
   $ oc apply -f custom-alert.yaml
   ```

**Verification**

1. Confirm the `PrometheusRule` resource was created in the target namespace by running the following command:

   ```
   $ oc get prometheusrules -n <namespace> -o yaml
   ```
2. Confirm the rule is active in the OpenShift Container Platform web console:

   1. Navigate to **Observe** → **Alerting** to see the firing status.
   2. Navigate to **Observe** → **Network Health** to view the dashboard integration.

### [11.3. Performance optimization with recording rules](#network-observability-recording-rules-performance-optimization_network-observability-health-rules) Copy linkLink copied to clipboard!

In large-scale clusters, recording rules optimize how Prometheus handles network data. Recording rules improve dashboard responsiveness and reduce the computational overhead of complex queries.

#### [11.3.1. Optimization benefits](#network-observability-recording-rules-benefits_network-observability-health-rules) Copy linkLink copied to clipboard!

Recording rules pre-compute complex Prometheus Query Language (PromQL) expressions and save the results as new time series. Unlike alerting rules, recording rules do not monitor thresholds.

Using recording rules provides the following advantages:

Improved performance
:   Pre-computing Prometheus queries allows dashboards to load faster by avoiding on-demand calculations for long-term trends.

Resource efficiency
:   Calculating data at fixed intervals reduces CPU load on the Prometheus server compared to recalculating data on every dashboard refresh.

Simplified queries
:   Using short metric names, such as `cluster:network_traffic:rate_5m`, simplifies complex aggregate calculations in custom dashboards.

#### [11.3.2. Comparison of rule modes](#network-observability-alert-vs-recording-comparison_network-observability-health-rules) Copy linkLink copied to clipboard!

The following table compares rule modes based on the expected outcome:

Expand

| Feature | Alerting rules | Recording rules |
| --- | --- | --- |
| Primary goal | Issue notification. | Persistent metric history. |
| Data output | Alerting state. | New time series metric. |
| UI visibility | **Alerting** and **Network Health** views. | **Metrics Explorer** and **Network Health** views. |
| Notifications | Triggers `Alertmanager` notifications. | Does not trigger notifications. |

Show more

#### [11.3.3. Integrating recording rules with the health dashboard](#network-observability-integrating-recording-rules-with-health-dashboard_network-observability-health-rules) Copy linkLink copied to clipboard!

Custom recording rules that contribute to the **Network Health** dashboard must meet specific metadata requirements.

Label requirements
:   Include the `netobserv: "true"` label in the `labels` field of the rule and the `PrometheusRule` metadata. The Network Observability Operator identifies `PrometheusRule` resources cluster-wide by using this label.

Annotation requirements
:   Include the `netobserv.io/network-health` annotation in the `PrometheusRule` metadata. This annotation is required for recording rules to appear in the **Network Health** dashboard. The value is a JSON object where keys are the metric names (the `record` field of each rule). Each value consists of the following fields:

    * `summary`: An optional short title. This field supports Prometheus template syntax, such as `{{ $labels.namespace }}`.
    * `description`: An optional description. This field supports Prometheus template syntax.
    * `netobserv_io_network_health`: A required JSON string. For recording rules, use the `recordingThresholds` field instead of `threshold`. This field determines the health score and UI coloring, such as `{"info":"10","warning":"25","critical":"50"}`.

#### [11.3.4. Optimizing dashboard metrics with recording rules](#network-observability-configuring-custom-recording-rules_network-observability-health-rules) Copy linkLink copied to clipboard!

Create custom recording rules to pre-compute metrics for the **Network Health** dashboard. Recording rules require specific annotations and labels to integrate with the Network Observability Operator.

**Prerequisites**

* Access to the cluster with `cluster-admin` privileges.
* The Network Observability Operator is installed.
* OpenShift Container Platform 4.16 or later is installed.
* Familiarity with PromQL.

Important

Custom `PrometheusRule` resources are not owned by the `FlowCollector` resource. Custom rules created in the `netobserv` namespace might be deleted if the Network Observability Operator is uninstalled. To prevent data loss, create custom rules in a different namespace, such as `openshift-monitoring`, and maintain a backup in version control.

**Procedure**

1. Define a `PrometheusRule` resource in a YAML file, such as `custom-recording-rule.yaml`, ensuring the `netobserv: "true"` label and `netobserv.io/network-health` annotation are included:

   ```
   apiVersion: monitoring.coreos.com/v1
   kind: PrometheusRule
   metadata:
     name: my-recording-rules
     namespace: openshift-monitoring
     labels:
       netobserv: "true"
     annotations:
       netobserv.io/network-health: |
         {
           "my_metric_per_namespace": {
             "summary": "Custom metric is {{ $value }} in the namespace {{ $labels.namespace }}",
             "description": "Custom metric is {{ $value }} in the namespace {{ $labels.namespace }}",
             "netobserv_io_network_health": "{\"unit\":\"%\",\"upperBound\":\"100\",\"namespaceLabels\":[\"namespace\"],\"recordingThresholds\":{\"info\":\"10\",\"warning\":\"25\",\"critical\":\"50\"}}"
           }
         }
   spec:
     groups:
       - name: MyRecordingRules
         interval: 30s
         rules:
           - record: my_metric_per_namespace
             expr: (count by (namespace) (kube_pod_info) * 0 + 20)
             labels:
               netobserv: "true"
   ```
2. Apply the custom recording rule by running the following command:

   ```
   $ oc apply -f custom-recording-rule.yaml
   ```

**Verification**

1. Confirm the `PrometheusRule` resource exists by running the following command:

   ```
   $ oc get prometheusrules my-recording-rules -n openshift-monitoring -o yaml
   ```
2. Confirm the recording rule appears in the OpenShift Container Platform web console by navigating to **Observe** → **Network Health**.

### [11.4. Disabling default rules](#network-observability-disable-predefined-rules_network-observability-health-rules) Copy linkLink copied to clipboard!

Rule templates can be disabled in the `spec.processor.metrics.disableAlerts` field of the `FlowCollector` custom resource (CR). This setting accepts a list of rule template names. For a list of alert template names, see "List of default rules".

If a rule template is included in the `disableAlerts` list, it is not created, even if a custom override exists in the `spec.processor.metrics.healthRules` field. The `disableAlerts` configuration takes precedence over all other health rule settings.

For a list of alert template names, see "List of default rules".

## [Chapter 12. Monitoring Transport Layer Security traffic](#network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

Monitor TLS traffic to identify insecure protocols, detect security risks, and maintain compliance without decrypting traffic.

### [12.1. Transport Layer Security traffic monitoring](#network-observability-tls-monitoring-overview_network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

Transport Layer Security (TLS) traffic monitoring identifies security risks and maintains compliance by analyzing encrypted traffic metadata without decryption.

As a network administrator or security practitioner, you must verify that encrypted traffic uses secure protocols and cipher suites. Monitoring TLS usage identifies security risks, such as workloads that use deprecated TLS versions, and helps maintain compliance with cluster security policies.

#### [12.1.1. Security improvements through metadata analysis](#tls-monitoring-security-benefits_network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

The Network Observability Operator captures TLS metadata from handshake messages without decrypting traffic, providing visibility into encryption protocols while maintaining data privacy. This approach enables the following improvements:

Security risk detection
:   Identifies workloads using deprecated TLS versions (1.0, 1.1) or weak cipher suites by capturing TLS version, cipher suite, and group information. You can configure Prometheus alerts to automatically report deprecated TLS configurations.

Compliance auditing
:   Audits TLS configurations to meet regulatory requirements through metric aggregation in dashboard charts and overview panels. You can filter flows by TLS fields to isolate specific protocol versions or cipher suites for compliance reporting.

Security posture assessment
:   Visualizes encrypted network traffic with lock icons in the topology view and identifies unencrypted communications across your cluster. You can analyze TLS usage patterns to evaluate your overall security posture.

Remediation prioritization
:   Targets workloads using deprecated protocols for updates by filtering and analyzing TLS fields to isolate problematic connections requiring immediate attention.

#### [12.1.2. TLS traffic monitoring workflow phases](#monitoring-tls-traffic-workflow_network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

To monitor TLS traffic effectively, complete the following phases:

* Enable the TLS tracking feature in the eBPF agent configuration.
* Analyze TLS traffic details in the **Network Traffic** view.
* Visualize secure connections in the **Topology** view.

### [12.2. Enable Transport Layer Security tracking](#network-observability-enable-tls-tracking_network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

Enable Transport Layer Security (TLS) tracking to monitor encryption protocols and identify security risks in the cluster.

Note

TLS fields only appear in flows for connections that perform a TLS handshake after the feature is enabled.

**Prerequisites**

* The Network Observability Operator is installed.
* The `FlowCollector` custom resource (CR) is configured with `spec.agent.type: eBPF`.
* Access to the cluster with `cluster-admin` privileges.

**Procedure**

1. Edit the `FlowCollector` CR by running the following command:

   ```
   $ oc edit flowcollector cluster
   ```
2. Add `TLSTracking` to the `spec.agent.ebpf.features` list:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     agent:
       type: eBPF
       ebpf:
         features:
         - TLSTracking
   # ...
   ```

   where:

   `spec.agent.ebpf.features`
   :   Specifies the list of eBPF agent features to enable. Add `TLSTracking` to this array to enable TLS metadata capture from handshake messages.
3. Save and exit your editor.

**Verification**

1. Confirm that the eBPF agent pods have restarted by running the following command:

   ```
   $ oc get pods -n netobserv-privileged
   ```

   **Example output**

   ```
   NAME                                    READY   STATUS    RESTARTS   AGE
   netobserv-ebpf-agent-abc12              1/1     Running   0          2m
   ```
2. Verify the TLS tracking feature is active by running the following command:

   ```
   $ oc logs -n netobserv-privileged ds/netobserv-ebpf-agent | grep "EnableTLSTracking"
   ```

   **Example output**

   ```
   EnableTLSTracking:true
   ```

   The output confirms that the TLS tracking feature has been initialized in the eBPF agent.

### [12.3. Analyze Transport Layer Security traffic data](#network-observability-analyze-tls-traffic_network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

View and filter Transport Layer Security (TLS) metadata to identify deprecated configurations and verify encryption compliance in the cluster.

**Prerequisites**

* The Network Observability Operator is installed.
* TLS tracking is enabled in the `FlowCollector` custom resource (CR).
* Access to the OpenShift Container Platform web console.

**Procedure**

1. Navigate to **Observe** → **Network Traffic** in the OpenShift Container Platform web console and click the **Traffic flows** tab.

   Note

   The **TLS Version** column is enabled by default. If the default TLS version column is not visible after enabling TLS tracking, click **Restore default columns** in **Manage columns** to refresh the table.
2. Add TLS-specific columns to the traffic table:

   1. Click **Manage columns**.
   2. Select the **TLS Cipher Suite**, **TLS Group**, and **TLS Types** checkboxes.
   3. Click **Save**.
3. Filter traffic by message type to view complete TLS metadata:

   1. In the filter bar, select **TLS Types** and choose **ServerHello** from the dropdown menu.

      `ServerHello` messages contain negotiated TLS metadata such as cipher suite and cryptographic group information.
4. Filter traffic by TLS version to identify deprecated configurations:

   1. In the filter bar, select **TLS Version**.
   2. Select the versions you want to review:

      * **1.0**: Deprecated
      * **1.1**: Deprecated
      * **1.2**: Legacy
      * **1.3**: Current standard

        To identify all deprecated connections, filter for TLS versions 1.0 and 1.1.
5. Analyze TLS metrics in the overview panel:

   1. Click the **Overview** tab.
   2. Review the default TLS panels, which include **TLS usage (network flows per second)** and **TLS per version (network flows per second)**.
   3. Optional: To view additional TLS metrics, click **Manage panels** to select and display additional panels, such as **TLS per group (network flows per second)** or **TLS per cipher suite (network flows per second)**.
6. Identify secure connections in the **Topology** view:

   1. Click the **Topology** tab.

      Connections secured with TLS are marked with a lock icon. The color of the lock icon indicates the security level:

      * **Red**: Deprecated TLS versions (1.0 or 1.1)
      * **Yellow**: Legacy configurations (TLS 1.2)
      * **Green**: Secure connections (TLS 1.3)
      * **Blue**: Post-Quantum Cryptography (PQC) compliant

        Select a connection node to view its specific TLS version and cipher suite details.
7. View TLS metrics in the Network Observability dashboard:

   1. Navigate to **Observe** → **Dashboards**.
   2. Search for **NetObserv** and review the available metrics:

      * **TLS Traffic**: Displays overall TLS traffic metrics.
      * **Flows rate per TLS version**: Displays traffic trends by TLS version over time.
      * **Flows rate per TLS group**: Displays traffic by TLS group over time.

### [12.4. Transport Layer Security tracking fields reference](#tls-tracking-fields_network-observability-monitoring-tls-traffic) Copy linkLink copied to clipboard!

Transport Layer Security (TLS) metadata fields track and define encryption protocols, protocol versions, and cipher suite data to help you analyze secure network flows.

Expand

Table 12.1. TLS tracking fields

| Field | Description | Possible values | Availability |
| --- | --- | --- | --- |
| **TLS Version** | Negotiated TLS protocol version. | * `1.0`: Deprecated * `1.1`: Deprecated * `1.2`: Secure * `1.3`: Current standard | `ClientHello`, `ServerHello`  `ClientHello` displays the version requested by the client. `ServerHello` displays the negotiated version selected by the server. |
| **TLS Cipher Suite** | Cryptographic algorithm suite negotiated between the client and server. | Examples:  * `TLS_AES_256_GCM_SHA384` * `TLS_CHACHA20_POLY1305_SHA256` | `ServerHello` only  Displays as `n/a` in `ClientHello` messages. |
| **TLS Group** | Elliptic curve used for key exchange. | Examples:  * `X25519`: Recommended for TLS 1.3 * `secp256r1` (P-256) | `ServerHello` (TLS 1.3 only)  Displays as `n/a` in `ClientHello` messages and TLS 1.2 connections. |
| **TLS Types** | Type of TLS handshake message captured. | * `ClientHello`: Initial client request * `ServerHello`: Server response | All TLS flows |

Show more

## [Chapter 13. Using metrics with dashboards and alerts](#metrics-dashboards-alerts) Copy linkLink copied to clipboard!

The Network Observability Operator uses the `flowlogs-pipeline` component to generate metrics from flow logs. Use these metrics to set custom alerts and view dashboards for network activity analysis.

### [13.1. Viewing network observability metrics dashboards](#network-observability-viewing-dashboards_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

View network observability metrics dashboards using the **Overview** tab in the OpenShift Container Platform console to monitor overall traffic flow and system health, with options to filter metrics by node, namespace, owner, pod, and service.

**Procedure**

1. In the web console **Observe** → **Dashboards**, select the **Netobserv** dashboard.
2. View network traffic metrics in the following categories, with each having the subset per node, namespace, source, and destination:

   * **Byte rates**
   * **Packet drops**
   * **DNS**
   * **RTT**
3. Select the **Netobserv/Health** dashboard.
4. View metrics about the health of the Operator in the following categories, with each having the subset per node, namespace, source, and destination:

   * **Flows**
   * **Flows Overhead**
   * **Flow rates**
   * **Agents**
   * **Processor**
   * **Operator**

     **Infrastructure** and **Application** metrics are shown in a split-view for namespace and workloads.

### [13.2. Network observability metrics](#network-observability-metrics_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Review the comprehensive list of network observability metrics, prefixed by `netobserv_`, which you can configure in the `FlowCollector` resource and use to monitor traffic and create Prometheus alerts.

Metrics generated by the `flowlogs-pipeline` are configurable in the `spec.processor.metrics.includeList` of the `FlowCollector` custom resource to add or remove metrics.

You can also create alerts by using the `includeList` metrics in Prometheus rules, as shown in the example "Creating alerts".

When looking for these metrics in Prometheus, such as in the Console through **Observe** → **Metrics**, or when defining alerts, all the metrics names are prefixed with `netobserv_`. For example, `netobserv_namespace_flows_total`. Available metrics names are as follows:

includeList metrics names
:   Names followed by an asterisk `*` are enabled by default.

    * `namespace_egress_bytes_total`
    * `namespace_egress_packets_total`
    * `namespace_ingress_bytes_total`
    * `namespace_ingress_packets_total`
    * `namespace_flows_total` \*
    * `node_egress_bytes_total`
    * `node_egress_packets_total`
    * `node_ingress_bytes_total` \*
    * `node_ingress_packets_total`
    * `node_flows_total`
    * `workload_egress_bytes_total`
    * `workload_egress_packets_total`
    * `workload_ingress_bytes_total` \*
    * `workload_ingress_packets_total`
    * `workload_flows_total`

PacketDrop metrics names
:   When the `PacketDrop` feature is enabled in `spec.agent.ebpf.features` (with `privileged` mode), the following additional metrics are available:

    * `namespace_drop_bytes_total`
    * `namespace_drop_packets_total` \*
    * `node_drop_bytes_total`
    * `node_drop_packets_total`
    * `workload_drop_bytes_total`
    * `workload_drop_packets_total`

DNS metrics names
:   When the `DNSTracking` feature is enabled in `spec.agent.ebpf.features`, the following additional metrics are available:

    * `namespace_dns_latency_seconds` \*
    * `node_dns_latency_seconds`
    * `workload_dns_latency_seconds`

FlowRTT metrics names
:   When the `FlowRTT` feature is enabled in `spec.agent.ebpf.features`, the following additional metrics are available:

    * `namespace_rtt_seconds` \*
    * `node_rtt_seconds`
    * `workload_rtt_seconds`

Network events metrics names
:   When `NetworkEvents` feature is enabled, this metric is available by default:

    * `namespace_network_policy_events_total`

### [13.3. Creating alerts](#network-observability-netobserv-dashboard-high-traffic-alert_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Create custom `AlertingRule` resources based on `Netobserv` dashboard metrics to define conditions that trigger alerts in the OpenShift Container Platform console.

**Prerequisites**

* You have access to the cluster as a user with the cluster-admin role or with view permissions for all projects.
* You have the Network Observability Operator installed.

**Procedure**

1. Create a YAML file by clicking the import icon, **+**.
2. Add an alerting rule configuration to the YAML file. In the YAML sample that follows, an alert is created for when the cluster ingress traffic reaches a given threshold of 10 MBps per destination workload.

   ```
   apiVersion: monitoring.openshift.io/v1
   kind: AlertingRule
   metadata:
     name: netobserv-alerts
     namespace: openshift-monitoring
   spec:
     groups:
     - name: NetObservAlerts
       rules:
       - alert: NetObservIncomingBandwidth
         annotations:
           message: |-
             {{ $labels.job }}: incoming traffic exceeding 10 MBps for 30s on {{ $labels.DstK8S_OwnerType }} {{ $labels.DstK8S_OwnerName }} ({{ $labels.DstK8S_Namespace }}).
           summary: "High incoming traffic."
         expr: sum(rate(netobserv_workload_ingress_bytes_total     {SrcK8S_Namespace="openshift-ingress"}[1m])) by (job, DstK8S_Namespace, DstK8S_OwnerName, DstK8S_OwnerType) > 10000000
         for: 30s
         labels:
           severity: warning
   ```

   * The `netobserv_workload_ingress_bytes_total` metric is enabled by default in `spec.processor.metrics.includeList`.
3. Click **Create** to apply the configuration file to the cluster.

### [13.4. Custom metrics](#network-observability-custom-metrics_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Define custom metrics from flowlog data using the `FlowMetric` API, leveraging log fields as Prometheus labels to customize dashboard information and monitor specific cluster data.

In every flowlogs data that is collected, there are several fields labeled per log, such as source name and destination name. These fields can be leveraged as Prometheus labels to enable the customization of cluster information on your dashboard.

### [13.5. Configuring custom metrics by using FlowMetric API](#network-observability-configuring-custom-metrics_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Configure the `FlowMetric` API to create custom Prometheus metrics by mapping flow log fields as labels to meet specific monitoring needs.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **FlowMetric**.
3. In the **Project:** dropdown list, select the project of the Network Observability Operator instance.
4. Click **Create FlowMetric**.
5. Configure the `FlowMetric` resource. See "Custom metrics configuration examples".

**Verification**

1. Once the pods refresh, navigate to **Observe** → **Metrics**.
2. In the **Expression** field, type the metric name to view the corresponding result. You can also enter an expression, such as `topk(5, sum(rate(netobserv_cluster_external_ingress_bytes_total{DstK8S_Namespace="my-namespace"}[2m])) by (DstK8S_HostName, DstK8S_OwnerName, DstK8S_OwnerType))`

#### [13.5.1. Custom metrics configuration examples](#network-observability-configuring-custom-metrics-examples_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

To monitor specific network behaviors not covered by default metrics, such as external traffic volume or latency spikes, use the `FlowMetric` custom resource (CR). These examples provide the configuration needed to generate targeted Prometheus metrics from network flows.

##### [13.5.1.1. Tracking ingress bytes from cluster external sources](#tracking-ingress-bytes-from-cluster-external-sources_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

To measure the volume of data entering the cluster from external networks, use the following `FlowMetric` configuration. This metric helps identify potential bandwidth issues or unexpected external data transfer costs.

```
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flowmetric-cluster-external-ingress-traffic
  namespace: netobserv
spec:
  metricName: cluster_external_ingress_bytes_total
  type: Counter
  valueField: Bytes
  direction: Ingress
  labels: [DstK8S_HostName,DstK8S_Namespace,DstK8S_OwnerName,DstK8S_OwnerType]
  filters:
  - field: SrcSubnetLabel
    matchType: Absence
```

where:

`metadata.namespace`
:   Specifies the namespace where the `FlowMetric` resources are created. This must match the namespace defined in the `FlowCollector` resource `spec.namespace` field, which is `netobserv` by default.

`spec.metricName`
:   Specifies the name of the Prometheus metric, which in the OpenShift Container Platform web console appears with the prefix `netobserv-<metricName>`.

`spec.type`
:   Specifies the type of metric. The `Counter` type is useful for counting bytes or packets.

`spec.direction`
:   Specifies the direction of traffic to capture. If not specified, both ingress and egress are captured, which can lead to duplicated counts.

`spec.labels`
:   Specifies the labels that define what the metrics look like, the relationship between the different entities, and the metrics cardinality. For example, `SrcK8S_Name` is a high cardinality metric.

`spec.filters`
:   Specifies the criteria to refine results based on the listed criteria. In this example, selecting only the cluster external traffic is done by matching only flows where `SrcSubnetLabel` is absent. This assumes the subnet labels feature is enabled (via `spec.processor.subnetLabels`), which is done by default

##### [13.5.1.2. Monitoring RTT latency for cluster external ingress traffic](#monitoring-rtt-latency-for-cluster-external-ingress-traffic_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

To analyze the performance of external connections and identify high-latency paths, use the following `FlowMetric` configuration. This metric converts nanoseconds to seconds to align with standard Prometheus latency dashboards.

```
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flowmetric-cluster-external-ingress-rtt
  namespace: netobserv
spec:
  metricName: cluster_external_ingress_rtt_seconds
  type: Histogram
  valueField: TimeFlowRttNs
  direction: Ingress
  labels: [DstK8S_HostName,DstK8S_Namespace,DstK8S_OwnerName,DstK8S_OwnerType]
  filters:
  - field: SrcSubnetLabel
    matchType: Absence
  - field: TimeFlowRttNs
    matchType: Presence
  divider: "1000000000"
  buckets: [".001", ".005", ".01", ".02", ".03", ".04", ".05", ".075", ".1", ".25", "1"]
```

where:

`metadata.namespace`
:   Specifies the namespace where the `FlowMetric` resources are created. This must match the namespace defined in the `FlowCollector` resource `spec.namespace` field, which is `netobserv` by default.

`spec.type`
:   Specifies the type of metric. The `Histogram` type is useful for a latency value, such as `TimeFlowRttNs`.

`spec.divider`
:   Specifies the value used to divide the metric. Because the Round-trip time (RTT) is provided as nanoseconds in flows, use a divider of 1,000,000,000 to convert the value into seconds, which is standard in Prometheus guidelines.

`spec.buckets`
:   Specifies custom buckets for RTT precision. The optimal precision ranges between 5ms and 250ms.

### [13.6. Creating metrics from nested or array fields in the Traffic flows table](#network-observability-creating-metrics-network-events_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Create a `FlowMetric` custom resource to generate metrics for nested or array fields in the **Traffic flows** table, such as **Network events** or **Interfaces**.

Important

OVN Observability / Viewing `NetworkEvents` is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Important

OVN Observability and the ability to view and track network events is available only in OpenShift Container Platform 4.17 and 4.18.

The following example shows how to generate metrics from the **Network events** field for network policy events.

**Prerequisites**

* Enable `NetworkEvents feature`. See the Additional resources for how to do this.
* A network policy specified.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **FlowMetric**.
3. In the **Project** dropdown list, select the project of the Network Observability Operator instance.
4. Click **Create FlowMetric**.
5. Create `FlowMetric` resources to add the following configurations:

   **Configuration counting network policy events per policy name and namespace**

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowMetric
   metadata:
     name: network-policy-events
     namespace: netobserv
   spec:
     metricName: network_policy_events_total
     type: Counter
     labels: [NetworkEvents>Type, NetworkEvents>Namespace, NetworkEvents>Name, NetworkEvents>Action, NetworkEvents>Direction]
     filters:
     - field: NetworkEvents>Feature
       value: acl
     flatten: [NetworkEvents]
     remap:
       "NetworkEvents>Type": type
       "NetworkEvents>Namespace": namespace
       "NetworkEvents>Name": name
       "NetworkEvents>Direction": direction
   ```

   where:

   `spec.labels`
   :   Specifies the labels that represent the nested fields for **Network Events** from the **Traffic flows** table. Each network event has a specific type, namespace, name, action, and direction. You can alternatively specify `Interfaces` if `NetworkEvents` is unavailable in your version of OpenShift Container Platform.

   `spec.flatten`
   :   Specifies an optional field that contains a list of items to be represented as distinct items.

   `spec.remap`
   :   Specifies an optional set of fields to rename in Prometheus.

**Verification**

1. In the web console, navigate to **Observe** → **Dashboards** and scroll down to see the **Network Policy** tab.
2. You should begin seeing metrics filter in based on the metric you created along with the network policy specifications.

Important

High cardinality can affect the memory usage of Prometheus. You can check if specific labels have high cardinality in the network flows format. See "Network Flows format reference".

### [13.7. Configuring custom charts using FlowMetric API](#network-observability-custom-charts-flowmetrics_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Generate custom charts for OpenShift Container Platform web console dashboards by defining the charts section of the `FlowMetric` custom resource.

You can view custom charts as an administrator in the **Dashboard** menu.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **FlowMetric**.
3. In the **Project:** dropdown list, select the project of the Network Observability Operator instance.
4. Click **Create FlowMetric**.
5. Configure the `FlowMetric` resource. See "Flowmetric chart configuration examples".

**Verification**

1. Once the pods refresh, navigate to **Observe** → **Dashboards**.
2. Search for the **NetObserv / Main** dashboard. View two panels under the **NetObserv / Main** dashboard, or optionally a dashboard name that you create:

   * A textual single statistic showing the global external ingress rate summed across all dimensions
   * A timeseries graph showing the same metric per destination workload

For more information about the query language, refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).

#### [13.7.1. Flowmetric chart configuration examples](#network-observability-flowmetrics-charts-examples_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

These `FlowMetric` custom resource examples demonstrate how to define charts in the OpenShift Container Platform web console for tracking external ingress traffic and round-trip time (RTT) latency.

##### [13.7.1.1. Ingress bytes chart for cluster external sources](#chart-tracking-ingress-bytes-cluster-external-sources_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Use the following configuration to track the rate of ingress traffic from cluster external sources. These charts help identify bandwidth usage per workload.

```
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flowmetric-cluster-external-ingress-traffic
  namespace: netobserv
# ...
  charts:
  - dashboardName: Main
    title: External ingress traffic
    unit: Bps
    type: SingleStat
    queries:
    - promQL: "sum(rate($METRIC[2m]))"
      legend: ""
  - dashboardName: Main
    sectionName: External
    title: Top external ingress traffic per workload
    unit: Bps
    type: StackArea
    queries:
    - promQL: "sum(rate($METRIC{DstK8S_Namespace!=\"\"}[2m])) by (DstK8S_Namespace, DstK8S_OwnerName)"
      legend: "{{DstK8S_Namespace}} / {{DstK8S_OwnerName}}"
# ...
```

where:

`metadata.namespace`
:   Specifies the namespace where the `FlowMetric` resources are created. This must match the namespace defined in the `FlowCollector` `spec.namespace`, which is `netobserv` by default.

`spec.charts.dashboardName`
:   Specifies the name of the dashboard. Using a different `dashboardName` creates a new dashboard that is prefixed with `Netobserv`. For example, **Netobserv / <dashboard\_name>**.

##### [13.7.1.2. RTT latency chart for cluster external ingress traffic](#chart-rtt-latency-cluster-external-ingress-traffic_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Use the following configuration to monitor round-trip time (RTT) for cluster external ingress traffic. These examples use the `histogram_quantile` function to display the 50th and 99th percentiles (p50 and p99).

```
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowMetric
metadata:
  name: flowmetric-cluster-external-ingress-traffic
  namespace: netobserv
# ...
  charts:
  - dashboardName: Main
    title: External ingress TCP latency
    unit: seconds
    type: SingleStat
    queries:
    - promQL: "histogram_quantile(0.99, sum(rate($METRIC_bucket[2m])) by (le)) > 0"
      legend: "p99"
  - dashboardName: Main
    sectionName: External
    title: "Top external ingress sRTT per workload, p50 (ms)"
    unit: seconds
    type: Line
    queries:
    - promQL: "histogram_quantile(0.5, sum(rate($METRIC_bucket{DstK8S_Namespace!=\"\"}[2m])) by (le,DstK8S_Namespace,DstK8S_OwnerName))*1000 > 0"
      legend: "{{DstK8S_Namespace}} / {{DstK8S_OwnerName}}"
  - dashboardName: Main
    sectionName: External
    title: "Top external ingress sRTT per workload, p99 (ms)"
    unit: seconds
    type: Line
    queries:
    - promQL: "histogram_quantile(0.99, sum(rate($METRIC_bucket{DstK8S_Namespace!=\"\"}[2m])) by (le,DstK8S_Namespace,DstK8S_OwnerName))*1000 > 0"
      legend: "{{DstK8S_Namespace}} / {{DstK8S_OwnerName}}"
# ...
```

where:

`metadata.namespace`
:   Specifies the namespace where the `FlowMetric` resources are created. This must match the namespace defined in the `FlowCollector` `spec.namespace`, which is `netobserv` by default.

`spec.charts.dashboardName`
:   Specifies the name of the dashboard. Using a different `dashboardName` creates a new dashboard that is prefixed with `Netobserv`. For example, **Netobserv / <dashboard\_name>**.

##### [13.7.1.3. Calculate histogram averages](#calculate-histogram-averages_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

You can show averages of histograms by dividing the metric, `$METRIC_sum`, by the metric, `$METRIC_count`, which are automatically generated when you create a histogram. With the preceding example, the Prometheus query to do this is as follows:

```
promQL: "(sum(rate($METRIC_sum{DstK8S_Namespace!=\"\"}[2m])) by (DstK8S_Namespace,DstK8S_OwnerName) / sum(rate($METRIC_count{DstK8S_Namespace!=\"\"}[2m])) by (DstK8S_Namespace,DstK8S_OwnerName))*1000"
```

### [13.8. Detecting SYN flooding using the FlowMetric API and TCP flags](#network-observability-tcp-flag-syn-flood_metrics-dashboards-alerts) Copy linkLink copied to clipboard!

Deploy a custom `AlertingRule` and `FlowMetric` configuration to monitor TCP flags, enabling real-time detection and alerting for SYN flooding attacks on the cluster.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. In the **Provided APIs** heading for the **NetObserv Operator**, select **FlowMetric**.
3. In the **Project** dropdown list, select the project of the Network Observability Operator instance.
4. Click **Create FlowMetric**.
5. Create `FlowMetric` resources to add the following configurations:

   **Configuration counting flows per destination host and resource, with TCP flags**

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowMetric
   metadata:
     name: flows-with-flags-per-destination
   spec:
     metricName: flows_with_flags_per_destination_total
     type: Counter
     labels: [SrcSubnetLabel,DstSubnetLabel,DstK8S_Name,DstK8S_Type,DstK8S_HostName,DstK8S_Namespace,Flags]
   ```

   **Configuration counting flows per source host and resource, with TCP flags**

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowMetric
   metadata:
     name: flows-with-flags-per-source
   spec:
     metricName: flows_with_flags_per_source_total
     type: Counter
     labels: [DstSubnetLabel,SrcSubnetLabel,SrcK8S_Name,SrcK8S_Type,SrcK8S_HostName,SrcK8S_Namespace,Flags]
   ```
6. Deploy the following `AlertingRule` resource to alert for SYN flooding:

   **`AlertingRule` for SYN flooding**

   ```
   apiVersion: monitoring.openshift.io/v1
   kind: AlertingRule
   metadata:
     name: netobserv-syn-alerts
     namespace: openshift-monitoring
   # ...
     spec:
     groups:
     - name: NetObservSYNAlerts
       rules:
       - alert: NetObserv-SYNFlood-in
         annotations:
           message: |-
             {{ $labels.job }}: incoming SYN-flood attack suspected to Host={{ $labels.DstK8S_HostName}}, Namespace={{ $labels.DstK8S_Namespace }}, Resource={{ $labels.DstK8S_Name }}. This is characterized by a high volume of SYN-only flows with different source IPs and/or ports.
           summary: "Incoming SYN-flood"
         expr: sum(rate(netobserv_flows_with_flags_per_destination_total{Flags="2"}[1m])) by (job, DstK8S_HostName, DstK8S_Namespace, DstK8S_Name) > 300
         for: 15s
         labels:
           severity: warning
           app: netobserv
       - alert: NetObserv-SYNFlood-out
         annotations:
           message: |-
             {{ $labels.job }}: outgoing SYN-flood attack suspected from Host={{ $labels.SrcK8S_HostName}}, Namespace={{ $labels.SrcK8S_Namespace }}, Resource={{ $labels.SrcK8S_Name }}. This is characterized by a high volume of SYN-only flows with different source IPs and/or ports.
           summary: "Outgoing SYN-flood"
         expr: sum(rate(netobserv_flows_with_flags_per_source_total{Flags="2"}[1m])) by (job, SrcK8S_HostName, SrcK8S_Namespace, SrcK8S_Name) > 300
         for: 15s
         labels:
           severity: warning
           app: netobserv
   # ...
   ```

   In this example, the threshold for the alert is `300`; however, you can adapt this value empirically. A threshold that is too low might produce false-positives, and if it’s too high it might miss actual attacks.

**Verification**

1. In the web console, click **Manage Columns** in the **Network Traffic** table view and click **TCP flags**.
2. In the **Network Traffic** table view, filter on **TCP protocol SYN TCPFlag**. A large number of flows with the same **byteSize** indicates a SYN flood.
3. Go to **Observe** → **Alerting** and select the **Alerting Rules** tab.
4. Filter on **netobserv-synflood-in alert**. The alert should fire when SYN flooding occurs.

## [Chapter 14. Monitoring the Network Observability Operator](#network-observability-operator-monitoring) Copy linkLink copied to clipboard!

Use the OpenShift Container Platform web console to monitor alerts related to the Network Observability Operator’s health. This helps you maintain system stability and quickly detect operational issues.

### [14.1. Health dashboards](#network-observability-health-dashboard-overview_network_observability) Copy linkLink copied to clipboard!

View the Network Observability Operator health dashboards in the OpenShift Container Platform web console to monitor the health status, resource usage, and internal statistics of the operator and its components.

Metrics are located in the **Observe** → **Dashboards** page in the OpenShift Container Platform web console. You can view metrics about the health of the Network Observability Operator in the following categories:

* **Flows per second**
* **Sampling**
* **Errors last minute**
* **Dropped flows per second**
* **Flowlogs-pipeline statistics**
* **Flowlogs-pipleine statistics views**
* **eBPF agent statistics views**
* **Operator statistics**
* **Resource usage**

### [14.2. Health alerts](#network-observability-health-alert-overview_network_observability) Copy linkLink copied to clipboard!

Understand the health alerts generated by the Network Observability Operator, which trigger banners when conditions like Loki ingestion errors, zero flow ingestion, or dropped eBPF flows occur.

A health alert banner that directs you to the dashboard can appear on the **Network Traffic** and **Home** pages if an alert is triggered. Alerts are generated in the following cases:

* The `NetObservLokiError` alert occurs if the `flowlogs-pipeline` workload is dropping flows because of Loki errors, such as if the Loki ingestion rate limit has been reached.
* The `NetObservNoFlows` alert occurs if no flows are ingested for a certain amount of time.
* The `NetObservFlowsDropped` alert occurs if the Network Observability eBPF agent hashmap table is full, and the eBPF agent processes flows with degraded performance, or when the capacity limiter is triggered.

### [14.3. Viewing health information](#network-observability-dashboard-view_network_observability) Copy linkLink copied to clipboard!

View the **Netobserv/Health** dashboard within the OpenShift Container Platform web console to monitor the health status and resource usage of the Network Observability Operator and its components.

**Prerequisites**

* You have the Network Observability Operator installed.
* You have access to the cluster as a user with the `cluster-admin` role or with view permissions for all projects.

**Procedure**

1. From the **Administrator** perspective in the web console, navigate to **Observe** → **Dashboards**.
2. From the **Dashboards** dropdown, select **Netobserv/Health**.
3. View the metrics about the health of the Operator that are displayed on the page.

#### [14.3.1. Disabling health alerts](#network-observability-disable-alerts_network_observability) Copy linkLink copied to clipboard!

Disable specific health alerts, such as `NetObservLokiError` or `NetObservNoFlows`, by editing the `FlowCollector` resource and using the `spec.processor.metrics.disableAlerts` specification.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** then select the **YAML** tab.
4. Add `spec.processor.metrics.disableAlerts` to disable health alerts, as in the following YAML sample:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     processor:
       metrics:
         disableAlerts: [NetObservLokiError, NetObservNoFlows]
   ```

   where:

   `spec.processor.metrics.disableAlerts`
   :   Specifies one or more types of alerts to disable.

### [14.4. Creating Loki rate limit alerts for the NetObserv dashboard](#network-observability-netobserv-dashboard-rate-limit-alerts_network_observability) Copy linkLink copied to clipboard!

Create a custom `AlertingRule` resource based on Loki metrics to monitor for and trigger alerts when the Loki ingestion rate limits are reached, indicated by HTTP 429 errors.

You can create custom alerting rules for the **Netobserv** dashboard metrics to trigger alerts when Loki rate limits have been reached.

**Prerequisites**

* You have access to the cluster as a user with the cluster-admin role or with view permissions for all projects.
* You have the Network Observability Operator installed.

**Procedure**

1. Create a YAML file by clicking the import icon, **+**.
2. Add an alerting rule configuration to the YAML file. In the YAML sample that follows, an alert is created for when Loki rate limits have been reached:

   ```
   apiVersion: monitoring.openshift.io/v1
   kind: AlertingRule
   metadata:
     name: loki-alerts
     namespace: openshift-monitoring
   spec:
     groups:
     - name: LokiRateLimitAlerts
       rules:
       - alert: LokiTenantRateLimit
         annotations:
           message: |-
             {{ $labels.job }} {{ $labels.route }} is experiencing 429 errors.
           summary: "At any number of requests are responded with the rate limit error code."
         expr: sum(irate(loki_request_duration_seconds_count{status_code="429"}[1m])) by (job, namespace, route) / sum(irate(loki_request_duration_seconds_count[1m])) by (job, namespace, route) * 100 > 0
         for: 10s
         labels:
           severity: warning
   ```
3. Click **Create** to apply the configuration file to the cluster.

### [14.5. Using the eBPF agent alert](#network-observability-netobserv-dashboard-ebpf-agent-alerts_network_observability) Copy linkLink copied to clipboard!

Resolve the `NetObservAgentFlowsDropped` alert, which occurs when the eBPF agent hashmap is full, by increasing the `spec.agent.ebpf.cacheMaxFlows` value in the `FlowCollector` custom resource.

An alert, `NetObservAgentFlowsDropped`, is also triggered when the capacity limiter is triggered. If you see this alert, consider increasing the `cacheMaxFlows` in the `FlowCollector`, as shown in the following example.

Note

Increasing the `cacheMaxFlows` might increase the memory usage of the eBPF agent.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **Network Observability Operator**, select **Flow Collector**.
3. Select **cluster**, and then select the **YAML** tab.
4. Increase the `spec.agent.ebpf.cacheMaxFlows` value, as shown in the following YAML sample:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     deploymentModel: Service
     agent:
       type: eBPF
       ebpf:
         cacheMaxFlows: 200000
   ```

   where:

   `spec.agent.ebpf.cacheMaxFlows`
   :   Specifies the maximum number of flows to cache. If a `NetObservAgentFlowsDropped` alert occurs, increase this value from its current level.

## [Chapter 15. Scheduling resources](#network-observability-scheduling-resources) Copy linkLink copied to clipboard!

Taints and tolerations help you control which nodes host certain pods. Use these tools, along with node selectors, to guide the placement of network observability components.

A node selector specifies a map of key/value pairs that are defined using custom labels on nodes and selectors specified in pods.

For the pod to be eligible to run on a node, the pod must have the same key/value node selector as the label on the node.

### [15.1. Network observability deployment in specific nodes](#network-observability-multi-tenancy_network_observability_scheduling) Copy linkLink copied to clipboard!

Configure the `FlowCollector` resource using scheduling specifications, including `NodeSelector`, `Tolerations`, and `Affinity`, to control the deployment of network observability components on specific nodes.

The `spec.agent.ebpf.advanced.scheduling`, `spec.processor.advanced.scheduling`, and `spec.consolePlugin.advanced.scheduling` specifications have the following configurable settings:

* `NodeSelector`
* `Tolerations`
* `Affinity`
* `PriorityClassName`

**Sample `FlowCollector` resource for `spec.<component>.advanced.scheduling`**

```
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
# ...
advanced:
  scheduling:
    tolerations:
    - key: "<taint key>"
      operator: "Equal"
      value: "<taint value>"
      effect: "<taint effect>"
      nodeSelector:
        <key>: <value>
      affinity:
        nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: name
              operator: In
              values:
              - app-worker-node
      priorityClassName: """
# ...
```

## [Chapter 16. Secondary networks](#network-observability-secondary-networks) Copy linkLink copied to clipboard!

You can configure the Network Observability Operator to collect and enrich network flow data from secondary networks, such as `SR-IOV` and `OVN-Kubernetes`.

### [16.1. Prerequisites](#network-observability-secondary-network-prerequisites_network-observability-secondary-networks) Copy linkLink copied to clipboard!

* Access to an OpenShift Container Platform cluster with an additional network interface, such as a secondary interface or an L2 network.

### [16.2. Configuring monitoring for SR-IOV interface traffic](#network-observability-SR-IOV-config_network-observability-secondary-networks) Copy linkLink copied to clipboard!

Configure the `FlowCollector` resource to monitor traffic on Single Root I/O Virtualization (SR-IOV) device by setting the `spec.agent.ebpf.privileged` field to `true`, which enables the eBPF agent to monitor other network namespaces.

The eBPF agent monitors other network namespaces in addition to the host network namespaces, which are monitored by default. When a pod with a virtual functions (VF) interface is created, a new network namespace is created. With `SRIOVNetwork` policy `IPAM` configurations specified, the VF interface is migrated from the host network namespace to the pod network namespace.

**Prerequisites**

* Access to an OpenShift Container Platform cluster with a SR-IOV device.
* The `SRIOVNetwork` custom resource (CR) `spec.ipam` configuration must be set with an IP address from the range that the interface lists or from other plugins.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**.
2. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
3. Select **cluster** and then select the **YAML** tab.
4. Configure the `FlowCollector` custom resource. A sample configuration is as follows:

   **Configure `FlowCollector` for SR-IOV monitoring**

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     namespace: netobserv
     deploymentModel: Service
     agent:
       type: eBPF
       ebpf:
         privileged: true
   ```

   * The `spec.agent.ebpf.privileged` field value must be set to `true` to enable SR-IOV monitoring.

### [16.3. Configuring virtual machine (VM) secondary network interfaces for Network Observability](#network-observability-virtualization-config_network-observability-secondary-networks) Copy linkLink copied to clipboard!

Configure the `FlowCollector` to monitor VM secondary network traffic by setting the eBPF agent to `privileged` mode and defining the indexing for secondary networks, enabling the capture and enrichment of flows from OpenShift Virtualization.

Network flows coming from VMs that are connected to the default internal pod network are automatically captured by network observability.

**Procedure**

1. Get information about the virtual machine launcher pod by running the following command. This information is used in Step 5:

   ```
   $ oc get pod virt-launcher-<vm_name>-<suffix> -n <namespace> -o yaml
   ```

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     annotations:
       k8s.v1.cni.cncf.io/network-status: |-
         [{
           "name": "ovn-kubernetes",
           "interface": "eth0",
           "ips": [
             "10.129.2.39"
           ],
           "mac": "0a:58:0a:81:02:27",
           "default": true,
           "dns": {}
         },
         {
           "name": "my-vms/l2-network",
           "interface": "podc0f69e19ba2",
           "ips": [
             "10.10.10.15"
           ],
           "mac": "02:fb:f8:00:00:12",
           "dns": {}
         }]
     name: virt-launcher-fedora-aqua-fowl-13-zr2x9
     namespace: my-vms
   spec:
   #  ...
   status:
   #  ...
   ```

   where:

   `name`
   :   Specifies the name of the secondary network.

   `interface`
   :   Specifies the network interface of the secondary network.

   `ips`
   :   Specifies the list of IP addresses used by the secondary network.

   `mac`
   :   Specifies the MAC address used for the secondary network.
2. In the web console, navigate to **Ecosystem** → **Installed Operators**.
3. Under the **Provided APIs** heading for the **NetObserv Operator**, select **Flow Collector**.
4. Select **cluster** and then select the **YAML** tab.
5. Configure `FlowCollector` based on the information you found from the additional network investigation:

   ```
   apiVersion: flows.netobserv.io/v1beta2
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     agent:
       ebpf:
         privileged: true
     processor:
       advanced:
         secondaryNetworks:
         - index:
           - MAC
           name: my-vms/l2-network
   # ...
   ```

   where:

   `spec.agent.ebpf.privileged`
   :   Specifies that the eBPF agent runs in `privileged` mode, which is required to collect flows from secondary network interfaces on virtual machine launcher pods.

   `spec.processor.advanced.secondaryNetworks.index`
   :   Specifies the fields to use for indexing the virtual machine launcher pods. It is recommended to use the `MAC` address as the indexing field to get network flows enrichment for secondary interfaces. If you have overlapping MAC addresses between pods, then additional indexing fields, such as `IP` and `Interface`, can be added to ensure accurate enrichment.

   `MAC`
   :   Specifies the MAC address as an indexing field value. Add `MAC` to the `index` field list if your additional network information includes a MAC address.

   `spec.processor.advanced.secondaryNetworks.name`
   :   Specifies the name of the secondary network as found in the `k8s.v1.cni.cncf.io/network-status` annotation of the virtual machine launcher pod. The format is typically `<namespace>/<network_attachment_definition_name>`.

**Verification**

1. Observe VM traffic:

   1. Navigate to the **Network Traffic** page.
   2. Filter by **Source** IP using your virtual machine IP found in `k8s.v1.cni.cncf.io/network-status` annotation.
   3. View both **Source** and **Destination** fields, which should be enriched, and identify the VM launcher pods and the VM instance as owners.

## [Chapter 17. Network Observability CLI](#network-observability-cli) Copy linkLink copied to clipboard!

### [17.1. Installing the Network Observability CLI](#netobserv-cli-install) Copy linkLink copied to clipboard!

The Network Observability CLI (oc netobserv) is a standalone OpenShift CLI (`oc`) plugin used to debug and troubleshoot cluster network traffic. It operates independently of the Network Observability Operator to gather immediate network performance diagnostics.

#### [17.1.1. About the Network Observability CLI](#network-observability-netoberv-cli-about_netobserv-cli-install) Copy linkLink copied to clipboard!

Use the Network Observability CLI (`oc netobserv`) to quickly debug and troubleshoot networking issues. This tool provides instant, live insight into flows and packets without installing the Network Observability Operator.

The Network Observability CLI is a flow and packet visualization tool that relies on eBPF agents to stream collected data to an ephemeral collector pod. It requires no persistent storage during the capture. After the run, the output is transferred to your local machine.

Important

CLI capture is meant to run only for short durations, such as 8-10 minutes. If it runs for too long, it can be difficult to delete the running process.

#### [17.1.2. Installing the Network Observability CLI](#network-observability-cli-install_netobserv-cli-install) Copy linkLink copied to clipboard!

The Network Observability CLI gives you a lightweight way to quickly debug and troubleshoot network observability. It must be installed separately.

Installing the Network Observability CLI (`oc netobserv`) is a separate procedure from the Network Observability Operator installation. This means that, even if the Operator is installed from the software catalog, the `CLI` must be installed separately.

Note

Users can optionally use Krew to install the `netobserv` CLI plugin. For more information, see "Installing a CLI plugin with Krew".

**Prerequisites**

* You must install the OpenShift CLI (`oc`).
* You must have a macOS or Linux operating system.
* You must install either `docker` or `podman`.

Note

You can use `podman` or `docker` to run the installation commands. This procedure uses `podman`.

**Procedure**

1. Log in to the **Red Hat registry** by running the following command:

   ```
   $ podman login registry.redhat.io
   ```
2. Extract the `oc-netobserv` file from the image by running the following commands:

   ```
   $ podman create --name netobserv-cli registry.redhat.io/network-observability/network-observability-cli-rhel9:1.11
   $ podman cp netobserv-cli:/oc-netobserv .
   $ podman rm netobserv-cli
   ```
3. Move the extracted file to a directory that is on the system’s `PATH`, such as `/usr/local/bin/`, by running the following command:

   ```
   $ sudo mv oc-netobserv /usr/local/bin/
   ```

**Verification**

1. Verify that `oc netobserv` is available:

   ```
   $ oc netobserv version
   ```

   This command should produce an outcome similar to the following example:

```
Netobserv CLI version <version>
```

### [17.2. Using the Network Observability CLI](#netobserv-cli-using) Copy linkLink copied to clipboard!

The Network Observability CLI filters and visualizes network flow and packet telemetry directly within the terminal. The tool exports captured data as JSON, database files, or Packet Capture (PCAP) files for seamless integration with third-party analysis utilities.

#### [17.2.1. Capturing flows](#network-observability-cli-capturing-flows_netobserv-cli-using) Copy linkLink copied to clipboard!

Capture network flows and apply filters based on resources or zones directly in the CLI. This helps you solve complex use cases, such as visualizing the Round-Trip Time (RTT) between two different zones.

Table visualization in the CLI provides viewing and flow search capabilities.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Install the Network Observability CLI (`oc netobserv`) plugin.

**Procedure**

1. Capture flows with filters enabled by running the following command:

   ```
   $ oc netobserv flows --enable_filter=true --action=Accept --cidr=0.0.0.0/0 --protocol=TCP --port=49051
   ```
2. Add filters to the `live table filter` prompt in the terminal to further refine the incoming flows. For example:

   ```
   live table filter: [SrcK8S_Zone:us-west-1b] press enter to match multiple regular expressions at once
   ```
3. Use the **PageUp** and **PageDown** keys to toggle between **None**, **Resource**, **Zone**, **Host**, **Owner** and **all of the above**.
4. To stop capturing, press `Ctrl`+`C`. The data that was captured is written to two separate files in an `./output` directory located in the same path used to install the CLI.
5. View the captured data in the `./output/flow/<capture_date_time>.json` JSON file, which contains JSON arrays of the captured data.

   **Example JSON file**

   ```
   {
     "AgentIP": "10.0.1.76",
     "Bytes": 561,
     "DnsErrno": 0,
     "Dscp": 20,
     "DstAddr": "f904:ece9:ba63:6ac7:8018:1e5:7130:0",
     "DstMac": "0A:58:0A:80:00:37",
     "DstPort": 9999,
     "Duplicate": false,
     "Etype": 2048,
     "Flags": 16,
     "FlowDirection": 0,
     "IfDirection": 0,
     "Interface": "ens5",
     "K8S_FlowLayer": "infra",
     "Packets": 1,
     "Proto": 6,
     "SrcAddr": "3e06:6c10:6440:2:a80:37:b756:270f",
     "SrcMac": "0A:58:0A:80:00:01",
     "SrcPort": 46934,
     "TimeFlowEndMs": 1709741962111,
     "TimeFlowRttNs": 121000,
     "TimeFlowStartMs": 1709741962111,
     "TimeReceived": 1709741964
   }
   ```
6. You can use SQLite to inspect the `./output/flow/<capture_date_time>.db` database file. For example:

   1. Open the file by running the following command:

      ```
      $ sqlite3 ./output/flow/<capture_date_time>.db
      ```
   2. Query the data by running a SQLite `SELECT` statement, for example:

      ```
      sqlite> SELECT DnsLatencyMs, DnsFlagsResponseCode, DnsId, DstAddr, DstPort, Interface, Proto, SrcAddr, SrcPort, Bytes, Packets FROM flow WHERE DnsLatencyMs >10 LIMIT 10;
      ```

      **Example output**

      ```
      12|NoError|58747|10.128.0.63|57856||17|172.30.0.10|53|284|1
      11|NoError|20486|10.128.0.52|56575||17|169.254.169.254|53|225|1
      11|NoError|59544|10.128.0.103|51089||17|172.30.0.10|53|307|1
      13|NoError|32519|10.128.0.52|55241||17|169.254.169.254|53|254|1
      12|NoError|32519|10.0.0.3|55241||17|169.254.169.254|53|254|1
      15|NoError|57673|10.128.0.19|59051||17|172.30.0.10|53|313|1
      13|NoError|35652|10.0.0.3|46532||17|169.254.169.254|53|183|1
      32|NoError|37326|10.0.0.3|52718||17|169.254.169.254|53|169|1
      14|NoError|14530|10.0.0.3|58203||17|169.254.169.254|53|246|1
      15|NoError|40548|10.0.0.3|45933||17|169.254.169.254|53|174|1
      ```

#### [17.2.2. Capturing packets](#network-observability-cli-capturing-packets_netobserv-cli-using) Copy linkLink copied to clipboard!

Use the Network Observability CLI to capture network packets. You can apply filters and refine them live in the terminal for accurate, real-time debugging.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Install the Network Observability CLI (`oc netobserv`) plugin.

**Procedure**

1. Run the packet capture with filters enabled:

   ```
   $ oc netobserv packets --action=Accept --cidr=0.0.0.0/0 --protocol=TCP --port=49051
   ```
2. Add filters to the `live table filter` prompt in the terminal to refine the incoming packets. An example filter is as follows:

   ```
   live table filter: [SrcK8S_Zone:us-west-1b] press enter to match multiple regular expressions at once
   ```
3. Use the **PageUp** and **PageDown** keys to toggle between **None**, **Resource**, **Zone**, **Host**, **Owner** and **all of the above**.
4. To stop capturing, press `Ctrl`+`C`.
5. View the captured data, which is written to a single file in an `./output/pcap` directory located in the same path that was used to install the CLI:

   1. The `./output/pcap/<capture_date_time>.pcap` file can be opened with Wireshark.

#### [17.2.3. Capturing metrics](#network-observability-cli-capturing-metrics_netobserv-cli-using) Copy linkLink copied to clipboard!

Generate on-demand network observability dashboards in Prometheus using a service monitor. This allows you to quickly view and analyze network metrics.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Install the Network Observability CLI (`oc netobserv`) plugin.

**Procedure**

1. Capture metrics with filters enabled by running the following command:

   **Example output**

   ```
   $ oc netobserv metrics --enable_filter=true --cidr=0.0.0.0/0 --protocol=TCP --port=49051
   ```
2. Open the link provided in the terminal to view the **NetObserv / On-Demand** dashboard:

   **Example URL**

   ```
   https://console-openshift-console.apps.rosa...openshiftapps.com/monitoring/dashboards/netobserv-cli
   ```

   Note

   Features that are not enabled present as empty graphs.

#### [17.2.4. Cleaning the Network Observability CLI](#network-observability-cli-uninstall_netobserv-cli-using) Copy linkLink copied to clipboard!

Use `oc netobserv cleanup` to manually remove all components installed by the Network Observability CLI from your cluster. While the client runs this command automatically after a capture, you may need to run it manually if you face connectivity issues.

**Procedure**

* Run the following command:

  ```
  $ oc netobserv cleanup
  ```

**Additional resources**

* [Network Observability CLI reference](#network-observability-netobserv-cli-reference_netobserv-cli-reference "17.3.1. Network Observability CLI usage")

### [17.3. Network Observability CLI (oc netobserv) reference](#netobserv-cli-reference) Copy linkLink copied to clipboard!

The Network Observability CLI (`oc netobserv`) provides feature and filtering parity with the Network Observability Operator. Use command-line arguments to dynamically toggle features and isolate specific cluster network traffic flows.

#### [17.3.1. Network Observability CLI usage](#network-observability-netobserv-cli-reference_netobserv-cli-reference) Copy linkLink copied to clipboard!

You can use the Network Observability CLI (`oc netobserv`) to pass command line arguments to capture flows data, packets data, and metrics for further analysis and enable features supported by the Network Observability Operator.

##### [17.3.1.1. Syntax](#cli-syntax_netobserv-cli-reference) Copy linkLink copied to clipboard!

The basic syntax for `oc netobserv` commands:

**`oc netobserv` syntax**

```
$ oc netobserv [<command>] [<feature_option>] [<command_options>]
```

1

[1](#CO1-1)
:   Feature options can only be used with the `oc netobserv flows` command. They cannot be used with the `oc netobserv packets` command.

##### [17.3.1.2. Basic commands](#cli-basic-commands_netobserv-cli-reference) Copy linkLink copied to clipboard!

Expand

Table 17.1. Basic commands

| Command | Description |
| --- | --- |
| flows | Capture flows information. For subcommands, see the "Flows capture options" table. |
| packets | Capture packets data. For subcommands, see the "Packets capture options" table. |
| metrics | Capture metrics data. For subcommands, see the "Metrics capture options" table. |
| follow | Follow collector logs when running in background. |
| stop | Stop collection by removing agent daemonset. |
| copy | Copy collector generated files locally. |
| cleanup | Remove the Network Observability CLI components. |
| version | Print the software version. |
| help | Show help. |

Show more

##### [17.3.1.3. Flows capture options](#cli-reference-flows-capture-options_netobserv-cli-reference) Copy linkLink copied to clipboard!

Flows capture has mandatory commands as well as additional options, such as enabling extra features about packet drops, DNS latencies, Round-trip time, and filtering.

**`oc netobserv flows` syntax**

```
$ oc netobserv flows [<feature_option>] [<command_options>]
```

Expand

| Option | Description | Default |
| --- | --- | --- |
| --enable\_all | enable all eBPF features | false |
| --enable\_dns | enable DNS tracking | false |
| --enable\_ipsec | enable IPsec tracking | false |
| --enable\_network\_events | enable network events monitoring | false |
| --enable\_pkt\_translation | enable packet translation | false |
| --enable\_pkt\_drop | enable packet drop | false |
| --enable\_rtt | enable RTT tracking | false |
| --enable\_udn\_mapping | enable User Defined Network mapping | false |
| --get-subnets | get subnets information | false |
| --privileged | force eBPF agent privileged mode | auto |
| --sampling | packets sampling interval | 1 |
| --background | run in background | false |
| --copy | copy the output files locally | prompt |
| --log-level | components logs | info |
| --max-time | maximum capture time | 5m |
| --max-bytes | maximum capture bytes | 50000000 = 50MB |
| --action | filter action | Accept |
| --cidr | filter CIDR | 0.0.0.0/0 |
| --direction | filter direction | - |
| --dport | filter destination port | - |
| --dport\_range | filter destination port range | - |
| --dports | filter on either of two destination ports | - |
| --drops | filter flows with only dropped packets | false |
| --icmp\_code | filter ICMP code | - |
| --icmp\_type | filter ICMP type | - |
| --node-selector | capture on specific nodes | - |
| --peer\_ip | filter peer IP | - |
| --peer\_cidr | filter peer CIDR | - |
| --port\_range | filter port range | - |
| --port | filter port | - |
| --ports | filter on either of two ports | - |
| --protocol | filter protocol | - |
| --query | filter flows using a custom query | - |
| --sport\_range | filter source port range | - |
| --sport | filter source port | - |
| --sports | filter on either of two source ports | - |
| --tcp\_flags | filter TCP flags | - |
| --interfaces | list of interfaces to monitor, comma separated | - |
| --exclude\_interfaces | list of interfaces to exclude, comma separated | lo |

Show more

**Example running flows capture on TCP protocol and port 49051 with PacketDrop and RTT features enabled:**

```
$ oc netobserv flows --enable_pkt_drop  --enable_rtt --action=Accept --cidr=0.0.0.0/0 --protocol=TCP --port=49051
```

##### [17.3.1.4. Packets capture options](#cli-reference-packet-capture-options_netobserv-cli-reference) Copy linkLink copied to clipboard!

You can filter packets capture data the as same as flows capture by using the filters. Certain features, such as packets drop, DNS, RTT, and network events, are only available for flows and metrics capture.

**`oc netobserv packets` syntax**

```
$ oc netobserv packets [<option>]
```

Expand

| Option | Description | Default |
| --- | --- | --- |
| --background | run in background | false |
| --copy | copy the output files locally | prompt |
| --log-level | components logs | info |
| --max-time | maximum capture time | 5m |
| --max-bytes | maximum capture bytes | 50000000 = 50MB |
| --action | filter action | Accept |
| --cidr | filter CIDR | 0.0.0.0/0 |
| --direction | filter direction | - |
| --dport | filter destination port | - |
| --dport\_range | filter destination port range | - |
| --dports | filter on either of two destination ports | - |
| --drops | filter flows with only dropped packets | false |
| --icmp\_code | filter ICMP code | - |
| --icmp\_type | filter ICMP type | - |
| --node-selector | capture on specific nodes | - |
| --peer\_ip | filter peer IP | - |
| --peer\_cidr | filter peer CIDR | - |
| --port\_range | filter port range | - |
| --port | filter port | - |
| --ports | filter on either of two ports | - |
| --protocol | filter protocol | - |
| --query | filter flows using a custom query | - |
| --sport\_range | filter source port range | - |
| --sport | filter source port | - |
| --sports | filter on either of two source ports | - |
| --tcp\_flags | filter TCP flags | - |

Show more

**Example running packets capture on TCP protocol and port 49051:**

```
$ oc netobserv packets --action=Accept --cidr=0.0.0.0/0 --protocol=TCP --port=49051
```

##### [17.3.1.5. Metrics capture options](#cli-reference-metrics-capture-options_netobserv-cli-reference) Copy linkLink copied to clipboard!

You can enable features and use filters on metrics capture, the same as flows capture. The generated graphs fill accordingly in the dashboard.

**`oc netobserv metrics` syntax**

```
$ oc netobserv metrics [<option>]
```

Expand

| Option | Description | Default |
| --- | --- | --- |
| --enable\_all | enable all eBPF features | false |
| --enable\_dns | enable DNS tracking | false |
| --enable\_ipsec | enable IPsec tracking | false |
| --enable\_network\_events | enable network events monitoring | false |
| --enable\_pkt\_translation | enable packet translation | false |
| --enable\_pkt\_drop | enable packet drop | false |
| --enable\_rtt | enable RTT tracking | false |
| --enable\_udn\_mapping | enable User Defined Network mapping | false |
| --get-subnets | get subnets information | false |
| --privileged | force eBPF agent privileged mode | auto |
| --sampling | packets sampling interval | 1 |
| --background | run in background | false |
| --log-level | components logs | info |
| --max-time | maximum capture time | 1h |
| --action | filter action | Accept |
| --cidr | filter CIDR | 0.0.0.0/0 |
| --direction | filter direction | - |
| --dport | filter destination port | - |
| --dport\_range | filter destination port range | - |
| --dports | filter on either of two destination ports | - |
| --drops | filter flows with only dropped packets | false |
| --icmp\_code | filter ICMP code | - |
| --icmp\_type | filter ICMP type | - |
| --node-selector | capture on specific nodes | - |
| --peer\_ip | filter peer IP | - |
| --peer\_cidr | filter peer CIDR | - |
| --port\_range | filter port range | - |
| --port | filter port | - |
| --ports | filter on either of two ports | - |
| --protocol | filter protocol | - |
| --query | filter flows using a custom query | - |
| --sport\_range | filter source port range | - |
| --sport | filter source port | - |
| --sports | filter on either of two source ports | - |
| --tcp\_flags | filter TCP flags | - |
| --include\_list | list of metric names to generate, comma separated | namespace\_flows\_total,node\_ingress\_bytes\_total,node\_egress\_bytes\_total,workload\_ingress\_bytes\_total |
| --interfaces | list of interfaces to monitor, comma separated | - |
| --exclude\_interfaces | list of interfaces to exclude, comma separated | lo |

Show more

**Example running metrics capture for TCP drops**

```
$ oc netobserv metrics --enable_pkt_drop --protocol=TCP
```

## [Chapter 18. FlowCollector API reference](#flowcollector-api) Copy linkLink copied to clipboard!

The `FlowCollector` API is the underlying schema used to pilot and configure the deployments for collecting network flows. This reference guide helps you manage those critical settings.

### [18.1. FlowCollector API specifications](#network-observability-flowcollector-api-specifications_network_observability) Copy linkLink copied to clipboard!

Description
:   `FlowCollector` is the schema for the network flows collection API, which pilots and configures the underlying deployments.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and might reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers might infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | `object` | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Defines the desired state of the FlowCollector resource.  \*: the mention of "unsupported" or "deprecated" for a feature throughout this document means that this feature is not officially supported by Red Hat. It might have been, for example, contributed by the community and accepted without a formal agreement for maintenance. The product maintainers might provide some support for these features as a best effort only. |

Show more

#### [18.1.1. .metadata](#metadata-2) Copy linkLink copied to clipboard!

Description
:   Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>

Type
:   `object`

#### [18.1.2. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   Defines the desired state of the FlowCollector resource.

    \*: the mention of "unsupported" or "deprecated" for a feature throughout this document means that this feature is not officially supported by Red Hat. It might have been, for example, contributed by the community and accepted without a formal agreement for maintenance. The product maintainers might provide some support for these features as a best effort only.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `agent` | `object` | Agent configuration for flows extraction. |
| `consolePlugin` | `object` | `consolePlugin` defines the settings related to the OpenShift Container Platform Console plugin, when available. |
| `deploymentModel` | `string` | `deploymentModel` defines the desired type of deployment for flow processing. Possible values are:  - `Service` (default) to make the flow processor listen as a Kubernetes Service, backed by a scalable Deployment.  - `Kafka` to make flows sent to a Kafka pipeline before consumption by the processor.  - `Direct` to make the flow processor listen directly from the agents using the host network, backed by a DaemonSet. Only recommended on small clusters, below 15 nodes.  Kafka can provide better scalability, resiliency, and high availability (for more details, see <https://www.redhat.com/en/topics/integration/what-is-apache-kafka>).  `Direct` is not recommended on large clusters as it is less memory efficient. |
| `execution` | `object` | `execution` defines configuration related to the execution of the flow collection process. |
| `exporters` | `array` | `exporters` defines additional optional exporters for custom consumption or storage. |
| `kafka` | `object` | Kafka configuration, allowing to use Kafka as a broker as part of the flow collection pipeline. Available when the `spec.deploymentModel` is `Kafka`. |
| `loki` | `object` | `loki`, the flow store, client settings. |
| `namespace` | `string` | Namespace where Network Observability pods are deployed. Those pods require various cluster role bindings in order to operate. Those bindings are preinstalled for service accounts located in the default namespace. If you configured a different namespace, you must update (or recreate) the cluster role bindings accordingly. You can see the list of preinstalled bindings here: <https://github.com/openshift/network-observability-operator/blob/release-1.12/helm/templates/component_role_bindings.yaml> |
| `networkPolicy` | `object` | `networkPolicy` defines network policy settings for Network Observability components isolation. |
| `processor` | `object` | `processor` defines the settings of the component that receives the flows from the agent, enriches them, generates metrics, and forwards them to the Loki persistence layer and/or any available exporter. |
| `prometheus` | `object` | `prometheus` defines Prometheus settings, such as querier configuration used to fetch metrics from the Console plugin. |

Show more

#### [18.1.3. .spec.agent](#spec-agent) Copy linkLink copied to clipboard!

Description
:   Agent configuration for flows extraction.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ebpf` | `object` | `ebpf` describes the settings related to the eBPF-based flow reporter when `spec.agent.type` is set to `eBPF`. |
| `type` | `string` | `type` [deprecated (\*)] selects the flows tracing agent. Previously, this field allowed to select between `eBPF` or `IPFIX`. Only `eBPF` is allowed now, so this field is deprecated and is planned for removal in a future version of the API. |

Show more

#### [18.1.4. .spec.agent.ebpf](#spec-agent-ebpf) Copy linkLink copied to clipboard!

Description
:   `ebpf` describes the settings related to the eBPF-based flow reporter when `spec.agent.type` is set to `eBPF`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `advanced` | `object` | `advanced` allows setting some aspects of the internal configuration of the eBPF agent. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk. You can also override the default Linux capabilities from there. |
| `cacheActiveTimeout` | `string` | `cacheActiveTimeout` is the period during which the agent aggregates flows before sending. Increasing `cacheMaxFlows` and `cacheActiveTimeout` can decrease the network traffic overhead and the CPU load, however you can expect higher memory consumption and an increased latency in the flow collection. |
| `cacheMaxFlows` | `integer` | `cacheMaxFlows` is the maximum number of flows in an aggregate; when reached, the reporter sends the flows. Increasing `cacheMaxFlows` and `cacheActiveTimeout` can decrease the network traffic overhead and the CPU load, however you can expect higher memory consumption and an increased latency in the flow collection. |
| `excludeInterfaces` | `array (string)` | `excludeInterfaces` contains the interface names that are excluded from flow tracing. An entry enclosed by slashes, such as `/br-/`, is matched as a regular expression. Otherwise it is matched as a case-sensitive string. |
| `features` | `array (string)` | List of additional features to enable. They are all disabled by default. Enabling additional features might have performance impacts. Possible values are:  - `PacketDrop`: Enable the packets drop flows logging feature. This feature requires mounting the kernel debug filesystem, so the eBPF agent pods must run as privileged via `spec.agent.ebpf.privileged`.  - `DNSTracking`: Enable the DNS tracking feature.  - `FlowRTT`: Enable flow latency (sRTT) extraction in the eBPF agent from TCP traffic.  - `NetworkEvents`: Enable the network events monitoring feature, such as correlating flows and network policies. This feature requires mounting the kernel debug filesystem, so the eBPF agent pods must run as privileged via `spec.agent.ebpf.privileged`. It requires using the OVN-Kubernetes network plugin with the Observability feature. IMPORTANT: This feature is available as a Technology Preview.  - `PacketTranslation`: Enable enriching flows with packet translation information, such as Service NAT.  - `EbpfManager`: [Unsupported (\*)]. Use eBPF Manager to manage Network Observability eBPF programs. Pre-requisite: the eBPF Manager operator (or upstream bpfman operator) must be installed.  - `UDNMapping`: Enable interfaces mapping to User Defined Networks (UDN).  This feature requires mounting the kernel debug filesystem, so the eBPF agent pods must run as privileged via `spec.agent.ebpf.privileged`. It requires using the OVN-Kubernetes network plugin with the Observability feature.  - `IPSec`, to track flows between nodes with IPsec encryption.  - `TLSTracking`, to track TLS usage. |
| `flowFilter` | `object` | `flowFilter` defines the eBPF agent configuration regarding flow filtering. |
| `imagePullPolicy` | `string` | `imagePullPolicy` is the Kubernetes pull policy for the image defined above |
| `interfaces` | `array (string)` | `interfaces` contains the interface names from where flows are collected. If empty, the agent fetches all the interfaces in the system, excepting the ones listed in `excludeInterfaces`. An entry enclosed by slashes, such as `/br-/`, is matched as a regular expression. Otherwise it is matched as a case-sensitive string. |
| `kafkaBatchSize` | `integer` | `kafkaBatchSize` limits the maximum size of a request in bytes before being sent to a partition. Ignored when not using Kafka. Default: 1MB. |
| `logLevel` | `string` | `logLevel` defines the log level for the Network Observability eBPF Agent |
| `metrics` | `object` | `metrics` defines the eBPF agent configuration regarding metrics. |
| `privileged` | `boolean` | Privileged mode for the eBPF Agent container. When set to `true`, the agent is able to capture more traffic, including from secondary interfaces. When ignored or set to `false`, the operator sets granular capabilities (BPF, PERFMON, NET\_ADMIN) to the container. Some agent features require the privileged mode, such as packet drops tracking (see `features`) and SR-IOV support. |
| `resources` | `object` | `resources` are the compute resources required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `sampling` | `integer` | Sampling interval of the eBPF probe. 100 means one packet on 100 is sent. 0 or 1 means all packets are sampled. |

Show more

#### [18.1.5. .spec.agent.ebpf.advanced](#spec-agent-ebpf-advanced) Copy linkLink copied to clipboard!

Description
:   `advanced` allows setting some aspects of the internal configuration of the eBPF agent. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk. You can also override the default Linux capabilities from there.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `capOverride` | `array (string)` | Linux capabilities override, when not running as privileged. Default capabilities are BPF, PERFMON and NET\_ADMIN. |
| `env` | `object (string)` | `env` allows passing custom environment variables to underlying components. Useful for passing some very concrete performance-tuning options, such as `GOGC` and `GOMAXPROCS`, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `scheduling` | `object` | scheduling controls how the pods are scheduled on nodes. |

Show more

#### [18.1.6. .spec.agent.ebpf.advanced.scheduling](#spec-agent-ebpf-advanced-scheduling) Copy linkLink copied to clipboard!

Description
:   scheduling controls how the pods are scheduled on nodes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `affinity` | `object` | If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |
| `nodeSelector` | `object (string)` | `nodeSelector` allows scheduling of pods only onto nodes that have each of the specified labels. For documentation, refer to <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/>. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. For documentation, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption>. If not specified, default priority is used, or zero if there is no default. |
| `tolerations` | `array` | `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |

Show more

#### [18.1.7. .spec.agent.ebpf.advanced.scheduling.affinity](#spec-agent-ebpf-advanced-scheduling-affinity) Copy linkLink copied to clipboard!

Description
:   If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
:   `object`

#### [18.1.8. .spec.agent.ebpf.advanced.scheduling.tolerations](#spec-agent-ebpf-advanced-scheduling-tolerations) Copy linkLink copied to clipboard!

Description
:   `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
:   `array`

#### [18.1.9. .spec.agent.ebpf.flowFilter](#spec-agent-ebpf-flowfilter) Copy linkLink copied to clipboard!

Description
:   `flowFilter` defines the eBPF agent configuration regarding flow filtering.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `action` | `string` | `action` defines the action to perform on the flows that match the filter. The available options are `Accept`, which is the default, and `Reject`. |
| `cidr` | `string` | `cidr` defines the IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `destPorts` | `integer-or-string` | `destPorts` optionally defines the destination ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `destPorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `destPorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `direction` | `string` | `direction` optionally defines a direction to filter flows by. The available options are `Ingress` and `Egress`. |
| `enable` | `boolean` | Set `enable` to `true` to enable the eBPF flow filtering feature. |
| `icmpCode` | `integer` | `icmpCode`, for Internet Control Message Protocol (ICMP) traffic, optionally defines the ICMP code to filter flows by. |
| `icmpType` | `integer` | `icmpType`, for ICMP traffic, optionally defines the ICMP type to filter flows by. |
| `peerCIDR` | `string` | `peerCIDR` defines the Peer IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `peerIP` | `string` | `peerIP` optionally defines the remote IP address to filter flows by. Example: `10.10.10.10`. |
| `pktDrops` | `boolean` | `pktDrops` optionally filters only flows containing packet drops. |
| `ports` | `integer-or-string` | `ports` optionally defines the ports to filter flows by. It is used both for source and destination ports. To filter a single port, set a single port as an integer value. For example, `ports: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `ports: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `protocol` | `string` | `protocol` optionally defines a protocol to filter flows by. The available options are `TCP`, `UDP`, `ICMP`, `ICMPv6`, and `SCTP`. |
| `rules` | `array` | `rules` defines a list of filtering rules on the eBPF Agents. When filtering is enabled, by default, flows that don’t match any rule are rejected. To change the default, you can define a rule that accepts everything: `{ action: "Accept", cidr: "0.0.0.0/0" }`, and then refine with rejecting rules. |
| `sampling` | `integer` | `sampling` is the sampling interval for the matched packets, overriding the global sampling defined at `spec.agent.ebpf.sampling`. |
| `sourcePorts` | `integer-or-string` | `sourcePorts` optionally defines the source ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `sourcePorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `sourcePorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `tcpFlags` | `string` | `tcpFlags` optionally defines TCP flags to filter flows by. In addition to the standard flags (RFC-9293), you can also filter by one of the three following combinations: `SYN-ACK`, `FIN-ACK`, and `RST-ACK`. |

Show more

#### [18.1.10. .spec.agent.ebpf.flowFilter.rules](#spec-agent-ebpf-flowfilter-rules) Copy linkLink copied to clipboard!

Description
:   `rules` defines a list of filtering rules on the eBPF Agents. When filtering is enabled, by default, flows that don’t match any rule are rejected. To change the default, you can define a rule that accepts everything: `{ action: "Accept", cidr: "0.0.0.0/0" }`, and then refine with rejecting rules.

Type
:   `array`

#### [18.1.11. .spec.agent.ebpf.flowFilter.rules[]](#spec-agent-ebpf-flowfilter-rules-2) Copy linkLink copied to clipboard!

Description
:   `EBPFFlowFilterRule` defines the desired eBPF agent configuration regarding flow filtering rule.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `action` | `string` | `action` defines the action to perform on the flows that match the filter. The available options are `Accept`, which is the default, and `Reject`. |
| `cidr` | `string` | `cidr` defines the IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `destPorts` | `integer-or-string` | `destPorts` optionally defines the destination ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `destPorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `destPorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `direction` | `string` | `direction` optionally defines a direction to filter flows by. The available options are `Ingress` and `Egress`. |
| `icmpCode` | `integer` | `icmpCode`, for Internet Control Message Protocol (ICMP) traffic, optionally defines the ICMP code to filter flows by. |
| `icmpType` | `integer` | `icmpType`, for ICMP traffic, optionally defines the ICMP type to filter flows by. |
| `peerCIDR` | `string` | `peerCIDR` defines the Peer IP CIDR to filter flows by. Examples: `10.10.10.0/24` or `100:100:100:100::/64` |
| `peerIP` | `string` | `peerIP` optionally defines the remote IP address to filter flows by. Example: `10.10.10.10`. |
| `pktDrops` | `boolean` | `pktDrops` optionally filters only flows containing packet drops. |
| `ports` | `integer-or-string` | `ports` optionally defines the ports to filter flows by. It is used both for source and destination ports. To filter a single port, set a single port as an integer value. For example, `ports: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `ports: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `protocol` | `string` | `protocol` optionally defines a protocol to filter flows by. The available options are `TCP`, `UDP`, `ICMP`, `ICMPv6`, and `SCTP`. |
| `sampling` | `integer` | `sampling` is the sampling interval for the matched packets, overriding the global sampling defined at `spec.agent.ebpf.sampling`. |
| `sourcePorts` | `integer-or-string` | `sourcePorts` optionally defines the source ports to filter flows by. To filter a single port, set a single port as an integer value. For example, `sourcePorts: 80`. To filter a range of ports, use a "start-end" range in string format. For example, `sourcePorts: "80-100"`. To filter two ports, use a "port1,port2" in string format. For example, `ports: "80,100"`. |
| `tcpFlags` | `string` | `tcpFlags` optionally defines TCP flags to filter flows by. In addition to the standard flags (RFC-9293), you can also filter by one of the three following combinations: `SYN-ACK`, `FIN-ACK`, and `RST-ACK`. |

Show more

#### [18.1.12. .spec.agent.ebpf.metrics](#spec-agent-ebpf-metrics) Copy linkLink copied to clipboard!

Description
:   `metrics` defines the eBPF agent configuration regarding metrics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `disableAlerts` | `array (string)` | `disableAlerts` is a list of alerts that should be disabled. Possible values are:  `NetObservDroppedFlows`, which is triggered when the eBPF agent is missing packets or flows, such as when the BPF hashmap is busy or full, or the capacity limiter is being triggered. |
| `enable` | `boolean` | Set `enable` to `false` to disable eBPF agent metrics collection. It is enabled by default. |
| `server` | `object` | Metrics server endpoint configuration for the Prometheus scraper. |

Show more

#### [18.1.13. .spec.agent.ebpf.metrics.server](#spec-agent-ebpf-metrics-server) Copy linkLink copied to clipboard!

Description
:   Metrics server endpoint configuration for the Prometheus scraper.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | The metrics server HTTP port. |
| `tls` | `object` | TLS configuration. |

Show more

#### [18.1.14. .spec.agent.ebpf.metrics.server.tls](#spec-agent-ebpf-metrics-server-tls) Copy linkLink copied to clipboard!

Description
:   TLS configuration.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the provided certificate. If set to `true`, the `providedCaFile` field is ignored. |
| `provided` | `object` | TLS configuration when `type` is set to `Provided`. |
| `providedCaFile` | `object` | Reference to the CA file when `type` is set to `Provided`. |
| `type` | `string` | Select the type of TLS configuration:  - `Disabled` (default) to not configure TLS for the endpoint. - `Provided` to manually provide cert file and a key file. [Unsupported (\*)]. - `Auto` to use OpenShift Container Platform auto generated certificate using annotations. |

Show more

#### [18.1.15. .spec.agent.ebpf.metrics.server.tls.provided](#spec-agent-ebpf-metrics-server-tls-provided) Copy linkLink copied to clipboard!

Description
:   TLS configuration when `type` is set to `Provided`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.16. .spec.agent.ebpf.metrics.server.tls.providedCaFile](#spec-agent-ebpf-metrics-server-tls-providedcafile) Copy linkLink copied to clipboard!

Description
:   Reference to the CA file when `type` is set to `Provided`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.17. .spec.agent.ebpf.resources](#spec-agent-ebpf-resources) Copy linkLink copied to clipboard!

Description
:   `resources` are the compute resources required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [18.1.18. .spec.consolePlugin](#spec-consoleplugin) Copy linkLink copied to clipboard!

Description
:   `consolePlugin` defines the settings related to the OpenShift Container Platform Console plugin, when available.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `advanced` | `object` | `advanced` allows setting some aspects of the internal configuration of the console plugin. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk. |
| `autoscaler` | `object` | `autoscaler` [deprecated (\*)] spec of a horizontal pod autoscaler to set up for the plugin Deployment. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.consolePlugin.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2). |
| `enable` | `boolean` | Enables the console plugin deployment. |
| `imagePullPolicy` | `string` | `imagePullPolicy` is the Kubernetes pull policy for the image defined above. |
| `logLevel` | `string` | `logLevel` for the console plugin backend. |
| `portNaming` | `object` | `portNaming` defines the configuration of the port-to-service name translation. |
| `quickFilters` | `array` | `quickFilters` configures quick filter presets for the Console plugin. Filters for external traffic assume the subnet labels are configured to distinguish internal and external traffic (see `spec.processor.subnetLabels`). |
| `replicas` | `integer` | `replicas` defines the number of replicas (pods) to start. |
| `resources` | `object` | `resources`, in terms of compute resources, required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>. |
| `standalone` | `boolean` | Deploy as a standalone console, instead of a plugin of the OpenShift Container Platform Console. This is not recommended when using with OpenShift Container Platform, as it doesn’t provide an integrated experience. [Unsupported (\*)]. |
| `unmanagedReplicas` | `boolean` | If `unmanagedReplicas` is `true`, the operator will not reconcile `replicas`. This is useful when using a pod autoscaler. |

Show more

#### [18.1.19. .spec.consolePlugin.advanced](#spec-consoleplugin-advanced) Copy linkLink copied to clipboard!

Description
:   `advanced` allows setting some aspects of the internal configuration of the console plugin. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `args` | `array (string)` | `args` allows passing custom arguments to underlying components. Useful for overriding some parameters, such as a URL or a configuration path, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `env` | `object (string)` | `env` allows passing custom environment variables to underlying components. Useful for passing some very concrete performance-tuning options, such as `GOGC` and `GOMAXPROCS`, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `port` | `integer` | `port` is the plugin service port. Do not use 9002, which is reserved for metrics. |
| `register` | `boolean` | `register` allows, when set to `true`, to automatically register the provided console plugin with the OpenShift Container Platform Console operator. When set to `false`, you can still register it manually by editing console.operator.openshift.io/cluster with the following command: `oc patch console.operator.openshift.io cluster --type='json' -p '[{"op": "add", "path": "/spec/plugins/-", "value": "netobserv-plugin"}]'` |
| `scheduling` | `object` | `scheduling` controls how the pods are scheduled on nodes. |

Show more

#### [18.1.20. .spec.consolePlugin.advanced.scheduling](#spec-consoleplugin-advanced-scheduling) Copy linkLink copied to clipboard!

Description
:   `scheduling` controls how the pods are scheduled on nodes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `affinity` | `object` | If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |
| `nodeSelector` | `object (string)` | `nodeSelector` allows scheduling of pods only onto nodes that have each of the specified labels. For documentation, refer to <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/>. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. For documentation, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption>. If not specified, default priority is used, or zero if there is no default. |
| `tolerations` | `array` | `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |

Show more

#### [18.1.21. .spec.consolePlugin.advanced.scheduling.affinity](#spec-consoleplugin-advanced-scheduling-affinity) Copy linkLink copied to clipboard!

Description
:   If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
:   `object`

#### [18.1.22. .spec.consolePlugin.advanced.scheduling.tolerations](#spec-consoleplugin-advanced-scheduling-tolerations) Copy linkLink copied to clipboard!

Description
:   `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
:   `array`

#### [18.1.23. .spec.consolePlugin.autoscaler](#spec-consoleplugin-autoscaler) Copy linkLink copied to clipboard!

Description
:   `autoscaler` [deprecated (\*)] spec of a horizontal pod autoscaler to set up for the plugin Deployment. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.consolePlugin.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2).

Type
:   `object`

#### [18.1.24. .spec.consolePlugin.portNaming](#spec-consoleplugin-portnaming) Copy linkLink copied to clipboard!

Description
:   `portNaming` defines the configuration of the port-to-service name translation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `enable` | `boolean` | Enable the console plugin port-to-service name translation |
| `portNames` | `object (string)` | `portNames` defines additional port names to use in the console, for example, `portNames: {"3100": "loki"}`. |

Show more

#### [18.1.25. .spec.consolePlugin.quickFilters](#spec-consoleplugin-quickfilters) Copy linkLink copied to clipboard!

Description
:   `quickFilters` configures quick filter presets for the Console plugin. Filters for external traffic assume the subnet labels are configured to distinguish internal and external traffic (see `spec.processor.subnetLabels`).

Type
:   `array`

#### [18.1.26. .spec.consolePlugin.quickFilters[]](#spec-consoleplugin-quickfilters-2) Copy linkLink copied to clipboard!

Description
:   `QuickFilter` defines preset configuration for Console’s quick filters

Type
:   `object`

Required
:   * `filter`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `default` | `boolean` | `default` defines whether this filter should be active by default or not |
| `filter` | `object (string)` | `filter` is a set of keys and values to be set when this filter is selected. Each key can relate to a list of values using a coma-separated string, for example, `filter: {"src_namespace": "namespace1,namespace2"}`. |
| `name` | `string` | Name of the filter, that is displayed in the Console |

Show more

#### [18.1.27. .spec.consolePlugin.resources](#spec-consoleplugin-resources) Copy linkLink copied to clipboard!

Description
:   `resources`, in terms of compute resources, required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [18.1.28. .spec.execution](#spec-execution) Copy linkLink copied to clipboard!

Description
:   `execution` defines configuration related to the execution of the flow collection process.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mode` | `string` | `mode` is the flow collection process execution desired mode: `Running` or `OnHold`. When `OnHold`, the operator deletes all managed services and workloads, with the exception of the static console plugin, and the operator itself. It allows to use minimal cluster resources without losing configuration. |

Show more

#### [18.1.29. .spec.exporters](#spec-exporters) Copy linkLink copied to clipboard!

Description
:   `exporters` defines additional optional exporters for custom consumption or storage.

Type
:   `array`

#### [18.1.30. .spec.exporters[]](#spec-exporters-2) Copy linkLink copied to clipboard!

Description
:   `FlowCollectorExporter` defines an additional exporter to send enriched flows to.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ipfix` | `object` | IPFIX configuration, such as the IP address and port to send enriched IPFIX flows to. |
| `kafka` | `object` | Kafka configuration, such as the address and topic, to send enriched flows to. |
| `openTelemetry` | `object` | OpenTelemetry configuration, such as the IP address and port to send enriched logs or metrics to. |
| `type` | `string` | `type` selects the type of exporters. The available options are `Kafka`, `IPFIX`, and `OpenTelemetry`. |

Show more

#### [18.1.31. .spec.exporters[].ipfix](#spec-exporters-ipfix) Copy linkLink copied to clipboard!

Description
:   IPFIX configuration, such as the IP address and port to send enriched IPFIX flows to.

Type
:   `object`

Required
:   * `enterpriseID`
    * `targetHost`
    * `targetPort`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `enterpriseID` | `integer` | EnterpriseID, or Private Enterprise Number (PEN). To date, Network Observability does not own an assigned number, so it is left open for configuration. The PEN is needed to collect non standard data, such as Kubernetes names, RTT, etc. |
| `targetHost` | `string` | Address of the IPFIX external receiver. |
| `targetPort` | `integer` | Port for the IPFIX external receiver. |
| `transport` | `string` | Transport protocol (`TCP` or `UDP`) to be used for the IPFIX connection, defaults to `TCP`. |

Show more

#### [18.1.32. .spec.exporters[].kafka](#spec-exporters-kafka) Copy linkLink copied to clipboard!

Description
:   Kafka configuration, such as the address and topic, to send enriched flows to.

Type
:   `object`

Required
:   * `address`
    * `topic`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `address` | `string` | Address of the Kafka server |
| `compression` | `string` | Compression codec to use when producing messages to Kafka. Accepted values are: `none` (default), `gzip`, `snappy`, `lz4`, `zstd`. |
| `sasl` | `object` | SASL authentication configuration. [Unsupported (\*)]. |
| `tls` | `object` | TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards. When configuring TLS, the operator watches the certificate secret and copies it to both the netobserv and netobserv-privileged namespaces. In order to do so, you must grant it permissions to the `netobserv-secret-watcher` and `netobserv-secret-creator` roles in the corresponding namespaces. Refer to the Kafka configuration documentation for more information. |
| `topic` | `string` | Kafka topic to use. It must exist. Network Observability does not create it. |

Show more

#### [18.1.33. .spec.exporters[].kafka.sasl](#spec-exporters-kafka-sasl) Copy linkLink copied to clipboard!

Description
:   SASL authentication configuration. [Unsupported (\*)].

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clientIDReference` | `object` | Reference to the secret or config map containing the client ID |
| `clientSecretReference` | `object` | Reference to the secret or config map containing the client secret |
| `type` | `string` | Type of SASL authentication to use, or `Disabled` if SASL is not used |

Show more

#### [18.1.34. .spec.exporters[].kafka.sasl.clientIDReference](#spec-exporters-kafka-sasl-clientidreference) Copy linkLink copied to clipboard!

Description
:   Reference to the secret or config map containing the client ID

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.35. .spec.exporters[].kafka.sasl.clientSecretReference](#spec-exporters-kafka-sasl-clientsecretreference) Copy linkLink copied to clipboard!

Description
:   Reference to the secret or config map containing the client secret

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.36. .spec.exporters[].kafka.tls](#spec-exporters-kafka-tls) Copy linkLink copied to clipboard!

Description
:   TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards. When configuring TLS, the operator watches the certificate secret and copies it to both the netobserv and netobserv-privileged namespaces. In order to do so, you must grant it permissions to the `netobserv-secret-watcher` and `netobserv-secret-creator` roles in the corresponding namespaces. Refer to the Kafka configuration documentation for more information.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.37. .spec.exporters[].kafka.tls.caCert](#spec-exporters-kafka-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.38. .spec.exporters[].kafka.tls.userCert](#spec-exporters-kafka-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.39. .spec.exporters[].openTelemetry](#spec-exporters-opentelemetry) Copy linkLink copied to clipboard!

Description
:   OpenTelemetry configuration, such as the IP address and port to send enriched logs or metrics to.

Type
:   `object`

Required
:   * `targetHost`
    * `targetPort`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldsMapping` | `array` | Custom fields mapping to an OpenTelemetry conformant format. By default, Network Observability format proposal is used: <https://github.com/rhobs/observability-data-model/blob/main/network-observability.md#format-proposal> . As there is currently no accepted standard for L3 or L4 enriched network logs, you can freely override it with your own. |
| `headers` | `object (string)` | Headers to add to messages (optional) |
| `logs` | `object` | OpenTelemetry configuration for logs. |
| `metrics` | `object` | OpenTelemetry configuration for metrics. |
| `protocol` | `string` | Protocol of the OpenTelemetry connection. The available options are `http` and `grpc`. |
| `targetHost` | `string` | Address of the OpenTelemetry receiver. |
| `targetPort` | `integer` | Port for the OpenTelemetry receiver. |
| `tls` | `object` | TLS client configuration. |

Show more

#### [18.1.40. .spec.exporters[].openTelemetry.fieldsMapping](#spec-exporters-opentelemetry-fieldsmapping) Copy linkLink copied to clipboard!

Description
:   Custom fields mapping to an OpenTelemetry conformant format. By default, Network Observability format proposal is used: <https://github.com/rhobs/observability-data-model/blob/main/network-observability.md#format-proposal> . As there is currently no accepted standard for L3 or L4 enriched network logs, you can freely override it with your own.

Type
:   `array`

#### [18.1.41. .spec.exporters[].openTelemetry.fieldsMapping[]](#spec-exporters-opentelemetry-fieldsmapping-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `input` | `string` |  |
| `multiplier` | `integer` |  |
| `output` | `string` |  |

Show more

#### [18.1.42. .spec.exporters[].openTelemetry.logs](#spec-exporters-opentelemetry-logs) Copy linkLink copied to clipboard!

Description
:   OpenTelemetry configuration for logs.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `enable` | `boolean` | Set `enable` to `true` to send logs to an OpenTelemetry receiver. |

Show more

#### [18.1.43. .spec.exporters[].openTelemetry.metrics](#spec-exporters-opentelemetry-metrics) Copy linkLink copied to clipboard!

Description
:   OpenTelemetry configuration for metrics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `enable` | `boolean` | Set `enable` to `true` to send metrics to an OpenTelemetry receiver. |
| `pushTimeInterval` | `string` | Specify how often metrics are sent to a collector. |

Show more

#### [18.1.44. .spec.exporters[].openTelemetry.tls](#spec-exporters-opentelemetry-tls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.45. .spec.exporters[].openTelemetry.tls.caCert](#spec-exporters-opentelemetry-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.46. .spec.exporters[].openTelemetry.tls.userCert](#spec-exporters-opentelemetry-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.47. .spec.kafka](#spec-kafka) Copy linkLink copied to clipboard!

Description
:   Kafka configuration, allowing to use Kafka as a broker as part of the flow collection pipeline. Available when the `spec.deploymentModel` is `Kafka`.

Type
:   `object`

Required
:   * `address`
    * `topic`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `address` | `string` | Address of the Kafka server |
| `compression` | `string` | Compression codec to use when producing messages to Kafka. Accepted values are: `none` (default), `gzip`, `snappy`, `lz4`, `zstd`. |
| `sasl` | `object` | SASL authentication configuration. [Unsupported (\*)]. |
| `tls` | `object` | TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards. When configuring TLS, the operator watches the certificate secret and copies it to both the netobserv and netobserv-privileged namespaces. In order to do so, you must grant it permissions to the `netobserv-secret-watcher` and `netobserv-secret-creator` roles in the corresponding namespaces. Refer to the Kafka configuration documentation for more information. |
| `topic` | `string` | Kafka topic to use. It must exist. Network Observability does not create it. |

Show more

#### [18.1.48. .spec.kafka.sasl](#spec-kafka-sasl) Copy linkLink copied to clipboard!

Description
:   SASL authentication configuration. [Unsupported (\*)].

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clientIDReference` | `object` | Reference to the secret or config map containing the client ID |
| `clientSecretReference` | `object` | Reference to the secret or config map containing the client secret |
| `type` | `string` | Type of SASL authentication to use, or `Disabled` if SASL is not used |

Show more

#### [18.1.49. .spec.kafka.sasl.clientIDReference](#spec-kafka-sasl-clientidreference) Copy linkLink copied to clipboard!

Description
:   Reference to the secret or config map containing the client ID

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.50. .spec.kafka.sasl.clientSecretReference](#spec-kafka-sasl-clientsecretreference) Copy linkLink copied to clipboard!

Description
:   Reference to the secret or config map containing the client secret

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.51. .spec.kafka.tls](#spec-kafka-tls) Copy linkLink copied to clipboard!

Description
:   TLS and mTLS client configuration. When using TLS, verify that the address matches the Kafka port used for TLS, generally 9093. We recommend the use of mTLS for higher security standards. When configuring TLS, the operator watches the certificate secret and copies it to both the netobserv and netobserv-privileged namespaces. In order to do so, you must grant it permissions to the `netobserv-secret-watcher` and `netobserv-secret-creator` roles in the corresponding namespaces. Refer to the Kafka configuration documentation for more information.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.52. .spec.kafka.tls.caCert](#spec-kafka-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.53. .spec.kafka.tls.userCert](#spec-kafka-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.54. .spec.loki](#spec-loki) Copy linkLink copied to clipboard!

Description
:   `loki`, the flow store, client settings.

Type
:   `object`

Required
:   * `mode`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `advanced` | `object` | `advanced` allows setting some aspects of the internal configuration of the Loki clients. This section is aimed mostly for debugging and fine-grained performance optimizations. |
| `enable` | `boolean` | Set `enable` to `true` to store flows in Loki. The Console plugin can use either Loki or Prometheus as a data source for metrics (see also `spec.prometheus.querier`), or both. Not all queries are transposable from Loki to Prometheus. Hence, if Loki is disabled, some features of the plugin are disabled as well, such as getting per-pod information or viewing raw flows. If both Prometheus and Loki are enabled, Prometheus takes precedence and Loki is used as a fallback for queries that Prometheus cannot handle. If they are both disabled, the Console plugin is not deployed. |
| `lokiStack` | `object` | Loki configuration for `LokiStack` mode. This is useful for an easy Loki Operator configuration. It is ignored for other modes. |
| `manual` | `object` | Loki configuration for `Manual` mode. This is the most flexible configuration. It is ignored for other modes. |
| `microservices` | `object` | Loki configuration for `Microservices` mode. Use this option when Loki is installed using the microservices deployment mode (<https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#microservices-mode>). It is ignored for other modes. |
| `mode` | `string` | `mode` must be set according to the installation mode of Loki:  - Use `LokiStack` when Loki is managed using the Loki Operator  - Use `Monolithic` when Loki is installed as a monolithic workload  - Use `Microservices` when Loki is installed as microservices, but without Loki Operator  - Use `Manual` if none of the options above match your setup |
| `monolithic` | `object` | Loki configuration for `Monolithic` mode. Use this option when Loki is installed using the monolithic deployment mode (<https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#monolithic-mode>). It is ignored for other modes. |
| `readTimeout` | `string` | `readTimeout` is the maximum console plugin loki query total time limit. A timeout of zero means no timeout. |
| `writeBatchSize` | `integer` | `writeBatchSize` is the maximum batch size (in bytes) of Loki logs to accumulate before sending. |
| `writeBatchWait` | `string` | `writeBatchWait` is the maximum time to wait before sending a Loki batch. |
| `writeTimeout` | `string` | `writeTimeout` is the maximum Loki time connection / request limit. A timeout of zero means no timeout. |

Show more

#### [18.1.55. .spec.loki.advanced](#spec-loki-advanced) Copy linkLink copied to clipboard!

Description
:   `advanced` allows setting some aspects of the internal configuration of the Loki clients. This section is aimed mostly for debugging and fine-grained performance optimizations.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `excludeLabels` | `array (string)` | `excludeLabels` is a list of fields to be excluded from the list of Loki labels. [Unsupported (\*)]. |
| `staticLabels` | `object (string)` | `staticLabels` is a map of common labels to set on each flow in Loki storage. |
| `writeMaxBackoff` | `string` | `writeMaxBackoff` is the maximum backoff time for Loki client connection between retries. |
| `writeMaxRetries` | `integer` | `writeMaxRetries` is the maximum number of retries for Loki client connections. |
| `writeMinBackoff` | `string` | `writeMinBackoff` is the initial backoff time for Loki client connection between retries. |

Show more

#### [18.1.56. .spec.loki.lokiStack](#spec-loki-lokistack) Copy linkLink copied to clipboard!

Description
:   Loki configuration for `LokiStack` mode. This is useful for an easy Loki Operator configuration. It is ignored for other modes.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of an existing LokiStack resource to use. |
| `namespace` | `string` | Namespace where this `LokiStack` resource is located. If omitted, it is assumed to be the same as `spec.namespace`. When configuring a different namespace, the operator watches certificate secret and copies it to the netobserv main namespaces. In order to do so, you must grant it permissions to the `netobserv-secret-watcher` and `netobserv-secret-creator` roles in the corresponding namespaces. Refer to the Loki configuration documentation for more information. |

Show more

#### [18.1.57. .spec.loki.manual](#spec-loki-manual) Copy linkLink copied to clipboard!

Description
:   Loki configuration for `Manual` mode. This is the most flexible configuration. It is ignored for other modes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `authToken` | `string` | `authToken` describes the way to get a token to authenticate to Loki.  - `Disabled` does not send any token with the request.  - `Forward` forwards the user token for authorization.  - `Host` [deprecated (\*)] - uses the local pod service account to authenticate to Loki.  When using the Loki Operator, this must be set to `Forward`. |
| `ingesterUrl` | `string` | `ingesterUrl` is the address of an existing Loki ingester service to push the flows to. When using the Loki Operator, set it to the Loki gateway service with the `network` tenant set in path, for example <https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network>. |
| `querierUrl` | `string` | `querierUrl` specifies the address of the Loki querier service. When using the Loki Operator, set it to the Loki gateway service with the `network` tenant set in path, for example <https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network>. |
| `statusTls` | `object` | TLS client configuration for Loki status URL. |
| `statusUrl` | `string` | `statusUrl` specifies the address of the Loki `/ready`, `/metrics` and `/config` endpoints, in case it is different from the Loki querier URL. If empty, the `querierUrl` value is used. This is useful to show error messages and some context in the frontend. When using the Loki Operator, set it to the Loki HTTP query frontend service, for example <https://loki-query-frontend-http.netobserv.svc:3100/>. `statusTLS` configuration is used when `statusUrl` is set. |
| `tenantID` | `string` | `tenantID` is the Loki `X-Scope-OrgID` that identifies the tenant for each request. When using the Loki Operator, set it to `network`, which corresponds to a special tenant mode. |
| `tls` | `object` | TLS client configuration for Loki URL. |

Show more

#### [18.1.58. .spec.loki.manual.statusTls](#spec-loki-manual-statustls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration for Loki status URL.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.59. .spec.loki.manual.statusTls.caCert](#spec-loki-manual-statustls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.60. .spec.loki.manual.statusTls.userCert](#spec-loki-manual-statustls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.61. .spec.loki.manual.tls](#spec-loki-manual-tls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration for Loki URL.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.62. .spec.loki.manual.tls.caCert](#spec-loki-manual-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.63. .spec.loki.manual.tls.userCert](#spec-loki-manual-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.64. .spec.loki.microservices](#spec-loki-microservices) Copy linkLink copied to clipboard!

Description
:   Loki configuration for `Microservices` mode. Use this option when Loki is installed using the microservices deployment mode (<https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#microservices-mode>). It is ignored for other modes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ingesterUrl` | `string` | `ingesterUrl` is the address of an existing Loki ingester service to push the flows to. |
| `querierUrl` | `string` | `querierURL` specifies the address of the Loki querier service. |
| `tenantID` | `string` | `tenantID` is the Loki `X-Scope-OrgID` header that identifies the tenant for each request. |
| `tls` | `object` | TLS client configuration for Loki URL. |

Show more

#### [18.1.65. .spec.loki.microservices.tls](#spec-loki-microservices-tls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration for Loki URL.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.66. .spec.loki.microservices.tls.caCert](#spec-loki-microservices-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.67. .spec.loki.microservices.tls.userCert](#spec-loki-microservices-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.68. .spec.loki.monolithic](#spec-loki-monolithic) Copy linkLink copied to clipboard!

Description
:   Loki configuration for `Monolithic` mode. Use this option when Loki is installed using the monolithic deployment mode (<https://grafana.com/docs/loki/latest/fundamentals/architecture/deployment-modes/#monolithic-mode>). It is ignored for other modes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `installDemoLoki` | `boolean` | Set `installDemoLoki` to `true` to automatically create Loki deployment, service and storage. This is useful for development and demo purposes. Do not use it in production. [Unsupported (\*)]. |
| `tenantID` | `string` | `tenantID` is the Loki `X-Scope-OrgID` header that identifies the tenant for each request. |
| `tls` | `object` | TLS client configuration for Loki URL. |
| `url` | `string` | `url` is the unique address of an existing Loki service that points to both the ingester and the querier. |

Show more

#### [18.1.69. .spec.loki.monolithic.tls](#spec-loki-monolithic-tls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration for Loki URL.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.70. .spec.loki.monolithic.tls.caCert](#spec-loki-monolithic-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.71. .spec.loki.monolithic.tls.userCert](#spec-loki-monolithic-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.72. .spec.networkPolicy](#spec-networkpolicy) Copy linkLink copied to clipboard!

Description
:   `networkPolicy` defines network policy settings for Network Observability components isolation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalNamespaces` | `array (string)` | `additionalNamespaces` contains additional namespaces allowed to connect to the Network Observability namespace. It provides flexibility in the network policy configuration, but if you need a more specific configuration, you can disable it and install your own instead. |
| `enable` | `boolean` | Deploys network policies on the namespaces used by Network Observability (main and privileged). These network policies better isolate the Network Observability components to prevent undesired connections from and to them. Because it cannot be tested with all CNIs, this option is only enabled by default when Network Observability runs in a known supported environment, and it is disabled by default otherwise. When disabled, it is highly recommended to create network policies manually, to prevent undesired accesses. More information: <https://github.com/netobserv/netobserv-operator/blob/main/docs/NetworkPolicy.md>. |

Show more

#### [18.1.73. .spec.processor](#spec-processor) Copy linkLink copied to clipboard!

Description
:   `processor` defines the settings of the component that receives the flows from the agent, enriches them, generates metrics, and forwards them to the Loki persistence layer and/or any available exporter.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `addZone` | `boolean` | `addZone` allows availability zone awareness by labeling flows with their source and destination zones. This feature requires the "topology.kubernetes.io/zone" label to be set on nodes. |
| `advanced` | `object` | `advanced` allows setting some aspects of the internal configuration of the flow processor. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk. |
| `clusterName` | `string` | `clusterName` is the name of the cluster to appear in the flows data. This is useful in a multi-cluster context. When using OpenShift Container Platform, leave empty to make it automatically determined. |
| `consumerReplicas` | `integer` | `consumerReplicas` defines the number of replicas (pods) to start for `flowlogs-pipeline`, default is 3. This setting is ignored when `spec.deploymentModel` is `Direct` or when `spec.processor.unmanagedReplicas` is `true`. |
| `deduper` | `object` | `deduper` allows you to sample or drop flows identified as duplicates, in order to save on resource usage. |
| `filters` | `array` | `filters` lets you define custom filters to limit the amount of generated flows. These filters provide more flexibility than the eBPF Agent filters (in `spec.agent.ebpf.flowFilter`), such as allowing to filter by Kubernetes namespace, but with a lesser improvement in performance. |
| `imagePullPolicy` | `string` | `imagePullPolicy` is the Kubernetes pull policy for the image defined above |
| `kafkaConsumerAutoscaler` | `object` | `kafkaConsumerAutoscaler` [deprecated (\*)] is the spec of a horizontal pod autoscaler to set up for `flowlogs-pipeline-transformer`, which consumes Kafka messages. This setting is ignored when Kafka is disabled. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.processor.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2). |
| `kafkaConsumerBatchSize` | `integer` | `kafkaConsumerBatchSize` indicates to the broker the maximum batch size, in bytes, that the consumer accepts. Ignored when not using Kafka. Default: 10MB. |
| `kafkaConsumerQueueCapacity` | `integer` | `kafkaConsumerQueueCapacity` defines the capacity of the internal message queue used in the Kafka consumer client. Ignored when not using Kafka. |
| `kafkaConsumerReplicas` | `integer` | `kafkaConsumerReplicas` [deprecated (\*)] defines the number of replicas (pods) to start for `flowlogs-pipeline-transformer`, which consumes Kafka messages. This setting is ignored when Kafka is disabled. Deprecation notice: use `spec.processor.consumerReplicas` instead. |
| `logLevel` | `string` | `logLevel` of the processor runtime |
| `logTypes` | `string` | `logTypes` defines the desired record types to generate. Possible values are:  - `Flows` to export regular network flows. This is the default.  - `Conversations` to generate events for started conversations, ended conversations as well as periodic "tick" updates. Note that in this mode, Prometheus metrics are not accurate on long-standing conversations.  - `EndedConversations` to generate only ended conversations events. Note that in this mode, Prometheus metrics are not accurate on long-standing conversations.  - `All` to generate both network flows and all conversations events. It is not recommended due to the impact on resources footprint. |
| `metrics` | `object` | `Metrics` define the processor configuration regarding metrics |
| `multiClusterDeployment` | `boolean` | Set `multiClusterDeployment` to `true` to enable multi clusters feature. This adds `clusterName` label to flows data |
| `resources` | `object` | `resources` are the compute resources required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `service` | `object` | Service configuration, only used when `spec.deploymentModel` is `Service`. |
| `slicesConfig` | `object` | Global configuration managing FlowCollectorSlices custom resources. |
| `subnetLabels` | `object` | `subnetLabels` allows to define custom labels on subnets and IPs or to enable automatic labeling of recognized subnets in OpenShift Container Platform, which is used to identify cluster external traffic. When a subnet matches the source or destination IP of a flow, a corresponding field is added: `SrcSubnetLabel` or `DstSubnetLabel`. |
| `unmanagedReplicas` | `boolean` | If `unmanagedReplicas` is `true`, the operator will not reconcile `consumerReplicas`. This is useful when using a pod autoscaler. |

Show more

#### [18.1.74. .spec.processor.advanced](#spec-processor-advanced) Copy linkLink copied to clipboard!

Description
:   `advanced` allows setting some aspects of the internal configuration of the flow processor. This section is aimed mostly for debugging and fine-grained performance optimizations, such as `GOGC` and `GOMAXPROCS` environment variables. Set these values at your own risk.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conversationEndTimeout` | `string` | `conversationEndTimeout` is the time to wait after a network flow is received, to consider the conversation ended. This delay is ignored when a FIN packet is collected for TCP flows (see `conversationTerminatingTimeout` instead). |
| `conversationHeartbeatInterval` | `string` | `conversationHeartbeatInterval` is the time to wait between "tick" events of a conversation |
| `conversationTerminatingTimeout` | `string` | `conversationTerminatingTimeout` is the time to wait from detected FIN flag to end a conversation. Only relevant for TCP flows. |
| `dropUnusedFields` | `boolean` | `dropUnusedFields` [deprecated (\*)] this setting is not used anymore. |
| `enableKubeProbes` | `boolean` | `enableKubeProbes` is a flag to enable or disable Kubernetes liveness and readiness probes |
| `env` | `object (string)` | `env` allows passing custom environment variables to underlying components. Useful for passing some very concrete performance-tuning options, such as `GOGC` and `GOMAXPROCS`, that should not be publicly exposed as part of the FlowCollector descriptor, as they are only useful in edge debug or support scenarios. |
| `healthPort` | `integer` | `healthPort` is a collector HTTP port in the Pod that exposes the health check API |
| `port` | `integer` | Port of the flow collector (host port). By convention, some values are forbidden. It must be greater than 1024 and different from 4500, 4789 and 6081. |
| `profilePort` | `integer` | `profilePort` allows setting up a Go pprof profiler listening to this port |
| `scheduling` | `object` | scheduling controls how the pods are scheduled on nodes. |
| `secondaryNetworks` | `array` | Defines secondary networks to be checked for resources identification. To guarantee a correct identification, indexed values must form an unique identifier across the cluster. If the same index is used by several resources, those resources might be incorrectly labeled. If not provided and `spec.agent.ebpf.privileged` is `true`, secondary networks are detected automatically. |

Show more

#### [18.1.75. .spec.processor.advanced.scheduling](#spec-processor-advanced-scheduling) Copy linkLink copied to clipboard!

Description
:   scheduling controls how the pods are scheduled on nodes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `affinity` | `object` | If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |
| `nodeSelector` | `object (string)` | `nodeSelector` allows scheduling of pods only onto nodes that have each of the specified labels. For documentation, refer to <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/>. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. For documentation, refer to <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption>. If not specified, default priority is used, or zero if there is no default. |
| `tolerations` | `array` | `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>. |

Show more

#### [18.1.76. .spec.processor.advanced.scheduling.affinity](#spec-processor-advanced-scheduling-affinity) Copy linkLink copied to clipboard!

Description
:   If specified, the pod’s scheduling constraints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
:   `object`

#### [18.1.77. .spec.processor.advanced.scheduling.tolerations](#spec-processor-advanced-scheduling-tolerations) Copy linkLink copied to clipboard!

Description
:   `tolerations` is a list of tolerations that allow the pod to schedule onto nodes with matching taints. For documentation, refer to <https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling>.

Type
:   `array`

#### [18.1.78. .spec.processor.advanced.secondaryNetworks](#spec-processor-advanced-secondarynetworks) Copy linkLink copied to clipboard!

Description
:   Defines secondary networks to be checked for resources identification. To guarantee a correct identification, indexed values must form an unique identifier across the cluster. If the same index is used by several resources, those resources might be incorrectly labeled.

Type
:   `array`

#### [18.1.79. .spec.processor.advanced.secondaryNetworks[]](#spec-processor-advanced-secondarynetworks-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `index`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `index` | `array (string)` | `index` is a list of fields to use for indexing the pods. They should form a unique Pod identifier across the cluster. Can be any of: `MAC`, `IP`, `Interface`. Fields absent from the 'k8s.v1.cni.cncf.io/network-status' annotation must not be added to the index. |
| `name` | `string` | Deprecated: `name` is unused. |

Show more

#### [18.1.80. .spec.processor.deduper](#spec-processor-deduper) Copy linkLink copied to clipboard!

Description
:   `deduper` allows you to sample or drop flows identified as duplicates, in order to save on resource usage.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mode` | `string` | Set the Processor de-duplication mode. It comes in addition to the Agent-based deduplication, since the Agent cannot de-duplicate same flows reported from different nodes.  - Use `Drop` to drop every flow considered as duplicates, allowing saving more on resource usage but potentially losing some information such as the network interfaces used from peer, or network events.  - Use `Sample` to randomly keep only one flow on 50, which is the default, among the ones considered as duplicates. This is a compromise between dropping every duplicate or keeping every duplicate. This sampling action comes in addition to the Agent-based sampling. If both Agent and Processor sampling values are `50`, the combined sampling is 1:2500.  - Use `Disabled` to turn off Processor-based de-duplication. |
| `sampling` | `integer` | `sampling` is the sampling interval when deduper `mode` is `Sample`. For example, a value of `50` means that 1 flow in 50 is sampled. |

Show more

#### [18.1.81. .spec.processor.filters](#spec-processor-filters) Copy linkLink copied to clipboard!

Description
:   `filters` lets you define custom filters to limit the amount of generated flows. These filters provide more flexibility than the eBPF Agent filters (in `spec.agent.ebpf.flowFilter`), such as allowing to filter by Kubernetes namespace, but with a lesser improvement in performance.

Type
:   `array`

#### [18.1.82. .spec.processor.filters[]](#spec-processor-filters-2) Copy linkLink copied to clipboard!

Description
:   `FLPFilterSet` defines the desired configuration for FLP-based filtering satisfying all conditions.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `outputTarget` | `string` | If specified, these filters target a single output: `Loki`, `Metrics` or `Exporters`. By default, all outputs are targeted. |
| `query` | `string` | A query that selects the network flows to keep. More information about this query language in <https://github.com/netobserv/flowlogs-pipeline/blob/main/docs/filtering.md>. |
| `sampling` | `integer` | `sampling` is an optional sampling interval to apply to this filter. For example, a value of `50` means that 1 matching flow in 50 is sampled. |

Show more

#### [18.1.83. .spec.processor.kafkaConsumerAutoscaler](#spec-processor-kafkaconsumerautoscaler) Copy linkLink copied to clipboard!

Description
:   `kafkaConsumerAutoscaler` [deprecated (\*)] is the spec of a horizontal pod autoscaler to set up for `flowlogs-pipeline-transformer`, which consumes Kafka messages. This setting is ignored when Kafka is disabled. Deprecation notice: managed autoscaler will be removed in a future version. You might configure instead an autoscaler of your choice, and set `spec.processor.unmanagedReplicas` to `true`. Refer to HorizontalPodAutoscaler documentation (autoscaling/v2).

Type
:   `object`

#### [18.1.84. .spec.processor.metrics](#spec-processor-metrics) Copy linkLink copied to clipboard!

Description
:   `Metrics` define the processor configuration regarding metrics

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalIncludeList` | `array (string)` | `additionalIncludeList` is a list of metric names to include in addition to the default metrics. Unlike `includeList`, this appends to the default list rather than replacing it. This field is mutually exclusive with `includeList`. If `includeList` is set, `additionalIncludeList` is ignored. The names correspond to the names in Prometheus without the prefix. For example, `namespace_egress_packets_total` shows up as `netobserv_namespace_egress_packets_total` in Prometheus. Note that the more metrics you add, the bigger is the impact on Prometheus workload resources. More information, with full list of available metrics: <https://github.com/netobserv/network-observability-operator/blob/main/docs/Metrics.md> |
| `disableAlerts` | `array (string)` | `disableAlerts` is a list of alert groups that should be disabled from the default set of alerts. Possible values are: `NetObservNoFlows`, `NetObservLokiError`, `PacketDropsByKernel`, `PacketDropsByDevice`, `IPsecErrors`, `NetpolDenied`, `LatencyHighTrend`, `DNSErrors`, `DNSNxDomain`, `ExternalEgressHighTrend`, `ExternalIngressHighTrend`, `Ingress5xxErrors`, `IngressHTTPLatencyTrend`. More information on alerts: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md> |
| `healthRules` | `array` | `healthRules` is a list of health rules to be created for Prometheus, organized by templates and variants. Each health rule can be configured to generate either alerts or recording rules based on the mode field. More information on health rules: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md> |
| `includeList` | `array (string)` | `includeList` is a list of metric names to specify which ones to generate. The names correspond to the names in Prometheus without the prefix. For example, `namespace_egress_packets_total` shows up as `netobserv_namespace_egress_packets_total` in Prometheus. Note that the more metrics you add, the bigger is the impact on Prometheus workload resources. Metrics enabled by default are: `namespace_flows_total`, `node_ingress_bytes_total`, `node_egress_bytes_total`, `workload_ingress_bytes_total`, `workload_egress_bytes_total`, `namespace_drop_packets_total` (when `PacketDrop` feature is enabled), `namespace_rtt_seconds` (when `FlowRTT` feature is enabled), `namespace_dns_latency_seconds` (when `DNSTracking` feature is enabled), `namespace_network_policy_events_total` (when `NetworkEvents` feature is enabled). More information, with full list of available metrics: <https://github.com/netobserv/network-observability-operator/blob/main/docs/Metrics.md> |
| `server` | `object` | Metrics server endpoint configuration for Prometheus scraper |

Show more

#### [18.1.85. .spec.processor.metrics.healthRules](#spec-processor-metrics-healthrules) Copy linkLink copied to clipboard!

Description
:   `healthRules` is a list of health rules to be created for Prometheus, organized by templates and variants. Each health rule can be configured to generate either alerts or recording rules based on the mode field. More information on health rules: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md>

Type
:   `array`

#### [18.1.86. .spec.processor.metrics.healthRules[]](#spec-processor-metrics-healthrules-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `template`
    * `variants`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mode` | `string` | Mode defines whether this health rule should be generated as an alert or a recording rule. Possible values are: `Alert` (default), `Recording`. Recording rules violations are visible in the Network Health dashboard without generating any Prometheus alert. This provides an alternative way of getting Health information for SRE and cluster admins who might find many new alerts burdensome. |
| `template` | `string` | Health rule template name. Possible values are: `PacketDropsByKernel`, `PacketDropsByDevice`, `IPsecErrors`, `NetpolDenied`, `LatencyHighTrend`, `DNSErrors`, `DNSNxDomain`, `ExternalEgressHighTrend`, `ExternalIngressHighTrend`, `Ingress5xxErrors`, `IngressHTTPLatencyTrend`. Note: `NetObservNoFlows` and `NetObservLokiError` are alert-only and cannot be used as health rules. More information on health rules: <https://github.com/netobserv/network-observability-operator/blob/main/docs/HealthRules.md> |
| `variants` | `array` | A list of variants for this template |

Show more

#### [18.1.87. .spec.processor.metrics.healthRules[].variants](#spec-processor-metrics-healthrules-variants) Copy linkLink copied to clipboard!

Description
:   A list of variants for this template

Type
:   `array`

#### [18.1.88. .spec.processor.metrics.healthRules[].variants[]](#spec-processor-metrics-healthrules-variants-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `thresholds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `groupBy` | `string` | Optional grouping criteria, possible values are: `Node`, `Namespace`, `Workload`. |
| `lowVolumeThreshold` | `string` | The low volume threshold allows to ignore metrics with a too low volume of traffic, in order to improve signal-to-noise. It is provided as an absolute rate (bytes per second or packets per second, depending on the context). When provided, it must be parsable as a float. |
| `mode` | `string` | Mode overrides the health rule mode for this specific variant. If not specified, inherits from the parent health rule’s mode. Possible values are: `Alert`, `Recording`. |
| `thresholds` | `object` | Thresholds of the health rule per severity. They are expressed as a percentage of errors above which the alert is triggered. They must be parsable as floats. Required for both alert and recording modes |
| `trendDuration` | `string` | For trending health rules, the duration interval for baseline comparison. For example, "2h" means comparing against a 2-hours average. Defaults to 2h. |
| `trendOffset` | `string` | For trending health rules, the time offset for baseline comparison. For example, "1d" means comparing against yesterday. Defaults to 1d. |

Show more

#### [18.1.89. .spec.processor.metrics.healthRules[].variants[].thresholds](#spec-processor-metrics-healthrules-variants-thresholds) Copy linkLink copied to clipboard!

Description
:   Thresholds of the health rule per severity. They are expressed as a percentage of errors above which the alert is triggered. They must be parsable as floats. Required for both alert and recording modes

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `critical` | `string` | Threshold for severity `critical`. Leave empty to not generate a Critical alert. |
| `info` | `string` | Threshold for severity `info`. Leave empty to not generate an Info alert. |
| `warning` | `string` | Threshold for severity `warning`. Leave empty to not generate a Warning alert. |

Show more

#### [18.1.90. .spec.processor.metrics.server](#spec-processor-metrics-server) Copy linkLink copied to clipboard!

Description
:   Metrics server endpoint configuration for Prometheus scraper

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | The metrics server HTTP port. |
| `tls` | `object` | TLS configuration. |

Show more

#### [18.1.91. .spec.processor.metrics.server.tls](#spec-processor-metrics-server-tls) Copy linkLink copied to clipboard!

Description
:   TLS configuration.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the provided certificate. If set to `true`, the `providedCaFile` field is ignored. |
| `provided` | `object` | TLS configuration when `type` is set to `Provided`. |
| `providedCaFile` | `object` | Reference to the CA file when `type` is set to `Provided`. |
| `type` | `string` | Select the type of TLS configuration:  - `Disabled` (default) to not configure TLS for the endpoint. - `Provided` to manually provide cert file and a key file. [Unsupported (\*)]. - `Auto` to use OpenShift Container Platform auto generated certificate using annotations. |

Show more

#### [18.1.92. .spec.processor.metrics.server.tls.provided](#spec-processor-metrics-server-tls-provided) Copy linkLink copied to clipboard!

Description
:   TLS configuration when `type` is set to `Provided`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.93. .spec.processor.metrics.server.tls.providedCaFile](#spec-processor-metrics-server-tls-providedcafile) Copy linkLink copied to clipboard!

Description
:   Reference to the CA file when `type` is set to `Provided`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.94. .spec.processor.resources](#spec-processor-resources) Copy linkLink copied to clipboard!

Description
:   `resources` are the compute resources required by this container. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [18.1.95. .spec.processor.service](#spec-processor-service) Copy linkLink copied to clipboard!

Description
:   Service configuration, only used when `spec.deploymentModel` is `Service`.

Type
:   `object`

Required
:   * `tlsType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `providedCertificates` | `object` | TLS or mTLS configuration when `type` is set to `Provided`. |
| `tlsType` | `string` | Select the type of TLS configuration:  - `Disabled` to not configure TLS for the endpoint. Disabling TLS results in a less secure deployment model.  - `Provided` to manually provide the key and certificate references.  - `Auto` (default) to enable automatically based on the running environment.  - `Auto-mTLS` to preconfigure mTLS. [Unsupported (\*)].  See also: <https://github.com/netobserv/netobserv-operator/blob/main/docs/TLS.md>. |

Show more

#### [18.1.96. .spec.processor.service.providedCertificates](#spec-processor-service-providedcertificates) Copy linkLink copied to clipboard!

Description
:   TLS or mTLS configuration when `type` is set to `Provided`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caFile` | `object` | Reference to the CA file. |
| `clientCert` | `object` | TLS client certificate reference, used for mTLS. Leave unset for simple TLS. |
| `serverCert` | `object` | TLS server certificate reference. |

Show more

#### [18.1.97. .spec.processor.service.providedCertificates.caFile](#spec-processor-service-providedcertificates-cafile) Copy linkLink copied to clipboard!

Description
:   Reference to the CA file.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `file` | `string` | File name within the config map or secret. |
| `name` | `string` | Name of the config map or secret containing the file. |
| `namespace` | `string` | Namespace of the config map or secret containing the file. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the file reference: `configmap` or `secret`. |

Show more

#### [18.1.98. .spec.processor.service.providedCertificates.clientCert](#spec-processor-service-providedcertificates-clientcert) Copy linkLink copied to clipboard!

Description
:   TLS client certificate reference, used for mTLS. Leave unset for simple TLS.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.99. .spec.processor.service.providedCertificates.serverCert](#spec-processor-service-providedcertificates-servercert) Copy linkLink copied to clipboard!

Description
:   TLS server certificate reference.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.100. .spec.processor.slicesConfig](#spec-processor-slicesconfig) Copy linkLink copied to clipboard!

Description
:   Global configuration managing FlowCollectorSlices custom resources.

Type
:   `object`

Required
:   * `enable`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `collectionMode` | `string` | `collectionMode` determines how the FlowCollectorSlice custom resources impacts the flow collection process:  - When set to `AlwaysCollect`, all flows are collected regardless of the presence of FlowCollectorSlice.  - When set to `AllowList`, only the flows related to namespaces where a FlowCollectorSlice resource is present, or configured via the global `namespacesAllowList`, are collected. |
| `enable` | `boolean` | `enable` determines if the FlowCollectorSlice feature is enabled. If not, all resources of kind FlowCollectorSlice are simply ignored. |
| `namespacesAllowList` | `array (string)` | `namespacesAllowList` is a list of namespaces for which flows are always collected, regardless of the presence of FlowCollectorSlice in those namespaces. An entry enclosed by slashes, such as `/openshift-.*/`, is matched as a regular expression. This setting is ignored if `collectionMode` is different from `AllowList`. |

Show more

#### [18.1.101. .spec.processor.subnetLabels](#spec-processor-subnetlabels) Copy linkLink copied to clipboard!

Description
:   `subnetLabels` allows to define custom labels on subnets and IPs or to enable automatic labeling of recognized subnets in OpenShift Container Platform, which is used to identify cluster external traffic. When a subnet matches the source or destination IP of a flow, a corresponding field is added: `SrcSubnetLabel` or `DstSubnetLabel`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `customLabels` | `array` | `customLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided.  If `openShiftAutoDetect` is disabled or you are not using OpenShift Container Platform, it is recommended to manually configure labels for the cluster subnets, to distinguish internal traffic from external traffic.  If `openShiftAutoDetect` is enabled, `customLabels` overrides the detected subnets when they overlap. |
| `openShiftAutoDetect` | `boolean` | `openShiftAutoDetect` allows, when set to `true`, to detect automatically the machines, pods and services subnets based on the OpenShift Container Platform install configuration and the Cluster Network Operator configuration. Indirectly, this is a way to accurately detect external traffic: flows that are not labeled for those subnets are external to the cluster. Enabled by default on OpenShift Container Platform. |

Show more

#### [18.1.102. .spec.processor.subnetLabels.customLabels](#spec-processor-subnetlabels-customlabels) Copy linkLink copied to clipboard!

Description
:   `customLabels` allows you to customize subnets and IPs labeling, such as to identify cluster external workloads or web services. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided.

    If `openShiftAutoDetect` is disabled or you are not using OpenShift Container Platform, it is recommended to manually configure labels for the cluster subnets, to distinguish internal traffic from external traffic.

    If `openShiftAutoDetect` is enabled, `customLabels` overrides the detected subnets when they overlap.

Type
:   `array`

#### [18.1.103. .spec.processor.subnetLabels.customLabels[]](#spec-processor-subnetlabels-customlabels-2) Copy linkLink copied to clipboard!

Description
:   SubnetLabel allows to label subnets and IPs, such as to identify cluster-external workloads or web services.

Type
:   `object`

Required
:   * `cidrs`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cidrs` | `array (string)` | List of CIDRs, such as `["1.2.3.4/32"]`. |
| `name` | `string` | Label name, used to flag matching flows. External subnets must be labeled with the prefix `EXT:`, or not labeled at all, in order to work with default quick filters and some metrics examples provided. |

Show more

#### [18.1.104. .spec.prometheus](#spec-prometheus) Copy linkLink copied to clipboard!

Description
:   `prometheus` defines Prometheus settings, such as querier configuration used to fetch metrics from the Console plugin.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `querier` | `object` | Prometheus querying configuration, such as client settings, used in the Console plugin. |

Show more

#### [18.1.105. .spec.prometheus.querier](#spec-prometheus-querier) Copy linkLink copied to clipboard!

Description
:   Prometheus querying configuration, such as client settings, used in the Console plugin.

Type
:   `object`

Required
:   * `mode`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `enable` | `boolean` | When `enable` is `true`, the Console plugin queries flow metrics from Prometheus instead of Loki whenever possible. It is enabled by default: set it to `false` to disable this feature. The Console plugin can use either Loki or Prometheus as a data source for metrics (see also `spec.loki`), or both. Not all queries are transposable from Loki to Prometheus. Hence, if Loki is disabled, some features of the plugin are disabled as well, such as getting per-pod information or viewing raw flows. If both Prometheus and Loki are enabled, Prometheus takes precedence and Loki is used as a fallback for queries that Prometheus cannot handle. If they are both disabled, the Console plugin is not deployed. |
| `manual` | `object` | Prometheus configuration for `Manual` mode. |
| `mode` | `string` | `mode` must be set according to the type of Prometheus installation that stores Network Observability metrics:  - Use `Auto` to try configuring automatically. In OpenShift Container Platform, it uses the Thanos querier from OpenShift Container Platform Cluster Monitoring.  - Use `Manual` for a manual setup. |
| `timeout` | `string` | `timeout` is the read timeout for console plugin queries to Prometheus. A timeout of zero means no timeout. |

Show more

#### [18.1.106. .spec.prometheus.querier.manual](#spec-prometheus-querier-manual) Copy linkLink copied to clipboard!

Description
:   Prometheus configuration for `Manual` mode.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `alertManager` | `object` | AlertManager configuration. This is used in the console to query silenced alerts, for displaying health information. When used in OpenShift Container Platform it can be left empty to use the Console API instead. [Unsupported (\*)]. |
| `forwardUserToken` | `boolean` | Set `true` to forward logged in user token in queries to Prometheus |
| `tls` | `object` | TLS client configuration for Prometheus URL. |
| `url` | `string` | `url` is the address of an existing Prometheus service to use for querying metrics. |

Show more

#### [18.1.107. .spec.prometheus.querier.manual.alertManager](#spec-prometheus-querier-manual-alertmanager) Copy linkLink copied to clipboard!

Description
:   AlertManager configuration. This is used in the console to query silenced alerts, for displaying health information. When used in OpenShift Container Platform it can be left empty to use the Console API instead. [Unsupported (\*)].

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `tls` | `object` | TLS client configuration for Prometheus AlertManager URL. |
| `url` | `string` | `url` is the address of an existing Prometheus AlertManager service to use for querying alerts. |

Show more

#### [18.1.108. .spec.prometheus.querier.manual.alertManager.tls](#spec-prometheus-querier-manual-alertmanager-tls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration for Prometheus AlertManager URL.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.109. .spec.prometheus.querier.manual.alertManager.tls.caCert](#spec-prometheus-querier-manual-alertmanager-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.110. .spec.prometheus.querier.manual.alertManager.tls.userCert](#spec-prometheus-querier-manual-alertmanager-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.111. .spec.prometheus.querier.manual.tls](#spec-prometheus-querier-manual-tls) Copy linkLink copied to clipboard!

Description
:   TLS client configuration for Prometheus URL.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caCert` | `object` | `caCert` defines the reference of the certificate for the Certificate Authority. |
| `enable` | `boolean` | Enable TLS |
| `insecureSkipVerify` | `boolean` | `insecureSkipVerify` allows skipping client-side verification of the server certificate. If set to `true`, the `caCert` field is ignored. |
| `userCert` | `object` | `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property. |

Show more

#### [18.1.112. .spec.prometheus.querier.manual.tls.caCert](#spec-prometheus-querier-manual-tls-cacert) Copy linkLink copied to clipboard!

Description
:   `caCert` defines the reference of the certificate for the Certificate Authority.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

#### [18.1.113. .spec.prometheus.querier.manual.tls.userCert](#spec-prometheus-querier-manual-tls-usercert) Copy linkLink copied to clipboard!

Description
:   `userCert` defines the user certificate reference and is used for mTLS. When you use one-way TLS, you can ignore this property.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certFile` | `string` | `certFile` defines the path to the certificate file name within the config map or secret. |
| `certKey` | `string` | `certKey` defines the path to the certificate private key file name within the config map or secret. Omit when the key is not necessary. |
| `name` | `string` | Name of the config map or secret containing certificates. |
| `namespace` | `string` | Namespace of the config map or secret containing certificates. If omitted, the default is to use the same namespace as where Network Observability is deployed. If the namespace is different, the config map or the secret is copied so that it can be mounted as required. |
| `type` | `string` | Type for the certificate reference: `configmap` or `secret`. |

Show more

## [Chapter 19. FlowMetric configuration parameters](#flowmetric-api) Copy linkLink copied to clipboard!

The `FlowMetric` API is used to generate custom observability metrics from collected network flow logs.

### [19.1. FlowMetric [flows.netobserv.io/v1alpha1]](#flowmetric-flows-netobserv-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   FlowMetric is the API allowing to create custom metrics from the collected flow logs.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and might reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers might infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | `object` | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | FlowMetricSpec defines the desired state of FlowMetric The provided API allows you to customize these metrics according to your needs.  When adding new metrics or modifying existing labels, you must carefully monitor the memory usage of Prometheus workloads as this could potentially have a high impact. Cf <https://rhobs-handbook.netlify.app/products/openshiftmonitoring/telemetry.md/#what-is-the-cardinality-of-a-metric>  To check the cardinality of all Network Observability metrics, run as `promql`: `count({name=~"netobserv.*"}) by (name)`. |

Show more

#### [19.1.1. .metadata](#metadata-3) Copy linkLink copied to clipboard!

Description
:   Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>

Type
:   `object`

#### [19.1.2. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   FlowMetricSpec defines the desired state of FlowMetric The provided API allows you to customize these metrics according to your needs.

    When adding new metrics or modifying existing labels, you must carefully monitor the memory usage of Prometheus workloads as this could potentially have a high impact. Cf <https://rhobs-handbook.netlify.app/products/openshiftmonitoring/telemetry.md/#what-is-the-cardinality-of-a-metric>

    To check the cardinality of all Network Observability metrics, run as `promql`: `count({name=~"netobserv.*"}) by (name)`.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `buckets` | `array (string)` | A list of buckets to use when `type` is "Histogram". The list must be parsable as floats. When not set, Prometheus default buckets are used. |
| `charts` | `array` | Charts configuration, for the OpenShift Container Platform Console in the administrator view, Dashboards menu. |
| `direction` | `string` | Filter for ingress, egress or any direction flows. When set to `Ingress`, it is equivalent to adding the regular expression filter on `FlowDirection`: `0|2`. When set to `Egress`, it is equivalent to adding the regular expression filter on `FlowDirection`: `1|2`. |
| `divider` | `string` | When nonzero, scale factor (divider) of the value. Metric value = Flow value / Divider. |
| `filters` | `array` | `filters` is a list of fields and values used to restrict which flows are taken into account. Refer to the documentation for the list of available fields: <https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/network_observability/json-flows-format-reference>. |
| `flatten` | `array (string)` | `flatten` is a list of array-type fields that must be flattened, such as Interfaces or NetworkEvents. Flattened fields generate one metric per item in that field. For instance, when flattening `Interfaces` on a bytes counter, a flow having Interfaces [br-ex, ens5] increases one counter for `br-ex` and another for `ens5`. |
| `help` | `string` | Help text of the metric, as it appears in Prometheus. |
| `labels` | `array (string)` | `labels` is a list of fields that should be used as Prometheus labels, also known as dimensions (for example: `SrcK8S_Namespace`). From choosing labels results the level of granularity of this metric, and the available aggregations at query time. It must be done carefully as it impacts the metric cardinality (cf <https://rhobs-handbook.netlify.app/products/openshiftmonitoring/telemetry.md/#what-is-the-cardinality-of-a-metric>). In general, avoid setting very high cardinality labels such as IP or MAC addresses. "SrcK8S\_OwnerName" or "DstK8S\_OwnerName" should be preferred over "SrcK8S\_Name" or "DstK8S\_Name" as much as possible. Refer to the documentation for the list of available fields: <https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/network_observability/json-flows-format-reference>. |
| `metricName` | `string` | Name of the metric. In Prometheus, it is automatically prefixed with "netobserv\_". Leave empty to generate the name based on the `FlowMetric` resource name. |
| `remap` | `object (string)` | Set the `remap` property to use different names for the generated metric labels than the flow fields. Use the origin flow fields as keys, and the desired label names as values. |
| `type` | `string` | Metric type: "Counter", "Histogram" or "Gauge". Use "Counter" for any value that increases over time and on which you can compute a rate, such as Bytes or Packets. Use "Histogram" for any value that must be sampled independently, such as latencies. Use "Gauge" for other values that don’t necessitate accuracy over time (gauges are sampled only every N seconds when Prometheus fetches the metric). |
| `valueField` | `string` | `valueField` is the flow field that must be used as a value for this metric (for example: `Bytes`). This field must hold numeric values. Leave empty to count flows rather than a specific value per flow. Refer to the documentation for the list of available fields: <https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/network_observability/json-flows-format-reference>. |

Show more

#### [19.1.3. .spec.charts](#spec-charts) Copy linkLink copied to clipboard!

Description
:   Charts configuration, for the OpenShift Container Platform Console in the administrator view, Dashboards menu.

Type
:   `array`

#### [19.1.4. .spec.charts[]](#spec-charts-2) Copy linkLink copied to clipboard!

Description
:   Configures charts / dashboard generation associated to a metric

Type
:   `object`

Required
:   * `dashboardName`
    * `queries`
    * `title`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `dashboardName` | `string` | Name of the containing dashboard. If this name does not refer to an existing dashboard, a new dashboard is created. |
| `queries` | `array` | List of queries to be displayed on this chart. If `type` is `SingleStat` and multiple queries are provided, this chart is automatically expanded in several panels (one per query). |
| `sectionName` | `string` | Name of the containing dashboard section. If this name does not refer to an existing section, a new section is created. If `sectionName` is omitted or empty, the chart is placed in the global top section. |
| `title` | `string` | Title of the chart. |
| `type` | `string` | Type of the chart. |
| `unit` | `string` | Unit of this chart. Only a few units are currently supported. Leave empty to use generic number. |

Show more

#### [19.1.5. .spec.charts[].queries](#spec-charts-queries) Copy linkLink copied to clipboard!

Description
:   List of queries to be displayed on this chart. If `type` is `SingleStat` and multiple queries are provided, this chart is automatically expanded in several panels (one per query).

Type
:   `array`

#### [19.1.6. .spec.charts[].queries[]](#spec-charts-queries-2) Copy linkLink copied to clipboard!

Description
:   Configures PromQL queries

Type
:   `object`

Required
:   * `legend`
    * `promQL`
    * `top`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `legend` | `string` | The query legend that applies to each timeseries represented in this chart. When multiple timeseries are displayed, you should set a legend that distinguishes each of them. It can be done with the following format: `{{ Label }}`. For example, if the `promQL` groups timeseries per label such as: `sum(rate($METRIC[2m])) by (Label1, Label2)`, you might write as the legend: `Label1={{ Label1 }}, Label2={{ Label2 }}`. |
| `promQL` | `string` | The `promQL` query to be run against Prometheus. If the chart `type` is `SingleStat`, this query should only return a single timeseries. For other types, a top 7 is displayed. You can use `$METRIC` to refer to the metric defined in this resource. For example: `sum(rate($METRIC[2m]))`. To learn more about `promQL`, refer to the Prometheus documentation: <https://prometheus.io/docs/prometheus/latest/querying/basics/> |
| `top` | `integer` | Top N series to display per timestamp. Does not apply to `SingleStat` chart type. |

Show more

#### [19.1.7. .spec.filters](#spec-filters) Copy linkLink copied to clipboard!

Description
:   `filters` is a list of fields and values used to restrict which flows are taken into account. Refer to the documentation for the list of available fields: <https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/network_observability/json-flows-format-reference>.

Type
:   `array`

#### [19.1.8. .spec.filters[]](#spec-filters-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `field`
    * `matchType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `field` | `string` | Name of the field to filter on (for example: `SrcK8S_Namespace`). |
| `matchType` | `string` | Type of matching to apply |
| `value` | `string` | Value to filter on. When `matchType` is `Equal` or `NotEqual`, you can use field injection with `$(SomeField)` to refer to any other field of the flow. |

Show more

## [Chapter 20. Network flows format reference](#json-flows-format-reference) Copy linkLink copied to clipboard!

Review the specifications for the network flow format, which is used internally and for exporting flow data to Kafka.

### [20.1. Network Flows format reference](#network-observability-flows-format_json_reference) Copy linkLink copied to clipboard!

This is the specification of the network flows format. That format is used when a Kafka exporter is configured, for Prometheus metrics labels as well as internally for the Loki store.

The "Filter ID" column shows which related name to use when defining Quick Filters (see `spec.consolePlugin.quickFilters` in the `FlowCollector` specification).

The "Loki label" column is useful when querying Loki directly: label fields need to be selected using [stream selectors](https://grafana.com/docs/loki/latest/logql/log_queries/#log-stream-selector).

The "Cardinality" column gives information about the implied metric cardinality if this field was to be used as a Prometheus label with the `FlowMetrics` API. Refer to the `FlowMetrics` documentation for more information on using this API.

Expand

| Name | Type | Description | Filter ID | Loki label | Cardinality | OpenTelemetry |
| --- | --- | --- | --- | --- | --- | --- |
| `Bytes` | number | Number of bytes | n/a | no | avoid | bytes |
| `DnsErrno` | number | Error number returned from DNS tracker ebpf hook function | `dns_errno` | no | fine | dns.errno |
| `DnsFlags` | number | DNS flags for DNS record | n/a | no | fine | dns.flags |
| `DnsFlagsResponseCode` | string | Parsed DNS header RCODEs name | `dns_flag_response_code` | no | fine | dns.responsecode |
| `DnsId` | number | DNS record id | `dns_id` | no | avoid | dns.id |
| `DnsLatencyMs` | number | Time between a DNS request and response, in milliseconds | `dns_latency` | no | avoid | dns.latency |
| `DnsName` | string | DNS queried name | `dns_name` | no | careful | dns.name |
| `Dscp` | number | Differentiated Services Code Point (DSCP) value | `dscp` | no | fine | dscp |
| `DstAddr` | string | Destination IP address (ipv4 or ipv6) | `dst_address` | no | avoid | destination.address |
| `DstK8S_HostIP` | string | Destination node IP | `dst_host_address` | no | fine | destination.k8s.host.address |
| `DstK8S_HostName` | string | Destination node name | `dst_host_name` | no | fine | destination.k8s.host.name |
| `DstK8S_Name` | string | Name of the destination Kubernetes object, such as Pod name, Service name or Node name. | `dst_name` | no | careful | destination.k8s.name |
| `DstK8S_Namespace` | string | Destination namespace | `dst_namespace` | yes | fine | destination.k8s.namespace.name |
| `DstK8S_NetworkName` | string | Destination network name | `dst_network` | no | fine | destination.network.name |
| `DstK8S_OwnerName` | string | Name of the destination owner, such as Deployment name, StatefulSet name, etc. | `dst_owner_name` | yes | fine | destination.k8s.owner.name |
| `DstK8S_OwnerType` | string | Kind of the destination owner, such as Deployment, StatefulSet, etc. | `dst_kind` | no | fine | destination.k8s.owner.kind |
| `DstK8S_Type` | string | Kind of the destination Kubernetes object, such as Pod, Service or Node. | `dst_kind` | yes | fine | destination.k8s.kind |
| `DstK8S_Zone` | string | Destination availability zone | `dst_zone` | yes | fine | destination.zone |
| `DstMac` | string | Destination MAC address | `dst_mac` | no | avoid | destination.mac |
| `DstPort` | number | Destination port | `dst_port` | no | careful | destination.port |
| `DstSubnetLabel` | string | Destination subnet label | `dst_subnet_label` | no | fine | destination.subnet.label |
| `Flags` | string[] | List of TCP flags comprised in the flow, according to RFC-9293, with additional custom flags to represent the following per-packet combinations:  - SYN\_ACK  - FIN\_ACK  - RST\_ACK | `tcp_flags` | no | careful | tcp.flags |
| `FlowDirection` | number | Flow interpreted direction from the node observation point. Can be one of:  - 0: Ingress (incoming traffic, from the node observation point)  - 1: Egress (outgoing traffic, from the node observation point)  - 2: Inner (with the same source and destination node) | `node_direction` | yes | fine | host.direction |
| `IPSecStatus` | string | Status of the IPsec encryption (on egress, given by the kernel xfrm\_output function) or decryption (on ingress, via xfrm\_input) | `ipsec_status` | no | fine | ipsec.status |
| `IcmpCode` | number | ICMP code | `icmp_code` | no | fine | icmp.code |
| `IcmpType` | number | ICMP type | `icmp_type` | no | fine | icmp.type |
| `IfDirections` | number[] | Flow directions from the network interface observation point. Can be one of:  - 0: Ingress (interface incoming traffic)  - 1: Egress (interface outgoing traffic) | `ifdirections` | no | fine | interface.directions |
| `Interfaces` | string[] | Network interfaces | `interfaces` | no | careful | interface.names |
| `K8S_ClusterName` | string | Cluster name or identifier | `cluster_name` | yes | fine | k8s.cluster.name |
| `K8S_FlowLayer` | string | Flow layer: 'app' or 'infra' | `flow_layer` | yes | fine | k8s.layer |
| `NetworkEvents` | object[] | Network events, such as network policy actions, composed of nested fields:  - Feature (such as "acl" for network policies)  - Type (such as an "AdminNetworkPolicy")  - Namespace (namespace where the event applies, if any)  - Name (name of the resource that triggered the event)  - Action (such as "allow" or "drop")  - Direction (Ingress or Egress) | `network_events` | no | avoid | n/a |
| `Packets` | number | Number of packets | n/a | no | avoid | packets |
| `PktDropBytes` | number | Number of bytes dropped by the kernel | n/a | no | avoid | drops.bytes |
| `PktDropLatestDropCause` | string | Latest drop cause | `pkt_drop_cause` | no | fine | drops.latestcause |
| `PktDropLatestFlags` | number | TCP flags on last dropped packet | n/a | no | fine | drops.latestflags |
| `PktDropLatestState` | string | TCP state on last dropped packet | `pkt_drop_state` | no | fine | drops.lateststate |
| `PktDropPackets` | number | Number of packets dropped by the kernel | n/a | no | avoid | drops.packets |
| `Proto` | number | L4 protocol | `protocol` | no | fine | protocol |
| `Sampling` | number | Sampling interval used for this flow | n/a | no | fine | n/a |
| `SrcAddr` | string | Source IP address (ipv4 or ipv6) | `src_address` | no | avoid | source.address |
| `SrcK8S_HostIP` | string | Source node IP | `src_host_address` | no | fine | source.k8s.host.address |
| `SrcK8S_HostName` | string | Source node name | `src_host_name` | no | fine | source.k8s.host.name |
| `SrcK8S_Name` | string | Name of the source Kubernetes object, such as Pod name, Service name or Node name. | `src_name` | no | careful | source.k8s.name |
| `SrcK8S_Namespace` | string | Source namespace | `src_namespace` | yes | fine | source.k8s.namespace.name |
| `SrcK8S_NetworkName` | string | Source network name | `src_network` | no | fine | source.network.name |
| `SrcK8S_OwnerName` | string | Name of the source owner, such as Deployment name, StatefulSet name, etc. | `src_owner_name` | yes | fine | source.k8s.owner.name |
| `SrcK8S_OwnerType` | string | Kind of the source owner, such as Deployment, StatefulSet, etc. | `src_kind` | no | fine | source.k8s.owner.kind |
| `SrcK8S_Type` | string | Kind of the source Kubernetes object, such as Pod, Service or Node. | `src_kind` | yes | fine | source.k8s.kind |
| `SrcK8S_Zone` | string | Source availability zone | `src_zone` | yes | fine | source.zone |
| `SrcMac` | string | Source MAC address | `src_mac` | no | avoid | source.mac |
| `SrcPort` | number | Source port | `src_port` | no | careful | source.port |
| `SrcSubnetLabel` | string | Source subnet label | `src_subnet_label` | no | fine | source.subnet.label |
| `TLSCipherSuite` | string | TLS cipher suite | `tls_cipher_suite` | no | fine | tls.ciphersuite |
| `TLSGroup` | string | TLS group name | `tls_group` | no | fine | tls.group |
| `TLSTypes` | string[] | TLS message types (bitfield) | `tls_types` | no | careful | tls.types |
| `TLSVersion` | string | TLS version | `tls_version` | no | fine | tls.version |
| `TimeFlowEndMs` | number | End timestamp of this flow, in milliseconds | n/a | no | avoid | timeflowend |
| `TimeFlowRttNs` | number | TCP Smoothed Round Trip Time (SRTT), in nanoseconds | `time_flow_rtt` | no | avoid | tcp.rtt |
| `TimeFlowStartMs` | number | Start timestamp of this flow, in milliseconds | n/a | no | avoid | timeflowstart |
| `TimeReceived` | number | Timestamp when this flow was received and processed by the flow collector, in seconds | n/a | no | avoid | timereceived |
| `Udns` | string[] | List of User Defined Networks | `udns` | no | careful | n/a |
| `XlatDstAddr` | string | packet translation destination address | `xlat_dst_address` | no | avoid | n/a |
| `XlatDstPort` | number | packet translation destination port | `xlat_dst_port` | no | careful | n/a |
| `XlatSrcAddr` | string | packet translation source address | `xlat_src_address` | no | avoid | n/a |
| `XlatSrcPort` | number | packet translation source port | `xlat_src_port` | no | careful | n/a |
| `ZoneId` | number | packet translation zone id | `xlat_zone_id` | no | avoid | n/a |
| `_HashId` | string | In conversation tracking, the conversation identifier | `id` | no | avoid | n/a |
| `_RecordType` | string | Type of record: `flowLog` for regular flow logs, or `newConnection`, `heartbeat`, `endConnection` for conversation tracking | `type` | yes | fine | n/a |

Show more

## [Chapter 21. Troubleshooting network observability](#installing-troubleshooting) Copy linkLink copied to clipboard!

Perform diagnostic actions to troubleshoot common issues related to the Network Observability Operator and its components.

### [21.1. Using the must-gather tool](#network-observability-must-gather_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Use the must-gather tool to collect diagnostic information about Network Observability Operator resources, including pod logs and configuration details, to assist in troubleshooting cluster issues.

**Procedure**

1. Navigate to the directory where you want to store the must-gather data.
2. Run the following command to collect cluster-wide must-gather resources:

   ```
   $ oc adm must-gather
    --image-stream=openshift/must-gather \
    --image=quay.io/netobserv/must-gather
   ```

### [21.2. Configuring network traffic menu entry in the OpenShift Container Platform console](#configure-network-traffic-console_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Restore a missing network traffic menu entry in the **Observe** menu of the OpenShift Container Platform console by manually registering the console plugin in the `FlowCollector` resource and the console operator configuration.

**Prerequisites**

* You have installed OpenShift Container Platform version 4.10 or newer.

**Procedure**

1. Check if the `spec.consolePlugin.register` field is set to `true` by running the following command:

   ```
   $ oc -n netobserv get flowcollector cluster -o yaml
   ```

   **Example output**

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     consolePlugin:
       register: false
   ```
2. Optional: Add the `netobserv-plugin` plugin by manually editing the Console Operator config:

   ```
   $ oc edit console.operator.openshift.io cluster
   ```

   **Example output**

   ```
   ...
   spec:
     plugins:
     - netobserv-plugin
   ...
   ```
3. Optional: Set the `spec.consolePlugin.register` field to `true` by running the following command:

   ```
   $ oc -n netobserv edit flowcollector cluster -o yaml
   ```

   **Example output**

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     consolePlugin:
       register: true
   ```
4. Ensure the status of console pods is `running` by running the following command:

   ```
   $ oc get pods -n openshift-console -l app=console
   ```
5. Restart the console pods by running the following command:

   ```
   $ oc delete pods -n openshift-console -l app=console
   ```
6. Clear your browser cache and history.
7. Check the status of network observability plugin pods by running the following command:

   ```
   $ oc get pods -n netobserv -l app=netobserv-plugin
   ```

   **Example output**

   ```
   NAME                                READY   STATUS    RESTARTS   AGE
   netobserv-plugin-68c7bbb9bb-b69q6   1/1     Running   0          21s
   ```
8. Check the logs of the network observability plugin pods by running the following command:

   ```
   $ oc logs -n netobserv -l app=netobserv-plugin
   ```

   **Example output**

   ```
   time="2022-12-13T12:06:49Z" level=info msg="Starting netobserv-console-plugin [build version: , build date: 2022-10-21 15:15] at log level info" module=main
   time="2022-12-13T12:06:49Z" level=info msg="listening on https://:9001" module=server
   ```

### [21.3. Flowlogs-Pipeline does not consume network flows after installing Kafka](#configure-network-traffic-flowlogs-pipeline-kafka_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Resolve issues where the flow-pipeline fails to consume network flows from Kafka by manually restarting the flow-pipeline pods to restore the connection between the flow collector and your Kafka deployment.

If you deployed the flow collector first with `deploymentModel: KAFKA` and then deployed Kafka, the flow collector might not connect correctly to Kafka. Manually restart the flow-pipeline pods where Flowlogs-pipeline does not consume network flows from Kafka.

**Procedure**

1. Delete the flow-pipeline pods to restart them by running the following command:

   ```
   $ oc delete pods -n netobserv -l app=flowlogs-pipeline-transformer
   ```

### [21.4. Failing to see network flows from both br-int and br-ex interfaces](#configure-network-traffic-interfaces_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Resolve issues with missing network flows by removing interface restrictions on virtual bridge devices like `br-int` and `br-ex`, ensuring the eBPF agent can attach to the appropriate Layer 3 interfaces.

`br-ex` and `br-int` are virtual bridge devices operated at OSI layer 2. The eBPF agent works at the IP and TCP levels, layers 3 and 4 respectively. You can expect that the eBPF agent captures the network traffic passing through `br-ex` and `br-int`, when the network traffic is processed by other interfaces such as physical host or virtual pod interfaces. If you restrict the eBPF agent network interfaces to attach only to `br-ex` and `br-int`, you do not see any network flow.

Manually remove the part in the `interfaces` or `excludeInterfaces` that restricts the network interfaces to `br-int` and `br-ex`.

**Procedure**

1. Remove the `interfaces: [ 'br-int', 'br-ex' ]` field. This allows the agent to fetch information from all the interfaces. Alternatively, you can specify the Layer-3 interface for example, `eth0`. Run the following command:

   ```
   $ oc edit -n netobserv flowcollector.yaml -o yaml
   ```

   **Example output**

   ```
   apiVersion: flows.netobserv.io/v1alpha1
   kind: FlowCollector
   metadata:
     name: cluster
   spec:
     agent:
       type: EBPF
       ebpf:
         interfaces: [ 'br-int', 'br-ex' ]
   ```

   1

   [1](#CO2-1)
   :   Specifies the network interfaces.

### [21.5. Network observability controller manager pod runs out of memory](#controller-manager-pod-runs-out-of-memory_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Resolve memory issues with the Network Observability Operator by increasing the memory limits in the `Subscription` object to prevent the controller manager pod from running out of memory.

You can increase memory limits for the Network Observability Operator by editing the `spec.config.resources.limits.memory` specification in the `Subscription` object.

**Procedure**

1. In the web console, navigate to **Ecosystem** → **Installed Operators**
2. Click **Network Observability** and then select **Subscription**.
3. From the **Actions** menu, click **Edit Subscription**.

   1. Alternatively, you can use the CLI to open the YAML configuration for the `Subscription` object by running the following command:

      ```
      $ oc edit subscription netobserv-operator -n openshift-netobserv-operator
      ```
4. Edit the `Subscription` object to add the `config.resources.limits.memory` specification and set the value to account for your memory requirements. See the Additional resources for more information about resource considerations:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: netobserv-operator
     namespace: openshift-netobserv-operator
   spec:
     channel: stable
     config:
       resources:
         limits:
           memory: 800Mi
   ```

   1

   ```
         requests:
           cpu: 100m
           memory: 100Mi
     installPlanApproval: Automatic
     name: netobserv-operator
     source: redhat-operators
     sourceNamespace: openshift-marketplace
     startingCSV: <network_observability_operator_latest_version>
   ```

   2

   [1](#CO3-1)
   :   For example, you can increase the memory limit to `800Mi`.

   [2](#CO3-2)
   :   This value should not be edited, but note that it changes depending on the most current release of the Operator.

### [21.6. Running custom queries to Loki](#troubleshooting-query-loki-manually_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Troubleshoot network flow data by running custom Loki queries to retrieve available labels or filter logs by specific criteria, such as source namespaces, using the command-line interface.

There are two examples of ways to do this, which you can adapt according to your needs by replacing the <api\_token> with your own.

Note

These examples use the `netobserv` namespace for the Network Observability Operator and Loki deployments. Additionally, the examples assume that the LokiStack is named `loki`. You can optionally use a different namespace and naming by adapting the examples, specifically the `-n netobserv` or the `loki-gateway` URL.

**Prerequisites**

* Installed Loki Operator for use with Network Observability Operator.

**Procedure**

1. To get all available labels, run the following command:

   ```
   $ oc exec deployment/netobserv-plugin -n netobserv -- curl -G -s -H 'X-Scope-OrgID:network' -H 'Authorization: Bearer <api_token>' -k https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network/loki/api/v1/labels | jq
   ```
2. To get all flows from the source namespace, `my-namespace`, run the following command:

   ```
   $ oc exec deployment/netobserv-plugin -n netobserv -- curl -G -s -H 'X-Scope-OrgID:network' -H 'Authorization: Bearer <api_token>' -k https://loki-gateway-http.netobserv.svc:8080/api/logs/v1/network/loki/api/v1/query --data-urlencode 'query={SrcK8S_Namespace="my-namespace"}' | jq
   ```

### [21.7. Troubleshooting Loki ResourceExhausted error](#network-observability-troubleshooting-loki-resource-exhausted_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Resolve Loki `ResourceExhausted` errors by adjusting the `batchSize` in the `FlowCollector` resource or the maximum message size settings in your Loki configuration to ensure flow data stays within memory limits.

Loki may return a `ResourceExhausted` error when network flow data sent by network observability exceeds the configured maximum message size. If you are using the Red Hat Loki Operator, this maximum message size is configured to 100 MiB.

**Procedure**

1. Navigate to **Ecosystem** → **Installed Operators**, viewing **All projects** from the **Project** drop-down menu.
2. In the **Provided APIs** list, select the Network Observability Operator.
3. Click the **Flow Collector** then the **YAML view** tab.

   1. If you are using the Loki Operator, check that the `spec.loki.batchSize` value does not exceed 98 MiB.
   2. If you are using a Loki installation method that is different from the Red Hat Loki Operator, such as Grafana Loki, verify that the `grpc_server_max_recv_msg_size` [Grafana Loki server setting](https://grafana.com/docs/loki/latest/configure/#server) is higher than the `FlowCollector` resource `spec.loki.batchSize` value. If it is not, you must either increase the `grpc_server_max_recv_msg_size` value, or decrease the `spec.loki.batchSize` value so that it is lower than the limit.
4. Click **Save** if you edited the **FlowCollector**.

### [21.8. Loki empty ring error](#network-observability-troubleshooting-loki-empty-ring_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Investigate and resolve Loki "empty ring" errors by checking pod health, clearing old persistent volume claims, or restarting pods to restore connectivity and ensure network flows are properly stored and displayed.

The Loki "empty ring" error results in flows not being stored in Loki and not showing up in the web console. This error might happen in various situations. A single workaround to address them all does not exist. There are some actions you can take to investigate the logs in your Loki pods, and verify that the `LokiStack` is healthy and ready.

Some of the situations where this error is observed are as follows:

* After a `LokiStack` is uninstalled and reinstalled in the same namespace, old PVCs are not removed, which can cause this error.

  + **Action**: You can try removing the `LokiStack` again, removing the PVC, then reinstalling the `LokiStack`.
* After a certificate rotation, this error can prevent communication with the `flowlogs-pipeline` and `console-plugin` pods.

  + **Action**: You can restart the pods to restore the connectivity.

### [21.9. LokiStack rate limit errors](#network-observability-troubleshooting-loki-tenant-rate-limit_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Resolve Loki rate limit errors and prevent data loss by updating the `LokiStack` resource to increase the ingestion rate and burst limits for your network observability data streams.

A rate-limit placed on the Loki tenant can result in potential temporary loss of data and a 429 error: `Per stream rate limit exceeded (limit:xMB/sec) while attempting to ingest for stream`. You might consider having an alert set to notify you of this error. For more information, see "Creating Loki rate limit alerts for the NetObserv dashboard" in the Additional resources of this section.

You can update the LokiStack CRD with the `perStreamRateLimit` and `perStreamRateLimitBurst` specifications, as shown in the following procedure.

**Procedure**

1. Navigate to **Ecosystem** → **Installed Operators**, viewing **All projects** from the **Project** dropdown.
2. Look for **Loki Operator**, and select the **LokiStack** tab.
3. Create or edit an existing **LokiStack** instance using the **YAML view** to add the `perStreamRateLimit` and `perStreamRateLimitBurst` specifications:

   ```
   apiVersion: loki.grafana.com/v1
   kind: LokiStack
   metadata:
     name: loki
     namespace: netobserv
   spec:
     limits:
       global:
         ingestion:
           perStreamRateLimit: 6
   ```

   1

   ```
           perStreamRateLimitBurst: 30
   ```

   2

   ```
     tenants:
       mode: openshift-network
     managementState: Managed
   ```

   [1](#CO4-1)
   :   The default value for `perStreamRateLimit` is `3`.

   [2](#CO4-2)
   :   The default value for `perStreamRateLimitBurst` is `15`.
4. Click **Save**.

**Verification**

Once you update the `perStreamRateLimit` and `perStreamRateLimitBurst` specifications, the pods in your cluster restart and the 429 rate-limit error no longer occurs.

### [21.10. Running a large query results in Loki errors](#network-observability-troubleshooting-large-query-timeout_network-observability-troubleshooting) Copy linkLink copied to clipboard!

Understand how you can mitigate Loki timeout and request errors when running large queries by using indexed filters, leveraging Prometheus for long time ranges, creating custom metrics, or adjusting Loki and FlowCollector performance settings.

When running large queries for a long time, Loki errors can occur, such as a `timeout` or `too many outstanding requests`. There is no complete corrective for this issue, but there are several ways to mitigate it:

Adapt your query to add an indexed filter
:   With Loki queries, you can query on both indexed and non-indexed fields or labels. Queries that contain filters on labels perform better. For example, if you query for a particular Pod, which is not an indexed field, you can add its Namespace to the query. The list of indexed fields can be found in the "Network flows format reference", in the `Loki label` column.

Consider querying Prometheus rather than Loki
:   Prometheus is a better fit than Loki to query on large time ranges. However, whether or not you can use Prometheus instead of Loki depends on the use case. For example, queries on Prometheus are much faster than on Loki, and large time ranges do not impact performance. But Prometheus metrics do not contain as much information as flow logs in Loki. The Network Observability OpenShift web console automatically favors Prometheus over Loki if the query is compatible; otherwise, it defaults to Loki. If your query does not run against Prometheus, you can change some filters or aggregations to make the switch. In the OpenShift web console, you can force the use of Prometheus. An error message is displayed when incompatible queries fail, which can help you figure out which labels to change to make the query compatible. For example, changing a filter or an aggregation from **Resource** or **Pods** to **Owner**.

Consider using the FlowMetrics API to create your own metric
:   If the data that you need isn’t available as a Prometheus metric, you can use the FlowMetrics API to create your own metric. For more information, see "FlowMetrics API Reference" and "Configuring custom metrics by using FlowMetric API".

Configure Loki to improve the query performance
:   If the problem persists, you can consider configuring Loki to improve the query performance. Some options depend on the installation mode you used for Loki, such as using the Operator and `LokiStack`, or `Monolithic` mode, or `Microservices` mode.

    * In `LokiStack` or `Microservices` modes, try [increasing the number of querier replicas](https://loki-operator.dev/docs/api.md/#loki-grafana-com-v1-LokiComponentSpec).
    * Increase the [query timeout](https://loki-operator.dev/docs/api.md/#loki-grafana-com-v1-QueryLimitSpec). You must also increase the Network Observability read timeout to Loki in the `FlowCollector` `spec.loki.readTimeout`.

## [Legal Notice](#idm140486421059392) Copy linkLink copied to clipboard!

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
