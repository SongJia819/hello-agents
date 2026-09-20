---
title: "Project APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/project_apis/index
retrieved_at: 2026-09-05T05:42:45.959896+00:00
---

# Project APIs

---

OpenShift Container Platform 4.22

## Reference guide for project APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140151704456432)

**Abstract**

This document describes the OpenShift Container Platform project API objects and their detailed specifications.

---

## [Chapter 1. Project APIs](#project-apis) Copy linkLink copied to clipboard!

### [1.1. Project [project.openshift.io/v1]](#project-project-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Projects are the unit of isolation and collaboration in OpenShift. A project has one or more members, a quota on the resources that the project may consume, and the security controls on the resources in the project. Within a project, members may have different roles - project administrators can set membership, editors can create and manage the resources, and viewers can see but not access running containers. In a normal cluster project administrators are not able to alter their quotas - that is restricted to cluster administrators.

    Listing or watching projects will return only projects the user has the reader role on.

    An OpenShift project is an alternative representation of a Kubernetes namespace. Projects are exposed as editable to end users while namespaces are not. Direct creation of a project is typically restricted to administrators, while end users should use the requestproject resource.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. ProjectRequest [project.openshift.io/v1]](#projectrequest-project-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ProjectRequest is the set of options necessary to fully qualify a project request

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

## [Chapter 2. Project [project.openshift.io/v1]](#project-project-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Projects are the unit of isolation and collaboration in OpenShift. A project has one or more members, a quota on the resources that the project may consume, and the security controls on the resources in the project. Within a project, members may have different roles - project administrators can set membership, editors can create and manage the resources, and viewers can see but not access running containers. In a normal cluster project administrators are not able to alter their quotas - that is restricted to cluster administrators.

    Listing or watching projects will return only projects the user has the reader role on.

    An OpenShift project is an alternative representation of a Kubernetes namespace. Projects are exposed as editable to end users while namespaces are not. Direct creation of a project is typically restricted to administrators, while end users should use the requestproject resource.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ProjectSpec describes the attributes on a Project |
| `status` | `object` | ProjectStatus is information about the current status of a Project |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   ProjectSpec describes the attributes on a Project

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `finalizers` | `array (string)` | finalizers is an opaque list of values that must be empty to permanently remove object from storage |

Show more

#### [2.1.2. .status](#status) Copy linkLink copied to clipboard!

Description
:   ProjectStatus is information about the current status of a Project

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | [`array (NamespaceCondition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-NamespaceCondition) | Represents the latest available observations of the project current state. |
| `phase` | `string` | phase is the current lifecycle phase of the project  Possible enum values: - `"Active"` means the namespace is available for use in the system - `"Terminating"` means the namespace is undergoing graceful termination |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/project.openshift.io/v1/projects`

  + `GET`: list or watch objects of kind Project
  + `POST`: create a Project
* `/apis/project.openshift.io/v1/watch/projects`

  + `GET`: watch individual changes to a list of Project. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/project.openshift.io/v1/projects/{name}`

  + `DELETE`: delete a Project
  + `GET`: read the specified Project
  + `PATCH`: partially update the specified Project
  + `PUT`: replace the specified Project
* `/apis/project.openshift.io/v1/watch/projects/{name}`

  + `GET`: watch changes to an object of kind Project. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [2.2.1. /apis/project.openshift.io/v1/projects](#apisproject-openshift-iov1projects) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind Project

Expand

Table 2.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-project-v1-ProjectList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Project

Expand

Table 2.2. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.3. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 201 - Created | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 202 - Accepted | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/project.openshift.io/v1/watch/projects](#apisproject-openshift-iov1watchprojects) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Project. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 2.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/project.openshift.io/v1/projects/{name}](#apisproject-openshift-iov1projectsname) Copy linkLink copied to clipboard!

Expand

Table 2.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Project |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Project

Expand

Table 2.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 2.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Project

Expand

Table 2.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Project

Expand

Table 2.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 201 - Created | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Project

Expand

Table 2.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 201 - Created | [`Project`](#project-project-openshift-io-v1 "Chapter 2. Project [project.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/project.openshift.io/v1/watch/projects/{name}](#apisproject-openshift-iov1watchprojectsname) Copy linkLink copied to clipboard!

Expand

Table 2.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Project |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind Project. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. ProjectRequest [project.openshift.io/v1]](#projectrequest-project-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ProjectRequest is the set of options necessary to fully qualify a project request

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `description` | `string` | description is the description to apply to a project |
| `displayName` | `string` | displayName is the display name to apply to a project |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/project.openshift.io/v1/projectrequests`

  + `GET`: list objects of kind ProjectRequest
  + `POST`: create a ProjectRequest

#### [3.2.1. /apis/project.openshift.io/v1/projectrequests](#apisproject-openshift-iov1projectrequests) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind ProjectRequest

Expand

Table 3.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ProjectRequest

Expand

Table 3.2. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.3. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ProjectRequest`](#projectrequest-project-openshift-io-v1 "Chapter 3. ProjectRequest [project.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectRequest`](#projectrequest-project-openshift-io-v1 "Chapter 3. ProjectRequest [project.openshift.io/v1]") schema |
| 201 - Created | [`ProjectRequest`](#projectrequest-project-openshift-io-v1 "Chapter 3. ProjectRequest [project.openshift.io/v1]") schema |
| 202 - Accepted | [`ProjectRequest`](#projectrequest-project-openshift-io-v1 "Chapter 3. ProjectRequest [project.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140151704456432) Copy linkLink copied to clipboard!

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
