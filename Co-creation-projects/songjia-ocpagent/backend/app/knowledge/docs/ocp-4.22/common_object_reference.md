---
title: "Common object reference"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/index
retrieved_at: 2026-09-05T05:41:40.751525+00:00
---

# Common object reference

---

OpenShift Container Platform 4.22

## Reference guide common API objects

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139685483508112)

**Abstract**

This document provides a common API object reference for the OpenShift Container Platform Authorization API.

---

## [Chapter 1. Common object reference](#api-object-reference) Copy linkLink copied to clipboard!

### [1.1. com.coreos.monitoring.v1.AlertmanagerList schema](#com-coreos-monitoring-v1-AlertmanagerList) Copy linkLink copied to clipboard!

Description
:   AlertmanagerList is a list of Alertmanager

Type
:   `object`

Required
:   * `items`

#### [1.1.1. Schema](#schema) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Alertmanager)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertmanager-monitoring-coreos-com-v1) | List of alertmanagers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.2. com.coreos.monitoring.v1.PodMonitorList schema](#com-coreos-monitoring-v1-PodMonitorList) Copy linkLink copied to clipboard!

Description
:   PodMonitorList is a list of PodMonitor

Type
:   `object`

Required
:   * `items`

#### [1.2.1. Schema](#schema-2) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodMonitor)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#podmonitor-monitoring-coreos-com-v1) | List of podmonitors. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.3. com.coreos.monitoring.v1.ProbeList schema](#com-coreos-monitoring-v1-ProbeList) Copy linkLink copied to clipboard!

Description
:   ProbeList is a list of Probe

Type
:   `object`

Required
:   * `items`

#### [1.3.1. Schema](#schema-3) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Probe)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#probe-monitoring-coreos-com-v1) | List of probes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.4. com.coreos.monitoring.v1.PrometheusList schema](#com-coreos-monitoring-v1-PrometheusList) Copy linkLink copied to clipboard!

Description
:   PrometheusList is a list of Prometheus

Type
:   `object`

Required
:   * `items`

#### [1.4.1. Schema](#schema-4) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Prometheus)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#prometheus-monitoring-coreos-com-v1) | List of prometheuses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.5. com.coreos.monitoring.v1.PrometheusRuleList schema](#com-coreos-monitoring-v1-PrometheusRuleList) Copy linkLink copied to clipboard!

Description
:   PrometheusRuleList is a list of PrometheusRule

Type
:   `object`

Required
:   * `items`

#### [1.5.1. Schema](#schema-5) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PrometheusRule)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#prometheusrule-monitoring-coreos-com-v1) | List of prometheusrules. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.6. com.coreos.monitoring.v1.ServiceMonitorList schema](#com-coreos-monitoring-v1-ServiceMonitorList) Copy linkLink copied to clipboard!

Description
:   ServiceMonitorList is a list of ServiceMonitor

Type
:   `object`

Required
:   * `items`

#### [1.6.1. Schema](#schema-6) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceMonitor)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#servicemonitor-monitoring-coreos-com-v1) | List of servicemonitors. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.7. com.coreos.monitoring.v1.ThanosRulerList schema](#com-coreos-monitoring-v1-ThanosRulerList) Copy linkLink copied to clipboard!

Description
:   ThanosRulerList is a list of ThanosRuler

Type
:   `object`

Required
:   * `items`

#### [1.7.1. Schema](#schema-7) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ThanosRuler)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#thanosruler-monitoring-coreos-com-v1) | List of thanosrulers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.8. com.coreos.monitoring.v1beta1.AlertmanagerConfigList schema](#com-coreos-monitoring-v1beta1-AlertmanagerConfigList) Copy linkLink copied to clipboard!

Description
:   AlertmanagerConfigList is a list of AlertmanagerConfig

Type
:   `object`

Required
:   * `items`

#### [1.8.1. Schema](#schema-8) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AlertmanagerConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertmanagerconfig-monitoring-coreos-com-v1beta1) | List of alertmanagerconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.9. com.coreos.operators.v1.OLMConfigList schema](#com-coreos-operators-v1-OLMConfigList) Copy linkLink copied to clipboard!

Description
:   OLMConfigList is a list of OLMConfig

Type
:   `object`

Required
:   * `items`

#### [1.9.1. Schema](#schema-9) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OLMConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#olmconfig-operators-coreos-com-v1) | List of olmconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.10. com.coreos.operators.v1.OperatorGroupList schema](#com-coreos-operators-v1-OperatorGroupList) Copy linkLink copied to clipboard!

Description
:   OperatorGroupList is a list of OperatorGroup

Type
:   `object`

Required
:   * `items`

#### [1.10.1. Schema](#schema-10) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorGroup)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#operatorgroup-operators-coreos-com-v1) | List of operatorgroups. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.11. com.coreos.operators.v1.OperatorList schema](#com-coreos-operators-v1-OperatorList) Copy linkLink copied to clipboard!

Description
:   OperatorList is a list of Operator

Type
:   `object`

Required
:   * `items`

#### [1.11.1. Schema](#schema-11) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Operator)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#operator-operators-coreos-com-v1) | List of operators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.12. com.coreos.operators.v1alpha1.CatalogSourceList schema](#com-coreos-operators-v1alpha1-CatalogSourceList) Copy linkLink copied to clipboard!

Description
:   CatalogSourceList is a list of CatalogSource

Type
:   `object`

Required
:   * `items`

#### [1.12.1. Schema](#schema-12) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CatalogSource)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#catalogsource-operators-coreos-com-v1alpha1) | List of catalogsources. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.13. com.coreos.operators.v1alpha1.ClusterServiceVersionList schema](#com-coreos-operators-v1alpha1-ClusterServiceVersionList) Copy linkLink copied to clipboard!

Description
:   ClusterServiceVersionList is a list of ClusterServiceVersion

Type
:   `object`

Required
:   * `items`

#### [1.13.1. Schema](#schema-13) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterServiceVersion)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#clusterserviceversion-operators-coreos-com-v1alpha1) | List of clusterserviceversions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.14. com.coreos.operators.v1alpha1.InstallPlanList schema](#com-coreos-operators-v1alpha1-InstallPlanList) Copy linkLink copied to clipboard!

Description
:   InstallPlanList is a list of InstallPlan

Type
:   `object`

Required
:   * `items`

#### [1.14.1. Schema](#schema-14) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (InstallPlan)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#installplan-operators-coreos-com-v1alpha1) | List of installplans. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.15. com.coreos.operators.v1alpha1.SubscriptionList schema](#com-coreos-operators-v1alpha1-SubscriptionList) Copy linkLink copied to clipboard!

Description
:   SubscriptionList is a list of Subscription

Type
:   `object`

Required
:   * `items`

#### [1.15.1. Schema](#schema-15) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Subscription)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#subscription-operators-coreos-com-v1alpha1) | List of subscriptions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.16. com.coreos.operators.v2.OperatorConditionList schema](#com-coreos-operators-v2-OperatorConditionList) Copy linkLink copied to clipboard!

Description
:   OperatorConditionList is a list of OperatorCondition

Type
:   `object`

Required
:   * `items`

#### [1.16.1. Schema](#schema-16) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorCondition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#operatorcondition-operators-coreos-com-v2) | List of operatorconditions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.17. com.github.openshift.api.apps.v1.DeploymentConfigList schema](#com-github-openshift-api-apps-v1-DeploymentConfigList) Copy linkLink copied to clipboard!

Description
:   DeploymentConfigList is a collection of deployment configs.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.17.1. Schema](#schema-17) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DeploymentConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deploymentconfig-apps-openshift-io-v1) | items is a list of deployment configs |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.18. com.github.openshift.api.authorization.v1.ClusterRoleBindingList schema](#com-github-openshift-api-authorization-v1-ClusterRoleBindingList) Copy linkLink copied to clipboard!

Description
:   ClusterRoleBindingList is a collection of ClusterRoleBindings

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.18.1. Schema](#schema-18) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRoleBinding)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#clusterrolebinding-authorization-openshift-io-v1) | items is a list of ClusterRoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.19. com.github.openshift.api.authorization.v1.ClusterRoleList schema](#com-github-openshift-api-authorization-v1-ClusterRoleList) Copy linkLink copied to clipboard!

Description
:   ClusterRoleList is a collection of ClusterRoles

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.19.1. Schema](#schema-19) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRole)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#clusterrole-authorization-openshift-io-v1) | items is a list of ClusterRoles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.20. com.github.openshift.api.authorization.v1.RoleBindingList schema](#com-github-openshift-api-authorization-v1-RoleBindingList) Copy linkLink copied to clipboard!

Description
:   RoleBindingList is a collection of RoleBindings

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.20.1. Schema](#schema-20) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RoleBinding)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#rolebinding-authorization-openshift-io-v1) | items is a list of RoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.21. com.github.openshift.api.authorization.v1.RoleList schema](#com-github-openshift-api-authorization-v1-RoleList) Copy linkLink copied to clipboard!

Description
:   RoleList is a collection of Roles

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.21.1. Schema](#schema-21) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Role)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#role-authorization-openshift-io-v1) | items is a list of Roles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.22. com.github.openshift.api.build.v1.BuildConfigList schema](#com-github-openshift-api-build-v1-BuildConfigList) Copy linkLink copied to clipboard!

Description
:   BuildConfigList is a collection of BuildConfigs.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.22.1. Schema](#schema-22) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BuildConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#buildconfig-build-openshift-io-v1) | items is a list of build configs |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.23. com.github.openshift.api.build.v1.BuildList schema](#com-github-openshift-api-build-v1-BuildList) Copy linkLink copied to clipboard!

Description
:   BuildList is a collection of Builds.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.23.1. Schema](#schema-23) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Build)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#build-build-openshift-io-v1) | items is a list of builds |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.24. com.github.openshift.api.image.v1.ImageList schema](#com-github-openshift-api-image-v1-ImageList) Copy linkLink copied to clipboard!

Description
:   ImageList is a list of Image objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.24.1. Schema](#schema-24) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Image)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#image-image-openshift-io-v1) | items is a list of images |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.25. com.github.openshift.api.image.v1.ImageStreamList schema](#com-github-openshift-api-image-v1-ImageStreamList) Copy linkLink copied to clipboard!

Description
:   ImageStreamList is a list of ImageStream objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.25.1. Schema](#schema-25) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageStream)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestream-image-openshift-io-v1) | items is a list of imageStreams |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.26. com.github.openshift.api.image.v1.ImageStreamTagList schema](#com-github-openshift-api-image-v1-ImageStreamTagList) Copy linkLink copied to clipboard!

Description
:   ImageStreamTagList is a list of ImageStreamTag objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.26.1. Schema](#schema-26) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageStreamTag)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestreamtag-image-openshift-io-v1) | items is the list of image stream tags |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.27. com.github.openshift.api.image.v1.ImageTagList schema](#com-github-openshift-api-image-v1-ImageTagList) Copy linkLink copied to clipboard!

Description
:   ImageTagList is a list of ImageTag objects. When listing image tags, the image field is not populated. Tags are returned in alphabetical order by image stream and then tag.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.27.1. Schema](#schema-27) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageTag)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagetag-image-openshift-io-v1) | items is the list of image stream tags |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.28. com.github.openshift.api.oauth.v1.OAuthAccessTokenList schema](#com-github-openshift-api-oauth-v1-OAuthAccessTokenList) Copy linkLink copied to clipboard!

Description
:   OAuthAccessTokenList is a collection of OAuth access tokens

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.28.1. Schema](#schema-28) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthAccessToken)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthaccesstoken-oauth-openshift-io-v1) | items is the list of OAuth access tokens |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.29. com.github.openshift.api.oauth.v1.OAuthAuthorizeTokenList schema](#com-github-openshift-api-oauth-v1-OAuthAuthorizeTokenList) Copy linkLink copied to clipboard!

Description
:   OAuthAuthorizeTokenList is a collection of OAuth authorization tokens

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.29.1. Schema](#schema-29) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthAuthorizeToken)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthauthorizetoken-oauth-openshift-io-v1) | items is the list of OAuth authorization tokens |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.30. com.github.openshift.api.oauth.v1.OAuthClientAuthorizationList schema](#com-github-openshift-api-oauth-v1-OAuthClientAuthorizationList) Copy linkLink copied to clipboard!

Description
:   OAuthClientAuthorizationList is a collection of OAuth client authorizations

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.30.1. Schema](#schema-30) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthClientAuthorization)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthclientauthorization-oauth-openshift-io-v1) | items is the list of OAuth client authorizations |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.31. com.github.openshift.api.oauth.v1.OAuthClientList schema](#com-github-openshift-api-oauth-v1-OAuthClientList) Copy linkLink copied to clipboard!

Description
:   OAuthClientList is a collection of OAuth clients

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.31.1. Schema](#schema-31) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthClient)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthclient-oauth-openshift-io-v1) | items is the list of OAuth clients |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.32. com.github.openshift.api.oauth.v1.UserOAuthAccessTokenList schema](#com-github-openshift-api-oauth-v1-UserOAuthAccessTokenList) Copy linkLink copied to clipboard!

Description
:   UserOAuthAccessTokenList is a collection of access tokens issued on behalf of the requesting user

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.32.1. Schema](#schema-32) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (UserOAuthAccessToken)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#useroauthaccesstoken-oauth-openshift-io-v1) |  |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.33. com.github.openshift.api.project.v1.ProjectList schema](#com-github-openshift-api-project-v1-ProjectList) Copy linkLink copied to clipboard!

Description
:   ProjectList is a list of Project objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.33.1. Schema](#schema-33) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Project)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/project_apis/#project-project-openshift-io-v1) | items is the list of projects |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.34. com.github.openshift.api.quota.v1.AppliedClusterResourceQuotaList schema](#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) Copy linkLink copied to clipboard!

Description
:   AppliedClusterResourceQuotaList is a collection of AppliedClusterResourceQuotas

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.34.1. Schema](#schema-34) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AppliedClusterResourceQuota)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#appliedclusterresourcequota-quota-openshift-io-v1) | items is a list of AppliedClusterResourceQuota |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.35. com.github.openshift.api.route.v1.RouteList schema](#com-github-openshift-api-route-v1-RouteList) Copy linkLink copied to clipboard!

Description
:   RouteList is a collection of Routes.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.35.1. Schema](#schema-35) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Route)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#route-route-openshift-io-v1) | items is a list of routes |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.36. com.github.openshift.api.security.v1.RangeAllocationList schema](#com-github-openshift-api-security-v1-RangeAllocationList) Copy linkLink copied to clipboard!

Description
:   RangeAllocationList is a list of RangeAllocations objects

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.36.1. Schema](#schema-36) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RangeAllocation)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#rangeallocation-security-openshift-io-v1) | List of RangeAllocations. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.37. com.github.openshift.api.template.v1.BrokerTemplateInstanceList schema](#com-github-openshift-api-template-v1-BrokerTemplateInstanceList) Copy linkLink copied to clipboard!

Description
:   BrokerTemplateInstanceList is a list of BrokerTemplateInstance objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.37.1. Schema](#schema-37) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BrokerTemplateInstance)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#brokertemplateinstance-template-openshift-io-v1) | items is a list of BrokerTemplateInstances |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.38. com.github.openshift.api.template.v1.TemplateInstanceList schema](#com-github-openshift-api-template-v1-TemplateInstanceList) Copy linkLink copied to clipboard!

Description
:   TemplateInstanceList is a list of TemplateInstance objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.38.1. Schema](#schema-38) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (TemplateInstance)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#templateinstance-template-openshift-io-v1) | items is a list of Templateinstances |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.39. com.github.openshift.api.template.v1.TemplateList schema](#com-github-openshift-api-template-v1-TemplateList) Copy linkLink copied to clipboard!

Description
:   TemplateList is a list of Template objects.

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.39.1. Schema](#schema-39) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Template)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#template-template-openshift-io-v1) | items is a list of templates |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.40. com.github.openshift.api.user.v1.GroupList schema](#com-github-openshift-api-user-v1-GroupList) Copy linkLink copied to clipboard!

Description
:   GroupList is a collection of Groups

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.40.1. Schema](#schema-40) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Group)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#group-user-openshift-io-v1) | items is the list of groups |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.41. com.github.openshift.api.user.v1.IdentityList schema](#com-github-openshift-api-user-v1-IdentityList) Copy linkLink copied to clipboard!

Description
:   IdentityList is a collection of Identities

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.41.1. Schema](#schema-41) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Identity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#identity-user-openshift-io-v1) | items is the list of identities |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.42. com.github.openshift.api.user.v1.UserList schema](#com-github-openshift-api-user-v1-UserList) Copy linkLink copied to clipboard!

Description
:   UserList is a collection of Users

    Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
:   `object`

Required
:   * `items`

#### [1.42.1. Schema](#schema-42) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (User)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#user-user-openshift-io-v1) | items is the list of users |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.43. com.github.operator-framework.api.pkg.operators.lib.version.OperatorVersion schema](#com-github-operator-framework-api-pkg-operators-lib-version-OperatorVersion) Copy linkLink copied to clipboard!

Description
:   OperatorVersion is a wrapper around semver.Version which supports correct marshaling to YAML and JSON.

Type
:   `string`

### [1.44. com.github.operator-framework.api.pkg.operators.v1alpha1.APIServiceDefinitions schema](#com-github-operator-framework-api-pkg-operators-v1alpha1-APIServiceDefinitions) Copy linkLink copied to clipboard!

Description
:   APIServiceDefinitions declares all of the extension apis managed or required by an operator being ran by ClusterServiceVersion.

Type
:   `object`

#### [1.44.1. Schema](#schema-43) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `owned` | `array (APIServiceDescription)` |  |
| `required` | `array (APIServiceDescription)` |  |

Show more

### [1.45. com.github.operator-framework.api.pkg.operators.v1alpha1.CustomResourceDefinitions schema](#com-github-operator-framework-api-pkg-operators-v1alpha1-CustomResourceDefinitions) Copy linkLink copied to clipboard!

Description
:   CustomResourceDefinitions declares all of the CRDs managed or required by an operator being ran by ClusterServiceVersion.

    If the CRD is present in the Owned list, it is implicitly required.

Type
:   `object`

#### [1.45.1. Schema](#schema-44) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `owned` | `array (CRDDescription)` |  |
| `required` | `array (CRDDescription)` |  |

Show more

### [1.46. com.github.operator-framework.api.pkg.operators.v1alpha1.InstallMode schema](#com-github-operator-framework-api-pkg-operators-v1alpha1-InstallMode) Copy linkLink copied to clipboard!

Description
:   InstallMode associates an InstallModeType with a flag representing if the CSV supports it

Type
:   `object`

Required
:   * `type`
    * `supported`

#### [1.46.1. Schema](#schema-45) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `supported` | `boolean` |  |
| `type` | `string` |  |

Show more

### [1.47. com.github.operator-framework.operator-lifecycle-manager.pkg.package-server.apis.operators.v1.PackageManifestList schema](#com-github-operator-framework-operator-lifecycle-manager-pkg-package-server-apis-operators-v1-PackageManifestList) Copy linkLink copied to clipboard!

Description
:   PackageManifestList is a list of PackageManifest objects.

Type
:   `object`

Required
:   * `items`

#### [1.47.1. Schema](#schema-46) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PackageManifest)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#packagemanifest-packages-operators-coreos-com-v1) |  |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  |

Show more

### [1.48. io.cncf.cni.k8s.v1.NetworkAttachmentDefinitionList schema](#io-cncf-cni-k8s-v1-NetworkAttachmentDefinitionList) Copy linkLink copied to clipboard!

Description
:   NetworkAttachmentDefinitionList is a list of NetworkAttachmentDefinition

Type
:   `object`

Required
:   * `items`

#### [1.48.1. Schema](#schema-47) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NetworkAttachmentDefinition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#networkattachmentdefinition-k8s-cni-cncf-io-v1) | List of network-attachment-definitions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.49. io.cncf.cni.k8s.v1alpha1.IPAMClaimList schema](#io-cncf-cni-k8s-v1alpha1-IPAMClaimList) Copy linkLink copied to clipboard!

Description
:   IPAMClaimList is a list of IPAMClaim

Type
:   `object`

Required
:   * `items`

#### [1.49.1. Schema](#schema-48) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAMClaim)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ipamclaim-k8s-cni-cncf-io-v1alpha1) | List of ipamclaims. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.50. io.cncf.cni.k8s.v1beta1.MultiNetworkPolicyList schema](#io-cncf-cni-k8s-v1beta1-MultiNetworkPolicyList) Copy linkLink copied to clipboard!

Description
:   MultiNetworkPolicyList is a list of MultiNetworkPolicy

Type
:   `object`

Required
:   * `items`

#### [1.50.1. Schema](#schema-49) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MultiNetworkPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#multinetworkpolicy-k8s-cni-cncf-io-v1beta1) | List of multi-networkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.51. io.cncf.cni.whereabouts.v1alpha1.IPPoolList schema](#io-cncf-cni-whereabouts-v1alpha1-IPPoolList) Copy linkLink copied to clipboard!

Description
:   IPPoolList is a list of IPPool

Type
:   `object`

Required
:   * `items`

#### [1.51.1. Schema](#schema-50) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPPool)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ippool-whereabouts-cni-cncf-io-v1alpha1) | List of ippools. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.52. io.cncf.cni.whereabouts.v1alpha1.NodeSlicePoolList schema](#io-cncf-cni-whereabouts-v1alpha1-NodeSlicePoolList) Copy linkLink copied to clipboard!

Description
:   NodeSlicePoolList is a list of NodeSlicePool

Type
:   `object`

Required
:   * `items`

#### [1.52.1. Schema](#schema-51) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NodeSlicePool)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) | List of nodeslicepools. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.53. io.cncf.cni.whereabouts.v1alpha1.OverlappingRangeIPReservationList schema](#io-cncf-cni-whereabouts-v1alpha1-OverlappingRangeIPReservationList) Copy linkLink copied to clipboard!

Description
:   OverlappingRangeIPReservationList is a list of OverlappingRangeIPReservation

Type
:   `object`

Required
:   * `items`

#### [1.53.1. Schema](#schema-52) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OverlappingRangeIPReservation)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) | List of overlappingrangeipreservations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.54. io.k8s.api.admissionregistration.v1.MutatingWebhookConfigurationList schema](#io-k8s-api-admissionregistration-v1-MutatingWebhookConfigurationList) Copy linkLink copied to clipboard!

Description
:   MutatingWebhookConfigurationList is a list of MutatingWebhookConfiguration.

Type
:   `object`

Required
:   * `items`

#### [1.54.1. Schema](#schema-53) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MutatingWebhookConfiguration)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#mutatingwebhookconfiguration-admissionregistration-k8s-io-v1) | List of MutatingWebhookConfiguration. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.55. io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyBindingList schema](#io-k8s-api-admissionregistration-v1-ValidatingAdmissionPolicyBindingList) Copy linkLink copied to clipboard!

Description
:   ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding.

Type
:   `object`

Required
:   * `items`

#### [1.55.1. Schema](#schema-54) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ValidatingAdmissionPolicyBinding)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) | List of PolicyBinding. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.56. io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyList schema](#io-k8s-api-admissionregistration-v1-ValidatingAdmissionPolicyList) Copy linkLink copied to clipboard!

Description
:   ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy.

Type
:   `object`

Required
:   * `items`

#### [1.56.1. Schema](#schema-55) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ValidatingAdmissionPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#validatingadmissionpolicy-admissionregistration-k8s-io-v1) | List of ValidatingAdmissionPolicy. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.57. io.k8s.api.admissionregistration.v1.ValidatingWebhookConfigurationList schema](#io-k8s-api-admissionregistration-v1-ValidatingWebhookConfigurationList) Copy linkLink copied to clipboard!

Description
:   ValidatingWebhookConfigurationList is a list of ValidatingWebhookConfiguration.

Type
:   `object`

Required
:   * `items`

#### [1.57.1. Schema](#schema-56) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ValidatingWebhookConfiguration)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) | List of ValidatingWebhookConfiguration. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.58. io.k8s.api.apps.v1.ControllerRevisionList schema](#io-k8s-api-apps-v1-ControllerRevisionList) Copy linkLink copied to clipboard!

Description
:   ControllerRevisionList is a resource containing a list of ControllerRevision objects.

Type
:   `object`

Required
:   * `items`

#### [1.58.1. Schema](#schema-57) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ControllerRevision)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#controllerrevision-apps-v1) | Items is the list of ControllerRevisions |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.59. io.k8s.api.apps.v1.DaemonSetList schema](#io-k8s-api-apps-v1-DaemonSetList) Copy linkLink copied to clipboard!

Description
:   DaemonSetList is a collection of daemon sets.

Type
:   `object`

Required
:   * `items`

#### [1.59.1. Schema](#schema-58) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DaemonSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#daemonset-apps-v1) | A list of daemon sets. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.60. io.k8s.api.apps.v1.DeploymentList schema](#io-k8s-api-apps-v1-DeploymentList) Copy linkLink copied to clipboard!

Description
:   DeploymentList is a list of Deployments.

Type
:   `object`

Required
:   * `items`

#### [1.60.1. Schema](#schema-59) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Deployment)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deployment-apps-v1) | Items is the list of Deployments. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. |

Show more

### [1.61. io.k8s.api.apps.v1.ReplicaSetList schema](#io-k8s-api-apps-v1-ReplicaSetList) Copy linkLink copied to clipboard!

Description
:   ReplicaSetList is a collection of ReplicaSets.

Type
:   `object`

Required
:   * `items`

#### [1.61.1. Schema](#schema-60) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ReplicaSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#replicaset-apps-v1) | List of ReplicaSets. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.62. io.k8s.api.apps.v1.StatefulSetList schema](#io-k8s-api-apps-v1-StatefulSetList) Copy linkLink copied to clipboard!

Description
:   StatefulSetList is a collection of StatefulSets.

Type
:   `object`

Required
:   * `items`

#### [1.62.1. Schema](#schema-61) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StatefulSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#statefulset-apps-v1) | Items is the list of stateful sets. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.63. io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerList schema](#io-k8s-api-autoscaling-v2-HorizontalPodAutoscalerList) Copy linkLink copied to clipboard!

Description
:   HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.

Type
:   `object`

Required
:   * `items`

#### [1.63.1. Schema](#schema-62) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HorizontalPodAutoscaler)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#horizontalpodautoscaler-autoscaling-v2) | items is the list of horizontal pod autoscaler objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | metadata is the standard list metadata. |

Show more

### [1.64. io.k8s.api.batch.v1.CronJobList schema](#io-k8s-api-batch-v1-CronJobList) Copy linkLink copied to clipboard!

Description
:   CronJobList is a collection of cron jobs.

Type
:   `object`

Required
:   * `items`

#### [1.64.1. Schema](#schema-63) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CronJob)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#cronjob-batch-v1) | items is the list of CronJobs. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.65. io.k8s.api.batch.v1.JobList schema](#io-k8s-api-batch-v1-JobList) Copy linkLink copied to clipboard!

Description
:   JobList is a collection of jobs.

Type
:   `object`

Required
:   * `items`

#### [1.65.1. Schema](#schema-64) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Job)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#job-batch-v1) | items is the list of Jobs. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.66. io.k8s.api.certificates.v1.CertificateSigningRequestList schema](#io-k8s-api-certificates-v1-CertificateSigningRequestList) Copy linkLink copied to clipboard!

Description
:   CertificateSigningRequestList is a collection of CertificateSigningRequest objects

Type
:   `object`

Required
:   * `items`

#### [1.66.1. Schema](#schema-65) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CertificateSigningRequest)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#certificatesigningrequest-certificates-k8s-io-v1) | items is a collection of CertificateSigningRequest objects |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  |

Show more

### [1.67. io.k8s.api.coordination.v1.LeaseList schema](#io-k8s-api-coordination-v1-LeaseList) Copy linkLink copied to clipboard!

Description
:   LeaseList is a list of Lease objects.

Type
:   `object`

Required
:   * `items`

#### [1.67.1. Schema](#schema-66) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Lease)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#lease-coordination-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.68. io.k8s.api.core.v1.ComponentStatusList schema](#io-k8s-api-core-v1-ComponentStatusList) Copy linkLink copied to clipboard!

Description
:   Status of all the conditions for the component as a list of ComponentStatus objects. Deprecated: This API is deprecated in v1.19+

Type
:   `object`

Required
:   * `items`

#### [1.68.1. Schema](#schema-67) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ComponentStatus)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#componentstatus-v1) | List of ComponentStatus objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.69. io.k8s.api.core.v1.ConfigMapList schema](#io-k8s-api-core-v1-ConfigMapList) Copy linkLink copied to clipboard!

Description
:   ConfigMapList is a resource containing a list of ConfigMap objects.

Type
:   `object`

Required
:   * `items`

#### [1.69.1. Schema](#schema-68) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConfigMap)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#configmap-v1) | Items is the list of ConfigMaps. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.70. io.k8s.api.core.v1.ConfigMapVolumeSource schema](#io-k8s-api-core-v1-ConfigMapVolumeSource) Copy linkLink copied to clipboard!

Description
:   Adapts a ConfigMap into a volume.

    The contents of the target ConfigMap’s Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.

Type
:   `object`

#### [1.70.1. Schema](#schema-69) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultMode` | `integer` | defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array (KeyToPath)` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

Show more

### [1.71. io.k8s.api.core.v1.CSIVolumeSource schema](#io-k8s-api-core-v1-CSIVolumeSource) Copy linkLink copied to clipboard!

Description
:   Represents a source location of a volume to mount, managed by an external CSI driver

Type
:   `object`

Required
:   * `driver`

#### [1.71.1. Schema](#schema-70) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `driver` | `string` | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. |
| `fsType` | `string` | fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. |
| `nodePublishSecretRef` | `LocalObjectReference` | nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. |
| `readOnly` | `boolean` | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver’s documentation for supported values. |

Show more

### [1.72. io.k8s.api.core.v1.EndpointsList schema](#io-k8s-api-core-v1-EndpointsList) Copy linkLink copied to clipboard!

Description
:   EndpointsList is a list of endpoints. Deprecated: This API is deprecated in v1.33+.

Type
:   `object`

Required
:   * `items`

#### [1.72.1. Schema](#schema-71) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Endpoints)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#endpoints-v1) | List of endpoints. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.73. io.k8s.api.core.v1.EnvVar schema](#io-k8s-api-core-v1-EnvVar) Copy linkLink copied to clipboard!

Description
:   EnvVar represents an environment variable present in a Container.

Type
:   `object`

Required
:   * `name`

#### [1.73.1. Schema](#schema-72) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the environment variable. May consist of any printable ASCII characters except '='. |
| `value` | `string` | Variable references $(VAR\_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `EnvVarSource` | Source for the environment variable’s value. Cannot be used if value is not empty. |

Show more

### [1.74. io.k8s.api.core.v1.EventList schema](#io-k8s-api-core-v1-EventList) Copy linkLink copied to clipboard!

Description
:   EventList is a list of events.

Type
:   `object`

Required
:   * `items`

#### [1.74.1. Schema](#schema-73) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Event)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#event-v1) | List of events |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.75. io.k8s.api.core.v1.EventSource schema](#io-k8s-api-core-v1-EventSource) Copy linkLink copied to clipboard!

Description
:   EventSource contains information for an event.

Type
:   `object`

#### [1.75.1. Schema](#schema-74) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `component` | `string` | Component from which the event is generated. |
| `host` | `string` | Node name on which the event is generated. |

Show more

### [1.76. io.k8s.api.core.v1.LimitRangeList schema](#io-k8s-api-core-v1-LimitRangeList) Copy linkLink copied to clipboard!

Description
:   LimitRangeList is a list of LimitRange items.

Type
:   `object`

Required
:   * `items`

#### [1.76.1. Schema](#schema-75) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (LimitRange)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#limitrange-v1) | Items is a list of LimitRange objects. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.77. io.k8s.api.core.v1.LocalObjectReference schema](#io-k8s-api-core-v1-LocalObjectReference) Copy linkLink copied to clipboard!

Description
:   LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
:   `object`

#### [1.77.1. Schema](#schema-76) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

Show more

### [1.78. io.k8s.api.core.v1.NamespaceCondition schema](#io-k8s-api-core-v1-NamespaceCondition) Copy linkLink copied to clipboard!

Description
:   NamespaceCondition contains details about state of namespace.

Type
:   `object`

Required
:   * `type`
    * `status`

#### [1.78.1. Schema](#schema-77) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | [`Time`](#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") | Last time the condition transitioned from one status to another. |
| `message` | `string` | Human-readable message indicating details about last transition. |
| `reason` | `string` | Unique, one-word, CamelCase reason for the condition’s last transition. |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of namespace controller condition. |

Show more

### [1.79. io.k8s.api.core.v1.NamespaceList schema](#io-k8s-api-core-v1-NamespaceList) Copy linkLink copied to clipboard!

Description
:   NamespaceList is a list of Namespaces.

Type
:   `object`

Required
:   * `items`

#### [1.79.1. Schema](#schema-78) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Namespace)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#namespace-v1) | Items is the list of Namespace objects in the list. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.80. io.k8s.api.core.v1.NodeList schema](#io-k8s-api-core-v1-NodeList) Copy linkLink copied to clipboard!

Description
:   NodeList is the whole list of all Nodes which have been registered with master.

Type
:   `object`

Required
:   * `items`

#### [1.80.1. Schema](#schema-79) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Node)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#node-v1) | List of nodes |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.81. io.k8s.api.core.v1.NodeSelector schema](#io-k8s-api-core-v1-NodeSelector) Copy linkLink copied to clipboard!

Description
:   A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.

Type
:   `object`

Required
:   * `nodeSelectorTerms`

#### [1.81.1. Schema](#schema-80) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `nodeSelectorTerms` | `array (NodeSelectorTerm)` | Required. A list of node selector terms. The terms are ORed. |

Show more

### [1.82. io.k8s.api.core.v1.ObjectReference schema](#io-k8s-api-core-v1-ObjectReference) Copy linkLink copied to clipboard!

Description
:   ObjectReference contains enough information to let you inspect or modify the referred object.

Type
:   `object`

#### [1.82.1. Schema](#schema-81) Copy linkLink copied to clipboard!

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

### [1.83. io.k8s.api.core.v1.PersistentVolumeClaim schema](#io-k8s-api-core-v1-PersistentVolumeClaim) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaim is a user’s request for and claim to a persistent volume

Type
:   `object`

#### [1.83.1. Schema](#schema-82) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta "1.142. io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |
| `status` | `object` | PersistentVolumeClaimStatus is the current status of a persistent volume claim. |

Show more

**.spec**

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
| `selector` | [`LabelSelector`](#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector "1.138. io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector schema") | selector is a label query over volumes to consider for binding. |
| `storageClassName` | `string` | storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1> |
| `volumeAttributesClassName` | `string` | volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string or nil value indicates that no VolumeAttributesClass will be applied to the claim. If the claim enters an Infeasible error state, this field can be reset to its previous value (including nil) to cancel the modification. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/> |
| `volumeMode` | `string` | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.  Possible enum values: - `"Block"` means the volume will not be formatted with a filesystem and will remain a raw block device. - `"Filesystem"` means the volume will be or is formatted with a filesystem. |
| `volumeName` | `string` | volumeName is the binding reference to the PersistentVolume backing this claim. |

Show more

**.spec.dataSource**

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

**.spec.dataSourceRef**

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

**.spec.resources**

Description
:   VolumeResourceRequirements describes the storage resource requirements for a volume.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `limits` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

**.status**

Description
:   PersistentVolumeClaimStatus is the current status of a persistent volume claim.

Type
:   `object`

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessModes` | `array (string)` | accessModes contains the actual access modes the volume backing the PVC has. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1> |
| `allocatedResourceStatuses` | `object (string)` | allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: \* Un-prefixed keys: - storage - the capacity of the volume. \* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states: - ControllerResizeInProgress: State set when resize controller starts resizing the volume in control-plane. - ControllerResizeFailed: State set when resize has failed in resize controller with a terminal error. - NodeResizePending: State set when resize controller has finished resizing the volume but further resizing of volume is needed on the node. - NodeResizeInProgress: State set when kubelet starts resizing the volume. - NodeResizeFailed: State set when resizing has failed in kubelet with a terminal error. Transient errors don’t set NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC. |
| `allocatedResources` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: \* Un-prefixed keys: - storage - the capacity of the volume. \* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC. |
| `capacity` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | capacity represents the actual resources of the underlying volume. |
| `conditions` | `array` | conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'. |
| `conditions[]` | `object` | PersistentVolumeClaimCondition contains details about state of pvc |
| `currentVolumeAttributesClassName` | `string` | currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim |
| `modifyVolumeStatus` | `object` | ModifyVolumeStatus represents the status object of ControllerModifyVolume operation |
| `phase` | `string` | phase represents the current phase of PersistentVolumeClaim.  Possible enum values: - `"Bound"` used for PersistentVolumeClaims that are bound - `"Lost"` used for PersistentVolumeClaims that lost their underlying PersistentVolume. The claim was bound to a PersistentVolume and this volume does not exist any longer and all data on it was lost. - `"Pending"` used for PersistentVolumeClaims that are not yet bound |

Show more

**.status.conditions**

Description
:   conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.

Type
:   `array`

**.status.conditions[]**

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
| `lastProbeTime` | [`Time`](#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") | lastProbeTime is the time we probed the condition. |
| `lastTransitionTime` | [`Time`](#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") | lastTransitionTime is the time the condition transitioned from one status to another. |
| `message` | `string` | message is the human-readable message indicating details about last transition. |
| `reason` | `string` | reason is a unique, this should be a short, machine understandable string that gives the reason for condition’s last transition. If it reports "Resizing" that means the underlying persistent volume is being resized. |
| `status` | `string` | Status is the status of the condition. Can be True, False, Unknown. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=state%20of%20pvc-,conditions.status,-(string)%2C%20required> |
| `type` | `string` | Type is the type of the condition. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about> |

Show more

**.status.modifyVolumeStatus**

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

### [1.84. io.k8s.api.core.v1.PersistentVolumeClaimList schema](#io-k8s-api-core-v1-PersistentVolumeClaimList) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeClaimList is a list of PersistentVolumeClaim items.

Type
:   `object`

Required
:   * `items`

#### [1.84.1. Schema](#schema-83) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PersistentVolumeClaim)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#persistentvolumeclaim-v1) | items is a list of persistent volume claims. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.85. io.k8s.api.core.v1.PersistentVolumeList schema](#io-k8s-api-core-v1-PersistentVolumeList) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeList is a list of PersistentVolume items.

Type
:   `object`

Required
:   * `items`

#### [1.85.1. Schema](#schema-84) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PersistentVolume)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#persistentvolume-v1) | items is a list of persistent volumes. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.86. io.k8s.api.core.v1.PersistentVolumeSpec schema](#io-k8s-api-core-v1-PersistentVolumeSpec) Copy linkLink copied to clipboard!

Description
:   PersistentVolumeSpec is the specification of a persistent volume.

Type
:   `object`

#### [1.86.1. Schema](#schema-85) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `accessModes` | `array (string)` | accessModes contains all ways the volume can be mounted. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes> |
| `awsElasticBlockStore` | `AWSElasticBlockStoreVolumeSource` | awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `azureDisk` | `AzureDiskVolumeSource` | azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver. |
| `azureFile` | `AzureFilePersistentVolumeSource` | azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver. |
| `capacity` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | capacity is the description of the persistent volume’s resources and capacity. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity> |
| `cephfs` | `CephFSPersistentVolumeSource` | cephFS represents a Ceph FS mount on the host that shares a pod’s lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported. |
| `cinder` | `CinderPersistentVolumeSource` | cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `claimRef` | [`ObjectReference`](#io-k8s-api-core-v1-ObjectReference "1.82. io.k8s.api.core.v1.ObjectReference schema") | claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding> |
| `csi` | `CSIPersistentVolumeSource` | csi represents storage that is handled by an external CSI driver. |
| `fc` | `FCVolumeSource` | fc represents a Fibre Channel resource that is attached to a kubelet’s host machine and then exposed to the pod. |
| `flexVolume` | `FlexPersistentVolumeSource` | flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead. |
| `flocker` | `FlockerVolumeSource` | flocker represents a Flocker volume attached to a kubelet’s host machine and exposed to the pod for its usage. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported. |
| `gcePersistentDisk` | `GCEPersistentDiskVolumeSource` | gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Provisioned by an admin. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `glusterfs` | `GlusterfsPersistentVolumeSource` | glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. More info: <https://examples.k8s.io/volumes/glusterfs/README.md> |
| `hostPath` | `HostPathVolumeSource` | hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath> |
| `iscsi` | `ISCSIPersistentVolumeSource` | iscsi represents an ISCSI Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Provisioned by an admin. |
| `local` | `LocalVolumeSource` | local represents directly-attached storage with node affinity |
| `mountOptions` | `array (string)` | mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options> |
| `nfs` | `NFSVolumeSource` | nfs represents an NFS mount on the host. Provisioned by an admin. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `nodeAffinity` | `VolumeNodeAffinity` | nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume. This field is mutable if MutablePVNodeAffinity feature gate is enabled. |
| `persistentVolumeReclaimPolicy` | `string` | persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming>  Possible enum values: - `"Delete"` means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - `"Recycle"` means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - `"Retain"` means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain. |
| `photonPersistentDisk` | `PhotonPersistentDiskVolumeSource` | photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported. |
| `portworxVolume` | `PortworxVolumeSource` | portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on. |
| `quobyte` | `QuobyteVolumeSource` | quobyte represents a Quobyte mount on the host that shares a pod’s lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported. |
| `rbd` | `RBDPersistentVolumeSource` | rbd represents a Rados Block Device mount on the host that shares a pod’s lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. More info: <https://examples.k8s.io/volumes/rbd/README.md> |
| `scaleIO` | `ScaleIOPersistentVolumeSource` | scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported. |
| `storageClassName` | `string` | storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. |
| `storageos` | `StorageOSPersistentVolumeSource` | storageOS represents a StorageOS volume that is attached to the kubelet’s host machine and mounted into the pod. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported. More info: <https://examples.k8s.io/volumes/storageos/README.md> |
| `volumeAttributesClassName` | `string` | Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. |
| `volumeMode` | `string` | volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.  Possible enum values: - `"Block"` means the volume will not be formatted with a filesystem and will remain a raw block device. - `"Filesystem"` means the volume will be or is formatted with a filesystem. |
| `vsphereVolume` | `VsphereVirtualDiskVolumeSource` | vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver. |

Show more

### [1.87. io.k8s.api.core.v1.PodList schema](#io-k8s-api-core-v1-PodList) Copy linkLink copied to clipboard!

Description
:   PodList is a list of Pods.

Type
:   `object`

Required
:   * `items`

#### [1.87.1. Schema](#schema-86) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Pod)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#pod-v1) | List of pods. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.88. io.k8s.api.core.v1.PodTemplateList schema](#io-k8s-api-core-v1-PodTemplateList) Copy linkLink copied to clipboard!

Description
:   PodTemplateList is a list of PodTemplates.

Type
:   `object`

Required
:   * `items`

#### [1.88.1. Schema](#schema-87) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodTemplate)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#podtemplate-v1) | List of pod templates |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.89. io.k8s.api.core.v1.PodTemplateSpec schema](#io-k8s-api-core-v1-PodTemplateSpec) Copy linkLink copied to clipboard!

Description
:   PodTemplateSpec describes the data a pod should have when created from a template

Type
:   `object`

#### [1.89.1. Schema](#schema-88) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `metadata` | [`ObjectMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta "1.142. io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `PodSpec` | Specification of the desired behavior of the pod. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

Show more

### [1.90. io.k8s.api.core.v1.ReplicationControllerList schema](#io-k8s-api-core-v1-ReplicationControllerList) Copy linkLink copied to clipboard!

Description
:   ReplicationControllerList is a collection of replication controllers.

Type
:   `object`

Required
:   * `items`

#### [1.90.1. Schema](#schema-89) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ReplicationController)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#replicationcontroller-v1) | List of replication controllers. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.91. io.k8s.api.core.v1.ResourceQuotaList schema](#io-k8s-api-core-v1-ResourceQuotaList) Copy linkLink copied to clipboard!

Description
:   ResourceQuotaList is a list of ResourceQuota items.

Type
:   `object`

Required
:   * `items`

#### [1.91.1. Schema](#schema-90) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ResourceQuota)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourcequota-v1) | Items is a list of ResourceQuota objects. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.92. io.k8s.api.core.v1.ResourceQuotaSpec schema](#io-k8s-api-core-v1-ResourceQuotaSpec) Copy linkLink copied to clipboard!

Description
:   ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

Type
:   `object`

#### [1.92.1. Schema](#schema-91) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hard` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `scopeSelector` | `ScopeSelector` | scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. |
| `scopes` | `array (string)` | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. |

Show more

### [1.93. io.k8s.api.core.v1.ResourceQuotaStatus schema](#io-k8s-api-core-v1-ResourceQuotaStatus) Copy linkLink copied to clipboard!

Description
:   ResourceQuotaStatus defines the enforced hard limits and observed use.

Type
:   `object`

#### [1.93.1. Schema](#schema-92) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `hard` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `used` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | Used is the current observed total usage of the resource in the namespace. |

Show more

### [1.94. io.k8s.api.core.v1.ResourceRequirements schema](#io-k8s-api-core-v1-ResourceRequirements) Copy linkLink copied to clipboard!

Description
:   ResourceRequirements describes the compute resource requirements.

Type
:   `object`

#### [1.94.1. Schema](#schema-93) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `claims` | `array (ResourceClaim)` | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. |
| `limits` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Show more

### [1.95. io.k8s.api.core.v1.Secret schema](#io-k8s-api-core-v1-Secret) Copy linkLink copied to clipboard!

Description
:   Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes.

Type
:   `object`

#### [1.95.1. Schema](#schema-94) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `data` | `object (string)` | Data contains the secret data. Each key must consist of alphanumeric characters, '-', '\_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in <https://tools.ietf.org/html/rfc4648#section-4> |
| `immutable` | `boolean` | Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta "1.142. io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `stringData` | `object (string)` | stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. |
| `type` | `string` | Used to facilitate programmatic handling of secret data. More info: <https://kubernetes.io/docs/concepts/configuration/secret/#secret-types> |

Show more

### [1.96. io.k8s.api.core.v1.SecretList schema](#io-k8s-api-core-v1-SecretList) Copy linkLink copied to clipboard!

Description
:   SecretList is a list of Secret.

Type
:   `object`

Required
:   * `items`

#### [1.96.1. Schema](#schema-95) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Secret)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#secret-v1) | Items is a list of secret objects. More info: <https://kubernetes.io/docs/concepts/configuration/secret> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.97. io.k8s.api.core.v1.SecretVolumeSource schema](#io-k8s-api-core-v1-SecretVolumeSource) Copy linkLink copied to clipboard!

Description
:   Adapts a Secret into a volume.

    The contents of the target Secret’s Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.

Type
:   `object`

#### [1.97.1. Schema](#schema-96) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `defaultMode` | `integer` | defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array (KeyToPath)` | items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `optional` | `boolean` | optional field specify whether the Secret or its keys must be defined |
| `secretName` | `string` | secretName is the name of the secret in the pod’s namespace to use. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret> |

Show more

### [1.98. io.k8s.api.core.v1.ServiceAccountList schema](#io-k8s-api-core-v1-ServiceAccountList) Copy linkLink copied to clipboard!

Description
:   ServiceAccountList is a list of ServiceAccount objects

Type
:   `object`

Required
:   * `items`

#### [1.98.1. Schema](#schema-97) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceAccount)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#serviceaccount-v1) | List of ServiceAccounts. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.99. io.k8s.api.core.v1.ServiceList schema](#io-k8s-api-core-v1-ServiceList) Copy linkLink copied to clipboard!

Description
:   ServiceList holds a list of services.

Type
:   `object`

Required
:   * `items`

#### [1.99.1. Schema](#schema-98) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Service)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#service-v1) | List of services |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.100. io.k8s.api.core.v1.Toleration schema](#io-k8s-api-core-v1-Toleration) Copy linkLink copied to clipboard!

Description
:   The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.

Type
:   `object`

#### [1.100.1. Schema](#schema-99) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `effect` | `string` | Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.  Possible enum values: - `"NoExecute"` Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController. - `"NoSchedule"` Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler. - `"PreferNoSchedule"` Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler. |
| `key` | `string` | Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. |
| `operator` | `string` | Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators).  Possible enum values: - `"Equal"` - `"Exists"` - `"Gt"` - `"Lt"` |
| `tolerationSeconds` | `integer` | TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. |
| `value` | `string` | Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. |

Show more

### [1.101. io.k8s.api.core.v1.TopologySelectorTerm schema](#io-k8s-api-core-v1-TopologySelectorTerm) Copy linkLink copied to clipboard!

Description
:   A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.

Type
:   `object`

#### [1.101.1. Schema](#schema-100) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchLabelExpressions` | `array (TopologySelectorLabelRequirement)` | A list of topology selector requirements by labels. |

Show more

### [1.102. io.k8s.api.core.v1.TypedLocalObjectReference schema](#io-k8s-api-core-v1-TypedLocalObjectReference) Copy linkLink copied to clipboard!

Description
:   TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

Type
:   `object`

Required
:   * `kind`
    * `name`

#### [1.102.1. Schema](#schema-101) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

Show more

### [1.103. io.k8s.api.discovery.v1.EndpointSliceList schema](#io-k8s-api-discovery-v1-EndpointSliceList) Copy linkLink copied to clipboard!

Description
:   EndpointSliceList represents a list of endpoint slices

Type
:   `object`

Required
:   * `items`

#### [1.103.1. Schema](#schema-102) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EndpointSlice)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#endpointslice-discovery-k8s-io-v1) | items is the list of endpoint slices |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. |

Show more

### [1.104. io.k8s.api.events.v1.EventList schema](#io-k8s-api-events-v1-EventList) Copy linkLink copied to clipboard!

Description
:   EventList is a list of Event objects.

Type
:   `object`

Required
:   * `items`

#### [1.104.1. Schema](#schema-103) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Event)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#event-events-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.105. io.k8s.api.flowcontrol.v1.FlowSchemaList schema](#io-k8s-api-flowcontrol-v1-FlowSchemaList) Copy linkLink copied to clipboard!

Description
:   FlowSchemaList is a list of FlowSchema objects.

Type
:   `object`

Required
:   * `items`

#### [1.105.1. Schema](#schema-104) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (FlowSchema)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#flowschema-flowcontrol-apiserver-k8s-io-v1) | `items` is a list of FlowSchemas. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | `metadata` is the standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.106. io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationList schema](#io-k8s-api-flowcontrol-v1-PriorityLevelConfigurationList) Copy linkLink copied to clipboard!

Description
:   PriorityLevelConfigurationList is a list of PriorityLevelConfiguration objects.

Type
:   `object`

Required
:   * `items`

#### [1.106.1. Schema](#schema-105) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PriorityLevelConfiguration)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1) | `items` is a list of request-priorities. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | `metadata` is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.107. io.k8s.api.networking.v1.IngressClassList schema](#io-k8s-api-networking-v1-IngressClassList) Copy linkLink copied to clipboard!

Description
:   IngressClassList is a collection of IngressClasses.

Type
:   `object`

Required
:   * `items`

#### [1.107.1. Schema](#schema-106) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IngressClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ingressclass-networking-k8s-io-v1) | items is the list of IngressClasses. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. |

Show more

### [1.108. io.k8s.api.networking.v1.IngressList schema](#io-k8s-api-networking-v1-IngressList) Copy linkLink copied to clipboard!

Description
:   IngressList is a collection of Ingress.

Type
:   `object`

Required
:   * `items`

#### [1.108.1. Schema](#schema-107) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Ingress)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ingress-networking-k8s-io-v1) | items is the list of Ingress. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.109. io.k8s.api.networking.v1.IPAddressList schema](#io-k8s-api-networking-v1-IPAddressList) Copy linkLink copied to clipboard!

Description
:   IPAddressList contains a list of IPAddress.

Type
:   `object`

Required
:   * `items`

#### [1.109.1. Schema](#schema-108) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAddress)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ipaddress-networking-k8s-io-v1) | items is the list of IPAddresses. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.110. io.k8s.api.networking.v1.NetworkPolicyList schema](#io-k8s-api-networking-v1-NetworkPolicyList) Copy linkLink copied to clipboard!

Description
:   NetworkPolicyList is a list of NetworkPolicy objects.

Type
:   `object`

Required
:   * `items`

#### [1.110.1. Schema](#schema-109) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NetworkPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#networkpolicy-networking-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.111. io.k8s.api.networking.v1.ServiceCIDRList schema](#io-k8s-api-networking-v1-ServiceCIDRList) Copy linkLink copied to clipboard!

Description
:   ServiceCIDRList contains a list of ServiceCIDR objects.

Type
:   `object`

Required
:   * `items`

#### [1.111.1. Schema](#schema-110) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceCIDR)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#servicecidr-networking-k8s-io-v1) | items is the list of ServiceCIDRs. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.112. io.k8s.api.node.v1.RuntimeClassList schema](#io-k8s-api-node-v1-RuntimeClassList) Copy linkLink copied to clipboard!

Description
:   RuntimeClassList is a list of RuntimeClass objects.

Type
:   `object`

Required
:   * `items`

#### [1.112.1. Schema](#schema-111) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RuntimeClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#runtimeclass-node-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.113. io.k8s.api.policy.v1.PodDisruptionBudgetList schema](#io-k8s-api-policy-v1-PodDisruptionBudgetList) Copy linkLink copied to clipboard!

Description
:   PodDisruptionBudgetList is a collection of PodDisruptionBudgets.

Type
:   `object`

Required
:   * `items`

#### [1.113.1. Schema](#schema-112) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodDisruptionBudget)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/policy_apis/#poddisruptionbudget-policy-v1) | Items is a list of PodDisruptionBudgets |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.114. io.k8s.api.rbac.v1.AggregationRule schema](#io-k8s-api-rbac-v1-AggregationRule) Copy linkLink copied to clipboard!

Description
:   AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

Type
:   `object`

#### [1.114.1. Schema](#schema-113) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `clusterRoleSelectors` | `array (LabelSelector)` | ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole’s permissions will be added |

Show more

### [1.115. io.k8s.api.rbac.v1.ClusterRoleBindingList schema](#io-k8s-api-rbac-v1-ClusterRoleBindingList) Copy linkLink copied to clipboard!

Description
:   ClusterRoleBindingList is a collection of ClusterRoleBindings

Type
:   `object`

Required
:   * `items`

#### [1.115.1. Schema](#schema-114) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRoleBinding)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#clusterrolebinding-rbac-authorization-k8s-io-v1) | Items is a list of ClusterRoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. |

Show more

### [1.116. io.k8s.api.rbac.v1.ClusterRoleList schema](#io-k8s-api-rbac-v1-ClusterRoleList) Copy linkLink copied to clipboard!

Description
:   ClusterRoleList is a collection of ClusterRoles

Type
:   `object`

Required
:   * `items`

#### [1.116.1. Schema](#schema-115) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRole)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#clusterrole-rbac-authorization-k8s-io-v1) | Items is a list of ClusterRoles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. |

Show more

### [1.117. io.k8s.api.rbac.v1.RoleBindingList schema](#io-k8s-api-rbac-v1-RoleBindingList) Copy linkLink copied to clipboard!

Description
:   RoleBindingList is a collection of RoleBindings

Type
:   `object`

Required
:   * `items`

#### [1.117.1. Schema](#schema-116) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RoleBinding)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#rolebinding-rbac-authorization-k8s-io-v1) | Items is a list of RoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. |

Show more

### [1.118. io.k8s.api.rbac.v1.RoleList schema](#io-k8s-api-rbac-v1-RoleList) Copy linkLink copied to clipboard!

Description
:   RoleList is a collection of Roles

Type
:   `object`

Required
:   * `items`

#### [1.118.1. Schema](#schema-117) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Role)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#role-rbac-authorization-k8s-io-v1) | Items is a list of Roles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata. |

Show more

### [1.119. io.k8s.api.resource.v1.DeviceClassList schema](#io-k8s-api-resource-v1-DeviceClassList) Copy linkLink copied to clipboard!

Description
:   DeviceClassList is a collection of classes.

Type
:   `object`

Required
:   * `items`

#### [1.119.1. Schema](#schema-118) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DeviceClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#deviceclass-resource-k8s-io-v1) | Items is the list of resource classes. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata |

Show more

### [1.120. io.k8s.api.resource.v1.ResourceClaimList schema](#io-k8s-api-resource-v1-ResourceClaimList) Copy linkLink copied to clipboard!

Description
:   ResourceClaimList is a collection of claims.

Type
:   `object`

Required
:   * `items`

#### [1.120.1. Schema](#schema-119) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ResourceClaim)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourceclaim-resource-k8s-io-v1) | Items is the list of resource claims. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata |

Show more

### [1.121. io.k8s.api.resource.v1.ResourceClaimTemplateList schema](#io-k8s-api-resource-v1-ResourceClaimTemplateList) Copy linkLink copied to clipboard!

Description
:   ResourceClaimTemplateList is a collection of claim templates.

Type
:   `object`

Required
:   * `items`

#### [1.121.1. Schema](#schema-120) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ResourceClaimTemplate)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourceclaimtemplate-resource-k8s-io-v1) | Items is the list of resource claim templates. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata |

Show more

### [1.122. io.k8s.api.resource.v1.ResourceSliceList schema](#io-k8s-api-resource-v1-ResourceSliceList) Copy linkLink copied to clipboard!

Description
:   ResourceSliceList is a collection of ResourceSlices.

Type
:   `object`

Required
:   * `items`

#### [1.122.1. Schema](#schema-121) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ResourceSlice)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourceslice-resource-k8s-io-v1) | Items is the list of resource ResourceSlices. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata |

Show more

### [1.123. io.k8s.api.scheduling.v1.PriorityClassList schema](#io-k8s-api-scheduling-v1-PriorityClassList) Copy linkLink copied to clipboard!

Description
:   PriorityClassList is a collection of priority classes.

Type
:   `object`

Required
:   * `items`

#### [1.123.1. Schema](#schema-122) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PriorityClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#priorityclass-scheduling-k8s-io-v1) | items is the list of PriorityClasses |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.124. io.k8s.api.storage.v1.CSIDriverList schema](#io-k8s-api-storage-v1-CSIDriverList) Copy linkLink copied to clipboard!

Description
:   CSIDriverList is a collection of CSIDriver objects.

Type
:   `object`

Required
:   * `items`

#### [1.124.1. Schema](#schema-123) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSIDriver)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#csidriver-storage-k8s-io-v1) | items is the list of CSIDriver |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.125. io.k8s.api.storage.v1.CSINodeList schema](#io-k8s-api-storage-v1-CSINodeList) Copy linkLink copied to clipboard!

Description
:   CSINodeList is a collection of CSINode objects.

Type
:   `object`

Required
:   * `items`

#### [1.125.1. Schema](#schema-124) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSINode)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#csinode-storage-k8s-io-v1) | items is the list of CSINode |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.126. io.k8s.api.storage.v1.CSIStorageCapacityList schema](#io-k8s-api-storage-v1-CSIStorageCapacityList) Copy linkLink copied to clipboard!

Description
:   CSIStorageCapacityList is a collection of CSIStorageCapacity objects.

Type
:   `object`

Required
:   * `items`

#### [1.126.1. Schema](#schema-125) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSIStorageCapacity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#csistoragecapacity-storage-k8s-io-v1) | items is the list of CSIStorageCapacity objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.127. io.k8s.api.storage.v1.StorageClassList schema](#io-k8s-api-storage-v1-StorageClassList) Copy linkLink copied to clipboard!

Description
:   StorageClassList is a collection of storage classes.

Type
:   `object`

Required
:   * `items`

#### [1.127.1. Schema](#schema-126) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StorageClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#storageclass-storage-k8s-io-v1) | items is the list of StorageClasses |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.128. io.k8s.api.storage.v1.VolumeAttachmentList schema](#io-k8s-api-storage-v1-VolumeAttachmentList) Copy linkLink copied to clipboard!

Description
:   VolumeAttachmentList is a collection of VolumeAttachment objects.

Type
:   `object`

Required
:   * `items`

#### [1.128.1. Schema](#schema-127) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeAttachment)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumeattachment-storage-k8s-io-v1) | items is the list of VolumeAttachments |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.129. io.k8s.api.storage.v1.VolumeAttributesClassList schema](#io-k8s-api-storage-v1-VolumeAttributesClassList) Copy linkLink copied to clipboard!

Description
:   VolumeAttributesClassList is a collection of VolumeAttributesClass objects.

Type
:   `object`

Required
:   * `items`

#### [1.129.1. Schema](#schema-128) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeAttributesClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumeattributesclass-storage-k8s-io-v1) | items is the list of VolumeAttributesClass objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.130. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionList schema](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-CustomResourceDefinitionList) Copy linkLink copied to clipboard!

Description
:   CustomResourceDefinitionList is a list of CustomResourceDefinition objects.

Type
:   `object`

Required
:   * `items`

#### [1.130.1. Schema](#schema-129) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CustomResourceDefinition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#customresourcedefinition-apiextensions-k8s-io-v1) | items list individual CustomResourceDefinition objects |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard object’s metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps) Copy linkLink copied to clipboard!

Description
:   JSONSchemaProps is a JSON-Schema following Specification Draft 4 (<http://json-schema.org/>).

Type
:   `object`

#### [1.131.1. Schema](#schema-130) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `$ref` | `string` |  |
| `$schema` | `string` |  |
| `additionalItems` | `` |  |
| `additionalProperties` | `` |  |
| `allOf` | [`array (undefined)`](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `anyOf` | [`array (undefined)`](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `default` | `JSON` | default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false. |
| `definitions` | [`object (undefined)`](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `dependencies` | `object (undefined)` |  |
| `description` | `string` |  |
| `enum` | `array (JSON)` |  |
| `example` | `JSON` |  |
| `exclusiveMaximum` | `boolean` |  |
| `exclusiveMinimum` | `boolean` |  |
| `externalDocs` | `ExternalDocumentation` |  |
| `format` | `string` | format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like "0321751043" or "978-0321751041" - isbn10: an ISBN10 number string like "0321751043" - isbn13: an ISBN13 number string like "978-0321751041" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: an hexadecimal color code like "FFFFFF: following the regex ^?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like "rgb(255,255,2559" - byte: base64 encoded binary data - password: any kind of string - date: a date string like "2006-01-02" as defined by full-date in RFC3339 - duration: a duration string like "22 ns" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like "2014-12-15T19:30:20.000Z" as defined by date-time in RFC3339. |
| `id` | `string` |  |
| `items` | `` |  |
| `maxItems` | `integer` |  |
| `maxLength` | `integer` |  |
| `maxProperties` | `integer` |  |
| `maximum` | `number` |  |
| `minItems` | `integer` |  |
| `minLength` | `integer` |  |
| `minProperties` | `integer` |  |
| `minimum` | `number` |  |
| `multipleOf` | `number` |  |
| `not` | [``](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `nullable` | `boolean` |  |
| `oneOf` | [`array (undefined)`](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `pattern` | `string` |  |
| `patternProperties` | [`object (undefined)`](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `properties` | [`object (undefined)`](#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps "1.131. io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema") |  |
| `required` | `array (string)` |  |
| `title` | `string` |  |
| `type` | `string` |  |
| `uniqueItems` | `boolean` |  |
| `x-kubernetes-embedded-resource` | `boolean` | x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata). |
| `x-kubernetes-int-or-string` | `boolean` | x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:  1) anyOf: - type: integer - type: string 2) allOf: - anyOf: - type: integer - type: string - …​ zero or more |
| `x-kubernetes-list-map-keys` | `array (string)` | x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type `map` by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the "x-kubernetes-list-type" extension set to "map". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).  The properties specified must either be required or have a default value, to ensure those properties are present for all list items. |
| `x-kubernetes-list-type` | `string` | x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) `atomic`: the list is treated as a single entity, like a scalar. Atomic lists will be entirely replaced when updated. This extension may be used on any type of list (struct, scalar, …​). 2) `set`: Sets are lists that must not have multiple items with the same value. Each value must be a scalar, an object with x-kubernetes-map-type `atomic` or an array with x-kubernetes-list-type `atomic`. 3) `map`: These lists are like maps in that their elements have a non-index key used to identify them. Order is preserved upon merge. The map tag must only be used on a list with elements of type object. Defaults to atomic for arrays. |
| `x-kubernetes-map-type` | `string` | x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:  1) `granular`: These maps are actual maps (key-value pairs) and each fields are independent from each other (they can each be manipulated by separate actors). This is the default behaviour for all maps. 2) `atomic`: the list is treated as a single entity, like a scalar. Atomic maps will be entirely replaced when updated. |
| `x-kubernetes-preserve-unknown-fields` | `boolean` | x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. |
| `x-kubernetes-validations` | `array (ValidationRule)` | x-kubernetes-validations describes a list of validation rules written in the CEL expression language. |

Show more

### [1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema](#io-k8s-apimachinery-pkg-api-resource-Quantity) Copy linkLink copied to clipboard!

Description
:   Quantity is a fixed-point representation of a number. It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors.

    The serialization format is:

    ```
    <quantity>        ::= <signedNumber><suffix>
    ```

    ```
    (Note that <suffix> may be empty, from the "" case in <decimalSI>.)
    ```

    <digit> ::= 0 \| 1 \| …​ \| 9 <digits> ::= <digit> \| <digit><digits> <number> ::= <digits> \| <digits>.<digits> \| <digits>. \| .<digits> <sign> ::= "+" \| "-" <signedNumber> ::= <number> \| <sign><number> <suffix> ::= <binarySI> \| <decimalExponent> \| <decimalSI> <binarySI> ::= Ki \| Mi \| Gi \| Ti \| Pi \| Ei

    ```
    (International System of units; See: http://physics.nist.gov/cuu/Units/binary.html)
    ```

    <decimalSI> ::= m \| "" \| k \| M \| G \| T \| P \| E

    ```
    (Note that 1024 = 1Ki but 1000 = 1k; I didn't choose the capitalization.)
    ```

    <decimalExponent> ::= "e" <signedNumber> \| "E" <signedNumber>

    No matter which of the three exponent forms is used, no quantity may represent a number greater than 2^63-1 in magnitude, nor may it have more than 3 decimal places. Numbers larger or more precise will be capped or rounded up. (E.g.: 0.1m will rounded up to 1m.) This may be extended in the future if we require larger or smaller quantities.

    When a Quantity is parsed from a string, it will remember the type of suffix it had, and will use the same type again when it is serialized.

    Before serializing, Quantity will be put in "canonical form". This means that Exponent/suffix will be adjusted up or down (with a corresponding increase or decrease in Mantissa) such that:

    * No precision is lost - No fractional digits will be emitted - The exponent (or suffix) is as large as possible.

    The sign will be omitted unless the number is negative.

    Examples:

    * 1.5 will be serialized as "1500m" - 1.5Gi will be serialized as "1536Mi"

    Note that the quantity will NEVER be internally represented by a floating point number. That is the whole point of this exercise.

    Non-canonical values will still parse as long as they are well formed, but will be re-emitted in their canonical form. (So always use canonical form, or don’t diff.)

    This format is intended to make it difficult to use these numbers without writing some sort of special handling code in the hopes that that will cause implementors to also use a fixed point implementation.

Type
:   `string`

### [1.133. io.k8s.apimachinery.pkg.apis.meta.v1.Condition schema](#io-k8s-apimachinery-pkg-apis-meta-v1-Condition) Copy linkLink copied to clipboard!

Description
:   Condition contains details for one aspect of the current state of this API Resource.

Type
:   `object`

Required
:   * `type`
    * `status`
    * `lastTransitionTime`
    * `reason`
    * `message`

#### [1.133.1. Schema](#schema-131) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `lastTransitionTime` | [`Time`](#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

Show more

### [1.134. io.k8s.apimachinery.pkg.apis.meta.v1.DeleteOptions schema](#io-k8s-apimachinery-pkg-apis-meta-v1-DeleteOptions) Copy linkLink copied to clipboard!

Description
:   DeleteOptions may be provided when deleting an API object.

Type
:   `object`

#### [1.134.1. Schema](#schema-132) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `dryRun` | `array (string)` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `gracePeriodSeconds` | `integer` | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. |
| `ignoreStoreReadErrorWithClusterBreakingPotential` | `boolean` | if set to true, it will trigger an unsafe deletion of the resource in case the normal deletion flow fails with a corrupt object error. A resource is considered corrupt if it can not be retrieved from the underlying storage successfully because of a) its data can not be transformed e.g. decryption failure, or b) it fails to decode into an object. NOTE: unsafe deletion ignores finalizer constraints, skips precondition checks, and removes the object from the storage. WARNING: This may potentially break the cluster if the workload associated with the resource being unsafe-deleted relies on normal deletion flow. Use only if you REALLY know what you are doing. The default value is false, and the user must opt in to enable it |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `orphanDependents` | `boolean` | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added to/removed from the object’s finalizers list. Either this field or PropagationPolicy may be set, but not both. |
| `preconditions` | `Preconditions` | Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned. |
| `propagationPolicy` | `string` | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. |

Show more

### [1.135. io.k8s.apimachinery.pkg.apis.meta.v1.Duration schema](#io-k8s-apimachinery-pkg-apis-meta-v1-Duration) Copy linkLink copied to clipboard!

Description
:   Duration is a wrapper around time.Duration which supports correct marshaling to YAML and JSON. In particular, it marshals into strings, which can be used as map keys in json.

Type
:   `string`

### [1.136. io.k8s.apimachinery.pkg.apis.meta.v1.FieldSelectorRequirement schema](#io-k8s-apimachinery-pkg-apis-meta-v1-FieldSelectorRequirement) Copy linkLink copied to clipboard!

Description
:   FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

#### [1.136.1. Schema](#schema-133) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the field selector key that the requirement applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. |

Show more

### [1.137. io.k8s.apimachinery.pkg.apis.meta.v1.GroupVersionKind schema](#io-k8s-apimachinery-pkg-apis-meta-v1-GroupVersionKind) Copy linkLink copied to clipboard!

Description
:   GroupVersionKind unambiguously identifies a kind. It doesn’t anonymously include GroupVersion to avoid automatic coercion. It doesn’t use a GroupVersion to avoid custom marshalling

Type
:   `object`

Required
:   * `group`
    * `version`
    * `kind`

#### [1.137.1. Schema](#schema-134) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `group` | `string` |  |
| `kind` | `string` |  |
| `version` | `string` |  |

Show more

### [1.138. io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector schema](#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) Copy linkLink copied to clipboard!

Description
:   A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.

Type
:   `object`

#### [1.138.1. Schema](#schema-135) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `matchExpressions` | [`array (LabelSelectorRequirement)`](#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement "1.139. io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement schema") | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

Show more

### [1.139. io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement schema](#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement) Copy linkLink copied to clipboard!

Description
:   A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
:   `object`

Required
:   * `key`
    * `operator`

#### [1.139.1. Schema](#schema-136) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

Show more

### [1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) Copy linkLink copied to clipboard!

Description
:   ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.

Type
:   `object`

#### [1.140.1. Schema](#schema-137) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `continue` | `string` | continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message. |
| `remainingItemCount` | `integer` | remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is **estimating** the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact. |
| `resourceVersion` | `string` | String that identifies the server’s internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `selfLink` | `string` | Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. |

Show more

### [1.141. io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime schema](#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) Copy linkLink copied to clipboard!

Description
:   MicroTime is version of Time with microsecond level precision.

Type
:   `string`

### [1.142. io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta schema](#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) Copy linkLink copied to clipboard!

Description
:   ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

Type
:   `object`

#### [1.142.1. Schema](#schema-138) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `annotations` | `object (string)` | Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations> |
| `creationTimestamp` | [`Time`](#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") | CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `deletionGracePeriodSeconds` | `integer` | Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only. |
| `deletionTimestamp` | [`Time`](#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") | DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `finalizers` | `array (string)` | Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list. |
| `generateName` | `string` | GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will return a 409.  Applied only if Name is not specified. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency> |
| `generation` | `integer` | A sequence number representing a specific generation of the desired state. Populated by the system. Read-only. |
| `labels` | `object (string)` | Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels> |
| `managedFields` | `array (ManagedFieldsEntry)` | ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn’t need to set or understand this field. A workflow can be the user’s name, a controller’s name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object. |
| `name` | `string` | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names> |
| `namespace` | `string` | Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS\_LABEL. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces> |
| `ownerReferences` | `array (OwnerReference)` | List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller. |
| `resourceVersion` | `string` | An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `selfLink` | `string` | Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. |
| `uid` | `string` | UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids> |

Show more

### [1.143. io.k8s.apimachinery.pkg.apis.meta.v1.Status schema](#io-k8s-apimachinery-pkg-apis-meta-v1-Status) Copy linkLink copied to clipboard!

Description
:   Status is a return value for calls that don’t return other objects.

Type
:   `object`

#### [1.143.1. Schema](#schema-139) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

Show more

### [1.144. io.k8s.apimachinery.pkg.apis.meta.v1.Status\_v2 schema](#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) Copy linkLink copied to clipboard!

Description
:   Status is a return value for calls that don’t return other objects.

Type
:   `object`

#### [1.144.1. Schema](#schema-140) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

Show more

### [1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema](#io-k8s-apimachinery-pkg-apis-meta-v1-Time) Copy linkLink copied to clipboard!

Description
:   Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.

Type
:   `string`

### [1.146. io.k8s.apimachinery.pkg.apis.meta.v1.WatchEvent schema](#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) Copy linkLink copied to clipboard!

Description
:   Event represents a single event to a watched resource.

Type
:   `object`

Required
:   * `type`
    * `object`

#### [1.146.1. Schema](#schema-141) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `object` | [`RawExtension`](#io-k8s-apimachinery-pkg-runtime-RawExtension "1.147. io.k8s.apimachinery.pkg.runtime.RawExtension schema") | Object is: \* If Type is Added or Modified: the new state of the object. \* If Type is Deleted: the state of the object immediately before deletion. \* If Type is Error: \*Status is recommended; other types may make sense depending on context. |
| `type` | `string` |  |

Show more

### [1.147. io.k8s.apimachinery.pkg.runtime.RawExtension schema](#io-k8s-apimachinery-pkg-runtime-RawExtension) Copy linkLink copied to clipboard!

Description
:   RawExtension is used to hold extensions in external versions.

    To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.

    ```
    type MyAPIObject struct {
    	runtime.TypeMeta `json:",inline"`
    	MyPlugin runtime.Object `json:"myPlugin"`
    }
    ```

    ```
    type PluginA struct {
    	AOption string `json:"aOption"`
    }
    ```

    ```
    type MyAPIObject struct {
    	runtime.TypeMeta `json:",inline"`
    	MyPlugin runtime.RawExtension `json:"myPlugin"`
    }
    ```

    ```
    type PluginA struct {
    	AOption string `json:"aOption"`
    }
    ```

    ```
    {
    	"kind":"MyAPIObject",
    	"apiVersion":"v1",
    	"myPlugin": {
    		"kind":"PluginA",
    		"aOption":"foo",
    	},
    }
    ```

    So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package’s DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)

Type
:   `object`

### [1.148. io.k8s.apimachinery.pkg.util.intstr.IntOrString schema](#io-k8s-apimachinery-pkg-util-intstr-IntOrString) Copy linkLink copied to clipboard!

Description
:   IntOrString is a type that can hold an int32 or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a name or number.

Type
:   `string`

### [1.149. io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceList schema](#io-k8s-kube-aggregator-pkg-apis-apiregistration-v1-APIServiceList) Copy linkLink copied to clipboard!

Description
:   APIServiceList is a list of APIService objects.

Type
:   `object`

Required
:   * `items`

#### [1.149.1. Schema](#schema-142) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (APIService)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#apiservice-apiregistration-k8s-io-v1) | Items is the list of APIService |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

Show more

### [1.150. io.k8s.metrics.pkg.apis.metrics.v1beta1.NodeMetricsList schema](#io-k8s-metrics-pkg-apis-metrics-v1beta1-NodeMetricsList) Copy linkLink copied to clipboard!

Description
:   NodeMetricsList is a list of NodeMetrics.

Type
:   `object`

Required
:   * `items`

#### [1.150.1. Schema](#schema-143) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NodeMetrics)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#nodemetrics-metrics-k8s-io-v1beta1) | List of node metrics. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.151. io.k8s.metrics.pkg.apis.metrics.v1beta1.PodMetricsList schema](#io-k8s-metrics-pkg-apis-metrics-v1beta1-PodMetricsList) Copy linkLink copied to clipboard!

Description
:   PodMetricsList is a list of PodMetrics.

Type
:   `object`

Required
:   * `items`

#### [1.151.1. Schema](#schema-144) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodMetrics)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#podmetrics-metrics-k8s-io-v1beta1) | List of pod metrics. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.152. io.k8s.migration.v1alpha1.StorageStateList schema](#io-k8s-migration-v1alpha1-StorageStateList) Copy linkLink copied to clipboard!

Description
:   StorageStateList is a list of StorageState

Type
:   `object`

Required
:   * `items`

#### [1.152.1. Schema](#schema-145) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StorageState)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#storagestate-migration-k8s-io-v1alpha1) | List of storagestates. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.153. io.k8s.migration.v1alpha1.StorageVersionMigrationList schema](#io-k8s-migration-v1alpha1-StorageVersionMigrationList) Copy linkLink copied to clipboard!

Description
:   StorageVersionMigrationList is a list of StorageVersionMigration

Type
:   `object`

Required
:   * `items`

#### [1.153.1. Schema](#schema-146) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StorageVersionMigration)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#storageversionmigration-migration-k8s-io-v1alpha1) | List of storageversionmigrations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.154. io.k8s.networking.gateway.v1.BackendTLSPolicyList schema](#io-k8s-networking-gateway-v1-BackendTLSPolicyList) Copy linkLink copied to clipboard!

Description
:   BackendTLSPolicyList is a list of BackendTLSPolicy

Type
:   `object`

Required
:   * `items`

#### [1.154.1. Schema](#schema-147) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BackendTLSPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#backendtlspolicy-gateway-networking-k8s-io-v1) | List of backendtlspolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.155. io.k8s.networking.gateway.v1.GatewayClassList schema](#io-k8s-networking-gateway-v1-GatewayClassList) Copy linkLink copied to clipboard!

Description
:   GatewayClassList is a list of GatewayClass

Type
:   `object`

Required
:   * `items`

#### [1.155.1. Schema](#schema-148) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (GatewayClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#gatewayclass-gateway-networking-k8s-io-v1) | List of gatewayclasses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.156. io.k8s.networking.gateway.v1.GatewayList schema](#io-k8s-networking-gateway-v1-GatewayList) Copy linkLink copied to clipboard!

Description
:   GatewayList is a list of Gateway

Type
:   `object`

Required
:   * `items`

#### [1.156.1. Schema](#schema-149) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Gateway)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#gateway-gateway-networking-k8s-io-v1) | List of gateways. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.157. io.k8s.networking.gateway.v1.GRPCRouteList schema](#io-k8s-networking-gateway-v1-GRPCRouteList) Copy linkLink copied to clipboard!

Description
:   GRPCRouteList is a list of GRPCRoute

Type
:   `object`

Required
:   * `items`

#### [1.157.1. Schema](#schema-150) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (GRPCRoute)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#grpcroute-gateway-networking-k8s-io-v1) | List of grpcroutes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.158. io.k8s.networking.gateway.v1.HTTPRouteList schema](#io-k8s-networking-gateway-v1-HTTPRouteList) Copy linkLink copied to clipboard!

Description
:   HTTPRouteList is a list of HTTPRoute

Type
:   `object`

Required
:   * `items`

#### [1.158.1. Schema](#schema-151) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HTTPRoute)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#httproute-gateway-networking-k8s-io-v1) | List of httproutes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.159. io.k8s.networking.gateway.v1beta1.ReferenceGrantList schema](#io-k8s-networking-gateway-v1beta1-ReferenceGrantList) Copy linkLink copied to clipboard!

Description
:   ReferenceGrantList is a list of ReferenceGrant

Type
:   `object`

Required
:   * `items`

#### [1.159.1. Schema](#schema-152) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ReferenceGrant)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#referencegrant-gateway-networking-k8s-io-v1beta1) | List of referencegrants. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.160. io.k8s.networking.policy.v1alpha1.AdminNetworkPolicyList schema](#io-k8s-networking-policy-v1alpha1-AdminNetworkPolicyList) Copy linkLink copied to clipboard!

Description
:   AdminNetworkPolicyList is a list of AdminNetworkPolicy

Type
:   `object`

Required
:   * `items`

#### [1.160.1. Schema](#schema-153) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AdminNetworkPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#adminnetworkpolicy-policy-networking-k8s-io-v1alpha1) | List of adminnetworkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.161. io.k8s.networking.policy.v1alpha1.BaselineAdminNetworkPolicyList schema](#io-k8s-networking-policy-v1alpha1-BaselineAdminNetworkPolicyList) Copy linkLink copied to clipboard!

Description
:   BaselineAdminNetworkPolicyList is a list of BaselineAdminNetworkPolicy

Type
:   `object`

Required
:   * `items`

#### [1.161.1. Schema](#schema-154) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BaselineAdminNetworkPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1) | List of baselineadminnetworkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.162. io.k8s.storage.populator.v1beta1.VolumePopulatorList schema](#io-k8s-storage-populator-v1beta1-VolumePopulatorList) Copy linkLink copied to clipboard!

Description
:   VolumePopulatorList is a list of VolumePopulator

Type
:   `object`

Required
:   * `items`

#### [1.162.1. Schema](#schema-155) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumePopulator)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumepopulator-populator-storage-k8s-io-v1beta1) | List of volumepopulators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.163. io.k8s.storage.snapshot.v1.VolumeSnapshotClassList schema](#io-k8s-storage-snapshot-v1-VolumeSnapshotClassList) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotClassList is a list of VolumeSnapshotClass

Type
:   `object`

Required
:   * `items`

#### [1.163.1. Schema](#schema-156) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeSnapshotClass)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumesnapshotclass-snapshot-storage-k8s-io-v1) | List of volumesnapshotclasses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.164. io.k8s.storage.snapshot.v1.VolumeSnapshotContentList schema](#io-k8s-storage-snapshot-v1-VolumeSnapshotContentList) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotContentList is a list of VolumeSnapshotContent

Type
:   `object`

Required
:   * `items`

#### [1.164.1. Schema](#schema-157) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeSnapshotContent)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumesnapshotcontent-snapshot-storage-k8s-io-v1) | List of volumesnapshotcontents. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.165. io.k8s.storage.snapshot.v1.VolumeSnapshotList schema](#io-k8s-storage-snapshot-v1-VolumeSnapshotList) Copy linkLink copied to clipboard!

Description
:   VolumeSnapshotList is a list of VolumeSnapshot

Type
:   `object`

Required
:   * `items`

#### [1.165.1. Schema](#schema-158) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeSnapshot)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumesnapshot-snapshot-storage-k8s-io-v1) | List of volumesnapshots. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.166. io.metal3.v1alpha1.BareMetalHostList schema](#io-metal3-v1alpha1-BareMetalHostList) Copy linkLink copied to clipboard!

Description
:   BareMetalHostList is a list of BareMetalHost

Type
:   `object`

Required
:   * `items`

#### [1.166.1. Schema](#schema-159) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BareMetalHost)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#baremetalhost-metal3-io-v1alpha1) | List of baremetalhosts. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.167. io.metal3.v1alpha1.BMCEventSubscriptionList schema](#io-metal3-v1alpha1-BMCEventSubscriptionList) Copy linkLink copied to clipboard!

Description
:   BMCEventSubscriptionList is a list of BMCEventSubscription

Type
:   `object`

Required
:   * `items`

#### [1.167.1. Schema](#schema-160) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BMCEventSubscription)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#bmceventsubscription-metal3-io-v1alpha1) | List of bmceventsubscriptions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.168. io.metal3.v1alpha1.DataImageList schema](#io-metal3-v1alpha1-DataImageList) Copy linkLink copied to clipboard!

Description
:   DataImageList is a list of DataImage

Type
:   `object`

Required
:   * `items`

#### [1.168.1. Schema](#schema-161) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DataImage)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#dataimage-metal3-io-v1alpha1) | List of dataimages. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.169. io.metal3.v1alpha1.FirmwareSchemaList schema](#io-metal3-v1alpha1-FirmwareSchemaList) Copy linkLink copied to clipboard!

Description
:   FirmwareSchemaList is a list of FirmwareSchema

Type
:   `object`

Required
:   * `items`

#### [1.169.1. Schema](#schema-162) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (FirmwareSchema)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#firmwareschema-metal3-io-v1alpha1) | List of firmwareschemas. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.170. io.metal3.v1alpha1.HardwareDataList schema](#io-metal3-v1alpha1-HardwareDataList) Copy linkLink copied to clipboard!

Description
:   HardwareDataList is a list of HardwareData

Type
:   `object`

Required
:   * `items`

#### [1.170.1. Schema](#schema-163) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HardwareData)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hardwaredata-metal3-io-v1alpha1) | List of hardwaredata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.171. io.metal3.v1alpha1.HostFirmwareComponentsList schema](#io-metal3-v1alpha1-HostFirmwareComponentsList) Copy linkLink copied to clipboard!

Description
:   HostFirmwareComponentsList is a list of HostFirmwareComponents

Type
:   `object`

Required
:   * `items`

#### [1.171.1. Schema](#schema-164) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HostFirmwareComponents)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hostfirmwarecomponents-metal3-io-v1alpha1) | List of hostfirmwarecomponents. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.172. io.metal3.v1alpha1.HostFirmwareSettingsList schema](#io-metal3-v1alpha1-HostFirmwareSettingsList) Copy linkLink copied to clipboard!

Description
:   HostFirmwareSettingsList is a list of HostFirmwareSettings

Type
:   `object`

Required
:   * `items`

#### [1.172.1. Schema](#schema-165) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HostFirmwareSettings)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hostfirmwaresettings-metal3-io-v1alpha1) | List of hostfirmwaresettings. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.173. io.metal3.v1alpha1.HostUpdatePolicyList schema](#io-metal3-v1alpha1-HostUpdatePolicyList) Copy linkLink copied to clipboard!

Description
:   HostUpdatePolicyList is a list of HostUpdatePolicy

Type
:   `object`

Required
:   * `items`

#### [1.173.1. Schema](#schema-166) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HostUpdatePolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hostupdatepolicy-metal3-io-v1alpha1) | List of hostupdatepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.174. io.metal3.v1alpha1.PreprovisioningImageList schema](#io-metal3-v1alpha1-PreprovisioningImageList) Copy linkLink copied to clipboard!

Description
:   PreprovisioningImageList is a list of PreprovisioningImage

Type
:   `object`

Required
:   * `items`

#### [1.174.1. Schema](#schema-167) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PreprovisioningImage)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#preprovisioningimage-metal3-io-v1alpha1) | List of preprovisioningimages. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.175. io.metal3.v1alpha1.ProvisioningList schema](#io-metal3-v1alpha1-ProvisioningList) Copy linkLink copied to clipboard!

Description
:   ProvisioningList is a list of Provisioning

Type
:   `object`

Required
:   * `items`

#### [1.175.1. Schema](#schema-168) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Provisioning)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#provisioning-metal3-io-v1alpha1) | List of provisionings. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.176. io.openshift.apiserver.v1.APIRequestCountList schema](#io-openshift-apiserver-v1-APIRequestCountList) Copy linkLink copied to clipboard!

Description
:   APIRequestCountList is a list of APIRequestCount

Type
:   `object`

Required
:   * `items`

#### [1.176.1. Schema](#schema-169) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (APIRequestCount)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#apirequestcount-apiserver-openshift-io-v1) | List of apirequestcounts. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.177. io.openshift.authorization.v1.RoleBindingRestrictionList schema](#io-openshift-authorization-v1-RoleBindingRestrictionList) Copy linkLink copied to clipboard!

Description
:   RoleBindingRestrictionList is a list of RoleBindingRestriction

Type
:   `object`

Required
:   * `items`

#### [1.177.1. Schema](#schema-170) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RoleBindingRestriction)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#rolebindingrestriction-authorization-openshift-io-v1) | List of rolebindingrestrictions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.178. io.openshift.autoscaling.v1.ClusterAutoscalerList schema](#io-openshift-autoscaling-v1-ClusterAutoscalerList) Copy linkLink copied to clipboard!

Description
:   ClusterAutoscalerList is a list of ClusterAutoscaler

Type
:   `object`

Required
:   * `items`

#### [1.178.1. Schema](#schema-171) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterAutoscaler)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#clusterautoscaler-autoscaling-openshift-io-v1) | List of clusterautoscalers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.179. io.openshift.autoscaling.v1beta1.MachineAutoscalerList schema](#io-openshift-autoscaling-v1beta1-MachineAutoscalerList) Copy linkLink copied to clipboard!

Description
:   MachineAutoscalerList is a list of MachineAutoscaler

Type
:   `object`

Required
:   * `items`

#### [1.179.1. Schema](#schema-172) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineAutoscaler)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#machineautoscaler-autoscaling-openshift-io-v1beta1) | List of machineautoscalers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.180. io.openshift.cloudcredential.v1.CredentialsRequestList schema](#io-openshift-cloudcredential-v1-CredentialsRequestList) Copy linkLink copied to clipboard!

Description
:   CredentialsRequestList is a list of CredentialsRequest

Type
:   `object`

Required
:   * `items`

#### [1.180.1. Schema](#schema-173) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CredentialsRequest)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#credentialsrequest-cloudcredential-openshift-io-v1) | List of credentialsrequests. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.181. io.openshift.config.v1.APIServerList schema](#io-openshift-config-v1-APIServerList) Copy linkLink copied to clipboard!

Description
:   APIServerList is a list of APIServer

Type
:   `object`

Required
:   * `items`

#### [1.181.1. Schema](#schema-174) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (APIServer)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#apiserver-config-openshift-io-v1) | List of apiservers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.182. io.openshift.config.v1.AuthenticationList schema](#io-openshift-config-v1-AuthenticationList) Copy linkLink copied to clipboard!

Description
:   AuthenticationList is a list of Authentication

Type
:   `object`

Required
:   * `items`

#### [1.182.1. Schema](#schema-175) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Authentication)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#authentication-config-openshift-io-v1) | List of authentications. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.183. io.openshift.config.v1.BuildList schema](#io-openshift-config-v1-BuildList) Copy linkLink copied to clipboard!

Description
:   BuildList is a list of Build

Type
:   `object`

Required
:   * `items`

#### [1.183.1. Schema](#schema-176) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Build)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#build-config-openshift-io-v1) | List of builds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.184. io.openshift.config.v1.ClusterImagePolicyList schema](#io-openshift-config-v1-ClusterImagePolicyList) Copy linkLink copied to clipboard!

Description
:   ClusterImagePolicyList is a list of ClusterImagePolicy

Type
:   `object`

Required
:   * `items`

#### [1.184.1. Schema](#schema-177) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterImagePolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#clusterimagepolicy-config-openshift-io-v1) | List of clusterimagepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.185. io.openshift.config.v1.ClusterOperatorList schema](#io-openshift-config-v1-ClusterOperatorList) Copy linkLink copied to clipboard!

Description
:   ClusterOperatorList is a list of ClusterOperator

Type
:   `object`

Required
:   * `items`

#### [1.185.1. Schema](#schema-178) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterOperator)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#clusteroperator-config-openshift-io-v1) | List of clusteroperators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.186. io.openshift.config.v1.ClusterVersionList schema](#io-openshift-config-v1-ClusterVersionList) Copy linkLink copied to clipboard!

Description
:   ClusterVersionList is a list of ClusterVersion

Type
:   `object`

Required
:   * `items`

#### [1.186.1. Schema](#schema-179) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterVersion)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#clusterversion-config-openshift-io-v1) | List of clusterversions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.187. io.openshift.config.v1.ConsoleList schema](#io-openshift-config-v1-ConsoleList) Copy linkLink copied to clipboard!

Description
:   ConsoleList is a list of Console

Type
:   `object`

Required
:   * `items`

#### [1.187.1. Schema](#schema-180) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Console)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#console-config-openshift-io-v1) | List of consoles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.188. io.openshift.config.v1.DNSList schema](#io-openshift-config-v1-DNSList) Copy linkLink copied to clipboard!

Description
:   DNSList is a list of DNS

Type
:   `object`

Required
:   * `items`

#### [1.188.1. Schema](#schema-181) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DNS)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#dns-config-openshift-io-v1) | List of dnses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.189. io.openshift.config.v1.FeatureGateList schema](#io-openshift-config-v1-FeatureGateList) Copy linkLink copied to clipboard!

Description
:   FeatureGateList is a list of FeatureGate

Type
:   `object`

Required
:   * `items`

#### [1.189.1. Schema](#schema-182) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (FeatureGate)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#featuregate-config-openshift-io-v1) | List of featuregates. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.190. io.openshift.config.v1.ImageContentPolicyList schema](#io-openshift-config-v1-ImageContentPolicyList) Copy linkLink copied to clipboard!

Description
:   ImageContentPolicyList is a list of ImageContentPolicy

Type
:   `object`

Required
:   * `items`

#### [1.190.1. Schema](#schema-183) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageContentPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagecontentpolicy-config-openshift-io-v1) | List of imagecontentpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.191. io.openshift.config.v1.ImageDigestMirrorSetList schema](#io-openshift-config-v1-ImageDigestMirrorSetList) Copy linkLink copied to clipboard!

Description
:   ImageDigestMirrorSetList is a list of ImageDigestMirrorSet

Type
:   `object`

Required
:   * `items`

#### [1.191.1. Schema](#schema-184) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageDigestMirrorSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagedigestmirrorset-config-openshift-io-v1) | List of imagedigestmirrorsets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.192. io.openshift.config.v1.ImageList schema](#io-openshift-config-v1-ImageList) Copy linkLink copied to clipboard!

Description
:   ImageList is a list of Image

Type
:   `object`

Required
:   * `items`

#### [1.192.1. Schema](#schema-185) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Image)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#image-config-openshift-io-v1) | List of images. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.193. io.openshift.config.v1.ImagePolicyList schema](#io-openshift-config-v1-ImagePolicyList) Copy linkLink copied to clipboard!

Description
:   ImagePolicyList is a list of ImagePolicy

Type
:   `object`

Required
:   * `items`

#### [1.193.1. Schema](#schema-186) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImagePolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagepolicy-config-openshift-io-v1) | List of imagepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.194. io.openshift.config.v1.ImageTagMirrorSetList schema](#io-openshift-config-v1-ImageTagMirrorSetList) Copy linkLink copied to clipboard!

Description
:   ImageTagMirrorSetList is a list of ImageTagMirrorSet

Type
:   `object`

Required
:   * `items`

#### [1.194.1. Schema](#schema-187) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageTagMirrorSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagetagmirrorset-config-openshift-io-v1) | List of imagetagmirrorsets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.195. io.openshift.config.v1.InfrastructureList schema](#io-openshift-config-v1-InfrastructureList) Copy linkLink copied to clipboard!

Description
:   InfrastructureList is a list of Infrastructure

Type
:   `object`

Required
:   * `items`

#### [1.195.1. Schema](#schema-188) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Infrastructure)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#infrastructure-config-openshift-io-v1) | List of infrastructures. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.196. io.openshift.config.v1.IngressList schema](#io-openshift-config-v1-IngressList) Copy linkLink copied to clipboard!

Description
:   IngressList is a list of Ingress

Type
:   `object`

Required
:   * `items`

#### [1.196.1. Schema](#schema-189) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Ingress)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#ingress-config-openshift-io-v1) | List of ingresses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.197. io.openshift.config.v1.InsightsDataGatherList schema](#io-openshift-config-v1-InsightsDataGatherList) Copy linkLink copied to clipboard!

Description
:   InsightsDataGatherList is a list of InsightsDataGather

Type
:   `object`

Required
:   * `items`

#### [1.197.1. Schema](#schema-190) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (InsightsDataGather)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#insightsdatagather-config-openshift-io-v1) | List of insightsdatagathers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.198. io.openshift.config.v1.NetworkList schema](#io-openshift-config-v1-NetworkList) Copy linkLink copied to clipboard!

Description
:   NetworkList is a list of Network

Type
:   `object`

Required
:   * `items`

#### [1.198.1. Schema](#schema-191) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Network)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#network-config-openshift-io-v1) | List of networks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.199. io.openshift.config.v1.NodeList schema](#io-openshift-config-v1-NodeList) Copy linkLink copied to clipboard!

Description
:   NodeList is a list of Node

Type
:   `object`

Required
:   * `items`

#### [1.199.1. Schema](#schema-192) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Node)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#node-config-openshift-io-v1) | List of nodes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.200. io.openshift.config.v1.OAuthList schema](#io-openshift-config-v1-OAuthList) Copy linkLink copied to clipboard!

Description
:   OAuthList is a list of OAuth

Type
:   `object`

Required
:   * `items`

#### [1.200.1. Schema](#schema-193) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuth)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#oauth-config-openshift-io-v1) | List of oauths. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.201. io.openshift.config.v1.OperatorHubList schema](#io-openshift-config-v1-OperatorHubList) Copy linkLink copied to clipboard!

Description
:   OperatorHubList is a list of OperatorHub

Type
:   `object`

Required
:   * `items`

#### [1.201.1. Schema](#schema-194) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorHub)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#operatorhub-config-openshift-io-v1) | List of operatorhubs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.202. io.openshift.config.v1.ProjectList schema](#io-openshift-config-v1-ProjectList) Copy linkLink copied to clipboard!

Description
:   ProjectList is a list of Project

Type
:   `object`

Required
:   * `items`

#### [1.202.1. Schema](#schema-195) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Project)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#project-config-openshift-io-v1) | List of projects. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.203. io.openshift.config.v1.ProxyList schema](#io-openshift-config-v1-ProxyList) Copy linkLink copied to clipboard!

Description
:   ProxyList is a list of Proxy

Type
:   `object`

Required
:   * `items`

#### [1.203.1. Schema](#schema-196) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Proxy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#proxy-config-openshift-io-v1) | List of proxies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.204. io.openshift.config.v1.SchedulerList schema](#io-openshift-config-v1-SchedulerList) Copy linkLink copied to clipboard!

Description
:   SchedulerList is a list of Scheduler

Type
:   `object`

Required
:   * `items`

#### [1.204.1. Schema](#schema-197) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Scheduler)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#scheduler-config-openshift-io-v1) | List of schedulers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.205. io.openshift.console.v1.ConsoleCLIDownloadList schema](#io-openshift-console-v1-ConsoleCLIDownloadList) Copy linkLink copied to clipboard!

Description
:   ConsoleCLIDownloadList is a list of ConsoleCLIDownload

Type
:   `object`

Required
:   * `items`

#### [1.205.1. Schema](#schema-198) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleCLIDownload)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleclidownload-console-openshift-io-v1) | List of consoleclidownloads. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.206. io.openshift.console.v1.ConsoleExternalLogLinkList schema](#io-openshift-console-v1-ConsoleExternalLogLinkList) Copy linkLink copied to clipboard!

Description
:   ConsoleExternalLogLinkList is a list of ConsoleExternalLogLink

Type
:   `object`

Required
:   * `items`

#### [1.206.1. Schema](#schema-199) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleExternalLogLink)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleexternalloglink-console-openshift-io-v1) | List of consoleexternalloglinks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.207. io.openshift.console.v1.ConsoleLinkList schema](#io-openshift-console-v1-ConsoleLinkList) Copy linkLink copied to clipboard!

Description
:   ConsoleLinkList is a list of ConsoleLink

Type
:   `object`

Required
:   * `items`

#### [1.207.1. Schema](#schema-200) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleLink)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolelink-console-openshift-io-v1) | List of consolelinks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.208. io.openshift.console.v1.ConsoleNotificationList schema](#io-openshift-console-v1-ConsoleNotificationList) Copy linkLink copied to clipboard!

Description
:   ConsoleNotificationList is a list of ConsoleNotification

Type
:   `object`

Required
:   * `items`

#### [1.208.1. Schema](#schema-201) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleNotification)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolenotification-console-openshift-io-v1) | List of consolenotifications. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.209. io.openshift.console.v1.ConsolePluginList schema](#io-openshift-console-v1-ConsolePluginList) Copy linkLink copied to clipboard!

Description
:   ConsolePluginList is a list of ConsolePlugin

Type
:   `object`

Required
:   * `items`

#### [1.209.1. Schema](#schema-202) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsolePlugin)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleplugin-console-openshift-io-v1) | List of consoleplugins. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.210. io.openshift.console.v1.ConsoleQuickStartList schema](#io-openshift-console-v1-ConsoleQuickStartList) Copy linkLink copied to clipboard!

Description
:   ConsoleQuickStartList is a list of ConsoleQuickStart

Type
:   `object`

Required
:   * `items`

#### [1.210.1. Schema](#schema-203) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleQuickStart)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolequickstart-console-openshift-io-v1) | List of consolequickstarts. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.211. io.openshift.console.v1.ConsoleSampleList schema](#io-openshift-console-v1-ConsoleSampleList) Copy linkLink copied to clipboard!

Description
:   ConsoleSampleList is a list of ConsoleSample

Type
:   `object`

Required
:   * `items`

#### [1.211.1. Schema](#schema-204) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleSample)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolesample-console-openshift-io-v1) | List of consolesamples. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.212. io.openshift.console.v1.ConsoleYAMLSampleList schema](#io-openshift-console-v1-ConsoleYAMLSampleList) Copy linkLink copied to clipboard!

Description
:   ConsoleYAMLSampleList is a list of ConsoleYAMLSample

Type
:   `object`

Required
:   * `items`

#### [1.212.1. Schema](#schema-205) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleYAMLSample)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleyamlsample-console-openshift-io-v1) | List of consoleyamlsamples. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.213. io.openshift.helm.v1beta1.HelmChartRepositoryList schema](#io-openshift-helm-v1beta1-HelmChartRepositoryList) Copy linkLink copied to clipboard!

Description
:   HelmChartRepositoryList is a list of HelmChartRepository

Type
:   `object`

Required
:   * `items`

#### [1.213.1. Schema](#schema-206) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HelmChartRepository)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#helmchartrepository-helm-openshift-io-v1beta1) | List of helmchartrepositories. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.214. io.openshift.helm.v1beta1.ProjectHelmChartRepositoryList schema](#io-openshift-helm-v1beta1-ProjectHelmChartRepositoryList) Copy linkLink copied to clipboard!

Description
:   ProjectHelmChartRepositoryList is a list of ProjectHelmChartRepository

Type
:   `object`

Required
:   * `items`

#### [1.214.1. Schema](#schema-207) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ProjectHelmChartRepository)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#projecthelmchartrepository-helm-openshift-io-v1beta1) | List of projecthelmchartrepositories. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.215. io.openshift.insights.v1.DataGatherList schema](#io-openshift-insights-v1-DataGatherList) Copy linkLink copied to clipboard!

Description
:   DataGatherList is a list of DataGather

Type
:   `object`

Required
:   * `items`

#### [1.215.1. Schema](#schema-208) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DataGather)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#datagather-insights-openshift-io-v1) | List of datagathers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.216. io.openshift.machine.v1.ControlPlaneMachineSetList schema](#io-openshift-machine-v1-ControlPlaneMachineSetList) Copy linkLink copied to clipboard!

Description
:   ControlPlaneMachineSetList is a list of ControlPlaneMachineSet

Type
:   `object`

Required
:   * `items`

#### [1.216.1. Schema](#schema-209) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ControlPlaneMachineSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#controlplanemachineset-machine-openshift-io-v1) | List of controlplanemachinesets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.217. io.openshift.machine.v1beta1.MachineHealthCheckList schema](#io-openshift-machine-v1beta1-MachineHealthCheckList) Copy linkLink copied to clipboard!

Description
:   MachineHealthCheckList is a list of MachineHealthCheck

Type
:   `object`

Required
:   * `items`

#### [1.217.1. Schema](#schema-210) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineHealthCheck)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machinehealthcheck-machine-openshift-io-v1beta1) | List of machinehealthchecks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.218. io.openshift.machine.v1beta1.MachineList schema](#io-openshift-machine-v1beta1-MachineList) Copy linkLink copied to clipboard!

Description
:   MachineList is a list of Machine

Type
:   `object`

Required
:   * `items`

#### [1.218.1. Schema](#schema-211) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Machine)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machine-machine-openshift-io-v1beta1) | List of machines. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.219. io.openshift.machine.v1beta1.MachineSetList schema](#io-openshift-machine-v1beta1-MachineSetList) Copy linkLink copied to clipboard!

Description
:   MachineSetList is a list of MachineSet

Type
:   `object`

Required
:   * `items`

#### [1.219.1. Schema](#schema-212) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineset-machine-openshift-io-v1beta1) | List of machinesets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.220. io.openshift.machineconfiguration.v1.ContainerRuntimeConfigList schema](#io-openshift-machineconfiguration-v1-ContainerRuntimeConfigList) Copy linkLink copied to clipboard!

Description
:   ContainerRuntimeConfigList is a list of ContainerRuntimeConfig

Type
:   `object`

Required
:   * `items`

#### [1.220.1. Schema](#schema-213) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ContainerRuntimeConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#containerruntimeconfig-machineconfiguration-openshift-io-v1) | List of containerruntimeconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.221. io.openshift.machineconfiguration.v1.ControllerConfigList schema](#io-openshift-machineconfiguration-v1-ControllerConfigList) Copy linkLink copied to clipboard!

Description
:   ControllerConfigList is a list of ControllerConfig

Type
:   `object`

Required
:   * `items`

#### [1.221.1. Schema](#schema-214) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ControllerConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#controllerconfig-machineconfiguration-openshift-io-v1) | List of controllerconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.222. io.openshift.machineconfiguration.v1.KubeletConfigList schema](#io-openshift-machineconfiguration-v1-KubeletConfigList) Copy linkLink copied to clipboard!

Description
:   KubeletConfigList is a list of KubeletConfig

Type
:   `object`

Required
:   * `items`

#### [1.222.1. Schema](#schema-215) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeletConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#kubeletconfig-machineconfiguration-openshift-io-v1) | List of kubeletconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.223. io.openshift.machineconfiguration.v1.MachineConfigList schema](#io-openshift-machineconfiguration-v1-MachineConfigList) Copy linkLink copied to clipboard!

Description
:   MachineConfigList is a list of MachineConfig

Type
:   `object`

Required
:   * `items`

#### [1.223.1. Schema](#schema-216) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineconfig-machineconfiguration-openshift-io-v1) | List of machineconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.224. io.openshift.machineconfiguration.v1.MachineConfigNodeList schema](#io-openshift-machineconfiguration-v1-MachineConfigNodeList) Copy linkLink copied to clipboard!

Description
:   MachineConfigNodeList is a list of MachineConfigNode

Type
:   `object`

Required
:   * `items`

#### [1.224.1. Schema](#schema-217) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfigNode)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineconfignode-machineconfiguration-openshift-io-v1) | List of machineconfignodes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.225. io.openshift.machineconfiguration.v1.MachineConfigPoolList schema](#io-openshift-machineconfiguration-v1-MachineConfigPoolList) Copy linkLink copied to clipboard!

Description
:   MachineConfigPoolList is a list of MachineConfigPool

Type
:   `object`

Required
:   * `items`

#### [1.225.1. Schema](#schema-218) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfigPool)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineconfigpool-machineconfiguration-openshift-io-v1) | List of machineconfigpools. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.226. io.openshift.machineconfiguration.v1.MachineOSBuildList schema](#io-openshift-machineconfiguration-v1-MachineOSBuildList) Copy linkLink copied to clipboard!

Description
:   MachineOSBuildList is a list of MachineOSBuild

Type
:   `object`

Required
:   * `items`

#### [1.226.1. Schema](#schema-219) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineOSBuild)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineosbuild-machineconfiguration-openshift-io-v1) | List of machineosbuilds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.227. io.openshift.machineconfiguration.v1.MachineOSConfigList schema](#io-openshift-machineconfiguration-v1-MachineOSConfigList) Copy linkLink copied to clipboard!

Description
:   MachineOSConfigList is a list of MachineOSConfig

Type
:   `object`

Required
:   * `items`

#### [1.227.1. Schema](#schema-220) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineOSConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineosconfig-machineconfiguration-openshift-io-v1) | List of machineosconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.228. io.openshift.machineconfiguration.v1.PinnedImageSetList schema](#io-openshift-machineconfiguration-v1-PinnedImageSetList) Copy linkLink copied to clipboard!

Description
:   PinnedImageSetList is a list of PinnedImageSet

Type
:   `object`

Required
:   * `items`

#### [1.228.1. Schema](#schema-221) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PinnedImageSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#pinnedimageset-machineconfiguration-openshift-io-v1) | List of pinnedimagesets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.229. io.openshift.monitoring.v1.AlertingRuleList schema](#io-openshift-monitoring-v1-AlertingRuleList) Copy linkLink copied to clipboard!

Description
:   AlertingRuleList is a list of AlertingRule

Type
:   `object`

Required
:   * `items`

#### [1.229.1. Schema](#schema-222) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AlertingRule)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertingrule-monitoring-openshift-io-v1) | List of alertingrules. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.230. io.openshift.monitoring.v1.AlertRelabelConfigList schema](#io-openshift-monitoring-v1-AlertRelabelConfigList) Copy linkLink copied to clipboard!

Description
:   AlertRelabelConfigList is a list of AlertRelabelConfig

Type
:   `object`

Required
:   * `items`

#### [1.230.1. Schema](#schema-223) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AlertRelabelConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertrelabelconfig-monitoring-openshift-io-v1) | List of alertrelabelconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.231. io.openshift.network.cloud.v1.CloudPrivateIPConfigList schema](#io-openshift-network-cloud-v1-CloudPrivateIPConfigList) Copy linkLink copied to clipboard!

Description
:   CloudPrivateIPConfigList is a list of CloudPrivateIPConfig

Type
:   `object`

Required
:   * `items`

#### [1.231.1. Schema](#schema-224) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CloudPrivateIPConfig)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#cloudprivateipconfig-cloud-network-openshift-io-v1) | List of cloudprivateipconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.232. io.openshift.operator.controlplane.v1alpha1.PodNetworkConnectivityCheckList schema](#io-openshift-operator-controlplane-v1alpha1-PodNetworkConnectivityCheckList) Copy linkLink copied to clipboard!

Description
:   PodNetworkConnectivityCheckList is a list of PodNetworkConnectivityCheck

Type
:   `object`

Required
:   * `items`

#### [1.232.1. Schema](#schema-225) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodNetworkConnectivityCheck)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1) | List of podnetworkconnectivitychecks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.233. io.openshift.operator.imageregistry.v1.ConfigList schema](#io-openshift-operator-imageregistry-v1-ConfigList) Copy linkLink copied to clipboard!

Description
:   ConfigList is a list of Config

Type
:   `object`

Required
:   * `items`

#### [1.233.1. Schema](#schema-226) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Config)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#config-imageregistry-operator-openshift-io-v1) | List of configs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.234. io.openshift.operator.imageregistry.v1.ImagePrunerList schema](#io-openshift-operator-imageregistry-v1-ImagePrunerList) Copy linkLink copied to clipboard!

Description
:   ImagePrunerList is a list of ImagePruner

Type
:   `object`

Required
:   * `items`

#### [1.234.1. Schema](#schema-227) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImagePruner)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#imagepruner-imageregistry-operator-openshift-io-v1) | List of imagepruners. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.235. io.openshift.operator.ingress.v1.DNSRecordList schema](#io-openshift-operator-ingress-v1-DNSRecordList) Copy linkLink copied to clipboard!

Description
:   DNSRecordList is a list of DNSRecord

Type
:   `object`

Required
:   * `items`

#### [1.235.1. Schema](#schema-228) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DNSRecord)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#dnsrecord-ingress-operator-openshift-io-v1) | List of dnsrecords. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.236. io.openshift.operator.network.v1.EgressRouterList schema](#io-openshift-operator-network-v1-EgressRouterList) Copy linkLink copied to clipboard!

Description
:   EgressRouterList is a list of EgressRouter

Type
:   `object`

Required
:   * `items`

#### [1.236.1. Schema](#schema-229) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressRouter)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressrouter-network-operator-openshift-io-v1) | List of egressrouters. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.237. io.openshift.operator.network.v1.OperatorPKIList schema](#io-openshift-operator-network-v1-OperatorPKIList) Copy linkLink copied to clipboard!

Description
:   OperatorPKIList is a list of OperatorPKI

Type
:   `object`

Required
:   * `items`

#### [1.237.1. Schema](#schema-230) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorPKI)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#operatorpki-network-operator-openshift-io-v1) | List of operatorpkis. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.238. io.openshift.operator.samples.v1.ConfigList schema](#io-openshift-operator-samples-v1-ConfigList) Copy linkLink copied to clipboard!

Description
:   ConfigList is a list of Config

Type
:   `object`

Required
:   * `items`

#### [1.238.1. Schema](#schema-231) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Config)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#config-samples-operator-openshift-io-v1) | List of configs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.239. io.openshift.operator.v1.AuthenticationList schema](#io-openshift-operator-v1-AuthenticationList) Copy linkLink copied to clipboard!

Description
:   AuthenticationList is a list of Authentication

Type
:   `object`

Required
:   * `items`

#### [1.239.1. Schema](#schema-232) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Authentication)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#authentication-operator-openshift-io-v1) | List of authentications. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.240. io.openshift.operator.v1.CloudCredentialList schema](#io-openshift-operator-v1-CloudCredentialList) Copy linkLink copied to clipboard!

Description
:   CloudCredentialList is a list of CloudCredential

Type
:   `object`

Required
:   * `items`

#### [1.240.1. Schema](#schema-233) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CloudCredential)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#cloudcredential-operator-openshift-io-v1) | List of cloudcredentials. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.241. io.openshift.operator.v1.ClusterCSIDriverList schema](#io-openshift-operator-v1-ClusterCSIDriverList) Copy linkLink copied to clipboard!

Description
:   ClusterCSIDriverList is a list of ClusterCSIDriver

Type
:   `object`

Required
:   * `items`

#### [1.241.1. Schema](#schema-234) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterCSIDriver)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#clustercsidriver-operator-openshift-io-v1) | List of clustercsidrivers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.242. io.openshift.operator.v1.ConfigList schema](#io-openshift-operator-v1-ConfigList) Copy linkLink copied to clipboard!

Description
:   ConfigList is a list of Config

Type
:   `object`

Required
:   * `items`

#### [1.242.1. Schema](#schema-235) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Config)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#config-operator-openshift-io-v1) | List of configs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.243. io.openshift.operator.v1.ConsoleList schema](#io-openshift-operator-v1-ConsoleList) Copy linkLink copied to clipboard!

Description
:   ConsoleList is a list of Console

Type
:   `object`

Required
:   * `items`

#### [1.243.1. Schema](#schema-236) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Console)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#console-operator-openshift-io-v1) | List of consoles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.244. io.openshift.operator.v1.CSISnapshotControllerList schema](#io-openshift-operator-v1-CSISnapshotControllerList) Copy linkLink copied to clipboard!

Description
:   CSISnapshotControllerList is a list of CSISnapshotController

Type
:   `object`

Required
:   * `items`

#### [1.244.1. Schema](#schema-237) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSISnapshotController)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#csisnapshotcontroller-operator-openshift-io-v1) | List of csisnapshotcontrollers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.245. io.openshift.operator.v1.DNSList schema](#io-openshift-operator-v1-DNSList) Copy linkLink copied to clipboard!

Description
:   DNSList is a list of DNS

Type
:   `object`

Required
:   * `items`

#### [1.245.1. Schema](#schema-238) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DNS)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#dns-operator-openshift-io-v1) | List of dnses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.246. io.openshift.operator.v1.EtcdList schema](#io-openshift-operator-v1-EtcdList) Copy linkLink copied to clipboard!

Description
:   EtcdList is a list of Etcd

Type
:   `object`

Required
:   * `items`

#### [1.246.1. Schema](#schema-239) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Etcd)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#etcd-operator-openshift-io-v1) | List of etcds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.247. io.openshift.operator.v1.IngressControllerList schema](#io-openshift-operator-v1-IngressControllerList) Copy linkLink copied to clipboard!

Description
:   IngressControllerList is a list of IngressController

Type
:   `object`

Required
:   * `items`

#### [1.247.1. Schema](#schema-240) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IngressController)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#ingresscontroller-operator-openshift-io-v1) | List of ingresscontrollers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.248. io.openshift.operator.v1.InsightsOperatorList schema](#io-openshift-operator-v1-InsightsOperatorList) Copy linkLink copied to clipboard!

Description
:   InsightsOperatorList is a list of InsightsOperator

Type
:   `object`

Required
:   * `items`

#### [1.248.1. Schema](#schema-241) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (InsightsOperator)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#insightsoperator-operator-openshift-io-v1) | List of insightsoperators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.249. io.openshift.operator.v1.KubeAPIServerList schema](#io-openshift-operator-v1-KubeAPIServerList) Copy linkLink copied to clipboard!

Description
:   KubeAPIServerList is a list of KubeAPIServer

Type
:   `object`

Required
:   * `items`

#### [1.249.1. Schema](#schema-242) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeAPIServer)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubeapiserver-operator-openshift-io-v1) | List of kubeapiservers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.250. io.openshift.operator.v1.KubeControllerManagerList schema](#io-openshift-operator-v1-KubeControllerManagerList) Copy linkLink copied to clipboard!

Description
:   KubeControllerManagerList is a list of KubeControllerManager

Type
:   `object`

Required
:   * `items`

#### [1.250.1. Schema](#schema-243) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeControllerManager)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubecontrollermanager-operator-openshift-io-v1) | List of kubecontrollermanagers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.251. io.openshift.operator.v1.KubeSchedulerList schema](#io-openshift-operator-v1-KubeSchedulerList) Copy linkLink copied to clipboard!

Description
:   KubeSchedulerList is a list of KubeScheduler

Type
:   `object`

Required
:   * `items`

#### [1.251.1. Schema](#schema-244) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeScheduler)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubescheduler-operator-openshift-io-v1) | List of kubeschedulers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.252. io.openshift.operator.v1.KubeStorageVersionMigratorList schema](#io-openshift-operator-v1-KubeStorageVersionMigratorList) Copy linkLink copied to clipboard!

Description
:   KubeStorageVersionMigratorList is a list of KubeStorageVersionMigrator

Type
:   `object`

Required
:   * `items`

#### [1.252.1. Schema](#schema-245) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeStorageVersionMigrator)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubestorageversionmigrator-operator-openshift-io-v1) | List of kubestorageversionmigrators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.253. io.openshift.operator.v1.MachineConfigurationList schema](#io-openshift-operator-v1-MachineConfigurationList) Copy linkLink copied to clipboard!

Description
:   MachineConfigurationList is a list of MachineConfiguration

Type
:   `object`

Required
:   * `items`

#### [1.253.1. Schema](#schema-246) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfiguration)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#machineconfiguration-operator-openshift-io-v1) | List of machineconfigurations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.254. io.openshift.operator.v1.NetworkList schema](#io-openshift-operator-v1-NetworkList) Copy linkLink copied to clipboard!

Description
:   NetworkList is a list of Network

Type
:   `object`

Required
:   * `items`

#### [1.254.1. Schema](#schema-247) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Network)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#network-operator-openshift-io-v1) | List of networks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.255. io.openshift.operator.v1.OLMList schema](#io-openshift-operator-v1-OLMList) Copy linkLink copied to clipboard!

Description
:   OLMList is a list of OLM

Type
:   `object`

Required
:   * `items`

#### [1.255.1. Schema](#schema-248) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OLM)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#olm-operator-openshift-io-v1) | List of olms. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.256. io.openshift.operator.v1.OpenShiftAPIServerList schema](#io-openshift-operator-v1-OpenShiftAPIServerList) Copy linkLink copied to clipboard!

Description
:   OpenShiftAPIServerList is a list of OpenShiftAPIServer

Type
:   `object`

Required
:   * `items`

#### [1.256.1. Schema](#schema-249) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OpenShiftAPIServer)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#openshiftapiserver-operator-openshift-io-v1) | List of openshiftapiservers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.257. io.openshift.operator.v1.OpenShiftControllerManagerList schema](#io-openshift-operator-v1-OpenShiftControllerManagerList) Copy linkLink copied to clipboard!

Description
:   OpenShiftControllerManagerList is a list of OpenShiftControllerManager

Type
:   `object`

Required
:   * `items`

#### [1.257.1. Schema](#schema-250) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OpenShiftControllerManager)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#openshiftcontrollermanager-operator-openshift-io-v1) | List of openshiftcontrollermanagers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.258. io.openshift.operator.v1.ServiceCAList schema](#io-openshift-operator-v1-ServiceCAList) Copy linkLink copied to clipboard!

Description
:   ServiceCAList is a list of ServiceCA

Type
:   `object`

Required
:   * `items`

#### [1.258.1. Schema](#schema-251) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceCA)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#serviceca-operator-openshift-io-v1) | List of servicecas. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.259. io.openshift.operator.v1.StorageList schema](#io-openshift-operator-v1-StorageList) Copy linkLink copied to clipboard!

Description
:   StorageList is a list of Storage

Type
:   `object`

Required
:   * `items`

#### [1.259.1. Schema](#schema-252) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Storage)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#storage-operator-openshift-io-v1) | List of storages. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.260. io.openshift.operator.v1alpha1.ImageContentSourcePolicyList schema](#io-openshift-operator-v1alpha1-ImageContentSourcePolicyList) Copy linkLink copied to clipboard!

Description
:   ImageContentSourcePolicyList is a list of ImageContentSourcePolicy

Type
:   `object`

Required
:   * `items`

#### [1.260.1. Schema](#schema-253) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageContentSourcePolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) | List of imagecontentsourcepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.261. io.openshift.performance.v2.PerformanceProfileList schema](#io-openshift-performance-v2-PerformanceProfileList) Copy linkLink copied to clipboard!

Description
:   PerformanceProfileList is a list of PerformanceProfile

Type
:   `object`

Required
:   * `items`

#### [1.261.1. Schema](#schema-254) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PerformanceProfile)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#performanceprofile-performance-openshift-io-v2) | List of performanceprofiles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.262. io.openshift.quota.v1.ClusterResourceQuotaList schema](#io-openshift-quota-v1-ClusterResourceQuotaList) Copy linkLink copied to clipboard!

Description
:   ClusterResourceQuotaList is a list of ClusterResourceQuota

Type
:   `object`

Required
:   * `items`

#### [1.262.1. Schema](#schema-255) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterResourceQuota)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#clusterresourcequota-quota-openshift-io-v1) | List of clusterresourcequotas. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.263. io.openshift.security.v1.SecurityContextConstraintsList schema](#io-openshift-security-v1-SecurityContextConstraintsList) Copy linkLink copied to clipboard!

Description
:   SecurityContextConstraintsList is a list of SecurityContextConstraints

Type
:   `object`

Required
:   * `items`

#### [1.263.1. Schema](#schema-256) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (SecurityContextConstraints)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#securitycontextconstraints-security-openshift-io-v1) | List of securitycontextconstraints. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.264. io.openshift.tuned.v1.ProfileList schema](#io-openshift-tuned-v1-ProfileList) Copy linkLink copied to clipboard!

Description
:   ProfileList is a list of Profile

Type
:   `object`

Required
:   * `items`

#### [1.264.1. Schema](#schema-257) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Profile)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#profile-tuned-openshift-io-v1) | List of profiles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.265. io.openshift.tuned.v1.TunedList schema](#io-openshift-tuned-v1-TunedList) Copy linkLink copied to clipboard!

Description
:   TunedList is a list of Tuned

Type
:   `object`

Required
:   * `items`

#### [1.265.1. Schema](#schema-258) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Tuned)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#tuned-tuned-openshift-io-v1) | List of tuneds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.266. io.operatorframework.olm.v1.ClusterCatalogList schema](#io-operatorframework-olm-v1-ClusterCatalogList) Copy linkLink copied to clipboard!

Description
:   ClusterCatalogList is a list of ClusterCatalog

Type
:   `object`

Required
:   * `items`

#### [1.266.1. Schema](#schema-259) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterCatalog)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#clustercatalog-olm-operatorframework-io-v1) | List of clustercatalogs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.267. io.operatorframework.olm.v1.ClusterExtensionList schema](#io-operatorframework-olm-v1-ClusterExtensionList) Copy linkLink copied to clipboard!

Description
:   ClusterExtensionList is a list of ClusterExtension

Type
:   `object`

Required
:   * `items`

#### [1.267.1. Schema](#schema-260) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterExtension)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#clusterextension-olm-operatorframework-io-v1) | List of clusterextensions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.268. io.redhat.testextension.v1.TestExtensionAdmissionList schema](#io-redhat-testextension-v1-TestExtensionAdmissionList) Copy linkLink copied to clipboard!

Description
:   TestExtensionAdmissionList is a list of TestExtensionAdmission

Type
:   `object`

Required
:   * `items`

#### [1.268.1. Schema](#schema-261) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (TestExtensionAdmission)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#testextensionadmission-testextension-redhat-io-v1) | List of testextensionadmissions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.269. io.x-k8s.cluster.infrastructure.v1beta1.Metal3RemediationList schema](#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationList) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationList is a list of Metal3Remediation

Type
:   `object`

Required
:   * `items`

#### [1.269.1. Schema](#schema-262) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Metal3Remediation)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) | List of metal3remediations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.270. io.x-k8s.cluster.infrastructure.v1beta1.Metal3RemediationTemplateList schema](#io-x-k8s-cluster-infrastructure-v1beta1-Metal3RemediationTemplateList) Copy linkLink copied to clipboard!

Description
:   Metal3RemediationTemplateList is a list of Metal3RemediationTemplate

Type
:   `object`

Required
:   * `items`

#### [1.270.1. Schema](#schema-263) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Metal3RemediationTemplate)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1) | List of metal3remediationtemplates. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.271. io.x-k8s.cluster.ipam.v1beta1.IPAddressClaimList schema](#io-x-k8s-cluster-ipam-v1beta1-IPAddressClaimList) Copy linkLink copied to clipboard!

Description
:   IPAddressClaimList is a list of IPAddressClaim

Type
:   `object`

Required
:   * `items`

#### [1.271.1. Schema](#schema-264) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAddressClaim)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ipaddressclaim-ipam-cluster-x-k8s-io-v1beta1) | List of ipaddressclaims. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.272. org.ovn.k8s.v1.AdminPolicyBasedExternalRouteList schema](#org-ovn-k8s-v1-AdminPolicyBasedExternalRouteList) Copy linkLink copied to clipboard!

Description
:   AdminPolicyBasedExternalRouteList is a list of AdminPolicyBasedExternalRoute

Type
:   `object`

Required
:   * `items`

#### [1.272.1. Schema](#schema-265) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AdminPolicyBasedExternalRoute)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#adminpolicybasedexternalroute-k8s-ovn-org-v1) | List of adminpolicybasedexternalroutes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.273. org.ovn.k8s.v1.ClusterUserDefinedNetworkList schema](#org-ovn-k8s-v1-ClusterUserDefinedNetworkList) Copy linkLink copied to clipboard!

Description
:   ClusterUserDefinedNetworkList is a list of ClusterUserDefinedNetwork

Type
:   `object`

Required
:   * `items`

#### [1.273.1. Schema](#schema-266) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterUserDefinedNetwork)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#clusteruserdefinednetwork-k8s-ovn-org-v1) | List of clusteruserdefinednetworks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.274. org.ovn.k8s.v1.EgressFirewallList schema](#org-ovn-k8s-v1-EgressFirewallList) Copy linkLink copied to clipboard!

Description
:   EgressFirewallList is a list of EgressFirewall

Type
:   `object`

Required
:   * `items`

#### [1.274.1. Schema](#schema-267) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressFirewall)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressfirewall-k8s-ovn-org-v1) | List of egressfirewalls. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.275. org.ovn.k8s.v1.EgressIPList schema](#org-ovn-k8s-v1-EgressIPList) Copy linkLink copied to clipboard!

Description
:   EgressIPList is a list of EgressIP

Type
:   `object`

Required
:   * `items`

#### [1.275.1. Schema](#schema-268) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressIP)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressip-k8s-ovn-org-v1) | List of egressips. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.276. org.ovn.k8s.v1.EgressQoSList schema](#org-ovn-k8s-v1-EgressQoSList) Copy linkLink copied to clipboard!

Description
:   EgressQoSList is a list of EgressQoS

Type
:   `object`

Required
:   * `items`

#### [1.276.1. Schema](#schema-269) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressQoS)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressqos-k8s-ovn-org-v1) | List of egressqoses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.277. org.ovn.k8s.v1.EgressServiceList schema](#org-ovn-k8s-v1-EgressServiceList) Copy linkLink copied to clipboard!

Description
:   EgressServiceList is a list of EgressService

Type
:   `object`

Required
:   * `items`

#### [1.277.1. Schema](#schema-270) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressService)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressservice-k8s-ovn-org-v1) | List of egressservices. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

### [1.278. org.ovn.k8s.v1.UserDefinedNetworkList schema](#org-ovn-k8s-v1-UserDefinedNetworkList) Copy linkLink copied to clipboard!

Description
:   UserDefinedNetworkList is a list of UserDefinedNetwork

Type
:   `object`

Required
:   * `items`

#### [1.278.1. Schema](#schema-271) Copy linkLink copied to clipboard!

Expand

| Property | Type | Description |
| --- | --- | --- |
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (UserDefinedNetwork)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#userdefinednetwork-k8s-ovn-org-v1) | List of userdefinednetworks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

Show more

## [Legal Notice](#idm139685483508112) Copy linkLink copied to clipboard!

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
