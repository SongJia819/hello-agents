---
title: "RBAC APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/index
retrieved_at: 2026-09-05T05:42:46.985062+00:00
---

# RBAC APIs

---

OpenShift Container Platform 4.22

## Reference guide for RBAC APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140021808695824)

**Abstract**

This document describes the OpenShift Container Platform RBAC API objects and their detailed specifications.

---

## [Chapter 1. RBAC APIs](#rbac-apis) Copy linkLink copied to clipboard!

### [1.1. ClusterRoleBinding [rbac.authorization.k8s.io/v1]](#clusterrolebinding-rbac-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterRoleBinding references a ClusterRole, but not contain it. It can reference a ClusterRole in the global namespace, and adds who information via Subject.

Type
:   `object`

### [1.2. ClusterRole [rbac.authorization.k8s.io/v1]](#clusterrole-rbac-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding.

Type
:   `object`

### [1.3. RoleBinding [rbac.authorization.k8s.io/v1]](#rolebinding-rbac-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   RoleBinding references a role, but does not contain it. It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in. RoleBindings in a given namespace only have effect in that namespace.

Type
:   `object`

### [1.4. Role [rbac.authorization.k8s.io/v1]](#role-rbac-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding.

Type
:   `object`

## [Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]](#clusterrolebinding-rbac-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterRoleBinding references a ClusterRole, but not contain it. It can reference a ClusterRole in the global namespace, and adds who information via Subject.

Type
:   `object`

Required
:   * `roleRef`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. |
| `roleRef` | `object` | RoleRef contains information that points to the role being used |
| `subjects` | `array` | Subjects holds references to the objects the role applies to. |
| `subjects[]` | `object` | Subject contains a reference to the object or user identities a role binding applies to. This can either hold a direct API object reference, or a value for non-objects such as user and group names. |

Show more

#### [2.1.1. .roleRef](#roleref) Copy linkLink copied to clipboard!

Description
:   RoleRef contains information that points to the role being used

Type
:   `object`

Required
:   * `apiGroup`
    * `kind`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

Show more

#### [2.1.2. .subjects](#subjects) Copy linkLink copied to clipboard!

Description
:   Subjects holds references to the objects the role applies to.

Type
:   `array`

#### [2.1.3. .subjects[]](#subjects-2) Copy linkLink copied to clipboard!

Description
:   Subject contains a reference to the object or user identities a role binding applies to. This can either hold a direct API object reference, or a value for non-objects such as user and group names.

Type
:   `object`

Required
:   * `kind`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. |
| `kind` | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. |
| `name` | `string` | Name of the object being referenced. |
| `namespace` | `string` | Namespace of the referenced object. If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/rbac.authorization.k8s.io/v1/clusterrolebindings`

  + `DELETE`: delete collection of ClusterRoleBinding
  + `GET`: list or watch objects of kind ClusterRoleBinding
  + `POST`: create a ClusterRoleBinding
* `/apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings`

  + `GET`: watch individual changes to a list of ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/rbac.authorization.k8s.io/v1/clusterrolebindings/{name}`

  + `DELETE`: delete a ClusterRoleBinding
  + `GET`: read the specified ClusterRoleBinding
  + `PATCH`: partially update the specified ClusterRoleBinding
  + `PUT`: replace the specified ClusterRoleBinding
* `/apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings/{name}`

  + `GET`: watch changes to an object of kind ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [2.2.1. /apis/rbac.authorization.k8s.io/v1/clusterrolebindings](#apisrbac-authorization-k8s-iov1clusterrolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ClusterRoleBinding

Expand

Table 2.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 2.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind ClusterRoleBinding

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-ClusterRoleBindingList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterRoleBinding

Expand

Table 2.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 2.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings](#apisrbac-authorization-k8s-iov1watchclusterrolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 2.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/rbac.authorization.k8s.io/v1/clusterrolebindings/{name}](#apisrbac-authorization-k8s-iov1clusterrolebindingsname) Copy linkLink copied to clipboard!

Expand

Table 2.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterRoleBinding |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterRoleBinding

Expand

Table 2.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 2.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ClusterRoleBinding

Expand

Table 2.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterRoleBinding

Expand

Table 2.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterRoleBinding

Expand

Table 2.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`ClusterRoleBinding`](#clusterrolebinding-rbac-authorization-k8s-io-v1 "Chapter 2. ClusterRoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings/{name}](#apisrbac-authorization-k8s-iov1watchclusterrolebindingsname) Copy linkLink copied to clipboard!

Expand

Table 2.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterRoleBinding |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 2.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]](#clusterrole-rbac-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding.

Type
:   `object`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `aggregationRule` | `object` | AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. |
| `rules` | `array` | Rules holds all the PolicyRules for this ClusterRole |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

Show more

#### [3.1.1. .aggregationRule](#aggregationrule) Copy linkLink copied to clipboard!

Description
:   AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterRoleSelectors` | [`array (LabelSelector)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole’s permissions will be added |

Show more

#### [3.1.2. .rules](#rules) Copy linkLink copied to clipboard!

Description
:   Rules holds all the PolicyRules for this ClusterRole

Type
:   `array`

#### [3.1.3. .rules[]](#rules-2) Copy linkLink copied to clipboard!

Description
:   PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
:   `object`

Required
:   * `verbs`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroups` | `array (string)` | APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "\*" represents all API groups. |
| `nonResourceURLs` | `array (string)` | NonResourceURLs is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both. |
| `resourceNames` | `array (string)` | ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | Resources is a list of resources this rule applies to. '\*' represents all resources. |
| `verbs` | `array (string)` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/rbac.authorization.k8s.io/v1/clusterroles`

  + `DELETE`: delete collection of ClusterRole
  + `GET`: list or watch objects of kind ClusterRole
  + `POST`: create a ClusterRole
* `/apis/rbac.authorization.k8s.io/v1/watch/clusterroles`

  + `GET`: watch individual changes to a list of ClusterRole. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/rbac.authorization.k8s.io/v1/clusterroles/{name}`

  + `DELETE`: delete a ClusterRole
  + `GET`: read the specified ClusterRole
  + `PATCH`: partially update the specified ClusterRole
  + `PUT`: replace the specified ClusterRole
* `/apis/rbac.authorization.k8s.io/v1/watch/clusterroles/{name}`

  + `GET`: watch changes to an object of kind ClusterRole. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [3.2.1. /apis/rbac.authorization.k8s.io/v1/clusterroles](#apisrbac-authorization-k8s-iov1clusterroles) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ClusterRole

Expand

Table 3.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind ClusterRole

Expand

Table 3.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-ClusterRoleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterRole

Expand

Table 3.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 3.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/rbac.authorization.k8s.io/v1/watch/clusterroles](#apisrbac-authorization-k8s-iov1watchclusterroles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of ClusterRole. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/rbac.authorization.k8s.io/v1/clusterroles/{name}](#apisrbac-authorization-k8s-iov1clusterrolesname) Copy linkLink copied to clipboard!

Expand

Table 3.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterRole |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterRole

Expand

Table 3.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ClusterRole

Expand

Table 3.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterRole

Expand

Table 3.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterRole

Expand

Table 3.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 3.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`ClusterRole`](#clusterrole-rbac-authorization-k8s-io-v1 "Chapter 3. ClusterRole [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/rbac.authorization.k8s.io/v1/watch/clusterroles/{name}](#apisrbac-authorization-k8s-iov1watchclusterrolesname) Copy linkLink copied to clipboard!

Expand

Table 3.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterRole |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind ClusterRole. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]](#rolebinding-rbac-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   RoleBinding references a role, but does not contain it. It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in. RoleBindings in a given namespace only have effect in that namespace.

Type
:   `object`

Required
:   * `roleRef`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. |
| `roleRef` | `object` | RoleRef contains information that points to the role being used |
| `subjects` | `array` | Subjects holds references to the objects the role applies to. |
| `subjects[]` | `object` | Subject contains a reference to the object or user identities a role binding applies to. This can either hold a direct API object reference, or a value for non-objects such as user and group names. |

Show more

#### [4.1.1. .roleRef](#roleref-2) Copy linkLink copied to clipboard!

Description
:   RoleRef contains information that points to the role being used

Type
:   `object`

Required
:   * `apiGroup`
    * `kind`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

Show more

#### [4.1.2. .subjects](#subjects-3) Copy linkLink copied to clipboard!

Description
:   Subjects holds references to the objects the role applies to.

Type
:   `array`

#### [4.1.3. .subjects[]](#subjects-4) Copy linkLink copied to clipboard!

Description
:   Subject contains a reference to the object or user identities a role binding applies to. This can either hold a direct API object reference, or a value for non-objects such as user and group names.

Type
:   `object`

Required
:   * `kind`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. |
| `kind` | `string` | Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. |
| `name` | `string` | Name of the object being referenced. |
| `namespace` | `string` | Namespace of the referenced object. If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/rbac.authorization.k8s.io/v1/rolebindings`

  + `GET`: list or watch objects of kind RoleBinding
* `/apis/rbac.authorization.k8s.io/v1/watch/rolebindings`

  + `GET`: watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings`

  + `DELETE`: delete collection of RoleBinding
  + `GET`: list or watch objects of kind RoleBinding
  + `POST`: create a RoleBinding
* `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings`

  + `GET`: watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings/{name}`

  + `DELETE`: delete a RoleBinding
  + `GET`: read the specified RoleBinding
  + `PATCH`: partially update the specified RoleBinding
  + `PUT`: replace the specified RoleBinding
* `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings/{name}`

  + `GET`: watch changes to an object of kind RoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [4.2.1. /apis/rbac.authorization.k8s.io/v1/rolebindings](#apisrbac-authorization-k8s-iov1rolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind RoleBinding

Expand

Table 4.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleBindingList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/rbac.authorization.k8s.io/v1/watch/rolebindings](#apisrbac-authorization-k8s-iov1watchrolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings](#apisrbac-authorization-k8s-iov1namespacesnamespacerolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of RoleBinding

Expand

Table 4.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind RoleBinding

Expand

Table 4.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleBindingList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a RoleBinding

Expand

Table 4.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 4.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.4. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings](#apisrbac-authorization-k8s-iov1watchnamespacesnamespacerolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.5. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings/{name}](#apisrbac-authorization-k8s-iov1namespacesnamespacerolebindingsname) Copy linkLink copied to clipboard!

Expand

Table 4.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the RoleBinding |

Show more

HTTP method
:   `DELETE`

Description
:   delete a RoleBinding

Expand

Table 4.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified RoleBinding

Expand

Table 4.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified RoleBinding

Expand

Table 4.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified RoleBinding

Expand

Table 4.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 4.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`RoleBinding`](#rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.6. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings/{name}](#apisrbac-authorization-k8s-iov1watchnamespacesnamespacerolebindingsname) Copy linkLink copied to clipboard!

Expand

Table 4.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the RoleBinding |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind RoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 4.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. Role [rbac.authorization.k8s.io/v1]](#role-rbac-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding.

Type
:   `object`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. |
| `rules` | `array` | Rules holds all the PolicyRules for this Role |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

Show more

#### [5.1.1. .rules](#rules-3) Copy linkLink copied to clipboard!

Description
:   Rules holds all the PolicyRules for this Role

Type
:   `array`

#### [5.1.2. .rules[]](#rules-4) Copy linkLink copied to clipboard!

Description
:   PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
:   `object`

Required
:   * `verbs`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroups` | `array (string)` | APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "\*" represents all API groups. |
| `nonResourceURLs` | `array (string)` | NonResourceURLs is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both. |
| `resourceNames` | `array (string)` | ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | Resources is a list of resources this rule applies to. '\*' represents all resources. |
| `verbs` | `array (string)` | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '\*' represents all verbs. |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/rbac.authorization.k8s.io/v1/roles`

  + `GET`: list or watch objects of kind Role
* `/apis/rbac.authorization.k8s.io/v1/watch/roles`

  + `GET`: watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles`

  + `DELETE`: delete collection of Role
  + `GET`: list or watch objects of kind Role
  + `POST`: create a Role
* `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles`

  + `GET`: watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles/{name}`

  + `DELETE`: delete a Role
  + `GET`: read the specified Role
  + `PATCH`: partially update the specified Role
  + `PUT`: replace the specified Role
* `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles/{name}`

  + `GET`: watch changes to an object of kind Role. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [5.2.1. /apis/rbac.authorization.k8s.io/v1/roles](#apisrbac-authorization-k8s-iov1roles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind Role

Expand

Table 5.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/rbac.authorization.k8s.io/v1/watch/roles](#apisrbac-authorization-k8s-iov1watchroles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles](#apisrbac-authorization-k8s-iov1namespacesnamespaceroles) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Role

Expand

Table 5.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 5.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind Role

Expand

Table 5.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Role

Expand

Table 5.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.7. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 5.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.4. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles](#apisrbac-authorization-k8s-iov1watchnamespacesnamespaceroles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.5. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles/{name}](#apisrbac-authorization-k8s-iov1namespacesnamespacerolesname) Copy linkLink copied to clipboard!

Expand

Table 5.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Role |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Role

Expand

Table 5.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 5.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Role

Expand

Table 5.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Role

Expand

Table 5.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Role

Expand

Table 5.16. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.17. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 201 - Created | [`Role`](#role-rbac-authorization-k8s-io-v1 "Chapter 5. Role [rbac.authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.6. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles/{name}](#apisrbac-authorization-k8s-iov1watchnamespacesnamespacerolesname) Copy linkLink copied to clipboard!

Expand

Table 5.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Role |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind Role. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 5.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140021808695824) Copy linkLink copied to clipboard!

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
