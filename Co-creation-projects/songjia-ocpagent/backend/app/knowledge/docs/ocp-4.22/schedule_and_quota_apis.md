---
title: "Schedule and quota APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/index
retrieved_at: 2026-09-05T05:42:50.216505+00:00
---

# Schedule and quota APIs

---

OpenShift Container Platform 4.22

## Reference guide for schedule and quota APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139879741575088)

**Abstract**

This document describes the OpenShift Container Platform schedule and quota API objects and their detailed specifications.

---

## [Chapter 1. Schedule and quota APIs](#schedule-and-quota-apis) Copy linkLink copied to clipboard!

### [1.1. AppliedClusterResourceQuota [quota.openshift.io/v1]](#appliedclusterresourcequota-quota-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   AppliedClusterResourceQuota mirrors ClusterResourceQuota at a project scope, for projection into a project. It allows a project-admin to know which ClusterResourceQuotas are applied to his project and their associated usage.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. ClusterResourceQuota [quota.openshift.io/v1]](#clusterresourcequota-quota-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterResourceQuota mirrors ResourceQuota at a cluster scope. This object is easily convertible to synthetic ResourceQuota object to allow quota evaluation re-use.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. DeviceClass [resource.k8s.io/v1]](#deviceclass-resource-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

### [1.4. FlowSchema [flowcontrol.apiserver.k8s.io/v1]](#flowschema-flowcontrol-apiserver-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher".

Type
:   `object`

### [1.5. LimitRange [v1]](#limitrange-v1-1) Copy linkLink copied to clipboard!

Description
:   LimitRange sets resource usage limits for each kind of resource in a Namespace.

Type
:   `object`

### [1.6. PriorityClass [scheduling.k8s.io/v1]](#priorityclass-scheduling-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.

Type
:   `object`

### [1.7. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfiguration represents the configuration of a priority level.

Type
:   `object`

### [1.8. ResourceQuota [v1]](#resourcequota-v1-1) Copy linkLink copied to clipboard!

Description
:   ResourceQuota sets aggregate quota restrictions enforced per namespace

Type
:   `object`

### [1.9. ResourceClaim [resource.k8s.io/v1]](#resourceclaim-resource-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

### [1.10. ResourceClaimTemplate [resource.k8s.io/v1]](#resourceclaimtemplate-resource-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   ResourceClaimTemplate is used to produce ResourceClaim objects.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

### [1.11. ResourceSlice [resource.k8s.io/v1]](#resourceslice-resource-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   ResourceSlice represents one or more resources in a pool of similar resources, managed by a common driver. A pool may span more than one ResourceSlice, and exactly how many ResourceSlices comprise a pool is determined by the driver.

    At the moment, the only supported resources are devices with attributes and capacities. Each device in a given pool, regardless of how many ResourceSlices, must have a unique name. The ResourceSlice in which a device gets published may change over time. The unique identifier for a device is the tuple <driver name>, <pool name>, <device name>.

    Whenever a driver needs to update a pool, it increments the pool.Spec.Pool.Generation number and updates all ResourceSlices with that new number and new resource definitions. A consumer must only use ResourceSlices with the highest generation number and ignore all others.

    When allocating all resources in a pool matching certain criteria or when looking for the best solution among several different alternatives, a consumer should check the number of ResourceSlices in a pool (included in each ResourceSlice) to determine whether its view of a pool is complete and if not, should wait until the driver has completed updating the pool.

    For resources that are not local to a node, the node name is not set. Instead, the driver may use a node selector to specify where the devices are available.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

## [Chapter 2. AppliedClusterResourceQuota [quota.openshift.io/v1]](#appliedclusterresourcequota-quota-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   AppliedClusterResourceQuota mirrors ClusterResourceQuota at a project scope, for projection into a project. It allows a project-admin to know which ClusterResourceQuotas are applied to his project and their associated usage.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `metadata`
    * `spec`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ClusterResourceQuotaSpec defines the desired quota restrictions |
| `status` | `object` | ClusterResourceQuotaStatus defines the actual enforced quota and its current usage |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   ClusterResourceQuotaSpec defines the desired quota restrictions

Type
:   `object`

Required
:   * `selector`
    * `quota`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `quota` | [`ResourceQuotaSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaSpec) | quota defines the desired quota |
| `selector` | `object` | ClusterResourceQuotaSelector is used to select projects. At least one of LabelSelector or AnnotationSelector must present. If only one is present, it is the only selection criteria. If both are specified, the project must match both restrictions. |

Show more

#### [2.1.2. .spec.selector](#spec-selector) Copy linkLink copied to clipboard!

Description
:   ClusterResourceQuotaSelector is used to select projects. At least one of LabelSelector or AnnotationSelector must present. If only one is present, it is the only selection criteria. If both are specified, the project must match both restrictions.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `annotations` | `object (string)` | AnnotationSelector is used to select projects by annotation. |
| `labels` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | LabelSelector is used to select projects by label. |

Show more

#### [2.1.3. .status](#status) Copy linkLink copied to clipboard!

Description
:   ClusterResourceQuotaStatus defines the actual enforced quota and its current usage

Type
:   `object`

Required
:   * `total`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `namespaces` | `array` | namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project. |
| `namespaces[]` | `object` | ResourceQuotaStatusByNamespace gives status for a particular project |
| `total` | [`ResourceQuotaStatus`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaStatus) | total defines the actual enforced quota and its current usage across all projects |

Show more

#### [2.1.4. .status.namespaces](#status-namespaces) Copy linkLink copied to clipboard!

Description
:   namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project.

Type
:   `array`

#### [2.1.5. .status.namespaces[]](#status-namespaces-2) Copy linkLink copied to clipboard!

Description
:   ResourceQuotaStatusByNamespace gives status for a particular project

Type
:   `object`

Required
:   * `namespace`
    * `status`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `namespace` | `string` | namespace the project this status applies to |
| `status` | [`ResourceQuotaStatus`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaStatus) | status indicates how many resources have been consumed by this project |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/quota.openshift.io/v1/appliedclusterresourcequotas`

  + `GET`: list objects of kind AppliedClusterResourceQuota
* `/apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas`

  + `GET`: list objects of kind AppliedClusterResourceQuota
* `/apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}`

  + `GET`: read the specified AppliedClusterResourceQuota

#### [2.2.1. /apis/quota.openshift.io/v1/appliedclusterresourcequotas](#apisquota-openshift-iov1appliedclusterresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind AppliedClusterResourceQuota

Expand

Table 2.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`AppliedClusterResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas](#apisquota-openshift-iov1namespacesnamespaceappliedclusterresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind AppliedClusterResourceQuota

Expand

Table 2.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`AppliedClusterResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}](#apisquota-openshift-iov1namespacesnamespaceappliedclusterresourcequotasname) Copy linkLink copied to clipboard!

Expand

Table 2.3. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the AppliedClusterResourceQuota |

Show more

HTTP method
:   `GET`

Description
:   read the specified AppliedClusterResourceQuota

Expand

Table 2.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`AppliedClusterResourceQuota`](#appliedclusterresourcequota-quota-openshift-io-v1 "Chapter 2. AppliedClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]](#clusterresourcequota-quota-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterResourceQuota mirrors ResourceQuota at a cluster scope. This object is easily convertible to synthetic ResourceQuota object to allow quota evaluation re-use.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `metadata`
    * `spec`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec defines the desired quota |
| `status` | `object` | status defines the actual enforced quota and its current usage |

Show more

#### [3.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   spec defines the desired quota

Type
:   `object`

Required
:   * `quota`
    * `selector`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `quota` | `object` | quota defines the desired quota |
| `selector` | `object` | selector is the selector used to match projects. It should only select active projects on the scale of dozens (though it can select many more less active projects). These projects will contend on object creation through this resource. |

Show more

#### [3.1.2. .spec.quota](#spec-quota) Copy linkLink copied to clipboard!

Description
:   quota defines the desired quota

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hard` | `integer-or-string` | hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `scopeSelector` | `object` | scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. |
| `scopes` | `array (string)` | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. |

Show more

#### [3.1.3. .spec.quota.scopeSelector](#spec-quota-scopeselector) Copy linkLink copied to clipboard!

Description
:   scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchExpressions` | `array` | A list of scope selector requirements by scope of the resources. |
| `matchExpressions[]` | `object` | A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values. |

Show more

#### [3.1.4. .spec.quota.scopeSelector.matchExpressions](#spec-quota-scopeselector-matchexpressions) Copy linkLink copied to clipboard!

Description
:   A list of scope selector requirements by scope of the resources.

Type
:   `array`

#### [3.1.5. .spec.quota.scopeSelector.matchExpressions[]](#spec-quota-scopeselector-matchexpressions-2) Copy linkLink copied to clipboard!

Description
:   A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.

Type
:   `object`

Required
:   * `operator`
    * `scopeName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `operator` | `string` | Represents a scope’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. |
| `scopeName` | `string` | The name of the scope that the selector applies to. |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

Show more

#### [3.1.6. .spec.selector](#spec-selector-2) Copy linkLink copied to clipboard!

Description
:   selector is the selector used to match projects. It should only select active projects on the scale of dozens (though it can select many more less active projects). These projects will contend on object creation through this resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `annotations` | `undefined (string)` | AnnotationSelector is used to select projects by annotation. |
| `labels` | `` | LabelSelector is used to select projects by label. |

Show more

#### [3.1.7. .status](#status-2) Copy linkLink copied to clipboard!

Description
:   status defines the actual enforced quota and its current usage

Type
:   `object`

Required
:   * `total`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `namespaces` | `` | namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project. |
| `total` | `object` | total defines the actual enforced quota and its current usage across all projects |

Show more

#### [3.1.8. .status.total](#status-total) Copy linkLink copied to clipboard!

Description
:   total defines the actual enforced quota and its current usage across all projects

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hard` | `integer-or-string` | Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `used` | `integer-or-string` | Used is the current observed total usage of the resource in the namespace. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/quota.openshift.io/v1/clusterresourcequotas`

  + `DELETE`: delete collection of ClusterResourceQuota
  + `GET`: list objects of kind ClusterResourceQuota
  + `POST`: create a ClusterResourceQuota
* `/apis/quota.openshift.io/v1/watch/clusterresourcequotas`

  + `GET`: watch individual changes to a list of ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/quota.openshift.io/v1/clusterresourcequotas/{name}`

  + `DELETE`: delete a ClusterResourceQuota
  + `GET`: read the specified ClusterResourceQuota
  + `PATCH`: partially update the specified ClusterResourceQuota
  + `PUT`: replace the specified ClusterResourceQuota
* `/apis/quota.openshift.io/v1/watch/clusterresourcequotas/{name}`

  + `GET`: watch changes to an object of kind ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status`

  + `GET`: read status of the specified ClusterResourceQuota
  + `PATCH`: partially update status of the specified ClusterResourceQuota
  + `PUT`: replace status of the specified ClusterResourceQuota

#### [3.2.1. /apis/quota.openshift.io/v1/clusterresourcequotas](#apisquota-openshift-iov1clusterresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ClusterResourceQuota

Expand

Table 3.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ClusterResourceQuota

Expand

Table 3.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-quota-v1-ClusterResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterResourceQuota

Expand

Table 3.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 201 - Created | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 202 - Accepted | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/quota.openshift.io/v1/watch/clusterresourcequotas](#apisquota-openshift-iov1watchclusterresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/quota.openshift.io/v1/clusterresourcequotas/{name}](#apisquota-openshift-iov1clusterresourcequotasname) Copy linkLink copied to clipboard!

Expand

Table 3.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterResourceQuota |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterResourceQuota

Expand

Table 3.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ClusterResourceQuota

Expand

Table 3.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterResourceQuota

Expand

Table 3.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterResourceQuota

Expand

Table 3.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 201 - Created | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/quota.openshift.io/v1/watch/clusterresourcequotas/{name}](#apisquota-openshift-iov1watchclusterresourcequotasname) Copy linkLink copied to clipboard!

Expand

Table 3.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterResourceQuota |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.5. /apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status](#apisquota-openshift-iov1clusterresourcequotasnamestatus) Copy linkLink copied to clipboard!

Expand

Table 3.18. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterResourceQuota |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ClusterResourceQuota

Expand

Table 3.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ClusterResourceQuota

Expand

Table 3.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ClusterResourceQuota

Expand

Table 3.22. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.23. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.24. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 201 - Created | [`ClusterResourceQuota`](#clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota [quota.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. DeviceClass [resource.k8s.io/v1]](#deviceclass-resource-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

Required
:   * `spec`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata |
| `spec` | `object` | DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it. |

Show more

#### [4.1.1. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `config` | `array` | Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim. |
| `config[]` | `object` | DeviceClassConfiguration is used in DeviceClass. |
| `extendedResourceName` | `string` | ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod’s extended resource requests. It has the same format as the name of a pod’s extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod’s extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.  This is an alpha field. |
| `selectors` | `array` | Each selector must be satisfied by a device which is claimed via this class. |
| `selectors[]` | `object` | DeviceSelector must have exactly one field set. |

Show more

#### [4.1.2. .spec.config](#spec-config) Copy linkLink copied to clipboard!

Description
:   Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.

    They are passed to the driver, but are not considered while allocating the claim.

Type
:   `array`

#### [4.1.3. .spec.config[]](#spec-config-2) Copy linkLink copied to clipboard!

Description
:   DeviceClassConfiguration is used in DeviceClass.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `opaque` | `object` | OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor. |

Show more

#### [4.1.4. .spec.config[].opaque](#spec-config-opaque) Copy linkLink copied to clipboard!

Description
:   OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
:   `object`

Required
:   * `driver`
    * `parameters`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
| `parameters` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki. |

Show more

#### [4.1.5. .spec.selectors](#spec-selectors) Copy linkLink copied to clipboard!

Description
:   Each selector must be satisfied by a device which is claimed via this class.

Type
:   `array`

#### [4.1.6. .spec.selectors[]](#spec-selectors-2) Copy linkLink copied to clipboard!

Description
:   DeviceSelector must have exactly one field set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

Show more

#### [4.1.7. .spec.selectors[].cel](#spec-selectors-cel) Copy linkLink copied to clipboard!

Description
:   CELDeviceSelector contains a CEL expression for selecting a device.

Type
:   `object`

Required
:   * `expression`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `expression` | `string` | Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.  The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).  Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:  device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules  The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.  The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.  A robust expression should check for the existence of attributes before referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:  cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/resource.k8s.io/v1/deviceclasses`

  + `DELETE`: delete collection of DeviceClass
  + `GET`: list or watch objects of kind DeviceClass
  + `POST`: create a DeviceClass
* `/apis/resource.k8s.io/v1/watch/deviceclasses`

  + `GET`: watch individual changes to a list of DeviceClass. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/resource.k8s.io/v1/deviceclasses/{name}`

  + `DELETE`: delete a DeviceClass
  + `GET`: read the specified DeviceClass
  + `PATCH`: partially update the specified DeviceClass
  + `PUT`: replace the specified DeviceClass
* `/apis/resource.k8s.io/v1/watch/deviceclasses/{name}`

  + `GET`: watch changes to an object of kind DeviceClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [4.2.1. /apis/resource.k8s.io/v1/deviceclasses](#apisresource-k8s-iov1deviceclasses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of DeviceClass

Expand

Table 4.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind DeviceClass

Expand

Table 4.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DeviceClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-DeviceClassList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a DeviceClass

Expand

Table 4.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 4.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 201 - Created | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/resource.k8s.io/v1/watch/deviceclasses](#apisresource-k8s-iov1watchdeviceclasses) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of DeviceClass. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/resource.k8s.io/v1/deviceclasses/{name}](#apisresource-k8s-iov1deviceclassesname) Copy linkLink copied to clipboard!

Expand

Table 4.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the DeviceClass |

Show more

HTTP method
:   `DELETE`

Description
:   delete a DeviceClass

Expand

Table 4.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified DeviceClass

Expand

Table 4.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified DeviceClass

Expand

Table 4.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 201 - Created | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified DeviceClass

Expand

Table 4.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 4.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 201 - Created | [`DeviceClass`](#deviceclass-resource-k8s-io-v1 "Chapter 4. DeviceClass [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.4. /apis/resource.k8s.io/v1/watch/deviceclasses/{name}](#apisresource-k8s-iov1watchdeviceclassesname) Copy linkLink copied to clipboard!

Expand

Table 4.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the DeviceClass |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind DeviceClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 4.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]](#flowschema-flowcontrol-apiserver-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher".

Type
:   `object`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | `metadata` is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | FlowSchemaSpec describes how the FlowSchema’s specification looks like. |
| `status` | `object` | FlowSchemaStatus represents the current state of a FlowSchema. |

Show more

#### [5.1.1. .spec](#spec-4) Copy linkLink copied to clipboard!

Description
:   FlowSchemaSpec describes how the FlowSchema’s specification looks like.

Type
:   `object`

Required
:   * `priorityLevelConfiguration`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `distinguisherMethod` | `object` | FlowDistinguisherMethod specifies the method of a flow distinguisher. |
| `matchingPrecedence` | `integer` | `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence. Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. |
| `priorityLevelConfiguration` | `object` | PriorityLevelConfigurationReference contains information that points to the "request-priority" being used. |
| `rules` | `array` | `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. |
| `rules[]` | `object` | PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request. |

Show more

#### [5.1.2. .spec.distinguisherMethod](#spec-distinguishermethod) Copy linkLink copied to clipboard!

Description
:   FlowDistinguisherMethod specifies the method of a flow distinguisher.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required. |

Show more

#### [5.1.3. .spec.priorityLevelConfiguration](#spec-prioritylevelconfiguration) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfigurationReference contains information that points to the "request-priority" being used.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | `name` is the name of the priority level configuration being referenced Required. |

Show more

#### [5.1.4. .spec.rules](#spec-rules) Copy linkLink copied to clipboard!

Description
:   `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema.

Type
:   `array`

#### [5.1.5. .spec.rules[]](#spec-rules-2) Copy linkLink copied to clipboard!

Description
:   PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request.

Type
:   `object`

Required
:   * `subjects`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nonResourceRules` | `array` | `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. |
| `nonResourceRules[]` | `object` | NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request. |
| `resourceRules` | `array` | `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty. |
| `resourceRules[]` | `object` | ResourcePolicyRule is a predicate that matches some resource requests, testing the request’s verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request’s namespace. |
| `subjects` | `array` | subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. |
| `subjects[]` | `object` | Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account. |

Show more

#### [5.1.6. .spec.rules[].nonResourceRules](#spec-rules-nonresourcerules) Copy linkLink copied to clipboard!

Description
:   `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.

Type
:   `array`

#### [5.1.7. .spec.rules[].nonResourceRules[]](#spec-rules-nonresourcerules-2) Copy linkLink copied to clipboard!

Description
:   NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request.

Type
:   `object`

Required
:   * `verbs`
    * `nonResourceURLs`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nonResourceURLs` | `array (string)` | `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example: - "/healthz" is legal - "/hea\*" is illegal - "/hea" is legal but matches nothing - "/hea/**" also matches nothing - "/healthz/**" matches all per-component health checks. "\*" matches all non-resource urls. if it is present, it must be the only entry. Required. |
| `verbs` | `array (string)` | `verbs` is a list of matching verbs and may not be empty. "\*" matches all verbs. If it is present, it must be the only entry. Required. |

Show more

#### [5.1.8. .spec.rules[].resourceRules](#spec-rules-resourcerules) Copy linkLink copied to clipboard!

Description
:   `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.

Type
:   `array`

#### [5.1.9. .spec.rules[].resourceRules[]](#spec-rules-resourcerules-2) Copy linkLink copied to clipboard!

Description
:   ResourcePolicyRule is a predicate that matches some resource requests, testing the request’s verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request’s namespace.

Type
:   `object`

Required
:   * `verbs`
    * `apiGroups`
    * `resources`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroups` | `array (string)` | `apiGroups` is a list of matching API groups and may not be empty. "\*" matches all API groups and, if present, must be the only entry. Required. |
| `clusterScope` | `boolean` | `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list. |
| `namespaces` | `array (string)` | `namespaces` is a list of target namespaces that restricts matches. A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "**". Note that "**" matches any specified namespace but does not match a request that *does not specify* a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true. |
| `resources` | `array (string)` | `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource. For example, [ "services", "nodes/status" ]. This list may not be empty. "\*" matches all resources and, if present, must be the only entry. Required. |
| `verbs` | `array (string)` | `verbs` is a list of matching verbs and may not be empty. "\*" matches all verbs and, if present, must be the only entry. Required. |

Show more

#### [5.1.10. .spec.rules[].subjects](#spec-rules-subjects) Copy linkLink copied to clipboard!

Description
:   subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.

Type
:   `array`

#### [5.1.11. .spec.rules[].subjects[]](#spec-rules-subjects-2) Copy linkLink copied to clipboard!

Description
:   Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.

Type
:   `object`

Required
:   * `kind`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `object` | GroupSubject holds detailed information for group-kind subject. |
| `kind` | `string` | `kind` indicates which one of the other fields is non-empty. Required |
| `serviceAccount` | `object` | ServiceAccountSubject holds detailed information for service-account-kind subject. |
| `user` | `object` | UserSubject holds detailed information for user-kind subject. |

Show more

#### [5.1.12. .spec.rules[].subjects[].group](#spec-rules-subjects-group) Copy linkLink copied to clipboard!

Description
:   GroupSubject holds detailed information for group-kind subject.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the user group that matches, or "\*" to match all user groups. See <https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go> for some well-known group names. Required. |

Show more

#### [5.1.13. .spec.rules[].subjects[].serviceAccount](#spec-rules-subjects-serviceaccount) Copy linkLink copied to clipboard!

Description
:   ServiceAccountSubject holds detailed information for service-account-kind subject.

Type
:   `object`

Required
:   * `namespace`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | `name` is the name of matching ServiceAccount objects, or "\*" to match regardless of name. Required. |
| `namespace` | `string` | `namespace` is the namespace of matching ServiceAccount objects. Required. |

Show more

#### [5.1.14. .spec.rules[].subjects[].user](#spec-rules-subjects-user) Copy linkLink copied to clipboard!

Description
:   UserSubject holds detailed information for user-kind subject.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | `name` is the username that matches, or "\*" to match all usernames. Required. |

Show more

#### [5.1.15. .status](#status-3) Copy linkLink copied to clipboard!

Description
:   FlowSchemaStatus represents the current state of a FlowSchema.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | `conditions` is a list of the current states of FlowSchema. |
| `conditions[]` | `object` | FlowSchemaCondition describes conditions for a FlowSchema. |

Show more

#### [5.1.16. .status.conditions](#status-conditions) Copy linkLink copied to clipboard!

Description
:   `conditions` is a list of the current states of FlowSchema.

Type
:   `array`

#### [5.1.17. .status.conditions[]](#status-conditions-2) Copy linkLink copied to clipboard!

Description
:   FlowSchemaCondition describes conditions for a FlowSchema.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | `lastTransitionTime` is the last time the condition transitioned from one status to another. |
| `message` | `string` | `message` is a human-readable message indicating details about last transition. |
| `reason` | `string` | `reason` is a unique, one-word, CamelCase reason for the condition’s last transition. |
| `status` | `string` | `status` is the status of the condition. Can be True, False, Unknown. Required. |
| `type` | `string` | `type` is the type of the condition. Required. |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/flowcontrol.apiserver.k8s.io/v1/flowschemas`

  + `DELETE`: delete collection of FlowSchema
  + `GET`: list or watch objects of kind FlowSchema
  + `POST`: create a FlowSchema
* `/apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas`

  + `GET`: watch individual changes to a list of FlowSchema. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}`

  + `DELETE`: delete a FlowSchema
  + `GET`: read the specified FlowSchema
  + `PATCH`: partially update the specified FlowSchema
  + `PUT`: replace the specified FlowSchema
* `/apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas/{name}`

  + `GET`: watch changes to an object of kind FlowSchema. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status`

  + `GET`: read status of the specified FlowSchema
  + `PATCH`: partially update status of the specified FlowSchema
  + `PUT`: replace status of the specified FlowSchema

#### [5.2.1. /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas](#apisflowcontrol-apiserver-k8s-iov1flowschemas) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of FlowSchema

Expand

Table 5.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 5.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind FlowSchema

Expand

Table 5.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchemaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-flowcontrol-v1-FlowSchemaList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a FlowSchema

Expand

Table 5.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |  |

Show more

Expand

Table 5.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 202 - Accepted | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas](#apisflowcontrol-apiserver-k8s-iov1watchflowschemas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of FlowSchema. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}](#apisflowcontrol-apiserver-k8s-iov1flowschemasname) Copy linkLink copied to clipboard!

Expand

Table 5.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the FlowSchema |

Show more

HTTP method
:   `DELETE`

Description
:   delete a FlowSchema

Expand

Table 5.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 5.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified FlowSchema

Expand

Table 5.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified FlowSchema

Expand

Table 5.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified FlowSchema

Expand

Table 5.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |  |

Show more

Expand

Table 5.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.4. /apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas/{name}](#apisflowcontrol-apiserver-k8s-iov1watchflowschemasname) Copy linkLink copied to clipboard!

Expand

Table 5.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the FlowSchema |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind FlowSchema. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.5. /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status](#apisflowcontrol-apiserver-k8s-iov1flowschemasnamestatus) Copy linkLink copied to clipboard!

Expand

Table 5.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the FlowSchema |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified FlowSchema

Expand

Table 5.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified FlowSchema

Expand

Table 5.21. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified FlowSchema

Expand

Table 5.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.24. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |  |

Show more

Expand

Table 5.25. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`FlowSchema`](#flowschema-flowcontrol-apiserver-k8s-io-v1 "Chapter 5. FlowSchema [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. LimitRange [v1]](#limitrange-v1) Copy linkLink copied to clipboard!

Description
:   LimitRange sets resource usage limits for each kind of resource in a Namespace.

Type
:   `object`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | LimitRangeSpec defines a min/max usage limit for resources that match on kind. |

Show more

#### [6.1.1. .spec](#spec-5) Copy linkLink copied to clipboard!

Description
:   LimitRangeSpec defines a min/max usage limit for resources that match on kind.

Type
:   `object`

Required
:   * `limits`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `limits` | `array` | Limits is the list of LimitRangeItem objects that are enforced. |
| `limits[]` | `object` | LimitRangeItem defines a min/max usage limit for any resource that matches on kind. |

Show more

#### [6.1.2. .spec.limits](#spec-limits) Copy linkLink copied to clipboard!

Description
:   Limits is the list of LimitRangeItem objects that are enforced.

Type
:   `array`

#### [6.1.3. .spec.limits[]](#spec-limits-2) Copy linkLink copied to clipboard!

Description
:   LimitRangeItem defines a min/max usage limit for any resource that matches on kind.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `default` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Default resource requirement limit value by resource name if resource limit is omitted. |
| `defaultRequest` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. |
| `max` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Max usage constraints on this kind by resource name. |
| `maxLimitRequestRatio` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. |
| `min` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Min usage constraints on this kind by resource name. |
| `type` | `string` | Type of resource that this limit applies to. |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/limitranges`

  + `GET`: list or watch objects of kind LimitRange
* `/api/v1/watch/limitranges`

  + `GET`: watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/limitranges`

  + `DELETE`: delete collection of LimitRange
  + `GET`: list or watch objects of kind LimitRange
  + `POST`: create a LimitRange
* `/api/v1/watch/namespaces/{namespace}/limitranges`

  + `GET`: watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/limitranges/{name}`

  + `DELETE`: delete a LimitRange
  + `GET`: read the specified LimitRange
  + `PATCH`: partially update the specified LimitRange
  + `PUT`: replace the specified LimitRange
* `/api/v1/watch/namespaces/{namespace}/limitranges/{name}`

  + `GET`: watch changes to an object of kind LimitRange. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [6.2.1. /api/v1/limitranges](#apiv1limitranges) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind LimitRange

Expand

Table 6.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LimitRangeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-LimitRangeList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /api/v1/watch/limitranges](#apiv1watchlimitranges) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.3. /api/v1/namespaces/{namespace}/limitranges](#apiv1namespacesnamespacelimitranges) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of LimitRange

Expand

Table 6.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 6.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind LimitRange

Expand

Table 6.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LimitRangeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-LimitRangeList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a LimitRange

Expand

Table 6.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |  |

Show more

Expand

Table 6.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 201 - Created | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 202 - Accepted | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.4. /api/v1/watch/namespaces/{namespace}/limitranges](#apiv1watchnamespacesnamespacelimitranges) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 6.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.5. /api/v1/namespaces/{namespace}/limitranges/{name}](#apiv1namespacesnamespacelimitrangesname) Copy linkLink copied to clipboard!

Expand

Table 6.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the LimitRange |

Show more

HTTP method
:   `DELETE`

Description
:   delete a LimitRange

Expand

Table 6.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 6.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified LimitRange

Expand

Table 6.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified LimitRange

Expand

Table 6.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 201 - Created | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified LimitRange

Expand

Table 6.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |  |

Show more

Expand

Table 6.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 201 - Created | [`LimitRange`](#limitrange-v1 "Chapter 6. LimitRange [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.6. /api/v1/watch/namespaces/{namespace}/limitranges/{name}](#apiv1watchnamespacesnamespacelimitrangesname) Copy linkLink copied to clipboard!

Expand

Table 6.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the LimitRange |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind LimitRange. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 6.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 7. PriorityClass [scheduling.k8s.io/v1]](#priorityclass-scheduling-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.

Type
:   `object`

Required
:   * `value`

### [7.1. Specification](#specification-6) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `description` | `string` | description is an arbitrary string that usually provides guidelines on when this priority class should be used. |
| `globalDefault` | `boolean` | globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `preemptionPolicy` | `string` | preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.  Possible enum values: - `"Never"` means that pod never preempts other pods with lower priority. - `"PreemptLowerPriority"` means that pod can preempt other pods with lower priority. |
| `value` | `integer` | value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec. |

Show more

### [7.2. API endpoints](#api-endpoints-6) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/scheduling.k8s.io/v1/priorityclasses`

  + `DELETE`: delete collection of PriorityClass
  + `GET`: list or watch objects of kind PriorityClass
  + `POST`: create a PriorityClass
* `/apis/scheduling.k8s.io/v1/watch/priorityclasses`

  + `GET`: watch individual changes to a list of PriorityClass. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/scheduling.k8s.io/v1/priorityclasses/{name}`

  + `DELETE`: delete a PriorityClass
  + `GET`: read the specified PriorityClass
  + `PATCH`: partially update the specified PriorityClass
  + `PUT`: replace the specified PriorityClass
* `/apis/scheduling.k8s.io/v1/watch/priorityclasses/{name}`

  + `GET`: watch changes to an object of kind PriorityClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [7.2.1. /apis/scheduling.k8s.io/v1/priorityclasses](#apisscheduling-k8s-iov1priorityclasses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PriorityClass

Expand

Table 7.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 7.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind PriorityClass

Expand

Table 7.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-scheduling-v1-PriorityClassList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PriorityClass

Expand

Table 7.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |  |

Show more

Expand

Table 7.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 201 - Created | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 202 - Accepted | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.2. /apis/scheduling.k8s.io/v1/watch/priorityclasses](#apisscheduling-k8s-iov1watchpriorityclasses) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PriorityClass. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 7.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.3. /apis/scheduling.k8s.io/v1/priorityclasses/{name}](#apisscheduling-k8s-iov1priorityclassesname) Copy linkLink copied to clipboard!

Expand

Table 7.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PriorityClass |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PriorityClass

Expand

Table 7.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 7.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PriorityClass

Expand

Table 7.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PriorityClass

Expand

Table 7.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 201 - Created | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PriorityClass

Expand

Table 7.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |  |

Show more

Expand

Table 7.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 201 - Created | [`PriorityClass`](#priorityclass-scheduling-k8s-io-v1 "Chapter 7. PriorityClass [scheduling.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.4. /apis/scheduling.k8s.io/v1/watch/priorityclasses/{name}](#apisscheduling-k8s-iov1watchpriorityclassesname) Copy linkLink copied to clipboard!

Expand

Table 7.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PriorityClass |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind PriorityClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 7.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfiguration represents the configuration of a priority level.

Type
:   `object`

### [8.1. Specification](#specification-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | `metadata` is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PriorityLevelConfigurationSpec specifies the configuration of a priority level. |
| `status` | `object` | PriorityLevelConfigurationStatus represents the current state of a "request-priority". |

Show more

#### [8.1.1. .spec](#spec-6) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfigurationSpec specifies the configuration of a priority level.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exempt` | `object` | ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`. |
| `limited` | `object` | LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues: - How are requests for this priority level limited? - What should be done with requests that exceed the limit? |
| `type` | `string` | `type` indicates whether this priority level is subject to limitation on request execution. A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels. A value of `"Limited"` means that (a) requests of this priority level *are* subject to limits and (b) some of the server’s limited capacity is made available exclusively to this priority level. Required. |

Show more

#### [8.1.2. .spec.exempt](#spec-exempt) Copy linkLink copied to clipboard!

Description
:   ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lendablePercent` | `integer` | `lendablePercent` prescribes the fraction of the level’s NominalCL that can be borrowed by other priority levels. This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level’s LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) \* lendablePercent(i)/100.0 ) |
| `nominalConcurrencyShares` | `integer` | `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server’s concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:  NominalCL(i) = ceil( ServerCL \* NCS(i) / sum\_ncs ) sum\_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero. |

Show more

#### [8.1.3. .spec.limited](#spec-limited) Copy linkLink copied to clipboard!

Description
:   LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues: - How are requests for this priority level limited? - What should be done with requests that exceed the limit?

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `borrowingLimitPercent` | `integer` | `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level’s BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level’s nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.  BorrowingCL(i) = round( NominalCL(i) \* borrowingLimitPercent(i)/100.0 )  The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite. |
| `lendablePercent` | `integer` | `lendablePercent` prescribes the fraction of the level’s NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level’s LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) \* lendablePercent(i)/100.0 ) |
| `limitResponse` | `object` | LimitResponse defines how to handle requests that can not be executed right now. |
| `nominalConcurrencyShares` | `integer` | `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server’s concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:  NominalCL(i) = ceil( ServerCL \* NCS(i) / sum\_ncs ) sum\_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level.  If not specified, this field defaults to a value of 30.  Setting this field to zero supports the construction of a "jail" for this priority level that is used to hold some request(s) |

Show more

#### [8.1.4. .spec.limited.limitResponse](#spec-limited-limitresponse) Copy linkLink copied to clipboard!

Description
:   LimitResponse defines how to handle requests that can not be executed right now.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `queuing` | `object` | QueuingConfiguration holds the configuration parameters for queuing |
| `type` | `string` | `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required. |

Show more

#### [8.1.5. .spec.limited.limitResponse.queuing](#spec-limited-limitresponse-queuing) Copy linkLink copied to clipboard!

Description
:   QueuingConfiguration holds the configuration parameters for queuing

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `handSize` | `integer` | `handSize` is a small positive number that configures the shuffle sharding of requests into queues. When enqueuing a request at this priority level the request’s flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here. The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues). See the user-facing documentation for more extensive guidance on setting this field. This field has a default value of 8. |
| `queueLengthLimit` | `integer` | `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected. This value must be positive. If not specified, it will be defaulted to 50. |
| `queues` | `integer` | `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive. Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant. This field has a default value of 64. |

Show more

#### [8.1.6. .status](#status-4) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfigurationStatus represents the current state of a "request-priority".

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | `conditions` is the current state of "request-priority". |
| `conditions[]` | `object` | PriorityLevelConfigurationCondition defines the condition of priority level. |

Show more

#### [8.1.7. .status.conditions](#status-conditions-3) Copy linkLink copied to clipboard!

Description
:   `conditions` is the current state of "request-priority".

Type
:   `array`

#### [8.1.8. .status.conditions[]](#status-conditions-4) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfigurationCondition defines the condition of priority level.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | `lastTransitionTime` is the last time the condition transitioned from one status to another. |
| `message` | `string` | `message` is a human-readable message indicating details about last transition. |
| `reason` | `string` | `reason` is a unique, one-word, CamelCase reason for the condition’s last transition. |
| `status` | `string` | `status` is the status of the condition. Can be True, False, Unknown. Required. |
| `type` | `string` | `type` is the type of the condition. Required. |

Show more

### [8.2. API endpoints](#api-endpoints-7) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations`

  + `DELETE`: delete collection of PriorityLevelConfiguration
  + `GET`: list or watch objects of kind PriorityLevelConfiguration
  + `POST`: create a PriorityLevelConfiguration
* `/apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations`

  + `GET`: watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}`

  + `DELETE`: delete a PriorityLevelConfiguration
  + `GET`: read the specified PriorityLevelConfiguration
  + `PATCH`: partially update the specified PriorityLevelConfiguration
  + `PUT`: replace the specified PriorityLevelConfiguration
* `/apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations/{name}`

  + `GET`: watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status`

  + `GET`: read status of the specified PriorityLevelConfiguration
  + `PATCH`: partially update status of the specified PriorityLevelConfiguration
  + `PUT`: replace status of the specified PriorityLevelConfiguration

#### [8.2.1. /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations](#apisflowcontrol-apiserver-k8s-iov1prioritylevelconfigurations) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PriorityLevelConfiguration

Expand

Table 8.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 8.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind PriorityLevelConfiguration

Expand

Table 8.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfigurationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-flowcontrol-v1-PriorityLevelConfigurationList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PriorityLevelConfiguration

Expand

Table 8.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |  |

Show more

Expand

Table 8.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 202 - Accepted | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.2. /apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations](#apisflowcontrol-apiserver-k8s-iov1watchprioritylevelconfigurations) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 8.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.3. /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}](#apisflowcontrol-apiserver-k8s-iov1prioritylevelconfigurationsname) Copy linkLink copied to clipboard!

Expand

Table 8.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PriorityLevelConfiguration |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PriorityLevelConfiguration

Expand

Table 8.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 8.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PriorityLevelConfiguration

Expand

Table 8.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PriorityLevelConfiguration

Expand

Table 8.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PriorityLevelConfiguration

Expand

Table 8.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |  |

Show more

Expand

Table 8.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.4. /apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations/{name}](#apisflowcontrol-apiserver-k8s-iov1watchprioritylevelconfigurationsname) Copy linkLink copied to clipboard!

Expand

Table 8.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PriorityLevelConfiguration |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 8.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.5. /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status](#apisflowcontrol-apiserver-k8s-iov1prioritylevelconfigurationsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 8.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PriorityLevelConfiguration |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified PriorityLevelConfiguration

Expand

Table 8.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified PriorityLevelConfiguration

Expand

Table 8.21. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified PriorityLevelConfiguration

Expand

Table 8.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.24. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |  |

Show more

Expand

Table 8.25. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 201 - Created | [`PriorityLevelConfiguration`](#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration [flowcontrol.apiserver.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 9. ResourceQuota [v1]](#resourcequota-v1) Copy linkLink copied to clipboard!

Description
:   ResourceQuota sets aggregate quota restrictions enforced per namespace

Type
:   `object`

### [9.1. Specification](#specification-8) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ResourceQuotaSpec defines the desired hard limits to enforce for Quota. |
| `status` | `object` | ResourceQuotaStatus defines the enforced hard limits and observed use. |

Show more

#### [9.1.1. .spec](#spec-7) Copy linkLink copied to clipboard!

Description
:   ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hard` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `scopeSelector` | `object` | A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements. |
| `scopes` | `array (string)` | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. |

Show more

#### [9.1.2. .spec.scopeSelector](#spec-scopeselector) Copy linkLink copied to clipboard!

Description
:   A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchExpressions` | `array` | A list of scope selector requirements by scope of the resources. |
| `matchExpressions[]` | `object` | A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values. |

Show more

#### [9.1.3. .spec.scopeSelector.matchExpressions](#spec-scopeselector-matchexpressions) Copy linkLink copied to clipboard!

Description
:   A list of scope selector requirements by scope of the resources.

Type
:   `array`

#### [9.1.4. .spec.scopeSelector.matchExpressions[]](#spec-scopeselector-matchexpressions-2) Copy linkLink copied to clipboard!

Description
:   A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.

Type
:   `object`

Required
:   * `scopeName`
    * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `operator` | `string` | Represents a scope’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.  Possible enum values: - `"DoesNotExist"` - `"Exists"` - `"In"` - `"NotIn"` |
| `scopeName` | `string` | The name of the scope that the selector applies to.  Possible enum values: - `"BestEffort"` Match all pod objects that have best effort quality of service - `"CrossNamespacePodAffinity"` Match all pod objects that have cross-namespace pod (anti)affinity mentioned. - `"NotBestEffort"` Match all pod objects that do not have best effort quality of service - `"NotTerminating"` Match all pod objects where spec.activeDeadlineSeconds is nil - `"PriorityClass"` Match all pod objects that have priority class mentioned - `"Terminating"` Match all pod objects where spec.activeDeadlineSeconds >=0 - `"VolumeAttributesClass"` Match all pvc objects that have volume attributes class mentioned. |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

Show more

#### [9.1.5. .status](#status-5) Copy linkLink copied to clipboard!

Description
:   ResourceQuotaStatus defines the enforced hard limits and observed use.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hard` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `used` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Used is the current observed total usage of the resource in the namespace. |

Show more

### [9.2. API endpoints](#api-endpoints-8) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/resourcequotas`

  + `GET`: list or watch objects of kind ResourceQuota
* `/api/v1/watch/resourcequotas`

  + `GET`: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/resourcequotas`

  + `DELETE`: delete collection of ResourceQuota
  + `GET`: list or watch objects of kind ResourceQuota
  + `POST`: create a ResourceQuota
* `/api/v1/watch/namespaces/{namespace}/resourcequotas`

  + `GET`: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/resourcequotas/{name}`

  + `DELETE`: delete a ResourceQuota
  + `GET`: read the specified ResourceQuota
  + `PATCH`: partially update the specified ResourceQuota
  + `PUT`: replace the specified ResourceQuota
* `/api/v1/watch/namespaces/{namespace}/resourcequotas/{name}`

  + `GET`: watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/api/v1/namespaces/{namespace}/resourcequotas/{name}/status`

  + `GET`: read status of the specified ResourceQuota
  + `PATCH`: partially update status of the specified ResourceQuota
  + `PUT`: replace status of the specified ResourceQuota

#### [9.2.1. /api/v1/resourcequotas](#apiv1resourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceQuota

Expand

Table 9.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.2. /api/v1/watch/resourcequotas](#apiv1watchresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 9.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.3. /api/v1/namespaces/{namespace}/resourcequotas](#apiv1namespacesnamespaceresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ResourceQuota

Expand

Table 9.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 9.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceQuota

Expand

Table 9.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ResourceQuota

Expand

Table 9.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |  |

Show more

Expand

Table 9.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 201 - Created | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 202 - Accepted | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.4. /api/v1/watch/namespaces/{namespace}/resourcequotas](#apiv1watchnamespacesnamespaceresourcequotas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 9.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.5. /api/v1/namespaces/{namespace}/resourcequotas/{name}](#apiv1namespacesnamespaceresourcequotasname) Copy linkLink copied to clipboard!

Expand

Table 9.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceQuota |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ResourceQuota

Expand

Table 9.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 9.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 202 - Accepted | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ResourceQuota

Expand

Table 9.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ResourceQuota

Expand

Table 9.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 201 - Created | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ResourceQuota

Expand

Table 9.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |  |

Show more

Expand

Table 9.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 201 - Created | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.6. /api/v1/watch/namespaces/{namespace}/resourcequotas/{name}](#apiv1watchnamespacesnamespaceresourcequotasname) Copy linkLink copied to clipboard!

Expand

Table 9.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceQuota |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 9.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.7. /api/v1/namespaces/{namespace}/resourcequotas/{name}/status](#apiv1namespacesnamespaceresourcequotasnamestatus) Copy linkLink copied to clipboard!

Expand

Table 9.21. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceQuota |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ResourceQuota

Expand

Table 9.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ResourceQuota

Expand

Table 9.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.24. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 201 - Created | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ResourceQuota

Expand

Table 9.25. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.26. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |  |

Show more

Expand

Table 9.27. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 201 - Created | [`ResourceQuota`](#resourcequota-v1 "Chapter 9. ResourceQuota [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 10. ResourceClaim [resource.k8s.io/v1]](#resourceclaim-resource-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

Required
:   * `spec`

### [10.1. Specification](#specification-9) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata |
| `spec` | `object` | ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it. |
| `status` | `object` | ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was. |

Show more

#### [10.1.1. .spec](#spec-8) Copy linkLink copied to clipboard!

Description
:   ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `devices` | `object` | DeviceClaim defines how to request devices with a ResourceClaim. |

Show more

#### [10.1.2. .spec.devices](#spec-devices) Copy linkLink copied to clipboard!

Description
:   DeviceClaim defines how to request devices with a ResourceClaim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `config` | `array` | This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim. |
| `config[]` | `object` | DeviceClaimConfiguration is used for configuration parameters in DeviceClaim. |
| `constraints` | `array` | These constraints must be satisfied by the set of devices that get allocated for the claim. |
| `constraints[]` | `object` | DeviceConstraint must have exactly one field set besides Requests. |
| `requests` | `array` | Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated. |
| `requests[]` | `object` | DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests. |

Show more

#### [10.1.3. .spec.devices.config](#spec-devices-config) Copy linkLink copied to clipboard!

Description
:   This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim.

Type
:   `array`

#### [10.1.4. .spec.devices.config[]](#spec-devices-config-2) Copy linkLink copied to clipboard!

Description
:   DeviceClaimConfiguration is used for configuration parameters in DeviceClaim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `opaque` | `object` | OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor. |
| `requests` | `array (string)` | Requests lists the names of requests where the configuration applies. If empty, it applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the configuration applies to all subrequests. |

Show more

#### [10.1.5. .spec.devices.config[].opaque](#spec-devices-config-opaque) Copy linkLink copied to clipboard!

Description
:   OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
:   `object`

Required
:   * `driver`
    * `parameters`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
| `parameters` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki. |

Show more

#### [10.1.6. .spec.devices.constraints](#spec-devices-constraints) Copy linkLink copied to clipboard!

Description
:   These constraints must be satisfied by the set of devices that get allocated for the claim.

Type
:   `array`

#### [10.1.7. .spec.devices.constraints[]](#spec-devices-constraints-2) Copy linkLink copied to clipboard!

Description
:   DeviceConstraint must have exactly one field set besides Requests.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `distinctAttribute` | `string` | DistinctAttribute requires that all devices in question have this attribute and that its type and value are unique across those devices.  This acts as the inverse of MatchAttribute.  This constraint is used to avoid allocating multiple requests to the same device by ensuring attribute-level differentiation.  This is useful for scenarios where resource requests must be fulfilled by separate physical devices. For example, a container requests two network interfaces that must be allocated from two different physical NICs. |
| `matchAttribute` | `string` | MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.  For example, if you specified "dra.example.com/numa" (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn’t, then it also will not be chosen.  Must include the domain qualifier. |
| `requests` | `array (string)` | Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the constraint applies to all subrequests. |

Show more

#### [10.1.8. .spec.devices.requests](#spec-devices-requests) Copy linkLink copied to clipboard!

Description
:   Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated.

Type
:   `array`

#### [10.1.9. .spec.devices.requests[]](#spec-devices-requests-2) Copy linkLink copied to clipboard!

Description
:   DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exactly` | `object` | ExactDeviceRequest is a request for one or more identical devices. |
| `firstAvailable` | `array` | FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.  DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later. |
| `firstAvailable[]` | `object` | DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.  DeviceSubRequest is similar to ExactDeviceRequest, but doesn’t expose the AdminAccess field as that one is only supported when requesting a specific device. |
| `name` | `string` | Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.  References using the name in the DeviceRequest will uniquely identify a request when the Exactly field is set. When the FirstAvailable field is set, a reference to the name of the DeviceRequest will match whatever subrequest is chosen by the scheduler.  Must be a DNS label. |

Show more

#### [10.1.10. .spec.devices.requests[].exactly](#spec-devices-requests-exactly) Copy linkLink copied to clipboard!

Description
:   ExactDeviceRequest is a request for one or more identical devices.

Type
:   `object`

Required
:   * `deviceClassName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `adminAccess` | `boolean` | AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device. They ignore all ordinary claims to the device with respect to access modes and any resource allocations.  This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled. |
| `allocationMode` | `string` | AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:  - ExactCount: This request is for a specific number of devices. This is the default. The exact number is provided in the count field.  - All: This request is for all of the matching devices in a pool. At least one device must exist on the node for the allocation to succeed. Allocation will fail if some devices are already allocated, unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.  Possible enum values: - `"All"` - `"ExactCount"` |
| `capacity` | `object` | CapacityRequirements defines the capacity requirements for a specific device request. |
| `count` | `integer` | Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. |
| `deviceClassName` | `string` | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.  A DeviceClassName is required.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. |
| `selectors` | `array` | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered. |
| `selectors[]` | `object` | DeviceSelector must have exactly one field set. |
| `tolerations` | `array` | If specified, the request’s tolerations.  Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. |
| `tolerations[]` | `object` | The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [10.1.11. .spec.devices.requests[].exactly.capacity](#spec-devices-requests-exactly-capacity) Copy linkLink copied to clipboard!

Description
:   CapacityRequirements defines the capacity requirements for a specific device request.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.  This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with `device.capacity[<domain>].<name>.compareTo(quantity(<request quantity>)) >= 0`. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.  When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.  For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.  If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[\*].consumedCapacity field. |

Show more

#### [10.1.12. .spec.devices.requests[].exactly.selectors](#spec-devices-requests-exactly-selectors) Copy linkLink copied to clipboard!

Description
:   Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.

Type
:   `array`

#### [10.1.13. .spec.devices.requests[].exactly.selectors[]](#spec-devices-requests-exactly-selectors-2) Copy linkLink copied to clipboard!

Description
:   DeviceSelector must have exactly one field set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

Show more

#### [10.1.14. .spec.devices.requests[].exactly.selectors[].cel](#spec-devices-requests-exactly-selectors-cel) Copy linkLink copied to clipboard!

Description
:   CELDeviceSelector contains a CEL expression for selecting a device.

Type
:   `object`

Required
:   * `expression`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `expression` | `string` | Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.  The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).  Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:  device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules  The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.  The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.  A robust expression should check for the existence of attributes before referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:  cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps. |

Show more

#### [10.1.15. .spec.devices.requests[].exactly.tolerations](#spec-devices-requests-exactly-tolerations) Copy linkLink copied to clipboard!

Description
:   If specified, the request’s tolerations.

    Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

    In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

    The maximum number of tolerations is 16.

    This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
:   `array`

#### [10.1.16. .spec.devices.requests[].exactly.tolerations[]](#spec-devices-requests-exactly-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint. - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - `"None"` No effect, the taint is purely informational. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.  Possible enum values: - `"Equal"` - `"Exists"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as <time when taint was adedd> + <toleration seconds>. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value. |

Show more

#### [10.1.17. .spec.devices.requests[].firstAvailable](#spec-devices-requests-firstavailable) Copy linkLink copied to clipboard!

Description
:   FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.

    DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.

Type
:   `array`

#### [10.1.18. .spec.devices.requests[].firstAvailable[]](#spec-devices-requests-firstavailable-2) Copy linkLink copied to clipboard!

Description
:   DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.

    DeviceSubRequest is similar to ExactDeviceRequest, but doesn’t expose the AdminAccess field as that one is only supported when requesting a specific device.

Type
:   `object`

Required
:   * `name`
    * `deviceClassName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allocationMode` | `string` | AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:  - ExactCount: This request is for a specific number of devices. This is the default. The exact number is provided in the count field.  - All: This subrequest is for all of the matching devices in a pool. Allocation will fail if some devices are already allocated, unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.  Possible enum values: - `"All"` - `"ExactCount"` |
| `capacity` | `object` | CapacityRequirements defines the capacity requirements for a specific device request. |
| `count` | `integer` | Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. |
| `deviceClassName` | `string` | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this subrequest.  A class is required. Which classes are available depends on the cluster.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. |
| `name` | `string` | Name can be used to reference this subrequest in the list of constraints or the list of configurations for the claim. References must use the format <main request>/<subrequest>.  Must be a DNS label. |
| `selectors` | `array` | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered. |
| `selectors[]` | `object` | DeviceSelector must have exactly one field set. |
| `tolerations` | `array` | If specified, the request’s tolerations.  Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. |
| `tolerations[]` | `object` | The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [10.1.19. .spec.devices.requests[].firstAvailable[].capacity](#spec-devices-requests-firstavailable-capacity) Copy linkLink copied to clipboard!

Description
:   CapacityRequirements defines the capacity requirements for a specific device request.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.  This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with `device.capacity[<domain>].<name>.compareTo(quantity(<request quantity>)) >= 0`. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.  When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.  For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.  If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[\*].consumedCapacity field. |

Show more

#### [10.1.20. .spec.devices.requests[].firstAvailable[].selectors](#spec-devices-requests-firstavailable-selectors) Copy linkLink copied to clipboard!

Description
:   Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.

Type
:   `array`

#### [10.1.21. .spec.devices.requests[].firstAvailable[].selectors[]](#spec-devices-requests-firstavailable-selectors-2) Copy linkLink copied to clipboard!

Description
:   DeviceSelector must have exactly one field set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

Show more

#### [10.1.22. .spec.devices.requests[].firstAvailable[].selectors[].cel](#spec-devices-requests-firstavailable-selectors-cel) Copy linkLink copied to clipboard!

Description
:   CELDeviceSelector contains a CEL expression for selecting a device.

Type
:   `object`

Required
:   * `expression`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `expression` | `string` | Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.  The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).  Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:  device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules  The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.  The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.  A robust expression should check for the existence of attributes before referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:  cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps. |

Show more

#### [10.1.23. .spec.devices.requests[].firstAvailable[].tolerations](#spec-devices-requests-firstavailable-tolerations) Copy linkLink copied to clipboard!

Description
:   If specified, the request’s tolerations.

    Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

    In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

    The maximum number of tolerations is 16.

    This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
:   `array`

#### [10.1.24. .spec.devices.requests[].firstAvailable[].tolerations[]](#spec-devices-requests-firstavailable-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint. - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - `"None"` No effect, the taint is purely informational. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.  Possible enum values: - `"Equal"` - `"Exists"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as <time when taint was adedd> + <toleration seconds>. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value. |

Show more

#### [10.1.25. .status](#status-6) Copy linkLink copied to clipboard!

Description
:   ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allocation` | `object` | AllocationResult contains attributes of an allocated resource. |
| `devices` | `array` | Devices contains the status of each device allocated for this claim, as reported by the driver. This can include driver-specific information. Entries are owned by their respective drivers. |
| `devices[]` | `object` | AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.  The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices. |
| `reservedFor` | `array` | ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.  In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.  Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.  There can be at most 256 such reservations. This may get increased in the future, but not reduced. |
| `reservedFor[]` | `object` | ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim. |

Show more

#### [10.1.26. .status.allocation](#status-allocation) Copy linkLink copied to clipboard!

Description
:   AllocationResult contains attributes of an allocated resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allocationTimestamp` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | AllocationTimestamp stores the time when the resources were allocated. This field is not guaranteed to be set, in which case that time is unknown.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate. |
| `devices` | `object` | DeviceAllocationResult is the result of allocating devices. |
| `nodeSelector` | [`NodeSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-NodeSelector) | NodeSelector defines where the allocated resources are available. If unset, they are available everywhere. |

Show more

#### [10.1.27. .status.allocation.devices](#status-allocation-devices) Copy linkLink copied to clipboard!

Description
:   DeviceAllocationResult is the result of allocating devices.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `config` | `array` | This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.  This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters. |
| `config[]` | `object` | DeviceAllocationConfiguration gets embedded in an AllocationResult. |
| `results` | `array` | Results lists all allocated devices. |
| `results[]` | `object` | DeviceRequestAllocationResult contains the allocation result for one request. |

Show more

#### [10.1.28. .status.allocation.devices.config](#status-allocation-devices-config) Copy linkLink copied to clipboard!

Description
:   This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.

    This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.

Type
:   `array`

#### [10.1.29. .status.allocation.devices.config[]](#status-allocation-devices-config-2) Copy linkLink copied to clipboard!

Description
:   DeviceAllocationConfiguration gets embedded in an AllocationResult.

Type
:   `object`

Required
:   * `source`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `opaque` | `object` | OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor. |
| `requests` | `array (string)` | Requests lists the names of requests where the configuration applies. If empty, its applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the configuration applies to all subrequests. |
| `source` | `string` | Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim.  Possible enum values: - `"FromClaim"` - `"FromClass"` |

Show more

#### [10.1.30. .status.allocation.devices.config[].opaque](#status-allocation-devices-config-opaque) Copy linkLink copied to clipboard!

Description
:   OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
:   `object`

Required
:   * `driver`
    * `parameters`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
| `parameters` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki. |

Show more

#### [10.1.31. .status.allocation.devices.results](#status-allocation-devices-results) Copy linkLink copied to clipboard!

Description
:   Results lists all allocated devices.

Type
:   `array`

#### [10.1.32. .status.allocation.devices.results[]](#status-allocation-devices-results-2) Copy linkLink copied to clipboard!

Description
:   DeviceRequestAllocationResult contains the allocation result for one request.

Type
:   `object`

Required
:   * `request`
    * `driver`
    * `pool`
    * `device`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `adminAccess` | `boolean` | AdminAccess indicates that this device was allocated for administrative access. See the corresponding request field for a definition of mode.  This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled. |
| `bindingConditions` | `array (string)` | BindingConditions contains a copy of the BindingConditions from the corresponding ResourceSlice at the time of allocation.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates. |
| `bindingFailureConditions` | `array (string)` | BindingFailureConditions contains a copy of the BindingFailureConditions from the corresponding ResourceSlice at the time of allocation.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates. |
| `consumedCapacity` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | ConsumedCapacity tracks the amount of capacity consumed per device as part of the claim request. The consumed amount may differ from the requested amount: it is rounded up to the nearest valid value based on the device’s requestPolicy if applicable (i.e., may not be less than the requested amount).  The total consumed capacity for each device must not exceed the DeviceCapacity’s Value.  This field is populated only for devices that allow multiple allocations. All capacity entries are included, even if the consumed amount is zero. |
| `device` | `string` | Device references one device instance via its name in the driver’s resource pool. It must be a DNS label. |
| `driver` | `string` | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
| `pool` | `string` | This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes. |
| `request` | `string` | Request is the name of the request in the claim which caused this device to be allocated. If it references a subrequest in the firstAvailable list on a DeviceRequest, this field must include both the name of the main request and the subrequest using the format <main request>/<subrequest>.  Multiple devices may have been allocated per request. |
| `shareID` | `string` | ShareID uniquely identifies an individual allocation share of the device, used when the device supports multiple simultaneous allocations. It serves as an additional map key to differentiate concurrent shares of the same device. |
| `tolerations` | `array` | A copy of all tolerations specified in the request at the time when the device got allocated.  The maximum number of tolerations is 16.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. |
| `tolerations[]` | `object` | The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [10.1.33. .status.allocation.devices.results[].tolerations](#status-allocation-devices-results-tolerations) Copy linkLink copied to clipboard!

Description
:   A copy of all tolerations specified in the request at the time when the device got allocated.

    The maximum number of tolerations is 16.

    This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
:   `array`

#### [10.1.34. .status.allocation.devices.results[].tolerations[]](#status-allocation-devices-results-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint. - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - `"None"` No effect, the taint is purely informational. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.  Possible enum values: - `"Equal"` - `"Exists"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as <time when taint was adedd> + <toleration seconds>. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value. |

Show more

#### [10.1.35. .status.devices](#status-devices) Copy linkLink copied to clipboard!

Description
:   Devices contains the status of each device allocated for this claim, as reported by the driver. This can include driver-specific information. Entries are owned by their respective drivers.

Type
:   `array`

#### [10.1.36. .status.devices[]](#status-devices-2) Copy linkLink copied to clipboard!

Description
:   AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.

    The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices.

Type
:   `object`

Required
:   * `driver`
    * `pool`
    * `device`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | [`array (Condition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Condition) | Conditions contains the latest observation of the device’s state. If the device has been configured according to the class and claim config references, the `Ready` condition should be True.  Must not contain more than 8 entries. |
| `data` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | Data contains arbitrary driver-specific data.  The length of the raw data must be smaller or equal to 10 Ki. |
| `device` | `string` | Device references one device instance via its name in the driver’s resource pool. It must be a DNS label. |
| `driver` | `string` | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
| `networkData` | `object` | NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context. |
| `pool` | `string` | This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes. |
| `shareID` | `string` | ShareID uniquely identifies an individual allocation share of the device. |

Show more

#### [10.1.37. .status.devices[].networkData](#status-devices-networkdata) Copy linkLink copied to clipboard!

Description
:   NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hardwareAddress` | `string` | HardwareAddress represents the hardware address (e.g. MAC Address) of the device’s network interface.  Must not be longer than 128 characters. |
| `interfaceName` | `string` | InterfaceName specifies the name of the network interface associated with the allocated device. This might be the name of a physical or virtual network interface being configured in the pod.  Must not be longer than 256 characters. |
| `ips` | `array (string)` | IPs lists the network addresses assigned to the device’s network interface. This can include both IPv4 and IPv6 addresses. The IPs are in the CIDR notation, which includes both the address and the associated subnet mask. e.g.: "192.0.2.5/24" for IPv4 and "2001:db8::5/64" for IPv6. |

Show more

#### [10.1.38. .status.reservedFor](#status-reservedfor) Copy linkLink copied to clipboard!

Description
:   ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.

    In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.

    Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.

    There can be at most 256 such reservations. This may get increased in the future, but not reduced.

Type
:   `array`

#### [10.1.39. .status.reservedFor[]](#status-reservedfor-2) Copy linkLink copied to clipboard!

Description
:   ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.

Type
:   `object`

Required
:   * `resource`
    * `name`
    * `uid`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. |
| `name` | `string` | Name is the name of resource being referenced. |
| `resource` | `string` | Resource is the type of resource being referenced, for example "pods". |
| `uid` | `string` | UID identifies exactly one incarnation of the resource. |

Show more

### [10.2. API endpoints](#api-endpoints-9) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/resource.k8s.io/v1/resourceclaims`

  + `GET`: list or watch objects of kind ResourceClaim
* `/apis/resource.k8s.io/v1/watch/resourceclaims`

  + `GET`: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims`

  + `DELETE`: delete collection of ResourceClaim
  + `GET`: list or watch objects of kind ResourceClaim
  + `POST`: create a ResourceClaim
* `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims`

  + `GET`: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}`

  + `DELETE`: delete a ResourceClaim
  + `GET`: read the specified ResourceClaim
  + `PATCH`: partially update the specified ResourceClaim
  + `PUT`: replace the specified ResourceClaim
* `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}`

  + `GET`: watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status`

  + `GET`: read status of the specified ResourceClaim
  + `PATCH`: partially update status of the specified ResourceClaim
  + `PUT`: replace status of the specified ResourceClaim

#### [10.2.1. /apis/resource.k8s.io/v1/resourceclaims](#apisresource-k8s-iov1resourceclaims) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceClaim

Expand

Table 10.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.2. /apis/resource.k8s.io/v1/watch/resourceclaims](#apisresource-k8s-iov1watchresourceclaims) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 10.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.3. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims](#apisresource-k8s-iov1namespacesnamespaceresourceclaims) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ResourceClaim

Expand

Table 10.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 10.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceClaim

Expand

Table 10.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ResourceClaim

Expand

Table 10.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.4. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims](#apisresource-k8s-iov1watchnamespacesnamespaceresourceclaims) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 10.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.5. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}](#apisresource-k8s-iov1namespacesnamespaceresourceclaimsname) Copy linkLink copied to clipboard!

Expand

Table 10.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceClaim |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ResourceClaim

Expand

Table 10.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 10.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ResourceClaim

Expand

Table 10.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ResourceClaim

Expand

Table 10.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ResourceClaim

Expand

Table 10.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.6. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}](#apisresource-k8s-iov1watchnamespacesnamespaceresourceclaimsname) Copy linkLink copied to clipboard!

Expand

Table 10.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceClaim |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 10.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.7. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status](#apisresource-k8s-iov1namespacesnamespaceresourceclaimsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 10.21. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceClaim |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ResourceClaim

Expand

Table 10.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ResourceClaim

Expand

Table 10.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.24. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ResourceClaim

Expand

Table 10.25. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.26. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.27. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaim`](#resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]](#resourceclaimtemplate-resource-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   ResourceClaimTemplate is used to produce ResourceClaim objects.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

Required
:   * `spec`

### [11.1. Specification](#specification-10) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata |
| `spec` | `object` | ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim. |

Show more

#### [11.1.1. .spec](#spec-9) Copy linkLink copied to clipboard!

Description
:   ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

Type
:   `object`

Required
:   * `spec`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | ObjectMeta may contain labels and annotations that will be copied into the ResourceClaim when creating it. No other fields are allowed and will be rejected during validation. |
| `spec` | `object` | ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it. |

Show more

#### [11.1.2. .spec.spec](#spec-spec) Copy linkLink copied to clipboard!

Description
:   ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `devices` | `object` | DeviceClaim defines how to request devices with a ResourceClaim. |

Show more

#### [11.1.3. .spec.spec.devices](#spec-spec-devices) Copy linkLink copied to clipboard!

Description
:   DeviceClaim defines how to request devices with a ResourceClaim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `config` | `array` | This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim. |
| `config[]` | `object` | DeviceClaimConfiguration is used for configuration parameters in DeviceClaim. |
| `constraints` | `array` | These constraints must be satisfied by the set of devices that get allocated for the claim. |
| `constraints[]` | `object` | DeviceConstraint must have exactly one field set besides Requests. |
| `requests` | `array` | Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated. |
| `requests[]` | `object` | DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests. |

Show more

#### [11.1.4. .spec.spec.devices.config](#spec-spec-devices-config) Copy linkLink copied to clipboard!

Description
:   This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim.

Type
:   `array`

#### [11.1.5. .spec.spec.devices.config[]](#spec-spec-devices-config-2) Copy linkLink copied to clipboard!

Description
:   DeviceClaimConfiguration is used for configuration parameters in DeviceClaim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `opaque` | `object` | OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor. |
| `requests` | `array (string)` | Requests lists the names of requests where the configuration applies. If empty, it applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the configuration applies to all subrequests. |

Show more

#### [11.1.6. .spec.spec.devices.config[].opaque](#spec-spec-devices-config-opaque) Copy linkLink copied to clipboard!

Description
:   OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

Type
:   `object`

Required
:   * `driver`
    * `parameters`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
| `parameters` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki. |

Show more

#### [11.1.7. .spec.spec.devices.constraints](#spec-spec-devices-constraints) Copy linkLink copied to clipboard!

Description
:   These constraints must be satisfied by the set of devices that get allocated for the claim.

Type
:   `array`

#### [11.1.8. .spec.spec.devices.constraints[]](#spec-spec-devices-constraints-2) Copy linkLink copied to clipboard!

Description
:   DeviceConstraint must have exactly one field set besides Requests.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `distinctAttribute` | `string` | DistinctAttribute requires that all devices in question have this attribute and that its type and value are unique across those devices.  This acts as the inverse of MatchAttribute.  This constraint is used to avoid allocating multiple requests to the same device by ensuring attribute-level differentiation.  This is useful for scenarios where resource requests must be fulfilled by separate physical devices. For example, a container requests two network interfaces that must be allocated from two different physical NICs. |
| `matchAttribute` | `string` | MatchAttribute requires that all devices in question have this attribute and that its type and value are the same across those devices.  For example, if you specified "dra.example.com/numa" (a hypothetical example!), then only devices in the same NUMA node will be chosen. A device which does not have that attribute will not be chosen. All devices should use a value of the same type for this attribute because that is part of its specification, but if one device doesn’t, then it also will not be chosen.  Must include the domain qualifier. |
| `requests` | `array (string)` | Requests is a list of the one or more requests in this claim which must co-satisfy this constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy the constraint. If this is not specified, this constraint applies to all requests in this claim.  References to subrequests must include the name of the main request and may include the subrequest using the format <main request>[/<subrequest>]. If just the main request is given, the constraint applies to all subrequests. |

Show more

#### [11.1.9. .spec.spec.devices.requests](#spec-spec-devices-requests) Copy linkLink copied to clipboard!

Description
:   Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated.

Type
:   `array`

#### [11.1.10. .spec.spec.devices.requests[]](#spec-spec-devices-requests-2) Copy linkLink copied to clipboard!

Description
:   DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exactly` | `object` | ExactDeviceRequest is a request for one or more identical devices. |
| `firstAvailable` | `array` | FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.  DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later. |
| `firstAvailable[]` | `object` | DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.  DeviceSubRequest is similar to ExactDeviceRequest, but doesn’t expose the AdminAccess field as that one is only supported when requesting a specific device. |
| `name` | `string` | Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.  References using the name in the DeviceRequest will uniquely identify a request when the Exactly field is set. When the FirstAvailable field is set, a reference to the name of the DeviceRequest will match whatever subrequest is chosen by the scheduler.  Must be a DNS label. |

Show more

#### [11.1.11. .spec.spec.devices.requests[].exactly](#spec-spec-devices-requests-exactly) Copy linkLink copied to clipboard!

Description
:   ExactDeviceRequest is a request for one or more identical devices.

Type
:   `object`

Required
:   * `deviceClassName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `adminAccess` | `boolean` | AdminAccess indicates that this is a claim for administrative access to the device(s). Claims with AdminAccess are expected to be used for monitoring or other management services for a device. They ignore all ordinary claims to the device with respect to access modes and any resource allocations.  This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled. |
| `allocationMode` | `string` | AllocationMode and its related fields define how devices are allocated to satisfy this request. Supported values are:  - ExactCount: This request is for a specific number of devices. This is the default. The exact number is provided in the count field.  - All: This request is for all of the matching devices in a pool. At least one device must exist on the node for the allocation to succeed. Allocation will fail if some devices are already allocated, unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other requests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.  Possible enum values: - `"All"` - `"ExactCount"` |
| `capacity` | `object` | CapacityRequirements defines the capacity requirements for a specific device request. |
| `count` | `integer` | Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. |
| `deviceClassName` | `string` | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this request.  A DeviceClassName is required.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. |
| `selectors` | `array` | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered. |
| `selectors[]` | `object` | DeviceSelector must have exactly one field set. |
| `tolerations` | `array` | If specified, the request’s tolerations.  Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. |
| `tolerations[]` | `object` | The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [11.1.12. .spec.spec.devices.requests[].exactly.capacity](#spec-spec-devices-requests-exactly-capacity) Copy linkLink copied to clipboard!

Description
:   CapacityRequirements defines the capacity requirements for a specific device request.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.  This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with `device.capacity[<domain>].<name>.compareTo(quantity(<request quantity>)) >= 0`. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.  When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.  For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.  If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[\*].consumedCapacity field. |

Show more

#### [11.1.13. .spec.spec.devices.requests[].exactly.selectors](#spec-spec-devices-requests-exactly-selectors) Copy linkLink copied to clipboard!

Description
:   Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this request. All selectors must be satisfied for a device to be considered.

Type
:   `array`

#### [11.1.14. .spec.spec.devices.requests[].exactly.selectors[]](#spec-spec-devices-requests-exactly-selectors-2) Copy linkLink copied to clipboard!

Description
:   DeviceSelector must have exactly one field set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

Show more

#### [11.1.15. .spec.spec.devices.requests[].exactly.selectors[].cel](#spec-spec-devices-requests-exactly-selectors-cel) Copy linkLink copied to clipboard!

Description
:   CELDeviceSelector contains a CEL expression for selecting a device.

Type
:   `object`

Required
:   * `expression`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `expression` | `string` | Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.  The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).  Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:  device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules  The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.  The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.  A robust expression should check for the existence of attributes before referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:  cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps. |

Show more

#### [11.1.16. .spec.spec.devices.requests[].exactly.tolerations](#spec-spec-devices-requests-exactly-tolerations) Copy linkLink copied to clipboard!

Description
:   If specified, the request’s tolerations.

    Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

    In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

    The maximum number of tolerations is 16.

    This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
:   `array`

#### [11.1.17. .spec.spec.devices.requests[].exactly.tolerations[]](#spec-spec-devices-requests-exactly-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint. - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - `"None"` No effect, the taint is purely informational. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.  Possible enum values: - `"Equal"` - `"Exists"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as <time when taint was adedd> + <toleration seconds>. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value. |

Show more

#### [11.1.18. .spec.spec.devices.requests[].firstAvailable](#spec-spec-devices-requests-firstavailable) Copy linkLink copied to clipboard!

Description
:   FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.

    DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.

Type
:   `array`

#### [11.1.19. .spec.spec.devices.requests[].firstAvailable[]](#spec-spec-devices-requests-firstavailable-2) Copy linkLink copied to clipboard!

Description
:   DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.

    DeviceSubRequest is similar to ExactDeviceRequest, but doesn’t expose the AdminAccess field as that one is only supported when requesting a specific device.

Type
:   `object`

Required
:   * `name`
    * `deviceClassName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allocationMode` | `string` | AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:  - ExactCount: This request is for a specific number of devices. This is the default. The exact number is provided in the count field.  - All: This subrequest is for all of the matching devices in a pool. Allocation will fail if some devices are already allocated, unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes.  Possible enum values: - `"All"` - `"ExactCount"` |
| `capacity` | `object` | CapacityRequirements defines the capacity requirements for a specific device request. |
| `count` | `integer` | Count is used only when the count mode is "ExactCount". Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. |
| `deviceClassName` | `string` | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this subrequest.  A class is required. Which classes are available depends on the cluster.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. |
| `name` | `string` | Name can be used to reference this subrequest in the list of constraints or the list of configurations for the claim. References must use the format <main request>/<subrequest>.  Must be a DNS label. |
| `selectors` | `array` | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered. |
| `selectors[]` | `object` | DeviceSelector must have exactly one field set. |
| `tolerations` | `array` | If specified, the request’s tolerations.  Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. |
| `tolerations[]` | `object` | The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [11.1.20. .spec.spec.devices.requests[].firstAvailable[].capacity](#spec-spec-devices-requests-firstavailable-capacity) Copy linkLink copied to clipboard!

Description
:   CapacityRequirements defines the capacity requirements for a specific device request.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.  This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with `device.capacity[<domain>].<name>.compareTo(quantity(<request quantity>)) >= 0`. For example, device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.  When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.  For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.  If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[\*].consumedCapacity field. |

Show more

#### [11.1.21. .spec.spec.devices.requests[].firstAvailable[].selectors](#spec-spec-devices-requests-firstavailable-selectors) Copy linkLink copied to clipboard!

Description
:   Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered.

Type
:   `array`

#### [11.1.22. .spec.spec.devices.requests[].firstAvailable[].selectors[]](#spec-spec-devices-requests-firstavailable-selectors-2) Copy linkLink copied to clipboard!

Description
:   DeviceSelector must have exactly one field set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cel` | `object` | CELDeviceSelector contains a CEL expression for selecting a device. |

Show more

#### [11.1.23. .spec.spec.devices.requests[].firstAvailable[].selectors[].cel](#spec-spec-devices-requests-firstavailable-selectors-cel) Copy linkLink copied to clipboard!

Description
:   CELDeviceSelector contains a CEL expression for selecting a device.

Type
:   `object`

Required
:   * `expression`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `expression` | `string` | Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.  The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).  Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:  device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules  The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.  The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.  A robust expression should check for the existence of attributes before referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:  cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps. |

Show more

#### [11.1.24. .spec.spec.devices.requests[].firstAvailable[].tolerations](#spec-spec-devices-requests-firstavailable-tolerations) Copy linkLink copied to clipboard!

Description
:   If specified, the request’s tolerations.

    Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.

    In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.

    The maximum number of tolerations is 16.

    This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
:   `array`

#### [11.1.25. .spec.spec.devices.requests[].firstAvailable[].tolerations[]](#spec-spec-devices-requests-firstavailable-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint. - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - `"None"` No effect, the taint is purely informational. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. Must be a label name. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can tolerate all taints of a particular category.  Possible enum values: - `"Equal"` - `"Exists"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be evicted is calculated as <time when taint was adedd> + <toleration seconds>. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty, otherwise just a regular string. Must be a label value. |

Show more

### [11.2. API endpoints](#api-endpoints-10) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/resource.k8s.io/v1/resourceclaimtemplates`

  + `GET`: list or watch objects of kind ResourceClaimTemplate
* `/apis/resource.k8s.io/v1/watch/resourceclaimtemplates`

  + `GET`: watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates`

  + `DELETE`: delete collection of ResourceClaimTemplate
  + `GET`: list or watch objects of kind ResourceClaimTemplate
  + `POST`: create a ResourceClaimTemplate
* `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates`

  + `GET`: watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}`

  + `DELETE`: delete a ResourceClaimTemplate
  + `GET`: read the specified ResourceClaimTemplate
  + `PATCH`: partially update the specified ResourceClaimTemplate
  + `PUT`: replace the specified ResourceClaimTemplate
* `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates/{name}`

  + `GET`: watch changes to an object of kind ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [11.2.1. /apis/resource.k8s.io/v1/resourceclaimtemplates](#apisresource-k8s-iov1resourceclaimtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceClaimTemplate

Expand

Table 11.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimTemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.2. /apis/resource.k8s.io/v1/watch/resourceclaimtemplates](#apisresource-k8s-iov1watchresourceclaimtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 11.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.3. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates](#apisresource-k8s-iov1namespacesnamespaceresourceclaimtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ResourceClaimTemplate

Expand

Table 11.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 11.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceClaimTemplate

Expand

Table 11.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimTemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ResourceClaimTemplate

Expand

Table 11.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 11.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.4. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates](#apisresource-k8s-iov1watchnamespacesnamespaceresourceclaimtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 11.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.5. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}](#apisresource-k8s-iov1namespacesnamespaceresourceclaimtemplatesname) Copy linkLink copied to clipboard!

Expand

Table 11.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceClaimTemplate |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ResourceClaimTemplate

Expand

Table 11.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 11.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ResourceClaimTemplate

Expand

Table 11.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ResourceClaimTemplate

Expand

Table 11.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ResourceClaimTemplate

Expand

Table 11.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 11.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceClaimTemplate`](#resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.6. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates/{name}](#apisresource-k8s-iov1watchnamespacesnamespaceresourceclaimtemplatesname) Copy linkLink copied to clipboard!

Expand

Table 11.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceClaimTemplate |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 11.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 12. ResourceSlice [resource.k8s.io/v1]](#resourceslice-resource-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   ResourceSlice represents one or more resources in a pool of similar resources, managed by a common driver. A pool may span more than one ResourceSlice, and exactly how many ResourceSlices comprise a pool is determined by the driver.

    At the moment, the only supported resources are devices with attributes and capacities. Each device in a given pool, regardless of how many ResourceSlices, must have a unique name. The ResourceSlice in which a device gets published may change over time. The unique identifier for a device is the tuple <driver name>, <pool name>, <device name>.

    Whenever a driver needs to update a pool, it increments the pool.Spec.Pool.Generation number and updates all ResourceSlices with that new number and new resource definitions. A consumer must only use ResourceSlices with the highest generation number and ignore all others.

    When allocating all resources in a pool matching certain criteria or when looking for the best solution among several different alternatives, a consumer should check the number of ResourceSlices in a pool (included in each ResourceSlice) to determine whether its view of a pool is complete and if not, should wait until the driver has completed updating the pool.

    For resources that are not local to a node, the node name is not set. Instead, the driver may use a node selector to specify where the devices are available.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

Type
:   `object`

Required
:   * `spec`

### [12.1. Specification](#specification-11) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata |
| `spec` | `object` | ResourceSliceSpec contains the information published by the driver in one ResourceSlice. |

Show more

#### [12.1.1. .spec](#spec-10) Copy linkLink copied to clipboard!

Description
:   ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

Type
:   `object`

Required
:   * `driver`
    * `pool`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allNodes` | `boolean` | AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. |
| `devices` | `array` | Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.  Only one of Devices and SharedCounters can be set in a ResourceSlice. |
| `devices[]` | `object` | Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set. |
| `driver` | `string` | Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. This field is immutable. |
| `nodeName` | `string` | NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. This field is immutable. |
| `nodeSelector` | [`NodeSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-NodeSelector) | NodeSelector defines which nodes have access to the resources in the pool, when that pool is not limited to a single node.  Must use exactly one term.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. |
| `perDeviceNodeSelection` | `boolean` | PerDeviceNodeSelection defines whether the access from nodes to resources in the pool is set on the ResourceSlice level or on each device. If it is set to true, every device defined the ResourceSlice must specify this individually.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. |
| `pool` | `object` | ResourcePool describes the pool that ResourceSlices belong to. |
| `sharedCounters` | `array` | SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.  The names of the counter sets must be unique in the ResourcePool.  Only one of Devices and SharedCounters can be set in a ResourceSlice.  The maximum number of counter sets is 8. |
| `sharedCounters[]` | `object` | CounterSet defines a named set of counters that are available to be used by devices defined in the ResourcePool.  The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices. |

Show more

#### [12.1.2. .spec.devices](#spec-devices-2) Copy linkLink copied to clipboard!

Description
:   Devices lists some or all of the devices in this pool.

    Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.

    Only one of Devices and SharedCounters can be set in a ResourceSlice.

Type
:   `array`

#### [12.1.3. .spec.devices[]](#spec-devices-3) Copy linkLink copied to clipboard!

Description
:   Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allNodes` | `boolean` | AllNodes indicates that all nodes have access to the device.  Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set. |
| `allowMultipleAllocations` | `boolean` | AllowMultipleAllocations marks whether the device is allowed to be allocated to multiple DeviceRequests.  If AllowMultipleAllocations is set to true, the device can be allocated more than once, and all of its capacity is consumable, regardless of whether the requestPolicy is defined or not. |
| `attributes` | `object` | Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.  The maximum number of attributes and capacities combined is 32. |
| `attributes{}` | `object` | DeviceAttribute must have exactly one field set. |
| `bindingConditions` | `array (string)` | BindingConditions defines the conditions for proceeding with binding. All of these conditions must be set in the per-device status conditions with a value of True to proceed with binding the pod to the node while scheduling the pod.  The maximum number of binding conditions is 4.  The conditions must be a valid condition type string.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates. |
| `bindingFailureConditions` | `array (string)` | BindingFailureConditions defines the conditions for binding failure. They may be set in the per-device status conditions. If any is set to "True", a binding failure occurred.  The maximum number of binding failure conditions is 4.  The conditions must be a valid condition type string.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates. |
| `bindsToNode` | `boolean` | BindsToNode indicates if the usage of an allocation involving this device has to be limited to exactly the node that was chosen when allocating the claim. If set to true, the scheduler will set the ResourceClaim.Status.Allocation.NodeSelector to match the node where the allocation was made.  This is an alpha field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates. |
| `capacity` | `object` | Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.  The maximum number of attributes and capacities combined is 32. |
| `capacity{}` | `object` | DeviceCapacity describes a quantity associated with a device. |
| `consumesCounters` | `array` | ConsumesCounters defines a list of references to sharedCounters and the set of counters that the device will consume from those counter sets.  There can only be a single entry per counterSet.  The maximum number of device counter consumptions per device is 2. |
| `consumesCounters[]` | `object` | DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet. |
| `name` | `string` | Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label. |
| `nodeName` | `string` | NodeName identifies the node where the device is available.  Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set. |
| `nodeSelector` | [`NodeSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-NodeSelector) | NodeSelector defines the nodes where the device is available.  Must use exactly one term.  Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can be set. |
| `taints` | `array` | If specified, these are the driver-defined taints.  The maximum number of taints is 16. If taints are set for any device in a ResourceSlice, then the maximum number of allowed devices per ResourceSlice is 64 instead of 128.  This is an alpha field and requires enabling the DRADeviceTaints feature gate. |
| `taints[]` | `object` | The device this taint is attached to has the "effect" on any claim which does not tolerate the taint and, through the claim, to pods using the claim. |

Show more

#### [12.1.4. .spec.devices[].attributes](#spec-devices-attributes) Copy linkLink copied to clipboard!

Description
:   Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.

    The maximum number of attributes and capacities combined is 32.

Type
:   `object`

#### [12.1.5. .spec.devices[].attributes{}](#spec-devices-attributes-2) Copy linkLink copied to clipboard!

Description
:   DeviceAttribute must have exactly one field set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `bool` | `boolean` | BoolValue is a true/false value. |
| `int` | `integer` | IntValue is a number. |
| `string` | `string` | StringValue is a string. Must not be longer than 64 characters. |
| `version` | `string` | VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters. |

Show more

#### [12.1.6. .spec.devices[].capacity](#spec-devices-capacity) Copy linkLink copied to clipboard!

Description
:   Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.

    The maximum number of attributes and capacities combined is 32.

Type
:   `object`

#### [12.1.7. .spec.devices[].capacity{}](#spec-devices-capacity-2) Copy linkLink copied to clipboard!

Description
:   DeviceCapacity describes a quantity associated with a device.

Type
:   `object`

Required
:   * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requestPolicy` | `object` | CapacityRequestPolicy defines how requests consume device capacity.  Must not set more than one ValidRequestValues. |
| `value` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Value defines how much of a certain capacity that device has.  This field reflects the fixed total capacity and does not change. The consumed amount is tracked separately by scheduler and does not affect this value. |

Show more

#### [12.1.8. .spec.devices[].capacity{}.requestPolicy](#spec-devices-capacity-requestpolicy) Copy linkLink copied to clipboard!

Description
:   CapacityRequestPolicy defines how requests consume device capacity.

    Must not set more than one ValidRequestValues.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `default` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Default specifies how much of this capacity is consumed by a request that does not contain an entry for it in DeviceRequest’s Capacity. |
| `validRange` | `object` | CapacityRequestPolicyRange defines a valid range for consumable capacity values.  - If the requested amount is less than Min, it is rounded up to the Min value. - If Step is set and the requested amount is between Min and Max but not aligned with Step, it will be rounded up to the next value equal to Min + (n \* Step). - If Step is not set, the requested amount is used as-is if it falls within the range Min to Max (if set). - If the requested or rounded amount exceeds Max (if set), the request does not satisfy the policy, and the device cannot be allocated. |
| `validValues` | [`array (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | ValidValues defines a set of acceptable quantity values in consuming requests.  Must not contain more than 10 entries. Must be sorted in ascending order.  If this field is set, Default must be defined and it must be included in ValidValues list.  If the requested amount does not match any valid value but smaller than some valid values, the scheduler calculates the smallest valid value that is greater than or equal to the request. That is: min(ceil(requestedValue) ∈ validValues), where requestedValue ≤ max(validValues).  If the requested amount exceeds all valid values, the request violates the policy, and this device cannot be allocated. |

Show more

#### [12.1.9. .spec.devices[].capacity{}.requestPolicy.validRange](#spec-devices-capacity-requestpolicy-validrange) Copy linkLink copied to clipboard!

Description
:   CapacityRequestPolicyRange defines a valid range for consumable capacity values.

    * If the requested amount is less than Min, it is rounded up to the Min value.
    * If Step is set and the requested amount is between Min and Max but not aligned with Step, it will be rounded up to the next value equal to Min + (n \* Step).
    * If Step is not set, the requested amount is used as-is if it falls within the range Min to Max (if set).
    * If the requested or rounded amount exceeds Max (if set), the request does not satisfy the policy, and the device cannot be allocated.

Type
:   `object`

Required
:   * `min`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `max` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Max defines the upper limit for capacity that can be requested.  Max must be less than or equal to the capacity value. Min and requestPolicy.default must be less than or equal to the maximum. |
| `min` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Min specifies the minimum capacity allowed for a consumption request.  Min must be greater than or equal to zero, and less than or equal to the capacity value. requestPolicy.default must be more than or equal to the minimum. |
| `step` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Step defines the step size between valid capacity amounts within the range.  Max (if set) and requestPolicy.default must be a multiple of Step. Min + Step must be less than or equal to the capacity value. |

Show more

#### [12.1.10. .spec.devices[].consumesCounters](#spec-devices-consumescounters) Copy linkLink copied to clipboard!

Description
:   ConsumesCounters defines a list of references to sharedCounters and the set of counters that the device will consume from those counter sets.

    There can only be a single entry per counterSet.

    The maximum number of device counter consumptions per device is 2.

Type
:   `array`

#### [12.1.11. .spec.devices[].consumesCounters[]](#spec-devices-consumescounters-2) Copy linkLink copied to clipboard!

Description
:   DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.

Type
:   `object`

Required
:   * `counterSet`
    * `counters`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `counterSet` | `string` | CounterSet is the name of the set from which the counters defined will be consumed. |
| `counters` | `object` | Counters defines the counters that will be consumed by the device.  The maximum number of counters is 32. |
| `counters{}` | `object` | Counter describes a quantity associated with a device. |

Show more

#### [12.1.12. .spec.devices[].consumesCounters[].counters](#spec-devices-consumescounters-counters) Copy linkLink copied to clipboard!

Description
:   Counters defines the counters that will be consumed by the device.

    The maximum number of counters is 32.

Type
:   `object`

#### [12.1.13. .spec.devices[].consumesCounters[].counters{}](#spec-devices-consumescounters-counters-2) Copy linkLink copied to clipboard!

Description
:   Counter describes a quantity associated with a device.

Type
:   `object`

Required
:   * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `value` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Value defines how much of a certain device counter is available. |

Show more

#### [12.1.14. .spec.devices[].taints](#spec-devices-taints) Copy linkLink copied to clipboard!

Description
:   If specified, these are the driver-defined taints.

    The maximum number of taints is 16. If taints are set for any device in a ResourceSlice, then the maximum number of allowed devices per ResourceSlice is 64 instead of 128.

    This is an alpha field and requires enabling the DRADeviceTaints feature gate.

Type
:   `array`

#### [12.1.15. .spec.devices[].taints[]](#spec-devices-taints-2) Copy linkLink copied to clipboard!

Description
:   The device this taint is attached to has the "effect" on any claim which does not tolerate the taint and, through the claim, to pods using the claim.

Type
:   `object`

Required
:   * `key`
    * `effect`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | The effect of the taint on claims that do not tolerate the taint and through such claims on the pods using them.  Valid effects are None, NoSchedule and NoExecute. PreferNoSchedule as used for nodes is not valid here. More effects may get added in the future. Consumers must treat unknown effects like None.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the device taint. - `"NoSchedule"` Do not allow new pods to schedule which use a tainted device unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. - `"None"` No effect, the taint is purely informational. |
| `key` | `string` | The taint key to be applied to a device. Must be a label name. |
| `timeAdded` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | TimeAdded represents the time at which the taint was added. Added automatically during create or update if not set. |
| `value` | `string` | The taint value corresponding to the taint key. Must be a label value. |

Show more

#### [12.1.16. .spec.pool](#spec-pool) Copy linkLink copied to clipboard!

Description
:   ResourcePool describes the pool that ResourceSlices belong to.

Type
:   `object`

Required
:   * `name`
    * `generation`
    * `resourceSliceCount`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `generation` | `integer` | Generation tracks the change in a pool over time. Whenever a driver changes something about one or more of the resources in a pool, it must change the generation in all ResourceSlices which are part of that pool. Consumers of ResourceSlices should only consider resources from the pool with the highest generation number. The generation may be reset by drivers, which should be fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.  Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are comprised of multiple ResourceSlices and are in an incomplete state. |
| `name` | `string` | Name is used to identify the pool. For node-local devices, this is often the node name, but this is not required.  It must not be longer than 253 characters and must consist of one or more DNS sub-domains separated by slashes. This field is immutable. |
| `resourceSliceCount` | `integer` | ResourceSliceCount is the total number of ResourceSlices in the pool at this generation number. Must be greater than zero.  Consumers can use this to check whether they have seen all ResourceSlices belonging to the same pool. |

Show more

#### [12.1.17. .spec.sharedCounters](#spec-sharedcounters) Copy linkLink copied to clipboard!

Description
:   SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.

    The names of the counter sets must be unique in the ResourcePool.

    Only one of Devices and SharedCounters can be set in a ResourceSlice.

    The maximum number of counter sets is 8.

Type
:   `array`

#### [12.1.18. .spec.sharedCounters[]](#spec-sharedcounters-2) Copy linkLink copied to clipboard!

Description
:   CounterSet defines a named set of counters that are available to be used by devices defined in the ResourcePool.

    The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.

Type
:   `object`

Required
:   * `name`
    * `counters`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `counters` | `object` | Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.  The maximum number of counters is 32. |
| `counters{}` | `object` | Counter describes a quantity associated with a device. |
| `name` | `string` | Name defines the name of the counter set. It must be a DNS label. |

Show more

#### [12.1.19. .spec.sharedCounters[].counters](#spec-sharedcounters-counters) Copy linkLink copied to clipboard!

Description
:   Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.

    The maximum number of counters is 32.

Type
:   `object`

#### [12.1.20. .spec.sharedCounters[].counters{}](#spec-sharedcounters-counters-2) Copy linkLink copied to clipboard!

Description
:   Counter describes a quantity associated with a device.

Type
:   `object`

Required
:   * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `value` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Value defines how much of a certain device counter is available. |

Show more

### [12.2. API endpoints](#api-endpoints-11) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/resource.k8s.io/v1/resourceslices`

  + `DELETE`: delete collection of ResourceSlice
  + `GET`: list or watch objects of kind ResourceSlice
  + `POST`: create a ResourceSlice
* `/apis/resource.k8s.io/v1/watch/resourceslices`

  + `GET`: watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/resource.k8s.io/v1/resourceslices/{name}`

  + `DELETE`: delete a ResourceSlice
  + `GET`: read the specified ResourceSlice
  + `PATCH`: partially update the specified ResourceSlice
  + `PUT`: replace the specified ResourceSlice
* `/apis/resource.k8s.io/v1/watch/resourceslices/{name}`

  + `GET`: watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [12.2.1. /apis/resource.k8s.io/v1/resourceslices](#apisresource-k8s-iov1resourceslices) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ResourceSlice

Expand

Table 12.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 12.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind ResourceSlice

Expand

Table 12.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceSliceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceSliceList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ResourceSlice

Expand

Table 12.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 12.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.2. /apis/resource.k8s.io/v1/watch/resourceslices](#apisresource-k8s-iov1watchresourceslices) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 12.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.3. /apis/resource.k8s.io/v1/resourceslices/{name}](#apisresource-k8s-iov1resourceslicesname) Copy linkLink copied to clipboard!

Expand

Table 12.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceSlice |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ResourceSlice

Expand

Table 12.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 12.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 202 - Accepted | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ResourceSlice

Expand

Table 12.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ResourceSlice

Expand

Table 12.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ResourceSlice

Expand

Table 12.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |  |

Show more

Expand

Table 12.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 201 - Created | [`ResourceSlice`](#resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice [resource.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.4. /apis/resource.k8s.io/v1/watch/resourceslices/{name}](#apisresource-k8s-iov1watchresourceslicesname) Copy linkLink copied to clipboard!

Expand

Table 12.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ResourceSlice |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 12.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm139879741575088) Copy linkLink copied to clipboard!

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
