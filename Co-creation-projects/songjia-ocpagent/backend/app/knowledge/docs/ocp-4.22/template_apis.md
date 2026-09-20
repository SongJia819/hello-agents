---
title: "Template APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/index
retrieved_at: 2026-09-05T05:43:00.460894+00:00
---

# Template APIs

---

OpenShift Container Platform 4.22

## Reference guide for template APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140170832687904)

**Abstract**

This document describes the OpenShift Container Platform template API objects and their detailed specifications.

---

## [Chapter 1. Template APIs](#template-apis) Copy linkLink copied to clipboard!

### [1.1. BrokerTemplateInstance [template.openshift.io/v1]](#brokertemplateinstance-template-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   BrokerTemplateInstance holds the service broker-related state associated with a TemplateInstance. BrokerTemplateInstance is part of an experimental API.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. PodTemplate [v1]](#podtemplate-v1-1) Copy linkLink copied to clipboard!

Description
:   PodTemplate describes a template for creating copies of a predefined pod.

Type
:   `object`

### [1.3. Template [template.openshift.io/v1]](#template-template-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Template contains the inputs needed to produce a Config.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. TemplateInstance [template.openshift.io/v1]](#templateinstance-template-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   TemplateInstance requests and records the instantiation of a Template. TemplateInstance is part of an experimental API.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

## [Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]](#brokertemplateinstance-template-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   BrokerTemplateInstance holds the service broker-related state associated with a TemplateInstance. BrokerTemplateInstance is part of an experimental API.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | BrokerTemplateInstanceSpec describes the state of a BrokerTemplateInstance. |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   BrokerTemplateInstanceSpec describes the state of a BrokerTemplateInstance.

Type
:   `object`

Required
:   * `templateInstance`
    * `secret`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `bindingIDs` | `array (string)` | bindingIDs is a list of 'binding\_id’s provided during successive bind calls to the template service broker. |
| `secret` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | secret is a reference to a Secret object residing in a namespace, containing the necessary template parameters. |
| `templateInstance` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | templateInstance is a reference to a TemplateInstance object residing in a namespace. |

Show more

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/template.openshift.io/v1/brokertemplateinstances`

  + `DELETE`: delete collection of BrokerTemplateInstance
  + `GET`: list or watch objects of kind BrokerTemplateInstance
  + `POST`: create a BrokerTemplateInstance
* `/apis/template.openshift.io/v1/watch/brokertemplateinstances`

  + `GET`: watch individual changes to a list of BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/template.openshift.io/v1/brokertemplateinstances/{name}`

  + `DELETE`: delete a BrokerTemplateInstance
  + `GET`: read the specified BrokerTemplateInstance
  + `PATCH`: partially update the specified BrokerTemplateInstance
  + `PUT`: replace the specified BrokerTemplateInstance
* `/apis/template.openshift.io/v1/watch/brokertemplateinstances/{name}`

  + `GET`: watch changes to an object of kind BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [2.2.1. /apis/template.openshift.io/v1/brokertemplateinstances](#apistemplate-openshift-iov1brokertemplateinstances) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of BrokerTemplateInstance

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
:   list or watch objects of kind BrokerTemplateInstance

Expand

Table 2.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BrokerTemplateInstanceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-BrokerTemplateInstanceList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a BrokerTemplateInstance

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
| `body` | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 202 - Accepted | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/template.openshift.io/v1/watch/brokertemplateinstances](#apistemplate-openshift-iov1watchbrokertemplateinstances) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 2.7. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/template.openshift.io/v1/brokertemplateinstances/{name}](#apistemplate-openshift-iov1brokertemplateinstancesname) Copy linkLink copied to clipboard!

Expand

Table 2.8. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the BrokerTemplateInstance |

Show more

HTTP method
:   `DELETE`

Description
:   delete a BrokerTemplateInstance

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
:   read the specified BrokerTemplateInstance

Expand

Table 2.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified BrokerTemplateInstance

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
| 200 - OK | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified BrokerTemplateInstance

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
| `body` | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`BrokerTemplateInstance`](#brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.4. /apis/template.openshift.io/v1/watch/brokertemplateinstances/{name}](#apistemplate-openshift-iov1watchbrokertemplateinstancesname) Copy linkLink copied to clipboard!

Expand

Table 2.17. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the BrokerTemplateInstance |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 2.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. PodTemplate [v1]](#podtemplate-v1) Copy linkLink copied to clipboard!

Description
:   PodTemplate describes a template for creating copies of a predefined pod.

Type
:   `object`

### [3.1. Specification](#specification-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `template` | `object` | PodTemplateSpec describes the data a pod should have when created from a template |

Show more

#### [3.1.1. .template](#template) Copy linkLink copied to clipboard!

Description
:   PodTemplateSpec describes the data a pod should have when created from a template

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PodSpec is a description of a pod. |

Show more

#### [3.1.2. .template.spec](#template-spec) Copy linkLink copied to clipboard!

Description
:   PodSpec is a description of a pod.

Type
:   `object`

Required
:   * `containers`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `activeDeadlineSeconds` | `integer` | Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer. |
| `affinity` | `object` | Affinity is a group of affinity scheduling rules. |
| `automountServiceAccountToken` | `boolean` | AutomountServiceAccountToken indicates whether a service account token should be automatically mounted. |
| `containers` | `array` | List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. |
| `containers[]` | `object` | A single application container that you want to run within a pod. |
| `dnsConfig` | `object` | PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy. |
| `dnsPolicy` | `string` | Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.  Possible enum values: - `"ClusterFirst"` indicates that the pod should use cluster DNS first unless hostNetwork is true, if it is available, then fall back on the default (as determined by kubelet) DNS settings. - `"ClusterFirstWithHostNet"` indicates that the pod should use cluster DNS first, if it is available, then fall back on the default (as determined by kubelet) DNS settings. - `"Default"` indicates that the pod should use the default (as determined by kubelet) DNS settings. - `"None"` indicates that the pod should use empty DNS settings. DNS parameters such as nameservers and search paths should be defined via DNSConfig. |
| `enableServiceLinks` | `boolean` | EnableServiceLinks indicates whether information about services should be injected into pod’s environment variables, matching the syntax of Docker links. Optional: Defaults to true. |
| `ephemeralContainers` | `array` | List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod’s ephemeralcontainers subresource. |
| `ephemeralContainers[]` | `object` | An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.  To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted. |
| `hostAliases` | `array` | HostAliases is an optional list of hosts and IPs that will be injected into the pod’s hosts file if specified. |
| `hostAliases[]` | `object` | HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file. |
| `hostIPC` | `boolean` | Use the host’s ipc namespace. Optional: Default to false. |
| `hostNetwork` | `boolean` | Host networking requested for this pod. Use the host’s network namespace. When using HostNetwork you should specify ports so the scheduler is aware. When `hostNetwork` is true, specified `hostPort` fields in port definitions must match `containerPort`, and unspecified `hostPort` fields in port definitions are defaulted to match `containerPort`. Default to false. |
| `hostPID` | `boolean` | Use the host’s pid namespace. Optional: Default to false. |
| `hostUsers` | `boolean` | Use the host’s user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP\_SYS\_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature. |
| `hostname` | `string` | Specifies the hostname of the Pod If not specified, the pod’s hostname will be set to a system-defined value. |
| `hostnameOverride` | `string` | HostnameOverride specifies an explicit override for the pod’s hostname as perceived by the pod. This field only specifies the pod’s hostname and does not affect its DNS records. When this field is set to a non-empty string: - It takes precedence over the values set in `hostname` and `subdomain`. - The Pod’s hostname will be set to this value. - `setHostnameAsFQDN` must be nil or set to false. - `hostNetwork` must be set to false.  This field must be a valid DNS subdomain as defined in RFC 1123 and contain at most 64 characters. Requires the HostnameOverride feature gate to be enabled. |
| `imagePullSecrets` | `array` | ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: <https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod> |
| `imagePullSecrets[]` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `initContainers` | `array` | List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| `initContainers[]` | `object` | A single application container that you want to run within a pod. |
| `nodeName` | `string` | NodeName indicates in which node this pod is scheduled. If empty, this pod is a candidate for scheduling by the scheduler defined in schedulerName. Once this field is set, the kubelet for this node becomes responsible for the lifecycle of this pod. This field should not be used to express a desire for the pod to be scheduled on a specific node. <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename> |
| `nodeSelector` | `object (string)` | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node’s labels for the pod to be scheduled on that node. More info: <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/> |
| `os` | `object` | PodOS defines the OS parameters of a pod. |
| `overhead` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: <https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md> |
| `preemptionPolicy` | `string` | PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.  Possible enum values: - `"Never"` means that pod never preempts other pods with lower priority. - `"PreemptLowerPriority"` means that pod can preempt other pods with lower priority. |
| `priority` | `integer` | The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. |
| `priorityClassName` | `string` | If specified, indicates the pod’s priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default. |
| `readinessGates` | `array` | If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: <https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates> |
| `readinessGates[]` | `object` | PodReadinessGate contains the reference to a pod condition |
| `resourceClaims` | `array` | ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.  This is a stable field but requires that the DynamicResourceAllocation feature gate is enabled.  This field is immutable. |
| `resourceClaims[]` | `object` | PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.  It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name. |
| `resources` | `object` | ResourceRequirements describes the compute resource requirements. |
| `restartPolicy` | `string` | Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy>  Possible enum values: - `"Always"` - `"Never"` - `"OnFailure"` |
| `runtimeClassName` | `string` | RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod. If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: <https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class> |
| `schedulerName` | `string` | If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler. |
| `schedulingGates` | `array` | SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.  SchedulingGates can only be set at pod creation time, and be removed only afterwards. |
| `schedulingGates[]` | `object` | PodSchedulingGate is associated to a Pod to guard its scheduling. |
| `securityContext` | `object` | PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext. Field values of container.securityContext take precedence over field values of PodSecurityContext. |
| `serviceAccount` | `string` | DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead. |
| `serviceAccountName` | `string` | ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/> |
| `setHostnameAsFQDN` | `boolean` | If true the pod’s hostname will be configured as the pod’s FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false. |
| `shareProcessNamespace` | `boolean` | Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. |
| `subdomain` | `string` | If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all. |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds. |
| `tolerations` | `array` | If specified, the pod’s tolerations. |
| `tolerations[]` | `object` | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |
| `topologySpreadConstraints` | `array` | TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed. |
| `topologySpreadConstraints[]` | `object` | TopologySpreadConstraint specifies how to spread matching pods among the given topology. |
| `volumes` | `array` | List of volumes that can be mounted by containers belonging to the pod. More info: <https://kubernetes.io/docs/concepts/storage/volumes> |
| `volumes[]` | `object` | Volume represents a named volume in a pod that may be accessed by any container in the pod. |
| `workloadRef` | `object` | WorkloadReference identifies the Workload object and PodGroup membership that a Pod belongs to. The scheduler uses this information to apply workload-aware scheduling semantics. |

Show more

#### [3.1.3. .template.spec.affinity](#template-spec-affinity) Copy linkLink copied to clipboard!

Description
:   Affinity is a group of affinity scheduling rules.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nodeAffinity` | `object` | Node affinity is a group of node affinity scheduling rules. |
| `podAffinity` | `object` | Pod affinity is a group of inter pod affinity scheduling rules. |
| `podAntiAffinity` | `object` | Pod anti affinity is a group of inter pod anti affinity scheduling rules. |

Show more

#### [3.1.4. .template.spec.affinity.nodeAffinity](#template-spec-affinity-nodeaffinity) Copy linkLink copied to clipboard!

Description
:   Node affinity is a group of node affinity scheduling rules.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op). |
| `requiredDuringSchedulingIgnoredDuringExecution` | `object` | A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms. |

Show more

#### [3.1.5. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution) Copy linkLink copied to clipboard!

Description
:   The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.

Type
:   `array`

#### [3.1.6. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[]](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution-2) Copy linkLink copied to clipboard!

Description
:   An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

Type
:   `object`

Required
:   * `weight`
    * `preference`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `preference` | `object` | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. |
| `weight` | `integer` | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. |

Show more

#### [3.1.7. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution-preference) Copy linkLink copied to clipboard!

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

#### [3.1.8. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchExpressions](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution-preference-matchexpressions) Copy linkLink copied to clipboard!

Description
:   A list of node selector requirements by node’s labels.

Type
:   `array`

#### [3.1.9. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchExpressions[]](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution-preference-matchexpressions-2) Copy linkLink copied to clipboard!

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

#### [3.1.10. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchFields](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution-preference-matchfields) Copy linkLink copied to clipboard!

Description
:   A list of node selector requirements by node’s fields.

Type
:   `array`

#### [3.1.11. .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchFields[]](#template-spec-affinity-nodeaffinity-preferredduringschedulingignoredduringexecution-preference-matchfields-2) Copy linkLink copied to clipboard!

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

#### [3.1.12. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution) Copy linkLink copied to clipboard!

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

#### [3.1.13. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution-nodeselectorterms) Copy linkLink copied to clipboard!

Description
:   Required. A list of node selector terms. The terms are ORed.

Type
:   `array`

#### [3.1.14. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[]](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution-nodeselectorterms-2) Copy linkLink copied to clipboard!

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

#### [3.1.15. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchExpressions](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution-nodeselectorterms-matchexpressions) Copy linkLink copied to clipboard!

Description
:   A list of node selector requirements by node’s labels.

Type
:   `array`

#### [3.1.16. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchExpressions[]](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution-nodeselectorterms-matchexpressions-2) Copy linkLink copied to clipboard!

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

#### [3.1.17. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchFields](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution-nodeselectorterms-matchfields) Copy linkLink copied to clipboard!

Description
:   A list of node selector requirements by node’s fields.

Type
:   `array`

#### [3.1.18. .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchFields[]](#template-spec-affinity-nodeaffinity-requiredduringschedulingignoredduringexecution-nodeselectorterms-matchfields-2) Copy linkLink copied to clipboard!

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

#### [3.1.19. .template.spec.affinity.podAffinity](#template-spec-affinity-podaffinity) Copy linkLink copied to clipboard!

Description
:   Pod affinity is a group of inter pod affinity scheduling rules.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) |
| `requiredDuringSchedulingIgnoredDuringExecution` | `array` | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. |
| `requiredDuringSchedulingIgnoredDuringExecution[]` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running |

Show more

#### [3.1.20. .template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution](#template-spec-affinity-podaffinity-preferredduringschedulingignoredduringexecution) Copy linkLink copied to clipboard!

Description
:   The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

Type
:   `array`

#### [3.1.21. .template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[]](#template-spec-affinity-podaffinity-preferredduringschedulingignoredduringexecution-2) Copy linkLink copied to clipboard!

Description
:   The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

Type
:   `object`

Required
:   * `weight`
    * `podAffinityTerm`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `podAffinityTerm` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running |
| `weight` | `integer` | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. |

Show more

#### [3.1.22. .template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm](#template-spec-affinity-podaffinity-preferredduringschedulingignoredduringexecution-podaffinityterm) Copy linkLink copied to clipboard!

Description
:   Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running

Type
:   `object`

Required
:   * `topologyKey`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `labelSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

Show more

#### [3.1.23. .template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution](#template-spec-affinity-podaffinity-requiredduringschedulingignoredduringexecution) Copy linkLink copied to clipboard!

Description
:   If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

Type
:   `array`

#### [3.1.24. .template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[]](#template-spec-affinity-podaffinity-requiredduringschedulingignoredduringexecution-2) Copy linkLink copied to clipboard!

Description
:   Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running

Type
:   `object`

Required
:   * `topologyKey`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `labelSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

Show more

#### [3.1.25. .template.spec.affinity.podAntiAffinity](#template-spec-affinity-podantiaffinity) Copy linkLink copied to clipboard!

Description
:   Pod anti affinity is a group of inter pod anti affinity scheduling rules.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and subtracting "weight" from the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) |
| `requiredDuringSchedulingIgnoredDuringExecution` | `array` | If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. |
| `requiredDuringSchedulingIgnoredDuringExecution[]` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running |

Show more

#### [3.1.26. .template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution](#template-spec-affinity-podantiaffinity-preferredduringschedulingignoredduringexecution) Copy linkLink copied to clipboard!

Description
:   The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and subtracting "weight" from the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

Type
:   `array`

#### [3.1.27. .template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[]](#template-spec-affinity-podantiaffinity-preferredduringschedulingignoredduringexecution-2) Copy linkLink copied to clipboard!

Description
:   The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

Type
:   `object`

Required
:   * `weight`
    * `podAffinityTerm`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `podAffinityTerm` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running |
| `weight` | `integer` | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. |

Show more

#### [3.1.28. .template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm](#template-spec-affinity-podantiaffinity-preferredduringschedulingignoredduringexecution-podaffinityterm) Copy linkLink copied to clipboard!

Description
:   Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running

Type
:   `object`

Required
:   * `topologyKey`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `labelSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

Show more

#### [3.1.29. .template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution](#template-spec-affinity-podantiaffinity-requiredduringschedulingignoredduringexecution) Copy linkLink copied to clipboard!

Description
:   If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

Type
:   `array`

#### [3.1.30. .template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[]](#template-spec-affinity-podantiaffinity-requiredduringschedulingignoredduringexecution-2) Copy linkLink copied to clipboard!

Description
:   Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running

Type
:   `object`

Required
:   * `topologyKey`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `labelSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

Show more

#### [3.1.31. .template.spec.containers](#template-spec-containers) Copy linkLink copied to clipboard!

Description
:   List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.

Type
:   `array`

#### [3.1.32. .template.spec.containers[]](#template-spec-containers-2) Copy linkLink copied to clipboard!

Description
:   A single application container that you want to run within a pod.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `args` | `array (string)` | Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references $(VAR\_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `command` | `array (string)` | Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR\_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `env` | `array` | List of environment variables to set in the container. Cannot be updated. |
| `env[]` | `object` | EnvVar represents an environment variable present in a Container. |
| `envFrom` | `array` | List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. |
| `envFrom[]` | `object` | EnvFromSource represents the source of a set of ConfigMaps or Secrets |
| `image` | `string` | Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. |
| `imagePullPolicy` | `string` | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images>  Possible enum values: - `"Always"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - `"IfNotPresent"` means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - `"Never"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present |
| `lifecycle` | `object` | Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted. |
| `livenessProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `name` | `string` | Name of the container specified as a DNS\_LABEL. Each container in a pod must have a unique name (DNS\_LABEL). Cannot be updated. |
| `ports` | `array` | List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated. |
| `ports[]` | `object` | ContainerPort represents a network port in a single container. |
| `readinessProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `resizePolicy` | `array` | Resources resize policy for the container. This field cannot be set on ephemeral containers. |
| `resizePolicy[]` | `object` | ContainerResizePolicy represents resource resize policy for the container. |
| `resources` | `object` | ResourceRequirements describes the compute resource requirements. |
| `restartPolicy` | `string` | RestartPolicy defines the restart behavior of individual containers in a pod. This overrides the pod-level restart policy. When this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Additionally, setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. |
| `restartPolicyRules` | `array` | Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy. |
| `restartPolicyRules[]` | `object` | ContainerRestartRule describes how a container exit is handled. |
| `securityContext` | `object` | SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence. |
| `startupProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `stdin` | `boolean` | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. |
| `stdinOnce` | `boolean` | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false |
| `terminationMessagePath` | `string` | Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. |
| `terminationMessagePolicy` | `string` | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.  Possible enum values: - `"FallbackToLogsOnError"` will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents. - `"File"` is the default behavior and will set the container status message to the contents of the container’s terminationMessagePath when the container exits. |
| `tty` | `boolean` | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. |
| `volumeDevices` | `array` | volumeDevices is the list of block devices to be used by the container. |
| `volumeDevices[]` | `object` | volumeDevice describes a mapping of a raw block device within a container. |
| `volumeMounts` | `array` | Pod volumes to mount into the container’s filesystem. Cannot be updated. |
| `volumeMounts[]` | `object` | VolumeMount describes a mounting of a Volume within a container. |
| `workingDir` | `string` | Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated. |

Show more

#### [3.1.33. .template.spec.containers[].env](#template-spec-containers-env) Copy linkLink copied to clipboard!

Description
:   List of environment variables to set in the container. Cannot be updated.

Type
:   `array`

#### [3.1.34. .template.spec.containers[].env[]](#template-spec-containers-env-2) Copy linkLink copied to clipboard!

Description
:   EnvVar represents an environment variable present in a Container.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the environment variable. May consist of any printable ASCII characters except '='. |
| `value` | `string` | Variable references $(VAR\_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | EnvVarSource represents a source for the value of an EnvVar. |

Show more

#### [3.1.35. .template.spec.containers[].env[].valueFrom](#template-spec-containers-env-valuefrom) Copy linkLink copied to clipboard!

Description
:   EnvVarSource represents a source for the value of an EnvVar.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapKeyRef` | `object` | Selects a key from a ConfigMap. |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `fileKeyRef` | `object` | FileKeySelector selects a key of the env file. |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |
| `secretKeyRef` | `object` | SecretKeySelector selects a key of a Secret. |

Show more

#### [3.1.36. .template.spec.containers[].env[].valueFrom.configMapKeyRef](#template-spec-containers-env-valuefrom-configmapkeyref) Copy linkLink copied to clipboard!

Description
:   Selects a key from a ConfigMap.

Type
:   `object`

Required
:   * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

Show more

#### [3.1.37. .template.spec.containers[].env[].valueFrom.fieldRef](#template-spec-containers-env-valuefrom-fieldref) Copy linkLink copied to clipboard!

Description
:   ObjectFieldSelector selects an APIVersioned field of an object.

Type
:   `object`

Required
:   * `fieldPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

Show more

#### [3.1.38. .template.spec.containers[].env[].valueFrom.fileKeyRef](#template-spec-containers-env-valuefrom-filekeyref) Copy linkLink copied to clipboard!

Description
:   FileKeySelector selects a key of the env file.

Type
:   `object`

Required
:   * `volumeName`
    * `path`
    * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters. |
| `optional` | `boolean` | Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod’s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation. |
| `path` | `string` | The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'. |
| `volumeName` | `string` | The name of the volume mount containing the env file. |

Show more

#### [3.1.39. .template.spec.containers[].env[].valueFrom.resourceFieldRef](#template-spec-containers-env-valuefrom-resourcefieldref) Copy linkLink copied to clipboard!

Description
:   ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

Show more

#### [3.1.40. .template.spec.containers[].env[].valueFrom.secretKeyRef](#template-spec-containers-env-valuefrom-secretkeyref) Copy linkLink copied to clipboard!

Description
:   SecretKeySelector selects a key of a Secret.

Type
:   `object`

Required
:   * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

Show more

#### [3.1.41. .template.spec.containers[].envFrom](#template-spec-containers-envfrom) Copy linkLink copied to clipboard!

Description
:   List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
:   `array`

#### [3.1.42. .template.spec.containers[].envFrom[]](#template-spec-containers-envfrom-2) Copy linkLink copied to clipboard!

Description
:   EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapRef` | `object` | ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.  The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables. |
| `prefix` | `string` | Optional text to prepend to the name of each environment variable. May consist of any printable ASCII characters except '='. |
| `secretRef` | `object` | SecretEnvSource selects a Secret to populate the environment variables with.  The contents of the target Secret’s Data field will represent the key-value pairs as environment variables. |

Show more

#### [3.1.43. .template.spec.containers[].envFrom[].configMapRef](#template-spec-containers-envfrom-configmapref) Copy linkLink copied to clipboard!

Description
:   ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

Show more

#### [3.1.44. .template.spec.containers[].envFrom[].secretRef](#template-spec-containers-envfrom-secretref) Copy linkLink copied to clipboard!

Description
:   SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

Show more

#### [3.1.45. .template.spec.containers[].lifecycle](#template-spec-containers-lifecycle) Copy linkLink copied to clipboard!

Description
:   Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `postStart` | `object` | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. |
| `preStop` | `object` | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. |
| `stopSignal` | `string` | StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name  Possible enum values: - `"SIGABRT"` - `"SIGALRM"` - `"SIGBUS"` - `"SIGCHLD"` - `"SIGCLD"` - `"SIGCONT"` - `"SIGFPE"` - `"SIGHUP"` - `"SIGILL"` - `"SIGINT"` - `"SIGIO"` - `"SIGIOT"` - `"SIGKILL"` - `"SIGPIPE"` - `"SIGPOLL"` - `"SIGPROF"` - `"SIGPWR"` - `"SIGQUIT"` - `"SIGRTMAX"` - `"SIGRTMAX-1"` - `"SIGRTMAX-10"` - `"SIGRTMAX-11"` - `"SIGRTMAX-12"` - `"SIGRTMAX-13"` - `"SIGRTMAX-14"` - `"SIGRTMAX-2"` - `"SIGRTMAX-3"` - `"SIGRTMAX-4"` - `"SIGRTMAX-5"` - `"SIGRTMAX-6"` - `"SIGRTMAX-7"` - `"SIGRTMAX-8"` - `"SIGRTMAX-9"` - `"SIGRTMIN"` - `"SIGRTMIN+1"` - `"SIGRTMIN+10"` - `"SIGRTMIN+11"` - `"SIGRTMIN+12"` - `"SIGRTMIN+13"` - `"SIGRTMIN+14"` - `"SIGRTMIN+15"` - `"SIGRTMIN+2"` - `"SIGRTMIN+3"` - `"SIGRTMIN+4"` - `"SIGRTMIN+5"` - `"SIGRTMIN+6"` - `"SIGRTMIN+7"` - `"SIGRTMIN+8"` - `"SIGRTMIN+9"` - `"SIGSEGV"` - `"SIGSTKFLT"` - `"SIGSTOP"` - `"SIGSYS"` - `"SIGTERM"` - `"SIGTRAP"` - `"SIGTSTP"` - `"SIGTTIN"` - `"SIGTTOU"` - `"SIGURG"` - `"SIGUSR1"` - `"SIGUSR2"` - `"SIGVTALRM"` - `"SIGWINCH"` - `"SIGXCPU"` - `"SIGXFSZ"` |

Show more

#### [3.1.46. .template.spec.containers[].lifecycle.postStart](#template-spec-containers-lifecycle-poststart) Copy linkLink copied to clipboard!

Description
:   LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

Show more

#### [3.1.47. .template.spec.containers[].lifecycle.postStart.exec](#template-spec-containers-lifecycle-poststart-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.48. .template.spec.containers[].lifecycle.postStart.httpGet](#template-spec-containers-lifecycle-poststart-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.49. .template.spec.containers[].lifecycle.postStart.httpGet.httpHeaders](#template-spec-containers-lifecycle-poststart-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.50. .template.spec.containers[].lifecycle.postStart.httpGet.httpHeaders[]](#template-spec-containers-lifecycle-poststart-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.51. .template.spec.containers[].lifecycle.postStart.sleep](#template-spec-containers-lifecycle-poststart-sleep) Copy linkLink copied to clipboard!

Description
:   SleepAction describes a "sleep" action.

Type
:   `object`

Required
:   * `seconds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

Show more

#### [3.1.52. .template.spec.containers[].lifecycle.postStart.tcpSocket](#template-spec-containers-lifecycle-poststart-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.53. .template.spec.containers[].lifecycle.preStop](#template-spec-containers-lifecycle-prestop) Copy linkLink copied to clipboard!

Description
:   LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

Show more

#### [3.1.54. .template.spec.containers[].lifecycle.preStop.exec](#template-spec-containers-lifecycle-prestop-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.55. .template.spec.containers[].lifecycle.preStop.httpGet](#template-spec-containers-lifecycle-prestop-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.56. .template.spec.containers[].lifecycle.preStop.httpGet.httpHeaders](#template-spec-containers-lifecycle-prestop-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.57. .template.spec.containers[].lifecycle.preStop.httpGet.httpHeaders[]](#template-spec-containers-lifecycle-prestop-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.58. .template.spec.containers[].lifecycle.preStop.sleep](#template-spec-containers-lifecycle-prestop-sleep) Copy linkLink copied to clipboard!

Description
:   SleepAction describes a "sleep" action.

Type
:   `object`

Required
:   * `seconds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

Show more

#### [3.1.59. .template.spec.containers[].lifecycle.preStop.tcpSocket](#template-spec-containers-lifecycle-prestop-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.60. .template.spec.containers[].livenessProbe](#template-spec-containers-livenessprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.61. .template.spec.containers[].livenessProbe.exec](#template-spec-containers-livenessprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.62. .template.spec.containers[].livenessProbe.grpc](#template-spec-containers-livenessprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.63. .template.spec.containers[].livenessProbe.httpGet](#template-spec-containers-livenessprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.64. .template.spec.containers[].livenessProbe.httpGet.httpHeaders](#template-spec-containers-livenessprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.65. .template.spec.containers[].livenessProbe.httpGet.httpHeaders[]](#template-spec-containers-livenessprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.66. .template.spec.containers[].livenessProbe.tcpSocket](#template-spec-containers-livenessprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.67. .template.spec.containers[].ports](#template-spec-containers-ports) Copy linkLink copied to clipboard!

Description
:   List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.

Type
:   `array`

#### [3.1.68. .template.spec.containers[].ports[]](#template-spec-containers-ports-2) Copy linkLink copied to clipboard!

Description
:   ContainerPort represents a network port in a single container.

Type
:   `object`

Required
:   * `containerPort`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerPort` | `integer` | Number of port to expose on the pod’s IP address. This must be a valid port number, 0 < x < 65536. |
| `hostIP` | `string` | What host IP to bind the external port to. |
| `hostPort` | `integer` | Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. |
| `name` | `string` | If specified, this must be an IANA\_SVC\_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. |
| `protocol` | `string` | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".  Possible enum values: - `"SCTP"` is the SCTP protocol. - `"TCP"` is the TCP protocol. - `"UDP"` is the UDP protocol. |

Show more

#### [3.1.69. .template.spec.containers[].readinessProbe](#template-spec-containers-readinessprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.70. .template.spec.containers[].readinessProbe.exec](#template-spec-containers-readinessprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.71. .template.spec.containers[].readinessProbe.grpc](#template-spec-containers-readinessprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.72. .template.spec.containers[].readinessProbe.httpGet](#template-spec-containers-readinessprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.73. .template.spec.containers[].readinessProbe.httpGet.httpHeaders](#template-spec-containers-readinessprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.74. .template.spec.containers[].readinessProbe.httpGet.httpHeaders[]](#template-spec-containers-readinessprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.75. .template.spec.containers[].readinessProbe.tcpSocket](#template-spec-containers-readinessprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.76. .template.spec.containers[].resizePolicy](#template-spec-containers-resizepolicy) Copy linkLink copied to clipboard!

Description
:   Resources resize policy for the container. This field cannot be set on ephemeral containers.

Type
:   `array`

#### [3.1.77. .template.spec.containers[].resizePolicy[]](#template-spec-containers-resizepolicy-2) Copy linkLink copied to clipboard!

Description
:   ContainerResizePolicy represents resource resize policy for the container.

Type
:   `object`

Required
:   * `resourceName`
    * `restartPolicy`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

Show more

#### [3.1.78. .template.spec.containers[].resources](#template-spec-containers-resources) Copy linkLink copied to clipboard!

Description
:   ResourceRequirements describes the compute resource requirements.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claims` | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. |
| `claims[]` | `object` | ResourceClaim references one entry in PodSpec.ResourceClaims. |
| `limits` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [3.1.79. .template.spec.containers[].resources.claims](#template-spec-containers-resources-claims) Copy linkLink copied to clipboard!

Description
:   Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This field depends on the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.

Type
:   `array`

#### [3.1.80. .template.spec.containers[].resources.claims[]](#template-spec-containers-resources-claims-2) Copy linkLink copied to clipboard!

Description
:   ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

Show more

#### [3.1.81. .template.spec.containers[].restartPolicyRules](#template-spec-containers-restartpolicyrules) Copy linkLink copied to clipboard!

Description
:   Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy.

Type
:   `array`

#### [3.1.82. .template.spec.containers[].restartPolicyRules[]](#template-spec-containers-restartpolicyrules-2) Copy linkLink copied to clipboard!

Description
:   ContainerRestartRule describes how a container exit is handled.

Type
:   `object`

Required
:   * `action`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `action` | `string` | Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is "Restart" to restart the container. |
| `exitCodes` | `object` | ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes. |

Show more

#### [3.1.83. .template.spec.containers[].restartPolicyRules[].exitCodes](#template-spec-containers-restartpolicyrules-exitcodes) Copy linkLink copied to clipboard!

Description
:   ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes.

Type
:   `object`

Required
:   * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `operator` | `string` | Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the set of specified values. - NotIn: the requirement is satisfied if the container exit code is not in the set of specified values. |
| `values` | `array (integer)` | Specifies the set of values to check for container exit codes. At most 255 elements are allowed. |

Show more

#### [3.1.84. .template.spec.containers[].securityContext](#template-spec-containers-securitycontext) Copy linkLink copied to clipboard!

Description
:   SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowPrivilegeEscalation` | `boolean` | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no\_new\_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP\_SYS\_ADMIN Note that this field cannot be set when spec.os.name is windows. |
| `appArmorProfile` | `object` | AppArmorProfile defines a pod or container’s AppArmor settings. |
| `capabilities` | `object` | Adds and removes POSIX capabilities from running containers. |
| `privileged` | `boolean` | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. |
| `procMount` | `string` | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.  Possible enum values: - `"Default"` uses the container runtime defaults for readonly and masked paths for /proc. Most container runtimes mask certain paths in /proc to avoid accidental security exposure of special devices or information. - `"Unmasked"` bypasses the default masking behavior of the container runtime and ensures the newly created /proc the container stays in tact with no modifications. |
| `readOnlyRootFilesystem` | `boolean` | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | SELinuxOptions are the labels to be applied to the container |
| `seccompProfile` | `object` | SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set. |
| `windowsOptions` | `object` | WindowsSecurityContextOptions contain Windows-specific options and credentials. |

Show more

#### [3.1.85. .template.spec.containers[].securityContext.appArmorProfile](#template-spec-containers-securitycontext-apparmorprofile) Copy linkLink copied to clipboard!

Description
:   AppArmorProfile defines a pod or container’s AppArmor settings.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.  Possible enum values: - `"Localhost"` indicates that a profile pre-loaded on the node should be used. - `"RuntimeDefault"` indicates that the container runtime’s default AppArmor profile should be used. - `"Unconfined"` indicates that no AppArmor profile should be enforced. |

Show more

#### [3.1.86. .template.spec.containers[].securityContext.capabilities](#template-spec-containers-securitycontext-capabilities) Copy linkLink copied to clipboard!

Description
:   Adds and removes POSIX capabilities from running containers.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `add` | `array (string)` | Added capabilities |
| `drop` | `array (string)` | Removed capabilities |

Show more

#### [3.1.87. .template.spec.containers[].securityContext.seLinuxOptions](#template-spec-containers-securitycontext-selinuxoptions) Copy linkLink copied to clipboard!

Description
:   SELinuxOptions are the labels to be applied to the container

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

Show more

#### [3.1.88. .template.spec.containers[].securityContext.seccompProfile](#template-spec-containers-securitycontext-seccompprofile) Copy linkLink copied to clipboard!

Description
:   SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. |
| `type` | `string` | type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.  Possible enum values: - `"Localhost"` indicates a profile defined in a file on the node should be used. The file’s location relative to <kubelet-root-dir>/seccomp. - `"RuntimeDefault"` represents the default container runtime seccomp profile. - `"Unconfined"` indicates no seccomp profile is applied (A.K.A. unconfined). |

Show more

#### [3.1.89. .template.spec.containers[].securityContext.windowsOptions](#template-spec-containers-securitycontext-windowsoptions) Copy linkLink copied to clipboard!

Description
:   WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

Show more

#### [3.1.90. .template.spec.containers[].startupProbe](#template-spec-containers-startupprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.91. .template.spec.containers[].startupProbe.exec](#template-spec-containers-startupprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.92. .template.spec.containers[].startupProbe.grpc](#template-spec-containers-startupprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.93. .template.spec.containers[].startupProbe.httpGet](#template-spec-containers-startupprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.94. .template.spec.containers[].startupProbe.httpGet.httpHeaders](#template-spec-containers-startupprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.95. .template.spec.containers[].startupProbe.httpGet.httpHeaders[]](#template-spec-containers-startupprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.96. .template.spec.containers[].startupProbe.tcpSocket](#template-spec-containers-startupprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.97. .template.spec.containers[].volumeDevices](#template-spec-containers-volumedevices) Copy linkLink copied to clipboard!

Description
:   volumeDevices is the list of block devices to be used by the container.

Type
:   `array`

#### [3.1.98. .template.spec.containers[].volumeDevices[]](#template-spec-containers-volumedevices-2) Copy linkLink copied to clipboard!

Description
:   volumeDevice describes a mapping of a raw block device within a container.

Type
:   `object`

Required
:   * `name`
    * `devicePath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

Show more

#### [3.1.99. .template.spec.containers[].volumeMounts](#template-spec-containers-volumemounts) Copy linkLink copied to clipboard!

Description
:   Pod volumes to mount into the container’s filesystem. Cannot be updated.

Type
:   `array`

#### [3.1.100. .template.spec.containers[].volumeMounts[]](#template-spec-containers-volumemounts-2) Copy linkLink copied to clipboard!

Description
:   VolumeMount describes a mounting of a Volume within a container.

Type
:   `object`

Required
:   * `name`
    * `mountPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mountPath` | `string` | Path within the container at which the volume should be mounted. Must not contain ':'. |
| `mountPropagation` | `string` | mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).  Possible enum values: - `"Bidirectional"` means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rshared" in Linux terminology). - `"HostToContainer"` means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rslave" in Linux terminology). - `"None"` means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode corresponds to "private" in Linux terminology. |
| `name` | `string` | This must match the Name of a Volume. |
| `readOnly` | `boolean` | Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. |
| `recursiveReadOnly` | `string` | RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled. |
| `subPath` | `string` | Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root). |
| `subPathExpr` | `string` | Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR\_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive. |

Show more

#### [3.1.101. .template.spec.dnsConfig](#template-spec-dnsconfig) Copy linkLink copied to clipboard!

Description
:   PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nameservers` | `array (string)` | A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. |
| `options` | `array` | A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. |
| `options[]` | `object` | PodDNSConfigOption defines DNS resolver options of a pod. |
| `searches` | `array (string)` | A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. |

Show more

#### [3.1.102. .template.spec.dnsConfig.options](#template-spec-dnsconfig-options) Copy linkLink copied to clipboard!

Description
:   A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.

Type
:   `array`

#### [3.1.103. .template.spec.dnsConfig.options[]](#template-spec-dnsconfig-options-2) Copy linkLink copied to clipboard!

Description
:   PodDNSConfigOption defines DNS resolver options of a pod.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name is this DNS resolver option’s name. Required. |
| `value` | `string` | Value is this DNS resolver option’s value. |

Show more

#### [3.1.104. .template.spec.ephemeralContainers](#template-spec-ephemeralcontainers) Copy linkLink copied to clipboard!

Description
:   List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod’s ephemeralcontainers subresource.

Type
:   `array`

#### [3.1.105. .template.spec.ephemeralContainers[]](#template-spec-ephemeralcontainers-2) Copy linkLink copied to clipboard!

Description
:   An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

    To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `args` | `array (string)` | Arguments to the entrypoint. The image’s CMD is used if this is not provided. Variable references $(VAR\_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `command` | `array (string)` | Entrypoint array. Not executed within a shell. The image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR\_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `env` | `array` | List of environment variables to set in the container. Cannot be updated. |
| `env[]` | `object` | EnvVar represents an environment variable present in a Container. |
| `envFrom` | `array` | List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. |
| `envFrom[]` | `object` | EnvFromSource represents the source of a set of ConfigMaps or Secrets |
| `image` | `string` | Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> |
| `imagePullPolicy` | `string` | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images>  Possible enum values: - `"Always"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - `"IfNotPresent"` means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - `"Never"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present |
| `lifecycle` | `object` | Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted. |
| `livenessProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `name` | `string` | Name of the ephemeral container specified as a DNS\_LABEL. This name must be unique among all containers, init containers and ephemeral containers. |
| `ports` | `array` | Ports are not allowed for ephemeral containers. |
| `ports[]` | `object` | ContainerPort represents a network port in a single container. |
| `readinessProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `resizePolicy` | `array` | Resources resize policy for the container. |
| `resizePolicy[]` | `object` | ContainerResizePolicy represents resource resize policy for the container. |
| `resources` | `object` | ResourceRequirements describes the compute resource requirements. |
| `restartPolicy` | `string` | Restart policy for the container to manage the restart behavior of each container within a pod. You cannot set this field on ephemeral containers. |
| `restartPolicyRules` | `array` | Represents a list of rules to be checked to determine if the container should be restarted on exit. You cannot set this field on ephemeral containers. |
| `restartPolicyRules[]` | `object` | ContainerRestartRule describes how a container exit is handled. |
| `securityContext` | `object` | SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence. |
| `startupProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `stdin` | `boolean` | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. |
| `stdinOnce` | `boolean` | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false |
| `targetContainerName` | `string` | If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.  The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined. |
| `terminationMessagePath` | `string` | Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. |
| `terminationMessagePolicy` | `string` | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.  Possible enum values: - `"FallbackToLogsOnError"` will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents. - `"File"` is the default behavior and will set the container status message to the contents of the container’s terminationMessagePath when the container exits. |
| `tty` | `boolean` | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. |
| `volumeDevices` | `array` | volumeDevices is the list of block devices to be used by the container. |
| `volumeDevices[]` | `object` | volumeDevice describes a mapping of a raw block device within a container. |
| `volumeMounts` | `array` | Pod volumes to mount into the container’s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. |
| `volumeMounts[]` | `object` | VolumeMount describes a mounting of a Volume within a container. |
| `workingDir` | `string` | Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated. |

Show more

#### [3.1.106. .template.spec.ephemeralContainers[].env](#template-spec-ephemeralcontainers-env) Copy linkLink copied to clipboard!

Description
:   List of environment variables to set in the container. Cannot be updated.

Type
:   `array`

#### [3.1.107. .template.spec.ephemeralContainers[].env[]](#template-spec-ephemeralcontainers-env-2) Copy linkLink copied to clipboard!

Description
:   EnvVar represents an environment variable present in a Container.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the environment variable. May consist of any printable ASCII characters except '='. |
| `value` | `string` | Variable references $(VAR\_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | EnvVarSource represents a source for the value of an EnvVar. |

Show more

#### [3.1.108. .template.spec.ephemeralContainers[].env[].valueFrom](#template-spec-ephemeralcontainers-env-valuefrom) Copy linkLink copied to clipboard!

Description
:   EnvVarSource represents a source for the value of an EnvVar.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapKeyRef` | `object` | Selects a key from a ConfigMap. |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `fileKeyRef` | `object` | FileKeySelector selects a key of the env file. |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |
| `secretKeyRef` | `object` | SecretKeySelector selects a key of a Secret. |

Show more

#### [3.1.109. .template.spec.ephemeralContainers[].env[].valueFrom.configMapKeyRef](#template-spec-ephemeralcontainers-env-valuefrom-configmapkeyref) Copy linkLink copied to clipboard!

Description
:   Selects a key from a ConfigMap.

Type
:   `object`

Required
:   * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

Show more

#### [3.1.110. .template.spec.ephemeralContainers[].env[].valueFrom.fieldRef](#template-spec-ephemeralcontainers-env-valuefrom-fieldref) Copy linkLink copied to clipboard!

Description
:   ObjectFieldSelector selects an APIVersioned field of an object.

Type
:   `object`

Required
:   * `fieldPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

Show more

#### [3.1.111. .template.spec.ephemeralContainers[].env[].valueFrom.fileKeyRef](#template-spec-ephemeralcontainers-env-valuefrom-filekeyref) Copy linkLink copied to clipboard!

Description
:   FileKeySelector selects a key of the env file.

Type
:   `object`

Required
:   * `volumeName`
    * `path`
    * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters. |
| `optional` | `boolean` | Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod’s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation. |
| `path` | `string` | The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'. |
| `volumeName` | `string` | The name of the volume mount containing the env file. |

Show more

#### [3.1.112. .template.spec.ephemeralContainers[].env[].valueFrom.resourceFieldRef](#template-spec-ephemeralcontainers-env-valuefrom-resourcefieldref) Copy linkLink copied to clipboard!

Description
:   ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

Show more

#### [3.1.113. .template.spec.ephemeralContainers[].env[].valueFrom.secretKeyRef](#template-spec-ephemeralcontainers-env-valuefrom-secretkeyref) Copy linkLink copied to clipboard!

Description
:   SecretKeySelector selects a key of a Secret.

Type
:   `object`

Required
:   * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

Show more

#### [3.1.114. .template.spec.ephemeralContainers[].envFrom](#template-spec-ephemeralcontainers-envfrom) Copy linkLink copied to clipboard!

Description
:   List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
:   `array`

#### [3.1.115. .template.spec.ephemeralContainers[].envFrom[]](#template-spec-ephemeralcontainers-envfrom-2) Copy linkLink copied to clipboard!

Description
:   EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapRef` | `object` | ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.  The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables. |
| `prefix` | `string` | Optional text to prepend to the name of each environment variable. May consist of any printable ASCII characters except '='. |
| `secretRef` | `object` | SecretEnvSource selects a Secret to populate the environment variables with.  The contents of the target Secret’s Data field will represent the key-value pairs as environment variables. |

Show more

#### [3.1.116. .template.spec.ephemeralContainers[].envFrom[].configMapRef](#template-spec-ephemeralcontainers-envfrom-configmapref) Copy linkLink copied to clipboard!

Description
:   ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

Show more

#### [3.1.117. .template.spec.ephemeralContainers[].envFrom[].secretRef](#template-spec-ephemeralcontainers-envfrom-secretref) Copy linkLink copied to clipboard!

Description
:   SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

Show more

#### [3.1.118. .template.spec.ephemeralContainers[].lifecycle](#template-spec-ephemeralcontainers-lifecycle) Copy linkLink copied to clipboard!

Description
:   Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `postStart` | `object` | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. |
| `preStop` | `object` | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. |
| `stopSignal` | `string` | StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name  Possible enum values: - `"SIGABRT"` - `"SIGALRM"` - `"SIGBUS"` - `"SIGCHLD"` - `"SIGCLD"` - `"SIGCONT"` - `"SIGFPE"` - `"SIGHUP"` - `"SIGILL"` - `"SIGINT"` - `"SIGIO"` - `"SIGIOT"` - `"SIGKILL"` - `"SIGPIPE"` - `"SIGPOLL"` - `"SIGPROF"` - `"SIGPWR"` - `"SIGQUIT"` - `"SIGRTMAX"` - `"SIGRTMAX-1"` - `"SIGRTMAX-10"` - `"SIGRTMAX-11"` - `"SIGRTMAX-12"` - `"SIGRTMAX-13"` - `"SIGRTMAX-14"` - `"SIGRTMAX-2"` - `"SIGRTMAX-3"` - `"SIGRTMAX-4"` - `"SIGRTMAX-5"` - `"SIGRTMAX-6"` - `"SIGRTMAX-7"` - `"SIGRTMAX-8"` - `"SIGRTMAX-9"` - `"SIGRTMIN"` - `"SIGRTMIN+1"` - `"SIGRTMIN+10"` - `"SIGRTMIN+11"` - `"SIGRTMIN+12"` - `"SIGRTMIN+13"` - `"SIGRTMIN+14"` - `"SIGRTMIN+15"` - `"SIGRTMIN+2"` - `"SIGRTMIN+3"` - `"SIGRTMIN+4"` - `"SIGRTMIN+5"` - `"SIGRTMIN+6"` - `"SIGRTMIN+7"` - `"SIGRTMIN+8"` - `"SIGRTMIN+9"` - `"SIGSEGV"` - `"SIGSTKFLT"` - `"SIGSTOP"` - `"SIGSYS"` - `"SIGTERM"` - `"SIGTRAP"` - `"SIGTSTP"` - `"SIGTTIN"` - `"SIGTTOU"` - `"SIGURG"` - `"SIGUSR1"` - `"SIGUSR2"` - `"SIGVTALRM"` - `"SIGWINCH"` - `"SIGXCPU"` - `"SIGXFSZ"` |

Show more

#### [3.1.119. .template.spec.ephemeralContainers[].lifecycle.postStart](#template-spec-ephemeralcontainers-lifecycle-poststart) Copy linkLink copied to clipboard!

Description
:   LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

Show more

#### [3.1.120. .template.spec.ephemeralContainers[].lifecycle.postStart.exec](#template-spec-ephemeralcontainers-lifecycle-poststart-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.121. .template.spec.ephemeralContainers[].lifecycle.postStart.httpGet](#template-spec-ephemeralcontainers-lifecycle-poststart-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.122. .template.spec.ephemeralContainers[].lifecycle.postStart.httpGet.httpHeaders](#template-spec-ephemeralcontainers-lifecycle-poststart-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.123. .template.spec.ephemeralContainers[].lifecycle.postStart.httpGet.httpHeaders[]](#template-spec-ephemeralcontainers-lifecycle-poststart-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.124. .template.spec.ephemeralContainers[].lifecycle.postStart.sleep](#template-spec-ephemeralcontainers-lifecycle-poststart-sleep) Copy linkLink copied to clipboard!

Description
:   SleepAction describes a "sleep" action.

Type
:   `object`

Required
:   * `seconds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

Show more

#### [3.1.125. .template.spec.ephemeralContainers[].lifecycle.postStart.tcpSocket](#template-spec-ephemeralcontainers-lifecycle-poststart-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.126. .template.spec.ephemeralContainers[].lifecycle.preStop](#template-spec-ephemeralcontainers-lifecycle-prestop) Copy linkLink copied to clipboard!

Description
:   LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

Show more

#### [3.1.127. .template.spec.ephemeralContainers[].lifecycle.preStop.exec](#template-spec-ephemeralcontainers-lifecycle-prestop-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.128. .template.spec.ephemeralContainers[].lifecycle.preStop.httpGet](#template-spec-ephemeralcontainers-lifecycle-prestop-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.129. .template.spec.ephemeralContainers[].lifecycle.preStop.httpGet.httpHeaders](#template-spec-ephemeralcontainers-lifecycle-prestop-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.130. .template.spec.ephemeralContainers[].lifecycle.preStop.httpGet.httpHeaders[]](#template-spec-ephemeralcontainers-lifecycle-prestop-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.131. .template.spec.ephemeralContainers[].lifecycle.preStop.sleep](#template-spec-ephemeralcontainers-lifecycle-prestop-sleep) Copy linkLink copied to clipboard!

Description
:   SleepAction describes a "sleep" action.

Type
:   `object`

Required
:   * `seconds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

Show more

#### [3.1.132. .template.spec.ephemeralContainers[].lifecycle.preStop.tcpSocket](#template-spec-ephemeralcontainers-lifecycle-prestop-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.133. .template.spec.ephemeralContainers[].livenessProbe](#template-spec-ephemeralcontainers-livenessprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.134. .template.spec.ephemeralContainers[].livenessProbe.exec](#template-spec-ephemeralcontainers-livenessprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.135. .template.spec.ephemeralContainers[].livenessProbe.grpc](#template-spec-ephemeralcontainers-livenessprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.136. .template.spec.ephemeralContainers[].livenessProbe.httpGet](#template-spec-ephemeralcontainers-livenessprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.137. .template.spec.ephemeralContainers[].livenessProbe.httpGet.httpHeaders](#template-spec-ephemeralcontainers-livenessprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.138. .template.spec.ephemeralContainers[].livenessProbe.httpGet.httpHeaders[]](#template-spec-ephemeralcontainers-livenessprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.139. .template.spec.ephemeralContainers[].livenessProbe.tcpSocket](#template-spec-ephemeralcontainers-livenessprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.140. .template.spec.ephemeralContainers[].ports](#template-spec-ephemeralcontainers-ports) Copy linkLink copied to clipboard!

Description
:   Ports are not allowed for ephemeral containers.

Type
:   `array`

#### [3.1.141. .template.spec.ephemeralContainers[].ports[]](#template-spec-ephemeralcontainers-ports-2) Copy linkLink copied to clipboard!

Description
:   ContainerPort represents a network port in a single container.

Type
:   `object`

Required
:   * `containerPort`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerPort` | `integer` | Number of port to expose on the pod’s IP address. This must be a valid port number, 0 < x < 65536. |
| `hostIP` | `string` | What host IP to bind the external port to. |
| `hostPort` | `integer` | Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. |
| `name` | `string` | If specified, this must be an IANA\_SVC\_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. |
| `protocol` | `string` | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".  Possible enum values: - `"SCTP"` is the SCTP protocol. - `"TCP"` is the TCP protocol. - `"UDP"` is the UDP protocol. |

Show more

#### [3.1.142. .template.spec.ephemeralContainers[].readinessProbe](#template-spec-ephemeralcontainers-readinessprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.143. .template.spec.ephemeralContainers[].readinessProbe.exec](#template-spec-ephemeralcontainers-readinessprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.144. .template.spec.ephemeralContainers[].readinessProbe.grpc](#template-spec-ephemeralcontainers-readinessprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.145. .template.spec.ephemeralContainers[].readinessProbe.httpGet](#template-spec-ephemeralcontainers-readinessprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.146. .template.spec.ephemeralContainers[].readinessProbe.httpGet.httpHeaders](#template-spec-ephemeralcontainers-readinessprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.147. .template.spec.ephemeralContainers[].readinessProbe.httpGet.httpHeaders[]](#template-spec-ephemeralcontainers-readinessprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.148. .template.spec.ephemeralContainers[].readinessProbe.tcpSocket](#template-spec-ephemeralcontainers-readinessprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.149. .template.spec.ephemeralContainers[].resizePolicy](#template-spec-ephemeralcontainers-resizepolicy) Copy linkLink copied to clipboard!

Description
:   Resources resize policy for the container.

Type
:   `array`

#### [3.1.150. .template.spec.ephemeralContainers[].resizePolicy[]](#template-spec-ephemeralcontainers-resizepolicy-2) Copy linkLink copied to clipboard!

Description
:   ContainerResizePolicy represents resource resize policy for the container.

Type
:   `object`

Required
:   * `resourceName`
    * `restartPolicy`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

Show more

#### [3.1.151. .template.spec.ephemeralContainers[].resources](#template-spec-ephemeralcontainers-resources) Copy linkLink copied to clipboard!

Description
:   ResourceRequirements describes the compute resource requirements.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claims` | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. |
| `claims[]` | `object` | ResourceClaim references one entry in PodSpec.ResourceClaims. |
| `limits` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [3.1.152. .template.spec.ephemeralContainers[].resources.claims](#template-spec-ephemeralcontainers-resources-claims) Copy linkLink copied to clipboard!

Description
:   Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This field depends on the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.

Type
:   `array`

#### [3.1.153. .template.spec.ephemeralContainers[].resources.claims[]](#template-spec-ephemeralcontainers-resources-claims-2) Copy linkLink copied to clipboard!

Description
:   ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

Show more

#### [3.1.154. .template.spec.ephemeralContainers[].restartPolicyRules](#template-spec-ephemeralcontainers-restartpolicyrules) Copy linkLink copied to clipboard!

Description
:   Represents a list of rules to be checked to determine if the container should be restarted on exit. You cannot set this field on ephemeral containers.

Type
:   `array`

#### [3.1.155. .template.spec.ephemeralContainers[].restartPolicyRules[]](#template-spec-ephemeralcontainers-restartpolicyrules-2) Copy linkLink copied to clipboard!

Description
:   ContainerRestartRule describes how a container exit is handled.

Type
:   `object`

Required
:   * `action`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `action` | `string` | Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is "Restart" to restart the container. |
| `exitCodes` | `object` | ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes. |

Show more

#### [3.1.156. .template.spec.ephemeralContainers[].restartPolicyRules[].exitCodes](#template-spec-ephemeralcontainers-restartpolicyrules-exitcodes) Copy linkLink copied to clipboard!

Description
:   ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes.

Type
:   `object`

Required
:   * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `operator` | `string` | Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the set of specified values. - NotIn: the requirement is satisfied if the container exit code is not in the set of specified values. |
| `values` | `array (integer)` | Specifies the set of values to check for container exit codes. At most 255 elements are allowed. |

Show more

#### [3.1.157. .template.spec.ephemeralContainers[].securityContext](#template-spec-ephemeralcontainers-securitycontext) Copy linkLink copied to clipboard!

Description
:   SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowPrivilegeEscalation` | `boolean` | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no\_new\_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP\_SYS\_ADMIN Note that this field cannot be set when spec.os.name is windows. |
| `appArmorProfile` | `object` | AppArmorProfile defines a pod or container’s AppArmor settings. |
| `capabilities` | `object` | Adds and removes POSIX capabilities from running containers. |
| `privileged` | `boolean` | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. |
| `procMount` | `string` | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.  Possible enum values: - `"Default"` uses the container runtime defaults for readonly and masked paths for /proc. Most container runtimes mask certain paths in /proc to avoid accidental security exposure of special devices or information. - `"Unmasked"` bypasses the default masking behavior of the container runtime and ensures the newly created /proc the container stays in tact with no modifications. |
| `readOnlyRootFilesystem` | `boolean` | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | SELinuxOptions are the labels to be applied to the container |
| `seccompProfile` | `object` | SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set. |
| `windowsOptions` | `object` | WindowsSecurityContextOptions contain Windows-specific options and credentials. |

Show more

#### [3.1.158. .template.spec.ephemeralContainers[].securityContext.appArmorProfile](#template-spec-ephemeralcontainers-securitycontext-apparmorprofile) Copy linkLink copied to clipboard!

Description
:   AppArmorProfile defines a pod or container’s AppArmor settings.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.  Possible enum values: - `"Localhost"` indicates that a profile pre-loaded on the node should be used. - `"RuntimeDefault"` indicates that the container runtime’s default AppArmor profile should be used. - `"Unconfined"` indicates that no AppArmor profile should be enforced. |

Show more

#### [3.1.159. .template.spec.ephemeralContainers[].securityContext.capabilities](#template-spec-ephemeralcontainers-securitycontext-capabilities) Copy linkLink copied to clipboard!

Description
:   Adds and removes POSIX capabilities from running containers.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `add` | `array (string)` | Added capabilities |
| `drop` | `array (string)` | Removed capabilities |

Show more

#### [3.1.160. .template.spec.ephemeralContainers[].securityContext.seLinuxOptions](#template-spec-ephemeralcontainers-securitycontext-selinuxoptions) Copy linkLink copied to clipboard!

Description
:   SELinuxOptions are the labels to be applied to the container

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

Show more

#### [3.1.161. .template.spec.ephemeralContainers[].securityContext.seccompProfile](#template-spec-ephemeralcontainers-securitycontext-seccompprofile) Copy linkLink copied to clipboard!

Description
:   SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. |
| `type` | `string` | type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.  Possible enum values: - `"Localhost"` indicates a profile defined in a file on the node should be used. The file’s location relative to <kubelet-root-dir>/seccomp. - `"RuntimeDefault"` represents the default container runtime seccomp profile. - `"Unconfined"` indicates no seccomp profile is applied (A.K.A. unconfined). |

Show more

#### [3.1.162. .template.spec.ephemeralContainers[].securityContext.windowsOptions](#template-spec-ephemeralcontainers-securitycontext-windowsoptions) Copy linkLink copied to clipboard!

Description
:   WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

Show more

#### [3.1.163. .template.spec.ephemeralContainers[].startupProbe](#template-spec-ephemeralcontainers-startupprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.164. .template.spec.ephemeralContainers[].startupProbe.exec](#template-spec-ephemeralcontainers-startupprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.165. .template.spec.ephemeralContainers[].startupProbe.grpc](#template-spec-ephemeralcontainers-startupprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.166. .template.spec.ephemeralContainers[].startupProbe.httpGet](#template-spec-ephemeralcontainers-startupprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.167. .template.spec.ephemeralContainers[].startupProbe.httpGet.httpHeaders](#template-spec-ephemeralcontainers-startupprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.168. .template.spec.ephemeralContainers[].startupProbe.httpGet.httpHeaders[]](#template-spec-ephemeralcontainers-startupprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.169. .template.spec.ephemeralContainers[].startupProbe.tcpSocket](#template-spec-ephemeralcontainers-startupprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.170. .template.spec.ephemeralContainers[].volumeDevices](#template-spec-ephemeralcontainers-volumedevices) Copy linkLink copied to clipboard!

Description
:   volumeDevices is the list of block devices to be used by the container.

Type
:   `array`

#### [3.1.171. .template.spec.ephemeralContainers[].volumeDevices[]](#template-spec-ephemeralcontainers-volumedevices-2) Copy linkLink copied to clipboard!

Description
:   volumeDevice describes a mapping of a raw block device within a container.

Type
:   `object`

Required
:   * `name`
    * `devicePath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

Show more

#### [3.1.172. .template.spec.ephemeralContainers[].volumeMounts](#template-spec-ephemeralcontainers-volumemounts) Copy linkLink copied to clipboard!

Description
:   Pod volumes to mount into the container’s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.

Type
:   `array`

#### [3.1.173. .template.spec.ephemeralContainers[].volumeMounts[]](#template-spec-ephemeralcontainers-volumemounts-2) Copy linkLink copied to clipboard!

Description
:   VolumeMount describes a mounting of a Volume within a container.

Type
:   `object`

Required
:   * `name`
    * `mountPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mountPath` | `string` | Path within the container at which the volume should be mounted. Must not contain ':'. |
| `mountPropagation` | `string` | mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).  Possible enum values: - `"Bidirectional"` means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rshared" in Linux terminology). - `"HostToContainer"` means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rslave" in Linux terminology). - `"None"` means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode corresponds to "private" in Linux terminology. |
| `name` | `string` | This must match the Name of a Volume. |
| `readOnly` | `boolean` | Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. |
| `recursiveReadOnly` | `string` | RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled. |
| `subPath` | `string` | Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root). |
| `subPathExpr` | `string` | Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR\_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive. |

Show more

#### [3.1.174. .template.spec.hostAliases](#template-spec-hostaliases) Copy linkLink copied to clipboard!

Description
:   HostAliases is an optional list of hosts and IPs that will be injected into the pod’s hosts file if specified.

Type
:   `array`

#### [3.1.175. .template.spec.hostAliases[]](#template-spec-hostaliases-2) Copy linkLink copied to clipboard!

Description
:   HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file.

Type
:   `object`

Required
:   * `ip`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hostnames` | `array (string)` | Hostnames for the above IP address. |
| `ip` | `string` | IP address of the host file entry. |

Show more

#### [3.1.176. .template.spec.imagePullSecrets](#template-spec-imagepullsecrets) Copy linkLink copied to clipboard!

Description
:   ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: <https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod>

Type
:   `array`

#### [3.1.177. .template.spec.imagePullSecrets[]](#template-spec-imagepullsecrets-2) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.178. .template.spec.initContainers](#template-spec-initcontainers) Copy linkLink copied to clipboard!

Description
:   List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>

Type
:   `array`

#### [3.1.179. .template.spec.initContainers[]](#template-spec-initcontainers-2) Copy linkLink copied to clipboard!

Description
:   A single application container that you want to run within a pod.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `args` | `array (string)` | Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references $(VAR\_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `command` | `array (string)` | Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR\_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell> |
| `env` | `array` | List of environment variables to set in the container. Cannot be updated. |
| `env[]` | `object` | EnvVar represents an environment variable present in a Container. |
| `envFrom` | `array` | List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. |
| `envFrom[]` | `object` | EnvFromSource represents the source of a set of ConfigMaps or Secrets |
| `image` | `string` | Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. |
| `imagePullPolicy` | `string` | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images>  Possible enum values: - `"Always"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - `"IfNotPresent"` means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - `"Never"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present |
| `lifecycle` | `object` | Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted. |
| `livenessProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `name` | `string` | Name of the container specified as a DNS\_LABEL. Each container in a pod must have a unique name (DNS\_LABEL). Cannot be updated. |
| `ports` | `array` | List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated. |
| `ports[]` | `object` | ContainerPort represents a network port in a single container. |
| `readinessProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `resizePolicy` | `array` | Resources resize policy for the container. This field cannot be set on ephemeral containers. |
| `resizePolicy[]` | `object` | ContainerResizePolicy represents resource resize policy for the container. |
| `resources` | `object` | ResourceRequirements describes the compute resource requirements. |
| `restartPolicy` | `string` | RestartPolicy defines the restart behavior of individual containers in a pod. This overrides the pod-level restart policy. When this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Additionally, setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. |
| `restartPolicyRules` | `array` | Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy. |
| `restartPolicyRules[]` | `object` | ContainerRestartRule describes how a container exit is handled. |
| `securityContext` | `object` | SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence. |
| `startupProbe` | `object` | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. |
| `stdin` | `boolean` | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. |
| `stdinOnce` | `boolean` | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false |
| `terminationMessagePath` | `string` | Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. |
| `terminationMessagePolicy` | `string` | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.  Possible enum values: - `"FallbackToLogsOnError"` will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents. - `"File"` is the default behavior and will set the container status message to the contents of the container’s terminationMessagePath when the container exits. |
| `tty` | `boolean` | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. |
| `volumeDevices` | `array` | volumeDevices is the list of block devices to be used by the container. |
| `volumeDevices[]` | `object` | volumeDevice describes a mapping of a raw block device within a container. |
| `volumeMounts` | `array` | Pod volumes to mount into the container’s filesystem. Cannot be updated. |
| `volumeMounts[]` | `object` | VolumeMount describes a mounting of a Volume within a container. |
| `workingDir` | `string` | Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated. |

Show more

#### [3.1.180. .template.spec.initContainers[].env](#template-spec-initcontainers-env) Copy linkLink copied to clipboard!

Description
:   List of environment variables to set in the container. Cannot be updated.

Type
:   `array`

#### [3.1.181. .template.spec.initContainers[].env[]](#template-spec-initcontainers-env-2) Copy linkLink copied to clipboard!

Description
:   EnvVar represents an environment variable present in a Container.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the environment variable. May consist of any printable ASCII characters except '='. |
| `value` | `string` | Variable references $(VAR\_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | EnvVarSource represents a source for the value of an EnvVar. |

Show more

#### [3.1.182. .template.spec.initContainers[].env[].valueFrom](#template-spec-initcontainers-env-valuefrom) Copy linkLink copied to clipboard!

Description
:   EnvVarSource represents a source for the value of an EnvVar.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapKeyRef` | `object` | Selects a key from a ConfigMap. |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `fileKeyRef` | `object` | FileKeySelector selects a key of the env file. |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |
| `secretKeyRef` | `object` | SecretKeySelector selects a key of a Secret. |

Show more

#### [3.1.183. .template.spec.initContainers[].env[].valueFrom.configMapKeyRef](#template-spec-initcontainers-env-valuefrom-configmapkeyref) Copy linkLink copied to clipboard!

Description
:   Selects a key from a ConfigMap.

Type
:   `object`

Required
:   * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

Show more

#### [3.1.184. .template.spec.initContainers[].env[].valueFrom.fieldRef](#template-spec-initcontainers-env-valuefrom-fieldref) Copy linkLink copied to clipboard!

Description
:   ObjectFieldSelector selects an APIVersioned field of an object.

Type
:   `object`

Required
:   * `fieldPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

Show more

#### [3.1.185. .template.spec.initContainers[].env[].valueFrom.fileKeyRef](#template-spec-initcontainers-env-valuefrom-filekeyref) Copy linkLink copied to clipboard!

Description
:   FileKeySelector selects a key of the env file.

Type
:   `object`

Required
:   * `volumeName`
    * `path`
    * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters. |
| `optional` | `boolean` | Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod’s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation. |
| `path` | `string` | The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'. |
| `volumeName` | `string` | The name of the volume mount containing the env file. |

Show more

#### [3.1.186. .template.spec.initContainers[].env[].valueFrom.resourceFieldRef](#template-spec-initcontainers-env-valuefrom-resourcefieldref) Copy linkLink copied to clipboard!

Description
:   ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

Show more

#### [3.1.187. .template.spec.initContainers[].env[].valueFrom.secretKeyRef](#template-spec-initcontainers-env-valuefrom-secretkeyref) Copy linkLink copied to clipboard!

Description
:   SecretKeySelector selects a key of a Secret.

Type
:   `object`

Required
:   * `key`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

Show more

#### [3.1.188. .template.spec.initContainers[].envFrom](#template-spec-initcontainers-envfrom) Copy linkLink copied to clipboard!

Description
:   List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
:   `array`

#### [3.1.189. .template.spec.initContainers[].envFrom[]](#template-spec-initcontainers-envfrom-2) Copy linkLink copied to clipboard!

Description
:   EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapRef` | `object` | ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.  The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables. |
| `prefix` | `string` | Optional text to prepend to the name of each environment variable. May consist of any printable ASCII characters except '='. |
| `secretRef` | `object` | SecretEnvSource selects a Secret to populate the environment variables with.  The contents of the target Secret’s Data field will represent the key-value pairs as environment variables. |

Show more

#### [3.1.190. .template.spec.initContainers[].envFrom[].configMapRef](#template-spec-initcontainers-envfrom-configmapref) Copy linkLink copied to clipboard!

Description
:   ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

Show more

#### [3.1.191. .template.spec.initContainers[].envFrom[].secretRef](#template-spec-initcontainers-envfrom-secretref) Copy linkLink copied to clipboard!

Description
:   SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

Show more

#### [3.1.192. .template.spec.initContainers[].lifecycle](#template-spec-initcontainers-lifecycle) Copy linkLink copied to clipboard!

Description
:   Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `postStart` | `object` | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. |
| `preStop` | `object` | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. |
| `stopSignal` | `string` | StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name  Possible enum values: - `"SIGABRT"` - `"SIGALRM"` - `"SIGBUS"` - `"SIGCHLD"` - `"SIGCLD"` - `"SIGCONT"` - `"SIGFPE"` - `"SIGHUP"` - `"SIGILL"` - `"SIGINT"` - `"SIGIO"` - `"SIGIOT"` - `"SIGKILL"` - `"SIGPIPE"` - `"SIGPOLL"` - `"SIGPROF"` - `"SIGPWR"` - `"SIGQUIT"` - `"SIGRTMAX"` - `"SIGRTMAX-1"` - `"SIGRTMAX-10"` - `"SIGRTMAX-11"` - `"SIGRTMAX-12"` - `"SIGRTMAX-13"` - `"SIGRTMAX-14"` - `"SIGRTMAX-2"` - `"SIGRTMAX-3"` - `"SIGRTMAX-4"` - `"SIGRTMAX-5"` - `"SIGRTMAX-6"` - `"SIGRTMAX-7"` - `"SIGRTMAX-8"` - `"SIGRTMAX-9"` - `"SIGRTMIN"` - `"SIGRTMIN+1"` - `"SIGRTMIN+10"` - `"SIGRTMIN+11"` - `"SIGRTMIN+12"` - `"SIGRTMIN+13"` - `"SIGRTMIN+14"` - `"SIGRTMIN+15"` - `"SIGRTMIN+2"` - `"SIGRTMIN+3"` - `"SIGRTMIN+4"` - `"SIGRTMIN+5"` - `"SIGRTMIN+6"` - `"SIGRTMIN+7"` - `"SIGRTMIN+8"` - `"SIGRTMIN+9"` - `"SIGSEGV"` - `"SIGSTKFLT"` - `"SIGSTOP"` - `"SIGSYS"` - `"SIGTERM"` - `"SIGTRAP"` - `"SIGTSTP"` - `"SIGTTIN"` - `"SIGTTOU"` - `"SIGURG"` - `"SIGUSR1"` - `"SIGUSR2"` - `"SIGVTALRM"` - `"SIGWINCH"` - `"SIGXCPU"` - `"SIGXFSZ"` |

Show more

#### [3.1.193. .template.spec.initContainers[].lifecycle.postStart](#template-spec-initcontainers-lifecycle-poststart) Copy linkLink copied to clipboard!

Description
:   LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

Show more

#### [3.1.194. .template.spec.initContainers[].lifecycle.postStart.exec](#template-spec-initcontainers-lifecycle-poststart-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.195. .template.spec.initContainers[].lifecycle.postStart.httpGet](#template-spec-initcontainers-lifecycle-poststart-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.196. .template.spec.initContainers[].lifecycle.postStart.httpGet.httpHeaders](#template-spec-initcontainers-lifecycle-poststart-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.197. .template.spec.initContainers[].lifecycle.postStart.httpGet.httpHeaders[]](#template-spec-initcontainers-lifecycle-poststart-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.198. .template.spec.initContainers[].lifecycle.postStart.sleep](#template-spec-initcontainers-lifecycle-poststart-sleep) Copy linkLink copied to clipboard!

Description
:   SleepAction describes a "sleep" action.

Type
:   `object`

Required
:   * `seconds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

Show more

#### [3.1.199. .template.spec.initContainers[].lifecycle.postStart.tcpSocket](#template-spec-initcontainers-lifecycle-poststart-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.200. .template.spec.initContainers[].lifecycle.preStop](#template-spec-initcontainers-lifecycle-prestop) Copy linkLink copied to clipboard!

Description
:   LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

Show more

#### [3.1.201. .template.spec.initContainers[].lifecycle.preStop.exec](#template-spec-initcontainers-lifecycle-prestop-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.202. .template.spec.initContainers[].lifecycle.preStop.httpGet](#template-spec-initcontainers-lifecycle-prestop-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.203. .template.spec.initContainers[].lifecycle.preStop.httpGet.httpHeaders](#template-spec-initcontainers-lifecycle-prestop-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.204. .template.spec.initContainers[].lifecycle.preStop.httpGet.httpHeaders[]](#template-spec-initcontainers-lifecycle-prestop-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.205. .template.spec.initContainers[].lifecycle.preStop.sleep](#template-spec-initcontainers-lifecycle-prestop-sleep) Copy linkLink copied to clipboard!

Description
:   SleepAction describes a "sleep" action.

Type
:   `object`

Required
:   * `seconds`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

Show more

#### [3.1.206. .template.spec.initContainers[].lifecycle.preStop.tcpSocket](#template-spec-initcontainers-lifecycle-prestop-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.207. .template.spec.initContainers[].livenessProbe](#template-spec-initcontainers-livenessprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.208. .template.spec.initContainers[].livenessProbe.exec](#template-spec-initcontainers-livenessprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.209. .template.spec.initContainers[].livenessProbe.grpc](#template-spec-initcontainers-livenessprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.210. .template.spec.initContainers[].livenessProbe.httpGet](#template-spec-initcontainers-livenessprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.211. .template.spec.initContainers[].livenessProbe.httpGet.httpHeaders](#template-spec-initcontainers-livenessprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.212. .template.spec.initContainers[].livenessProbe.httpGet.httpHeaders[]](#template-spec-initcontainers-livenessprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.213. .template.spec.initContainers[].livenessProbe.tcpSocket](#template-spec-initcontainers-livenessprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.214. .template.spec.initContainers[].ports](#template-spec-initcontainers-ports) Copy linkLink copied to clipboard!

Description
:   List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.

Type
:   `array`

#### [3.1.215. .template.spec.initContainers[].ports[]](#template-spec-initcontainers-ports-2) Copy linkLink copied to clipboard!

Description
:   ContainerPort represents a network port in a single container.

Type
:   `object`

Required
:   * `containerPort`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerPort` | `integer` | Number of port to expose on the pod’s IP address. This must be a valid port number, 0 < x < 65536. |
| `hostIP` | `string` | What host IP to bind the external port to. |
| `hostPort` | `integer` | Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. |
| `name` | `string` | If specified, this must be an IANA\_SVC\_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. |
| `protocol` | `string` | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".  Possible enum values: - `"SCTP"` is the SCTP protocol. - `"TCP"` is the TCP protocol. - `"UDP"` is the UDP protocol. |

Show more

#### [3.1.216. .template.spec.initContainers[].readinessProbe](#template-spec-initcontainers-readinessprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.217. .template.spec.initContainers[].readinessProbe.exec](#template-spec-initcontainers-readinessprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.218. .template.spec.initContainers[].readinessProbe.grpc](#template-spec-initcontainers-readinessprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.219. .template.spec.initContainers[].readinessProbe.httpGet](#template-spec-initcontainers-readinessprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.220. .template.spec.initContainers[].readinessProbe.httpGet.httpHeaders](#template-spec-initcontainers-readinessprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.221. .template.spec.initContainers[].readinessProbe.httpGet.httpHeaders[]](#template-spec-initcontainers-readinessprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.222. .template.spec.initContainers[].readinessProbe.tcpSocket](#template-spec-initcontainers-readinessprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.223. .template.spec.initContainers[].resizePolicy](#template-spec-initcontainers-resizepolicy) Copy linkLink copied to clipboard!

Description
:   Resources resize policy for the container. This field cannot be set on ephemeral containers.

Type
:   `array`

#### [3.1.224. .template.spec.initContainers[].resizePolicy[]](#template-spec-initcontainers-resizepolicy-2) Copy linkLink copied to clipboard!

Description
:   ContainerResizePolicy represents resource resize policy for the container.

Type
:   `object`

Required
:   * `resourceName`
    * `restartPolicy`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

Show more

#### [3.1.225. .template.spec.initContainers[].resources](#template-spec-initcontainers-resources) Copy linkLink copied to clipboard!

Description
:   ResourceRequirements describes the compute resource requirements.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claims` | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. |
| `claims[]` | `object` | ResourceClaim references one entry in PodSpec.ResourceClaims. |
| `limits` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [3.1.226. .template.spec.initContainers[].resources.claims](#template-spec-initcontainers-resources-claims) Copy linkLink copied to clipboard!

Description
:   Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This field depends on the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.

Type
:   `array`

#### [3.1.227. .template.spec.initContainers[].resources.claims[]](#template-spec-initcontainers-resources-claims-2) Copy linkLink copied to clipboard!

Description
:   ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

Show more

#### [3.1.228. .template.spec.initContainers[].restartPolicyRules](#template-spec-initcontainers-restartpolicyrules) Copy linkLink copied to clipboard!

Description
:   Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy.

Type
:   `array`

#### [3.1.229. .template.spec.initContainers[].restartPolicyRules[]](#template-spec-initcontainers-restartpolicyrules-2) Copy linkLink copied to clipboard!

Description
:   ContainerRestartRule describes how a container exit is handled.

Type
:   `object`

Required
:   * `action`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `action` | `string` | Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is "Restart" to restart the container. |
| `exitCodes` | `object` | ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes. |

Show more

#### [3.1.230. .template.spec.initContainers[].restartPolicyRules[].exitCodes](#template-spec-initcontainers-restartpolicyrules-exitcodes) Copy linkLink copied to clipboard!

Description
:   ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes.

Type
:   `object`

Required
:   * `operator`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `operator` | `string` | Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the set of specified values. - NotIn: the requirement is satisfied if the container exit code is not in the set of specified values. |
| `values` | `array (integer)` | Specifies the set of values to check for container exit codes. At most 255 elements are allowed. |

Show more

#### [3.1.231. .template.spec.initContainers[].securityContext](#template-spec-initcontainers-securitycontext) Copy linkLink copied to clipboard!

Description
:   SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowPrivilegeEscalation` | `boolean` | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no\_new\_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP\_SYS\_ADMIN Note that this field cannot be set when spec.os.name is windows. |
| `appArmorProfile` | `object` | AppArmorProfile defines a pod or container’s AppArmor settings. |
| `capabilities` | `object` | Adds and removes POSIX capabilities from running containers. |
| `privileged` | `boolean` | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. |
| `procMount` | `string` | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.  Possible enum values: - `"Default"` uses the container runtime defaults for readonly and masked paths for /proc. Most container runtimes mask certain paths in /proc to avoid accidental security exposure of special devices or information. - `"Unmasked"` bypasses the default masking behavior of the container runtime and ensures the newly created /proc the container stays in tact with no modifications. |
| `readOnlyRootFilesystem` | `boolean` | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | SELinuxOptions are the labels to be applied to the container |
| `seccompProfile` | `object` | SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set. |
| `windowsOptions` | `object` | WindowsSecurityContextOptions contain Windows-specific options and credentials. |

Show more

#### [3.1.232. .template.spec.initContainers[].securityContext.appArmorProfile](#template-spec-initcontainers-securitycontext-apparmorprofile) Copy linkLink copied to clipboard!

Description
:   AppArmorProfile defines a pod or container’s AppArmor settings.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.  Possible enum values: - `"Localhost"` indicates that a profile pre-loaded on the node should be used. - `"RuntimeDefault"` indicates that the container runtime’s default AppArmor profile should be used. - `"Unconfined"` indicates that no AppArmor profile should be enforced. |

Show more

#### [3.1.233. .template.spec.initContainers[].securityContext.capabilities](#template-spec-initcontainers-securitycontext-capabilities) Copy linkLink copied to clipboard!

Description
:   Adds and removes POSIX capabilities from running containers.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `add` | `array (string)` | Added capabilities |
| `drop` | `array (string)` | Removed capabilities |

Show more

#### [3.1.234. .template.spec.initContainers[].securityContext.seLinuxOptions](#template-spec-initcontainers-securitycontext-selinuxoptions) Copy linkLink copied to clipboard!

Description
:   SELinuxOptions are the labels to be applied to the container

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

Show more

#### [3.1.235. .template.spec.initContainers[].securityContext.seccompProfile](#template-spec-initcontainers-securitycontext-seccompprofile) Copy linkLink copied to clipboard!

Description
:   SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. |
| `type` | `string` | type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.  Possible enum values: - `"Localhost"` indicates a profile defined in a file on the node should be used. The file’s location relative to <kubelet-root-dir>/seccomp. - `"RuntimeDefault"` represents the default container runtime seccomp profile. - `"Unconfined"` indicates no seccomp profile is applied (A.K.A. unconfined). |

Show more

#### [3.1.236. .template.spec.initContainers[].securityContext.windowsOptions](#template-spec-initcontainers-securitycontext-windowsoptions) Copy linkLink copied to clipboard!

Description
:   WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

Show more

#### [3.1.237. .template.spec.initContainers[].startupProbe](#template-spec-initcontainers-startupprobe) Copy linkLink copied to clipboard!

Description
:   Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

Show more

#### [3.1.238. .template.spec.initContainers[].startupProbe.exec](#template-spec-initcontainers-startupprobe-exec) Copy linkLink copied to clipboard!

Description
:   ExecAction describes a "run in container" action.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

Show more

#### [3.1.239. .template.spec.initContainers[].startupProbe.grpc](#template-spec-initcontainers-startupprobe-grpc) Copy linkLink copied to clipboard!

Description
:   GRPCAction specifies an action involving a GRPC service.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `port` | `integer` | Port number of the gRPC service. Number must be in the range 1 to 65535. |
| `service` | `string` | Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC. |

Show more

#### [3.1.240. .template.spec.initContainers[].startupProbe.httpGet](#template-spec-initcontainers-startupprobe-httpget) Copy linkLink copied to clipboard!

Description
:   HTTPGetAction describes an action based on HTTP Get requests.

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. |
| `httpHeaders` | `array` | Custom headers to set in the request. HTTP allows repeated headers. |
| `httpHeaders[]` | `object` | HTTPHeader describes a custom header to be used in HTTP probes |
| `path` | `string` | Path to access on the HTTP server. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |
| `scheme` | `string` | Scheme to use for connecting to the host. Defaults to HTTP.  Possible enum values: - `"HTTP"` means that the scheme used will be http:// - `"HTTPS"` means that the scheme used will be https:// |

Show more

#### [3.1.241. .template.spec.initContainers[].startupProbe.httpGet.httpHeaders](#template-spec-initcontainers-startupprobe-httpget-httpheaders) Copy linkLink copied to clipboard!

Description
:   Custom headers to set in the request. HTTP allows repeated headers.

Type
:   `array`

#### [3.1.242. .template.spec.initContainers[].startupProbe.httpGet.httpHeaders[]](#template-spec-initcontainers-startupprobe-httpget-httpheaders-2) Copy linkLink copied to clipboard!

Description
:   HTTPHeader describes a custom header to be used in HTTP probes

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

Show more

#### [3.1.243. .template.spec.initContainers[].startupProbe.tcpSocket](#template-spec-initcontainers-startupprobe-tcpsocket) Copy linkLink copied to clipboard!

Description
:   TCPSocketAction describes an action based on opening a socket

Type
:   `object`

Required
:   * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA\_SVC\_NAME. |

Show more

#### [3.1.244. .template.spec.initContainers[].volumeDevices](#template-spec-initcontainers-volumedevices) Copy linkLink copied to clipboard!

Description
:   volumeDevices is the list of block devices to be used by the container.

Type
:   `array`

#### [3.1.245. .template.spec.initContainers[].volumeDevices[]](#template-spec-initcontainers-volumedevices-2) Copy linkLink copied to clipboard!

Description
:   volumeDevice describes a mapping of a raw block device within a container.

Type
:   `object`

Required
:   * `name`
    * `devicePath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

Show more

#### [3.1.246. .template.spec.initContainers[].volumeMounts](#template-spec-initcontainers-volumemounts) Copy linkLink copied to clipboard!

Description
:   Pod volumes to mount into the container’s filesystem. Cannot be updated.

Type
:   `array`

#### [3.1.247. .template.spec.initContainers[].volumeMounts[]](#template-spec-initcontainers-volumemounts-2) Copy linkLink copied to clipboard!

Description
:   VolumeMount describes a mounting of a Volume within a container.

Type
:   `object`

Required
:   * `name`
    * `mountPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mountPath` | `string` | Path within the container at which the volume should be mounted. Must not contain ':'. |
| `mountPropagation` | `string` | mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).  Possible enum values: - `"Bidirectional"` means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rshared" in Linux terminology). - `"HostToContainer"` means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rslave" in Linux terminology). - `"None"` means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode corresponds to "private" in Linux terminology. |
| `name` | `string` | This must match the Name of a Volume. |
| `readOnly` | `boolean` | Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. |
| `recursiveReadOnly` | `string` | RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled. |
| `subPath` | `string` | Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root). |
| `subPathExpr` | `string` | Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR\_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive. |

Show more

#### [3.1.248. .template.spec.os](#template-spec-os) Copy linkLink copied to clipboard!

Description
:   PodOS defines the OS parameters of a pod.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: <https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration> Clients should expect to handle additional values and treat unrecognized values in this field as os: null |

Show more

#### [3.1.249. .template.spec.readinessGates](#template-spec-readinessgates) Copy linkLink copied to clipboard!

Description
:   If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: <https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates>

Type
:   `array`

#### [3.1.250. .template.spec.readinessGates[]](#template-spec-readinessgates-2) Copy linkLink copied to clipboard!

Description
:   PodReadinessGate contains the reference to a pod condition

Type
:   `object`

Required
:   * `conditionType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditionType` | `string` | ConditionType refers to a condition in the pod’s condition list with matching type. |

Show more

#### [3.1.251. .template.spec.resourceClaims](#template-spec-resourceclaims) Copy linkLink copied to clipboard!

Description
:   ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.

    This is a stable field but requires that the DynamicResourceAllocation feature gate is enabled.

    This field is immutable.

Type
:   `array`

#### [3.1.252. .template.spec.resourceClaims[]](#template-spec-resourceclaims-2) Copy linkLink copied to clipboard!

Description
:   PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.

    It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name uniquely identifies this resource claim inside the pod. This must be a DNS\_LABEL. |
| `resourceClaimName` | `string` | ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. |
| `resourceClaimTemplateName` | `string` | ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. |

Show more

#### [3.1.253. .template.spec.resources](#template-spec-resources) Copy linkLink copied to clipboard!

Description
:   ResourceRequirements describes the compute resource requirements.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claims` | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. |
| `claims[]` | `object` | ResourceClaim references one entry in PodSpec.ResourceClaims. |
| `limits` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [3.1.254. .template.spec.resources.claims](#template-spec-resources-claims) Copy linkLink copied to clipboard!

Description
:   Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This field depends on the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.

Type
:   `array`

#### [3.1.255. .template.spec.resources.claims[]](#template-spec-resources-claims-2) Copy linkLink copied to clipboard!

Description
:   ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

Show more

#### [3.1.256. .template.spec.schedulingGates](#template-spec-schedulinggates) Copy linkLink copied to clipboard!

Description
:   SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.

    SchedulingGates can only be set at pod creation time, and be removed only afterwards.

Type
:   `array`

#### [3.1.257. .template.spec.schedulingGates[]](#template-spec-schedulinggates-2) Copy linkLink copied to clipboard!

Description
:   PodSchedulingGate is associated to a Pod to guard its scheduling.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the scheduling gate. Each scheduling gate must have a unique name field. |

Show more

#### [3.1.258. .template.spec.securityContext](#template-spec-securitycontext) Copy linkLink copied to clipboard!

Description
:   PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext. Field values of container.securityContext take precedence over field values of PodSecurityContext.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `appArmorProfile` | `object` | AppArmorProfile defines a pod or container’s AppArmor settings. |
| `fsGroup` | `integer` | A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR’d with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows. |
| `fsGroupChangePolicy` | `string` | fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.  Possible enum values: - `"Always"` indicates that volume’s ownership and permissions should always be changed whenever volume is mounted inside a Pod. This the default behavior. - `"OnRootMismatch"` indicates that volume’s ownership and permissions will be changed only when permission and ownership of root directory does not match with expected permissions on the volume. This can help shorten the time it takes to change ownership and permissions of a volume. |
| `runAsGroup` | `integer` | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. |
| `runAsNonRoot` | `boolean` | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |
| `runAsUser` | `integer` | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxChangePolicy` | `string` | seLinuxChangePolicy defines how the container’s SELinux label is applied to all volumes used by the Pod. It has no effect on nodes that do not support SELinux or to volumes does not support SELinux. Valid values are "MountOption" and "Recursive".  "Recursive" means relabeling of all files on all Pod volumes by the container runtime. This may be slow for large volumes, but allows mixing privileged and unprivileged Pods sharing the same volume on the same node.  "MountOption" mounts all eligible Pod volumes with `-o context` mount option. This requires all Pods that share the same volume to use the same SELinux label. It is not possible to share the same volume among privileged and unprivileged Pods. Eligible volumes are in-tree FibreChannel and iSCSI volumes, and all CSI volumes whose CSI driver announces SELinux support by setting spec.seLinuxMount: true in their CSIDriver instance. Other volumes are always re-labelled recursively. "MountOption" value is allowed only when SELinuxMount feature gate is enabled.  If not specified and SELinuxMount feature gate is enabled, "MountOption" is used. If not specified and SELinuxMount feature gate is disabled, "MountOption" is used for ReadWriteOncePod volumes and "Recursive" for all other volumes.  This field affects only Pods that have SELinux label set, either in PodSecurityContext or in SecurityContext of all containers.  All Pods that use the same volume should use the same seLinuxChangePolicy, otherwise some pods can get stuck in ContainerCreating state. Note that this field cannot be set when spec.os.name is windows. |
| `seLinuxOptions` | `object` | SELinuxOptions are the labels to be applied to the container |
| `seccompProfile` | `object` | SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set. |
| `supplementalGroups` | `array (integer)` | A list of groups applied to the first process run in each container, in addition to the container’s primary GID and fsGroup (if specified). If the SupplementalGroupsPolicy feature is enabled, the supplementalGroupsPolicy field determines whether these are in addition to or instead of any group memberships defined in the container image. If unspecified, no additional groups are added, though group memberships defined in the container image may still be used, depending on the supplementalGroupsPolicy field. Note that this field cannot be set when spec.os.name is windows. |
| `supplementalGroupsPolicy` | `string` | Defines how supplemental groups of the first container processes are calculated. Valid values are "Merge" and "Strict". If not specified, "Merge" is used. (Alpha) Using the field requires the SupplementalGroupsPolicy feature gate to be enabled and the container runtime must implement support for this feature. Note that this field cannot be set when spec.os.name is windows.  Possible enum values: - `"Merge"` means that the container’s provided SupplementalGroups and FsGroup (specified in SecurityContext) will be merged with the primary user’s groups as defined in the container image (in /etc/group). - `"Strict"` means that the container’s provided SupplementalGroups and FsGroup (specified in SecurityContext) will be used instead of any groups defined in the container image. |
| `sysctls` | `array` | Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. |
| `sysctls[]` | `object` | Sysctl defines a kernel parameter to be set |
| `windowsOptions` | `object` | WindowsSecurityContextOptions contain Windows-specific options and credentials. |

Show more

#### [3.1.259. .template.spec.securityContext.appArmorProfile](#template-spec-securitycontext-apparmorprofile) Copy linkLink copied to clipboard!

Description
:   AppArmorProfile defines a pod or container’s AppArmor settings.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". |
| `type` | `string` | type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.  Possible enum values: - `"Localhost"` indicates that a profile pre-loaded on the node should be used. - `"RuntimeDefault"` indicates that the container runtime’s default AppArmor profile should be used. - `"Unconfined"` indicates that no AppArmor profile should be enforced. |

Show more

#### [3.1.260. .template.spec.securityContext.seLinuxOptions](#template-spec-securitycontext-selinuxoptions) Copy linkLink copied to clipboard!

Description
:   SELinuxOptions are the labels to be applied to the container

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

Show more

#### [3.1.261. .template.spec.securityContext.seccompProfile](#template-spec-securitycontext-seccompprofile) Copy linkLink copied to clipboard!

Description
:   SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `localhostProfile` | `string` | localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. |
| `type` | `string` | type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.  Possible enum values: - `"Localhost"` indicates a profile defined in a file on the node should be used. The file’s location relative to <kubelet-root-dir>/seccomp. - `"RuntimeDefault"` represents the default container runtime seccomp profile. - `"Unconfined"` indicates no seccomp profile is applied (A.K.A. unconfined). |

Show more

#### [3.1.262. .template.spec.securityContext.sysctls](#template-spec-securitycontext-sysctls) Copy linkLink copied to clipboard!

Description
:   Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.

Type
:   `array`

#### [3.1.263. .template.spec.securityContext.sysctls[]](#template-spec-securitycontext-sysctls-2) Copy linkLink copied to clipboard!

Description
:   Sysctl defines a kernel parameter to be set

Type
:   `object`

Required
:   * `name`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of a property to set |
| `value` | `string` | Value of a property to set |

Show more

#### [3.1.264. .template.spec.securityContext.windowsOptions](#template-spec-securitycontext-windowsoptions) Copy linkLink copied to clipboard!

Description
:   WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

Show more

#### [3.1.265. .template.spec.tolerations](#template-spec-tolerations) Copy linkLink copied to clipboard!

Description
:   If specified, the pod’s tolerations.

Type
:   `array`

#### [3.1.266. .template.spec.tolerations[]](#template-spec-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController. - `"NoSchedule"` Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler. - `"PreferNoSchedule"` Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators).  Possible enum values: - `"Equal"` - `"Exists"` - `"Gt"` - `"Lt"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

Show more

#### [3.1.267. .template.spec.topologySpreadConstraints](#template-spec-topologyspreadconstraints) Copy linkLink copied to clipboard!

Description
:   TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.

Type
:   `array`

#### [3.1.268. .template.spec.topologySpreadConstraints[]](#template-spec-topologyspreadconstraints-2) Copy linkLink copied to clipboard!

Description
:   TopologySpreadConstraint specifies how to spread matching pods among the given topology.

Type
:   `object`

Required
:   * `maxSkew`
    * `topologyKey`
    * `whenUnsatisfiable`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `labelSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn’t set. Keys that don’t exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default). |
| `maxSkew` | `integer` | MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | | P P | P P | P | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It’s a required field. Default value is 1 and 0 is not allowed. |
| `minDomains` | `integer` | MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won’t schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | | P P | P P | P P | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew. |
| `nodeAffinityPolicy` | `string` | NodeAffinityPolicy indicates how we will treat Pod’s nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy.  Possible enum values: - `"Honor"` means use this scheduling directive when calculating pod topology spread skew. - `"Ignore"` means ignore this scheduling directive when calculating pod topology spread skew. |
| `nodeTaintsPolicy` | `string` | NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy.  Possible enum values: - `"Honor"` means use this scheduling directive when calculating pod topology spread skew. - `"Ignore"` means ignore this scheduling directive when calculating pod topology spread skew. |
| `topologyKey` | `string` | TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It’s a required field. |
| `whenUnsatisfiable` | `string` | WhenUnsatisfiable indicates how to deal with a pod if it doesn’t satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P | P | P | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won’t make it **more** imbalanced. It’s a required field.  Possible enum values: - `"DoNotSchedule"` instructs the scheduler not to schedule the pod when constraints are not satisfied. - `"ScheduleAnyway"` instructs the scheduler to schedule the pod even if constraints are not satisfied. |

Show more

#### [3.1.269. .template.spec.volumes](#template-spec-volumes) Copy linkLink copied to clipboard!

Description
:   List of volumes that can be mounted by containers belonging to the pod. More info: <https://kubernetes.io/docs/concepts/storage/volumes>

Type
:   `array`

#### [3.1.270. .template.spec.volumes[]](#template-spec-volumes-2) Copy linkLink copied to clipboard!

Description
:   Volume represents a named volume in a pod that may be accessed by any container in the pod.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `awsElasticBlockStore` | `object` | Represents a Persistent Disk resource in AWS.  An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling. |
| `azureDisk` | `object` | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. |
| `azureFile` | `object` | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. |
| `cephfs` | `object` | Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling. |
| `cinder` | `object` | Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling. |
| `configMap` | `object` | Adapts a ConfigMap into a volume.  The contents of the target ConfigMap’s Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling. |
| `csi` | `object` | Represents a source location of a volume to mount, managed by an external CSI driver |
| `downwardAPI` | `object` | DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling. |
| `emptyDir` | `object` | Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling. |
| `ephemeral` | `object` | Represents an ephemeral volume that is handled by a normal storage driver. |
| `fc` | `object` | Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling. |
| `flexVolume` | `object` | FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. |
| `flocker` | `object` | Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling. |
| `gcePersistentDisk` | `object` | Represents a Persistent Disk resource in Google Compute Engine.  A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling. |
| `gitRepo` | `object` | Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.  DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container. |
| `glusterfs` | `object` | Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling. |
| `hostPath` | `object` | Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling. |
| `image` | `object` | ImageVolumeSource represents a image volume resource. |
| `iscsi` | `object` | Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling. |
| `name` | `string` | name of the volume. Must be a DNS\_LABEL and unique within the pod. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `nfs` | `object` | Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling. |
| `persistentVolumeClaim` | `object` | PersistentVolumeClaimVolumeSource references the user’s PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system). |
| `photonPersistentDisk` | `object` | Represents a Photon Controller persistent disk resource. |
| `portworxVolume` | `object` | PortworxVolumeSource represents a Portworx volume resource. |
| `projected` | `object` | Represents a projected volume source |
| `quobyte` | `object` | Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling. |
| `rbd` | `object` | Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling. |
| `scaleIO` | `object` | ScaleIOVolumeSource represents a persistent ScaleIO volume |
| `secret` | `object` | Adapts a Secret into a volume.  The contents of the target Secret’s Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling. |
| `storageos` | `object` | Represents a StorageOS persistent volume resource. |
| `vsphereVolume` | `object` | Represents a vSphere volume resource. |

Show more

#### [3.1.271. .template.spec.volumes[].awsElasticBlockStore](#template-spec-volumes-awselasticblockstore) Copy linkLink copied to clipboard!

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

#### [3.1.272. .template.spec.volumes[].azureDisk](#template-spec-volumes-azuredisk) Copy linkLink copied to clipboard!

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

#### [3.1.273. .template.spec.volumes[].azureFile](#template-spec-volumes-azurefile) Copy linkLink copied to clipboard!

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
| `shareName` | `string` | shareName is the azure share Name |

Show more

#### [3.1.274. .template.spec.volumes[].cephfs](#template-spec-volumes-cephfs) Copy linkLink copied to clipboard!

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
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `user` | `string` | user is optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |

Show more

#### [3.1.275. .template.spec.volumes[].cephfs.secretRef](#template-spec-volumes-cephfs-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.276. .template.spec.volumes[].cinder](#template-spec-volumes-cinder) Copy linkLink copied to clipboard!

Description
:   Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.

Type
:   `object`

Required
:   * `volumeID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `volumeID` | `string` | volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |

Show more

#### [3.1.277. .template.spec.volumes[].cinder.secretRef](#template-spec-volumes-cinder-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.278. .template.spec.volumes[].configMap](#template-spec-volumes-configmap) Copy linkLink copied to clipboard!

Description
:   Adapts a ConfigMap into a volume.

    The contents of the target ConfigMap’s Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultMode` | `integer` | defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

Show more

#### [3.1.279. .template.spec.volumes[].configMap.items](#template-spec-volumes-configmap-items) Copy linkLink copied to clipboard!

Description
:   items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
:   `array`

#### [3.1.280. .template.spec.volumes[].configMap.items[]](#template-spec-volumes-configmap-items-2) Copy linkLink copied to clipboard!

Description
:   Maps a string key to a path within a volume.

Type
:   `object`

Required
:   * `key`
    * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

Show more

#### [3.1.281. .template.spec.volumes[].csi](#template-spec-volumes-csi) Copy linkLink copied to clipboard!

Description
:   Represents a source location of a volume to mount, managed by an external CSI driver

Type
:   `object`

Required
:   * `driver`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. |
| `fsType` | `string` | fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. |
| `nodePublishSecretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `readOnly` | `boolean` | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver’s documentation for supported values. |

Show more

#### [3.1.282. .template.spec.volumes[].csi.nodePublishSecretRef](#template-spec-volumes-csi-nodepublishsecretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.283. .template.spec.volumes[].downwardAPI](#template-spec-volumes-downwardapi) Copy linkLink copied to clipboard!

Description
:   DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultMode` | `integer` | Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | Items is a list of downward API volume file |
| `items[]` | `object` | DownwardAPIVolumeFile represents information to create the file containing the pod field |

Show more

#### [3.1.284. .template.spec.volumes[].downwardAPI.items](#template-spec-volumes-downwardapi-items) Copy linkLink copied to clipboard!

Description
:   Items is a list of downward API volume file

Type
:   `array`

#### [3.1.285. .template.spec.volumes[].downwardAPI.items[]](#template-spec-volumes-downwardapi-items-2) Copy linkLink copied to clipboard!

Description
:   DownwardAPIVolumeFile represents information to create the file containing the pod field

Type
:   `object`

Required
:   * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `mode` | `integer` | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |

Show more

#### [3.1.286. .template.spec.volumes[].downwardAPI.items[].fieldRef](#template-spec-volumes-downwardapi-items-fieldref) Copy linkLink copied to clipboard!

Description
:   ObjectFieldSelector selects an APIVersioned field of an object.

Type
:   `object`

Required
:   * `fieldPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

Show more

#### [3.1.287. .template.spec.volumes[].downwardAPI.items[].resourceFieldRef](#template-spec-volumes-downwardapi-items-resourcefieldref) Copy linkLink copied to clipboard!

Description
:   ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

Show more

#### [3.1.288. .template.spec.volumes[].emptyDir](#template-spec-volumes-emptydir) Copy linkLink copied to clipboard!

Description
:   Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `medium` | `string` | medium represents what type of storage medium should back this directory. The default is "" which means to use the node’s default medium. Must be an empty string (default) or Memory. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |
| `sizeLimit` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |

Show more

#### [3.1.289. .template.spec.volumes[].ephemeral](#template-spec-volumes-ephemeral) Copy linkLink copied to clipboard!

Description
:   Represents an ephemeral volume that is handled by a normal storage driver.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `volumeClaimTemplate` | `object` | PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource. |

Show more

#### [3.1.290. .template.spec.volumes[].ephemeral.volumeClaimTemplate](#template-spec-volumes-ephemeral-volumeclaimtemplate) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource.

Type
:   `object`

Required
:   * `spec`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |

Show more

#### [3.1.291. .template.spec.volumes[].ephemeral.volumeClaimTemplate.spec](#template-spec-volumes-ephemeral-volumeclaimtemplate-spec) Copy linkLink copied to clipboard!

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

#### [3.1.292. .template.spec.volumes[].ephemeral.volumeClaimTemplate.spec.dataSource](#template-spec-volumes-ephemeral-volumeclaimtemplate-spec-datasource) Copy linkLink copied to clipboard!

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

#### [3.1.293. .template.spec.volumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef](#template-spec-volumes-ephemeral-volumeclaimtemplate-spec-datasourceref) Copy linkLink copied to clipboard!

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

#### [3.1.294. .template.spec.volumes[].ephemeral.volumeClaimTemplate.spec.resources](#template-spec-volumes-ephemeral-volumeclaimtemplate-spec-resources) Copy linkLink copied to clipboard!

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

#### [3.1.295. .template.spec.volumes[].fc](#template-spec-volumes-fc) Copy linkLink copied to clipboard!

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

#### [3.1.296. .template.spec.volumes[].flexVolume](#template-spec-volumes-flexvolume) Copy linkLink copied to clipboard!

Description
:   FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.

Type
:   `object`

Required
:   * `driver`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | driver is the name of the driver to use for this volume. |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. |
| `options` | `object (string)` | options is Optional: this field holds extra command options if any. |
| `readOnly` | `boolean` | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |

Show more

#### [3.1.297. .template.spec.volumes[].flexVolume.secretRef](#template-spec-volumes-flexvolume-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.298. .template.spec.volumes[].flocker](#template-spec-volumes-flocker) Copy linkLink copied to clipboard!

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

#### [3.1.299. .template.spec.volumes[].gcePersistentDisk](#template-spec-volumes-gcepersistentdisk) Copy linkLink copied to clipboard!

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

#### [3.1.300. .template.spec.volumes[].gitRepo](#template-spec-volumes-gitrepo) Copy linkLink copied to clipboard!

Description
:   Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container.

Type
:   `object`

Required
:   * `repository`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `directory` | `string` | directory is the target directory name. Must not contain or start with '..'. If '.' is supplied, the volume directory will be the git repository. Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. |
| `repository` | `string` | repository is the URL |
| `revision` | `string` | revision is the commit hash for the specified revision. |

Show more

#### [3.1.301. .template.spec.volumes[].glusterfs](#template-spec-volumes-glusterfs) Copy linkLink copied to clipboard!

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
| `endpoints` | `string` | endpoints is the endpoint name that details Glusterfs topology. |
| `path` | `string` | path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `readOnly` | `boolean` | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |

Show more

#### [3.1.302. .template.spec.volumes[].hostPath](#template-spec-volumes-hostpath) Copy linkLink copied to clipboard!

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

#### [3.1.303. .template.spec.volumes[].image](#template-spec-volumes-image) Copy linkLink copied to clipboard!

Description
:   ImageVolumeSource represents a image volume resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `pullPolicy` | `string` | Policy for pulling OCI objects. Possible values are: Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise.  Possible enum values: - `"Always"` means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - `"IfNotPresent"` means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - `"Never"` means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present |
| `reference` | `string` | Required: Image or artifact reference to be used. Behaves in the same way as pod.spec.containers[\*].image. Pull secrets will be assembled in the same way as for the container image by looking up node credentials, SA image pull secrets, and pod spec image pull secrets. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. |

Show more

#### [3.1.304. .template.spec.volumes[].iscsi](#template-spec-volumes-iscsi) Copy linkLink copied to clipboard!

Description
:   Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.

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
| `iqn` | `string` | iqn is the target iSCSI Qualified Name. |
| `iscsiInterface` | `string` | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). |
| `lun` | `integer` | lun represents iSCSI Target Lun number. |
| `portals` | `array (string)` | portals is the iSCSI Target Portal List. The portal is either an IP or ip\_addr:port if the port is other than default (typically TCP ports 860 and 3260). |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `targetPortal` | `string` | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip\_addr:port if the port is other than default (typically TCP ports 860 and 3260). |

Show more

#### [3.1.305. .template.spec.volumes[].iscsi.secretRef](#template-spec-volumes-iscsi-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.306. .template.spec.volumes[].nfs](#template-spec-volumes-nfs) Copy linkLink copied to clipboard!

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

#### [3.1.307. .template.spec.volumes[].persistentVolumeClaim](#template-spec-volumes-persistentvolumeclaim) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaimVolumeSource references the user’s PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system).

Type
:   `object`

Required
:   * `claimName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claimName` | `string` | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims> |
| `readOnly` | `boolean` | readOnly Will force the ReadOnly setting in VolumeMounts. Default false. |

Show more

#### [3.1.308. .template.spec.volumes[].photonPersistentDisk](#template-spec-volumes-photonpersistentdisk) Copy linkLink copied to clipboard!

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

#### [3.1.309. .template.spec.volumes[].portworxVolume](#template-spec-volumes-portworxvolume) Copy linkLink copied to clipboard!

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

#### [3.1.310. .template.spec.volumes[].projected](#template-spec-volumes-projected) Copy linkLink copied to clipboard!

Description
:   Represents a projected volume source

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultMode` | `integer` | defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `sources` | `array` | sources is the list of volume projections. Each entry in this list handles one source. |
| `sources[]` | `object` | Projection that may be projected along with other supported volume types. Exactly one of these fields must be set. |

Show more

#### [3.1.311. .template.spec.volumes[].projected.sources](#template-spec-volumes-projected-sources) Copy linkLink copied to clipboard!

Description
:   sources is the list of volume projections. Each entry in this list handles one source.

Type
:   `array`

#### [3.1.312. .template.spec.volumes[].projected.sources[]](#template-spec-volumes-projected-sources-2) Copy linkLink copied to clipboard!

Description
:   Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterTrustBundle` | `object` | ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem. |
| `configMap` | `object` | Adapts a ConfigMap into a projected volume.  The contents of the target ConfigMap’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode. |
| `downwardAPI` | `object` | Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode. |
| `podCertificate` | `object` | PodCertificateProjection provides a private key and X.509 certificate in the pod filesystem. |
| `secret` | `object` | Adapts a secret into a projected volume.  The contents of the target Secret’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode. |
| `serviceAccountToken` | `object` | ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise). |

Show more

#### [3.1.313. .template.spec.volumes[].projected.sources[].clusterTrustBundle](#template-spec-volumes-projected-sources-clustertrustbundle) Copy linkLink copied to clipboard!

Description
:   ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem.

Type
:   `object`

Required
:   * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `labelSelector` | [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything". |
| `name` | `string` | Select a single ClusterTrustBundle by object name. Mutually-exclusive with signerName and labelSelector. |
| `optional` | `boolean` | If true, don’t block pod startup if the referenced ClusterTrustBundle(s) aren’t available. If using name, then the named ClusterTrustBundle is allowed not to exist. If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. |
| `path` | `string` | Relative path from the volume root to write the bundle. |
| `signerName` | `string` | Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name. The contents of all selected ClusterTrustBundles will be unified and deduplicated. |

Show more

#### [3.1.314. .template.spec.volumes[].projected.sources[].configMap](#template-spec-volumes-projected-sources-configmap) Copy linkLink copied to clipboard!

Description
:   Adapts a ConfigMap into a projected volume.

    The contents of the target ConfigMap’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

Show more

#### [3.1.315. .template.spec.volumes[].projected.sources[].configMap.items](#template-spec-volumes-projected-sources-configmap-items) Copy linkLink copied to clipboard!

Description
:   items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
:   `array`

#### [3.1.316. .template.spec.volumes[].projected.sources[].configMap.items[]](#template-spec-volumes-projected-sources-configmap-items-2) Copy linkLink copied to clipboard!

Description
:   Maps a string key to a path within a volume.

Type
:   `object`

Required
:   * `key`
    * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

Show more

#### [3.1.317. .template.spec.volumes[].projected.sources[].downwardAPI](#template-spec-volumes-projected-sources-downwardapi) Copy linkLink copied to clipboard!

Description
:   Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `items` | `array` | Items is a list of DownwardAPIVolume file |
| `items[]` | `object` | DownwardAPIVolumeFile represents information to create the file containing the pod field |

Show more

#### [3.1.318. .template.spec.volumes[].projected.sources[].downwardAPI.items](#template-spec-volumes-projected-sources-downwardapi-items) Copy linkLink copied to clipboard!

Description
:   Items is a list of DownwardAPIVolume file

Type
:   `array`

#### [3.1.319. .template.spec.volumes[].projected.sources[].downwardAPI.items[]](#template-spec-volumes-projected-sources-downwardapi-items-2) Copy linkLink copied to clipboard!

Description
:   DownwardAPIVolumeFile represents information to create the file containing the pod field

Type
:   `object`

Required
:   * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `mode` | `integer` | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |

Show more

#### [3.1.320. .template.spec.volumes[].projected.sources[].downwardAPI.items[].fieldRef](#template-spec-volumes-projected-sources-downwardapi-items-fieldref) Copy linkLink copied to clipboard!

Description
:   ObjectFieldSelector selects an APIVersioned field of an object.

Type
:   `object`

Required
:   * `fieldPath`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

Show more

#### [3.1.321. .template.spec.volumes[].projected.sources[].downwardAPI.items[].resourceFieldRef](#template-spec-volumes-projected-sources-downwardapi-items-resourcefieldref) Copy linkLink copied to clipboard!

Description
:   ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

Show more

#### [3.1.322. .template.spec.volumes[].projected.sources[].podCertificate](#template-spec-volumes-projected-sources-podcertificate) Copy linkLink copied to clipboard!

Description
:   PodCertificateProjection provides a private key and X.509 certificate in the pod filesystem.

Type
:   `object`

Required
:   * `signerName`
    * `keyType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `certificateChainPath` | `string` | Write the certificate chain at this path in the projected volume.  Most applications should use credentialBundlePath. When using keyPath and certificateChainPath, your application needs to check that the key and leaf certificate are consistent, because it is possible to read the files mid-rotation. |
| `credentialBundlePath` | `string` | Write the credential bundle at this path in the projected volume.  The credential bundle is a single file that contains multiple PEM blocks. The first PEM block is a PRIVATE KEY block, containing a PKCS#8 private key.  The remaining blocks are CERTIFICATE blocks, containing the issued certificate chain from the signer (leaf and any intermediates).  Using credentialBundlePath lets your Pod’s application code make a single atomic read that retrieves a consistent key and certificate chain. If you project them to separate files, your application code will need to additionally check that the leaf certificate was issued to the key. |
| `keyPath` | `string` | Write the key at this path in the projected volume.  Most applications should use credentialBundlePath. When using keyPath and certificateChainPath, your application needs to check that the key and leaf certificate are consistent, because it is possible to read the files mid-rotation. |
| `keyType` | `string` | The type of keypair Kubelet will generate for the pod.  Valid values are "RSA3072", "RSA4096", "ECDSAP256", "ECDSAP384", "ECDSAP521", and "ED25519". |
| `maxExpirationSeconds` | `integer` | maxExpirationSeconds is the maximum lifetime permitted for the certificate.  Kubelet copies this value verbatim into the PodCertificateRequests it generates for this projection.  If omitted, kube-apiserver will set it to 86400(24 hours). kube-apiserver will reject values shorter than 3600 (1 hour). The maximum allowable value is 7862400 (91 days).  The signer implementation is then free to issue a certificate with any lifetime **shorter** than MaxExpirationSeconds, but no shorter than 3600 seconds (1 hour). This constraint is enforced by kube-apiserver. `kubernetes.io` signers will never issue certificates with a lifetime longer than 24 hours. |
| `signerName` | `string` | Kubelet’s generated CSRs will be addressed to this signer. |
| `userAnnotations` | `object (string)` | userAnnotations allow pod authors to pass additional information to the signer implementation. Kubernetes does not restrict or validate this metadata in any way.  These values are copied verbatim into the `spec.unverifiedUserAnnotations` field of the PodCertificateRequest objects that Kubelet creates.  Entries are subject to the same validation as object metadata annotations, with the addition that all keys must be domain-prefixed. No restrictions are placed on values, except an overall size limitation on the entire field.  Signers should document the keys and values they support. Signers should deny requests that contain keys they do not recognize. |

Show more

#### [3.1.323. .template.spec.volumes[].projected.sources[].secret](#template-spec-volumes-projected-sources-secret) Copy linkLink copied to clipboard!

Description
:   Adapts a secret into a projected volume.

    The contents of the target Secret’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional field specify whether the Secret or its key must be defined |

Show more

#### [3.1.324. .template.spec.volumes[].projected.sources[].secret.items](#template-spec-volumes-projected-sources-secret-items) Copy linkLink copied to clipboard!

Description
:   items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
:   `array`

#### [3.1.325. .template.spec.volumes[].projected.sources[].secret.items[]](#template-spec-volumes-projected-sources-secret-items-2) Copy linkLink copied to clipboard!

Description
:   Maps a string key to a path within a volume.

Type
:   `object`

Required
:   * `key`
    * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

Show more

#### [3.1.326. .template.spec.volumes[].projected.sources[].serviceAccountToken](#template-spec-volumes-projected-sources-serviceaccounttoken) Copy linkLink copied to clipboard!

Description
:   ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise).

Type
:   `object`

Required
:   * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `audience` | `string` | audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. |
| `expirationSeconds` | `integer` | expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. |
| `path` | `string` | path is the path relative to the mount point of the file to project the token into. |

Show more

#### [3.1.327. .template.spec.volumes[].quobyte](#template-spec-volumes-quobyte) Copy linkLink copied to clipboard!

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

#### [3.1.328. .template.spec.volumes[].rbd](#template-spec-volumes-rbd) Copy linkLink copied to clipboard!

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
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `user` | `string` | user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |

Show more

#### [3.1.329. .template.spec.volumes[].rbd.secretRef](#template-spec-volumes-rbd-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.330. .template.spec.volumes[].scaleIO](#template-spec-volumes-scaleio) Copy linkLink copied to clipboard!

Description
:   ScaleIOVolumeSource represents a persistent ScaleIO volume

Type
:   `object`

Required
:   * `gateway`
    * `system`
    * `secretRef`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs". |
| `gateway` | `string` | gateway is the host address of the ScaleIO API Gateway. |
| `protectionDomain` | `string` | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. |
| `readOnly` | `boolean` | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `sslEnabled` | `boolean` | sslEnabled Flag enable/disable SSL communication with Gateway, default false |
| `storageMode` | `string` | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. |
| `storagePool` | `string` | storagePool is the ScaleIO Storage Pool associated with the protection domain. |
| `system` | `string` | system is the name of the storage system as configured in ScaleIO. |
| `volumeName` | `string` | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. |

Show more

#### [3.1.331. .template.spec.volumes[].scaleIO.secretRef](#template-spec-volumes-scaleio-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.332. .template.spec.volumes[].secret](#template-spec-volumes-secret) Copy linkLink copied to clipboard!

Description
:   Adapts a Secret into a volume.

    The contents of the target Secret’s Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultMode` | `integer` | defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `optional` | `boolean` | optional field specify whether the Secret or its keys must be defined |
| `secretName` | `string` | secretName is the name of the secret in the pod’s namespace to use. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret> |

Show more

#### [3.1.333. .template.spec.volumes[].secret.items](#template-spec-volumes-secret-items) Copy linkLink copied to clipboard!

Description
:   items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
:   `array`

#### [3.1.334. .template.spec.volumes[].secret.items[]](#template-spec-volumes-secret-items-2) Copy linkLink copied to clipboard!

Description
:   Maps a string key to a path within a volume.

Type
:   `object`

Required
:   * `key`
    * `path`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

Show more

#### [3.1.335. .template.spec.volumes[].storageos](#template-spec-volumes-storageos) Copy linkLink copied to clipboard!

Description
:   Represents a StorageOS persistent volume resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `volumeName` | `string` | volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace. |
| `volumeNamespace` | `string` | volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. |

Show more

#### [3.1.336. .template.spec.volumes[].storageos.secretRef](#template-spec-volumes-storageos-secretref) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

#### [3.1.337. .template.spec.volumes[].vsphereVolume](#template-spec-volumes-vspherevolume) Copy linkLink copied to clipboard!

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

#### [3.1.338. .template.spec.workloadRef](#template-spec-workloadref) Copy linkLink copied to clipboard!

Description
:   WorkloadReference identifies the Workload object and PodGroup membership that a Pod belongs to. The scheduler uses this information to apply workload-aware scheduling semantics.

Type
:   `object`

Required
:   * `name`
    * `podGroup`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name defines the name of the Workload object this Pod belongs to. Workload must be in the same namespace as the Pod. If it doesn’t match any existing Workload, the Pod will remain unschedulable until a Workload object is created and observed by the kube-scheduler. It must be a DNS subdomain. |
| `podGroup` | `string` | PodGroup is the name of the PodGroup within the Workload that this Pod belongs to. If it doesn’t match any existing PodGroup within the Workload, the Pod will remain unschedulable until the Workload object is recreated and observed by the kube-scheduler. It must be a DNS label. |
| `podGroupReplicaKey` | `string` | PodGroupReplicaKey specifies the replica key of the PodGroup to which this Pod belongs. It is used to distinguish pods belonging to different replicas of the same pod group. The pod group policy is applied separately to each replica. When set, it must be a DNS label. |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/api/v1/podtemplates`

  + `GET`: list or watch objects of kind PodTemplate
* `/api/v1/watch/podtemplates`

  + `GET`: watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/podtemplates`

  + `DELETE`: delete collection of PodTemplate
  + `GET`: list or watch objects of kind PodTemplate
  + `POST`: create a PodTemplate
* `/api/v1/watch/namespaces/{namespace}/podtemplates`

  + `GET`: watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* `/api/v1/namespaces/{namespace}/podtemplates/{name}`

  + `DELETE`: delete a PodTemplate
  + `GET`: read the specified PodTemplate
  + `PATCH`: partially update the specified PodTemplate
  + `PUT`: replace the specified PodTemplate
* `/api/v1/watch/namespaces/{namespace}/podtemplates/{name}`

  + `GET`: watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [3.2.1. /api/v1/podtemplates](#apiv1podtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind PodTemplate

Expand

Table 3.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /api/v1/watch/podtemplates](#apiv1watchpodtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /api/v1/namespaces/{namespace}/podtemplates](#apiv1namespacesnamespacepodtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of PodTemplate

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
:   list or watch objects of kind PodTemplate

Expand

Table 3.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a PodTemplate

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
| `body` | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |  |

Show more

Expand

Table 3.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 201 - Created | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 202 - Accepted | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.4. /api/v1/watch/namespaces/{namespace}/podtemplates](#apiv1watchnamespacesnamespacepodtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 3.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.5. /api/v1/namespaces/{namespace}/podtemplates/{name}](#apiv1namespacesnamespacepodtemplatesname) Copy linkLink copied to clipboard!

Expand

Table 3.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PodTemplate |

Show more

HTTP method
:   `DELETE`

Description
:   delete a PodTemplate

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
| 200 - OK | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 202 - Accepted | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified PodTemplate

Expand

Table 3.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified PodTemplate

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
| 200 - OK | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 201 - Created | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified PodTemplate

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
| `body` | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |  |

Show more

Expand

Table 3.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 201 - Created | [`PodTemplate`](#podtemplate-v1 "Chapter 3. PodTemplate [v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.6. /api/v1/watch/namespaces/{namespace}/podtemplates/{name}](#apiv1watchnamespacesnamespacepodtemplatesname) Copy linkLink copied to clipboard!

Expand

Table 3.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the PodTemplate |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 3.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. Template [template.openshift.io/v1]](#template-template-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Template contains the inputs needed to produce a Config.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `objects`

### [4.1. Specification](#specification-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `labels` | `object (string)` | labels is a optional set of labels that are applied to every object during the Template to Config transformation. |
| `message` | `string` | message is an optional instructional message that will be displayed when this template is instantiated. This field should inform the user how to utilize the newly created resources. Parameter substitution will be performed on the message before being displayed so that generated credentials and other parameters can be included in the output. |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `objects` | [`array (RawExtension)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | objects is an array of resources to include in this template. If a namespace value is hardcoded in the object, it will be removed during template instantiation, however if the namespace value is, or contains, a ${PARAMETER\_REFERENCE}, the resolved value after parameter substitution will be respected and the object will be created in that namespace. |
| `parameters` | `array` | parameters is an optional array of Parameters used during the Template to Config transformation. |
| `parameters[]` | `object` | Parameter defines a name/value variable that is to be processed during the Template to Config transformation. |

Show more

#### [4.1.1. .parameters](#parameters) Copy linkLink copied to clipboard!

Description
:   parameters is an optional array of Parameters used during the Template to Config transformation.

Type
:   `array`

#### [4.1.2. .parameters[]](#parameters-2) Copy linkLink copied to clipboard!

Description
:   Parameter defines a name/value variable that is to be processed during the Template to Config transformation.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `description` | `string` | description of a parameter. Optional. |
| `displayName` | `string` | Optional: The name that will show in UI instead of parameter 'Name' |
| `from` | `string` | from is an input value for the generator. Optional. |
| `generate` | `string` | generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.  The only supported generator is "expression", which accepts a "from" value in the form of a simple regular expression containing the range expression "[a-zA-Z0-9]", and the length expression "a{length}".  Examples:  from | value ----------------------------- "test[0-9]{1}x" | "test7x" "[0-1]{8}" | "01001100" "0x[A-F0-9]{4}" | "0xB3AF" "[a-zA-Z0-9]{8}" | "hW4yQU5i" |
| `name` | `string` | name must be set and it can be referenced in Template Items using ${PARAMETER\_NAME}. Required. |
| `required` | `boolean` | Optional: Indicates the parameter must have a value. Defaults to false. |
| `value` | `string` | value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/template.openshift.io/v1/templates`

  + `GET`: list or watch objects of kind Template
* `/apis/template.openshift.io/v1/watch/templates`

  + `GET`: watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/template.openshift.io/v1/namespaces/{namespace}/templates`

  + `DELETE`: delete collection of Template
  + `GET`: list or watch objects of kind Template
  + `POST`: create a Template
* `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates`

  + `GET`: watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/template.openshift.io/v1/namespaces/{namespace}/templates/{name}`

  + `DELETE`: delete a Template
  + `GET`: read the specified Template
  + `PATCH`: partially update the specified Template
  + `PUT`: replace the specified Template
* `/apis/template.openshift.io/v1/namespaces/{namespace}/processedtemplates`

  + `POST`: create a Template
* `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates/{name}`

  + `GET`: watch changes to an object of kind Template. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

#### [4.2.1. /apis/template.openshift.io/v1/templates](#apistemplate-openshift-iov1templates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind Template

Expand

Table 4.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/template.openshift.io/v1/watch/templates](#apistemplate-openshift-iov1watchtemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/template.openshift.io/v1/namespaces/{namespace}/templates](#apistemplate-openshift-iov1namespacesnamespacetemplates) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Template

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind Template

Expand

Table 4.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Template

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
| `body` | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 201 - Created | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 202 - Accepted | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.4. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates](#apistemplate-openshift-iov1watchnamespacesnamespacetemplates) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.5. /apis/template.openshift.io/v1/namespaces/{namespace}/templates/{name}](#apistemplate-openshift-iov1namespacesnamespacetemplatesname) Copy linkLink copied to clipboard!

Expand

Table 4.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Template |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Template

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
| 200 - OK | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 202 - Accepted | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Template

Expand

Table 4.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Template

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
| 200 - OK | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 201 - Created | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Template

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
| `body` | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 201 - Created | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.6. /apis/template.openshift.io/v1/namespaces/{namespace}/processedtemplates](#apistemplate-openshift-iov1namespacesnamespaceprocessedtemplates) Copy linkLink copied to clipboard!

Expand

Table 4.19. Global query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

HTTP method
:   `POST`

Description
:   create a Template

Expand

Table 4.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 201 - Created | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 202 - Accepted | [`Template`](#template-template-openshift-io-v1 "Chapter 4. Template [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.7. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates/{name}](#apistemplate-openshift-iov1watchnamespacesnamespacetemplatesname) Copy linkLink copied to clipboard!

Expand

Table 4.22. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Template |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind Template. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 4.23. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. TemplateInstance [template.openshift.io/v1]](#templateinstance-template-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   TemplateInstance requests and records the instantiation of a Template. TemplateInstance is part of an experimental API.

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
| `spec` | `object` | TemplateInstanceSpec describes the desired state of a TemplateInstance. |
| `status` | `object` | TemplateInstanceStatus describes the current state of a TemplateInstance. |

Show more

#### [5.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   TemplateInstanceSpec describes the desired state of a TemplateInstance.

Type
:   `object`

Required
:   * `template`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requester` | `object` | TemplateInstanceRequester holds the identity of an agent requesting a template instantiation. |
| `secret` | `LocalObjectReference` | secret is a reference to a Secret object containing the necessary template parameters. |
| `template` | `object` | Template contains the inputs needed to produce a Config.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). |

Show more

#### [5.1.2. .spec.requester](#spec-requester) Copy linkLink copied to clipboard!

Description
:   TemplateInstanceRequester holds the identity of an agent requesting a template instantiation.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `extra` | `object` | extra holds additional information provided by the authenticator. |
| `extra{}` | `array (string)` |  |
| `groups` | `array (string)` | groups represent the groups this user is a part of. |
| `uid` | `string` | uid is a unique value that identifies this user across time; if this user is deleted and another user by the same name is added, they will have different UIDs. |
| `username` | `string` | username uniquely identifies this user among all active users. |

Show more

#### [5.1.3. .spec.requester.extra](#spec-requester-extra) Copy linkLink copied to clipboard!

Description
:   extra holds additional information provided by the authenticator.

Type
:   `object`

#### [5.1.4. .spec.template](#spec-template) Copy linkLink copied to clipboard!

Description
:   Template contains the inputs needed to produce a Config.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `objects`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `labels` | `object (string)` | labels is a optional set of labels that are applied to every object during the Template to Config transformation. |
| `message` | `string` | message is an optional instructional message that will be displayed when this template is instantiated. This field should inform the user how to utilize the newly created resources. Parameter substitution will be performed on the message before being displayed so that generated credentials and other parameters can be included in the output. |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `objects` | [`array (RawExtension)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) | objects is an array of resources to include in this template. If a namespace value is hardcoded in the object, it will be removed during template instantiation, however if the namespace value is, or contains, a ${PARAMETER\_REFERENCE}, the resolved value after parameter substitution will be respected and the object will be created in that namespace. |
| `parameters` | `array` | parameters is an optional array of Parameters used during the Template to Config transformation. |
| `parameters[]` | `object` | Parameter defines a name/value variable that is to be processed during the Template to Config transformation. |

Show more

#### [5.1.5. .spec.template.parameters](#spec-template-parameters) Copy linkLink copied to clipboard!

Description
:   parameters is an optional array of Parameters used during the Template to Config transformation.

Type
:   `array`

#### [5.1.6. .spec.template.parameters[]](#spec-template-parameters-2) Copy linkLink copied to clipboard!

Description
:   Parameter defines a name/value variable that is to be processed during the Template to Config transformation.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `description` | `string` | description of a parameter. Optional. |
| `displayName` | `string` | Optional: The name that will show in UI instead of parameter 'Name' |
| `from` | `string` | from is an input value for the generator. Optional. |
| `generate` | `string` | generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.  The only supported generator is "expression", which accepts a "from" value in the form of a simple regular expression containing the range expression "[a-zA-Z0-9]", and the length expression "a{length}".  Examples:  from | value ----------------------------- "test[0-9]{1}x" | "test7x" "[0-1]{8}" | "01001100" "0x[A-F0-9]{4}" | "0xB3AF" "[a-zA-Z0-9]{8}" | "hW4yQU5i" |
| `name` | `string` | name must be set and it can be referenced in Template Items using ${PARAMETER\_NAME}. Required. |
| `required` | `boolean` | Optional: Indicates the parameter must have a value. Defaults to false. |
| `value` | `string` | value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional. |

Show more

#### [5.1.7. .status](#status) Copy linkLink copied to clipboard!

Description
:   TemplateInstanceStatus describes the current state of a TemplateInstance.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions represent the latest available observations of a TemplateInstance’s current state. |
| `conditions[]` | `object` | TemplateInstanceCondition contains condition information for a TemplateInstance. |
| `objects` | `array` | objects references the objects created by the TemplateInstance. |
| `objects[]` | `object` | TemplateInstanceObject references an object created by a TemplateInstance. |

Show more

#### [5.1.8. .status.conditions](#status-conditions) Copy linkLink copied to clipboard!

Description
:   conditions represent the latest available observations of a TemplateInstance’s current state.

Type
:   `array`

#### [5.1.9. .status.conditions[]](#status-conditions-2) Copy linkLink copied to clipboard!

Description
:   TemplateInstanceCondition contains condition information for a TemplateInstance.

Type
:   `object`

Required
:   * `type`
    * `status`
    * `lastTransitionTime`
    * `reason`
    * `message`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastTransitionTime is the last time a condition status transitioned from one state to another. |
| `message` | `string` | message is a human readable description of the details of the last transition, complementing reason. |
| `reason` | `string` | reason is a brief machine readable explanation for the condition’s last transition. |
| `status` | `string` | status of the condition, one of True, False or Unknown. |
| `type` | `string` | type of the condition, currently Ready or InstantiateFailure. |

Show more

#### [5.1.10. .status.objects](#status-objects) Copy linkLink copied to clipboard!

Description
:   objects references the objects created by the TemplateInstance.

Type
:   `array`

#### [5.1.11. .status.objects[]](#status-objects-2) Copy linkLink copied to clipboard!

Description
:   TemplateInstanceObject references an object created by a TemplateInstance.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ref` | [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) | ref is a reference to the created object. When used under .spec, only name and namespace are used; these can contain references to parameters which will be substituted following the usual rules. |

Show more

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/template.openshift.io/v1/templateinstances`

  + `GET`: list or watch objects of kind TemplateInstance
* `/apis/template.openshift.io/v1/watch/templateinstances`

  + `GET`: watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances`

  + `DELETE`: delete collection of TemplateInstance
  + `GET`: list or watch objects of kind TemplateInstance
  + `POST`: create a TemplateInstance
* `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances`

  + `GET`: watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.
* `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}`

  + `DELETE`: delete a TemplateInstance
  + `GET`: read the specified TemplateInstance
  + `PATCH`: partially update the specified TemplateInstance
  + `PUT`: replace the specified TemplateInstance
* `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances/{name}`

  + `GET`: watch changes to an object of kind TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}/status`

  + `GET`: read status of the specified TemplateInstance
  + `PATCH`: partially update status of the specified TemplateInstance
  + `PUT`: replace status of the specified TemplateInstance

#### [5.2.1. /apis/template.openshift.io/v1/templateinstances](#apistemplate-openshift-iov1templateinstances) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list or watch objects of kind TemplateInstance

Expand

Table 5.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstanceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateInstanceList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/template.openshift.io/v1/watch/templateinstances](#apistemplate-openshift-iov1watchtemplateinstances) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances](#apistemplate-openshift-iov1namespacesnamespacetemplateinstances) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of TemplateInstance

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list or watch objects of kind TemplateInstance

Expand

Table 5.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstanceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateInstanceList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a TemplateInstance

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
| `body` | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 202 - Accepted | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.4. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances](#apistemplate-openshift-iov1watchnamespacesnamespacetemplateinstances) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead.

Expand

Table 5.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.5. /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}](#apistemplate-openshift-iov1namespacesnamespacetemplateinstancesname) Copy linkLink copied to clipboard!

Expand

Table 5.10. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the TemplateInstance |

Show more

HTTP method
:   `DELETE`

Description
:   delete a TemplateInstance

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
| 200 - OK | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 202 - Accepted | [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified TemplateInstance

Expand

Table 5.13. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified TemplateInstance

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
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified TemplateInstance

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
| `body` | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.6. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances/{name}](#apistemplate-openshift-iov1watchnamespacesnamespacetemplateinstancesname) Copy linkLink copied to clipboard!

Expand

Table 5.19. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the TemplateInstance |

Show more

HTTP method
:   `GET`

Description
:   watch changes to an object of kind TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

Expand

Table 5.20. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.7. /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}/status](#apistemplate-openshift-iov1namespacesnamespacetemplateinstancesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 5.21. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the TemplateInstance |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified TemplateInstance

Expand

Table 5.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified TemplateInstance

Expand

Table 5.23. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.24. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified TemplateInstance

Expand

Table 5.25. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 5.26. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.27. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 201 - Created | [`TemplateInstance`](#templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance [template.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140170832687904) Copy linkLink copied to clipboard!

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
