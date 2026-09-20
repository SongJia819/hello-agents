---
title: "Observability overview"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/observability_overview/index
retrieved_at: 2026-09-05T05:42:36.105583+00:00
---

# Observability overview

---

OpenShift Container Platform 4.22

## Contains information about observability for OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140241145222976)

**Abstract**

Red Hat OpenShift Observability provides real-time visibility, monitoring, and analysis of various system metrics, logs, traces, and events to help users quickly diagnose and troubleshoot issues before they impact systems or applications.

---

## [Chapter 1. About Observability](#observability-overview) Copy linkLink copied to clipboard!

Red Hat OpenShift Observability provides real-time visibility, monitoring, and analysis of various system metrics, logs, traces, and events to help users quickly diagnose and troubleshoot issues before they impact systems or applications. To help ensure the reliability, performance, and security of your applications and infrastructure, OpenShift Container Platform offers the following Observability components:

* Monitoring
* Logging
* Distributed tracing
* Red Hat build of OpenTelemetry
* Network Observability
* Power monitoring

Red Hat OpenShift Observability connects open-source observability tools and technologies to create a unified Observability solution. The components of Red Hat OpenShift Observability work together to help you collect, store, deliver, analyze, and visualize data.

Note

With the exception of monitoring, Red Hat OpenShift Observability components have distinct release cycles separate from the core OpenShift Container Platform release cycles. See the Red Hat [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) page for their release compatibility.

### [1.1. Monitoring](#monitoring-overview-index_observability-overview) Copy linkLink copied to clipboard!

Monitor the in-cluster health and performance of your applications running on OpenShift Container Platform with metrics and customized alerts for CPU and memory usage, network connectivity, and other resource usage. Monitoring stack components are deployed and managed by the Cluster Monitoring Operator.

Monitoring stack components are deployed by default in every OpenShift Container Platform installation and are managed by the Cluster Monitoring Operator (CMO). These components include Prometheus, Alertmanager, Thanos Querier, and others. The CMO also deploys the Telemeter Client, which sends a subset of data from platform Prometheus instances to Red Hat to facilitate Remote Health Monitoring for clusters.

For more information, see [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring) and [About remote health monitoring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#about-remote-health-monitoring).

### [1.2. Logging](#cluster-logging-index_observability-overview) Copy linkLink copied to clipboard!

Collect, visualize, forward, and store log data to troubleshoot issues, identify performance bottlenecks, and detect security threats. In logging 5.7 and later versions, users can configure the LokiStack deployment to produce customized alerts and recorded metrics.

### [1.3. Distributed tracing](#distr-tracing-architecture-index_observability-overview) Copy linkLink copied to clipboard!

Store and visualize large volumes of requests passing through distributed systems, across the whole stack of microservices, and under heavy loads. Use it for monitoring distributed transactions, gathering insights into your instrumented services, network profiling, performance and latency optimization, root cause analysis, and troubleshooting the interaction between components in modern cloud-native microservices-based applications.

For more information, see [Red Hat OpenShift Distributed Tracing Platform](https://docs.redhat.com/en/documentation/red_hat_openshift_distributed_tracing_platform/latest).

### [1.4. Red Hat build of OpenTelemetry](#otel-release-notes-index_observability-overview) Copy linkLink copied to clipboard!

Instrument, generate, collect, and export telemetry traces, metrics, and logs to analyze and understand your software’s performance and behavior. Use open-source back ends like Tempo or Prometheus, or use commercial offerings. Learn a single set of APIs and conventions, and own the data that you generate.

For more information, see [Red Hat build of OpenTelemetry](https://docs.redhat.com/en/documentation/red_hat_build_of_opentelemetry/latest/html/installing_red_hat_build_of_opentelemetry/install-otel).

### [1.5. Network Observability](#network-observability-overview-index_observability-overview) Copy linkLink copied to clipboard!

Observe the network traffic for OpenShift Container Platform clusters and create network flows with the Network Observability Operator. View and analyze the stored network flows information in the OpenShift Container Platform console for further insight and troubleshooting.

For more information, see [Network Observability overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_observability/#network-observability-overview).

### [1.6. Power monitoring](#power-monitoring-overview-index_observability-overview) Copy linkLink copied to clipboard!

Monitor the power usage of workloads and identify the most power-consuming namespaces running in a cluster with key power consumption metrics, such as CPU or DRAM measured at the container level. Visualize energy-related system statistics with the Power Monitoring Operator.

For more information, see [About power monitoring](https://docs.redhat.com/en/documentation/power_monitoring_for_red_hat_openshift/latest/html/about_power_monitoring/about-power-monitoring).

## [Legal Notice](#idm140241145222976) Copy linkLink copied to clipboard!

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
