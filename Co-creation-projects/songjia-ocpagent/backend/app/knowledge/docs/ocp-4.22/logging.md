---
title: "Logging"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/logging/index
retrieved_at: 2026-09-05T05:42:10.786825+00:00
---

# Logging

---

OpenShift Container Platform 4.22

## Configuring and using logging in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140208537692160)

**Abstract**

Use logging to collect, visualize, forward, and store log data to troubleshoot issues, identify performance bottlenecks, and detect security threats in OpenShift Container Platform.

---

## [Chapter 1. About Logging](#about-logging) Copy linkLink copied to clipboard!

As a cluster administrator, you can deploy logging on your OpenShift Container Platform cluster, and use it to collect and aggregate node system audit logs, application container logs, and infrastructure logs.

You can use logging to perform the following tasks:

* Forward logs to your chosen log outputs, including on-cluster, Red Hat managed log storage.
* Visualize your log data in the OpenShift Container Platform web console.

Note

Because logging releases on a different cadence from OpenShift Container Platform, the logging documentation is available as a separate documentation set at [Red Hat OpenShift Logging](https://docs.redhat.com/en/documentation/red_hat_openshift_logging/).

## [Legal Notice](#idm140208537692160) Copy linkLink copied to clipboard!

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
