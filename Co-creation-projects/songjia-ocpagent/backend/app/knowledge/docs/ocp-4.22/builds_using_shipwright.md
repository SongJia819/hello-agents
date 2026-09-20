---
title: "Builds using Shipwright"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_shipwright/index
retrieved_at: 2026-09-05T05:41:37.715440+00:00
---

# Builds using Shipwright

---

OpenShift Container Platform 4.22

## An extensible build framework to build container images on an OpenShift cluster

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140425869614992)

**Abstract**

Builds is an extensible build framework based on the Shipwright project, which you can use to build container images on an OpenShift Container Platform cluster. You can build container images from source code and Dockerfiles by using image build tools, such as Source-to-Image (S2I) and Buildah.

---

## [Chapter 1. Overview of Builds](#overview-openshift-builds) Copy linkLink copied to clipboard!

Builds is an extensible build framework based on the [Shipwright project](https://shipwright.io/), which you can use to build container images on your OpenShift Container Platform cluster. You can build container images from source code and Dockerfiles by using image build tools, such as Source-to-Image (S2I) and Buildah. You can create and apply build resources, view logs of build runs, and manage builds in your OpenShift Container Platform namespaces.

Builds includes the following capabilities:

* Standard Kubernetes-native API for building container images from source code and Dockerfiles
* Support for Source-to-Image (S2I) and Buildah build strategies
* Extensibility with your own custom build strategies
* Execution of builds from source code in a local directory
* Shipwright CLI for creating and viewing logs, and managing builds on the cluster
* Integrated user experience with the **Developer** perspective of the OpenShift Container Platform web console

Note

Because Builds releases on a different cadence from OpenShift Container Platform, the Builds documentation is now available as a separate documentation set at [Builds for Red Hat OpenShift](https://docs.redhat.com/en/documentation/builds_for_red_hat_openshift).

## [Legal Notice](#idm140425869614992) Copy linkLink copied to clipboard!

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
