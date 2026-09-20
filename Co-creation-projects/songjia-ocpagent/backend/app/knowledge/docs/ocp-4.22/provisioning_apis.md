---
title: "Provisioning APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/index
retrieved_at: 2026-09-05T05:42:46.732235+00:00
---

# Provisioning APIs

---

OpenShift Container Platform 4.22

## Reference guide for provisioning APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139703733052944)

**Abstract**

This document describes the OpenShift Container Platform provisioning API objects and their detailed specifications.

---

## [Chapter 1. Provisioning APIs](#provisioning-apis) Copy linkLink copied to clipboard!

### [1.1. BMCEventSubscription [metal3.io/v1alpha1]](#bmceventsubscription-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   BMCEventSubscription is the Schema for the fast eventing API

Type
:   `object`

### [1.2. BareMetalHost [metal3.io/v1alpha1]](#baremetalhost-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   BareMetalHost is the Schema for the baremetalhosts API

Type
:   `object`

### [1.3. DataImage [metal3.io/v1alpha1]](#dataimage-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   DataImage is the Schema for the dataimages API.

Type
:   `object`

### [1.4. FirmwareSchema [metal3.io/v1alpha1]](#firmwareschema-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   FirmwareSchema is the Schema for the firmwareschemas API.

Type
:   `object`

### [1.5. HardwareData [metal3.io/v1alpha1]](#hardwaredata-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   HardwareData is the Schema for the hardwaredata API.

Type
:   `object`

### [1.6. HostFirmwareComponents [metal3.io/v1alpha1]](#hostfirmwarecomponents-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   HostFirmwareComponents is the Schema for the hostfirmwarecomponents API.

Type
:   `object`

### [1.7. HostFirmwareSettings [metal3.io/v1alpha1]](#hostfirmwaresettings-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   HostFirmwareSettings is the Schema for the hostfirmwaresettings API.

Type
:   `object`

### [1.8. HostUpdatePolicy [metal3.io/v1alpha1]](#hostupdatepolicy-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   HostUpdatePolicy is the Schema for the hostupdatepolicy API.

Type
:   `object`

### [1.9. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]](#metal3remediation-infrastructure-cluster-x-k8s-iov1beta1) Copy linkLink copied to clipboard!

Description
:   Metal3Remediation is the Schema for the metal3remediations API.

Type
:   `object`

### [1.10. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]](#metal3remediationtemplate-infrastructure-cluster-x-k8s-iov1beta1) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationTemplate is the Schema for the metal3remediationtemplates API.

Type
:   `object`

### [1.11. PreprovisioningImage [metal3.io/v1alpha1]](#preprovisioningimage-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   PreprovisioningImage is the Schema for the preprovisioningimages API.

Type
:   `object`

### [1.12. Provisioning [metal3.io/v1alpha1]](#provisioning-metal3-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   Provisioning contains configuration used by the Provisioning service (Ironic) to provision baremetal hosts. Provisioning is created by the OpenShift installer using admin or user provided information about the provisioning network and the NIC on the server that can be used to PXE boot it. This CR is a singleton, created by the installer and currently only consumed by the cluster-baremetal-operator to bring up and update containers in a metal3 cluster.

Type
:   `object`

## [Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]](#bmceventsubscription-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   BMCEventSubscription is the Schema for the fast eventing API

Type
:   `object`

### [2.1. Specification](#specification) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` |  |
| `status` | `object` |  |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `context` | `string` | Arbitrary user-provided context for the event |
| `destination` | `string` | A webhook URL to send events to |
| `hostName` | `string` | A reference to a BareMetalHost |
| `httpHeadersRef` | `object` | A secret containing HTTP headers which should be passed along to the Destination when making a request |

Show more

#### [2.1.2. .spec.httpHeadersRef](#spec-httpheadersref) Copy linkLink copied to clipboard!

Description
:   A secret containing HTTP headers which should be passed along to the Destination when making a request

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

Show more

#### [2.1.3. .status](#status) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `error` | `string` |  |
| `subscriptionID` | `string` |  |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/bmceventsubscriptions`

  + `GET`: list objects of kind BMCEventSubscription
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions`

  + `DELETE`: delete collection of BMCEventSubscription
  + `GET`: list objects of kind BMCEventSubscription
  + `POST`: create a BMCEventSubscription
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}`

  + `DELETE`: delete a BMCEventSubscription
  + `GET`: read the specified BMCEventSubscription
  + `PATCH`: partially update the specified BMCEventSubscription
  + `PUT`: replace the specified BMCEventSubscription
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}/status`

  + `GET`: read status of the specified BMCEventSubscription
  + `PATCH`: partially update status of the specified BMCEventSubscription
  + `PUT`: replace status of the specified BMCEventSubscription

#### [2.2.1. /apis/metal3.io/v1alpha1/bmceventsubscriptions](#apismetal3-iov1alpha1bmceventsubscriptions) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind BMCEventSubscription

Expand

Table 2.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscriptionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-BMCEventSubscriptionList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions](#apismetal3-iov1alpha1namespacesnamespacebmceventsubscriptions) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of BMCEventSubscription

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
:   list objects of kind BMCEventSubscription

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscriptionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-BMCEventSubscriptionList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a BMCEventSubscription

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
| `body` | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 2.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 201 - Created | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}](#apismetal3-iov1alpha1namespacesnamespacebmceventsubscriptionsname) Copy linkLink copied to clipboard!

Expand

Table 2.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the BMCEventSubscription |

Show more

HTTP method
:   `DELETE`

Description
:   delete a BMCEventSubscription

Expand

Table 2.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 2.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified BMCEventSubscription

Expand

Table 2.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified BMCEventSubscription

Expand

Table 2.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified BMCEventSubscription

Expand

Table 2.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 2.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 201 - Created | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}/status](#apismetal3-iov1alpha1namespacesnamespacebmceventsubscriptionsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 2.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the BMCEventSubscription |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified BMCEventSubscription

Expand

Table 2.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified BMCEventSubscription

Expand

Table 2.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified BMCEventSubscription

Expand

Table 2.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 2.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 2.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 201 - Created | [`BMCEventSubscription`](#bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. BareMetalHost [metal3.io/v1alpha1]](#baremetalhost-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   BareMetalHost is the Schema for the baremetalhosts API

Type
:   `object`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | BareMetalHostSpec defines the desired state of BareMetalHost. |
| `status` | `object` | BareMetalHostStatus defines the observed state of BareMetalHost. |

Show more

#### [3.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   BareMetalHostSpec defines the desired state of BareMetalHost.

Type
:   `object`

Required
:   * `online`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `architecture` | `string` | CPU architecture of the host, e.g. "x86\_64" or "aarch64". If unset, eventually populated by inspection. |
| `automatedCleaningMode` | `string` | When set to disabled, automated cleaning will be skipped during provisioning and deprovisioning. |
| `bmc` | `object` | How do we connect to the BMC (Baseboard Management Controller) on the host? |
| `bootMACAddress` | `string` | The MAC address of the NIC used for provisioning the host. In case of network boot, this is the MAC address of the PXE booting interface. The MAC address of the BMC must never be used here! |
| `bootMode` | `string` | Select the method of initializing the hardware during boot. Defaults to UEFI. Legacy boot should only be used for hardware that does not support UEFI correctly. Set to UEFISecureBoot to turn secure boot on automatically after provisioning. |
| `consumerRef` | `object` | ConsumerRef can be used to store information about something that is using a host. When it is not empty, the host is considered "in use". The common use case is a link to a Machine resource when the host is used by Cluster API. |
| `customDeploy` | `object` | A custom deploy procedure. This is an advanced feature that allows using a custom deploy step provided by a site-specific deployment ramdisk. Most users will want to use "image" instead. Setting this field triggers provisioning. |
| `description` | `string` | Description is a human-entered text used to help identify the host. |
| `disablePowerOff` | `boolean` | When set to true, power off of the node will be disabled, instead, a reboot will be used in place of power on/off |
| `externallyProvisioned` | `boolean` | ExternallyProvisioned means something else has provisioned the image running on the host, and the operator should only manage the power status. This field is used for integration with already provisioned hosts and when pivoting hosts between clusters.  This field can be set to true either: 1. During initial host creation (e.g., for pre-provisioned hosts) 2. After inspection completes when the host reaches Available state  When used in environments with Cluster API Provider Metal3 (CAPM3), ensure hosts are labeled appropriately so CAPM3’s host selector can distinguish them from CAPM3-managed hosts. If unsure, leave this field as false. |
| `firmware` | `object` | Firmware (BIOS) configuration for bare metal server. If set, the requested settings will be applied before the host is provisioned.  Deprecated: no longer supported by any driver. An alternative is to use HostFirmwareSettings resources that allow changing arbitrary values and support the generic Redfish-based drivers. |
| `hardwareProfile` | `string` | What is the name of the hardware profile for this host? Hardware profiles are deprecated and should not be used. Use the separate fields Architecture and RootDeviceHints instead. Set to "empty" to prepare for the future version of the API without hardware profiles. |
| `image` | `object` | Image holds the details of the image to be provisioned. Populating the image will cause the host to start provisioning. |
| `inspectionMode` | `string` | Specifies the mode for host inspection. "disabled" - no inspection will be performed "agent" - normal agent-based inspection will run |
| `metaData` | `object` | MetaData holds the reference to the Secret containing host metadata which is passed to the Config Drive. By default, metadata will be generated for the host, so most users do not need to set this field. |
| `networkData` | `object` | NetworkData holds the reference to the Secret containing network configuration which is passed to the Config Drive and interpreted by the first boot software such as cloud-init. |
| `online` | `boolean` | Should the host be powered on? If the host is currently in a stable state (e.g. provisioned), its power state will be forced to match this value. |
| `preprovisioningNetworkDataName` | `string` | PreprovisioningNetworkDataName is the name of the Secret in the local namespace containing network configuration which is passed to the preprovisioning image, and to the Config Drive if not overridden by specifying NetworkData. |
| `raid` | `object` | RAID configuration for bare metal server. If set, the RAID settings will be applied before the host is provisioned. If not, the current settings will not be modified. Only one of the sub-fields hardwareRAIDVolumes and softwareRAIDVolumes can be set at the same time. |
| `rootDeviceHints` | `object` | Provide guidance about how to choose the device for the image being provisioned. The default is currently to use /dev/sda as the root device. |
| `taints` | `array` | Taints is the full, authoritative list of taints to apply to the corresponding Machine. This list will overwrite any modifications made to the Machine on an ongoing basis. |
| `taints[]` | `object` | The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint. |
| `userData` | `object` | UserData holds the reference to the Secret containing the user data which is passed to the Config Drive and interpreted by the first-boot software such as cloud-init. The format of user data is specific to the first-boot software. |

Show more

#### [3.1.2. .spec.bmc](#spec-bmc) Copy linkLink copied to clipboard!

Description
:   How do we connect to the BMC (Baseboard Management Controller) on the host?

Type
:   `object`

Required
:   * `address`
    * `credentialsName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `address` | `string` | Address holds the URL for accessing the controller on the network. The scheme part designates the driver to use with the host. |
| `credentialsName` | `string` | The name of the secret containing the BMC credentials (requires keys "username" and "password"). |
| `disableCertificateVerification` | `boolean` | DisableCertificateVerification disables verification of server certificates when using HTTPS to connect to the BMC. This is required when the server certificate is self-signed, but is insecure because it allows a man-in-the-middle to intercept the connection. |

Show more

#### [3.1.3. .spec.consumerRef](#spec-consumerref) Copy linkLink copied to clipboard!

Description
:   ConsumerRef can be used to store information about something that is using a host. When it is not empty, the host is considered "in use". The common use case is a link to a Machine resource when the host is used by Cluster API.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

Show more

#### [3.1.4. .spec.customDeploy](#spec-customdeploy) Copy linkLink copied to clipboard!

Description
:   A custom deploy procedure. This is an advanced feature that allows using a custom deploy step provided by a site-specific deployment ramdisk. Most users will want to use "image" instead. Setting this field triggers provisioning.

Type
:   `object`

Required
:   * `method`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `method` | `string` | Custom deploy method name. This name is specific to the deploy ramdisk used. If you don’t have a custom deploy ramdisk, you shouldn’t use CustomDeploy. |

Show more

#### [3.1.5. .spec.firmware](#spec-firmware) Copy linkLink copied to clipboard!

Description
:   Firmware (BIOS) configuration for bare metal server. If set, the requested settings will be applied before the host is provisioned.

    Deprecated: no longer supported by any driver. An alternative is to use HostFirmwareSettings resources that allow changing arbitrary values and support the generic Redfish-based drivers.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `simultaneousMultithreadingEnabled` | `boolean` | Allows a single physical processor core to appear as several logical processors. |
| `sriovEnabled` | `boolean` | SR-IOV support enables a hypervisor to create virtual instances of a PCI-express device, potentially increasing performance. |
| `virtualizationEnabled` | `boolean` | Supports the virtualization of platform hardware. |

Show more

#### [3.1.6. .spec.image](#spec-image) Copy linkLink copied to clipboard!

Description
:   Image holds the details of the image to be provisioned. Populating the image will cause the host to start provisioning.

Type
:   `object`

Required
:   * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `checksum` | `string` | Checksum is the checksum for the image. Required for all formats except for "live-iso" and OCI images (oci://). |
| `checksumType` | `string` | ChecksumType is the checksum algorithm for the image, e.g md5, sha256 or sha512. The special value "auto" can be used to detect the algorithm from the checksum. If missing, MD5 is used. If in doubt, use "auto". |
| `format` | `string` | Format contains the format of the image (raw, qcow2, …​). When set to "live-iso", an ISO 9660 image referenced by the url will be live-booted and not deployed to disk. |
| `url` | `string` | URL is a location of an image to deploy. |

Show more

#### [3.1.7. .spec.metaData](#spec-metadata) Copy linkLink copied to clipboard!

Description
:   MetaData holds the reference to the Secret containing host metadata which is passed to the Config Drive. By default, metadata will be generated for the host, so most users do not need to set this field.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

Show more

#### [3.1.8. .spec.networkData](#spec-networkdata) Copy linkLink copied to clipboard!

Description
:   NetworkData holds the reference to the Secret containing network configuration which is passed to the Config Drive and interpreted by the first boot software such as cloud-init.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

Show more

#### [3.1.9. .spec.raid](#spec-raid) Copy linkLink copied to clipboard!

Description
:   RAID configuration for bare metal server. If set, the RAID settings will be applied before the host is provisioned. If not, the current settings will not be modified. Only one of the sub-fields hardwareRAIDVolumes and softwareRAIDVolumes can be set at the same time.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hardwareRAIDVolumes` | `` | The list of logical disks for hardware RAID, if rootDeviceHints isn’t used, first volume is root volume. You can set the value of this field to `[]` to clear all the hardware RAID configurations. |
| `softwareRAIDVolumes` | `` | The list of logical disks for software RAID, if rootDeviceHints isn’t used, first volume is root volume. If HardwareRAIDVolumes is set this item will be invalid. The number of created Software RAID devices must be 1 or 2. If there is only one Software RAID device, it has to be a RAID-1. If there are two, the first one has to be a RAID-1, while the RAID level for the second one can be 0, 1, or 1+0. As the first RAID device will be the deployment device, enforcing a RAID-1 reduces the risk of ending up with a non-booting host in case of a disk failure. Software RAID will always be deleted. |

Show more

#### [3.1.10. .spec.rootDeviceHints](#spec-rootdevicehints) Copy linkLink copied to clipboard!

Description
:   Provide guidance about how to choose the device for the image being provisioned. The default is currently to use /dev/sda as the root device.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `deviceName` | `string` | A Linux device name like "/dev/vda", or a by-path link to it like "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0". The hint must match the actual value exactly. |
| `hctl` | `string` | A SCSI bus address like 0:0:0:0. The hint must match the actual value exactly. |
| `minSizeGigabytes` | `integer` | The minimum size of the device in Gigabytes. |
| `model` | `string` | A vendor-specific device identifier. The hint can be a substring of the actual value. |
| `rotational` | `boolean` | True if the device should use spinning media, false otherwise. |
| `serialNumber` | `string` | Device serial number. The hint must match the actual value exactly. |
| `vendor` | `string` | The name of the vendor or manufacturer of the device. The hint can be a substring of the actual value. |
| `wwn` | `string` | Unique storage identifier. The hint must match the actual value exactly. |
| `wwnVendorExtension` | `string` | Unique vendor storage identifier. The hint must match the actual value exactly. |
| `wwnWithExtension` | `string` | Unique storage identifier with the vendor extension appended. The hint must match the actual value exactly. |

Show more

#### [3.1.11. .spec.taints](#spec-taints) Copy linkLink copied to clipboard!

Description
:   Taints is the full, authoritative list of taints to apply to the corresponding Machine. This list will overwrite any modifications made to the Machine on an ongoing basis.

Type
:   `array`

#### [3.1.12. .spec.taints[]](#spec-taints-2) Copy linkLink copied to clipboard!

Description
:   The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.

Type
:   `object`

Required
:   * `effect`
    * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Required. The taint key to be applied to a node. |
| `timeAdded` | `string` | TimeAdded represents the time at which the taint was added. |
| `value` | `string` | The taint value corresponding to the taint key. |

Show more

#### [3.1.13. .spec.userData](#spec-userdata) Copy linkLink copied to clipboard!

Description
:   UserData holds the reference to the Secret containing the user data which is passed to the Config Drive and interpreted by the first-boot software such as cloud-init. The format of user data is specific to the first-boot software.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

Show more

#### [3.1.14. .status](#status-2) Copy linkLink copied to clipboard!

Description
:   BareMetalHostStatus defines the observed state of BareMetalHost.

Type
:   `object`

Required
:   * `errorCount`
    * `errorMessage`
    * `operationalStatus`
    * `poweredOn`
    * `provisioning`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | Conditions defines current service state of the BareMetalHost. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `errorCount` | `integer` | ErrorCount records how many times the host has encoutered an error since the last successful operation |
| `errorMessage` | `string` | The last error message reported by the provisioning subsystem. |
| `errorType` | `string` | ErrorType indicates the type of failure encountered when the OperationalStatus is OperationalStatusError |
| `goodCredentials` | `object` | The last credentials we were able to validate as working. |
| `hardware` | `object` | The hardware discovered to exist on the host. This field will be removed in the next API version in favour of the separate HardwareData resource. |
| `hardwareProfile` | `string` | The name of the profile matching the hardware details. Hardware profiles are deprecated and should not be relied on. |
| `lastUpdated` | `string` | LastUpdated identifies when this status was last observed. |
| `operationHistory` | `object` | OperationHistory holds information about operations performed on this host. |
| `operationalStatus` | `string` | OperationalStatus holds the status of the host |
| `poweredOn` | `boolean` | The currently detected power state of the host. This field may get briefly out of sync with the actual state of the hardware while provisioning processes are running. |
| `provisioning` | `object` | Information tracked by the provisioner. |
| `triedCredentials` | `object` | The last credentials we sent to the provisioning backend. |

Show more

#### [3.1.15. .status.conditions](#status-conditions) Copy linkLink copied to clipboard!

Description
:   Conditions defines current service state of the BareMetalHost.

Type
:   `array`

#### [3.1.16. .status.conditions[]](#status-conditions-2) Copy linkLink copied to clipboard!

Description
:   Condition contains details for one aspect of the current state of this API Resource.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `message`
    * `reason`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

Show more

#### [3.1.17. .status.goodCredentials](#status-goodcredentials) Copy linkLink copied to clipboard!

Description
:   The last credentials we were able to validate as working.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `credentials` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `credentialsVersion` | `string` |  |

Show more

#### [3.1.18. .status.goodCredentials.credentials](#status-goodcredentials-credentials) Copy linkLink copied to clipboard!

Description
:   SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

Show more

#### [3.1.19. .status.hardware](#status-hardware) Copy linkLink copied to clipboard!

Description
:   The hardware discovered to exist on the host. This field will be removed in the next API version in favour of the separate HardwareData resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cpu` | `object` | Details of the CPU(s) in the system. |
| `firmware` | `object` | System firmware information. |
| `hostname` | `string` | Name of the host at the inspection time. |
| `nics` | `array` | List of network interfaces for the host. |
| `nics[]` | `object` | NIC describes one network interface on the host. |
| `ramMebibytes` | `integer` | The host’s amount of memory in Mebibytes. |
| `storage` | `array` | List of storage (disk, SSD, etc.) available to the host. |
| `storage[]` | `object` | Storage describes one storage device (disk, SSD, etc.) on the host. |
| `systemVendor` | `object` | System vendor information. |

Show more

#### [3.1.20. .status.hardware.cpu](#status-hardware-cpu) Copy linkLink copied to clipboard!

Description
:   Details of the CPU(s) in the system.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `arch` | `string` |  |
| `clockMegahertz` | `number` | ClockSpeed is a clock speed in MHz |
| `count` | `integer` |  |
| `flags` | `array (string)` |  |
| `model` | `string` |  |

Show more

#### [3.1.21. .status.hardware.firmware](#status-hardware-firmware) Copy linkLink copied to clipboard!

Description
:   System firmware information.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `bios` | `object` | The BIOS for this firmware |

Show more

#### [3.1.22. .status.hardware.firmware.bios](#status-hardware-firmware-bios) Copy linkLink copied to clipboard!

Description
:   The BIOS for this firmware

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `date` | `string` | The release/build date for this BIOS |
| `vendor` | `string` | The vendor name for this BIOS |
| `version` | `string` | The version of the BIOS |

Show more

#### [3.1.23. .status.hardware.nics](#status-hardware-nics) Copy linkLink copied to clipboard!

Description
:   List of network interfaces for the host.

Type
:   `array`

#### [3.1.24. .status.hardware.nics[]](#status-hardware-nics-2) Copy linkLink copied to clipboard!

Description
:   NIC describes one network interface on the host.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ip` | `string` | The IP address of the interface. This will be an IPv4 or IPv6 address if one is present. If both IPv4 and IPv6 addresses are present in a dual-stack environment, two nics will be output, one with each IP. |
| `lldp` | `object` | LLDP data for this interface |
| `mac` | `string` | The device MAC address |
| `model` | `string` | The vendor and product IDs of the NIC, e.g. "0x8086 0x1572" |
| `name` | `string` | The name of the network interface, e.g. "en0" |
| `pciAddress` | `string` | The NIC PCI address |
| `pxe` | `boolean` | Whether the NIC is PXE Bootable |
| `speedGbps` | `integer` | The speed of the device in Gigabits per second |
| `vlanId` | `integer` | The untagged VLAN ID |
| `vlans` | `array` | The VLANs available |
| `vlans[]` | `object` | VLAN represents the name and ID of a VLAN. |

Show more

#### [3.1.25. .status.hardware.nics[].lldp](#status-hardware-nics-lldp) Copy linkLink copied to clipboard!

Description
:   LLDP data for this interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `portID` | `string` | The switch port ID from LLDP |
| `switchID` | `string` | The switch chassis ID from LLDP |
| `switchSystemName` | `string` | The switch system name from LLDP |

Show more

#### [3.1.26. .status.hardware.nics[].vlans](#status-hardware-nics-vlans) Copy linkLink copied to clipboard!

Description
:   The VLANs available

Type
:   `array`

#### [3.1.27. .status.hardware.nics[].vlans[]](#status-hardware-nics-vlans-2) Copy linkLink copied to clipboard!

Description
:   VLAN represents the name and ID of a VLAN.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `id` | `integer` | VLANID is a 12-bit 802.1Q VLAN identifier |
| `name` | `string` |  |

Show more

#### [3.1.28. .status.hardware.storage](#status-hardware-storage) Copy linkLink copied to clipboard!

Description
:   List of storage (disk, SSD, etc.) available to the host.

Type
:   `array`

#### [3.1.29. .status.hardware.storage[]](#status-hardware-storage-2) Copy linkLink copied to clipboard!

Description
:   Storage describes one storage device (disk, SSD, etc.) on the host.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `alternateNames` | `array (string)` | A list of alternate Linux device names of the disk, e.g. "/dev/sda". Note that this list is not exhaustive, and names may not be stable across reboots. |
| `hctl` | `string` | The SCSI location of the device |
| `model` | `string` | Hardware model |
| `name` | `string` | A Linux device name of the disk, e.g. "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0". This will be a name that is stable across reboots if one is available. |
| `rotational` | `boolean` | Whether this disk represents rotational storage. This field is not recommended for usage, please prefer using 'Type' field instead, this field will be deprecated eventually. |
| `serialNumber` | `string` | The serial number of the device |
| `sizeBytes` | `integer` | The size of the disk in Bytes |
| `type` | `string` | Device type, one of: HDD, SSD, NVME. |
| `vendor` | `string` | The name of the vendor of the device |
| `wwn` | `string` | The WWN of the device |
| `wwnVendorExtension` | `string` | The WWN Vendor extension of the device |
| `wwnWithExtension` | `string` | The WWN with the extension |

Show more

#### [3.1.30. .status.hardware.systemVendor](#status-hardware-systemvendor) Copy linkLink copied to clipboard!

Description
:   System vendor information.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `manufacturer` | `string` |  |
| `productName` | `string` |  |
| `serialNumber` | `string` |  |

Show more

#### [3.1.31. .status.operationHistory](#status-operationhistory) Copy linkLink copied to clipboard!

Description
:   OperationHistory holds information about operations performed on this host.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `deprovision` | `object` | OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics. |
| `inspect` | `object` | OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics. |
| `provision` | `object` | OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics. |
| `register` | `object` | OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics. |

Show more

#### [3.1.32. .status.operationHistory.deprovision](#status-operationhistory-deprovision) Copy linkLink copied to clipboard!

Description
:   OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `end` | `` |  |
| `start` | `` |  |

Show more

#### [3.1.33. .status.operationHistory.inspect](#status-operationhistory-inspect) Copy linkLink copied to clipboard!

Description
:   OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `end` | `` |  |
| `start` | `` |  |

Show more

#### [3.1.34. .status.operationHistory.provision](#status-operationhistory-provision) Copy linkLink copied to clipboard!

Description
:   OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `end` | `` |  |
| `start` | `` |  |

Show more

#### [3.1.35. .status.operationHistory.register](#status-operationhistory-register) Copy linkLink copied to clipboard!

Description
:   OperationMetric contains metadata about an operation (inspection, provisioning, etc.) used for tracking metrics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `end` | `` |  |
| `start` | `` |  |

Show more

#### [3.1.36. .status.provisioning](#status-provisioning) Copy linkLink copied to clipboard!

Description
:   Information tracked by the provisioner.

Type
:   `object`

Required
:   * `ID`
    * `state`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ID` | `string` | The hosts’s ID from the underlying provisioning tool (e.g. the Ironic node UUID). |
| `bootMode` | `string` | BootMode indicates the boot mode used to provision the host. |
| `customDeploy` | `object` | Custom deploy procedure applied to the host. |
| `firmware` | `object` | The firmware settings that have been applied. |
| `image` | `object` | Image holds the details of the last image successfully provisioned to the host. |
| `raid` | `object` | The RAID configuration that has been applied. |
| `rootDeviceHints` | `object` | The root device hints used to provision the host. |
| `state` | `string` | An indicator for what the provisioner is doing with the host. |

Show more

#### [3.1.37. .status.provisioning.customDeploy](#status-provisioning-customdeploy) Copy linkLink copied to clipboard!

Description
:   Custom deploy procedure applied to the host.

Type
:   `object`

Required
:   * `method`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `method` | `string` | Custom deploy method name. This name is specific to the deploy ramdisk used. If you don’t have a custom deploy ramdisk, you shouldn’t use CustomDeploy. |

Show more

#### [3.1.38. .status.provisioning.firmware](#status-provisioning-firmware) Copy linkLink copied to clipboard!

Description
:   The firmware settings that have been applied.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `simultaneousMultithreadingEnabled` | `boolean` | Allows a single physical processor core to appear as several logical processors. |
| `sriovEnabled` | `boolean` | SR-IOV support enables a hypervisor to create virtual instances of a PCI-express device, potentially increasing performance. |
| `virtualizationEnabled` | `boolean` | Supports the virtualization of platform hardware. |

Show more

#### [3.1.39. .status.provisioning.image](#status-provisioning-image) Copy linkLink copied to clipboard!

Description
:   Image holds the details of the last image successfully provisioned to the host.

Type
:   `object`

Required
:   * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `checksum` | `string` | Checksum is the checksum for the image. Required for all formats except for "live-iso" and OCI images (oci://). |
| `checksumType` | `string` | ChecksumType is the checksum algorithm for the image, e.g md5, sha256 or sha512. The special value "auto" can be used to detect the algorithm from the checksum. If missing, MD5 is used. If in doubt, use "auto". |
| `format` | `string` | Format contains the format of the image (raw, qcow2, …​). When set to "live-iso", an ISO 9660 image referenced by the url will be live-booted and not deployed to disk. |
| `url` | `string` | URL is a location of an image to deploy. |

Show more

#### [3.1.40. .status.provisioning.raid](#status-provisioning-raid) Copy linkLink copied to clipboard!

Description
:   The RAID configuration that has been applied.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hardwareRAIDVolumes` | `` | The list of logical disks for hardware RAID, if rootDeviceHints isn’t used, first volume is root volume. You can set the value of this field to `[]` to clear all the hardware RAID configurations. |
| `softwareRAIDVolumes` | `` | The list of logical disks for software RAID, if rootDeviceHints isn’t used, first volume is root volume. If HardwareRAIDVolumes is set this item will be invalid. The number of created Software RAID devices must be 1 or 2. If there is only one Software RAID device, it has to be a RAID-1. If there are two, the first one has to be a RAID-1, while the RAID level for the second one can be 0, 1, or 1+0. As the first RAID device will be the deployment device, enforcing a RAID-1 reduces the risk of ending up with a non-booting host in case of a disk failure. Software RAID will always be deleted. |

Show more

#### [3.1.41. .status.provisioning.rootDeviceHints](#status-provisioning-rootdevicehints) Copy linkLink copied to clipboard!

Description
:   The root device hints used to provision the host.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `deviceName` | `string` | A Linux device name like "/dev/vda", or a by-path link to it like "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0". The hint must match the actual value exactly. |
| `hctl` | `string` | A SCSI bus address like 0:0:0:0. The hint must match the actual value exactly. |
| `minSizeGigabytes` | `integer` | The minimum size of the device in Gigabytes. |
| `model` | `string` | A vendor-specific device identifier. The hint can be a substring of the actual value. |
| `rotational` | `boolean` | True if the device should use spinning media, false otherwise. |
| `serialNumber` | `string` | Device serial number. The hint must match the actual value exactly. |
| `vendor` | `string` | The name of the vendor or manufacturer of the device. The hint can be a substring of the actual value. |
| `wwn` | `string` | Unique storage identifier. The hint must match the actual value exactly. |
| `wwnVendorExtension` | `string` | Unique vendor storage identifier. The hint must match the actual value exactly. |
| `wwnWithExtension` | `string` | Unique storage identifier with the vendor extension appended. The hint must match the actual value exactly. |

Show more

#### [3.1.42. .status.triedCredentials](#status-triedcredentials) Copy linkLink copied to clipboard!

Description
:   The last credentials we sent to the provisioning backend.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `credentials` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `credentialsVersion` | `string` |  |

Show more

#### [3.1.43. .status.triedCredentials.credentials](#status-triedcredentials-credentials) Copy linkLink copied to clipboard!

Description
:   SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is unique within a namespace to reference a secret resource. |
| `namespace` | `string` | namespace defines the space within which the secret name must be unique. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/baremetalhosts`

  + `GET`: list objects of kind BareMetalHost
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/baremetalhosts`

  + `DELETE`: delete collection of BareMetalHost
  + `GET`: list objects of kind BareMetalHost
  + `POST`: create a BareMetalHost
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/baremetalhosts/{name}`

  + `DELETE`: delete a BareMetalHost
  + `GET`: read the specified BareMetalHost
  + `PATCH`: partially update the specified BareMetalHost
  + `PUT`: replace the specified BareMetalHost
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/baremetalhosts/{name}/status`

  + `GET`: read status of the specified BareMetalHost
  + `PATCH`: partially update status of the specified BareMetalHost
  + `PUT`: replace status of the specified BareMetalHost

#### [3.2.1. /apis/metal3.io/v1alpha1/baremetalhosts](#apismetal3-iov1alpha1baremetalhosts) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind BareMetalHost

Expand

Table 3.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHostList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-BareMetalHostList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/baremetalhosts](#apismetal3-iov1alpha1namespacesnamespacebaremetalhosts) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of BareMetalHost

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
:   list objects of kind BareMetalHost

Expand

Table 3.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHostList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-BareMetalHostList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a BareMetalHost

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
| `body` | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 3.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 201 - Created | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/baremetalhosts/{name}](#apismetal3-iov1alpha1namespacesnamespacebaremetalhostsname) Copy linkLink copied to clipboard!

Expand

Table 3.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the BareMetalHost |

Show more

HTTP method
:   `DELETE`

Description
:   delete a BareMetalHost

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
:   read the specified BareMetalHost

Expand

Table 3.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified BareMetalHost

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
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified BareMetalHost

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
| `body` | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 3.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 201 - Created | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/baremetalhosts/{name}/status](#apismetal3-iov1alpha1namespacesnamespacebaremetalhostsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 3.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the BareMetalHost |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified BareMetalHost

Expand

Table 3.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified BareMetalHost

Expand

Table 3.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified BareMetalHost

Expand

Table 3.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 3.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 3.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 201 - Created | [`BareMetalHost`](#baremetalhost-metal3-io-v1alpha1 "Chapter 3. BareMetalHost [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. DataImage [metal3.io/v1alpha1]](#dataimage-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   DataImage is the Schema for the dataimages API.

Type
:   `object`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | DataImageSpec defines the desired state of DataImage. |
| `status` | `object` | DataImageStatus defines the observed state of DataImage. |

Show more

#### [4.1.1. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   DataImageSpec defines the desired state of DataImage.

Type
:   `object`

Required
:   * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `url` | `string` | Url is the address of the dataImage that we want to attach to a BareMetalHost |

Show more

#### [4.1.2. .status](#status-3) Copy linkLink copied to clipboard!

Description
:   DataImageStatus defines the observed state of DataImage.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `attachedImage` | `object` | Currently attached DataImage |
| `error` | `object` | Error count and message when attaching/detaching |
| `lastReconciled` | `string` | Time of last reconciliation |

Show more

#### [4.1.3. .status.attachedImage](#status-attachedimage) Copy linkLink copied to clipboard!

Description
:   Currently attached DataImage

Type
:   `object`

Required
:   * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `url` | `string` |  |

Show more

#### [4.1.4. .status.error](#status-error) Copy linkLink copied to clipboard!

Description
:   Error count and message when attaching/detaching

Type
:   `object`

Required
:   * `count`
    * `message`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `count` | `integer` |  |
| `message` | `string` |  |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/dataimages`

  + `GET`: list objects of kind DataImage
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages`

  + `DELETE`: delete collection of DataImage
  + `GET`: list objects of kind DataImage
  + `POST`: create a DataImage
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}`

  + `DELETE`: delete a DataImage
  + `GET`: read the specified DataImage
  + `PATCH`: partially update the specified DataImage
  + `PUT`: replace the specified DataImage
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}/status`

  + `GET`: read status of the specified DataImage
  + `PATCH`: partially update status of the specified DataImage
  + `PUT`: replace status of the specified DataImage

#### [4.2.1. /apis/metal3.io/v1alpha1/dataimages](#apismetal3-iov1alpha1dataimages) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind DataImage

Expand

Table 4.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-DataImageList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages](#apismetal3-iov1alpha1namespacesnamespacedataimages) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of DataImage

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
:   list objects of kind DataImage

Expand

Table 4.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-DataImageList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a DataImage

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
| `body` | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 4.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 201 - Created | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}](#apismetal3-iov1alpha1namespacesnamespacedataimagesname) Copy linkLink copied to clipboard!

Expand

Table 4.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the DataImage |

Show more

HTTP method
:   `DELETE`

Description
:   delete a DataImage

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
:   read the specified DataImage

Expand

Table 4.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified DataImage

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
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified DataImage

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
| `body` | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 4.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 201 - Created | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}/status](#apismetal3-iov1alpha1namespacesnamespacedataimagesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 4.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the DataImage |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified DataImage

Expand

Table 4.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified DataImage

Expand

Table 4.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified DataImage

Expand

Table 4.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 4.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 4.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 201 - Created | [`DataImage`](#dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. FirmwareSchema [metal3.io/v1alpha1]](#firmwareschema-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   FirmwareSchema is the Schema for the firmwareschemas API.

Type
:   `object`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | FirmwareSchemaSpec defines the desired state of FirmwareSchema. |

Show more

#### [5.1.1. .spec](#spec-4) Copy linkLink copied to clipboard!

Description
:   FirmwareSchemaSpec defines the desired state of FirmwareSchema.

Type
:   `object`

Required
:   * `schema`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hardwareModel` | `string` | The hardware model associated with this schema |
| `hardwareVendor` | `string` | The hardware vendor associated with this schema |
| `schema` | `object` | Map of firmware name to schema |
| `schema{}` | `object` | Additional data describing the firmware setting. |

Show more

#### [5.1.2. .spec.schema](#spec-schema) Copy linkLink copied to clipboard!

Description
:   Map of firmware name to schema

Type
:   `object`

#### [5.1.3. .spec.schema{}](#spec-schema-2) Copy linkLink copied to clipboard!

Description
:   Additional data describing the firmware setting.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowable_values` | `array (string)` | The allowable value for an Enumeration type setting. |
| `attribute_type` | `string` | The type of setting. |
| `lower_bound` | `integer` | The lowest value for an Integer type setting. |
| `max_length` | `integer` | Maximum length for a String type setting. |
| `min_length` | `integer` | Minimum length for a String type setting. |
| `read_only` | `boolean` | Whether or not this setting is read only. |
| `unique` | `boolean` | Whether or not this setting’s value is unique to this node, e.g. a serial number. |
| `upper_bound` | `integer` | The highest value for an Integer type setting. |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/firmwareschemas`

  + `GET`: list objects of kind FirmwareSchema
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas`

  + `DELETE`: delete collection of FirmwareSchema
  + `GET`: list objects of kind FirmwareSchema
  + `POST`: create a FirmwareSchema
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas/{name}`

  + `DELETE`: delete a FirmwareSchema
  + `GET`: read the specified FirmwareSchema
  + `PATCH`: partially update the specified FirmwareSchema
  + `PUT`: replace the specified FirmwareSchema

#### [5.2.1. /apis/metal3.io/v1alpha1/firmwareschemas](#apismetal3-iov1alpha1firmwareschemas) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind FirmwareSchema

Expand

Table 5.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FirmwareSchemaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-FirmwareSchemaList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas](#apismetal3-iov1alpha1namespacesnamespacefirmwareschemas) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of FirmwareSchema

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
:   list objects of kind FirmwareSchema

Expand

Table 5.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FirmwareSchemaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-FirmwareSchemaList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a FirmwareSchema

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
| `body` | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 5.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 201 - Created | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/firmwareschemas/{name}](#apismetal3-iov1alpha1namespacesnamespacefirmwareschemasname) Copy linkLink copied to clipboard!

Expand

Table 5.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the FirmwareSchema |

Show more

HTTP method
:   `DELETE`

Description
:   delete a FirmwareSchema

Expand

Table 5.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 5.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified FirmwareSchema

Expand

Table 5.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified FirmwareSchema

Expand

Table 5.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified FirmwareSchema

Expand

Table 5.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 5.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 201 - Created | [`FirmwareSchema`](#firmwareschema-metal3-io-v1alpha1 "Chapter 5. FirmwareSchema [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. HardwareData [metal3.io/v1alpha1]](#hardwaredata-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   HardwareData is the Schema for the hardwaredata API.

Type
:   `object`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | HardwareDataSpec defines the desired state of HardwareData. |

Show more

#### [6.1.1. .spec](#spec-5) Copy linkLink copied to clipboard!

Description
:   HardwareDataSpec defines the desired state of HardwareData.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hardware` | `object` | The hardware discovered on the host during its inspection. |

Show more

#### [6.1.2. .spec.hardware](#spec-hardware) Copy linkLink copied to clipboard!

Description
:   The hardware discovered on the host during its inspection.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cpu` | `object` | Details of the CPU(s) in the system. |
| `firmware` | `object` | System firmware information. |
| `hostname` | `string` | Name of the host at the inspection time. |
| `nics` | `array` | List of network interfaces for the host. |
| `nics[]` | `object` | NIC describes one network interface on the host. |
| `ramMebibytes` | `integer` | The host’s amount of memory in Mebibytes. |
| `storage` | `array` | List of storage (disk, SSD, etc.) available to the host. |
| `storage[]` | `object` | Storage describes one storage device (disk, SSD, etc.) on the host. |
| `systemVendor` | `object` | System vendor information. |

Show more

#### [6.1.3. .spec.hardware.cpu](#spec-hardware-cpu) Copy linkLink copied to clipboard!

Description
:   Details of the CPU(s) in the system.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `arch` | `string` |  |
| `clockMegahertz` | `number` | ClockSpeed is a clock speed in MHz |
| `count` | `integer` |  |
| `flags` | `array (string)` |  |
| `model` | `string` |  |

Show more

#### [6.1.4. .spec.hardware.firmware](#spec-hardware-firmware) Copy linkLink copied to clipboard!

Description
:   System firmware information.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `bios` | `object` | The BIOS for this firmware |

Show more

#### [6.1.5. .spec.hardware.firmware.bios](#spec-hardware-firmware-bios) Copy linkLink copied to clipboard!

Description
:   The BIOS for this firmware

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `date` | `string` | The release/build date for this BIOS |
| `vendor` | `string` | The vendor name for this BIOS |
| `version` | `string` | The version of the BIOS |

Show more

#### [6.1.6. .spec.hardware.nics](#spec-hardware-nics) Copy linkLink copied to clipboard!

Description
:   List of network interfaces for the host.

Type
:   `array`

#### [6.1.7. .spec.hardware.nics[]](#spec-hardware-nics-2) Copy linkLink copied to clipboard!

Description
:   NIC describes one network interface on the host.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ip` | `string` | The IP address of the interface. This will be an IPv4 or IPv6 address if one is present. If both IPv4 and IPv6 addresses are present in a dual-stack environment, two nics will be output, one with each IP. |
| `lldp` | `object` | LLDP data for this interface |
| `mac` | `string` | The device MAC address |
| `model` | `string` | The vendor and product IDs of the NIC, e.g. "0x8086 0x1572" |
| `name` | `string` | The name of the network interface, e.g. "en0" |
| `pciAddress` | `string` | The NIC PCI address |
| `pxe` | `boolean` | Whether the NIC is PXE Bootable |
| `speedGbps` | `integer` | The speed of the device in Gigabits per second |
| `vlanId` | `integer` | The untagged VLAN ID |
| `vlans` | `array` | The VLANs available |
| `vlans[]` | `object` | VLAN represents the name and ID of a VLAN. |

Show more

#### [6.1.8. .spec.hardware.nics[].lldp](#spec-hardware-nics-lldp) Copy linkLink copied to clipboard!

Description
:   LLDP data for this interface

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `portID` | `string` | The switch port ID from LLDP |
| `switchID` | `string` | The switch chassis ID from LLDP |
| `switchSystemName` | `string` | The switch system name from LLDP |

Show more

#### [6.1.9. .spec.hardware.nics[].vlans](#spec-hardware-nics-vlans) Copy linkLink copied to clipboard!

Description
:   The VLANs available

Type
:   `array`

#### [6.1.10. .spec.hardware.nics[].vlans[]](#spec-hardware-nics-vlans-2) Copy linkLink copied to clipboard!

Description
:   VLAN represents the name and ID of a VLAN.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `id` | `integer` | VLANID is a 12-bit 802.1Q VLAN identifier |
| `name` | `string` |  |

Show more

#### [6.1.11. .spec.hardware.storage](#spec-hardware-storage) Copy linkLink copied to clipboard!

Description
:   List of storage (disk, SSD, etc.) available to the host.

Type
:   `array`

#### [6.1.12. .spec.hardware.storage[]](#spec-hardware-storage-2) Copy linkLink copied to clipboard!

Description
:   Storage describes one storage device (disk, SSD, etc.) on the host.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `alternateNames` | `array (string)` | A list of alternate Linux device names of the disk, e.g. "/dev/sda". Note that this list is not exhaustive, and names may not be stable across reboots. |
| `hctl` | `string` | The SCSI location of the device |
| `model` | `string` | Hardware model |
| `name` | `string` | A Linux device name of the disk, e.g. "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0". This will be a name that is stable across reboots if one is available. |
| `rotational` | `boolean` | Whether this disk represents rotational storage. This field is not recommended for usage, please prefer using 'Type' field instead, this field will be deprecated eventually. |
| `serialNumber` | `string` | The serial number of the device |
| `sizeBytes` | `integer` | The size of the disk in Bytes |
| `type` | `string` | Device type, one of: HDD, SSD, NVME. |
| `vendor` | `string` | The name of the vendor of the device |
| `wwn` | `string` | The WWN of the device |
| `wwnVendorExtension` | `string` | The WWN Vendor extension of the device |
| `wwnWithExtension` | `string` | The WWN with the extension |

Show more

#### [6.1.13. .spec.hardware.systemVendor](#spec-hardware-systemvendor) Copy linkLink copied to clipboard!

Description
:   System vendor information.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `manufacturer` | `string` |  |
| `productName` | `string` |  |
| `serialNumber` | `string` |  |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/hardwaredata`

  + `GET`: list objects of kind HardwareData
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata`

  + `DELETE`: delete collection of HardwareData
  + `GET`: list objects of kind HardwareData
  + `POST`: create a HardwareData
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata/{name}`

  + `DELETE`: delete a HardwareData
  + `GET`: read the specified HardwareData
  + `PATCH`: partially update the specified HardwareData
  + `PUT`: replace the specified HardwareData

#### [6.2.1. /apis/metal3.io/v1alpha1/hardwaredata](#apismetal3-iov1alpha1hardwaredata) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind HardwareData

Expand

Table 6.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HardwareDataList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HardwareDataList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata](#apismetal3-iov1alpha1namespacesnamespacehardwaredata) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of HardwareData

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind HardwareData

Expand

Table 6.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HardwareDataList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HardwareDataList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a HardwareData

Expand

Table 6.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 6.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata/{name}](#apismetal3-iov1alpha1namespacesnamespacehardwaredataname) Copy linkLink copied to clipboard!

Expand

Table 6.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HardwareData |

Show more

HTTP method
:   `DELETE`

Description
:   delete a HardwareData

Expand

Table 6.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 6.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified HardwareData

Expand

Table 6.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified HardwareData

Expand

Table 6.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified HardwareData

Expand

Table 6.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 6.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HardwareData`](#hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]](#hostfirmwarecomponents-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   HostFirmwareComponents is the Schema for the hostfirmwarecomponents API.

Type
:   `object`

### [7.1. Specification](#specification-6) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | HostFirmwareComponentsSpec defines the desired state of HostFirmwareComponents. |
| `status` | `object` | HostFirmwareComponentsStatus defines the observed state of HostFirmwareComponents. |

Show more

#### [7.1.1. .spec](#spec-6) Copy linkLink copied to clipboard!

Description
:   HostFirmwareComponentsSpec defines the desired state of HostFirmwareComponents.

Type
:   `object`

Required
:   * `updates`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `updates` | `array` |  |
| `updates[]` | `object` | FirmwareUpdate defines a firmware update specification. |

Show more

#### [7.1.2. .spec.updates](#spec-updates) Copy linkLink copied to clipboard!

Description

Type
:   `array`

#### [7.1.3. .spec.updates[]](#spec-updates-2) Copy linkLink copied to clipboard!

Description
:   FirmwareUpdate defines a firmware update specification.

Type
:   `object`

Required
:   * `component`
    * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `component` | `string` |  |
| `url` | `string` |  |

Show more

#### [7.1.4. .status](#status-4) Copy linkLink copied to clipboard!

Description
:   HostFirmwareComponentsStatus defines the observed state of HostFirmwareComponents.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `components` | `array` | Components is the list of all available firmware components and their information. |
| `components[]` | `object` | FirmwareComponentStatus defines the status of a firmware component. |
| `conditions` | `array` | Track whether updates stored in the spec are valid based on the schema |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `lastUpdated` | `string` | Time that the status was last updated |
| `updates` | `array` | Updates is the list of all firmware components that should be updated they are specified via name and url fields. |
| `updates[]` | `object` | FirmwareUpdate defines a firmware update specification. |

Show more

#### [7.1.5. .status.components](#status-components) Copy linkLink copied to clipboard!

Description
:   Components is the list of all available firmware components and their information.

Type
:   `array`

#### [7.1.6. .status.components[]](#status-components-2) Copy linkLink copied to clipboard!

Description
:   FirmwareComponentStatus defines the status of a firmware component.

Type
:   `object`

Required
:   * `component`
    * `initialVersion`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `component` | `string` |  |
| `currentVersion` | `string` |  |
| `initialVersion` | `string` |  |
| `lastVersionFlashed` | `string` |  |
| `updatedAt` | `string` |  |

Show more

#### [7.1.7. .status.conditions](#status-conditions-3) Copy linkLink copied to clipboard!

Description
:   Track whether updates stored in the spec are valid based on the schema

Type
:   `array`

#### [7.1.8. .status.conditions[]](#status-conditions-4) Copy linkLink copied to clipboard!

Description
:   Condition contains details for one aspect of the current state of this API Resource.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `message`
    * `reason`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

Show more

#### [7.1.9. .status.updates](#status-updates) Copy linkLink copied to clipboard!

Description
:   Updates is the list of all firmware components that should be updated they are specified via name and url fields.

Type
:   `array`

#### [7.1.10. .status.updates[]](#status-updates-2) Copy linkLink copied to clipboard!

Description
:   FirmwareUpdate defines a firmware update specification.

Type
:   `object`

Required
:   * `component`
    * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `component` | `string` |  |
| `url` | `string` |  |

Show more

### [7.2. API endpoints](#api-endpoints-6) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/hostfirmwarecomponents`

  + `GET`: list objects of kind HostFirmwareComponents
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwarecomponents`

  + `DELETE`: delete collection of HostFirmwareComponents
  + `GET`: list objects of kind HostFirmwareComponents
  + `POST`: create HostFirmwareComponents
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwarecomponents/{name}`

  + `DELETE`: delete HostFirmwareComponents
  + `GET`: read the specified HostFirmwareComponents
  + `PATCH`: partially update the specified HostFirmwareComponents
  + `PUT`: replace the specified HostFirmwareComponents
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwarecomponents/{name}/status`

  + `GET`: read status of the specified HostFirmwareComponents
  + `PATCH`: partially update status of the specified HostFirmwareComponents
  + `PUT`: replace status of the specified HostFirmwareComponents

#### [7.2.1. /apis/metal3.io/v1alpha1/hostfirmwarecomponents](#apismetal3-iov1alpha1hostfirmwarecomponents) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind HostFirmwareComponents

Expand

Table 7.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponentsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostFirmwareComponentsList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwarecomponents](#apismetal3-iov1alpha1namespacesnamespacehostfirmwarecomponents) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of HostFirmwareComponents

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
:   list objects of kind HostFirmwareComponents

Expand

Table 7.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponentsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostFirmwareComponentsList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create HostFirmwareComponents

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
| `body` | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 7.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwarecomponents/{name}](#apismetal3-iov1alpha1namespacesnamespacehostfirmwarecomponentsname) Copy linkLink copied to clipboard!

Expand

Table 7.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HostFirmwareComponents |

Show more

HTTP method
:   `DELETE`

Description
:   delete HostFirmwareComponents

Expand

Table 7.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 7.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified HostFirmwareComponents

Expand

Table 7.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified HostFirmwareComponents

Expand

Table 7.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified HostFirmwareComponents

Expand

Table 7.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 7.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwarecomponents/{name}/status](#apismetal3-iov1alpha1namespacesnamespacehostfirmwarecomponentsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 7.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HostFirmwareComponents |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified HostFirmwareComponents

Expand

Table 7.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified HostFirmwareComponents

Expand

Table 7.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified HostFirmwareComponents

Expand

Table 7.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 7.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostFirmwareComponents`](#hostfirmwarecomponents-metal3-io-v1alpha1 "Chapter 7. HostFirmwareComponents [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]](#hostfirmwaresettings-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   HostFirmwareSettings is the Schema for the hostfirmwaresettings API.

Type
:   `object`

### [8.1. Specification](#specification-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | HostFirmwareSettingsSpec defines the desired state of HostFirmwareSettings. |
| `status` | `object` | HostFirmwareSettingsStatus defines the observed state of HostFirmwareSettings. |

Show more

#### [8.1.1. .spec](#spec-7) Copy linkLink copied to clipboard!

Description
:   HostFirmwareSettingsSpec defines the desired state of HostFirmwareSettings.

Type
:   `object`

Required
:   * `settings`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `settings` | `integer-or-string` | Settings are the desired firmware settings stored as name/value pairs. |

Show more

#### [8.1.2. .status](#status-5) Copy linkLink copied to clipboard!

Description
:   HostFirmwareSettingsStatus defines the observed state of HostFirmwareSettings.

Type
:   `object`

Required
:   * `settings`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | Track whether settings stored in the spec are valid based on the schema |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `lastUpdated` | `string` | Time that the status was last updated |
| `schema` | `object` | FirmwareSchema is a reference to the Schema used to describe each FirmwareSetting. By default, this will be a Schema in the same Namespace as the settings but it can be overwritten in the Spec |
| `settings` | `object (string)` | Settings are the firmware settings stored as name/value pairs |

Show more

#### [8.1.3. .status.conditions](#status-conditions-5) Copy linkLink copied to clipboard!

Description
:   Track whether settings stored in the spec are valid based on the schema

Type
:   `array`

#### [8.1.4. .status.conditions[]](#status-conditions-6) Copy linkLink copied to clipboard!

Description
:   Condition contains details for one aspect of the current state of this API Resource.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `message`
    * `reason`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

Show more

#### [8.1.5. .status.schema](#status-schema) Copy linkLink copied to clipboard!

Description
:   FirmwareSchema is a reference to the Schema used to describe each FirmwareSetting. By default, this will be a Schema in the same Namespace as the settings but it can be overwritten in the Spec

Type
:   `object`

Required
:   * `name`
    * `namespace`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | `name` is the reference to the schema. |
| `namespace` | `string` | `namespace` is the namespace of the where the schema is stored. |

Show more

### [8.2. API endpoints](#api-endpoints-7) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/hostfirmwaresettings`

  + `GET`: list objects of kind HostFirmwareSettings
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings`

  + `DELETE`: delete collection of HostFirmwareSettings
  + `GET`: list objects of kind HostFirmwareSettings
  + `POST`: create HostFirmwareSettings
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}`

  + `DELETE`: delete HostFirmwareSettings
  + `GET`: read the specified HostFirmwareSettings
  + `PATCH`: partially update the specified HostFirmwareSettings
  + `PUT`: replace the specified HostFirmwareSettings
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}/status`

  + `GET`: read status of the specified HostFirmwareSettings
  + `PATCH`: partially update status of the specified HostFirmwareSettings
  + `PUT`: replace status of the specified HostFirmwareSettings

#### [8.2.1. /apis/metal3.io/v1alpha1/hostfirmwaresettings](#apismetal3-iov1alpha1hostfirmwaresettings) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind HostFirmwareSettings

Expand

Table 8.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettingsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostFirmwareSettingsList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings](#apismetal3-iov1alpha1namespacesnamespacehostfirmwaresettings) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of HostFirmwareSettings

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
:   list objects of kind HostFirmwareSettings

Expand

Table 8.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettingsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostFirmwareSettingsList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create HostFirmwareSettings

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
| `body` | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 8.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}](#apismetal3-iov1alpha1namespacesnamespacehostfirmwaresettingsname) Copy linkLink copied to clipboard!

Expand

Table 8.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HostFirmwareSettings |

Show more

HTTP method
:   `DELETE`

Description
:   delete HostFirmwareSettings

Expand

Table 8.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 8.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified HostFirmwareSettings

Expand

Table 8.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified HostFirmwareSettings

Expand

Table 8.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified HostFirmwareSettings

Expand

Table 8.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 8.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}/status](#apismetal3-iov1alpha1namespacesnamespacehostfirmwaresettingsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 8.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HostFirmwareSettings |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified HostFirmwareSettings

Expand

Table 8.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified HostFirmwareSettings

Expand

Table 8.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified HostFirmwareSettings

Expand

Table 8.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 8.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostFirmwareSettings`](#hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]](#hostupdatepolicy-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   HostUpdatePolicy is the Schema for the hostupdatepolicy API.

Type
:   `object`

### [9.1. Specification](#specification-8) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | HostUpdatePolicySpec defines the desired state of HostUpdatePolicy. |
| `status` | `object` | HostUpdatePolicyStatus defines the observed state of HostUpdatePolicy. |

Show more

#### [9.1.1. .spec](#spec-8) Copy linkLink copied to clipboard!

Description
:   HostUpdatePolicySpec defines the desired state of HostUpdatePolicy.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `firmwareSettings` | `string` | Defines policy for changing firmware settings |
| `firmwareUpdates` | `string` | Defines policy for updating firmware |

Show more

#### [9.1.2. .status](#status-6) Copy linkLink copied to clipboard!

Description
:   HostUpdatePolicyStatus defines the observed state of HostUpdatePolicy.

Type
:   `object`

### [9.2. API endpoints](#api-endpoints-8) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/hostupdatepolicies`

  + `GET`: list objects of kind HostUpdatePolicy
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostupdatepolicies`

  + `DELETE`: delete collection of HostUpdatePolicy
  + `GET`: list objects of kind HostUpdatePolicy
  + `POST`: create a HostUpdatePolicy
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostupdatepolicies/{name}`

  + `DELETE`: delete a HostUpdatePolicy
  + `GET`: read the specified HostUpdatePolicy
  + `PATCH`: partially update the specified HostUpdatePolicy
  + `PUT`: replace the specified HostUpdatePolicy

#### [9.2.1. /apis/metal3.io/v1alpha1/hostupdatepolicies](#apismetal3-iov1alpha1hostupdatepolicies) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind HostUpdatePolicy

Expand

Table 9.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostUpdatePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostUpdatePolicyList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostupdatepolicies](#apismetal3-iov1alpha1namespacesnamespacehostupdatepolicies) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of HostUpdatePolicy

Expand

Table 9.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind HostUpdatePolicy

Expand

Table 9.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostUpdatePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostUpdatePolicyList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a HostUpdatePolicy

Expand

Table 9.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 9.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostupdatepolicies/{name}](#apismetal3-iov1alpha1namespacesnamespacehostupdatepoliciesname) Copy linkLink copied to clipboard!

Expand

Table 9.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HostUpdatePolicy |

Show more

HTTP method
:   `DELETE`

Description
:   delete a HostUpdatePolicy

Expand

Table 9.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 9.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified HostUpdatePolicy

Expand

Table 9.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified HostUpdatePolicy

Expand

Table 9.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified HostUpdatePolicy

Expand

Table 9.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 9.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 201 - Created | [`HostUpdatePolicy`](#hostupdatepolicy-metal3-io-v1alpha1 "Chapter 9. HostUpdatePolicy [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) Copy linkLink copied to clipboard!

Description
:   Metal3Remediation is the Schema for the metal3remediations API.

Type
:   `object`

### [10.1. Specification](#specification-9) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Metal3RemediationSpec defines the desired state of Metal3Remediation. |
| `status` | `object` | Metal3RemediationStatus defines the observed state of Metal3Remediation. |

Show more

#### [10.1.1. .spec](#spec-9) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationSpec defines the desired state of Metal3Remediation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `strategy` | `object` | Strategy field defines remediation strategy. |

Show more

#### [10.1.2. .spec.strategy](#spec-strategy) Copy linkLink copied to clipboard!

Description
:   Strategy field defines remediation strategy.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `retryLimit` | `integer` | Sets maximum number of remediation retries. |
| `timeout` | `string` | Sets the timeout between remediation retries. |
| `type` | `string` | Type of remediation. |

Show more

#### [10.1.3. .status](#status-7) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationStatus defines the observed state of Metal3Remediation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastRemediated` | `string` | LastRemediated identifies when the host was last remediated |
| `phase` | `string` | Phase represents the current phase of machine remediation. E.g. Pending, Running, Done etc. |
| `retryCount` | `integer` | RetryCount can be used as a counter during the remediation. Field can hold number of reboots etc. |

Show more

### [10.2. API endpoints](#api-endpoints-9) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/metal3remediations`

  + `GET`: list objects of kind Metal3Remediation
* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations`

  + `DELETE`: delete collection of Metal3Remediation
  + `GET`: list objects of kind Metal3Remediation
  + `POST`: create a Metal3Remediation
* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}`

  + `DELETE`: delete a Metal3Remediation
  + `GET`: read the specified Metal3Remediation
  + `PATCH`: partially update the specified Metal3Remediation
  + `PUT`: replace the specified Metal3Remediation
* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}/status`

  + `GET`: read status of the specified Metal3Remediation
  + `PATCH`: partially update status of the specified Metal3Remediation
  + `PUT`: replace status of the specified Metal3Remediation

#### [10.2.1. /apis/infrastructure.cluster.x-k8s.io/v1beta1/metal3remediations](#apisinfrastructure-cluster-x-k8s-iov1beta1metal3remediations) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind Metal3Remediation

Expand

Table 10.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.2. /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations](#apisinfrastructure-cluster-x-k8s-iov1beta1namespacesnamespacemetal3remediations) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Metal3Remediation

Expand

Table 10.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Metal3Remediation

Expand

Table 10.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Metal3Remediation

Expand

Table 10.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 10.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 201 - Created | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 202 - Accepted | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.3. /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}](#apisinfrastructure-cluster-x-k8s-iov1beta1namespacesnamespacemetal3remediationsname) Copy linkLink copied to clipboard!

Expand

Table 10.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Metal3Remediation |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Metal3Remediation

Expand

Table 10.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 10.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Metal3Remediation

Expand

Table 10.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Metal3Remediation

Expand

Table 10.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Metal3Remediation

Expand

Table 10.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 10.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 201 - Created | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.4. /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediations/{name}/status](#apisinfrastructure-cluster-x-k8s-iov1beta1namespacesnamespacemetal3remediationsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 10.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Metal3Remediation |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Metal3Remediation

Expand

Table 10.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Metal3Remediation

Expand

Table 10.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Metal3Remediation

Expand

Table 10.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 10.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 201 - Created | [`Metal3Remediation`](#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 10. Metal3Remediation [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationTemplate is the Schema for the metal3remediationtemplates API.

Type
:   `object`

### [11.1. Specification](#specification-10) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Metal3RemediationTemplateSpec defines the desired state of Metal3RemediationTemplate. |
| `status` | `object` | Metal3RemediationTemplateStatus defines the observed state of Metal3RemediationTemplate. |

Show more

#### [11.1.1. .spec](#spec-10) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationTemplateSpec defines the desired state of Metal3RemediationTemplate.

Type
:   `object`

Required
:   * `template`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `template` | `object` | Metal3RemediationTemplateResource describes the data needed to create a Metal3Remediation from a template. |

Show more

#### [11.1.2. .spec.template](#spec-template) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationTemplateResource describes the data needed to create a Metal3Remediation from a template.

Type
:   `object`

Required
:   * `spec`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `spec` | `object` | Spec is the specification of the desired behavior of the Metal3Remediation. |

Show more

#### [11.1.3. .spec.template.spec](#spec-template-spec) Copy linkLink copied to clipboard!

Description
:   Spec is the specification of the desired behavior of the Metal3Remediation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `strategy` | `object` | Strategy field defines remediation strategy. |

Show more

#### [11.1.4. .spec.template.spec.strategy](#spec-template-spec-strategy) Copy linkLink copied to clipboard!

Description
:   Strategy field defines remediation strategy.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `retryLimit` | `integer` | Sets maximum number of remediation retries. |
| `timeout` | `string` | Sets the timeout between remediation retries. |
| `type` | `string` | Type of remediation. |

Show more

#### [11.1.5. .status](#status-8) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationTemplateStatus defines the observed state of Metal3RemediationTemplate.

Type
:   `object`

Required
:   * `status`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `status` | `object` | Metal3RemediationStatus defines the observed state of Metal3Remediation |

Show more

#### [11.1.6. .status.status](#status-status) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationStatus defines the observed state of Metal3Remediation

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastRemediated` | `string` | LastRemediated identifies when the host was last remediated |
| `phase` | `string` | Phase represents the current phase of machine remediation. E.g. Pending, Running, Done etc. |
| `retryCount` | `integer` | RetryCount can be used as a counter during the remediation. Field can hold number of reboots etc. |

Show more

### [11.2. API endpoints](#api-endpoints-10) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/metal3remediationtemplates`

  + `GET`: list objects of kind Metal3RemediationTemplate
* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediationtemplates`

  + `DELETE`: delete collection of Metal3RemediationTemplate
  + `GET`: list objects of kind Metal3RemediationTemplate
  + `POST`: create a Metal3RemediationTemplate
* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediationtemplates/{name}`

  + `DELETE`: delete a Metal3RemediationTemplate
  + `GET`: read the specified Metal3RemediationTemplate
  + `PATCH`: partially update the specified Metal3RemediationTemplate
  + `PUT`: replace the specified Metal3RemediationTemplate
* `/apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediationtemplates/{name}/status`

  + `GET`: read status of the specified Metal3RemediationTemplate
  + `PATCH`: partially update status of the specified Metal3RemediationTemplate
  + `PUT`: replace status of the specified Metal3RemediationTemplate

#### [11.2.1. /apis/infrastructure.cluster.x-k8s.io/v1beta1/metal3remediationtemplates](#apisinfrastructure-cluster-x-k8s-iov1beta1metal3remediationtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind Metal3RemediationTemplate

Expand

Table 11.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationTemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.2. /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediationtemplates](#apisinfrastructure-cluster-x-k8s-iov1beta1namespacesnamespacemetal3remediationtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Metal3RemediationTemplate

Expand

Table 11.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Metal3RemediationTemplate

Expand

Table 11.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationTemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Metal3RemediationTemplate

Expand

Table 11.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 11.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 201 - Created | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 202 - Accepted | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.3. /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediationtemplates/{name}](#apisinfrastructure-cluster-x-k8s-iov1beta1namespacesnamespacemetal3remediationtemplatesname) Copy linkLink copied to clipboard!

Expand

Table 11.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Metal3RemediationTemplate |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Metal3RemediationTemplate

Expand

Table 11.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 11.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Metal3RemediationTemplate

Expand

Table 11.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Metal3RemediationTemplate

Expand

Table 11.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Metal3RemediationTemplate

Expand

Table 11.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 11.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 201 - Created | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.4. /apis/infrastructure.cluster.x-k8s.io/v1beta1/namespaces/{namespace}/metal3remediationtemplates/{name}/status](#apisinfrastructure-cluster-x-k8s-iov1beta1namespacesnamespacemetal3remediationtemplatesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 11.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Metal3RemediationTemplate |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Metal3RemediationTemplate

Expand

Table 11.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Metal3RemediationTemplate

Expand

Table 11.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Metal3RemediationTemplate

Expand

Table 11.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 11.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 201 - Created | [`Metal3RemediationTemplate`](#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1 "Chapter 11. Metal3RemediationTemplate [infrastructure.cluster.x-k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]](#preprovisioningimage-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   PreprovisioningImage is the Schema for the preprovisioningimages API.

Type
:   `object`

### [12.1. Specification](#specification-11) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PreprovisioningImageSpec defines the desired state of PreprovisioningImage. |
| `status` | `object` | PreprovisioningImageStatus defines the observed state of PreprovisioningImage. |

Show more

#### [12.1.1. .spec](#spec-11) Copy linkLink copied to clipboard!

Description
:   PreprovisioningImageSpec defines the desired state of PreprovisioningImage.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `acceptFormats` | `array (string)` | acceptFormats is a list of acceptable image formats. |
| `architecture` | `string` | architecture is the processor architecture for which to build the image. |
| `networkDataName` | `string` | networkDataName is the name of a Secret in the local namespace that contains network data to build in to the image. |

Show more

#### [12.1.2. .status](#status-9) Copy linkLink copied to clipboard!

Description
:   PreprovisioningImageStatus defines the observed state of PreprovisioningImage.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `architecture` | `string` | architecture is the processor architecture for which the image is built |
| `conditions` | `array` | conditions describe the state of the built image |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `extraKernelParams` | `string` | extraKernelParams is a string with extra parameters to pass to the kernel when booting the image over network. Only makes sense for initrd images. |
| `format` | `string` | format is the type of image that is available at the download url: either iso or initrd. |
| `imageUrl` | `string` | imageUrl is the URL from which the built image can be downloaded. |
| `kernelUrl` | `string` | kernelUrl is the URL from which the kernel of the image can be downloaded. Only makes sense for initrd images. |
| `networkData` | `object` | networkData is a reference to the version of the Secret containing the network data used to build the image. |

Show more

#### [12.1.3. .status.conditions](#status-conditions-7) Copy linkLink copied to clipboard!

Description
:   conditions describe the state of the built image

Type
:   `array`

#### [12.1.4. .status.conditions[]](#status-conditions-8) Copy linkLink copied to clipboard!

Description
:   Condition contains details for one aspect of the current state of this API Resource.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `message`
    * `reason`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

Show more

#### [12.1.5. .status.networkData](#status-networkdata) Copy linkLink copied to clipboard!

Description
:   networkData is a reference to the version of the Secret containing the network data used to build the image.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` |  |
| `version` | `string` |  |

Show more

### [12.2. API endpoints](#api-endpoints-11) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/preprovisioningimages`

  + `GET`: list objects of kind PreprovisioningImage
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages`

  + `DELETE`: delete collection of PreprovisioningImage
  + `GET`: list objects of kind PreprovisioningImage
  + `POST`: create a PreprovisioningImage
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}`

  + `DELETE`: delete a PreprovisioningImage
  + `GET`: read the specified PreprovisioningImage
  + `PATCH`: partially update the specified PreprovisioningImage
  + `PUT`: replace the specified PreprovisioningImage
* `/apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}/status`

  + `GET`: read status of the specified PreprovisioningImage
  + `PATCH`: partially update status of the specified PreprovisioningImage
  + `PUT`: replace status of the specified PreprovisioningImage

#### [12.2.1. /apis/metal3.io/v1alpha1/preprovisioningimages](#apismetal3-iov1alpha1preprovisioningimages) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind PreprovisioningImage

Expand

Table 12.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-PreprovisioningImageList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages](#apismetal3-iov1alpha1namespacesnamespacepreprovisioningimages) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PreprovisioningImage

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
:   list objects of kind PreprovisioningImage

Expand

Table 12.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-PreprovisioningImageList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PreprovisioningImage

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
| `body` | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 12.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 201 - Created | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}](#apismetal3-iov1alpha1namespacesnamespacepreprovisioningimagesname) Copy linkLink copied to clipboard!

Expand

Table 12.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PreprovisioningImage |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PreprovisioningImage

Expand

Table 12.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 12.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PreprovisioningImage

Expand

Table 12.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PreprovisioningImage

Expand

Table 12.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PreprovisioningImage

Expand

Table 12.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 12.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 201 - Created | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}/status](#apismetal3-iov1alpha1namespacesnamespacepreprovisioningimagesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 12.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PreprovisioningImage |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified PreprovisioningImage

Expand

Table 12.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified PreprovisioningImage

Expand

Table 12.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified PreprovisioningImage

Expand

Table 12.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 12.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 201 - Created | [`PreprovisioningImage`](#preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 13. Provisioning [metal3.io/v1alpha1]](#provisioning-metal3-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   Provisioning contains configuration used by the Provisioning service (Ironic) to provision baremetal hosts. Provisioning is created by the OpenShift installer using admin or user provided information about the provisioning network and the NIC on the server that can be used to PXE boot it. This CR is a singleton, created by the installer and currently only consumed by the cluster-baremetal-operator to bring up and update containers in a metal3 cluster.

Type
:   `object`

### [13.1. Specification](#specification-12) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | ProvisioningSpec defines the desired state of Provisioning |
| `status` | `object` | ProvisioningStatus defines the observed state of Provisioning |

Show more

#### [13.1.1. .spec](#spec-12) Copy linkLink copied to clipboard!

Description
:   ProvisioningSpec defines the desired state of Provisioning

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalNTPServers` | `array (string)` | AdditionalNTPServers is a list of NTP Servers to be used by the provisioning service |
| `bootIsoSource` | `string` | BootIsoSource provides a way to set the location where the iso image to boot the nodes will be served from. By default the boot iso image is cached locally and served from the Provisioning service (Ironic) nodes using an auxiliary httpd server. If the boot iso image is already served by an httpd server, setting this option to http allows to directly provide the image from there; in this case, the network (either internal or external) where the httpd server that hosts the boot iso is needs to be accessible by the metal3 pod. |
| `disableVirtualMediaTLS` | `boolean` | DisableVirtualMediaTLS turns off TLS on the virtual media server, which may be required for hardware that cannot accept HTTPS links. |
| `externalIPs` | `array (string)` | ExternalIPs are the external-facing IP addresses used to access the Ironic service. Most users will not need this set. It is recommended to leave this unset unless actually necessary. |
| `preProvisioningOSDownloadURLs` | `object` | PreprovisioningOSDownloadURLs is set of CoreOS Live URLs that would be necessary to provision a worker either using virtual media or PXE. |
| `prometheusExporter` | `object` | PrometheusExporter configures sensor data collection and Prometheus metrics export. When enabled, this configures Ironic to collect sensor data, deploys the ironic-prometheus-exporter container, and creates supporting resources (ServiceMonitor, Service ports) to expose hardware sensor metrics for Prometheus. |
| `provisioningDHCPExternal` | `boolean` | ProvisioningDHCPExternal indicates whether the DHCP server for IP addresses in the provisioning DHCP range is present within the metal3 cluster or external to it. This field is being deprecated in favor of provisioningNetwork. |
| `provisioningDHCPRange` | `string` | ProvisioningDHCPRange needs to be interpreted along with ProvisioningDHCPExternal. If the value of provisioningDHCPExternal is set to False, then ProvisioningDHCPRange represents the range of IP addresses that the DHCP server running within the metal3 cluster can use while provisioning baremetal servers. If the value of ProvisioningDHCPExternal is set to True, then the value of ProvisioningDHCPRange will be ignored. When the value of ProvisioningDHCPExternal is set to False, indicating an internal DHCP server and the value of ProvisioningDHCPRange is not set, then the DHCP range is taken to be the default range which goes from .10 to .100 of the ProvisioningNetworkCIDR. This is the only value in all of the Provisioning configuration that can be changed after the installer has created the CR. This value needs to be two comma sererated IP addresses within the ProvisioningNetworkCIDR where the 1st address represents the start of the range and the 2nd address represents the last usable address in the range. |
| `provisioningDNS` | `boolean` | ProvisioningDNS allows sending the DNS information via DHCP on the provisionig network. It is off by default since the Provisioning service itself (Ironic) does not require DNS, but it may be useful for layered products (e.g. ZTP). |
| `provisioningIP` | `string` | ProvisioningIP is the IP address assigned to the provisioningInterface of the baremetal server. This IP address should be within the provisioning subnet, and outside of the DHCP range. |
| `provisioningInterface` | `string` | ProvisioningInterface is the name of the network interface on a baremetal server to the provisioning network. It can have values like eth1 or ens3. |
| `provisioningMacAddresses` | `array (string)` | ProvisioningMacAddresses is a list of mac addresses of network interfaces on a baremetal server to the provisioning network. Use this instead of ProvisioningInterface to allow interfaces of different names. If not provided it will be populated by the BMH.Spec.BootMacAddress of each master. |
| `provisioningNetwork` | `string` | ProvisioningNetwork provides a way to indicate the state of the underlying network configuration for the provisioning network. This field can have one of the following values - `Managed`- when the provisioning network is completely managed by the Baremetal IPI solution. `Unmanaged`- when the provsioning network is present and used but the user is responsible for managing DHCP. Virtual media provisioning is recommended but PXE is still available if required. `Disabled`- when the provisioning network is fully disabled. User can bring up the baremetal cluster using virtual media or assisted installation. If using metal3 for power management, BMCs must be accessible from the machine networks. User should provide two IPs on the external network that would be used for provisioning services. |
| `provisioningNetworkCIDR` | `string` | ProvisioningNetworkCIDR is the network on which the baremetal nodes are provisioned. The provisioningIP and the IPs in the dhcpRange all come from within this network. When using IPv6 and in a network managed by the Baremetal IPI solution this cannot be a network larger than a /64. |
| `provisioningNetworkGateway` | `string` | ProvisioningNetworkGateway is the IP address of the default gateway for the provisioning network. This gateway is provided to baremetal hosts via DHCP to enable routing to external networks during inspection and provisioning. This field is optional and only used when ProvisioningNetwork is set to Managed. The gateway IP must be within the ProvisioningNetworkCIDR but outside of the ProvisioningDHCPRange and must not be the same as ProvisioningIP. |
| `provisioningOSDownloadURL` | `string` | ProvisioningOSDownloadURL is the location from which the OS Image used to boot baremetal host machines can be downloaded by the metal3 cluster. |
| `unsupportedConfigOverrides` | `object` | UnsupportedConfigOverrides are site-specific overrides that are not officially supported in the Metal platform and may cause the deployment to fail. Carefully check the description of each field you modify to understand its implications for stability and upgradability of your cluster. When reporting a bug, please make sure to reproduce it with UnsupportedConfigOverrides set to nil. |
| `virtualMediaViaExternalNetwork` | `boolean` | VirtualMediaViaExternalNetwork flag when set to "true" allows for workers to boot via Virtual Media and contact metal3 over the External Network. When the flag is set to "false" (which is the default), virtual media deployments can still happen based on the configuration specified in the ProvisioningNetwork i.e when in Disabled mode, over the External Network and over Provisioning Network when in Managed mode. PXE deployments will always use the Provisioning Network and will not be affected by this flag. |
| `watchAllNamespaces` | `boolean` | WatchAllNamespaces provides a way to explicitly allow use of this Provisioning configuration across all Namespaces. It is an optional configuration which defaults to false and in that state will be used to provision baremetal hosts in only the openshift-machine-api namespace. When set to true, this provisioning configuration would be used for baremetal hosts across all namespaces. |

Show more

#### [13.1.2. .spec.preProvisioningOSDownloadURLs](#spec-preprovisioningosdownloadurls) Copy linkLink copied to clipboard!

Description
:   PreprovisioningOSDownloadURLs is set of CoreOS Live URLs that would be necessary to provision a worker either using virtual media or PXE.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `initramfsURL` | `string` | InitramfsURL Image URL to be used for PXE deployments |
| `isoURL` | `string` | IsoURL Image URL to be used for Live ISO deployments |
| `kernelURL` | `string` | KernelURL is an Image URL to be used for PXE deployments |
| `rootfsURL` | `string` | RootfsURL Image URL to be used for PXE deployments |

Show more

#### [13.1.3. .spec.prometheusExporter](#spec-prometheusexporter) Copy linkLink copied to clipboard!

Description
:   PrometheusExporter configures sensor data collection and Prometheus metrics export. When enabled, this configures Ironic to collect sensor data, deploys the ironic-prometheus-exporter container, and creates supporting resources (ServiceMonitor, Service ports) to expose hardware sensor metrics for Prometheus.

Type
:   `object`

Required
:   * `enabled`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `disableDefaultPrometheusRules` | `boolean` | DisableDefaultPrometheusRules controls whether default hardware health alerting rules should NOT be deployed alongside the prometheus exporter. When false (default), default prometheus rules are deployed. |
| `enabled` | `boolean` | Enabled controls whether sensor data collection is active. When true, configures Ironic to collect sensor data, deploys the ironic-prometheus-exporter container, and creates supporting resources. |
| `sensorCollectionInterval` | `integer` | SensorCollectionInterval defines how often (in seconds) sensor data is collected from BMCs using Ironic. Must be at least 60 seconds. |

Show more

#### [13.1.4. .spec.unsupportedConfigOverrides](#spec-unsupportedconfigoverrides) Copy linkLink copied to clipboard!

Description
:   UnsupportedConfigOverrides are site-specific overrides that are not officially supported in the Metal platform and may cause the deployment to fail. Carefully check the description of each field you modify to understand its implications for stability and upgradability of your cluster. When reporting a bug, please make sure to reproduce it with UnsupportedConfigOverrides set to nil.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ironicAgentImage` | `string` | Override for the IPA container image. The image must be based on openshift/ironic-agent-image of the same release as the cluster. After each cluster upgrade, it must be rebased and updated immediately, before any BareMetalHosts are enrolled, provisioned or deprovisioned. |

Show more

#### [13.1.5. .status](#status-10) Copy linkLink copied to clipboard!

Description
:   ProvisioningStatus defines the observed state of Provisioning

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions is a list of conditions and their status |
| `conditions[]` | `object` | OperatorCondition is just the standard condition fields. |
| `generations` | `array` | generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. |
| `generations[]` | `object` | GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made. |
| `latestAvailableRevision` | `integer` | latestAvailableRevision is the deploymentID of the most recent deployment |
| `observedGeneration` | `integer` | observedGeneration is the last generation change you’ve dealt with |
| `readyReplicas` | `integer` | readyReplicas indicates how many replicas are ready and at the desired state |
| `version` | `string` | version is the level this availability applies to |

Show more

#### [13.1.6. .status.conditions](#status-conditions-9) Copy linkLink copied to clipboard!

Description
:   conditions is a list of conditions and their status

Type
:   `array`

#### [13.1.7. .status.conditions[]](#status-conditions-10) Copy linkLink copied to clipboard!

Description
:   OperatorCondition is just the standard condition fields.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` |  |
| `reason` | `string` |  |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

Show more

#### [13.1.8. .status.generations](#status-generations) Copy linkLink copied to clipboard!

Description
:   generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.

Type
:   `array`

#### [13.1.9. .status.generations[]](#status-generations-2) Copy linkLink copied to clipboard!

Description
:   GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.

Type
:   `object`

Required
:   * `group`
    * `name`
    * `namespace`
    * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | group is the group of the thing you’re tracking |
| `hash` | `string` | hash is an optional field set for resources without generation that are content sensitive like secrets and configmaps |
| `lastGeneration` | `integer` | lastGeneration is the last generation of the workload controller involved |
| `name` | `string` | name is the name of the thing you’re tracking |
| `namespace` | `string` | namespace is where the thing you’re tracking is |
| `resource` | `string` | resource is the resource type of the thing you’re tracking |

Show more

### [13.2. API endpoints](#api-endpoints-12) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/metal3.io/v1alpha1/provisionings`

  + `DELETE`: delete collection of Provisioning
  + `GET`: list objects of kind Provisioning
  + `POST`: create a Provisioning
* `/apis/metal3.io/v1alpha1/provisionings/{name}`

  + `DELETE`: delete a Provisioning
  + `GET`: read the specified Provisioning
  + `PATCH`: partially update the specified Provisioning
  + `PUT`: replace the specified Provisioning
* `/apis/metal3.io/v1alpha1/provisionings/{name}/status`

  + `GET`: read status of the specified Provisioning
  + `PATCH`: partially update status of the specified Provisioning
  + `PUT`: replace status of the specified Provisioning

#### [13.2.1. /apis/metal3.io/v1alpha1/provisionings](#apismetal3-iov1alpha1provisionings) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Provisioning

Expand

Table 13.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Provisioning

Expand

Table 13.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProvisioningList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-ProvisioningList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Provisioning

Expand

Table 13.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 13.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 201 - Created | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 202 - Accepted | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.2. /apis/metal3.io/v1alpha1/provisionings/{name}](#apismetal3-iov1alpha1provisioningsname) Copy linkLink copied to clipboard!

Expand

Table 13.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Provisioning |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Provisioning

Expand

Table 13.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 13.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Provisioning

Expand

Table 13.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Provisioning

Expand

Table 13.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Provisioning

Expand

Table 13.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 13.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 201 - Created | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.3. /apis/metal3.io/v1alpha1/provisionings/{name}/status](#apismetal3-iov1alpha1provisioningsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 13.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Provisioning |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Provisioning

Expand

Table 13.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Provisioning

Expand

Table 13.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Provisioning

Expand

Table 13.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |  |

Show more

Expand

Table 13.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 201 - Created | [`Provisioning`](#provisioning-metal3-io-v1alpha1 "Chapter 13. Provisioning [metal3.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm139703733052944) Copy linkLink copied to clipboard!

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
