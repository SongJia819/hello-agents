---
title: "User and group APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/index
retrieved_at: 2026-09-05T05:43:01.301757+00:00
---

# User and group APIs

---

OpenShift Container Platform 4.22

## Reference guide for user and group APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139981907719136)

**Abstract**

This document describes the OpenShift Container Platform user and group API objects and their detailed specifications.

---

## [Chapter 1. User and group APIs](#user-and-group-apis) Copy linkLink copied to clipboard!

### [1.1. Group [user.openshift.io/v1]](#group-user-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Group represents a referenceable set of Users

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. Identity [user.openshift.io/v1]](#identity-user-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Identity records a successful authentication of a user with an identity provider. The information about the source of authentication is stored on the identity, and the identity is then associated with a single user object. Multiple identities can reference a single user. Information retrieved from the authentication provider is stored in the extra field using a schema determined by the provider.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. UserIdentityMapping [user.openshift.io/v1]](#useridentitymapping-user-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   UserIdentityMapping maps a user to an identity

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. User [user.openshift.io/v1]](#user-user-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Upon log in, every user of the system receives a User and Identity resource. Administrators may directly manipulate the attributes of the users for their own tracking, or set groups via the API. The user name is unique and is chosen based on the value provided by the identity provider - if a user already exists with the incoming name, the user name may have a number appended to it depending on the configuration of the system.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

## [Chapter 2. Group [user.openshift.io/v1]](#group-user-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Group represents a referenceable set of Users

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `users`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `users` | `array (string)` | users is the list of users in this group. |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/user.openshift.io/v1/groups`

  + `DELETE`: delete collection of Group
  + `GET`: list or watch objects of kind Group
  + `POST`: create a Group
* `/apis/user.openshift.io/v1/watch/groups`

  + `GET`: watch individual changes to a list of Group. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/user.openshift.io/v1/groups/{name}`

  + `DELETE`: delete a Group
  + `GET`: read the specified Group
  + `PATCH`: partially update the specified Group
  + `PUT`: replace the specified Group
* `/apis/user.openshift.io/v1/watch/groups/{name}`

  + `GET`: watch changes to an object of kind Group. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [2.2.1. /apis/user.openshift.io/v1/groups](#apisuser-openshift-iov1groups) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Group

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind Group

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`GroupList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-user-v1-GroupList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Group

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
| `body` | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 201 - Created | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 202 - Accepted | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/user.openshift.io/v1/watch/groups](#apisuser-openshift-iov1watchgroups) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Group. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 2.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/user.openshift.io/v1/groups/{name}](#apisuser-openshift-iov1groupsname) Copy linkLink copied to clipboard!

Expand

Table 2.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Group |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Group

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Group

Expand

Table 2.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Group

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
| 200 - OK | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 201 - Created | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Group

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
| `body` | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 201 - Created | [`Group`](#group-user-openshift-io-v1 "Chapter 2. Group [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/user.openshift.io/v1/watch/groups/{name}](#apisuser-openshift-iov1watchgroupsname) Copy linkLink copied to clipboard!

Expand

Table 2.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Group |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind Group. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 2.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. Identity [user.openshift.io/v1]](#identity-user-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Identity records a successful authentication of a user with an identity provider. The information about the source of authentication is stored on the identity, and the identity is then associated with a single user object. Multiple identities can reference a single user. Information retrieved from the authentication provider is stored in the extra field using a schema determined by the provider.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `providerName`
    * `providerUserName`
    * `user`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `extra` | `object (string)` | extra holds extra information about this identity |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `providerName` | `string` | providerName is the source of identity information |
| `providerUserName` | `string` | providerUserName uniquely represents this identity in the scope of the provider |
| `user` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | user is a reference to the user this identity is associated with Both Name and UID must be set |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/user.openshift.io/v1/identities`

  + `DELETE`: delete collection of Identity
  + `GET`: list or watch objects of kind Identity
  + `POST`: create an Identity
* `/apis/user.openshift.io/v1/watch/identities`

  + `GET`: watch individual changes to a list of Identity. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/user.openshift.io/v1/identities/{name}`

  + `DELETE`: delete an Identity
  + `GET`: read the specified Identity
  + `PATCH`: partially update the specified Identity
  + `PUT`: replace the specified Identity
* `/apis/user.openshift.io/v1/watch/identities/{name}`

  + `GET`: watch changes to an object of kind Identity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [3.2.1. /apis/user.openshift.io/v1/identities](#apisuser-openshift-iov1identities) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Identity

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind Identity

Expand

Table 3.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`IdentityList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-user-v1-IdentityList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an Identity

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
| `body` | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 201 - Created | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 202 - Accepted | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/user.openshift.io/v1/watch/identities](#apisuser-openshift-iov1watchidentities) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Identity. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/user.openshift.io/v1/identities/{name}](#apisuser-openshift-iov1identitiesname) Copy linkLink copied to clipboard!

Expand

Table 3.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Identity |

Show more

HTTP method
:   `DELETE`

Description
:   delete an Identity

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Identity

Expand

Table 3.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Identity

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
| 200 - OK | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 201 - Created | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Identity

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
| `body` | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 201 - Created | [`Identity`](#identity-user-openshift-io-v1 "Chapter 3. Identity [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/user.openshift.io/v1/watch/identities/{name}](#apisuser-openshift-iov1watchidentitiesname) Copy linkLink copied to clipboard!

Expand

Table 3.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Identity |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind Identity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. UserIdentityMapping [user.openshift.io/v1]](#useridentitymapping-user-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   UserIdentityMapping maps a user to an identity

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `identity` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | identity is a reference to an identity |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `user` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | user is a reference to a user |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/user.openshift.io/v1/useridentitymappings`

  + `POST`: create an UserIdentityMapping
* `/apis/user.openshift.io/v1/useridentitymappings/{name}`

  + `DELETE`: delete an UserIdentityMapping
  + `GET`: read the specified UserIdentityMapping
  + `PATCH`: partially update the specified UserIdentityMapping
  + `PUT`: replace the specified UserIdentityMapping

#### [4.2.1. /apis/user.openshift.io/v1/useridentitymappings](#apisuser-openshift-iov1useridentitymappings) Copy linkLink copied to clipboard!

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
:   create an UserIdentityMapping

Expand

Table 4.2. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 201 - Created | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 202 - Accepted | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/user.openshift.io/v1/useridentitymappings/{name}](#apisuser-openshift-iov1useridentitymappingsname) Copy linkLink copied to clipboard!

Expand

Table 4.4. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the UserIdentityMapping |

Show more

HTTP method
:   `DELETE`

Description
:   delete an UserIdentityMapping

Expand

Table 4.5. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified UserIdentityMapping

Expand

Table 4.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified UserIdentityMapping

Expand

Table 4.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 201 - Created | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified UserIdentityMapping

Expand

Table 4.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.11. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 201 - Created | [`UserIdentityMapping`](#useridentitymapping-user-openshift-io-v1 "Chapter 4. UserIdentityMapping [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. User [user.openshift.io/v1]](#user-user-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Upon log in, every user of the system receives a User and Identity resource. Administrators may directly manipulate the attributes of the users for their own tracking, or set groups via the API. The user name is unique and is chosen based on the value provided by the identity provider - if a user already exists with the incoming name, the user name may have a number appended to it depending on the configuration of the system.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `groups`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `fullName` | `string` | fullName is the full name of user |
| `groups` | `array (string)` | groups specifies group names this user is a member of. This field is deprecated and will be removed in a future release. Instead, create a Group object containing the name of this User. |
| `identities` | `array (string)` | identities are the identities associated with this user |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/user.openshift.io/v1/users`

  + `DELETE`: delete collection of User
  + `GET`: list or watch objects of kind User
  + `POST`: create an User
* `/apis/user.openshift.io/v1/watch/users`

  + `GET`: watch individual changes to a list of User. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/user.openshift.io/v1/users/{name}`

  + `DELETE`: delete an User
  + `GET`: read the specified User
  + `PATCH`: partially update the specified User
  + `PUT`: replace the specified User
* `/apis/user.openshift.io/v1/watch/users/{name}`

  + `GET`: watch changes to an object of kind User. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [5.2.1. /apis/user.openshift.io/v1/users](#apisuser-openshift-iov1users) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of User

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind User

Expand

Table 5.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-user-v1-UserList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an User

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
| `body` | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 201 - Created | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 202 - Accepted | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/user.openshift.io/v1/watch/users](#apisuser-openshift-iov1watchusers) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of User. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/user.openshift.io/v1/users/{name}](#apisuser-openshift-iov1usersname) Copy linkLink copied to clipboard!

Expand

Table 5.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the User |

Show more

HTTP method
:   `DELETE`

Description
:   delete an User

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified User

Expand

Table 5.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified User

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
| 200 - OK | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 201 - Created | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified User

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
| `body` | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 201 - Created | [`User`](#user-user-openshift-io-v1 "Chapter 5. User [user.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.4. /apis/user.openshift.io/v1/watch/users/{name}](#apisuser-openshift-iov1watchusersname) Copy linkLink copied to clipboard!

Expand

Table 5.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the User |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind User. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm139981907719136) Copy linkLink copied to clipboard!

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
