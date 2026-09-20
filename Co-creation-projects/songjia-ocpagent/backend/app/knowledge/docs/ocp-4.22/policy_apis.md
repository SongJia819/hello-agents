---
title: "Policy APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/policy_apis/index
retrieved_at: 2026-09-05T05:42:43.889465+00:00
---

# Policy APIs

---

OpenShift Container Platform 4.22

## Reference guide for policy APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139684269053968)

**Abstract**

This document describes the OpenShift Container Platform policy API objects and their detailed specifications.

---

## [Chapter 1. Policy APIs](#policy-apis) Copy linkLink copied to clipboard!

### [1.1. Eviction [policy/v1]](#eviction-policyv1) Copy linkLink copied to clipboard!

Description
:   Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod. A request to cause such an eviction is created by POSTing to …​/pods/<pod name>/evictions.

Type
:   `object`

### [1.2. PodDisruptionBudget [policy/v1]](#poddisruptionbudget-policyv1) Copy linkLink copied to clipboard!

Description
:   PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods

Type
:   `object`

## [Chapter 2. Eviction [policy/v1]](#eviction-policy-v1) Copy linkLink copied to clipboard!

Description
:   Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod. A request to cause such an eviction is created by POSTing to …​/pods/<pod name>/evictions.

Type
:   `object`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `deleteOptions` | [`DeleteOptions`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-DeleteOptions) | DeleteOptions may be provided |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | ObjectMeta describes the pod that is being evicted. |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/namespaces/{namespace}/pods/{name}/eviction`

  + `POST`: create eviction of a Pod

#### [2.2.1. /api/v1/namespaces/{namespace}/pods/{name}/eviction](#apiv1namespacesnamespacepodsnameeviction) Copy linkLink copied to clipboard!

Expand

Table 2.1. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Eviction |

Show more

Expand

Table 2.2. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create eviction of a Pod

Expand

Table 2.3. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Eviction`](#eviction-policy-v1 "Chapter 2. Eviction [policy/v1]") schema |  |

Show more

Expand

Table 2.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Eviction`](#eviction-policy-v1 "Chapter 2. Eviction [policy/v1]") schema |
| 201 - Created | [`Eviction`](#eviction-policy-v1 "Chapter 2. Eviction [policy/v1]") schema |
| 202 - Accepted | [`Eviction`](#eviction-policy-v1 "Chapter 2. Eviction [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. PodDisruptionBudget [policy/v1]](#poddisruptionbudget-policy-v1) Copy linkLink copied to clipboard!

Description
:   PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods

Type
:   `object`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PodDisruptionBudgetSpec is a description of a PodDisruptionBudget. |
| `status` | `object` | PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system. |

Show more

#### [3.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `maxUnavailable` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable". |
| `minAvailable` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod. So for example you can prevent all voluntary evictions by specifying "100%". |
| `selector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace. |
| `unhealthyPodEvictionPolicy` | `string` | UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".  Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.  IfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.  AlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.  Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.  Possible enum values: - `"AlwaysAllow"` policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction. - `"IfHealthyBudget"` policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction. |

Show more

#### [3.1.2. .status](#status) Copy linkLink copied to clipboard!

Description
:   PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system.

Type
:   `object`

Required
:   * `disruptionsAllowed`
    * `currentHealthy`
    * `desiredHealthy`
    * `expectedPods`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | [`array (Condition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Condition) | Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn’t able to compute the number of allowed disruptions. Therefore no disruptions are allowed and the status of the condition will be False. - InsufficientPods: The number of pods are either at or below the number required by the PodDisruptionBudget. No disruptions are allowed and the status of the condition will be False. - SufficientPods: There are more pods than required by the PodDisruptionBudget. The condition will be True, and the number of allowed disruptions are provided by the disruptionsAllowed property. |
| `currentHealthy` | `integer` | current number of healthy pods |
| `desiredHealthy` | `integer` | minimum desired number of healthy pods |
| `disruptedPods` | [`object (Time)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn’t occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions. |
| `disruptionsAllowed` | `integer` | Number of pod disruptions that are currently allowed. |
| `expectedPods` | `integer` | total number of pods counted by this disruption budget |
| `observedGeneration` | `integer` | Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB’s object generation. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/policy/v1/poddisruptionbudgets`

  + `GET`: list or watch objects of kind PodDisruptionBudget
* `/apis/policy/v1/watch/poddisruptionbudgets`

  + `GET`: watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets`

  + `DELETE`: delete collection of PodDisruptionBudget
  + `GET`: list or watch objects of kind PodDisruptionBudget
  + `POST`: create a PodDisruptionBudget
* `/apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets`

  + `GET`: watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}`

  + `DELETE`: delete a PodDisruptionBudget
  + `GET`: read the specified PodDisruptionBudget
  + `PATCH`: partially update the specified PodDisruptionBudget
  + `PUT`: replace the specified PodDisruptionBudget
* `/apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets/{name}`

  + `GET`: watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}/status`

  + `GET`: read status of the specified PodDisruptionBudget
  + `PATCH`: partially update status of the specified PodDisruptionBudget
  + `PUT`: replace status of the specified PodDisruptionBudget

#### [3.2.1. /apis/policy/v1/poddisruptionbudgets](#apispolicyv1poddisruptionbudgets) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind PodDisruptionBudget

Expand

Table 3.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudgetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-policy-v1-PodDisruptionBudgetList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/policy/v1/watch/poddisruptionbudgets](#apispolicyv1watchpoddisruptionbudgets) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets](#apispolicyv1namespacesnamespacepoddisruptionbudgets) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PodDisruptionBudget

Expand

Table 3.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind PodDisruptionBudget

Expand

Table 3.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudgetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-policy-v1-PodDisruptionBudgetList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PodDisruptionBudget

Expand

Table 3.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |  |

Show more

Expand

Table 3.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 201 - Created | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 202 - Accepted | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets](#apispolicyv1watchnamespacesnamespacepoddisruptionbudgets) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.5. /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}](#apispolicyv1namespacesnamespacepoddisruptionbudgetsname) Copy linkLink copied to clipboard!

Expand

Table 3.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PodDisruptionBudget |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PodDisruptionBudget

Expand

Table 3.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PodDisruptionBudget

Expand

Table 3.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PodDisruptionBudget

Expand

Table 3.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 201 - Created | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PodDisruptionBudget

Expand

Table 3.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |  |

Show more

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 201 - Created | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.6. /apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets/{name}](#apispolicyv1watchnamespacesnamespacepoddisruptionbudgetsname) Copy linkLink copied to clipboard!

Expand

Table 3.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PodDisruptionBudget |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.7. /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}/status](#apispolicyv1namespacesnamespacepoddisruptionbudgetsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 3.21. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PodDisruptionBudget |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified PodDisruptionBudget

Expand

Table 3.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified PodDisruptionBudget

Expand

Table 3.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.24. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 201 - Created | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified PodDisruptionBudget

Expand

Table 3.25. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.26. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |  |

Show more

Expand

Table 3.27. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 201 - Created | [`PodDisruptionBudget`](#poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget [policy/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm139684269053968) Copy linkLink copied to clipboard!

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
