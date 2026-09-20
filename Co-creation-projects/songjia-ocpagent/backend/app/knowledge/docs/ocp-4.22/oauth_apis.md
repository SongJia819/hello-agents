---
title: "OAuth APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/index
retrieved_at: 2026-09-05T05:42:36.048504+00:00
---

# OAuth APIs

---

OpenShift Container Platform 4.22

## Reference guide for Oauth APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140223514838672)

**Abstract**

This document describes the OpenShift Container Platform Oauth API objects and their detailed specifications.

---

## [Chapter 1. OAuth APIs](#oauth-apis) Copy linkLink copied to clipboard!

### [1.1. OAuthAccessToken [oauth.openshift.io/v1]](#oauthaccesstoken-oauth-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   OAuthAccessToken describes an OAuth access token. The name of a token must be prefixed with a `sha256~` string, must not contain "/" or "%" characters and must be at least 32 characters long.

    The name of the token is constructed from the actual token by sha256-hashing it and using URL-safe unpadded base64-encoding (as described in RFC4648) on the hashed result.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. OAuthAuthorizeToken [oauth.openshift.io/v1]](#oauthauthorizetoken-oauth-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   OAuthAuthorizeToken describes an OAuth authorization token

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. OAuthClientAuthorization [oauth.openshift.io/v1]](#oauthclientauthorization-oauth-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   OAuthClientAuthorization describes an authorization created by an OAuth client

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. OAuthClient [oauth.openshift.io/v1]](#oauthclient-oauth-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   OAuthClient describes an OAuth client

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.5. UserOAuthAccessToken [oauth.openshift.io/v1]](#useroauthaccesstoken-oauth-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   UserOAuthAccessToken is a virtual resource to mirror OAuthAccessTokens to the user the access token was issued for

Type
:   `object`

## [Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]](#oauthaccesstoken-oauth-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   OAuthAccessToken describes an OAuth access token. The name of a token must be prefixed with a `sha256~` string, must not contain "/" or "%" characters and must be at least 32 characters long.

    The name of the token is constructed from the actual token by sha256-hashing it and using URL-safe unpadded base64-encoding (as described in RFC4648) on the hashed result.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `authorizeToken` | `string` | authorizeToken contains the token that authorized this token |
| `clientName` | `string` | clientName references the client that created this token. |
| `expiresIn` | `integer` | expiresIn is the seconds from CreationTime before this token expires. |
| `inactivityTimeoutSeconds` | `integer` | inactivityTimeoutSeconds is the value in seconds, from the CreationTimestamp, after which this token can no longer be used. The value is automatically incremented when the token is used. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `redirectURI` | `string` | redirectURI is the redirection associated with the token. |
| `refreshToken` | `string` | refreshToken is the value by which this token can be renewed. Can be blank. |
| `scopes` | `array (string)` | scopes is an array of the requested scopes. |
| `userName` | `string` | userName is the user name associated with this token |
| `userUID` | `string` | userUID is the unique UID associated with this token |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/oauth.openshift.io/v1/oauthaccesstokens`

  + `DELETE`: delete collection of OAuthAccessToken
  + `GET`: list or watch objects of kind OAuthAccessToken
  + `POST`: create an OAuthAccessToken
* `/apis/oauth.openshift.io/v1/watch/oauthaccesstokens`

  + `GET`: watch individual changes to a list of OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/oauth.openshift.io/v1/oauthaccesstokens/{name}`

  + `DELETE`: delete an OAuthAccessToken
  + `GET`: read the specified OAuthAccessToken
  + `PATCH`: partially update the specified OAuthAccessToken
  + `PUT`: replace the specified OAuthAccessToken
* `/apis/oauth.openshift.io/v1/watch/oauthaccesstokens/{name}`

  + `GET`: watch changes to an object of kind OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [2.2.1. /apis/oauth.openshift.io/v1/oauthaccesstokens](#apisoauth-openshift-iov1oauthaccesstokens) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of OAuthAccessToken

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
:   list or watch objects of kind OAuthAccessToken

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAccessTokenList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-OAuthAccessTokenList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an OAuthAccessToken

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
| `body` | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/oauth.openshift.io/v1/watch/oauthaccesstokens](#apisoauth-openshift-iov1watchoauthaccesstokens) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 2.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/oauth.openshift.io/v1/oauthaccesstokens/{name}](#apisoauth-openshift-iov1oauthaccesstokensname) Copy linkLink copied to clipboard!

Expand

Table 2.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthAccessToken |

Show more

HTTP method
:   `DELETE`

Description
:   delete an OAuthAccessToken

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
| 200 - OK | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified OAuthAccessToken

Expand

Table 2.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified OAuthAccessToken

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
| 200 - OK | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified OAuthAccessToken

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
| `body` | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthAccessToken`](#oauthaccesstoken-oauth-openshift-io-v1 "Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/oauth.openshift.io/v1/watch/oauthaccesstokens/{name}](#apisoauth-openshift-iov1watchoauthaccesstokensname) Copy linkLink copied to clipboard!

Expand

Table 2.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthAccessToken |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind OAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 2.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]](#oauthauthorizetoken-oauth-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   OAuthAuthorizeToken describes an OAuth authorization token

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `clientName` | `string` | clientName references the client that created this token. |
| `codeChallenge` | `string` | codeChallenge is the optional code\_challenge associated with this authorization code, as described in rfc7636 |
| `codeChallengeMethod` | `string` | codeChallengeMethod is the optional code\_challenge\_method associated with this authorization code, as described in rfc7636 |
| `expiresIn` | `integer` | expiresIn is the seconds from CreationTime before this token expires. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `redirectURI` | `string` | redirectURI is the redirection associated with the token. |
| `scopes` | `array (string)` | scopes is an array of the requested scopes. |
| `state` | `string` | state data from request |
| `userName` | `string` | userName is the user name associated with this token |
| `userUID` | `string` | userUID is the unique UID associated with this token. UserUID and UserName must both match for this token to be valid. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/oauth.openshift.io/v1/oauthauthorizetokens`

  + `DELETE`: delete collection of OAuthAuthorizeToken
  + `GET`: list or watch objects of kind OAuthAuthorizeToken
  + `POST`: create an OAuthAuthorizeToken
* `/apis/oauth.openshift.io/v1/watch/oauthauthorizetokens`

  + `GET`: watch individual changes to a list of OAuthAuthorizeToken. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/oauth.openshift.io/v1/oauthauthorizetokens/{name}`

  + `DELETE`: delete an OAuthAuthorizeToken
  + `GET`: read the specified OAuthAuthorizeToken
  + `PATCH`: partially update the specified OAuthAuthorizeToken
  + `PUT`: replace the specified OAuthAuthorizeToken
* `/apis/oauth.openshift.io/v1/watch/oauthauthorizetokens/{name}`

  + `GET`: watch changes to an object of kind OAuthAuthorizeToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [3.2.1. /apis/oauth.openshift.io/v1/oauthauthorizetokens](#apisoauth-openshift-iov1oauthauthorizetokens) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of OAuthAuthorizeToken

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
:   list or watch objects of kind OAuthAuthorizeToken

Expand

Table 3.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAuthorizeTokenList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-OAuthAuthorizeTokenList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an OAuthAuthorizeToken

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
| `body` | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/oauth.openshift.io/v1/watch/oauthauthorizetokens](#apisoauth-openshift-iov1watchoauthauthorizetokens) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of OAuthAuthorizeToken. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/oauth.openshift.io/v1/oauthauthorizetokens/{name}](#apisoauth-openshift-iov1oauthauthorizetokensname) Copy linkLink copied to clipboard!

Expand

Table 3.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthAuthorizeToken |

Show more

HTTP method
:   `DELETE`

Description
:   delete an OAuthAuthorizeToken

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
| 200 - OK | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified OAuthAuthorizeToken

Expand

Table 3.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified OAuthAuthorizeToken

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
| 200 - OK | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified OAuthAuthorizeToken

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
| `body` | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthAuthorizeToken`](#oauthauthorizetoken-oauth-openshift-io-v1 "Chapter 3. OAuthAuthorizeToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/oauth.openshift.io/v1/watch/oauthauthorizetokens/{name}](#apisoauth-openshift-iov1watchoauthauthorizetokensname) Copy linkLink copied to clipboard!

Expand

Table 3.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthAuthorizeToken |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind OAuthAuthorizeToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]](#oauthclientauthorization-oauth-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   OAuthClientAuthorization describes an authorization created by an OAuth client

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `clientName` | `string` | clientName references the client that created this authorization |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `scopes` | `array (string)` | scopes is an array of the granted scopes. |
| `userName` | `string` | userName is the user name that authorized this client |
| `userUID` | `string` | userUID is the unique UID associated with this authorization. UserUID and UserName must both match for this authorization to be valid. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/oauth.openshift.io/v1/oauthclientauthorizations`

  + `DELETE`: delete collection of OAuthClientAuthorization
  + `GET`: list or watch objects of kind OAuthClientAuthorization
  + `POST`: create an OAuthClientAuthorization
* `/apis/oauth.openshift.io/v1/watch/oauthclientauthorizations`

  + `GET`: watch individual changes to a list of OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/oauth.openshift.io/v1/oauthclientauthorizations/{name}`

  + `DELETE`: delete an OAuthClientAuthorization
  + `GET`: read the specified OAuthClientAuthorization
  + `PATCH`: partially update the specified OAuthClientAuthorization
  + `PUT`: replace the specified OAuthClientAuthorization
* `/apis/oauth.openshift.io/v1/watch/oauthclientauthorizations/{name}`

  + `GET`: watch changes to an object of kind OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [4.2.1. /apis/oauth.openshift.io/v1/oauthclientauthorizations](#apisoauth-openshift-iov1oauthclientauthorizations) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of OAuthClientAuthorization

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind OAuthClientAuthorization

Expand

Table 4.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClientAuthorizationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-OAuthClientAuthorizationList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an OAuthClientAuthorization

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
| `body` | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/oauth.openshift.io/v1/watch/oauthclientauthorizations](#apisoauth-openshift-iov1watchoauthclientauthorizations) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/oauth.openshift.io/v1/oauthclientauthorizations/{name}](#apisoauth-openshift-iov1oauthclientauthorizationsname) Copy linkLink copied to clipboard!

Expand

Table 4.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthClientAuthorization |

Show more

HTTP method
:   `DELETE`

Description
:   delete an OAuthClientAuthorization

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified OAuthClientAuthorization

Expand

Table 4.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified OAuthClientAuthorization

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
| 200 - OK | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified OAuthClientAuthorization

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
| `body` | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthClientAuthorization`](#oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.4. /apis/oauth.openshift.io/v1/watch/oauthclientauthorizations/{name}](#apisoauth-openshift-iov1watchoauthclientauthorizationsname) Copy linkLink copied to clipboard!

Expand

Table 4.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthClientAuthorization |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 4.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. OAuthClient [oauth.openshift.io/v1]](#oauthclient-oauth-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   OAuthClient describes an OAuth client

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessTokenInactivityTimeoutSeconds` | `integer` | accessTokenInactivityTimeoutSeconds overrides the default token inactivity timeout for tokens granted to this client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. This value needs to be set only if the default set in configuration is not appropriate for this client. Valid values are: - 0: Tokens for this client never time out - X: Tokens time out if there is no activity for X seconds The current minimum allowed value for X is 300 (5 minutes)  WARNING: existing tokens' timeout will not be affected (lowered) by changing this value |
| `accessTokenMaxAgeSeconds` | `integer` | accessTokenMaxAgeSeconds overrides the default access token max age for tokens granted to this client. 0 means no expiration. |
| `additionalSecrets` | `array (string)` | additionalSecrets holds other secrets that may be used to identify the client. This is useful for rotation and for service account token validation |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `grantMethod` | `string` | grantMethod is a required field which determines how to handle grants for this client. Valid grant handling methods are: - auto: always approves grant requests, useful for trusted clients - prompt: prompts the end user for approval of grant requests, useful for third-party clients |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `redirectURIs` | `array (string)` | redirectURIs is the valid redirection URIs associated with a client |
| `respondWithChallenges` | `boolean` | respondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects |
| `scopeRestrictions` | `array` | scopeRestrictions describes which scopes this client can request. Each requested scope is checked against each restriction. If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied. |
| `scopeRestrictions[]` | `object` | ScopeRestriction describe one restriction on scopes. Exactly one option must be non-nil. |
| `secret` | `string` | secret is the unique secret associated with a client |

Show more

#### [5.1.1. .scopeRestrictions](#scoperestrictions) Copy linkLink copied to clipboard!

Description
:   scopeRestrictions describes which scopes this client can request. Each requested scope is checked against each restriction. If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied.

Type
:   `array`

#### [5.1.2. .scopeRestrictions[]](#scoperestrictions-2) Copy linkLink copied to clipboard!

Description
:   ScopeRestriction describe one restriction on scopes. Exactly one option must be non-nil.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterRole` | `object` | ClusterRoleScopeRestriction describes restrictions on cluster role scopes |
| `literals` | `array (string)` | ExactValues means the scope has to match a particular set of strings exactly |

Show more

#### [5.1.3. .scopeRestrictions[].clusterRole](#scoperestrictions-clusterrole) Copy linkLink copied to clipboard!

Description
:   ClusterRoleScopeRestriction describes restrictions on cluster role scopes

Type
:   `object`

Required
:   * `roleNames`
    * `namespaces`
    * `allowEscalation`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowEscalation` | `boolean` | allowEscalation indicates whether you can request roles and their escalating resources |
| `namespaces` | `array (string)` | namespaces is the list of namespaces that can be referenced. \* means any of them (including \*) |
| `roleNames` | `array (string)` | roleNames is the list of cluster roles that can referenced. \* means anything |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/oauth.openshift.io/v1/oauthclients`

  + `DELETE`: delete collection of OAuthClient
  + `GET`: list or watch objects of kind OAuthClient
  + `POST`: create an OAuthClient
* `/apis/oauth.openshift.io/v1/watch/oauthclients`

  + `GET`: watch individual changes to a list of OAuthClient. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/oauth.openshift.io/v1/oauthclients/{name}`

  + `DELETE`: delete an OAuthClient
  + `GET`: read the specified OAuthClient
  + `PATCH`: partially update the specified OAuthClient
  + `PUT`: replace the specified OAuthClient
* `/apis/oauth.openshift.io/v1/watch/oauthclients/{name}`

  + `GET`: watch changes to an object of kind OAuthClient. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [5.2.1. /apis/oauth.openshift.io/v1/oauthclients](#apisoauth-openshift-iov1oauthclients) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of OAuthClient

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
:   list or watch objects of kind OAuthClient

Expand

Table 5.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClientList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-OAuthClientList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an OAuthClient

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
| `body` | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/oauth.openshift.io/v1/watch/oauthclients](#apisoauth-openshift-iov1watchoauthclients) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of OAuthClient. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/oauth.openshift.io/v1/oauthclients/{name}](#apisoauth-openshift-iov1oauthclientsname) Copy linkLink copied to clipboard!

Expand

Table 5.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthClient |

Show more

HTTP method
:   `DELETE`

Description
:   delete an OAuthClient

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
:   read the specified OAuthClient

Expand

Table 5.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified OAuthClient

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
| 200 - OK | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified OAuthClient

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
| `body` | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 201 - Created | [`OAuthClient`](#oauthclient-oauth-openshift-io-v1 "Chapter 5. OAuthClient [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.4. /apis/oauth.openshift.io/v1/watch/oauthclients/{name}](#apisoauth-openshift-iov1watchoauthclientsname) Copy linkLink copied to clipboard!

Expand

Table 5.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuthClient |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind OAuthClient. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. UserOAuthAccessToken [oauth.openshift.io/v1]](#useroauthaccesstoken-oauth-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   UserOAuthAccessToken is a virtual resource to mirror OAuthAccessTokens to the user the access token was issued for

Type
:   `object`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `authorizeToken` | `string` | authorizeToken contains the token that authorized this token |
| `clientName` | `string` | clientName references the client that created this token. |
| `expiresIn` | `integer` | expiresIn is the seconds from CreationTime before this token expires. |
| `inactivityTimeoutSeconds` | `integer` | inactivityTimeoutSeconds is the value in seconds, from the CreationTimestamp, after which this token can no longer be used. The value is automatically incremented when the token is used. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `redirectURI` | `string` | redirectURI is the redirection associated with the token. |
| `refreshToken` | `string` | refreshToken is the value by which this token can be renewed. Can be blank. |
| `scopes` | `array (string)` | scopes is an array of the requested scopes. |
| `userName` | `string` | userName is the user name associated with this token |
| `userUID` | `string` | userUID is the unique UID associated with this token |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/oauth.openshift.io/v1/useroauthaccesstokens`

  + `GET`: list or watch objects of kind UserOAuthAccessToken
* `/apis/oauth.openshift.io/v1/watch/useroauthaccesstokens`

  + `GET`: watch individual changes to a list of UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/oauth.openshift.io/v1/useroauthaccesstokens/{name}`

  + `DELETE`: delete an UserOAuthAccessToken
  + `GET`: read the specified UserOAuthAccessToken
* `/apis/oauth.openshift.io/v1/watch/useroauthaccesstokens/{name}`

  + `GET`: watch changes to an object of kind UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [6.2.1. /apis/oauth.openshift.io/v1/useroauthaccesstokens](#apisoauth-openshift-iov1useroauthaccesstokens) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind UserOAuthAccessToken

Expand

Table 6.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserOAuthAccessTokenList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-UserOAuthAccessTokenList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /apis/oauth.openshift.io/v1/watch/useroauthaccesstokens](#apisoauth-openshift-iov1watchuseroauthaccesstokens) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.3. /apis/oauth.openshift.io/v1/useroauthaccesstokens/{name}](#apisoauth-openshift-iov1useroauthaccesstokensname) Copy linkLink copied to clipboard!

Expand

Table 6.3. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the UserOAuthAccessToken |

Show more

HTTP method
:   `DELETE`

Description
:   delete an UserOAuthAccessToken

Expand

Table 6.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 6.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified UserOAuthAccessToken

Expand

Table 6.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`UserOAuthAccessToken`](#useroauthaccesstoken-oauth-openshift-io-v1 "Chapter 6. UserOAuthAccessToken [oauth.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.4. /apis/oauth.openshift.io/v1/watch/useroauthaccesstokens/{name}](#apisoauth-openshift-iov1watchuseroauthaccesstokensname) Copy linkLink copied to clipboard!

Expand

Table 6.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the UserOAuthAccessToken |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 6.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140223514838672) Copy linkLink copied to clipboard!

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
