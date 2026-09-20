---
title: "Extensions"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extensions/index
retrieved_at: 2026-09-05T05:41:48.407282+00:00
---

# Extensions

---

OpenShift Container Platform 4.22

## Working with extensions in OpenShift Container Platform using Operator Lifecycle Manager (OLM) v1.

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140529071897808)

**Abstract**

This document provides information about installing, managing, and configuring extensions and Operators on OpenShift Container Platform.

---

## [Chapter 1. Extensions overview](#extensions-overview) Copy linkLink copied to clipboard!

You can configure the operating system of your nodes and extend capabilities to your cluster by using pre-packaged software extensions. These extensions include ready-to-use tools that customize your environment for your requirements.

Operator Lifecycle Manager (OLM) has been included with OpenShift Container Platform 4 since its initial release. OpenShift Container Platform 4.22 includes components for a next-generation iteration of OLM as a Generally Available (GA) feature, known during this phase as *OLM v1*. This updated framework evolves many of the concepts that have been part of previous versions of OLM and adds new capabilities.

Note

For OpenShift Container Platform 4.22, documented procedures for OLM v1 are CLI-based only. Alternatively, administrators can create and view related objects in the web console by using normal methods, such as the **Import YAML** and **Search** pages. However, the existing **Software Catalog** and **Installed Operators** pages do not yet display OLM v1 components.

### [1.1. OLM v1 highlights](#olmv1-highlights_extensions-overview) Copy linkLink copied to clipboard!

As an administrator, use OLM v1 to securely manage your cluster configurations and streamline updates through GitOps-based declarative management, granular extension controls, and flexible packaging formats.

Administrators can explore the following highlights:

Fully declarative model that supports GitOps workflows
:   OLM v1 simplifies extension management through two key APIs:

    * A new `ClusterExtension` API streamlines management of installed extensions, which includes Operators via the `registry+v1` bundle format, by consolidating user-facing APIs into a single object. This API is provided as `clusterextension.olm.operatorframework.io` by the new Operator Controller component. Administrators and SREs can use the API to automate processes and define desired states by using GitOps principles.

      Note

      Earlier Technology Preview phases of OLM v1 introduced a new `Operator` API; this API is renamed `ClusterExtension` in OpenShift Container Platform 4.16 to address the following improvements:

      + More accurately reflects the simplified functionality of extending a cluster’s capabilities
      + Better represents a more flexible packaging format
      + `Cluster` prefix clearly indicates that `ClusterExtension` objects are cluster-scoped, a change from OLM (Classic) where Operators could be either namespace-scoped or cluster-scoped
    * The `Catalog` API, provided by the new catalogd component, serves as the foundation for OLM v1, unpacking catalogs for on-cluster clients so that users can discover installable content, such as Kubernetes extensions and Operators. This provides increased visibility into all available Operator bundle versions, including their details, channels, and update edges.

    For more information, see "Operator Controller and Catalogd".

Improved control over extension updates
:   With improved insight into catalog content, administrators can specify target versions for installation and updates. This grants administrators more control over the target version of extension updates. For more information, see "Updating a cluster extension".

Flexible extension packaging format
:   Administrators can use file-based catalogs to install and manage extensions, such as OLM-based Operators, similar to the OLM (Classic) experience.

    In addition, bundle size is no longer constrained by the etcd value size limit. For more information, see "Installing extensions".

Secure catalog communication
:   OLM v1 uses HTTPS encryption for catalogd server responses.

Basic support for proxied environments and trusted CA certificates
:   Operator Controller and catalogd can run in proxied environments and include basic support for trusted CA certificates.

### [1.2. Purpose of Operator Lifecycle Manager](#olmv1-about-purpose_extensions-overview) Copy linkLink copied to clipboard!

The Operator Lifecycle Manager (OLM) simplifies management of extensions on Kubernetes clusters. It provides administrators with a safe, reliable, and centralized way to install, run, and update cluster extensions.

The initial version of OLM, which launched with OpenShift Container Platform 4 and is included by default, focused on providing unique support for these specific needs for a particular type of cluster extension, known as Operators. Operators are classified as one or more Kubernetes controllers, shipping with one or more API extensions, as `CustomResourceDefinition` (CRD) objects, to provide additional functionality to the cluster.

After running in production clusters for many releases, the next-generation of OLM aims to encompass lifecycles for cluster extensions that are not just Operators.

## [Chapter 2. Architecture](#architecture) Copy linkLink copied to clipboard!

### [2.1. OLM v1 components overview](#olm-components) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 uses two key microservice components, Operator Controller and Catalogd, to unpack content and manage extensions on your cluster.

Operator Controller
:   Extends Kubernetes with an API to install and manage Operators and extensions using metadata from Catalogd.

Catalogd
:   Unpacks file-based catalog (FBC) content and hosts metadata so users can discover installable extensions.

### [2.2. Operator Controller](#operator-controller) Copy linkLink copied to clipboard!

Operator Controller is the central component of Operator Lifecycle Manager (OLM) v1 and consumes the other OLM v1 component, catalogd. It extends Kubernetes with an API through which users can install Operators and extensions.

#### [2.2.1. ClusterExtension API](#olmv1-clusterextension-api_operator-controller) Copy linkLink copied to clipboard!

To manage installed extensions in OLM v1, use the `ClusterExtension` API. This consolidated API simplifies extension management by replacing multiple OLM (Classic) objects with a single cluster-scoped resource.

Important

In OLM v1, `ClusterExtension` objects are cluster-scoped. This differs from OLM (Classic) where Operators can be either namespace-scoped or cluster-scoped. In OLM (Classic), the scope depends on the configuration of related `Subscription` and `OperatorGroup` objects.

For more information about OLM (Classic) behavior, see *Multitenancy and Operator colocation*.

**Example `ClusterExtension` object**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <namespace_name>
  config:
    configType: Inline
    inline:
      watchNamespace: <namespace_name>
  serviceAccount:
    name: <service_account_name>
  source:
    sourceType: Catalog
    catalog:
      packageName: <package_name>
      channels:
        - <channel>
      version: "<version>"
```

`config`
:   If the extension supports watching a specific namespace, use this field to configure extension behavior. For more information, see "Extension configuration".

##### [2.2.1.1. Example custom resources (CRs) that specify a target version](#olmv1-about-target-versions_operator-controller) Copy linkLink copied to clipboard!

In Operator Lifecycle Manager (OLM) v1, cluster administrators can declaratively set the target version of an Operator or extension in the custom resource (CR).

You can define a target version by specifying any of the following fields:

* Channel
* Version number
* Version range

If you specify a channel in the CR, OLM v1 installs the latest version of the Operator or extension that can be resolved within the specified channel. When updates are published to the specified channel, OLM v1 automatically updates to the latest release that can be resolved from the channel.

**Example CR with a specified channel**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        channels:
          - latest
```

Installs the latest release that can be resolved from the specified channel. Updates to the channel are automatically installed. Specify the value of the `channels` parameter as an array. This field is optional

If you specify the Operator or extension’s target version in the CR, OLM v1 installs the specified version. When the target version is specified in the CR, OLM v1 does not change the target version when updates are published to the catalog.

If you want to update the version of the Operator that is installed on the cluster, you must manually edit the Operator’s CR. Specifying an Operator’s target version pins the Operator’s version to the specified release.

**Example CR with the target version specified**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: "1.11.1"
```

Specifies the target version. If you want to update the version of the Operator or extension that is installed, you must manually update this field the CR to the desired target version. This field is optional.

If you want to define a range of acceptable versions for an Operator or extension, you can specify a version range by using a comparison string. When you specify a version range, OLM v1 installs the latest version of an Operator or extension that can be resolved by the Operator Controller.

**Example CR with a version range specified**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: ">1.11.1"
```

Specifies that the desired version range is greater than version `1.11.1`. This field is optional.

After you create or update a CR, apply the configuration file by running the following command:

**Command syntax**

```
$ oc apply -f <extension_name>.yaml
```

#### [2.2.2. Object ownership for cluster extensions](#olmv1-object-ownership_operator-controller) Copy linkLink copied to clipboard!

In Operator Lifecycle Manager (OLM) v1, a Kubernetes object can only be owned by a single `ClusterExtension` object at a time. This ensures that objects within an OpenShift Container Platform cluster are managed consistently and prevents conflicts between multiple cluster extensions attempting to control the same object.

##### [2.2.2.1. Single ownership](#olmv1-single-ownership_operator-controller) Copy linkLink copied to clipboard!

The core ownership principle enforced by OLM v1 is that each object can only have one cluster extension as its owner. This prevents overlapping or conflicting management by multiple cluster extensions, ensuring that each object is uniquely associated with only one bundle. Single ownership has the following implications:

* Bundles that provide a `CustomResourceDefinition` (CRD) object can only be installed once.

  Bundles provide CRDs, which are part of a `ClusterExtension` object. This means you can install a bundle only once in a cluster. Attempting to install another bundle that provides the same CRD results in failure, as each custom resource can have only one cluster extension as its owner.
* Cluster extensions cannot share objects.

  The single-owner policy of OLM v1 means that cluster extensions cannot share ownership of any objects. If one cluster extension manages a specific object, such as a `Deployment`, `CustomResourceDefinition`, or `Service` object, another cluster extension cannot claim ownership of the same object. Any attempt to do so is blocked by OLM v1.

##### [2.2.2.2. Error messages](#olmv1-error-messages_operator-controller) Copy linkLink copied to clipboard!

When a conflict occurs due to multiple cluster extensions attempting to manage the same object, Operator Controller returns an error message indicating the ownership conflict, such as the following:

**Example error message**

```
CustomResourceDefinition 'logfilemetricexporters.logging.kubernetes.io' already exists in namespace 'kubernetes-logging' and cannot be managed by operator-controller
```

This error message signals that the object is already being managed by another cluster extension and cannot be reassigned or shared.

##### [2.2.2.3. Considerations](#olmv1-ownership-considerations_operator-controller) Copy linkLink copied to clipboard!

As a cluster or extension administrator, review the following considerations:

Uniqueness of bundles
:   Ensure that Operator bundles providing the same CRDs are not installed more than once. This can prevent potential installation failures due to ownership conflicts.

Avoid object sharing
:   If you need different cluster extensions to interact with similar resources, ensure they are managing separate objects. Cluster extensions cannot jointly manage the same object due to the single-owner enforcement.

#### [2.2.3. ClusterObjectSets](#olmv1-clusterobjectsets_operator-controller) Copy linkLink copied to clipboard!

Important

ClusterObjectSets is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

As part of Operator Lifecycle Manager (OLM) v1, the operator-controller creates `ClusterObjectSet` resources when you install or upgrade content with a `ClusterExtension` object. `ClusterObjectSet` objects enable safe, phased rollouts of Kubernetes resources.

A `ClusterObjectSet` object is a cluster-scoped resource. It is not content that you install. It is the controller’s internal record for one revision of your `ClusterExtension` object. It rolls out related resources sequentially with built-in readiness checks between phases.

A `ClusterObjectSet` object solves several problems when managing sets of related Kubernetes resources:

Immutable revision content
:   The revision number, phases, objects, and collision protection strategy are immutable, that is, they cannot change once set. This provides a clear audit trail of what was deployed at each revision.

Phased rollout
:   Resources are grouped into phases, for example, CRDs before Deployments, and are deployed sequentially. A phase only progresses after all its objects pass readiness probes. Manifests are organized into phases, applied to the cluster, and must pass some status probes before they progress to the next phase. This avoids incomplete installs.

Safe transitions
:   During upgrades, both old and new revisions remain active until the new revision succeeds. Object ownership transitions between revisions automatically.

Single ownership
:   Each resource can only be managed by one `ClusterObjectSet` at a time, preventing conflicts.

Large resource support
:   Object manifests can be stored inline or externalized into secrets, allowing bundles larger than the etcd 1.5 MiB object size limit.

Note

Archived `ClusterObjectSet` revisions stay on the cluster as a history of what was applied for that `ClusterExtension` object.

Each `ClusterObjectSet` contains the following content:

A revision number
:   A permanent, sequential integer that identifies the version. When the bundle version changes, it creates a new revision. During an upgrade, the old and new revision can both be active until the new one finishes. Older revisions are archived.

A lifecycle state
:   This shows the status of the `ClusterObjectSet`, which can be `Active` (managed and reconciled) or `Archived`. The `lifecycleState` transitions from `Active` to `Archived` but not back.

A list of phases
:   Objects within a `ClusterObjectSet` are organized into phases. Each phase groups related resources, and phases are applied sequentially. Within a phase, all objects are applied simultaneously in no particular order.

A collision protection strategy
:   Controls whether a `ClusterObjectSet` can adopt pre-existing objects on the cluster.

Status conditions
:   Indicates whether the revision is actively rolling out and reports rollout progress, availability, and success.

At most, one `ClusterObjectSet` manages a given cluster object at a time. Very large bundles store manifests in `Secret` objects so that size limits do not block installs or upgrades.

Additionally, support for management of large object bundles created by `ClusterObjectSet` is provided. `ClusterObjectSet` embeds Kubernetes manifests in `.spec.phases[].objects[].object`. Currently, with up to 20 phases and 50 objects per phase, they can exceed the etcd 1.5 MiB object size limit. Large Operators with many CRDs, Deployments, RBAC rules, and webhook configurations frequently hit this limit, causing the API server to reject the `ClusterObjectSet` and fail installation or upgrade.

To solve this, objects can be externalized into `Secret` resources using per-object references. The phases data is immutable and only consumed by the revision reconciler, making it suitable for externalization.

### [2.3. Catalogd](#catalogd) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 uses the catalogd component and its resources to manage Operator and extension catalogs.

#### [2.3.1. About catalogs in OLM v1](#olmv1-about-catalogs_catalogd) Copy linkLink copied to clipboard!

You can discover installable content by querying a catalog for Kubernetes extensions, such as Operators and controllers, by using the catalogd component.

Catalogd is a Kubernetes extension that unpacks catalog content for on-cluster clients and is part of the Operator Lifecycle Manager (OLM) v1 suite of microservices. Currently, catalogd unpacks catalog content that is packaged and distributed as container images.

## [Chapter 3. Operator Framework glossary of common terms](#of-terms) Copy linkLink copied to clipboard!

Review the Operator Framework terminology, including Operator Lifecycle Manager (OLM) v1 terms, used throughout the documentation.

### [3.1. Bundle](#olm-common-terms-bundle_of-terms) Copy linkLink copied to clipboard!

In the bundle format, a *bundle* is a collection of an Operator CSV, manifests, and metadata. Together, they form a unique version of an Operator that can be installed onto the cluster.

### [3.2. Bundle image](#olm-common-terms-bundle-image_of-terms) Copy linkLink copied to clipboard!

In the bundle format, a *bundle image* is a container image that is built from Operator manifests and that contains one bundle. Bundle images are stored and distributed by Open Container Initiative (OCI) spec container registries, such as Quay.io or DockerHub.

### [3.3. Catalog source](#olm-common-terms-catalogsource_of-terms) Copy linkLink copied to clipboard!

A *catalog source* represents a store of metadata that OLM can query to discover and install Operators and their dependencies.

### [3.4. Channel](#olm-common-terms-channel_of-terms) Copy linkLink copied to clipboard!

A *channel* defines a stream of updates for an Operator and is used to roll out updates for subscribers. The head points to the latest version of that channel. For example, a `stable` channel would have all stable versions of an Operator arranged from the earliest to the latest.

An Operator can have several channels, and a subscription binding to a certain channel would only look for updates in that channel.

### [3.5. Channel head](#olm-common-terms-channel-head_of-terms) Copy linkLink copied to clipboard!

A *channel head* refers to the latest known update in a particular channel.

### [3.6. Cluster service version](#olm-common-terms-csv_of-terms) Copy linkLink copied to clipboard!

A *cluster service version (CSV)* is a YAML manifest created from Operator metadata that assists OLM in running the Operator in a cluster. It is the metadata that accompanies an Operator container image, used to populate user interfaces with information such as its logo, description, and version.

It is also a source of technical information that is required to run the Operator, like the RBAC rules it requires and which custom resources (CRs) it manages or depends on.

### [3.7. Dependency](#olm-common-terms-dependency_of-terms) Copy linkLink copied to clipboard!

An Operator may have a *dependency* on another Operator being present in the cluster. For example, the Vault Operator has a dependency on the etcd Operator for its data persistence layer.

OLM resolves dependencies by ensuring that all specified versions of Operators and CRDs are installed on the cluster during the installation phase. This dependency is resolved by finding and installing an Operator in a catalog that satisfies the required CRD API, and is not related to packages or bundles.

### [3.8. Extension](#olm-common-terms-extension_of-terms) Copy linkLink copied to clipboard!

Extensions enable cluster administrators to extend capabilities for users on their OpenShift Container Platform cluster. Extensions are managed by Operator Lifecycle Manager (OLM) v1.

The `ClusterExtension` API streamlines management of installed extensions, which includes Operators via the `registry+v1` bundle format, by consolidating user-facing APIs into a single object. Administrators and SREs can use the API to automate processes and define desired states by using GitOps principles.

### [3.9. Index image](#olm-common-terms-index-image_of-terms) Copy linkLink copied to clipboard!

In the bundle format, an *index image* refers to an image of a database (a database snapshot) that contains information about Operator bundles including CSVs and CRDs of all versions. This index can host a history of Operators on a cluster and be maintained by adding or removing Operators using the `opm` CLI tool.

### [3.10. Install plan](#olm-common-terms-installplan_of-terms) Copy linkLink copied to clipboard!

An *install plan* is a calculated list of resources to be created to automatically install or upgrade a CSV.

### [3.11. Multitenancy](#olm-common-terms-multitenancy_of-terms) Copy linkLink copied to clipboard!

A *tenant* in OpenShift Container Platform is a user or group of users that share common access and privileges for a set of deployed workloads, typically represented by a namespace or project. You can use tenants to provide a level of isolation between different groups or teams.

When a cluster is shared by multiple users or groups, it is considered a *multitenant* cluster.

### [3.12. Operator](#olm-common-terms-operator_of-terms) Copy linkLink copied to clipboard!

Operators are a method of packaging, deploying, and managing a Kubernetes application. A Kubernetes application is an app that is both deployed on Kubernetes and managed using the Kubernetes APIs and `kubectl` or `oc` tooling.

In Operator Lifecycle Manager (OLM) v1, the `ClusterExtension` API streamlines management of installed extensions, which includes Operators via the `registry+v1` bundle format.

### [3.13. Operator group](#olm-common-terms-operatorgroup_of-terms) Copy linkLink copied to clipboard!

An *Operator group* configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their CR in a list of namespaces or cluster-wide.

### [3.14. Package](#olm-common-terms-package_of-terms) Copy linkLink copied to clipboard!

In the bundle format, a *package* is a directory that encloses all released history of an Operator with each version. A released version of an Operator is described in a CSV manifest alongside the CRDs.

### [3.15. Registry](#olm-common-terms-registry_of-terms) Copy linkLink copied to clipboard!

A *registry* is a database that stores bundle images of Operators, each with all of its latest and historical versions in all channels.

### [3.16. Subscription](#olm-common-terms-subscription_of-terms) Copy linkLink copied to clipboard!

A *subscription* keeps CSVs up to date by tracking a channel in a package.

### [3.17. Update graph](#olm-common-terms-update-graph_of-terms) Copy linkLink copied to clipboard!

An *update graph* links versions of CSVs together, similar to the update graph of any other packaged software. Operators can be installed sequentially, or certain versions can be skipped. The update graph is expected to grow only at the head with newer versions being added.

Also known as *update edges* or *update paths*.

## [Chapter 4. Catalogs](#catalogs) Copy linkLink copied to clipboard!

### [4.1. File-based catalogs](#fbc) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 in OpenShift Container Platform supports *file-based catalogs* for discovering and sourcing cluster extensions, including Operators, on a cluster.

#### [4.1.1. Introduction to file-based catalogs](#olm-file-based-catalogs_fbc) Copy linkLink copied to clipboard!

File-based catalogs are the latest plain text (JSON or YAML) catalog format for Operator Lifecycle Manager (OLM). This format enables catalog editing, composability, and extensibility while remaining compatible with earlier SQLite-based catalogs.

Editing
:   With file-based catalogs, users interacting with the contents of a catalog are able to make direct changes to the format and verify that their changes are valid. Because this format is plain text JSON or YAML, catalog maintainers can easily manipulate catalog metadata by hand or with widely known and supported JSON or YAML tooling, such as the `jq` CLI.

    This editability enables the following features and user-defined extensions:

    * Promoting an existing bundle to a new channel
    * Changing the default channel of a package
    * Custom algorithms for adding, updating, and removing upgrade paths

Composability
:   File-based catalogs are stored in an arbitrary directory hierarchy, which enables catalog composition. For example, consider two separate file-based catalog directories: `catalogA` and `catalogB`. A catalog maintainer can create a new combined catalog by making a new directory `catalogC` and copying `catalogA` and `catalogB` into it.

    This composability enables decentralized catalogs. The format permits Operator authors to maintain Operator-specific catalogs, and it permits maintainers to trivially build a catalog composed of individual Operator catalogs. File-based catalogs can be composed by combining multiple other catalogs, by extracting subsets of one catalog, or a combination of both of these.

    Note

    Duplicate packages and duplicate bundles within a package are not permitted. The `opm validate` command returns an error if any duplicates are found.

    Because Operator authors are most familiar with their Operator, its dependencies, and its upgrade compatibility, they are able to maintain their own Operator-specific catalog and have direct control over its contents. With file-based catalogs, Operator authors own the task of building and maintaining their packages in a catalog. Composite catalog maintainers, however, only own the task of curating the packages in their catalog and publishing the catalog to users.

Extensibility
:   The file-based catalog specification is a low-level representation of a catalog. While it can be maintained directly in its low-level form, catalog maintainers can build interesting extensions on top that can be used by their own custom tooling to make any number of mutations.

    For example, a tool could translate a high-level API, such as `(mode=semver)`, down to the low-level, file-based catalog format for upgrade paths. Or a catalog maintainer might need to customize all of the bundle metadata by adding a new property to bundles that meet a certain criteria.

    While this extensibility allows for additional official tooling to be developed on top of the low-level APIs for future OpenShift Container Platform releases, the major benefit is that catalog maintainers have this capability as well.

Important

As of OpenShift Container Platform 4.11, the default Red Hat-provided Operator catalog releases in the file-based catalog format. The default Red Hat-provided Operator catalogs for OpenShift Container Platform 4.6 through 4.10 released in the deprecated SQLite database format.

The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format.

Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format.

#### [4.1.2. Directory structure](#olm-fb-catalogs-structure_fbc) Copy linkLink copied to clipboard!

File-based catalogs can be stored and loaded from directory-based file systems. The `opm` CLI loads the catalog by walking the root directory and recursing into subdirectories. The CLI attempts to load every file it finds and fails if any errors occur.

Non-catalog files can be ignored using `.indexignore` files, which have the same rules for patterns and precedence as `.gitignore` files.

**Example `.indexignore` file**

```
# Ignore everything except non-object .json and .yaml files
**/*
!*.json
!*.yaml
**/objects/*.json
**/objects/*.yaml
```

Catalog maintainers have the flexibility to choose their layout, but it is recommended to store each package’s file-based catalog blobs in separate subdirectories. Each individual file can be either JSON or YAML; it is not necessary for every file in a catalog to use the same format.

**Basic recommended structure**

```
catalog
├── packageA
│   └── index.yaml
├── packageB
│   ├── .indexignore
│   ├── index.yaml
│   └── objects
│       └── packageB.v0.1.0.clusterserviceversion.yaml
└── packageC
    └── index.json
    └── deprecations.yaml
```

This recommended structure has the property that each subdirectory in the directory hierarchy is a self-contained catalog, which makes catalog composition, discovery, and navigation trivial file system operations. The catalog can also be included in a parent catalog by copying it into the parent catalog’s root directory.

#### [4.1.3. Schemas](#olm-fb-catalogs-schemas_fbc) Copy linkLink copied to clipboard!

File-based catalogs on OpenShift Container Platform use a CUE-based format with schemas that define catalog structure for Operator Lifecycle Manager (OLM). Each Operator package requires one `olm.package` blob, at least one `olm.channel` blob, and one or more `olm.bundle` blobs.

**`_Meta` schema**

```
_Meta: {
  // schema is required and must be a non-empty string
  schema: string & !=""

  // package is optional, but if it's defined, it must be a non-empty string
  package?: string & !=""

  // properties is optional, but if it's defined, it must be a list of 0 or more properties
  properties?: [... #Property]
}

#Property: {
  // type is required
  type: string & !=""

  // value is required, and it must not be null
  value: !=null
}
```

Note

No CUE schemas listed in this specification should be considered exhaustive. The `opm validate` command has additional validations that are difficult or impossible to express concisely in CUE.

Note

All `olm.*` schemas are reserved for OLM-defined schemas. Custom schemas must use a unique prefix, such as a domain that you own.

##### [4.1.3.1. olm.package schema](#olm-package-schema_fbc) Copy linkLink copied to clipboard!

The `olm.package` schema specifies package-level metadata for Operators in file-based catalogs, including name, default channel, and icon. Use this schema reference when you build or validate Operator package definitions for Operator Lifecycle Manager (OLM).

**Example 4.1. `olm.package` schema**

```
#Package: {
  schema: "olm.package"

  // Package name
  name: string & !=""

  // A description of the package
  description?: string

  // The package's default channel
  defaultChannel: string & !=""

  // An optional icon
  icon?: {
    base64data: string
    mediatype:  string
  }
}
```

##### [4.1.3.2. olm.channel schema](#olm-channel-schema_fbc) Copy linkLink copied to clipboard!

The `olm.channel` schema defines a channel within a package, the bundle entries that are members of the channel, and the upgrade paths for those bundles.

If a bundle entry represents an edge in multiple `olm.channel` blobs, it can only appear once per channel.

It is valid for an entry’s `replaces` value to reference another bundle name that cannot be found in this catalog or another catalog. However, all other channel invariants must hold true, such as a channel not having multiple heads.

**Example 4.2. `olm.channel` schema**

```
#Channel: {
  schema: "olm.channel"
  package: string & !=""
  name: string & !=""
  entries: [...#ChannelEntry]
}

#ChannelEntry: {
  // name is required. It is the name of an `olm.bundle` that
  // is present in the channel.
  name: string & !=""

  // replaces is optional. It is the name of bundle that is replaced
  // by this entry. It does not have to be present in the entry list.
  replaces?: string & !=""

  // skips is optional. It is a list of bundle names that are skipped by
  // this entry. The skipped bundles do not have to be present in the
  // entry list.
  skips?: [...string & !=""]

  // skipRange is optional. It is the semver range of bundle versions
  // that are skipped by this entry.
  skipRange?: string & !=""
}
```

Warning

When using the `skipRange` field, the skipped Operator versions are pruned from the update graph and are longer installable by users with the `spec.startingCSV` property of `Subscription` objects.

You can update an Operator incrementally while keeping previously installed versions available to users for future installation by using both the `skipRange` and `replaces` field. Ensure that the `replaces` field points to the immediate previous version of the Operator version in question.

##### [4.1.3.3. olm.bundle schema](#olm-bundle-schema_fbc) Copy linkLink copied to clipboard!

The `olm.bundle` schema defines the structure of bundle entries stored in an Operator catalog index. It specifies required fields such as package name, bundle name, image reference, and optional properties and related images.

**Example 4.3. `olm.bundle` schema**

```
#Bundle: {
  schema: "olm.bundle"
  package: string & !=""
  name: string & !=""
  image: string & !=""
  properties: [...#Property]
  relatedImages?: [...#RelatedImage]
}

#Property: {
  // type is required
  type: string & !=""

  // value is required, and it must not be null
  value: !=null
}

#RelatedImage: {
  // image is the image reference
  image: string & !=""

  // name is an optional descriptive name for an image that
  // helps identify its purpose in the context of the bundle
  name?: string & !=""
}
```

##### [4.1.3.4. olm.deprecations schema](#olm-deprecations-schema_fbc) Copy linkLink copied to clipboard!

The optional `olm.deprecations` schema defines deprecation information for packages, bundles, and channels in an Operator catalog. When you define this schema, the web console displays warning badges and deprecation messages in the software catalog.

An `olm.deprecations` schema entry contains one or more of the following `reference` types, which indicates the deprecation scope. After the Operator is installed, any specified messages can be viewed as status conditions on the related `Subscription` object.

Expand

Table 4.1. Deprecation reference types

| Type | Scope | Status condition |
| --- | --- | --- |
| `olm.package` | Represents the entire package | `PackageDeprecated` |
| `olm.channel` | Represents one channel | `ChannelDeprecated` |
| `olm.bundle` | Represents one bundle version | `BundleDeprecated` |

Show more

Each `reference` type has their own requirements, as detailed in the following example.

**Example `olm.deprecations` schema with each `reference` type**

```
schema: olm.deprecations
package: my-operator
entries:
  - reference:
      schema: olm.package
    message: |
    The 'my-operator' package is end of life. Please use the
    'my-operator-new' package for support.
  - reference:
      schema: olm.channel
      name: alpha
    message: |
    The 'alpha' channel is no longer supported. Please switch to the
    'stable' channel.
  - reference:
      schema: olm.bundle
      name: my-operator.v1.68.0
    message: |
    my-operator.v1.68.0 is deprecated. Uninstall my-operator.v1.68.0 and
    install my-operator.v1.72.0 for support.
```

* Each deprecation schema must have a `package` value, and that package reference must be unique across the catalog. There must not be an associated `name` field.
* The `olm.package` schema must not include a `name` field, because it is determined by the `package` field defined earlier in the schema.
* All `message` fields, for any `reference` type, must be a non-zero length and represented as an opaque text blob.
* The `name` field for the `olm.channel` schema is required.
* The `name` field for the `olm.bundle` schema is required.

Note

The deprecation feature does not consider overlapping deprecation, for example package versus channel versus bundle.

Operator authors can save `olm.deprecations` schema entries as a `deprecations.yaml` file in the same directory as the package’s `index.yaml` file:

**Example directory structure for a catalog with deprecations**

```
my-catalog
└── my-operator
    ├── index.yaml
    └── deprecations.yaml
```

#### [4.1.4. Properties](#olm-fb-catalogs-prop_fbc) Copy linkLink copied to clipboard!

Properties are arbitrary pieces of metadata that can be attached to file-based catalog schemas. The `type` field is a string that effectively specifies the semantic and syntactic meaning of the `value` field. The value can be any arbitrary JSON or YAML.

OLM defines a handful of property types, again using the reserved `olm.*` prefix.

##### [4.1.4.1. olm.package property](#olm-fb-catalogs-package-prop_fbc) Copy linkLink copied to clipboard!

The `olm.package` property defines the package name and version. This is a required property on bundles, and there must be exactly one of these properties. The `packageName` field must match the bundle’s first-class `package` field, and the `version` field must be a valid semantic version.

**`olm.package` property**

```
#PropertyPackage: {
  type: "olm.package"
  value: {
    packageName: string & !=""
    version: string & !=""
  }
}
```

##### [4.1.4.2. olm.gvk property](#olm-fb-catalogs-gvk-prop_fbc) Copy linkLink copied to clipboard!

The `olm.gvk` property defines the group/version/kind (GVK) of a Kubernetes API that is provided by this bundle. This property is used by OLM to resolve a bundle with this property as a dependency for other bundles that list the same GVK as a required API. The GVK must adhere to Kubernetes GVK validations.

**`olm.gvk` property**

```
#PropertyGVK: {
  type: "olm.gvk"
  value: {
    group: string & !=""
    version: string & !=""
    kind: string & !=""
  }
}
```

##### [4.1.4.3. olm.package.required](#olm-fb-catalogs-package-reqd-prop_fbc) Copy linkLink copied to clipboard!

The `olm.package.required` property defines the package name and version range of another package that this bundle requires. For every required package property a bundle lists, OLM ensures there is an Operator installed on the cluster for the listed package and in the required version range. The `versionRange` field must be a valid semantic version (semver) range.

**`olm.package.required` property**

```
#PropertyPackageRequired: {
  type: "olm.package.required"
  value: {
    packageName: string & !=""
    versionRange: string & !=""
  }
}
```

##### [4.1.4.4. olm.gvk.required](#olm-fb-catalogs-gvk-reqd-prop_fbc) Copy linkLink copied to clipboard!

The `olm.gvk.required` property defines the group/version/kind (GVK) of a Kubernetes API that this bundle requires. For every required GVK property a bundle lists, OLM ensures there is an Operator installed on the cluster that provides it. The GVK must adhere to Kubernetes GVK validations.

**`olm.gvk.required` property**

```
#PropertyGVKRequired: {
  type: "olm.gvk.required"
  value: {
    group: string & !=""
    version: string & !=""
    kind: string & !=""
  }
}
```

#### [4.1.5. Example catalog](#olm-fb-catalogs-example_fbc) Copy linkLink copied to clipboard!

With file-based catalogs, catalog maintainers can focus on Operator curation and compatibility.

Because Operator authors have already produced Operator-specific catalogs for their Operators, catalog maintainers can build their catalog by rendering each Operator catalog into a subdirectory of the catalog’s root directory.

There are many possible ways to build a file-based catalog; the following steps outline a simple approach:

1. Maintain a single configuration file for the catalog, containing image references for each Operator in the catalog:

   **Example catalog configuration file**

   ```
   name: community-operators
   repo: quay.io/community-operators/catalog
   tag: latest
   references:
   - name: etcd-operator
     image: quay.io/etcd-operator/index@sha256:5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03
   - name: prometheus-operator
     image: quay.io/prometheus-operator/index@sha256:e258d248fda94c63753607f7c4494ee0fcbe92f1a76bfdac795c9d84101eb317
   ```
2. Run a script that parses the configuration file and creates a new catalog from its references:

   **Example script**

   ```
   name=$(yq eval '.name' catalog.yaml)
   mkdir "$name"
   yq eval '.name + "/" + .references[].name' catalog.yaml | xargs mkdir
   for l in $(yq e '.name as $catalog | .references[] | .image + "|" + $catalog + "/" + .name + "/index.yaml"' catalog.yaml); do
     image=$(echo $l | cut -d'|' -f1)
     file=$(echo $l | cut -d'|' -f2)
     opm render "$image" > "$file"
   done
   opm generate dockerfile "$name"
   indexImage=$(yq eval '.repo + ":" + .tag' catalog.yaml)
   docker build -t "$indexImage" -f "$name.Dockerfile" .
   docker push "$indexImage"
   ```

#### [4.1.6. Guidelines](#olm-fb-catalogs-guidelines_fbc) Copy linkLink copied to clipboard!

Follow the guidelines to maintain file-based Operator catalogs. Treat bundle images and metadata as immutable. Store catalog metadata in source control as the source of truth.

##### [4.1.6.1. Immutable bundles](#olm-fb-catalogs-immutable_fbc) Copy linkLink copied to clipboard!

The general advice with Operator Lifecycle Manager (OLM) is that bundle images and their metadata should be treated as immutable.

If a broken bundle has been pushed to a catalog, you must assume that at least one of your users has upgraded to that bundle. Based on that assumption, you must release another bundle with an upgrade path from the broken bundle to ensure users with the broken bundle installed receive an upgrade. OLM will not reinstall an installed bundle if the contents of that bundle are updated in the catalog.

However, there are some cases where a change in the catalog metadata is preferred:

* Channel promotion: If you already released a bundle and later decide that you want to add it to another channel, you can add an entry for your bundle in another `olm.channel` blob.
* New upgrade paths: If you release a new `1.2.z` bundle version, for example `1.2.4`, but `1.3.0` is already released, you can update the catalog metadata for `1.3.0` to skip `1.2.4`.

##### [4.1.6.2. Source control](#olm-fb-catalogs-source-control_fbc) Copy linkLink copied to clipboard!

Catalog metadata should be stored in source control and treated as the source of truth. Updates to catalog images should include the following steps:

1. Update the source-controlled catalog directory with a new commit.
2. Build and push the catalog image. Use a consistent tagging taxonomy, such as `:latest` or `:<target_cluster_version>`, so that users can receive updates to a catalog as they become available.

Note

For more information about creating file-based catalogs by using the `opm` CLI, see "Creating a file-based catalog image".

#### [4.1.7. CLI usage](#olm-fbc-cli_fbc) Copy linkLink copied to clipboard!

To create and manage file-based catalogs, you can use the `opm` command-line interface (CLI).

For instructions about creating file-based catalogs by using the `opm` CLI, see "Creating a file-based catalog image".

For reference documentation about the `opm` CLI commands related to managing file-based catalogs, see "opm CLI reference".

#### [4.1.8. Automation](#olm-fb-catalogs-automation_fbc) Copy linkLink copied to clipboard!

Operator authors and catalog maintainers can automate file-based catalog maintenance with CI/CD workflows.

Catalog maintainers can use GitOps automation to accomplish the following example tasks:

* Check that pull request (PR) authors are permitted to make the requested changes, for example by updating their package’s image reference.
* Check that the catalog updates pass the `opm validate` command.
* Check that the updated bundle or catalog image references exist, the catalog images run successfully in a cluster, and Operators from that package can be successfully installed.
* Automatically merge PRs that pass the previous checks.
* Automatically rebuild and republish the catalog image.

### [4.2. Red Hat-provided catalogs](#rh-catalogs) Copy linkLink copied to clipboard!

Red Hat provides several Operator catalogs that are included with OpenShift Container Platform by default.

#### [4.2.1. About Red Hat-provided Operator catalogs](#olm-rh-catalogs_rh-catalogs) Copy linkLink copied to clipboard!

The Red Hat-provided catalog sources are installed by default in the `openshift-marketplace` namespace, which makes the catalogs available cluster-wide in all namespaces.

The following Operator catalogs are distributed by Red Hat:

Expand

| Catalog | Index image | Description |
| --- | --- | --- |
| `redhat-operators` | `registry.redhat.io/redhat/redhat-operator-index:v4.22` | Red Hat products packaged and shipped by Red Hat. Supported by Red Hat. |
| `certified-operators` | `registry.redhat.io/redhat/certified-operator-index:v4.22` | Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV. |
| `community-operators` | `registry.redhat.io/redhat/community-operator-index:v4.22` | Software maintained by relevant representatives in the community Operators GitHub repository. No official support. |

Show more

During a cluster upgrade, the index image tag for the default Red Hat-provided catalog sources are updated automatically by the Cluster Version Operator (CVO) so that Operator Lifecycle Manager (OLM) pulls the updated version of the catalog. For example, during an upgrade from OpenShift Container Platform 4.8 to 4.9, the `spec.image` field in the `CatalogSource` object for the `redhat-operators` catalog is updated from:

```
registry.redhat.io/redhat/redhat-operator-index:v4.8
```

to:

```
registry.redhat.io/redhat/redhat-operator-index:v4.9
```

### [4.3. Managing catalogs](#managing-catalogs) Copy linkLink copied to clipboard!

Cluster administrators can add *catalogs*, or curated collections of Operators and Kubernetes extensions, to their clusters. Operator authors publish their products to these catalogs.

When you add a catalog to your cluster, you have access to the versions, patches, and over-the-air updates of the Operators and extensions that are published to the catalog.

You can manage catalogs and extensions declaratively from the CLI by using custom resources (CRs).

*File-based catalogs* are the latest iteration of the catalog format in Operator Lifecycle Manager (OLM). It is a plain text-based (JSON or YAML) and declarative config evolution of the earlier SQLite database format, and it is fully compatible with earlier versions.

Important

Kubernetes periodically deprecates certain APIs that are removed in subsequent releases. As a result, Operators are unable to use removed APIs starting with the version of OpenShift Container Platform that uses the Kubernetes version that removed the API.

#### [4.3.1. About catalogs in OLM v1](#olmv1-about-catalogs_managing-catalogs) Copy linkLink copied to clipboard!

You can discover installable content by querying a catalog for Kubernetes extensions, such as Operators and controllers, by using the catalogd component.

Catalogd is a Kubernetes extension that unpacks catalog content for on-cluster clients and is part of the Operator Lifecycle Manager (OLM) v1 suite of microservices. Currently, catalogd unpacks catalog content that is packaged and distributed as container images.

#### [4.3.2. Red Hat-provided Operator catalogs in OLM v1](#olmv1-red-hat-catalogs_managing-catalogs) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 includes several Red Hat-provided Operator catalogs on the cluster by default. If you want to add a catalog to your cluster, create a custom resource (CR) for the catalog and apply it to the cluster.

The following custom resource (CR) examples show the default catalogs installed on the cluster:

**Red Hat Operators catalog**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-redhat-operators
spec:
  priority: -100
  source:
    image:
      pollIntervalMinutes: <poll_interval_duration>
      ref: registry.redhat.io/redhat/redhat-operator-index:v4.22
    type: Image
```

Replace `<poll_interval_duration>` with the interval in minutes for polling the remote registry for newer image digests. To disable polling, do not set the field.

**Certified Operators catalog**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-certified-operators
spec:
priority: -200
  source:
    type: image
    image:
      pollIntervalMinutes: 10
      ref: registry.redhat.io/redhat/certified-operator-index:v4.22
    type: Image
```

**Red Hat Marketplace catalog**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-redhat-marketplace
spec:
  priority: -300
  source:
    image:
      pollIntervalMinutes: 10
      ref: registry.redhat.io/redhat/redhat-marketplace-index:v4.22
    type: Image
```

**Community Operators catalog**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: openshift-community-operators
spec:
  priority: -400
  source:
    image:
      pollIntervalMinutes: 10
      ref: registry.redhat.io/redhat/community-operator-index:v4.22
    type: Image
```

The following command adds a catalog to your cluster:

**Command syntax**

```
$ oc apply -f <catalog_name>.yaml
```

Replace `<catalog_name>.yaml` with the catalog CR, such as `my-catalog.yaml`.

#### [4.3.3. Adding a catalog to a cluster](#olmv1-adding-a-catalog-to-a-cluster_managing-catalogs) Copy linkLink copied to clipboard!

To add a catalog to a cluster for Operator Lifecycle Manager (OLM) v1 usage, create a `ClusterCatalog` custom resource (CR) and apply it to the cluster.

**Procedure**

1. Create a catalog custom resource (CR), similar to the following example:

   **Example `my-redhat-operators.yaml` file**

   ```
   apiVersion: olm.operatorframework.io/v1
   kind: ClusterCatalog
   metadata:
     name: my-redhat-operators
   spec:
     priority: 1000
     source:
       image:
         pollIntervalMinutes: 10
         ref: registry.redhat.io/redhat/community-operator-index:v4.22
       type: Image
   ```

   where:

   `metadata.name`
   :   The catalog is automatically labeled with the value of the `metadata.name` field when it is applied to the cluster. For more information about labels and catalog selection, see "Catalog content resolution".

   `spec.priority`
   :   Optional: Specifies the priority of the catalog in relation to the other catalogs on the cluster. For more information, see "Catalog selection by priority".

   `spec.source.image.pollIntervalMinutes`
   :   Specifies the interval in minutes for polling the remote registry for newer image digests. To disable polling, do not set the field.

   `spec.source.image.ref`
   :   Specifies the catalog image in the `spec.source.image.ref` field.
2. Add the catalog to your cluster by running the following command:

   ```
   $ oc apply -f my-redhat-operators.yaml
   ```

   **Example output**

   ```
   clustercatalog.olm.operatorframework.io/my-redhat-operators created
   ```

**Verification**

* Run the following commands to verify the status of your catalog:

  1. Check if your catalog is available by running the following command:

     ```
     $ oc get clustercatalog
     ```

     **Example output**

     ```
     NAME                            LASTUNPACKED   SERVING   AGE
     my-redhat-operators             55s            True      64s
     openshift-certified-operators   83m            True      84m
     openshift-community-operators   43m            True      84m
     openshift-redhat-marketplace    83m            True      84m
     openshift-redhat-operators      54m            True      84m
     ```
  2. Check the status of your catalog by running the following command:

     ```
     $ oc describe clustercatalog my-redhat-operators
     ```

     **Example output**

     ```
     Name:         my-redhat-operators
     Namespace:
     Labels:       olm.operatorframework.io/metadata.name=my-redhat-operators
     Annotations:  <none>
     API Version:  olm.operatorframework.io/v1
     Kind:         ClusterCatalog
     Metadata:
       Creation Timestamp:  2025-02-18T20:28:50Z
       Finalizers:
         olm.operatorframework.io/delete-server-cache
       Generation:        1
       Resource Version:  50248
       UID:               86adf94f-d2a8-4e70-895b-31139f2eeab7
     Spec:
       Availability Mode:  Available
       Priority:           1000
       Source:
         Image:
           Poll Interval Minutes:  10
           Ref:                    registry.redhat.io/redhat/community-operator-index:v4.22
         Type:                     Image
     Status:
       Conditions:
         Last Transition Time:  2025-02-18T20:29:00Z
         Message:               Successfully unpacked and stored content from resolved source
         Observed Generation:   1
         Reason:                Succeeded
         Status:                True
         Type:                  Progressing
         Last Transition Time:  2025-02-18T20:29:00Z
         Message:               Serving desired content from resolved source
         Observed Generation:   1
         Reason:                Available
         Status:                True
         Type:                  Serving
       Last Unpacked:           2025-02-18T20:28:59Z
       Resolved Source:
         Image:
           Ref:  registry.redhat.io/redhat/community-operator-index@sha256:11627ea6fdd06b8092df815076e03cae9b7cede8b353c0b461328842d02896c5
         Type:   Image
       Urls:
         Base:  https://catalogd-service.openshift-catalogd.svc/catalogs/my-redhat-operators
     Events:    <none>
     ```

     In the output, the `Status` section describes the status of the catalog. In the `Status` section, the `Reason` field displays the reason the catalog is in the current state. In the `Resolved Source` section, the `Ref` field displays the image reference of the catalog.

#### [4.3.4. Deleting a catalog](#olmv1-deleting-catalog_managing-catalogs) Copy linkLink copied to clipboard!

You can delete a catalog by deleting its custom resource (CR).

**Prerequisites**

* You have a catalog installed.

**Procedure**

* Delete a catalog by running the following command:

  ```
  $ oc delete clustercatalog <catalog_name>
  ```

  **Example output**

  ```
  clustercatalog.olm.operatorframework.io "my-redhat-operators" deleted
  ```

**Verification**

* Verify the catalog is deleted by running the following command:

  ```
  $ oc get clustercatalog
  ```

#### [4.3.5. Disabling a default catalog](#olmv1-disabling-a-default-catalog_managing-catalogs) Copy linkLink copied to clipboard!

You can disable the Red Hat-provided catalogs that are included with OpenShift Container Platform by default.

**Procedure**

* Disable a default catalog by running the following command:

  ```
  $ oc patch clustercatalog openshift-certified-operators -p \
    '{"spec": {"availabilityMode": "Unavailable"}}' --type=merge
  ```

  **Example output**

  ```
  clustercatalog.olm.operatorframework.io/openshift-certified-operators patched
  ```

**Verification**

* Verify the catalog is disabled by running the following command:

  ```
  $ oc get clustercatalog openshift-certified-operators
  ```

  **Example output**

  ```
  NAME                            LASTUNPACKED   SERVING   AGE
  openshift-certified-operators                  False     6h54m
  ```

### [4.4. Catalog content resolution](#catalog-content-resolution) Copy linkLink copied to clipboard!

When you specify the cluster extension you want to install in a custom resource (CR), Operator Lifecycle Manager (OLM) v1 uses catalog selection to resolve what content is installed.

You can perform the following actions to control the selection of catalog content:

* Specify labels to select the catalog.
* Use match expressions to perform complex filtering across catalogs.
* Set catalog priority.

If you do not specify any catalog selection criteria, Operator Lifecycle Manager (OLM) v1 selects an extension from any available catalog on the cluster that provides the requested package.

During resolution, bundles that are not deprecated are preferred over deprecated bundles by default.

#### [4.4.1. Catalog selection by name](#olmv1-catalog-selection-by-name_catalog-content-resolution) Copy linkLink copied to clipboard!

When a catalog is added to a cluster, a label is created by using the value of the `metadata.name` field of the catalog custom resource (CR). In the CR of an extension, you can specify the catalog name by using the `spec.source.catalog.selector.matchLabels` field.

The value of the `matchLabels` field uses the following format:

**Example label derived from the `metadata.name` field**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
  labels:
    olm.operatorframework.io/metadata.name: <example_extension>
...
```

The `<example_extension>` value is the label derived from the `metadata.name` field and automatically added when the catalog is applied.

The following example resolves the `<example_extension>-operator` package from a catalog with the `openshift-redhat-operators` label:

**Example extension CR**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchLabels:
          olm.operatorframework.io/metadata.name: openshift-redhat-operators
```

#### [4.4.2. Catalog selection by labels or expressions](#olmv1-catalog-selection-by-labels-or-exp_catalog-content-resolution) Copy linkLink copied to clipboard!

You can add metadata to a catalog by using labels in the custom resource (CR) of a cluster catalog. You can then filter catalog selection by specifying the assigned labels or using expressions in the CR of the cluster extension.

The following cluster catalog CR adds the `example.com/support` label with the value of `true` to the `catalog-a` cluster catalog:

**Example cluster catalog CR with labels**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: catalog-a
  labels:
    example.com/support: "true"
spec:
  source:
    type: Image
    image:
      ref: quay.io/example/content-management-a:latest
```

The following cluster extension CR uses the `matchLabels` selector to select catalogs with the `example.com/support` label and the value of `true`:

**Example cluster extension CR with `matchLabels` selector**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchLabels:
          example.com/support: "true"
```

You can use the `matchExpressions` field to perform more complex filtering for labels. The following cluster extension CR selects catalogs with the `example.com/support` label and a value of `production` or `supported`:

**Example cluster extension CR with `matchExpression` selector**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchExpressions:
          - key: example.com/support
            operator: In
            values:
              - "production"
              - "supported"
```

Note

If you use both the `matchLabels` and `matchExpressions` fields, the selected catalog must satisfy all specified criteria.

#### [4.4.3. Catalog exclusion by labels or expressions](#olmv1-catalog-exclusion-by-labels-or-expressions_catalog-content-resolution) Copy linkLink copied to clipboard!

You can exclude catalogs by using match expressions on metadata with the `NotIn` or `DoesNotExist` operators.

The following custom resources (CRs) add an `example.com/testing` label to the `unwanted-catalog-1` and `unwanted-catalog-2` cluster catalogs:

**Example cluster catalog CR**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: unwanted-catalog-1
  labels:
    example.com/testing: "true"
spec:
  source:
    type: Image
    image:
      ref: quay.io/example/content-management-a:latest
```

**Example cluster catalog CR**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: unwanted-catalog-2
  labels:
    example.com/testing: "true"
spec:
  source:
    type: Image
    image:
      ref: quay.io/example/content-management-b:latest
```

The following cluster extension CR excludes selection from the `unwanted-catalog-1` catalog:

**Example cluster extension CR that excludes a specific catalog**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchExpressions:
          - key: olm.operatorframework.io/metadata.name
            operator: NotIn
            values:
              - unwanted-catalog-1
```

The following cluster extension CR selects from catalogs that do not have the `example.com/testing` label. As a result, both `unwanted-catalog-1` and `unwanted-catalog-2` are excluded from catalog selection.

**Example cluster extension CR that excludes catalogs with a specific label**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <example_extension>
spec:
  namespace: <example_namespace>
  serviceAccount:
    name: <example_extension>-installer
  source:
    sourceType: Catalog
    catalog:
      packageName: <example_extension>-operator
      selector:
        matchExpressions:
          - key: example.com/testing
            operator: DoesNotExist
```

#### [4.4.4. Catalog selection by priority](#olmv1-catalog-exclusion-by-priority_catalog-content-resolution) Copy linkLink copied to clipboard!

When multiple catalogs provide the same package, you can resolve ambiguities by specifying the priority in the custom resource (CR) of each catalog. If unspecified, catalogs have a default priority value of `0`. The priority can be any positive or negative 32-bit integer.

Note

* During bundle resolution, catalogs with higher priority values are selected over catalogs with lower priority values.
* Bundles that are not deprecated are prioritized over bundles that are deprecated.
* If multiple bundles exist in catalogs with the same priority and the catalog selection is ambiguous, an error is printed.

**Example cluster catalog CR with a higher priority**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: high-priority-catalog
spec:
  priority: 1000
  source:
    type: Image
    image:
      ref: quay.io/example/higher-priority-catalog:latest
```

**Example cluster catalog CR with a lower priority**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterCatalog
metadata:
  name: lower-priority-catalog
spec:
  priority: 10
  source:
    type: Image
    image:
      ref: quay.io/example/lower-priority-catalog:latest
```

#### [4.4.5. Troubleshooting catalog selection errors](#olmv1-troubleshooting-catalog-selection-errors_catalog-content-resolution) Copy linkLink copied to clipboard!

If bundle resolution fails because of ambiguity or because no catalog is selected, an error message is printed in the `status.conditions` field of the cluster extension.

Perform the following actions to troubleshoot catalog selection errors:

* Refine your selection criteria using labels or expressions.
* Adjust your catalog priorities.
* Ensure that only one bundle matches your package name and version requirements.

### [4.5. Creating catalogs](#creating-catalogs) Copy linkLink copied to clipboard!

Catalog maintainers can create new catalogs in the file-based catalog format for use with Operator Lifecycle Manager (OLM) v1 on OpenShift Container Platform.

#### [4.5.1. Creating a file-based catalog image](#olm-creating-fb-catalog-image_creating-catalogs) Copy linkLink copied to clipboard!

You can use the `opm` CLI to create a catalog image that uses the plain text *file-based catalog* format (JSON or YAML), which replaces the deprecated SQLite database format.

**Prerequisites**

* You have installed the `opm` CLI.
* You have `podman` version 1.9.3+.
* A bundle image is built and pushed to a registry that supports [Docker v2-2](https://docs.docker.com/registry/spec/manifest-v2-2/).

**Procedure**

1. Initialize the catalog:

   1. Create a directory for the catalog by running the following command:

      ```
      $ mkdir <catalog_dir>
      ```
   2. Generate a Dockerfile that can build a catalog image by running the `opm generate dockerfile` command:

      ```
      $ opm generate dockerfile <catalog_dir> \
          -i registry.redhat.io/openshift4/ose-operator-registry-rhel9:v4.22
      ```

      + Specify the official Red Hat base image by using the `-i` flag, otherwise the Dockerfile uses the default upstream image.

      The Dockerfile must be in the same parent directory as the catalog directory that you created in the previous step:

      **Example directory structure**

      ```
      .
      ├── <catalog_dir>
      └── <catalog_dir>.Dockerfile
      ```

      where:

      `.`
      :   Specifies the parent directory.

      `<catalog_dir>`
      :   Specifies the catalog directory.

      `<catalog_dir>.Dockerfile`
      :   Specifies the Dockerfile generated by the `opm generate dockerfile` command.
   3. Populate the catalog with the package definition for your Operator by running the `opm init` command:

      ```
      $ opm init <operator_name> \
          --default-channel=preview \
          --description=./README.md \
          --icon=./operator-icon.svg \
          --output yaml \
          > <catalog_dir>/index.yaml
      ```

      * Replace the `<operator_name>` variable with the Operator or package, name.
      * The `--default-channel` flag specifies the channel that subscriptions default to if unspecified.
      * The `--description` flag specifies the path to the Operator’s `README.md` or other documentation.
      * The `--icon` flag specifies the path to the Operator’s icon.
      * The `--output` flag specifies the output format. `JSON` or `YAML` are valid values.
      * Replace the `<catalog_dir>` variable with the path for creating the catalog configuration file.

        This command generates an `olm.package` declarative config blob in the specified catalog configuration file.
2. Add a bundle to the catalog by running the `opm render` command:

   ```
   $ opm render <registry>/<namespace>/<bundle_image_name>:<tag> \
       --output=yaml \
       >> <catalog_dir>/index.yaml
   ```

   where:

   <registry>/<namespace>/<bundle\_image\_name>:<tag>
   :   Specifies the pull spec for the bundle image.

   <catalog\_dir>/index.yaml
   :   Specifies the path to the catalog configuration file.

       Note

       Channels must contain at least one bundle.
3. Add a channel entry for the bundle. For example, modify the following example to your specifications, and add it to your `<catalog_dir>/index.yaml` file:

   **Example channel entry**

   ```
   ---
   schema: olm.channel
   package: <operator_name>
   name: preview
   entries:
     - name: <operator_name>.v0.1.0
   ```

   Ensure that you include the period (`.`) after the `` <operator_name>`variable but before the `v `` in the version. Otherwise, the entry fails to pass the `opm validate` command.
4. Validate the file-based catalog:

   1. Run the `opm validate` command against the catalog directory:

      ```
      $ opm validate <catalog_dir>
      ```
   2. Check that the error code is `0`:

      ```
      $ echo $?
      ```

      **Example output**

      ```
      0
      ```
5. Build the catalog image by running the `podman build` command:

   ```
   $ podman build . \
       -f <catalog_dir>.Dockerfile \
       -t <registry>/<namespace>/<catalog_image_name>:<tag>
   ```
6. Push the catalog image to a registry:

   1. If required, authenticate with your target registry by running the `podman login` command:

      ```
      $ podman login <registry>
      ```
   2. Push the catalog image by running the `podman push` command:

      ```
      $ podman push <registry>/<namespace>/<catalog_image_name>:<tag>
      ```

#### [4.5.2. Updating or filtering a file-based catalog image](#olm-filtering-fbc_creating-catalogs) Copy linkLink copied to clipboard!

To keep your catalog accurate and ensure users can safely upgrade installed Operators, you can use the `opm` CLI to extract, edit, and rebuild a file-based catalog image. You can also specify deprecation messages for packages, channels, and bundles.

After you complete the changes, you can rebuild the image as an updated version of the catalog.

Note

Alternatively, if you already have a catalog image on a mirror registry, you can use the oc-mirror CLI plugin to automatically prune any removed images from an updated source version of that catalog image while mirroring it to the target registry.

For more information about the oc-mirror plugin and this use case, see the "Keeping your mirror registry content updated" section, and specifically the "Pruning images" subsection, of "Mirroring images for a disconnected installation using the oc-mirror plugin".

**Prerequisites**

* You have the following on your workstation:

  + The `opm` CLI.
  + `podman` version 1.9.3+.
  + A file-based catalog image.
  + A catalog directory structure recently initialized on your workstation related to this catalog.

    If you do not have an initialized catalog directory, create the directory and generate the Dockerfile. For more information, see the "Initialize the catalog" step from the "Creating a file-based catalog image" procedure.

**Procedure**

1. Extract the contents of the catalog image in YAML format to an `index.yaml` file in your catalog directory:

   ```
   $ opm render <registry>/<namespace>/<catalog_image_name>:<tag> \
       -o yaml > <catalog_dir>/index.yaml
   ```

   Note

   Alternatively, you can use the `-o json` flag to output in JSON format.
2. Modify the contents of the resulting `index.yaml` file to your specifications:

   Important

   After a bundle has been published in a catalog, assume that one of your users has installed it. Ensure that all previously published bundles in a catalog have an update path to the current or newer channel head to avoid stranding users that have that version installed.

   * To add an Operator, follow the steps for creating package, bundle, and channel entries in the "Creating a file-based catalog image" procedure.
   * To remove an Operator, delete the set of `olm.package`, `olm.channel`, and `olm.bundle` blobs that relate to the package. The following example shows a set that must be deleted to remove the `example-operator` package from the catalog:

     **Example removed entries**

     ```
     ---
     defaultChannel: release-2.7
     icon:
       base64data: <base64_string>
       mediatype: image/svg+xml
     name: example-operator
     schema: olm.package
     ---
     entries:
     - name: example-operator.v2.7.0
       skipRange: '>=2.6.0 <2.7.0'
     - name: example-operator.v2.7.1
       replaces: example-operator.v2.7.0
       skipRange: '>=2.6.0 <2.7.1'
     - name: example-operator.v2.7.2
       replaces: example-operator.v2.7.1
       skipRange: '>=2.6.0 <2.7.2'
     - name: example-operator.v2.7.3
       replaces: example-operator.v2.7.2
       skipRange: '>=2.6.0 <2.7.3'
     - name: example-operator.v2.7.4
       replaces: example-operator.v2.7.3
       skipRange: '>=2.6.0 <2.7.4'
     name: release-2.7
     package: example-operator
     schema: olm.channel
     ---
     image: example.com/example-inc/example-operator-bundle@sha256:<digest>
     name: example-operator.v2.7.0
     package: example-operator
     properties:
     - type: olm.gvk
       value:
         group: example-group.example.io
         kind: MyObject
         version: v1alpha1
     - type: olm.gvk
       value:
         group: example-group.example.io
         kind: MyOtherObject
         version: v1beta1
     - type: olm.package
       value:
         packageName: example-operator
         version: 2.7.0
     - type: olm.bundle.object
       value:
         data: <base64_string>
     - type: olm.bundle.object
       value:
         data: <base64_string>
     relatedImages:
     - image: example.com/example-inc/example-related-image@sha256:<digest>
       name: example-related-image
     schema: olm.bundle
     ---
     ```
   * To add or update deprecation messages for an Operator, ensure there is a `deprecations.yaml` file in the same directory as the package’s `index.yaml` file. For information on the `deprecations.yaml` file format, see "olm.deprecations schema".
3. Save your changes.
4. Validate the catalog:

   ```
   $ opm validate <catalog_dir>
   ```
5. Rebuild the catalog:

   ```
   $ podman build . \
       -f <catalog_dir>.Dockerfile \
       -t <registry>/<namespace>/<catalog_image_name>:<tag>
   ```
6. Push the updated catalog image to a registry:

   ```
   $ podman push <registry>/<namespace>/<catalog_image_name>:<tag>
   ```

**Verification**

1. In the web console, navigate to the OperatorHub configuration resource in the **Administration** → **Cluster Settings** → **Configuration** page.
2. Add the catalog source or update the existing catalog source to use the pull spec for your updated catalog image.

   For more information, see "Adding a catalog source to a cluster".
3. After the catalog source is in a **READY** state, navigate to the **Ecosystem** → **Software Catalog** page. Select **Operators** under the **Type** heading and check that the changes you made are reflected in the list of Operators.

### [4.6. Disconnected environment support in OLM v1](#disconnected-catalogs) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 supports cluster extension lifecycle management in internet-disconnected environments. This feature helps cluster administrators run mission-critical production workloads in high-security, disconnected clusters.

#### [4.6.1. About disconnected support and the oc-mirror plugin in OLM v1](#olmv1-about-disconnected_disconnected-catalogs) Copy linkLink copied to clipboard!

After you use the oc-mirror plugin for the OpenShift CLI (`oc`) to mirror images to a mirror registry, OLM v1 relies on specific resource sets to function.

Depending on your oc-mirror plugin version, OLM v1 uses one of the following resource sets:

oc-mirror plugin v1
:   Automatically generates `ImageContentSourcePolicy` resources and requires manually created `ClusterCatalog` resources.

oc-mirror plugin v2
:   Automatically generates `ImageDigestMirrorSet`, `ImageTagMirrorSet`, and `ClusterCatalog` resources.

Note

The oc-mirror plugin v2 is the recommended version for mirroring.

## [Chapter 5. Cluster extensions](#cluster-extensions) Copy linkLink copied to clipboard!

### [5.1. Supported extensions](#olmv1-supported-extensions) Copy linkLink copied to clipboard!

To install an Operator as a cluster extension, it must meet bundle format, install mode, and dependency requirements. Operator Lifecycle Manager (OLM) v1 supports extensions that use webhooks for validation, mutation, or conversion.

Operator Lifecycle Manager (OLM) v1 supports extensions that use the `AllNamespaces` install mode. With this mode, the Operator watches and manages resources across all namespaces in the cluster.

As a Technology Preview feature, you can configure an extension to watch a specific namespace. This limits watching to one namespace instead of the entire cluster.

#### [5.1.1. Supported bundle formats and dependencies](#olmv1-about-supported-bundle-formats_olmv1-supported-extensions) Copy linkLink copied to clipboard!

To install an Operator as a cluster extension, the Operator must be packaged using the `registry+v1` bundle format. OLM v1 does not support Operators that declare dependencies by using file-based catalog properties.

To install an Operator as a cluster extension, it must meet the following criteria:

* The Operator is packaged using the `registry+v1` bundle format.
* The Operator does not declare dependencies by using the following file-based catalog properties:

  + `olm.gvk.required`
  + `olm.package.required`
  + `olm.constraint`

OLM v1 verifies that an Operator meets these requirements during installation. If an Operator does not meet these criteria, OLM v1 reports the issue in the cluster extension status conditions.

Operator Lifecycle Manager (OLM) v1 does not support the `OperatorConditions` API introduced in OLM (Classic).

If an extension relies on only the `OperatorConditions` API to manage updates, the extension might not install correctly. Most extensions that rely on this API fail at start time, but some might fail during reconciliation.

As a workaround, you can pin your extension to a specific version. When you want to update your extension, consult the extension’s documentation to find out when it is safe to pin the extension to a new version.

#### [5.1.2. Webhook support](#olmv1-webhook-support_olmv1-supported-extensions) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 supports Operators that use webhooks for validation, mutation, or conversion. Operators use webhooks to enforce security policies or inject configurations into resources.

The OpenShift Service CA Operator automatically manages webhook certificates. When you install an Operator that includes webhooks, the OpenShift Service CA Operator completes the following actions:

* Applies Service CA annotations to webhook configurations and services.
* Generates TLS certificates in the namespace where you install the cluster extension.
* Mounts certificate secrets to the Operator deployment.
* Configures webhook services with proper TLS settings.

### [5.2. Managing cluster extensions](#managing-ce) Copy linkLink copied to clipboard!

You use catalogs to access the versions, patches, and over-the-air updates for extensions and Operators. You use custom resources (CRs) to manage extensions declaratively from the CLI.

Note

For OpenShift Container Platform 4.22, documented procedures for OLM v1 are CLI-based only. Alternatively, administrators can create and view related objects in the web console by using normal methods, such as the **Import YAML** and **Search** pages. However, the existing **Software Catalog** and **Installed Operators** pages do not yet display OLM v1 components.

#### [5.2.1. Finding Operators to install from a catalog](#olmv1-finding-operators-to-install_managing-ce) Copy linkLink copied to clipboard!

After you add a catalog to your cluster, you can query the catalog to find Operators and extensions to install.

Currently in Operator Lifecycle Manager (OLM) v1, you cannot query on-cluster catalogs managed by catalogd. In OLM v1, you must use the `opm` and `jq` CLI tools to query the catalog registry.

**Prerequisites**

* You have added a catalog to your cluster.
* You have installed the `jq` CLI tool.
* You have installed the `opm` CLI tool.

**Procedure**

1. To return a list of extensions that support the `AllNamespaces` install mode and do not use webhooks, enter the following command:

   ```
   $ opm render <catalog_registry_url>:<tag> \
     | jq -cs '[.[] | select(.schema == "olm.bundle" \
     and (.properties[] | select(.type == "olm.csv.metadata").value.installModes[] \
     | select(.type == "AllNamespaces" and .supported == true)) \
     and .spec.webhookdefinitions == null) | .package] | unique[]'
   ```

   where:

   `catalog_registry_url`
   :   Specifies the URL of the catalog registry, such as `registry.redhat.io/redhat/redhat-operator-index`.

   `tag`
   :   Specifies the tag or version of the catalog, such as `v4.22` or `latest`.

       **Example command**

       ```
       $ opm render \
         registry.redhat.io/redhat/redhat-operator-index:v4.22 \
         | jq -cs '[.[] | select(.schema == "olm.bundle" \
         and (.properties[] | select(.type == "olm.csv.metadata").value.installModes[] \
         | select(.type == "AllNamespaces" and .supported == true)) \
         and .spec.webhookdefinitions == null) | .package] | unique[]'
       ```

       **Example output**

       ```
       "3scale-operator"
       "amq-broker-rhel8"
       "amq-online"
       "amq-streams"
       "amq-streams-console"
       "ansible-automation-platform-operator"
       "ansible-cloud-addons-operator"
       "apicast-operator"
       "authorino-operator"
       "aws-load-balancer-operator"
       "bamoe-kogito-operator"
       "cephcsi-operator"
       "cincinnati-operator"
       "cluster-logging"
       "cluster-observability-operator"
       "compliance-operator"
       "container-security-operator"
       "cryostat-operator"
       "datagrid"
       "devspaces"
       ...
       ```
2. Inspect the contents of an extension’s metadata by running the following command:

   ```
   $ opm render <catalog_registry_url>:<tag> \
     | jq -s '.[] | select( .schema == "olm.package") \
     | select( .name == "<package_name>")'
   ```

   **Example command**

   ```
   $ opm render \
     registry.redhat.io/redhat/redhat-operator-index:v4.22 \
     | jq -s '.[] | select( .schema == "olm.package") \
     | select( .name == "openshift-pipelines-operator-rh")'
   ```

   **Example output**

   ```
   {
     "schema": "olm.package",
     "name": "openshift-pipelines-operator-rh",
     "defaultChannel": "latest",
     "icon": {
       "base64data": "iVBORw0KGgoAAAANSUhE...",
       "mediatype": "image/png"
     }
   }
   ```

##### [5.2.1.1. Common catalog queries](#olmv1-catalog-queries_managing-ce) Copy linkLink copied to clipboard!

You can query catalogs by using the `opm` and `jq` CLI tools to help you install, update, and manage the lifecycle of extensions.

The following examples show common catalog queries for extensions:

**Command syntax**

```
$ opm render <catalog_registry_url>:<tag> | <jq_request>
```

where:

`catalog_registry_url`
:   Specifies the URL of the catalog registry, such as `registry.redhat.io/redhat/redhat-operator-index`.

`tag`
:   Specifies the tag or version of the catalog, such as `v4.22` or `latest`.

`jq_request`
:   Specifies the query you want to run on the catalog.

**Example 5.1. Example command**

```
$ opm render \
  registry.redhat.io/redhat/redhat-operator-index:v4.22 \
  | jq -cs '[.[] | select(.schema == "olm.bundle" and (.properties[] \
  | select(.type == "olm.csv.metadata").value.installModes[] \
  | select(.type == "AllNamespaces" and .supported == true)) \
  and .spec.webhookdefinitions == null) \
  | .package] | unique[]'
```

Expand

Table 5.1. Common package queries

| Query | Request |
| --- | --- |
| Available packages in a catalog | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .schema == "olm.package")' ``` |
| Packages that support `AllNamespaces` install mode and do not use webhooks | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -cs '[.[] | select(.schema == "olm.bundle" and (.properties[] \   | select(.type == "olm.csv.metadata").value.installModes[] \   | select(.type == "AllNamespaces" and .supported == true)) \   and .spec.webhookdefinitions == null) \   | .package] | unique[]' ``` |
| Package metadata | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .schema == "olm.package") \   | select( .name == "<package_name>")' ``` |
| Catalog blobs in a package | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .package == "<package_name>")' ``` |

Show more

Expand

Table 5.2. Common channel queries

| Query | Request |
| --- | --- |
| Channels in a package | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .schema == "olm.channel" ) \   | select( .package == "<package_name>") | .name' ``` |
| Versions in a channel | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .package == "<package_name>" ) \   | select( .schema == "olm.channel" ) \   | select( .name == "<channel_name>" ) .entries \   | .[] | .name' ``` |
| * Latest version in a channel * Upgrade path | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .schema == "olm.channel" ) \   | select ( .name == "<channel_name>") \   | select( .package == "<package_name>")' ``` |

Show more

Expand

Table 5.3. Common bundle queries

| Query | Request |
| --- | --- |
| Bundles in a package | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .schema == "olm.bundle" ) \   | select( .package == "<package_name>") | .name' ``` |
| * Bundle dependencies * Available APIs | ``` $ opm render <catalog_registry_url>:<tag> \   | jq -s '.[] | select( .schema == "olm.bundle" ) \   | select ( .name == "<bundle_name>") \   | select( .package == "<package_name>")' ``` |

Show more

#### [5.2.2. Cluster extension permissions](#olmv1-cluster-extension-permissions_managing-ce) Copy linkLink copied to clipboard!

In Operator Lifecycle Manager (OLM) Classic, a single service account with cluster administrator privileges manages all cluster extensions.

OLM v1 is designed to be more secure than OLM (Classic) by default. OLM v1 manages a cluster extension by using the service account specified in an extension’s custom resource (CR). Cluster administrators can create a service account for each cluster extension. As a result, administrators can follow the principle of least privilege and assign only the role-based access controls (RBAC) to install and manage that extension.

You must add each permission to either a cluster role or role. Then you must bind the cluster role or role to the service account with a cluster role binding or role binding.

You can scope the RBAC to either the cluster or to a namespace. Use cluster roles and cluster role bindings to scope permissions to the cluster. Use roles and role bindings to scope permissions to a namespace. Whether you scope the permissions to the cluster or to a namespace depends on the design of the extension you want to install and manage.

Important

To simply the following procedure and improve readability, the following example manifest uses permissions that are scoped to the cluster. You can further restrict some of the permissions by scoping them to the namespace of the extension instead of the cluster.

If a new version of an installed extension requires additional permissions, OLM v1 halts the update process until a cluster administrator grants those permissions.

##### [5.2.2.1. Creating a namespace](#olmv1-creating-a-namespace_managing-ce) Copy linkLink copied to clipboard!

Before you create a service account to install and manage your cluster extension, you must create a namespace.

**Prerequisites**

* Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

**Procedure**

* Create a new namespace for the service account of the extension that you want to install by running the following command:

  ```
  $ oc adm new-project <new_namespace>
  ```

##### [5.2.2.2. Creating a service account for an extension](#olmv1-creating-a-service-account_managing-ce) Copy linkLink copied to clipboard!

You must create a service account to install, manage, and update a cluster extension.

**Prerequisites**

* Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

**Procedure**

1. Create a service account, similar to the following example:

   ```
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: <extension>-installer
     namespace: <namespace>
   ```

   **Example `extension-service-account.yaml` file**

   ```
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: pipelines-installer
     namespace: pipelines
   ```
2. Apply the service account by running the following command:

   ```
   $ oc apply -f extension-service-account.yaml
   ```

##### [5.2.2.3. Downloading the bundle manifests of an extension](#olmv1-downloading-bundle-manifests_managing-ce) Copy linkLink copied to clipboard!

Use the `opm` CLI tool to download the bundle manifests of the extension that you want to install. Use the CLI tool or text editor of your choice to view the manifests and find the required permissions to install and manage the extension.

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have decided which extension you want to install.
* You have installed the `opm` CLI tool.

**Procedure**

1. Inspect the available versions and images of the extension you want to install by running the following command:

   ```
   $ opm render <registry_url>:<tag_or_version> | \
     jq -cs '.[] | select( .schema == "olm.bundle" ) | \
     select( .package == "<extension_name>") | \
     {"name":.name, "image":.image}'
   ```

   **Example command**

   ```
   $ opm render registry.redhat.io/redhat/redhat-operator-index:v4.22 | \
     jq -cs '.[] | select( .schema == "olm.bundle" ) | \
     select( .package == "openshift-pipelines-operator-rh") | \
     {"name":.name, "image":.image}'
   ```

   **Example output**

   ```
   {"name":"openshift-pipelines-operator-rh.v1.14.3","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:3f64b29f6903981470d0917b2557f49d84067bccdba0544bfe874ec4412f45b0"}
   {"name":"openshift-pipelines-operator-rh.v1.14.4","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:dd3d18367da2be42539e5dde8e484dac3df33ba3ce1d5bcf896838954f3864ec"}
   {"name":"openshift-pipelines-operator-rh.v1.14.5","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:f7b19ce26be742c4aaa458d37bc5ad373b5b29b20aaa7d308349687d3cbd8838"}
   {"name":"openshift-pipelines-operator-rh.v1.15.0","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:22be152950501a933fe6e1df0e663c8056ca910a89dab3ea801c3bb2dc2bf1e6"}
   {"name":"openshift-pipelines-operator-rh.v1.15.1","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:64afb32e3640bb5968904b3d1a317e9dfb307970f6fda0243e2018417207fd75"}
   {"name":"openshift-pipelines-operator-rh.v1.15.2","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:8a593c1144709c9aeffbeb68d0b4b08368f528e7bb6f595884b2474bcfbcafcd"}
   {"name":"openshift-pipelines-operator-rh.v1.16.0","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:a46b7990c0ad07dae78f43334c9bd5e6cba7b50ca60d3f880099b71e77bed214"}
   {"name":"openshift-pipelines-operator-rh.v1.16.1","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:29f27245e93b3f605647993884751c490c4a44070d3857a878d2aee87d43f85b"}
   {"name":"openshift-pipelines-operator-rh.v1.16.2","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:2037004666526c90329f4791f14cb6cc06e8775cb84ba107a24cc4c2cf944649"}
   {"name":"openshift-pipelines-operator-rh.v1.17.0","image":"registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:d75065e999826d38408049aa1fde674cd1e45e384bfdc96523f6bad58a0e0dbc"}
   ```
2. Make a directory to extract the image of the bundle that you want to install by running the following command:

   ```
   $ mkdir <new_dir>
   ```
3. Change into the directory by running the following command:

   ```
   $ cd <new_dir>
   ```
4. Find the image reference of the version that you want to install and run the following command:

   ```
   $ oc image extract <full_path_to_registry_image>@sha256:<sha>
   ```

   **Example command**

   ```
   $ oc image extract registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:f7b19ce26be742c4aaa458d37bc5ad373b5b29b20aaa7d308349687d3cbd8838
   ```
5. Change into the `manifests` directory by running the following command:

   ```
   $ cd manifests
   ```
6. View the contents of the manifests directory by entering the following command. The output lists the manifests of the resources required to install, manage, and operate your extension.

   ```
   $ tree
   ```

   **Example output**

   ```
   .
   ├── manifests
   │   ├── config-logging_v1_configmap.yaml
   │   ├── openshift-pipelines-operator-monitor_monitoring.coreos.com_v1_servicemonitor.yaml
   │   ├── openshift-pipelines-operator-prometheus-k8s-read-binding_rbac.authorization.k8s.io_v1_rolebinding.yaml
   │   ├── openshift-pipelines-operator-read_rbac.authorization.k8s.io_v1_role.yaml
   │   ├── openshift-pipelines-operator-rh.clusterserviceversion.yaml
   │   ├── operator.tekton.dev_manualapprovalgates.yaml
   │   ├── operator.tekton.dev_openshiftpipelinesascodes.yaml
   │   ├── operator.tekton.dev_tektonaddons.yaml
   │   ├── operator.tekton.dev_tektonchains.yaml
   │   ├── operator.tekton.dev_tektonconfigs.yaml
   │   ├── operator.tekton.dev_tektonhubs.yaml
   │   ├── operator.tekton.dev_tektoninstallersets.yaml
   │   ├── operator.tekton.dev_tektonpipelines.yaml
   │   ├── operator.tekton.dev_tektonresults.yaml
   │   ├── operator.tekton.dev_tektontriggers.yaml
   │   ├── tekton-config-defaults_v1_configmap.yaml
   │   ├── tekton-config-observability_v1_configmap.yaml
   │   ├── tekton-config-read-rolebinding_rbac.authorization.k8s.io_v1_clusterrolebinding.yaml
   │   ├── tekton-config-read-role_rbac.authorization.k8s.io_v1_clusterrole.yaml
   │   ├── tekton-operator-controller-config-leader-election_v1_configmap.yaml
   │   ├── tekton-operator-info_rbac.authorization.k8s.io_v1_rolebinding.yaml
   │   ├── tekton-operator-info_rbac.authorization.k8s.io_v1_role.yaml
   │   ├── tekton-operator-info_v1_configmap.yaml
   │   ├── tekton-operator_v1_service.yaml
   │   ├── tekton-operator-webhook-certs_v1_secret.yaml
   │   ├── tekton-operator-webhook-config-leader-election_v1_configmap.yaml
   │   ├── tekton-operator-webhook_v1_service.yaml
   │   ├── tekton-result-read-rolebinding_rbac.authorization.k8s.io_v1_clusterrolebinding.yaml
   │   └── tekton-result-read-role_rbac.authorization.k8s.io_v1_clusterrole.yaml
   ├── metadata
   │   ├── annotations.yaml
   │   └── properties.yaml
   └── root
       └── buildinfo
           ├── content_manifests
           │   └── openshift-pipelines-operator-bundle-container-v1.16.2-3.json
           └── Dockerfile-openshift-pipelines-pipelines-operator-bundle-container-v1.16.2-3
   ```

**Next steps**

* View the contents of the `install.spec.clusterpermissions` stanza of cluster service version (CSV) file in the `manifests` directory using your preferred CLI tool or text editor. The following examples reference the `openshift-pipelines-operator-rh.clusterserviceversion.yaml` file of the Red Hat OpenShift Pipelines Operator.
* Keep this file open as a reference while assigning permissions to the cluster role file in the following procedure.

##### [5.2.2.4. Required permissions to install and manage a cluster extension](#olmv1-required-rbac-to-install-and-manage-extension-resources_managing-ce) Copy linkLink copied to clipboard!

To assign the necessary permissions for a cluster extension, inspect the manifests in its bundle image and grant the service account sufficient role-based access control (RBAC).

Important

Follow the principle of least privilege and scope permissions to specific resource names with the least RBAC required to run.

Grant the service account permissions to create and manage the following extension resources:

Admission plugins
:   Because OpenShift Container Platform clusters use the `OwnerReferencesPermissionEnforcement` admission plugin, cluster extensions must have permissions to update the `blockOwnerDeletion` and `ownerReferences` finalizers.

Cluster role and cluster role bindings for the controllers of the extension
:   You must define RBAC so that the installation service account can create and manage cluster roles and cluster role bindings for the extension controllers.

Cluster service version (CSV)
:   You must define RBAC for the resources defined in the CSV of the cluster extension.

Cluster-scoped bundle resources
:   You must define RBAC to create and manage any cluster-scoped resources included in the bundle. If the cluster-scoped resources matches another resource type, such as a `ClusterRole`, you can add the resource to the pre-existing rule under the `resources` or `resourceNames` field.

Custom resource definitions (CRDs)
:   You must define RBAC so that the installation service account can create and manage the CRDs for the extension. Also, you must grant the service account for the controller of the extension the RBAC to manage its CRDs.

Deployments
:   You must define RBAC for the installation service account to create and manage the deployments needed by the extension controller, such as services and config maps.

Extension permissions
:   You must include RBAC for the permissions and cluster permissions defined in the CSV. The installation service account needs the ability to grant these permissions to the extension controller, which needs these permissions to run.

Namespace-scoped bundle resources
:   You must define RBAC for any namespace-scoped bundle resources. The installation service account requires permission to create and manage resources, such as config maps or services.

Roles and role bindings
:   You must define RBAC for any roles or role bindings defined in the CSV. The installation service account needs permission to create and manage those roles and role bindings.

Service accounts
:   You must define RBAC so that the installation service account can create and manage the service accounts for the extension controllers.

##### [5.2.2.5. Creating a cluster role for an extension](#olmv1-creating-a-cluster-role_managing-ce) Copy linkLink copied to clipboard!

To set up access controls for an extension, review the `install.spec.clusterpermissions` section of the cluster service version (CSV) and the extension manifests. Then, create a cluster role by copying the required role-based access control (RBAC) rules from the CSV into a new manifest.

Tip

If you want to test the process for installing and updating an extension in OLM v1, you can use the following cluster role to grant cluster administrator permissions. This manifest is for testing purposes only. It should not be used in production clusters.

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: <extension>-installer-clusterrole
rules:
- apiGroups: ["*"]
  resources: ["*"]
  verbs: ["*"]
```

The following procedure uses the `openshift-pipelines-operator-rh.clusterserviceversion.yaml` file of the Red Hat OpenShift Pipelines Operator as an example. The examples include excerpts of the RBAC required to install and manage the OpenShift Pipelines Operator. For a complete manifest, see "Example cluster role for the Red Hat OpenShift Pipelines Operator".

Important

To simply the following procedure and improve readability, the following example manifest uses permissions that are scoped to the cluster. You can further restrict some of the permissions by scoping them to the namespace of the extension instead of the cluster.

**Prerequisites**

* Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have downloaded the manifests in the image reference of the extension that you want to install.

**Procedure**

1. Create a new cluster role manifest, similar to the following example:

   **Example `<extension>-cluster-role.yaml` file**

   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRole
   metadata:
     name: <extension>-installer-clusterrole
   ```
2. Edit your cluster role manifest to include permission to update finalizers on the extension, similar to the following example:

   **Example <extension>-cluster-role.yaml**

   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRole
   metadata:
     name: pipelines-installer-clusterrole
   rules:
   - apiGroups:
     - olm.operatorframework.io
     resources:
     - clusterextensions/finalizers
     verbs:
     - update
     # Scoped to the name of the ClusterExtension
     resourceNames:
     - <metadata_name>
   ```

   Replace `<metadata_name>` with the value of the metadata.name field from the custom resource (CR) of the extension.
3. Search for the `clusterrole` and `clusterrolebindings` values in the `rules.resources` field in the extension’s CSV file.

   * Copy the API groups, resources, verbs, and resource names to your manifest, similar to the following example:

     **Example cluster role manifest**

     ```
     apiVersion: rbac.authorization.k8s.io/v1
     kind: ClusterRole
     metadata:
       name: pipelines-installer-clusterrole
     rules:
     # ...
     # ClusterRoles and ClusterRoleBindings for the controllers of the extension
     - apiGroups:
       - rbac.authorization.k8s.io
       resources:
       - clusterroles
       verbs:
       - create
       - list
       - watch
     - apiGroups:
       - rbac.authorization.k8s.io
       resources:
       - clusterroles
       verbs:
       - get
       - update
       - patch
       - delete
       resourceNames:
       - "*"
     - apiGroups:
       - rbac.authorization.k8s.io
       resources:
       - clusterrolebindings
       verbs:
       - create
       - list
       - watch
     - apiGroups:
       - rbac.authorization.k8s.io
       resources:
       - clusterrolebindings
       verbs:
       - get
       - update
       - patch
       - delete
       resourceNames:
       - "*"
     # ...
     ```

     + You cannot scope the `create`, `list`, and `watch` verbs to specific resource names (the `resourceNames` field). You must scope these permissions to their resources (the `resources` field).
     + The resource names in the `resourceNames` field for the `get`, `update`, `patch`, and `delete` verbs are generated by using the following format: `<package_name>.<hash>`. After you install the extension, look up the resource names for the cluster roles and cluster role bindings for the controller of the extension. Replace the wildcard characters in this example with the generated names and follow the principle of least privilege.
4. Search for the `customresourcedefinitions` value in the `rules.resources` field in the extension’s CSV file.

   * Copy the API groups, resources, verbs, and resource names to your manifest, similar to the following example:

     ```
     apiVersion: rbac.authorization.k8s.io/v1
     kind: ClusterRole
     metadata:
       name: pipelines-installer-clusterrole
     rules:
     # ...
     # Custom resource definitions of the extension
     - apiGroups:
       - apiextensions.k8s.io
       resources:
       - customresourcedefinitions
       verbs:
       - create
       - list
       - watch
     - apiGroups:
       - apiextensions.k8s.io
       resources:
       - customresourcedefinitions
       verbs:
       - get
       - update
       - patch
       - delete
       resourceNames:
       - manualapprovalgates.operator.tekton.dev
       - openshiftpipelinesascodes.operator.tekton.dev
       - tektonaddons.operator.tekton.dev
       - tektonchains.operator.tekton.dev
       - tektonconfigs.operator.tekton.dev
       - tektonhubs.operator.tekton.dev
       - tektoninstallersets.operator.tekton.dev
       - tektonpipelines.operator.tekton.dev
       - tektonresults.operator.tekton.dev
       - tektontriggers.operator.tekton.dev
     # ...
     ```
5. Search the CSV file for stanzas with the `permissions` and `clusterPermissions` values in the `rules.resources` spec.

   * Copy the API groups, resources, verbs, and resource names to your manifest, similar to the following example:

     ```
     apiVersion: rbac.authorization.k8s.io/v1
     kind: ClusterRole
     metadata:
       name: pipelines-installer-clusterrole
     rules:
     # ...
     # Excerpt from install.spec.clusterPermissions
     - apiGroups:
       - ''
       resources:
       - nodes
       - pods
       - services
       - endpoints
       - persistentvolumeclaims
       - events
       - configmaps
       - secrets
       - pods/log
       - limitranges
       verbs:
       - create
       - list
       - watch
       - delete
       - deletecollection
       - patch
       - get
       - update
     - apiGroups:
       - extensions
       - apps
       resources:
       - ingresses
       - ingresses/status
       verbs:
       - create
       - list
       - watch
       - delete
       - patch
       - get
       - update
      # ...
     ```
6. Search the CSV file for resources under the `install.spec.deployments` stanza.

   * Copy the API groups, resources, verbs, and resource names to your manifest, similar to the following example:

     ```
     apiVersion: rbac.authorization.k8s.io/v1
     kind: ClusterRole
     metadata:
       name: pipelines-installer-clusterrole
     rules:
     # ...
     # Excerpt from install.spec.deployments
     - apiGroups:
       - apps
       resources:
       - deployments
       verbs:
       - create
       - list
       - watch
     - apiGroups:
       - apps
       resources:
       - deployments
       verbs:
       - get
       - update
       - patch
       - delete
       # scoped to the extension controller deployment name
       resourceNames:
       - openshift-pipelines-operator
       - tekton-operator-webhook
     # ...
     ```
7. Search for the `services` and `configmaps` values in the `rules.resources` field in the extension’s CSV file.

   * Copy the API groups, resources, verbs, and resource names to your manifest, similar to the following example:

     ```
     apiVersion: rbac.authorization.k8s.io/v1
     kind: ClusterRole
     metadata:
       name: pipelines-installer-clusterrole
     rules:
     # ...
     # Services
     - apiGroups:
       - ""
       resources:
       - services
       verbs:
       - create
     - apiGroups:
       - ""
       resources:
       - services
       verbs:
       - get
       - list
       - watch
       - update
       - patch
       - delete
       # scoped to the service name
       resourceNames:
       - openshift-pipelines-operator-monitor
       - tekton-operator
       - tekton-operator-webhook
     # configmaps
     - apiGroups:
       - ""
       resources:
       - configmaps
       verbs:
       - create
     - apiGroups:
       - ""
       resources:
       - configmaps
       verbs:
       - get
       - list
       - watch
       - update
       - patch
       - delete
       # scoped to the configmap name
       resourceNames:
       - config-logging
       - tekton-config-defaults
       - tekton-config-observability
       - tekton-operator-controller-config-leader-election
       - tekton-operator-info
       - tekton-operator-webhook-config-leader-election
     - apiGroups:
       - operator.tekton.dev
       resources:
       - tekton-config-read-role
       - tekton-result-read-role
       verbs:
       - get
       - watch
       - list
     ```
8. Add the cluster role manifest to the cluster by running the following command:

   ```
   $ oc apply -f <extension>-installer-clusterrole.yaml
   ```

   **Example command**

   ```
   $ oc apply -f pipelines-installer-clusterrole.yaml
   ```

##### [5.2.2.6. Example cluster role for the Red Hat OpenShift Pipelines Operator](#olmv1-example-cluster-role-pipelines_managing-ce) Copy linkLink copied to clipboard!

Review the complete cluster role manifest for the OpenShift Pipelines Operator, including all of the RBAC required to install and manage the extension.

```
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pipelines-installer-clusterrole
rules:
- apiGroups:
  - olm.operatorframework.io
  resources:
  - clusterextensions/finalizers
  verbs:
  - update
  # Scoped to the name of the ClusterExtension
  resourceNames:
  - pipes # the value from <metadata.name> from the extension's custom resource (CR)
# ClusterRoles and ClusterRoleBindings for the controllers of the extension
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - clusterroles
  verbs:
  - create
  - list
  - watch
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - clusterroles
  verbs:
  - get
  - update
  - patch
  - delete
  resourceNames:
  - "*"
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - clusterrolebindings
  verbs:
  - create
  - list
  - watch
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - clusterrolebindings
  verbs:
  - get
  - update
  - patch
  - delete
  resourceNames:
  - "*"
# Extension's custom resource definitions
- apiGroups:
  - apiextensions.k8s.io
  resources:
  - customresourcedefinitions
  verbs:
  - create
  - list
  - watch
- apiGroups:
  - apiextensions.k8s.io
  resources:
  - customresourcedefinitions
  verbs:
  - get
  - update
  - patch
  - delete
  resourceNames:
  - manualapprovalgates.operator.tekton.dev
  - openshiftpipelinesascodes.operator.tekton.dev
  - tektonaddons.operator.tekton.dev
  - tektonchains.operator.tekton.dev
  - tektonconfigs.operator.tekton.dev
  - tektonhubs.operator.tekton.dev
  - tektoninstallersets.operator.tekton.dev
  - tektonpipelines.operator.tekton.dev
  - tektonresults.operator.tekton.dev
  - tektontriggers.operator.tekton.dev
- apiGroups:
  - ''
  resources:
  - nodes
  - pods
  - services
  - endpoints
  - persistentvolumeclaims
  - events
  - configmaps
  - secrets
  - pods/log
  - limitranges
  verbs:
  - create
  - list
  - watch
  - delete
  - deletecollection
  - patch
  - get
  - update
- apiGroups:
  - extensions
  - apps
  resources:
  - ingresses
  - ingresses/status
  verbs:
  - create
  - list
  - watch
  - delete
  - patch
  - get
  - update
- apiGroups:
  - ''
  resources:
  - namespaces
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
- apiGroups:
  - apps
  resources:
  - deployments
  - daemonsets
  - replicasets
  - statefulsets
  - deployments/finalizers
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - monitoring.coreos.com
  resources:
  - servicemonitors
  verbs:
  - get
  - create
  - delete
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - clusterroles
  - roles
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
  - bind
  - escalate
- apiGroups:
  - ''
  resources:
  - serviceaccounts
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
  - impersonate
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - clusterrolebindings
  - rolebindings
  verbs:
  - get
  - update
  - delete
  - patch
  - create
  - list
  - watch
- apiGroups:
  - apiextensions.k8s.io
  resources:
  - customresourcedefinitions
  - customresourcedefinitions/status
  verbs:
  - get
  - create
  - update
  - delete
  - list
  - patch
  - watch
- apiGroups:
  - admissionregistration.k8s.io
  resources:
  - mutatingwebhookconfigurations
  - validatingwebhookconfigurations
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
- apiGroups:
  - build.knative.dev
  resources:
  - builds
  - buildtemplates
  - clusterbuildtemplates
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
- apiGroups:
  - extensions
  resources:
  - deployments
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
- apiGroups:
  - extensions
  resources:
  - deployments/finalizers
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
- apiGroups:
  - operator.tekton.dev
  resources:
  - '*'
  - tektonaddons
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - tekton.dev
  - triggers.tekton.dev
  - operator.tekton.dev
  - pipelinesascode.tekton.dev
  resources:
  - '*'
  verbs:
  - add
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - dashboard.tekton.dev
  resources:
  - '*'
  - tektonaddons
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - security.openshift.io
  resources:
  - securitycontextconstraints
  verbs:
  - use
  - get
  - list
  - create
  - update
  - delete
- apiGroups:
  - events.k8s.io
  resources:
  - events
  verbs:
  - create
- apiGroups:
  - route.openshift.io
  resources:
  - routes
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - coordination.k8s.io
  resources:
  - leases
  verbs:
  - get
  - list
  - create
  - update
  - delete
  - patch
  - watch
- apiGroups:
  - console.openshift.io
  resources:
  - consoleyamlsamples
  - consoleclidownloads
  - consolequickstarts
  - consolelinks
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - autoscaling
  resources:
  - horizontalpodautoscalers
  verbs:
  - delete
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - policy
  resources:
  - poddisruptionbudgets
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - monitoring.coreos.com
  resources:
  - servicemonitors
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - batch
  resources:
  - jobs
  - cronjobs
  verbs:
  - delete
  - deletecollection
  - create
  - patch
  - get
  - list
  - update
  - watch
- apiGroups:
  - ''
  resources:
  - namespaces/finalizers
  verbs:
  - update
- apiGroups:
  - resolution.tekton.dev
  resources:
  - resolutionrequests
  - resolutionrequests/status
  verbs:
  - get
  - list
  - watch
  - create
  - delete
  - update
  - patch
- apiGroups:
  - console.openshift.io
  resources:
  - consoleplugins
  verbs:
  - get
  - list
  - watch
  - create
  - delete
  - update
  - patch
# Deployments specified in install.spec.deployments
- apiGroups:
  - apps
  resources:
  - deployments
  verbs:
  - create
  - list
  - watch
- apiGroups:
  - apps
  resources:
  - deployments
  verbs:
  - get
  - update
  - patch
  - delete
  # scoped to the extension controller deployment name
  resourceNames:
  - openshift-pipelines-operator
  - tekton-operator-webhook
# Service accounts in the CSV
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - create
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - get
  - update
  - patch
  - delete
  # scoped to the extension controller's deployment service account
  resourceNames:
  - openshift-pipelines-operator
# Services
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - get
  - list
  - watch
  - update
  - patch
  - delete
  # scoped to the service name
  resourceNames:
  - openshift-pipelines-operator-monitor
  - tekton-operator
  - tekton-operator-webhook
# configmaps
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - get
  - list
  - watch
  - update
  - patch
  - delete
  # scoped to the configmap name
  resourceNames:
  - config-logging
  - tekton-config-defaults
  - tekton-config-observability
  - tekton-operator-controller-config-leader-election
  - tekton-operator-info
  - tekton-operator-webhook-config-leader-election
- apiGroups:
  - operator.tekton.dev
  resources:
  - tekton-config-read-role
  - tekton-result-read-role
  verbs:
  - get
  - watch
  - list
---
```

##### [5.2.2.7. Creating a cluster role binding for an extension](#olmv1-creating-a-cluster-rol-binding_managing-ce) Copy linkLink copied to clipboard!

After you have created a service account and cluster role, you must bind the cluster role to the service account with a cluster role binding manifest.

**Prerequisites**

* Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have created and applied the following resources for the extension you want to install:

  + Namespace
  + Service account
  + Cluster role

**Procedure**

1. Create a cluster role binding to bind the cluster role to the service account, similar to the following example:

   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRoleBinding
   metadata:
     name: <extension>-installer-binding
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: <extension>-installer-clusterrole
   subjects:
   - kind: ServiceAccount
     name: <extension>-installer
     namespace: <namespace>
   ```

   **Example `pipelines-cluster-role-binding.yaml` file**

   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRoleBinding
   metadata:
     name: pipelines-installer-binding
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: pipelines-installer-clusterrole
   subjects:
   - kind: ServiceAccount
     name: pipelines-installer
     namespace: pipelines
   ```
2. Apply the cluster role binding by running the following command:

   ```
   $ oc apply -f pipelines-cluster-role-binding.yaml
   ```

#### [5.2.3. Installing a cluster extension in all namespaces](#olmv1-installing-an-operator_managing-ce) Copy linkLink copied to clipboard!

You can install an extension from a catalog by creating a custom resource (CR) and applying it to the cluster. Operator Lifecycle Manager (OLM) v1 supports installing cluster extensions, including OLM (Classic) Operators in the `registry+v1` bundle format, that are scoped to the cluster.

Note

For OpenShift Container Platform 4.22, documented procedures for OLM v1 are CLI-based only. Alternatively, administrators can create and view related objects in the web console by using normal methods, such as the **Import YAML** and **Search** pages. However, the existing **Software Catalog** and **Installed Operators** pages do not yet display OLM v1 components.

**Prerequisites**

* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension that you want to install. For more information, see "Cluster extension permissions".

**Procedure**

1. Create a CR, similar to the following example:

   ```
   apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: <clusterextension_name>
     spec:
       namespace: <installed_namespace>
       serviceAccount:
         name: <service_account_installer_name>
       source:
         sourceType: Catalog
         catalog:
           packageName: <package_name>
           channels:
             - <channel_name>
           version: <version_or_version_range>
           upgradeConstraintPolicy: CatalogProvided
   ```

   where:

   `spec.namespace`
   :   Specifies the namespace where you want the bundle installed, such as `pipelines` or `my-extension`. Extensions are still cluster-scoped and might contain resources that are installed in different namespaces.

   `spec.serviceAccount.name`
   :   Specifies the name of the service account you created to install, update, and manage your extension.

   `spec.source.catalog.channels`
   :   Specifies channel names as an array, such as `pipelines-1.14` or `latest`. This field is optional.

   `spec.source.catalog.version`
   :   Specifies the version or version range, such as `1.14.0`, `1.14.x`, or `>=1.16`, of the package you want to install or update. This field is optional.

   `spec.source.catalog.upgradeConstraintPolicy`
   :   Specifies the upgrade constraint policy. If unspecified, the default setting is `CatalogProvided`. The `CatalogProvided` setting only updates if the new version satisfies the upgrade constraints set by the package author. To force an update or rollback, set the field to `SelfCertified`. This field is optional.

       **Example `pipelines-operator.yaml` CR**

       ```
       apiVersion: olm.operatorframework.io/v1
       kind: ClusterExtension
       metadata:
         name: pipelines-operator
       spec:
         namespace: pipelines
         serviceAccount:
           name: pipelines-installer
         source:
           sourceType: Catalog
           catalog:
             packageName: openshift-pipelines-operator-rh
             version: "1.14.x"
       ```
2. Apply the CR to the cluster by running the following command:

   ```
   $ oc apply -f pipeline-operator.yaml
   ```

   **Example output**

   ```
   clusterextension.olm.operatorframework.io/pipelines-operator created
   ```

**Verification**

1. View the Operator or extension’s CR in the YAML format by running the following command:

   ```
   $ oc get clusterextension pipelines-operator -o yaml
   ```

   **Example output**

   ```
   apiVersion: v1
   items:
   - apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       annotations:
         kubectl.kubernetes.io/last-applied-configuration: |
           {"apiVersion":"olm.operatorframework.io/v1","kind":"ClusterExtension","metadata":{"annotations":{},"name":"pipes"},"spec":{"namespace":"pipelines","serviceAccount":{"name":"pipelines-installer"},"source":{"catalog":{"packageName":"openshift-pipelines-operator-rh","version":"1.14.x"},"sourceType":"Catalog"}}}
       creationTimestamp: "2025-02-18T21:48:13Z"
       finalizers:
       - olm.operatorframework.io/cleanup-unpack-cache
       - olm.operatorframework.io/cleanup-contentmanager-cache
       generation: 1
       name: pipelines-operator
       resourceVersion: "72725"
       uid: e18b13fb-a96d-436f-be75-a9a0f2b07993
     spec:
       namespace: pipelines
       serviceAccount:
         name: pipelines-installer
       source:
         catalog:
           packageName: openshift-pipelines-operator-rh
           upgradeConstraintPolicy: CatalogProvided
           version: 1.14.x
         sourceType: Catalog
     status:
       conditions:
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: Deprecated
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: PackageDeprecated
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: ChannelDeprecated
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: BundleDeprecated
       - lastTransitionTime: "2025-02-18T21:48:16Z"
         message: Installed bundle registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:f7b19ce26be742c4aaa458d37bc5ad373b5b29b20aaa7d308349687d3cbd8838
           successfully
         observedGeneration: 1
         reason: Succeeded
         status: "True"
         type: Installed
       - lastTransitionTime: "2025-02-18T21:48:16Z"
         message: desired state reached
         observedGeneration: 1
         reason: Succeeded
         status: "True"
         type: Progressing
       install:
         bundle:
           name: openshift-pipelines-operator-rh.v1.14.5
           version: 1.14.5
   kind: List
   metadata:
     resourceVersion: ""
   ```

   where:

   `spec.channel`
   :   Displays the channel defined in the CR of the extension.

   `spec.version`
   :   Displays the version or version range defined in the CR of the extension.

   `status.conditions`
   :   Displays information about the status and health of the extension.

   `type: Deprecated`
   :   Displays whether one or more of following are deprecated:

       `type: PackageDeprecated`
       :   Displays whether the resolved package is deprecated.

       `type: ChannelDeprecated`
       :   Displays whether the resolved channel is deprecated.

       `type: BundleDeprecated`
       :   Displays whether the resolved bundle is deprecated.

       The value of `False` in the `status` field indicates that the `reason: Deprecated` condition is not deprecated. The value of `True` in the `status` field indicates that the `reason: Deprecated` condition is deprecated.

   `installedBundle.name`
   :   Displays the name of the bundle installed.

   `installedBundle.version`
   :   Displays the version of the bundle installed.

#### [5.2.4. Configuring a watch namespace for a cluster extension (Technology Preview)](#olmv1-deploying-a-ce-in-a-specific-namespace_managing-ce) Copy linkLink copied to clipboard!

You can configure the watch namespace for extensions that support namespace-scoped resource watching.

Important

Configuring watch namespace for a cluster extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have enabled the `TechPreviewNoUpgrade` feature set on the cluster.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension. For more information, see "Cluster extension permissions".
* You have verified the supported install modes for the extension and determined the required `watchNamespace` configuration.

**Procedure**

1. Create a custom resource (CR) based on where you want the extension to watch for resources:

   * To configure the extension to watch its own installation namespace:

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: <extension_name>
     spec:
       namespace: <installation_namespace>
       config:
         configType: Inline
         inline:
           watchNamespace: <installation_namespace>
       serviceAccount:
         name: <service_account>
       source:
         sourceType: Catalog
         catalog:
           packageName: <package_name>
           version: <version>
           upgradeConstraintPolicy: CatalogProvided
     ```

     where:

     `config.inline.watchNamespace`
     :   Specifies the namespace to watch for resources. For requirements and valid values, see "Extension configuration".
   * To configure the extension to watch a different namespace:

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: <extension_name>
     spec:
       namespace: <installation_namespace>
       config:
         configType: Inline
         inline:
           watchNamespace: <watched_namespace>
       serviceAccount:
         name: <service_account>
       source:
         sourceType: Catalog
         catalog:
           packageName: <package_name>
           version: <version>
           upgradeConstraintPolicy: CatalogProvided
     ```
2. Apply the CR to the cluster by running the following command:

   ```
   $ oc apply -f <cluster_extension_cr>.yaml
   ```

**Verification**

* Verify that the extension installed successfully by running the following command:

  ```
  $ oc get clusterextension <extension_name> -o yaml
  ```

  **Example output**

  ```
  apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <extension_name>
  spec:
    namespace: <installation_namespace>
    config:
      configType: Inline
      inline:
        watchNamespace: <installation_namespace>
  status:
    conditions:
    - type: Installed
      status: "True"
      reason: Succeeded
  ```

#### [5.2.5. Preflight permissions check for cluster extensions (Technology Preview)](#olmv1-troubleshooting-rbac-errors-with-preflight-check_managing-ce) Copy linkLink copied to clipboard!

Before installing an extension, the Operator Controller performs a dry run to verify service account access. This process confirms that the service account can create all required Kubernetes resources and RBAC rules defined by the extension bundle.

Important

The preflight permissions check for cluster extensions is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

If the service account is missing any required RBAC rules, the preflight check fails before the actual installation proceeds. If the preflight check fails, the Operator Controller reports the errors in the status conditions of the extension and in the logs of the Operator Controller.

To proceed with the installation, update the roles and bindings to grant the missing permissions to the service account and apply the changes. If there are no errors, the Operator Controller reconciles the updated permissions and completes the installation.

##### [5.2.5.1. Example report from the preflight permissions check](#olmv1-preflight-permissions-check-output_managing-ce) Copy linkLink copied to clipboard!

The following report indicates that the service account requires the following missing permissions:

* RBAC rules to perform `list` and `watch` actions for the `services` resource in the core API group for the entire cluster
* RBAC rules to perform `create` actions for `deployments` resources in the `apps` API group for the `pipelines` namespace

You can access the reports from the preflight permissions check in the status conditions of the cluster extension. The `oc describe clusterextension` command prints information about a cluster extension, including the status conditions.

**Example command**

```
$ oc describe clusterextension <extension_name>
```

**Example report**

```
apiVersion: v1
items:
- apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
...
Conditions:
  Type:    Progressing
  Status:  False
  Reason:  Retrying
  Message: pre-authorization failed: service account requires the following permissions to manage cluster extension:
           Namespace:"" APIGroups:[] Resources:[services] Verbs:[list,watch]
           Namespace:"pipelines" APIGroups:["apps"] Resources:[deployments] Verbs:[create]
```

`Namespace`
:   Specifies the scope of the required RBAC rules at the namespace level, for example the `pipelines` namespace. An empty namespace value, `""`, indicates that you must scope the permission to the cluster.

`APIGroups`
:   Specifies the name of the API group the required permissions apply to. An empty value in the API group, `[]`, indicates the permissions apply to the core API group. For example, services, secrets, and config maps are all core resources.

    If a resource belongs to a named API group, the report lists the name in between the brackets. For example, the value of `APIGroups:[apps]` indicates the extension requires RBAC rules to act on resources in the `apps` API group.

`Resources`
:   Specifies the resource types that require permissions. For example, services, secrets, and custom resource definitions are common resource types.

`Verbs`
:   Specifies the actions, or *verbs*, that the service account needs permission to perform. If the report lists several verbs, all of the listed verbs require RBAC rules.

##### [5.2.5.2. Common permission errors](#olmv1-common-rbac-errors_managing-ce) Copy linkLink copied to clipboard!

Missing verbs
:   The service account does not have permission to perform a required action. To resolve this issue, update or create a role and binding to grant the necessary permissions. Roles and role bindings define resource permissions for a namespace. Cluster roles and cluster role bindings define resource permissions for the cluster.

Privilege escalation
:   The service account does not have enough permission to create a role or cluster role that the extension needs. When this happens, the preflight check reports the verbs as missing to prevent privilege escalation. To resolve this issue, grant enough permission to the service account so that it can create the roles.

Missing role references
:   The extension references a role or cluster role that the Operator Controller cannot find. When this happens, the preflight check lists the missing role and reports an `authorization evalutation error`. To resolve the issue, create or update the roles and cluster roles to ensure that all role references exist.

#### [5.2.6. Updating a cluster extension](#olmv1-updating-an-operator_managing-ce) Copy linkLink copied to clipboard!

You can update your cluster extension or Operator by manually editing the custom resource (CR) and applying the changes.

**Prerequisites**

* You have an Operator or extension installed.
* You have installed the `jq` CLI tool.
* You have installed the `opm` CLI tool.

**Procedure**

1. Inspect a package for channel and version information from a local copy of your catalog file by completing the following steps:

   1. Get a list of channels from a selected package by running the following command:

      ```
      $ opm render <catalog_registry_url>:<tag> \
        | jq -s '.[] | select( .schema == "olm.channel" ) \
        | select( .package == "openshift-pipelines-operator-rh") | .name'
      ```

      **Example command**

      ```
      $ opm render registry.redhat.io/redhat/redhat-operator-index:v4.22 \
        | jq -s '.[] | select( .schema == "olm.channel" ) \
        | select( .package == "openshift-pipelines-operator-rh") | .name'
      ```

      **Example output**

      ```
      "latest"
      "pipelines-1.14"
      "pipelines-1.15"
      "pipelines-1.16"
      "pipelines-1.17"
      ```
   2. Get a list of the versions published in a channel by running the following command:

      ```
      $ opm render <catalog_registry_url>:<tag> \
        | jq -s '.[] | select( .package == "<package_name>" ) \
        | select( .schema == "olm.channel" ) \
        | select( .name == "<channel_name>" ) | .entries \
        | .[] | .name'
      ```

      **Example command**

      ```
      $ opm render registry.redhat.io/redhat/redhat-operator-index:v4.22 \
        | jq -s '.[] | select( .package == "openshift-pipelines-operator-rh" ) \
        | select( .schema == "olm.channel" ) | select( .name == "latest" ) \
        | .entries | .[] | .name'
      ```

      **Example output**

      ```
      "openshift-pipelines-operator-rh.v1.15.0"
      "openshift-pipelines-operator-rh.v1.16.0"
      "openshift-pipelines-operator-rh.v1.17.0"
      "openshift-pipelines-operator-rh.v1.17.1"
      ```
2. Find out what version or channel is specified in your Operator or extension’s CR by running the following command:

   ```
   $ oc get clusterextension <operator_name> -o yaml
   ```

   **Example command**

   ```
   $ oc get clusterextension pipelines-operator -o yaml
   ```

   **Example output**

   ```
   apiVersion: v1
   items:
   - apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       annotations:
         kubectl.kubernetes.io/last-applied-configuration: |
           {"apiVersion":"olm.operatorframework.io/v1","kind":"ClusterExtension","metadata":{"annotations":{},"name":"pipes"},"spec":{"namespace":"pipelines","serviceAccount":{"name":"pipelines-installer"},"source":{"catalog":{"packageName":"openshift-pipelines-operator-rh","version":"1.14.x"},"sourceType":"Catalog"}}}
       creationTimestamp: "2025-02-18T21:48:13Z"
       finalizers:
       - olm.operatorframework.io/cleanup-unpack-cache
       - olm.operatorframework.io/cleanup-contentmanager-cache
       generation: 1
       name: pipelines-operator
       resourceVersion: "72725"
       uid: e18b13fb-a96d-436f-be75-a9a0f2b07993
     spec:
       namespace: pipelines
       serviceAccount:
         name: pipelines-installer
       source:
         catalog:
           packageName: openshift-pipelines-operator-rh
           upgradeConstraintPolicy: CatalogProvided
           version: 1.14.x
         sourceType: Catalog
     status:
       conditions:
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: Deprecated
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: PackageDeprecated
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: ChannelDeprecated
       - lastTransitionTime: "2025-02-18T21:48:13Z"
         message: ""
         observedGeneration: 1
         reason: Deprecated
         status: "False"
         type: BundleDeprecated
       - lastTransitionTime: "2025-02-18T21:48:16Z"
         message: Installed bundle registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:f7b19ce26be742c4aaa458d37bc5ad373b5b29b20aaa7d308349687d3cbd8838
           successfully
         observedGeneration: 1
         reason: Succeeded
         status: "True"
         type: Installed
       - lastTransitionTime: "2025-02-18T21:48:16Z"
         message: desired state reached
         observedGeneration: 1
         reason: Succeeded
         status: "True"
         type: Progressing
       install:
         bundle:
           name: openshift-pipelines-operator-rh.v1.14.5
           version: 1.14.5
   kind: List
   metadata:
     resourceVersion: ""
   ```
3. Edit your CR by using one of the following methods:

   * If you want to pin your Operator or extension to specific version, such as `1.15.0`, edit your CR similar to the following example:

     **Example `pipelines-operator.yaml` CR**

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: pipelines-operator
     spec:
       namespace: pipelines
       serviceAccount:
         name: pipelines-installer
       source:
         sourceType: Catalog
         catalog:
           packageName: openshift-pipelines-operator-rh
           version: "1.15.0"
     ```

     This example updates the version from `1.14.x` to `1.15.0`.
   * If you want to define a range of acceptable update versions, edit your CR similar to the following example:

     **Example CR with a version range specified**

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: pipelines-operator
     spec:
       namespace: pipelines
       serviceAccount:
         name: pipelines-installer
       source:
         sourceType: Catalog
         catalog:
           packageName: openshift-pipelines-operator-rh
           version: ">1.15, <1.17"
     ```

     The `spec.source.catalog.version` value specifies that the desired version range is greater than version `1.15` and less than `1.17`.
   * If you want to update to the latest version that can be resolved from a channel, edit your CR similar to the following example:

     **Example CR with a specified channel**

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: pipelines-operator
     spec:
       namespace: pipelines
       serviceAccount:
         name: pipelines-installer
       source:
         sourceType: Catalog
         catalog:
           packageName: openshift-pipelines-operator-rh
           channels:
             - latest
     ```

     The `spec.source.catalog.channels` value installs the latest release that can be resolved from the specified channel. Updates to the channel are automatically installed. Enter values as an array.
   * If you want to specify a channel and version or version range, edit your CR similar to the following example:

     **Example CR with a specified channel and version range**

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: pipelines-operator
     spec:
       namespace: pipelines
       serviceAccount:
         name: pipelines-installer
       source:
         sourceType: Catalog
         catalog:
           packageName: openshift-pipelines-operator-rh
           channels:
             - latest
           version: "<1.16"
     ```

     For more information, see "Example custom resources (CRs) that specify a target version".
4. Apply the update to the cluster by running the following command:

   ```
   $ oc apply -f pipelines-operator.yaml
   ```

   **Example output**

   ```
   clusterextension.olm.operatorframework.io/pipelines-operator configured
   ```

**Verification**

* Verify that the channel and version updates have been applied by running the following command:

  ```
  $ oc get clusterextension pipelines-operator -o yaml
  ```

  **Example output**

  ```
  apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"olm.operatorframework.io/v1","kind":"ClusterExtension","metadata":{"annotations":{},"name":"pipes"},"spec":{"namespace":"pipelines","serviceAccount":{"name":"pipelines-installer"},"source":{"catalog":{"packageName":"openshift-pipelines-operator-rh","version":"\u003c1.16"},"sourceType":"Catalog"}}}
    creationTimestamp: "2025-02-18T21:48:13Z"
    finalizers:
    - olm.operatorframework.io/cleanup-unpack-cache
    - olm.operatorframework.io/cleanup-contentmanager-cache
    generation: 2
    name: pipes
    resourceVersion: "90693"
    uid: e18b13fb-a96d-436f-be75-a9a0f2b07993
  spec:
    namespace: pipelines
    serviceAccount:
      name: pipelines-installer
    source:
      catalog:
        packageName: openshift-pipelines-operator-rh
        upgradeConstraintPolicy: CatalogProvided
        version: <1.16
      sourceType: Catalog
  status:
    conditions:
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: Deprecated
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: PackageDeprecated
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: ChannelDeprecated
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: BundleDeprecated
    - lastTransitionTime: "2025-02-18T21:48:16Z"
      message: Installed bundle registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:8a593c1144709c9aeffbeb68d0b4b08368f528e7bb6f595884b2474bcfbcafcd
        successfully
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: Installed
    - lastTransitionTime: "2025-02-18T21:48:16Z"
      message: desired state reached
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: Progressing
    install:
      bundle:
        name: openshift-pipelines-operator-rh.v1.15.2
        version: 1.15.2
  ```

**Troubleshooting**

* If you specify a target version or channel that is deprecated or does not exist, you can run the following command to check the status of your extension:

  ```
  $ oc get clusterextension <operator_name> -o yaml
  ```

  **Example output for a version that does not exist**

  ```
  apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"olm.operatorframework.io/v1","kind":"ClusterExtension","metadata":{"annotations":{},"name":"pipes"},"spec":{"namespace":"pipelines","serviceAccount":{"name":"pipelines-installer"},"source":{"catalog":{"packageName":"openshift-pipelines-operator-rh","version":"9.x"},"sourceType":"Catalog"}}}
    creationTimestamp: "2025-02-18T21:48:13Z"
    finalizers:
    - olm.operatorframework.io/cleanup-unpack-cache
    - olm.operatorframework.io/cleanup-contentmanager-cache
    generation: 3
    name: pipes
    resourceVersion: "93334"
    uid: e18b13fb-a96d-436f-be75-a9a0f2b07993
  spec:
    namespace: pipelines
    serviceAccount:
      name: pipelines-installer
    source:
      catalog:
        packageName: openshift-pipelines-operator-rh
        upgradeConstraintPolicy: CatalogProvided
        version: 9.x
      sourceType: Catalog
  status:
    conditions:
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: Deprecated
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: PackageDeprecated
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: ChannelDeprecated
    - lastTransitionTime: "2025-02-18T21:48:13Z"
      message: ""
      observedGeneration: 2
      reason: Deprecated
      status: "False"
      type: BundleDeprecated
    - lastTransitionTime: "2025-02-18T21:48:16Z"
      message: Installed bundle registry.redhat.io/openshift-pipelines/pipelines-operator-bundle@sha256:8a593c1144709c9aeffbeb68d0b4b08368f528e7bb6f595884b2474bcfbcafcd
        successfully
      observedGeneration: 3
      reason: Succeeded
      status: "True"
      type: Installed
    - lastTransitionTime: "2025-02-18T21:48:16Z"
      message: 'error upgrading from currently installed version "1.15.2": no bundles
        found for package "openshift-pipelines-operator-rh" matching version "9.x"'
      observedGeneration: 3
      reason: Retrying
      status: "True"
      type: Progressing
    install:
      bundle:
        name: openshift-pipelines-operator-rh.v1.15.2
        version: 1.15.2
  ```

#### [5.2.7. Deleting an Operator](#olmv1-deleting-an-operator_managing-ce) Copy linkLink copied to clipboard!

You can delete an Operator and its custom resource definitions (CRDs) by deleting the `ClusterExtension` custom resource (CR).

**Prerequisites**

* You have a catalog installed.
* You have an Operator installed.

**Procedure**

* Delete an Operator and its CRDs by running the following command:

  ```
  $ oc delete clusterextension <operator_name>
  ```

  **Example output**

  ```
  clusterextension.olm.operatorframework.io "<operator_name>" deleted
  ```

**Verification**

* Run the following commands to verify that your Operator and its resources were deleted:

  + Verify the Operator is deleted by running the following command:

    ```
    $ oc get clusterextensions
    ```

    **Example output**

    ```
    No resources found
    ```
  + Verify that the Operator’s system namespace is deleted by running the following command:

    ```
    $ oc get ns <operator_name>-system
    ```

    **Example output**

    ```
    Error from server (NotFound): namespaces "<operator_name>-system" not found
    ```

### [5.3. Configuring cluster extensions](#olmv1-configuring-extensions) Copy linkLink copied to clipboard!

You can customize Operator installations to control namespace scope and manage deployment behavior including resource allocation, node placement, and pod scheduling.

Important

Configuring cluster extensions is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [5.3.1. Extension configuration](#olmv1-config-api_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Configure the namespace an extension watches by using the `.spec.config` field in the `ClusterExtension` resource.

Important

OLM v1 configuration API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Extensions watch all namespaces by default. Some Operators support only namespace-scoped watching based on OLM (Classic) install modes. Configure the `.spec.config.inline.watchNamespace` field to install these Operators.

Whether you must configure this field depends on the install modes supported by the bundle.

##### [5.3.1.1. Configuration API structure](#olmv1-config-api-structure_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

The configuration API uses an opaque structure. The bundle validates the configuration values, not OLM v1. Operator authors can define their own configuration requirements.

Currently, the `Inline` configuration type is the only supported type:

**Example inline configuration**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
...
spec:
  namespace: <installation_namespace>
  config:
    configType: Inline
    inline:
      watchNamespace: <watch_namespace>
```

where:

`<installation_namespace>`
:   Specifies the namespace where the extension components run.

`config.configType`
:   Specifies the configuration type. Currently, `Inline` is the only supported type.

`<watch_namespace>`
:   Specifies the namespace where the extension watches for custom resources. The watch namespace can match or differ from the installation namespace, depending on the install modes supported by the bundle.

#### [5.3.2. Watch namespace configuration requirements](#olmv1-config-api-watch-namespace-requirements_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Avoid installation failures by using the correct `watchNamespace` value for the install modes supported by your bundle. Requirements vary based on whether the bundle supports `AllNamespaces`, `OwnNamespace`, and `SingleNamespace` install modes.

OLM (Classic) `registry+v1` bundles declare the install modes they support. These install modes control whether `watchNamespace` configuration is required or optional, and what values are valid.

Note

OLM v1 does not support multi-tenancy. You cannot install the same extension more than once on a cluster. As a result, the `MultiNamespace` install mode is not supported.

`AllNamespaces`
:   Watches resources across all namespaces in the cluster.

`OwnNamespace`
:   Watches resources only in the installation namespace.

`SingleNamespace`
:   Watches resources in a single namespace that differs from the installation namespace.

Whether the `.spec.config.inline.watchNamespace` field is required depends on the install modes that the bundle supports.

Expand

Table 5.4. Watch namespace requirements by bundle capability

| Bundle install mode support | watchNamespace field | Valid values |
| --- | --- | --- |
| `AllNamespaces` mode only | Not applicable | The `watchNamespace` field is not supported. Extensions watch all namespaces. |
| `OwnNamespace` mode only | Required | Must match `.spec.namespace` field |
| `SingleNamespace` mode only | Required | Must differ from `.spec.namespace` field |
| Both `OwnNamespace` and `SingleNamespace` install modes | Required | Can match or differ from `.spec.namespace` field |
| `AllNamespaces` install mode with one or both of the `OwnNamespace` and `SingleNamespace` install modes | Optional | Omit to watch all namespaces, or specify a namespace to watch only that namespace |

Show more

Important

OLM v1 validates the `watchNamespace` value based on the install mode support that is declared by the bundle. The installation fails with a validation error if you specify an invalid value or omit a required field.

#### [5.3.3. Discovering bundle install modes](#olmv1-discovering-bundle-install-modes_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

You can render the bundle metadata to find which install modes a bundle supports.

**Prerequisites**

* You have installed the `jq` CLI tool.
* You have installed the `opm` CLI tool.

**Procedure**

1. Render the bundle metadata by running the following command:

   ```
   $ opm render <bundle_image> -o json | \
     jq 'select(.schema == "olm.bundle") | .properties[] | select(.type == "olm.bundle.object")'
   ```

   **Example output**

   ```
   {
     "type": "olm.bundle.object",
     "value": {
       "data": "...",
       "ref": "olm.csv"
     }
   }
   ```
2. Decode the base64-encoded CSV data to view install mode declarations:

   ```
   $ echo "<base64_data>" | base64 -d | jq '.spec.installModes'
   ```

   **Example output**

   ```
   [
     {
       "type": "OwnNamespace",
       "supported": true
     },
     {
       "type": "SingleNamespace",
       "supported": true
     },
     {
       "type": "MultiNamespace",
       "supported": false
     },
     {
       "type": "AllNamespaces",
       "supported": false
     }
   ]
   ```

   In this example, the bundle supports both `OwnNamespace` and `SingleNamespace` modes. The `.spec.config.inline.watchNamespace` field is required and can match or differ from the `.spec.namespace` field.

#### [5.3.4. Configuring a watch namespace for a cluster extension (Technology Preview)](#olmv1-deploying-a-ce-in-a-specific-namespace_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

You can configure the watch namespace for extensions that support namespace-scoped resource watching.

Important

Configuring watch namespace for a cluster extension is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have enabled the `TechPreviewNoUpgrade` feature set on the cluster.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension. For more information, see "Cluster extension permissions".
* You have verified the supported install modes for the extension and determined the required `watchNamespace` configuration.

**Procedure**

1. Create a custom resource (CR) based on where you want the extension to watch for resources:

   * To configure the extension to watch its own installation namespace:

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: <extension_name>
     spec:
       namespace: <installation_namespace>
       config:
         configType: Inline
         inline:
           watchNamespace: <installation_namespace>
       serviceAccount:
         name: <service_account>
       source:
         sourceType: Catalog
         catalog:
           packageName: <package_name>
           version: <version>
           upgradeConstraintPolicy: CatalogProvided
     ```

     where:

     `config.inline.watchNamespace`
     :   Specifies the namespace to watch for resources. For requirements and valid values, see "Extension configuration".
   * To configure the extension to watch a different namespace:

     ```
     apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: <extension_name>
     spec:
       namespace: <installation_namespace>
       config:
         configType: Inline
         inline:
           watchNamespace: <watched_namespace>
       serviceAccount:
         name: <service_account>
       source:
         sourceType: Catalog
         catalog:
           packageName: <package_name>
           version: <version>
           upgradeConstraintPolicy: CatalogProvided
     ```
2. Apply the CR to the cluster by running the following command:

   ```
   $ oc apply -f <cluster_extension_cr>.yaml
   ```

**Verification**

* Verify that the extension installed successfully by running the following command:

  ```
  $ oc get clusterextension <extension_name> -o yaml
  ```

  **Example output**

  ```
  apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <extension_name>
  spec:
    namespace: <installation_namespace>
    config:
      configType: Inline
      inline:
        watchNamespace: <installation_namespace>
  status:
    conditions:
    - type: Installed
      status: "True"
      reason: Succeeded
  ```

##### [5.3.4.1. Watch namespace configuration examples](#olmv1-config-api-watch-namespace-examples_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

To configure the `watchNamespace` field correctly for your bundle’s install mode, see the following examples. These show valid configurations for Operators that support the `AllNamespaces`, `OwnNamespace`, and `SingleNamespace` install modes.

**Example `AllNamespaces` install mode**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: openshift-operators
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
```

* The `config` field is omitted. The extension watches all namespaces by default.

**Example `OwnNamespace` install mode**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: example-operators
  config:
    configType: Inline
    inline:
      watchNamespace: example-operators
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
```

* You must set the `watchNamespace` field to use the `OwnNamespace` install mode.
* The `watchNamespace` value must match the `spec.namespace` field value.

**Example `SingleNamespace` install mode**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: example-operators
  config:
    configType: Inline
    inline:
      watchNamespace: production
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
```

* You must set the `watchNamespace` field to use the `SingleNamespace` install mode.
* The `watchNamespace` value must differ from the `spec.namespace` field value.
* In this example, the extension runs in the `example-operators` namespace but watches resources in the `production` namespace.

##### [5.3.4.2. Watch namespace validation errors](#olmv1-clusterextension-watchnamespace-validation-errors_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Validation errors occur when the `watchNamespace` field is omitted or contains an invalid value for the install modes supported by the bundle.

Expand

Table 5.5. Common watchNamespace field validation errors

| Error | Cause | Resolution |
| --- | --- | --- |
| Required field missing | The bundle requires the `watchNamespace` field but it is omitted. | Add the `watchNamespace` field with a value that matches the install modes supported by the bundle. |
| `OwnNamespace` validation error | The bundle only supports `OwnNamespace` mode but the `watchNamespace` value does not match the `.spec.namespace` field. | Set the `watchNamespace` field to the same value as the `.spec.namespace` field. |
| `SingleNamespace` validation error | The bundle only supports `SingleNamespace` mode but the `watchNamespace` value matches the `.spec.namespace` field. | Set the `watchNamespace` field to a different namespace than the `.spec.namespace` field. |
| Invalid configuration | The `.spec.config` structure is malformed or has unsupported fields. | Verify the configuration follows the correct API structure with `configType: Inline` and valid `inline` fields. |

Show more

#### [5.3.5. deploymentConfig API](#olmv1-deployment-config-api_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

The `deploymentConfig` API controls Operator pod runtime settings such as resources, node placement, and environment variables, providing feature parity with OLM (Classic) Subscription configuration.

Important

OLM v1 `deploymentConfig` API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Provides feature parity with the `Subscription.spec.config` configuration of the OLM (Classic). Configure resources, node placement, storage, environment variables, and other deployment settings.

##### [5.3.5.1. deploymentConfig structure](#olmv1-deployment-config-structure_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Configure how the Operator deploys in the `spec.config.inline.deploymentConfig` field as a JSON object.

**Example `deploymentConfig` object**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <installation_namespace>
  serviceAccount:
    name: <service_account_name>
  source:
    sourceType: Catalog
    catalog:
      packageName: <package_name>
  config:
    configType: Inline
    inline:
      deploymentConfig:
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
```

where:

`serviceAccount:`
:   Specifies the service account name for the Operator.

`source:`
:   Specifies the package source configuration.

`deploymentConfig:`
:   Specifies the object for customizing the deployment.

`resources:`
:   Specifies the CPU and memory requests and limits.

`nodeSelector:`
:   Specifies the node placement selector.

`tolerations:`
:   Specifies the node taint tolerations.

##### [5.3.5.2. Supported configuration fields](#olmv1-deployment-config-fields_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Environment variables
:   Add or override environment variables with `env`. Values are merged with existing container environment variables, with `deploymentConfig` values taking precedence.

Environment variable sources
:   Add environment variable sources with `envFrom`. Sources are appended to existing sources; duplicates are skipped.

Resource requirements
:   Specify CPU and memory requests and limits with `resources`. Replaces existing resource requirements.

Node selector
:   Control pod node placement with `nodeSelector`. Replaces existing node selector.

Tolerations
:   Schedule pods on nodes with taints by using `tolerations`. Appended to existing tolerations.

Affinity rules
:   Define pod affinity and anti-affinity rules with `affinity`. Non-nil fields replace corresponding bundle fields.

Volumes and volume mounts
:   Add volumes and volume mounts. Volumes with the same name as existing bundle volumes are overridden; new volumes are appended.

Annotations
:   Add custom pod annotations. Merged with existing annotations. Annotations already set by the bundle cannot be overridden.

##### [5.3.5.3. Configuration validation](#olmv1-deployment-config-validation_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

OLM v1 validates configuration against a JSON schema generated from Kubernetes API definitions. The schema derives from the `SubscriptionConfig` type used in OLM (Classic), providing consistent validation across versions.

Invalid configurations prevent installation and report errors in the `ClusterExtension` resource’s `Progressing` condition. Common validation errors include:

* Unknown field errors when using unsupported configuration options
* Type mismatch errors when field values do not match the expected type
* Required field errors when mandatory nested fields are missing

Note

OLM v1 applies configurations during the `ClusterObjectSet` deployment process, modifying Operator manifests before organizing them into phases.

##### [5.3.5.4. Converting from OLM (Classic)](#olmv1-deployment-config-migration_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Transfer existing `Subscription.spec.config` settings to the `deploymentConfig` object. The YAML structure is the same, but some merge behaviors differ from OLM (Classic).

Note

`volumes` and `volumeMounts` with the same name override existing entries in OLM v1 rather than appending as in OLM (Classic).

**Example OLM (Classic) subscription configuration**

```
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: my-operator
spec:
  name: my-operator
  channel: stable
  config:
    nodeSelector:
      node-role.kubernetes.io/infra: ""
    tolerations:
    - key: node-role.kubernetes.io/infra
      operator: Exists
      effect: NoSchedule
```

**Equivalent OLM v1 cluster extension configuration**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
```

#### [5.3.6. ClusterObjectSets deployment mechanism](#olmv1-clusterobjectsets-deployment-mechanism_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

`ClusterObjectSets` deploy cluster extensions through ordered phases, enabling safe upgrades by maintaining both old and new revisions until the new version succeeds.

Important

OLM v1 ClusterObjectSets is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

`ClusterObjectSets` are cluster-scoped APIs representing versioned resource sets organized into ordered phases. OLM v1 uses `ClusterObjectSets` to deploy Operator resources sequentially.

##### [5.3.6.1. Benefits](#olmv1-clusterobjectsets-benefits_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Phased rollouts
:   Resources deploy in a defined order by kind. For example, Custom Resource Definitions (CRDs) are created before deployments that use them.

Safe upgrades
:   Both old and new revisions remain active until the new version succeeds, mitigating service disruption.

Immutable revision records
:   Immutable revisions provide a clear deployment record.

Large bundle support
:   References externalized secrets to bypass the etcd 1.5 MiB size limit, enabling large bundle deployments.

##### [5.3.6.2. Relationship to the deploymentConfig API](#olmv1-clusterobjectsets-relationship_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

OLM v1 applies `deploymentConfig` settings during the `ClusterObjectSet` process, modifying Operator manifests before organizing them into phases.

##### [5.3.6.3. Deployment phases](#olmv1-clusterobjectsets-phases_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Phases are system-determined groups that organize resources into ordered deployment stages based on their API group and kind. Objects are automatically assigned to well-known phases.

Note

All objects within a phase are applied in no particular order. The next phase begins only after all objects in the current phase pass their readiness probes.

The system assigns resources to the following phases in order:

`namespaces`
:   `Namespace` objects.

`policies`
:   `NetworkPolicy`, `PodDisruptionBudget`, and `PriorityClass` objects.

`identity`
:   `ServiceAccount` objects.

`configuration`
:   `Secret` and `ConfigMap` objects.

`storage`
:   `PersistentVolume`, `PersistentVolumeClaim`, and `StorageClass` objects.

`crds`
:   `CustomResourceDefinition` objects.

`roles`
:   `ClusterRole` and `Role` objects.

`bindings`
:   `ClusterRoleBinding` and `RoleBinding` objects.

`infrastructure`
:   `Service`, `Issuer`, and `Certificate` objects.

`deploy`
:   `Deployment` objects.

`scaling`
:   `VerticalPodAutoscaler` objects.

`publish`
:   `PrometheusRule`, `ServiceMonitor`, `PodMonitor`, `Ingress`, `Route`, and console resources.

`admission`
:   `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` objects.

#### [5.3.7. Inspecting ClusterObjectSets](#olmv1-inspecting-clusterobjectsets_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Monitor and troubleshoot cluster extension deployments by viewing ClusterObjectSet phases, resource status, and revision history.

**Procedure**

1. List all `ClusterObjectSets` in the cluster by entering the following command:

   ```
   $ oc get clusterobjectsets
   ```
2. List `ClusterObjectSets` for a specific extension by running the following command:

   ```
   $ oc get clusterobjectsets -l olm.operatorframework.io/owner-name=<extension_name>
   ```

   Replace `<extension_name>` with your `ClusterExtension` name.
3. View the details of a specific `ClusterObjectSet` by running the following command:

   ```
   $ oc get clusterobjectset <clusterobjectset_name> -o yaml
   ```

   Shows deployment phases, resource status, and conditions.
4. Check the `ClusterExtension` status to see active revisions by running the following command:

   ```
   $ oc get clusterextension <extension_name> -o jsonpath='{.status.activeRevisions}{"\n"}'
   ```

   Shows the active revisions currently deployed.

#### [5.3.8. Customize operator deployments](#olmv1-customizing-operator-deployments_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Customize Operator pod deployments to meet production requirements by configuring resource allocation, node placement, and pod tolerations through the `ClusterExtension` resource.

Important

OLM v1 `deploymentConfig` API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have enabled the `TechPreviewNoUpgrade` feature set on the cluster.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension. For more information, see "Cluster extension permissions".
* You have installed the OpenShift CLI (`oc`).
* You have identified the operator you want to install and customize.

**Procedure**

1. Create a `ClusterExtension` resource with `deploymentConfig` customizations:

   ```
   apiVersion: olm.operatorframework.io/v1
   kind: ClusterExtension
   metadata:
     name: my-operator
   spec:
     namespace: my-operator-ns
     serviceAccount:
       name: my-operator-installer
     config:
       configType: Inline
       inline:
         deploymentConfig:
           resources:
             requests:
               cpu: 100m
               memory: 128Mi
             limits:
               cpu: 500m
               memory: 512Mi
           nodeSelector:
             node-role.kubernetes.io/infra: ""
           tolerations:
           - key: node-role.kubernetes.io/infra
             operator: Exists
             effect: NoSchedule
     source:
       sourceType: Catalog
       catalog:
         packageName: my-operator
         version: 1.0.0
   ```

   where:

   `resources:`
   :   Specifies CPU and memory resource requests and limits for the Operator pod.

   `nodeSelector:`
   :   Specifies pod scheduling restrictions to infrastructure nodes.

   `tolerations:`
   :   Specifies pod tolerations that allow scheduling on nodes with the specified taint.
2. Apply the `ClusterExtension` resource:

   ```
   $ oc apply -f my-operator.yaml
   ```
3. Verify the installation:

   ```
   $ oc get clusterextension my-operator -o yaml
   ```

**Verification**

* Verify that the `deploymentConfig` settings were applied:

  ```
  $ oc get deployment -n my-operator-ns -l olm.operatorframework.io/owner-name=my-operator -o yaml
  ```

  Check the deployment specification for your configured settings such as resource limits, node selectors, tolerations, and volumes.

#### [5.3.9. deploymentConfig examples](#olmv1-deployment-config-examples_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Customize Operator deployments using resource limits, node placement, custom volumes, environment variables, and combined configurations.

Important

OLM v1 `deploymentConfig` API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [5.3.9.1. Environment variables](#olmv1-deployment-config-env-vars_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Add environment variables for runtime configuration.

**Adding environment variables**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: kmm-operator
spec:
  namespace: openshift-kmm
  serviceAccount:
    name: kmm-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        env:
        - name: KMM_MANAGED
          value: "1"
  source:
    sourceType: Catalog
    catalog:
      packageName: kernel-module-management
```

where:

`KMM_MANAGED`
:   Specifies the environment variable used when deploying the Kernel Module Management Operator in a hub-and-spoke configuration.

##### [5.3.9.2. Custom volumes](#olmv1-deployment-config-volumes_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Mount a custom CA certificate for HTTPS communication through a proxy.

**Mounting a custom CA certificate**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        volumes:
        - name: trusted-ca
          configMap:
            name: trusted-ca
            items:
            - key: ca-bundle.crt
              path: tls-ca-bundle.pem
        volumeMounts:
        - name: trusted-ca
          mountPath: /etc/pki/ca-trust/extracted/pem
          readOnly: true
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
```

where:

`volumes:`
:   Specifies a volume created from the `trusted-ca` config map.

`volumeMounts:`
:   Specifies the volume mount to the Operator container at the specified path.

`mountPath:`
:   Specifies the path where the certificate bundle is available inside the container.

##### [5.3.9.3. Pod anti-affinity](#olmv1-deployment-config-affinity_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Spread Operator pods across nodes for high availability.

**Pod anti-affinity for high availability**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: app.kubernetes.io/name
                    operator: In
                    values:
                    - my-operator
                topologyKey: kubernetes.io/hostname
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
```

where:

`podAntiAffinity:`
:   Specifies anti-affinity rules for the Operator pod.

`preferredDuringSchedulingIgnoredDuringExecution:`
:   Specifies soft constraints that the scheduler tries to enforce but does not guarantee.

`topologyKey`
:   Specifies the topology key that groups nodes by hostname to ensure pods are spread across different nodes.

##### [5.3.9.4. Multiple customizations](#olmv1-deployment-config-combined_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Combine multiple deployment customizations.

**Production Operator with combined customizations**

```
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: production-operator
spec:
  namespace: production-operators
  serviceAccount:
    name: production-operator-installer
  config:
    configType: Inline
    inline:
      deploymentConfig:
        resources:
          requests:
            cpu: 200m
            memory: 256Mi
          limits:
            cpu: 1000m
            memory: 1Gi
        env:
        - name: LOG_LEVEL
          value: info
        - name: ENABLE_METRICS
          value: "true"
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
        annotations:
          monitoring.openshift.io/scrape: "true"
          monitoring.openshift.io/port: "8080"
  source:
    sourceType: Catalog
    catalog:
      packageName: production-operator
      version: 2.1.0
```

where:

`resources:`
:   Specifies memory and CPU requests and limits for the Operator pod.

`env:`
:   Specifies environment variables for the Operator.

`nodeSelector:`
:   Specifies that the pod runs on infrastructure nodes.

`tolerations:`
:   Specifies pod tolerations that allow scheduling on nodes with the specified taint.

`annotations:`
:   Specifies Prometheus monitoring annotations for the pod.

#### [5.3.10. deploymentConfig field reference](#olmv1-deployment-config-reference_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Field reference for the `deploymentConfig` API including OLM (Classic) to OLM v1 field mappings and merge behavior for each configuration option.

Important

OLM v1 `deploymentConfig` API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [5.3.10.1. Field mapping from OLM (Classic) to OLM v1](#olmv1-deployment-config-field-mapping_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Field conversion from OLM (Classic) to OLM v1:

Expand

Table 5.6. OLM (Classic) to OLM v1 configuration field mapping

| OLM (Classic) field path | OLM v1 field path | Notes |
| --- | --- | --- |
| `spec.config.env` | `spec.config.inline.deploymentConfig.env` | Environment variables are merged. OLM v1 values take precedence over bundle values. |
| `spec.config.envFrom` | `spec.config.inline.deploymentConfig.envFrom` | Environment variable sources are appended to bundle sources. Duplicates are skipped. |
| `spec.config.resources` | `spec.config.inline.deploymentConfig.resources` | Resource specifications completely replace bundle resource requirements. |
| `spec.config.nodeSelector` | `spec.config.inline.deploymentConfig.nodeSelector` | Node selectors completely replace bundle node selectors. |
| `spec.config.tolerations` | `spec.config.inline.deploymentConfig.tolerations` | Tolerations are appended to bundle tolerations. |
| `spec.config.affinity` | `spec.config.inline.deploymentConfig.affinity` | Affinity rules selectively override bundle affinity. Non-nil fields replace corresponding bundle fields. |
| `spec.config.volumes` | `spec.config.inline.deploymentConfig.volumes` | Volumes override existing bundle volumes with the same name; new volumes are appended. |
| `spec.config.volumeMounts` | `spec.config.inline.deploymentConfig.volumeMounts` | Volume mounts override existing bundle volume mounts with the same name; new mounts are appended. |
| `spec.config.annotations` | `spec.config.inline.deploymentConfig.annotations` | Annotations are merged with bundle annotations. Bundle annotations take precedence on conflicts. |
| `spec.config.selector` | Not supported | The `selector` field from OLM (Classic) is not supported in OLM v1. This field was never used in OLM (Classic). |

Show more

##### [5.3.10.2. Merge and override behavior](#olmv1-deployment-config-merge-behavior_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Configuration fields have different merge behaviors:

Replace
:   Completely replaces bundle values. Applies to: `resources`, `nodeSelector`

Append
:   Adds to existing bundle values. Applies to: `tolerations`, `envFrom`

Override and append
:   Overrides existing values with the same name; new values are appended. Applies to: `volumes`, `volumeMounts`

Merge with precedence
:   Merges with bundle values. `deploymentConfig` values take precedence on conflicts. Applies to: `env`

Merge with bundle precedence
:   Merges with bundle values. Bundle takes precedence on conflicts. Applies to: `annotations`

Selective override
:   Non-nil fields replace corresponding bundle fields. Applies to: `affinity`

##### [5.3.10.3. Environment variable fields](#olmv1-deployment-config-env-reference_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

`env`
:   Specifies an array of environment variable objects. Merged with existing container environment variables, with `deploymentConfig` values taking precedence. Each object has:

    * `name`: Environment variable name (string, required).
    * `value`: Environment variable value (string, optional).
    * `valueFrom`: Reference to a secret or config map key (object, optional).

`envFrom`
:   Specifies an array of environment variable source objects merged with existing sources. Each object can reference:

    * `configMapRef`: Config map containing environment variables.
    * `secretRef`: Secret containing environment variables.

##### [5.3.10.4. Resource requirements fields](#olmv1-deployment-config-resources-reference_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

`resources`
:   Specifies compute resource requirements that completely replace existing bundle resource requirements. Contains:

    * `requests`: Minimum resources required.

      + `cpu`: CPU request (string, for example, `"100m"`, `"0.5"`).
      + `memory`: Memory request (string, for example, `"128Mi"`, `"1Gi"`).
    * `limits`: Maximum resources allowed.

      + `cpu`: CPU limit (string).
      + `memory`: Memory limit (string).

##### [5.3.10.5. Node placement fields](#olmv1-deployment-config-node-placement-reference_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

`nodeSelector`
:   Specifies a map of key-value pairs for node selection. Completely replaces any existing node selector. Pods schedule only on nodes with all specified labels.

    **Example node selector**

    ```
    nodeSelector:
      node-role.kubernetes.io/infra: ""
      disktype: ssd
    ```

`tolerations`
:   Specifies an array of toleration objects appended to existing bundle tolerations. Each toleration has:

    * `key`: Taint key (string).
    * `operator`: Operator (string: `Exists`, `Equal`).
    * `value`: Taint value (string, required if `operator` is `Equal`).
    * `effect`: Taint effect (string: `NoSchedule`, `PreferNoSchedule`, `NoExecute`).
    * `tolerationSeconds`: Time before pod eviction for `NoExecute` effect (integer).

`affinity`
:   Specifies an affinity rules object. Non-nil fields replace corresponding bundle fields. Contains:

    * `nodeAffinity`: Node label-based scheduling rules.
    * `podAffinity`: Pod label-based scheduling rules.
    * `podAntiAffinity`: Pod spreading rules across nodes.

##### [5.3.10.6. Storage fields](#olmv1-deployment-config-storage-reference_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

`volumes`
:   Specifies an array of volume objects. Volumes with the same name as existing bundle volumes are overridden; new volumes are appended. All Kubernetes volume types are supported. Each volume requires a `name` field (string).

`volumeMounts`
:   Specifies an array of volume mount objects. Volume mounts with the same name as existing bundle volume mounts are overridden; new mounts are appended. Each mount has:

    * `name`: Volume name to mount (string, required).
    * `mountPath`: The path within the container (string, required).
    * `readOnly`: Whether the volume is read-only (boolean, optional).
    * `subPath`: A path within the volume (string, optional).

##### [5.3.10.7. Metadata fields](#olmv1-deployment-config-metadata-reference_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

`annotations`
:   Specifies a map of key-value pairs for deployment and pod annotations. Annotations are applied to both the deployment metadata and the pod template metadata. Annotations from `deploymentConfig` are merged with bundle annotations. When keys conflict, bundle annotations take precedence.

    **Example annotations**

    ```
    annotations:
      monitoring.openshift.io/scrape: "true"
      monitoring.openshift.io/port: "8080"
    ```

#### [5.3.11. Troubleshooting deploymentConfig](#olmv1-deployment-config-troubleshooting_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Common `deploymentConfig` issues include validation errors, configuration verification problems, and annotation conflicts that can prevent successful Operator installation.

Important

OLM v1 `deploymentConfig` API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [5.3.11.1. Validation errors](#olmv1-deployment-config-troubleshooting-validation_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Check the `Progressing` condition for validation errors when installation fails:

```
$ oc get clusterextension <extension_name> -o jsonpath='{.status.conditions[?(@.type=="Progressing")].message}'
```

Common validation errors and resolutions:

Unknown field
:   Configuration includes an unsupported field. Remove unsupported fields.

Type mismatch
:   Field value does not match the expected type. Verify field types match Kubernetes specifications.

Required field missing
:   Mandatory nested field is missing. Complete all required fields in nested structures.

##### [5.3.11.2. Verifying applied configuration](#olmv1-deployment-config-troubleshooting-applied_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Inspect the Operator deployment to verify applied configurations:

```
$ oc get deployment -n <namespace> -l olm.operatorframework.io/owner-name=<extension_name> -o yaml
```

Configuration locations in the deployment specification:

* **Environment variables**: `spec.template.spec.containers[].env` and `spec.template.spec.containers[].envFrom`
* **Resources**: `spec.template.spec.containers[].resources`
* **Node selector**: `spec.template.spec.nodeSelector`
* **Tolerations**: `spec.template.spec.tolerations`
* **Affinity**: `spec.template.spec.affinity`
* **Volumes**: `spec.template.spec.volumes` and `spec.template.spec.containers[].volumeMounts`
* **Annotations**: `metadata.annotations` and `spec.template.metadata.annotations`

##### [5.3.11.3. Annotation conflicts](#olmv1-deployment-config-troubleshooting-conflicts_olmv1-configuring-extensions) Copy linkLink copied to clipboard!

Bundle annotations take precedence over `deploymentConfig` annotations when keys conflict. View the installed bundle information:

```
$ oc get clusterextension <extension_name> -o jsonpath='{.status.install.bundle}'
```

This returns the bundle name and version. To see the annotations applied to the Operator pod template:

```
$ oc get deployment -n <namespace> -l olm.operatorframework.io/owner-name=<extension_name> -o jsonpath='{.items[0].spec.template.metadata.annotations}'
```

To override a bundle annotation, modify the bundle or accept the bundle value.

### [5.4. User access to extension resources](#user-access-resources) Copy linkLink copied to clipboard!

After you install a cluster extension managed by Operator Lifecycle Manager (OLM) v1, the extension might provide `CustomResourceDefinition` (CRD) objects that expose new cluster APIs. While cluster administrators automatically have full access to these resources, regular users usually require additional permissions.

OLM v1 does not automatically configure or manage role-based access control (RBAC) for regular users to interact with the APIs provided by installed extensions. Cluster administrators must define the required RBAC policy to create, view, or edit these custom resources (CRs) for such users.

Note

The RBAC permissions described for user access to extension resources are different from the permissions that must be added to a service account to enable OLM v1-based initial installation of a cluster extension itself. For more on RBAC requirements while installing an extension, see "Cluster extension permissions" in "Managing extensions".

#### [5.4.1. Common default cluster roles for users](#olmv1-default-cluster-roles-users_user-access-resources) Copy linkLink copied to clipboard!

An installed cluster extension can include default cluster roles that grant regular users role-based access control (RBAC) to the extension’s API resources.

Cluster extensions commonly include the following default cluster role policies:

`view` cluster role
:   Grants read-only access to custom resource (CR) objects for specified API resources across the cluster. This role provides resource visibility without permission to modify resources, which is ideal for monitoring and viewing.

`edit` cluster role
:   Grants permissions to create, update, and delete CR objects across the cluster. This role is intended for users who manage resources but do not manage RBAC or cluster permissions.

`admin` cluster role
:   Grants full administrative permissions, including create, update, and delete actions, over all CR objects for specified API resources across the cluster.

#### [5.4.2. Finding API groups and resources exposed by a cluster extension](#olmv1-finding-ce-resources_user-access-resources) Copy linkLink copied to clipboard!

To create appropriate RBAC policies for granting user access to cluster extension resources, you must know which API groups and resources are exposed by the installed extension. As an administrator, you can inspect custom resource definitions (CRDs) installed on the cluster by using OpenShift CLI (`oc`).

**Prerequisites**

* A cluster extension has been installed on your cluster.

**Procedure**

* To list installed CRDs while specifying a label selector targeting a specific cluster extension by name to find only CRDs owned by that extension, run the following command:

  ```
  $ oc get crds -l 'olm.operatorframework.io/owner-kind=ClusterExtension,olm.operatorframework.io/owner-name=<cluster_extension_name>'
  ```
* Alternatively, you can search through all installed CRDs and individually inspect them by CRD name:

  1. List all available custom resource definitions (CRDs) currently installed on the cluster by running the following command:

     ```
     $ oc get crds
     ```

     Find the CRD you are looking for in the output.
  2. Inspect the individual CRD further to find its API groups by running the following command:

     ```
     $ oc get crd <crd_name> -o yaml
     ```

#### [5.4.3. Granting user access to extension resources by using custom role bindings](#olmv1-granting-user-access-binding_user-access-resources) Copy linkLink copied to clipboard!

As a cluster administrator, you can manually create and configure role-based access control (RBAC) policies to grant user access to extension resources by using custom role bindings.

**Prerequisites**

* A cluster extension has been installed on your cluster.
* You have a list of API groups and resource names, as described in "Finding API groups and resources exposed by a cluster extension".

**Procedure**

1. If the installed cluster extension does not provide default cluster roles, manually create one or more roles:

   1. Consider the use cases for the set of roles described in "Common default cluster roles for users".

      For example, create one or more of the following `ClusterRole` object definitions, replacing `<cluster_extension_api_group>` and `<cluster_extension_custom_resource>` with the actual API group and resource names provided by the installed cluster extension:

      **Example `view-custom-resource.yaml` file**

      ```
      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRole
      metadata:
        name: view-custom-resource
      rules:
      - apiGroups:
        - <cluster_extension_api_group>
        resources:
        - <cluster_extension_custom_resources>
        verbs:
        - get
        - list
        - watch
      ```

      **Example `edit-custom-resource.yaml` file**

      ```
      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRole
      metadata:
        name: edit-custom-resource
      rules:
      - apiGroups:
        - <cluster_extension_api_group>
        resources:
        - <cluster_extension_custom_resources>
        verbs:
        - get
        - list
        - watch
        - create
        - update
        - patch
        - delete
      ```

      **Example `admin-custom-resource.yaml` file**

      ```
      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRole
      metadata:
        name: admin-custom-resource
      rules:
      - apiGroups:
        - <cluster_extension_api_group>
        resources:
        - <cluster_extension_custom_resources>
        verbs:
        - '*'
      ```

      Setting a wildcard (`*`) in the `rules.verbs` field allows all actions on the specified resources.
   2. Create the cluster roles by running the following command for any YAML files you created:

      ```
      $ oc create -f <filename>.yaml
      ```
2. Associate a cluster role to specific users or groups to grant them the necessary permissions for the resource by binding the cluster roles to individual user or group names:

   1. Create an object definition for either a *cluster role binding* to grant access across all namespaces or a *role binding* to grant access within a specific namespace:

      * The following example cluster role bindings grant read-only `view` access to the custom resource across all namespaces:

        **Example `ClusterRoleBinding` object for a user**

        ```
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          name: view-custom-resource-binding
        subjects:
        - kind: User
          name: <user_name>
        roleRef:
          kind: ClusterRole
          name: view-custom-resource
          apiGroup: rbac.authorization.k8s.io
        ```

        **Example `ClusterRoleBinding` object for a user**

        ```
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          name: view-custom-resource-binding
        subjects:
        - kind: Group
          name: <group_name>
        roleRef:
          kind: ClusterRole
          name: view-custom-resource
          apiGroup: rbac.authorization.k8s.io
        ```
      * The following role binding restricts `edit` permissions to a specific namespace:

        **Example `RoleBinding` object for a user**

        ```
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: edit-custom-resource-edit-binding
          namespace: <namespace>
        subjects:
        - kind: User
          name: <username>
        roleRef:
          kind: Role
          name: custom-resource-edit
          apiGroup: rbac.authorization.k8s.io
        ```
   2. Save your object definition to a YAML file.
   3. Create the object by running the following command:

      ```
      $ oc create -f <filename>.yaml
      ```

#### [5.4.4. Granting user access to extension resources by using aggregated cluster roles](#olmv1-granting-user-access-aggregated_user-access-resources) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure role-based access control (RBAC) policies to grant user access to extension resources by using aggregated cluster roles.

Note

To automatically extend existing default cluster roles, you can add *aggregation labels* by adding one or more of the following labels to a `ClusterRole` object:

```
# ..
metadata:
  labels:
    rbac.authorization.k8s.io/aggregate-to-admin: "true"
    rbac.authorization.k8s.io/aggregate-to-edit: "true"
    rbac.authorization.k8s.io/aggregate-to-view: "true"
# ..
```

This allows users who already have `view`, `edit`, or `admin` roles to interact with the custom resource specified by the `ClusterRole` object without requiring additional role or cluster role bindings to specific users or groups.

**Prerequisites**

* A cluster extension has been installed on your cluster.
* You have a list of API groups and resource names, as described in "Finding API groups and resources exposed by a cluster extension".

**Procedure**

1. Create an object definition for a cluster role that specifies the API groups and resources provided by the cluster extension and add an aggregation label to extend one or more existing default cluster roles:

   **Example `ClusterRole` object with an aggregation label**

   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRole
   metadata:
     name: view-custom-resource-aggregated
     labels:
       rbac.authorization.k8s.io/aggregate-to-view: "true"
   rules:
     - apiGroups:
         - <cluster_extension_api_group>
       resources:
         - <cluster_extension_custom_resource>
       verbs:
         - get
         - list
         - watch
   ```

   You can create similar `ClusterRole` objects for `edit` and `admin` with appropriate verbs, such as `create`, `update`, and `delete`. By using aggregation labels, the permissions for the custom resources are added to the default roles.
2. Save your object definition to a YAML file.
3. Create the object by running the following command:

   ```
   $ oc create -f <filename>.yaml
   ```

### [5.5. Update paths](#update-paths) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) v1 supports OLM (Classic) semantics for update paths, also known as upgrade edges or upgrade constraints. Support includes `replaces`, `skips`, and `skipRange` directives, with a few noted differences.

By supporting OLM (Classic) semantics, OLM v1 accurately reflects the update graph from catalogs.

OLM v1 differs from the original OLM (Classic) implementation in the following ways:

* If there are multiple possible successors, OLM v1 behavior differs in the following ways:

  + In OLM (Classic), the successor closest to the channel head is chosen.
  + In OLM v1, the successor with the highest semantic version (semver) is chosen.
* Consider the following set of file-based catalog (FBC) channel entries:

  ```
  # ...
  - name: example.v3.0.0
    skips: ["example.v2.0.0"]
  - name: example.v2.0.0
    skipRange: >=1.0.0 <2.0.0
  ```

  If `1.0.0` is installed, OLM v1 behavior differs in the following ways:

  + OLM (Classic) will not detect an update path to `v2.0.0` because `v2.0.0` is skipped and not on the `replaces` chain.
  + OLM v1 will detect the update path because OLM v1 does not have a concept of a `replaces` chain. OLM v1 finds all entries that have a `replace`, `skip`, or `skipRange` value that covers the currently installed version.

#### [5.5.1. Support for version ranges](#olmv1-version-range-support_update-paths) Copy linkLink copied to clipboard!

In Operator Lifecycle Manager (OLM) v1, you can specify a version range by using a comparison string in an Operator or extension’s custom resource (CR). If you specify a version range in the CR, OLM v1 installs or updates to the latest version of the Operator that can be resolved within the version range.

The resolved version workflow includes the following steps:

* The resolved version is the latest version of the Operator that satisfies the constraints of the Operator and the environment.
* An Operator update within the specified range is automatically installed if it is resolved successfully.
* An update is not installed if it is outside of the specified range or if it cannot be resolved successfully.

#### [5.5.2. Version comparison strings](#olmv1-version-range-comparisons_update-paths) Copy linkLink copied to clipboard!

To define a version range for a cluster extension, add a comparison string to the custom resource (CR) of the extension.

A comparison string is a list of space- or comma-separated values and one or more comparison operators enclosed in double quotation marks (`"`). You can add another comparison string by including an `OR`, or double vertical bar (`||`), comparison operator between the strings.

Expand

Table 5.7. Basic comparisons

| Comparison operator | Definition |
| --- | --- |
| `=` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Show more

You can specify a version range in an Operator or extension’s CR by using a range comparison similar to the following example:

**Example version range comparison**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: ">=1.11, <1.13"
```

You can use wildcard characters in all types of comparison strings. OLM v1 accepts `x`, `X`, and asterisks (`*`) as wildcard characters. When you use a wildcard character with the equal sign (`=`) comparison operator, you define a comparison at the patch or minor version level.

Expand

Table 5.8. Example wildcard characters in comparison strings

| Wildcard comparison | Matching string |
| --- | --- |
| `1.11.x` | `>=1.11.0, <1.12.0` |
| `>=1.12.X` | `>=1.12.0` |
| `<=2.x` | `<3` |
| `*` | `>=0.0.0` |

Show more

You can make patch release comparisons by using the tilde (`~`) comparison operator. Patch release comparisons specify a minor version up to the next major version.

Expand

Table 5.9. Example patch release comparisons

| Patch release comparison | Matching string |
| --- | --- |
| `~1.11.0` | `>=1.11.0, <1.12.0` |
| `~1` | `>=1, <2` |
| `~1.12` | `>=1.12, <1.13` |
| `~1.12.x` | `>=1.12.0, <1.13.0` |
| `~1.x` | `>=1, <2` |

Show more

You can use the caret (`^`) comparison operator to make a comparison for a major release. If you make a major release comparison before the first stable release is published, the minor versions define the API’s level of stability. In the semantic versioning (semver) specification, the first stable release is published as the `1.0.0` version.

Expand

Table 5.10. Example major release comparisons

| Major release comparison | Matching string |
| --- | --- |
| `^0` | `>=0.0.0, <1.0.0` |
| `^0.0` | `>=0.0.0, <0.1.0` |
| `^0.0.3` | `>=0.0.3, <0.0.4` |
| `^0.2` | `>=0.2.0, <0.3.0` |
| `^0.2.3` | `>=0.2.3, <0.3.0` |
| `^1.2.x` | `>= 1.2.0, < 2.0.0` |
| `^1.2.3` | `>= 1.2.3, < 2.0.0` |
| `^2.x` | `>= 2.0.0, < 3` |
| `^2.3` | `>= 2.3, < 3` |

Show more

#### [5.5.3. Example custom resources (CRs) that specify a target version](#olmv1-about-target-versions_update-paths) Copy linkLink copied to clipboard!

In Operator Lifecycle Manager (OLM) v1, cluster administrators can declaratively set the target version of an Operator or extension in the custom resource (CR).

You can define a target version by specifying any of the following fields:

* Channel
* Version number
* Version range

If you specify a channel in the CR, OLM v1 installs the latest version of the Operator or extension that can be resolved within the specified channel. When updates are published to the specified channel, OLM v1 automatically updates to the latest release that can be resolved from the channel.

**Example CR with a specified channel**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        channels:
          - latest
```

Installs the latest release that can be resolved from the specified channel. Updates to the channel are automatically installed. Specify the value of the `channels` parameter as an array. This field is optional

If you specify the Operator or extension’s target version in the CR, OLM v1 installs the specified version. When the target version is specified in the CR, OLM v1 does not change the target version when updates are published to the catalog.

If you want to update the version of the Operator that is installed on the cluster, you must manually edit the Operator’s CR. Specifying an Operator’s target version pins the Operator’s version to the specified release.

**Example CR with the target version specified**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: "1.11.1"
```

Specifies the target version. If you want to update the version of the Operator or extension that is installed, you must manually update this field the CR to the desired target version. This field is optional.

If you want to define a range of acceptable versions for an Operator or extension, you can specify a version range by using a comparison string. When you specify a version range, OLM v1 installs the latest version of an Operator or extension that can be resolved by the Operator Controller.

**Example CR with a version range specified**

```
apiVersion: olm.operatorframework.io/v1
  kind: ClusterExtension
  metadata:
    name: <clusterextension_name>
  spec:
    namespace: <installed_namespace>
    serviceAccount:
      name: <service_account_installer_name>
    source:
      sourceType: Catalog
      catalog:
        packageName: <package_name>
        version: ">1.11.1"
```

Specifies that the desired version range is greater than version `1.11.1`. This field is optional.

After you create or update a CR, apply the configuration file by running the following command:

**Command syntax**

```
$ oc apply -f <extension_name>.yaml
```

#### [5.5.4. Forcing an update or rollback](#olmv1-forcing-an-update-or-rollback_update-paths) Copy linkLink copied to clipboard!

OLM v1 does not support automatic updates to the next major version or rollbacks to an earlier version. If you want to perform a major version update or rollback, you must verify and force the update manually.

Warning

You must verify the consequences of forcing a manual update or rollback. Failure to verify a forced update or rollback might have catastrophic consequences such as data loss.

**Prerequisites**

* You have a catalog installed.
* You have an Operator or extension installed.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension you want to install. For more information, see *Creating a service account*.

**Procedure**

1. Edit the custom resource (CR) of your Operator or extension as shown in the following example:

   **Example CR**

   ```
   apiVersion: olm.operatorframework.io/v1
     kind: ClusterExtension
     metadata:
       name: <clusterextension_name>
     spec:
       namespace: <installed_namespace>
       serviceAccount:
         name: <service_account_installer_name>
       source:
         sourceType: Catalog
         catalog:
           packageName: <package_name>
           channels:
             - <channel_name>
           version: <version_or_version_range>
           upgradeConstraintPolicy: SelfCertified
   ```

   where:

   `spec.namespace`
   :   Specifies the namespace where you want the bundle installed, such as `pipelines` or `my-extension`. Extensions are still cluster-scoped and might contain resources that are installed in different namespaces.

   `spec.serviceAccount.name`
   :   Specifies the name of the service account you created to install, update, and manage your extension.

   `spec.source.catalog.channels`
   :   Specifies channel names as an array, such as `pipelines-1.14` or `latest`. This field is optional.

   `spec.source.catalog.version`
   :   Specifies the version or version range, such as `1.14.0`, `1.14.x`, or `>=1.16`, of the package you want to install or update. This field is optional.

   `spec.source.catalog.upgradeConstraintPolicy`
   :   Specifies the upgrade constraint policy. To force an update or rollback, set the field to `SelfCertified`. If unspecified, the default setting is `CatalogProvided`. The `CatalogProvided` setting only updates if the new version satisfies the upgrade constraints set by the package author. This field is optional.
2. Apply the changes to your Operator or extensions CR by running the following command:

   ```
   $ oc apply -f <extension_name>.yaml
   ```

#### [5.5.5. Compatibility with OpenShift Container Platform versions](#olmv1-ocp-compat_update-paths) Copy linkLink copied to clipboard!

Before cluster administrators can update their OpenShift Container Platform cluster to its next minor version, they must ensure that all installed Operators are updated to a bundle version that is compatible with the cluster’s next minor version (4.y+1).

For example, Kubernetes periodically deprecates certain APIs that are removed in subsequent releases. If an extension is using a deprecated API, it might no longer work after the OpenShift Container Platform cluster is updated to the Kubernetes version where the API has been removed.

If an Operator author knows that a specific bundle version is not supported and will not work correctly, for any reason, on OpenShift Container Platform later than a certain cluster minor version, they can configure the maximum version of OpenShift Container Platform that their Operator is compatible with.

In the Operator project’s cluster service version (CSV), authors can set the `olm.maxOpenShiftVersion` annotation to prevent administrators from updating the cluster before updating the installed Operator to a compatible version.

**Example CSV with `olm.maxOpenShiftVersion` annotation**

```
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  annotations:
    "olm.properties": '[{"type": "olm.maxOpenShiftVersion", "value": "<cluster_version>"}]'
```

+ Replace `<cluster_version>` with the latest minor version of OpenShift Container Platform (4.y) that an Operator is compatible with. For example, setting `value` to `4.22` prevents cluster updates to minor versions later than 4.22 when this bundle is installed on a cluster.

If the `olm.maxOpenShiftVersion` field is omitted, cluster updates are not blocked by this Operator.

Note

When determining a cluster’s next minor version (4.y+1), OLM v1 only considers major and minor versions (x and y) for comparisons. It ignores any *z-stream* versions (4.y.z), also known as patch releases, or pre-release versions.

For example, if the cluster’s current version is `4.22.0`, the next minor version is `4.23`. If the current version is `4.22.0-rc1`, the next minor version is still `4.23`.

##### [5.5.5.1. Cluster updates blocked by olm cluster Operator](#olmv1-blocked-cluster-updates_update-paths) Copy linkLink copied to clipboard!

If an installed Operator’s `olm.maxOpenShiftVersion` field is set and a cluster administrator attempts to update their cluster to a version that the Operator does not provide a valid update path for, the cluster update fails and the `Upgradeable` status for the `olm` cluster Operator is set to `False`.

To resolve the issue, the cluster administrator must either update the installed Operator to a version with a valid update path, if one is available, or they must uninstall the Operator. Then, they can attempt the cluster update again.

### [5.6. Custom resource definition (CRD) upgrade safety](#crd-upgrade-safety) Copy linkLink copied to clipboard!

When you update a custom resource definition (CRD) provided by a cluster extension, Operator Lifecycle Manager (OLM) v1 runs a CRD upgrade safety preflight check to ensure compatibility with earlier versions.

The CRD update must pass the validation checks before the change is allowed to progress on a cluster.

#### [5.6.1. Prohibited CRD upgrade changes](#prohibited-crd-upgrades_crd-upgrade-safety) Copy linkLink copied to clipboard!

To avoid making a modification that does not validate, review the custom resource definiton (CRD) changes that are blocked by the upgrade safety preflight check.

The CRD upgrade safety preflight check blocks an upgrade if it detects any of the following changes to an existing CRD:

* Adding a new required field to an existing version
* Removing an existing field from an existing version
* Changing an existing field type in an existing version
* Adding a default value to a field that did not previously have one
* Changing the default value of an existing field
* Removing the default value of an existing field
* Adding enum restrictions to a field that did not previously have them
* Removing existing enum values from an existing field
* Increasing the minimum value of an existing field in an existing version
* Decreasing the maximum value of an existing field in an existing version
* Adding minimum or maximum constraints to a field that did not previously have them

Note

Rules for minimum and maximum values apply to the `minimum`, `minLength`, `minProperties`, `minItems`, `maximum`, `maxLength`, `maxProperties`, and `maxItems` constraints.

The preflight check also blocks an upgrade for the following structural changes, which are handled by the Kubernetes API server:

* Changing the CRD scope between `Cluster` and `Namespace`
* Removing an existing stored version of the CRD

If the CRD upgrade safety preflight check detects any prohibited change, it logs an error for each violation.

Tip

If a CRD change is neither explicitly allowed nor categorized as a known prohibited change, the preflight check blocks the upgrade and logs an "unknown change" error.

#### [5.6.2. Allowed CRD upgrade changes](#allowed-crd-changes_crd-upgrade-safety) Copy linkLink copied to clipboard!

Reference which custom resource definition (CRD) changes are compatible with earlier versions to avoid unexpected halts during the upgrade safety preflight check.

The following CRD changes are compatible with earlier versions and pass the upgrade safety preflight check:

* Adding new values to an existing enum field
* Changing an existing required field to optional in an existing version
* Decreasing the minimum value of an existing field in an existing version
* Increasing the maximum value of an existing field in an existing version
* Adding a new version of the CRD without modifying existing versions

#### [5.6.3. Disabling the CRD upgrade safety preflight check](#disabling-crd-preflight_crd-upgrade-safety) Copy linkLink copied to clipboard!

You can disable the custom resource definition (CRD) upgrade safety preflight check. In the `ClusterExtension` object that provides the CRD, set the `install.preflight.crdUpgradeSafety.enforcement` field with the value of `None`.

Warning

Disabling the CRD upgrade safety preflight check could break backwards compatibility with stored versions of the CRD and cause other unintended consequences on the cluster.

You cannot disable individual field validators. If you disable the CRD upgrade safety preflight check, you disable all field validators.

Note

If you disable the CRD upgrade safety preflight check in Operator Lifecycle Manager (OLM) v1, the Kubernetes API server still prevents the following operations:

* Changing scope from `Cluster` to `Namespace` or from `Namespace` to `Cluster`
* Removing an existing stored version of the CRD

**Prerequisites**

* You have a cluster extension installed.

**Procedure**

1. Edit the `ClusterExtension` object of the CRD:

   ```
   $ oc edit clusterextension <clusterextension_name>
   ```
2. Set the `install.preflight.crdUpgradeSafety.enforcement` field to `None`:

   **Example `ClusterExtension` object**

   ```
   apiVersion: olm.operatorframework.io/v1
   kind: ClusterExtension
   metadata:
     name: clusterextension-sample
   spec:
     namespace: default
     serviceAccount:
       name: sa-example
     source:
       sourceType: "Catalog"
       catalog:
         packageName: argocd-operator
         version: 0.6.0
     install:
       preflight:
         crdUpgradeSafety:
           enforcement: None
   ```

#### [5.6.4. Examples of unsafe CRD changes](#examples-unsafe_crd-upgrade-safety) Copy linkLink copied to clipboard!

Review the example unsafe custom resource definition (CRD) changes to recognize modifications that trigger the CRD upgrade safety preflight check.

The following examples use this baseline `CustomResourceDefinition` object:

**Example CRD object**

```
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.13.0
  name: example.test.example.com
spec:
  group: test.example.com
  names:
    kind: Sample
    listKind: SampleList
    plural: samples
    singular: sample
  scope: Namespaced
  versions:
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        properties:
          apiVersion:
            type: string
          kind:
            type: string
          metadata:
            type: object
          spec:
            type: object
          status:
            type: object
          pollInterval:
            type: string
        type: object
    served: true
    storage: true
    subresources:
      status: {}
```

##### [5.6.4.1. Scope change](#scope-change_crd-upgrade-safety) Copy linkLink copied to clipboard!

The following example changes the `spec.scope` field from `Namespaced` to `Cluster`:

**Example scope change in a CRD**

```
spec:
  group: test.example.com
  names:
    kind: Sample
    listKind: SampleList
    plural: samples
    singular: sample
  scope: Cluster
  versions:
  - name: v1alpha1
```

**Example error output**

```
validating upgrade for CRD "test.example.com" failed: CustomResourceDefinition test.example.com failed upgrade safety validation. "NoScopeChange" validation failed: scope changed from "Namespaced" to "Cluster"
```

##### [5.6.4.2. Removal of a stored version](#stored-version-removal_crd-upgrade-safety) Copy linkLink copied to clipboard!

The following example removes the existing stored version, `v1alpha1`:

**Example removal of a stored version in a CRD**

```
versions:
- name: v1alpha2
  schema:
    openAPIV3Schema:
      properties:
        apiVersion:
          type: string
        kind:
          type: string
        metadata:
          type: object
        spec:
          type: object
        status:
          type: object
        pollInterval:
          type: string
      type: object
```

**Example error output**

```
validating upgrade for CRD "test.example.com" failed: CustomResourceDefinition test.example.com failed upgrade safety validation. "NoStoredVersionRemoved" validation failed: stored version "v1alpha1" removed
```

##### [5.6.4.3. Removal of an existing field](#removal-existing-field_crd-upgrade-safety) Copy linkLink copied to clipboard!

The following example removes the `pollInterval` property field from the `v1alpha1` schema:

**Example removal of an existing field in a CRD**

```
versions:
- name: v1alpha1
  schema:
    openAPIV3Schema:
      properties:
        apiVersion:
          type: string
        kind:
          type: string
        metadata:
          type: object
        spec:
          type: object
        status:
          type: object
      type: object
```

**Example error output**

```
validating upgrade for CRD "test.example.com" failed: CustomResourceDefinition test.example.com failed upgrade safety validation. "NoExistingFieldRemoved" validation failed: crd/test.example.com version/v1alpha1 field/^.spec.pollInterval may not be removed
```

##### [5.6.4.4. Addition of a required field](#addition-required-field_crd-upgrade-safety) Copy linkLink copied to clipboard!

The following example changes the `pollInterval` property to a required field:

**Example addition of a required field in a CRD**

```
versions:
- name: v1alpha2
  schema:
    openAPIV3Schema:
      properties:
        apiVersion:
          type: string
        kind:
          type: string
        metadata:
          type: object
        spec:
          type: object
        status:
          type: object
        pollInterval:
          type: string
      type: object
      required:
      - pollInterval
```

**Example error output**

```
validating upgrade for CRD "test.example.com" failed: CustomResourceDefinition test.example.com failed upgrade safety validation. "ChangeValidator" validation failed: version "v1alpha1", field "^": new required fields added: [pollInterval]
```

## [Legal Notice](#idm140529071897808) Copy linkLink copied to clipboard!

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
