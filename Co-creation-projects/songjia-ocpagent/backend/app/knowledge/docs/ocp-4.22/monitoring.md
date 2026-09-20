---
title: "Monitoring"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring/index
retrieved_at: 2026-09-05T05:42:14.776676+00:00
---

# Monitoring

---

OpenShift Container Platform 4.22

## Configuring and using the monitoring stack in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139663936013984)

**Abstract**

Use metrics and customized alerts provided by the monitoring stack to track the health and performance of your applications running on OpenShift Container Platform clusters.

---

## [Chapter 1. About OpenShift Container Platform monitoring](#about-ocp-monitoring) Copy linkLink copied to clipboard!

OpenShift Container Platform includes a preconfigured, preinstalled, and self-updating monitoring stack that provides monitoring for core platform components. After installing OpenShift Container Platform, cluster administrators can optionally enable monitoring for user-defined projects. By using this feature, cluster administrators, developers, and other users can specify how services and pods are monitored in their own projects.

Note

The monitoring stack documentation is available as a separate documentation set at [Monitoring stack for Red Hat OpenShift](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest).

## [Legal Notice](#idm139663936013984) Copy linkLink copied to clipboard!

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
