---
title: "CI/CD overview"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cicd_overview/index
retrieved_at: 2026-09-05T05:41:37.845756+00:00
---

# CI/CD overview

---

OpenShift Container Platform 4.22

## Contains information about CI/CD for OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140366024770496)

**Abstract**

OpenShift Container Platform provides several CI/CD solutions.

---

## [Chapter 1. About CI/CD](#ci-cd-overview) Copy linkLink copied to clipboard!

OpenShift Container Platform is an enterprise-ready Kubernetes platform for developers, which enables organizations to automate the application delivery process through DevOps practices, such as continuous integration (CI) and continuous delivery (CD). To meet your organizational needs, the OpenShift Container Platform provides the following CI/CD solutions:

* OpenShift Builds
* OpenShift Pipelines
* OpenShift GitOps
* Jenkins

### [1.1. OpenShift Builds](#openshift-builds) Copy linkLink copied to clipboard!

OpenShift Builds provides you the following options to configure and run a build:

* Builds using Shipwright is an extensible build framework based on the Shipwright project. You can use it to build container images on a cluster. You can build container images from source code and Dockerfile by using image build tools, such as Source-to-Image (S2I) and Buildah.

  For more information, see [builds for Red Hat OpenShift](https://docs.redhat.com/en/documentation/builds_for_red_hat_openshift).
* Builds using `BuildConfig` objects is a declarative build process to create cloud-native apps. You can define the build process in a YAML file that you use to create a `BuildConfig` object. This definition includes attributes such as build triggers, input parameters, and source code. When deployed, the `BuildConfig` object builds a runnable image and pushes the image to a container image registry. With the `BuildConfig` object, you can create a Docker, Source-to-image (S2I), or custom build.

  For more information, see [Understanding image builds](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#understanding-image-builds).

### [1.2. OpenShift Pipelines](#openshift-pipelines) Copy linkLink copied to clipboard!

OpenShift Pipelines provides a Kubernetes-native CI/CD framework to design and run each step of the CI/CD pipeline in its own container. It can scale independently to meet the on-demand pipelines with predictable outcomes.

For more information, see [Red Hat OpenShift Pipelines](https://docs.redhat.com/en/documentation/red_hat_openshift_pipelines).

### [1.3. OpenShift GitOps](#openshift-gitops) Copy linkLink copied to clipboard!

OpenShift GitOps is an Operator that uses Argo CD as the declarative GitOps engine. It enables GitOps workflows across multicluster OpenShift and Kubernetes infrastructure. Using OpenShift GitOps, administrators can consistently configure and deploy Kubernetes-based infrastructure and applications across clusters and development lifecycles.

For more information, see [Red Hat OpenShift GitOps](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops).

### [1.4. Jenkins](#jenkins-ci-cd) Copy linkLink copied to clipboard!

Jenkins automates the process of building, testing, and deploying applications and projects. OpenShift Developer Tools provides a Jenkins image that integrates directly with OpenShift Container Platform. Jenkins can be deployed on OpenShift by using the Samples Operator templates or certified Helm chart.

For more information, see [Configuring Jenkins images](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/jenkins/#images-other-jenkins).

## [Legal Notice](#idm140366024770496) Copy linkLink copied to clipboard!

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
