---
title: "Authorization APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/index
retrieved_at: 2026-09-05T05:41:33.591619+00:00
---

# Authorization APIs

---

OpenShift Container Platform 4.22

## Reference guide for authorization APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140638203732192)

**Abstract**

This document describes the OpenShift Container Platform authorization API objects and their detailed specifications.

---

## [Chapter 1. Authorization APIs](#authorization-apis) Copy linkLink copied to clipboard!

### [1.1. LocalResourceAccessReview [authorization.openshift.io/v1]](#localresourceaccessreview-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   LocalResourceAccessReview is a means to request a list of which users and groups are authorized to perform the action specified by spec in a particular namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. LocalSubjectAccessReview [authorization.openshift.io/v1]](#localsubjectaccessreview-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   LocalSubjectAccessReview is an object for requesting information about whether a user or group can perform an action in a particular namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. ResourceAccessReview [authorization.openshift.io/v1]](#resourceaccessreview-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ResourceAccessReview is a means to request a list of which users and groups are authorized to perform the action specified by spec

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. SelfSubjectRulesReview [authorization.openshift.io/v1]](#selfsubjectrulesreview-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectRulesReview is a resource you can create to determine which actions you can perform in a namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.5. SubjectAccessReview [authorization.openshift.io/v1]](#subjectaccessreview-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReview is an object for requesting information about whether a user or group can perform an action

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.6. SubjectRulesReview [authorization.openshift.io/v1]](#subjectrulesreview-authorization-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   SubjectRulesReview is a resource you can create to determine which actions another user can perform in a namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.7. SelfSubjectReview [authentication.k8s.io/v1]](#selfsubjectreview-authentication-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated. If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase.

Type
:   `object`

### [1.8. TokenRequest [authentication.k8s.io/v1]](#tokenrequest-authentication-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   TokenRequest requests a token for a given service account.

Type
:   `object`

### [1.9. TokenReview [authentication.k8s.io/v1]](#tokenreview-authentication-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver.

Type
:   `object`

### [1.10. LocalSubjectAccessReview [authorization.k8s.io/v1]](#localsubjectaccessreview-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking.

Type
:   `object`

### [1.11. SelfSubjectAccessReview [authorization.k8s.io/v1]](#selfsubjectaccessreview-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectAccessReview checks whether or the current user can perform an action. Not filling in a spec.namespace means "in all namespaces". Self is a special case, because users should always be able to check whether they can perform an action

Type
:   `object`

### [1.12. SelfSubjectRulesReview [authorization.k8s.io/v1]](#selfsubjectrulesreview-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server’s authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server.

Type
:   `object`

### [1.13. SubjectAccessReview [authorization.k8s.io/v1]](#subjectaccessreview-authorization-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReview checks whether or not a user or group can perform an action.

Type
:   `object`

## [Chapter 2. LocalResourceAccessReview [authorization.openshift.io/v1]](#localresourceaccessreview-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   LocalResourceAccessReview is a means to request a list of which users and groups are authorized to perform the action specified by spec in a particular namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `namespace`
    * `verb`
    * `resourceAPIGroup`
    * `resourceAPIVersion`
    * `resource`
    * `resourceName`
    * `path`
    * `isNonResourceURL`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `content` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | content is the actual content of the request for create and update |
| `isNonResourceURL` | `boolean` | isNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy) |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `namespace` | `string` | namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces |
| `path` | `string` | path is the path of a non resource URL |
| `resource` | `string` | resource is one of the existing resource types |
| `resourceAPIGroup` | `string` | Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined |
| `resourceAPIVersion` | `string` | Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined |
| `resourceName` | `string` | resourceName is the name of the resource being requested for a "get" or deleted for a "delete" |
| `verb` | `string` | verb is one of: get, list, watch, create, update, delete |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/localresourceaccessreviews`

  + `POST`: create a LocalResourceAccessReview

#### [2.2.1. /apis/authorization.openshift.io/v1/namespaces/{namespace}/localresourceaccessreviews](#apisauthorization-openshift-iov1namespacesnamespacelocalresourceaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 2.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a LocalResourceAccessReview

Expand

Table 2.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`LocalResourceAccessReview`](#localresourceaccessreview-authorization-openshift-io-v1 "Chapter 2. LocalResourceAccessReview [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LocalResourceAccessReview`](#localresourceaccessreview-authorization-openshift-io-v1 "Chapter 2. LocalResourceAccessReview [authorization.openshift.io/v1]") schema |
| 201 - Created | [`LocalResourceAccessReview`](#localresourceaccessreview-authorization-openshift-io-v1 "Chapter 2. LocalResourceAccessReview [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`LocalResourceAccessReview`](#localresourceaccessreview-authorization-openshift-io-v1 "Chapter 2. LocalResourceAccessReview [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. LocalSubjectAccessReview [authorization.openshift.io/v1]](#localsubjectaccessreview-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   LocalSubjectAccessReview is an object for requesting information about whether a user or group can perform an action in a particular namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `namespace`
    * `verb`
    * `resourceAPIGroup`
    * `resourceAPIVersion`
    * `resource`
    * `resourceName`
    * `path`
    * `isNonResourceURL`
    * `user`
    * `groups`
    * `scopes`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `content` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | content is the actual content of the request for create and update |
| `groups` | `array (string)` | groups is optional. Groups is the list of groups to which the User belongs. |
| `isNonResourceURL` | `boolean` | isNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy) |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `namespace` | `string` | namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces |
| `path` | `string` | path is the path of a non resource URL |
| `resource` | `string` | resource is one of the existing resource types |
| `resourceAPIGroup` | `string` | Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined |
| `resourceAPIVersion` | `string` | Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined |
| `resourceName` | `string` | resourceName is the name of the resource being requested for a "get" or deleted for a "delete" |
| `scopes` | `array (string)` | scopes to use for the evaluation. Empty means "use the unscoped (full) permissions of the user/groups". Nil for a self-SAR, means "use the scopes on this request". Nil for a regular SAR, means the same as empty. |
| `user` | `string` | user is optional. If both User and Groups are empty, the current authenticated user is used. |
| `verb` | `string` | verb is one of: get, list, watch, create, update, delete |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/localsubjectaccessreviews`

  + `POST`: create a LocalSubjectAccessReview

#### [3.2.1. /apis/authorization.openshift.io/v1/namespaces/{namespace}/localsubjectaccessreviews](#apisauthorization-openshift-iov1namespacesnamespacelocalsubjectaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 3.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a LocalSubjectAccessReview

Expand

Table 3.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-openshift-io-v1 "Chapter 3. LocalSubjectAccessReview [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-openshift-io-v1 "Chapter 3. LocalSubjectAccessReview [authorization.openshift.io/v1]") schema |
| 201 - Created | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-openshift-io-v1 "Chapter 3. LocalSubjectAccessReview [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-openshift-io-v1 "Chapter 3. LocalSubjectAccessReview [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. ResourceAccessReview [authorization.openshift.io/v1]](#resourceaccessreview-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ResourceAccessReview is a means to request a list of which users and groups are authorized to perform the action specified by spec

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `namespace`
    * `verb`
    * `resourceAPIGroup`
    * `resourceAPIVersion`
    * `resource`
    * `resourceName`
    * `path`
    * `isNonResourceURL`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `content` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | content is the actual content of the request for create and update |
| `isNonResourceURL` | `boolean` | isNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy) |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `namespace` | `string` | namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces |
| `path` | `string` | path is the path of a non resource URL |
| `resource` | `string` | resource is one of the existing resource types |
| `resourceAPIGroup` | `string` | Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined |
| `resourceAPIVersion` | `string` | Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined |
| `resourceName` | `string` | resourceName is the name of the resource being requested for a "get" or deleted for a "delete" |
| `verb` | `string` | verb is one of: get, list, watch, create, update, delete |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/resourceaccessreviews`

  + `POST`: create a ResourceAccessReview

#### [4.2.1. /apis/authorization.openshift.io/v1/resourceaccessreviews](#apisauthorization-openshift-iov1resourceaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 4.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a ResourceAccessReview

Expand

Table 4.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ResourceAccessReview`](#resourceaccessreview-authorization-openshift-io-v1 "Chapter 4. ResourceAccessReview [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ResourceAccessReview`](#resourceaccessreview-authorization-openshift-io-v1 "Chapter 4. ResourceAccessReview [authorization.openshift.io/v1]") schema |
| 201 - Created | [`ResourceAccessReview`](#resourceaccessreview-authorization-openshift-io-v1 "Chapter 4. ResourceAccessReview [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`ResourceAccessReview`](#resourceaccessreview-authorization-openshift-io-v1 "Chapter 4. ResourceAccessReview [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. SelfSubjectRulesReview [authorization.openshift.io/v1]](#selfsubjectrulesreview-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectRulesReview is a resource you can create to determine which actions you can perform in a namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | SelfSubjectRulesReviewSpec adds information about how to conduct the check |
| `status` | `object` | SubjectRulesReviewStatus is contains the result of a rules check |

Show more

#### [5.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   SelfSubjectRulesReviewSpec adds information about how to conduct the check

Type
:   `object`

Required
:   * `scopes`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `scopes` | `array (string)` | scopes to use for the evaluation. Empty means "use the unscoped (full) permissions of the user/groups". Nil means "use the scopes on this request". |

Show more

#### [5.1.2. .status](#status) Copy linkLink copied to clipboard!

Description
:   SubjectRulesReviewStatus is contains the result of a rules check

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `evaluationError` | `string` | evaluationError can appear in combination with Rules. It means some error happened during evaluation that may have prevented additional rules from being populated. |
| `rules` | `array` | rules is the list of rules (no particular sort) that are allowed for the subject |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

Show more

#### [5.1.3. .status.rules](#status-rules) Copy linkLink copied to clipboard!

Description
:   rules is the list of rules (no particular sort) that are allowed for the subject

Type
:   `array`

#### [5.1.4. .status.rules[]](#status-rules-2) Copy linkLink copied to clipboard!

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

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/selfsubjectrulesreviews`

  + `POST`: create a SelfSubjectRulesReview

#### [5.2.1. /apis/authorization.openshift.io/v1/namespaces/{namespace}/selfsubjectrulesreviews](#apisauthorization-openshift-iov1namespacesnamespaceselfsubjectrulesreviews) Copy linkLink copied to clipboard!

Expand

Table 5.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SelfSubjectRulesReview

Expand

Table 5.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview [authorization.openshift.io/v1]") schema |
| 201 - Created | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. SubjectAccessReview [authorization.openshift.io/v1]](#subjectaccessreview-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReview is an object for requesting information about whether a user or group can perform an action

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `namespace`
    * `verb`
    * `resourceAPIGroup`
    * `resourceAPIVersion`
    * `resource`
    * `resourceName`
    * `path`
    * `isNonResourceURL`
    * `user`
    * `groups`
    * `scopes`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `content` | [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | content is the actual content of the request for create and update |
| `groups` | `array (string)` | GroupsSlice is optional. Groups is the list of groups to which the User belongs. |
| `isNonResourceURL` | `boolean` | isNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy) |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `namespace` | `string` | namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces |
| `path` | `string` | path is the path of a non resource URL |
| `resource` | `string` | resource is one of the existing resource types |
| `resourceAPIGroup` | `string` | Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined |
| `resourceAPIVersion` | `string` | Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined |
| `resourceName` | `string` | resourceName is the name of the resource being requested for a "get" or deleted for a "delete" |
| `scopes` | `array (string)` | scopes to use for the evaluation. Empty means "use the unscoped (full) permissions of the user/groups". Nil for a self-SAR, means "use the scopes on this request". Nil for a regular SAR, means the same as empty. |
| `user` | `string` | user is optional. If both User and Groups are empty, the current authenticated user is used. |
| `verb` | `string` | verb is one of: get, list, watch, create, update, delete |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/subjectaccessreviews`

  + `POST`: create a SubjectAccessReview

#### [6.2.1. /apis/authorization.openshift.io/v1/subjectaccessreviews](#apisauthorization-openshift-iov1subjectaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 6.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SubjectAccessReview

Expand

Table 6.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SubjectAccessReview`](#subjectaccessreview-authorization-openshift-io-v1 "Chapter 6. SubjectAccessReview [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SubjectAccessReview`](#subjectaccessreview-authorization-openshift-io-v1 "Chapter 6. SubjectAccessReview [authorization.openshift.io/v1]") schema |
| 201 - Created | [`SubjectAccessReview`](#subjectaccessreview-authorization-openshift-io-v1 "Chapter 6. SubjectAccessReview [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`SubjectAccessReview`](#subjectaccessreview-authorization-openshift-io-v1 "Chapter 6. SubjectAccessReview [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 7. SubjectRulesReview [authorization.openshift.io/v1]](#subjectrulesreview-authorization-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   SubjectRulesReview is a resource you can create to determine which actions another user can perform in a namespace

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [7.1. Specification](#specification-6) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | SubjectRulesReviewSpec adds information about how to conduct the check |
| `status` | `object` | SubjectRulesReviewStatus is contains the result of a rules check |

Show more

#### [7.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   SubjectRulesReviewSpec adds information about how to conduct the check

Type
:   `object`

Required
:   * `user`
    * `groups`
    * `scopes`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `groups` | `array (string)` | groups is optional. Groups is the list of groups to which the User belongs. At least one of User and Groups must be specified. |
| `scopes` | `array (string)` | scopes to use for the evaluation. Empty means "use the unscoped (full) permissions of the user/groups". |
| `user` | `string` | user is optional. At least one of User and Groups must be specified. |

Show more

#### [7.1.2. .status](#status-2) Copy linkLink copied to clipboard!

Description
:   SubjectRulesReviewStatus is contains the result of a rules check

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `evaluationError` | `string` | evaluationError can appear in combination with Rules. It means some error happened during evaluation that may have prevented additional rules from being populated. |
| `rules` | `array` | rules is the list of rules (no particular sort) that are allowed for the subject |
| `rules[]` | `object` | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to. |

Show more

#### [7.1.3. .status.rules](#status-rules-3) Copy linkLink copied to clipboard!

Description
:   rules is the list of rules (no particular sort) that are allowed for the subject

Type
:   `array`

#### [7.1.4. .status.rules[]](#status-rules-4) Copy linkLink copied to clipboard!

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

### [7.2. API endpoints](#api-endpoints-6) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.openshift.io/v1/namespaces/{namespace}/subjectrulesreviews`

  + `POST`: create a SubjectRulesReview

#### [7.2.1. /apis/authorization.openshift.io/v1/namespaces/{namespace}/subjectrulesreviews](#apisauthorization-openshift-iov1namespacesnamespacesubjectrulesreviews) Copy linkLink copied to clipboard!

Expand

Table 7.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SubjectRulesReview

Expand

Table 7.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SubjectRulesReview`](#subjectrulesreview-authorization-openshift-io-v1 "Chapter 7. SubjectRulesReview [authorization.openshift.io/v1]") schema |  |

Show more

Expand

Table 7.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SubjectRulesReview`](#subjectrulesreview-authorization-openshift-io-v1 "Chapter 7. SubjectRulesReview [authorization.openshift.io/v1]") schema |
| 201 - Created | [`SubjectRulesReview`](#subjectrulesreview-authorization-openshift-io-v1 "Chapter 7. SubjectRulesReview [authorization.openshift.io/v1]") schema |
| 202 - Accepted | [`SubjectRulesReview`](#subjectrulesreview-authorization-openshift-io-v1 "Chapter 7. SubjectRulesReview [authorization.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 8. SelfSubjectReview [authentication.k8s.io/v1]](#selfsubjectreview-authentication-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated. If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase.

Type
:   `object`

### [8.1. Specification](#specification-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `status` | `object` | SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user. |

Show more

#### [8.1.1. .status](#status-3) Copy linkLink copied to clipboard!

Description
:   SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `userInfo` | `object` | UserInfo holds the information about the user needed to implement the user.Info interface. |

Show more

#### [8.1.2. .status.userInfo](#status-userinfo) Copy linkLink copied to clipboard!

Description
:   UserInfo holds the information about the user needed to implement the user.Info interface.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `extra` | `object` | Any additional information provided by the authenticator. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | The names of groups this user is a part of. |
| `uid` | `string` | A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. |
| `username` | `string` | The name that uniquely identifies this user among all active users. |

Show more

#### [8.1.3. .status.userInfo.extra](#status-userinfo-extra) Copy linkLink copied to clipboard!

Description
:   Any additional information provided by the authenticator.

Type
:   `object`

### [8.2. API endpoints](#api-endpoints-7) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authentication.k8s.io/v1/selfsubjectreviews`

  + `POST`: create a SelfSubjectReview

#### [8.2.1. /apis/authentication.k8s.io/v1/selfsubjectreviews](#apisauthentication-k8s-iov1selfsubjectreviews) Copy linkLink copied to clipboard!

Expand

Table 8.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SelfSubjectReview

Expand

Table 8.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SelfSubjectReview`](#selfsubjectreview-authentication-k8s-io-v1 "Chapter 8. SelfSubjectReview [authentication.k8s.io/v1]") schema |  |

Show more

Expand

Table 8.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SelfSubjectReview`](#selfsubjectreview-authentication-k8s-io-v1 "Chapter 8. SelfSubjectReview [authentication.k8s.io/v1]") schema |
| 201 - Created | [`SelfSubjectReview`](#selfsubjectreview-authentication-k8s-io-v1 "Chapter 8. SelfSubjectReview [authentication.k8s.io/v1]") schema |
| 202 - Accepted | [`SelfSubjectReview`](#selfsubjectreview-authentication-k8s-io-v1 "Chapter 8. SelfSubjectReview [authentication.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 9. TokenRequest [authentication.k8s.io/v1]](#tokenrequest-authentication-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   TokenRequest requests a token for a given service account.

Type
:   `object`

Required
:   * `spec`

### [9.1. Specification](#specification-8) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | TokenRequestSpec contains client provided parameters of a token request. |
| `status` | `object` | TokenRequestStatus is the result of a token request. |

Show more

#### [9.1.1. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   TokenRequestSpec contains client provided parameters of a token request.

Type
:   `object`

Required
:   * `audiences`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `audiences` | `array (string)` | Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. |
| `boundObjectRef` | `object` | BoundObjectReference is a reference to an object that a token is bound to. |
| `expirationSeconds` | `integer` | ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. |

Show more

#### [9.1.2. .spec.boundObjectRef](#spec-boundobjectref) Copy linkLink copied to clipboard!

Description
:   BoundObjectReference is a reference to an object that a token is bound to.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | API version of the referent. |
| `kind` | `string` | Kind of the referent. Valid kinds are 'Pod' and 'Secret'. |
| `name` | `string` | Name of the referent. |
| `uid` | `string` | UID of the referent. |

Show more

#### [9.1.3. .status](#status-4) Copy linkLink copied to clipboard!

Description
:   TokenRequestStatus is the result of a token request.

Type
:   `object`

Required
:   * `token`
    * `expirationTimestamp`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `expirationTimestamp` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | ExpirationTimestamp is the time of expiration of the returned token. |
| `token` | `string` | Token is the opaque bearer token. |

Show more

### [9.2. API endpoints](#api-endpoints-8) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/namespaces/{namespace}/serviceaccounts/{name}/token`

  + `POST`: create token of a ServiceAccount

#### [9.2.1. /api/v1/namespaces/{namespace}/serviceaccounts/{name}/token](#apiv1namespacesnamespaceserviceaccountsnametoken) Copy linkLink copied to clipboard!

Expand

Table 9.1. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the TokenRequest |

Show more

Expand

Table 9.2. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create token of a ServiceAccount

Expand

Table 9.3. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`TokenRequest`](#tokenrequest-authentication-k8s-io-v1 "Chapter 9. TokenRequest [authentication.k8s.io/v1]") schema |  |

Show more

Expand

Table 9.4. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TokenRequest`](#tokenrequest-authentication-k8s-io-v1 "Chapter 9. TokenRequest [authentication.k8s.io/v1]") schema |
| 201 - Created | [`TokenRequest`](#tokenrequest-authentication-k8s-io-v1 "Chapter 9. TokenRequest [authentication.k8s.io/v1]") schema |
| 202 - Accepted | [`TokenRequest`](#tokenrequest-authentication-k8s-io-v1 "Chapter 9. TokenRequest [authentication.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 10. TokenReview [authentication.k8s.io/v1]](#tokenreview-authentication-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | TokenReviewSpec is a description of the token authentication request. |
| `status` | `object` | TokenReviewStatus is the result of the token authentication request. |

Show more

#### [10.1.1. .spec](#spec-4) Copy linkLink copied to clipboard!

Description
:   TokenReviewSpec is a description of the token authentication request.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `audiences` | `array (string)` | Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. |
| `token` | `string` | Token is the opaque bearer token. |

Show more

#### [10.1.2. .status](#status-5) Copy linkLink copied to clipboard!

Description
:   TokenReviewStatus is the result of the token authentication request.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `audiences` | `array (string)` | Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token’s audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server. |
| `authenticated` | `boolean` | Authenticated indicates that the token was associated with a known user. |
| `error` | `string` | Error indicates that the token couldn’t be checked |
| `user` | `object` | UserInfo holds the information about the user needed to implement the user.Info interface. |

Show more

#### [10.1.3. .status.user](#status-user) Copy linkLink copied to clipboard!

Description
:   UserInfo holds the information about the user needed to implement the user.Info interface.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `extra` | `object` | Any additional information provided by the authenticator. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | The names of groups this user is a part of. |
| `uid` | `string` | A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. |
| `username` | `string` | The name that uniquely identifies this user among all active users. |

Show more

#### [10.1.4. .status.user.extra](#status-user-extra) Copy linkLink copied to clipboard!

Description
:   Any additional information provided by the authenticator.

Type
:   `object`

### [10.2. API endpoints](#api-endpoints-9) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/oauth.openshift.io/v1/tokenreviews`

  + `POST`: create a TokenReview
* `/apis/authentication.k8s.io/v1/tokenreviews`

  + `POST`: create a TokenReview

#### [10.2.1. /apis/oauth.openshift.io/v1/tokenreviews](#apisoauth-openshift-iov1tokenreviews) Copy linkLink copied to clipboard!

Expand

Table 10.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a TokenReview

Expand

Table 10.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |
| 201 - Created | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |
| 202 - Accepted | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.2. /apis/authentication.k8s.io/v1/tokenreviews](#apisauthentication-k8s-iov1tokenreviews) Copy linkLink copied to clipboard!

Expand

Table 10.4. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a TokenReview

Expand

Table 10.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |
| 201 - Created | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |
| 202 - Accepted | [`TokenReview`](#tokenreview-authentication-k8s-io-v1 "Chapter 10. TokenReview [authentication.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 11. LocalSubjectAccessReview [authorization.k8s.io/v1]](#localsubjectaccessreview-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set |
| `status` | `object` | SubjectAccessReviewStatus |

Show more

#### [11.1.1. .spec](#spec-5) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `extra` | `object` | Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer it needs a reflection here. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | Groups is the groups you’re testing for. |
| `nonResourceAttributes` | `object` | NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface |
| `resourceAttributes` | `object` | ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface |
| `uid` | `string` | UID information about the requesting user. |
| `user` | `string` | User is the user you’re testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups |

Show more

#### [11.1.2. .spec.extra](#spec-extra) Copy linkLink copied to clipboard!

Description
:   Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer it needs a reflection here.

Type
:   `object`

#### [11.1.3. .spec.nonResourceAttributes](#spec-nonresourceattributes) Copy linkLink copied to clipboard!

Description
:   NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `path` | `string` | Path is the URL path of the request |
| `verb` | `string` | Verb is the standard HTTP verb |

Show more

#### [11.1.4. .spec.resourceAttributes](#spec-resourceattributes) Copy linkLink copied to clipboard!

Description
:   ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldSelector` | `object` | FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid. |
| `group` | `string` | Group is the API Group of the Resource. "\*" means all. |
| `labelSelector` | `object` | LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid. |
| `name` | `string` | Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. |
| `namespace` | `string` | Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview |
| `resource` | `string` | Resource is one of the existing resource types. "\*" means all. |
| `subresource` | `string` | Subresource is one of the existing resource types. "" means none. |
| `verb` | `string` | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "\*" means all. |
| `version` | `string` | Version is the API Version of the Resource. "\*" means all. |

Show more

#### [11.1.5. .spec.resourceAttributes.fieldSelector](#spec-resourceattributes-fieldselector) Copy linkLink copied to clipboard!

Description
:   FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | [`array (FieldSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-FieldSelectorRequirement) | requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |

Show more

#### [11.1.6. .spec.resourceAttributes.labelSelector](#spec-resourceattributes-labelselector) Copy linkLink copied to clipboard!

Description
:   LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | [`array (LabelSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement) | requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |

Show more

#### [11.1.7. .status](#status-6) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReviewStatus

Type
:   `object`

Required
:   * `allowed`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowed` | `boolean` | Allowed is required. True if the action would be allowed, false otherwise. |
| `denied` | `boolean` | Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. |
| `evaluationError` | `string` | EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. |
| `reason` | `string` | Reason is optional. It indicates why a request was allowed or denied. |

Show more

### [11.2. API endpoints](#api-endpoints-10) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.k8s.io/v1/namespaces/{namespace}/localsubjectaccessreviews`

  + `POST`: create a LocalSubjectAccessReview

#### [11.2.1. /apis/authorization.k8s.io/v1/namespaces/{namespace}/localsubjectaccessreviews](#apisauthorization-k8s-iov1namespacesnamespacelocalsubjectaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 11.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a LocalSubjectAccessReview

Expand

Table 11.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-k8s-io-v1 "Chapter 11. LocalSubjectAccessReview [authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 11.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-k8s-io-v1 "Chapter 11. LocalSubjectAccessReview [authorization.k8s.io/v1]") schema |
| 201 - Created | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-k8s-io-v1 "Chapter 11. LocalSubjectAccessReview [authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`LocalSubjectAccessReview`](#localsubjectaccessreview-authorization-k8s-io-v1 "Chapter 11. LocalSubjectAccessReview [authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 12. SelfSubjectAccessReview [authorization.k8s.io/v1]](#selfsubjectaccessreview-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectAccessReview checks whether or the current user can perform an action. Not filling in a spec.namespace means "in all namespaces". Self is a special case, because users should always be able to check whether they can perform an action

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | SelfSubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set |
| `status` | `object` | SubjectAccessReviewStatus |

Show more

#### [12.1.1. .spec](#spec-6) Copy linkLink copied to clipboard!

Description
:   SelfSubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nonResourceAttributes` | `object` | NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface |
| `resourceAttributes` | `object` | ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface |

Show more

#### [12.1.2. .spec.nonResourceAttributes](#spec-nonresourceattributes-2) Copy linkLink copied to clipboard!

Description
:   NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `path` | `string` | Path is the URL path of the request |
| `verb` | `string` | Verb is the standard HTTP verb |

Show more

#### [12.1.3. .spec.resourceAttributes](#spec-resourceattributes-2) Copy linkLink copied to clipboard!

Description
:   ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldSelector` | `object` | FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid. |
| `group` | `string` | Group is the API Group of the Resource. "\*" means all. |
| `labelSelector` | `object` | LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid. |
| `name` | `string` | Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. |
| `namespace` | `string` | Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview |
| `resource` | `string` | Resource is one of the existing resource types. "\*" means all. |
| `subresource` | `string` | Subresource is one of the existing resource types. "" means none. |
| `verb` | `string` | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "\*" means all. |
| `version` | `string` | Version is the API Version of the Resource. "\*" means all. |

Show more

#### [12.1.4. .spec.resourceAttributes.fieldSelector](#spec-resourceattributes-fieldselector-2) Copy linkLink copied to clipboard!

Description
:   FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | [`array (FieldSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-FieldSelectorRequirement) | requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |

Show more

#### [12.1.5. .spec.resourceAttributes.labelSelector](#spec-resourceattributes-labelselector-2) Copy linkLink copied to clipboard!

Description
:   LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | [`array (LabelSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement) | requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |

Show more

#### [12.1.6. .status](#status-7) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReviewStatus

Type
:   `object`

Required
:   * `allowed`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowed` | `boolean` | Allowed is required. True if the action would be allowed, false otherwise. |
| `denied` | `boolean` | Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. |
| `evaluationError` | `string` | EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. |
| `reason` | `string` | Reason is optional. It indicates why a request was allowed or denied. |

Show more

### [12.2. API endpoints](#api-endpoints-11) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.k8s.io/v1/selfsubjectaccessreviews`

  + `POST`: create a SelfSubjectAccessReview

#### [12.2.1. /apis/authorization.k8s.io/v1/selfsubjectaccessreviews](#apisauthorization-k8s-iov1selfsubjectaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 12.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SelfSubjectAccessReview

Expand

Table 12.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SelfSubjectAccessReview`](#selfsubjectaccessreview-authorization-k8s-io-v1 "Chapter 12. SelfSubjectAccessReview [authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 12.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SelfSubjectAccessReview`](#selfsubjectaccessreview-authorization-k8s-io-v1 "Chapter 12. SelfSubjectAccessReview [authorization.k8s.io/v1]") schema |
| 201 - Created | [`SelfSubjectAccessReview`](#selfsubjectaccessreview-authorization-k8s-io-v1 "Chapter 12. SelfSubjectAccessReview [authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`SelfSubjectAccessReview`](#selfsubjectaccessreview-authorization-k8s-io-v1 "Chapter 12. SelfSubjectAccessReview [authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 13. SelfSubjectRulesReview [authorization.k8s.io/v1]](#selfsubjectrulesreview-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server’s authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server.

Type
:   `object`

Required
:   * `spec`

### [13.1. Specification](#specification-12) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview. |
| `status` | `object` | SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it’s safe to assume the subject has that permission, even if that list is incomplete. |

Show more

#### [13.1.1. .spec](#spec-7) Copy linkLink copied to clipboard!

Description
:   SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `namespace` | `string` | Namespace to evaluate rules for. Required. |

Show more

#### [13.1.2. .status](#status-8) Copy linkLink copied to clipboard!

Description
:   SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it’s safe to assume the subject has that permission, even if that list is incomplete.

Type
:   `object`

Required
:   * `resourceRules`
    * `nonResourceRules`
    * `incomplete`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `evaluationError` | `string` | EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn’t support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. |
| `incomplete` | `boolean` | Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn’t support rules evaluation. |
| `nonResourceRules` | `array` | NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete. |
| `nonResourceRules[]` | `object` | NonResourceRule holds information that describes a rule for the non-resource |
| `resourceRules` | `array` | ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete. |
| `resourceRules[]` | `object` | ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete. |

Show more

#### [13.1.3. .status.nonResourceRules](#status-nonresourcerules) Copy linkLink copied to clipboard!

Description
:   NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete.

Type
:   `array`

#### [13.1.4. .status.nonResourceRules[]](#status-nonresourcerules-2) Copy linkLink copied to clipboard!

Description
:   NonResourceRule holds information that describes a rule for the non-resource

Type
:   `object`

Required
:   * `verbs`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nonResourceURLs` | `array (string)` | NonResourceURLs is a set of partial urls that a user should have access to. **s are allowed, but only as the full, final step in the path. "**" means all. |
| `verbs` | `array (string)` | Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options. "\*" means all. |

Show more

#### [13.1.5. .status.resourceRules](#status-resourcerules) Copy linkLink copied to clipboard!

Description
:   ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete.

Type
:   `array`

#### [13.1.6. .status.resourceRules[]](#status-resourcerules-2) Copy linkLink copied to clipboard!

Description
:   ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn’t significant, may contain duplicates, and possibly be incomplete.

Type
:   `object`

Required
:   * `verbs`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroups` | `array (string)` | APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "\*" means all. |
| `resourceNames` | `array (string)` | ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed. "\*" means all. |
| `resources` | `array (string)` | Resources is a list of resources this rule applies to. "**" means all in the specified apiGroups. "**/foo" represents the subresource 'foo' for all resources in the specified apiGroups. |
| `verbs` | `array (string)` | Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy. "\*" means all. |

Show more

### [13.2. API endpoints](#api-endpoints-12) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.k8s.io/v1/selfsubjectrulesreviews`

  + `POST`: create a SelfSubjectRulesReview

#### [13.2.1. /apis/authorization.k8s.io/v1/selfsubjectrulesreviews](#apisauthorization-k8s-iov1selfsubjectrulesreviews) Copy linkLink copied to clipboard!

Expand

Table 13.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SelfSubjectRulesReview

Expand

Table 13.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-k8s-io-v1 "Chapter 13. SelfSubjectRulesReview [authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 13.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-k8s-io-v1 "Chapter 13. SelfSubjectRulesReview [authorization.k8s.io/v1]") schema |
| 201 - Created | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-k8s-io-v1 "Chapter 13. SelfSubjectRulesReview [authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`SelfSubjectRulesReview`](#selfsubjectrulesreview-authorization-k8s-io-v1 "Chapter 13. SelfSubjectRulesReview [authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 14. SubjectAccessReview [authorization.k8s.io/v1]](#subjectaccessreview-authorization-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReview checks whether or not a user or group can perform an action.

Type
:   `object`

Required
:   * `spec`

### [14.1. Specification](#specification-13) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set |
| `status` | `object` | SubjectAccessReviewStatus |

Show more

#### [14.1.1. .spec](#spec-8) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `extra` | `object` | Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer it needs a reflection here. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | Groups is the groups you’re testing for. |
| `nonResourceAttributes` | `object` | NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface |
| `resourceAttributes` | `object` | ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface |
| `uid` | `string` | UID information about the requesting user. |
| `user` | `string` | User is the user you’re testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups |

Show more

#### [14.1.2. .spec.extra](#spec-extra-2) Copy linkLink copied to clipboard!

Description
:   Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer it needs a reflection here.

Type
:   `object`

#### [14.1.3. .spec.nonResourceAttributes](#spec-nonresourceattributes-3) Copy linkLink copied to clipboard!

Description
:   NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `path` | `string` | Path is the URL path of the request |
| `verb` | `string` | Verb is the standard HTTP verb |

Show more

#### [14.1.4. .spec.resourceAttributes](#spec-resourceattributes-3) Copy linkLink copied to clipboard!

Description
:   ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldSelector` | `object` | FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid. |
| `group` | `string` | Group is the API Group of the Resource. "\*" means all. |
| `labelSelector` | `object` | LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid. |
| `name` | `string` | Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. |
| `namespace` | `string` | Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview |
| `resource` | `string` | Resource is one of the existing resource types. "\*" means all. |
| `subresource` | `string` | Subresource is one of the existing resource types. "" means none. |
| `verb` | `string` | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "\*" means all. |
| `version` | `string` | Version is the API Version of the Resource. "\*" means all. |

Show more

#### [14.1.5. .spec.resourceAttributes.fieldSelector](#spec-resourceattributes-fieldselector-3) Copy linkLink copied to clipboard!

Description
:   FieldSelectorAttributes indicates a field limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | [`array (FieldSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-FieldSelectorRequirement) | requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |

Show more

#### [14.1.6. .spec.resourceAttributes.labelSelector](#spec-resourceattributes-labelselector-3) Copy linkLink copied to clipboard!

Description
:   LabelSelectorAttributes indicates a label limited access. Webhook authors are encouraged to \* ensure rawSelector and requirements are not both set \* consider the requirements field if set \* not try to parse or consider the rawSelector field if set. This is to avoid another CVE-2022-2880 (i.e. getting different systems to agree on how exactly to parse a query is not something we want), see <https://www.oxeye.io/resources/golang-parameter-smuggling-attack> for more details. For the \*SubjectAccessReview endpoints of the kube-apiserver: \* If rawSelector is empty and requirements are empty, the request is not limited. \* If rawSelector is present and requirements are empty, the rawSelector will be parsed and limited if the parsing succeeds. \* If rawSelector is empty and requirements are present, the requirements should be honored \* If rawSelector is present and requirements are present, the request is invalid.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | [`array (LabelSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement) | requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |

Show more

#### [14.1.7. .status](#status-9) Copy linkLink copied to clipboard!

Description
:   SubjectAccessReviewStatus

Type
:   `object`

Required
:   * `allowed`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowed` | `boolean` | Allowed is required. True if the action would be allowed, false otherwise. |
| `denied` | `boolean` | Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. |
| `evaluationError` | `string` | EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. |
| `reason` | `string` | Reason is optional. It indicates why a request was allowed or denied. |

Show more

### [14.2. API endpoints](#api-endpoints-13) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/authorization.k8s.io/v1/subjectaccessreviews`

  + `POST`: create a SubjectAccessReview

#### [14.2.1. /apis/authorization.k8s.io/v1/subjectaccessreviews](#apisauthorization-k8s-iov1subjectaccessreviews) Copy linkLink copied to clipboard!

Expand

Table 14.1. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a SubjectAccessReview

Expand

Table 14.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`SubjectAccessReview`](#subjectaccessreview-authorization-k8s-io-v1 "Chapter 14. SubjectAccessReview [authorization.k8s.io/v1]") schema |  |

Show more

Expand

Table 14.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SubjectAccessReview`](#subjectaccessreview-authorization-k8s-io-v1 "Chapter 14. SubjectAccessReview [authorization.k8s.io/v1]") schema |
| 201 - Created | [`SubjectAccessReview`](#subjectaccessreview-authorization-k8s-io-v1 "Chapter 14. SubjectAccessReview [authorization.k8s.io/v1]") schema |
| 202 - Accepted | [`SubjectAccessReview`](#subjectaccessreview-authorization-k8s-io-v1 "Chapter 14. SubjectAccessReview [authorization.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140638203732192) Copy linkLink copied to clipboard!

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
