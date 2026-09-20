---
title: "Console APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/index
retrieved_at: 2026-09-05T05:41:43.723225+00:00
---

# Console APIs

---

OpenShift Container Platform 4.22

## Reference guide for console APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140555431531280)

**Abstract**

This document describes the OpenShift Container Platform console API objects and their detailed specifications.

---

## [Chapter 1. Console APIs](#console-apis) Copy linkLink copied to clipboard!

### [1.1. ConsoleCLIDownload [console.openshift.io/v1]](#consoleclidownload-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleCLIDownload is an extension for configuring openshift web console command line interface (CLI) downloads.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. ConsoleExternalLogLink [console.openshift.io/v1]](#consoleexternalloglink-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleExternalLogLink is an extension for customizing OpenShift web console log links.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. ConsoleLink [console.openshift.io/v1]](#consolelink-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleLink is an extension for customizing OpenShift web console links.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. ConsoleNotification [console.openshift.io/v1]](#consolenotification-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleNotification is the extension for configuring openshift web console notifications.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.5. ConsolePlugin [console.openshift.io/v1]](#consoleplugin-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsolePlugin is an extension for customizing OpenShift web console by dynamically loading code from another service running on the cluster.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.6. ConsoleQuickStart [console.openshift.io/v1]](#consolequickstart-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleQuickStart is an extension for guiding user through various workflows in the OpenShift web console.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.7. ConsoleSample [console.openshift.io/v1]](#consolesample-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleSample is an extension to customizing OpenShift web console by adding samples.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.8. ConsoleYAMLSample [console.openshift.io/v1]](#consoleyamlsample-console-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ConsoleYAMLSample is an extension for customizing OpenShift web console YAML samples.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

## [Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]](#consoleclidownload-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleCLIDownload is an extension for configuring openshift web console command line interface (CLI) downloads.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConsoleCLIDownloadSpec is the desired cli download configuration. |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   ConsoleCLIDownloadSpec is the desired cli download configuration.

Type
:   `object`

Required
:   * `description`
    * `displayName`
    * `links`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `description` | `string` | description is the description of the CLI download (can include markdown). |
| `displayName` | `string` | displayName is the display name of the CLI download. |
| `links` | `array` | links is a list of objects that provide CLI download link details. |
| `links[]` | `object` |  |

Show more

#### [2.1.2. .spec.links](#spec-links) Copy linkLink copied to clipboard!

Description
:   links is a list of objects that provide CLI download link details.

Type
:   `array`

#### [2.1.3. .spec.links[]](#spec-links-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `href`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `href` | `string` | href is the absolute secure URL for the link (must use https) |
| `text` | `string` | text is the display text for the link |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consoleclidownloads`

  + `DELETE`: delete collection of ConsoleCLIDownload
  + `GET`: list objects of kind ConsoleCLIDownload
  + `POST`: create a ConsoleCLIDownload
* `/apis/console.openshift.io/v1/consoleclidownloads/{name}`

  + `DELETE`: delete a ConsoleCLIDownload
  + `GET`: read the specified ConsoleCLIDownload
  + `PATCH`: partially update the specified ConsoleCLIDownload
  + `PUT`: replace the specified ConsoleCLIDownload
* `/apis/console.openshift.io/v1/consoleclidownloads/{name}/status`

  + `GET`: read status of the specified ConsoleCLIDownload
  + `PATCH`: partially update status of the specified ConsoleCLIDownload
  + `PUT`: replace status of the specified ConsoleCLIDownload

#### [2.2.1. /apis/console.openshift.io/v1/consoleclidownloads](#apisconsole-openshift-iov1consoleclidownloads) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleCLIDownload

Expand

Table 2.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsoleCLIDownload

Expand

Table 2.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownloadList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleCLIDownloadList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleCLIDownload

Expand

Table 2.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/console.openshift.io/v1/consoleclidownloads/{name}](#apisconsole-openshift-iov1consoleclidownloadsname) Copy linkLink copied to clipboard!

Expand

Table 2.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleCLIDownload |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleCLIDownload

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
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleCLIDownload

Expand

Table 2.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleCLIDownload

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
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleCLIDownload

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
| `body` | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/console.openshift.io/v1/consoleclidownloads/{name}/status](#apisconsole-openshift-iov1consoleclidownloadsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 2.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleCLIDownload |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ConsoleCLIDownload

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ConsoleCLIDownload

Expand

Table 2.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ConsoleCLIDownload

Expand

Table 2.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleCLIDownload`](#consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]](#consoleexternalloglink-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleExternalLogLink is an extension for customizing OpenShift web console log links.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page. |

Show more

#### [3.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page.

Type
:   `object`

Required
:   * `hrefTemplate`
    * `text`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hrefTemplate` | `string` | hrefTemplate is an absolute secure URL (must use https) for the log link including variables to be replaced. Variables are specified in the URL with the format ${variableName}, for instance, ${containerName} and will be replaced with the corresponding values from the resource. Resource is a pod. Supported variables are: - ${resourceName} - name of the resource which containes the logs - ${resourceUID} - UID of the resource which contains the logs - e.g. `11111111-2222-3333-4444-555555555555` - ${containerName} - name of the resource’s container that contains the logs - ${resourceNamespace} - namespace of the resource that contains the logs - ${resourceNamespaceUID} - namespace UID of the resource that contains the logs - ${podLabels} - JSON representation of labels matching the pod with the logs - e.g. `{"key1":"value1","key2":"value2"}`  e.g., <https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}> |
| `namespaceFilter` | `string` | namespaceFilter is a regular expression used to restrict a log link to a matching set of namespaces (e.g., `^openshift-`). The string is converted into a regular expression using the JavaScript RegExp constructor. If not specified, links will be displayed for all the namespaces. |
| `text` | `string` | text is the display text for the link |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consoleexternalloglinks`

  + `DELETE`: delete collection of ConsoleExternalLogLink
  + `GET`: list objects of kind ConsoleExternalLogLink
  + `POST`: create a ConsoleExternalLogLink
* `/apis/console.openshift.io/v1/consoleexternalloglinks/{name}`

  + `DELETE`: delete a ConsoleExternalLogLink
  + `GET`: read the specified ConsoleExternalLogLink
  + `PATCH`: partially update the specified ConsoleExternalLogLink
  + `PUT`: replace the specified ConsoleExternalLogLink
* `/apis/console.openshift.io/v1/consoleexternalloglinks/{name}/status`

  + `GET`: read status of the specified ConsoleExternalLogLink
  + `PATCH`: partially update status of the specified ConsoleExternalLogLink
  + `PUT`: replace status of the specified ConsoleExternalLogLink

#### [3.2.1. /apis/console.openshift.io/v1/consoleexternalloglinks](#apisconsole-openshift-iov1consoleexternalloglinks) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleExternalLogLink

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
:   list objects of kind ConsoleExternalLogLink

Expand

Table 3.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLinkList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleExternalLogLinkList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleExternalLogLink

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
| `body` | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/console.openshift.io/v1/consoleexternalloglinks/{name}](#apisconsole-openshift-iov1consoleexternalloglinksname) Copy linkLink copied to clipboard!

Expand

Table 3.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleExternalLogLink |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleExternalLogLink

Expand

Table 3.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 3.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleExternalLogLink

Expand

Table 3.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleExternalLogLink

Expand

Table 3.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleExternalLogLink

Expand

Table 3.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/console.openshift.io/v1/consoleexternalloglinks/{name}/status](#apisconsole-openshift-iov1consoleexternalloglinksnamestatus) Copy linkLink copied to clipboard!

Expand

Table 3.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleExternalLogLink |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ConsoleExternalLogLink

Expand

Table 3.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ConsoleExternalLogLink

Expand

Table 3.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ConsoleExternalLogLink

Expand

Table 3.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleExternalLogLink`](#consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. ConsoleLink [console.openshift.io/v1]](#consolelink-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleLink is an extension for customizing OpenShift web console links.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConsoleLinkSpec is the desired console link configuration. |

Show more

#### [4.1.1. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   ConsoleLinkSpec is the desired console link configuration.

Type
:   `object`

Required
:   * `href`
    * `location`
    * `text`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `applicationMenu` | `object` | applicationMenu holds information about section and icon used for the link in the application menu, and it is applicable only when location is set to ApplicationMenu. |
| `href` | `string` | href is the absolute URL for the link. Must use https:// for web URLs or mailto: for email links. |
| `location` | `string` | location determines which location in the console the link will be appended to (ApplicationMenu, HelpMenu, UserMenu, NamespaceDashboard). |
| `namespaceDashboard` | `object` | namespaceDashboard holds information about namespaces in which the dashboard link should appear, and it is applicable only when location is set to NamespaceDashboard. If not specified, the link will appear in all namespaces. |
| `text` | `string` | text is the display text for the link |

Show more

#### [4.1.2. .spec.applicationMenu](#spec-applicationmenu) Copy linkLink copied to clipboard!

Description
:   applicationMenu holds information about section and icon used for the link in the application menu, and it is applicable only when location is set to ApplicationMenu.

Type
:   `object`

Required
:   * `section`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `imageURL` | `string` | imageURL is the URL for the icon used in front of the link in the application menu. The URL must be an HTTPS URL or a Data URI. The image should be square and will be shown at 24x24 pixels. |
| `section` | `string` | section is the section of the application menu in which the link should appear. This can be any text that will appear as a subheading in the application menu dropdown. A new section will be created if the text does not match text of an existing section. |

Show more

#### [4.1.3. .spec.namespaceDashboard](#spec-namespacedashboard) Copy linkLink copied to clipboard!

Description
:   namespaceDashboard holds information about namespaces in which the dashboard link should appear, and it is applicable only when location is set to NamespaceDashboard. If not specified, the link will appear in all namespaces.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `namespaceSelector` | `object` | namespaceSelector is used to select the Namespaces that should contain dashboard link by label. If the namespace labels match, dashboard link will be shown for the namespaces. |
| `namespaces` | `array (string)` | namespaces is an array of namespace names in which the dashboard link should appear. |

Show more

#### [4.1.4. .spec.namespaceDashboard.namespaceSelector](#spec-namespacedashboard-namespaceselector) Copy linkLink copied to clipboard!

Description
:   namespaceSelector is used to select the Namespaces that should contain dashboard link by label. If the namespace labels match, dashboard link will be shown for the namespaces.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

Show more

#### [4.1.5. .spec.namespaceDashboard.namespaceSelector.matchExpressions](#spec-namespacedashboard-namespaceselector-matchexpressions) Copy linkLink copied to clipboard!

Description
:   matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
:   `array`

#### [4.1.6. .spec.namespaceDashboard.namespaceSelector.matchExpressions[]](#spec-namespacedashboard-namespaceselector-matchexpressions-2) Copy linkLink copied to clipboard!

Description
:   A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consolelinks`

  + `DELETE`: delete collection of ConsoleLink
  + `GET`: list objects of kind ConsoleLink
  + `POST`: create a ConsoleLink
* `/apis/console.openshift.io/v1/consolelinks/{name}`

  + `DELETE`: delete a ConsoleLink
  + `GET`: read the specified ConsoleLink
  + `PATCH`: partially update the specified ConsoleLink
  + `PUT`: replace the specified ConsoleLink
* `/apis/console.openshift.io/v1/consolelinks/{name}/status`

  + `GET`: read status of the specified ConsoleLink
  + `PATCH`: partially update status of the specified ConsoleLink
  + `PUT`: replace status of the specified ConsoleLink

#### [4.2.1. /apis/console.openshift.io/v1/consolelinks](#apisconsole-openshift-iov1consolelinks) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleLink

Expand

Table 4.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsoleLink

Expand

Table 4.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLinkList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleLinkList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleLink

Expand

Table 4.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/console.openshift.io/v1/consolelinks/{name}](#apisconsole-openshift-iov1consolelinksname) Copy linkLink copied to clipboard!

Expand

Table 4.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleLink |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleLink

Expand

Table 4.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 4.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleLink

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleLink

Expand

Table 4.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleLink

Expand

Table 4.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/console.openshift.io/v1/consolelinks/{name}/status](#apisconsole-openshift-iov1consolelinksnamestatus) Copy linkLink copied to clipboard!

Expand

Table 4.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleLink |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ConsoleLink

Expand

Table 4.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ConsoleLink

Expand

Table 4.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ConsoleLink

Expand

Table 4.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleLink`](#consolelink-console-openshift-io-v1 "Chapter 4. ConsoleLink [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. ConsoleNotification [console.openshift.io/v1]](#consolenotification-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleNotification is the extension for configuring openshift web console notifications.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConsoleNotificationSpec is the desired console notification configuration. |

Show more

#### [5.1.1. .spec](#spec-4) Copy linkLink copied to clipboard!

Description
:   ConsoleNotificationSpec is the desired console notification configuration.

Type
:   `object`

Required
:   * `text`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `backgroundColor` | `string` | backgroundColor is the color of the background for the notification as CSS data type color. |
| `color` | `string` | color is the color of the text for the notification as CSS data type color. |
| `link` | `object` | link is an object that holds notification link details. |
| `location` | `string` | location is the location of the notification in the console. Valid values are: "BannerTop", "BannerBottom", "BannerTopBottom". |
| `text` | `string` | text is the visible text of the notification. |

Show more

#### [5.1.2. .spec.link](#spec-link) Copy linkLink copied to clipboard!

Description
:   link is an object that holds notification link details.

Type
:   `object`

Required
:   * `href`
    * `text`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `href` | `string` | href is the absolute URL for the link. Must use https:// for web URLs or mailto: for email links. |
| `text` | `string` | text is the display text for the link |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consolenotifications`

  + `DELETE`: delete collection of ConsoleNotification
  + `GET`: list objects of kind ConsoleNotification
  + `POST`: create a ConsoleNotification
* `/apis/console.openshift.io/v1/consolenotifications/{name}`

  + `DELETE`: delete a ConsoleNotification
  + `GET`: read the specified ConsoleNotification
  + `PATCH`: partially update the specified ConsoleNotification
  + `PUT`: replace the specified ConsoleNotification
* `/apis/console.openshift.io/v1/consolenotifications/{name}/status`

  + `GET`: read status of the specified ConsoleNotification
  + `PATCH`: partially update status of the specified ConsoleNotification
  + `PUT`: replace status of the specified ConsoleNotification

#### [5.2.1. /apis/console.openshift.io/v1/consolenotifications](#apisconsole-openshift-iov1consolenotifications) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleNotification

Expand

Table 5.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsoleNotification

Expand

Table 5.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotificationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleNotificationList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleNotification

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
| `body` | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/console.openshift.io/v1/consolenotifications/{name}](#apisconsole-openshift-iov1consolenotificationsname) Copy linkLink copied to clipboard!

Expand

Table 5.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleNotification |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleNotification

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
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleNotification

Expand

Table 5.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleNotification

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
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleNotification

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
| `body` | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/console.openshift.io/v1/consolenotifications/{name}/status](#apisconsole-openshift-iov1consolenotificationsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 5.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleNotification |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ConsoleNotification

Expand

Table 5.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ConsoleNotification

Expand

Table 5.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ConsoleNotification

Expand

Table 5.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleNotification`](#consolenotification-console-openshift-io-v1 "Chapter 5. ConsoleNotification [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. ConsolePlugin [console.openshift.io/v1]](#consoleplugin-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsolePlugin is an extension for customizing OpenShift web console by dynamically loading code from another service running on the cluster.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `metadata`
    * `spec`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec contains the desired configuration for the console plugin. |

Show more

#### [6.1.1. .spec](#spec-5) Copy linkLink copied to clipboard!

Description
:   spec contains the desired configuration for the console plugin.

Type
:   `object`

Required
:   * `backend`
    * `displayName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `backend` | `object` | backend holds the configuration of backend which is serving console’s plugin . |
| `contentSecurityPolicy` | `array` | contentSecurityPolicy is a list of Content-Security-Policy (CSP) directives for the plugin. Each directive specifies a list of values, appropriate for the given directive type, for example a list of remote endpoints for fetch directives such as ScriptSrc. Console web application uses CSP to detect and mitigate certain types of attacks, such as cross-site scripting (XSS) and data injection attacks. Dynamic plugins should specify this field if need to load assets from outside the cluster or if violation reports are observed. Dynamic plugins should always prefer loading their assets from within the cluster, either by vendoring them, or fetching from a cluster service. CSP violation reports can be viewed in the browser’s console logs during development and testing of the plugin in the OpenShift web console. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. Each of the available directives may be defined only once in the list. The value 'self' is automatically included in all fetch directives by the OpenShift web console’s backend. For more information about the CSP directives, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>  The OpenShift web console server aggregates the CSP directives and values across its own default values and all enabled ConsolePlugin CRs, merging them into a single policy string that is sent to the browser via `Content-Security-Policy` HTTP response header.  Example: ConsolePlugin A directives: script-src: <https://script1.com/>, <https://script2.com/> font-src: <https://font1.com/>  ConsolePlugin B directives: script-src: <https://script2.com/>, <https://script3.com/> font-src: <https://font2.com/> img-src: <https://img1.com/>  Unified set of CSP directives, passed to the OpenShift web console server: script-src: <https://script1.com/>, <https://script2.com/>, <https://script3.com/> font-src: <https://font1.com/>, <https://font2.com/> img-src: <https://img1.com/>  OpenShift web console server CSP response header: Content-Security-Policy: default-src 'self'; base-uri 'self'; script-src 'self' <https://script1.com/> <https://script2.com/> <https://script3.com/>; font-src 'self' <https://font1.com/> <https://font2.com/>; img-src 'self' <https://img1.com/>; style-src 'self'; frame-src 'none'; object-src 'none' |
| `contentSecurityPolicy[]` | `object` | ConsolePluginCSP holds configuration for a specific CSP directive |
| `displayName` | `string` | displayName is the display name of the plugin. The dispalyName should be between 1 and 128 characters. |
| `i18n` | `object` | i18n is the configuration of plugin’s localization resources. |
| `proxy` | `array` | proxy is a list of proxies that describe various service type to which the plugin needs to connect to. |
| `proxy[]` | `object` | ConsolePluginProxy holds information on various service types to which console’s backend will proxy the plugin’s requests. |

Show more

#### [6.1.2. .spec.backend](#spec-backend) Copy linkLink copied to clipboard!

Description
:   backend holds the configuration of backend which is serving console’s plugin .

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `service` | `object` | service is a Kubernetes Service that exposes the plugin using a deployment with an HTTP server. The Service must use HTTPS and Service serving certificate. The console backend will proxy the plugins assets from the Service using the service CA bundle. |
| `type` | `string` | type is the backend type which servers the console’s plugin. Currently only "Service" is supported. |

Show more

#### [6.1.3. .spec.backend.service](#spec-backend-service) Copy linkLink copied to clipboard!

Description
:   service is a Kubernetes Service that exposes the plugin using a deployment with an HTTP server. The Service must use HTTPS and Service serving certificate. The console backend will proxy the plugins assets from the Service using the service CA bundle.

Type
:   `object`

Required
:   * `name`
    * `namespace`
    * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `basePath` | `string` | basePath is the path to the plugin’s assets. The primary asset it the manifest file called `plugin-manifest.json`, which is a JSON document that contains metadata about the plugin and the extensions. |
| `name` | `string` | name of Service that is serving the plugin assets. |
| `namespace` | `string` | namespace of Service that is serving the plugin assets. |
| `port` | `integer` | port on which the Service that is serving the plugin is listening to. |

Show more

#### [6.1.4. .spec.contentSecurityPolicy](#spec-contentsecuritypolicy) Copy linkLink copied to clipboard!

Description
:   contentSecurityPolicy is a list of Content-Security-Policy (CSP) directives for the plugin. Each directive specifies a list of values, appropriate for the given directive type, for example a list of remote endpoints for fetch directives such as ScriptSrc. Console web application uses CSP to detect and mitigate certain types of attacks, such as cross-site scripting (XSS) and data injection attacks. Dynamic plugins should specify this field if need to load assets from outside the cluster or if violation reports are observed. Dynamic plugins should always prefer loading their assets from within the cluster, either by vendoring them, or fetching from a cluster service. CSP violation reports can be viewed in the browser’s console logs during development and testing of the plugin in the OpenShift web console. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. Each of the available directives may be defined only once in the list. The value 'self' is automatically included in all fetch directives by the OpenShift web console’s backend. For more information about the CSP directives, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy>

    The OpenShift web console server aggregates the CSP directives and values across its own default values and all enabled ConsolePlugin CRs, merging them into a single policy string that is sent to the browser via `Content-Security-Policy` HTTP response header.

    Example: ConsolePlugin A directives: script-src: <https://script1.com/>, <https://script2.com/> font-src: <https://font1.com/>

    ```
    ConsolePlugin B directives:
      script-src: https://script2.com/, https://script3.com/
      font-src: https://font2.com/
      img-src: https://img1.com/
    ```

    ```
    Unified set of CSP directives, passed to the OpenShift web console server:
      script-src: https://script1.com/, https://script2.com/, https://script3.com/
      font-src: https://font1.com/, https://font2.com/
      img-src: https://img1.com/
    ```

    ```
    OpenShift web console server CSP response header:
      Content-Security-Policy: default-src 'self'; base-uri 'self'; script-src 'self' https://script1.com/ https://script2.com/ https://script3.com/; font-src 'self' https://font1.com/ https://font2.com/; img-src 'self' https://img1.com/; style-src 'self'; frame-src 'none'; object-src 'none'
    ```

Type
:   `array`

#### [6.1.5. .spec.contentSecurityPolicy[]](#spec-contentsecuritypolicy-2) Copy linkLink copied to clipboard!

Description
:   ConsolePluginCSP holds configuration for a specific CSP directive

Type
:   `object`

Required
:   * `directive`
    * `values`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `directive` | `string` | directive specifies which Content-Security-Policy directive to configure. Available directive types are DefaultSrc, ScriptSrc, StyleSrc, ImgSrc, FontSrc and ConnectSrc. DefaultSrc directive serves as a fallback for the other CSP fetch directives. For more information about the DefaultSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/default-src> ScriptSrc directive specifies valid sources for JavaScript. For more information about the ScriptSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src> StyleSrc directive specifies valid sources for stylesheets. For more information about the StyleSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/style-src> ImgSrc directive specifies a valid sources of images and favicons. For more information about the ImgSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/img-src> FontSrc directive specifies valid sources for fonts loaded using @font-face. For more information about the FontSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/font-src> ConnectSrc directive restricts the URLs which can be loaded using script interfaces. For more information about the ConnectSrc directive, see: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src> |
| `values` | `array (string)` | values defines an array of values to append to the console defaults for this directive. Each ConsolePlugin may define their own directives with their values. These will be set by the OpenShift web console’s backend, as part of its Content-Security-Policy header. The array can contain at most 16 values. Each directive value must have a maximum length of 1024 characters and must not contain whitespace, commas (,), semicolons (;) or single quotes ('). The value '\*' is not permitted. Each value in the array must be unique. |

Show more

#### [6.1.6. .spec.i18n](#spec-i18n) Copy linkLink copied to clipboard!

Description
:   i18n is the configuration of plugin’s localization resources.

Type
:   `object`

Required
:   * `loadType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `loadType` | `string` | loadType indicates how the plugin’s localization resource should be loaded. Valid values are Preload, Lazy and the empty string. When set to Preload, all localization resources are fetched when the plugin is loaded. When set to Lazy, localization resources are lazily loaded as and when they are required by the console. When omitted or set to the empty string, the behaviour is equivalent to Lazy type. |

Show more

#### [6.1.7. .spec.proxy](#spec-proxy) Copy linkLink copied to clipboard!

Description
:   proxy is a list of proxies that describe various service type to which the plugin needs to connect to.

Type
:   `array`

#### [6.1.8. .spec.proxy[]](#spec-proxy-2) Copy linkLink copied to clipboard!

Description
:   ConsolePluginProxy holds information on various service types to which console’s backend will proxy the plugin’s requests.

Type
:   `object`

Required
:   * `alias`
    * `endpoint`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `alias` | `string` | alias is a proxy name that identifies the plugin’s proxy. An alias name should be unique per plugin. The console backend exposes following proxy endpoint:  /api/proxy/plugin/<plugin-name>/<proxy-alias>/<request-path>?<optional-query-parameters>  Request example path:  /api/proxy/plugin/acm/search/pods?namespace=openshift-apiserver |
| `authorization` | `string` | authorization provides information about authorization type, which the proxied request should contain |
| `caCertificate` | `string` | caCertificate provides the cert authority certificate contents, in case the proxied Service is using custom service CA. By default, the service CA bundle provided by the service-ca operator is used. |
| `endpoint` | `object` | endpoint provides information about endpoint to which the request is proxied to. |

Show more

#### [6.1.9. .spec.proxy[].endpoint](#spec-proxy-endpoint) Copy linkLink copied to clipboard!

Description
:   endpoint provides information about endpoint to which the request is proxied to.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `service` | `object` | service is an in-cluster Service that the plugin will connect to. The Service must use HTTPS. The console backend exposes an endpoint in order to proxy communication between the plugin and the Service. Note: service field is required for now, since currently only "Service" type is supported. |
| `type` | `string` | type is the type of the console plugin’s proxy. Currently only "Service" is supported. |

Show more

#### [6.1.10. .spec.proxy[].endpoint.service](#spec-proxy-endpoint-service) Copy linkLink copied to clipboard!

Description
:   service is an in-cluster Service that the plugin will connect to. The Service must use HTTPS. The console backend exposes an endpoint in order to proxy communication between the plugin and the Service. Note: service field is required for now, since currently only "Service" type is supported.

Type
:   `object`

Required
:   * `name`
    * `namespace`
    * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of Service that the plugin needs to connect to. |
| `namespace` | `string` | namespace of Service that the plugin needs to connect to |
| `port` | `integer` | port on which the Service that the plugin needs to connect to is listening on. |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consoleplugins`

  + `DELETE`: delete collection of ConsolePlugin
  + `GET`: list objects of kind ConsolePlugin
  + `POST`: create a ConsolePlugin
* `/apis/console.openshift.io/v1/consoleplugins/{name}`

  + `DELETE`: delete a ConsolePlugin
  + `GET`: read the specified ConsolePlugin
  + `PATCH`: partially update the specified ConsolePlugin
  + `PUT`: replace the specified ConsolePlugin

#### [6.2.1. /apis/console.openshift.io/v1/consoleplugins](#apisconsole-openshift-iov1consoleplugins) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsolePlugin

Expand

Table 6.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsolePlugin

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsolePluginList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsolePluginList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsolePlugin

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
| `body` | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /apis/console.openshift.io/v1/consoleplugins/{name}](#apisconsole-openshift-iov1consolepluginsname) Copy linkLink copied to clipboard!

Expand

Table 6.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsolePlugin |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsolePlugin

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
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsolePlugin

Expand

Table 6.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsolePlugin

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
| 200 - OK | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsolePlugin

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
| `body` | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsolePlugin`](#consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 7. ConsoleQuickStart [console.openshift.io/v1]](#consolequickstart-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleQuickStart is an extension for guiding user through various workflows in the OpenShift web console.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConsoleQuickStartSpec is the desired quick start configuration. |

Show more

#### [7.1.1. .spec](#spec-6) Copy linkLink copied to clipboard!

Description
:   ConsoleQuickStartSpec is the desired quick start configuration.

Type
:   `object`

Required
:   * `description`
    * `displayName`
    * `durationMinutes`
    * `introduction`
    * `tasks`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessReviewResources` | `array` | accessReviewResources contains a list of resources that the user’s access will be reviewed against in order for the user to complete the Quick Start. The Quick Start will be hidden if any of the access reviews fail. |
| `accessReviewResources[]` | `object` | ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface |
| `conclusion` | `string` | conclusion sums up the Quick Start and suggests the possible next steps. (includes markdown) |
| `description` | `string` | description is the description of the Quick Start. (includes markdown) |
| `displayName` | `string` | displayName is the display name of the Quick Start. |
| `durationMinutes` | `integer` | durationMinutes describes approximately how many minutes it will take to complete the Quick Start. |
| `icon` | `string` | icon is a base64 encoded image that will be displayed beside the Quick Start display name. The icon should be an vector image for easy scaling. The size of the icon should be 40x40. |
| `introduction` | `string` | introduction describes the purpose of the Quick Start. (includes markdown) |
| `nextQuickStart` | `array (string)` | nextQuickStart is a list of the following Quick Starts, suggested for the user to try. |
| `prerequisites` | `array (string)` | prerequisites contains all prerequisites that need to be met before taking a Quick Start. (includes markdown) |
| `tags` | `array (string)` | tags is a list of strings that describe the Quick Start. |
| `tasks` | `array` | tasks is the list of steps the user has to perform to complete the Quick Start. |
| `tasks[]` | `object` | ConsoleQuickStartTask is a single step in a Quick Start. |

Show more

#### [7.1.2. .spec.accessReviewResources](#spec-accessreviewresources) Copy linkLink copied to clipboard!

Description
:   accessReviewResources contains a list of resources that the user’s access will be reviewed against in order for the user to complete the Quick Start. The Quick Start will be hidden if any of the access reviews fail.

Type
:   `array`

#### [7.1.3. .spec.accessReviewResources[]](#spec-accessreviewresources-2) Copy linkLink copied to clipboard!

Description
:   ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldSelector` | `object` | fieldSelector describes the limitation on access based on field. It can only limit access, not broaden it. |
| `group` | `string` | Group is the API Group of the Resource. "\*" means all. |
| `labelSelector` | `object` | labelSelector describes the limitation on access based on labels. It can only limit access, not broaden it. |
| `name` | `string` | Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. |
| `namespace` | `string` | Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview |
| `resource` | `string` | Resource is one of the existing resource types. "\*" means all. |
| `subresource` | `string` | Subresource is one of the existing resource types. "" means none. |
| `verb` | `string` | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "\*" means all. |
| `version` | `string` | Version is the API Version of the Resource. "\*" means all. |

Show more

#### [7.1.4. .spec.accessReviewResources[].fieldSelector](#spec-accessreviewresources-fieldselector) Copy linkLink copied to clipboard!

Description
:   fieldSelector describes the limitation on access based on field. It can only limit access, not broaden it.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | `array` | requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |
| `requirements[]` | `object` | FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values. |

Show more

#### [7.1.5. .spec.accessReviewResources[].fieldSelector.requirements](#spec-accessreviewresources-fieldselector-requirements) Copy linkLink copied to clipboard!

Description
:   requirements is the parsed interpretation of a field selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.

Type
:   `array`

#### [7.1.6. .spec.accessReviewResources[].fieldSelector.requirements[]](#spec-accessreviewresources-fieldselector-requirements-2) Copy linkLink copied to clipboard!

Description
:   FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the field selector key that the requirement applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. |

Show more

#### [7.1.7. .spec.accessReviewResources[].labelSelector](#spec-accessreviewresources-labelselector) Copy linkLink copied to clipboard!

Description
:   labelSelector describes the limitation on access based on labels. It can only limit access, not broaden it.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rawSelector` | `string` | rawSelector is the serialization of a field selector that would be included in a query parameter. Webhook implementations are encouraged to ignore rawSelector. The kube-apiserver’s \*SubjectAccessReview will parse the rawSelector as long as the requirements are not present. |
| `requirements` | `array` | requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood. |
| `requirements[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

Show more

#### [7.1.8. .spec.accessReviewResources[].labelSelector.requirements](#spec-accessreviewresources-labelselector-requirements) Copy linkLink copied to clipboard!

Description
:   requirements is the parsed interpretation of a label selector. All requirements must be met for a resource instance to match the selector. Webhook implementations should handle requirements, but how to handle them is up to the webhook. Since requirements can only limit the request, it is safe to authorize as unlimited request if the requirements are not understood.

Type
:   `array`

#### [7.1.9. .spec.accessReviewResources[].labelSelector.requirements[]](#spec-accessreviewresources-labelselector-requirements-2) Copy linkLink copied to clipboard!

Description
:   A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

Show more

#### [7.1.10. .spec.tasks](#spec-tasks) Copy linkLink copied to clipboard!

Description
:   tasks is the list of steps the user has to perform to complete the Quick Start.

Type
:   `array`

#### [7.1.11. .spec.tasks[]](#spec-tasks-2) Copy linkLink copied to clipboard!

Description
:   ConsoleQuickStartTask is a single step in a Quick Start.

Type
:   `object`

Required
:   * `description`
    * `title`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `description` | `string` | description describes the steps needed to complete the task. (includes markdown) |
| `review` | `object` | review contains instructions to validate the task is complete. The user will select 'Yes' or 'No'. using a radio button, which indicates whether the step was completed successfully. |
| `summary` | `object` | summary contains information about the passed step. |
| `title` | `string` | title describes the task and is displayed as a step heading. |

Show more

#### [7.1.12. .spec.tasks[].review](#spec-tasks-review) Copy linkLink copied to clipboard!

Description
:   review contains instructions to validate the task is complete. The user will select 'Yes' or 'No'. using a radio button, which indicates whether the step was completed successfully.

Type
:   `object`

Required
:   * `failedTaskHelp`
    * `instructions`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `failedTaskHelp` | `string` | failedTaskHelp contains suggestions for a failed task review and is shown at the end of task. (includes markdown) |
| `instructions` | `string` | instructions contains steps that user needs to take in order to validate his work after going through a task. (includes markdown) |

Show more

#### [7.1.13. .spec.tasks[].summary](#spec-tasks-summary) Copy linkLink copied to clipboard!

Description
:   summary contains information about the passed step.

Type
:   `object`

Required
:   * `failed`
    * `success`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `failed` | `string` | failed briefly describes the unsuccessfully passed task. (includes markdown) |
| `success` | `string` | success describes the succesfully passed task. |

Show more

### [7.2. API endpoints](#api-endpoints-6) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consolequickstarts`

  + `DELETE`: delete collection of ConsoleQuickStart
  + `GET`: list objects of kind ConsoleQuickStart
  + `POST`: create a ConsoleQuickStart
* `/apis/console.openshift.io/v1/consolequickstarts/{name}`

  + `DELETE`: delete a ConsoleQuickStart
  + `GET`: read the specified ConsoleQuickStart
  + `PATCH`: partially update the specified ConsoleQuickStart
  + `PUT`: replace the specified ConsoleQuickStart

#### [7.2.1. /apis/console.openshift.io/v1/consolequickstarts](#apisconsole-openshift-iov1consolequickstarts) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleQuickStart

Expand

Table 7.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsoleQuickStart

Expand

Table 7.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleQuickStartList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleQuickStartList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleQuickStart

Expand

Table 7.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 7.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.2. /apis/console.openshift.io/v1/consolequickstarts/{name}](#apisconsole-openshift-iov1consolequickstartsname) Copy linkLink copied to clipboard!

Expand

Table 7.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleQuickStart |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleQuickStart

Expand

Table 7.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 7.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleQuickStart

Expand

Table 7.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleQuickStart

Expand

Table 7.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleQuickStart

Expand

Table 7.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 7.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleQuickStart`](#consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 8. ConsoleSample [console.openshift.io/v1]](#consolesample-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleSample is an extension to customizing OpenShift web console by adding samples.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `metadata`
    * `spec`

### [8.1. Specification](#specification-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec contains configuration for a console sample. |

Show more

#### [8.1.1. .spec](#spec-7) Copy linkLink copied to clipboard!

Description
:   spec contains configuration for a console sample.

Type
:   `object`

Required
:   * `abstract`
    * `description`
    * `source`
    * `title`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `abstract` | `string` | abstract is a short introduction to the sample.  It is required and must be no more than 100 characters in length.  The abstract is shown on the sample card tile below the title and provider and is limited to three lines of content. |
| `description` | `string` | description is a long form explanation of the sample.  It is required and can have a maximum length of **4096** characters.  It is a README.md-like content for additional information, links, pre-conditions, and other instructions. It will be rendered as Markdown so that it can contain line breaks, links, and other simple formatting. |
| `icon` | `string` | icon is an optional base64 encoded image and shown beside the sample title.  The format must follow the data: URL format and can have a maximum size of **10 KB**.  data:[<mediatype>][;base64],<base64 encoded image>  For example:  data:image;base64, plus the base64 encoded image.  Vector images can also be used. SVG icons must start with:  data:image/svg+xml;base64, plus the base64 encoded SVG image.  All sample catalog icons will be shown on a white background (also when the dark theme is used). The web console ensures that different aspect ratios work correctly. Currently, the surface of the icon is at most 40x100px.  For more information on the data URL format, please visit <https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs>. |
| `provider` | `string` | provider is an optional label to honor who provides the sample.  It is optional and must be no more than 50 characters in length.  A provider can be a company like "Red Hat" or an organization like "CNCF" or "Knative".  Currently, the provider is only shown on the sample card tile below the title with the prefix "Provided by " |
| `source` | `object` | source defines where to deploy the sample service from. The sample may be sourced from an external git repository or container image. |
| `tags` | `array (string)` | tags are optional string values that can be used to find samples in the samples catalog.  Examples of common tags may be "Java", "Quarkus", etc.  They will be displayed on the samples details page. |
| `title` | `string` | title is the display name of the sample.  It is required and must be no more than 50 characters in length. |
| `type` | `string` | type is an optional label to group multiple samples.  It is optional and must be no more than 20 characters in length.  Recommendation is a singular term like "Builder Image", "Devfile" or "Serverless Function".  Currently, the type is shown a badge on the sample card tile in the top right corner. |

Show more

#### [8.1.2. .spec.source](#spec-source) Copy linkLink copied to clipboard!

Description
:   source defines where to deploy the sample service from. The sample may be sourced from an external git repository or container image.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerImport` | `object` | containerImport allows the user import a container image. |
| `gitImport` | `object` | gitImport allows the user to import code from a git repository. |
| `type` | `string` | type of the sample, currently supported: "GitImport";"ContainerImport" |

Show more

#### [8.1.3. .spec.source.containerImport](#spec-source-containerimport) Copy linkLink copied to clipboard!

Description
:   containerImport allows the user import a container image.

Type
:   `object`

Required
:   * `image`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `image` | `string` | reference to a container image that provides a HTTP service. The service must be exposed on the default port (8080) unless otherwise configured with the port field.  Supported formats: - <repository-name>/<image-name> - docker.io/<repository-name>/<image-name> - quay.io/<repository-name>/<image-name> - quay.io/<repository-name>/<image-name>@sha256:<image hash> - quay.io/<repository-name>/<image-name>:<tag> |
| `service` | `object` | service contains configuration for the Service resource created for this sample. |

Show more

#### [8.1.4. .spec.source.containerImport.service](#spec-source-containerimport-service) Copy linkLink copied to clipboard!

Description
:   service contains configuration for the Service resource created for this sample.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `targetPort` | `integer` | targetPort is the port that the service listens on for HTTP requests. This port will be used for Service and Route created for this sample. Port must be in the range 1 to 65535. Default port is 8080. |

Show more

#### [8.1.5. .spec.source.gitImport](#spec-source-gitimport) Copy linkLink copied to clipboard!

Description
:   gitImport allows the user to import code from a git repository.

Type
:   `object`

Required
:   * `repository`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `repository` | `object` | repository contains the reference to the actual Git repository. |
| `service` | `object` | service contains configuration for the Service resource created for this sample. |

Show more

#### [8.1.6. .spec.source.gitImport.repository](#spec-source-gitimport-repository) Copy linkLink copied to clipboard!

Description
:   repository contains the reference to the actual Git repository.

Type
:   `object`

Required
:   * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `contextDir` | `string` | contextDir is used to specify a directory within the repository to build the component. Must start with `/` and have a maximum length of 256 characters. When omitted, the default value is to build from the root of the repository. |
| `revision` | `string` | revision is the git revision at which to clone the git repository Can be used to clone a specific branch, tag or commit SHA. Must be at most 256 characters in length. When omitted the repository’s default branch is used. |
| `url` | `string` | url of the Git repository that contains a HTTP service. The HTTP service must be exposed on the default port (8080) unless otherwise configured with the port field.  Only public repositories on GitHub, GitLab and Bitbucket are currently supported:  - <https://github.com/<org>/<repository>> - <https://gitlab.com/<org>/<repository>> - <https://bitbucket.org/<org>/<repository>>  The url must have a maximum length of 256 characters. |

Show more

#### [8.1.7. .spec.source.gitImport.service](#spec-source-gitimport-service) Copy linkLink copied to clipboard!

Description
:   service contains configuration for the Service resource created for this sample.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `targetPort` | `integer` | targetPort is the port that the service listens on for HTTP requests. This port will be used for Service created for this sample. Port must be in the range 1 to 65535. Default port is 8080. |

Show more

### [8.2. API endpoints](#api-endpoints-7) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consolesamples`

  + `DELETE`: delete collection of ConsoleSample
  + `GET`: list objects of kind ConsoleSample
  + `POST`: create a ConsoleSample
* `/apis/console.openshift.io/v1/consolesamples/{name}`

  + `DELETE`: delete a ConsoleSample
  + `GET`: read the specified ConsoleSample
  + `PATCH`: partially update the specified ConsoleSample
  + `PUT`: replace the specified ConsoleSample

#### [8.2.1. /apis/console.openshift.io/v1/consolesamples](#apisconsole-openshift-iov1consolesamples) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleSample

Expand

Table 8.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsoleSample

Expand

Table 8.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleSampleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleSampleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleSample

Expand

Table 8.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 8.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.2. /apis/console.openshift.io/v1/consolesamples/{name}](#apisconsole-openshift-iov1consolesamplesname) Copy linkLink copied to clipboard!

Expand

Table 8.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleSample |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleSample

Expand

Table 8.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 8.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleSample

Expand

Table 8.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleSample

Expand

Table 8.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleSample

Expand

Table 8.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 8.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleSample`](#consolesample-console-openshift-io-v1 "Chapter 8. ConsoleSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]](#consoleyamlsample-console-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ConsoleYAMLSample is an extension for customizing OpenShift web console YAML samples.

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `metadata`
    * `spec`

### [9.1. Specification](#specification-8) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console. |

Show more

#### [9.1.1. .spec](#spec-8) Copy linkLink copied to clipboard!

Description
:   ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console.

Type
:   `object`

Required
:   * `description`
    * `targetResource`
    * `title`
    * `yaml`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `description` | `string` | description of the YAML sample. |
| `snippet` | `boolean` | snippet indicates that the YAML sample is not the full YAML resource definition, but a fragment that can be inserted into the existing YAML document at the user’s cursor. |
| `targetResource` | `object` | targetResource contains apiVersion and kind of the resource YAML sample is representating. |
| `title` | `string` | title of the YAML sample. |
| `yaml` | `string` | yaml is the YAML sample to display. |

Show more

#### [9.1.2. .spec.targetResource](#spec-targetresource) Copy linkLink copied to clipboard!

Description
:   targetResource contains apiVersion and kind of the resource YAML sample is representating.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [9.2. API endpoints](#api-endpoints-8) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/console.openshift.io/v1/consoleyamlsamples`

  + `DELETE`: delete collection of ConsoleYAMLSample
  + `GET`: list objects of kind ConsoleYAMLSample
  + `POST`: create a ConsoleYAMLSample
* `/apis/console.openshift.io/v1/consoleyamlsamples/{name}`

  + `DELETE`: delete a ConsoleYAMLSample
  + `GET`: read the specified ConsoleYAMLSample
  + `PATCH`: partially update the specified ConsoleYAMLSample
  + `PUT`: replace the specified ConsoleYAMLSample

#### [9.2.1. /apis/console.openshift.io/v1/consoleyamlsamples](#apisconsole-openshift-iov1consoleyamlsamples) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ConsoleYAMLSample

Expand

Table 9.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ConsoleYAMLSample

Expand

Table 9.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleYAMLSampleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleYAMLSampleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ConsoleYAMLSample

Expand

Table 9.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 9.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 202 - Accepted | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.2. /apis/console.openshift.io/v1/consoleyamlsamples/{name}](#apisconsole-openshift-iov1consoleyamlsamplesname) Copy linkLink copied to clipboard!

Expand

Table 9.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ConsoleYAMLSample |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ConsoleYAMLSample

Expand

Table 9.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 9.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ConsoleYAMLSample

Expand

Table 9.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ConsoleYAMLSample

Expand

Table 9.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ConsoleYAMLSample

Expand

Table 9.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |  |

Show more

Expand

Table 9.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 201 - Created | [`ConsoleYAMLSample`](#consoleyamlsample-console-openshift-io-v1 "Chapter 9. ConsoleYAMLSample [console.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140555431531280) Copy linkLink copied to clipboard!

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
