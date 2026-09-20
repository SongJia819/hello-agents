---
title: "GitOps"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/gitops/index
retrieved_at: 2026-09-05T05:41:48.463210+00:00
---

# GitOps

---

OpenShift Container Platform 4.22

## A declarative way to implement continuous deployment for cloud native applications.

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140301976307776)

**Abstract**

OpenShift GitOps is an Operator that uses Argo CD as the declarative GitOps engine. It enables GitOps workflows across multicluster OpenShift and Kubernetes infrastructure. Using OpenShift GitOps, administrators can consistently configure and deploy Kubernetes-based infrastructure and applications across clusters and development lifecycles.

---

## [Chapter 1. About Red Hat OpenShift GitOps](#about-redhat-openshift-gitops) Copy linkLink copied to clipboard!

Red Hat OpenShift GitOps is an Operator that uses Argo CD as the declarative GitOps engine. It enables GitOps workflows across multicluster OpenShift and Kubernetes infrastructure. Using Red Hat OpenShift GitOps, administrators can consistently configure and deploy Kubernetes-based infrastructure and applications across clusters and development lifecycles. Red Hat OpenShift GitOps is based on the open source project [Argo CD](https://argoproj.github.io/cd/) and provides a similar set of features to what the upstream offers, with additional automation, integration into Red Hat OpenShift Container Platform and the benefits of Red Hat’s enterprise support, quality assurance and focus on enterprise security.

Note

Because Red Hat OpenShift GitOps releases on a different cadence from OpenShift Container Platform, the Red Hat OpenShift GitOps documentation is now available as a separate documentation set at [Red Hat OpenShift GitOps](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops).

## [Legal Notice](#idm140301976307776) Copy linkLink copied to clipboard!

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
