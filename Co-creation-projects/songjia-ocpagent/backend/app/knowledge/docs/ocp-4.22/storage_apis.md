---
title: "Storage APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/index
retrieved_at: 2026-09-05T05:42:58.232633+00:00
---

# Storage APIs

---

OpenShift Container Platform 4.22

## Reference guide for storage APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140350886283232)

**Abstract**

This document describes the OpenShift Container Platform storage API objects and their detailed specifications.

---

## [Chapter 1. Storage APIs](#storage-apis) Copy linkLink copied to clipboard!

### [1.1. CSIDriver [storage.k8s.io/v1]](#csidriver-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster. Kubernetes attach detach controller uses this object to determine whether attach is required. Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver objects are non-namespaced.

Type
:   `object`

### [1.2. CSINode [storage.k8s.io/v1]](#csinode-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn’t create this object. CSINode has an OwnerReference that points to the corresponding node object.

Type
:   `object`

### [1.3. CSIStorageCapacity [storage.k8s.io/v1]](#csistoragecapacity-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this describes the available capacity in a particular topology segment. This can be used when considering where to instantiate new PersistentVolumes.

    For example this can express things like: - StorageClass "standard" has "1234 GiB" available in "topology.kubernetes.io/zone=us-east1" - StorageClass "localssd" has "10 GiB" available in "kubernetes.io/hostname=knode-abc123"

    The following three cases all imply that no capacity is available for a certain combination: - no object exists with suitable topology and storage class name - such an object exists, but the capacity is unset - such an object exists, but the capacity is zero

    The producer of these objects can decide which approach is more suitable.

    They are consumed by the kube-scheduler when a CSI driver opts into capacity-aware scheduling with CSIDriverSpec.StorageCapacity. The scheduler compares the MaximumVolumeSize against the requested size of pending volumes to filter out unsuitable nodes. If MaximumVolumeSize is unset, it falls back to a comparison against the less precise Capacity. If that is also unset, the scheduler assumes that capacity is insufficient and tries some other node.

Type
:   `object`

### [1.4. PersistentVolume [v1]](#persistentvolume-v1-1) Copy linkLink copied to clipboard!

Description
:   PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes>

Type
:   `object`

### [1.5. PersistentVolumeClaim [v1]](#persistentvolumeclaim-v1-1) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaim is a user’s request for and claim to a persistent volume

Type
:   `object`

### [1.6. StorageClass [storage.k8s.io/v1]](#storageclass-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.

    StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.

Type
:   `object`

### [1.7. StorageState [migration.k8s.io/v1alpha1]](#storagestate-migration-k8s-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   The state of the storage of a specific resource.

Type
:   `object`

### [1.8. StorageVersionMigration [migration.k8s.io/v1alpha1]](#storageversionmigration-migration-k8s-iov1alpha1) Copy linkLink copied to clipboard!

Description
:   StorageVersionMigration represents a migration of stored data to the latest storage version.

Type
:   `object`

### [1.9. VolumeAttachment [storage.k8s.io/v1]](#volumeattachment-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

    VolumeAttachment objects are non-namespaced.

Type
:   `object`

### [1.10. VolumeAttributesClass [storage.k8s.io/v1]](#volumeattributesclass-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   VolumeAttributesClass represents a specification of mutable volume attributes defined by the CSI driver. The class can be specified during dynamic provisioning of PersistentVolumeClaims, and changed in the PersistentVolumeClaim spec after provisioning.

Type
:   `object`

### [1.11. VolumePopulator [populator.storage.k8s.io/v1beta1]](#volumepopulator-populator-storage-k8s-iov1beta1) Copy linkLink copied to clipboard!

Description
:   VolumePopulator represents the registration for a volume populator. VolumePopulators are cluster scoped.

Type
:   `object`

### [1.12. VolumeSnapshot [snapshot.storage.k8s.io/v1]](#volumesnapshot-snapshot-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshot is a user’s request for either creating a point-in-time snapshot of a persistent volume, or binding to a pre-existing snapshot.

Type
:   `object`

### [1.13. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]](#volumesnapshotclass-snapshot-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotClass specifies parameters that a underlying storage system uses when creating a volume snapshot. A specific VolumeSnapshotClass is used by specifying its name in a VolumeSnapshot object. VolumeSnapshotClasses are non-namespaced

Type
:   `object`

### [1.14. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]](#volumesnapshotcontent-snapshot-storage-k8s-iov1) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotContent represents the actual "on-disk" snapshot object in the underlying storage system

Type
:   `object`

## [Chapter 2. CSIDriver [storage.k8s.io/v1]](#csidriver-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster. Kubernetes attach detach controller uses this object to determine whether attach is required. Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver objects are non-namespaced.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata. metadata.Name indicates the name of the CSI driver that this object refers to; it MUST be the same name returned by the CSI GetPluginName() call for that driver. The driver name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | CSIDriverSpec is the specification of a CSIDriver. |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   CSIDriverSpec is the specification of a CSIDriver.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `attachRequired` | `boolean` | attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  This field is immutable. |
| `fsGroupPolicy` | `string` | fsGroupPolicy defines if the underlying volume supports changing ownership and permission of the volume before being mounted. Refer to the specific FSGroupPolicy values for additional details.  This field was immutable in Kubernetes < 1.29 and now is mutable.  Defaults to ReadWriteOnceWithFSType, which will examine each volume to determine if Kubernetes should modify ownership and permissions of the volume. With the default policy the defined fsGroup will only be applied if a fstype is defined and the volume’s access mode contains ReadWriteOnce. |
| `nodeAllocatableUpdatePeriodSeconds` | `integer` | nodeAllocatableUpdatePeriodSeconds specifies the interval between periodic updates of the CSINode allocatable capacity for this driver. When set, both periodic updates and updates triggered by capacity-related failures are enabled. If not set, no updates occur (neither periodic nor upon detecting capacity-related failures), and the allocatable.count remains static. The minimum allowed value for this field is 10 seconds.  This is a beta feature and requires the MutableCSINodeAllocatableCount feature gate to be enabled.  This field is mutable. |
| `podInfoOnMount` | `boolean` | podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations, if set to true. If set to false, pod information will not be passed on mount. Default is false.  The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext.  The following VolumeContext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. "csi.storage.k8s.io/pod.name": pod.Name "csi.storage.k8s.io/pod.namespace": pod.Namespace "csi.storage.k8s.io/pod.uid": string(pod.UID) "csi.storage.k8s.io/ephemeral": "true" if the volume is an ephemeral inline volume defined by a CSIVolumeSource, otherwise "false"  "csi.storage.k8s.io/ephemeral" is a new feature in Kubernetes 1.16. It is only required for drivers which support both the "Persistent" and "Ephemeral" VolumeLifecycleMode. Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn’t support this field, drivers can only support one mode when deployed on such a cluster and the deployment determines which mode that is, for example via a command line parameter of the driver.  This field was immutable in Kubernetes < 1.29 and now is mutable. |
| `requiresRepublish` | `boolean` | requiresRepublish indicates the CSI driver wants `NodePublishVolume` being periodically called to reflect any possible change in the mounted volume. This field defaults to false.  Note: After a successful initial NodePublishVolume call, subsequent calls to NodePublishVolume should only update the contents of the volume. New mount points will not be seen by a running container. |
| `seLinuxMount` | `boolean` | seLinuxMount specifies if the CSI driver supports "-o context" mount option.  When "true", the CSI driver must ensure that all volumes provided by this CSI driver can be mounted separately with different `-o context` options. This is typical for storage backends that provide volumes as filesystems on block devices or as independent shared volumes. Kubernetes will call NodeStage / NodePublish with "-o context=xyz" mount option when mounting a ReadWriteOncePod volume used in Pod that has explicitly set SELinux context. In the future, it may be expanded to other volume AccessModes. In any case, Kubernetes will ensure that the volume is mounted only with a single SELinux context.  When "false", Kubernetes won’t pass any special SELinux mount options to the driver. This is typical for volumes that represent subdirectories of a bigger shared filesystem.  Default is "false". |
| `serviceAccountTokenInSecrets` | `boolean` | serviceAccountTokenInSecrets is an opt-in for CSI drivers to indicate that service account tokens should be passed via the Secrets field in NodePublishVolumeRequest instead of the VolumeContext field. The CSI specification provides a dedicated Secrets field for sensitive information like tokens, which is the appropriate mechanism for handling credentials. This addresses security concerns where sensitive tokens were being logged as part of volume context.  When "true", kubelet will pass the tokens only in the Secrets field with the key "csi.storage.k8s.io/serviceAccount.tokens". The CSI driver must be updated to read tokens from the Secrets field instead of VolumeContext.  When "false" or not set, kubelet will pass the tokens in VolumeContext with the key "csi.storage.k8s.io/serviceAccount.tokens" (existing behavior). This maintains backward compatibility with existing CSI drivers.  This field can only be set when TokenRequests is configured. The API server will reject CSIDriver specs that set this field without TokenRequests.  Default behavior if unset is to pass tokens in the VolumeContext field. |
| `storageCapacity` | `boolean` | storageCapacity indicates that the CSI volume driver wants pod scheduling to consider the storage capacity that the driver deployment will report by creating CSIStorageCapacity objects with capacity information, if set to true.  The check can be enabled immediately when deploying a driver. In that case, provisioning new volumes with late binding will pause until the driver deployment has published some suitable CSIStorageCapacity object.  Alternatively, the driver can be deployed with the field unset or false and it can be flipped later when storage capacity information has been published.  This field was immutable in Kubernetes ⇐ 1.22 and now is mutable. |
| `tokenRequests` | `array` | tokenRequests indicates the CSI driver needs pods' service account tokens it is mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following VolumeContext: "csi.storage.k8s.io/serviceAccount.tokens": { "<audience>": { "token": <token>, "expirationTimestamp": <expiration timestamp in RFC3339>, }, …​ }  Note: Audience in each TokenRequest should be different and at most one token is empty string. To receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume periodically. |
| `tokenRequests[]` | `object` | TokenRequest contains parameters of a service account token. |
| `volumeLifecycleModes` | `array (string)` | volumeLifecycleModes defines what kind of volumes this CSI volume driver supports. The default if the list is empty is "Persistent", which is the usage defined by the CSI specification and implemented in Kubernetes via the usual PV/PVC mechanism.  The other mode is "Ephemeral". In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it is only going to get a NodePublishVolume call for such a volume.  For more information about implementing this mode, see <https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html> A driver can support one or more of these modes and more modes may be added in the future.  This field is beta. This field is immutable. |

Show more

#### [2.1.2. .spec.tokenRequests](#spec-tokenrequests) Copy linkLink copied to clipboard!

Description
:   tokenRequests indicates the CSI driver needs pods' service account tokens it is mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following VolumeContext: "csi.storage.k8s.io/serviceAccount.tokens": { "<audience>": { "token": <token>, "expirationTimestamp": <expiration timestamp in RFC3339>, }, …​ }

    Note: Audience in each TokenRequest should be different and at most one token is empty string. To receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume periodically.

Type
:   `array`

#### [2.1.3. .spec.tokenRequests[]](#spec-tokenrequests-2) Copy linkLink copied to clipboard!

Description
:   TokenRequest contains parameters of a service account token.

Type
:   `object`

Required
:   * `audience`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `audience` | `string` | audience is the intended audience of the token in "TokenRequestSpec". It will default to the audiences of kube apiserver. |
| `expirationSeconds` | `integer` | expirationSeconds is the duration of validity of the token in "TokenRequestSpec". It has the same default value of "ExpirationSeconds" in "TokenRequestSpec". |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/storage.k8s.io/v1/csidrivers`

  + `DELETE`: delete collection of CSIDriver
  + `GET`: list or watch objects of kind CSIDriver
  + `POST`: create a CSIDriver
* `/apis/storage.k8s.io/v1/watch/csidrivers`

  + `GET`: watch individual changes to a list of CSIDriver. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/csidrivers/{name}`

  + `DELETE`: delete a CSIDriver
  + `GET`: read the specified CSIDriver
  + `PATCH`: partially update the specified CSIDriver
  + `PUT`: replace the specified CSIDriver
* `/apis/storage.k8s.io/v1/watch/csidrivers/{name}`

  + `GET`: watch changes to an object of kind CSIDriver. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [2.2.1. /apis/storage.k8s.io/v1/csidrivers](#apisstorage-k8s-iov1csidrivers) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of CSIDriver

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
:   list or watch objects of kind CSIDriver

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIDriverList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSIDriverList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a CSIDriver

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
| `body` | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 2.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/storage.k8s.io/v1/watch/csidrivers](#apisstorage-k8s-iov1watchcsidrivers) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of CSIDriver. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 2.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/storage.k8s.io/v1/csidrivers/{name}](#apisstorage-k8s-iov1csidriversname) Copy linkLink copied to clipboard!

Expand

Table 2.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the CSIDriver |

Show more

HTTP method
:   `DELETE`

Description
:   delete a CSIDriver

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
| 200 - OK | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified CSIDriver

Expand

Table 2.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified CSIDriver

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
| 200 - OK | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified CSIDriver

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
| `body` | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSIDriver`](#csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/storage.k8s.io/v1/watch/csidrivers/{name}](#apisstorage-k8s-iov1watchcsidriversname) Copy linkLink copied to clipboard!

Expand

Table 2.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the CSIDriver |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind CSIDriver. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 2.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. CSINode [storage.k8s.io/v1]](#csinode-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn’t create this object. CSINode has an OwnerReference that points to the corresponding node object.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. metadata.name must be the Kubernetes node name. |
| `spec` | `object` | CSINodeSpec holds information about the specification of all CSI drivers installed on a node |

Show more

#### [3.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   CSINodeSpec holds information about the specification of all CSI drivers installed on a node

Type
:   `object`

Required
:   * `drivers`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `drivers` | `array` | drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty. |
| `drivers[]` | `object` | CSINodeDriver holds information about the specification of one CSI driver installed on a node |

Show more

#### [3.1.2. .spec.drivers](#spec-drivers) Copy linkLink copied to clipboard!

Description
:   drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.

Type
:   `array`

#### [3.1.3. .spec.drivers[]](#spec-drivers-2) Copy linkLink copied to clipboard!

Description
:   CSINodeDriver holds information about the specification of one CSI driver installed on a node

Type
:   `object`

Required
:   * `name`
    * `nodeID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allocatable` | `object` | VolumeNodeResources is a set of resource limits for scheduling of volumes. |
| `name` | `string` | name represents the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver. |
| `nodeID` | `string` | nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required. |
| `topologyKeys` | `array (string)` | topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology. |

Show more

#### [3.1.4. .spec.drivers[].allocatable](#spec-drivers-allocatable) Copy linkLink copied to clipboard!

Description
:   VolumeNodeResources is a set of resource limits for scheduling of volumes.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `count` | `integer` | count indicates the maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/storage.k8s.io/v1/csinodes`

  + `DELETE`: delete collection of CSINode
  + `GET`: list or watch objects of kind CSINode
  + `POST`: create a CSINode
* `/apis/storage.k8s.io/v1/watch/csinodes`

  + `GET`: watch individual changes to a list of CSINode. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/csinodes/{name}`

  + `DELETE`: delete a CSINode
  + `GET`: read the specified CSINode
  + `PATCH`: partially update the specified CSINode
  + `PUT`: replace the specified CSINode
* `/apis/storage.k8s.io/v1/watch/csinodes/{name}`

  + `GET`: watch changes to an object of kind CSINode. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [3.2.1. /apis/storage.k8s.io/v1/csinodes](#apisstorage-k8s-iov1csinodes) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of CSINode

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
:   list or watch objects of kind CSINode

Expand

Table 3.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSINodeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSINodeList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a CSINode

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
| `body` | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 3.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/storage.k8s.io/v1/watch/csinodes](#apisstorage-k8s-iov1watchcsinodes) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of CSINode. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/storage.k8s.io/v1/csinodes/{name}](#apisstorage-k8s-iov1csinodesname) Copy linkLink copied to clipboard!

Expand

Table 3.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the CSINode |

Show more

HTTP method
:   `DELETE`

Description
:   delete a CSINode

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
| 200 - OK | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified CSINode

Expand

Table 3.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified CSINode

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
| 200 - OK | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified CSINode

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
| `body` | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 3.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSINode`](#csinode-storage-k8s-io-v1 "Chapter 3. CSINode [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /apis/storage.k8s.io/v1/watch/csinodes/{name}](#apisstorage-k8s-iov1watchcsinodesname) Copy linkLink copied to clipboard!

Expand

Table 3.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the CSINode |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind CSINode. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]](#csistoragecapacity-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this describes the available capacity in a particular topology segment. This can be used when considering where to instantiate new PersistentVolumes.

    For example this can express things like: - StorageClass "standard" has "1234 GiB" available in "topology.kubernetes.io/zone=us-east1" - StorageClass "localssd" has "10 GiB" available in "kubernetes.io/hostname=knode-abc123"

    The following three cases all imply that no capacity is available for a certain combination: - no object exists with suitable topology and storage class name - such an object exists, but the capacity is unset - such an object exists, but the capacity is zero

    The producer of these objects can decide which approach is more suitable.

    They are consumed by the kube-scheduler when a CSI driver opts into capacity-aware scheduling with CSIDriverSpec.StorageCapacity. The scheduler compares the MaximumVolumeSize against the requested size of pending volumes to filter out unsuitable nodes. If MaximumVolumeSize is unset, it falls back to a comparison against the less precise Capacity. If that is also unset, the scheduler assumes that capacity is insufficient and tries some other node.

Type
:   `object`

Required
:   * `storageClassName`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `capacity` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `maximumVolumeSize` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | maximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity\_range.required\_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim. |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. The name has no particular meaning. It must be a DNS subdomain (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on the cluster, the recommendation is to use csisc-<uuid>, a generated name, or a reverse-domain name which ends with the unique CSI driver name.  Objects are namespaced.  More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `nodeTopology` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | nodeTopology defines which nodes have access to the storage for which capacity was reported. If not set, the storage is not accessible from any node in the cluster. If empty, the storage is accessible from all nodes. This field is immutable. |
| `storageClassName` | `string` | storageClassName represents the name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/storage.k8s.io/v1/csistoragecapacities`

  + `GET`: list or watch objects of kind CSIStorageCapacity
* `/apis/storage.k8s.io/v1/watch/csistoragecapacities`

  + `GET`: watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities`

  + `DELETE`: delete collection of CSIStorageCapacity
  + `GET`: list or watch objects of kind CSIStorageCapacity
  + `POST`: create a CSIStorageCapacity
* `/apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities`

  + `GET`: watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name}`

  + `DELETE`: delete a CSIStorageCapacity
  + `GET`: read the specified CSIStorageCapacity
  + `PATCH`: partially update the specified CSIStorageCapacity
  + `PUT`: replace the specified CSIStorageCapacity
* `/apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities/{name}`

  + `GET`: watch changes to an object of kind CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [4.2.1. /apis/storage.k8s.io/v1/csistoragecapacities](#apisstorage-k8s-iov1csistoragecapacities) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind CSIStorageCapacity

Expand

Table 4.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIStorageCapacityList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSIStorageCapacityList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/storage.k8s.io/v1/watch/csistoragecapacities](#apisstorage-k8s-iov1watchcsistoragecapacities) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities](#apisstorage-k8s-iov1namespacesnamespacecsistoragecapacities) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of CSIStorageCapacity

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
:   list or watch objects of kind CSIStorageCapacity

Expand

Table 4.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIStorageCapacityList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSIStorageCapacityList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a CSIStorageCapacity

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
| `body` | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 4.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.4. /apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities](#apisstorage-k8s-iov1watchnamespacesnamespacecsistoragecapacities) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.5. /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name}](#apisstorage-k8s-iov1namespacesnamespacecsistoragecapacitiesname) Copy linkLink copied to clipboard!

Expand

Table 4.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the CSIStorageCapacity |

Show more

HTTP method
:   `DELETE`

Description
:   delete a CSIStorageCapacity

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
:   read the specified CSIStorageCapacity

Expand

Table 4.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified CSIStorageCapacity

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
| 200 - OK | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified CSIStorageCapacity

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
| `body` | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 4.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 201 - Created | [`CSIStorageCapacity`](#csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.6. /apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities/{name}](#apisstorage-k8s-iov1watchnamespacesnamespacecsistoragecapacitiesname) Copy linkLink copied to clipboard!

Expand

Table 4.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the CSIStorageCapacity |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 4.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. PersistentVolume [v1]](#persistentvolume-v1) Copy linkLink copied to clipboard!

Description
:   PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes>

Type
:   `object`

### [5.1. Specification](#specification-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PersistentVolumeSpec is the specification of a persistent volume. |
| `status` | `object` | PersistentVolumeStatus is the current status of a persistent volume. |

Show more

#### [5.1.1. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeSpec is the specification of a persistent volume.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessModes` | `array (string)` | accessModes contains all ways the volume can be mounted. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes> |
| `awsElasticBlockStore` | `object` | Represents a Persistent Disk resource in AWS.  An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling. |
| `azureDisk` | `object` | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. |
| `azureFile` | `object` | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. |
| `capacity` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | capacity is the description of the persistent volume’s resources and capacity. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity> |
| `cephfs` | `object` | Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling. |
| `cinder` | `object` | Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling. |
| `claimRef` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| `csi` | `object` | Represents storage that is managed by an external CSI volume driver |
| `fc` | `object` | Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling. |
| `flexVolume` | `object` | FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin. |
| `flocker` | `object` | Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling. |
| `gcePersistentDisk` | `object` | Represents a Persistent Disk resource in Google Compute Engine.  A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling. |
| `glusterfs` | `object` | Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling. |
| `hostPath` | `object` | Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling. |
| `iscsi` | `object` | ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling. |
| `local` | `object` | Local represents directly-attached storage with node affinity |
| `mountOptions` | `array (string)` | mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options> |
| `nfs` | `object` | Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling. |
| `nodeAffinity` | `object` | VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from. |
| `persistentVolumeReclaimPolicy` | `string` | persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming>  Possible enum values: - `"Delete"` means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - `"Recycle"` means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - `"Retain"` means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain. |
| `photonPersistentDisk` | `object` | Represents a Photon Controller persistent disk resource. |
| `portworxVolume` | `object` | PortworxVolumeSource represents a Portworx volume resource. |
| `quobyte` | `object` | Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling. |
| `rbd` | `object` | Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling. |
| `scaleIO` | `object` | ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume |
| `storageClassName` | `string` | storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. |
| `storageos` | `object` | Represents a StorageOS persistent volume resource. |
| `volumeAttributesClassName` | `string` | Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. |
| `volumeMode` | `string` | volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.  Possible enum values: - `"Block"` means the volume will not be formatted with a filesystem and will remain a raw block device. - `"Filesystem"` means the volume will be or is formatted with a filesystem. |
| `vsphereVolume` | `object` | Represents a vSphere volume resource. |

Show more

#### [5.1.2. .spec.awsElasticBlockStore](#spec-awselasticblockstore) Copy linkLink copied to clipboard!

Description
:   Represents a Persistent Disk resource in AWS.

    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.

Type
:   `object`

Required
:   * `volumeID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). |
| `readOnly` | `boolean` | readOnly value true will force the readOnly setting in VolumeMounts. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `volumeID` | `string` | volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |

Show more

#### [5.1.3. .spec.azureDisk](#spec-azuredisk) Copy linkLink copied to clipboard!

Description
:   AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

Type
:   `object`

Required
:   * `diskName`
    * `diskURI`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cachingMode` | `string` | cachingMode is the Host Caching mode: None, Read Only, Read Write.  Possible enum values: - `"None"` - `"ReadOnly"` - `"ReadWrite"` |
| `diskName` | `string` | diskName is the Name of the data disk in the blob storage |
| `diskURI` | `string` | diskURI is the URI of data disk in the blob storage |
| `fsType` | `string` | fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `kind` | `string` | kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared  Possible enum values: - `"Dedicated"` - `"Managed"` - `"Shared"` |
| `readOnly` | `boolean` | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |

Show more

#### [5.1.4. .spec.azureFile](#spec-azurefile) Copy linkLink copied to clipboard!

Description
:   AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

Type
:   `object`

Required
:   * `secretName`
    * `shareName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretName` | `string` | secretName is the name of secret that contains Azure Storage Account Name and Key |
| `secretNamespace` | `string` | secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod |
| `shareName` | `string` | shareName is the azure Share Name |

Show more

#### [5.1.5. .spec.cephfs](#spec-cephfs) Copy linkLink copied to clipboard!

Description
:   Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.

Type
:   `object`

Required
:   * `monitors`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `monitors` | `array (string)` | monitors is Required: Monitors is a collection of Ceph monitors More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `path` | `string` | path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretFile` | `string` | secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `user` | `string` | user is Optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |

Show more

#### [5.1.6. .spec.cephfs.secretRef](#spec-cephfs-secretref) Copy linkLink copied to clipboard!

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

#### [5.1.7. .spec.cinder](#spec-cinder) Copy linkLink copied to clipboard!

Description
:   Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.

Type
:   `object`

Required
:   * `volumeID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `volumeID` | `string` | volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |

Show more

#### [5.1.8. .spec.cinder.secretRef](#spec-cinder-secretref) Copy linkLink copied to clipboard!

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

#### [5.1.9. .spec.claimRef](#spec-claimref) Copy linkLink copied to clipboard!

Description
:   ObjectReference contains enough information to let you inspect or modify the referred object.

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

#### [5.1.10. .spec.csi](#spec-csi) Copy linkLink copied to clipboard!

Description
:   Represents storage that is managed by an external CSI volume driver

Type
:   `object`

Required
:   * `driver`
    * `volumeHandle`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `controllerExpandSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `controllerPublishSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `driver` | `string` | driver is the name of the driver to use for this volume. Required. |
| `fsType` | `string` | fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". |
| `nodeExpandSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `nodePublishSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `nodeStageSecretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `readOnly` | `boolean` | readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes of the volume to publish. |
| `volumeHandle` | `string` | volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. |

Show more

#### [5.1.11. .spec.csi.controllerExpandSecretRef](#spec-csi-controllerexpandsecretref) Copy linkLink copied to clipboard!

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

#### [5.1.12. .spec.csi.controllerPublishSecretRef](#spec-csi-controllerpublishsecretref) Copy linkLink copied to clipboard!

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

#### [5.1.13. .spec.csi.nodeExpandSecretRef](#spec-csi-nodeexpandsecretref) Copy linkLink copied to clipboard!

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

#### [5.1.14. .spec.csi.nodePublishSecretRef](#spec-csi-nodepublishsecretref) Copy linkLink copied to clipboard!

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

#### [5.1.15. .spec.csi.nodeStageSecretRef](#spec-csi-nodestagesecretref) Copy linkLink copied to clipboard!

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

#### [5.1.16. .spec.fc](#spec-fc) Copy linkLink copied to clipboard!

Description
:   Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `lun` | `integer` | lun is Optional: FC target lun number |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `targetWWNs` | `array (string)` | targetWWNs is Optional: FC target worldwide names (WWNs) |
| `wwids` | `array (string)` | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. |

Show more

#### [5.1.17. .spec.flexVolume](#spec-flexvolume) Copy linkLink copied to clipboard!

Description
:   FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.

Type
:   `object`

Required
:   * `driver`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | driver is the name of the driver to use for this volume. |
| `fsType` | `string` | fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. |
| `options` | `object (string)` | options is Optional: this field holds extra command options if any. |
| `readOnly` | `boolean` | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |

Show more

#### [5.1.18. .spec.flexVolume.secretRef](#spec-flexvolume-secretref) Copy linkLink copied to clipboard!

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

#### [5.1.19. .spec.flocker](#spec-flocker) Copy linkLink copied to clipboard!

Description
:   Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `datasetName` | `string` | datasetName is Name of the dataset stored as metadata → name on the dataset for Flocker should be considered as deprecated |
| `datasetUUID` | `string` | datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset |

Show more

#### [5.1.20. .spec.gcePersistentDisk](#spec-gcepersistentdisk) Copy linkLink copied to clipboard!

Description
:   Represents a Persistent Disk resource in Google Compute Engine.

    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.

Type
:   `object`

Required
:   * `pdName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `pdName` | `string` | pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |

Show more

#### [5.1.21. .spec.glusterfs](#spec-glusterfs) Copy linkLink copied to clipboard!

Description
:   Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.

Type
:   `object`

Required
:   * `endpoints`
    * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `endpoints` | `string` | endpoints is the endpoint name that details Glusterfs topology. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `endpointsNamespace` | `string` | endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `path` | `string` | path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `readOnly` | `boolean` | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |

Show more

#### [5.1.22. .spec.hostPath](#spec-hostpath) Copy linkLink copied to clipboard!

Description
:   Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.

Type
:   `object`

Required
:   * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `path` | `string` | path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath> |
| `type` | `string` | type for HostPath Volume Defaults to "" More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>  Possible enum values: - `""` For backwards compatible, leave it empty if unset - `"BlockDevice"` A block device must exist at the given path - `"CharDevice"` A character device must exist at the given path - `"Directory"` A directory must exist at the given path - `"DirectoryOrCreate"` If nothing exists at the given path, an empty directory will be created there as needed with file mode 0755, having the same group and ownership with Kubelet. - `"File"` A file must exist at the given path - `"FileOrCreate"` If nothing exists at the given path, an empty file will be created there as needed with file mode 0644, having the same group and ownership with Kubelet. - `"Socket"` A UNIX socket must exist at the given path |

Show more

#### [5.1.23. .spec.iscsi](#spec-iscsi) Copy linkLink copied to clipboard!

Description
:   ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.

Type
:   `object`

Required
:   * `targetPortal`
    * `iqn`
    * `lun`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `chapAuthDiscovery` | `boolean` | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication |
| `chapAuthSession` | `boolean` | chapAuthSession defines whether support iSCSI Session CHAP authentication |
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#iscsi> |
| `initiatorName` | `string` | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. |
| `iqn` | `string` | iqn is Target iSCSI Qualified Name. |
| `iscsiInterface` | `string` | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). |
| `lun` | `integer` | lun is iSCSI Target Lun number. |
| `portals` | `array (string)` | portals is the iSCSI Target Portal List. The Portal is either an IP or ip\_addr:port if the port is other than default (typically TCP ports 860 and 3260). |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `targetPortal` | `string` | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip\_addr:port if the port is other than default (typically TCP ports 860 and 3260). |

Show more

#### [5.1.24. .spec.iscsi.secretRef](#spec-iscsi-secretref) Copy linkLink copied to clipboard!

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

#### [5.1.25. .spec.local](#spec-local) Copy linkLink copied to clipboard!

Description
:   Local represents directly-attached storage with node affinity

Type
:   `object`

Required
:   * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified. |
| `path` | `string` | path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, …​). |

Show more

#### [5.1.26. .spec.nfs](#spec-nfs) Copy linkLink copied to clipboard!

Description
:   Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.

Type
:   `object`

Required
:   * `server`
    * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `path` | `string` | path that is exported by the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `readOnly` | `boolean` | readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `server` | `string` | server is the hostname or IP address of the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |

Show more

#### [5.1.27. .spec.nodeAffinity](#spec-nodeaffinity) Copy linkLink copied to clipboard!

Description
:   VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `required` | `object` | A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms. |

Show more

#### [5.1.28. .spec.nodeAffinity.required](#spec-nodeaffinity-required) Copy linkLink copied to clipboard!

Description
:   A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.

Type
:   `object`

Required
:   * `nodeSelectorTerms`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nodeSelectorTerms` | `array` | Required. A list of node selector terms. The terms are ORed. |
| `nodeSelectorTerms[]` | `object` | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. |

Show more

#### [5.1.29. .spec.nodeAffinity.required.nodeSelectorTerms](#spec-nodeaffinity-required-nodeselectorterms) Copy linkLink copied to clipboard!

Description
:   Required. A list of node selector terms. The terms are ORed.

Type
:   `array`

#### [5.1.30. .spec.nodeAffinity.required.nodeSelectorTerms[]](#spec-nodeaffinity-required-nodeselectorterms-2) Copy linkLink copied to clipboard!

Description
:   A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchExpressions` | `array` | A list of node selector requirements by node’s labels. |
| `matchExpressions[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchFields` | `array` | A list of node selector requirements by node’s fields. |
| `matchFields[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

Show more

#### [5.1.31. .spec.nodeAffinity.required.nodeSelectorTerms[].matchExpressions](#spec-nodeaffinity-required-nodeselectorterms-matchexpressions) Copy linkLink copied to clipboard!

Description
:   A list of node selector requirements by node’s labels.

Type
:   `array`

#### [5.1.32. .spec.nodeAffinity.required.nodeSelectorTerms[].matchExpressions[]](#spec-nodeaffinity-required-nodeselectorterms-matchexpressions-2) Copy linkLink copied to clipboard!

Description
:   A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The label key that the selector applies to. |
| `operator` | `string` | Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.  Possible enum values: - `"DoesNotExist"` - `"Exists"` - `"Gt"` - `"In"` - `"Lt"` - `"NotIn"` |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. |

Show more

#### [5.1.33. .spec.nodeAffinity.required.nodeSelectorTerms[].matchFields](#spec-nodeaffinity-required-nodeselectorterms-matchfields) Copy linkLink copied to clipboard!

Description
:   A list of node selector requirements by node’s fields.

Type
:   `array`

#### [5.1.34. .spec.nodeAffinity.required.nodeSelectorTerms[].matchFields[]](#spec-nodeaffinity-required-nodeselectorterms-matchfields-2) Copy linkLink copied to clipboard!

Description
:   A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The label key that the selector applies to. |
| `operator` | `string` | Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.  Possible enum values: - `"DoesNotExist"` - `"Exists"` - `"Gt"` - `"In"` - `"Lt"` - `"NotIn"` |
| `values` | `array (string)` | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. |

Show more

#### [5.1.35. .spec.photonPersistentDisk](#spec-photonpersistentdisk) Copy linkLink copied to clipboard!

Description
:   Represents a Photon Controller persistent disk resource.

Type
:   `object`

Required
:   * `pdID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `pdID` | `string` | pdID is the ID that identifies Photon Controller persistent disk |

Show more

#### [5.1.36. .spec.portworxVolume](#spec-portworxvolume) Copy linkLink copied to clipboard!

Description
:   PortworxVolumeSource represents a Portworx volume resource.

Type
:   `object`

Required
:   * `volumeID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `volumeID` | `string` | volumeID uniquely identifies a Portworx volume |

Show more

#### [5.1.37. .spec.quobyte](#spec-quobyte) Copy linkLink copied to clipboard!

Description
:   Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.

Type
:   `object`

Required
:   * `registry`
    * `volume`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | group to map volume access to Default is no group |
| `readOnly` | `boolean` | readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. |
| `registry` | `string` | registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes |
| `tenant` | `string` | tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin |
| `user` | `string` | user to map volume access to Defaults to serivceaccount user |
| `volume` | `string` | volume is a string that references an already created Quobyte volume by name. |

Show more

#### [5.1.38. .spec.rbd](#spec-rbd) Copy linkLink copied to clipboard!

Description
:   Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.

Type
:   `object`

Required
:   * `monitors`
    * `image`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#rbd> |
| `image` | `string` | image is the rados image name. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `keyring` | `string` | keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `monitors` | `array (string)` | monitors is a collection of Ceph monitors. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `pool` | `string` | pool is the rados pool name. Default is rbd. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `user` | `string` | user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |

Show more

#### [5.1.39. .spec.rbd.secretRef](#spec-rbd-secretref) Copy linkLink copied to clipboard!

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

#### [5.1.40. .spec.scaleIO](#spec-scaleio) Copy linkLink copied to clipboard!

Description
:   ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume

Type
:   `object`

Required
:   * `gateway`
    * `system`
    * `secretRef`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs" |
| `gateway` | `string` | gateway is the host address of the ScaleIO API Gateway. |
| `protectionDomain` | `string` | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace |
| `sslEnabled` | `boolean` | sslEnabled is the flag to enable/disable SSL communication with Gateway, default false |
| `storageMode` | `string` | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. |
| `storagePool` | `string` | storagePool is the ScaleIO Storage Pool associated with the protection domain. |
| `system` | `string` | system is the name of the storage system as configured in ScaleIO. |
| `volumeName` | `string` | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. |

Show more

#### [5.1.41. .spec.scaleIO.secretRef](#spec-scaleio-secretref) Copy linkLink copied to clipboard!

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

#### [5.1.42. .spec.storageos](#spec-storageos) Copy linkLink copied to clipboard!

Description
:   Represents a StorageOS persistent volume resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| `volumeName` | `string` | volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace. |
| `volumeNamespace` | `string` | volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. |

Show more

#### [5.1.43. .spec.storageos.secretRef](#spec-storageos-secretref) Copy linkLink copied to clipboard!

Description
:   ObjectReference contains enough information to let you inspect or modify the referred object.

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

#### [5.1.44. .spec.vsphereVolume](#spec-vspherevolume) Copy linkLink copied to clipboard!

Description
:   Represents a vSphere volume resource.

Type
:   `object`

Required
:   * `volumePath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `storagePolicyID` | `string` | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. |
| `storagePolicyName` | `string` | storagePolicyName is the storage Policy Based Management (SPBM) profile name. |
| `volumePath` | `string` | volumePath is the path that identifies vSphere volume vmdk |

Show more

#### [5.1.45. .status](#status) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeStatus is the current status of a persistent volume.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastPhaseTransitionTime` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. |
| `message` | `string` | message is a human-readable message indicating details about why the volume is in this state. |
| `phase` | `string` | phase indicates if a volume is available, bound to a claim, or released by a claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase>  Possible enum values: - `"Available"` used for PersistentVolumes that are not yet bound Available volumes are held by the binder and matched to PersistentVolumeClaims - `"Bound"` used for PersistentVolumes that are bound - `"Failed"` used for PersistentVolumes that failed to be correctly recycled or deleted after being released from a claim - `"Pending"` used for PersistentVolumes that are not available - `"Released"` used for PersistentVolumes where the bound PersistentVolumeClaim was deleted released volumes must be recycled before becoming available again this phase is used by the persistent volume claim binder to signal to another process to reclaim the resource |
| `reason` | `string` | reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/persistentvolumes`

  + `DELETE`: delete collection of PersistentVolume
  + `GET`: list or watch objects of kind PersistentVolume
  + `POST`: create a PersistentVolume
* `/api/v1/watch/persistentvolumes`

  + `GET`: watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/persistentvolumes/{name}`

  + `DELETE`: delete a PersistentVolume
  + `GET`: read the specified PersistentVolume
  + `PATCH`: partially update the specified PersistentVolume
  + `PUT`: replace the specified PersistentVolume
* `/api/v1/watch/persistentvolumes/{name}`

  + `GET`: watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/api/v1/persistentvolumes/{name}/status`

  + `GET`: read status of the specified PersistentVolume
  + `PATCH`: partially update status of the specified PersistentVolume
  + `PUT`: replace status of the specified PersistentVolume

#### [5.2.1. /api/v1/persistentvolumes](#apiv1persistentvolumes) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PersistentVolume

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
:   list or watch objects of kind PersistentVolume

Expand

Table 5.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PersistentVolume

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
| `body` | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |  |

Show more

Expand

Table 5.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 201 - Created | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 202 - Accepted | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /api/v1/watch/persistentvolumes](#apiv1watchpersistentvolumes) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /api/v1/persistentvolumes/{name}](#apiv1persistentvolumesname) Copy linkLink copied to clipboard!

Expand

Table 5.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PersistentVolume |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PersistentVolume

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
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 202 - Accepted | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PersistentVolume

Expand

Table 5.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PersistentVolume

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
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 201 - Created | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PersistentVolume

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
| `body` | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |  |

Show more

Expand

Table 5.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 201 - Created | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.4. /api/v1/watch/persistentvolumes/{name}](#apiv1watchpersistentvolumesname) Copy linkLink copied to clipboard!

Expand

Table 5.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PersistentVolume |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.5. /api/v1/persistentvolumes/{name}/status](#apiv1persistentvolumesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 5.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PersistentVolume |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified PersistentVolume

Expand

Table 5.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified PersistentVolume

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
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 201 - Created | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified PersistentVolume

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
| `body` | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |  |

Show more

Expand

Table 5.25. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 201 - Created | [`PersistentVolume`](#persistentvolume-v1 "Chapter 5. PersistentVolume [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. PersistentVolumeClaim [v1]](#persistentvolumeclaim-v1) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaim is a user’s request for and claim to a persistent volume

Type
:   `object`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |
| `status` | `object` | PersistentVolumeClaimStatus is the current status of a persistent volume claim. |

Show more

#### [6.1.1. .spec](#spec-4) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessModes` | `array (string)` | accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1> |
| `dataSource` | `object` | TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace. |
| `dataSourceRef` | `object` | TypedObjectReference contains enough information to let you locate the typed referenced object |
| `resources` | `object` | VolumeResourceRequirements describes the storage resource requirements for a volume. |
| `selector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | selector is a label query over volumes to consider for binding. |
| `storageClassName` | `string` | storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1> |
| `volumeAttributesClassName` | `string` | volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string or nil value indicates that no VolumeAttributesClass will be applied to the claim. If the claim enters an Infeasible error state, this field can be reset to its previous value (including nil) to cancel the modification. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/> |
| `volumeMode` | `string` | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  Possible enum values: - `"Block"` means the volume will not be formatted with a filesystem and will remain a raw block device. - `"Filesystem"` means the volume will be or is formatted with a filesystem. |
| `volumeName` | `string` | volumeName is the binding reference to the PersistentVolume backing this claim. |

Show more

#### [6.1.2. .spec.dataSource](#spec-datasource) Copy linkLink copied to clipboard!

Description
:   TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

Type
:   `object`

Required
:   * `kind`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

Show more

#### [6.1.3. .spec.dataSourceRef](#spec-datasourceref) Copy linkLink copied to clipboard!

Description
:   TypedObjectReference contains enough information to let you locate the typed referenced object

Type
:   `object`

Required
:   * `kind`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |
| `namespace` | `string` | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |

Show more

#### [6.1.4. .spec.resources](#spec-resources) Copy linkLink copied to clipboard!

Description
:   VolumeResourceRequirements describes the storage resource requirements for a volume.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `limits` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [6.1.5. .status](#status-2) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaimStatus is the current status of a persistent volume claim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessModes` | `array (string)` | accessModes contains the actual access modes the volume backing the PVC has. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1> |
| `allocatedResourceStatuses` | `object (string)` | allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: \* Un-prefixed keys: - storage - the capacity of the volume. \* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states: - ControllerResizeInProgress: State set when resize controller starts resizing the volume in control-plane. - ControllerResizeFailed: State set when resize has failed in resize controller with a terminal error. - NodeResizePending: State set when resize controller has finished resizing the volume but further resizing of volume is needed on the node. - NodeResizeInProgress: State set when kubelet starts resizing the volume. - NodeResizeFailed: State set when resizing has failed in kubelet with a terminal error. Transient errors don’t set NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC. |
| `allocatedResources` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: \* Un-prefixed keys: - storage - the capacity of the volume. \* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC. |
| `capacity` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | capacity represents the actual resources of the underlying volume. |
| `conditions` | `array` | conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'. |
| `conditions[]` | `object` | PersistentVolumeClaimCondition contains details about state of pvc |
| `currentVolumeAttributesClassName` | `string` | currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim |
| `modifyVolumeStatus` | `object` | ModifyVolumeStatus represents the status object of ControllerModifyVolume operation |
| `phase` | `string` | phase represents the current phase of PersistentVolumeClaim.  Possible enum values: - `"Bound"` used for PersistentVolumeClaims that are bound - `"Lost"` used for PersistentVolumeClaims that lost their underlying PersistentVolume. The claim was bound to a PersistentVolume and this volume does not exist any longer and all data on it was lost. - `"Pending"` used for PersistentVolumeClaims that are not yet bound |

Show more

#### [6.1.6. .status.conditions](#status-conditions) Copy linkLink copied to clipboard!

Description
:   conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.

Type
:   `array`

#### [6.1.7. .status.conditions[]](#status-conditions-2) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaimCondition contains details about state of pvc

Type
:   `object`

Required
:   * `type`
    * `status`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastProbeTime` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastProbeTime is the time we probed the condition. |
| `lastTransitionTime` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastTransitionTime is the time the condition transitioned from one status to another. |
| `message` | `string` | message is the human-readable message indicating details about last transition. |
| `reason` | `string` | reason is a unique, this should be a short, machine understandable string that gives the reason for condition’s last transition. If it reports "Resizing" that means the underlying persistent volume is being resized. |
| `status` | `string` | Status is the status of the condition. Can be True, False, Unknown. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=state%20of%20pvc-,conditions.status,-(string)%2C%20required> |
| `type` | `string` | Type is the type of the condition. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about> |

Show more

#### [6.1.8. .status.modifyVolumeStatus](#status-modifyvolumestatus) Copy linkLink copied to clipboard!

Description
:   ModifyVolumeStatus represents the status object of ControllerModifyVolume operation

Type
:   `object`

Required
:   * `status`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `status` | `string` | status is the status of the ControllerModifyVolume operation. It can be in any of following states: - Pending Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing. - InProgress InProgress indicates that the volume is being modified. - Infeasible Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.  Possible enum values: - `"InProgress"` InProgress indicates that the volume is being modified - `"Infeasible"` Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified - `"Pending"` Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing |
| `targetVolumeAttributesClassName` | `string` | targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/persistentvolumeclaims`

  + `GET`: list or watch objects of kind PersistentVolumeClaim
* `/api/v1/watch/persistentvolumeclaims`

  + `GET`: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/persistentvolumeclaims`

  + `DELETE`: delete collection of PersistentVolumeClaim
  + `GET`: list or watch objects of kind PersistentVolumeClaim
  + `POST`: create a PersistentVolumeClaim
* `/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims`

  + `GET`: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}`

  + `DELETE`: delete a PersistentVolumeClaim
  + `GET`: read the specified PersistentVolumeClaim
  + `PATCH`: partially update the specified PersistentVolumeClaim
  + `PUT`: replace the specified PersistentVolumeClaim
* `/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}`

  + `GET`: watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status`

  + `GET`: read status of the specified PersistentVolumeClaim
  + `PATCH`: partially update status of the specified PersistentVolumeClaim
  + `PUT`: replace status of the specified PersistentVolumeClaim

#### [6.2.1. /api/v1/persistentvolumeclaims](#apiv1persistentvolumeclaims) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind PersistentVolumeClaim

Expand

Table 6.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeClaimList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /api/v1/watch/persistentvolumeclaims](#apiv1watchpersistentvolumeclaims) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.3. /api/v1/namespaces/{namespace}/persistentvolumeclaims](#apiv1namespacesnamespacepersistentvolumeclaims) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PersistentVolumeClaim

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
:   list or watch objects of kind PersistentVolumeClaim

Expand

Table 6.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeClaimList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PersistentVolumeClaim

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
| `body` | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |  |

Show more

Expand

Table 6.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 201 - Created | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 202 - Accepted | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.4. /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims](#apiv1watchnamespacesnamespacepersistentvolumeclaims) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 6.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.5. /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}](#apiv1namespacesnamespacepersistentvolumeclaimsname) Copy linkLink copied to clipboard!

Expand

Table 6.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PersistentVolumeClaim |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PersistentVolumeClaim

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
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 202 - Accepted | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PersistentVolumeClaim

Expand

Table 6.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PersistentVolumeClaim

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
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 201 - Created | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PersistentVolumeClaim

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
| `body` | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |  |

Show more

Expand

Table 6.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 201 - Created | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.6. /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}](#apiv1watchnamespacesnamespacepersistentvolumeclaimsname) Copy linkLink copied to clipboard!

Expand

Table 6.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PersistentVolumeClaim |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 6.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.7. /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status](#apiv1namespacesnamespacepersistentvolumeclaimsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 6.21. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PersistentVolumeClaim |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified PersistentVolumeClaim

Expand

Table 6.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified PersistentVolumeClaim

Expand

Table 6.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.24. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 201 - Created | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified PersistentVolumeClaim

Expand

Table 6.25. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.26. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |  |

Show more

Expand

Table 6.27. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 201 - Created | [`PersistentVolumeClaim`](#persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 7. StorageClass [storage.k8s.io/v1]](#storageclass-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.

    StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.

Type
:   `object`

Required
:   * `provisioner`

### [7.1. Specification](#specification-6) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowVolumeExpansion` | `boolean` | allowVolumeExpansion shows whether the storage class allow volume expand. |
| `allowedTopologies` | [`array (TopologySelectorTerm)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-TopologySelectorTerm) | allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `mountOptions` | `array (string)` | mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid. |
| `parameters` | `object (string)` | parameters holds the parameters for the provisioner that should create volumes of this storage class. |
| `provisioner` | `string` | provisioner indicates the type of the provisioner. |
| `reclaimPolicy` | `string` | reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete.  Possible enum values: - `"Delete"` means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - `"Recycle"` means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - `"Retain"` means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain. |
| `volumeBindingMode` | `string` | volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound. When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.  Possible enum values: - `"Immediate"` indicates that PersistentVolumeClaims should be immediately provisioned and bound. This is the default mode. - `"WaitForFirstConsumer"` indicates that PersistentVolumeClaims should not be provisioned and bound until the first Pod is created that references the PeristentVolumeClaim. The volume provisioning and binding will occur during Pod scheduing. |

Show more

### [7.2. API endpoints](#api-endpoints-6) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/storage.k8s.io/v1/storageclasses`

  + `DELETE`: delete collection of StorageClass
  + `GET`: list or watch objects of kind StorageClass
  + `POST`: create a StorageClass
* `/apis/storage.k8s.io/v1/watch/storageclasses`

  + `GET`: watch individual changes to a list of StorageClass. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/storageclasses/{name}`

  + `DELETE`: delete a StorageClass
  + `GET`: read the specified StorageClass
  + `PATCH`: partially update the specified StorageClass
  + `PUT`: replace the specified StorageClass
* `/apis/storage.k8s.io/v1/watch/storageclasses/{name}`

  + `GET`: watch changes to an object of kind StorageClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [7.2.1. /apis/storage.k8s.io/v1/storageclasses](#apisstorage-k8s-iov1storageclasses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of StorageClass

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
:   list or watch objects of kind StorageClass

Expand

Table 7.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-StorageClassList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a StorageClass

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
| `body` | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 7.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 201 - Created | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.2. /apis/storage.k8s.io/v1/watch/storageclasses](#apisstorage-k8s-iov1watchstorageclasses) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of StorageClass. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 7.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.3. /apis/storage.k8s.io/v1/storageclasses/{name}](#apisstorage-k8s-iov1storageclassesname) Copy linkLink copied to clipboard!

Expand

Table 7.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the StorageClass |

Show more

HTTP method
:   `DELETE`

Description
:   delete a StorageClass

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
| 200 - OK | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified StorageClass

Expand

Table 7.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified StorageClass

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
| 200 - OK | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 201 - Created | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified StorageClass

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
| `body` | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 7.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 201 - Created | [`StorageClass`](#storageclass-storage-k8s-io-v1 "Chapter 7. StorageClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.4. /apis/storage.k8s.io/v1/watch/storageclasses/{name}](#apisstorage-k8s-iov1watchstorageclassesname) Copy linkLink copied to clipboard!

Expand

Table 7.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the StorageClass |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind StorageClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 7.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 8. StorageState [migration.k8s.io/v1alpha1]](#storagestate-migration-k8s-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   The state of the storage of a specific resource.

Type
:   `object`

### [8.1. Specification](#specification-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of the storage state. |
| `status` | `object` | Status of the storage state. |

Show more

#### [8.1.1. .spec](#spec-5) Copy linkLink copied to clipboard!

Description
:   Specification of the storage state.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `resource` | `object` | The resource this storageState is about. |

Show more

#### [8.1.2. .spec.resource](#spec-resource) Copy linkLink copied to clipboard!

Description
:   The resource this storageState is about.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | The name of the group. |
| `resource` | `string` | The name of the resource. |

Show more

#### [8.1.3. .status](#status-3) Copy linkLink copied to clipboard!

Description
:   Status of the storage state.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `currentStorageVersionHash` | `string` | The hash value of the current storage version, as shown in the discovery document served by the API server. Storage Version is the version to which objects are converted to before persisted. |
| `lastHeartbeatTime` | `string` | LastHeartbeatTime is the last time the storage migration triggering controller checks the storage version hash of this resource in the discovery document and updates this field. |
| `persistedStorageVersionHashes` | `array (string)` | The hash values of storage versions that persisted instances of spec.resource might still be encoded in. "Unknown" is a valid value in the list, and is the default value. It is not safe to upgrade or downgrade to an apiserver binary that does not support all versions listed in this field, or if "Unknown" is listed. Once the storage version migration for this resource has completed, the value of this field is refined to only contain the currentStorageVersionHash. Once the apiserver has changed the storage version, the new storage version is appended to the list. |

Show more

### [8.2. API endpoints](#api-endpoints-7) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/migration.k8s.io/v1alpha1/storagestates`

  + `DELETE`: delete collection of StorageState
  + `GET`: list objects of kind StorageState
  + `POST`: create a StorageState
* `/apis/migration.k8s.io/v1alpha1/storagestates/{name}`

  + `DELETE`: delete a StorageState
  + `GET`: read the specified StorageState
  + `PATCH`: partially update the specified StorageState
  + `PUT`: replace the specified StorageState
* `/apis/migration.k8s.io/v1alpha1/storagestates/{name}/status`

  + `GET`: read status of the specified StorageState
  + `PATCH`: partially update status of the specified StorageState
  + `PUT`: replace status of the specified StorageState

#### [8.2.1. /apis/migration.k8s.io/v1alpha1/storagestates](#apismigration-k8s-iov1alpha1storagestates) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of StorageState

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
:   list objects of kind StorageState

Expand

Table 8.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageStateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-migration-v1alpha1-StorageStateList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a StorageState

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
| `body` | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |  |

Show more

Expand

Table 8.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 201 - Created | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 202 - Accepted | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.2. /apis/migration.k8s.io/v1alpha1/storagestates/{name}](#apismigration-k8s-iov1alpha1storagestatesname) Copy linkLink copied to clipboard!

Expand

Table 8.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the StorageState |

Show more

HTTP method
:   `DELETE`

Description
:   delete a StorageState

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
:   read the specified StorageState

Expand

Table 8.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified StorageState

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
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified StorageState

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
| `body` | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |  |

Show more

Expand

Table 8.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 201 - Created | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.3. /apis/migration.k8s.io/v1alpha1/storagestates/{name}/status](#apismigration-k8s-iov1alpha1storagestatesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 8.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the StorageState |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified StorageState

Expand

Table 8.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified StorageState

Expand

Table 8.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified StorageState

Expand

Table 8.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 8.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |  |

Show more

Expand

Table 8.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 201 - Created | [`StorageState`](#storagestate-migration-k8s-io-v1alpha1 "Chapter 8. StorageState [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]](#storageversionmigration-migration-k8s-io-v1alpha1) Copy linkLink copied to clipboard!

Description
:   StorageVersionMigration represents a migration of stored data to the latest storage version.

Type
:   `object`

### [9.1. Specification](#specification-8) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | Specification of the migration. |
| `status` | `object` | Status of the migration. |

Show more

#### [9.1.1. .spec](#spec-6) Copy linkLink copied to clipboard!

Description
:   Specification of the migration.

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `continueToken` | `string` | The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration. |
| `resource` | `object` | The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable. |

Show more

#### [9.1.2. .spec.resource](#spec-resource-2) Copy linkLink copied to clipboard!

Description
:   The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | The name of the group. |
| `resource` | `string` | The name of the resource. |
| `version` | `string` | The name of the version. |

Show more

#### [9.1.3. .status](#status-4) Copy linkLink copied to clipboard!

Description
:   Status of the migration.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | The latest available observations of the migration’s current state. |
| `conditions[]` | `object` | Describes the state of a migration at a certain point. |

Show more

#### [9.1.4. .status.conditions](#status-conditions-3) Copy linkLink copied to clipboard!

Description
:   The latest available observations of the migration’s current state.

Type
:   `array`

#### [9.1.5. .status.conditions[]](#status-conditions-4) Copy linkLink copied to clipboard!

Description
:   Describes the state of a migration at a certain point.

Type
:   `object`

Required
:   * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastUpdateTime` | `string` | The last time this condition was updated. |
| `message` | `string` | A human readable message indicating details about the transition. |
| `reason` | `string` | The reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of the condition. |

Show more

### [9.2. API endpoints](#api-endpoints-8) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/migration.k8s.io/v1alpha1/storageversionmigrations`

  + `DELETE`: delete collection of StorageVersionMigration
  + `GET`: list objects of kind StorageVersionMigration
  + `POST`: create a StorageVersionMigration
* `/apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}`

  + `DELETE`: delete a StorageVersionMigration
  + `GET`: read the specified StorageVersionMigration
  + `PATCH`: partially update the specified StorageVersionMigration
  + `PUT`: replace the specified StorageVersionMigration
* `/apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}/status`

  + `GET`: read status of the specified StorageVersionMigration
  + `PATCH`: partially update status of the specified StorageVersionMigration
  + `PUT`: replace status of the specified StorageVersionMigration

#### [9.2.1. /apis/migration.k8s.io/v1alpha1/storageversionmigrations](#apismigration-k8s-iov1alpha1storageversionmigrations) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of StorageVersionMigration

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
:   list objects of kind StorageVersionMigration

Expand

Table 9.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigrationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-migration-v1alpha1-StorageVersionMigrationList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a StorageVersionMigration

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
| `body` | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |  |

Show more

Expand

Table 9.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 201 - Created | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 202 - Accepted | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.2. /apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}](#apismigration-k8s-iov1alpha1storageversionmigrationsname) Copy linkLink copied to clipboard!

Expand

Table 9.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the StorageVersionMigration |

Show more

HTTP method
:   `DELETE`

Description
:   delete a StorageVersionMigration

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
:   read the specified StorageVersionMigration

Expand

Table 9.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified StorageVersionMigration

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
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified StorageVersionMigration

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
| `body` | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |  |

Show more

Expand

Table 9.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 201 - Created | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.3. /apis/migration.k8s.io/v1alpha1/storageversionmigrations/{name}/status](#apismigration-k8s-iov1alpha1storageversionmigrationsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 9.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the StorageVersionMigration |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified StorageVersionMigration

Expand

Table 9.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified StorageVersionMigration

Expand

Table 9.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified StorageVersionMigration

Expand

Table 9.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 9.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |  |

Show more

Expand

Table 9.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 201 - Created | [`StorageVersionMigration`](#storageversionmigration-migration-k8s-io-v1alpha1 "Chapter 9. StorageVersionMigration [migration.k8s.io/v1alpha1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 10. VolumeAttachment [storage.k8s.io/v1]](#volumeattachment-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

    VolumeAttachment objects are non-namespaced.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | VolumeAttachmentSpec is the specification of a VolumeAttachment request. |
| `status` | `object` | VolumeAttachmentStatus is the status of a VolumeAttachment request. |

Show more

#### [10.1.1. .spec](#spec-7) Copy linkLink copied to clipboard!

Description
:   VolumeAttachmentSpec is the specification of a VolumeAttachment request.

Type
:   `object`

Required
:   * `attacher`
    * `source`
    * `nodeName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `attacher` | `string` | attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). |
| `nodeName` | `string` | nodeName represents the node that the volume should be attached to. |
| `source` | `object` | VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set. |

Show more

#### [10.1.2. .spec.source](#spec-source) Copy linkLink copied to clipboard!

Description
:   VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `inlineVolumeSpec` | [`PersistentVolumeSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeSpec) | inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod’s inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod’s inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature. |
| `persistentVolumeName` | `string` | persistentVolumeName represents the name of the persistent volume to attach. |

Show more

#### [10.1.3. .status](#status-5) Copy linkLink copied to clipboard!

Description
:   VolumeAttachmentStatus is the status of a VolumeAttachment request.

Type
:   `object`

Required
:   * `attached`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `attachError` | `object` | VolumeError captures an error encountered during a volume operation. |
| `attached` | `boolean` | attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. |
| `attachmentMetadata` | `object (string)` | attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. |
| `detachError` | `object` | VolumeError captures an error encountered during a volume operation. |

Show more

#### [10.1.4. .status.attachError](#status-attacherror) Copy linkLink copied to clipboard!

Description
:   VolumeError captures an error encountered during a volume operation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `errorCode` | `integer` | errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.  This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set. |
| `message` | `string` | message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information. |
| `time` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | time represents the time the error was encountered. |

Show more

#### [10.1.5. .status.detachError](#status-detacherror) Copy linkLink copied to clipboard!

Description
:   VolumeError captures an error encountered during a volume operation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `errorCode` | `integer` | errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.  This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set. |
| `message` | `string` | message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information. |
| `time` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | time represents the time the error was encountered. |

Show more

### [10.2. API endpoints](#api-endpoints-9) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/storage.k8s.io/v1/volumeattachments`

  + `DELETE`: delete collection of VolumeAttachment
  + `GET`: list or watch objects of kind VolumeAttachment
  + `POST`: create a VolumeAttachment
* `/apis/storage.k8s.io/v1/watch/volumeattachments`

  + `GET`: watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/volumeattachments/{name}`

  + `DELETE`: delete a VolumeAttachment
  + `GET`: read the specified VolumeAttachment
  + `PATCH`: partially update the specified VolumeAttachment
  + `PUT`: replace the specified VolumeAttachment
* `/apis/storage.k8s.io/v1/watch/volumeattachments/{name}`

  + `GET`: watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/storage.k8s.io/v1/volumeattachments/{name}/status`

  + `GET`: read status of the specified VolumeAttachment
  + `PATCH`: partially update status of the specified VolumeAttachment
  + `PUT`: replace status of the specified VolumeAttachment

#### [10.2.1. /apis/storage.k8s.io/v1/volumeattachments](#apisstorage-k8s-iov1volumeattachments) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of VolumeAttachment

Expand

Table 10.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

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
:   list or watch objects of kind VolumeAttachment

Expand

Table 10.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachmentList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-VolumeAttachmentList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a VolumeAttachment

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
| `body` | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.2. /apis/storage.k8s.io/v1/watch/volumeattachments](#apisstorage-k8s-iov1watchvolumeattachments) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 10.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.3. /apis/storage.k8s.io/v1/volumeattachments/{name}](#apisstorage-k8s-iov1volumeattachmentsname) Copy linkLink copied to clipboard!

Expand

Table 10.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeAttachment |

Show more

HTTP method
:   `DELETE`

Description
:   delete a VolumeAttachment

Expand

Table 10.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 10.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified VolumeAttachment

Expand

Table 10.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified VolumeAttachment

Expand

Table 10.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified VolumeAttachment

Expand

Table 10.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.4. /apis/storage.k8s.io/v1/watch/volumeattachments/{name}](#apisstorage-k8s-iov1watchvolumeattachmentsname) Copy linkLink copied to clipboard!

Expand

Table 10.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeAttachment |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 10.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.5. /apis/storage.k8s.io/v1/volumeattachments/{name}/status](#apisstorage-k8s-iov1volumeattachmentsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 10.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeAttachment |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified VolumeAttachment

Expand

Table 10.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified VolumeAttachment

Expand

Table 10.21. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified VolumeAttachment

Expand

Table 10.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.24. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 10.25. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttachment`](#volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]](#volumeattributesclass-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   VolumeAttributesClass represents a specification of mutable volume attributes defined by the CSI driver. The class can be specified during dynamic provisioning of PersistentVolumeClaims, and changed in the PersistentVolumeClaim spec after provisioning.

Type
:   `object`

Required
:   * `driverName`

### [11.1. Specification](#specification-10) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `driverName` | `string` | Name of the CSI driver This field is immutable. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `parameters` | `object (string)` | parameters hold volume attributes defined by the CSI driver. These values are opaque to the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports changing these attributes on an existing volume, however the parameters field itself is immutable. To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.  This field is required and must contain at least one key/value pair. The keys cannot be empty, and the maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects invalid parameters, the target PersistentVolumeClaim will be set to an "Infeasible" state in the modifyVolumeStatus field. |

Show more

### [11.2. API endpoints](#api-endpoints-10) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/storage.k8s.io/v1/volumeattributesclasses`

  + `DELETE`: delete collection of VolumeAttributesClass
  + `GET`: list or watch objects of kind VolumeAttributesClass
  + `POST`: create a VolumeAttributesClass
* `/apis/storage.k8s.io/v1/watch/volumeattributesclasses`

  + `GET`: watch individual changes to a list of VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/storage.k8s.io/v1/volumeattributesclasses/{name}`

  + `DELETE`: delete a VolumeAttributesClass
  + `GET`: read the specified VolumeAttributesClass
  + `PATCH`: partially update the specified VolumeAttributesClass
  + `PUT`: replace the specified VolumeAttributesClass
* `/apis/storage.k8s.io/v1/watch/volumeattributesclasses/{name}`

  + `GET`: watch changes to an object of kind VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [11.2.1. /apis/storage.k8s.io/v1/volumeattributesclasses](#apisstorage-k8s-iov1volumeattributesclasses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of VolumeAttributesClass

Expand

Table 11.1. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

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
:   list or watch objects of kind VolumeAttributesClass

Expand

Table 11.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttributesClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-VolumeAttributesClassList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a VolumeAttributesClass

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
| `body` | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 11.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.2. /apis/storage.k8s.io/v1/watch/volumeattributesclasses](#apisstorage-k8s-iov1watchvolumeattributesclasses) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 11.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.3. /apis/storage.k8s.io/v1/volumeattributesclasses/{name}](#apisstorage-k8s-iov1volumeattributesclassesname) Copy linkLink copied to clipboard!

Expand

Table 11.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeAttributesClass |

Show more

HTTP method
:   `DELETE`

Description
:   delete a VolumeAttributesClass

Expand

Table 11.9. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 11.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified VolumeAttributesClass

Expand

Table 11.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified VolumeAttributesClass

Expand

Table 11.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified VolumeAttributesClass

Expand

Table 11.14. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.15. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 11.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeAttributesClass`](#volumeattributesclass-storage-k8s-io-v1 "Chapter 11. VolumeAttributesClass [storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.4. /apis/storage.k8s.io/v1/watch/volumeattributesclasses/{name}](#apisstorage-k8s-iov1watchvolumeattributesclassesname) Copy linkLink copied to clipboard!

Expand

Table 11.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeAttributesClass |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 11.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]](#volumepopulator-populator-storage-k8s-io-v1beta1) Copy linkLink copied to clipboard!

Description
:   VolumePopulator represents the registration for a volume populator. VolumePopulators are cluster scoped.

Type
:   `object`

Required
:   * `sourceKind`

### [12.1. Specification](#specification-11) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `sourceKind` | `object` | Kind of the data source this populator supports |

Show more

#### [12.1.1. .sourceKind](#sourcekind) Copy linkLink copied to clipboard!

Description
:   Kind of the data source this populator supports

Type
:   `object`

Required
:   * `group`
    * `kind`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` |  |
| `kind` | `string` |  |

Show more

### [12.2. API endpoints](#api-endpoints-11) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/populator.storage.k8s.io/v1beta1/volumepopulators`

  + `DELETE`: delete collection of VolumePopulator
  + `GET`: list objects of kind VolumePopulator
  + `POST`: create a VolumePopulator
* `/apis/populator.storage.k8s.io/v1beta1/volumepopulators/{name}`

  + `DELETE`: delete a VolumePopulator
  + `GET`: read the specified VolumePopulator
  + `PATCH`: partially update the specified VolumePopulator
  + `PUT`: replace the specified VolumePopulator

#### [12.2.1. /apis/populator.storage.k8s.io/v1beta1/volumepopulators](#apispopulator-storage-k8s-iov1beta1volumepopulators) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of VolumePopulator

Expand

Table 12.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind VolumePopulator

Expand

Table 12.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumePopulatorList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-populator-v1beta1-VolumePopulatorList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a VolumePopulator

Expand

Table 12.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 12.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 201 - Created | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 202 - Accepted | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.2. /apis/populator.storage.k8s.io/v1beta1/volumepopulators/{name}](#apispopulator-storage-k8s-iov1beta1volumepopulatorsname) Copy linkLink copied to clipboard!

Expand

Table 12.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumePopulator |

Show more

HTTP method
:   `DELETE`

Description
:   delete a VolumePopulator

Expand

Table 12.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 12.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified VolumePopulator

Expand

Table 12.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified VolumePopulator

Expand

Table 12.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified VolumePopulator

Expand

Table 12.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |  |

Show more

Expand

Table 12.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 201 - Created | [`VolumePopulator`](#volumepopulator-populator-storage-k8s-io-v1beta1 "Chapter 12. VolumePopulator [populator.storage.k8s.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]](#volumesnapshot-snapshot-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshot is a user’s request for either creating a point-in-time snapshot of a persistent volume, or binding to a pre-existing snapshot.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec defines the desired characteristics of a snapshot requested by a user. More info: <https://kubernetes.io/docs/concepts/storage/volume-snapshots#volumesnapshots> Required. |
| `status` | `object` | status represents the current information of a snapshot. Consumers must verify binding between VolumeSnapshot and VolumeSnapshotContent objects is successful (by validating that both VolumeSnapshot and VolumeSnapshotContent point at each other) before using this object. |

Show more

#### [13.1.1. .spec](#spec-8) Copy linkLink copied to clipboard!

Description
:   spec defines the desired characteristics of a snapshot requested by a user. More info: <https://kubernetes.io/docs/concepts/storage/volume-snapshots#volumesnapshots> Required.

Type
:   `object`

Required
:   * `source`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `source` | `object` | source specifies where a snapshot will be created from. This field is immutable after creation. Required. |
| `volumeSnapshotClassName` | `string` | VolumeSnapshotClassName is the name of the VolumeSnapshotClass requested by the VolumeSnapshot. VolumeSnapshotClassName may be left nil to indicate that the default SnapshotClass should be used. A given cluster may have multiple default Volume SnapshotClasses: one default per CSI Driver. If a VolumeSnapshot does not specify a SnapshotClass, VolumeSnapshotSource will be checked to figure out what the associated CSI Driver is, and the default VolumeSnapshotClass associated with that CSI Driver will be used. If more than one VolumeSnapshotClass exist for a given CSI Driver and more than one have been marked as default, CreateSnapshot will fail and generate an event. Empty string is not allowed for this field. |

Show more

#### [13.1.2. .spec.source](#spec-source-2) Copy linkLink copied to clipboard!

Description
:   source specifies where a snapshot will be created from. This field is immutable after creation. Required.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `persistentVolumeClaimName` | `string` | persistentVolumeClaimName specifies the name of the PersistentVolumeClaim object representing the volume from which a snapshot should be created. This PVC is assumed to be in the same namespace as the VolumeSnapshot object. This field should be set if the snapshot does not exists, and needs to be created. This field is immutable. |
| `volumeSnapshotContentName` | `string` | volumeSnapshotContentName specifies the name of a pre-existing VolumeSnapshotContent object representing an existing volume snapshot. This field should be set if the snapshot already exists and only needs a representation in Kubernetes. This field is immutable. |

Show more

#### [13.1.3. .status](#status-6) Copy linkLink copied to clipboard!

Description
:   status represents the current information of a snapshot. Consumers must verify binding between VolumeSnapshot and VolumeSnapshotContent objects is successful (by validating that both VolumeSnapshot and VolumeSnapshotContent point at each other) before using this object.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `boundVolumeSnapshotContentName` | `string` | boundVolumeSnapshotContentName is the name of the VolumeSnapshotContent object to which this VolumeSnapshot object intends to bind to. If not specified, it indicates that the VolumeSnapshot object has not been successfully bound to a VolumeSnapshotContent object yet. NOTE: To avoid possible security issues, consumers must verify binding between VolumeSnapshot and VolumeSnapshotContent objects is successful (by validating that both VolumeSnapshot and VolumeSnapshotContent point at each other) before using this object. |
| `creationTime` | `string` | creationTime is the timestamp when the point-in-time snapshot is taken by the underlying storage system. In dynamic snapshot creation case, this field will be filled in by the snapshot controller with the "creation\_time" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "creation\_time" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it. If not specified, it may indicate that the creation time of the snapshot is unknown. |
| `error` | `object` | error is the last observed error during snapshot creation, if any. This field could be helpful to upper level controllers(i.e., application controller) to decide whether they should continue on waiting for the snapshot to be created based on the type of error reported. The snapshot controller will keep retrying when an error occurs during the snapshot creation. Upon success, this error field will be cleared. |
| `readyToUse` | `boolean` | readyToUse indicates if the snapshot is ready to be used to restore a volume. In dynamic snapshot creation case, this field will be filled in by the snapshot controller with the "ready\_to\_use" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "ready\_to\_use" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it, otherwise, this field will be set to "True". If not specified, it means the readiness of a snapshot is unknown. |
| `restoreSize` | `integer-or-string` | restoreSize represents the minimum size of volume required to create a volume from this snapshot. In dynamic snapshot creation case, this field will be filled in by the snapshot controller with the "size\_bytes" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "size\_bytes" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it. When restoring a volume from this snapshot, the size of the volume MUST NOT be smaller than the restoreSize if it is specified, otherwise the restoration will fail. If not specified, it indicates that the size is unknown. |
| `volumeGroupSnapshotName` | `string` | VolumeGroupSnapshotName is the name of the VolumeGroupSnapshot of which this VolumeSnapshot is a part of. |

Show more

#### [13.1.4. .status.error](#status-error) Copy linkLink copied to clipboard!

Description
:   error is the last observed error during snapshot creation, if any. This field could be helpful to upper level controllers(i.e., application controller) to decide whether they should continue on waiting for the snapshot to be created based on the type of error reported. The snapshot controller will keep retrying when an error occurs during the snapshot creation. Upon success, this error field will be cleared.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `message` | `string` | message is a string detailing the encountered error during snapshot creation if specified. NOTE: message may be logged, and it should not contain sensitive information. |
| `time` | `string` | time is the timestamp when the error was encountered. |

Show more

### [13.2. API endpoints](#api-endpoints-12) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/snapshot.storage.k8s.io/v1/volumesnapshots`

  + `GET`: list objects of kind VolumeSnapshot
* `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots`

  + `DELETE`: delete collection of VolumeSnapshot
  + `GET`: list objects of kind VolumeSnapshot
  + `POST`: create a VolumeSnapshot
* `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}`

  + `DELETE`: delete a VolumeSnapshot
  + `GET`: read the specified VolumeSnapshot
  + `PATCH`: partially update the specified VolumeSnapshot
  + `PUT`: replace the specified VolumeSnapshot
* `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}/status`

  + `GET`: read status of the specified VolumeSnapshot
  + `PATCH`: partially update status of the specified VolumeSnapshot
  + `PUT`: replace status of the specified VolumeSnapshot

#### [13.2.1. /apis/snapshot.storage.k8s.io/v1/volumesnapshots](#apissnapshot-storage-k8s-iov1volumesnapshots) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind VolumeSnapshot

Expand

Table 13.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-snapshot-v1-VolumeSnapshotList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.2. /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots](#apissnapshot-storage-k8s-iov1namespacesnamespacevolumesnapshots) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of VolumeSnapshot

Expand

Table 13.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind VolumeSnapshot

Expand

Table 13.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-snapshot-v1-VolumeSnapshotList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a VolumeSnapshot

Expand

Table 13.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 13.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.3. /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}](#apissnapshot-storage-k8s-iov1namespacesnamespacevolumesnapshotsname) Copy linkLink copied to clipboard!

Expand

Table 13.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeSnapshot |

Show more

HTTP method
:   `DELETE`

Description
:   delete a VolumeSnapshot

Expand

Table 13.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 13.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified VolumeSnapshot

Expand

Table 13.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified VolumeSnapshot

Expand

Table 13.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified VolumeSnapshot

Expand

Table 13.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 13.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.4. /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}/status](#apissnapshot-storage-k8s-iov1namespacesnamespacevolumesnapshotsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 13.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeSnapshot |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified VolumeSnapshot

Expand

Table 13.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified VolumeSnapshot

Expand

Table 13.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified VolumeSnapshot

Expand

Table 13.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 13.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 13.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshot`](#volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]](#volumesnapshotclass-snapshot-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotClass specifies parameters that a underlying storage system uses when creating a volume snapshot. A specific VolumeSnapshotClass is used by specifying its name in a VolumeSnapshot object. VolumeSnapshotClasses are non-namespaced

Type
:   `object`

Required
:   * `deletionPolicy`
    * `driver`

### [14.1. Specification](#specification-13) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `deletionPolicy` | `string` | deletionPolicy determines whether a VolumeSnapshotContent created through the VolumeSnapshotClass should be deleted when its bound VolumeSnapshot is deleted. Supported values are "Retain" and "Delete". "Retain" means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are kept. "Delete" means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are deleted. Required. |
| `driver` | `string` | driver is the name of the storage driver that handles this VolumeSnapshotClass. Required. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `parameters` | `object (string)` | parameters is a key-value map with storage driver specific parameters for creating snapshots. These values are opaque to Kubernetes. |

Show more

### [14.2. API endpoints](#api-endpoints-13) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses`

  + `DELETE`: delete collection of VolumeSnapshotClass
  + `GET`: list objects of kind VolumeSnapshotClass
  + `POST`: create a VolumeSnapshotClass
* `/apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses/{name}`

  + `DELETE`: delete a VolumeSnapshotClass
  + `GET`: read the specified VolumeSnapshotClass
  + `PATCH`: partially update the specified VolumeSnapshotClass
  + `PUT`: replace the specified VolumeSnapshotClass

#### [14.2.1. /apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses](#apissnapshot-storage-k8s-iov1volumesnapshotclasses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of VolumeSnapshotClass

Expand

Table 14.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind VolumeSnapshotClass

Expand

Table 14.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-snapshot-v1-VolumeSnapshotClassList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a VolumeSnapshotClass

Expand

Table 14.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 14.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 14.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [14.2.2. /apis/snapshot.storage.k8s.io/v1/volumesnapshotclasses/{name}](#apissnapshot-storage-k8s-iov1volumesnapshotclassesname) Copy linkLink copied to clipboard!

Expand

Table 14.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeSnapshotClass |

Show more

HTTP method
:   `DELETE`

Description
:   delete a VolumeSnapshotClass

Expand

Table 14.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 14.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified VolumeSnapshotClass

Expand

Table 14.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified VolumeSnapshotClass

Expand

Table 14.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 14.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified VolumeSnapshotClass

Expand

Table 14.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 14.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 14.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshotClass`](#volumesnapshotclass-snapshot-storage-k8s-io-v1 "Chapter 14. VolumeSnapshotClass [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]](#volumesnapshotcontent-snapshot-storage-k8s-io-v1) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotContent represents the actual "on-disk" snapshot object in the underlying storage system

Type
:   `object`

Required
:   * `spec`

### [15.1. Specification](#specification-14) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec defines properties of a VolumeSnapshotContent created by the underlying storage system. Required. |
| `status` | `object` | status represents the current information of a snapshot. |

Show more

#### [15.1.1. .spec](#spec-9) Copy linkLink copied to clipboard!

Description
:   spec defines properties of a VolumeSnapshotContent created by the underlying storage system. Required.

Type
:   `object`

Required
:   * `deletionPolicy`
    * `driver`
    * `source`
    * `volumeSnapshotRef`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `deletionPolicy` | `string` | deletionPolicy determines whether this VolumeSnapshotContent and its physical snapshot on the underlying storage system should be deleted when its bound VolumeSnapshot is deleted. Supported values are "Retain" and "Delete". "Retain" means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are kept. "Delete" means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are deleted. For dynamically provisioned snapshots, this field will automatically be filled in by the CSI snapshotter sidecar with the "DeletionPolicy" field defined in the corresponding VolumeSnapshotClass. For pre-existing snapshots, users MUST specify this field when creating the VolumeSnapshotContent object. Required. |
| `driver` | `string` | driver is the name of the CSI driver used to create the physical snapshot on the underlying storage system. This MUST be the same as the name returned by the CSI GetPluginName() call for that driver. Required. |
| `source` | `object` | source specifies whether the snapshot is (or should be) dynamically provisioned or already exists, and just requires a Kubernetes object representation. This field is immutable after creation. Required. |
| `sourceVolumeMode` | `string` | SourceVolumeMode is the mode of the volume whose snapshot is taken. Can be either “Filesystem” or “Block”. If not specified, it indicates the source volume’s mode is unknown. This field is immutable. This field is an alpha field. |
| `volumeSnapshotClassName` | `string` | name of the VolumeSnapshotClass from which this snapshot was (or will be) created. Note that after provisioning, the VolumeSnapshotClass may be deleted or recreated with different set of values, and as such, should not be referenced post-snapshot creation. |
| `volumeSnapshotRef` | `object` | volumeSnapshotRef specifies the VolumeSnapshot object to which this VolumeSnapshotContent object is bound. VolumeSnapshot.Spec.VolumeSnapshotContentName field must reference to this VolumeSnapshotContent’s name for the bidirectional binding to be valid. For a pre-existing VolumeSnapshotContent object, name and namespace of the VolumeSnapshot object MUST be provided for binding to happen. This field is immutable after creation. Required. |

Show more

#### [15.1.2. .spec.source](#spec-source-3) Copy linkLink copied to clipboard!

Description
:   source specifies whether the snapshot is (or should be) dynamically provisioned or already exists, and just requires a Kubernetes object representation. This field is immutable after creation. Required.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `snapshotHandle` | `string` | snapshotHandle specifies the CSI "snapshot\_id" of a pre-existing snapshot on the underlying storage system for which a Kubernetes object representation was (or should be) created. This field is immutable. |
| `volumeHandle` | `string` | volumeHandle specifies the CSI "volume\_id" of the volume from which a snapshot should be dynamically taken from. This field is immutable. |

Show more

#### [15.1.3. .spec.volumeSnapshotRef](#spec-volumesnapshotref) Copy linkLink copied to clipboard!

Description
:   volumeSnapshotRef specifies the VolumeSnapshot object to which this VolumeSnapshotContent object is bound. VolumeSnapshot.Spec.VolumeSnapshotContentName field must reference to this VolumeSnapshotContent’s name for the bidirectional binding to be valid. For a pre-existing VolumeSnapshotContent object, name and namespace of the VolumeSnapshot object MUST be provided for binding to happen. This field is immutable after creation. Required.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

Show more

#### [15.1.4. .status](#status-7) Copy linkLink copied to clipboard!

Description
:   status represents the current information of a snapshot.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `creationTime` | `integer` | creationTime is the timestamp when the point-in-time snapshot is taken by the underlying storage system. In dynamic snapshot creation case, this field will be filled in by the CSI snapshotter sidecar with the "creation\_time" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "creation\_time" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it. If not specified, it indicates the creation time is unknown. The format of this field is a Unix nanoseconds time encoded as an int64. On Unix, the command `date +%s%N` returns the current time in nanoseconds since 1970-01-01 00:00:00 UTC. |
| `error` | `object` | error is the last observed error during snapshot creation, if any. Upon success after retry, this error field will be cleared. |
| `readyToUse` | `boolean` | readyToUse indicates if a snapshot is ready to be used to restore a volume. In dynamic snapshot creation case, this field will be filled in by the CSI snapshotter sidecar with the "ready\_to\_use" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "ready\_to\_use" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it, otherwise, this field will be set to "True". If not specified, it means the readiness of a snapshot is unknown. |
| `restoreSize` | `integer` | restoreSize represents the complete size of the snapshot in bytes. In dynamic snapshot creation case, this field will be filled in by the CSI snapshotter sidecar with the "size\_bytes" value returned from CSI "CreateSnapshot" gRPC call. For a pre-existing snapshot, this field will be filled with the "size\_bytes" value returned from the CSI "ListSnapshots" gRPC call if the driver supports it. When restoring a volume from this snapshot, the size of the volume MUST NOT be smaller than the restoreSize if it is specified, otherwise the restoration will fail. If not specified, it indicates that the size is unknown. |
| `snapshotHandle` | `string` | snapshotHandle is the CSI "snapshot\_id" of a snapshot on the underlying storage system. If not specified, it indicates that dynamic snapshot creation has either failed or it is still in progress. |
| `volumeGroupSnapshotHandle` | `string` | VolumeGroupSnapshotHandle is the CSI "group\_snapshot\_id" of a group snapshot on the underlying storage system. |

Show more

#### [15.1.5. .status.error](#status-error-2) Copy linkLink copied to clipboard!

Description
:   error is the last observed error during snapshot creation, if any. Upon success after retry, this error field will be cleared.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `message` | `string` | message is a string detailing the encountered error during snapshot creation if specified. NOTE: message may be logged, and it should not contain sensitive information. |
| `time` | `string` | time is the timestamp when the error was encountered. |

Show more

### [15.2. API endpoints](#api-endpoints-14) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/snapshot.storage.k8s.io/v1/volumesnapshotcontents`

  + `DELETE`: delete collection of VolumeSnapshotContent
  + `GET`: list objects of kind VolumeSnapshotContent
  + `POST`: create a VolumeSnapshotContent
* `/apis/snapshot.storage.k8s.io/v1/volumesnapshotcontents/{name}`

  + `DELETE`: delete a VolumeSnapshotContent
  + `GET`: read the specified VolumeSnapshotContent
  + `PATCH`: partially update the specified VolumeSnapshotContent
  + `PUT`: replace the specified VolumeSnapshotContent
* `/apis/snapshot.storage.k8s.io/v1/volumesnapshotcontents/{name}/status`

  + `GET`: read status of the specified VolumeSnapshotContent
  + `PATCH`: partially update status of the specified VolumeSnapshotContent
  + `PUT`: replace status of the specified VolumeSnapshotContent

#### [15.2.1. /apis/snapshot.storage.k8s.io/v1/volumesnapshotcontents](#apissnapshot-storage-k8s-iov1volumesnapshotcontents) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of VolumeSnapshotContent

Expand

Table 15.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind VolumeSnapshotContent

Expand

Table 15.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContentList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-snapshot-v1-VolumeSnapshotContentList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a VolumeSnapshotContent

Expand

Table 15.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 15.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 202 - Accepted | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [15.2.2. /apis/snapshot.storage.k8s.io/v1/volumesnapshotcontents/{name}](#apissnapshot-storage-k8s-iov1volumesnapshotcontentsname) Copy linkLink copied to clipboard!

Expand

Table 15.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeSnapshotContent |

Show more

HTTP method
:   `DELETE`

Description
:   delete a VolumeSnapshotContent

Expand

Table 15.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 15.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified VolumeSnapshotContent

Expand

Table 15.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified VolumeSnapshotContent

Expand

Table 15.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified VolumeSnapshotContent

Expand

Table 15.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 15.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [15.2.3. /apis/snapshot.storage.k8s.io/v1/volumesnapshotcontents/{name}/status](#apissnapshot-storage-k8s-iov1volumesnapshotcontentsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 15.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the VolumeSnapshotContent |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified VolumeSnapshotContent

Expand

Table 15.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified VolumeSnapshotContent

Expand

Table 15.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified VolumeSnapshotContent

Expand

Table 15.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |  |

Show more

Expand

Table 15.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 201 - Created | [`VolumeSnapshotContent`](#volumesnapshotcontent-snapshot-storage-k8s-io-v1 "Chapter 15. VolumeSnapshotContent [snapshot.storage.k8s.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140350886283232) Copy linkLink copied to clipboard!

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
