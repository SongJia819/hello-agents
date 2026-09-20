---
title: "Config APIs"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/index
retrieved_at: 2026-09-05T05:41:43.043395+00:00
---

# Config APIs

---

OpenShift Container Platform 4.22

## Reference guide for config APIs

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140338227649984)

**Abstract**

This document describes the OpenShift Container Platform config API objects and their detailed specifications.

---

## [Chapter 1. Config APIs](#config-apis) Copy linkLink copied to clipboard!

### [1.1. APIServer [config.openshift.io/v1]](#apiserver-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   APIServer holds configuration (like serving certificates, client CA and CORS domains) shared by all API servers in the system, among them especially kube-apiserver and openshift-apiserver. The canonical name of an instance is 'cluster'.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.2. Authentication [config.openshift.io/v1]](#authentication-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Authentication specifies cluster-wide settings for authentication (like OAuth and webhook token authenticators). The canonical name of an instance is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.3. Build [config.openshift.io/v1]](#build-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Build configures the behavior of OpenShift builds for the entire cluster. This includes default settings that can be overridden in BuildConfig objects, and overrides which are applied to all builds.

    The canonical name is "cluster"

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.4. ClusterImagePolicy [config.openshift.io/v1]](#clusterimagepolicy-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterImagePolicy holds cluster-wide configuration for image signature verification

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.5. ClusterOperator [config.openshift.io/v1]](#clusteroperator-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterOperator holds the status of a core or optional OpenShift component managed by the Cluster Version Operator (CVO). This object is used by operators to convey their state to the rest of the cluster. Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.6. ClusterVersion [config.openshift.io/v1]](#clusterversion-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ClusterVersion is the configuration for the ClusterVersionOperator. This is where parameters related to automatic updates can be set.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.7. Console [config.openshift.io/v1]](#console-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Console holds cluster-wide configuration for the web console, including the logout URL, and reports the public URL of the console. The canonical name is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.8. DNS [config.openshift.io/v1]](#dns-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   DNS holds cluster-wide information about DNS. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.9. FeatureGate [config.openshift.io/v1]](#featuregate-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Feature holds cluster-wide information about feature gates. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.10. HelmChartRepository [helm.openshift.io/v1beta1]](#helmchartrepository-helm-openshift-iov1beta1) Copy linkLink copied to clipboard!

Description
:   HelmChartRepository holds cluster-wide configuration for proxied Helm chart repository

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.11. Image [config.openshift.io/v1]](#image-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Image governs policies related to imagestream imports and runtime configuration for external registries. It allows cluster admins to configure which registries OpenShift is allowed to import images from, extra CA trust bundles for external registries, and policies to block or allow registry hostnames. When exposing OpenShift’s image registry to the public, this also lets cluster admins specify the external hostname.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.12. ImageDigestMirrorSet [config.openshift.io/v1]](#imagedigestmirrorset-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ImageDigestMirrorSet holds cluster-wide information about how to handle registry mirror rules on using digest pull specification. When multiple policies are defined, the outcome of the behavior is defined on each field.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.13. ImageContentPolicy [config.openshift.io/v1]](#imagecontentpolicy-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ImageContentPolicy holds cluster-wide information about how to handle registry mirror rules. When multiple policies are defined, the outcome of the behavior is defined on each field.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.14. ImagePolicy [config.openshift.io/v1]](#imagepolicy-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ImagePolicy holds namespace-wide configuration for image signature verification

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.15. ImageTagMirrorSet [config.openshift.io/v1]](#imagetagmirrorset-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   ImageTagMirrorSet holds cluster-wide information about how to handle registry mirror rules on using tag pull specification. When multiple policies are defined, the outcome of the behavior is defined on each field.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.16. InsightsDataGather [config.openshift.io/v1]](#insightsdatagather-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   InsightsDataGather provides data gather configuration options for the Insights Operator.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.17. Infrastructure [config.openshift.io/v1]](#infrastructure-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Infrastructure holds cluster-wide information about Infrastructure. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.18. Ingress [config.openshift.io/v1]](#ingress-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Ingress holds cluster-wide information about ingress, including the default ingress domain used for routes. The canonical name is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.19. Network [config.openshift.io/v1]](#network-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Network holds cluster-wide information about Network. The canonical name is `cluster`. It is used to configure the desired network configuration, such as: IP address pools for services/pod IPs, network plugin, etc. Please view network.spec for an explanation on what applies when configuring this resource.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.20. Node [config.openshift.io/v1]](#node-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Node holds cluster-wide information about node specific features.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.21. OAuth [config.openshift.io/v1]](#oauth-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   OAuth holds cluster-wide information about OAuth. The canonical name is `cluster`. It is used to configure the integrated OAuth server. This configuration is only honored when the top level Authentication config has type set to IntegratedOAuth.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.22. OperatorHub [config.openshift.io/v1]](#operatorhub-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   OperatorHub is the Schema for the operatorhubs API. It can be used to change the state of the default hub sources for OperatorHub on the cluster from enabled to disabled and vice versa.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.23. Project [config.openshift.io/v1]](#project-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Project holds cluster-wide information about Project. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.24. ProjectHelmChartRepository [helm.openshift.io/v1beta1]](#projecthelmchartrepository-helm-openshift-iov1beta1) Copy linkLink copied to clipboard!

Description
:   ProjectHelmChartRepository holds namespace-wide configuration for proxied Helm chart repository

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.25. Proxy [config.openshift.io/v1]](#proxy-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Proxy holds cluster-wide information on how to configure default proxies for the cluster. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [1.26. Scheduler [config.openshift.io/v1]](#scheduler-config-openshift-iov1) Copy linkLink copied to clipboard!

Description
:   Scheduler holds cluster-wide config information to run the Kubernetes Scheduler and influence its placement decisions. The canonical name for this config is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

## [Chapter 2. APIServer [config.openshift.io/v1]](#apiserver-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   APIServer holds configuration (like serving certificates, client CA and CORS domains) shared by all API servers in the system, among them especially kube-apiserver and openshift-apiserver. The canonical name of an instance is 'cluster'.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [2.1.1. .spec](#spec) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalCORSAllowedOrigins` | `array (string)` | additionalCORSAllowedOrigins lists additional, user-defined regular expressions describing hosts for which the API server allows access using the CORS headers. This may be needed to access the API and the integrated OAuth server from JavaScript applications. The values are regular expressions that correspond to the Golang regular expression language. |
| `audit` | `object` | audit specifies the settings for audit configuration to be applied to all OpenShift-provided API servers in the cluster. |
| `clientCA` | `object` | clientCA references a ConfigMap containing a certificate bundle for the signers that will be recognized for incoming client certificates in addition to the operator managed signers. If this is empty, then only operator managed signers are valid. You usually only have to set this if you have your own PKI you wish to honor client certificates from. The ConfigMap must exist in the openshift-config namespace and contain the following required fields: - ConfigMap.Data["ca-bundle.crt"] - CA bundle. |
| `encryption` | `object` | encryption allows the configuration of encryption of resources at the datastore layer. |
| `servingCerts` | `object` | servingCert is the TLS cert info for serving secure traffic. If not specified, operator managed certificates will be used for serving secure traffic. |
| `tlsSecurityProfile` | `object` | tlsSecurityProfile specifies settings for TLS connections for externally exposed servers.  When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default is the Intermediate profile. |

Show more

#### [2.1.2. .spec.audit](#spec-audit) Copy linkLink copied to clipboard!

Description
:   audit specifies the settings for audit configuration to be applied to all OpenShift-provided API servers in the cluster.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `customRules` | `array` | customRules specify profiles per group. These profile take precedence over the top-level profile field if they apply. They are evaluation from top to bottom and the first one that matches, applies. |
| `customRules[]` | `object` | AuditCustomRule describes a custom rule for an audit profile that takes precedence over the top-level profile. |
| `profile` | `string` | profile specifies the name of the desired top-level audit profile to be applied to all requests sent to any of the OpenShift-provided API servers in the cluster (kube-apiserver, openshift-apiserver and oauth-apiserver), with the exception of those requests that match one or more of the customRules.  The following profiles are provided: - Default: default policy which means MetaData level logging with the exception of events (not logged at all), oauthaccesstokens and oauthauthorizetokens (both logged at RequestBody level). - WriteRequestBodies: like 'Default', but logs request and response HTTP payloads for write requests (create, update, patch). - AllRequestBodies: like 'WriteRequestBodies', but also logs request and response HTTP payloads for read requests (get, list). - None: no requests are logged at all, not even oauthaccesstokens and oauthauthorizetokens.  Warning: It is not recommended to disable audit logging by using the `None` profile unless you are fully aware of the risks of not logging data that can be beneficial when troubleshooting issues. If you disable audit logging and a support situation arises, you might need to enable audit logging and reproduce the issue in order to troubleshoot properly.  If unset, the 'Default' profile is used as the default. |

Show more

#### [2.1.3. .spec.audit.customRules](#spec-audit-customrules) Copy linkLink copied to clipboard!

Description
:   customRules specify profiles per group. These profile take precedence over the top-level profile field if they apply. They are evaluation from top to bottom and the first one that matches, applies.

Type
:   `array`

#### [2.1.4. .spec.audit.customRules[]](#spec-audit-customrules-2) Copy linkLink copied to clipboard!

Description
:   AuditCustomRule describes a custom rule for an audit profile that takes precedence over the top-level profile.

Type
:   `object`

Required
:   * `group`
    * `profile`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | group is a name of group a request user must be member of in order to this profile to apply. |
| `profile` | `string` | profile specifies the name of the desired audit policy configuration to be deployed to all OpenShift-provided API servers in the cluster.  The following profiles are provided: - Default: the existing default policy. - WriteRequestBodies: like 'Default', but logs request and response HTTP payloads for write requests (create, update, patch). - AllRequestBodies: like 'WriteRequestBodies', but also logs request and response HTTP payloads for read requests (get, list). - None: no requests are logged at all, not even oauthaccesstokens and oauthauthorizetokens.  If unset, the 'Default' profile is used as the default. |

Show more

#### [2.1.5. .spec.clientCA](#spec-clientca) Copy linkLink copied to clipboard!

Description
:   clientCA references a ConfigMap containing a certificate bundle for the signers that will be recognized for incoming client certificates in addition to the operator managed signers. If this is empty, then only operator managed signers are valid. You usually only have to set this if you have your own PKI you wish to honor client certificates from. The ConfigMap must exist in the openshift-config namespace and contain the following required fields: - ConfigMap.Data["ca-bundle.crt"] - CA bundle.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [2.1.6. .spec.encryption](#spec-encryption) Copy linkLink copied to clipboard!

Description
:   encryption allows the configuration of encryption of resources at the datastore layer.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type defines what encryption type should be used to encrypt resources at the datastore layer. When this field is unset (i.e. when it is set to the empty string), identity is implied. The behavior of unset can and will change over time. Even if encryption is enabled by default, the meaning of unset may change to a different encryption type based on changes in best practices.  When encryption is enabled, all sensitive resources shipped with the platform are encrypted. This list of sensitive resources can and will change over time. The current authoritative list is:  1. secrets 2. configmaps 3. routes.route.openshift.io 4. oauthaccesstokens.oauth.openshift.io 5. oauthauthorizetokens.oauth.openshift.io |

Show more

#### [2.1.7. .spec.servingCerts](#spec-servingcerts) Copy linkLink copied to clipboard!

Description
:   servingCert is the TLS cert info for serving secure traffic. If not specified, operator managed certificates will be used for serving secure traffic.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `namedCertificates` | `array` | namedCertificates references secrets containing the TLS cert info for serving secure traffic to specific hostnames. If no named certificates are provided, or no named certificates match the server name as understood by a client, the defaultServingCertificate will be used. |
| `namedCertificates[]` | `object` | APIServerNamedServingCert maps a server DNS name, as understood by a client, to a certificate. |

Show more

#### [2.1.8. .spec.servingCerts.namedCertificates](#spec-servingcerts-namedcertificates) Copy linkLink copied to clipboard!

Description
:   namedCertificates references secrets containing the TLS cert info for serving secure traffic to specific hostnames. If no named certificates are provided, or no named certificates match the server name as understood by a client, the defaultServingCertificate will be used.

Type
:   `array`

#### [2.1.9. .spec.servingCerts.namedCertificates[]](#spec-servingcerts-namedcertificates-2) Copy linkLink copied to clipboard!

Description
:   APIServerNamedServingCert maps a server DNS name, as understood by a client, to a certificate.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `names` | `array (string)` | names is a optional list of explicit DNS names (leading wildcards allowed) that should use this certificate to serve secure traffic. If no names are provided, the implicit names will be extracted from the certificates. Exact names trump over wildcard names. Explicit names defined here trump over extracted implicit names. |
| `servingCertificate` | `object` | servingCertificate references a kubernetes.io/tls type secret containing the TLS cert info for serving secure traffic. The secret must exist in the openshift-config namespace and contain the following required fields: - Secret.Data["tls.key"] - TLS private key. - Secret.Data["tls.crt"] - TLS certificate. |

Show more

#### [2.1.10. .spec.servingCerts.namedCertificates[].servingCertificate](#spec-servingcerts-namedcertificates-servingcertificate) Copy linkLink copied to clipboard!

Description
:   servingCertificate references a kubernetes.io/tls type secret containing the TLS cert info for serving secure traffic. The secret must exist in the openshift-config namespace and contain the following required fields: - Secret.Data["tls.key"] - TLS private key. - Secret.Data["tls.crt"] - TLS certificate.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [2.1.11. .spec.tlsSecurityProfile](#spec-tlssecurityprofile) Copy linkLink copied to clipboard!

Description
:   tlsSecurityProfile specifies settings for TLS connections for externally exposed servers.

    When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default is the Intermediate profile.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `custom` | `` | custom is a user-defined TLS security profile. Be extremely careful using a custom profile as invalid configurations can be catastrophic. An example custom profile looks like this:  minTLSVersion: VersionTLS11 ciphers: - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 |
| `intermediate` | `` | intermediate is a TLS profile for use when you do not need compatibility with legacy clients and want to remain highly secure while being compatible with most clients currently in use.  This profile is equivalent to a Custom profile specified as: minTLSVersion: VersionTLS12 ciphers: - TLS\_AES\_128\_GCM\_SHA256 - TLS\_AES\_256\_GCM\_SHA384 - TLS\_CHACHA20\_POLY1305\_SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 - ECDHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 |
| `modern` | `` | modern is a TLS security profile for use with clients that support TLS 1.3 and do not need backward compatibility for older clients.  This profile is equivalent to a Custom profile specified as: minTLSVersion: VersionTLS13 ciphers: - TLS\_AES\_128\_GCM\_SHA256 - TLS\_AES\_256\_GCM\_SHA384 - TLS\_CHACHA20\_POLY1305\_SHA256 |
| `old` | `` | old is a TLS profile for use when services need to be accessed by very old clients or libraries and should be used only as a last resort.  This profile is equivalent to a Custom profile specified as: minTLSVersion: VersionTLS10 ciphers: - TLS\_AES\_128\_GCM\_SHA256 - TLS\_AES\_256\_GCM\_SHA384 - TLS\_CHACHA20\_POLY1305\_SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 - ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 - ECDHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 - ECDHE-ECDSA-AES128-SHA256 - ECDHE-RSA-AES128-SHA256 - ECDHE-ECDSA-AES128-SHA - ECDHE-RSA-AES128-SHA - ECDHE-ECDSA-AES256-SHA - ECDHE-RSA-AES256-SHA - AES128-GCM-SHA256 - AES256-GCM-SHA384 - AES128-SHA256 - AES128-SHA - AES256-SHA - DES-CBC3-SHA |
| `type` | `string` | type is one of Old, Intermediate, Modern or Custom. Custom provides the ability to specify individual TLS security profile parameters.  The profiles are based on version 5.7 of the Mozilla Server Side TLS configuration guidelines. The cipher lists consist of the configuration’s "ciphersuites" followed by the Go-specific "ciphers" from the guidelines. See: <https://ssl-config.mozilla.org/guidelines/5.7.json>  The profiles are intent based, so they may change over time as new ciphers are developed and existing ciphers are found to be insecure. Depending on precisely which ciphers are available to a process, the list may be reduced. |

Show more

#### [2.1.12. .status](#status) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

### [2.2. API endpoints](#api-endpoints) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/apiservers`

  + `DELETE`: delete collection of APIServer
  + `GET`: list objects of kind APIServer
  + `POST`: create an APIServer
* `/apis/config.openshift.io/v1/apiservers/{name}`

  + `DELETE`: delete an APIServer
  + `GET`: read the specified APIServer
  + `PATCH`: partially update the specified APIServer
  + `PUT`: replace the specified APIServer
* `/apis/config.openshift.io/v1/apiservers/{name}/status`

  + `GET`: read status of the specified APIServer
  + `PATCH`: partially update status of the specified APIServer
  + `PUT`: replace status of the specified APIServer

#### [2.2.1. /apis/config.openshift.io/v1/apiservers](#apisconfig-openshift-iov1apiservers) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of APIServer

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
:   list objects of kind APIServer

Expand

Table 2.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`APIServerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-APIServerList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an APIServer

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
| `body` | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 201 - Created | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 202 - Accepted | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.2. /apis/config.openshift.io/v1/apiservers/{name}](#apisconfig-openshift-iov1apiserversname) Copy linkLink copied to clipboard!

Expand

Table 2.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the APIServer |

Show more

HTTP method
:   `DELETE`

Description
:   delete an APIServer

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
:   read the specified APIServer

Expand

Table 2.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified APIServer

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
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified APIServer

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
| `body` | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 201 - Created | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [2.2.3. /apis/config.openshift.io/v1/apiservers/{name}/status](#apisconfig-openshift-iov1apiserversnamestatus) Copy linkLink copied to clipboard!

Expand

Table 2.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the APIServer |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified APIServer

Expand

Table 2.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified APIServer

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
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified APIServer

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
| `body` | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 2.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 201 - Created | [`APIServer`](#apiserver-config-openshift-io-v1 "Chapter 2. APIServer [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 3. Authentication [config.openshift.io/v1]](#authentication-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Authentication specifies cluster-wide settings for authentication (like OAuth and webhook token authenticators). The canonical name of an instance is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [3.1.1. .spec](#spec-2) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `oauthMetadata` | `object` | oauthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for an external OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> If oauthMetadata.name is non-empty, this value has precedence over any metadata reference stored in status. The key "oauthMetadata" is used to locate the data. If specified and the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config. |
| `oidcProviders` | `array` | oidcProviders are OIDC identity providers that can issue tokens for this cluster Can only be set if "Type" is set to "OIDC".  At most one provider can be configured. |
| `oidcProviders[]` | `object` |  |
| `serviceAccountIssuer` | `string` | serviceAccountIssuer is the identifier of the bound service account token issuer. The default is <https://kubernetes.default.svc> WARNING: Updating this field will not result in immediate invalidation of all bound tokens with the previous issuer value. Instead, the tokens issued by previous service account issuer will continue to be trusted for a time period chosen by the platform (currently set to 24h). This time period is subject to change over time. This allows internal components to transition to use new service account issuer without service distruption. |
| `type` | `string` | type identifies the cluster managed, user facing authentication mode in use. Specifically, it manages the component that responds to login attempts. The default is IntegratedOAuth. |
| `webhookTokenAuthenticator` | `object` | webhookTokenAuthenticator configures a remote token reviewer. These remote authentication webhooks can be used to verify bearer tokens via the tokenreviews.authentication.k8s.io REST API. This is required to honor bearer tokens that are provisioned by an external authentication service.  Can only be set if "Type" is set to "None". |
| `webhookTokenAuthenticators` | `array` | webhookTokenAuthenticators is DEPRECATED, setting it has no effect. |
| `webhookTokenAuthenticators[]` | `object` | deprecatedWebhookTokenAuthenticator holds the necessary configuration options for a remote token authenticator. It’s the same as WebhookTokenAuthenticator but it’s missing the 'required' validation on KubeConfig field. |

Show more

#### [3.1.2. .spec.oauthMetadata](#spec-oauthmetadata) Copy linkLink copied to clipboard!

Description
:   oauthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for an external OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> If oauthMetadata.name is non-empty, this value has precedence over any metadata reference stored in status. The key "oauthMetadata" is used to locate the data. If specified and the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [3.1.3. .spec.oidcProviders](#spec-oidcproviders) Copy linkLink copied to clipboard!

Description
:   oidcProviders are OIDC identity providers that can issue tokens for this cluster Can only be set if "Type" is set to "OIDC".

    At most one provider can be configured.

Type
:   `array`

#### [3.1.4. .spec.oidcProviders[]](#spec-oidcproviders-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `claimMappings`
    * `issuer`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claimMappings` | `object` | claimMappings is a required field that configures the rules to be used by the Kubernetes API server for translating claims in a JWT token, issued by the identity provider, to a cluster identity. |
| `claimValidationRules` | `array` | claimValidationRules is an optional field that configures the rules to be used by the Kubernetes API server for validating the claims in a JWT token issued by the identity provider.  Validation rules are joined via an AND operation. |
| `claimValidationRules[]` | `object` | TokenClaimValidationRule represents a validation rule based on token claims. If type is RequiredClaim, requiredClaim must be set. If Type is CEL, CEL must be set and RequiredClaim must be omitted. |
| `issuer` | `object` | issuer is a required field that configures how the platform interacts with the identity provider and how tokens issued from the identity provider are evaluated by the Kubernetes API server. |
| `name` | `string` | name is a required field that configures the unique human-readable identifier associated with the identity provider. It is used to distinguish between multiple identity providers and has no impact on token validation or authentication mechanics.  name must not be an empty string (""). |
| `oidcClients` | `array` | oidcClients is an optional field that configures how on-cluster, platform clients should request tokens from the identity provider. oidcClients must not exceed 20 entries and entries must have unique namespace/name pairs. |
| `oidcClients[]` | `object` | OIDCClientConfig configures how platform clients interact with identity providers as an authentication method. |

Show more

#### [3.1.5. .spec.oidcProviders[].claimMappings](#spec-oidcproviders-claimmappings) Copy linkLink copied to clipboard!

Description
:   claimMappings is a required field that configures the rules to be used by the Kubernetes API server for translating claims in a JWT token, issued by the identity provider, to a cluster identity.

Type
:   `object`

Required
:   * `username`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `extra` | `array` | extra is an optional field for configuring the mappings used to construct the extra attribute for the cluster identity. When omitted, no extra attributes will be present on the cluster identity.  key values for extra mappings must be unique. A maximum of 32 extra attribute mappings may be provided. |
| `extra[]` | `object` | ExtraMapping allows specifying a key and CEL expression to evaluate the keys' value. It is used to create additional mappings and attributes added to a cluster identity from a provided authentication token. |
| `groups` | `object` | groups is an optional field that configures how the groups of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.  When referencing a claim, if the claim is present in the JWT token, its value must be a list of groups separated by a comma (',').  For example - '"example"' and '"exampleOne", "exampleTwo", "exampleThree"' are valid claim values. |
| `uid` | `object` | uid is an optional field for configuring the claim mapping used to construct the uid for the cluster identity.  When using uid.claim to specify the claim it must be a single string value. When using uid.expression the expression must result in a single string value.  When omitted, this means the user has no opinion and the platform is left to choose a default, which is subject to change over time.  The current default is to use the 'sub' claim. |
| `username` | `object` | username is a required field that configures how the username of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider. |

Show more

#### [3.1.6. .spec.oidcProviders[].claimMappings.extra](#spec-oidcproviders-claimmappings-extra) Copy linkLink copied to clipboard!

Description
:   extra is an optional field for configuring the mappings used to construct the extra attribute for the cluster identity. When omitted, no extra attributes will be present on the cluster identity.

    key values for extra mappings must be unique. A maximum of 32 extra attribute mappings may be provided.

Type
:   `array`

#### [3.1.7. .spec.oidcProviders[].claimMappings.extra[]](#spec-oidcproviders-claimmappings-extra-2) Copy linkLink copied to clipboard!

Description
:   ExtraMapping allows specifying a key and CEL expression to evaluate the keys' value. It is used to create additional mappings and attributes added to a cluster identity from a provided authentication token.

Type
:   `object`

Required
:   * `key`
    * `valueExpression`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is a required field that specifies the string to use as the extra attribute key.  key must be a domain-prefix path (e.g 'example.org/foo'). key must not exceed 510 characters in length. key must contain the '/' character, separating the domain and path characters. key must not be empty.  The domain portion of the key (string of characters prior to the '/') must be a valid RFC1123 subdomain. It must not exceed 253 characters in length. It must start and end with an alphanumeric character. It must only contain lower case alphanumeric characters and '-' or '.'. It must not use the reserved domains, or be subdomains of, "kubernetes.io", "k8s.io", and "openshift.io".  The path portion of the key (string of characters after the '/') must not be empty and must consist of at least one alphanumeric character, percent-encoded octets, '-', '.', '\_', '~', '!', '$', '&', ''', '(', ')', '\*', '+', ',', ';', '=', and ':'. It must not exceed 256 characters in length. |
| `valueExpression` | `string` | valueExpression is a required field to specify the CEL expression to extract the extra attribute value from a JWT token’s claims. valueExpression must produce a string or string array value. "", [], and null are treated as the extra mapping not being present. Empty string values within an array are filtered out.  CEL expressions have access to the token claims through a CEL variable, 'claims'. 'claims' is a map of claim names to claim values. For example, the 'sub' claim value can be accessed as 'claims.sub'. Nested claims can be accessed using dot notation ('claims.foo.bar').  valueExpression must not exceed 1024 characters in length. valueExpression must not be empty. |

Show more

#### [3.1.8. .spec.oidcProviders[].claimMappings.groups](#spec-oidcproviders-claimmappings-groups) Copy linkLink copied to clipboard!

Description
:   groups is an optional field that configures how the groups of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.

    When referencing a claim, if the claim is present in the JWT token, its value must be a list of groups separated by a comma (',').

    For example - '"example"' and '"exampleOne", "exampleTwo", "exampleThree"' are valid claim values.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claim` | `string` | claim is an optional field for specifying the JWT token claim that is used in the mapping. The value of this claim will be assigned to the field in which this mapping is associated. claim must not exceed 256 characters in length. When set to the empty string `""`, this means that no named claim should be used for the group mapping. claim is required when the ExternalOIDCWithUpstreamParity feature gate is not enabled. |
| `prefix` | `string` | prefix is an optional field that configures the prefix that will be applied to the cluster identity attribute during the process of mapping JWT claims to cluster identity attributes.  When omitted or set to an empty string (""), no prefix is applied to the cluster identity attribute. Must not be set to a non-empty value when expression is set.  Example: if `prefix` is set to "myoidc:" and the `claim` in JWT contains an array of strings "a", "b" and "c", the mapping will result in an array of string "myoidc:a", "myoidc:b" and "myoidc:c". |

Show more

#### [3.1.9. .spec.oidcProviders[].claimMappings.uid](#spec-oidcproviders-claimmappings-uid) Copy linkLink copied to clipboard!

Description
:   uid is an optional field for configuring the claim mapping used to construct the uid for the cluster identity.

    When using uid.claim to specify the claim it must be a single string value. When using uid.expression the expression must result in a single string value.

    When omitted, this means the user has no opinion and the platform is left to choose a default, which is subject to change over time.

    The current default is to use the 'sub' claim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claim` | `string` | claim is an optional field for specifying the JWT token claim that is used in the mapping. The value of this claim will be assigned to the field in which this mapping is associated.  Precisely one of claim or expression must be set. claim must not be specified when expression is set. When specified, claim must be at least 1 character in length and must not exceed 256 characters in length. |
| `expression` | `string` | expression is an optional field for specifying a CEL expression that produces a string value from JWT token claims.  CEL expressions have access to the token claims through a CEL variable, 'claims'. 'claims' is a map of claim names to claim values. For example, the 'sub' claim value can be accessed as 'claims.sub'. Nested claims can be accessed using dot notation ('claims.foo.bar').  Precisely one of claim or expression must be set. expression must not be specified when claim is set. When specified, expression must be at least 1 character in length and must not exceed 1024 characters in length. |

Show more

#### [3.1.10. .spec.oidcProviders[].claimMappings.username](#spec-oidcproviders-claimmappings-username) Copy linkLink copied to clipboard!

Description
:   username is a required field that configures how the username of a cluster identity should be constructed from the claims in a JWT token issued by the identity provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claim` | `string` | claim is an optional field that configures the JWT token claim whose value is assigned to the cluster identity field associated with this mapping. claim is required when the ExternalOIDCWithUpstreamParity feature gate is not enabled. When the ExternalOIDCWithUpstreamParity feature gate is enabled, claim must not be set when expression is set.  claim must not be an empty string ("") and must not exceed 256 characters. |
| `prefix` | `object` | prefix configures the prefix that should be prepended to the value of the JWT claim.  prefix must be set when prefixPolicy is set to 'Prefix' and must be unset otherwise. |
| `prefixPolicy` | `string` | prefixPolicy is an optional field that configures how a prefix should be applied to the value of the JWT claim specified in the 'claim' field.  Allowed values are 'Prefix', 'NoPrefix', and omitted (not provided or an empty string).  When set to 'Prefix', the value specified in the prefix field will be prepended to the value of the JWT claim. The prefix field must be set when prefixPolicy is 'Prefix'. Must not be set to 'Prefix' when expression is set. When set to 'NoPrefix', no prefix will be prepended to the value of the JWT claim. When omitted, this means no opinion and the platform is left to choose any prefixes that are applied which is subject to change over time. Currently, the platform prepends `{issuerURL}#` to the value of the JWT claim when the claim is not 'email'.  As an example, consider the following scenario:  `prefix` is unset, `issuerURL` is set to `https://myoidc.tld`, the JWT claims include "username":"userA" and "email":"[userA@myoidc.tld](mailto:userA@myoidc.tld)", and `claim` is set to: - "username": the mapped value will be "https://myoidc.tld#userA" - "email": the mapped value will be "[userA@myoidc.tld](mailto:userA@myoidc.tld)" |

Show more

#### [3.1.11. .spec.oidcProviders[].claimMappings.username.prefix](#spec-oidcproviders-claimmappings-username-prefix) Copy linkLink copied to clipboard!

Description
:   prefix configures the prefix that should be prepended to the value of the JWT claim.

    prefix must be set when prefixPolicy is set to 'Prefix' and must be unset otherwise.

Type
:   `object`

Required
:   * `prefixString`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `prefixString` | `string` | prefixString is a required field that configures the prefix that will be applied to cluster identity username attribute during the process of mapping JWT claims to cluster identity attributes.  prefixString must not be an empty string (""). |

Show more

#### [3.1.12. .spec.oidcProviders[].claimValidationRules](#spec-oidcproviders-claimvalidationrules) Copy linkLink copied to clipboard!

Description
:   claimValidationRules is an optional field that configures the rules to be used by the Kubernetes API server for validating the claims in a JWT token issued by the identity provider.

    Validation rules are joined via an AND operation.

Type
:   `array`

#### [3.1.13. .spec.oidcProviders[].claimValidationRules[]](#spec-oidcproviders-claimvalidationrules-2) Copy linkLink copied to clipboard!

Description
:   TokenClaimValidationRule represents a validation rule based on token claims. If type is RequiredClaim, requiredClaim must be set. If Type is CEL, CEL must be set and RequiredClaim must be omitted.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `requiredClaim` | `object` | requiredClaim allows configuring a required claim name and its expected value. This field is required when `type` is set to RequiredClaim, and must be omitted when `type` is set to any other value. The Kubernetes API server uses this field to validate if an incoming JWT is valid for this identity provider. |
| `type` | `string` | type is an optional field that configures the type of the validation rule.  Allowed values are "RequiredClaim" and "CEL".  When set to 'RequiredClaim', the Kubernetes API server will be configured to validate that the incoming JWT contains the required claim and that its value matches the required value.  When set to 'CEL', the Kubernetes API server will be configured to validate the incoming JWT against the configured CEL expression. |

Show more

#### [3.1.14. .spec.oidcProviders[].claimValidationRules[].requiredClaim](#spec-oidcproviders-claimvalidationrules-requiredclaim) Copy linkLink copied to clipboard!

Description
:   requiredClaim allows configuring a required claim name and its expected value. This field is required when `type` is set to RequiredClaim, and must be omitted when `type` is set to any other value. The Kubernetes API server uses this field to validate if an incoming JWT is valid for this identity provider.

Type
:   `object`

Required
:   * `claim`
    * `requiredValue`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claim` | `string` | claim is a required field that configures the name of the required claim. When taken from the JWT claims, claim must be a string value.  claim must not be an empty string (""). |
| `requiredValue` | `string` | requiredValue is a required field that configures the value that 'claim' must have when taken from the incoming JWT claims. If the value in the JWT claims does not match, the token will be rejected for authentication.  requiredValue must not be an empty string (""). |

Show more

#### [3.1.15. .spec.oidcProviders[].issuer](#spec-oidcproviders-issuer) Copy linkLink copied to clipboard!

Description
:   issuer is a required field that configures how the platform interacts with the identity provider and how tokens issued from the identity provider are evaluated by the Kubernetes API server.

Type
:   `object`

Required
:   * `audiences`
    * `issuerURL`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `audiences` | `array (string)` | audiences is a required field that configures the acceptable audiences the JWT token, issued by the identity provider, must be issued to. At least one of the entries must match the 'aud' claim in the JWT token.  audiences must contain at least one entry and must not exceed ten entries. |
| `issuerCertificateAuthority` | `object` | issuerCertificateAuthority is an optional field that configures the certificate authority, used by the Kubernetes API server, to validate the connection to the identity provider when fetching discovery information.  When not specified, the system trust is used.  When specified, it must reference a ConfigMap in the openshift-config namespace containing the PEM-encoded CA certificates under the 'ca-bundle.crt' key in the data field of the ConfigMap. |
| `issuerURL` | `string` | issuerURL is a required field that configures the URL used to issue tokens by the identity provider. The Kubernetes API server determines how authentication tokens should be handled by matching the 'iss' claim in the JWT to the issuerURL of configured identity providers.  Must be at least 1 character and must not exceed 512 characters in length. Must be a valid URL that uses the 'https' scheme and does not contain a query, fragment or user. |

Show more

#### [3.1.16. .spec.oidcProviders[].issuer.issuerCertificateAuthority](#spec-oidcproviders-issuer-issuercertificateauthority) Copy linkLink copied to clipboard!

Description
:   issuerCertificateAuthority is an optional field that configures the certificate authority, used by the Kubernetes API server, to validate the connection to the identity provider when fetching discovery information.

    When not specified, the system trust is used.

    When specified, it must reference a ConfigMap in the openshift-config namespace containing the PEM-encoded CA certificates under the 'ca-bundle.crt' key in the data field of the ConfigMap.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [3.1.17. .spec.oidcProviders[].oidcClients](#spec-oidcproviders-oidcclients) Copy linkLink copied to clipboard!

Description
:   oidcClients is an optional field that configures how on-cluster, platform clients should request tokens from the identity provider. oidcClients must not exceed 20 entries and entries must have unique namespace/name pairs.

Type
:   `array`

#### [3.1.18. .spec.oidcProviders[].oidcClients[]](#spec-oidcproviders-oidcclients-2) Copy linkLink copied to clipboard!

Description
:   OIDCClientConfig configures how platform clients interact with identity providers as an authentication method.

Type
:   `object`

Required
:   * `clientID`
    * `componentName`
    * `componentNamespace`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clientID` | `string` | clientID is a required field that configures the client identifier, from the identity provider, that the platform component uses for authentication requests made to the identity provider. The identity provider must accept this identifier for platform components to be able to use the identity provider as an authentication mode.  clientID must not be an empty string (""). |
| `clientSecret` | `object` | clientSecret is an optional field that configures the client secret used by the platform component when making authentication requests to the identity provider.  When not specified, no client secret will be used when making authentication requests to the identity provider.  When specified, clientSecret references a Secret in the 'openshift-config' namespace that contains the client secret in the 'clientSecret' key of the '.data' field.  The client secret will be used when making authentication requests to the identity provider.  Public clients do not require a client secret but private clients do require a client secret to work with the identity provider. |
| `componentName` | `string` | componentName is a required field that specifies the name of the platform component being configured to use the identity provider as an authentication mode.  It is used in combination with componentNamespace as a unique identifier.  componentName must not be an empty string ("") and must not exceed 256 characters in length. |
| `componentNamespace` | `string` | componentNamespace is a required field that specifies the namespace in which the platform component being configured to use the identity provider as an authentication mode is running.  It is used in combination with componentName as a unique identifier.  componentNamespace must not be an empty string ("") and must not exceed 63 characters in length. |
| `extraScopes` | `array (string)` | extraScopes is an optional field that configures the extra scopes that should be requested by the platform component when making authentication requests to the identity provider. This is useful if you have configured claim mappings that requires specific scopes to be requested beyond the standard OIDC scopes.  When omitted, no additional scopes are requested. |

Show more

#### [3.1.19. .spec.oidcProviders[].oidcClients[].clientSecret](#spec-oidcproviders-oidcclients-clientsecret) Copy linkLink copied to clipboard!

Description
:   clientSecret is an optional field that configures the client secret used by the platform component when making authentication requests to the identity provider.

    When not specified, no client secret will be used when making authentication requests to the identity provider.

    When specified, clientSecret references a Secret in the 'openshift-config' namespace that contains the client secret in the 'clientSecret' key of the '.data' field.

    The client secret will be used when making authentication requests to the identity provider.

    Public clients do not require a client secret but private clients do require a client secret to work with the identity provider.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [3.1.20. .spec.webhookTokenAuthenticator](#spec-webhooktokenauthenticator) Copy linkLink copied to clipboard!

Description
:   webhookTokenAuthenticator configures a remote token reviewer. These remote authentication webhooks can be used to verify bearer tokens via the tokenreviews.authentication.k8s.io REST API. This is required to honor bearer tokens that are provisioned by an external authentication service.

    Can only be set if "Type" is set to "None".

Type
:   `object`

Required
:   * `kubeConfig`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `kubeConfig` | `object` | kubeConfig references a secret that contains kube config file data which describes how to access the remote webhook service. The namespace for the referenced secret is openshift-config.  For further details, see:  <https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication>  The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored. |

Show more

#### [3.1.21. .spec.webhookTokenAuthenticator.kubeConfig](#spec-webhooktokenauthenticator-kubeconfig) Copy linkLink copied to clipboard!

Description
:   kubeConfig references a secret that contains kube config file data which describes how to access the remote webhook service. The namespace for the referenced secret is openshift-config.

    For further details, see:

    <https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication>

    The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [3.1.22. .spec.webhookTokenAuthenticators](#spec-webhooktokenauthenticators) Copy linkLink copied to clipboard!

Description
:   webhookTokenAuthenticators is DEPRECATED, setting it has no effect.

Type
:   `array`

#### [3.1.23. .spec.webhookTokenAuthenticators[]](#spec-webhooktokenauthenticators-2) Copy linkLink copied to clipboard!

Description
:   deprecatedWebhookTokenAuthenticator holds the necessary configuration options for a remote token authenticator. It’s the same as WebhookTokenAuthenticator but it’s missing the 'required' validation on KubeConfig field.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `kubeConfig` | `object` | kubeConfig contains kube config file data which describes how to access the remote webhook service. For further details, see: <https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication> The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored. The namespace for this secret is determined by the point of use. |

Show more

#### [3.1.24. .spec.webhookTokenAuthenticators[].kubeConfig](#spec-webhooktokenauthenticators-kubeconfig) Copy linkLink copied to clipboard!

Description
:   kubeConfig contains kube config file data which describes how to access the remote webhook service. For further details, see: <https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication> The key "kubeConfig" is used to locate the data. If the secret or expected key is not found, the webhook is not honored. If the specified kube config data is not valid, the webhook is not honored. The namespace for this secret is determined by the point of use.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [3.1.25. .status](#status-2) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `integratedOAuthMetadata` | `object` | integratedOAuthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for the in-cluster integrated OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> This contains the observed value based on cluster state. An explicitly set value in spec.oauthMetadata has precedence over this field. This field has no meaning if authentication spec.type is not set to IntegratedOAuth. The key "oauthMetadata" is used to locate the data. If the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config-managed. |
| `oidcClients` | `array` | oidcClients is where participating operators place the current OIDC client status for OIDC clients that can be customized by the cluster-admin. |
| `oidcClients[]` | `object` | OIDCClientStatus represents the current state of platform components and how they interact with the configured identity providers. |

Show more

#### [3.1.26. .status.integratedOAuthMetadata](#status-integratedoauthmetadata) Copy linkLink copied to clipboard!

Description
:   integratedOAuthMetadata contains the discovery endpoint data for OAuth 2.0 Authorization Server Metadata for the in-cluster integrated OAuth server. This discovery document can be viewed from its served location: oc get --raw '/.well-known/oauth-authorization-server' For further details, see the IETF Draft: <https://tools.ietf.org/html/draft-ietf-oauth-discovery-04#section-2> This contains the observed value based on cluster state. An explicitly set value in spec.oauthMetadata has precedence over this field. This field has no meaning if authentication spec.type is not set to IntegratedOAuth. The key "oauthMetadata" is used to locate the data. If the config map or expected key is not found, no metadata is served. If the specified metadata is not valid, no metadata is served. The namespace for this config map is openshift-config-managed.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [3.1.27. .status.oidcClients](#status-oidcclients) Copy linkLink copied to clipboard!

Description
:   oidcClients is where participating operators place the current OIDC client status for OIDC clients that can be customized by the cluster-admin.

Type
:   `array`

#### [3.1.28. .status.oidcClients[]](#status-oidcclients-2) Copy linkLink copied to clipboard!

Description
:   OIDCClientStatus represents the current state of platform components and how they interact with the configured identity providers.

Type
:   `object`

Required
:   * `componentName`
    * `componentNamespace`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `componentName` | `string` | componentName is a required field that specifies the name of the platform component using the identity provider as an authentication mode. It is used in combination with componentNamespace as a unique identifier.  componentName must not be an empty string ("") and must not exceed 256 characters in length. |
| `componentNamespace` | `string` | componentNamespace is a required field that specifies the namespace in which the platform component using the identity provider as an authentication mode is running.  It is used in combination with componentName as a unique identifier.  componentNamespace must not be an empty string ("") and must not exceed 63 characters in length. |
| `conditions` | `array` | conditions are used to communicate the state of the `oidcClients` entry.  Supported conditions include Available, Degraded and Progressing.  If Available is true, the component is successfully using the configured client. If Degraded is true, that means something has gone wrong trying to handle the client configuration. If Progressing is true, that means the component is taking some action related to the `oidcClients` entry. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `consumingUsers` | `array (string)` | consumingUsers is an optional list of ServiceAccounts requiring read permissions on the `clientSecret` secret.  consumingUsers must not exceed 5 entries. |
| `currentOIDCClients` | `array` | currentOIDCClients is an optional list of clients that the component is currently using.  Entries must have unique issuerURL/clientID pairs. |
| `currentOIDCClients[]` | `object` | OIDCClientReference is a reference to a platform component client configuration. |

Show more

#### [3.1.29. .status.oidcClients[].conditions](#status-oidcclients-conditions) Copy linkLink copied to clipboard!

Description
:   conditions are used to communicate the state of the `oidcClients` entry.

    Supported conditions include Available, Degraded and Progressing.

    If Available is true, the component is successfully using the configured client. If Degraded is true, that means something has gone wrong trying to handle the client configuration. If Progressing is true, that means the component is taking some action related to the `oidcClients` entry.

Type
:   `array`

#### [3.1.30. .status.oidcClients[].conditions[]](#status-oidcclients-conditions-2) Copy linkLink copied to clipboard!

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

#### [3.1.31. .status.oidcClients[].currentOIDCClients](#status-oidcclients-currentoidcclients) Copy linkLink copied to clipboard!

Description
:   currentOIDCClients is an optional list of clients that the component is currently using.

    Entries must have unique issuerURL/clientID pairs.

Type
:   `array`

#### [3.1.32. .status.oidcClients[].currentOIDCClients[]](#status-oidcclients-currentoidcclients-2) Copy linkLink copied to clipboard!

Description
:   OIDCClientReference is a reference to a platform component client configuration.

Type
:   `object`

Required
:   * `clientID`
    * `issuerURL`
    * `oidcProviderName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clientID` | `string` | clientID is a required field that specifies the client identifier, from the identity provider, that the platform component is using for authentication requests made to the identity provider.  clientID must not be empty. |
| `issuerURL` | `string` | issuerURL is a required field that specifies the URL of the identity provider that this client is configured to make requests against.  issuerURL must use the 'https' scheme. |
| `oidcProviderName` | `string` | oidcProviderName is a required reference to the 'name' of the identity provider configured in 'oidcProviders' that this client is associated with.  oidcProviderName must not be an empty string (""). |

Show more

### [3.2. API endpoints](#api-endpoints-2) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/authentications`

  + `DELETE`: delete collection of Authentication
  + `GET`: list objects of kind Authentication
  + `POST`: create an Authentication
* `/apis/config.openshift.io/v1/authentications/{name}`

  + `DELETE`: delete an Authentication
  + `GET`: read the specified Authentication
  + `PATCH`: partially update the specified Authentication
  + `PUT`: replace the specified Authentication
* `/apis/config.openshift.io/v1/authentications/{name}/status`

  + `GET`: read status of the specified Authentication
  + `PATCH`: partially update status of the specified Authentication
  + `PUT`: replace status of the specified Authentication

#### [3.2.1. /apis/config.openshift.io/v1/authentications](#apisconfig-openshift-iov1authentications) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Authentication

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
:   list objects of kind Authentication

Expand

Table 3.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`AuthenticationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-AuthenticationList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an Authentication

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
| `body` | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 201 - Created | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.2. /apis/config.openshift.io/v1/authentications/{name}](#apisconfig-openshift-iov1authenticationsname) Copy linkLink copied to clipboard!

Expand

Table 3.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Authentication |

Show more

HTTP method
:   `DELETE`

Description
:   delete an Authentication

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
:   read the specified Authentication

Expand

Table 3.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Authentication

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
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Authentication

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
| `body` | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 201 - Created | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [3.2.3. /apis/config.openshift.io/v1/authentications/{name}/status](#apisconfig-openshift-iov1authenticationsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 3.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Authentication |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Authentication

Expand

Table 3.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Authentication

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
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Authentication

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
| `body` | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 3.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 201 - Created | [`Authentication`](#authentication-config-openshift-io-v1 "Chapter 3. Authentication [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 4. Build [config.openshift.io/v1]](#build-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Build configures the behavior of OpenShift builds for the entire cluster. This includes default settings that can be overridden in BuildConfig objects, and overrides which are applied to all builds.

    The canonical name is "cluster"

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user-settable values for the build controller configuration |

Show more

#### [4.1.1. .spec](#spec-3) Copy linkLink copied to clipboard!

Description
:   spec holds user-settable values for the build controller configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalTrustedCA` | `object` | additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted for image pushes and pulls during builds. The namespace for this config map is openshift-config.  DEPRECATED: Additional CAs for image pull and push should be set on image.config.openshift.io/cluster instead. |
| `buildDefaults` | `object` | buildDefaults controls the default information for Builds |
| `buildOverrides` | `object` | buildOverrides controls override settings for builds |

Show more

#### [4.1.2. .spec.additionalTrustedCA](#spec-additionaltrustedca) Copy linkLink copied to clipboard!

Description
:   additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted for image pushes and pulls during builds. The namespace for this config map is openshift-config.

    DEPRECATED: Additional CAs for image pull and push should be set on image.config.openshift.io/cluster instead.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [4.1.3. .spec.buildDefaults](#spec-builddefaults) Copy linkLink copied to clipboard!

Description
:   buildDefaults controls the default information for Builds

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultProxy` | `object` | defaultProxy contains the default proxy settings for all build operations, including image pull/push and source download.  Values can be overrode by setting the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables in the build config’s strategy. |
| `env` | `array` | env is a set of default environment variables that will be applied to the build if the specified variables do not exist on the build |
| `env[]` | `object` | EnvVar represents an environment variable present in a Container. |
| `gitProxy` | `object` | gitProxy contains the proxy settings for git operations only. If set, this will override any Proxy settings for all git commands, such as git clone.  Values that are not set here will be inherited from DefaultProxy. |
| `imageLabels` | `array` | imageLabels is a list of docker labels that are applied to the resulting image. User can override a default label by providing a label with the same name in their Build/BuildConfig. |
| `imageLabels[]` | `object` |  |
| `resources` | `object` | resources defines resource requirements to execute the build. |

Show more

#### [4.1.4. .spec.buildDefaults.defaultProxy](#spec-builddefaults-defaultproxy) Copy linkLink copied to clipboard!

Description
:   defaultProxy contains the default proxy settings for all build operations, including image pull/push and source download.

    Values can be overrode by setting the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables in the build config’s strategy.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `httpProxy` | `string` | httpProxy is the URL of the proxy for HTTP requests. Empty means unset and will not result in an env var. |
| `httpsProxy` | `string` | httpsProxy is the URL of the proxy for HTTPS requests. Empty means unset and will not result in an env var. |
| `noProxy` | `string` | noProxy is a comma-separated list of hostnames and/or CIDRs and/or IPs for which the proxy should not be used. Empty means unset and will not result in an env var. |
| `readinessEndpoints` | `array (string)` | readinessEndpoints is a list of endpoints used to verify readiness of the proxy. |
| `trustedCA` | `object` | trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.  The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):  apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: | -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE----- |

Show more

#### [4.1.5. .spec.buildDefaults.defaultProxy.trustedCA](#spec-builddefaults-defaultproxy-trustedca) Copy linkLink copied to clipboard!

Description
:   trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.

    The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):

    apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: \| -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE-----

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [4.1.6. .spec.buildDefaults.env](#spec-builddefaults-env) Copy linkLink copied to clipboard!

Description
:   env is a set of default environment variables that will be applied to the build if the specified variables do not exist on the build

Type
:   `array`

#### [4.1.7. .spec.buildDefaults.env[]](#spec-builddefaults-env-2) Copy linkLink copied to clipboard!

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
| `valueFrom` | `object` | Source for the environment variable’s value. Cannot be used if value is not empty. |

Show more

#### [4.1.8. .spec.buildDefaults.env[].valueFrom](#spec-builddefaults-env-valuefrom) Copy linkLink copied to clipboard!

Description
:   Source for the environment variable’s value. Cannot be used if value is not empty.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configMapKeyRef` | `object` | Selects a key of a ConfigMap. |
| `fieldRef` | `object` | Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. |
| `fileKeyRef` | `object` | FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled. |
| `resourceFieldRef` | `object` | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. |
| `secretKeyRef` | `object` | Selects a key of a secret in the pod’s namespace |

Show more

#### [4.1.9. .spec.buildDefaults.env[].valueFrom.configMapKeyRef](#spec-builddefaults-env-valuefrom-configmapkeyref) Copy linkLink copied to clipboard!

Description
:   Selects a key of a ConfigMap.

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

#### [4.1.10. .spec.buildDefaults.env[].valueFrom.fieldRef](#spec-builddefaults-env-valuefrom-fieldref) Copy linkLink copied to clipboard!

Description
:   Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

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

#### [4.1.11. .spec.buildDefaults.env[].valueFrom.fileKeyRef](#spec-builddefaults-env-valuefrom-filekeyref) Copy linkLink copied to clipboard!

Description
:   FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled.

Type
:   `object`

Required
:   * `key`
    * `path`
    * `volumeName`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters. |
| `optional` | `boolean` | Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod’s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation. |
| `path` | `string` | The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'. |
| `volumeName` | `string` | The name of the volume mount containing the env file. |

Show more

#### [4.1.12. .spec.buildDefaults.env[].valueFrom.resourceFieldRef](#spec-builddefaults-env-valuefrom-resourcefieldref) Copy linkLink copied to clipboard!

Description
:   Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

Type
:   `object`

Required
:   * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | `integer-or-string` | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

Show more

#### [4.1.13. .spec.buildDefaults.env[].valueFrom.secretKeyRef](#spec-builddefaults-env-valuefrom-secretkeyref) Copy linkLink copied to clipboard!

Description
:   Selects a key of a secret in the pod’s namespace

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

#### [4.1.14. .spec.buildDefaults.gitProxy](#spec-builddefaults-gitproxy) Copy linkLink copied to clipboard!

Description
:   gitProxy contains the proxy settings for git operations only. If set, this will override any Proxy settings for all git commands, such as git clone.

    Values that are not set here will be inherited from DefaultProxy.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `httpProxy` | `string` | httpProxy is the URL of the proxy for HTTP requests. Empty means unset and will not result in an env var. |
| `httpsProxy` | `string` | httpsProxy is the URL of the proxy for HTTPS requests. Empty means unset and will not result in an env var. |
| `noProxy` | `string` | noProxy is a comma-separated list of hostnames and/or CIDRs and/or IPs for which the proxy should not be used. Empty means unset and will not result in an env var. |
| `readinessEndpoints` | `array (string)` | readinessEndpoints is a list of endpoints used to verify readiness of the proxy. |
| `trustedCA` | `object` | trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.  The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):  apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: | -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE----- |

Show more

#### [4.1.15. .spec.buildDefaults.gitProxy.trustedCA](#spec-builddefaults-gitproxy-trustedca) Copy linkLink copied to clipboard!

Description
:   trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.

    The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):

    apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: \| -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE-----

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [4.1.16. .spec.buildDefaults.imageLabels](#spec-builddefaults-imagelabels) Copy linkLink copied to clipboard!

Description
:   imageLabels is a list of docker labels that are applied to the resulting image. User can override a default label by providing a label with the same name in their Build/BuildConfig.

Type
:   `array`

#### [4.1.17. .spec.buildDefaults.imageLabels[]](#spec-builddefaults-imagelabels-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name defines the name of the label. It must have non-zero length. |
| `value` | `string` | value defines the literal value of the label. |

Show more

#### [4.1.18. .spec.buildDefaults.resources](#spec-builddefaults-resources) Copy linkLink copied to clipboard!

Description
:   resources defines resource requirements to execute the build.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claims` | `array` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. |
| `claims[]` | `object` | ResourceClaim references one entry in PodSpec.ResourceClaims. |
| `limits` | `integer-or-string` | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | `integer-or-string` | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

#### [4.1.19. .spec.buildDefaults.resources.claims](#spec-builddefaults-resources-claims) Copy linkLink copied to clipboard!

Description
:   Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This field depends on the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.

Type
:   `array`

#### [4.1.20. .spec.buildDefaults.resources.claims[]](#spec-builddefaults-resources-claims-2) Copy linkLink copied to clipboard!

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

#### [4.1.21. .spec.buildOverrides](#spec-buildoverrides) Copy linkLink copied to clipboard!

Description
:   buildOverrides controls override settings for builds

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `forcePull` | `boolean` | forcePull overrides, if set, the equivalent value in the builds, i.e. false disables force pull for all builds, true enables force pull for all builds, independently of what each build specifies itself |
| `imageLabels` | `array` | imageLabels is a list of docker labels that are applied to the resulting image. If user provided a label in their Build/BuildConfig with the same name as one in this list, the user’s label will be overwritten. |
| `imageLabels[]` | `object` |  |
| `nodeSelector` | `object (string)` | nodeSelector is a selector which must be true for the build pod to fit on a node |
| `tolerations` | `array` | tolerations is a list of Tolerations that will override any existing tolerations set on a build pod. |
| `tolerations[]` | `object` | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [4.1.22. .spec.buildOverrides.imageLabels](#spec-buildoverrides-imagelabels) Copy linkLink copied to clipboard!

Description
:   imageLabels is a list of docker labels that are applied to the resulting image. If user provided a label in their Build/BuildConfig with the same name as one in this list, the user’s label will be overwritten.

Type
:   `array`

#### [4.1.23. .spec.buildOverrides.imageLabels[]](#spec-buildoverrides-imagelabels-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name defines the name of the label. It must have non-zero length. |
| `value` | `string` | value defines the literal value of the label. |

Show more

#### [4.1.24. .spec.buildOverrides.tolerations](#spec-buildoverrides-tolerations) Copy linkLink copied to clipboard!

Description
:   tolerations is a list of Tolerations that will override any existing tolerations set on a build pod.

Type
:   `array`

#### [4.1.25. .spec.buildOverrides.tolerations[]](#spec-buildoverrides-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators). |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

Show more

### [4.2. API endpoints](#api-endpoints-3) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/builds`

  + `DELETE`: delete collection of Build
  + `GET`: list objects of kind Build
  + `POST`: create a Build
* `/apis/config.openshift.io/v1/builds/{name}`

  + `DELETE`: delete a Build
  + `GET`: read the specified Build
  + `PATCH`: partially update the specified Build
  + `PUT`: replace the specified Build
* `/apis/config.openshift.io/v1/builds/{name}/status`

  + `GET`: read status of the specified Build
  + `PATCH`: partially update status of the specified Build
  + `PUT`: replace status of the specified Build

#### [4.2.1. /apis/config.openshift.io/v1/builds](#apisconfig-openshift-iov1builds) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Build

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
:   list objects of kind Build

Expand

Table 4.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`BuildList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-BuildList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Build

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
| `body` | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 201 - Created | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.2. /apis/config.openshift.io/v1/builds/{name}](#apisconfig-openshift-iov1buildsname) Copy linkLink copied to clipboard!

Expand

Table 4.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Build |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Build

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
:   read the specified Build

Expand

Table 4.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Build

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
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Build

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
| `body` | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 201 - Created | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [4.2.3. /apis/config.openshift.io/v1/builds/{name}/status](#apisconfig-openshift-iov1buildsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 4.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Build |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Build

Expand

Table 4.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Build

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
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Build

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
| `body` | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 4.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 201 - Created | [`Build`](#build-config-openshift-io-v1 "Chapter 4. Build [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 5. ClusterImagePolicy [config.openshift.io/v1]](#clusterimagepolicy-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterImagePolicy holds cluster-wide configuration for image signature verification

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec contains the configuration for the cluster image policy. |
| `status` | `object` | status contains the observed state of the resource. |

Show more

#### [5.1.1. .spec](#spec-4) Copy linkLink copied to clipboard!

Description
:   spec contains the configuration for the cluster image policy.

Type
:   `object`

Required
:   * `policy`
    * `scopes`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `policy` | `object` | policy is a required field that contains configuration to allow scopes to be verified, and defines how images not matching the verification policy will be treated. |
| `scopes` | `array (string)` | scopes is a required field that defines the list of image identities assigned to a policy. Each item refers to a scope in a registry implementing the "Docker Registry HTTP API V2". Scopes matching individual images are named Docker references in the fully expanded form, either using a tag or digest. For example, docker.io/library/busybox:latest (not busybox:latest). More general scopes are prefixes of individual-image scopes, and specify a repository (by omitting the tag or digest), a repository namespace, or a registry host (by only specifying the host name and possibly a port number) or a wildcard expression starting with `*.`, for matching all subdomains (not including a port number). Wildcards are only supported for subdomain matching, and may not be used in the middle of the host, i.e. \\*.example.com is a valid case, but example\*.\*.com is not. This support no more than 256 scopes in one object. If multiple scopes match a given image, only the policy requirements for the most specific scope apply. The policy requirements for more general scopes are ignored. In addition to setting a policy appropriate for your own deployed applications, make sure that a policy on the OpenShift image repositories quay.io/openshift-release-dev/ocp-release, quay.io/openshift-release-dev/ocp-v4.0-art-dev (or on a more general scope) allows deployment of the OpenShift images required for cluster operation. If a scope is configured in both the ClusterImagePolicy and the ImagePolicy, or if the scope in ImagePolicy is nested under one of the scopes from the ClusterImagePolicy, only the policy from the ClusterImagePolicy will be applied. For additional details about the format, please refer to the document explaining the docker transport field, which can be found at: <https://github.com/containers/image/blob/main/docs/containers-policy.json.5.md#docker> |

Show more

#### [5.1.2. .spec.policy](#spec-policy) Copy linkLink copied to clipboard!

Description
:   policy is a required field that contains configuration to allow scopes to be verified, and defines how images not matching the verification policy will be treated.

Type
:   `object`

Required
:   * `rootOfTrust`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rootOfTrust` | `object` | rootOfTrust is a required field that defines the root of trust for verifying image signatures during retrieval. This allows image consumers to specify policyType and corresponding configuration of the policy, matching how the policy was generated. |
| `signedIdentity` | `object` | signedIdentity is an optional field specifies what image identity the signature claims about the image. This is useful when the image identity in the signature differs from the original image spec, such as when mirror registry is configured for the image scope, the signature from the mirror registry contains the image identity of the mirror instead of the original scope. The required matchPolicy field specifies the approach used in the verification process to verify the identity in the signature and the actual image identity, the default matchPolicy is "MatchRepoDigestOrExact". |

Show more

#### [5.1.3. .spec.policy.rootOfTrust](#spec-policy-rootoftrust) Copy linkLink copied to clipboard!

Description
:   rootOfTrust is a required field that defines the root of trust for verifying image signatures during retrieval. This allows image consumers to specify policyType and corresponding configuration of the policy, matching how the policy was generated.

Type
:   `object`

Required
:   * `policyType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fulcioCAWithRekor` | `object` | fulcioCAWithRekor defines the root of trust configuration based on the Fulcio certificate and the Rekor public key. fulcioCAWithRekor is required when policyType is FulcioCAWithRekor, and forbidden otherwise For more information about Fulcio and Rekor, please refer to the document at: <https://github.com/sigstore/fulcio> and <https://github.com/sigstore/rekor> |
| `pki` | `object` | pki defines the root of trust configuration based on Bring Your Own Public Key Infrastructure (BYOPKI) Root CA(s) and corresponding intermediate certificates. pki is required when policyType is PKI, and forbidden otherwise. |
| `policyType` | `string` | policyType is a required field specifies the type of the policy for verification. This field must correspond to how the policy was generated. Allowed values are "PublicKey", "FulcioCAWithRekor", and "PKI". When set to "PublicKey", the policy relies on a sigstore publicKey and may optionally use a Rekor verification. When set to "FulcioCAWithRekor", the policy is based on the Fulcio certification and incorporates a Rekor verification. When set to "PKI", the policy is based on the certificates from Bring Your Own Public Key Infrastructure (BYOPKI). |
| `publicKey` | `object` | publicKey defines the root of trust configuration based on a sigstore public key. Optionally include a Rekor public key for Rekor verification. publicKey is required when policyType is PublicKey, and forbidden otherwise. |

Show more

#### [5.1.4. .spec.policy.rootOfTrust.fulcioCAWithRekor](#spec-policy-rootoftrust-fulciocawithrekor) Copy linkLink copied to clipboard!

Description
:   fulcioCAWithRekor defines the root of trust configuration based on the Fulcio certificate and the Rekor public key. fulcioCAWithRekor is required when policyType is FulcioCAWithRekor, and forbidden otherwise For more information about Fulcio and Rekor, please refer to the document at: <https://github.com/sigstore/fulcio> and <https://github.com/sigstore/rekor>

Type
:   `object`

Required
:   * `fulcioCAData`
    * `fulcioSubject`
    * `rekorKeyData`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fulcioCAData` | `string` | fulcioCAData is a required field contains inline base64-encoded data for the PEM format fulcio CA. fulcioCAData must be at most 8192 characters. |
| `fulcioSubject` | `object` | fulcioSubject is a required field specifies OIDC issuer and the email of the Fulcio authentication configuration. |
| `rekorKeyData` | `string` | rekorKeyData is a required field contains inline base64-encoded data for the PEM format from the Rekor public key. rekorKeyData must be at most 8192 characters. |

Show more

#### [5.1.5. .spec.policy.rootOfTrust.fulcioCAWithRekor.fulcioSubject](#spec-policy-rootoftrust-fulciocawithrekor-fulciosubject) Copy linkLink copied to clipboard!

Description
:   fulcioSubject is a required field specifies OIDC issuer and the email of the Fulcio authentication configuration.

Type
:   `object`

Required
:   * `oidcIssuer`
    * `signedEmail`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `oidcIssuer` | `string` | oidcIssuer is a required filed contains the expected OIDC issuer. The oidcIssuer must be a valid URL and at most 2048 characters in length. It will be verified that the Fulcio-issued certificate contains a (Fulcio-defined) certificate extension pointing at this OIDC issuer URL. When Fulcio issues certificates, it includes a value based on an URL inside the client-provided ID token. Example: "https://expected.OIDC.issuer/" |
| `signedEmail` | `string` | signedEmail is a required field holds the email address that the Fulcio certificate is issued for. The signedEmail must be a valid email address and at most 320 characters in length. Example: "[expected-signing-user@example.com](mailto:expected-signing-user@example.com)" |

Show more

#### [5.1.6. .spec.policy.rootOfTrust.pki](#spec-policy-rootoftrust-pki) Copy linkLink copied to clipboard!

Description
:   pki defines the root of trust configuration based on Bring Your Own Public Key Infrastructure (BYOPKI) Root CA(s) and corresponding intermediate certificates. pki is required when policyType is PKI, and forbidden otherwise.

Type
:   `object`

Required
:   * `caRootsData`
    * `pkiCertificateSubject`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caIntermediatesData` | `string` | caIntermediatesData contains base64-encoded data of a certificate bundle PEM file, which contains one or more intermediate certificates in the PEM format. The total length of the data must not exceed 8192 characters. caIntermediatesData requires caRootsData to be set. |
| `caRootsData` | `string` | caRootsData contains base64-encoded data of a certificate bundle PEM file, which contains one or more CA roots in the PEM format. The total length of the data must not exceed 8192 characters. |
| `pkiCertificateSubject` | `object` | pkiCertificateSubject defines the requirements imposed on the subject to which the certificate was issued. |

Show more

#### [5.1.7. .spec.policy.rootOfTrust.pki.pkiCertificateSubject](#spec-policy-rootoftrust-pki-pkicertificatesubject) Copy linkLink copied to clipboard!

Description
:   pkiCertificateSubject defines the requirements imposed on the subject to which the certificate was issued.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `email` | `string` | email specifies the expected email address imposed on the subject to which the certificate was issued, and must match the email address listed in the Subject Alternative Name (SAN) field of the certificate. The email must be a valid email address and at most 320 characters in length. |
| `hostname` | `string` | hostname specifies the expected hostname imposed on the subject to which the certificate was issued, and it must match the hostname listed in the Subject Alternative Name (SAN) DNS field of the certificate. The hostname must be a valid dns 1123 subdomain name, optionally prefixed by '\*.', and at most 253 characters in length. It must consist only of lowercase alphanumeric characters, hyphens, periods and the optional preceding asterisk. |

Show more

#### [5.1.8. .spec.policy.rootOfTrust.publicKey](#spec-policy-rootoftrust-publickey) Copy linkLink copied to clipboard!

Description
:   publicKey defines the root of trust configuration based on a sigstore public key. Optionally include a Rekor public key for Rekor verification. publicKey is required when policyType is PublicKey, and forbidden otherwise.

Type
:   `object`

Required
:   * `keyData`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `keyData` | `string` | keyData is a required field contains inline base64-encoded data for the PEM format public key. keyData must be at most 8192 characters. |
| `rekorKeyData` | `string` | rekorKeyData is an optional field contains inline base64-encoded data for the PEM format from the Rekor public key. rekorKeyData must be at most 8192 characters. |

Show more

#### [5.1.9. .spec.policy.signedIdentity](#spec-policy-signedidentity) Copy linkLink copied to clipboard!

Description
:   signedIdentity is an optional field specifies what image identity the signature claims about the image. This is useful when the image identity in the signature differs from the original image spec, such as when mirror registry is configured for the image scope, the signature from the mirror registry contains the image identity of the mirror instead of the original scope. The required matchPolicy field specifies the approach used in the verification process to verify the identity in the signature and the actual image identity, the default matchPolicy is "MatchRepoDigestOrExact".

Type
:   `object`

Required
:   * `matchPolicy`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exactRepository` | `object` | exactRepository specifies the repository that must be exactly matched by the identity in the signature. exactRepository is required if matchPolicy is set to "ExactRepository". It is used to verify that the signature claims an identity matching this exact repository, rather than the original image identity. |
| `matchPolicy` | `string` | matchPolicy is a required filed specifies matching strategy to verify the image identity in the signature against the image scope. Allowed values are "MatchRepoDigestOrExact", "MatchRepository", "ExactRepository", "RemapIdentity". When omitted, the default value is "MatchRepoDigestOrExact". When set to "MatchRepoDigestOrExact", the identity in the signature must be in the same repository as the image identity if the image identity is referenced by a digest. Otherwise, the identity in the signature must be the same as the image identity. When set to "MatchRepository", the identity in the signature must be in the same repository as the image identity. When set to "ExactRepository", the exactRepository must be specified. The identity in the signature must be in the same repository as a specific identity specified by "repository". When set to "RemapIdentity", the remapIdentity must be specified. The signature must be in the same as the remapped image identity. Remapped image identity is obtained by replacing the "prefix" with the specified “signedPrefix” if the the image identity matches the specified remapPrefix. |
| `remapIdentity` | `object` | remapIdentity specifies the prefix remapping rule for verifying image identity. remapIdentity is required if matchPolicy is set to "RemapIdentity". It is used to verify that the signature claims a different registry/repository prefix than the original image. |

Show more

#### [5.1.10. .spec.policy.signedIdentity.exactRepository](#spec-policy-signedidentity-exactrepository) Copy linkLink copied to clipboard!

Description
:   exactRepository specifies the repository that must be exactly matched by the identity in the signature. exactRepository is required if matchPolicy is set to "ExactRepository". It is used to verify that the signature claims an identity matching this exact repository, rather than the original image identity.

Type
:   `object`

Required
:   * `repository`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `repository` | `string` | repository is the reference of the image identity to be matched. repository is required if matchPolicy is set to "ExactRepository". The value should be a repository name (by omitting the tag or digest) in a registry implementing the "Docker Registry HTTP API V2". For example, docker.io/library/busybox |

Show more

#### [5.1.11. .spec.policy.signedIdentity.remapIdentity](#spec-policy-signedidentity-remapidentity) Copy linkLink copied to clipboard!

Description
:   remapIdentity specifies the prefix remapping rule for verifying image identity. remapIdentity is required if matchPolicy is set to "RemapIdentity". It is used to verify that the signature claims a different registry/repository prefix than the original image.

Type
:   `object`

Required
:   * `prefix`
    * `signedPrefix`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `prefix` | `string` | prefix is required if matchPolicy is set to "RemapIdentity". prefix is the prefix of the image identity to be matched. If the image identity matches the specified prefix, that prefix is replaced by the specified “signedPrefix” (otherwise it is used as unchanged and no remapping takes place). This is useful when verifying signatures for a mirror of some other repository namespace that preserves the vendor’s repository structure. The prefix and signedPrefix values can be either host[:port] values (matching exactly the same host[:port], string), repository namespaces, or repositories (i.e. they must not contain tags/digests), and match as prefixes of the fully expanded form. For example, docker.io/library/busybox (not busybox) to specify that single repository, or docker.io/library (not an empty string) to specify the parent namespace of docker.io/library/busybox. |
| `signedPrefix` | `string` | signedPrefix is required if matchPolicy is set to "RemapIdentity". signedPrefix is the prefix of the image identity to be matched in the signature. The format is the same as "prefix". The values can be either host[:port] values (matching exactly the same host[:port], string), repository namespaces, or repositories (i.e. they must not contain tags/digests), and match as prefixes of the fully expanded form. For example, docker.io/library/busybox (not busybox) to specify that single repository, or docker.io/library (not an empty string) to specify the parent namespace of docker.io/library/busybox. |

Show more

#### [5.1.12. .status](#status-3) Copy linkLink copied to clipboard!

Description
:   status contains the observed state of the resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions provide details on the status of this API Resource. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |

Show more

#### [5.1.13. .status.conditions](#status-conditions) Copy linkLink copied to clipboard!

Description
:   conditions provide details on the status of this API Resource.

Type
:   `array`

#### [5.1.14. .status.conditions[]](#status-conditions-2) Copy linkLink copied to clipboard!

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

### [5.2. API endpoints](#api-endpoints-4) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/clusterimagepolicies`

  + `DELETE`: delete collection of ClusterImagePolicy
  + `GET`: list objects of kind ClusterImagePolicy
  + `POST`: create a ClusterImagePolicy
* `/apis/config.openshift.io/v1/clusterimagepolicies/{name}`

  + `DELETE`: delete a ClusterImagePolicy
  + `GET`: read the specified ClusterImagePolicy
  + `PATCH`: partially update the specified ClusterImagePolicy
  + `PUT`: replace the specified ClusterImagePolicy
* `/apis/config.openshift.io/v1/clusterimagepolicies/{name}/status`

  + `GET`: read status of the specified ClusterImagePolicy
  + `PATCH`: partially update status of the specified ClusterImagePolicy
  + `PUT`: replace status of the specified ClusterImagePolicy

#### [5.2.1. /apis/config.openshift.io/v1/clusterimagepolicies](#apisconfig-openshift-iov1clusterimagepolicies) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ClusterImagePolicy

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
:   list objects of kind ClusterImagePolicy

Expand

Table 5.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterImagePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ClusterImagePolicyList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterImagePolicy

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
| `body` | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.2. /apis/config.openshift.io/v1/clusterimagepolicies/{name}](#apisconfig-openshift-iov1clusterimagepoliciesname) Copy linkLink copied to clipboard!

Expand

Table 5.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterImagePolicy |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterImagePolicy

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
:   read the specified ClusterImagePolicy

Expand

Table 5.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterImagePolicy

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
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterImagePolicy

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
| `body` | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [5.2.3. /apis/config.openshift.io/v1/clusterimagepolicies/{name}/status](#apisconfig-openshift-iov1clusterimagepoliciesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 5.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterImagePolicy |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ClusterImagePolicy

Expand

Table 5.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ClusterImagePolicy

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
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ClusterImagePolicy

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
| `body` | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 5.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterImagePolicy`](#clusterimagepolicy-config-openshift-io-v1 "Chapter 5. ClusterImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 6. ClusterOperator [config.openshift.io/v1]](#clusteroperator-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterOperator holds the status of a core or optional OpenShift component managed by the Cluster Version Operator (CVO). This object is used by operators to convey their state to the rest of the cluster. Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [6.1. Specification](#specification-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds configuration that could apply to any operator. |
| `status` | `object` | status holds the information about the state of an operator. It is consistent with status information across the Kubernetes ecosystem. |

Show more

#### [6.1.1. .spec](#spec-5) Copy linkLink copied to clipboard!

Description
:   spec holds configuration that could apply to any operator.

Type
:   `object`

#### [6.1.2. .status](#status-4) Copy linkLink copied to clipboard!

Description
:   status holds the information about the state of an operator. It is consistent with status information across the Kubernetes ecosystem.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions describes the state of the operator’s managed and monitored components. |
| `conditions[]` | `object` | ClusterOperatorStatusCondition represents the state of the operator’s managed and monitored components. |
| `extension` | `` | extension contains any additional status information specific to the operator which owns this status object. |
| `relatedObjects` | `array` | relatedObjects is a list of objects that are "interesting" or related to this operator. Common uses are: 1. the detailed resource driving the operator 2. operator namespaces 3. operand namespaces |
| `relatedObjects[]` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |
| `versions` | `array` | versions is a slice of operator and operand version tuples. Operators which manage multiple operands will have multiple operand entries in the array. Available operators must report the version of the operator itself with the name "operator". An operator reports a new "operator" version when it has rolled out the new version to all of its operands. |
| `versions[]` | `object` |  |

Show more

#### [6.1.3. .status.conditions](#status-conditions-3) Copy linkLink copied to clipboard!

Description
:   conditions describes the state of the operator’s managed and monitored components.

Type
:   `array`

#### [6.1.4. .status.conditions[]](#status-conditions-4) Copy linkLink copied to clipboard!

Description
:   ClusterOperatorStatusCondition represents the state of the operator’s managed and monitored components.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the time of the last update to the current status property. |
| `message` | `string` | message provides additional information about the current condition. This is only to be consumed by humans. It may contain Line Feed characters (U+000A), which should be rendered as new lines. |
| `reason` | `string` | reason is the CamelCase reason for the condition’s current status. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type specifies the aspect reported by this condition. |

Show more

#### [6.1.5. .status.relatedObjects](#status-relatedobjects) Copy linkLink copied to clipboard!

Description
:   relatedObjects is a list of objects that are "interesting" or related to this operator. Common uses are: 1. the detailed resource driving the operator 2. operator namespaces 3. operand namespaces

Type
:   `array`

#### [6.1.6. .status.relatedObjects[]](#status-relatedobjects-2) Copy linkLink copied to clipboard!

Description
:   ObjectReference contains enough information to let you inspect or modify the referred object.

Type
:   `object`

Required
:   * `group`
    * `name`
    * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | group of the referent. |
| `name` | `string` | name of the referent. |
| `namespace` | `string` | namespace of the referent. |
| `resource` | `string` | resource of the referent. |

Show more

#### [6.1.7. .status.versions](#status-versions) Copy linkLink copied to clipboard!

Description
:   versions is a slice of operator and operand version tuples. Operators which manage multiple operands will have multiple operand entries in the array. Available operators must report the version of the operator itself with the name "operator". An operator reports a new "operator" version when it has rolled out the new version to all of its operands.

Type
:   `array`

#### [6.1.8. .status.versions[]](#status-versions-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `name`
    * `version`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the particular operand this version is for. It usually matches container images, not operators. |
| `version` | `string` | version indicates which version of a particular operand is currently being managed. It must always match the Available operand. If 1.0.0 is Available, then this must indicate 1.0.0 even if the operator is trying to rollout 1.1.0 |

Show more

### [6.2. API endpoints](#api-endpoints-5) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/clusteroperators`

  + `DELETE`: delete collection of ClusterOperator
  + `GET`: list objects of kind ClusterOperator
  + `POST`: create a ClusterOperator
* `/apis/config.openshift.io/v1/clusteroperators/{name}`

  + `DELETE`: delete a ClusterOperator
  + `GET`: read the specified ClusterOperator
  + `PATCH`: partially update the specified ClusterOperator
  + `PUT`: replace the specified ClusterOperator
* `/apis/config.openshift.io/v1/clusteroperators/{name}/status`

  + `GET`: read status of the specified ClusterOperator
  + `PATCH`: partially update status of the specified ClusterOperator
  + `PUT`: replace status of the specified ClusterOperator

#### [6.2.1. /apis/config.openshift.io/v1/clusteroperators](#apisconfig-openshift-iov1clusteroperators) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ClusterOperator

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
:   list objects of kind ClusterOperator

Expand

Table 6.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperatorList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ClusterOperatorList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterOperator

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
| `body` | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.2. /apis/config.openshift.io/v1/clusteroperators/{name}](#apisconfig-openshift-iov1clusteroperatorsname) Copy linkLink copied to clipboard!

Expand

Table 6.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterOperator |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterOperator

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
:   read the specified ClusterOperator

Expand

Table 6.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterOperator

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
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterOperator

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
| `body` | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [6.2.3. /apis/config.openshift.io/v1/clusteroperators/{name}/status](#apisconfig-openshift-iov1clusteroperatorsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 6.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterOperator |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ClusterOperator

Expand

Table 6.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ClusterOperator

Expand

Table 6.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ClusterOperator

Expand

Table 6.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 6.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 6.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterOperator`](#clusteroperator-config-openshift-io-v1 "Chapter 6. ClusterOperator [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 7. ClusterVersion [config.openshift.io/v1]](#clusterversion-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ClusterVersion is the configuration for the ClusterVersionOperator. This is where parameters related to automatic updates can be set.

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec is the desired state of the cluster version - the operator will work to ensure that the desired version is applied to the cluster. |
| `status` | `object` | status contains information about the available updates and any in-progress updates. |

Show more

#### [7.1.1. .spec](#spec-6) Copy linkLink copied to clipboard!

Description
:   spec is the desired state of the cluster version - the operator will work to ensure that the desired version is applied to the cluster.

Type
:   `object`

Required
:   * `clusterID`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `capabilities` | `object` | capabilities configures the installation of optional, core cluster components. A null value here is identical to an empty object; see the child properties for default semantics. |
| `channel` | `string` | channel is an identifier for explicitly requesting a non-default set of updates to be applied to this cluster. The default channel will contain stable updates that are appropriate for production clusters. |
| `clusterID` | `string` | clusterID uniquely identifies this cluster. This is expected to be an RFC4122 UUID value (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx in hexadecimal values). This is a required field. |
| `desiredUpdate` | `object` | desiredUpdate is an optional field that indicates the desired value of the cluster version. Setting this value will trigger an upgrade (if the current version does not match the desired version). The set of recommended update values is listed as part of available updates in status, and setting values outside that range may cause the upgrade to fail.  Some of the fields are inter-related with restrictions and meanings described here. 1. image is specified, version is specified, architecture is specified. API validation error. 2. image is specified, version is specified, architecture is not specified. The version extracted from the referenced image must match the specified version. 3. image is specified, version is not specified, architecture is specified. API validation error. 4. image is specified, version is not specified, architecture is not specified. image is used. 5. image is not specified, version is specified, architecture is specified. version and desired architecture are used to select an image. 6. image is not specified, version is specified, architecture is not specified. version and current architecture are used to select an image. 7. image is not specified, version is not specified, architecture is specified. API validation error. 8. image is not specified, version is not specified, architecture is not specified. API validation error.  If an upgrade fails the operator will halt and report status about the failing component. Setting the desired update value back to the previous version will cause a rollback to be attempted if the previous version is within the current minor version. Not all rollbacks will succeed, and some may unrecoverably break the cluster. |
| `overrides` | `array` | overrides is list of overides for components that are managed by cluster version operator. Marking a component unmanaged will prevent the operator from creating or updating the object. |
| `overrides[]` | `object` | ComponentOverride allows overriding cluster version operator’s behavior for a component. |
| `upstream` | `string` | upstream may be used to specify the preferred update server. By default it will use the appropriate update server for the cluster and region. |

Show more

#### [7.1.2. .spec.capabilities](#spec-capabilities) Copy linkLink copied to clipboard!

Description
:   capabilities configures the installation of optional, core cluster components. A null value here is identical to an empty object; see the child properties for default semantics.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalEnabledCapabilities` | `array (string)` | additionalEnabledCapabilities extends the set of managed capabilities beyond the baseline defined in baselineCapabilitySet. The default is an empty set. |
| `baselineCapabilitySet` | `string` | baselineCapabilitySet selects an initial set of optional capabilities to enable, which can be extended via additionalEnabledCapabilities. If unset, the cluster will choose a default, and the default may change over time. The current default is vCurrent. |

Show more

#### [7.1.3. .spec.desiredUpdate](#spec-desiredupdate) Copy linkLink copied to clipboard!

Description
:   desiredUpdate is an optional field that indicates the desired value of the cluster version. Setting this value will trigger an upgrade (if the current version does not match the desired version). The set of recommended update values is listed as part of available updates in status, and setting values outside that range may cause the upgrade to fail.

    Some of the fields are inter-related with restrictions and meanings described here. 1. image is specified, version is specified, architecture is specified. API validation error. 2. image is specified, version is specified, architecture is not specified. The version extracted from the referenced image must match the specified version. 3. image is specified, version is not specified, architecture is specified. API validation error. 4. image is specified, version is not specified, architecture is not specified. image is used. 5. image is not specified, version is specified, architecture is specified. version and desired architecture are used to select an image. 6. image is not specified, version is specified, architecture is not specified. version and current architecture are used to select an image. 7. image is not specified, version is not specified, architecture is specified. API validation error. 8. image is not specified, version is not specified, architecture is not specified. API validation error.

    If an upgrade fails the operator will halt and report status about the failing component. Setting the desired update value back to the previous version will cause a rollback to be attempted if the previous version is within the current minor version. Not all rollbacks will succeed, and some may unrecoverably break the cluster.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `architecture` | `string` | architecture is an optional field that indicates the desired value of the cluster architecture. In this context cluster architecture means either a single architecture or a multi architecture. architecture can only be set to Multi thereby only allowing updates from single to multi architecture. If architecture is set, image cannot be set and version must be set. Valid values are 'Multi' and empty. |
| `force` | `boolean` | force allows an administrator to update to an image that has failed verification or upgradeable checks that are designed to keep your cluster safe. Only use this if: \* you are testing unsigned release images in short-lived test clusters or \* you are working around a known bug in the cluster-version operator and you have verified the authenticity of the provided image yourself. The provided image will run with full administrative access to the cluster. Do not use this flag with images that come from unknown or potentially malicious sources. |
| `image` | `string` | image is a container image location that contains the update. image should be used when the desired version does not exist in availableUpdates or history. When image is set, architecture cannot be specified. If both version and image are set, the version extracted from the referenced image must match the specified version. |
| `version` | `string` | version is a semantic version identifying the update version. version is required if architecture is specified. If both version and image are set, the version extracted from the referenced image must match the specified version. |

Show more

#### [7.1.4. .spec.overrides](#spec-overrides) Copy linkLink copied to clipboard!

Description
:   overrides is list of overides for components that are managed by cluster version operator. Marking a component unmanaged will prevent the operator from creating or updating the object.

Type
:   `array`

#### [7.1.5. .spec.overrides[]](#spec-overrides-2) Copy linkLink copied to clipboard!

Description
:   ComponentOverride allows overriding cluster version operator’s behavior for a component.

Type
:   `object`

Required
:   * `group`
    * `kind`
    * `name`
    * `namespace`
    * `unmanaged`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | group identifies the API group that the kind is in. |
| `kind` | `string` | kind indentifies which object to override. |
| `name` | `string` | name is the component’s name. |
| `namespace` | `string` | namespace is the component’s namespace. If the resource is cluster scoped, the namespace should be empty. |
| `unmanaged` | `boolean` | unmanaged controls if cluster version operator should stop managing the resources in this cluster. Default: false |

Show more

#### [7.1.6. .status](#status-5) Copy linkLink copied to clipboard!

Description
:   status contains information about the available updates and any in-progress updates.

Type
:   `object`

Required
:   * `desired`
    * `observedGeneration`
    * `versionHash`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `availableUpdates` | `` | availableUpdates contains updates recommended for this cluster. Updates which appear in conditionalUpdates but not in availableUpdates may expose this cluster to known issues. This list may be empty if no updates are recommended, if the update service is unavailable, or if an invalid channel has been specified. |
| `capabilities` | `object` | capabilities describes the state of optional, core cluster components. |
| `conditionalUpdates` | `array` | conditionalUpdates contains the list of updates that may be recommended for this cluster if it meets specific required conditions. Consumers interested in the set of updates that are actually recommended for this cluster should use availableUpdates. This list may be empty if no updates are recommended, if the update service is unavailable, or if an empty or invalid channel has been specified. |
| `conditionalUpdates[]` | `object` | ConditionalUpdate represents an update which is recommended to some clusters on the version the current cluster is reconciling, but which may not be recommended for the current cluster. |
| `conditions` | `array` | conditions provides information about the cluster version. The condition "Available" is set to true if the desiredUpdate has been reached. The condition "Progressing" is set to true if an update is being applied. The condition "Degraded" is set to true if an update is currently blocked by a temporary or permanent error. Conditions are only valid for the current desiredUpdate when metadata.generation is equal to status.generation. |
| `conditions[]` | `object` | ClusterOperatorStatusCondition represents the state of the operator’s managed and monitored components. |
| `desired` | `object` | desired is the version that the cluster is reconciling towards. If the cluster is not yet fully initialized desired will be set with the information available, which may be an image or a tag. |
| `history` | `array` | history contains a list of the most recent versions applied to the cluster. This value may be empty during cluster startup, and then will be updated when a new update is being applied. The newest update is first in the list and it is ordered by recency. Updates in the history have state Completed if the rollout completed - if an update was failing or halfway applied the state will be Partial. Only a limited amount of update history is preserved. |
| `history[]` | `object` | UpdateHistory is a single attempted update to the cluster. |
| `observedGeneration` | `integer` | observedGeneration reports which version of the spec is being synced. If this value is not equal to metadata.generation, then the desired and conditions fields may represent a previous version. |
| `versionHash` | `string` | versionHash is a fingerprint of the content that the cluster will be updated with. It is used by the operator to avoid unnecessary work and is for internal use only. |

Show more

#### [7.1.7. .status.capabilities](#status-capabilities) Copy linkLink copied to clipboard!

Description
:   capabilities describes the state of optional, core cluster components.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `enabledCapabilities` | `array (string)` | enabledCapabilities lists all the capabilities that are currently managed. |
| `knownCapabilities` | `array (string)` | knownCapabilities lists all the capabilities known to the current cluster. |

Show more

#### [7.1.8. .status.conditionalUpdates](#status-conditionalupdates) Copy linkLink copied to clipboard!

Description
:   conditionalUpdates contains the list of updates that may be recommended for this cluster if it meets specific required conditions. Consumers interested in the set of updates that are actually recommended for this cluster should use availableUpdates. This list may be empty if no updates are recommended, if the update service is unavailable, or if an empty or invalid channel has been specified.

Type
:   `array`

#### [7.1.9. .status.conditionalUpdates[]](#status-conditionalupdates-2) Copy linkLink copied to clipboard!

Description
:   ConditionalUpdate represents an update which is recommended to some clusters on the version the current cluster is reconciling, but which may not be recommended for the current cluster.

Type
:   `object`

Required
:   * `release`
    * `risks`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions represents the observations of the conditional update’s current status. Known types are: \* Recommended, for whether the update is recommended for the current cluster. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `release` | `object` | release is the target of the update. |
| `risks` | `array` | risks represents the range of issues associated with updating to the target release. The cluster-version operator will evaluate all entries, and only recommend the update if there is at least one entry and all entries recommend the update. |
| `risks[]` | `object` | ConditionalUpdateRisk represents a reason and cluster-state for not recommending a conditional update. |

Show more

#### [7.1.10. .status.conditionalUpdates[].conditions](#status-conditionalupdates-conditions) Copy linkLink copied to clipboard!

Description
:   conditions represents the observations of the conditional update’s current status. Known types are: \* Recommended, for whether the update is recommended for the current cluster.

Type
:   `array`

#### [7.1.11. .status.conditionalUpdates[].conditions[]](#status-conditionalupdates-conditions-2) Copy linkLink copied to clipboard!

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

#### [7.1.12. .status.conditionalUpdates[].release](#status-conditionalupdates-release) Copy linkLink copied to clipboard!

Description
:   release is the target of the update.

Type
:   `object`

Required
:   * `image`
    * `version`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `architecture` | `string` | architecture is an optional field that indicates the value of the cluster architecture. In this context cluster architecture means either a single architecture or a multi architecture. Valid values are 'Multi' and empty. |
| `channels` | `array (string)` | channels is the set of Cincinnati channels to which the release currently belongs. |
| `image` | `string` | image is a container image location that contains the update. When this field is part of spec, image is optional if version is specified and the availableUpdates field contains a matching version. |
| `url` | `string` | url contains information about this release. This URL is set by the 'url' metadata property on a release or the metadata returned by the update API and should be displayed as a link in user interfaces. The URL field may not be set for test or nightly releases. |
| `version` | `string` | version is a semantic version identifying the update version. When this field is part of spec, version is optional if image is specified. |

Show more

#### [7.1.13. .status.conditionalUpdates[].risks](#status-conditionalupdates-risks) Copy linkLink copied to clipboard!

Description
:   risks represents the range of issues associated with updating to the target release. The cluster-version operator will evaluate all entries, and only recommend the update if there is at least one entry and all entries recommend the update.

Type
:   `array`

#### [7.1.14. .status.conditionalUpdates[].risks[]](#status-conditionalupdates-risks-2) Copy linkLink copied to clipboard!

Description
:   ConditionalUpdateRisk represents a reason and cluster-state for not recommending a conditional update.

Type
:   `object`

Required
:   * `matchingRules`
    * `message`
    * `name`
    * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchingRules` | `array` | matchingRules is a slice of conditions for deciding which clusters match the risk and which do not. The slice is ordered by decreasing precedence. The cluster-version operator will walk the slice in order, and stop after the first it can successfully evaluate. If no condition can be successfully evaluated, the update will not be recommended. |
| `matchingRules[]` | `object` | ClusterCondition is a union of typed cluster conditions. The 'type' property determines which of the type-specific properties are relevant. When evaluated on a cluster, the condition may match, not match, or fail to evaluate. |
| `message` | `string` | message provides additional information about the risk of updating, in the event that matchingRules match the cluster state. This is only to be consumed by humans. It may contain Line Feed characters (U+000A), which should be rendered as new lines. |
| `name` | `string` | name is the CamelCase reason for not recommending a conditional update, in the event that matchingRules match the cluster state. |
| `url` | `string` | url contains information about this risk. |

Show more

#### [7.1.15. .status.conditionalUpdates[].risks[].matchingRules](#status-conditionalupdates-risks-matchingrules) Copy linkLink copied to clipboard!

Description
:   matchingRules is a slice of conditions for deciding which clusters match the risk and which do not. The slice is ordered by decreasing precedence. The cluster-version operator will walk the slice in order, and stop after the first it can successfully evaluate. If no condition can be successfully evaluated, the update will not be recommended.

Type
:   `array`

#### [7.1.16. .status.conditionalUpdates[].risks[].matchingRules[]](#status-conditionalupdates-risks-matchingrules-2) Copy linkLink copied to clipboard!

Description
:   ClusterCondition is a union of typed cluster conditions. The 'type' property determines which of the type-specific properties are relevant. When evaluated on a cluster, the condition may match, not match, or fail to evaluate.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `promql` | `object` | promql represents a cluster condition based on PromQL. |
| `type` | `string` | type represents the cluster-condition type. This defines the members and semantics of any additional properties. |

Show more

#### [7.1.17. .status.conditionalUpdates[].risks[].matchingRules[].promql](#status-conditionalupdates-risks-matchingrules-promql) Copy linkLink copied to clipboard!

Description
:   promql represents a cluster condition based on PromQL.

Type
:   `object`

Required
:   * `promql`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `promql` | `string` | promql is a PromQL query classifying clusters. This query query should return a 1 in the match case and a 0 in the does-not-match case. Queries which return no time series, or which return values besides 0 or 1, are evaluation failures. |

Show more

#### [7.1.18. .status.conditions](#status-conditions-5) Copy linkLink copied to clipboard!

Description
:   conditions provides information about the cluster version. The condition "Available" is set to true if the desiredUpdate has been reached. The condition "Progressing" is set to true if an update is being applied. The condition "Degraded" is set to true if an update is currently blocked by a temporary or permanent error. Conditions are only valid for the current desiredUpdate when metadata.generation is equal to status.generation.

Type
:   `array`

#### [7.1.19. .status.conditions[]](#status-conditions-6) Copy linkLink copied to clipboard!

Description
:   ClusterOperatorStatusCondition represents the state of the operator’s managed and monitored components.

Type
:   `object`

Required
:   * `lastTransitionTime`
    * `status`
    * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | `string` | lastTransitionTime is the time of the last update to the current status property. |
| `message` | `string` | message provides additional information about the current condition. This is only to be consumed by humans. It may contain Line Feed characters (U+000A), which should be rendered as new lines. |
| `reason` | `string` | reason is the CamelCase reason for the condition’s current status. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type specifies the aspect reported by this condition. |

Show more

#### [7.1.20. .status.desired](#status-desired) Copy linkLink copied to clipboard!

Description
:   desired is the version that the cluster is reconciling towards. If the cluster is not yet fully initialized desired will be set with the information available, which may be an image or a tag.

Type
:   `object`

Required
:   * `image`
    * `version`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `architecture` | `string` | architecture is an optional field that indicates the value of the cluster architecture. In this context cluster architecture means either a single architecture or a multi architecture. Valid values are 'Multi' and empty. |
| `channels` | `array (string)` | channels is the set of Cincinnati channels to which the release currently belongs. |
| `image` | `string` | image is a container image location that contains the update. When this field is part of spec, image is optional if version is specified and the availableUpdates field contains a matching version. |
| `url` | `string` | url contains information about this release. This URL is set by the 'url' metadata property on a release or the metadata returned by the update API and should be displayed as a link in user interfaces. The URL field may not be set for test or nightly releases. |
| `version` | `string` | version is a semantic version identifying the update version. When this field is part of spec, version is optional if image is specified. |

Show more

#### [7.1.21. .status.history](#status-history) Copy linkLink copied to clipboard!

Description
:   history contains a list of the most recent versions applied to the cluster. This value may be empty during cluster startup, and then will be updated when a new update is being applied. The newest update is first in the list and it is ordered by recency. Updates in the history have state Completed if the rollout completed - if an update was failing or halfway applied the state will be Partial. Only a limited amount of update history is preserved.

Type
:   `array`

#### [7.1.22. .status.history[]](#status-history-2) Copy linkLink copied to clipboard!

Description
:   UpdateHistory is a single attempted update to the cluster.

Type
:   `object`

Required
:   * `image`
    * `startedTime`
    * `state`
    * `verified`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `acceptedRisks` | `string` | acceptedRisks records risks which were accepted to initiate the update. For example, it may mention an Upgradeable=False or missing signature that was overridden via desiredUpdate.force, or an update that was initiated despite not being in the availableUpdates set of recommended update targets. |
| `completionTime` | `` | completionTime, if set, is when the update was fully applied. The update that is currently being applied will have a null completion time. Completion time will always be set for entries that are not the current update (usually to the started time of the next update). |
| `image` | `string` | image is a container image location that contains the update. This value is always populated. |
| `startedTime` | `string` | startedTime is the time at which the update was started. |
| `state` | `string` | state reflects whether the update was fully applied. The Partial state indicates the update is not fully applied, while the Completed state indicates the update was successfully rolled out at least once (all parts of the update successfully applied). |
| `verified` | `boolean` | verified indicates whether the provided update was properly verified before it was installed. If this is false the cluster may not be trusted. Verified does not cover upgradeable checks that depend on the cluster state at the time when the update target was accepted. |
| `version` | `string` | version is a semantic version identifying the update version. If the requested image does not define a version, or if a failure occurs retrieving the image, this value may be empty. |

Show more

### [7.2. API endpoints](#api-endpoints-6) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/clusterversions`

  + `DELETE`: delete collection of ClusterVersion
  + `GET`: list objects of kind ClusterVersion
  + `POST`: create a ClusterVersion
* `/apis/config.openshift.io/v1/clusterversions/{name}`

  + `DELETE`: delete a ClusterVersion
  + `GET`: read the specified ClusterVersion
  + `PATCH`: partially update the specified ClusterVersion
  + `PUT`: replace the specified ClusterVersion
* `/apis/config.openshift.io/v1/clusterversions/{name}/status`

  + `GET`: read status of the specified ClusterVersion
  + `PATCH`: partially update status of the specified ClusterVersion
  + `PUT`: replace status of the specified ClusterVersion

#### [7.2.1. /apis/config.openshift.io/v1/clusterversions](#apisconfig-openshift-iov1clusterversions) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ClusterVersion

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
:   list objects of kind ClusterVersion

Expand

Table 7.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ClusterVersionList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ClusterVersion

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
| `body` | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 7.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.2. /apis/config.openshift.io/v1/clusterversions/{name}](#apisconfig-openshift-iov1clusterversionsname) Copy linkLink copied to clipboard!

Expand

Table 7.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterVersion |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ClusterVersion

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
:   read the specified ClusterVersion

Expand

Table 7.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ClusterVersion

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
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ClusterVersion

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
| `body` | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 7.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [7.2.3. /apis/config.openshift.io/v1/clusterversions/{name}/status](#apisconfig-openshift-iov1clusterversionsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 7.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ClusterVersion |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ClusterVersion

Expand

Table 7.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ClusterVersion

Expand

Table 7.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ClusterVersion

Expand

Table 7.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 7.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 7.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 201 - Created | [`ClusterVersion`](#clusterversion-config-openshift-io-v1 "Chapter 7. ClusterVersion [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 8. Console [config.openshift.io/v1]](#console-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Console holds cluster-wide configuration for the web console, including the logout URL, and reports the public URL of the console. The canonical name is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [8.1. Specification](#specification-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [8.1.1. .spec](#spec-7) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `authentication` | `object` | ConsoleAuthentication defines a list of optional configuration for console authentication. |

Show more

#### [8.1.2. .spec.authentication](#spec-authentication) Copy linkLink copied to clipboard!

Description
:   ConsoleAuthentication defines a list of optional configuration for console authentication.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `logoutRedirect` | `string` | An optional, absolute URL to redirect web browsers to after logging out of the console. If not specified, it will redirect to the default login page. This is required when using an identity provider that supports single sign-on (SSO) such as: - OpenID (Keycloak, Azure) - RequestHeader (GSSAPI, SSPI, SAML) - OAuth (GitHub, GitLab, Google) Logging out of the console will destroy the user’s token. The logoutRedirect provides the user the option to perform single logout (SLO) through the identity provider to destroy their single sign-on session. |

Show more

#### [8.1.3. .status](#status-6) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `consoleURL` | `string` | The URL for the console. This will be derived from the host for the route that is created for the console. |

Show more

### [8.2. API endpoints](#api-endpoints-7) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/consoles`

  + `DELETE`: delete collection of Console
  + `GET`: list objects of kind Console
  + `POST`: create a Console
* `/apis/config.openshift.io/v1/consoles/{name}`

  + `DELETE`: delete a Console
  + `GET`: read the specified Console
  + `PATCH`: partially update the specified Console
  + `PUT`: replace the specified Console
* `/apis/config.openshift.io/v1/consoles/{name}/status`

  + `GET`: read status of the specified Console
  + `PATCH`: partially update status of the specified Console
  + `PUT`: replace status of the specified Console

#### [8.2.1. /apis/config.openshift.io/v1/consoles](#apisconfig-openshift-iov1consoles) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Console

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
:   list objects of kind Console

Expand

Table 8.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ConsoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ConsoleList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Console

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
| `body` | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 8.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 201 - Created | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.2. /apis/config.openshift.io/v1/consoles/{name}](#apisconfig-openshift-iov1consolesname) Copy linkLink copied to clipboard!

Expand

Table 8.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Console |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Console

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
:   read the specified Console

Expand

Table 8.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Console

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
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Console

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
| `body` | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 8.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 201 - Created | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [8.2.3. /apis/config.openshift.io/v1/consoles/{name}/status](#apisconfig-openshift-iov1consolesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 8.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Console |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Console

Expand

Table 8.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Console

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
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Console

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
| `body` | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 8.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 201 - Created | [`Console`](#console-config-openshift-io-v1 "Chapter 8. Console [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 9. DNS [config.openshift.io/v1]](#dns-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   DNS holds cluster-wide information about DNS. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [9.1.1. .spec](#spec-8) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `baseDomain` | `string` | baseDomain is the base domain of the cluster. All managed DNS records will be sub-domains of this base.  For example, given the base domain `openshift.example.com`, an API server DNS record may be created for `cluster-api.openshift.example.com`.  Once set, this field cannot be changed. |
| `platform` | `object` | platform holds configuration specific to the underlying infrastructure provider for DNS. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. |
| `privateZone` | `object` | privateZone is the location where all the DNS records that are only available internally to the cluster exist.  If this field is nil, no private records should be created.  Once set, this field cannot be changed. |
| `publicZone` | `object` | publicZone is the location where all the DNS records that are publicly accessible to the internet exist.  If this field is nil, no public records should be created.  Once set, this field cannot be changed. |

Show more

#### [9.1.2. .spec.platform](#spec-platform) Copy linkLink copied to clipboard!

Description
:   platform holds configuration specific to the underlying infrastructure provider for DNS. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `aws` | `object` | aws contains DNS configuration specific to the Amazon Web Services cloud provider. |
| `type` | `string` | type is the underlying infrastructure provider for the cluster. Allowed values: "", "AWS".  Individual components may not support all platforms, and must handle unrecognized platforms with best-effort defaults. |

Show more

#### [9.1.3. .spec.platform.aws](#spec-platform-aws) Copy linkLink copied to clipboard!

Description
:   aws contains DNS configuration specific to the Amazon Web Services cloud provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `privateZoneIAMRole` | `string` | privateZoneIAMRole contains the ARN of an IAM role that should be assumed when performing operations on the cluster’s private hosted zone specified in the cluster DNS config. When left empty, no role should be assumed.  The ARN must follow the format: arn:<partition>:iam::<account-id>:role/<role-name>, where: <partition> is the AWS partition (aws, aws-cn, aws-us-gov, or aws-eusc), <account-id> is a 12-digit numeric identifier for the AWS account, <role-name> is the IAM role name. |

Show more

#### [9.1.4. .spec.privateZone](#spec-privatezone) Copy linkLink copied to clipboard!

Description
:   privateZone is the location where all the DNS records that are only available internally to the cluster exist.

    If this field is nil, no private records should be created.

    Once set, this field cannot be changed.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | id is the identifier that can be used to find the DNS hosted zone.  on AWS zone can be fetched using `ID` as id in [1] on Azure zone can be fetched using `ID` as a pre-determined name in [2], on GCP zone can be fetched using `ID` as a pre-determined name in [3].  [1]: <https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options> [2]: <https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show> [3]: <https://cloud.google.com/dns/docs/reference/v1/managedZones/get> |
| `tags` | `object (string)` | tags can be used to query the DNS hosted zone.  on AWS, resourcegroupstaggingapi [1] can be used to fetch a zone using `Tags` as tag-filters,  [1]: <https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options> |

Show more

#### [9.1.5. .spec.publicZone](#spec-publiczone) Copy linkLink copied to clipboard!

Description
:   publicZone is the location where all the DNS records that are publicly accessible to the internet exist.

    If this field is nil, no public records should be created.

    Once set, this field cannot be changed.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | id is the identifier that can be used to find the DNS hosted zone.  on AWS zone can be fetched using `ID` as id in [1] on Azure zone can be fetched using `ID` as a pre-determined name in [2], on GCP zone can be fetched using `ID` as a pre-determined name in [3].  [1]: <https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options> [2]: <https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show> [3]: <https://cloud.google.com/dns/docs/reference/v1/managedZones/get> |
| `tags` | `object (string)` | tags can be used to query the DNS hosted zone.  on AWS, resourcegroupstaggingapi [1] can be used to fetch a zone using `Tags` as tag-filters,  [1]: <https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options> |

Show more

#### [9.1.6. .status](#status-7) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

### [9.2. API endpoints](#api-endpoints-8) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/dnses`

  + `DELETE`: delete collection of DNS
  + `GET`: list objects of kind DNS
  + `POST`: create a DNS
* `/apis/config.openshift.io/v1/dnses/{name}`

  + `DELETE`: delete a DNS
  + `GET`: read the specified DNS
  + `PATCH`: partially update the specified DNS
  + `PUT`: replace the specified DNS
* `/apis/config.openshift.io/v1/dnses/{name}/status`

  + `GET`: read status of the specified DNS
  + `PATCH`: partially update status of the specified DNS
  + `PUT`: replace status of the specified DNS

#### [9.2.1. /apis/config.openshift.io/v1/dnses](#apisconfig-openshift-iov1dnses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of DNS

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
:   list objects of kind DNS

Expand

Table 9.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DNSList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-DNSList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a DNS

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
| `body` | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 9.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 201 - Created | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 202 - Accepted | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.2. /apis/config.openshift.io/v1/dnses/{name}](#apisconfig-openshift-iov1dnsesname) Copy linkLink copied to clipboard!

Expand

Table 9.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the DNS |

Show more

HTTP method
:   `DELETE`

Description
:   delete a DNS

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
:   read the specified DNS

Expand

Table 9.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified DNS

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
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified DNS

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
| `body` | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 9.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 201 - Created | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [9.2.3. /apis/config.openshift.io/v1/dnses/{name}/status](#apisconfig-openshift-iov1dnsesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 9.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the DNS |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified DNS

Expand

Table 9.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified DNS

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
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified DNS

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
| `body` | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 9.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 201 - Created | [`DNS`](#dns-config-openshift-io-v1 "Chapter 9. DNS [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 10. FeatureGate [config.openshift.io/v1]](#featuregate-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Feature holds cluster-wide information about feature gates. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [10.1.1. .spec](#spec-9) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `customNoUpgrade` | `` | customNoUpgrade allows the enabling or disabling of any feature. Turning this feature set on IS NOT SUPPORTED, CANNOT BE UNDONE, and PREVENTS UPGRADES. Because of its nature, this setting cannot be validated. If you have any typos or accidentally apply invalid combinations your cluster may fail in an unrecoverable way. featureSet must equal "CustomNoUpgrade" must be set to use this field. |
| `featureSet` | `string` | featureSet changes the list of features in the cluster. The default is empty. Be very careful adjusting this setting. Turning on or off features may cause irreversible changes in your cluster which cannot be undone. |

Show more

#### [10.1.2. .status](#status-8) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions represent the observations of the current state. Known .status.conditions.type are: "DeterminationDegraded" |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `featureGates` | `array` | featureGates contains a list of enabled and disabled featureGates that are keyed by payloadVersion. Operators other than the CVO and cluster-config-operator, must read the .status.featureGates, locate the version they are managing, find the enabled/disabled featuregates and make the operand and operator match. The enabled/disabled values for a particular version may change during the life of the cluster as various .spec.featureSet values are selected. Operators may choose to restart their processes to pick up these changes, but remembering past enable/disable lists is beyond the scope of this API and is the responsibility of individual operators. Only featureGates with .version in the ClusterVersion.status will be present in this list. |
| `featureGates[]` | `object` |  |

Show more

#### [10.1.3. .status.conditions](#status-conditions-7) Copy linkLink copied to clipboard!

Description
:   conditions represent the observations of the current state. Known .status.conditions.type are: "DeterminationDegraded"

Type
:   `array`

#### [10.1.4. .status.conditions[]](#status-conditions-8) Copy linkLink copied to clipboard!

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

#### [10.1.5. .status.featureGates](#status-featuregates) Copy linkLink copied to clipboard!

Description
:   featureGates contains a list of enabled and disabled featureGates that are keyed by payloadVersion. Operators other than the CVO and cluster-config-operator, must read the .status.featureGates, locate the version they are managing, find the enabled/disabled featuregates and make the operand and operator match. The enabled/disabled values for a particular version may change during the life of the cluster as various .spec.featureSet values are selected. Operators may choose to restart their processes to pick up these changes, but remembering past enable/disable lists is beyond the scope of this API and is the responsibility of individual operators. Only featureGates with .version in the ClusterVersion.status will be present in this list.

Type
:   `array`

#### [10.1.6. .status.featureGates[]](#status-featuregates-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `version`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `disabled` | `array` | disabled is a list of all feature gates that are disabled in the cluster for the named version. |
| `disabled[]` | `object` |  |
| `enabled` | `array` | enabled is a list of all feature gates that are enabled in the cluster for the named version. |
| `enabled[]` | `object` |  |
| `version` | `string` | version matches the version provided by the ClusterVersion and in the ClusterOperator.Status.Versions field. |

Show more

#### [10.1.7. .status.featureGates[].disabled](#status-featuregates-disabled) Copy linkLink copied to clipboard!

Description
:   disabled is a list of all feature gates that are disabled in the cluster for the named version.

Type
:   `array`

#### [10.1.8. .status.featureGates[].disabled[]](#status-featuregates-disabled-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the FeatureGate. |

Show more

#### [10.1.9. .status.featureGates[].enabled](#status-featuregates-enabled) Copy linkLink copied to clipboard!

Description
:   enabled is a list of all feature gates that are enabled in the cluster for the named version.

Type
:   `array`

#### [10.1.10. .status.featureGates[].enabled[]](#status-featuregates-enabled-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the FeatureGate. |

Show more

### [10.2. API endpoints](#api-endpoints-9) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/featuregates`

  + `DELETE`: delete collection of FeatureGate
  + `GET`: list objects of kind FeatureGate
  + `POST`: create a FeatureGate
* `/apis/config.openshift.io/v1/featuregates/{name}`

  + `DELETE`: delete a FeatureGate
  + `GET`: read the specified FeatureGate
  + `PATCH`: partially update the specified FeatureGate
  + `PUT`: replace the specified FeatureGate
* `/apis/config.openshift.io/v1/featuregates/{name}/status`

  + `GET`: read status of the specified FeatureGate
  + `PATCH`: partially update status of the specified FeatureGate
  + `PUT`: replace status of the specified FeatureGate

#### [10.2.1. /apis/config.openshift.io/v1/featuregates](#apisconfig-openshift-iov1featuregates) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of FeatureGate

Expand

Table 10.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind FeatureGate

Expand

Table 10.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-FeatureGateList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a FeatureGate

Expand

Table 10.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 10.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 201 - Created | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 202 - Accepted | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.2. /apis/config.openshift.io/v1/featuregates/{name}](#apisconfig-openshift-iov1featuregatesname) Copy linkLink copied to clipboard!

Expand

Table 10.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the FeatureGate |

Show more

HTTP method
:   `DELETE`

Description
:   delete a FeatureGate

Expand

Table 10.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 10.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified FeatureGate

Expand

Table 10.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified FeatureGate

Expand

Table 10.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified FeatureGate

Expand

Table 10.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 10.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 201 - Created | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [10.2.3. /apis/config.openshift.io/v1/featuregates/{name}/status](#apisconfig-openshift-iov1featuregatesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 10.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the FeatureGate |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified FeatureGate

Expand

Table 10.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified FeatureGate

Expand

Table 10.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified FeatureGate

Expand

Table 10.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 10.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 10.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 201 - Created | [`FeatureGate`](#featuregate-config-openshift-io-v1 "Chapter 10. FeatureGate [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]](#helmchartrepository-helm-openshift-io-v1beta1) Copy linkLink copied to clipboard!

Description
:   HelmChartRepository holds cluster-wide configuration for proxied Helm chart repository

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | Observed status of the repository within the cluster.. |

Show more

#### [11.1.1. .spec](#spec-10) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `connectionConfig` | `object` | Required configuration for connecting to the chart repo |
| `description` | `string` | Optional human readable repository description, it can be used by UI for displaying purposes |
| `disabled` | `boolean` | If set to true, disable the repo usage in the cluster/namespace |
| `name` | `string` | Optional associated human readable repository name, it can be used by UI for displaying purposes |

Show more

#### [11.1.2. .spec.connectionConfig](#spec-connectionconfig) Copy linkLink copied to clipboard!

Description
:   Required configuration for connecting to the chart repo

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this config map is openshift-config. |
| `tlsClientConfig` | `object` | tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret is openshift-config. |
| `url` | `string` | Chart repository URL |

Show more

#### [11.1.3. .spec.connectionConfig.ca](#spec-connectionconfig-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [11.1.4. .spec.connectionConfig.tlsClientConfig](#spec-connectionconfig-tlsclientconfig) Copy linkLink copied to clipboard!

Description
:   tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [11.1.5. .status](#status-9) Copy linkLink copied to clipboard!

Description
:   Observed status of the repository within the cluster..

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions is a list of conditions and their statuses |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |

Show more

#### [11.1.6. .status.conditions](#status-conditions-9) Copy linkLink copied to clipboard!

Description
:   conditions is a list of conditions and their statuses

Type
:   `array`

#### [11.1.7. .status.conditions[]](#status-conditions-10) Copy linkLink copied to clipboard!

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

### [11.2. API endpoints](#api-endpoints-10) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/helm.openshift.io/v1beta1/helmchartrepositories`

  + `DELETE`: delete collection of HelmChartRepository
  + `GET`: list objects of kind HelmChartRepository
  + `POST`: create a HelmChartRepository
* `/apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}`

  + `DELETE`: delete a HelmChartRepository
  + `GET`: read the specified HelmChartRepository
  + `PATCH`: partially update the specified HelmChartRepository
  + `PUT`: replace the specified HelmChartRepository
* `/apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}/status`

  + `GET`: read status of the specified HelmChartRepository
  + `PATCH`: partially update status of the specified HelmChartRepository
  + `PUT`: replace status of the specified HelmChartRepository

#### [11.2.1. /apis/helm.openshift.io/v1beta1/helmchartrepositories](#apishelm-openshift-iov1beta1helmchartrepositories) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of HelmChartRepository

Expand

Table 11.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind HelmChartRepository

Expand

Table 11.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepositoryList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-helm-v1beta1-HelmChartRepositoryList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a HelmChartRepository

Expand

Table 11.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |  |

Show more

Expand

Table 11.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 201 - Created | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 202 - Accepted | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.2. /apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}](#apishelm-openshift-iov1beta1helmchartrepositoriesname) Copy linkLink copied to clipboard!

Expand

Table 11.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HelmChartRepository |

Show more

HTTP method
:   `DELETE`

Description
:   delete a HelmChartRepository

Expand

Table 11.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 11.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified HelmChartRepository

Expand

Table 11.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified HelmChartRepository

Expand

Table 11.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified HelmChartRepository

Expand

Table 11.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |  |

Show more

Expand

Table 11.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 201 - Created | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [11.2.3. /apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}/status](#apishelm-openshift-iov1beta1helmchartrepositoriesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 11.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the HelmChartRepository |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified HelmChartRepository

Expand

Table 11.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified HelmChartRepository

Expand

Table 11.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified HelmChartRepository

Expand

Table 11.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 11.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |  |

Show more

Expand

Table 11.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 201 - Created | [`HelmChartRepository`](#helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 12. Image [config.openshift.io/v1]](#image-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Image governs policies related to imagestream imports and runtime configuration for external registries. It allows cluster admins to configure which registries OpenShift is allowed to import images from, extra CA trust bundles for external registries, and policies to block or allow registry hostnames. When exposing OpenShift’s image registry to the public, this also lets cluster admins specify the external hostname.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [12.1.1. .spec](#spec-11) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `additionalTrustedCA` | `object` | additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted during imagestream import, pod image pull, build image pull, and imageregistry pullthrough. The namespace for this config map is openshift-config. |
| `allowedRegistriesForImport` | `array` | allowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions. |
| `allowedRegistriesForImport[]` | `object` | RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '\*' or '??'. |
| `externalRegistryHostnames` | `array (string)` | externalRegistryHostnames provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in 'publicDockerImageRepository' field in ImageStreams. The value must be in "hostname[:port]" format. |
| `imageStreamImportMode` | `string` | imageStreamImportMode controls the import mode behaviour of imagestreams. It can be set to `Legacy` or `PreserveOriginal` or the empty string. If this value is specified, this setting is applied to all newly created imagestreams which do not have the value set. `Legacy` indicates that the legacy behaviour should be used. For manifest lists, the legacy behaviour will discard the manifest list and import a single sub-manifest. In this case, the platform is chosen in the following order of priority: 1. tag annotations; 2. control plane arch/os; 3. linux/amd64; 4. the first manifest in the list. `PreserveOriginal` indicates that the original manifest will be preserved. For manifest lists, the manifest list and all its sub-manifests will be imported. When empty, the behaviour will be decided based on the payload type advertised by the ClusterVersion status, i.e single arch payload implies the import mode is Legacy and multi payload implies PreserveOriginal. |
| `registrySources` | `object` | registrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds+pods. (e.g. whether or not to allow insecure access). It does not contain configuration for the internal cluster registry. |

Show more

#### [12.1.2. .spec.additionalTrustedCA](#spec-additionaltrustedca-2) Copy linkLink copied to clipboard!

Description
:   additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted during imagestream import, pod image pull, build image pull, and imageregistry pullthrough. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [12.1.3. .spec.allowedRegistriesForImport](#spec-allowedregistriesforimport) Copy linkLink copied to clipboard!

Description
:   allowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions.

Type
:   `array`

#### [12.1.4. .spec.allowedRegistriesForImport[]](#spec-allowedregistriesforimport-2) Copy linkLink copied to clipboard!

Description
:   RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '\*' or '??'.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `domainName` | `string` | domainName specifies a domain name for the registry In case the registry use non-standard (80 or 443) port, the port should be included in the domain name as well. |
| `insecure` | `boolean` | insecure indicates whether the registry is secure (https) or insecure (http) By default (if not specified) the registry is assumed as secure. |

Show more

#### [12.1.5. .spec.registrySources](#spec-registrysources) Copy linkLink copied to clipboard!

Description
:   registrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds+pods. (e.g. whether or not to allow insecure access). It does not contain configuration for the internal cluster registry.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowedRegistries` | `array (string)` | allowedRegistries are the only registries permitted for image pull and push actions. All other registries are denied.  Only one of BlockedRegistries or AllowedRegistries may be set. |
| `blockedRegistries` | `array (string)` | blockedRegistries cannot be used for image pull and push actions. All other registries are permitted.  Only one of BlockedRegistries or AllowedRegistries may be set. |
| `containerRuntimeSearchRegistries` | `array (string)` | containerRuntimeSearchRegistries are registries that will be searched when pulling images that do not have fully qualified domains in their pull specs. Registries will be searched in the order provided in the list. Note: this search list only works with the container runtime, i.e CRI-O. Will NOT work with builds or imagestream imports. |
| `insecureRegistries` | `array (string)` | insecureRegistries are registries which do not have a valid TLS certificates or only support HTTP connections. |

Show more

#### [12.1.6. .status](#status-10) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `externalRegistryHostnames` | `array (string)` | externalRegistryHostnames provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in 'publicDockerImageRepository' field in ImageStreams. The value must be in "hostname[:port]" format. |
| `imageStreamImportMode` | `string` | imageStreamImportMode controls the import mode behaviour of imagestreams. It can be `Legacy` or `PreserveOriginal`. `Legacy` indicates that the legacy behaviour should be used. For manifest lists, the legacy behaviour will discard the manifest list and import a single sub-manifest. In this case, the platform is chosen in the following order of priority: 1. tag annotations; 2. control plane arch/os; 3. linux/amd64; 4. the first manifest in the list. `PreserveOriginal` indicates that the original manifest will be preserved. For manifest lists, the manifest list and all its sub-manifests will be imported. This value will be reconciled based on either the spec value or if no spec value is specified, the image registry operator would look at the ClusterVersion status to determine the payload type and set the import mode accordingly, i.e single arch payload implies the import mode is Legacy and multi payload implies PreserveOriginal. |
| `internalRegistryHostname` | `string` | internalRegistryHostname sets the hostname for the default internal image registry. The value must be in "hostname[:port]" format. This value is set by the image registry operator which controls the internal registry hostname. |

Show more

### [12.2. API endpoints](#api-endpoints-11) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/images`

  + `DELETE`: delete collection of Image
  + `GET`: list objects of kind Image
  + `POST`: create an Image
* `/apis/config.openshift.io/v1/images/{name}`

  + `DELETE`: delete an Image
  + `GET`: read the specified Image
  + `PATCH`: partially update the specified Image
  + `PUT`: replace the specified Image
* `/apis/config.openshift.io/v1/images/{name}/status`

  + `GET`: read status of the specified Image
  + `PATCH`: partially update status of the specified Image
  + `PUT`: replace status of the specified Image

#### [12.2.1. /apis/config.openshift.io/v1/images](#apisconfig-openshift-iov1images) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Image

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
:   list objects of kind Image

Expand

Table 12.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImageList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an Image

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
| `body` | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 12.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 201 - Created | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.2. /apis/config.openshift.io/v1/images/{name}](#apisconfig-openshift-iov1imagesname) Copy linkLink copied to clipboard!

Expand

Table 12.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Image |

Show more

HTTP method
:   `DELETE`

Description
:   delete an Image

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
:   read the specified Image

Expand

Table 12.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Image

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
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Image

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
| `body` | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 12.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 201 - Created | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [12.2.3. /apis/config.openshift.io/v1/images/{name}/status](#apisconfig-openshift-iov1imagesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 12.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Image |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Image

Expand

Table 12.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Image

Expand

Table 12.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Image

Expand

Table 12.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 12.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 12.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 201 - Created | [`Image`](#image-config-openshift-io-v1 "Chapter 12. Image [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]](#imagedigestmirrorset-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ImageDigestMirrorSet holds cluster-wide information about how to handle registry mirror rules on using digest pull specification. When multiple policies are defined, the outcome of the behavior is defined on each field.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status contains the observed state of the resource. |

Show more

#### [13.1.1. .spec](#spec-12) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `imageDigestMirrors` | `array` | imageDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using tag specification, users should configure a list of mirrors using "ImageTagMirrorSet" CRD.  If the image pull specification matches the repository of "source" in multiple imagedigestmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.  If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.  When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a specific order of mirrors, should configure them into one list of mirrors using the expected order. |
| `imageDigestMirrors[]` | `object` | ImageDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config. |

Show more

#### [13.1.2. .spec.imageDigestMirrors](#spec-imagedigestmirrors) Copy linkLink copied to clipboard!

Description
:   imageDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using tag specification, users should configure a list of mirrors using "ImageTagMirrorSet" CRD.

    If the image pull specification matches the repository of "source" in multiple imagedigestmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.

    If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.

    When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a specific order of mirrors, should configure them into one list of mirrors using the expected order.

Type
:   `array`

#### [13.1.3. .spec.imageDigestMirrors[]](#spec-imagedigestmirrors-2) Copy linkLink copied to clipboard!

Description
:   ImageDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config.

Type
:   `object`

Required
:   * `source`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mirrorSourcePolicy` | `string` | mirrorSourcePolicy defines the fallback policy if fails to pull image from the mirrors. If unset, the image will continue to be pulled from the the repository in the pull spec. sourcePolicy is valid configuration only when one or more mirrors are in the mirror list. |
| `mirrors` | `array (string)` | mirrors is zero or more locations that may also contain the same images. No mirror will be configured if not specified. Images can be pulled from these mirrors only if they are referenced by their digests. The mirrored location is obtained by replacing the part of the input reference that matches source by the mirrors entry, e.g. for registry.redhat.io/product/repo reference, a (source, mirror) pair \*.redhat.io, mirror.local/redhat causes a mirror.local/redhat/product/repo repository to be used. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. If no mirror is specified or all image pulls from the mirror list fail, the image will continue to be pulled from the repository in the pull spec unless explicitly prohibited by "mirrorSourcePolicy" Other cluster configuration, including (but not limited to) other imageDigestMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. "mirrors" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table> |
| `source` | `string` | source matches the repository that users refer to, e.g. in image pull specifications. Setting source to a registry hostname e.g. docker.io. quay.io, or registry.redhat.io, will match the image pull specification of corressponding registry. "source" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo [\*.]host for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table> |

Show more

#### [13.1.4. .status](#status-11) Copy linkLink copied to clipboard!

Description
:   status contains the observed state of the resource.

Type
:   `object`

### [13.2. API endpoints](#api-endpoints-12) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/imagedigestmirrorsets`

  + `DELETE`: delete collection of ImageDigestMirrorSet
  + `GET`: list objects of kind ImageDigestMirrorSet
  + `POST`: create an ImageDigestMirrorSet
* `/apis/config.openshift.io/v1/imagedigestmirrorsets/{name}`

  + `DELETE`: delete an ImageDigestMirrorSet
  + `GET`: read the specified ImageDigestMirrorSet
  + `PATCH`: partially update the specified ImageDigestMirrorSet
  + `PUT`: replace the specified ImageDigestMirrorSet
* `/apis/config.openshift.io/v1/imagedigestmirrorsets/{name}/status`

  + `GET`: read status of the specified ImageDigestMirrorSet
  + `PATCH`: partially update status of the specified ImageDigestMirrorSet
  + `PUT`: replace status of the specified ImageDigestMirrorSet

#### [13.2.1. /apis/config.openshift.io/v1/imagedigestmirrorsets](#apisconfig-openshift-iov1imagedigestmirrorsets) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ImageDigestMirrorSet

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
:   list objects of kind ImageDigestMirrorSet

Expand

Table 13.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageDigestMirrorSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImageDigestMirrorSetList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an ImageDigestMirrorSet

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
| `body` | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 13.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.2. /apis/config.openshift.io/v1/imagedigestmirrorsets/{name}](#apisconfig-openshift-iov1imagedigestmirrorsetsname) Copy linkLink copied to clipboard!

Expand

Table 13.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImageDigestMirrorSet |

Show more

HTTP method
:   `DELETE`

Description
:   delete an ImageDigestMirrorSet

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
:   read the specified ImageDigestMirrorSet

Expand

Table 13.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ImageDigestMirrorSet

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
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ImageDigestMirrorSet

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
| `body` | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 13.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [13.2.3. /apis/config.openshift.io/v1/imagedigestmirrorsets/{name}/status](#apisconfig-openshift-iov1imagedigestmirrorsetsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 13.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImageDigestMirrorSet |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ImageDigestMirrorSet

Expand

Table 13.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ImageDigestMirrorSet

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
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ImageDigestMirrorSet

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
| `body` | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 13.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageDigestMirrorSet`](#imagedigestmirrorset-config-openshift-io-v1 "Chapter 13. ImageDigestMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 14. ImageContentPolicy [config.openshift.io/v1]](#imagecontentpolicy-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ImageContentPolicy holds cluster-wide information about how to handle registry mirror rules. When multiple policies are defined, the outcome of the behavior is defined on each field.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |

Show more

#### [14.1.1. .spec](#spec-13) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `repositoryDigestMirrors` | `array` | repositoryDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in RepositoryDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To pull image from mirrors by tags, should set the "allowMirrorByTags".  Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.  If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.  When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. |
| `repositoryDigestMirrors[]` | `object` | RepositoryDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config. |

Show more

#### [14.1.2. .spec.repositoryDigestMirrors](#spec-repositorydigestmirrors) Copy linkLink copied to clipboard!

Description
:   repositoryDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in RepositoryDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To pull image from mirrors by tags, should set the "allowMirrorByTags".

    Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.

    If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.

    When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified.

Type
:   `array`

#### [14.1.3. .spec.repositoryDigestMirrors[]](#spec-repositorydigestmirrors-2) Copy linkLink copied to clipboard!

Description
:   RepositoryDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config.

Type
:   `object`

Required
:   * `source`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowMirrorByTags` | `boolean` | allowMirrorByTags if true, the mirrors can be used to pull the images that are referenced by their tags. Default is false, the mirrors only work when pulling the images that are referenced by their digests. Pulling images by tag can potentially yield different images, depending on which endpoint we pull from. Forcing digest-pulls for mirrors avoids that issue. |
| `mirrors` | `array (string)` | mirrors is zero or more repositories that may also contain the same images. If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec. No mirror will be configured. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. Other cluster configuration, including (but not limited to) other repositoryDigestMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. |
| `source` | `string` | source is the repository that users refer to, e.g. in image pull specifications. |

Show more

### [14.2. API endpoints](#api-endpoints-13) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/imagecontentpolicies`

  + `DELETE`: delete collection of ImageContentPolicy
  + `GET`: list objects of kind ImageContentPolicy
  + `POST`: create an ImageContentPolicy
* `/apis/config.openshift.io/v1/imagecontentpolicies/{name}`

  + `DELETE`: delete an ImageContentPolicy
  + `GET`: read the specified ImageContentPolicy
  + `PATCH`: partially update the specified ImageContentPolicy
  + `PUT`: replace the specified ImageContentPolicy
* `/apis/config.openshift.io/v1/imagecontentpolicies/{name}/status`

  + `GET`: read status of the specified ImageContentPolicy
  + `PATCH`: partially update status of the specified ImageContentPolicy
  + `PUT`: replace status of the specified ImageContentPolicy

#### [14.2.1. /apis/config.openshift.io/v1/imagecontentpolicies](#apisconfig-openshift-iov1imagecontentpolicies) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ImageContentPolicy

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
:   list objects of kind ImageContentPolicy

Expand

Table 14.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImageContentPolicyList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an ImageContentPolicy

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
| `body` | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 14.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [14.2.2. /apis/config.openshift.io/v1/imagecontentpolicies/{name}](#apisconfig-openshift-iov1imagecontentpoliciesname) Copy linkLink copied to clipboard!

Expand

Table 14.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImageContentPolicy |

Show more

HTTP method
:   `DELETE`

Description
:   delete an ImageContentPolicy

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
:   read the specified ImageContentPolicy

Expand

Table 14.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ImageContentPolicy

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
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ImageContentPolicy

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
| `body` | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 14.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [14.2.3. /apis/config.openshift.io/v1/imagecontentpolicies/{name}/status](#apisconfig-openshift-iov1imagecontentpoliciesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 14.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImageContentPolicy |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ImageContentPolicy

Expand

Table 14.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ImageContentPolicy

Expand

Table 14.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 14.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ImageContentPolicy

Expand

Table 14.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 14.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 14.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageContentPolicy`](#imagecontentpolicy-config-openshift-io-v1 "Chapter 14. ImageContentPolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 15. ImagePolicy [config.openshift.io/v1]](#imagepolicy-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ImagePolicy holds namespace-wide configuration for image signature verification

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

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
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status contains the observed state of the resource. |

Show more

#### [15.1.1. .spec](#spec-14) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Required
:   * `policy`
    * `scopes`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `policy` | `object` | policy is a required field that contains configuration to allow scopes to be verified, and defines how images not matching the verification policy will be treated. |
| `scopes` | `array (string)` | scopes is a required field that defines the list of image identities assigned to a policy. Each item refers to a scope in a registry implementing the "Docker Registry HTTP API V2". Scopes matching individual images are named Docker references in the fully expanded form, either using a tag or digest. For example, docker.io/library/busybox:latest (not busybox:latest). More general scopes are prefixes of individual-image scopes, and specify a repository (by omitting the tag or digest), a repository namespace, or a registry host (by only specifying the host name and possibly a port number) or a wildcard expression starting with `*.`, for matching all subdomains (not including a port number). Wildcards are only supported for subdomain matching, and may not be used in the middle of the host, i.e. \\*.example.com is a valid case, but example\*.\*.com is not. This support no more than 256 scopes in one object. If multiple scopes match a given image, only the policy requirements for the most specific scope apply. The policy requirements for more general scopes are ignored. In addition to setting a policy appropriate for your own deployed applications, make sure that a policy on the OpenShift image repositories quay.io/openshift-release-dev/ocp-release, quay.io/openshift-release-dev/ocp-v4.0-art-dev (or on a more general scope) allows deployment of the OpenShift images required for cluster operation. If a scope is configured in both the ClusterImagePolicy and the ImagePolicy, or if the scope in ImagePolicy is nested under one of the scopes from the ClusterImagePolicy, only the policy from the ClusterImagePolicy will be applied. For additional details about the format, please refer to the document explaining the docker transport field, which can be found at: <https://github.com/containers/image/blob/main/docs/containers-policy.json.5.md#docker> |

Show more

#### [15.1.2. .spec.policy](#spec-policy-2) Copy linkLink copied to clipboard!

Description
:   policy is a required field that contains configuration to allow scopes to be verified, and defines how images not matching the verification policy will be treated.

Type
:   `object`

Required
:   * `rootOfTrust`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `rootOfTrust` | `object` | rootOfTrust is a required field that defines the root of trust for verifying image signatures during retrieval. This allows image consumers to specify policyType and corresponding configuration of the policy, matching how the policy was generated. |
| `signedIdentity` | `object` | signedIdentity is an optional field specifies what image identity the signature claims about the image. This is useful when the image identity in the signature differs from the original image spec, such as when mirror registry is configured for the image scope, the signature from the mirror registry contains the image identity of the mirror instead of the original scope. The required matchPolicy field specifies the approach used in the verification process to verify the identity in the signature and the actual image identity, the default matchPolicy is "MatchRepoDigestOrExact". |

Show more

#### [15.1.3. .spec.policy.rootOfTrust](#spec-policy-rootoftrust-2) Copy linkLink copied to clipboard!

Description
:   rootOfTrust is a required field that defines the root of trust for verifying image signatures during retrieval. This allows image consumers to specify policyType and corresponding configuration of the policy, matching how the policy was generated.

Type
:   `object`

Required
:   * `policyType`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fulcioCAWithRekor` | `object` | fulcioCAWithRekor defines the root of trust configuration based on the Fulcio certificate and the Rekor public key. fulcioCAWithRekor is required when policyType is FulcioCAWithRekor, and forbidden otherwise For more information about Fulcio and Rekor, please refer to the document at: <https://github.com/sigstore/fulcio> and <https://github.com/sigstore/rekor> |
| `pki` | `object` | pki defines the root of trust configuration based on Bring Your Own Public Key Infrastructure (BYOPKI) Root CA(s) and corresponding intermediate certificates. pki is required when policyType is PKI, and forbidden otherwise. |
| `policyType` | `string` | policyType is a required field specifies the type of the policy for verification. This field must correspond to how the policy was generated. Allowed values are "PublicKey", "FulcioCAWithRekor", and "PKI". When set to "PublicKey", the policy relies on a sigstore publicKey and may optionally use a Rekor verification. When set to "FulcioCAWithRekor", the policy is based on the Fulcio certification and incorporates a Rekor verification. When set to "PKI", the policy is based on the certificates from Bring Your Own Public Key Infrastructure (BYOPKI). |
| `publicKey` | `object` | publicKey defines the root of trust configuration based on a sigstore public key. Optionally include a Rekor public key for Rekor verification. publicKey is required when policyType is PublicKey, and forbidden otherwise. |

Show more

#### [15.1.4. .spec.policy.rootOfTrust.fulcioCAWithRekor](#spec-policy-rootoftrust-fulciocawithrekor-2) Copy linkLink copied to clipboard!

Description
:   fulcioCAWithRekor defines the root of trust configuration based on the Fulcio certificate and the Rekor public key. fulcioCAWithRekor is required when policyType is FulcioCAWithRekor, and forbidden otherwise For more information about Fulcio and Rekor, please refer to the document at: <https://github.com/sigstore/fulcio> and <https://github.com/sigstore/rekor>

Type
:   `object`

Required
:   * `fulcioCAData`
    * `fulcioSubject`
    * `rekorKeyData`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fulcioCAData` | `string` | fulcioCAData is a required field contains inline base64-encoded data for the PEM format fulcio CA. fulcioCAData must be at most 8192 characters. |
| `fulcioSubject` | `object` | fulcioSubject is a required field specifies OIDC issuer and the email of the Fulcio authentication configuration. |
| `rekorKeyData` | `string` | rekorKeyData is a required field contains inline base64-encoded data for the PEM format from the Rekor public key. rekorKeyData must be at most 8192 characters. |

Show more

#### [15.1.5. .spec.policy.rootOfTrust.fulcioCAWithRekor.fulcioSubject](#spec-policy-rootoftrust-fulciocawithrekor-fulciosubject-2) Copy linkLink copied to clipboard!

Description
:   fulcioSubject is a required field specifies OIDC issuer and the email of the Fulcio authentication configuration.

Type
:   `object`

Required
:   * `oidcIssuer`
    * `signedEmail`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `oidcIssuer` | `string` | oidcIssuer is a required filed contains the expected OIDC issuer. The oidcIssuer must be a valid URL and at most 2048 characters in length. It will be verified that the Fulcio-issued certificate contains a (Fulcio-defined) certificate extension pointing at this OIDC issuer URL. When Fulcio issues certificates, it includes a value based on an URL inside the client-provided ID token. Example: "https://expected.OIDC.issuer/" |
| `signedEmail` | `string` | signedEmail is a required field holds the email address that the Fulcio certificate is issued for. The signedEmail must be a valid email address and at most 320 characters in length. Example: "[expected-signing-user@example.com](mailto:expected-signing-user@example.com)" |

Show more

#### [15.1.6. .spec.policy.rootOfTrust.pki](#spec-policy-rootoftrust-pki-2) Copy linkLink copied to clipboard!

Description
:   pki defines the root of trust configuration based on Bring Your Own Public Key Infrastructure (BYOPKI) Root CA(s) and corresponding intermediate certificates. pki is required when policyType is PKI, and forbidden otherwise.

Type
:   `object`

Required
:   * `caRootsData`
    * `pkiCertificateSubject`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `caIntermediatesData` | `string` | caIntermediatesData contains base64-encoded data of a certificate bundle PEM file, which contains one or more intermediate certificates in the PEM format. The total length of the data must not exceed 8192 characters. caIntermediatesData requires caRootsData to be set. |
| `caRootsData` | `string` | caRootsData contains base64-encoded data of a certificate bundle PEM file, which contains one or more CA roots in the PEM format. The total length of the data must not exceed 8192 characters. |
| `pkiCertificateSubject` | `object` | pkiCertificateSubject defines the requirements imposed on the subject to which the certificate was issued. |

Show more

#### [15.1.7. .spec.policy.rootOfTrust.pki.pkiCertificateSubject](#spec-policy-rootoftrust-pki-pkicertificatesubject-2) Copy linkLink copied to clipboard!

Description
:   pkiCertificateSubject defines the requirements imposed on the subject to which the certificate was issued.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `email` | `string` | email specifies the expected email address imposed on the subject to which the certificate was issued, and must match the email address listed in the Subject Alternative Name (SAN) field of the certificate. The email must be a valid email address and at most 320 characters in length. |
| `hostname` | `string` | hostname specifies the expected hostname imposed on the subject to which the certificate was issued, and it must match the hostname listed in the Subject Alternative Name (SAN) DNS field of the certificate. The hostname must be a valid dns 1123 subdomain name, optionally prefixed by '\*.', and at most 253 characters in length. It must consist only of lowercase alphanumeric characters, hyphens, periods and the optional preceding asterisk. |

Show more

#### [15.1.8. .spec.policy.rootOfTrust.publicKey](#spec-policy-rootoftrust-publickey-2) Copy linkLink copied to clipboard!

Description
:   publicKey defines the root of trust configuration based on a sigstore public key. Optionally include a Rekor public key for Rekor verification. publicKey is required when policyType is PublicKey, and forbidden otherwise.

Type
:   `object`

Required
:   * `keyData`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `keyData` | `string` | keyData is a required field contains inline base64-encoded data for the PEM format public key. keyData must be at most 8192 characters. |
| `rekorKeyData` | `string` | rekorKeyData is an optional field contains inline base64-encoded data for the PEM format from the Rekor public key. rekorKeyData must be at most 8192 characters. |

Show more

#### [15.1.9. .spec.policy.signedIdentity](#spec-policy-signedidentity-2) Copy linkLink copied to clipboard!

Description
:   signedIdentity is an optional field specifies what image identity the signature claims about the image. This is useful when the image identity in the signature differs from the original image spec, such as when mirror registry is configured for the image scope, the signature from the mirror registry contains the image identity of the mirror instead of the original scope. The required matchPolicy field specifies the approach used in the verification process to verify the identity in the signature and the actual image identity, the default matchPolicy is "MatchRepoDigestOrExact".

Type
:   `object`

Required
:   * `matchPolicy`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `exactRepository` | `object` | exactRepository specifies the repository that must be exactly matched by the identity in the signature. exactRepository is required if matchPolicy is set to "ExactRepository". It is used to verify that the signature claims an identity matching this exact repository, rather than the original image identity. |
| `matchPolicy` | `string` | matchPolicy is a required filed specifies matching strategy to verify the image identity in the signature against the image scope. Allowed values are "MatchRepoDigestOrExact", "MatchRepository", "ExactRepository", "RemapIdentity". When omitted, the default value is "MatchRepoDigestOrExact". When set to "MatchRepoDigestOrExact", the identity in the signature must be in the same repository as the image identity if the image identity is referenced by a digest. Otherwise, the identity in the signature must be the same as the image identity. When set to "MatchRepository", the identity in the signature must be in the same repository as the image identity. When set to "ExactRepository", the exactRepository must be specified. The identity in the signature must be in the same repository as a specific identity specified by "repository". When set to "RemapIdentity", the remapIdentity must be specified. The signature must be in the same as the remapped image identity. Remapped image identity is obtained by replacing the "prefix" with the specified “signedPrefix” if the the image identity matches the specified remapPrefix. |
| `remapIdentity` | `object` | remapIdentity specifies the prefix remapping rule for verifying image identity. remapIdentity is required if matchPolicy is set to "RemapIdentity". It is used to verify that the signature claims a different registry/repository prefix than the original image. |

Show more

#### [15.1.10. .spec.policy.signedIdentity.exactRepository](#spec-policy-signedidentity-exactrepository-2) Copy linkLink copied to clipboard!

Description
:   exactRepository specifies the repository that must be exactly matched by the identity in the signature. exactRepository is required if matchPolicy is set to "ExactRepository". It is used to verify that the signature claims an identity matching this exact repository, rather than the original image identity.

Type
:   `object`

Required
:   * `repository`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `repository` | `string` | repository is the reference of the image identity to be matched. repository is required if matchPolicy is set to "ExactRepository". The value should be a repository name (by omitting the tag or digest) in a registry implementing the "Docker Registry HTTP API V2". For example, docker.io/library/busybox |

Show more

#### [15.1.11. .spec.policy.signedIdentity.remapIdentity](#spec-policy-signedidentity-remapidentity-2) Copy linkLink copied to clipboard!

Description
:   remapIdentity specifies the prefix remapping rule for verifying image identity. remapIdentity is required if matchPolicy is set to "RemapIdentity". It is used to verify that the signature claims a different registry/repository prefix than the original image.

Type
:   `object`

Required
:   * `prefix`
    * `signedPrefix`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `prefix` | `string` | prefix is required if matchPolicy is set to "RemapIdentity". prefix is the prefix of the image identity to be matched. If the image identity matches the specified prefix, that prefix is replaced by the specified “signedPrefix” (otherwise it is used as unchanged and no remapping takes place). This is useful when verifying signatures for a mirror of some other repository namespace that preserves the vendor’s repository structure. The prefix and signedPrefix values can be either host[:port] values (matching exactly the same host[:port], string), repository namespaces, or repositories (i.e. they must not contain tags/digests), and match as prefixes of the fully expanded form. For example, docker.io/library/busybox (not busybox) to specify that single repository, or docker.io/library (not an empty string) to specify the parent namespace of docker.io/library/busybox. |
| `signedPrefix` | `string` | signedPrefix is required if matchPolicy is set to "RemapIdentity". signedPrefix is the prefix of the image identity to be matched in the signature. The format is the same as "prefix". The values can be either host[:port] values (matching exactly the same host[:port], string), repository namespaces, or repositories (i.e. they must not contain tags/digests), and match as prefixes of the fully expanded form. For example, docker.io/library/busybox (not busybox) to specify that single repository, or docker.io/library (not an empty string) to specify the parent namespace of docker.io/library/busybox. |

Show more

#### [15.1.12. .status](#status-12) Copy linkLink copied to clipboard!

Description
:   status contains the observed state of the resource.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions provide details on the status of this API Resource. condition type 'Pending' indicates that the customer resource contains a policy that cannot take effect. It is either overwritten by a global policy or the image scope is not valid. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |

Show more

#### [15.1.13. .status.conditions](#status-conditions-11) Copy linkLink copied to clipboard!

Description
:   conditions provide details on the status of this API Resource. condition type 'Pending' indicates that the customer resource contains a policy that cannot take effect. It is either overwritten by a global policy or the image scope is not valid.

Type
:   `array`

#### [15.1.14. .status.conditions[]](#status-conditions-12) Copy linkLink copied to clipboard!

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

### [15.2. API endpoints](#api-endpoints-14) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/imagepolicies`

  + `GET`: list objects of kind ImagePolicy
* `/apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies`

  + `DELETE`: delete collection of ImagePolicy
  + `GET`: list objects of kind ImagePolicy
  + `POST`: create an ImagePolicy
* `/apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}`

  + `DELETE`: delete an ImagePolicy
  + `GET`: read the specified ImagePolicy
  + `PATCH`: partially update the specified ImagePolicy
  + `PUT`: replace the specified ImagePolicy
* `/apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}/status`

  + `GET`: read status of the specified ImagePolicy
  + `PATCH`: partially update status of the specified ImagePolicy
  + `PUT`: replace status of the specified ImagePolicy

#### [15.2.1. /apis/config.openshift.io/v1/imagepolicies](#apisconfig-openshift-iov1imagepolicies) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind ImagePolicy

Expand

Table 15.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImagePolicyList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [15.2.2. /apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies](#apisconfig-openshift-iov1namespacesnamespaceimagepolicies) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ImagePolicy

Expand

Table 15.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ImagePolicy

Expand

Table 15.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImagePolicyList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an ImagePolicy

Expand

Table 15.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 15.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [15.2.3. /apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}](#apisconfig-openshift-iov1namespacesnamespaceimagepoliciesname) Copy linkLink copied to clipboard!

Expand

Table 15.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImagePolicy |

Show more

HTTP method
:   `DELETE`

Description
:   delete an ImagePolicy

Expand

Table 15.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 15.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ImagePolicy

Expand

Table 15.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ImagePolicy

Expand

Table 15.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ImagePolicy

Expand

Table 15.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 15.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [15.2.4. /apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}/status](#apisconfig-openshift-iov1namespacesnamespaceimagepoliciesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 15.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImagePolicy |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ImagePolicy

Expand

Table 15.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ImagePolicy

Expand

Table 15.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ImagePolicy

Expand

Table 15.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 15.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 15.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 201 - Created | [`ImagePolicy`](#imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]](#imagetagmirrorset-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   ImageTagMirrorSet holds cluster-wide information about how to handle registry mirror rules on using tag pull specification. When multiple policies are defined, the outcome of the behavior is defined on each field.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [16.1. Specification](#specification-15) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status contains the observed state of the resource. |

Show more

#### [16.1.1. .spec](#spec-15) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `imageTagMirrors` | `array` | imageTagMirrors allows images referenced by image tags in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageTagMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using digest specification only, users should configure a list of mirrors using "ImageDigestMirrorSet" CRD.  If the image pull specification matches the repository of "source" in multiple imagetagmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.  If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.  When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a deterministic order of mirrors, should configure them into one list of mirrors using the expected order. |
| `imageTagMirrors[]` | `object` | ImageTagMirrors holds cluster-wide information about how to handle mirrors in the registries config. |

Show more

#### [16.1.2. .spec.imageTagMirrors](#spec-imagetagmirrors) Copy linkLink copied to clipboard!

Description
:   imageTagMirrors allows images referenced by image tags in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageTagMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using digest specification only, users should configure a list of mirrors using "ImageDigestMirrorSet" CRD.

    If the image pull specification matches the repository of "source" in multiple imagetagmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.

    If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.

    When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a deterministic order of mirrors, should configure them into one list of mirrors using the expected order.

Type
:   `array`

#### [16.1.3. .spec.imageTagMirrors[]](#spec-imagetagmirrors-2) Copy linkLink copied to clipboard!

Description
:   ImageTagMirrors holds cluster-wide information about how to handle mirrors in the registries config.

Type
:   `object`

Required
:   * `source`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mirrorSourcePolicy` | `string` | mirrorSourcePolicy defines the fallback policy if fails to pull image from the mirrors. If unset, the image will continue to be pulled from the repository in the pull spec. sourcePolicy is valid configuration only when one or more mirrors are in the mirror list. |
| `mirrors` | `array (string)` | mirrors is zero or more locations that may also contain the same images. No mirror will be configured if not specified. Images can be pulled from these mirrors only if they are referenced by their tags. The mirrored location is obtained by replacing the part of the input reference that matches source by the mirrors entry, e.g. for registry.redhat.io/product/repo reference, a (source, mirror) pair \*.redhat.io, mirror.local/redhat causes a mirror.local/redhat/product/repo repository to be used. Pulling images by tag can potentially yield different images, depending on which endpoint we pull from. Configuring a list of mirrors using "ImageDigestMirrorSet" CRD and forcing digest-pulls for mirrors avoids that issue. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. If no mirror is specified or all image pulls from the mirror list fail, the image will continue to be pulled from the repository in the pull spec unless explicitly prohibited by "mirrorSourcePolicy". Other cluster configuration, including (but not limited to) other imageTagMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. "mirrors" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table> |
| `source` | `string` | source matches the repository that users refer to, e.g. in image pull specifications. Setting source to a registry hostname e.g. docker.io. quay.io, or registry.redhat.io, will match the image pull specification of corressponding registry. "source" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo [\*.]host for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table> |

Show more

#### [16.1.4. .status](#status-13) Copy linkLink copied to clipboard!

Description
:   status contains the observed state of the resource.

Type
:   `object`

### [16.2. API endpoints](#api-endpoints-15) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/imagetagmirrorsets`

  + `DELETE`: delete collection of ImageTagMirrorSet
  + `GET`: list objects of kind ImageTagMirrorSet
  + `POST`: create an ImageTagMirrorSet
* `/apis/config.openshift.io/v1/imagetagmirrorsets/{name}`

  + `DELETE`: delete an ImageTagMirrorSet
  + `GET`: read the specified ImageTagMirrorSet
  + `PATCH`: partially update the specified ImageTagMirrorSet
  + `PUT`: replace the specified ImageTagMirrorSet
* `/apis/config.openshift.io/v1/imagetagmirrorsets/{name}/status`

  + `GET`: read status of the specified ImageTagMirrorSet
  + `PATCH`: partially update status of the specified ImageTagMirrorSet
  + `PUT`: replace status of the specified ImageTagMirrorSet

#### [16.2.1. /apis/config.openshift.io/v1/imagetagmirrorsets](#apisconfig-openshift-iov1imagetagmirrorsets) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ImageTagMirrorSet

Expand

Table 16.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ImageTagMirrorSet

Expand

Table 16.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImageTagMirrorSetList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an ImageTagMirrorSet

Expand

Table 16.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 16.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 16.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 202 - Accepted | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [16.2.2. /apis/config.openshift.io/v1/imagetagmirrorsets/{name}](#apisconfig-openshift-iov1imagetagmirrorsetsname) Copy linkLink copied to clipboard!

Expand

Table 16.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImageTagMirrorSet |

Show more

HTTP method
:   `DELETE`

Description
:   delete an ImageTagMirrorSet

Expand

Table 16.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 16.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ImageTagMirrorSet

Expand

Table 16.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ImageTagMirrorSet

Expand

Table 16.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 16.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ImageTagMirrorSet

Expand

Table 16.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 16.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 16.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [16.2.3. /apis/config.openshift.io/v1/imagetagmirrorsets/{name}/status](#apisconfig-openshift-iov1imagetagmirrorsetsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 16.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ImageTagMirrorSet |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ImageTagMirrorSet

Expand

Table 16.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ImageTagMirrorSet

Expand

Table 16.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 16.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ImageTagMirrorSet

Expand

Table 16.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 16.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 16.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 201 - Created | [`ImageTagMirrorSet`](#imagetagmirrorset-config-openshift-io-v1 "Chapter 16. ImageTagMirrorSet [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 17. InsightsDataGather [config.openshift.io/v1]](#insightsdatagather-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   InsightsDataGather provides data gather configuration options for the Insights Operator.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [17.1. Specification](#specification-16) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |

Show more

#### [17.1.1. .spec](#spec-16) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Required
:   * `gatherConfig`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `gatherConfig` | `object` | gatherConfig is a required spec attribute that includes all the configuration options related to gathering of the Insights data and its uploading to the ingress. |

Show more

#### [17.1.2. .spec.gatherConfig](#spec-gatherconfig) Copy linkLink copied to clipboard!

Description
:   gatherConfig is a required spec attribute that includes all the configuration options related to gathering of the Insights data and its uploading to the ingress.

Type
:   `object`

Required
:   * `gatherers`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `dataPolicy` | `array (string)` | dataPolicy is an optional list of DataPolicyOptions that allows user to enable additional obfuscation of the Insights archive data. It may not exceed 2 items and must not contain duplicates. Valid values are ObfuscateNetworking and WorkloadNames. When set to ObfuscateNetworking the IP addresses and the cluster domain name are obfuscated. When set to WorkloadNames, the gathered data about cluster resources will not contain the workload names for your deployments. Resources UIDs will be used instead. When omitted no obfuscation is applied. |
| `gatherers` | `object` | gatherers is a required field that specifies the configuration of the gatherers. |
| `storage` | `object` | storage is an optional field that allows user to define persistent storage for gathering jobs to store the Insights data archive. If omitted, the gathering job will use ephemeral storage. |

Show more

#### [17.1.3. .spec.gatherConfig.gatherers](#spec-gatherconfig-gatherers) Copy linkLink copied to clipboard!

Description
:   gatherers is a required field that specifies the configuration of the gatherers.

Type
:   `object`

Required
:   * `mode`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `custom` | `object` | custom provides gathering configuration. It is required when mode is Custom, and forbidden otherwise. Custom configuration allows user to disable only a subset of gatherers. Gatherers that are not explicitly disabled in custom configuration will run. |
| `mode` | `string` | mode is a required field that specifies the mode for gatherers. Allowed values are All, None, and Custom. When set to All, all gatherers will run and gather data. When set to None, all gatherers will be disabled and no data will be gathered. When set to Custom, the custom configuration from the custom field will be applied. |

Show more

#### [17.1.4. .spec.gatherConfig.gatherers.custom](#spec-gatherconfig-gatherers-custom) Copy linkLink copied to clipboard!

Description
:   custom provides gathering configuration. It is required when mode is Custom, and forbidden otherwise. Custom configuration allows user to disable only a subset of gatherers. Gatherers that are not explicitly disabled in custom configuration will run.

Type
:   `object`

Required
:   * `configs`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `configs` | `array` | configs is a required list of gatherers configurations that can be used to enable or disable specific gatherers. It may not exceed 100 items and each gatherer can be present only once. It is possible to disable an entire set of gatherers while allowing a specific function within that set. The particular gatherers IDs can be found at <https://github.com/openshift/insights-operator/blob/master/docs/gathered-data.md>. Run the following command to get the names of last active gatherers: "oc get insightsoperators.operator.openshift.io cluster -o json | jq '.status.gatherStatus.gatherers[].name'" |
| `configs[]` | `object` | GathererConfig allows to configure specific gatherers |

Show more

#### [17.1.5. .spec.gatherConfig.gatherers.custom.configs](#spec-gatherconfig-gatherers-custom-configs) Copy linkLink copied to clipboard!

Description
:   configs is a required list of gatherers configurations that can be used to enable or disable specific gatherers. It may not exceed 100 items and each gatherer can be present only once. It is possible to disable an entire set of gatherers while allowing a specific function within that set. The particular gatherers IDs can be found at <https://github.com/openshift/insights-operator/blob/master/docs/gathered-data.md>. Run the following command to get the names of last active gatherers: "oc get insightsoperators.operator.openshift.io cluster -o json \| jq '.status.gatherStatus.gatherers[].name'"

Type
:   `array`

#### [17.1.6. .spec.gatherConfig.gatherers.custom.configs[]](#spec-gatherconfig-gatherers-custom-configs-2) Copy linkLink copied to clipboard!

Description
:   GathererConfig allows to configure specific gatherers

Type
:   `object`

Required
:   * `name`
    * `state`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the required name of a specific gatherer. It may not exceed 256 characters. The format for a gatherer name is: {gatherer}/{function} where the function is optional. Gatherer consists of a lowercase letters only that may include underscores (*). Function consists of a lowercase letters only that may include underscores (*) and is separated from the gatherer by a forward slash (/). The particular gatherers can be found at <https://github.com/openshift/insights-operator/blob/master/docs/gathered-data.md>. Run the following command to get the names of last active gatherers: "oc get insightsoperators.operator.openshift.io cluster -o json | jq '.status.gatherStatus.gatherers[].name'" |
| `state` | `string` | state is a required field that allows you to configure specific gatherer. Valid values are "Enabled" and "Disabled". When set to Enabled the gatherer will run. When set to Disabled the gatherer will not run. |

Show more

#### [17.1.7. .spec.gatherConfig.storage](#spec-gatherconfig-storage) Copy linkLink copied to clipboard!

Description
:   storage is an optional field that allows user to define persistent storage for gathering jobs to store the Insights data archive. If omitted, the gathering job will use ephemeral storage.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `persistentVolume` | `object` | persistentVolume is an optional field that specifies the PersistentVolume that will be used to store the Insights data archive. The PersistentVolume must be created in the openshift-insights namespace. |
| `type` | `string` | type is a required field that specifies the type of storage that will be used to store the Insights data archive. Valid values are "PersistentVolume" and "Ephemeral". When set to Ephemeral, the Insights data archive is stored in the ephemeral storage of the gathering job. When set to PersistentVolume, the Insights data archive is stored in the PersistentVolume that is defined by the persistentVolume field. |

Show more

#### [17.1.8. .spec.gatherConfig.storage.persistentVolume](#spec-gatherconfig-storage-persistentvolume) Copy linkLink copied to clipboard!

Description
:   persistentVolume is an optional field that specifies the PersistentVolume that will be used to store the Insights data archive. The PersistentVolume must be created in the openshift-insights namespace.

Type
:   `object`

Required
:   * `claim`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claim` | `object` | claim is a required field that specifies the configuration of the PersistentVolumeClaim that will be used to store the Insights data archive. The PersistentVolumeClaim must be created in the openshift-insights namespace. |
| `mountPath` | `string` | mountPath is an optional field specifying the directory where the PVC will be mounted inside the Insights data gathering Pod. When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default mount path is /var/lib/insights-operator The path may not exceed 1024 characters and must not contain a colon. |

Show more

#### [17.1.9. .spec.gatherConfig.storage.persistentVolume.claim](#spec-gatherconfig-storage-persistentvolume-claim) Copy linkLink copied to clipboard!

Description
:   claim is a required field that specifies the configuration of the PersistentVolumeClaim that will be used to store the Insights data archive. The PersistentVolumeClaim must be created in the openshift-insights namespace.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the PersistentVolumeClaim that will be used to store the Insights data archive. It is a string that follows the DNS1123 subdomain format. It must be at most 253 characters in length, and must consist only of lower case alphanumeric characters, '-' and '.', and must start and end with an alphanumeric character. |

Show more

### [17.2. API endpoints](#api-endpoints-16) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/insightsdatagathers`

  + `DELETE`: delete collection of InsightsDataGather
  + `GET`: list objects of kind InsightsDataGather
  + `POST`: create an InsightsDataGather
* `/apis/config.openshift.io/v1/insightsdatagathers/{name}`

  + `DELETE`: delete an InsightsDataGather
  + `GET`: read the specified InsightsDataGather
  + `PATCH`: partially update the specified InsightsDataGather
  + `PUT`: replace the specified InsightsDataGather

#### [17.2.1. /apis/config.openshift.io/v1/insightsdatagathers](#apisconfig-openshift-iov1insightsdatagathers) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of InsightsDataGather

Expand

Table 17.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind InsightsDataGather

Expand

Table 17.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`InsightsDataGatherList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-InsightsDataGatherList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an InsightsDataGather

Expand

Table 17.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 17.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 17.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 201 - Created | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 202 - Accepted | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [17.2.2. /apis/config.openshift.io/v1/insightsdatagathers/{name}](#apisconfig-openshift-iov1insightsdatagathersname) Copy linkLink copied to clipboard!

Expand

Table 17.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the InsightsDataGather |

Show more

HTTP method
:   `DELETE`

Description
:   delete an InsightsDataGather

Expand

Table 17.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 17.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified InsightsDataGather

Expand

Table 17.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified InsightsDataGather

Expand

Table 17.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 17.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified InsightsDataGather

Expand

Table 17.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 17.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 17.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 201 - Created | [`InsightsDataGather`](#insightsdatagather-config-openshift-io-v1 "Chapter 17. InsightsDataGather [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 18. Infrastructure [config.openshift.io/v1]](#infrastructure-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Infrastructure holds cluster-wide information about Infrastructure. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [18.1. Specification](#specification-17) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [18.1.1. .spec](#spec-17) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cloudConfig` | `object` | cloudConfig is a reference to a ConfigMap containing the cloud provider configuration file. This configuration file is used to configure the Kubernetes cloud provider integration when using the built-in cloud provider integration or the external cloud controller manager. The namespace for this config map is openshift-config.  cloudConfig should only be consumed by the kube\_cloud\_config controller. The controller is responsible for using the user configuration in the spec for various platforms and combining that with the user provided ConfigMap in this field to create a stitched kube cloud config. The controller generates a ConfigMap `kube-cloud-config` in `openshift-config-managed` namespace with the kube cloud config is stored in `cloud.conf` key. All the clients are expected to use the generated ConfigMap only. |
| `platformSpec` | `object` | platformSpec holds desired information specific to the underlying infrastructure provider. |

Show more

#### [18.1.2. .spec.cloudConfig](#spec-cloudconfig) Copy linkLink copied to clipboard!

Description
:   cloudConfig is a reference to a ConfigMap containing the cloud provider configuration file. This configuration file is used to configure the Kubernetes cloud provider integration when using the built-in cloud provider integration or the external cloud controller manager. The namespace for this config map is openshift-config.

    cloudConfig should only be consumed by the kube\_cloud\_config controller. The controller is responsible for using the user configuration in the spec for various platforms and combining that with the user provided ConfigMap in this field to create a stitched kube cloud config. The controller generates a ConfigMap `kube-cloud-config` in `openshift-config-managed` namespace with the kube cloud config is stored in `cloud.conf` key. All the clients are expected to use the generated ConfigMap only.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key allows pointing to a specific key/value inside of the configmap. This is useful for logical file references. |
| `name` | `string` |  |

Show more

#### [18.1.3. .spec.platformSpec](#spec-platformspec) Copy linkLink copied to clipboard!

Description
:   platformSpec holds desired information specific to the underlying infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `alibabaCloud` | `object` | alibabaCloud contains settings specific to the Alibaba Cloud infrastructure provider. |
| `aws` | `object` | aws contains settings specific to the Amazon Web Services infrastructure provider. |
| `azure` | `object` | azure contains settings specific to the Azure infrastructure provider. |
| `baremetal` | `object` | baremetal contains settings specific to the BareMetal platform. |
| `equinixMetal` | `object` | equinixMetal contains settings specific to the Equinix Metal infrastructure provider. |
| `external` | `object` | ExternalPlatformType represents generic infrastructure provider. Platform-specific components should be supplemented separately. |
| `gcp` | `object` | gcp contains settings specific to the Google Cloud Platform infrastructure provider. |
| `ibmcloud` | `object` | ibmcloud contains settings specific to the IBMCloud infrastructure provider. |
| `kubevirt` | `object` | kubevirt contains settings specific to the kubevirt infrastructure provider. |
| `nutanix` | `object` | nutanix contains settings specific to the Nutanix infrastructure provider. |
| `openstack` | `object` | openstack contains settings specific to the OpenStack infrastructure provider. |
| `ovirt` | `object` | ovirt contains settings specific to the oVirt infrastructure provider. |
| `powervs` | `object` | powervs contains settings specific to the IBM Power Systems Virtual Servers infrastructure provider. |
| `type` | `string` | type is the underlying infrastructure provider for the cluster. This value controls whether infrastructure automation such as service load balancers, dynamic volume provisioning, machine creation and deletion, and other integrations are enabled. If None, no infrastructure automation is enabled. Allowed values are "AWS", "Azure", "BareMetal", "GCP", "Libvirt", "OpenStack", "VSphere", "oVirt", "IBMCloud", "KubeVirt", "EquinixMetal", "PowerVS", "AlibabaCloud", "Nutanix", "External", and "None". Individual components may not support all platforms, and must handle unrecognized platforms as None if they do not support that platform. |
| `vsphere` | `object` | vsphere contains settings specific to the VSphere infrastructure provider. |

Show more

#### [18.1.4. .spec.platformSpec.alibabaCloud](#spec-platformspec-alibabacloud) Copy linkLink copied to clipboard!

Description
:   alibabaCloud contains settings specific to the Alibaba Cloud infrastructure provider.

Type
:   `object`

#### [18.1.5. .spec.platformSpec.aws](#spec-platformspec-aws) Copy linkLink copied to clipboard!

Description
:   aws contains settings specific to the Amazon Web Services infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `serviceEndpoints` | `array` | serviceEndpoints list contains custom endpoints which will override default service endpoint of AWS Services. There must be only one ServiceEndpoint for a service. |
| `serviceEndpoints[]` | `object` | AWSServiceEndpoint store the configuration of a custom url to override existing defaults of AWS Services. |

Show more

#### [18.1.6. .spec.platformSpec.aws.serviceEndpoints](#spec-platformspec-aws-serviceendpoints) Copy linkLink copied to clipboard!

Description
:   serviceEndpoints list contains custom endpoints which will override default service endpoint of AWS Services. There must be only one ServiceEndpoint for a service.

Type
:   `array`

#### [18.1.7. .spec.platformSpec.aws.serviceEndpoints[]](#spec-platformspec-aws-serviceendpoints-2) Copy linkLink copied to clipboard!

Description
:   AWSServiceEndpoint store the configuration of a custom url to override existing defaults of AWS Services.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the AWS service. The list of all the service names can be found at <https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html> This must be provided and cannot be empty. |
| `url` | `string` | url is fully qualified URI with scheme https, that overrides the default generated endpoint for a client. This must be provided and cannot be empty. |

Show more

#### [18.1.8. .spec.platformSpec.azure](#spec-platformspec-azure) Copy linkLink copied to clipboard!

Description
:   azure contains settings specific to the Azure infrastructure provider.

Type
:   `object`

#### [18.1.9. .spec.platformSpec.baremetal](#spec-platformspec-baremetal) Copy linkLink copied to clipboard!

Description
:   baremetal contains settings specific to the BareMetal platform.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IP addresses, one from IPv4 family and one from IPv6. In single stack clusters a single IP address is expected. When omitted, values from the status.apiServerInternalIPs will be used. Once set, the list cannot be completely removed (but its second entry can). |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IP addresses, one from IPv4 family and one from IPv6. In single stack clusters a single IP address is expected. When omitted, values from the status.ingressIPs will be used. Once set, the list cannot be completely removed (but its second entry can). |
| `machineNetworks` | `array (string)` | machineNetworks are IP networks used to connect all the OpenShift cluster nodes. Each network is provided in the CIDR format and should be IPv4 or IPv6, for example "10.0.0.0/8" or "fd00::/8". |

Show more

#### [18.1.10. .spec.platformSpec.equinixMetal](#spec-platformspec-equinixmetal) Copy linkLink copied to clipboard!

Description
:   equinixMetal contains settings specific to the Equinix Metal infrastructure provider.

Type
:   `object`

#### [18.1.11. .spec.platformSpec.external](#spec-platformspec-external) Copy linkLink copied to clipboard!

Description
:   ExternalPlatformType represents generic infrastructure provider. Platform-specific components should be supplemented separately.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `platformName` | `string` | platformName holds the arbitrary string representing the infrastructure provider name, expected to be set at the installation time. This field is solely for informational and reporting purposes and is not expected to be used for decision-making. |

Show more

#### [18.1.12. .spec.platformSpec.gcp](#spec-platformspec-gcp) Copy linkLink copied to clipboard!

Description
:   gcp contains settings specific to the Google Cloud Platform infrastructure provider.

Type
:   `object`

#### [18.1.13. .spec.platformSpec.ibmcloud](#spec-platformspec-ibmcloud) Copy linkLink copied to clipboard!

Description
:   ibmcloud contains settings specific to the IBMCloud infrastructure provider.

Type
:   `object`

#### [18.1.14. .spec.platformSpec.kubevirt](#spec-platformspec-kubevirt) Copy linkLink copied to clipboard!

Description
:   kubevirt contains settings specific to the kubevirt infrastructure provider.

Type
:   `object`

#### [18.1.15. .spec.platformSpec.nutanix](#spec-platformspec-nutanix) Copy linkLink copied to clipboard!

Description
:   nutanix contains settings specific to the Nutanix infrastructure provider.

Type
:   `object`

Required
:   * `prismCentral`
    * `prismElements`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `failureDomains` | `array` | failureDomains configures failure domains information for the Nutanix platform. When set, the failure domains defined here may be used to spread Machines across prism element clusters to improve fault tolerance of the cluster. |
| `failureDomains[]` | `object` | NutanixFailureDomain configures failure domain information for the Nutanix platform. |
| `prismCentral` | `object` | prismCentral holds the endpoint address and port to access the Nutanix Prism Central. When a cluster-wide proxy is installed, by default, this endpoint will be accessed via the proxy. Should you wish for communication with this endpoint not to be proxied, please add the endpoint to the proxy spec.noProxy list. |
| `prismElements` | `array` | prismElements holds one or more endpoint address and port data to access the Nutanix Prism Elements (clusters) of the Nutanix Prism Central. Currently we only support one Prism Element (cluster) for an OpenShift cluster, where all the Nutanix resources (VMs, subnets, volumes, etc.) used in the OpenShift cluster are located. In the future, we may support Nutanix resources (VMs, etc.) spread over multiple Prism Elements (clusters) of the Prism Central. |
| `prismElements[]` | `object` | NutanixPrismElementEndpoint holds the name and endpoint data for a Prism Element (cluster) |

Show more

#### [18.1.16. .spec.platformSpec.nutanix.failureDomains](#spec-platformspec-nutanix-failuredomains) Copy linkLink copied to clipboard!

Description
:   failureDomains configures failure domains information for the Nutanix platform. When set, the failure domains defined here may be used to spread Machines across prism element clusters to improve fault tolerance of the cluster.

Type
:   `array`

#### [18.1.17. .spec.platformSpec.nutanix.failureDomains[]](#spec-platformspec-nutanix-failuredomains-2) Copy linkLink copied to clipboard!

Description
:   NutanixFailureDomain configures failure domain information for the Nutanix platform.

Type
:   `object`

Required
:   * `cluster`
    * `name`
    * `subnets`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cluster` | `object` | cluster is to identify the cluster (the Prism Element under management of the Prism Central), in which the Machine’s VM will be created. The cluster identifier (uuid or name) can be obtained from the Prism Central console or using the prism\_central API. |
| `name` | `string` | name defines the unique name of a failure domain. Name is required and must be at most 64 characters in length. It must consist of only lower case alphanumeric characters and hyphens (-). It must start and end with an alphanumeric character. This value is arbitrary and is used to identify the failure domain within the platform. |
| `subnets` | `array` | subnets holds a list of identifiers (one or more) of the cluster’s network subnets If the feature gate NutanixMultiSubnets is enabled, up to 32 subnets may be configured. for the Machine’s VM to connect to. The subnet identifiers (uuid or name) can be obtained from the Prism Central console or using the prism\_central API. |
| `subnets[]` | `object` | NutanixResourceIdentifier holds the identity of a Nutanix PC resource (cluster, image, subnet, etc.) |

Show more

#### [18.1.18. .spec.platformSpec.nutanix.failureDomains[].cluster](#spec-platformspec-nutanix-failuredomains-cluster) Copy linkLink copied to clipboard!

Description
:   cluster is to identify the cluster (the Prism Element under management of the Prism Central), in which the Machine’s VM will be created. The cluster identifier (uuid or name) can be obtained from the Prism Central console or using the prism\_central API.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the resource name in the PC. It cannot be empty if the type is Name. |
| `type` | `string` | type is the identifier type to use for this resource. |
| `uuid` | `string` | uuid is the UUID of the resource in the PC. It cannot be empty if the type is UUID. |

Show more

#### [18.1.19. .spec.platformSpec.nutanix.failureDomains[].subnets](#spec-platformspec-nutanix-failuredomains-subnets) Copy linkLink copied to clipboard!

Description
:   subnets holds a list of identifiers (one or more) of the cluster’s network subnets If the feature gate NutanixMultiSubnets is enabled, up to 32 subnets may be configured. for the Machine’s VM to connect to. The subnet identifiers (uuid or name) can be obtained from the Prism Central console or using the prism\_central API.

Type
:   `array`

#### [18.1.20. .spec.platformSpec.nutanix.failureDomains[].subnets[]](#spec-platformspec-nutanix-failuredomains-subnets-2) Copy linkLink copied to clipboard!

Description
:   NutanixResourceIdentifier holds the identity of a Nutanix PC resource (cluster, image, subnet, etc.)

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the resource name in the PC. It cannot be empty if the type is Name. |
| `type` | `string` | type is the identifier type to use for this resource. |
| `uuid` | `string` | uuid is the UUID of the resource in the PC. It cannot be empty if the type is UUID. |

Show more

#### [18.1.21. .spec.platformSpec.nutanix.prismCentral](#spec-platformspec-nutanix-prismcentral) Copy linkLink copied to clipboard!

Description
:   prismCentral holds the endpoint address and port to access the Nutanix Prism Central. When a cluster-wide proxy is installed, by default, this endpoint will be accessed via the proxy. Should you wish for communication with this endpoint not to be proxied, please add the endpoint to the proxy spec.noProxy list.

Type
:   `object`

Required
:   * `address`
    * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `address` | `string` | address is the endpoint address (DNS name or IP address) of the Nutanix Prism Central or Element (cluster) |
| `port` | `integer` | port is the port number to access the Nutanix Prism Central or Element (cluster) |

Show more

#### [18.1.22. .spec.platformSpec.nutanix.prismElements](#spec-platformspec-nutanix-prismelements) Copy linkLink copied to clipboard!

Description
:   prismElements holds one or more endpoint address and port data to access the Nutanix Prism Elements (clusters) of the Nutanix Prism Central. Currently we only support one Prism Element (cluster) for an OpenShift cluster, where all the Nutanix resources (VMs, subnets, volumes, etc.) used in the OpenShift cluster are located. In the future, we may support Nutanix resources (VMs, etc.) spread over multiple Prism Elements (clusters) of the Prism Central.

Type
:   `array`

#### [18.1.23. .spec.platformSpec.nutanix.prismElements[]](#spec-platformspec-nutanix-prismelements-2) Copy linkLink copied to clipboard!

Description
:   NutanixPrismElementEndpoint holds the name and endpoint data for a Prism Element (cluster)

Type
:   `object`

Required
:   * `endpoint`
    * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `endpoint` | `object` | endpoint holds the endpoint address and port data of the Prism Element (cluster). When a cluster-wide proxy is installed, by default, this endpoint will be accessed via the proxy. Should you wish for communication with this endpoint not to be proxied, please add the endpoint to the proxy spec.noProxy list. |
| `name` | `string` | name is the name of the Prism Element (cluster). This value will correspond with the cluster field configured on other resources (eg Machines, PVCs, etc). |

Show more

#### [18.1.24. .spec.platformSpec.nutanix.prismElements[].endpoint](#spec-platformspec-nutanix-prismelements-endpoint) Copy linkLink copied to clipboard!

Description
:   endpoint holds the endpoint address and port data of the Prism Element (cluster). When a cluster-wide proxy is installed, by default, this endpoint will be accessed via the proxy. Should you wish for communication with this endpoint not to be proxied, please add the endpoint to the proxy spec.noProxy list.

Type
:   `object`

Required
:   * `address`
    * `port`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `address` | `string` | address is the endpoint address (DNS name or IP address) of the Nutanix Prism Central or Element (cluster) |
| `port` | `integer` | port is the port number to access the Nutanix Prism Central or Element (cluster) |

Show more

#### [18.1.25. .spec.platformSpec.openstack](#spec-platformspec-openstack) Copy linkLink copied to clipboard!

Description
:   openstack contains settings specific to the OpenStack infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IP addresses, one from IPv4 family and one from IPv6. In single stack clusters a single IP address is expected. When omitted, values from the status.apiServerInternalIPs will be used. Once set, the list cannot be completely removed (but its second entry can). |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IP addresses, one from IPv4 family and one from IPv6. In single stack clusters a single IP address is expected. When omitted, values from the status.ingressIPs will be used. Once set, the list cannot be completely removed (but its second entry can). |
| `machineNetworks` | `array (string)` | machineNetworks are IP networks used to connect all the OpenShift cluster nodes. Each network is provided in the CIDR format and should be IPv4 or IPv6, for example "10.0.0.0/8" or "fd00::/8". |

Show more

#### [18.1.26. .spec.platformSpec.ovirt](#spec-platformspec-ovirt) Copy linkLink copied to clipboard!

Description
:   ovirt contains settings specific to the oVirt infrastructure provider.

Type
:   `object`

#### [18.1.27. .spec.platformSpec.powervs](#spec-platformspec-powervs) Copy linkLink copied to clipboard!

Description
:   powervs contains settings specific to the IBM Power Systems Virtual Servers infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `serviceEndpoints` | `array` | serviceEndpoints is a list of custom endpoints which will override the default service endpoints of a Power VS service. |
| `serviceEndpoints[]` | `object` | PowervsServiceEndpoint stores the configuration of a custom url to override existing defaults of PowerVS Services. |

Show more

#### [18.1.28. .spec.platformSpec.powervs.serviceEndpoints](#spec-platformspec-powervs-serviceendpoints) Copy linkLink copied to clipboard!

Description
:   serviceEndpoints is a list of custom endpoints which will override the default service endpoints of a Power VS service.

Type
:   `array`

#### [18.1.29. .spec.platformSpec.powervs.serviceEndpoints[]](#spec-platformspec-powervs-serviceendpoints-2) Copy linkLink copied to clipboard!

Description
:   PowervsServiceEndpoint stores the configuration of a custom url to override existing defaults of PowerVS Services.

Type
:   `object`

Required
:   * `name`
    * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the Power VS service. Few of the services are IAM - <https://cloud.ibm.com/apidocs/iam-identity-token-api> ResourceController - <https://cloud.ibm.com/apidocs/resource-controller/resource-controller> Power Cloud - <https://cloud.ibm.com/apidocs/power-cloud> |
| `url` | `string` | url is fully qualified URI with scheme https, that overrides the default generated endpoint for a client. This must be provided and cannot be empty. |

Show more

#### [18.1.30. .spec.platformSpec.vsphere](#spec-platformspec-vsphere) Copy linkLink copied to clipboard!

Description
:   vsphere contains settings specific to the VSphere infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IP addresses, one from IPv4 family and one from IPv6. In single stack clusters a single IP address is expected. When omitted, values from the status.apiServerInternalIPs will be used. Once set, the list cannot be completely removed (but its second entry can). |
| `failureDomains` | `array` | failureDomains contains the definition of region, zone and the vCenter topology. If this is omitted failure domains (regions and zones) will not be used. |
| `failureDomains[]` | `object` | VSpherePlatformFailureDomainSpec holds the region and zone failure domain and the vCenter topology of that failure domain. |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IP addresses, one from IPv4 family and one from IPv6. In single stack clusters a single IP address is expected. When omitted, values from the status.ingressIPs will be used. Once set, the list cannot be completely removed (but its second entry can). |
| `machineNetworks` | `array (string)` | machineNetworks are IP networks used to connect all the OpenShift cluster nodes. Each network is provided in the CIDR format and should be IPv4 or IPv6, for example "10.0.0.0/8" or "fd00::/8". |
| `nodeNetworking` | `object` | nodeNetworking contains the definition of internal and external network constraints for assigning the node’s networking. If this field is omitted, networking defaults to the legacy address selection behavior which is to only support a single address and return the first one found. |
| `vcenters` | `array` | vcenters holds the connection details for services to communicate with vCenter. Currently, only a single vCenter is supported, but in tech preview 3 vCenters are supported. Once the cluster has been installed, you are unable to change the current number of defined vCenters except in the case where the cluster has been upgraded from a version of OpenShift where the vsphere platform spec was not present. You may make modifications to the existing vCenters that are defined in the vcenters list in order to match with any added or modified failure domains. |
| `vcenters[]` | `object` | VSpherePlatformVCenterSpec stores the vCenter connection fields. This is used by the vSphere CCM. |

Show more

#### [18.1.31. .spec.platformSpec.vsphere.failureDomains](#spec-platformspec-vsphere-failuredomains) Copy linkLink copied to clipboard!

Description
:   failureDomains contains the definition of region, zone and the vCenter topology. If this is omitted failure domains (regions and zones) will not be used.

Type
:   `array`

#### [18.1.32. .spec.platformSpec.vsphere.failureDomains[]](#spec-platformspec-vsphere-failuredomains-2) Copy linkLink copied to clipboard!

Description
:   VSpherePlatformFailureDomainSpec holds the region and zone failure domain and the vCenter topology of that failure domain.

Type
:   `object`

Required
:   * `name`
    * `region`
    * `server`
    * `topology`
    * `zone`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name defines the arbitrary but unique name of a failure domain. |
| `region` | `string` | region defines the name of a region tag that will be attached to a vCenter datacenter. The tag category in vCenter must be named openshift-region. |
| `regionAffinity` | `object` | regionAffinity holds the type of region, Datacenter or ComputeCluster. When set to Datacenter, this means the region is a vCenter Datacenter as defined in topology. When set to ComputeCluster, this means the region is a vCenter Cluster as defined in topology. |
| `server` | `string` | server is the fully-qualified domain name or the IP address of the vCenter server. |
| `topology` | `object` | topology describes a given failure domain using vSphere constructs |
| `zone` | `string` | zone defines the name of a zone tag that will be attached to a vCenter cluster. The tag category in vCenter must be named openshift-zone. |
| `zoneAffinity` | `object` | zoneAffinity holds the type of the zone and the hostGroup which vmGroup and the hostGroup names in vCenter corresponds to a vm-host group of type Virtual Machine and Host respectively. Is also contains the vmHostRule which is an affinity vm-host rule in vCenter. |

Show more

#### [18.1.33. .spec.platformSpec.vsphere.failureDomains[].regionAffinity](#spec-platformspec-vsphere-failuredomains-regionaffinity) Copy linkLink copied to clipboard!

Description
:   regionAffinity holds the type of region, Datacenter or ComputeCluster. When set to Datacenter, this means the region is a vCenter Datacenter as defined in topology. When set to ComputeCluster, this means the region is a vCenter Cluster as defined in topology.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type determines the vSphere object type for a region within this failure domain. Available types are Datacenter and ComputeCluster. When set to Datacenter, this means the vCenter Datacenter defined is the region. When set to ComputeCluster, this means the vCenter cluster defined is the region. |

Show more

#### [18.1.34. .spec.platformSpec.vsphere.failureDomains[].topology](#spec-platformspec-vsphere-failuredomains-topology) Copy linkLink copied to clipboard!

Description
:   topology describes a given failure domain using vSphere constructs

Type
:   `object`

Required
:   * `computeCluster`
    * `datacenter`
    * `datastore`
    * `networks`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `computeCluster` | `string` | computeCluster the absolute path of the vCenter cluster in which virtual machine will be located. The absolute path is of the form /<datacenter>/host/<cluster>. The maximum length of the path is 2048 characters. |
| `datacenter` | `string` | datacenter is the name of vCenter datacenter in which virtual machines will be located. The maximum length of the datacenter name is 80 characters. |
| `datastore` | `string` | datastore is the absolute path of the datastore in which the virtual machine is located. The absolute path is of the form /<datacenter>/datastore/<datastore> The maximum length of the path is 2048 characters. |
| `folder` | `string` | folder is the absolute path of the folder where virtual machines are located. The absolute path is of the form /<datacenter>/vm/<folder>. The maximum length of the path is 2048 characters. |
| `networks` | `array (string)` | networks is the list of port group network names within this failure domain. If feature gate VSphereMultiNetworks is enabled, up to 10 network adapters may be defined. 10 is the maximum number of virtual network devices which may be attached to a VM as defined by: <https://configmax.esp.vmware.com/guest?vmwareproduct=vSphere&release=vSphere%208.0&categories=1-0> The available networks (port groups) can be listed using `govc ls 'network/*'` Networks should be in the form of an absolute path: /<datacenter>/network/<portgroup>. |
| `resourcePool` | `string` | resourcePool is the absolute path of the resource pool where virtual machines will be created. The absolute path is of the form /<datacenter>/host/<cluster>/Resources/<resourcepool>. The maximum length of the path is 2048 characters. |
| `template` | `string` | template is the full inventory path of the virtual machine or template that will be cloned when creating new machines in this failure domain. The maximum length of the path is 2048 characters.  When omitted, the template will be calculated by the control plane machineset operator based on the region and zone defined in VSpherePlatformFailureDomainSpec. For example, for zone=zonea, region=region1, and infrastructure name=test, the template path would be calculated as /<datacenter>/vm/test-rhcos-region1-zonea. |

Show more

#### [18.1.35. .spec.platformSpec.vsphere.failureDomains[].zoneAffinity](#spec-platformspec-vsphere-failuredomains-zoneaffinity) Copy linkLink copied to clipboard!

Description
:   zoneAffinity holds the type of the zone and the hostGroup which vmGroup and the hostGroup names in vCenter corresponds to a vm-host group of type Virtual Machine and Host respectively. Is also contains the vmHostRule which is an affinity vm-host rule in vCenter.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hostGroup` | `object` | hostGroup holds the vmGroup and the hostGroup names in vCenter corresponds to a vm-host group of type Virtual Machine and Host respectively. Is also contains the vmHostRule which is an affinity vm-host rule in vCenter. |
| `type` | `string` | type determines the vSphere object type for a zone within this failure domain. Available types are ComputeCluster and HostGroup. When set to ComputeCluster, this means the vCenter cluster defined is the zone. When set to HostGroup, hostGroup must be configured with hostGroup, vmGroup and vmHostRule and this means the zone is defined by the grouping of those fields. |

Show more

#### [18.1.36. .spec.platformSpec.vsphere.failureDomains[].zoneAffinity.hostGroup](#spec-platformspec-vsphere-failuredomains-zoneaffinity-hostgroup) Copy linkLink copied to clipboard!

Description
:   hostGroup holds the vmGroup and the hostGroup names in vCenter corresponds to a vm-host group of type Virtual Machine and Host respectively. Is also contains the vmHostRule which is an affinity vm-host rule in vCenter.

Type
:   `object`

Required
:   * `hostGroup`
    * `vmGroup`
    * `vmHostRule`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hostGroup` | `string` | hostGroup is the name of the vm-host group of type host within vCenter for this failure domain. hostGroup is limited to 80 characters. This field is required when the VSphereFailureDomain ZoneType is HostGroup |
| `vmGroup` | `string` | vmGroup is the name of the vm-host group of type virtual machine within vCenter for this failure domain. vmGroup is limited to 80 characters. This field is required when the VSphereFailureDomain ZoneType is HostGroup |
| `vmHostRule` | `string` | vmHostRule is the name of the affinity vm-host rule within vCenter for this failure domain. vmHostRule is limited to 80 characters. This field is required when the VSphereFailureDomain ZoneType is HostGroup |

Show more

#### [18.1.37. .spec.platformSpec.vsphere.nodeNetworking](#spec-platformspec-vsphere-nodenetworking) Copy linkLink copied to clipboard!

Description
:   nodeNetworking contains the definition of internal and external network constraints for assigning the node’s networking. If this field is omitted, networking defaults to the legacy address selection behavior which is to only support a single address and return the first one found.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `external` | `object` | external represents the network configuration of the node that is externally routable. |
| `internal` | `object` | internal represents the network configuration of the node that is routable only within the cluster. |

Show more

#### [18.1.38. .spec.platformSpec.vsphere.nodeNetworking.external](#spec-platformspec-vsphere-nodenetworking-external) Copy linkLink copied to clipboard!

Description
:   external represents the network configuration of the node that is externally routable.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `excludeNetworkSubnetCidr` | `array (string)` | excludeNetworkSubnetCidr IP addresses in subnet ranges will be excluded when selecting the IP address from the VirtualMachine’s VM for use in the status.addresses fields. |
| `network` | `string` | network VirtualMachine’s VM Network names that will be used to when searching for status.addresses fields. Note that if internal.networkSubnetCIDR and external.networkSubnetCIDR are not set, then the vNIC associated to this network must only have a single IP address assigned to it. The available networks (port groups) can be listed using `govc ls 'network/*'` |
| `networkSubnetCidr` | `array (string)` | networkSubnetCidr IP address on VirtualMachine’s network interfaces included in the fields' CIDRs that will be used in respective status.addresses fields. |

Show more

#### [18.1.39. .spec.platformSpec.vsphere.nodeNetworking.internal](#spec-platformspec-vsphere-nodenetworking-internal) Copy linkLink copied to clipboard!

Description
:   internal represents the network configuration of the node that is routable only within the cluster.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `excludeNetworkSubnetCidr` | `array (string)` | excludeNetworkSubnetCidr IP addresses in subnet ranges will be excluded when selecting the IP address from the VirtualMachine’s VM for use in the status.addresses fields. |
| `network` | `string` | network VirtualMachine’s VM Network names that will be used to when searching for status.addresses fields. Note that if internal.networkSubnetCIDR and external.networkSubnetCIDR are not set, then the vNIC associated to this network must only have a single IP address assigned to it. The available networks (port groups) can be listed using `govc ls 'network/*'` |
| `networkSubnetCidr` | `array (string)` | networkSubnetCidr IP address on VirtualMachine’s network interfaces included in the fields' CIDRs that will be used in respective status.addresses fields. |

Show more

#### [18.1.40. .spec.platformSpec.vsphere.vcenters](#spec-platformspec-vsphere-vcenters) Copy linkLink copied to clipboard!

Description
:   vcenters holds the connection details for services to communicate with vCenter. Currently, only a single vCenter is supported, but in tech preview 3 vCenters are supported. Once the cluster has been installed, you are unable to change the current number of defined vCenters except in the case where the cluster has been upgraded from a version of OpenShift where the vsphere platform spec was not present. You may make modifications to the existing vCenters that are defined in the vcenters list in order to match with any added or modified failure domains.

Type
:   `array`

#### [18.1.41. .spec.platformSpec.vsphere.vcenters[]](#spec-platformspec-vsphere-vcenters-2) Copy linkLink copied to clipboard!

Description
:   VSpherePlatformVCenterSpec stores the vCenter connection fields. This is used by the vSphere CCM.

Type
:   `object`

Required
:   * `datacenters`
    * `server`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `datacenters` | `array (string)` | The vCenter Datacenters in which the RHCOS vm guests are located. This field will be used by the Cloud Controller Manager. Each datacenter listed here should be used within a topology. |
| `port` | `integer` | port is the TCP port that will be used to communicate to the vCenter endpoint. When omitted, this means the user has no opinion and it is up to the platform to choose a sensible default, which is subject to change over time. |
| `server` | `string` | server is the fully-qualified domain name or the IP address of the vCenter server. |

Show more

#### [18.1.42. .status](#status-14) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalURI` | `string` | apiServerInternalURL is a valid URI with scheme 'https', address and optionally a port (defaulting to 443). apiServerInternalURL can be used by components like kubelets, to contact the Kubernetes API server using the infrastructure provider rather than Kubernetes networking. |
| `apiServerURL` | `string` | apiServerURL is a valid URI with scheme 'https', address and optionally a port (defaulting to 443). apiServerURL can be used by components like the web console to tell users where to find the Kubernetes API. |
| `controlPlaneTopology` | `string` | controlPlaneTopology expresses the expectations for operands that normally run on control nodes. The default is 'HighlyAvailable', which represents the behavior operators have in a "normal" cluster. The 'SingleReplica' mode will be used in single-node deployments and the operators should not configure the operand for highly-available operation The 'External' mode indicates that the control plane is hosted externally to the cluster and that its components are not visible within the cluster. The 'HighlyAvailableArbiter' mode indicates that the control plane will consist of 2 control-plane nodes that run conventional services and 1 smaller sized arbiter node that runs a bare minimum of services to maintain quorum. |
| `cpuPartitioning` | `string` | cpuPartitioning expresses if CPU partitioning is a currently enabled feature in the cluster. CPU Partitioning means that this cluster can support partitioning workloads to specific CPU Sets. Valid values are "None" and "AllNodes". When omitted, the default value is "None". The default value of "None" indicates that no nodes will be setup with CPU partitioning. The "AllNodes" value indicates that all nodes have been setup with CPU partitioning, and can then be further configured via the PerformanceProfile API. |
| `etcdDiscoveryDomain` | `string` | etcdDiscoveryDomain is the domain used to fetch the SRV records for discovering etcd servers and clients. For more info: <https://github.com/etcd-io/etcd/blob/329be66e8b3f9e2e6af83c123ff89297e49ebd15/Documentation/op-guide/clustering.md#dns-discovery> deprecated: as of 4.7, this field is no longer set or honored. It will be removed in a future release. |
| `infrastructureName` | `string` | infrastructureName uniquely identifies a cluster with a human friendly name. Once set it should not be changed. Must be of max length 27 and must have only alphanumeric or hyphen characters. |
| `infrastructureTopology` | `string` | infrastructureTopology expresses the expectations for infrastructure services that do not run on control plane nodes, usually indicated by a node selector for a `role` value other than `master`. The default is 'HighlyAvailable', which represents the behavior operators have in a "normal" cluster. The 'SingleReplica' mode will be used in single-node deployments and the operators should not configure the operand for highly-available operation NOTE: External topology mode is not applicable for this field. |
| `platform` | `string` | platform is the underlying infrastructure provider for the cluster.  Deprecated: Use platformStatus.type instead. |
| `platformStatus` | `object` | platformStatus holds status information specific to the underlying infrastructure provider. |

Show more

#### [18.1.43. .status.platformStatus](#status-platformstatus) Copy linkLink copied to clipboard!

Description
:   platformStatus holds status information specific to the underlying infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `alibabaCloud` | `object` | alibabaCloud contains settings specific to the Alibaba Cloud infrastructure provider. |
| `aws` | `object` | aws contains settings specific to the Amazon Web Services infrastructure provider. |
| `azure` | `object` | azure contains settings specific to the Azure infrastructure provider. |
| `baremetal` | `object` | baremetal contains settings specific to the BareMetal platform. |
| `equinixMetal` | `object` | equinixMetal contains settings specific to the Equinix Metal infrastructure provider. |
| `external` | `object` | external contains settings specific to the generic External infrastructure provider. |
| `gcp` | `object` | gcp contains settings specific to the Google Cloud Platform infrastructure provider. |
| `ibmcloud` | `object` | ibmcloud contains settings specific to the IBMCloud infrastructure provider. |
| `kubevirt` | `object` | kubevirt contains settings specific to the kubevirt infrastructure provider. |
| `nutanix` | `object` | nutanix contains settings specific to the Nutanix infrastructure provider. |
| `openstack` | `object` | openstack contains settings specific to the OpenStack infrastructure provider. |
| `ovirt` | `object` | ovirt contains settings specific to the oVirt infrastructure provider. |
| `powervs` | `object` | powervs contains settings specific to the Power Systems Virtual Servers infrastructure provider. |
| `type` | `string` | type is the underlying infrastructure provider for the cluster. This value controls whether infrastructure automation such as service load balancers, dynamic volume provisioning, machine creation and deletion, and other integrations are enabled. If None, no infrastructure automation is enabled. Allowed values are "AWS", "Azure", "BareMetal", "GCP", "Libvirt", "OpenStack", "VSphere", "oVirt", "EquinixMetal", "PowerVS", "AlibabaCloud", "Nutanix" and "None". Individual components may not support all platforms, and must handle unrecognized platforms as None if they do not support that platform.  This value will be synced with to the `status.platform` and `status.platformStatus.type`. Currently this value cannot be changed once set. |
| `vsphere` | `object` | vsphere contains settings specific to the VSphere infrastructure provider. |

Show more

#### [18.1.44. .status.platformStatus.alibabaCloud](#status-platformstatus-alibabacloud) Copy linkLink copied to clipboard!

Description
:   alibabaCloud contains settings specific to the Alibaba Cloud infrastructure provider.

Type
:   `object`

Required
:   * `region`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `region` | `string` | region specifies the region for Alibaba Cloud resources created for the cluster. |
| `resourceGroupID` | `string` | resourceGroupID is the ID of the resource group for the cluster. |
| `resourceTags` | `array` | resourceTags is a list of additional tags to apply to Alibaba Cloud resources created for the cluster. |
| `resourceTags[]` | `object` | AlibabaCloudResourceTag is the set of tags to add to apply to resources. |

Show more

#### [18.1.45. .status.platformStatus.alibabaCloud.resourceTags](#status-platformstatus-alibabacloud-resourcetags) Copy linkLink copied to clipboard!

Description
:   resourceTags is a list of additional tags to apply to Alibaba Cloud resources created for the cluster.

Type
:   `array`

#### [18.1.46. .status.platformStatus.alibabaCloud.resourceTags[]](#status-platformstatus-alibabacloud-resourcetags-2) Copy linkLink copied to clipboard!

Description
:   AlibabaCloudResourceTag is the set of tags to add to apply to resources.

Type
:   `object`

Required
:   * `key`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key of the tag. |
| `value` | `string` | value is the value of the tag. |

Show more

#### [18.1.47. .status.platformStatus.aws](#status-platformstatus-aws) Copy linkLink copied to clipboard!

Description
:   aws contains settings specific to the Amazon Web Services infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `region` | `string` | region holds the default AWS region for new AWS resources created by the cluster. |
| `resourceTags` | `array` | resourceTags is a list of additional tags to apply to AWS resources created for the cluster. See <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html> for information on tagging AWS resources. AWS supports a maximum of 50 tags per resource. OpenShift reserves 25 tags for its use, leaving 25 tags available for the user. |
| `resourceTags[]` | `object` | AWSResourceTag is a tag to apply to AWS resources created for the cluster. |
| `serviceEndpoints` | `array` | serviceEndpoints list contains custom endpoints which will override default service endpoint of AWS Services. There must be only one ServiceEndpoint for a service. |
| `serviceEndpoints[]` | `object` | AWSServiceEndpoint store the configuration of a custom url to override existing defaults of AWS Services. |

Show more

#### [18.1.48. .status.platformStatus.aws.resourceTags](#status-platformstatus-aws-resourcetags) Copy linkLink copied to clipboard!

Description
:   resourceTags is a list of additional tags to apply to AWS resources created for the cluster. See <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html> for information on tagging AWS resources. AWS supports a maximum of 50 tags per resource. OpenShift reserves 25 tags for its use, leaving 25 tags available for the user.

Type
:   `array`

#### [18.1.49. .status.platformStatus.aws.resourceTags[]](#status-platformstatus-aws-resourcetags-2) Copy linkLink copied to clipboard!

Description
:   AWSResourceTag is a tag to apply to AWS resources created for the cluster.

Type
:   `object`

Required
:   * `key`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key sets the key of the AWS resource tag key-value pair. Key is required when defining an AWS resource tag. Key should consist of between 1 and 128 characters, and may contain only the set of alphanumeric characters, space (' '), '\_', '.', '/', '=', '+', '-', ':', and '@'. |
| `value` | `string` | value sets the value of the AWS resource tag key-value pair. Value is required when defining an AWS resource tag. Value should consist of between 1 and 256 characters, and may contain only the set of alphanumeric characters, space (' '), '\_', '.', '/', '=', '+', '-', ':', and '@'. Some AWS service do not support empty values. Since tags are added to resources in many services, the length of the tag value must meet the requirements of all services. |

Show more

#### [18.1.50. .status.platformStatus.aws.serviceEndpoints](#status-platformstatus-aws-serviceendpoints) Copy linkLink copied to clipboard!

Description
:   serviceEndpoints list contains custom endpoints which will override default service endpoint of AWS Services. There must be only one ServiceEndpoint for a service.

Type
:   `array`

#### [18.1.51. .status.platformStatus.aws.serviceEndpoints[]](#status-platformstatus-aws-serviceendpoints-2) Copy linkLink copied to clipboard!

Description
:   AWSServiceEndpoint store the configuration of a custom url to override existing defaults of AWS Services.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the AWS service. The list of all the service names can be found at <https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html> This must be provided and cannot be empty. |
| `url` | `string` | url is fully qualified URI with scheme https, that overrides the default generated endpoint for a client. This must be provided and cannot be empty. |

Show more

#### [18.1.52. .status.platformStatus.azure](#status-platformstatus-azure) Copy linkLink copied to clipboard!

Description
:   azure contains settings specific to the Azure infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `armEndpoint` | `string` | armEndpoint specifies a URL to use for resource management in non-soverign clouds such as Azure Stack. |
| `cloudLoadBalancerConfig` | `object` | cloudLoadBalancerConfig holds configuration related to DNS and cloud load balancers. It allows configuration of in-cluster DNS as an alternative to the platform default DNS implementation. When using the ClusterHosted DNS type, Load Balancer IP addresses must be provided for the API and internal API load balancers as well as the ingress load balancer. |
| `cloudName` | `string` | cloudName is the name of the Azure cloud environment which can be used to configure the Azure SDK with the appropriate Azure API endpoints. If empty, the value is equal to `AzurePublicCloud`. |
| `networkResourceGroupName` | `string` | networkResourceGroupName is the Resource Group for network resources like the Virtual Network and Subnets used by the cluster. If empty, the value is same as ResourceGroupName. |
| `resourceGroupName` | `string` | resourceGroupName is the Resource Group for new Azure resources created for the cluster. |
| `resourceTags` | `array` | resourceTags is a list of additional tags to apply to Azure resources created for the cluster. See <https://docs.microsoft.com/en-us/rest/api/resources/tags> for information on tagging Azure resources. Due to limitations on Automation, Content Delivery Network, DNS Azure resources, a maximum of 15 tags may be applied. OpenShift reserves 5 tags for internal use, allowing 10 tags for user configuration. |
| `resourceTags[]` | `object` | AzureResourceTag is a tag to apply to Azure resources created for the cluster. |

Show more

#### [18.1.53. .status.platformStatus.azure.cloudLoadBalancerConfig](#status-platformstatus-azure-cloudloadbalancerconfig) Copy linkLink copied to clipboard!

Description
:   cloudLoadBalancerConfig holds configuration related to DNS and cloud load balancers. It allows configuration of in-cluster DNS as an alternative to the platform default DNS implementation. When using the ClusterHosted DNS type, Load Balancer IP addresses must be provided for the API and internal API load balancers as well as the ingress load balancer.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterHosted` | `object` | clusterHosted holds the IP addresses of API, API-Int and Ingress Load Balancers on Cloud Platforms. The DNS solution hosted within the cluster use these IP addresses to provide resolution for API, API-Int and Ingress services. |
| `dnsType` | `string` | dnsType indicates the type of DNS solution in use within the cluster. Its default value of `PlatformDefault` indicates that the cluster’s DNS is the default provided by the cloud platform. It can be set to `ClusterHosted` to bypass the configuration of the cloud default DNS. In this mode, the cluster needs to provide a self-hosted DNS solution for the cluster’s installation to succeed. The cluster’s use of the cloud’s Load Balancers is unaffected by this setting. The value is immutable after it has been set at install time. Currently, there is no way for the customer to add additional DNS entries into the cluster hosted DNS. Enabling this functionality allows the user to start their own DNS solution outside the cluster after installation is complete. The customer would be responsible for configuring this custom DNS solution, and it can be run in addition to the in-cluster DNS solution. |

Show more

#### [18.1.54. .status.platformStatus.azure.cloudLoadBalancerConfig.clusterHosted](#status-platformstatus-azure-cloudloadbalancerconfig-clusterhosted) Copy linkLink copied to clipboard!

Description
:   clusterHosted holds the IP addresses of API, API-Int and Ingress Load Balancers on Cloud Platforms. The DNS solution hosted within the cluster use these IP addresses to provide resolution for API, API-Int and Ingress services.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiIntLoadBalancerIPs` | `array (string)` | apiIntLoadBalancerIPs holds Load Balancer IPs for the internal API service. These Load Balancer IP addresses can be IPv4 and/or IPv6 addresses. Entries in the apiIntLoadBalancerIPs must be unique. A maximum of 16 IP addresses are permitted. |
| `apiLoadBalancerIPs` | `array (string)` | apiLoadBalancerIPs holds Load Balancer IPs for the API service. These Load Balancer IP addresses can be IPv4 and/or IPv6 addresses. Could be empty for private clusters. Entries in the apiLoadBalancerIPs must be unique. A maximum of 16 IP addresses are permitted. |
| `ingressLoadBalancerIPs` | `array (string)` | ingressLoadBalancerIPs holds IPs for Ingress Load Balancers. These Load Balancer IP addresses can be IPv4 and/or IPv6 addresses. Entries in the ingressLoadBalancerIPs must be unique. A maximum of 16 IP addresses are permitted. |

Show more

#### [18.1.55. .status.platformStatus.azure.resourceTags](#status-platformstatus-azure-resourcetags) Copy linkLink copied to clipboard!

Description
:   resourceTags is a list of additional tags to apply to Azure resources created for the cluster. See <https://docs.microsoft.com/en-us/rest/api/resources/tags> for information on tagging Azure resources. Due to limitations on Automation, Content Delivery Network, DNS Azure resources, a maximum of 15 tags may be applied. OpenShift reserves 5 tags for internal use, allowing 10 tags for user configuration.

Type
:   `array`

#### [18.1.56. .status.platformStatus.azure.resourceTags[]](#status-platformstatus-azure-resourcetags-2) Copy linkLink copied to clipboard!

Description
:   AzureResourceTag is a tag to apply to Azure resources created for the cluster.

Type
:   `object`

Required
:   * `key`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key part of the tag. A tag key can have a maximum of 128 characters and cannot be empty. Key must begin with a letter, end with a letter, number or underscore, and must contain only alphanumeric characters and the following special characters `_ . -`. |
| `value` | `string` | value is the value part of the tag. A tag value can have a maximum of 256 characters and cannot be empty. Value must contain only alphanumeric characters and the following special characters `_ + , - . / : ; < = > ? @`. |

Show more

#### [18.1.57. .status.platformStatus.baremetal](#status-platformstatus-baremetal) Copy linkLink copied to clipboard!

Description
:   baremetal contains settings specific to the BareMetal platform.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers.  Deprecated: Use APIServerInternalIPs instead. |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IPs otherwise only one. |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names.  Deprecated: Use IngressIPs instead. |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IPs otherwise only one. |
| `loadBalancer` | `object` | loadBalancer defines how the load balancer used by the cluster is configured. |
| `machineNetworks` | `array (string)` | machineNetworks are IP networks used to connect all the OpenShift cluster nodes. |
| `nodeDNSIP` | `string` | nodeDNSIP is the IP address for the internal DNS used by the nodes. Unlike the one managed by the DNS operator, `NodeDNSIP` provides name resolution for the nodes themselves. There is no DNS-as-a-service for BareMetal deployments. In order to minimize necessary changes to the datacenter DNS, a DNS service is hosted as a static pod to serve those hostnames to the nodes in the cluster. |

Show more

#### [18.1.58. .status.platformStatus.baremetal.loadBalancer](#status-platformstatus-baremetal-loadbalancer) Copy linkLink copied to clipboard!

Description
:   loadBalancer defines how the load balancer used by the cluster is configured.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type defines the type of load balancer used by the cluster on BareMetal platform which can be a user-managed or openshift-managed load balancer that is to be used for the OpenShift API and Ingress endpoints. When set to OpenShiftManagedDefault the static pods in charge of API and Ingress traffic load-balancing defined in the machine config operator will be deployed. When set to UserManaged these static pods will not be deployed and it is expected that the load balancer is configured out of band by the deployer. When omitted, this means no opinion and the platform is left to choose a reasonable default. The default value is OpenShiftManagedDefault. |

Show more

#### [18.1.59. .status.platformStatus.equinixMetal](#status-platformstatus-equinixmetal) Copy linkLink copied to clipboard!

Description
:   equinixMetal contains settings specific to the Equinix Metal infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers. |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names. |

Show more

#### [18.1.60. .status.platformStatus.external](#status-platformstatus-external) Copy linkLink copied to clipboard!

Description
:   external contains settings specific to the generic External infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cloudControllerManager` | `object` | cloudControllerManager contains settings specific to the external Cloud Controller Manager (a.k.a. CCM or CPI). When omitted, new nodes will be not tainted and no extra initialization from the cloud controller manager is expected. |

Show more

#### [18.1.61. .status.platformStatus.external.cloudControllerManager](#status-platformstatus-external-cloudcontrollermanager) Copy linkLink copied to clipboard!

Description
:   cloudControllerManager contains settings specific to the external Cloud Controller Manager (a.k.a. CCM or CPI). When omitted, new nodes will be not tainted and no extra initialization from the cloud controller manager is expected.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `state` | `string` | state determines whether or not an external Cloud Controller Manager is expected to be installed within the cluster. <https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/#running-cloud-controller-manager>  Valid values are "External", "None" and omitted. When set to "External", new nodes will be tainted as uninitialized when created, preventing them from running workloads until they are initialized by the cloud controller manager. When omitted or set to "None", new nodes will be not tainted and no extra initialization from the cloud controller manager is expected. |

Show more

#### [18.1.62. .status.platformStatus.gcp](#status-platformstatus-gcp) Copy linkLink copied to clipboard!

Description
:   gcp contains settings specific to the Google Cloud Platform infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cloudLoadBalancerConfig` | `` | cloudLoadBalancerConfig holds configuration related to DNS and cloud load balancers. It allows configuration of in-cluster DNS as an alternative to the platform default DNS implementation. When using the ClusterHosted DNS type, Load Balancer IP addresses must be provided for the API and internal API load balancers as well as the ingress load balancer. |
| `projectID` | `string` | resourceGroupName is the Project ID for new GCP resources created for the cluster. |
| `region` | `string` | region holds the region for new GCP resources created for the cluster. |
| `resourceLabels` | `array` | resourceLabels is a list of additional labels to apply to GCP resources created for the cluster. See <https://cloud.google.com/compute/docs/labeling-resources> for information on labeling GCP resources. GCP supports a maximum of 64 labels per resource. OpenShift reserves 32 labels for internal use, allowing 32 labels for user configuration. |
| `resourceLabels[]` | `object` | GCPResourceLabel is a label to apply to GCP resources created for the cluster. |
| `resourceTags` | `array` | resourceTags is a list of additional tags to apply to GCP resources created for the cluster. See <https://cloud.google.com/resource-manager/docs/tags/tags-overview> for information on tagging GCP resources. GCP supports a maximum of 50 tags per resource. |
| `resourceTags[]` | `object` | GCPResourceTag is a tag to apply to GCP resources created for the cluster. |

Show more

#### [18.1.63. .status.platformStatus.gcp.resourceLabels](#status-platformstatus-gcp-resourcelabels) Copy linkLink copied to clipboard!

Description
:   resourceLabels is a list of additional labels to apply to GCP resources created for the cluster. See <https://cloud.google.com/compute/docs/labeling-resources> for information on labeling GCP resources. GCP supports a maximum of 64 labels per resource. OpenShift reserves 32 labels for internal use, allowing 32 labels for user configuration.

Type
:   `array`

#### [18.1.64. .status.platformStatus.gcp.resourceLabels[]](#status-platformstatus-gcp-resourcelabels-2) Copy linkLink copied to clipboard!

Description
:   GCPResourceLabel is a label to apply to GCP resources created for the cluster.

Type
:   `object`

Required
:   * `key`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key part of the label. A label key can have a maximum of 63 characters and cannot be empty. Label key must begin with a lowercase letter, and must contain only lowercase letters, numeric characters, and the following special characters `_-`. Label key must not have the reserved prefixes `kubernetes-io` and `openshift-io`. |
| `value` | `string` | value is the value part of the label. A label value can have a maximum of 63 characters and cannot be empty. Value must contain only lowercase letters, numeric characters, and the following special characters `_-`. |

Show more

#### [18.1.65. .status.platformStatus.gcp.resourceTags](#status-platformstatus-gcp-resourcetags) Copy linkLink copied to clipboard!

Description
:   resourceTags is a list of additional tags to apply to GCP resources created for the cluster. See <https://cloud.google.com/resource-manager/docs/tags/tags-overview> for information on tagging GCP resources. GCP supports a maximum of 50 tags per resource.

Type
:   `array`

#### [18.1.66. .status.platformStatus.gcp.resourceTags[]](#status-platformstatus-gcp-resourcetags-2) Copy linkLink copied to clipboard!

Description
:   GCPResourceTag is a tag to apply to GCP resources created for the cluster.

Type
:   `object`

Required
:   * `key`
    * `parentID`
    * `value`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the key part of the tag. A tag key can have a maximum of 63 characters and cannot be empty. Tag key must begin and end with an alphanumeric character, and must contain only uppercase, lowercase alphanumeric characters, and the following special characters `._-`. |
| `parentID` | `string` | parentID is the ID of the hierarchical resource where the tags are defined, e.g. at the Organization or the Project level. To find the Organization or Project ID refer to the following pages: <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>, <https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects>. An OrganizationID must consist of decimal numbers, and cannot have leading zeroes. A ProjectID must be 6 to 30 characters in length, can only contain lowercase letters, numbers, and hyphens, and must start with a letter, and cannot end with a hyphen. |
| `value` | `string` | value is the value part of the tag. A tag value can have a maximum of 63 characters and cannot be empty. Tag value must begin and end with an alphanumeric character, and must contain only uppercase, lowercase alphanumeric characters, and the following special characters `_-.@%=+:,*#&(){}[]` and spaces. |

Show more

#### [18.1.67. .status.platformStatus.ibmcloud](#status-platformstatus-ibmcloud) Copy linkLink copied to clipboard!

Description
:   ibmcloud contains settings specific to the IBMCloud infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cisInstanceCRN` | `string` | cisInstanceCRN is the CRN of the Cloud Internet Services instance managing the DNS zone for the cluster’s base domain |
| `dnsInstanceCRN` | `string` | dnsInstanceCRN is the CRN of the DNS Services instance managing the DNS zone for the cluster’s base domain |
| `location` | `string` | location is where the cluster has been deployed |
| `providerType` | `string` | providerType indicates the type of cluster that was created |
| `resourceGroupName` | `string` | resourceGroupName is the Resource Group for new IBMCloud resources created for the cluster. |
| `serviceEndpoints` | `array` | serviceEndpoints is a list of custom endpoints which will override the default service endpoints of an IBM service. These endpoints are used by components within the cluster when trying to reach the IBM Cloud Services that have been overridden. The CCCMO reads in the IBMCloudPlatformSpec and validates each endpoint is resolvable. Once validated, the cloud config and IBMCloudPlatformStatus are updated to reflect the same custom endpoints. |
| `serviceEndpoints[]` | `object` | IBMCloudServiceEndpoint stores the configuration of a custom url to override existing defaults of IBM Cloud Services. |

Show more

#### [18.1.68. .status.platformStatus.ibmcloud.serviceEndpoints](#status-platformstatus-ibmcloud-serviceendpoints) Copy linkLink copied to clipboard!

Description
:   serviceEndpoints is a list of custom endpoints which will override the default service endpoints of an IBM service. These endpoints are used by components within the cluster when trying to reach the IBM Cloud Services that have been overridden. The CCCMO reads in the IBMCloudPlatformSpec and validates each endpoint is resolvable. Once validated, the cloud config and IBMCloudPlatformStatus are updated to reflect the same custom endpoints.

Type
:   `array`

#### [18.1.69. .status.platformStatus.ibmcloud.serviceEndpoints[]](#status-platformstatus-ibmcloud-serviceendpoints-2) Copy linkLink copied to clipboard!

Description
:   IBMCloudServiceEndpoint stores the configuration of a custom url to override existing defaults of IBM Cloud Services.

Type
:   `object`

Required
:   * `name`
    * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the IBM Cloud service. Possible values are: CIS, COS, COSConfig, DNSServices, GlobalCatalog, GlobalSearch, GlobalTagging, HyperProtect, IAM, KeyProtect, ResourceController, ResourceManager, or VPC. For example, the IBM Cloud Private IAM service could be configured with the service `name` of `IAM` and `url` of `https://private.iam.cloud.ibm.com` Whereas the IBM Cloud Private VPC service for US South (Dallas) could be configured with the service `name` of `VPC` and `url` of `https://us.south.private.iaas.cloud.ibm.com` |
| `url` | `string` | url is fully qualified URI with scheme https, that overrides the default generated endpoint for a client. This must be provided and cannot be empty. The path must follow the pattern /v[0,9]+ or /api/v[0,9]+ |

Show more

#### [18.1.70. .status.platformStatus.kubevirt](#status-platformstatus-kubevirt) Copy linkLink copied to clipboard!

Description
:   kubevirt contains settings specific to the kubevirt infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers. |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names. |

Show more

#### [18.1.71. .status.platformStatus.nutanix](#status-platformstatus-nutanix) Copy linkLink copied to clipboard!

Description
:   nutanix contains settings specific to the Nutanix infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers.  Deprecated: Use APIServerInternalIPs instead. |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IPs otherwise only one. |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names.  Deprecated: Use IngressIPs instead. |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IPs otherwise only one. |
| `loadBalancer` | `object` | loadBalancer defines how the load balancer used by the cluster is configured. |

Show more

#### [18.1.72. .status.platformStatus.nutanix.loadBalancer](#status-platformstatus-nutanix-loadbalancer) Copy linkLink copied to clipboard!

Description
:   loadBalancer defines how the load balancer used by the cluster is configured.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type defines the type of load balancer used by the cluster on Nutanix platform which can be a user-managed or openshift-managed load balancer that is to be used for the OpenShift API and Ingress endpoints. When set to OpenShiftManagedDefault the static pods in charge of API and Ingress traffic load-balancing defined in the machine config operator will be deployed. When set to UserManaged these static pods will not be deployed and it is expected that the load balancer is configured out of band by the deployer. When omitted, this means no opinion and the platform is left to choose a reasonable default. The default value is OpenShiftManagedDefault. |

Show more

#### [18.1.73. .status.platformStatus.openstack](#status-platformstatus-openstack) Copy linkLink copied to clipboard!

Description
:   openstack contains settings specific to the OpenStack infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers.  Deprecated: Use APIServerInternalIPs instead. |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IPs otherwise only one. |
| `cloudName` | `string` | cloudName is the name of the desired OpenStack cloud in the client configuration file (`clouds.yaml`). |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names.  Deprecated: Use IngressIPs instead. |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IPs otherwise only one. |
| `loadBalancer` | `object` | loadBalancer defines how the load balancer used by the cluster is configured. |
| `machineNetworks` | `array (string)` | machineNetworks are IP networks used to connect all the OpenShift cluster nodes. |
| `nodeDNSIP` | `string` | nodeDNSIP is the IP address for the internal DNS used by the nodes. Unlike the one managed by the DNS operator, `NodeDNSIP` provides name resolution for the nodes themselves. There is no DNS-as-a-service for OpenStack deployments. In order to minimize necessary changes to the datacenter DNS, a DNS service is hosted as a static pod to serve those hostnames to the nodes in the cluster. |

Show more

#### [18.1.74. .status.platformStatus.openstack.loadBalancer](#status-platformstatus-openstack-loadbalancer) Copy linkLink copied to clipboard!

Description
:   loadBalancer defines how the load balancer used by the cluster is configured.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type defines the type of load balancer used by the cluster on OpenStack platform which can be a user-managed or openshift-managed load balancer that is to be used for the OpenShift API and Ingress endpoints. When set to OpenShiftManagedDefault the static pods in charge of API and Ingress traffic load-balancing defined in the machine config operator will be deployed. When set to UserManaged these static pods will not be deployed and it is expected that the load balancer is configured out of band by the deployer. When omitted, this means no opinion and the platform is left to choose a reasonable default. The default value is OpenShiftManagedDefault. |

Show more

#### [18.1.75. .status.platformStatus.ovirt](#status-platformstatus-ovirt) Copy linkLink copied to clipboard!

Description
:   ovirt contains settings specific to the oVirt infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers.  Deprecated: Use APIServerInternalIPs instead. |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IPs otherwise only one. |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names.  Deprecated: Use IngressIPs instead. |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IPs otherwise only one. |
| `loadBalancer` | `object` | loadBalancer defines how the load balancer used by the cluster is configured. |
| `nodeDNSIP` | `string` | deprecated: as of 4.6, this field is no longer set or honored. It will be removed in a future release. |

Show more

#### [18.1.76. .status.platformStatus.ovirt.loadBalancer](#status-platformstatus-ovirt-loadbalancer) Copy linkLink copied to clipboard!

Description
:   loadBalancer defines how the load balancer used by the cluster is configured.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type defines the type of load balancer used by the cluster on Ovirt platform which can be a user-managed or openshift-managed load balancer that is to be used for the OpenShift API and Ingress endpoints. When set to OpenShiftManagedDefault the static pods in charge of API and Ingress traffic load-balancing defined in the machine config operator will be deployed. When set to UserManaged these static pods will not be deployed and it is expected that the load balancer is configured out of band by the deployer. When omitted, this means no opinion and the platform is left to choose a reasonable default. The default value is OpenShiftManagedDefault. |

Show more

#### [18.1.77. .status.platformStatus.powervs](#status-platformstatus-powervs) Copy linkLink copied to clipboard!

Description
:   powervs contains settings specific to the Power Systems Virtual Servers infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cisInstanceCRN` | `string` | cisInstanceCRN is the CRN of the Cloud Internet Services instance managing the DNS zone for the cluster’s base domain |
| `dnsInstanceCRN` | `string` | dnsInstanceCRN is the CRN of the DNS Services instance managing the DNS zone for the cluster’s base domain |
| `region` | `string` | region holds the default Power VS region for new Power VS resources created by the cluster. |
| `resourceGroup` | `string` | resourceGroup is the resource group name for new IBMCloud resources created for a cluster. The resource group specified here will be used by cluster-image-registry-operator to set up a COS Instance in IBMCloud for the cluster registry. More about resource groups can be found here: <https://cloud.ibm.com/docs/account?topic=account-rgs>. When omitted, the image registry operator won’t be able to configure storage, which results in the image registry cluster operator not being in an available state. |
| `serviceEndpoints` | `array` | serviceEndpoints is a list of custom endpoints which will override the default service endpoints of a Power VS service. |
| `serviceEndpoints[]` | `object` | PowervsServiceEndpoint stores the configuration of a custom url to override existing defaults of PowerVS Services. |
| `zone` | `string` | zone holds the default zone for the new Power VS resources created by the cluster. Note: Currently only single-zone OCP clusters are supported |

Show more

#### [18.1.78. .status.platformStatus.powervs.serviceEndpoints](#status-platformstatus-powervs-serviceendpoints) Copy linkLink copied to clipboard!

Description
:   serviceEndpoints is a list of custom endpoints which will override the default service endpoints of a Power VS service.

Type
:   `array`

#### [18.1.79. .status.platformStatus.powervs.serviceEndpoints[]](#status-platformstatus-powervs-serviceendpoints-2) Copy linkLink copied to clipboard!

Description
:   PowervsServiceEndpoint stores the configuration of a custom url to override existing defaults of PowerVS Services.

Type
:   `object`

Required
:   * `name`
    * `url`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the name of the Power VS service. Few of the services are IAM - <https://cloud.ibm.com/apidocs/iam-identity-token-api> ResourceController - <https://cloud.ibm.com/apidocs/resource-controller/resource-controller> Power Cloud - <https://cloud.ibm.com/apidocs/power-cloud> |
| `url` | `string` | url is fully qualified URI with scheme https, that overrides the default generated endpoint for a client. This must be provided and cannot be empty. |

Show more

#### [18.1.80. .status.platformStatus.vsphere](#status-platformstatus-vsphere) Copy linkLink copied to clipboard!

Description
:   vsphere contains settings specific to the VSphere infrastructure provider.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiServerInternalIP` | `string` | apiServerInternalIP is an IP address to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. It is the IP that the Infrastructure.status.apiServerInternalURI points to. It is the IP for a self-hosted load balancer in front of the API servers.  Deprecated: Use APIServerInternalIPs instead. |
| `apiServerInternalIPs` | `array (string)` | apiServerInternalIPs are the IP addresses to contact the Kubernetes API server that can be used by components inside the cluster, like kubelets using the infrastructure rather than Kubernetes networking. These are the IPs for a self-hosted load balancer in front of the API servers. In dual stack clusters this list contains two IPs otherwise only one. |
| `ingressIP` | `string` | ingressIP is an external IP which routes to the default ingress controller. The IP is a suitable target of a wildcard DNS record used to resolve default route host names.  Deprecated: Use IngressIPs instead. |
| `ingressIPs` | `array (string)` | ingressIPs are the external IPs which route to the default ingress controller. The IPs are suitable targets of a wildcard DNS record used to resolve default route host names. In dual stack clusters this list contains two IPs otherwise only one. |
| `loadBalancer` | `object` | loadBalancer defines how the load balancer used by the cluster is configured. |
| `machineNetworks` | `array (string)` | machineNetworks are IP networks used to connect all the OpenShift cluster nodes. |
| `nodeDNSIP` | `string` | nodeDNSIP is the IP address for the internal DNS used by the nodes. Unlike the one managed by the DNS operator, `NodeDNSIP` provides name resolution for the nodes themselves. There is no DNS-as-a-service for vSphere deployments. In order to minimize necessary changes to the datacenter DNS, a DNS service is hosted as a static pod to serve those hostnames to the nodes in the cluster. |

Show more

#### [18.1.81. .status.platformStatus.vsphere.loadBalancer](#status-platformstatus-vsphere-loadbalancer) Copy linkLink copied to clipboard!

Description
:   loadBalancer defines how the load balancer used by the cluster is configured.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type defines the type of load balancer used by the cluster on VSphere platform which can be a user-managed or openshift-managed load balancer that is to be used for the OpenShift API and Ingress endpoints. When set to OpenShiftManagedDefault the static pods in charge of API and Ingress traffic load-balancing defined in the machine config operator will be deployed. When set to UserManaged these static pods will not be deployed and it is expected that the load balancer is configured out of band by the deployer. When omitted, this means no opinion and the platform is left to choose a reasonable default. The default value is OpenShiftManagedDefault. |

Show more

### [18.2. API endpoints](#api-endpoints-17) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/infrastructures`

  + `DELETE`: delete collection of Infrastructure
  + `GET`: list objects of kind Infrastructure
  + `POST`: create an Infrastructure
* `/apis/config.openshift.io/v1/infrastructures/{name}`

  + `DELETE`: delete an Infrastructure
  + `GET`: read the specified Infrastructure
  + `PATCH`: partially update the specified Infrastructure
  + `PUT`: replace the specified Infrastructure
* `/apis/config.openshift.io/v1/infrastructures/{name}/status`

  + `GET`: read status of the specified Infrastructure
  + `PATCH`: partially update status of the specified Infrastructure
  + `PUT`: replace status of the specified Infrastructure

#### [18.2.1. /apis/config.openshift.io/v1/infrastructures](#apisconfig-openshift-iov1infrastructures) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Infrastructure

Expand

Table 18.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Infrastructure

Expand

Table 18.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`InfrastructureList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-InfrastructureList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an Infrastructure

Expand

Table 18.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 18.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 18.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 201 - Created | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [18.2.2. /apis/config.openshift.io/v1/infrastructures/{name}](#apisconfig-openshift-iov1infrastructuresname) Copy linkLink copied to clipboard!

Expand

Table 18.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Infrastructure |

Show more

HTTP method
:   `DELETE`

Description
:   delete an Infrastructure

Expand

Table 18.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 18.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Infrastructure

Expand

Table 18.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Infrastructure

Expand

Table 18.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 18.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Infrastructure

Expand

Table 18.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 18.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 18.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 201 - Created | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [18.2.3. /apis/config.openshift.io/v1/infrastructures/{name}/status](#apisconfig-openshift-iov1infrastructuresnamestatus) Copy linkLink copied to clipboard!

Expand

Table 18.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Infrastructure |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Infrastructure

Expand

Table 18.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Infrastructure

Expand

Table 18.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 18.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Infrastructure

Expand

Table 18.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 18.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 18.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 201 - Created | [`Infrastructure`](#infrastructure-config-openshift-io-v1 "Chapter 18. Infrastructure [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 19. Ingress [config.openshift.io/v1]](#ingress-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Ingress holds cluster-wide information about ingress, including the default ingress domain used for routes. The canonical name is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [19.1. Specification](#specification-18) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [19.1.1. .spec](#spec-18) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `appsDomain` | `string` | appsDomain is an optional domain to use instead of the one specified in the domain field when a Route is created without specifying an explicit host. If appsDomain is nonempty, this value is used to generate default host values for Route. Unlike domain, appsDomain may be modified after installation. This assumes a new ingresscontroller has been setup with a wildcard certificate. |
| `componentRoutes` | `array` | componentRoutes is an optional list of routes that are managed by OpenShift components that a cluster-admin is able to configure the hostname and serving certificate for. The namespace and name of each route in this list should match an existing entry in the status.componentRoutes list.  To determine the set of configurable Routes, look at namespace and name of entries in the .status.componentRoutes list, where participating operators write the status of configurable routes. |
| `componentRoutes[]` | `object` | ComponentRouteSpec allows for configuration of a route’s hostname and serving certificate. |
| `domain` | `string` | domain is used to generate a default host name for a route when the route’s host name is empty. The generated host name will follow this pattern: "<route-name>.<route-namespace>.<domain>".  It is also used as the default wildcard domain suffix for ingress. The default ingresscontroller domain will follow this pattern: "\*.<domain>".  Once set, changing domain is not currently supported. |
| `loadBalancer` | `object` | loadBalancer contains the load balancer details in general which are not only specific to the underlying infrastructure provider of the current cluster and are required for Ingress Controller to work on OpenShift. |
| `requiredHSTSPolicies` | `array` | requiredHSTSPolicies specifies HSTS policies that are required to be set on newly created or updated routes matching the domainPattern/s and namespaceSelector/s that are specified in the policy. Each requiredHSTSPolicy must have at least a domainPattern and a maxAge to validate a route HSTS Policy route annotation, and affect route admission.  A candidate route is checked for HSTS Policies if it has the HSTS Policy route annotation: "haproxy.router.openshift.io/hsts\_header" E.g. haproxy.router.openshift.io/hsts\_header: max-age=31536000;preload;includeSubDomains  - For each candidate route, if it matches a requiredHSTSPolicy domainPattern and optional namespaceSelector, then the maxAge, preloadPolicy, and includeSubdomainsPolicy must be valid to be admitted. Otherwise, the route is rejected. - The first match, by domainPattern and optional namespaceSelector, in the ordering of the RequiredHSTSPolicies determines the route’s admission status. - If the candidate route doesn’t match any requiredHSTSPolicy domainPattern and optional namespaceSelector, then it may use any HSTS Policy annotation.  The HSTS policy configuration may be changed after routes have already been created. An update to a previously admitted route may then fail if the updated route does not conform to the updated HSTS policy configuration. However, changing the HSTS policy configuration will not cause a route that is already admitted to stop working.  Note that if there are no RequiredHSTSPolicies, any HSTS Policy annotation on the route is valid. |
| `requiredHSTSPolicies[]` | `object` |  |

Show more

#### [19.1.2. .spec.componentRoutes](#spec-componentroutes) Copy linkLink copied to clipboard!

Description
:   componentRoutes is an optional list of routes that are managed by OpenShift components that a cluster-admin is able to configure the hostname and serving certificate for. The namespace and name of each route in this list should match an existing entry in the status.componentRoutes list.

    To determine the set of configurable Routes, look at namespace and name of entries in the .status.componentRoutes list, where participating operators write the status of configurable routes.

Type
:   `array`

#### [19.1.3. .spec.componentRoutes[]](#spec-componentroutes-2) Copy linkLink copied to clipboard!

Description
:   ComponentRouteSpec allows for configuration of a route’s hostname and serving certificate.

Type
:   `object`

Required
:   * `hostname`
    * `name`
    * `namespace`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hostname` | `string` | hostname is the hostname that should be used by the route. |
| `name` | `string` | name is the logical name of the route to customize.  The namespace and name of this componentRoute must match a corresponding entry in the list of status.componentRoutes if the route is to be customized. |
| `namespace` | `string` | namespace is the namespace of the route to customize.  The namespace and name of this componentRoute must match a corresponding entry in the list of status.componentRoutes if the route is to be customized. |
| `servingCertKeyPairSecret` | `object` | servingCertKeyPairSecret is a reference to a secret of type `kubernetes.io/tls` in the openshift-config namespace. The serving cert/key pair must match and will be used by the operator to fulfill the intent of serving with this name. If the custom hostname uses the default routing suffix of the cluster, the Secret specification for a serving certificate will not be needed. |

Show more

#### [19.1.4. .spec.componentRoutes[].servingCertKeyPairSecret](#spec-componentroutes-servingcertkeypairsecret) Copy linkLink copied to clipboard!

Description
:   servingCertKeyPairSecret is a reference to a secret of type `kubernetes.io/tls` in the openshift-config namespace. The serving cert/key pair must match and will be used by the operator to fulfill the intent of serving with this name. If the custom hostname uses the default routing suffix of the cluster, the Secret specification for a serving certificate will not be needed.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [19.1.5. .spec.loadBalancer](#spec-loadbalancer) Copy linkLink copied to clipboard!

Description
:   loadBalancer contains the load balancer details in general which are not only specific to the underlying infrastructure provider of the current cluster and are required for Ingress Controller to work on OpenShift.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `platform` | `object` | platform holds configuration specific to the underlying infrastructure provider for the ingress load balancers. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. |

Show more

#### [19.1.6. .spec.loadBalancer.platform](#spec-loadbalancer-platform) Copy linkLink copied to clipboard!

Description
:   platform holds configuration specific to the underlying infrastructure provider for the ingress load balancers. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `aws` | `object` | aws contains settings specific to the Amazon Web Services infrastructure provider. |
| `type` | `string` | type is the underlying infrastructure provider for the cluster. Allowed values are "AWS", "Azure", "BareMetal", "GCP", "Libvirt", "OpenStack", "VSphere", "oVirt", "KubeVirt", "EquinixMetal", "PowerVS", "AlibabaCloud", "Nutanix" and "None". Individual components may not support all platforms, and must handle unrecognized platforms as None if they do not support that platform. |

Show more

#### [19.1.7. .spec.loadBalancer.platform.aws](#spec-loadbalancer-platform-aws) Copy linkLink copied to clipboard!

Description
:   aws contains settings specific to the Amazon Web Services infrastructure provider.

Type
:   `object`

Required
:   * `type`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` | type allows user to set a load balancer type. When this field is set the default ingresscontroller will get created using the specified LBType. If this field is not set then the default ingress controller of LBType Classic will be created. Valid values are:  \* "Classic": A Classic Load Balancer that makes routing decisions at either the transport layer (TCP/SSL) or the application layer (HTTP/HTTPS). See the following for additional details:  <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#clb>  \* "NLB": A Network Load Balancer that makes routing decisions at the transport layer (TCP/SSL). See the following for additional details:  <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-types.html#nlb> |

Show more

#### [19.1.8. .spec.requiredHSTSPolicies](#spec-requiredhstspolicies) Copy linkLink copied to clipboard!

Description
:   requiredHSTSPolicies specifies HSTS policies that are required to be set on newly created or updated routes matching the domainPattern/s and namespaceSelector/s that are specified in the policy. Each requiredHSTSPolicy must have at least a domainPattern and a maxAge to validate a route HSTS Policy route annotation, and affect route admission.

    A candidate route is checked for HSTS Policies if it has the HSTS Policy route annotation: "haproxy.router.openshift.io/hsts\_header" E.g. haproxy.router.openshift.io/hsts\_header: max-age=31536000;preload;includeSubDomains

    * For each candidate route, if it matches a requiredHSTSPolicy domainPattern and optional namespaceSelector, then the maxAge, preloadPolicy, and includeSubdomainsPolicy must be valid to be admitted. Otherwise, the route is rejected.
    * The first match, by domainPattern and optional namespaceSelector, in the ordering of the RequiredHSTSPolicies determines the route’s admission status.
    * If the candidate route doesn’t match any requiredHSTSPolicy domainPattern and optional namespaceSelector, then it may use any HSTS Policy annotation.

    The HSTS policy configuration may be changed after routes have already been created. An update to a previously admitted route may then fail if the updated route does not conform to the updated HSTS policy configuration. However, changing the HSTS policy configuration will not cause a route that is already admitted to stop working.

    Note that if there are no RequiredHSTSPolicies, any HSTS Policy annotation on the route is valid.

Type
:   `array`

#### [19.1.9. .spec.requiredHSTSPolicies[]](#spec-requiredhstspolicies-2) Copy linkLink copied to clipboard!

Description

Type
:   `object`

Required
:   * `domainPatterns`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `domainPatterns` | `array (string)` | domainPatterns is a list of domains for which the desired HSTS annotations are required. If domainPatterns is specified and a route is created with a spec.host matching one of the domains, the route must specify the HSTS Policy components described in the matching RequiredHSTSPolicy.  The use of wildcards is allowed like this: **.foo.com matches everything under foo.com. foo.com only matches foo.com, so to cover foo.com and everything under it, you must specify \*both**. |
| `includeSubDomainsPolicy` | `string` | includeSubDomainsPolicy means the HSTS Policy should apply to any subdomains of the host’s domain name. Thus, for the host bar.foo.com, if includeSubDomainsPolicy was set to RequireIncludeSubDomains: - the host app.bar.foo.com would inherit the HSTS Policy of bar.foo.com - the host bar.foo.com would inherit the HSTS Policy of bar.foo.com - the host foo.com would NOT inherit the HSTS Policy of bar.foo.com - the host def.foo.com would NOT inherit the HSTS Policy of bar.foo.com |
| `maxAge` | `object` | maxAge is the delta time range in seconds during which hosts are regarded as HSTS hosts. If set to 0, it negates the effect, and hosts are removed as HSTS hosts. If set to 0 and includeSubdomains is specified, all subdomains of the host are also removed as HSTS hosts. maxAge is a time-to-live value, and if this policy is not refreshed on a client, the HSTS policy will eventually expire on that client. |
| `namespaceSelector` | `object` | namespaceSelector specifies a label selector such that the policy applies only to those routes that are in namespaces with labels that match the selector, and are in one of the DomainPatterns. Defaults to the empty LabelSelector, which matches everything. |
| `preloadPolicy` | `string` | preloadPolicy directs the client to include hosts in its host preload list so that it never needs to do an initial load to get the HSTS header (note that this is not defined in RFC 6797 and is therefore client implementation-dependent). |

Show more

#### [19.1.10. .spec.requiredHSTSPolicies[].maxAge](#spec-requiredhstspolicies-maxage) Copy linkLink copied to clipboard!

Description
:   maxAge is the delta time range in seconds during which hosts are regarded as HSTS hosts. If set to 0, it negates the effect, and hosts are removed as HSTS hosts. If set to 0 and includeSubdomains is specified, all subdomains of the host are also removed as HSTS hosts. maxAge is a time-to-live value, and if this policy is not refreshed on a client, the HSTS policy will eventually expire on that client.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `largestMaxAge` | `integer` | The largest allowed value (in seconds) of the RequiredHSTSPolicy max-age This value can be left unspecified, in which case no upper limit is enforced. |
| `smallestMaxAge` | `integer` | The smallest allowed value (in seconds) of the RequiredHSTSPolicy max-age Setting max-age=0 allows the deletion of an existing HSTS header from a host. This is a necessary tool for administrators to quickly correct mistakes. This value can be left unspecified, in which case no lower limit is enforced. |

Show more

#### [19.1.11. .spec.requiredHSTSPolicies[].namespaceSelector](#spec-requiredhstspolicies-namespaceselector) Copy linkLink copied to clipboard!

Description
:   namespaceSelector specifies a label selector such that the policy applies only to those routes that are in namespaces with labels that match the selector, and are in one of the DomainPatterns. Defaults to the empty LabelSelector, which matches everything.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchExpressions` | `array` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchExpressions[]` | `object` | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

Show more

#### [19.1.12. .spec.requiredHSTSPolicies[].namespaceSelector.matchExpressions](#spec-requiredhstspolicies-namespaceselector-matchexpressions) Copy linkLink copied to clipboard!

Description
:   matchExpressions is a list of label selector requirements. The requirements are ANDed.

Type
:   `array`

#### [19.1.13. .spec.requiredHSTSPolicies[].namespaceSelector.matchExpressions[]](#spec-requiredhstspolicies-namespaceselector-matchexpressions-2) Copy linkLink copied to clipboard!

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

#### [19.1.14. .status](#status-15) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `componentRoutes` | `array` | componentRoutes is where participating operators place the current route status for routes whose hostnames and serving certificates can be customized by the cluster-admin. |
| `componentRoutes[]` | `object` | ComponentRouteStatus contains information allowing configuration of a route’s hostname and serving certificate. |
| `defaultPlacement` | `string` | defaultPlacement is set at installation time to control which nodes will host the ingress router pods by default. The options are control-plane nodes or worker nodes.  This field works by dictating how the Cluster Ingress Operator will consider unset replicas and nodePlacement fields in IngressController resources when creating the corresponding Deployments.  See the documentation for the IngressController replicas and nodePlacement fields for more information.  When omitted, the default value is Workers |

Show more

#### [19.1.15. .status.componentRoutes](#status-componentroutes) Copy linkLink copied to clipboard!

Description
:   componentRoutes is where participating operators place the current route status for routes whose hostnames and serving certificates can be customized by the cluster-admin.

Type
:   `array`

#### [19.1.16. .status.componentRoutes[]](#status-componentroutes-2) Copy linkLink copied to clipboard!

Description
:   ComponentRouteStatus contains information allowing configuration of a route’s hostname and serving certificate.

Type
:   `object`

Required
:   * `defaultHostname`
    * `name`
    * `namespace`
    * `relatedObjects`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions are used to communicate the state of the componentRoutes entry.  Supported conditions include Available, Degraded and Progressing.  If available is true, the content served by the route can be accessed by users. This includes cases where a default may continue to serve content while the customized route specified by the cluster-admin is being configured.  If Degraded is true, that means something has gone wrong trying to handle the componentRoutes entry. The currentHostnames field may or may not be in effect.  If Progressing is true, that means the component is taking some action related to the componentRoutes entry. |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `consumingUsers` | `array (string)` | consumingUsers is a slice of ServiceAccounts that need to have read permission on the servingCertKeyPairSecret secret. |
| `currentHostnames` | `array (string)` | currentHostnames is the list of current names used by the route. Typically, this list should consist of a single hostname, but if multiple hostnames are supported by the route the operator may write multiple entries to this list. |
| `defaultHostname` | `string` | defaultHostname is the hostname of this route prior to customization. |
| `name` | `string` | name is the logical name of the route to customize. It does not have to be the actual name of a route resource but it cannot be renamed.  The namespace and name of this componentRoute must match a corresponding entry in the list of spec.componentRoutes if the route is to be customized. |
| `namespace` | `string` | namespace is the namespace of the route to customize. It must be a real namespace. Using an actual namespace ensures that no two components will conflict and the same component can be installed multiple times.  The namespace and name of this componentRoute must match a corresponding entry in the list of spec.componentRoutes if the route is to be customized. |
| `relatedObjects` | `array` | relatedObjects is a list of resources which are useful when debugging or inspecting how spec.componentRoutes is applied. |
| `relatedObjects[]` | `object` | ObjectReference contains enough information to let you inspect or modify the referred object. |

Show more

#### [19.1.17. .status.componentRoutes[].conditions](#status-componentroutes-conditions) Copy linkLink copied to clipboard!

Description
:   conditions are used to communicate the state of the componentRoutes entry.

    Supported conditions include Available, Degraded and Progressing.

    If available is true, the content served by the route can be accessed by users. This includes cases where a default may continue to serve content while the customized route specified by the cluster-admin is being configured.

    If Degraded is true, that means something has gone wrong trying to handle the componentRoutes entry. The currentHostnames field may or may not be in effect.

    If Progressing is true, that means the component is taking some action related to the componentRoutes entry.

Type
:   `array`

#### [19.1.18. .status.componentRoutes[].conditions[]](#status-componentroutes-conditions-2) Copy linkLink copied to clipboard!

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

#### [19.1.19. .status.componentRoutes[].relatedObjects](#status-componentroutes-relatedobjects) Copy linkLink copied to clipboard!

Description
:   relatedObjects is a list of resources which are useful when debugging or inspecting how spec.componentRoutes is applied.

Type
:   `array`

#### [19.1.20. .status.componentRoutes[].relatedObjects[]](#status-componentroutes-relatedobjects-2) Copy linkLink copied to clipboard!

Description
:   ObjectReference contains enough information to let you inspect or modify the referred object.

Type
:   `object`

Required
:   * `group`
    * `name`
    * `resource`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` | group of the referent. |
| `name` | `string` | name of the referent. |
| `namespace` | `string` | namespace of the referent. |
| `resource` | `string` | resource of the referent. |

Show more

### [19.2. API endpoints](#api-endpoints-18) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/ingresses`

  + `DELETE`: delete collection of Ingress
  + `GET`: list objects of kind Ingress
  + `POST`: create an Ingress
* `/apis/config.openshift.io/v1/ingresses/{name}`

  + `DELETE`: delete an Ingress
  + `GET`: read the specified Ingress
  + `PATCH`: partially update the specified Ingress
  + `PUT`: replace the specified Ingress
* `/apis/config.openshift.io/v1/ingresses/{name}/status`

  + `GET`: read status of the specified Ingress
  + `PATCH`: partially update status of the specified Ingress
  + `PUT`: replace status of the specified Ingress

#### [19.2.1. /apis/config.openshift.io/v1/ingresses](#apisconfig-openshift-iov1ingresses) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Ingress

Expand

Table 19.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Ingress

Expand

Table 19.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`IngressList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-IngressList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an Ingress

Expand

Table 19.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 19.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 19.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 201 - Created | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [19.2.2. /apis/config.openshift.io/v1/ingresses/{name}](#apisconfig-openshift-iov1ingressesname) Copy linkLink copied to clipboard!

Expand

Table 19.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Ingress |

Show more

HTTP method
:   `DELETE`

Description
:   delete an Ingress

Expand

Table 19.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 19.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Ingress

Expand

Table 19.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Ingress

Expand

Table 19.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 19.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Ingress

Expand

Table 19.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 19.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 19.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 201 - Created | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [19.2.3. /apis/config.openshift.io/v1/ingresses/{name}/status](#apisconfig-openshift-iov1ingressesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 19.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Ingress |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Ingress

Expand

Table 19.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Ingress

Expand

Table 19.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 19.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Ingress

Expand

Table 19.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 19.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 19.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 201 - Created | [`Ingress`](#ingress-config-openshift-io-v1 "Chapter 19. Ingress [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 20. Network [config.openshift.io/v1]](#network-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Network holds cluster-wide information about Network. The canonical name is `cluster`. It is used to configure the desired network configuration, such as: IP address pools for services/pod IPs, network plugin, etc. Please view network.spec for an explanation on what applies when configuring this resource.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [20.1. Specification](#specification-19) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration. As a general rule, this SHOULD NOT be read directly. Instead, you should consume the NetworkStatus, as it indicates the currently deployed configuration. Currently, most spec fields are immutable after installation. Please view the individual ones for further details on each. |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [20.1.1. .spec](#spec-19) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration. As a general rule, this SHOULD NOT be read directly. Instead, you should consume the NetworkStatus, as it indicates the currently deployed configuration. Currently, most spec fields are immutable after installation. Please view the individual ones for further details on each.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterNetwork` | `array` | IP address pool to use for pod IPs. This field is immutable after installation. |
| `clusterNetwork[]` | `object` | ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated. |
| `externalIP` | `object` | externalIP defines configuration for controllers that affect Service.ExternalIP. If nil, then ExternalIP is not allowed to be set. |
| `networkDiagnostics` | `object` | networkDiagnostics defines network diagnostics configuration.  Takes precedence over spec.disableNetworkDiagnostics in network.operator.openshift.io. If networkDiagnostics is not specified or is empty, and the spec.disableNetworkDiagnostics flag in network.operator.openshift.io is set to true, the network diagnostics feature will be disabled. |
| `networkType` | `string` | networkType is the plugin that is to be deployed (e.g. OVNKubernetes). This should match a value that the cluster-network-operator understands, or else no networking will be installed. Currently supported values are: - OVNKubernetes This field is immutable after installation. |
| `serviceNetwork` | `array (string)` | IP address pool for services. Currently, we only support a single entry here. This field is immutable after installation. |
| `serviceNodePortRange` | `string` | The port range allowed for Services of type NodePort. If not specified, the default of 30000-32767 will be used. Such Services without a NodePort specified will have one automatically allocated from this range. This parameter can be updated after the cluster is installed. |

Show more

#### [20.1.2. .spec.clusterNetwork](#spec-clusternetwork) Copy linkLink copied to clipboard!

Description
:   IP address pool to use for pod IPs. This field is immutable after installation.

Type
:   `array`

#### [20.1.3. .spec.clusterNetwork[]](#spec-clusternetwork-2) Copy linkLink copied to clipboard!

Description
:   ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cidr` | `string` | The complete block for pod IPs. |
| `hostPrefix` | `integer` | The size (prefix) of block to allocate to each node. If this field is not used by the plugin, it can be left unset. |

Show more

#### [20.1.4. .spec.externalIP](#spec-externalip) Copy linkLink copied to clipboard!

Description
:   externalIP defines configuration for controllers that affect Service.ExternalIP. If nil, then ExternalIP is not allowed to be set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `autoAssignCIDRs` | `array (string)` | autoAssignCIDRs is a list of CIDRs from which to automatically assign Service.ExternalIP. These are assigned when the service is of type LoadBalancer. In general, this is only useful for bare-metal clusters. In Openshift 3.x, this was misleadingly called "IngressIPs". Automatically assigned External IPs are not affected by any ExternalIPPolicy rules. Currently, only one entry may be provided. |
| `policy` | `object` | policy is a set of restrictions applied to the ExternalIP field. If nil or empty, then ExternalIP is not allowed to be set. |

Show more

#### [20.1.5. .spec.externalIP.policy](#spec-externalip-policy) Copy linkLink copied to clipboard!

Description
:   policy is a set of restrictions applied to the ExternalIP field. If nil or empty, then ExternalIP is not allowed to be set.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `allowedCIDRs` | `array (string)` | allowedCIDRs is the list of allowed CIDRs. |
| `rejectedCIDRs` | `array (string)` | rejectedCIDRs is the list of disallowed CIDRs. These take precedence over allowedCIDRs. |

Show more

#### [20.1.6. .spec.networkDiagnostics](#spec-networkdiagnostics) Copy linkLink copied to clipboard!

Description
:   networkDiagnostics defines network diagnostics configuration.

    Takes precedence over spec.disableNetworkDiagnostics in network.operator.openshift.io. If networkDiagnostics is not specified or is empty, and the spec.disableNetworkDiagnostics flag in network.operator.openshift.io is set to true, the network diagnostics feature will be disabled.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mode` | `string` | mode controls the network diagnostics mode  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is All. |
| `sourcePlacement` | `object` | sourcePlacement controls the scheduling of network diagnostics source deployment  See NetworkDiagnosticsSourcePlacement for more details about default values. |
| `targetPlacement` | `object` | targetPlacement controls the scheduling of network diagnostics target daemonset  See NetworkDiagnosticsTargetPlacement for more details about default values. |

Show more

#### [20.1.7. .spec.networkDiagnostics.sourcePlacement](#spec-networkdiagnostics-sourceplacement) Copy linkLink copied to clipboard!

Description
:   sourcePlacement controls the scheduling of network diagnostics source deployment

    See NetworkDiagnosticsSourcePlacement for more details about default values.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nodeSelector` | `object (string)` | nodeSelector is the node selector applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `kubernetes.io/os: linux`. |
| `tolerations` | `array` | tolerations is a list of tolerations applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is an empty list. |
| `tolerations[]` | `object` | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [20.1.8. .spec.networkDiagnostics.sourcePlacement.tolerations](#spec-networkdiagnostics-sourceplacement-tolerations) Copy linkLink copied to clipboard!

Description
:   tolerations is a list of tolerations applied to network diagnostics components

    When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is an empty list.

Type
:   `array`

#### [20.1.9. .spec.networkDiagnostics.sourcePlacement.tolerations[]](#spec-networkdiagnostics-sourceplacement-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators). |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

Show more

#### [20.1.10. .spec.networkDiagnostics.targetPlacement](#spec-networkdiagnostics-targetplacement) Copy linkLink copied to clipboard!

Description
:   targetPlacement controls the scheduling of network diagnostics target daemonset

    See NetworkDiagnosticsTargetPlacement for more details about default values.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nodeSelector` | `object (string)` | nodeSelector is the node selector applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `kubernetes.io/os: linux`. |
| `tolerations` | `array` | tolerations is a list of tolerations applied to network diagnostics components  When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `- operator: "Exists"` which means that all taints are tolerated. |
| `tolerations[]` | `object` | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. |

Show more

#### [20.1.11. .spec.networkDiagnostics.targetPlacement.tolerations](#spec-networkdiagnostics-targetplacement-tolerations) Copy linkLink copied to clipboard!

Description
:   tolerations is a list of tolerations applied to network diagnostics components

    When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. The current default is `- operator: "Exists"` which means that all taints are tolerated.

Type
:   `array`

#### [20.1.12. .spec.networkDiagnostics.targetPlacement.tolerations[]](#spec-networkdiagnostics-targetplacement-tolerations-2) Copy linkLink copied to clipboard!

Description
:   The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators). |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

Show more

#### [20.1.13. .status](#status-16) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterNetwork` | `array` | IP address pool to use for pod IPs. |
| `clusterNetwork[]` | `object` | ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated. |
| `clusterNetworkMTU` | `integer` | clusterNetworkMTU is the MTU for inter-pod networking. |
| `conditions` | `array` | conditions represents the observations of a network.config current state. Known .status.conditions.type are: "NetworkDiagnosticsAvailable" |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |
| `migration` | `object` | migration contains the cluster network migration configuration. |
| `networkType` | `string` | networkType is the plugin that is deployed (e.g. OVNKubernetes). |
| `serviceNetwork` | `array (string)` | IP address pool for services. Currently, we only support a single entry here. |

Show more

#### [20.1.14. .status.clusterNetwork](#status-clusternetwork) Copy linkLink copied to clipboard!

Description
:   IP address pool to use for pod IPs.

Type
:   `array`

#### [20.1.15. .status.clusterNetwork[]](#status-clusternetwork-2) Copy linkLink copied to clipboard!

Description
:   ClusterNetworkEntry is a contiguous block of IP addresses from which pod IPs are allocated.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cidr` | `string` | The complete block for pod IPs. |
| `hostPrefix` | `integer` | The size (prefix) of block to allocate to each node. If this field is not used by the plugin, it can be left unset. |

Show more

#### [20.1.16. .status.conditions](#status-conditions-13) Copy linkLink copied to clipboard!

Description
:   conditions represents the observations of a network.config current state. Known .status.conditions.type are: "NetworkDiagnosticsAvailable"

Type
:   `array`

#### [20.1.17. .status.conditions[]](#status-conditions-14) Copy linkLink copied to clipboard!

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

#### [20.1.18. .status.migration](#status-migration) Copy linkLink copied to clipboard!

Description
:   migration contains the cluster network migration configuration.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `mtu` | `object` | mtu is the MTU configuration that is being deployed. |
| `networkType` | `string` | networkType is the target plugin that is being deployed. DEPRECATED: network type migration is no longer supported, so this should always be unset. |

Show more

#### [20.1.19. .status.migration.mtu](#status-migration-mtu) Copy linkLink copied to clipboard!

Description
:   mtu is the MTU configuration that is being deployed.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `machine` | `object` | machine contains MTU migration configuration for the machine’s uplink. |
| `network` | `object` | network contains MTU migration configuration for the default network. |

Show more

#### [20.1.20. .status.migration.mtu.machine](#status-migration-mtu-machine) Copy linkLink copied to clipboard!

Description
:   machine contains MTU migration configuration for the machine’s uplink.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `from` | `integer` | from is the MTU to migrate from. |
| `to` | `integer` | to is the MTU to migrate to. |

Show more

#### [20.1.21. .status.migration.mtu.network](#status-migration-mtu-network) Copy linkLink copied to clipboard!

Description
:   network contains MTU migration configuration for the default network.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `from` | `integer` | from is the MTU to migrate from. |
| `to` | `integer` | to is the MTU to migrate to. |

Show more

### [20.2. API endpoints](#api-endpoints-19) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/networks`

  + `DELETE`: delete collection of Network
  + `GET`: list objects of kind Network
  + `POST`: create a Network
* `/apis/config.openshift.io/v1/networks/{name}`

  + `DELETE`: delete a Network
  + `GET`: read the specified Network
  + `PATCH`: partially update the specified Network
  + `PUT`: replace the specified Network

#### [20.2.1. /apis/config.openshift.io/v1/networks](#apisconfig-openshift-iov1networks) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Network

Expand

Table 20.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Network

Expand

Table 20.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`NetworkList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-NetworkList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Network

Expand

Table 20.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 20.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 20.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 201 - Created | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [20.2.2. /apis/config.openshift.io/v1/networks/{name}](#apisconfig-openshift-iov1networksname) Copy linkLink copied to clipboard!

Expand

Table 20.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Network |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Network

Expand

Table 20.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 20.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Network

Expand

Table 20.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Network

Expand

Table 20.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 20.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Network

Expand

Table 20.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 20.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 20.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 201 - Created | [`Network`](#network-config-openshift-io-v1 "Chapter 20. Network [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 21. Node [config.openshift.io/v1]](#node-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Node holds cluster-wide information about node specific features.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [21.1. Specification](#specification-20) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values. |

Show more

#### [21.1.1. .spec](#spec-20) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `cgroupMode` | `string` | cgroupMode determines the cgroups version on the node |
| `workerLatencyProfile` | `string` | workerLatencyProfile determins the how fast the kubelet is updating the status and corresponding reaction of the cluster |

Show more

#### [21.1.2. .status](#status-17) Copy linkLink copied to clipboard!

Description
:   status holds observed values.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions contain the details and the current state of the nodes.config object |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |

Show more

#### [21.1.3. .status.conditions](#status-conditions-15) Copy linkLink copied to clipboard!

Description
:   conditions contain the details and the current state of the nodes.config object

Type
:   `array`

#### [21.1.4. .status.conditions[]](#status-conditions-16) Copy linkLink copied to clipboard!

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

### [21.2. API endpoints](#api-endpoints-20) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/nodes`

  + `DELETE`: delete collection of Node
  + `GET`: list objects of kind Node
  + `POST`: create a Node
* `/apis/config.openshift.io/v1/nodes/{name}`

  + `DELETE`: delete a Node
  + `GET`: read the specified Node
  + `PATCH`: partially update the specified Node
  + `PUT`: replace the specified Node
* `/apis/config.openshift.io/v1/nodes/{name}/status`

  + `GET`: read status of the specified Node
  + `PATCH`: partially update status of the specified Node
  + `PUT`: replace status of the specified Node

#### [21.2.1. /apis/config.openshift.io/v1/nodes](#apisconfig-openshift-iov1nodes) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Node

Expand

Table 21.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Node

Expand

Table 21.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`NodeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-NodeList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Node

Expand

Table 21.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 21.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 21.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 201 - Created | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [21.2.2. /apis/config.openshift.io/v1/nodes/{name}](#apisconfig-openshift-iov1nodesname) Copy linkLink copied to clipboard!

Expand

Table 21.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Node |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Node

Expand

Table 21.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 21.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Node

Expand

Table 21.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Node

Expand

Table 21.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 21.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Node

Expand

Table 21.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 21.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 21.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 201 - Created | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [21.2.3. /apis/config.openshift.io/v1/nodes/{name}/status](#apisconfig-openshift-iov1nodesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 21.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Node |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Node

Expand

Table 21.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Node

Expand

Table 21.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 21.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Node

Expand

Table 21.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 21.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 21.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 201 - Created | [`Node`](#node-config-openshift-io-v1 "Chapter 21. Node [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 22. OAuth [config.openshift.io/v1]](#oauth-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   OAuth holds cluster-wide information about OAuth. The canonical name is `cluster`. It is used to configure the integrated OAuth server. This configuration is only honored when the top level Authentication config has type set to IntegratedOAuth.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [22.1. Specification](#specification-21) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [22.1.1. .spec](#spec-21) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `identityProviders` | `array` | identityProviders is an ordered list of ways for a user to identify themselves. When this list is empty, no identities are provisioned for users. |
| `identityProviders[]` | `object` | IdentityProvider provides identities for users authenticating using credentials |
| `templates` | `object` | templates allow you to customize pages like the login page. |
| `tokenConfig` | `object` | tokenConfig contains options for authorization and access tokens |

Show more

#### [22.1.2. .spec.identityProviders](#spec-identityproviders) Copy linkLink copied to clipboard!

Description
:   identityProviders is an ordered list of ways for a user to identify themselves. When this list is empty, no identities are provisioned for users.

Type
:   `array`

#### [22.1.3. .spec.identityProviders[]](#spec-identityproviders-2) Copy linkLink copied to clipboard!

Description
:   IdentityProvider provides identities for users authenticating using credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `basicAuth` | `object` | basicAuth contains configuration options for the BasicAuth IdP |
| `github` | `object` | github enables user authentication using GitHub credentials |
| `gitlab` | `object` | gitlab enables user authentication using GitLab credentials |
| `google` | `object` | google enables user authentication using Google credentials |
| `htpasswd` | `object` | htpasswd enables user authentication using an HTPasswd file to validate credentials |
| `keystone` | `object` | keystone enables user authentication using keystone password credentials |
| `ldap` | `object` | ldap enables user authentication using LDAP credentials |
| `mappingMethod` | `string` | mappingMethod determines how identities from this provider are mapped to users Defaults to "claim" |
| `name` | `string` | name is used to qualify the identities returned by this provider. - It MUST be unique and not shared by any other identity provider used - It MUST be a valid path segment: name cannot equal "." or ".." or contain "/" or "%" or ":" Ref: <https://godoc.org/github.com/openshift/origin/pkg/user/apis/user/validation#ValidateIdentityProviderName> |
| `openID` | `object` | openID enables user authentication using OpenID credentials |
| `requestHeader` | `object` | requestHeader enables user authentication using request header credentials |
| `type` | `string` | type identifies the identity provider type for this entry. |

Show more

#### [22.1.4. .spec.identityProviders[].basicAuth](#spec-identityproviders-basicauth) Copy linkLink copied to clipboard!

Description
:   basicAuth contains configuration options for the BasicAuth IdP

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. |
| `tlsClientCert` | `object` | tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `tlsClientKey` | `object` | tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `url` | `string` | url is the remote URL to connect to |

Show more

#### [22.1.5. .spec.identityProviders[].basicAuth.ca](#spec-identityproviders-basicauth-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.6. .spec.identityProviders[].basicAuth.tlsClientCert](#spec-identityproviders-basicauth-tlsclientcert) Copy linkLink copied to clipboard!

Description
:   tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.7. .spec.identityProviders[].basicAuth.tlsClientKey](#spec-identityproviders-basicauth-tlsclientkey) Copy linkLink copied to clipboard!

Description
:   tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.8. .spec.identityProviders[].github](#spec-identityproviders-github) Copy linkLink copied to clipboard!

Description
:   github enables user authentication using GitHub credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. This can only be configured when hostname is set to a non-empty value. The namespace for this config map is openshift-config. |
| `clientID` | `string` | clientID is the oauth client ID |
| `clientSecret` | `object` | clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `hostname` | `string` | hostname is the optional domain (e.g. "mycompany.com") for use with a hosted instance of GitHub Enterprise. It must match the GitHub Enterprise settings value configured at /setup/settings#hostname. |
| `organizations` | `array (string)` | organizations optionally restricts which organizations are allowed to log in |
| `teams` | `array (string)` | teams optionally restricts which teams are allowed to log in. Format is <org>/<team>. |

Show more

#### [22.1.9. .spec.identityProviders[].github.ca](#spec-identityproviders-github-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. This can only be configured when hostname is set to a non-empty value. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.10. .spec.identityProviders[].github.clientSecret](#spec-identityproviders-github-clientsecret) Copy linkLink copied to clipboard!

Description
:   clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.11. .spec.identityProviders[].gitlab](#spec-identityproviders-gitlab) Copy linkLink copied to clipboard!

Description
:   gitlab enables user authentication using GitLab credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. |
| `clientID` | `string` | clientID is the oauth client ID |
| `clientSecret` | `object` | clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `url` | `string` | url is the oauth server base URL |

Show more

#### [22.1.12. .spec.identityProviders[].gitlab.ca](#spec-identityproviders-gitlab-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.13. .spec.identityProviders[].gitlab.clientSecret](#spec-identityproviders-gitlab-clientsecret) Copy linkLink copied to clipboard!

Description
:   clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.14. .spec.identityProviders[].google](#spec-identityproviders-google) Copy linkLink copied to clipboard!

Description
:   google enables user authentication using Google credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clientID` | `string` | clientID is the oauth client ID |
| `clientSecret` | `object` | clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `hostedDomain` | `string` | hostedDomain is the optional Google App domain (e.g. "mycompany.com") to restrict logins to |

Show more

#### [22.1.15. .spec.identityProviders[].google.clientSecret](#spec-identityproviders-google-clientsecret) Copy linkLink copied to clipboard!

Description
:   clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.16. .spec.identityProviders[].htpasswd](#spec-identityproviders-htpasswd) Copy linkLink copied to clipboard!

Description
:   htpasswd enables user authentication using an HTPasswd file to validate credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `fileData` | `object` | fileData is a required reference to a secret by name containing the data to use as the htpasswd file. The key "htpasswd" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. If the specified htpasswd data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. |

Show more

#### [22.1.17. .spec.identityProviders[].htpasswd.fileData](#spec-identityproviders-htpasswd-filedata) Copy linkLink copied to clipboard!

Description
:   fileData is a required reference to a secret by name containing the data to use as the htpasswd file. The key "htpasswd" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. If the specified htpasswd data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.18. .spec.identityProviders[].keystone](#spec-identityproviders-keystone) Copy linkLink copied to clipboard!

Description
:   keystone enables user authentication using keystone password credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. |
| `domainName` | `string` | domainName is required for keystone v3 |
| `tlsClientCert` | `object` | tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `tlsClientKey` | `object` | tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `url` | `string` | url is the remote URL to connect to |

Show more

#### [22.1.19. .spec.identityProviders[].keystone.ca](#spec-identityproviders-keystone-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.20. .spec.identityProviders[].keystone.tlsClientCert](#spec-identityproviders-keystone-tlsclientcert) Copy linkLink copied to clipboard!

Description
:   tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.21. .spec.identityProviders[].keystone.tlsClientKey](#spec-identityproviders-keystone-tlsclientkey) Copy linkLink copied to clipboard!

Description
:   tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.22. .spec.identityProviders[].ldap](#spec-identityproviders-ldap) Copy linkLink copied to clipboard!

Description
:   ldap enables user authentication using LDAP credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `attributes` | `object` | attributes maps LDAP attributes to identities |
| `bindDN` | `string` | bindDN is an optional DN to bind with during the search phase. |
| `bindPassword` | `object` | bindPassword is an optional reference to a secret by name containing a password to bind with during the search phase. The key "bindPassword" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. |
| `insecure` | `boolean` | insecure, if true, indicates the connection should not use TLS WARNING: Should not be set to `true` with the URL scheme "ldaps://" as "ldaps://" URLs always attempt to connect using TLS, even when `insecure` is set to `true` When `true`, "ldap://" URLS connect insecurely. When `false`, "ldap://" URLs are upgraded to a TLS connection using StartTLS as specified in <https://tools.ietf.org/html/rfc2830>. |
| `url` | `string` | url is an RFC 2255 URL which specifies the LDAP search parameters to use. The syntax of the URL is: ldap://host:port/basedn?attribute?scope?filter |

Show more

#### [22.1.23. .spec.identityProviders[].ldap.attributes](#spec-identityproviders-ldap-attributes) Copy linkLink copied to clipboard!

Description
:   attributes maps LDAP attributes to identities

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `email` | `array (string)` | email is the list of attributes whose values should be used as the email address. Optional. If unspecified, no email is set for the identity |
| `id` | `array (string)` | id is the list of attributes whose values should be used as the user ID. Required. First non-empty attribute is used. At least one attribute is required. If none of the listed attribute have a value, authentication fails. LDAP standard identity attribute is "dn" |
| `name` | `array (string)` | name is the list of attributes whose values should be used as the display name. Optional. If unspecified, no display name is set for the identity LDAP standard display name attribute is "cn" |
| `preferredUsername` | `array (string)` | preferredUsername is the list of attributes whose values should be used as the preferred username. LDAP standard login attribute is "uid" |

Show more

#### [22.1.24. .spec.identityProviders[].ldap.bindPassword](#spec-identityproviders-ldap-bindpassword) Copy linkLink copied to clipboard!

Description
:   bindPassword is an optional reference to a secret by name containing a password to bind with during the search phase. The key "bindPassword" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.25. .spec.identityProviders[].ldap.ca](#spec-identityproviders-ldap-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.26. .spec.identityProviders[].openID](#spec-identityproviders-openid) Copy linkLink copied to clipboard!

Description
:   openID enables user authentication using OpenID credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. |
| `claims` | `object` | claims mappings |
| `clientID` | `string` | clientID is the oauth client ID |
| `clientSecret` | `object` | clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. |
| `extraAuthorizeParameters` | `object (string)` | extraAuthorizeParameters are any custom parameters to add to the authorize request. |
| `extraScopes` | `array (string)` | extraScopes are any scopes to request in addition to the standard "openid" scope. |
| `issuer` | `string` | issuer is the URL that the OpenID Provider asserts as its Issuer Identifier. It must use the https scheme with no query or fragment component. |

Show more

#### [22.1.27. .spec.identityProviders[].openID.ca](#spec-identityproviders-openid-ca) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.28. .spec.identityProviders[].openID.claims](#spec-identityproviders-openid-claims) Copy linkLink copied to clipboard!

Description
:   claims mappings

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `email` | `array (string)` | email is the list of claims whose values should be used as the email address. Optional. If unspecified, no email is set for the identity |
| `groups` | `array (string)` | groups is the list of claims value of which should be used to synchronize groups from the OIDC provider to OpenShift for the user. If multiple claims are specified, the first one with a non-empty value is used. |
| `name` | `array (string)` | name is the list of claims whose values should be used as the display name. Optional. If unspecified, no display name is set for the identity |
| `preferredUsername` | `array (string)` | preferredUsername is the list of claims whose values should be used as the preferred username. If unspecified, the preferred username is determined from the value of the sub claim |

Show more

#### [22.1.29. .spec.identityProviders[].openID.clientSecret](#spec-identityproviders-openid-clientsecret) Copy linkLink copied to clipboard!

Description
:   clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.30. .spec.identityProviders[].requestHeader](#spec-identityproviders-requestheader) Copy linkLink copied to clipboard!

Description
:   requestHeader enables user authentication using request header credentials

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `ca` | `object` | ca is a required reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. Specifically, it allows verification of incoming requests to prevent header spoofing. The key "ca.crt" is used to locate the data. If the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. The namespace for this config map is openshift-config. |
| `challengeURL` | `string` | challengeURL is a URL to redirect unauthenticated /authorize requests to Unauthenticated requests from OAuth clients which expect WWW-Authenticate challenges will be redirected here. ${url} is replaced with the current URL, escaped to be safe in a query parameter <https://www.example.com/sso-login?then=${url}> ${query} is replaced with the current query string <https://www.example.com/auth-proxy/oauth/authorize?${query}> Required when challenge is set to true. |
| `clientCommonNames` | `array (string)` | clientCommonNames is an optional list of common names to require a match from. If empty, any client certificate validated against the clientCA bundle is considered authoritative. |
| `emailHeaders` | `array (string)` | emailHeaders is the set of headers to check for the email address |
| `headers` | `array (string)` | headers is the set of headers to check for identity information |
| `loginURL` | `string` | loginURL is a URL to redirect unauthenticated /authorize requests to Unauthenticated requests from OAuth clients which expect interactive logins will be redirected here ${url} is replaced with the current URL, escaped to be safe in a query parameter <https://www.example.com/sso-login?then=${url}> ${query} is replaced with the current query string <https://www.example.com/auth-proxy/oauth/authorize?${query}> Required when login is set to true. |
| `nameHeaders` | `array (string)` | nameHeaders is the set of headers to check for the display name |
| `preferredUsernameHeaders` | `array (string)` | preferredUsernameHeaders is the set of headers to check for the preferred username |

Show more

#### [22.1.31. .spec.identityProviders[].requestHeader.ca](#spec-identityproviders-requestheader-ca) Copy linkLink copied to clipboard!

Description
:   ca is a required reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. Specifically, it allows verification of incoming requests to prevent header spoofing. The key "ca.crt" is used to locate the data. If the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. The namespace for this config map is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [22.1.32. .spec.templates](#spec-templates) Copy linkLink copied to clipboard!

Description
:   templates allow you to customize pages like the login page.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `error` | `object` | error is the name of a secret that specifies a go template to use to render error pages during the authentication or grant flow. The key "errors.html" is used to locate the template data. If specified and the secret or expected key is not found, the default error page is used. If the specified template is not valid, the default error page is used. If unspecified, the default error page is used. The namespace for this secret is openshift-config. |
| `login` | `object` | login is the name of a secret that specifies a go template to use to render the login page. The key "login.html" is used to locate the template data. If specified and the secret or expected key is not found, the default login page is used. If the specified template is not valid, the default login page is used. If unspecified, the default login page is used. The namespace for this secret is openshift-config. |
| `providerSelection` | `object` | providerSelection is the name of a secret that specifies a go template to use to render the provider selection page. The key "providers.html" is used to locate the template data. If specified and the secret or expected key is not found, the default provider selection page is used. If the specified template is not valid, the default provider selection page is used. If unspecified, the default provider selection page is used. The namespace for this secret is openshift-config. |

Show more

#### [22.1.33. .spec.templates.error](#spec-templates-error) Copy linkLink copied to clipboard!

Description
:   error is the name of a secret that specifies a go template to use to render error pages during the authentication or grant flow. The key "errors.html" is used to locate the template data. If specified and the secret or expected key is not found, the default error page is used. If the specified template is not valid, the default error page is used. If unspecified, the default error page is used. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.34. .spec.templates.login](#spec-templates-login) Copy linkLink copied to clipboard!

Description
:   login is the name of a secret that specifies a go template to use to render the login page. The key "login.html" is used to locate the template data. If specified and the secret or expected key is not found, the default login page is used. If the specified template is not valid, the default login page is used. If unspecified, the default login page is used. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.35. .spec.templates.providerSelection](#spec-templates-providerselection) Copy linkLink copied to clipboard!

Description
:   providerSelection is the name of a secret that specifies a go template to use to render the provider selection page. The key "providers.html" is used to locate the template data. If specified and the secret or expected key is not found, the default provider selection page is used. If the specified template is not valid, the default provider selection page is used. If unspecified, the default provider selection page is used. The namespace for this secret is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [22.1.36. .spec.tokenConfig](#spec-tokenconfig) Copy linkLink copied to clipboard!

Description
:   tokenConfig contains options for authorization and access tokens

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessTokenInactivityTimeout` | `string` | accessTokenInactivityTimeout defines the token inactivity timeout for tokens granted by any client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. Takes valid time duration string such as "5m", "1.5h" or "2h45m". The minimum allowed value for duration is 300s (5 minutes). If the timeout is configured per client, then that value takes precedence. If the timeout value is not specified and the client does not override the value, then tokens are valid until their lifetime.  WARNING: existing tokens' timeout will not be affected (lowered) by changing this value |
| `accessTokenInactivityTimeoutSeconds` | `integer` | accessTokenInactivityTimeoutSeconds - DEPRECATED: setting this field has no effect. |
| `accessTokenMaxAgeSeconds` | `integer` | accessTokenMaxAgeSeconds defines the maximum age of access tokens |

Show more

#### [22.1.37. .status](#status-18) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

### [22.2. API endpoints](#api-endpoints-21) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/oauths`

  + `DELETE`: delete collection of OAuth
  + `GET`: list objects of kind OAuth
  + `POST`: create an OAuth
* `/apis/config.openshift.io/v1/oauths/{name}`

  + `DELETE`: delete an OAuth
  + `GET`: read the specified OAuth
  + `PATCH`: partially update the specified OAuth
  + `PUT`: replace the specified OAuth
* `/apis/config.openshift.io/v1/oauths/{name}/status`

  + `GET`: read status of the specified OAuth
  + `PATCH`: partially update status of the specified OAuth
  + `PUT`: replace status of the specified OAuth

#### [22.2.1. /apis/config.openshift.io/v1/oauths](#apisconfig-openshift-iov1oauths) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of OAuth

Expand

Table 22.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind OAuth

Expand

Table 22.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuthList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-OAuthList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an OAuth

Expand

Table 22.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 22.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 22.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 201 - Created | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 202 - Accepted | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [22.2.2. /apis/config.openshift.io/v1/oauths/{name}](#apisconfig-openshift-iov1oauthsname) Copy linkLink copied to clipboard!

Expand

Table 22.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuth |

Show more

HTTP method
:   `DELETE`

Description
:   delete an OAuth

Expand

Table 22.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 22.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified OAuth

Expand

Table 22.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified OAuth

Expand

Table 22.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 22.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified OAuth

Expand

Table 22.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 22.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 22.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 201 - Created | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [22.2.3. /apis/config.openshift.io/v1/oauths/{name}/status](#apisconfig-openshift-iov1oauthsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 22.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OAuth |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified OAuth

Expand

Table 22.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified OAuth

Expand

Table 22.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 22.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified OAuth

Expand

Table 22.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 22.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 22.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 201 - Created | [`OAuth`](#oauth-config-openshift-io-v1 "Chapter 22. OAuth [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 23. OperatorHub [config.openshift.io/v1]](#operatorhub-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   OperatorHub is the Schema for the operatorhubs API. It can be used to change the state of the default hub sources for OperatorHub on the cluster from enabled to disabled and vice versa.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

### [23.1. Specification](#specification-22) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | OperatorHubSpec defines the desired state of OperatorHub |
| `status` | `object` | OperatorHubStatus defines the observed state of OperatorHub. The current state of the default hub sources will always be reflected here. |

Show more

#### [23.1.1. .spec](#spec-22) Copy linkLink copied to clipboard!

Description
:   OperatorHubSpec defines the desired state of OperatorHub

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `disableAllDefaultSources` | `boolean` | disableAllDefaultSources allows you to disable all the default hub sources. If this is true, a specific entry in sources can be used to enable a default source. If this is false, a specific entry in sources can be used to disable or enable a default source. |
| `sources` | `array` | sources is the list of default hub sources and their configuration. If the list is empty, it implies that the default hub sources are enabled on the cluster unless disableAllDefaultSources is true. If disableAllDefaultSources is true and sources is not empty, the configuration present in sources will take precedence. The list of default hub sources and their current state will always be reflected in the status block. |
| `sources[]` | `object` | HubSource is used to specify the hub source and its configuration |

Show more

#### [23.1.2. .spec.sources](#spec-sources) Copy linkLink copied to clipboard!

Description
:   sources is the list of default hub sources and their configuration. If the list is empty, it implies that the default hub sources are enabled on the cluster unless disableAllDefaultSources is true. If disableAllDefaultSources is true and sources is not empty, the configuration present in sources will take precedence. The list of default hub sources and their current state will always be reflected in the status block.

Type
:   `array`

#### [23.1.3. .spec.sources[]](#spec-sources-2) Copy linkLink copied to clipboard!

Description
:   HubSource is used to specify the hub source and its configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `disabled` | `boolean` | disabled is used to disable a default hub source on cluster |
| `name` | `string` | name is the name of one of the default hub sources |

Show more

#### [23.1.4. .status](#status-19) Copy linkLink copied to clipboard!

Description
:   OperatorHubStatus defines the observed state of OperatorHub. The current state of the default hub sources will always be reflected here.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `sources` | `array` | sources encapsulates the result of applying the configuration for each hub source |
| `sources[]` | `object` | HubSourceStatus is used to reflect the current state of applying the configuration to a default source |

Show more

#### [23.1.5. .status.sources](#status-sources) Copy linkLink copied to clipboard!

Description
:   sources encapsulates the result of applying the configuration for each hub source

Type
:   `array`

#### [23.1.6. .status.sources[]](#status-sources-2) Copy linkLink copied to clipboard!

Description
:   HubSourceStatus is used to reflect the current state of applying the configuration to a default source

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `disabled` | `boolean` | disabled is used to disable a default hub source on cluster |
| `message` | `string` | message provides more information regarding failures |
| `name` | `string` | name is the name of one of the default hub sources |
| `status` | `string` | status indicates success or failure in applying the configuration |

Show more

### [23.2. API endpoints](#api-endpoints-22) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/operatorhubs`

  + `DELETE`: delete collection of OperatorHub
  + `GET`: list objects of kind OperatorHub
  + `POST`: create an OperatorHub
* `/apis/config.openshift.io/v1/operatorhubs/{name}`

  + `DELETE`: delete an OperatorHub
  + `GET`: read the specified OperatorHub
  + `PATCH`: partially update the specified OperatorHub
  + `PUT`: replace the specified OperatorHub
* `/apis/config.openshift.io/v1/operatorhubs/{name}/status`

  + `GET`: read status of the specified OperatorHub
  + `PATCH`: partially update status of the specified OperatorHub
  + `PUT`: replace status of the specified OperatorHub

#### [23.2.1. /apis/config.openshift.io/v1/operatorhubs](#apisconfig-openshift-iov1operatorhubs) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of OperatorHub

Expand

Table 23.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind OperatorHub

Expand

Table 23.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHubList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-OperatorHubList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create an OperatorHub

Expand

Table 23.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 23.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 23.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 201 - Created | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 202 - Accepted | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [23.2.2. /apis/config.openshift.io/v1/operatorhubs/{name}](#apisconfig-openshift-iov1operatorhubsname) Copy linkLink copied to clipboard!

Expand

Table 23.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OperatorHub |

Show more

HTTP method
:   `DELETE`

Description
:   delete an OperatorHub

Expand

Table 23.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 23.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified OperatorHub

Expand

Table 23.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified OperatorHub

Expand

Table 23.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 23.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified OperatorHub

Expand

Table 23.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 23.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 23.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 201 - Created | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [23.2.3. /apis/config.openshift.io/v1/operatorhubs/{name}/status](#apisconfig-openshift-iov1operatorhubsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 23.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the OperatorHub |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified OperatorHub

Expand

Table 23.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified OperatorHub

Expand

Table 23.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 23.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified OperatorHub

Expand

Table 23.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 23.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 23.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 201 - Created | [`OperatorHub`](#operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 24. Project [config.openshift.io/v1]](#project-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Project holds cluster-wide information about Project. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [24.1. Specification](#specification-23) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [24.1.1. .spec](#spec-23) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `projectRequestMessage` | `string` | projectRequestMessage is the string presented to a user if they are unable to request a project via the projectrequest api endpoint |
| `projectRequestTemplate` | `object` | projectRequestTemplate is the template to use for creating projects in response to projectrequest. This must point to a template in 'openshift-config' namespace. It is optional. If it is not specified, a default template is used. |

Show more

#### [24.1.2. .spec.projectRequestTemplate](#spec-projectrequesttemplate) Copy linkLink copied to clipboard!

Description
:   projectRequestTemplate is the template to use for creating projects in response to projectrequest. This must point to a template in 'openshift-config' namespace. It is optional. If it is not specified, a default template is used.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced project request template |

Show more

#### [24.1.3. .status](#status-20) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

### [24.2. API endpoints](#api-endpoints-23) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/projects`

  + `DELETE`: delete collection of Project
  + `GET`: list objects of kind Project
  + `POST`: create a Project
* `/apis/config.openshift.io/v1/projects/{name}`

  + `DELETE`: delete a Project
  + `GET`: read the specified Project
  + `PATCH`: partially update the specified Project
  + `PUT`: replace the specified Project
* `/apis/config.openshift.io/v1/projects/{name}/status`

  + `GET`: read status of the specified Project
  + `PATCH`: partially update status of the specified Project
  + `PUT`: replace status of the specified Project

#### [24.2.1. /apis/config.openshift.io/v1/projects](#apisconfig-openshift-iov1projects) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Project

Expand

Table 24.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Project

Expand

Table 24.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ProjectList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Project

Expand

Table 24.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 24.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 24.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 201 - Created | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [24.2.2. /apis/config.openshift.io/v1/projects/{name}](#apisconfig-openshift-iov1projectsname) Copy linkLink copied to clipboard!

Expand

Table 24.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Project |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Project

Expand

Table 24.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 24.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Project

Expand

Table 24.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Project

Expand

Table 24.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 24.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Project

Expand

Table 24.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 24.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 24.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 201 - Created | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [24.2.3. /apis/config.openshift.io/v1/projects/{name}/status](#apisconfig-openshift-iov1projectsnamestatus) Copy linkLink copied to clipboard!

Expand

Table 24.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Project |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Project

Expand

Table 24.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Project

Expand

Table 24.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 24.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Project

Expand

Table 24.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 24.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 24.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 201 - Created | [`Project`](#project-config-openshift-io-v1 "Chapter 24. Project [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]](#projecthelmchartrepository-helm-openshift-io-v1beta1) Copy linkLink copied to clipboard!

Description
:   ProjectHelmChartRepository holds namespace-wide configuration for proxied Helm chart repository

    Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [25.1. Specification](#specification-24) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | Observed status of the repository within the namespace.. |

Show more

#### [25.1.1. .spec](#spec-24) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `connectionConfig` | `object` | Required configuration for connecting to the chart repo |
| `description` | `string` | Optional human readable repository description, it can be used by UI for displaying purposes |
| `disabled` | `boolean` | If set to true, disable the repo usage in the namespace |
| `name` | `string` | Optional associated human readable repository name, it can be used by UI for displaying purposes |

Show more

#### [25.1.2. .spec.connectionConfig](#spec-connectionconfig-2) Copy linkLink copied to clipboard!

Description
:   Required configuration for connecting to the chart repo

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `basicAuthConfig` | `object` | basicAuthConfig is an optional reference to a secret by name that contains the basic authentication credentials to present when connecting to the server. The key "username" is used locate the username. The key "password" is used to locate the password. The namespace for this secret must be same as the namespace where the project helm chart repository is getting instantiated. |
| `ca` | `object` | ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this configmap must be same as the namespace where the project helm chart repository is getting instantiated. |
| `tlsClientConfig` | `object` | tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret must be same as the namespace where the project helm chart repository is getting instantiated. |
| `url` | `string` | Chart repository URL |

Show more

#### [25.1.3. .spec.connectionConfig.basicAuthConfig](#spec-connectionconfig-basicauthconfig) Copy linkLink copied to clipboard!

Description
:   basicAuthConfig is an optional reference to a secret by name that contains the basic authentication credentials to present when connecting to the server. The key "username" is used locate the username. The key "password" is used to locate the password. The namespace for this secret must be same as the namespace where the project helm chart repository is getting instantiated.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [25.1.4. .spec.connectionConfig.ca](#spec-connectionconfig-ca-2) Copy linkLink copied to clipboard!

Description
:   ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this configmap must be same as the namespace where the project helm chart repository is getting instantiated.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [25.1.5. .spec.connectionConfig.tlsClientConfig](#spec-connectionconfig-tlsclientconfig-2) Copy linkLink copied to clipboard!

Description
:   tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret must be same as the namespace where the project helm chart repository is getting instantiated.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced secret |

Show more

#### [25.1.6. .status](#status-21) Copy linkLink copied to clipboard!

Description
:   Observed status of the repository within the namespace..

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `conditions` | `array` | conditions is a list of conditions and their statuses |
| `conditions[]` | `object` | Condition contains details for one aspect of the current state of this API Resource. |

Show more

#### [25.1.7. .status.conditions](#status-conditions-17) Copy linkLink copied to clipboard!

Description
:   conditions is a list of conditions and their statuses

Type
:   `array`

#### [25.1.8. .status.conditions[]](#status-conditions-18) Copy linkLink copied to clipboard!

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

### [25.2. API endpoints](#api-endpoints-24) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/helm.openshift.io/v1beta1/projecthelmchartrepositories`

  + `GET`: list objects of kind ProjectHelmChartRepository
* `/apis/helm.openshift.io/v1beta1/namespaces/{namespace}/projecthelmchartrepositories`

  + `DELETE`: delete collection of ProjectHelmChartRepository
  + `GET`: list objects of kind ProjectHelmChartRepository
  + `POST`: create a ProjectHelmChartRepository
* `/apis/helm.openshift.io/v1beta1/namespaces/{namespace}/projecthelmchartrepositories/{name}`

  + `DELETE`: delete a ProjectHelmChartRepository
  + `GET`: read the specified ProjectHelmChartRepository
  + `PATCH`: partially update the specified ProjectHelmChartRepository
  + `PUT`: replace the specified ProjectHelmChartRepository
* `/apis/helm.openshift.io/v1beta1/namespaces/{namespace}/projecthelmchartrepositories/{name}/status`

  + `GET`: read status of the specified ProjectHelmChartRepository
  + `PATCH`: partially update status of the specified ProjectHelmChartRepository
  + `PUT`: replace status of the specified ProjectHelmChartRepository

#### [25.2.1. /apis/helm.openshift.io/v1beta1/projecthelmchartrepositories](#apishelm-openshift-iov1beta1projecthelmchartrepositories) Copy linkLink copied to clipboard!

HTTP method
:   `GET`

Description
:   list objects of kind ProjectHelmChartRepository

Expand

Table 25.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepositoryList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-helm-v1beta1-ProjectHelmChartRepositoryList) schema |
| 401 - Unauthorized | Empty |

Show more

#### [25.2.2. /apis/helm.openshift.io/v1beta1/namespaces/{namespace}/projecthelmchartrepositories](#apishelm-openshift-iov1beta1namespacesnamespaceprojecthelmchartrepositories) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of ProjectHelmChartRepository

Expand

Table 25.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind ProjectHelmChartRepository

Expand

Table 25.3. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepositoryList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-helm-v1beta1-ProjectHelmChartRepositoryList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a ProjectHelmChartRepository

Expand

Table 25.4. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 25.5. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |  |

Show more

Expand

Table 25.6. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 201 - Created | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 202 - Accepted | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [25.2.3. /apis/helm.openshift.io/v1beta1/namespaces/{namespace}/projecthelmchartrepositories/{name}](#apishelm-openshift-iov1beta1namespacesnamespaceprojecthelmchartrepositoriesname) Copy linkLink copied to clipboard!

Expand

Table 25.7. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ProjectHelmChartRepository |

Show more

HTTP method
:   `DELETE`

Description
:   delete a ProjectHelmChartRepository

Expand

Table 25.8. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 25.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified ProjectHelmChartRepository

Expand

Table 25.10. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified ProjectHelmChartRepository

Expand

Table 25.11. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 25.12. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified ProjectHelmChartRepository

Expand

Table 25.13. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 25.14. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |  |

Show more

Expand

Table 25.15. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 201 - Created | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [25.2.4. /apis/helm.openshift.io/v1beta1/namespaces/{namespace}/projecthelmchartrepositories/{name}/status](#apishelm-openshift-iov1beta1namespacesnamespaceprojecthelmchartrepositoriesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 25.16. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the ProjectHelmChartRepository |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified ProjectHelmChartRepository

Expand

Table 25.17. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified ProjectHelmChartRepository

Expand

Table 25.18. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 25.19. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified ProjectHelmChartRepository

Expand

Table 25.20. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 25.21. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |  |

Show more

Expand

Table 25.22. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 201 - Created | [`ProjectHelmChartRepository`](#projecthelmchartrepository-helm-openshift-io-v1beta1 "Chapter 25. ProjectHelmChartRepository [helm.openshift.io/v1beta1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 26. Proxy [config.openshift.io/v1]](#proxy-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Proxy holds cluster-wide information on how to configure default proxies for the cluster. The canonical name is `cluster`

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [26.1. Specification](#specification-25) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user-settable values for the proxy configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [26.1.1. .spec](#spec-25) Copy linkLink copied to clipboard!

Description
:   spec holds user-settable values for the proxy configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `httpProxy` | `string` | httpProxy is the URL of the proxy for HTTP requests. Empty means unset and will not result in an env var. |
| `httpsProxy` | `string` | httpsProxy is the URL of the proxy for HTTPS requests. Empty means unset and will not result in an env var. |
| `noProxy` | `string` | noProxy is a comma-separated list of hostnames and/or CIDRs and/or IPs for which the proxy should not be used. Empty means unset and will not result in an env var. |
| `readinessEndpoints` | `array (string)` | readinessEndpoints is a list of endpoints used to verify readiness of the proxy. |
| `trustedCA` | `object` | trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.  The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):  apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: | -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE----- |

Show more

#### [26.1.2. .spec.trustedCA](#spec-trustedca) Copy linkLink copied to clipboard!

Description
:   trustedCA is a reference to a ConfigMap containing a CA certificate bundle. The trustedCA field should only be consumed by a proxy validator. The validator is responsible for reading the certificate bundle from the required key "ca-bundle.crt", merging it with the system default trust bundle, and writing the merged trust bundle to a ConfigMap named "trusted-ca-bundle" in the "openshift-config-managed" namespace. Clients that expect to make proxy connections must use the trusted-ca-bundle for all HTTPS requests to the proxy, and may use the trusted-ca-bundle for non-proxy HTTPS requests as well.

    The namespace for the ConfigMap referenced by trustedCA is "openshift-config". Here is an example ConfigMap (in yaml):

    apiVersion: v1 kind: ConfigMap metadata: name: user-ca-bundle namespace: openshift-config data: ca-bundle.crt: \| -----BEGIN CERTIFICATE----- Custom CA certificate bundle. -----END CERTIFICATE-----

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [26.1.3. .status](#status-22) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `httpProxy` | `string` | httpProxy is the URL of the proxy for HTTP requests. |
| `httpsProxy` | `string` | httpsProxy is the URL of the proxy for HTTPS requests. |
| `noProxy` | `string` | noProxy is a comma-separated list of hostnames and/or CIDRs for which the proxy should not be used. |

Show more

### [26.2. API endpoints](#api-endpoints-25) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/proxies`

  + `DELETE`: delete collection of Proxy
  + `GET`: list objects of kind Proxy
  + `POST`: create a Proxy
* `/apis/config.openshift.io/v1/proxies/{name}`

  + `DELETE`: delete a Proxy
  + `GET`: read the specified Proxy
  + `PATCH`: partially update the specified Proxy
  + `PUT`: replace the specified Proxy
* `/apis/config.openshift.io/v1/proxies/{name}/status`

  + `GET`: read status of the specified Proxy
  + `PATCH`: partially update status of the specified Proxy
  + `PUT`: replace status of the specified Proxy

#### [26.2.1. /apis/config.openshift.io/v1/proxies](#apisconfig-openshift-iov1proxies) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Proxy

Expand

Table 26.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Proxy

Expand

Table 26.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`ProxyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ProxyList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Proxy

Expand

Table 26.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 26.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 26.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 201 - Created | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [26.2.2. /apis/config.openshift.io/v1/proxies/{name}](#apisconfig-openshift-iov1proxiesname) Copy linkLink copied to clipboard!

Expand

Table 26.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Proxy |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Proxy

Expand

Table 26.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 26.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Proxy

Expand

Table 26.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Proxy

Expand

Table 26.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 26.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Proxy

Expand

Table 26.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 26.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 26.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 201 - Created | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [26.2.3. /apis/config.openshift.io/v1/proxies/{name}/status](#apisconfig-openshift-iov1proxiesnamestatus) Copy linkLink copied to clipboard!

Expand

Table 26.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Proxy |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Proxy

Expand

Table 26.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Proxy

Expand

Table 26.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 26.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Proxy

Expand

Table 26.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 26.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 26.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 201 - Created | [`Proxy`](#proxy-config-openshift-io-v1 "Chapter 26. Proxy [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Chapter 27. Scheduler [config.openshift.io/v1]](#scheduler-config-openshift-io-v1) Copy linkLink copied to clipboard!

Description
:   Scheduler holds cluster-wide config information to run the Kubernetes Scheduler and influence its placement decisions. The canonical name for this config is `cluster`.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `spec`

### [27.1. Specification](#specification-26) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | spec holds user settable values for configuration |
| `status` | `object` | status holds observed values from the cluster. They may not be overridden. |

Show more

#### [27.1.1. .spec](#spec-26) Copy linkLink copied to clipboard!

Description
:   spec holds user settable values for configuration

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultNodeSelector` | `string` | defaultNodeSelector helps set the cluster-wide default node selector to restrict pod placement to specific nodes. This is applied to the pods created in all namespaces and creates an intersection with any existing nodeSelectors already set on a pod, additionally constraining that pod’s selector. For example, defaultNodeSelector: "type=user-node,region=east" would set nodeSelector field in pod spec to "type=user-node,region=east" to all pods created in all namespaces. Namespaces having project-wide node selectors won’t be impacted even if this field is set. This adds an annotation section to the namespace. For example, if a new namespace is created with node-selector='type=user-node,region=east', the annotation openshift.io/node-selector: type=user-node,region=east gets added to the project. When the openshift.io/node-selector annotation is set on the project the value is used in preference to the value we are setting for defaultNodeSelector field. For instance, openshift.io/node-selector: "type=user-node,region=west" means that the default of "type=user-node,region=east" set in defaultNodeSelector would not be applied. |
| `mastersSchedulable` | `boolean` | mastersSchedulable allows masters nodes to be schedulable. When this flag is turned on, all the master nodes in the cluster will be made schedulable, so that workload pods can run on them. The default value for this field is false, meaning none of the master nodes are schedulable. Important Note: Once the workload pods start running on the master nodes, extreme care must be taken to ensure that cluster-critical control plane components are not impacted. Please turn on this field after doing due diligence. |
| `policy` | `object` | DEPRECATED: the scheduler Policy API has been deprecated and will be removed in a future release. policy is a reference to a ConfigMap containing scheduler policy which has user specified predicates and priorities. If this ConfigMap is not available scheduler will default to use DefaultAlgorithmProvider. The namespace for this configmap is openshift-config. |
| `profile` | `string` | profile sets which scheduling profile should be set in order to configure scheduling decisions for new pods.  Valid values are "LowNodeUtilization", "HighNodeUtilization", "NoScoring" Defaults to "LowNodeUtilization" |

Show more

#### [27.1.2. .spec.policy](#spec-policy-3) Copy linkLink copied to clipboard!

Description
:   DEPRECATED: the scheduler Policy API has been deprecated and will be removed in a future release. policy is a reference to a ConfigMap containing scheduler policy which has user specified predicates and priorities. If this ConfigMap is not available scheduler will default to use DefaultAlgorithmProvider. The namespace for this configmap is openshift-config.

Type
:   `object`

Required
:   * `name`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | name is the metadata.name of the referenced config map |

Show more

#### [27.1.3. .status](#status-23) Copy linkLink copied to clipboard!

Description
:   status holds observed values from the cluster. They may not be overridden.

Type
:   `object`

### [27.2. API endpoints](#api-endpoints-26) Copy linkLink copied to clipboard!

The following API endpoints are available:

* `/apis/config.openshift.io/v1/schedulers`

  + `DELETE`: delete collection of Scheduler
  + `GET`: list objects of kind Scheduler
  + `POST`: create a Scheduler
* `/apis/config.openshift.io/v1/schedulers/{name}`

  + `DELETE`: delete a Scheduler
  + `GET`: read the specified Scheduler
  + `PATCH`: partially update the specified Scheduler
  + `PUT`: replace the specified Scheduler
* `/apis/config.openshift.io/v1/schedulers/{name}/status`

  + `GET`: read status of the specified Scheduler
  + `PATCH`: partially update status of the specified Scheduler
  + `PUT`: replace status of the specified Scheduler

#### [27.2.1. /apis/config.openshift.io/v1/schedulers](#apisconfig-openshift-iov1schedulers) Copy linkLink copied to clipboard!

HTTP method
:   `DELETE`

Description
:   delete collection of Scheduler

Expand

Table 27.1. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   list objects of kind Scheduler

Expand

Table 27.2. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`SchedulerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-SchedulerList) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `POST`

Description
:   create a Scheduler

Expand

Table 27.3. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 27.4. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 27.5. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 201 - Created | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 202 - Accepted | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [27.2.2. /apis/config.openshift.io/v1/schedulers/{name}](#apisconfig-openshift-iov1schedulersname) Copy linkLink copied to clipboard!

Expand

Table 27.6. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Scheduler |

Show more

HTTP method
:   `DELETE`

Description
:   delete a Scheduler

Expand

Table 27.7. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Show more

Expand

Table 27.8. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `GET`

Description
:   read the specified Scheduler

Expand

Table 27.9. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update the specified Scheduler

Expand

Table 27.10. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 27.11. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace the specified Scheduler

Expand

Table 27.12. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 27.13. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 27.14. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 201 - Created | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

#### [27.2.3. /apis/config.openshift.io/v1/schedulers/{name}/status](#apisconfig-openshift-iov1schedulersnamestatus) Copy linkLink copied to clipboard!

Expand

Table 27.15. Global path parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | name of the Scheduler |

Show more

HTTP method
:   `GET`

Description
:   read status of the specified Scheduler

Expand

Table 27.16. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PATCH`

Description
:   partially update status of the specified Scheduler

Expand

Table 27.17. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 27.18. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

HTTP method
:   `PUT`

Description
:   replace status of the specified Scheduler

Expand

Table 27.19. Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Show more

Expand

Table 27.20. Body parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `body` | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |  |

Show more

Expand

Table 27.21. HTTP responses

| HTTP code | Reponse body |
| --- | --- |
| 200 - OK | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 201 - Created | [`Scheduler`](#scheduler-config-openshift-io-v1 "Chapter 27. Scheduler [config.openshift.io/v1]") schema |
| 401 - Unauthorized | Empty |

Show more

## [Legal Notice](#idm140338227649984) Copy linkLink copied to clipboard!

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
