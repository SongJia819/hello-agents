---
title: "Role APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/index
retrieved_at: 2026-09-05T05:42:47.872021+00:00
---

# Role APIs

---

OpenShift Container Platform 4.22

## Reference guide for role APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139643529323344)

**Abstract**

This document describes the OpenShift Container Platform role API objects and their detailed specifications.

---

## [Chapter 1. Role APIs](#role-apis) Copy linkLink copied to clipboard!

### [1.1. ClusterRoleBinding [authorization.openshift.io/v1]](#clusterrolebinding-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterRoleBinding references a ClusterRole, but not contain it. It can reference any ClusterRole in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. ClusterRoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces).

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. ClusterRole [authorization.openshift.io/v1]](#clusterrole-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterRole is a logical grouping of PolicyRules that can be referenced as a unit by ClusterRoleBindings.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. RoleBindingRestriction [authorization.openshift.io/v1]](#rolebindingrestriction-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   RoleBindingRestriction is an object that can be matched against a subject (user, group, or service account) to determine whether rolebindings on that subject are allowed in the namespace to which the RoleBindingRestriction belongs. If any one of those RoleBindingRestriction objects matches a subject, rolebindings on that subject in the namespace are allowed.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. RoleBinding [authorization.openshift.io/v1]](#rolebinding-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   RoleBinding references a Role, but not contain it. It can reference any Role in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. RoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces).

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.5. Role [authorization.openshift.io/v1]](#role-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Role is a logical grouping of PolicyRules that can be referenced as a unit by RoleBindings.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

## [Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]](#clusterrolebinding-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterRoleBinding references a ClusterRole, but not contain it. It can reference any ClusterRole in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. ClusterRoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces).

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `subjects`
    * `roleRef`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `groupNames` | `array (string)` | groupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `roleRef` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | roleRef can only reference the current namespace and the global namespace. If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role. |
| `subjects` | [`array (ObjectReference)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames. |
| `userNames` | `array (string)` | userNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details. |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/clusterrolebindings`

  + `GET`: list objects of kind ClusterRoleBinding
  + `POST`: create a ClusterRoleBinding
* `/apis/authorization.openshift.io/v1/clusterrolebindings/{name}`

  + `DELETE`: delete a ClusterRoleBinding
  + `GET`: read the specified ClusterRoleBinding
  + `PATCH`: partially update the specified ClusterRoleBinding
  + `PUT`: replace the specified ClusterRoleBinding

#### [2.2.1. /apis/authorization.openshift.io/v1/clusterrolebindings](#apisauthorization-openshift-iov1clusterrolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind ClusterRoleBinding

Expand

Table 2.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-authorization-v1-ClusterRoleBindingList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterRoleBinding

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
| `body` | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/authorization.openshift.io/v1/clusterrolebindings/{name}](#apisauthorization-openshift-iov1clusterrolebindingsname) Copy linkLink copied to clipboard!

Expand

Table 2.5. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterRoleBinding |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterRoleBinding

Expand

Table 2.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 2.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ClusterRoleBinding

Expand

Table 2.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterRoleBinding

Expand

Table 2.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterRoleBinding

Expand

Table 2.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.12. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ClusterRoleBinding`](#clusterrolebinding-authorization-openshift-io-v1 "Chapter 2. ClusterRoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. ClusterRole [authorization.openshift.io/v1]](#clusterrole-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterRole is a logical grouping of PolicyRules that can be referenced as a unit by ClusterRoleBindings.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `rules`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `aggregationRule` | [`AggregationRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-AggregationRule) | aggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `rules` | `array` | rules holds all the PolicyRules for this ClusterRole |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

Show more

#### [3.1.1. .rules](#rules) Copy linkLink copied to clipboard!

Description
:   rules holds all the PolicyRules for this ClusterRole

Type
:   `array`

#### [3.1.2. .rules[]](#rules-2) Copy linkLink copied to clipboard!

Description
:   PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
:   `object`

Required
:   * `verbs`
    * `resources`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroups` | `array (string)` | apiGroups is the name of the APIGroup that contains the resources. If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed |
| `attributeRestrictions` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | attributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error. |
| `nonResourceURLs` | `array (string)` | NonResourceURLsSlice is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different. |
| `resourceNames` | `array (string)` | resourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | resources is a list of resources this rule applies to. ResourceAll represents all resources. |
| `verbs` | `array (string)` | verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule. VerbAll represents all kinds. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/clusterroles`

  + `GET`: list objects of kind ClusterRole
  + `POST`: create a ClusterRole
* `/apis/authorization.openshift.io/v1/clusterroles/{name}`

  + `DELETE`: delete a ClusterRole
  + `GET`: read the specified ClusterRole
  + `PATCH`: partially update the specified ClusterRole
  + `PUT`: replace the specified ClusterRole

#### [3.2.1. /apis/authorization.openshift.io/v1/clusterroles](#apisauthorization-openshift-iov1clusterroles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind ClusterRole

Expand

Table 3.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-authorization-v1-ClusterRoleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterRole

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
| `body` | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/authorization.openshift.io/v1/clusterroles/{name}](#apisauthorization-openshift-iov1clusterrolesname) Copy linkLink copied to clipboard!

Expand

Table 3.5. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterRole |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterRole

Expand

Table 3.6. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ClusterRole

Expand

Table 3.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterRole

Expand

Table 3.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterRole

Expand

Table 3.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.12. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ClusterRole`](#clusterrole-authorization-openshift-io-v1 "Chapter 3. ClusterRole [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]](#rolebindingrestriction-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   RoleBindingRestriction is an object that can be matched against a subject (user, group, or service account) to determine whether rolebindings on that subject are allowed in the namespace to which the RoleBindingRestriction belongs. If any one of those RoleBindingRestriction objects matches a subject, rolebindings on that subject in the namespace are allowed.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec defines the matcher. |

Show more

#### [4.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   spec defines the matcher.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `grouprestriction` | `` | grouprestriction matches against group subjects. |
| `serviceaccountrestriction` | `` | serviceaccountrestriction matches against service-account subjects. |
| `userrestriction` | `` | userrestriction matches against user subjects. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/rolebindingrestrictions`

  + `GET`: list objects of kind RoleBindingRestriction
* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions`

  + `DELETE`: delete collection of RoleBindingRestriction
  + `GET`: list objects of kind RoleBindingRestriction
  + `POST`: create a RoleBindingRestriction
* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions/{name}`

  + `DELETE`: delete a RoleBindingRestriction
  + `GET`: read the specified RoleBindingRestriction
  + `PATCH`: partially update the specified RoleBindingRestriction
  + `PUT`: replace the specified RoleBindingRestriction

#### [4.2.1. /apis/authorization.openshift.io/v1/rolebindingrestrictions](#apisauthorization-openshift-iov1rolebindingrestrictions) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind RoleBindingRestriction

Expand

Table 4.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingRestrictionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-authorization-v1-RoleBindingRestrictionList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions](#apisauthorization-openshift-iov1namespacesnamespacerolebindingrestrictions) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of RoleBindingRestriction

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
:   list objects of kind RoleBindingRestriction

Expand

Table 4.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingRestrictionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-authorization-v1-RoleBindingRestrictionList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a RoleBindingRestriction

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
| `body` | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 201 - Created | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindingrestrictions/{name}](#apisauthorization-openshift-iov1namespacesnamespacerolebindingrestrictionsname) Copy linkLink copied to clipboard!

Expand

Table 4.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the RoleBindingRestriction |

Show more

HTTP method
:   `DELETE`

Description
:   delete a RoleBindingRestriction

Expand

Table 4.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified RoleBindingRestriction

Expand

Table 4.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified RoleBindingRestriction

Expand

Table 4.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified RoleBindingRestriction

Expand

Table 4.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 201 - Created | [`RoleBindingRestriction`](#rolebindingrestriction-authorization-openshift-io-v1 "Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. RoleBinding [authorization.openshift.io/v1]](#rolebinding-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   RoleBinding references a Role, but not contain it. It can reference any Role in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. RoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces).

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `subjects`
    * `roleRef`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `groupNames` | `array (string)` | groupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `roleRef` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | roleRef can only reference the current namespace and the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role. |
| `subjects` | [`array (ObjectReference)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames. |
| `userNames` | `array (string)` | userNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details. |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/rolebindings`

  + `GET`: list objects of kind RoleBinding
* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindings`

  + `GET`: list objects of kind RoleBinding
  + `POST`: create a RoleBinding
* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindings/{name}`

  + `DELETE`: delete a RoleBinding
  + `GET`: read the specified RoleBinding
  + `PATCH`: partially update the specified RoleBinding
  + `PUT`: replace the specified RoleBinding

#### [5.2.1. /apis/authorization.openshift.io/v1/rolebindings](#apisauthorization-openshift-iov1rolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind RoleBinding

Expand

Table 5.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-authorization-v1-RoleBindingList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindings](#apisauthorization-openshift-iov1namespacesnamespacerolebindings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind RoleBinding

Expand

Table 5.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-authorization-v1-RoleBindingList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a RoleBinding

Expand

Table 5.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 201 - Created | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/authorization.openshift.io/v1/namespaces/{namespace}/rolebindings/{name}](#apisauthorization-openshift-iov1namespacesnamespacerolebindingsname) Copy linkLink copied to clipboard!

Expand

Table 5.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the RoleBinding |

Show more

HTTP method
:   `DELETE`

Description
:   delete a RoleBinding

Expand

Table 5.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 5.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified RoleBinding

Expand

Table 5.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified RoleBinding

Expand

Table 5.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 201 - Created | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified RoleBinding

Expand

Table 5.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 201 - Created | [`RoleBinding`](#rolebinding-authorization-openshift-io-v1 "Chapter 5. RoleBinding [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. Role [authorization.openshift.io/v1]](#role-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Role is a logical grouping of PolicyRules that can be referenced as a unit by RoleBindings.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `rules`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `rules` | `array` | rules holds all the PolicyRules for this Role |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

Show more

#### [6.1.1. .rules](#rules-3) Copy linkLink copied to clipboard!

Description
:   rules holds all the PolicyRules for this Role

Type
:   `array`

#### [6.1.2. .rules[]](#rules-4) Copy linkLink copied to clipboard!

Description
:   PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

Type
:   `object`

Required
:   * `verbs`
    * `resources`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroups` | `array (string)` | apiGroups is the name of the APIGroup that contains the resources. If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed |
| `attributeRestrictions` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | attributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error. |
| `nonResourceURLs` | `array (string)` | NonResourceURLsSlice is a set of partial urls that a user should have access to. \*s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different. |
| `resourceNames` | `array (string)` | resourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. |
| `resources` | `array (string)` | resources is a list of resources this rule applies to. ResourceAll represents all resources. |
| `verbs` | `array (string)` | verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule. VerbAll represents all kinds. |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/roles`

  + `GET`: list objects of kind Role
* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/roles`

  + `GET`: list objects of kind Role
  + `POST`: create a Role
* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/roles/{name}`

  + `DELETE`: delete a Role
  + `GET`: read the specified Role
  + `PATCH`: partially update the specified Role
  + `PUT`: replace the specified Role

#### [6.2.1. /apis/authorization.openshift.io/v1/roles](#apisauthorization-openshift-iov1roles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind Role

Expand

Table 6.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-authorization-v1-RoleList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /apis/authorization.openshift.io/v1/namespaces/{namespace}/roles](#apisauthorization-openshift-iov1namespacesnamespaceroles) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind Role

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`RoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-authorization-v1-RoleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Role

Expand

Table 6.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 201 - Created | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.3. /apis/authorization.openshift.io/v1/namespaces/{namespace}/roles/{name}](#apisauthorization-openshift-iov1namespacesnamespacerolesname) Copy linkLink copied to clipboard!

Expand

Table 6.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Role |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Role

Expand

Table 6.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 6.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Role

Expand

Table 6.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Role

Expand

Table 6.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 201 - Created | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Role

Expand

Table 6.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 201 - Created | [`Role`](#role-authorization-openshift-io-v1 "Chapter 6. Role [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm139643529323344) Copy linkLink copied to clipboard!

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
