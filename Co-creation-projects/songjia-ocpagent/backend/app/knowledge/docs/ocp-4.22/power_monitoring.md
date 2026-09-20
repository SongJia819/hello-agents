---
title: "Power Monitoring"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/power_monitoring/index
retrieved_at: 2026-09-05T05:42:45.864676+00:00
---

# Power Monitoring

---

OpenShift Container Platform 4.22

## Configuring and using power monitoring for OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139947662678832)

**Abstract**

Use power monitoring to monitor the power consumption for various components, such as CPU and DRAM, for each container running in an OpenShift Container Platform cluster.

---

## [Chapter 1. About power monitoring for Red Hat OpenShift](#about-power-monitoring) Copy linkLink copied to clipboard!

With Power monitoring for Red Hat OpenShift, you can track energy consumption across your cluster infrastructure. It provides granular power metrics for pods and namespaces to help you identify and optimize workload energy usage.

Important

Power monitoring for Red Hat OpenShift is deprecated and will have no further releases or support.

You can use power monitoring for Red Hat OpenShift to monitor the power usage and identify power-consuming containers running in an OpenShift Container Platform cluster. Power monitoring collects and exports energy-related system statistics from various components, such as CPU and DRAM. It provides estimates and granular power consumption data for Kubernetes pods and namespaces, and reads the power consumption of nodes.

Note

The power monitoring documentation is available as a separate documentation set at [Power monitoring for Red Hat OpenShift](https://docs.redhat.com/en/documentation/power_monitoring_for_red_hat_openshift/latest).

## [Legal Notice](#idm139947662678832) Copy linkLink copied to clipboard!

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
