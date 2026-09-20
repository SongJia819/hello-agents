---
title: "Building applications"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/index
retrieved_at: 2026-09-05T05:41:37.162692+00:00
---

# Building applications

---

OpenShift Container Platform 4.22

## Creating and managing applications on OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139966756849552)

**Abstract**

This document provides instructions for the various ways to create and manage instances of user-provisioned applications running on OpenShift Container Platform. This includes working with projects and provisioning applications using the Open Service Broker API.

---

## [Chapter 1. Building applications overview](#building-applications-overview) Copy linkLink copied to clipboard!

You can organize workloads into isolated projects and streamline your application lifecycle by using the web console or command-line interface (CLI) to create, manage, and deploy applications in OpenShift Container Platform.

### [1.1. Working on a project](#applications-projects-overview_building-applications-overview) Copy linkLink copied to clipboard!

Manage the complete lifecycle of isolated projects, from initial provisioning to user access control, to securely organize applications across your cluster.

After you create the project, you can grant or revoke access to a project and manage cluster roles for the users. You can also edit the project configuration resource while creating a project template that is used for automatic provisioning of new projects.

Using the CLI, you can create a project as a different user by impersonating a request to the OpenShift Container Platform API. When you make a request to create a new project, the OpenShift Container Platform uses an endpoint to provision the project according to a customizable template. As a cluster administrator, you can choose to prevent an authenticated user group from self-provisioning new projects.

### [1.2. Working on an application](#applications-application-lifecycle_building-applications-overview) Copy linkLink copied to clipboard!

Manage your complete application lifecycle by creating, maintaining, and deploying software by using the web console, CLI, or Operators to optimize cluster resources and minimize downtime.

Creating an application
:   To create applications, you must have created a project or have access to a project with the appropriate roles and permissions. You can create an application by using either installed Operators, or the OpenShift CLI (`oc`). You can source the applications to be added to the project from Git, JAR files, devfiles, or the developer catalog.

    You can also use components that include source or binary code, images, and templates to create an application by using the OpenShift CLI (`oc`). With the OpenShift Container Platform web console, you can create an application from an Operator installed by a cluster administrator.

Maintaining an application
:   After you create the application, you can use the web console to monitor your project or application metrics. You can also edit or delete the application using the web console.

    When the application is running, not all application resources are used. As a cluster administrator, you can choose to idle these scalable resources to reduce resource consumption.

Deploying an application
:   You can deploy your application using `Deployment` or `DeploymentConfig` objects and manage them from the web console. You can create deployment strategies that help reduce downtime during a change or an upgrade to the application.

    You can also use Helm, a software package manager that simplifies deployment of applications and services to OpenShift Container Platform clusters.

## [Chapter 2. Projects](#projects) Copy linkLink copied to clipboard!

### [2.1. Working with projects](#working-with-projects) Copy linkLink copied to clipboard!

A *project* allows a community of users to organize and manage their content in isolation from other communities.

Note

Projects starting with `openshift-` and `kube-` are default projects. For more information, see "Default projects". These projects host cluster components that run as pods and other infrastructure components. As such, OpenShift Container Platform does not allow you to create projects starting with `openshift-` or `kube-` using the `oc new-project` command. Cluster administrators can create these projects using the `oc adm new-project` command.

Important

Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components.

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects.

You can complete the following tasks on either the OpenShift Container Platform web console or the OpenShift CLI (`oc`):

* Create a project in your cluster.
* View a project.
* Check the status of a project.
* Delete a project.

Important

When you delete a project, the server updates the project status to **Terminating** from **Active**. The server then clears all content from a project that is in the **Terminating** state before finally removing the project. While a project is in **Terminating** status, you cannot add new content to the project.

#### [2.1.1. Creating a project by using the web console](#creating-a-project-using-the-web-console_projects) Copy linkLink copied to clipboard!

You can use the OpenShift Container Platform web console to create a project in your cluster.

Note

Projects starting with `openshift-` and `kube-` are considered critical by OpenShift Container Platform. As such, OpenShift Container Platform does not allow you to create projects starting with `openshift-` using the web console.

**Prerequisites**

* You have the appropriate roles and permissions to create projects, applications, and other workloads in OpenShift Container Platform.

**Procedure**

* If you are using the **Administrator** perspective:

  1. Navigate to **Home** → **Projects**.
  2. Click **Create Project**:

     1. In the **Create Project** dialog box, enter a unique name, such as `myproject`, in the **Name** field.
     2. Optional: Add the **Display name** and **Description** details for the project.
     3. Click **Create**.

        The dashboard for your project is displayed.
  3. Optional: Select the **Details** tab to view the project details.
  4. Optional: If you have adequate permissions for a project, you can use the **Project Access** tab to provide or revoke `admin`, `edit`, and `view` privileges for the project.
* If you are using the **Developer** perspective:

  1. Click the **Project** menu and select **Create Project**:

     **Figure 2.1. Create project**

     1. In the **Create Project** dialog box, enter a unique name, such as `myproject`, in the **Name** field.
     2. Optional: Add the **Display name** and **Description** details for the project.
     3. Click **Create**.
  2. Optional: Use the left navigation panel to navigate to the **Project** view and see the dashboard for your project.
  3. Optional: In the project dashboard, select the **Details** tab to view the project details.
  4. Optional: If you have adequate permissions for a project, you can use the **Project Access** tab of the project dashboard to provide or revoke admin, edit, and view privileges for the project.

**Additional resources**

* [Customizing the available cluster roles using the web console](#odc-customizing-available-cluster-roles-using-the-web-console_projects "2.1.6. Customizing the available cluster roles using the web console")

#### [2.1.2. Creating a project by using the CLI](#creating-a-project-using-the-CLI_projects) Copy linkLink copied to clipboard!

If your cluster administrator has provided you with the required permissions, you can create a new project.

Note

Projects starting with `openshift-` and `kube-` are considered critical by OpenShift Container Platform. OpenShift Container Platform does not allow you to create projects that start with `openshift-` or `kube-` by using the `oc new-project` command. Cluster administrators can create these projects by using the `oc adm new-project` command.

**Procedure**

* To create a project, enter the following command:

  ```
  $ oc new-project <project_name> \
      --description="<description>" --display-name="<display_name>"
  ```

  The following example uses actual values:

  ```
  $ oc new-project hello-openshift \
      --description="This is an example project" \
      --display-name="Hello OpenShift"
  ```

  Note

  The number of projects that you can create might be limited by the system administrator. After your limit is reached, you might have to delete an existing project to create a new one.

#### [2.1.3. Viewing a project by using the web console](#viewing-a-project-using-the-web-console_projects) Copy linkLink copied to clipboard!

You can view the projects that you have access to by using the OpenShift Container Platform web console.

Important

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. The **Developer** perspective is no longer enabled by default.

All users can interact with all OpenShift Container Platform web console features. However, if you are not the cluster owner, you might need to request permission to access certain features from the cluster owner.

You can still enable the **Developer** perspective. On the **Getting Started** pane in the web console, you can take a tour of the console, find information on setting up your cluster, view a quick start for enabling the **Developer** perspective, and follow links to explore new features and capabilities.

See also, "Enabling the **Developer** perspective in the web console".

**Procedure**

* If you are logged in as an administrator, complete the following steps:

  1. Navigate to **Home** → **Projects** in the navigation menu.
  2. Select a project to view. The **Overview** tab includes a dashboard for your project.
  3. Select the **Details** tab to view the project details.
  4. Select the **YAML** tab to view and update the YAML configuration for the project resource.
  5. Select the **Workloads** tab to see workloads in the project.
  6. Select the **RoleBindings** tab to view and create role bindings for your project.
* If you are logged in as a developer, complete the following steps:

  1. Navigate to the **Project** page in the navigation menu.
  2. Select **All Projects** from the **Project** drop-down menu at the top of the screen to list all of the projects in your cluster.
  3. Select a project to view.
  4. Select the **Details** tab to view the project details.
  5. If you have adequate permissions for a project, select the **Project access** tab to view and update the privileges for the project.

#### [2.1.4. Viewing a project using the CLI](#viewing-a-project-using-the-CLI_projects) Copy linkLink copied to clipboard!

When viewing projects, you are restricted to seeing only the projects you have access to view based on the authorization policy.

**Procedure**

1. To view a list of projects, enter the following command:

   ```
   $ oc get projects
   ```
2. To change from the current project to a different project for CLI operations, enter the following command. The specified project is then used in all subsequent operations that manipulate project-scoped content.

   ```
   $ oc project <project_name>
   ```

#### [2.1.5. Providing access permissions to your project using the Developer perspective](#odc-providing-project-permissions-using-developer-perspective_projects) Copy linkLink copied to clipboard!

You can use the **Project** view in the **Developer** perspective to grant or revoke access permissions to your project. You can add users to your project and provide them with **Admin**, **Edit**, or **View** access.

**Prerequisites**

* You have created a project.

**Procedure**

1. In the **Developer** perspective, navigate to the **Project** page.
2. Select your project from the **Project** menu.
3. Select the **Project Access** tab.
4. Click **Add access** to add a new row of permissions to the default ones.

   **Figure 2.2. Project permissions**
5. Enter the user name, click the **Select a role** drop-down list, and select an appropriate role.
6. Click **Save** to add the new permissions.
7. Optional: You can complete any of the following additional tasks:

   * The **Select a role** drop-down list, to modify the access permissions of an existing user.
   * The **Remove Access** icon, to completely remove the access permissions of an existing user to the project.

     Note

     Advanced role-based access control is managed in the **Roles** and **Roles Binding** views in the **Administrator** perspective.

#### [2.1.6. Customizing the available cluster roles using the web console](#odc-customizing-available-cluster-roles-using-the-web-console_projects) Copy linkLink copied to clipboard!

In the **Developer** perspective of the web console, the **Project** → **Project access** page enables a project administrator to grant roles to users in a project. By default, the available cluster roles that can be granted to users in a project are `admin`, `edit`, and `view`.

As a cluster administrator, you can define which cluster roles are available in the **Project access** page for all projects cluster-wide. You can specify the available roles by customizing the `spec.customization.projectAccess.availableClusterRoles` object in the `Console` configuration resource.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. In the **Administrator** perspective, navigate to **Administration** → **Cluster settings**.
2. Click the **Configuration** tab.
3. From the **Configuration resource** list, select **Console `operator.openshift.io`**.
4. Navigate to the **YAML** tab to view and edit the YAML code.
5. In the YAML code under `spec`, customize the list of available cluster roles for project access. The following example specifies the default `admin`, `edit`, and `view` roles:

   ```
   apiVersion: operator.openshift.io/v1
   kind: Console
   metadata:
     name: cluster
   # ...
   spec:
     customization:
       projectAccess:
         availableClusterRoles:
         - admin
         - edit
         - view
   ```
6. Click **Save** to save the changes to the `Console` configuration resource.

**Verification**

1. In the **Developer** perspective, navigate to the **Project** page.
2. Select a project from the **Project** menu.
3. Select the **Project access** tab.
4. Click the menu in the **Role** column and verify that the available roles match the configuration that you applied to the `Console` resource configuration.

#### [2.1.7. Adding to a project](#adding-to-a-project_projects) Copy linkLink copied to clipboard!

You can add items to your project by using the **+Add** page.

**Prerequisites**

* You have created a project.

**Procedure**

1. Navigate to the **+Add** page.
2. Select your project from the **Project** menu.
3. Click an item on the **+Add** page and then follow the workflow.

   Note

   You can also use the search feature in the **+Add** page to find additional items to add to your project. Click **+** under **Add** at the top of the page and type the name of a component in the search field.

#### [2.1.8. Checking project status by using the web console](#checking-project-status-using-the-web-console_projects) Copy linkLink copied to clipboard!

You can review the status of your project by using the web console.

**Prerequisites**

* You have created a project.

**Procedure**

1. Navigate to **Home** → **Projects**.
2. Select a project from the list.
3. Review the project status in the **Overview** page.

#### [2.1.9. Checking project status by using the CLI](#checking-project-status-using-the-CLI_projects) Copy linkLink copied to clipboard!

You can review the status of your project by using the OpenShift CLI (`oc`).

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have created a project.

**Procedure**

1. Switch to your project:

   ```
   $ oc project <project_name>
   ```

   * Replace `<project_name>` with the name of your project.
2. Obtain a high-level overview of the project:

   ```
   $ oc status
   ```

#### [2.1.10. Deleting a project by using the web console](#deleting-a-project-using-the-web-console_projects) Copy linkLink copied to clipboard!

You can delete a project by using the web console.

**Prerequisites**

* You have created a project.
* You have the required permissions to delete the project.

**Procedure**

* If you are using the **Administrator** perspective, complete the following steps:

  1. Navigate to **Home** → **Projects**.
  2. Select a project from the list.
  3. Click the **Actions** drop-down menu for the project and select **Delete Project**.

     Note

     The **Delete Project** option is not available if you do not have the required permissions to delete the project.
  4. In the **Delete Project?** pane, confirm the deletion by entering the name of your project.
  5. Click **Delete**.
* If you are using the **Developer** perspective, complete the following steps:

  1. Navigate to the **Project** page.
  2. Select the project that you want to delete from the **Project** menu.
  3. Click the **Actions** drop-down menu for the project and select **Delete Project**.

     Note

     If you do not have the required permissions to delete the project, the **Delete Project** option is not available.
  4. In the **Delete Project?** pane, confirm the deletion by entering the name of your project.
  5. Click **Delete**.

#### [2.1.11. Deleting a project by using the CLI](#deleting-a-project-using-the-CLI_projects) Copy linkLink copied to clipboard!

You can delete a project by using the OpenShift CLI (`oc`).

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have created a project.
* You have the required permissions to delete the project.

**Procedure**

* Delete your project by entering the following command:

  ```
  $ oc delete project <project_name>
  ```

  + Replace `<project_name>` with the name of the project that you want to delete.

### [2.2. Creating a project as another user](#creating-project-other-user) Copy linkLink copied to clipboard!

You can use impersonation to create a project on behalf of a different user account.

#### [2.2.1. API impersonation](#authentication-api-impersonation_creating-project-other-user) Copy linkLink copied to clipboard!

You can configure API requests in OpenShift Container Platform to act as another user. Impersonation allows you to perform actions on behalf of another account without switching credentials.

#### [2.2.2. Impersonating a user when you create a project](#impersonation-project-creation_creating-project-other-user) Copy linkLink copied to clipboard!

You can impersonate a different user when you create a project request. Because `system:authenticated:oauth` is the only bootstrap group that can create project requests, you must impersonate that group.

**Procedure**

* To create a project request on behalf of a different user:

  ```
  $ oc new-project <project> --as=<user> \
      --as-group=system:authenticated --as-group=system:authenticated:oauth
  ```

### [2.3. Configuring project creation](#configuring-project-creation) Copy linkLink copied to clipboard!

As a cluster administrator, you can allow and configure how developers and service accounts can create, or *self-provision*, their own projects.

In OpenShift Container Platform, *projects* are used to group and isolate related objects. When you request to create a new project by using the web console or `oc new-project` command, an endpoint in OpenShift Container Platform provisions the project according to a template. You can customize this template to meet your needs.

#### [2.3.1. About project creation](#about-project-creation_configuring-project-creation) Copy linkLink copied to clipboard!

When you request a new project, the OpenShift Container Platform API server automatically provisions the new project based on the project template. The project template is identified by the `projectRequestTemplate` parameter in the project configuration resource of the cluster.

If the parameter is not defined, the API server creates a default template that creates a project with the requested name. The API server then assigns the requesting user to the `admin` role for that project.

When a project request is submitted, the API substitutes the following parameters into the template:

Expand

Table 2.1. Default project template parameters

| Parameter | Description |
| --- | --- |
| `PROJECT_NAME` | The name of the project. Required. |
| `PROJECT_DISPLAYNAME` | The display name of the project. Might be empty. |
| `PROJECT_DESCRIPTION` | The description of the project. Might be empty. |
| `PROJECT_ADMIN_USER` | The user name of the administrating user. |
| `PROJECT_REQUESTING_USER` | The user name of the requesting user. |

Show more

Access to the API is granted to developers with the `self-provisioner` role and the `self-provisioners` cluster role binding. This role is available to all authenticated developers by default.

#### [2.3.2. Modifying the template for new projects](#modifying-template-for-new-projects_configuring-project-creation) Copy linkLink copied to clipboard!

To modify the default project template to customize the resources and settings applied when users create new projects, you can create a custom project template.

As a cluster administrator, you can modify the default project template so that new projects are created using your custom requirements.

To create your own custom project template:

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

**Procedure**

1. Log in as a user with `cluster-admin` privileges.
2. Generate the default project template:

   ```
   $ oc adm create-bootstrap-project-template -o yaml > template.yaml
   ```
3. Use a text editor to modify the generated `template.yaml` file by adding objects or modifying existing objects.
4. The project template must be created in the `openshift-config` namespace. Load your modified template:

   ```
   $ oc create -f template.yaml -n openshift-config
   ```
5. Edit the project configuration resource using the web console or CLI.

   * Using the web console, complete the following tasks:

     1. Navigate to the **Administration** → **Cluster Settings** page.
     2. Click **Configuration** to view all configuration resources.
     3. Find the entry for **Project** and click **Edit YAML**.
   * Using the CLI, complete the following tasks:

     1. Edit the `project.config.openshift.io/cluster` resource:

        ```
        $ oc edit project.config.openshift.io/cluster
        ```
6. Update the `spec` section to include the `projectRequestTemplate` and `name` parameters. Ensure you set the name of your uploaded project template. The default name is `project-request`.

   **Project configuration resource with custom project template**

   ```
   apiVersion: config.openshift.io/v1
   kind: Project
   metadata:
   # ...
   spec:
     projectRequestTemplate:
       name: <template_name>
   # ...
   ```
7. After you save your changes, create a new project to verify that your changes were successfully applied.

#### [2.3.3. Disabling project self-provisioning](#disabling-project-self-provisioning_configuring-project-creation) Copy linkLink copied to clipboard!

You can prevent an authenticated user group from self-provisioning new projects.

**Procedure**

1. Log in as a user with `cluster-admin` privileges.
2. View the `self-provisioners` cluster role binding usage by running the following command:

   ```
   $ oc describe clusterrolebinding.rbac self-provisioners
   ```

   **Example output**

   ```
   Name:		self-provisioners
   Labels:		<none>
   Annotations:	rbac.authorization.kubernetes.io/autoupdate=true
   Role:
     Kind:	ClusterRole
     Name:	self-provisioner
   Subjects:
     Kind	Name				Namespace
     ----	----				---------
     Group	system:authenticated:oauth
   ```

   Review the subjects in the `self-provisioners` section.
3. Remove the `self-provisioner` cluster role from the group `system:authenticated:oauth`.

   * If the `self-provisioners` cluster role binding binds only the `self-provisioner` role to the `system:authenticated:oauth` group, run the following command:

     ```
     $ oc patch clusterrolebinding.rbac self-provisioners -p '{"subjects": null}'
     ```
   * If the `self-provisioners` cluster role binding binds the `self-provisioner` role to more users, groups, or service accounts than the `system:authenticated:oauth` group, run the following command:

     ```
     $ oc adm policy \
         remove-cluster-role-from-group self-provisioner \
         system:authenticated:oauth
     ```
4. Edit the `self-provisioners` cluster role binding to prevent automatic updates to the role. Automatic updates reset the cluster roles to the default state.

   * To update the role binding by using the CLI, complete the following steps:

     1. To edit the `self-provisioners` cluster role binding, enter the following command:

        ```
        $ oc edit clusterrolebinding.rbac self-provisioners
        ```
     2. In the displayed role binding, set the `rbac.authorization.kubernetes.io/autoupdate` parameter value to `false`, as shown in the following example:

        ```
        apiVersion: authorization.openshift.io/v1
        kind: ClusterRoleBinding
        metadata:
          annotations:
            rbac.authorization.kubernetes.io/autoupdate: "false"
        # ...
        ```
   * To update the role binding, run the following single command:

     ```
     $ oc patch clusterrolebinding.rbac self-provisioners -p '{ "metadata": { "annotations": { "rbac.authorization.kubernetes.io/autoupdate": "false" } } }'
     ```
5. Log in as an authenticated user and verify that the user can no longer self-provision a project:

   ```
   $ oc new-project test
   ```

   **Example output**

   ```
   Error from server (Forbidden): You may not request a new project via this API.
   ```

   Consider customizing this project request message to provide more helpful instructions specific to your organization.

#### [2.3.4. Customizing the project request message](#customizing-project-request-message_configuring-project-creation) Copy linkLink copied to clipboard!

A developer or a service account that is unable to self-provision projects can make a project creation request by using the web console or CLI.

The following error message is returned by default:

```
You may not request a new project via this API.
```

Cluster administrators can customize this message. Consider updating the message to provide further instructions on how to request a new project specific to your organization. The following examples show a customized message:

* To request a project, contact your system administrator at `projectname@example.com`.
* To request a new project, fill out the project request form located at `https://internal.example.com/openshift-project-request`.

**Procedure**

1. Edit the project configuration resource using the web console or CLI.

   * By using the web console, complete the following steps:

     1. Navigate to the **Administration** → **Cluster Settings** page.
     2. Click **Configuration** to view all configuration resources.
     3. Find the entry for **Project** and click **Edit YAML**.
   * By using the CLI, complete the following steps:

     1. Log in as a user with `cluster-admin` privileges.
     2. Edit the `project.config.openshift.io/cluster` resource:

        ```
        $ oc edit project.config.openshift.io/cluster
        ```
2. Update the `spec` section to include the `projectRequestMessage` parameter and set the value to your custom message:

   **Project configuration resource with custom project request message**

   ```
   apiVersion: config.openshift.io/v1
   kind: Project
   metadata:
   # ...
   spec:
     projectRequestMessage: <message_string>
   # ...
   ```

   The following example uses actual values:

   ```
   apiVersion: config.openshift.io/v1
   kind: Project
   metadata:
   # ...
   spec:
     projectRequestMessage: To request a project, contact your system administrator at projectname@example.com.
   # ...
   ```
3. After saving your changes, attempt to create a new project by using a developer or service account that cannot self-provision projects. By doing this task, you can verify that your changes were successfully applied.

## [Chapter 3. Creating applications](#creating-applications) Copy linkLink copied to clipboard!

### [3.1. Using templates](#using-templates) Copy linkLink copied to clipboard!

You can use templates to deploy preconfigured applications and create reusable object definitions on your OpenShift Container Platform cluster. Upload, instantiate, and author templates from the web console or CLI to speed up application creation.

#### [3.1.1. Understanding templates](#templates-overview_using-templates) Copy linkLink copied to clipboard!

You can use templates to describe reusable, parameterized object sets that OpenShift Container Platform processes into resources such as `Service` and `DeploymentConfig` objects. Templates help you deploy the same application structure consistently from the web console or CLI.

A template can be processed to create anything you have permission to create within a project. A template can also define a set of labels to apply to every object defined in the template.

#### [3.1.2. Uploading a template](#templates-uploading_using-templates) Copy linkLink copied to clipboard!

To add a template to your OpenShift Container Platform project, upload a JSON or YAML template file with the CLI. Uploaded templates are saved to the project template library for reuse by users with access to that project.

**Procedure**

* Upload a template using one of the following methods:

  + Upload a JSON or YAML template file to the template library of your current project by running the following command:

    ```
    $ oc create -f <filename>
    ```
  + Upload a template to a different project using the `-n` option with the name of the project by running the following command:

    ```
    $ oc create -f <filename> -n <project>
    ```

    The template is now available for selection using the web console or the CLI.

#### [3.1.3. Creating an application by using the web console](#templates-creating-from-console_using-templates) Copy linkLink copied to clipboard!

To create an application from a template on your OpenShift Container Platform cluster, use the web console **Developer Catalog**. Select a template or builder image and configure the generated objects before you deploy.

**Procedure**

1. Navigate to your project and click **+Add**.
2. Click **All services** in the **Developer Catalog** tile.
3. Click **Builder Images** under **Type** to see the available builder images.

   Note

   Only image stream tags that have the `builder` tag listed in their annotations appear in this list, as demonstrated in the following example. Include `builder` in the `tags` annotation so the image stream tag appears in the web console as a builder.

   ```
   kind: "ImageStream"
   apiVersion: "image.openshift.io/v1"
   metadata:
     name: "ruby"
     creationTimestamp: null
   spec:
   # ...
     tags:
       - name: "2.6"
         annotations:
           description: "Build and run Ruby 2.6 applications"
           iconClass: "icon-ruby"
           tags: "builder,ruby"
           supports: "ruby:2.6,ruby"
           version: "2.6"
   # ...
   ```
4. Modify the settings in the new application screen to configure the objects to support your application.

#### [3.1.4. Creating objects from templates by using the CLI](#templates-using-the-cli_using-templates) Copy linkLink copied to clipboard!

You can use the CLI to create objects from templates on your OpenShift Container Platform cluster by processing a template into a list of objects in your project. Use CLI commands to manage template labels, parameters, and generated object lists.

##### [3.1.4.1. Adding labels](#templates-cli-labels_using-templates) Copy linkLink copied to clipboard!

To add labels when you process a template on your OpenShift Container Platform cluster, pass label selectors to the `oc process` command. The labels specified in the template are applied to every object that is generated from the template.

Labels are used to manage and organize generated objects, such as pods.

**Procedure**

* Add labels in the template by running the following command:

  ```
  $ oc process -f <filename> -l name=otherLabel
  ```

##### [3.1.4.2. Listing parameters](#templates-cli-parameters_using-templates) Copy linkLink copied to clipboard!

You can list template parameters on your OpenShift Container Platform cluster to see which values you can override before processing a template. Use the `oc process --parameters` command with a template file or uploaded template name.

**Procedure**

* List template parameters from a local template file by running the following command:

  ```
  $ oc process --parameters -f <filename>
  ```
* List template parameters from an uploaded template by running the following command:

  ```
  $ oc process --parameters -n <project> <template_name>
  ```

  For example, to list parameters for the `rails-postgresql-example` quick start template in the default `openshift` project, run the following command:

  ```
  $ oc process --parameters -n openshift rails-postgresql-example
  ```

  **Example output**

  ```
  NAME                         DESCRIPTION                                                                                              GENERATOR           VALUE
  SOURCE_REPOSITORY_URL        The URL of the repository with your application source code                                                                  https://github.com/sclorg/rails-ex.git
  SOURCE_REPOSITORY_REF        Set this to a branch name, tag or other ref of your repository if you are not using the default branch
  CONTEXT_DIR                  Set this to the relative path to your project if it is not in the root of your repository
  APPLICATION_DOMAIN           The exposed hostname that will route to the Rails service                                                                    rails-postgresql-example.openshiftapps.com
  GITHUB_WEBHOOK_SECRET        A secret string used to configure the GitHub webhook                                                     expression          [a-zA-Z0-9]{40}
  SECRET_KEY_BASE              Your secret key for verifying the integrity of signed cookies                                            expression          [a-z0-9]{127}
  APPLICATION_USER             The application user that is used within the sample application to authorize access on pages                                 openshift
  APPLICATION_PASSWORD         The application password that is used within the sample application to authorize access on pages                             secret
  DATABASE_SERVICE_NAME        Database service name                                                                                                        postgresql
  POSTGRESQL_USER              database username                                                                                        expression          user[A-Z0-9]{3}
  POSTGRESQL_PASSWORD          database password                                                                                        expression          [a-zA-Z0-9]{8}
  POSTGRESQL_DATABASE          database name                                                                                                                root
  POSTGRESQL_MAX_CONNECTIONS   database max connections                                                                                                     10
  POSTGRESQL_SHARED_BUFFERS    database shared buffers                                                                                                      12MB
  ```

  The output identifies several parameters that are generated with a regular expression-like generator when the template is processed.

##### [3.1.4.3. Generating a list of objects](#templates-cli-generating-list-of-objects_using-templates) Copy linkLink copied to clipboard!

To preview objects a template creates on your OpenShift Container Platform cluster, run `oc process` on the template without applying it. Review the generated object list and save it to a file before you create resources in your project.

**Procedure**

* Process a file defining a template to return the list of objects to standard output by running the following command:

  ```
  $ oc process -f <filename>
  ```
* Process an uploaded template in the current project to return the list of objects to standard output by running the following command:

  ```
  $ oc process <template_name>
  ```
* Create objects from a template by processing the template and piping the output to `oc create` by running the following command:

  ```
  $ oc process -f <filename> | oc create -f -
  ```
* Create objects from an uploaded template in the current project by processing the template and piping the output to `oc create` by running the following command:

  ```
  $ oc process <template> | oc create -f -
  ```
* You can override any parameter values defined in the file by adding the `-p` option for each `<name>=<value>` pair you want to override. A parameter reference appears in any text field inside the template items.

  For example, in the following the `POSTGRESQL_USER` and `POSTGRESQL_DATABASE` parameters of a template are overridden to output a configuration with customized environment variables:

  + Create a list of objects from a template by running the following command:

    ```
    $ oc process -f my-rails-postgresql \
        -p POSTGRESQL_USER=bob \
        -p POSTGRESQL_DATABASE=mydatabase
    ```
  + Create the objects from the processed output by running the following command:

    ```
    $ oc process -f my-rails-postgresql \
        -p POSTGRESQL_USER=bob \
        -p POSTGRESQL_DATABASE=mydatabase \
        | oc create -f -
    ```

    Note

    You can redirect the JSON output to a file, or apply it directly without uploading the template by piping it to the `oc create` command.
  + If you have a large number of parameters, you can store them in a file and then pass this file to `oc process` by running the following commands:

    ```
    $ cat postgres.env
    ```

    ```
    $ oc process -f my-rails-postgresql --param-file=postgres.env
    ```

    **Example output**

    ```
    POSTGRESQL_USER=bob
    POSTGRESQL_DATABASE=mydatabase
    ```
  + You can also read parameter values from standard input by specifying "-" as the value of the `--param-file` option by running the following command:

    ```
    $ sed s/bob/alice/ postgres.env | oc process -f my-rails-postgresql --param-file=-
    ```

#### [3.1.5. Modifying uploaded templates](#templates-modifying-uploaded-template_using-templates) Copy linkLink copied to clipboard!

To update a template already stored in your OpenShift Container Platform project, edit the template object and replace the existing version. Updated templates remain available in the project template library for reuse.

**Procedure**

* Modify a template that has already been uploaded by running the following command:

  ```
  $ oc edit template <template>
  ```

#### [3.1.6. Using instant app and quick start templates](#templates-using-instant-app-quickstart_using-templates) Copy linkLink copied to clipboard!

To try a sample application from an instant-app template on your OpenShift Container Platform cluster, create the application from the template and optionally fork the source repository of the template. Customize the build configuration to test changes and rebuild the application.

OpenShift Container Platform provides several default instant app and quick start templates to help you get started quickly creating a new application for different languages. Templates are provided for Rails (Ruby), Django (Python), Node.js, CakePHP (PHP), and Dancer (Perl). Your cluster administrator must create these templates in the default, global `openshift` project so you have access to them.

By default, the templates build using a public source repository on GitHub that contains the necessary application code.

**Procedure**

1. List the available default instant app and quick start templates by running the following command:

   ```
   $ oc get templates -n openshift
   ```
2. Modify the source to build your own version of the application:

   1. Fork the repository referenced by the default `SOURCE_REPOSITORY_URL` parameter of the template.
   2. Override the value of the `SOURCE_REPOSITORY_URL` parameter when creating from the template, specifying your fork instead of the default value.

      By doing this, the build configuration created by the template now points to your fork of the application code. You can then modify the code and rebuild the application as needed.

      Note

      Some of the instant app and quick start templates define a database `DeploymentConfig` object. The configuration they define uses ephemeral storage for the database content. These templates should be used for demonstration purposes only as all database data is lost if the database pod restarts for any reason.

##### [3.1.6.1. Quick start templates](#templates-quickstart_using-templates) Copy linkLink copied to clipboard!

To browse sample instant app and quick start templates on your OpenShift Container Platform cluster, review the default templates in the `openshift` project. Use these templates to deploy example applications for common languages and frameworks.

A quick start template is a basic example of an application running on OpenShift Container Platform. Quick starts come in a variety of languages and frameworks, and are defined in a template, which is constructed from a set of `Service`, `BuildConfig`, and `DeploymentConfig` objects. This template references the necessary images and source repositories to build and deploy the application.

Your administrator must have already installed these templates in your OpenShift Container Platform cluster, in which case you can select it from the web console.

Quick starts refer to a source repository that contains the application source code. To customize the quick start, fork the repository and, when creating an application from the template, substitute the default source repository name with your forked repository. This results in builds that are performed using your source code instead of the provided example source. You can then update the code in your source repository and launch a new build to see the changes reflected in the deployed application.

##### [3.1.6.1.1. Web framework quick start templates](#templates-quickstart-web-framework_using-templates) Copy linkLink copied to clipboard!

These quick start templates provide a basic application of the indicated framework and language:

* CakePHP: a PHP web framework that includes a MySQL database
* Dancer: a Perl web framework that includes a MySQL database
* Django: a Python web framework that includes a PostgreSQL database
* NodeJS: a NodeJS web application that includes a MongoDB database
* Rails: a Ruby web framework that includes a PostgreSQL database

#### [3.1.7. Writing templates](#templates-writing_using-templates) Copy linkLink copied to clipboard!

To define reusable application templates on your OpenShift Container Platform cluster, create a `Template` object that lists the resources to deploy and metadata that guides their creation.

Use the following sample YAML to review the structure before you author your own template.

```
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: redis-template
  annotations:
    description: "Description"
    iconClass: "icon-redis"
    tags: "database,nosql"
objects:
- apiVersion: v1
  kind: Pod
  metadata:
    name: redis-master
  spec:
    containers:
    - env:
      - name: REDIS_PASSWORD
        value: ${REDIS_PASSWORD}
      image: dockerfile/redis
      name: master
      ports:
      - containerPort: 6379
        protocol: TCP
parameters:
- description: Password used for Redis authentication
  from: '[A-Z0-9]{8}'
  generate: expression
  name: REDIS_PASSWORD
labels:
  redis: master
```

##### [3.1.7.1. Writing the template description](#templates-writing-description_using-templates) Copy linkLink copied to clipboard!

To help users find and understand your template in the web console, add description metadata such as display name, tags, and icon class. Use the annotations in this reference to document purpose, caveats, and support links.

The following is an example of template description metadata:

```
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: cakephp-mysql-example
  annotations:
    openshift.io/display-name: "CakePHP MySQL Example (Ephemeral)"
    description: >-
      An example CakePHP application with a MySQL database. For more information
      about using this template, including OpenShift considerations, see
      https://github.com/sclorg/cakephp-ex/blob/master/README.md.

      WARNING: Any data stored will be lost upon pod destruction. Only use this
      template for testing."
    openshift.io/long-description: >-
      This template defines resources needed to develop a CakePHP application,
      including a build configuration, application DeploymentConfig, and
      database DeploymentConfig.  The database is stored in
      non-persistent storage, so this configuration should be used for
      experimental purposes only.
    tags: "quickstart,php,cakephp"
    iconClass: icon-php
    openshift.io/provider-display-name: "Red Hat, Inc."
    openshift.io/documentation-url: "https://github.com/sclorg/cakephp-ex"
    openshift.io/support-url: "https://access.redhat.com"
message: "Your admin credentials are ${ADMIN_USERNAME}:${ADMIN_PASSWORD}"
```

where:

`metadata.name`
:   Specifies the unique name of the template.

`metadata.annotations.openshift.io/display-name`
:   Specifies a brief, user-friendly name, which can be employed by user interfaces.

`metadata.annotations.description`
:   Specifies a description of the template. Include enough detail that users understand what is being deployed and any caveats they must know before deploying. It should also provide links to additional information, such as a README file. You can include line breaks to create paragraphs.

`metadata.annotations.openshift.io/long-description`
:   Specifies an additional template description. This might be displayed by the service catalog.

`metadata.annotations.tags`
:   Specifies the tags to be associated with the template for searching and grouping. Add tags that group the template into one of the provided catalog categories. Refer to the `id` and `categoryAliases` in `CATALOG_CATEGORIES` in the console constants file. The categories can also be customized for the whole cluster.

`metadata.annotations.iconClass`
:   Specifies an icon to be displayed with your template in the web console.

    The following is a list of available icons.

* `icon-3scale`
* `icon-aerogear`
* `icon-amq`
* `icon-angularjs`
* `icon-ansible`
* `icon-apache`
* `icon-beaker`
* `icon-camel`
* `icon-capedwarf`
* `icon-cassandra`
* `icon-catalog-icon`
* `icon-clojure`
* `icon-codeigniter`
* `icon-cordova`
* `icon-datagrid`
* `icon-datavirt`
* `icon-debian`
* `icon-decisionserver`
* `icon-django`
* `icon-dotnet`
* `icon-drupal`
* `icon-eap`
* `icon-elastic`
* `icon-erlang`
* `icon-fedora`
* `icon-freebsd`
* `icon-git`
* `icon-github`
* `icon-gitlab`
* `icon-glassfish`
* `icon-go-gopher`
* `icon-golang`
* `icon-grails`
* `icon-hadoop`
* `icon-haproxy`
* `icon-helm`
* `icon-infinispan`
* `icon-jboss`
* `icon-jenkins`
* `icon-jetty`
* `icon-joomla`
* `icon-jruby`
* `icon-js`
* `icon-knative`
* `icon-kubevirt`
* `icon-laravel`
* `icon-load-balancer`
* `icon-mariadb`
* `icon-mediawiki`
* `icon-memcached`
* `icon-mongodb`
* `icon-mssql`
* `icon-mysql-database`
* `icon-nginx`
* `icon-nodejs`
* `icon-openjdk`
* `icon-openliberty`
* `icon-openshift`
* `icon-openstack`
* `icon-other-linux`
* `icon-other-unknown`
* `icon-perl`
* `icon-phalcon`
* `icon-php`
* `icon-play`
* `iconpostgresql`
* `icon-processserver`
* `icon-python`
* `icon-quarkus`
* `icon-rabbitmq`
* `icon-rails`
* `icon-redhat`
* `icon-redis`
* `icon-rh-integration`
* `icon-rh-spring-boot`
* `icon-rh-tomcat`
* `icon-ruby`
* `icon-scala`
* `icon-serverlessfx`
* `icon-shadowman`
* `icon-spring-boot`
* `icon-spring`
* `icon-sso`
* `icon-stackoverflow`
* `icon-suse`
* `icon-symfony`
* `icon-tomcat`
* `icon-ubuntu`
* `icon-vertx`
* `icon-wildfly`
* `icon-windows`
* `icon-wordpress`
* `icon-xamarin`
* `icon-zend`

`metadata.annotations.openshift.io/provider-display-name`
:   Specifies the name of the person or organization providing the template.

`metadata.annotations.openshift.io/documentation-url`
:   Specifies a URL referencing further documentation for the template.

`metadata.annotations.openshift.io/support-url`
:   Specifies a URL where support can be obtained for the template.

`message`
:   Specifies an instructional message that is displayed when this template is instantiated. This field should inform the user how to use the newly created resources. Parameter substitution is performed on the message before being displayed so that generated credentials and other parameters can be included in the output. Include links to any next-steps documentation that users should follow.

##### [3.1.7.2. Writing template labels](#templates-writing-labels_using-templates) Copy linkLink copied to clipboard!

To label every object created from a template, add a `labels` section to the template definition. Use parameterized labels so users can identify and manage resources created from your template.

The following is an example of template object labels:

```
kind: "Template"
apiVersion: "v1"
...
labels:
  template: "cakephp-mysql-example"
  app: "${NAME}"
```

where:

`labels.template`
:   Specifies a label that is applied to all objects created from this template.

`labels.app`
:   Specifies a parameterized label that is also applied to all objects created from this template. Parameter expansion is carried out on both label keys and values.

##### [3.1.7.3. Writing template parameters](#templates-writing-parameters_using-templates) Copy linkLink copied to clipboard!

To customize a template when you process it, define parameters with default or generated values and reference them in template fields. Use string or JSON substitution syntax to pass user-specific values into created objects.

Parameters allow a value to be supplied by you or generated when you process the template. Then, that value is substituted wherever the parameter is referenced. References can be defined in any field in the objects list field. This is useful for generating random passwords or allowing you to supply a hostname or other user-specific value that is required to customize the template. Parameters can be referenced in two ways:

* As a string value by placing values in the form `${PARAMETER_NAME}` in any string field in the template.
* As a JSON or YAML value by placing values in the form `${{PARAMETER_NAME}}` in place of any field in the template.

When using the `${PARAMETER_NAME}` syntax, multiple parameter references can be combined in a single field and the reference can be embedded within fixed data, such as `"http://${PARAMETER_1}${PARAMETER_2}"`. Both parameter values are substituted and the resulting value is a quoted string.

When using the `${{PARAMETER_NAME}}` syntax, only a single parameter reference is allowed and leading and trailing characters are not permitted. The resulting value is unquoted unless, after substitution is performed, the result is not a valid JSON object. If the result is not a valid JSON value, the resulting value is quoted and treated as a standard string.

A single parameter can be referenced multiple times within a template and it can be referenced using both substitution syntaxes within a single template.

A default value can be provided, which is used if you do not supply a different value:

The following is an example of setting an explicit value as the default value:

```
parameters:
  - name: USERNAME
    description: "The user name for Joe"
    value: joe
```

Parameter values can also be generated based on rules specified in the parameter definition:

```
parameters:
  - name: PASSWORD
    description: "The random user password"
    generate: expression
    from: "[a-zA-Z0-9]{12}"
```

In the previous example, processing generates a random password 12 characters long consisting of all upper and lowercase alphabet letters and numbers.

The syntax available is not a full regular expression syntax. However, you can use `\w`, `\d`, `\a`, and `\A` modifiers:

* `[\w]{10}` produces 10 alphabet characters, numbers, and underscores. This follows the PCRE standard and is equal to `[a-zA-Z0-9_]{10}`.
* `[\d]{10}` produces 10 numbers. This is equal to `[0-9]{10}`.
* `[\a]{10}` produces 10 alphabetical characters. This is equal to `[a-zA-Z]{10}`.
* `[\A]{10}` produces 10 punctuation or symbol characters. This is equal to `` [~!@#$%\^&*()\-_+={}\[\]\\|<,>.?/"';:`]{10} ``.

Note

Depending on whether the template is written in YAML or JSON, you might need to escape the backslash with a second backslash. This also depends on the type of string in which the modifier is embedded. The following examples are equivalent:

**Example YAML template with a modifier**

```
  parameters:
  - name: singlequoted_example
    generate: expression
    from: '[\A]{10}'
  - name: doublequoted_example
    generate: expression
    from: "[\\A]{10}"
```

**Example JSON template with a modifier**

```
{
    "parameters": [
       {
        "name": "json_example",
        "generate": "expression",
        "from": "[\\A]{10}"
       }
    ]
}
```

Here is an example of a full template with parameter definitions and references:

```
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: my-template
objects:
  - kind: BuildConfig
    apiVersion: build.openshift.io/v1
    metadata:
      name: cakephp-mysql-example
      annotations:
        description: Defines how to build the application
    spec:
      source:
        type: Git
        git:
          uri: "${SOURCE_REPOSITORY_URL}"
          ref: "${SOURCE_REPOSITORY_REF}"
        contextDir: "${CONTEXT_DIR}"
  - kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: frontend
    spec:
      replicas: "${{REPLICA_COUNT}}"
parameters:
  - name: SOURCE_REPOSITORY_URL
    displayName: Source Repository URL
    description: The URL of the repository with your application source code
    value: https://github.com/sclorg/cakephp-ex.git
    required: true
  - name: GITHUB_WEBHOOK_SECRET
    description: A secret string used to configure the GitHub webhook
    generate: expression
    from: "[a-zA-Z0-9]{40}"
  - name: REPLICA_COUNT
    description: Number of replicas to run
    value: "2"
    required: true
message: "... The GitHub webhook secret is ${GITHUB_WEBHOOK_SECRET} ..."
```

where:

`spec.git.uri`
:   Specifies the value to be replaced with the value of the `SOURCE_REPOSITORY_URL` parameter when you process the template.

`spec.replicas`
:   Specifies the value to be replaced with the unquoted value of the `REPLICA_COUNT` parameter when you process the template.

`parameters.name`
:   Specifies the name of the parameter. This value is used to reference the parameter within the template.

`parameters.displayName`
:   Specifies the user-friendly name for the parameter. This is displayed to users.

`parameters.description`
:   Specifies a description of the parameter. Provide more detailed information for the purpose of the parameter, including any constraints on the expected value. Descriptions should use complete sentences to follow the console text standards. Do not make this a duplicate of the display name.

`parameters.value`
:   Specifies a default value for the parameter which is used if you do not override the value when you process the template. Avoid using default values for things like passwords, instead use generated parameters in combination with secrets.

`parameters.required`
:   Specifies that this parameter is required, meaning you cannot override it with an empty value. If the parameter does not provide a default or generated value, you must supply a value.

`parameters.generate`
:   Specifies that the parameter value is generated.

`parameters.from`
:   Specifies the input to the generator. In this case, the generator produces a 40 character alphanumeric value including upper and lowercase characters.

`message`
:   Specifies that parameters can be included in the template message. This field informs you about generated values.

##### [3.1.7.4. Writing the template object list](#templates-writing-object-list_using-templates) Copy linkLink copied to clipboard!

To specify what a template creates when processed, define an `objects` list with the API resources to deploy. Parameter values are substituted into each object definition before creation.

The following is an example of an object list:

```
kind: "Template"
apiVersion: "v1"
metadata:
  name: my-template
objects:
  - kind: "Service"
    apiVersion: "v1"
    metadata:
      name: "cakephp-mysql-example"
      annotations:
        description: "Exposes and load balances the application pods"
    spec:
      ports:
        - name: "web"
          port: 8080
          targetPort: 8080
      selector:
        name: "cakephp-mysql-example"
```

where:

`objects.kind`
:   Specifies the definition of a service, which is created by this template.

Note

If an object definition metadata includes a fixed `namespace` field value, the field is stripped out of the definition during template instantiation. If the `namespace` field contains a parameter reference, normal parameter substitution is performed, and the object is created in the resulting namespace. This requires that the user has permission to create objects in that namespace.

##### [3.1.7.5. Marking a template as bindable](#templates-marking-as-bindable_using-templates) Copy linkLink copied to clipboard!

To prevent end users from binding to services provisioned from your template, add the `template.openshift.io/bindable: "false"` annotation to the template object. By default, the Template Service Broker advertises each template service as bindable in the service catalog.

**Procedure**

* Prevent end users from binding against services provisioned from a given template by adding the annotation `template.openshift.io/bindable: "false"` to the template.

##### [3.1.7.6. Exposing template object fields](#templates-exposing-object-fields_using-templates) Copy linkLink copied to clipboard!

To return connection details when users bind to your template service, add `template.openshift.io/expose-` or `template.openshift.io/base64-expose-` annotations to `ConfigMap`, `Secret`, `Service`, or `Route` objects. Binding clients then receive the needed credentials and endpoints directly.

Each annotation key, with the prefix removed, is passed through to become a key in a `bind` response.

Each annotation value is a Kubernetes JSONPath expression, which is resolved at bind time to indicate the object field whose value should be returned in the `bind` response.

Note

Unless escaped with a backslash, the JSONPath implementation of Kubernetes interprets characters such as `.`, `@`, and others as metacharacters, regardless of their position in the expression. Therefore, for example, to refer to a `ConfigMap` data named `my.key`, the required JSONPath expression is `{.data['my\.key']}`. Depending on how the JSONPath expression is then written in YAML, an additional backslash might be required, for example `"{.data['my\\.key']}"`.

The following is an example of fields of different objects being exposed:

```
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: my-template
objects:
- kind: ConfigMap
  apiVersion: v1
  metadata:
    name: my-template-config
    annotations:
      template.openshift.io/expose-username: "{.data['my\\.username']}"
  data:
    my.username: foo
- kind: Secret
  apiVersion: v1
  metadata:
    name: my-template-config-secret
    annotations:
      template.openshift.io/base64-expose-password: "{.data['password']}"
  stringData:
    password: <password>
- kind: Service
  apiVersion: v1
  metadata:
    name: my-template-service
    annotations:
      template.openshift.io/expose-service_ip_port: "{.spec.clusterIP}:{.spec.ports[?(.name==\"web\")].port}"
  spec:
    ports:
    - name: "web"
      port: 8080
- kind: Route
  apiVersion: route.openshift.io/v1
  metadata:
    name: my-template-route
    annotations:
      template.openshift.io/expose-uri: "http://{.spec.host}{.spec.path}"
  spec:
    path: mypath
```

Note

`Bind` response key-value pairs can be used in other parts of the system as environment variables. Therefore, each annotation key, with the prefix removed, should be a valid environment variable name. Valid names begin with a character `A-Z`, `a-z`, or `_`, followed by zero or more characters `A-Z`, `a-z`, `0-9`, or `_`.

An example response to a `bind` operation given the previous partial template:

```
{
  "credentials": {
    "username": "foo",
    "password": "YmFy",
    "service_ip_port": "172.30.12.34:8080",
    "uri": "http://route-test.router.default.svc.cluster.local/mypath"
  }
}
```

**Procedure**

* Use the `template.openshift.io/expose-` annotation to return the field value as a string. This approach does not handle arbitrary binary data.
* If you want to return binary data, use the `template.openshift.io/base64-expose-` annotation instead to Base64 encode the data before it is returned.

##### [3.1.7.7. Waiting for template readiness](#templates-waiting-for-readiness_using-templates) Copy linkLink copied to clipboard!

To delay creating resources from a template until key resources are ready, add the `template.alpha.openshift.io/wait-for-ready: "true"` annotation to supported object kinds. The service catalog, Template Service Broker, and `TemplateInstance` API wait for annotated objects to report ready.

Before starting the procedure, read the following considerations:

* Set memory, CPU, and storage default sizes to ensure your application is given enough resources to run smoothly.
* Avoid referencing the `latest` tag from images if that tag is used across major versions. This can cause running applications to break when new images are pushed to that tag.
* A good template builds and deploys cleanly without requiring modifications after the template is deployed.

**Procedure**

* To use the template feature, mark one or more objects of kind `Build`, `BuildConfig`, `Deployment`, `DeploymentConfig`, `Job`, or `StatefulSet` in a template with the following annotation:

  ```
  "template.alpha.openshift.io/wait-for-ready": "true"
  ```

  Creating resources from the template is not complete until all objects marked with the annotation report ready. Similarly, if any of the annotated objects report failed, or if the template fails to become ready within a fixed timeout of one hour, creating resources from the template fails.

  When you create resources from a template, readiness and failure of each object kind are defined as follows:

  Expand

  | Kind | Readiness | Failure |
  | --- | --- | --- |
  | `Build` | Object reports phase complete. | Object reports phase canceled, error, or failed. |
  | `BuildConfig` | Latest associated build object reports phase complete. | Latest associated build object reports phase canceled, error, or failed. |
  | `Deployment` | Object reports new replica set and deployment available. This honors readiness probes defined on the object. | Object reports progressing condition as false. |
  | `DeploymentConfig` | Object reports new replication controller and deployment available. This honors readiness probes defined on the object. | Object reports progressing condition as false. |
  | `Job` | Object reports completion. | Object reports that one or more failures have occurred. |
  | `StatefulSet` | Object reports all replicas ready. This honors readiness probes defined on the object. | Not applicable. |

  Show more

  The following is an example template extract, which uses the `wait-for-ready` annotation. Further examples can be found in the OpenShift Container Platform quick start templates.

  ```
  kind: Template
  apiVersion: template.openshift.io/v1
  metadata:
    name: my-template
  objects:
  - kind: BuildConfig
    apiVersion: build.openshift.io/v1
    metadata:
      name: ...
      annotations:
        # wait-for-ready used on BuildConfig ensures that creating resources from the template
        # fails immediately if the build fails
        template.alpha.openshift.io/wait-for-ready: "true"
    spec:
      ...
  - kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: ...
      annotations:
        template.alpha.openshift.io/wait-for-ready: "true"
    spec:
      ...
  - kind: Service
    apiVersion: v1
    metadata:
      name: ...
    spec:
      ...
  ```

##### [3.1.7.8. Creating a template from existing objects](#templates-create-from-existing-object_using-templates) Copy linkLink copied to clipboard!

To create a template from existing objects in your project, export those objects and add parameters and other template customizations. Reusing deployed resources helps you capture a working configuration that others can deploy consistently from the template.

**Procedure**

* Export objects in a project by running the following command:

  ```
  $ oc get -o yaml all > <yaml_filename>
  ```

  You can also substitute a particular resource type or multiple resources instead of `all`. Run `oc get -h` for more examples.

  The object types included in `oc get -o yaml all` are:

  + `BuildConfig`
  + `Build`
  + `DeploymentConfig`
  + `ImageStream`
  + `Pod`
  + `ReplicationController`
  + `Route`
  + `Service`

    Note

    Using the `all` alias is not recommended because the contents might vary across different clusters and versions. Instead, specify all required resources.

### [3.2. Creating applications by using the Developer perspective](#odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

Create and deploy applications on OpenShift Container Platform by using the **Developer** perspective in the web console.

The **Developer** perspective in the web console provides you the following options from the **+Add** view to create applications and associated services and deploy them on OpenShift Container Platform:

* **Getting started resources**: Use these resources to help you get started with Developer Console. You can choose to hide the header using the Options menu
  .

  + **Creating applications using samples**: Use existing code samples to get started with creating applications on the OpenShift Container Platform.
  + **Build with guided documentation**: Follow the guided documentation to build applications and familiarize yourself with key concepts and terminologies.
  + **Explore new developer features**: Explore the new features and resources within the **Developer** perspective.
* **Developer catalog**: Explore the Developer Catalog to select the required applications, services, or Source-to-Image (S2I) builders, and then add it to your project.

  + **All Services**: Browse the catalog to discover services across OpenShift Container Platform.
  + **Database**: Select the required database service and add it to your application.
  + **Operator Backed**: Select and deploy the required Operator-managed service.
  + **Helm chart**: Select the required Helm chart to simplify deployment of applications and services.
  + **Devfile**: Select a devfile from the **Devfile registry** to declaratively define a development environment.
  + **Event Source**: Select an event source to register interest in a class of events from a particular system.

    Note

    The Managed services option is also available if the RHOAS Operator is installed.
* **Git repository**: Import an existing codebase, Devfile, or Dockerfile from your Git repository using the **From Git**, **From Devfile**, or **From Dockerfile** options respectively, to build and deploy an application on OpenShift Container Platform.
* **Container images**: Use existing images from an image stream or registry to deploy it on to the OpenShift Container Platform.
* **Pipelines**: Use Tekton pipeline to create CI/CD pipelines for your software delivery process on the OpenShift Container Platform.
* **Serverless**: Explore the **Serverless** options to create, build, and deploy stateless and serverless applications on the OpenShift Container Platform.

  + **Channel**: Create a Knative channel to create an event forwarding and persistence layer with in-memory and reliable implementations.
* **Samples**: Explore the available sample applications to create, build, and deploy an application quickly.
* **Quick Starts**: Explore the quick start options to create, import, and run applications with step-by-step instructions and tasks.
* **From Local Machine**: Explore the **From Local Machine** tile to import or upload files on your local machine for building and deploying applications easily.

  + **Import YAML**: Upload a YAML file to create and define resources for building and deploying applications.
  + **Upload JAR file**: Upload a JAR file to build and deploy Java applications.
* **Share my Project**: Use this option to add or remove users to a project and provide accessibility options to them.
* **Helm Chart repositories**: Use this option to add Helm Chart repositories in a namespace.
* **Re-ordering of resources**: Use these resources to re-order pinned resources added to your navigation pane. The drag-and-drop icon is displayed on the left side of the pinned resource when you hover over it in the navigation pane. The dragged resource can be dropped only in the section where it is located.

Note that certain options, such as **Pipelines**, **Event Source**, and **Import Virtual Machines**, are displayed only when the OpenShift Pipelines Operator, OpenShift Serverless Operator, and OpenShift Virtualization Operator are installed.

#### [3.2.1. Prerequisites](#prerequisites_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

To create applications by using the **Developer** perspective, ensure that the following requirements are met:

* You have logged in to the OpenShift web console.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

To create serverless applications, in addition to the preceding prerequisites, ensure that:

* You have installed the OpenShift Serverless Operator.
* You have created a `KnativeServing` resource in the `knative-serving` namespace.

#### [3.2.2. Creating sample applications](#odc-creating-sample-applications_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

You can use the sample applications in the **+Add** flow of the **Developer** perspective to create, build, and deploy applications quickly.

**Prerequisites**

* You have logged in to the OpenShift Container Platform web console and are in the **Developer** perspective.

**Procedure**

1. In the **+Add** view, click the **Samples** tile to see the **Samples** page.
2. On the **Samples** page, select one of the available sample applications to see the **Create Sample Application** form.
3. In the **Create Sample Application Form**:

   * In the **Name** field, the deployment name is displayed by default. You can modify this name as required.
   * In the **Builder Image Version**, a builder image is selected by default. You can modify this image version by using the **Builder Image Version** drop-down list.
   * A sample Git repository URL is added by default.
4. Click **Create** to create the sample application. The build status of the sample application is displayed on the **Topology** view. After the sample application is created, you can see the deployment added to the application.

#### [3.2.3. Creating applications by using Quick Starts](#odc-using-quickstarts_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

The **Quick Starts** page shows you how to create, import, and run applications on OpenShift Container Platform, with step-by-step instructions and tasks.

**Prerequisites**

* You have logged in to the OpenShift Container Platform web console and are in the **Developer** perspective.

**Procedure**

1. In the **+Add** view, click the **Getting Started resources** → **Build with guided documentation** → **View all quick starts** link to view the **Quick Starts** page.
2. In the **Quick Starts** page, click the tile for the quick start that you want to use.
3. Click **Start** to begin the quick start.
4. Perform the steps that are displayed.

#### [3.2.4. Importing a codebase from Git to create an application](#odc-importing-codebase-from-git-to-create-application_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

You can use the **Developer** perspective to create, build, and deploy an application on OpenShift Container Platform using an existing codebase in GitHub.

The following procedure walks you through the **From Git** option in the **Developer** perspective to create an application.

**Procedure**

1. In the **+Add** view, click **From Git** in the **Git Repository** tile to see the **Import from git** form.
2. In the **Git** section, enter the Git repository URL for the codebase you want to use to create an application. For example, enter the URL of this sample Node.js application `https://github.com/sclorg/nodejs-ex`. The URL is then validated.
3. Optional: You can click **Show Advanced Git Options** to add details such as:

   * **Git Reference** to point to code in a specific branch, tag, or commit to be used to build the application.
   * **Context Dir** to specify the subdirectory for the application source code you want to use to build the application.
   * **Source Secret** to create a **Secret Name** with credentials for pulling your source code from a private repository.
4. Optional: You can import a `Devfile`, a `Dockerfile`, `Builder Image`, or a `Serverless Function` through your Git repository to further customize your deployment.

   * If your Git repository contains a `Devfile`, a `Dockerfile`, a `Builder Image`, or a `func.yaml`, it is automatically detected and populated on the respective path fields.
   * If a `Devfile`, a `Dockerfile`, or a `Builder Image` are detected in the same repository, the `Devfile` is selected by default.
   * If `func.yaml` is detected in the Git repository, the **Import Strategy** changes to `Serverless Function`.
   * Alternatively, you can create a serverless function by clicking **Create Serverless function** in the **+Add** view using the Git repository URL.
   * To edit the file import type and select a different strategy, click **Edit import strategy** option.
   * If multiple `Devfiles`, a `Dockerfiles`, or a `Builder Images` are detected, to import a specific instance, specify the respective paths relative to the context directory.
5. After the Git URL is validated, the recommended builder image is selected and marked with a star. If the builder image is not auto-detected, select a builder image. For the `https://github.com/sclorg/nodejs-ex` Git URL, by default the Node.js builder image is selected.

   1. Optional: Use the **Builder Image Version** drop-down to specify a version.
   2. Optional: Use the **Edit import strategy** to select a different strategy.
   3. Optional: For the Node.js builder image, use the **Run command** field to override the command to run the application.
6. In the **General** section:

   1. In the **Application** field, enter a unique name for the application grouping, for example, `myapp`. Ensure that the application name is unique in a namespace.
   2. The **Name** field to identify the resources created for this application is automatically populated based on the Git repository URL if there are no existing applications. If there are existing applications, you can choose to deploy the component within an existing application, create a new application, or keep the component unassigned.

      Note

      The resource name must be unique in a namespace. Modify the resource name if you get an error.
7. In the **Resources** section, select:

   * **Deployment**, to create an application in plain Kubernetes style.
   * **Deployment Config**, to create an OpenShift Container Platform style application.
   * **Serverless Deployment**, to create a Knative service.

     Note

     To set the default resource preference for importing an application, go to **User Preferences** → **Applications** → **Resource type** field. The **Serverless Deployment** option is displayed in the **Import from Git** form only if the OpenShift Serverless Operator is installed in your cluster. The **Resources** section is not available while creating a serverless function. For further details, refer to the OpenShift Serverless documentation.
8. In the **Pipelines** section, select **Add Pipeline**, and then click **Show Pipeline Visualization** to see the pipeline for the application. A default pipeline is selected, but you can choose the pipeline you want from the list of available pipelines for the application.

   Note

   The **Add pipeline** checkbox is checked and **Configure PAC** is selected by default if the following criterias are fulfilled:

   * Pipeline operator is installed
   * `pipelines-as-code` is enabled
   * `.tekton` directory is detected in the Git repository
9. Add a webhook to your repository. If **Configure PAC** is checked and the GitHub App is set up, you can see the **Use GitHub App** and **Setup a webhook** options. If GitHub App is not set up, you can only see the **Setup a webhook** option:

   1. Go to **Settings** → **Webhooks** and click **Add webhook**.
   2. Set the **Payload URL** to the Pipelines as Code controller public URL.
   3. Select the content type as **application/json**.
   4. Add a webhook secret and note it in an alternate location. With `openssl` installed on your local machine, generate a random secret.
   5. Click **Let me select individual events** and select these events: **Commit comments**, **Issue comments**, **Pull request**, and **Pushes**.
   6. Click **Add webhook**.
10. Optional: In the **Advanced Options** section, the **Target port** and the **Create a route to the application** is selected by default so that you can access your application using a publicly available URL.

    If your application does not expose its data on the default public port, 80, clear the check box, and set the target port number you want to expose.
11. Optional: You can use the following advanced options to further customize your application:

    Routing
    :   By clicking the **Routing** link, you can perform the following actions:

        * Customize the hostname for the route.
        * Specify the path the router watches.
        * Select the target port for the traffic from the drop-down list.
        * Secure your route by selecting the **Secure Route** check box. Select the required TLS termination type and set a policy for insecure traffic from the respective drop-down lists.

          Note

          For serverless applications, the Knative service manages all the routing options above. However, you can customize the target port for traffic, if required. If the target port is not specified, the default port of `8080` is used.

    Domain mapping
    :   If you are creating a **Serverless Deployment**, you can add a custom domain mapping to the Knative service during creation.

        * In the **Advanced options** section, click **Show advanced Routing options**.

          + If the domain mapping CR that you want to map to the service already exists, you can select it from the **Domain mapping** drop-down menu.
          + If you want to create a new domain mapping CR, type the domain name into the box, and select the **Create** option. For example, if you type in `example.com`, the **Create** option is **Create "example.com"**.

    Health Checks
    :   Click the **Health Checks** link to add Readiness, Liveness, and Startup probes to your application. All the probes have prepopulated default data; you can add the probes with the default data or customize it as required.

        To customize the health probes:

        * Click **Add Readiness Probe**, if required, modify the parameters to check if the container is ready to handle requests, and select the check mark to add the probe.
        * Click **Add Liveness Probe**, if required, modify the parameters to check if a container is still running, and select the check mark to add the probe.
        * Click **Add Startup Probe**, if required, modify the parameters to check if the application within the container has started, and select the check mark to add the probe.

          For each of the probes, you can specify the request type - **HTTP GET**, **Container Command**, or **TCP Socket**, from the drop-down list. The form changes as per the selected request type. You can then modify the default values for the other parameters, such as the success and failure thresholds for the probe, number of seconds before performing the first probe after the container starts, frequency of the probe, and the timeout value.

    Build Configuration and Deployment
    :   Click the **Build Configuration** and **Deployment** links to see the respective configuration options. Some options are selected by default; you can customize them further by adding the necessary triggers and environment variables.

        For serverless applications, the **Deployment** option is not displayed as the Knative configuration resource maintains the desired state for your deployment instead of a `DeploymentConfig` resource.

    Scaling
    :   Click the **Scaling** link to define the number of pods or instances of the application you want to deploy initially.

        If you are creating a serverless deployment, you can also configure the following settings:

        * **Min Pods** determines the lower limit for the number of pods that must be running at any given time for a Knative service. This is also known as the `minScale` setting.
        * **Max Pods** determines the upper limit for the number of pods that can be running at any given time for a Knative service. This is also known as the `maxScale` setting.
        * **Concurrency target** determines the number of concurrent requests desired for each instance of the application at a given time.
        * **Concurrency limit** determines the limit for the number of concurrent requests allowed for each instance of the application at a given time.
        * **Concurrency utilization** determines the percentage of the concurrent requests limit that must be met before Knative scales up additional pods to handle additional traffic.
        * **Autoscale window** defines the time window over which metrics are averaged to provide input for scaling decisions when the autoscaler is not in panic mode. A service is scaled-to-zero if no requests are received during this window. The default duration for the autoscale window is `60s`. This is also known as the stable window.

    Resource Limit
    :   Click the **Resource Limit** link to set the amount of **CPU** and **Memory** resources a container is guaranteed or allowed to use when running.

    Labels
    :   Click the **Labels** link to add custom labels to your application.
12. Click **Create** to create the application and a success notification is displayed. You can see the build status of the application in the **Topology** view.

#### [3.2.5. Creating applications by deploying container image](#odc-deploying-container-image_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

You can use an external image registry or an image stream tag from an internal registry to deploy an application on your cluster.

**Prerequisites**

* You have logged in to the OpenShift Container Platform web console and are in the **Developer** perspective.

**Procedure**

1. In the **+Add** view, click **Container images** to view the **Deploy Images** page.
2. In the **Image** section:

   1. Select **Image name from external registry** to deploy an image from a public or a private registry, or select **Image stream tag from internal registry** to deploy an image from an internal registry.
   2. Select an icon for your image in the **Runtime icon** tab.
3. In the **General** section:

   1. In the **Application name** field, enter a unique name for the application grouping.
   2. In the **Name** field, enter a unique name to identify the resources created for this component.
4. In the **Resource type** section, select the resource type to generate:

   1. Select **Deployment** to enable declarative updates for `Pod` and `ReplicaSet` objects.
   2. Select **DeploymentConfig** to define the template for a `Pod` object, and manage deploying new images and configuration sources.
   3. Select **Serverless Deployment** to enable scaling to zero when idle.
5. Click **Create**. You can view the build status of the application in the **Topology** view.

#### [3.2.6. Deploying a Java application by uploading a JAR file](#odc-deploying-java-applications_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

You can use the web console **Developer** perspective to upload a JAR file by using the following options:

* Navigate to the **+Add** view of the **Developer** perspective, and click **Upload JAR file** in the **From Local Machine** tile. Browse and select your JAR file, or drag a JAR file to deploy your application.
* Navigate to the **Topology** view and use the **Upload JAR file** option, or drag a JAR file to deploy your application.
* Use the in-context menu in the **Topology** view, and then use the **Upload JAR file** option to upload your JAR file to deploy your application.

**Prerequisites**

* The Cluster Samples Operator must be installed by a cluster administrator.
* You have access to the OpenShift Container Platform web console and are in the **Developer** perspective.

**Procedure**

1. In the **Topology** view, right-click anywhere to view the **Add to Project** menu.
2. Hover over the **Add to Project** menu to see the menu options, and then select the **Upload JAR file** option to see the **Upload JAR file** form. Alternatively, you can drag the JAR file into the **Topology** view.
3. In the **JAR file** field, browse for the required JAR file on your local machine and upload it. Alternatively, you can drag the JAR file on to the field. A toast alert is displayed at the top right if an incompatible file type is dragged into the **Topology** view. A field error is displayed if an incompatible file type is dropped on the field in the upload form.
4. The runtime icon and builder image are selected by default. If a builder image is not auto-detected, select a builder image. If required, you can change the version using the **Builder Image Version** drop-down list.
5. Optional: In the **Application Name** field, enter a unique name for your application to use for resource labelling.
6. In the **Name** field, enter a unique component name for the associated resources.
7. Optional: Use the **Resource type** drop-down list to change the resource type.
8. In the **Advanced options** menu, click **Create a Route to the Application** to configure a public URL for your deployed application.
9. Click **Create** to deploy the application. A toast notification is shown to notify you that the JAR file is being uploaded. The toast notification also includes a link to view the build logs.

Note

If you attempt to close the browser tab while the build is running, a web alert is displayed.

After the JAR file is uploaded and the application is deployed, you can view the application in the **Topology** view.

#### [3.2.7. Using the Devfile registry to access devfiles](#odc-using-the-devfile-registry_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

You can use the devfiles in the **+Add** flow of the **Developer** perspective to create an application. The **+Add** flow provides a complete integration with the [devfile community registry](https://registry.devfile.io/viewer). A devfile is a portable YAML file that describes your development environment without needing to configure it from scratch. Using the **Devfile registry**, you can use a preconfigured devfile to create an application.

**Procedure**

1. Navigate to **Developer Perspective** → **+Add** → **Developer Catalog** → **All Services**. A list of all the available services in the **Developer Catalog** is displayed.
2. Under **Type**, click **Devfiles** to browse for devfiles that support a particular language or framework. Alternatively, you can use the keyword filter to search for a particular devfile using their name, tag, or description.
3. Click the devfile you want to use to create an application. The devfile tile displays the details of the devfile, including the name, description, provider, and the documentation of the devfile.
4. Click **Create** to create an application and view the application in the **Topology** view.

#### [3.2.8. Using the Developer Catalog to add services or components to your application](#odc-using-the-developer-catalog-to-add-services-or-components_odc-creating-applications-using-developer-perspective) Copy linkLink copied to clipboard!

You use the Developer Catalog to deploy applications and services based on Operator backed services such as Databases, Builder Images, and Helm Charts. The Developer Catalog contains a collection of application components, services, event sources, or source-to-image builders that you can add to your project. Cluster administrators can customize the content made available in the catalog.

**Procedure**

1. In the **Developer** perspective, navigate to the **+Add** view and from the **Developer Catalog** tile, click **All Services** to view all the available services in the **Developer Catalog**.
2. Under **All Services**, select the kind of service or the component you need to add to your project. For this example, select **Databases** to list all the database services and then click **MariaDB** to see the details for the service.
3. Click **Instantiate Template** to see an automatically populated template with details for the **MariaDB** service, and then click **Create** to create and view the MariaDB service in the **Topology** view.

   **Figure 3.1. MariaDB in Topology**

### [3.3. Creating applications from installed Operators](#creating-apps-from-installed-operators) Copy linkLink copied to clipboard!

You can deploy applications on your OpenShift Container Platform cluster from Operators that a cluster administrator installed. Use the **Installed Operators** page in the web console to create an application from an Operator custom resource (CR) API.

#### [3.3.1. Creating an etcd cluster using an Operator](#olm-creating-etcd-cluster-from-operator_creating-apps-from-installed-operators) Copy linkLink copied to clipboard!

You can create an etcd cluster using the etcd Operator in the OpenShift Container Platform web console. The Operator creates the pods, services, and other cluster resources for you.

**Prerequisites**

* Access to an OpenShift Container Platform 4.22 cluster.
* The etcd Operator already installed cluster-wide by an administrator.

**Procedure**

1. Create a new project in the OpenShift Container Platform web console for this procedure. This example uses a project called `my-etcd`.
2. Navigate to the **Ecosystem** → **Installed Operators** page.

   The Operators installed on the cluster by the cluster administrator and available for use are shown here as a list of cluster service versions (CSVs). Each CSV launches and manages the software provided by the Operator.

   Tip

   You can get this list from the CLI by running the following command:

   ```
   $ oc get csv
   ```
3. On the **Installed Operators** page, click the etcd Operator to view more details and available actions.

   As shown under **Provided APIs**, this Operator makes available three new resource types, including one for an **etcd Cluster**, the `EtcdCluster` resource.

   These objects work similarly to the built-in native Kubernetes ones, such as `Deployment` or `ReplicaSet`, but contain logic specific to managing etcd.
4. Create a new etcd cluster:

   1. In the **etcd Cluster** API box, click **Create instance**.
   2. Optional: Modify the minimal starting template of an `EtcdCluster` object, such as the size of the cluster.
   3. Click **Create** to finalize. This triggers the Operator to start up the pods, services, and other components of the new etcd cluster.
5. Click the **example** etcd cluster.
6. Click the **Resources** tab.

   Your project contains several resources that the Operator created and configured.
7. Verify that a Kubernetes service exists that allows you to access the database from other pods in your project.
8. Optional: To grant another user permission to create Operator-managed applications in the project, add the `edit` role by running the following command:

   ```
   $ oc policy add-role-to-user edit <user> -n <target_project>
   ```

   Users with the `edit` role in a project can create, manage, and delete Operator-managed application instances, such as an etcd cluster.

**Results**

You have an etcd cluster that reacts to failures and rebalances data as pods become unhealthy or migrate between nodes in the cluster. Cluster administrators or developers with proper access can use the database with their applications.

### [3.4. Creating applications by using the CLI](#creating-applications-using-cli) Copy linkLink copied to clipboard!

You can create applications on your OpenShift Container Platform cluster from a Git repository, a container image, or a template using the `oc new-app` command. Customize names, labels, environment variables, target projects, and other deployment options with command flags.

#### [3.4.1. Creating an application from source code](#applications-create-using-cli-source-code_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can create an application on your OpenShift Container Platform cluster from a local or remote Git repository using the `oc new-app` command. Use command flags to target a specific branch or subdirectory, authenticate to a private repository, or control the build strategy and builder image.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`) and logged in to your cluster.
* You have access to a Git repository containing your application source code.

**Procedure**

1. Create an application from a Git repository in a local directory by running the following command:

   ```
   $ oc new-app /<path_to_source_code>
   ```

   Note

   If you use a local Git repository, the repository must have a remote named `origin` that points to a URL that is accessible by the OpenShift Container Platform cluster. If there is no recognized remote, running the `new-app` command creates a binary build.
2. Create an application from a public remote Git repository by running the following command:

   ```
   $ oc new-app https://github.com/sclorg/cakephp-ex
   ```
3. Create an application from a private remote Git repository by running the following command:

   ```
   $ oc new-app https://github.com/<your_user>/<your_private_repo> --source-secret=yoursecret
   ```

   Note

   If you use a private remote Git repository, use the `--source-secret` flag to specify a source clone secret for access to the repository.
4. Use a subdirectory of your source repository by running the following command:

   ```
   $ oc new-app https://github.com/sclorg/s2i-ruby-container.git \
       --context-dir=2.0/test/puma-test-app
   ```
5. Specify a Git branch by running the following command:

   ```
   $ oc new-app https://github.com/openshift/ruby-hello-world.git#beta4
   ```
6. Override the automatically detected build strategy by running the following command:

   ```
   $ oc new-app /home/user/code/myapp --strategy=docker
   ```

   Note

   The `oc` command requires that files containing build sources are available in a remote Git repository. For all source builds, you must use `git remote -v`.
7. Specify the builder image and source repository:

   1. Specify the builder image and source repository for a remote repository by running the following command:

      ```
      $ oc new-app myproject/my-ruby~https://github.com/openshift/ruby-hello-world.git
      ```
   2. Specify the builder image and source repository for a local repository by running the following command:

      ```
      $ oc new-app openshift/ruby-20-centos7:latest~/home/user/code/my-ruby-app
      ```

#### [3.4.2. Build strategy and language detection for source applications](#applications-create-using-cli-source-reference_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can determine which build strategy and language builder the `oc new-app` command selects by reviewing files in the root or context directory of your Git repository. Use these detection rules to override the build strategy or specify a builder image when automatic detection does not apply.

##### [3.4.2.1. Build strategy detection](#build-strategy-detection_creating-applications-using-cli) Copy linkLink copied to clipboard!

OpenShift Container Platform automatically determines which build strategy to use by detecting certain files:

* If a `Jenkinsfile` exists in the root or specified context directory of the source repository when creating a new application, OpenShift Container Platform generates a pipeline build strategy.

  Note

  The `pipeline` build strategy is deprecated; consider using Red Hat OpenShift Pipelines instead.
* If a `Dockerfile` exists in the root or specified context directory of the source repository when creating a new application, OpenShift Container Platform generates a docker build strategy.
* If neither a `Jenkinsfile` nor a `Dockerfile` is detected, OpenShift Container Platform generates a source build strategy.

##### [3.4.2.2. Language detection](#language-detection_creating-applications-using-cli) Copy linkLink copied to clipboard!

If you use the source build strategy, `new-app` detects the language builder from certain files in the root or context directory of the repository.

Expand

Table 3.1. Languages detected by new-app

| Language | Files |
| --- | --- |
| `dotnet` | `project.json`, `*.csproj` |
| `jee` | `pom.xml` |
| `nodejs` | `app.json`, `package.json` |
| `perl` | `cpanfile`, `index.pl` |
| `php` | `composer.json`, `index.php` |
| `python` | `requirements.txt`, `setup.py` |
| `ruby` | `Gemfile`, `Rakefile`, `config.ru` |
| `scala` | `build.sbt` |
| `golang` | `Godeps`, `main.go` |

Show more

After a language is detected, the `new-app` command searches the OpenShift Container Platform server for image stream tags with a matching `supports` annotation or image streams that match the language name. If a match is not found, the `new-app` command searches the Docker Hub registry for an image that matches the detected language based on name.

When you specify an image and repository with the `~` separator, build strategy detection and language detection are not carried out.

Note

Language detection requires the Git client to be locally installed so that your repository can be cloned and inspected. If Git is not available, you can avoid the language detection step by specifying the builder image to use with your repository with the `<image>~<repository>` syntax.

The `-i <image> <repository>` invocation requires that `new-app` attempt to clone `repository` to determine what type of artifact it is, so the command fails if Git is not available.

The `-i <image> --code <repository>` invocation requires that `new-app` clone `repository` to learn whether `image` is a builder for the source or a separate deployment, such as a database image.

#### [3.4.3. Creating an application from an image](#applications-create-using-cli-image_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can use the `oc new-app` command to create an application from a container image in Docker Hub, a private registry, or an image stream on your cluster. Use this procedure when you know the container image name or image stream you want to deploy.

Use the command that matches where your container image is stored.

Note

If you specify an image from your local Docker repository, you must ensure that the same image is available to the OpenShift Container Platform cluster nodes.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`) and logged in to your cluster.
* You know the container image name or image stream you want to deploy.

**Procedure**

* Create an application from the Docker Hub MySQL image by running the following command:

  ```
  $ oc new-app mysql
  ```
* Create an application from an image in a private registry by specifying the full image path in the following command:

  ```
  $ oc new-app myregistry:5000/example/myimage
  ```
* Create an application from an existing image stream and optional image stream tag by running the following command:

  ```
  $ oc new-app my-stream:v1
  ```

#### [3.4.4. Creating an application from a template](#applications-create-using-cli-template_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can use the `oc new-app` command to create an application from a template stored in your project or from a template file on your local system. Use this procedure when you have a template JSON or YAML file, or a template in the template library of your current project.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`) and logged in to your cluster.
* You have a template JSON or YAML file, or a template stored in the template library of your current project.

**Procedure**

1. Upload an application template to the template library of your current project by running the following command:

   ```
   $ oc create -f examples/sample-app/application-template-stibuild.json
   ```
2. Create a new application from a stored template by running the following command:

   ```
   $ oc new-app ruby-helloworld-sample
   ```
3. Create a new application from a template file on your local file system without storing it in OpenShift Container Platform by running the following command:

   ```
   $ oc new-app -f examples/sample-app/application-template-stibuild.json
   ```
4. Set template parameter values when creating an application by running the following command:

   ```
   $ oc new-app ruby-helloworld-sample \
       -p ADMIN_USERNAME=admin -p ADMIN_PASSWORD=mypassword
   ```
5. Store template parameters in a file by creating a file such as `helloworld.params` with the following content:

   ```
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=mypassword
   ```

   You can store your parameters in a file, then use that file with `--param-file` when instantiating a template. If you want to read the parameters from standard input, use `--param-file=-`.
6. Create a new application from a template by using a parameter file by running the following command:

   ```
   $ oc new-app ruby-helloworld-sample --param-file=helloworld.params
   ```

   Note

   To read parameters from standard input, use `--param-file=-`.

#### [3.4.5. Customization options for application creation](#applications-create-using-cli-modify_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can customize how the `oc new-app` command creates applications by setting names, labels, environment variables, target projects, and other options. Use these flags to control the objects the command generates before you deploy.

Expand

Table 3.2. new-app output objects

| Object | Description |
| --- | --- |
| `BuildConfig` | A `BuildConfig` object is created for each source repository that is specified in the command line. The `BuildConfig` object specifies the strategy to use, the source location, and the build output location. |
| `ImageStreams` | For the `BuildConfig` object, two image streams are usually created. One represents the input image. With source builds, this is the builder image. With `Docker` builds, this is the **FROM** image. The second one represents the output image. If a container image was specified as input to `new-app`, then an image stream is created for that image as well. |
| `DeploymentConfig` | A `DeploymentConfig` object is created either to deploy the output of a build, or a specified image. The `new-app` command creates `emptyDir` volumes for all Docker volumes that are specified in containers included in the resulting `DeploymentConfig` object. |
| `Service` | The `new-app` command attempts to detect exposed ports in input images. It uses the lowest numeric exposed port to generate a service that exposes that port. To expose a different port, after `new-app` has completed, use the `oc expose` command to generate additional services. |
| Other | Other objects can be generated when creating applications from templates, according to the template. |

Show more

##### [3.4.5.1. Specifying environment variables](#specifying-environment-variables_creating-applications-using-cli) Copy linkLink copied to clipboard!

When generating applications from a template, source, or an image, you can use the `-e|--env` argument to pass environment variables to the application container at run time.

```
$ oc new-app openshift/postgresql-92-centos7 \
    -e POSTGRESQL_USER=user \
    -e POSTGRESQL_DATABASE=db \
    -e POSTGRESQL_PASSWORD=password
```

The variables can also be read from file using the `--env-file` argument. The following is an example file called `postgresql.env`:

```
POSTGRESQL_USER=user
POSTGRESQL_DATABASE=db
POSTGRESQL_PASSWORD=password
```

Read the variables from the file:

```
$ oc new-app openshift/postgresql-92-centos7 --env-file=postgresql.env
```

Additionally, environment variables can be given on standard input by using the `--env-file=-` argument:

```
$ cat postgresql.env | oc new-app openshift/postgresql-92-centos7 --env-file=-
```

Note

Any `BuildConfig` objects created as part of `new-app` processing are not updated with environment variables passed with the `-e|--env` or `--env-file` argument.

##### [3.4.5.2. Specifying build environment variables](#specifying-build-environment-variables_creating-applications-using-cli) Copy linkLink copied to clipboard!

When generating applications from a template, source, or an image, you can use the `--build-env` argument to pass environment variables to the build container at run time:

```
$ oc new-app openshift/ruby-23-centos7 \
    --build-env HTTP_PROXY=http://myproxy.net:1337/ \
    --build-env GEM_HOME=~/.gem
```

The variables can also be read from a file using the `--build-env-file` argument. The following is an example file called `ruby.env`:

```
HTTP_PROXY=http://myproxy.net:1337/
GEM_HOME=~/.gem
```

Read the variables from the file:

```
$ oc new-app openshift/ruby-23-centos7 --build-env-file=ruby.env
```

Additionally, environment variables can be given on standard input by using `--build-env-file=-`:

```
$ cat ruby.env | oc new-app openshift/ruby-23-centos7 --build-env-file=-
```

##### [3.4.5.3. Specifying labels](#specifying-labels_creating-applications-using-cli) Copy linkLink copied to clipboard!

When generating applications from source, images, or templates, you can use the `-l|--label` argument to add labels to the created objects. Labels make it easy to collectively select, configure, and delete objects associated with the application.

```
$ oc new-app https://github.com/openshift/ruby-hello-world -l name=hello-world
```

##### [3.4.5.4. Viewing the output without creation](#viewing-output-without-creation_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can preview objects without creating them by using `-o` or `--output` with a `yaml` or `json` value. Redirect the output to a file, edit the file, then create the objects with `oc create`.

**Writing `new-app` output to a file**

```
$ oc new-app https://github.com/openshift/ruby-hello-world \
    -o yaml > myapp.yaml
```

**Creating objects from an edited file**

```
$ oc create -f myapp.yaml
```

##### [3.4.5.5. Creating objects with different names](#creating-objects-different-names_creating-applications-using-cli) Copy linkLink copied to clipboard!

Objects created by `new-app` are normally named after the source repository, or the image used to generate them. You can set the name of the objects produced by adding a `--name` flag to the command:

```
$ oc new-app https://github.com/openshift/ruby-hello-world --name=myapp
```

##### [3.4.5.6. Creating objects in a different project](#creating-objects-different-project_creating-applications-using-cli) Copy linkLink copied to clipboard!

Normally, `new-app` creates objects in the current project. However, you can create objects in a different project by using the `-n|--namespace` argument:

```
$ oc new-app https://github.com/openshift/ruby-hello-world -n myproject
```

##### [3.4.5.7. Creating multiple objects](#creating-multiple-objects_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can create multiple applications by specifying multiple parameters to `new-app`. Labels specified in the command line apply to all objects created by the single command. Environment variables apply to all components created from source or images.

To create an application from a source repository and a Docker Hub image:

```
$ oc new-app https://github.com/openshift/ruby-hello-world mysql
```

Note

If a source code repository and a builder image are specified as separate arguments, `new-app` uses the builder image as the builder for the source code repository. If this is not the intent, specify the required builder image for the source using the `~` separator.

##### [3.4.5.8. Grouping images and source in a single pod](#grouping-images-source-single-pod_creating-applications-using-cli) Copy linkLink copied to clipboard!

You can deploy multiple images together in a single pod. To specify which images to group together, use the `+` separator. The `--group` command-line argument can also be used to specify the images that should be grouped together. To group the image built from a source repository with other images, specify the builder image for the source in the group:

```
$ oc new-app ruby+mysql
```

To deploy an image built from source and an external image together:

```
$ oc new-app \
    ruby~https://github.com/openshift/ruby-hello-world \
    mysql \
    --group=ruby+mysql
```

##### [3.4.5.9. Searching for images, templates, and other inputs](#searching-for-images-templates-other-inputs_creating-applications-using-cli) Copy linkLink copied to clipboard!

To search for images, templates, and other inputs for the `oc new-app` command, add the `--search` and `--list` flags. For example, to find all of the images or templates that include PHP:

```
$ oc new-app --search php
```

##### [3.4.5.10. Setting the import mode](#setting-the-import-mode_creating-applications-using-cli) Copy linkLink copied to clipboard!

To set the import mode when using `oc new-app`, add the `--import-mode` flag. This flag can be appended with `Legacy` or `PreserveOriginal`, which provides users the option to create image streams using a single sub-manifest, or all manifests, respectively.

```
$ oc new-app --image=registry.redhat.io/ubi8/httpd-24:latest --import-mode=Legacy --name=test
```

```
$ oc new-app --image=registry.redhat.io/ubi8/httpd-24:latest --import-mode=PreserveOriginal --name=test
```

### [3.5. Creating applications using Ruby on Rails](#templates-using-ruby-on-rails) Copy linkLink copied to clipboard!

You can build and deploy a Ruby on Rails 4 application on OpenShift Container Platform by developing it locally.

Store the source in Git, then deploy the database, frontend, and route services. With this process, you can validate your application locally before deploying it to the cluster as a set of distinct services.

Warning

You must complete each part of this tutorial in order to before you deploy your application on OpenShift Container Platform. If a step fails, confirm that every preceding step completed successfully before you continue.

#### [3.5.1. Prerequisites](#prerequisites) Copy linkLink copied to clipboard!

* You have basic Ruby on Rails knowledge.
* You have Ruby 2.0.0+, Rubygems, and Bundler installed locally.
* You have basic Git knowledge.
* You have a running instance of OpenShift Container Platform 4.
* The OpenShift CLI (`oc`) installed.
* You are logged into a running OpenShift Container Platform cluster.

#### [3.5.2. Setting up the database](#templates-rails-setting-up-database_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can install PostgreSQL on your local system for Ruby on Rails development. This gives your application a local database to connect to during development and testing before you deploy to OpenShift Container Platform.

**Procedure**

1. Install the database by running the following command:

   ```
   $ sudo yum install -y postgresql postgresql-server postgresql-devel
   ```
2. Initialize the database by running the following command:

   ```
   $ sudo postgresql-setup initdb
   ```

   This command creates the `/var/lib/pgsql/data` directory, in which the data is stored.
3. Start the database by running the following command:

   ```
   $ sudo systemctl start postgresql.service
   ```
4. When the database is running, create your `rails` user by running the following command:

   ```
   $ sudo -u postgres createuser -s rails
   ```

   Note

   The user that is created has no password.

#### [3.5.3. Writing your application](#templates-rails-writing-application_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can create a Ruby on Rails application that uses PostgreSQL. Install the Rails gem, configure the `database.yml` file, and initialize the development and test databases. These steps ensure that your application can interact with PostgreSQL in both development and test environments.

**Procedure**

1. Install the Rails gem by running the following command:

   ```
   $ gem install rails
   ```

   **Example output**

   ```
   Successfully installed rails-4.3.0
   1 gem installed
   ```
2. Create a new application with PostgreSQL as your database by running the following command:

   ```
   $ rails new rails-app --database=postgresql
   ```
3. Change into your new application directory by running the following command:

   ```
   $ cd rails-app
   ```
4. If you already have an application, ensure that the PostgreSQL adapter gem (`pg`) is present in your `Gemfile`. If not, edit your `Gemfile` by adding the gem:

   ```
   gem 'pg'
   ```
5. Generate a new `Gemfile.lock` with all your dependencies by running the following command:

   ```
   $ bundle install
   ```
6. Update the `default` section in the `config/database.yml` file to use the `postgresql` adapter, as shown in the following example:

   ```
   default: &default
     adapter: postgresql
     encoding: unicode
     pool: 5
     host: localhost
     username: rails
     password: <password>
   ```
7. Create the `development` and `test` databases for your application by running the following command:

   ```
   $ rake db:create
   ```

##### [3.5.3.1. Creating a welcome page](#templates-rails-creating-welcome-page_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can run the Rails generator to create a custom welcome page for your Rails application. A welcome page gives you content to display when you run the Rails server and open the application in your browser.

**Procedure**

1. Run the Rails generator by running the following command:

   ```
   $ rails generate controller welcome index
   ```

   The command creates all the necessary files.
2. Edit line 2 in the `config/routes.rb` file as follows:

   ```
   root 'welcome#index'
   ```
3. Run the Rails server to verify that the page is available by running the following command:

   ```
   $ rails server
   ```

   Verify that the page is available by visiting `http://localhost:3000` in your browser. If the page does not display, check the server logs for errors.

##### [3.5.3.2. Configuring application for OpenShift Container Platform](#templates-rails-configuring-application_templates-ruby-on-rails) Copy linkLink copied to clipboard!

To configure your Rails application for OpenShift Container Platform, you must edit the `default` section in the `config/database.yml` file. This is required for OpenShift Container Platform to supply the correct database credentials at runtime so your application can connect to PostgreSQL on the cluster.

**Procedure**

* Edit the `default` section in your `config/database.yml` with pre-defined variables as follows:

  **Sample `config/database` YAML file**

  ```
  <% user = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? "root" : ENV["POSTGRESQL_USER"] %>
  <% password = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? ENV["POSTGRESQL_ADMIN_PASSWORD"] : ENV["POSTGRESQL_PASSWORD"] %>
  <% db_service = ENV.fetch("DATABASE_SERVICE_NAME","").upcase %>

  default: &default
    adapter: postgresql
    encoding: unicode
    # For details on connection pooling, see rails configuration guide
    # http://guides.rubyonrails.org/configuring.html#database-pooling
    pool: <%= ENV["POSTGRESQL_MAX_CONNECTIONS"] || 5 %>
    username: <%= user %>
    password: <%= password %>
    host: <%= ENV["#{db_service}_SERVICE_HOST"] %>
    port: <%= ENV["#{db_service}_SERVICE_PORT"] %>
    database: <%= ENV["POSTGRESQL_DATABASE"] %>
  ```

##### [3.5.3.3. Storing your application in Git](#templates-rails-storing-application-in-git_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can commit your Rails application to Git and push the source to a remote repository. Remote storage keeps your source available for deployment on OpenShift Container Platform.

**Prerequisites**

* You have installed Git.

**Procedure**

1. Verify that you are in your Rails application directory by running the following command:

   ```
   $ ls -1
   ```

   **Example output**

   ```
   app
   bin
   config
   config.ru
   db
   Gemfile
   Gemfile.lock
   lib
   log
   public
   Rakefile
   README.rdoc
   test
   tmp
   vendor
   ```
2. Initialize a Git repository in your Rails application directory by running the following command:

   ```
   $ git init
   ```
3. Stage all application files by running the following command:

   ```
   $ git add .
   ```
4. Commit the staged files by running the following command:

   ```
   $ git commit -m "initial commit"
   ```
5. Create a GitHub repository for your application.
6. Set the remote that points to your `git` repository by running the following command:

   ```
   $ git remote add origin git@github.com:<namespace/repository-name>.git
   ```
7. Push your application to your remote Git repository by running the following command:

   ```
   $ git push
   ```

#### [3.5.4. Deploying your application to OpenShift Container Platform](#templates-rails-deploying-application_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can create an OpenShift Container Platform project to deploy your Ruby on Rails application. This separates your database, frontend, and route into distinct services that OpenShift Container Platform can manage independently.

Deploying your application on OpenShift Container Platform takes three steps:

1. Creating a database service from the PostgreSQL image on OpenShift Container Platform.
2. Creating a frontend service from the Ruby 2.0 builder image on OpenShift Container Platform and your Ruby on Rails source code, connected to the database service.
3. Creating a route for your application.

**Procedure**

* Create a project for your Rails application by running the following command:

  ```
  $ oc new-project rails-app --description="My Rails application" --display-name="Rails Application"
  ```

##### [3.5.4.1. Creating the database service](#templates-rails-creating-database-service_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You must create a database service for your Rails application. Be sure to set the environment variables for the database name, username, and password. These are required for the service to connect correctly to your Rails application.

You can change the values of these environment variables to any values you choose. The variables are as follows:

* `POSTGRESQL_DATABASE`
* `POSTGRESQL_USER`
* `POSTGRESQL_PASSWORD`

Setting these variables ensures that the following occurs:

* A database exists with the specified name.
* A user exists with the specified name.
* The user can access the specified database with the specified password.

**Procedure**

1. Create the database service by running the following command:

   ```
   $ oc new-app postgresql -e POSTGRESQL_DATABASE=db_name -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password
   ```

   Note

   To also set a database administrator password, add `-e POSTGRESQL_ADMIN_PASSWORD=admin_pw` to the command.
2. Monitor the pod status by running the following command:

   ```
   $ oc get pods --watch
   ```

##### [3.5.4.2. Creating the frontend service](#templates-rails-creating-frontend-service_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can create a frontend service with the `oc new-app` command. Specifying your source repository and database environment variables enables OpenShift Container Platform to build your application image and deploy it on the cluster.

**Procedure**

1. Create the frontend service and specify the database-related environment variables that were set up when creating the database service by running the following command:

   ```
   $ oc new-app path/to/source/code --name=rails-app -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password -e POSTGRESQL_DATABASE=db_name -e DATABASE_SERVICE_NAME=postgresql
   ```

   With this command, OpenShift Container Platform fetches the source code, sets up the builder, builds your application image, and deploys the newly created image together with the specified environment variables. The application is named `rails-app`.
2. Verify that the environment variables have been added by viewing the JSON document of the `rails-app` deployment config by running the following command:

   ```
   $ oc get dc rails-app -o json
   ```

   The output includes the following section:

   **Example output**

   ```
   env": [
       {
           "name": "POSTGRESQL_USER",
           "value": "username"
       },
       {
           "name": "POSTGRESQL_PASSWORD",
           "value": "password"
       },
       {
           "name": "POSTGRESQL_DATABASE",
           "value": "db_name"
       },
       {
           "name": "DATABASE_SERVICE_NAME",
           "value": "postgresql"
       }

   ],
   ```
3. Check the build process by running the following command:

   ```
   $ oc logs -f build/rails-app-1
   ```
4. After the build is complete, check the running pods in OpenShift Container Platform by running the following command:

   ```
   $ oc get pods
   ```

   The output includes a line starting with `myapp-<number>-<hash>`, which confirms that the application is running in OpenShift Container Platform.
5. Before your application is functional, you must initialize the database by running the database migration script. There are two ways you can do this:

   * Manually from the running frontend container:

     + Open a remote shell to the frontend pod by running the following command:

       ```
       $ oc rsh <frontend_pod_id>
       ```
     + Run the migration from inside the container by running the following command:

       ```
       $ RAILS_ENV=production bundle exec rake db:migrate
       ```

       If you are running your Rails application in a `development` or `test` environment, you do not have to specify the `RAILS_ENV` environment variable.
   * You can also run the migration by adding pre-deployment lifecycle hooks to your template.

##### [3.5.4.3. Creating a route for your application](#templates-rails-creating-route-for-application_templates-ruby-on-rails) Copy linkLink copied to clipboard!

You can create a route for your application with the `oc expose service` command. The route makes the application accessible from outside the cluster.

**Procedure**

* Make the frontend service accessible externally by running the following command:

  ```
  $ oc expose service rails-app --hostname=www.example.com
  ```

  Warning

  Ensure that the hostname you specify resolves to the IP address of the router.

## [Chapter 4. Viewing application composition by using the Topology view](#odc-viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

The **Topology** view in the **Developer** perspective of the web console provides a visual representation of all the applications within a project, their build status, and the components and services associated with them.

### [4.1. Prerequisites](#prerequisites-2) Copy linkLink copied to clipboard!

To view your applications in the **Topology** view and interact with them, ensure that:

* You have [logged in to the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#web-console).
* You have the appropriate [roles and permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#default-roles_using-rbac) in a project to create applications and other workloads in OpenShift Container Platform.
* You are in [the **Developer** perspective](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#about-developer-perspective_web-console-overview).

### [4.2. Viewing the topology of your application](#odc-viewing-application-topology_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

You can navigate to the **Topology** view using the left navigation panel in the **Developer** perspective. After you deploy an application, you are directed automatically to the **Graph view** where you can see the status of the application pods, quickly access the application on a public URL, access the source code to modify it, and see the status of your last build. You can zoom in and out to see more details for a particular application.

The **Topology** view provides you the option to monitor your applications using the **List** view. Use the **List view** icon (
) to see a list of all your applications and use the **Graph view** icon (
) to switch back to the graph view.

You can customize the views as required using the following:

* Use the **Find by name** field to find the required components. Search results may appear outside of the visible area; click **Fit to Screen** from the lower-left toolbar to resize the **Topology** view to show all components.
* Use the **Display Options** drop-down list to configure the **Topology** view of the various application groupings. The options are available depending on the types of components deployed in the project:

  + **Expand** group

    - Virtual Machines: Toggle to show or hide the virtual machines.
    - Application Groupings: Clear to condense the application groups into cards with an overview of an application group and alerts associated with it.
    - Helm Releases: Clear to condense the components deployed as Helm Release into cards with an overview of a given release.
    - Knative Services: Clear to condense the Knative Service components into cards with an overview of a given component.
    - Operator Groupings: Clear to condense the components deployed with an Operator into cards with an overview of the given group.
  + **Show** elements based on **Pod Count** or **Labels**

    - Pod Count: Select to show the number of pods of a component in the component icon.
    - Labels: Toggle to show or hide the component labels.

The **Topology** view also provides you the **Export application** option to download your application in the ZIP file format. You can then import the downloaded application to another project or cluster. For more details, see *Exporting an application to another project or cluster* in the *Additional resources* section.

### [4.3. Interacting with applications and components](#odc-interacting-with-applications-and-components_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

In the **Topology** view in the **Developer** perspective of the web console, the **Graph view** provides the following options to interact with applications and components:

* Click **Open URL** (
  ) to see your application exposed by the route on a public URL.
* Click **Edit Source code** to access your source code and modify it.

  Note

  This feature is available only when you create applications using the **From Git**, **From Catalog**, and the **From Dockerfile** options.
* Hover your cursor over the lower left icon on the pod to see the name of the latest build and its status. The status of the application build is indicated as **New** (
  ), **Pending** (
  ), **Running** (
  ), **Completed** (
  ), **Failed** (
  ), and **Canceled** (
  ).
* The status or phase of the pod is indicated by different colors and tooltips as:

  + **Running** (
    ): The pod is bound to a node and all of the containers are created. At least one container is still running or is in the process of starting or restarting.
  + **Not Ready** (
    ): The pods which are running multiple containers, not all containers are ready.
  + **Warning**(
    ): Containers in pods are being terminated, however termination did not succeed. Some containers may be other states.
  + **Failed**(
    ): All containers in the pod terminated but least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system.
  + **Pending**(
    ): The pod is accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a pod spends waiting to be scheduled as well as the time spent downloading container images over the network.
  + **Succeeded**(
    ): All containers in the pod terminated successfully and will not be restarted.
  + **Terminating**(
    ): When a pod is being deleted, it is shown as **Terminating** by some kubectl commands. **Terminating** status is not one of the pod phases. A pod is granted a graceful termination period, which defaults to 30 seconds.
  + **Unknown**(
    ): The state of the pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the pod should be running.
* After you create an application and an image is deployed, the status is shown as **Pending**. After the application is built, it is displayed as **Running**.

  **Figure 4.1. Application topology**

  The application resource name is appended with indicators for the different types of resource objects as follows:

  + **CJ**: `CronJob`
  + **D**: `Deployment`
  + **DC**: `DeploymentConfig`
  + **DS**: `DaemonSet`
  + **J**: `Job`
  + **P**: `Pod`
  + **SS**: `StatefulSet`
  + (Knative): A serverless application

    Note

    Serverless applications take some time to load and display on the **Graph view**. When you deploy a serverless application, it first creates a service resource and then a revision. After that, it is deployed and displayed on the **Graph view**. If it is the only workload, you might be redirected to the **Add** page. After the revision is deployed, the serverless application is displayed on the **Graph view**.

### [4.4. Scaling application pods and checking builds and routes](#odc-scaling-application-pods-and-checking-builds-and-routes_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

The **Topology** view provides the details of the deployed components in the **Overview** panel. You can use the **Overview** and **Details** tabs to scale the application pods, check build status, services, and routes as follows:

* Click on the component node to see the **Overview** panel to the right. Use the **Details** tab to:

  + Scale your pods using the up and down arrows to increase or decrease the number of instances of the application manually. For serverless applications, the pods are automatically scaled down to zero when idle and scaled up depending on the channel traffic.
  + Check the **Labels**, **Annotations**, and **Status** of the application.
* Click the **Resources** tab to:

  + See the list of all the pods, view their status, access logs, and click on the pod to see the pod details.
  + See the builds, their status, access logs, and start a new build if needed.
  + See the services and routes used by the component.

  For serverless applications, the **Resources** tab provides information on the revision, routes, and the configurations used for that component.

### [4.5. Adding components to an existing project](#odc-adding-components-to-an-existing-project_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

You can add components to a project.

**Procedure**

1. Navigate to the **+Add** view.
2. Click **Add to Project** (
   ) next to left navigation pane or press `Ctrl`+`Space`
3. Search for the component and click the **Start**/**Create**/**Install** button or click `Enter` to add the component to the project and see it in the topology **Graph view**.

   **Figure 4.2. Adding component via quick search**

Alternatively, you can also use the available options in the context menu, such as **Import from Git**, **Container Image**, **Database**, **From Catalog**, **Operator Backed**, **Helm Charts**, **Samples**, or **Upload JAR file**, by right-clicking in the topology **Graph view** to add a component to your project.

**Figure 4.3. Context menu to add services**

### [4.6. Grouping multiple components within an application](#odc-grouping-multiple-components_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

You can use the **+Add** view to add multiple components or services to your project and use the topology **Graph view** to group applications and resources within an application group.

**Prerequisites**

* You have created and deployed minimum two or more components on OpenShift Container Platform using the **Developer** perspective.

**Procedure**

* To add a service to the existing application group, press `Shift`+ drag it to the existing application group. Dragging a component and adding it to an application group adds the required labels to the component.

  **Figure 4.4. Application grouping**

Alternatively, you can also add the component to an application as follows:

1. Click the service pod to see the **Overview** panel to the right.
2. Click the **Actions** drop-down menu and select **Edit Application Grouping**.
3. In the **Edit Application Grouping** dialog box, click the **Application** drop-down list, and select an appropriate application group.
4. Click **Save** to add the service to the application group.

You can remove a component from an application group by selecting the component and using `Shift`+ drag to drag it out of the application group.

### [4.7. Adding services to your application](#odc-adding-services-to-your-application_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

To add a service to your application use the **+Add** actions using the context menu in the topology **Graph view**.

Note

In addition to the context menu, you can add services by using the sidebar or hovering and dragging the dangling arrow from the application group.

**Procedure**

1. Right-click an application group in the topology **Graph view** to display the context menu.

   **Figure 4.5. Add resource context menu**
2. Use **Add to Application** to select a method for adding a service to the application group, such as **From Git**, **Container Image**, **From Dockerfile**, **From Devfile**, **Upload JAR file**, **Event Source**, **Channel**, or **Broker**.
3. Complete the form for the method you choose and click **Create**. For example, to add a service based on the source code in your Git repository, choose the **From Git** method, fill in the **Import from Git** form, and click **Create**.

### [4.8. Removing services from your application](#odc-removing-services-from-your-application_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

In the topology **Graph view** remove a service from your application using the context menu.

**Procedure**

1. Right-click on a service in an application group in the topology **Graph view** to display the context menu.
2. Select **Delete Deployment** to delete the service.

   **Figure 4.6. Deleting deployment option**

### [4.9. Labels and annotations used for the Topology view](#odc-labels-and-annotations-used-for-topology-view_viewing-application-composition-using-topology-view) Copy linkLink copied to clipboard!

The **Topology** view uses the following labels and annotations:

Icon displayed in the node
:   Icons in the node are defined by looking for matching icons using the `app.openshift.io/runtime` label, followed by the `app.kubernetes.io/name` label. This matching is done using a predefined set of icons.

Link to the source code editor or the source
:   The `app.openshift.io/vcs-uri` annotation is used to create links to the source code editor.

Node Connector
:   The `app.openshift.io/connects-to` annotation is used to connect the nodes.

App grouping
:   The `app.kubernetes.io/part-of=<appname>` label is used to group the applications, services, and components.

For detailed information on the labels and annotations OpenShift Container Platform applications must use, see [Guidelines for labels and annotations for OpenShift applications](https://github.com/redhat-developer/app-labels/blob/master/labels-annotation-for-openshift.adoc).

## [Chapter 5. Exporting applications](#odc-exporting-applications) Copy linkLink copied to clipboard!

As a developer, you can export your application in the ZIP file format. Based on your needs, import the exported application to another project in the same cluster or a different cluster by using the **Import YAML** option in the **+Add** view. Exporting your application helps you to reuse your application resources and saves your time.

### [5.1. Prerequisites](#prerequisites_odc-exporting-applications) Copy linkLink copied to clipboard!

* You have installed the gitops-primer Operator from the software catalog.

  Note

  The **Export application** option is disabled in the **Topology** view even after installing the gitops-primer Operator.
* You have created an application in the **Topology** view to enable **Export application**.

### [5.2. Procedure](#odc-exporting-applications-procedure) Copy linkLink copied to clipboard!

1. In the developer perspective, perform one of the following steps:

   1. Navigate to the **+Add** view and click **Export application** in the **Application portability** tile.
   2. Navigate to the **Topology** view and click **Export application**.
2. Click **OK** in the **Export Application** dialog box. A notification opens to confirm that the export of resources from your project has started.
3. Optional steps that you might need to perform in the following scenarios:

   * If you have started exporting an incorrect application, click **Export application** → **Cancel Export**.
   * If your export is already in progress and you want to start a fresh export, click **Export application** → **Restart Export**.
   * If you want to view logs associated with exporting an application, click **Export application** and the **View Logs** link.
4. After a successful export, click **Download** in the dialog box to download application resources in ZIP format onto your machine.

## [Chapter 6. Working with Helm charts](#working-with-helm-charts) Copy linkLink copied to clipboard!

### [6.1. Understanding Helm](#understanding-helm) Copy linkLink copied to clipboard!

Helm is a software package manager that simplifies deployment of applications and services to OpenShift Container Platform clusters.

Helm uses a packaging format called *charts*. A Helm chart is a collection of files that describes the OpenShift Container Platform resources.

Creating a chart in a cluster creates a running instance of the chart known as a *release*.

Each time a chart is created, or a release is upgraded or rolled back, an incremental revision is created.

#### [6.1.1. Key features](#key-features) Copy linkLink copied to clipboard!

Helm provides the ability to:

* Search through a large collection of charts stored in the chart repository.
* Modify existing charts.
* Create your own charts with OpenShift Container Platform or Kubernetes resources.
* Package and share your applications as charts.

#### [6.1.2. Red Hat Certification of Helm charts for OpenShift](#red-hat-certification-of-helm-charts-for-openshift) Copy linkLink copied to clipboard!

You can choose to verify and certify your Helm charts by Red Hat for all the components you will be deploying on the Red Hat OpenShift Container Platform. Charts go through an automated Red Hat OpenShift certification workflow that guarantees security compliance as well as best integration and experience with the platform. Certification assures the integrity of the chart and ensures that the Helm chart works seamlessly on Red Hat OpenShift clusters.

### [6.2. Installing Helm](#installing-helm) Copy linkLink copied to clipboard!

Install the Helm CLI to manage software packages on your OpenShift Container Platform cluster from a local workstation.

You can also find the URL to the latest binaries from the OpenShift Container Platform web console by clicking the **?** icon in the upper-right corner and selecting **Command Line Tools**.

#### [6.2.1. On Linux](#on-linux) Copy linkLink copied to clipboard!

1. Download the Helm binary:

   * Linux (x86\_64, amd64)

     ```
     # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm
     ```
   * Linux on IBM Z® and IBM® LinuxONE (s390x)

     ```
     # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-s390x -o /usr/local/bin/helm
     ```
   * Linux on IBM Power® (ppc64le)

     ```
     # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-ppc64le -o /usr/local/bin/helm
     ```
   * Linux on ARM (arm64)

     ```
     # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-arm64 -o /usr/local/bin/helm
     ```
2. Make the binary file executable:

   ```
   # chmod +x /usr/local/bin/helm
   ```
3. Check the installed version:

   ```
   $ helm version
   ```

   **Example output**

   ```
   version.BuildInfo{Version:"v3.0", GitCommit:"b31719aab7963acf4887a1c1e6d5e53378e34d93", GitTreeState:"clean", GoVersion:"go1.13.4"}
   ```

#### [6.2.2. On Windows](#on-windows) Copy linkLink copied to clipboard!

1. Download the Helm binary: [`.exe` file](https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-windows-amd64.exe).
2. Click **Search** and type `env` or `environment`.
3. Select **Edit environment variables for your account**.
4. Select **Path** from the **Variable** section and click **Edit**.
5. Click **New** and type the path to the directory with the exe file into the field or click **Browse** and select the directory, and click **OK**.

#### [6.2.3. On macOS](#on-macos) Copy linkLink copied to clipboard!

1. Download the Helm binary:

   * For macOS on Intel (x86\_64):

     ```
     # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-darwin-amd64 -o /usr/local/bin/helm
     ```
   * For macOS on ARM (Apple Silicon):

     ```
     # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-darwin-arm64 -o /usr/local/bin/helm
     ```
2. Make the binary file executable:

   ```
   # chmod +x /usr/local/bin/helm
   ```
3. Check the installed version:

   ```
   $ helm version
   ```

   **Example output**

   ```
   version.BuildInfo{Version:"v3.0", GitCommit:"b31719aab7963acf4887a1c1e6d5e53378e34d93", GitTreeState:"clean", GoVersion:"go1.13.4"}
   ```

### [6.3. Configuring custom Helm chart repositories](#configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

You can create Helm releases on an OpenShift Container Platform cluster using the following methods:

* The CLI.
* The **Developer** perspective of the web console.

The **Developer Catalog**, in the **Developer** perspective of the web console, displays the Helm charts available in the cluster. By default, it lists the Helm charts from the Red Hat OpenShift Helm chart repository. For a list of the charts, see [the Red Hat `Helm index` file](https://charts.openshift.io/index.yaml).

As a cluster administrator, you can add multiple cluster-scoped and namespace-scoped Helm chart repositories, separate from the default cluster-scoped Helm repository, and display the Helm charts from these repositories in the **Developer Catalog**.

As a regular user or project member with the appropriate role-based access control (RBAC) permissions, you can add multiple namespace-scoped Helm chart repositories, apart from the default cluster-scoped Helm repository, and display the Helm charts from these repositories in the **Developer Catalog**.

In the **Developer** perspective of the web console, you can use the **Helm** page to:

* Create Helm Releases and Repositories using the **Create** button.
* Create, update, or delete a cluster-scoped or namespace-scoped Helm chart repository.
* View the list of the existing Helm chart repositories in the Repositories tab, which can also be easily distinguished as either cluster scoped or namespace scoped.

#### [6.3.1. Installing a Helm chart on an OpenShift Container Platform cluster](#installing-a-helm-chart-on-an-openshift-cluster_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

**Prerequisites**

* You have a running OpenShift Container Platform cluster and you have logged into it.
* You have installed Helm.

**Procedure**

1. Create a new project:

   ```
   $ oc new-project vault
   ```
2. Add a repository of Helm charts to your local Helm client:

   ```
   $ helm repo add openshift-helm-charts https://charts.openshift.io/
   ```

   **Example output**

   ```
   "openshift-helm-charts" has been added to your repositories
   ```
3. Update the repository:

   ```
   $ helm repo update
   ```
4. Install an example HashiCorp Vault:

   ```
   $ helm install example-vault openshift-helm-charts/hashicorp-vault
   ```

   **Example output**

   ```
   NAME: example-vault
   LAST DEPLOYED: Fri Mar 11 12:02:12 2022
   NAMESPACE: vault
   STATUS: deployed
   REVISION: 1
   NOTES:
   Thank you for installing HashiCorp Vault!
   ```
5. Verify that the chart has installed successfully:

   ```
   $ helm list
   ```

   **Example output**

   ```
   NAME         	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART       	APP VERSION
   example-vault	vault    	1       	2022-03-11 12:02:12.296226673 +0530 IST	deployed	vault-0.19.0	1.9.2
   ```

#### [6.3.2. Creating Helm releases using the Developer perspective](#odc-creating-helm-releases-using-developer-perspective_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

You can use either the **Developer** perspective in the web console or the CLI to select and create a release from the Helm charts listed in the **Developer Catalog**. You can create Helm releases by installing Helm charts and see them in the **Developer** perspective of the web console.

**Prerequisites**

* You have logged in to the web console and have switched to [the **Developer** perspective](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#about-developer-perspective_web-console-overview).

**Procedure**

To create Helm releases from the Helm charts provided in the **Developer Catalog**:

1. In the **Developer** perspective, navigate to the **+Add** view and select a project. Then click **Helm Chart** option to see all the Helm Charts in the **Developer Catalog**.
2. Select a chart and read the description, README, and other details about the chart.
3. Click **Create**.

   **Figure 6.1. Helm charts in developer catalog**
4. In the **Create Helm Release** page:

   1. Enter a unique name for the release in the **Release Name** field.
   2. Select the required chart version from the **Chart Version** drop-down list.
   3. Configure your Helm chart by using the **Form View** or the **YAML View**.

      Note

      Where available, you can switch between the **YAML View** and **Form View**. The data is persisted when switching between the views.
   4. Click **Create** to create a Helm release. The web console displays the new release in the **Topology** view.

      If a Helm chart has release notes, the web console displays them.

      If a Helm chart creates workloads, the web console displays them on the **Topology** or **Helm release details** page. The workloads are `DaemonSet`, `CronJob`, `Pod`, `Deployment`, and `DeploymentConfig`.
   5. View the newly created Helm release in the **Helm Releases** page.

You can upgrade, rollback, or delete a Helm release by using the **Actions** button on the side panel or by right-clicking a Helm release.

#### [6.3.3. Using Helm in the web terminal](#using-helm-in-the-web-terminal) Copy linkLink copied to clipboard!

You can use Helm by [Accessing the web terminal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#odc-access-web-terminal_odc-using-web-terminal) in the **Developer** perspective of the web console.

#### [6.3.4. Creating a custom Helm chart on OpenShift Container Platform](#creating-a-custom-helm-chart-on-openshift_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

**Procedure**

1. Create a new project:

   ```
   $ oc new-project nodejs-ex-k
   ```
2. Download an example Node.js chart that contains OpenShift Container Platform objects:

   ```
   $ git clone https://github.com/redhat-developer/redhat-helm-charts
   ```
3. Go to the directory with the sample chart:

   ```
   $ cd redhat-helm-charts/alpha/nodejs-ex-k/
   ```
4. Edit the `Chart.yaml` file and add a description of your chart:

   ```
   apiVersion: v2
   ```

   1

   ```
   name: nodejs-ex-k
   ```

   2

   ```
   description: A Helm chart for OpenShift
   ```

   3

   ```
   icon: https://static.redhat.com/libs/redhat/brand-assets/latest/corp/logo.svg
   ```

   4

   ```
   version: 0.2.1
   ```

   5

   [1](#CO1-1)
   :   The chart API version. It should be `v2` for Helm charts that require at least Helm 3.

   [2](#CO1-2)
   :   The name of your chart.

   [3](#CO1-3)
   :   The description of your chart.

   [4](#CO1-4)
   :   The URL to an image to be used as an icon.

   [5](#CO1-5)
   :   The Version of your chart as per the Semantic Versioning (SemVer) 2.0.0 Specification.
5. Verify that the chart is formatted properly:

   ```
   $ helm lint
   ```

   **Example output**

   ```
   [INFO] Chart.yaml: icon is recommended

   1 chart(s) linted, 0 chart(s) failed
   ```
6. Navigate to the previous directory level:

   ```
   $ cd ..
   ```
7. Install the chart:

   ```
   $ helm install nodejs-chart nodejs-ex-k
   ```
8. Verify that the chart has installed successfully:

   ```
   $ helm list
   ```

   **Example output**

   ```
   NAME NAMESPACE REVISION UPDATED STATUS CHART APP VERSION
   nodejs-chart nodejs-ex-k 1 2019-12-05 15:06:51.379134163 -0500 EST deployed nodejs-0.1.0  1.16.0
   ```

#### [6.3.5. Adding custom Helm chart repositories](#adding-helm-chart-repositories_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

As a cluster administrator, you can add custom Helm chart repositories to your cluster and enable access to the Helm charts from these repositories in the **Developer Catalog**.

**Procedure**

1. To add a new Helm Chart Repository, you must add the Helm Chart Repository custom resource (CR) to your cluster.

   **Sample Helm Chart Repository CR**

   ```
   apiVersion: helm.openshift.io/v1beta1
   kind: HelmChartRepository
   metadata:
     name: <name>
   spec:
    # optional name that might be used by console
    # name: <chart-display-name>
     connectionConfig:
       url: <helm-chart-repository-url>
   ```

   For example, to add an Azure sample chart repository, run:

   ```
   $ cat <<EOF | oc apply -f -
   apiVersion: helm.openshift.io/v1beta1
   kind: HelmChartRepository
   metadata:
     name: azure-sample-repo
   spec:
     name: azure-sample-repo
     connectionConfig:
       url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
   EOF
   ```
2. Navigate to the **Developer Catalog** in the web console to verify that the Helm charts from the chart repository are displayed.

   For example, use the **Chart repositories** filter to search for a Helm chart from the repository.

   **Figure 6.2. Chart repositories filter**

   Note

   If a cluster administrator removes all of the chart repositories, then you cannot view the Helm option in the **+Add** view, **Developer Catalog**, and left navigation panel.

#### [6.3.6. Adding namespace-scoped custom Helm chart repositories](#adding-namespace-scoped-helm-chart-repositories_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

The cluster-scoped `HelmChartRepository` custom resource definition (CRD) for Helm repository provides the ability for administrators to add Helm repositories as custom resources. The namespace-scoped `ProjectHelmChartRepository` CRD allows project members with the appropriate role-based access control (RBAC) permissions to create Helm repository resources of their choice but scoped to their namespace. Such project members can see charts from both cluster-scoped and namespace-scoped Helm repository resources.

Note

* Administrators can limit users from creating namespace-scoped Helm repository resources. By limiting users, administrators have the flexibility to control the RBAC through a namespace role instead of a cluster role. This avoids unnecessary permission elevation for the user and prevents access to unauthorized services or applications.
* The addition of the namespace-scoped Helm repository does not impact the behavior of the existing cluster-scoped Helm repository.

As a regular user or project member with the appropriate RBAC permissions, you can add custom namespace-scoped Helm chart repositories to your cluster and enable access to the Helm charts from these repositories in the **Developer Catalog**.

**Procedure**

1. To add a new namespace-scoped Helm Chart Repository, you must add the Helm Chart Repository custom resource (CR) to your namespace.

   **Sample Namespace-scoped Helm Chart Repository CR**

   ```
   apiVersion: helm.openshift.io/v1beta1
   kind: ProjectHelmChartRepository
   metadata:
     name: <name>
   spec:
     url: https://my.chart-repo.org/stable

     # optional name that might be used by console
     name: <chart-repo-display-name>

     # optional and only needed for UI purposes
     description: <My private chart repo>

     # required: chart repository URL
     connectionConfig:
       url: <helm-chart-repository-url>
   ```

   For example, to add an Azure sample chart repository scoped to your `my-namespace` namespace, run:

   ```
   $ cat <<EOF | oc apply --namespace my-namespace -f -
   apiVersion: helm.openshift.io/v1beta1
   kind: ProjectHelmChartRepository
   metadata:
     name: azure-sample-repo
   spec:
     name: azure-sample-repo
     connectionConfig:
       url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
   EOF
   ```

   The output verifies that the namespace-scoped Helm Chart Repository CR is created:

   **Example output**

   ```
   projecthelmchartrepository.helm.openshift.io/azure-sample-repo created
   ```
2. Navigate to the **Developer Catalog** in the web console to verify that the Helm charts from the chart repository are displayed in your `my-namespace` namespace.

   For example, use the **Chart repositories** filter to search for a Helm chart from the repository.

   **Figure 6.3. Chart repositories filter in your namespace**

   Alternatively, run:

   ```
   $ oc get projecthelmchartrepositories --namespace my-namespace
   ```

   **Example output**

   ```
   NAME                     AGE
   azure-sample-repo        1m
   ```

   Note

   If a cluster administrator or a regular user with appropriate RBAC permissions removes all of the chart repositories in a specific namespace, then you cannot view the Helm option in the **+Add** view, **Developer Catalog**, and left navigation panel for that specific namespace.

#### [6.3.7. Creating credentials and CA certificates to add Helm chart repositories](#creating-credentials-and-certificates-to-add-helm-repositories_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

Some Helm chart repositories need credentials and custom certificate authority (CA) certificates to connect to it. You can use the web console as well as the CLI to add credentials and certificates.

**Procedure**

To configure the credentials and certificates, and then add a Helm chart repository using the CLI:

1. In the `openshift-config` namespace, create a `ConfigMap` object with a custom CA certificate in PEM encoded format, and store it under the `ca-bundle.crt` key within the config map:

   ```
   $ oc create configmap helm-ca-cert \
   --from-file=ca-bundle.crt=/path/to/certs/ca.crt \
   -n openshift-config
   ```
2. In the `openshift-config` namespace, create a `Secret` object to add the client TLS configurations:

   ```
   $ oc create secret tls helm-tls-configs \
   --cert=/path/to/certs/client.crt \
   --key=/path/to/certs/client.key \
   -n openshift-config
   ```

   Note that the client certificate and key must be in PEM encoded format and stored under the keys `tls.crt` and `tls.key`, respectively.
3. Add the Helm repository as follows:

   ```
   $ cat <<EOF | oc apply -f -
   apiVersion: helm.openshift.io/v1beta1
   kind: HelmChartRepository
   metadata:
     name: <helm-repository>
   spec:
     name: <helm-repository>
     connectionConfig:
       url: <URL for the Helm repository>
       tlsConfig:
           name: helm-tls-configs
       ca:
   	name: helm-ca-cert
   EOF
   ```

   The `ConfigMap` and `Secret` are consumed in the HelmChartRepository CR using the `tlsConfig` and `ca` fields. These certificates are used to connect to the Helm repository URL.
4. By default, all authenticated users have access to all configured charts. However, for chart repositories where certificates are needed, you must provide users with read access to the `helm-ca-cert` config map and `helm-tls-configs` secret in the `openshift-config` namespace, as follows:

   ```
   $ cat <<EOF | kubectl apply -f -
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     namespace: openshift-config
     name: helm-chartrepos-tls-conf-viewer
   rules:
   - apiGroups: [""]
     resources: ["configmaps"]
     resourceNames: ["helm-ca-cert"]
     verbs: ["get"]
   - apiGroups: [""]
     resources: ["secrets"]
     resourceNames: ["helm-tls-configs"]
     verbs: ["get"]
   ---
   kind: RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   metadata:
     namespace: openshift-config
     name: helm-chartrepos-tls-conf-viewer
   subjects:
     - kind: Group
       apiGroup: rbac.authorization.k8s.io
       name: 'system:authenticated'
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: helm-chartrepos-tls-conf-viewer
   EOF
   ```

#### [6.3.8. Filtering Helm Charts by their certification level](#filtering-helm-charts-by-certification-level_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

You can filter Helm charts based on their certification level in the **Developer Catalog**.

**Procedure**

1. In the **Developer** perspective, navigate to the **+Add** view and select a project.
2. From the **Developer Catalog** tile, select the **Helm Chart** option to see all the Helm charts in the **Developer Catalog**.
3. Use the filters to the left of the list of Helm charts to filter the required charts:

   * Use the **Chart Repositories** filter to filter charts provided by **Red Hat Certification Charts** or **OpenShift Helm Charts**.
   * Use the **Source** filter to filter charts sourced from **Partners**, **Community**, or **Red Hat**. Certified charts are indicated with the (
     ) icon.

Note

The **Source** filter will not be visible when there is only one provider type.

You can now select the required chart and install it.

#### [6.3.9. Disabling Helm Chart repositories](#helm-disabling-helm-chart-repositories_configuring-custom-helm-chart-repositories) Copy linkLink copied to clipboard!

You can disable Helm Charts from a particular Helm Chart Repository in the catalog by setting the `disabled` property in the `HelmChartRepository` custom resource to `true`.

**Procedure**

* To disable a Helm Chart repository by using CLI, add the `disabled: true` flag to the custom resource. For example, to remove an Azure sample chart repository, run:

  ```
  $ cat <<EOF | oc apply -f -
  apiVersion: helm.openshift.io/v1beta1
  kind: HelmChartRepository
  metadata:
    name: azure-sample-repo
  spec:
    connectionConfig:
     url:https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
    disabled: true
  EOF
  ```
* To disable a recently added Helm Chart repository by using Web Console:

  1. Go to **Custom Resource Definitions** and search for the `HelmChartRepository` custom resource.
  2. Go to **Instances**, find the repository you want to disable, and click its name.
  3. Go to the **YAML** tab, add the `disabled: true` flag in the `spec` section, and click `Save`.

     **Example**

     ```
     spec:
       connectionConfig:
         url: <url-of-the-repositoru-to-be-disabled>
       disabled: true
     ```

     The repository is now disabled and will not appear in the catalog.

### [6.4. Working with Helm releases](#odc-working-with-helm-releases) Copy linkLink copied to clipboard!

You can use the web console to create, update, roll back, or delete a Helm release.

#### [6.4.1. Installing a Helm release from a URL](#odc-creating-helm-release-from-url_working-with-helm-releases) Copy linkLink copied to clipboard!

A Helm release is a deployed instance of a Helm chart within your OpenShift Container Platform cluster. You can install charts from the developer catalog or by using a direct chart URL. Using a direct URL avoids the need for a configured Helm repository. However, this method circumvents the validation provided by the developer catalog. Use the direct URL method only when a chart is not available from the developer catalog or configured repositories.

Warning

Installing a Helm chart from a direct URL bypasses the validation checks provided by the developer catalog. Install charts only from URLs you trust, because unverified charts can introduce security risks to your cluster. When possible, use charts from the developer catalog or a configured Helm repository instead.

**Prerequisites**

* You’ve logged in to the OpenShift Container Platform web console.
* You have the necessary project permissions to install a Helm chart.
* You have a URL for a Helm chart.

**Procedure**

1. In the OpenShift Container Platform web console, select **Ecosystem > Helm** from the navigation menu. The **Helm** view opens.
2. In the **Project** drop-down menu, select the project where you want to install the Helm release; for example, **default**.
3. From the **Helm Releases** tab, click **Create**.
4. Select **Helm chart URL**. The **Install Helm chart from URL** view opens.
5. In the **Chart URL** field, enter the URL for the Helm chart you want to install.

   Note

   For Helm charts stored in an OCI-compliant registry, the URL must use the `oci://` protocol; for example, `oci://quay.io/organization/repository/chart-name`.
6. In the **Release name** field, enter a name for the Helm release you want to install.
7. In the **Chart version** field, enter the chart version number if it is not detected automatically.
8. Click **Next**. The **Configure Helm release** view opens.

   * Review the configuration. Make sure that **Chart URL**, **Release name**, and **Chart version** are correct.
9. For the **Configure via** option, select either **Form view** or **YAML view**.

   * Choose **Form view** (the default) for a guided configuration of standard parameters.
   * Choose **YAML view** if you need to modify advanced settings that are not available in the form view.

     Note

     The **Form view** might not display every field from your Helm chart. For full control over all configuration parameters, select **YAML view**.
10. Click **Install**. The **Helm Releases** tab opens and, if the release installation is successful, its status is **Deployed**.

**Verification**

* The new Helm release is listed in the table on the **Helm Releases** tab.
* The **Status** column for the Helm release displays **Deployed**.

#### [6.4.2. Upgrading a Helm release](#odc-upgrading-helm-release_working-with-helm-releases) Copy linkLink copied to clipboard!

You can upgrade a Helm release to use a new chart version or update your release configuration.

**Procedure**

1. In the **Topology** view, select the Helm release to see the side panel.
2. Click **Actions > Upgrade Helm Release**.
3. On the **Upgrade Helm Release** page, if you can edit the **Chart Version** field, select the chart version you want to upgrade to, edit the values as needed, then click **Upgrade** to create a revision of the Helm release. The **Helm Releases** page shows both revisions.

   Note

   If you installed the Helm chart using a direct URL, you can’t change **Chart Version**. Instead, edit the values in **Form view** or **YAML view**.

#### [6.4.3. Rolling back a Helm release](#odc-rolling-back-helm-release_working-with-helm-releases) Copy linkLink copied to clipboard!

If a release fails, you can rollback the Helm release to a previous version.

**Procedure**

To rollback a release using the **Helm** view:

1. In the **Developer** perspective, navigate to the **Helm** view to see the **Helm Releases** in the namespace.
2. Click the Options menu
   adjoining the listed release, and select **Rollback**.
3. In the **Rollback Helm Release** page, select the **Revision** you want to rollback to and click **Rollback**.
4. In the **Helm Releases** page, click on the chart to see the details and resources for that release.
5. Go to the **Revision History** tab to see all the revisions for the chart.

   **Figure 6.4. Helm revision history**
6. If required, you can further use the Options menu
   adjoining a particular revision and select the revision to rollback to.

#### [6.4.4. Deleting a Helm release](#odc-deleting-helm-release_working-with-helm-releases) Copy linkLink copied to clipboard!

**Procedure**

1. In the **Topology** view, right-click the Helm release and select **Delete Helm Release**.
2. In the confirmation prompt, enter the name of the chart and click **Delete**.

## [Chapter 7. Deployments](#deployments) Copy linkLink copied to clipboard!

### [7.1. Understanding deployments](#what-deployments-are) Copy linkLink copied to clipboard!

You can use `Deployment` and `DeploymentConfig` objects in OpenShift Container Platform to describe the desired state of an application and to manage pods through replica sets or replication controllers. Use `Deployment` objects unless you need a feature that only `DeploymentConfig` objects provide.

The `Deployment` and `DeploymentConfig` API objects provide two similar but different methods for fine-grained management over common user applications. They are composed of the following separate API objects:

* A `Deployment` or `DeploymentConfig` object, either of which describes the desired state of a particular component of the application as a pod template.
* `Deployment` objects involve one or more *replica sets*, which contain a point-in-time record of the state of a deployment as a pod template. Similarly, `DeploymentConfig` objects involve one or more *replication controllers*, which preceded replica sets.
* One or more pods, which represent an instance of a particular version of an application.

Important

As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.

Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

#### [7.1.1. Building blocks of a deployment](#what-deployments-are-build-blocks) Copy linkLink copied to clipboard!

Deployments and deployment configs are enabled by the use of native Kubernetes API objects `ReplicaSet` and `ReplicationController`, respectively, as their building blocks.

Users do not have to manipulate replica sets, replication controllers, or pods owned by `Deployment` or `DeploymentConfig` objects. The deployment systems ensure changes are propagated appropriately.

Tip

If the existing deployment strategies are not suited for your use case and you must run manual steps during the lifecycle of your deployment, then you should consider creating a custom deployment strategy.

The following sections provide further details on these objects.

##### [7.1.1.1. Replica sets](#deployments-replicasets_what-deployments-are) Copy linkLink copied to clipboard!

To keep a specified number of identical pods running in OpenShift Container Platform, you can use a Kubernetes `ReplicaSet` object. Deployments create and manage replica sets for you, so use a replica set directly only when you need custom update orchestration or no updates at all.

Note

Only use replica sets if you require custom update orchestration or do not require updates at all. Otherwise, use deployments. Replica sets can be used independently, but are used by deployments to orchestrate pod creation, deletion, and updates. Deployments manage their replica sets automatically, provide declarative updates to pods, and do not have to manually manage the replica sets that they create.

The following is an example `ReplicaSet` definition:

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend-1
  labels:
    tier: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
    matchExpressions:
      - {key: tier, operator: In, values: [frontend]}
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
```

* `spec.selector` is a label query over a set of resources. The result of `matchLabels` and `matchExpressions` are logically conjoined.
* `spec.selector.matchLabels` is an equality-based selector that specifies resources with labels that match the selector.
* `spec.selector.matchExpressions` is a set-based selector that filters keys. This parameter selects all resources with key equal to `tier` and value equal to `frontend`.

##### [7.1.1.2. Replication controllers](#deployments-replicationcontrollers_what-deployments-are) Copy linkLink copied to clipboard!

To keep a specified number of identical pods running in OpenShift Container Platform, you can use a replication controller. Create one through a `DeploymentConfig` object rather than directly, and use a replica set instead when you need set-based selectors or custom update orchestration.

Similar to a replica set, a replication controller ensures that a specified number of replicas of a pod are running at all times. If pods exit or are deleted, the replication controller instantiates more up to the defined number. Likewise, if there are more running than desired, it deletes as many as necessary to match the defined amount. The difference between a replica set and a replication controller is that a replica set supports set-based selector requirements whereas a replication controller only supports equality-based selector requirements.

A replication controller configuration consists of:

* The number of replicas desired, which can be adjusted at run time.
* A `Pod` definition to use when creating a replicated pod.
* A selector for identifying managed pods.

A selector is a set of labels assigned to the pods that are managed by the replication controller. These labels are included in the `Pod` definition that the replication controller instantiates. The replication controller uses the selector to determine how many instances of the pod are already running in order to adjust as needed.

The replication controller does not perform auto-scaling based on load or traffic, as it does not track either. Rather, this requires its replica count to be adjusted by an external auto-scaler.

Note

Use a `DeploymentConfig` to create a replication controller instead of creating replication controllers directly.

If you require custom orchestration or do not require updates, use replica sets instead of replication controllers.

The following is an example definition of a replication controller:

```
apiVersion: v1
kind: ReplicationController
metadata:
  name: frontend-1
spec:
  replicas: 1
  selector:
    name: frontend
  template:
    metadata:
      labels:
        name: frontend
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
```

* `spec.replicas` specifies the number of copies of the pod to run.
* `spec.selector` specifies the label selector of the pod to run.
* `spec.template` specifies the template for the pod the controller creates.
* `spec.template.metadata.labels` specifies the labels that the pod should include from the label selector.
* `spec.template.metadata.labels.name` specifies the name of the labels. The maximum name length after expanding any parameters is 63 characters.

#### [7.1.2. Deployments](#deployments-kube-deployments_what-deployments-are) Copy linkLink copied to clipboard!

To run and update application pods in OpenShift Container Platform, you can use a Kubernetes `Deployment` object. A deployment describes the desired state of an application component as a pod template and creates replica sets that manage pod lifecycles.

For example, the following deployment definition creates a replica set to bring up one `hello-openshift` pod:

**Deployment definition**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-openshift
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-openshift
  template:
    metadata:
      labels:
        app: hello-openshift
    spec:
      containers:
      - name: hello-openshift
        image: openshift/hello-openshift:latest
        ports:
        - containerPort: 80
```

#### [7.1.3. DeploymentConfig objects](#deployments-and-deploymentconfigs_what-deployments-are) Copy linkLink copied to clipboard!

Important

As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.

Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

You can use `DeploymentConfig` objects in OpenShift Container Platform to roll out image updates, run lifecycle hooks, trigger automated deployments, and scale or roll back applications. A `DeploymentConfig` object builds on replication controllers to manage the application deployment lifecycle.

Building on replication controllers, OpenShift Container Platform adds expanded support for the software development and deployment lifecycle with the concept of `DeploymentConfig` objects. In the simplest case, a `DeploymentConfig` object creates a new replication controller and lets it start up pods.

However, OpenShift Container Platform deployments from `DeploymentConfig` objects also provide the ability to transition from an existing deployment of an image to a new one and also define hooks to be run before or after creating the replication controller.

The `DeploymentConfig` deployment system provides the following capabilities:

* A `DeploymentConfig` object, which is a template for running applications.
* Triggers that drive automated deployments in response to events.
* User-customizable deployment strategies to transition from the previous version to the new version. A strategy runs inside a pod commonly referred as the deployment process.
* A set of hooks (lifecycle hooks) for executing custom behavior in different points during the lifecycle of a deployment.
* Versioning of your application to support rollbacks either manually or automatically in case of deployment failure.
* Manual replication scaling and autoscaling.

When you create a `DeploymentConfig` object, a replication controller is created representing the `DeploymentConfig` object’s pod template. If the deployment changes, a new replication controller is created with the latest pod template, and a deployment process runs to scale down the old replication controller and scale up the new one.

Instances of your application are automatically added and removed from both service load balancers and routers as they are created. As long as your application supports graceful shutdown when it receives the `TERM` signal, you can ensure that running user connections are given a chance to complete normally.

The OpenShift Container Platform `DeploymentConfig` object defines the following details:

1. The elements of a `ReplicationController` definition.
2. Triggers for creating a new deployment automatically.
3. The strategy for transitioning between deployments.
4. Lifecycle hooks.

Each time a deployment is triggered, whether manually or automatically, a deployer pod manages the deployment (including scaling down the old replication controller, scaling up the new one, and running hooks). The deployment pod remains for an indefinite amount of time after it completes the deployment to retain its logs of the deployment. When a deployment is superseded by another, the previous replication controller is retained to enable easy rollback if needed.

**Example `DeploymentConfig` definition**

```
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: frontend
spec:
  replicas: 5
  selector:
    name: frontend
  template: { ... }
  triggers:
  - type: ConfigChange
  - imageChangeParams:
      automatic: true
      containerNames:
      - helloworld
      from:
        kind: ImageStreamTag
        name: hello-openshift:latest
    type: ImageChange
  strategy:
    type: Rolling
```

* `spec.triggers.type.ConfigChange` is a configuration change trigger that creates a new replication controller whenever changes are detected in the pod template of the deployment configuration.
* `spec.triggers.type.ImageChange` is an image change trigger that causes a new deployment to be created each time a new version of the backing image is available in the named image stream.
* `spec.strategy.type.Rolling` is the default strategy that makes a downtime-free transition between deployments.

#### [7.1.4. Comparing Deployment and DeploymentConfig objects](#deployments-comparing-deploymentconfigs_what-deployments-are) Copy linkLink copied to clipboard!

You can use both Kubernetes `Deployment` objects and OpenShift Container Platform `DeploymentConfig` objects to manage application rollouts. Before deciding which to use, understand the differences between the two objects in design and supported features.

Use `Deployment` objects unless you need a capability that only `DeploymentConfig` objects provide.

The following sections go into more detail on the differences between the two object types to further help you decide which type to use.

Important

As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.

Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

##### [7.1.4.1. Design](#deployments-design_what-deployments-are) Copy linkLink copied to clipboard!

One important difference between `Deployment` and `DeploymentConfig` objects is the properties of the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) that each design has chosen for the rollout process. `DeploymentConfig` objects prefer consistency, whereas `Deployments` objects take availability over consistency.

For `DeploymentConfig` objects, if a node running a deployer pod goes down, it will not get replaced. The process waits until the node comes back online or is manually deleted. Manually deleting the node also deletes the corresponding pod. This means that you can not delete the pod to unstick the rollout, as the kubelet is responsible for deleting the associated pod.

However, deployment rollouts are driven from a controller manager. The controller manager runs in high availability mode on masters and uses leader election algorithms to value availability over consistency. During a failure it is possible for other masters to act on the same deployment at the same time, but this issue will be reconciled shortly after the failure occurs.

##### [7.1.4.2. Deployment-specific features](#deployment-specific-features_what-deployments-are) Copy linkLink copied to clipboard!

You can use `Deployment` objects in OpenShift Container Platform to roll out multiple sets of rollouts, scale ongoing rollouts during updates, or pause mid-rollout. These capabilities differ from `DeploymentConfig` objects and can make application updates faster and more flexible.

##### [7.1.4.2.1. Rollover](#deployment-specific-features-rollover_what-deployments-are) Copy linkLink copied to clipboard!

The deployment process for `Deployment` objects is driven by a controller loop, in contrast to `DeploymentConfig` objects that use deployer pods for every new rollout. This means that the `Deployment` object can have as many active replica sets as possible, and eventually the deployment controller will scale down all old replica sets and scale up the newest one.

`DeploymentConfig` objects can have at most one deployer pod running, otherwise multiple deployers might conflict when trying to scale up what they think should be the newest replication controller. Because of this, only two replication controllers can be active at any point in time. Ultimately, this results in faster rapid rollouts for `Deployment` objects.

##### [7.1.4.2.2. Proportional scaling](#deployment-specific-features-proportional-scaling_what-deployments-are) Copy linkLink copied to clipboard!

Because the deployment controller is the sole source of truth for the sizes of new and old replica sets owned by a `Deployment` object, it can scale ongoing rollouts. Additional replicas are distributed proportionally based on the size of each replica set.

`DeploymentConfig` objects cannot be scaled when a rollout is ongoing because the controller will have issues with the deployer process about the size of the new replication controller.

##### [7.1.4.2.3. Pausing mid-rollout](#deployment-specific-features-pausing-mid-rollout_what-deployments-are) Copy linkLink copied to clipboard!

Deployments can be paused at any point in time, meaning you can also pause ongoing rollouts. However, you currently cannot pause deployer pods; if you try to pause a deployment in the middle of a rollout, the deployer process is not affected and continues until it finishes.

##### [7.1.4.3. DeploymentConfig object-specific features](#deploymentconfig-object-specific-features_what-deployments-are) Copy linkLink copied to clipboard!

When using `DeploymentConfig` objects in OpenShift Container Platform, you can set Lifecycle hooks and configure custom deployment strategies. `DeploymentConfig` objects also provide automatic replica set rollbacks upon failure and automatic roll out of updates.

These capabilities are specific to `DeploymentConfig` objects and are not available on Kubernetes `Deployment` objects.

##### [7.1.4.3.1. Automatic rollbacks](#deploymentconfig-object-specific-features-automatic-rollbacks_what-deployments-are) Copy linkLink copied to clipboard!

Currently, deployments do not support automatically rolling back to the last successfully deployed replica set in case of a failure.

##### [7.1.4.3.2. Triggers](#deploymentconfig-object-specific-features-triggers_what-deployments-are) Copy linkLink copied to clipboard!

Deployments have an implicit config change trigger in that every change in the pod template of a deployment automatically triggers a new rollout. If you do not want new rollouts on pod template changes, pause the deployment:

```
$ oc rollout pause deployments/<name>
```

##### [7.1.4.3.3. Lifecycle hooks](#deploymentconfig-object-specific-features-lifecycle-hooks_what-deployments-are) Copy linkLink copied to clipboard!

Deployments do not yet support any lifecycle hooks.

##### [7.1.4.3.4. Custom strategies](#deploymentconfig-object-specific-features-custom-strategies_what-deployments-are) Copy linkLink copied to clipboard!

Deployments do not support user-specified custom deployment strategies.

### [7.2. Managing deployment processes](#deployment-operations) Copy linkLink copied to clipboard!

#### [7.2.1. Managing DeploymentConfig objects](#deploymentconfig-operations) Copy linkLink copied to clipboard!

Important

As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.

Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

You can manage `DeploymentConfig` objects from the OpenShift Container Platform web console’s **Workloads** page or by using the `oc` CLI, depending on your preference.

The following procedures show CLI usage unless otherwise stated.

##### [7.2.1.1. Starting a deployment](#deployments-starting-a-deployment_deployment-operations) Copy linkLink copied to clipboard!

To begin a new rollout of your application in OpenShift Container Platform, you can start a deployment from an existing `DeploymentConfig` object. Use the `oc rollout latest` command to create a new replication controller and run the deployment process.

**Procedure**

1. To start a new deployment process from an existing `DeploymentConfig` object, run the following command:

   ```
   $ oc rollout latest dc/<name>
   ```

   Note

   If a deployment process is already in progress, the command displays a message and a new replication controller will not be deployed.

##### [7.2.1.2. Viewing a deployment](#deployments-viewing-a-deployment_deployment-operations) Copy linkLink copied to clipboard!

To review the rollout history of your application in OpenShift Container Platform, you can view a deployment. Use the `oc rollout history` and `oc describe` commands to inspect revisions of a `DeploymentConfig` object.

**Procedure**

1. To show details about all recently created replication controllers for the provided `DeploymentConfig` object, including any currently running deployment process, run the following command:

   ```
   $ oc rollout history dc/<name>
   ```
2. To view details specific to a revision, add the `--revision` flag:

   ```
   $ oc rollout history dc/<name> --revision=1
   ```
3. For more detailed information about a `DeploymentConfig` object and its latest revision, use the `oc describe` command:

   ```
   $ oc describe dc <name>
   ```

##### [7.2.1.3. Retrying a deployment](#deployments-retrying-deployment_deployment-operations) Copy linkLink copied to clipboard!

To restart a failed rollout of a `DeploymentConfig` object in OpenShift Container Platform, you can retry the deployment. Use the `oc rollout retry` command to restart the same revision without creating a new deployment revision.

**Procedure**

1. To restart a failed deployment process:

   ```
   $ oc rollout retry dc/<name>
   ```

   If the latest revision of it was deployed successfully, the command displays a message and the deployment process is not retried.

   Note

   Retrying a deployment restarts the deployment process and does not create a new deployment revision. The restarted replication controller has the same configuration it had when it failed.

##### [7.2.1.4. Rolling back a deployment](#deployments-rolling-back_deployment-operations) Copy linkLink copied to clipboard!

To revert an application to a previous revision, you can perform a roll back by using the REST API, the CLI, or the web console.

**Procedure**

1. To rollback to the last successful deployed revision of your configuration:

   ```
   $ oc rollout undo dc/<name>
   ```

   The `DeploymentConfig` object’s template is reverted to match the deployment revision specified in the undo command, and a new replication controller is started. If no revision is specified with `--to-revision`, then the last successfully deployed revision is used.
2. Image change triggers on the `DeploymentConfig` object are disabled as part of the rollback to prevent accidentally starting a new deployment process soon after the rollback is complete.

   To re-enable the image change triggers:

   ```
   $ oc set triggers dc/<name> --auto
   ```

Note

Deployment configs also support automatically rolling back to the last successful revision of the configuration in case the latest deployment process fails. In that case, the latest template that failed to deploy stays intact by the system and it is up to users to fix their configurations.

##### [7.2.1.5. Executing commands inside a container](#deployments-exe-cmd-in-container_deployment-operations) Copy linkLink copied to clipboard!

To change how a container starts in a `DeploymentConfig` object in OpenShift Container Platform, you can set a `command` and optional `args` in the pod template. These values override the image `ENTRYPOINT` and differ from lifecycle hooks, which run once per deployment at a specified time.

**Procedure**

1. Add the `command` parameters to the `spec` field of the `DeploymentConfig` object. You can also add an `args` field, which modifies the `command` (or the `ENTRYPOINT` if `command` does not exist).

   ```
   kind: DeploymentConfig
   apiVersion: apps.openshift.io/v1
   metadata:
     name: example-dc
   # ...
   spec:
     template:
   # ...
       spec:
        containers:
        - name: <container_name>
          image: 'image'
          command:
            - '<command>'
          args:
            - '<argument_1>'
            - '<argument_2>'
            - '<argument_3>'
   ```

   For example, to execute the `java` command with the `-jar` and `/opt/app-root/springboots2idemo.jar` arguments:

   ```
   kind: DeploymentConfig
   apiVersion: apps.openshift.io/v1
   metadata:
     name: example-dc
   # ...
   spec:
     template:
   # ...
       spec:
         containers:
           - name: example-spring-boot
             image: 'image'
             command:
               - java
             args:
               - '-jar'
               - /opt/app-root/springboots2idemo.jar
   # ...
   ```

##### [7.2.1.6. Viewing deployment logs](#deployments-viewing-logs_deployment-operations) Copy linkLink copied to clipboard!

To troubleshoot a rollout in OpenShift Container Platform, you can view deployment logs for a `DeploymentConfig` object. Use the `oc logs` command to stream logs from the latest revision or from an older failed deployment process.

**Procedure**

1. To stream the logs of the latest revision for a given `DeploymentConfig` object:

   ```
   $ oc logs -f dc/<name>
   ```

   If the latest revision is running or failed, the command returns the logs of the process that is responsible for deploying your pods. If it is successful, it returns the logs from a pod of your application.
2. You can also view logs from older failed deployment processes, if and only if these processes (old replication controllers and their deployer pods) exist and have not been pruned or deleted manually:

   ```
   $ oc logs --version=1 dc/<name>
   ```

##### [7.2.1.7. Deployment triggers](#deployments-triggers_deployment-operations) Copy linkLink copied to clipboard!

A deployment trigger on a `DeploymentConfig` object in OpenShift Container Platform starts a new deployment process when cluster events occur. Use config change or image change triggers to roll out automatically, or leave triggers empty if you want to start deployments manually.

Warning

If no triggers are defined on a `DeploymentConfig` object, a config change trigger is added by default. If triggers are defined as an empty field, deployments must be started manually.

##### [7.2.1.7.1. Config change deployment triggers](#deployments-configchange-trigger_deployment-operations) Copy linkLink copied to clipboard!

The config change trigger results in a new replication controller whenever configuration changes are detected in the pod template of the `DeploymentConfig` object.

Note

If a config change trigger is defined on a `DeploymentConfig` object, the first replication controller is automatically created soon after the `DeploymentConfig` object itself is created and it is not paused.

**Config change deployment trigger**

```
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  triggers:
    - type: "ConfigChange"
```

##### [7.2.1.7.2. Image change deployment triggers](#deployments-imagechange-trigger_deployment-operations) Copy linkLink copied to clipboard!

The image change trigger results in a new replication controller whenever the content of an image stream tag changes (when a new version of the image is pushed).

**Image change deployment trigger**

```
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  triggers:
    - type: "ImageChange"
      imageChangeParams:
        automatic: true
        from:
          kind: "ImageStreamTag"
          name: "origin-ruby-sample:latest"
          namespace: "myproject"
        containerNames:
          - "helloworld"
```

If the `spec.triggers.imageChangeParams.automatic` field is set to `true`, the trigger is enabled. If `false`, the trigger is disabled.

With the above example, when the `latest` tag value of the `origin-ruby-sample` image stream changes and the new image value differs from the current image specified in the `DeploymentConfig` object’s `helloworld` container, a new replication controller is created using the new image for the `helloworld` container.

Note

If an image change trigger is defined on a `DeploymentConfig` object (with a config change trigger and `automatic=false`, or with `automatic=true`) and the image stream tag pointed by the image change trigger does not exist yet, the initial deployment process will automatically start as soon as an image is imported or pushed by a build to the image stream tag.

##### [7.2.1.7.3. Setting deployment triggers](#deployments-setting-triggers_deployment-operations) Copy linkLink copied to clipboard!

To automatically start a new rollout when an image changes in OpenShift Container Platform, you can set deployment triggers on a `DeploymentConfig` object. Use the `oc set triggers` command to configure an image change trigger for a container.

**Procedure**

1. You can set deployment triggers for a `DeploymentConfig` object using the `oc set triggers` command. For example, to set a image change trigger, use the following command:

   ```
   $ oc set triggers dc/<dc_name> \
       --from-image=<project>/<image>:<tag> -c <container_name>
   ```

##### [7.2.1.8. Setting deployment resources](#deployments-setting-resources_deployment-operations) Copy linkLink copied to clipboard!

To limit CPU, memory, and ephemeral storage used by a deployment in OpenShift Container Platform, you can set resource limits on the deployment strategy. Define limits in the `resources` section so deployer pods do not consume unbounded node capacity.

A deployment is completed by a pod that consumes resources (memory, CPU, and ephemeral storage) on a node. By default, pods consume unbounded node resources. However, if a project specifies default container limits, then pods consume resources up to those limits.

Note

The minimum memory limit for a deployment is 12 MB. If a container fails to start due to a `Cannot allocate memory` pod event, the memory limit is too low. Either increase or remove the memory limit. Removing the limit allows pods to consume unbounded node resources.

You can also limit resource use by specifying resource limits as part of the deployment strategy. Deployment resources can be used with the recreate, rolling, or custom deployment strategies.

**Procedure**

1. In the following example, each of `resources`, `cpu`, `memory`, and `ephemeral-storage` is optional:

   ```
   kind: Deployment
   apiVersion: apps/v1
   metadata:
     name: hello-openshift
   # ...
   spec:
   # ...
     type: "Recreate"
     resources:
       limits:
         cpu: "100m"
         memory: "256Mi"
         ephemeral-storage: "1Gi"
   ```

   * `spec.resources.limits.cpu` specifies the CPU units: `100m` represents 0.1 CPU units (100 \* 1e-3).
   * `spec.resources.limits.memory` specifies the bytes for memory: `256Mi` represents 268435456 bytes (256 \* 2 ^ 20).
   * `spec.resources.limits.ephemeral-storage` specifies the bytes for ephemeral-storage: `1Gi` represents 1073741824 bytes (2 ^ 30).

     However, if a quota has been defined for your project, one of the following two items is required:

     + A `resources` section set with an explicit `requests`:

       ```
       kind: Deployment
       apiVersion: apps/v1
       metadata:
         name: hello-openshift
       # ...
       spec:
       # ...
         type: "Recreate"
         resources:
           requests:
             cpu: "100m"
             memory: "256Mi"
             ephemeral-storage: "1Gi"
       ```

       The `spec.resources.requests` object contains the list of resources that correspond to the list of resources in the quota.
     + A limit range defined in your project, where the defaults from the `LimitRange` object apply to pods created during the deployment process.

     To set deployment resources, choose one of the above options. Otherwise, deploy pod creation fails, citing a failure to satisfy quota.

##### [7.2.1.9. Scaling manually](#deployments-scaling-manually_deployment-operations) Copy linkLink copied to clipboard!

To control how many pod replicas run for a `DeploymentConfig` object in OpenShift Container Platform, you can scale manually. Use the `oc scale` command to set the desired number of replicas.

Note

Pods can also be auto-scaled using the `oc autoscale` command.

**Procedure**

1. To manually scale a `DeploymentConfig` object, use the `oc scale` command. For example, the following command sets the replicas in the `frontend` `DeploymentConfig` object to `3`.

   ```
   $ oc scale dc frontend --replicas=3
   ```

   The number of replicas eventually propagates to the desired and current state of the deployment configured by the `DeploymentConfig` object `frontend`.

##### [7.2.1.10. Accessing private repositories from DeploymentConfig objects](#deployments-accessing-private-repos_deployment-operations) Copy linkLink copied to clipboard!

To pull container images from a private repository into a `DeploymentConfig` object in OpenShift Container Platform, you can add a pull secret to the object. Create the secret in the web console, then set it as the pull secret in the `DeploymentConfig` object.

**Procedure**

1. Create a new project.
2. Navigate to **Workloads** → **Secrets**.
3. Create a secret that contains credentials for accessing a private image repository.
4. Navigate to **Workloads** → **DeploymentConfigs**.
5. Create a `DeploymentConfig` object.
6. On the `DeploymentConfig` object editor page, set the **Pull Secret** and save your changes.

##### [7.2.1.11. Assigning pods to specific nodes](#deployments-assigning-pods-to-nodes_deployment-operations) Copy linkLink copied to clipboard!

To control which nodes run your application pods in OpenShift Container Platform, you can set a node selector on a `Pod` configuration or pod template. Combine your selector with labels on nodes, including any default project selectors set by a cluster administrator.

Cluster administrators can set the default node selector for a project in order to restrict pod placement to specific nodes. As a developer, you can set a node selector on a `Pod` configuration to restrict nodes even further.

**Procedure**

1. To add a node selector when creating a pod, edit the `Pod` configuration, and add the `nodeSelector` value. This can be added to a single `Pod` configuration, or in a `Pod` template:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-pod
   # ...
   spec:
     nodeSelector:
       disktype: ssd
   # ...
   ```

   Pods created when the node selector is in place are assigned to nodes with the specified labels. The labels specified here are used in conjunction with the labels added by a cluster administrator.

   For example, if a project has the `type=user-node` and `region=east` labels added to a project by the cluster administrator, and you add the above `disktype: ssd` label to a pod, the pod is only ever scheduled on nodes that have all three labels.

   Note

   Labels can only be set to one value, so setting a node selector of `region=west` in a `Pod` configuration that has `region=east` as the administrator-set default, results in a pod that will never be scheduled.

##### [7.2.1.12. Running a pod with a different service account](#deployments-running-pod-svc-acct_deployment-operations) Copy linkLink copied to clipboard!

To run pods under a non-default identity in OpenShift Container Platform, you can assign a different service account to a `DeploymentConfig` object. Edit the object and set the `serviceAccount` and `serviceAccountName` fields to the account you want to use.

**Procedure**

1. Edit the `DeploymentConfig` object:

   ```
   $ oc edit dc/<deployment_config>
   ```
2. Add the `serviceAccount` and `serviceAccountName` parameters to the `spec` field, and specify the service account you want to use:

   ```
   apiVersion: apps.openshift.io/v1
   kind: DeploymentConfig
   metadata:
     name: example-dc
   # ...
   spec:
   # ...
     securityContext: {}
     serviceAccount: <service_account>
     serviceAccountName: <service_account>
   ```

### [7.3. Using deployment strategies](#deployment-strategies) Copy linkLink copied to clipboard!

To upgrade applications with little or no downtime in OpenShift Container Platform, you can use a deployment strategy. Choose strategies that use `DeploymentConfig` object features or router features depending on whether you need to affect all routes or only specific ones.

Because users generally access applications through a route handled by a router, deployment strategies can focus on `DeploymentConfig` object features or routing features. Strategies that focus on `DeploymentConfig` object features impact all routes that use the application. Strategies that use router features target individual routes.

Most deployment strategies are supported through the `DeploymentConfig` object, and some additional strategies are supported through router features.

#### [7.3.1. Choosing a deployment strategy](#choosing-deployment-strategies) Copy linkLink copied to clipboard!

Consider the following when choosing a deployment strategy:

* Long-running connections must be handled gracefully.
* Database conversions can be complex and must be done and rolled back along with the application.
* If the application is a hybrid of microservices and traditional components, downtime might be required to complete the transition.
* You must have the infrastructure to do this.
* If you have a non-isolated test environment, you can break both new and old versions.

A deployment strategy uses readiness checks to determine if a new pod is ready for use. If a readiness check fails, the `DeploymentConfig` object retries to run the pod until it times out. The default timeout is `10m`, a value set in `TimeoutSeconds` in `dc.spec.strategy.*params`.

#### [7.3.2. Rolling strategy](#deployments-rolling-strategy_deployment-strategies) Copy linkLink copied to clipboard!

To update an application with little or no downtime in OpenShift Container Platform, you can use the rolling deployment strategy. New pods replace previous instances gradually after readiness checks succeed. This strategy is the default when none is specified on a `DeploymentConfig` object.

A rolling deployment typically waits for new pods to become `ready` via a readiness check before scaling down the old components. If a significant issue occurs, the rolling deployment can be aborted.

**When to use a rolling deployment:**

* When you want to take no downtime during an application update.
* When your application supports having old code and new code running at the same time.

A rolling deployment means you have both old and new versions of your code running at the same time. This typically requires that your application handle N-1 compatibility.

**Example rolling strategy definition**

```
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  strategy:
    type: Rolling
    rollingParams:
      updatePeriodSeconds: 1
      intervalSeconds: 1
      timeoutSeconds: 120
      maxSurge: "20%"
      maxUnavailable: "10%"
      pre: {}
     post: {}
```

* `spec.strategy.rollingParams.updatePeriodSeconds` is the time to wait between individual pod updates. If unspecified, this value defaults to `1`.
* `spec.strategy.rollingParams.intervalSeconds` is the time to wait between polling the deployment status after update. If unspecified, this value defaults to `1`.
* `spec.strategy.rollingParams.timeoutSeconds` is the time to wait for a scaling event before giving up. Optional; the default is `600`. Here, *giving up* means automatically rolling back to the previous complete deployment.
* `spec.strategy.rollingParams.maxSurge` is optional and defaults to `25%` if not specified. See the information below the following procedure.
* `spec.strategy.rollingParams.maxUnavailable` is optional and defaults to `25%` if not specified. See the information below the following procedure.
* `spec.strategy.rollingParams.pre` and `spec.strategy.rollingParams.post` are lifecycle hooks.

The rolling strategy:

1. Executes any `pre` lifecycle hook.
2. Scales up the new replication controller based on the surge count.
3. Scales down the old replication controller based on the max unavailable count.
4. Repeats this scaling until the new replication controller has reached the desired replica count and the old replication controller has been scaled to zero.
5. Executes any `post` lifecycle hook.

Important

When scaling down, the rolling strategy waits for pods to become ready so it can decide whether further scaling would affect availability. If scaled up pods never become ready, the deployment process will eventually time out and result in a deployment failure.

The `maxUnavailable` parameter is the maximum number of pods that can be unavailable during the update. The `maxSurge` parameter is the maximum number of pods that can be scheduled above the original number of pods. Both parameters can be set to either a percentage (e.g., `10%`) or an absolute value (e.g., `2`). The default value for both is `25%`.

These parameters allow the deployment to be tuned for availability and speed. For example:

* `maxUnavailable*=0` and `maxSurge*=20%` ensures full capacity is maintained during the update and rapid scale up.
* `maxUnavailable*=10%` and `maxSurge*=0` performs an update using no extra capacity (an in-place update).
* `maxUnavailable*=10%` and `maxSurge*=10%` scales up and down quickly with some potential for capacity loss.

Generally, if you want fast rollouts, use `maxSurge`. If you have to take into account resource quota and can accept partial unavailability, use `maxUnavailable`.

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

##### [7.3.2.1. Canary deployments](#deployments-canary-deployments_deployment-strategies) Copy linkLink copied to clipboard!

To validate a new application version before replacing all pods in OpenShift Container Platform, you can use a canary deployment. All rolling deployments are canary deployments: the new instance is tested with readiness checks and automatically rolled back if it never becomes ready.

The readiness check is part of the application code and can be as sophisticated as necessary to ensure the new instance is ready to be used. If you must implement more complex checks of the application (such as sending real user workloads to the new instance), consider implementing a custom deployment or using a blue-green deployment strategy.

##### [7.3.2.2. Creating a rolling deployment](#deployments-creating-rolling-deployment_deployment-strategies) Copy linkLink copied to clipboard!

To update an application with minimal downtime in OpenShift Container Platform, you can create a rolling deployment. Use the CLI to deploy an application, expose it, and trigger a new rollout so pods are gradually replaced.

**Procedure**

1. Create an application based on the example deployment images found in [Quay.io](https://quay.io/repository/openshifttest/deployment-example):

   ```
   $ oc new-app quay.io/openshifttest/deployment-example:latest
   ```

   Note

   This image does not expose any ports. If you want to expose your applications over an external LoadBalancer service or enable access to the application over the public internet, create a service by using the `oc expose dc/deployment-example --port=<port>` command after completing this procedure.
2. If you have the router installed, make the application available via a route or use the service IP directly.

   ```
   $ oc expose svc/deployment-example
   ```
3. Browse to the application at `deployment-example.<project>.<router_domain>` to verify you see the `v1` image.
4. Scale the `DeploymentConfig` object up to three replicas:

   ```
   $ oc scale dc/deployment-example --replicas=3
   ```
5. Trigger a new deployment automatically by tagging a new version of the example as the `latest` tag:

   ```
   $ oc tag deployment-example:v2 deployment-example:latest
   ```
6. In your browser, refresh the page until you see the `v2` image.
7. When using the CLI, the following command shows how many pods are on version 1 and how many are on version 2. In the web console, the pods are progressively added to v2 and removed from v1:

   ```
   $ oc describe dc deployment-example
   ```

   During the deployment process, the new replication controller is incrementally scaled up. After the new pods are marked as `ready` (by passing their readiness check), the deployment process continues. If the pods do not become ready, the process aborts, and the deployment rolls back to its previous version.

##### [7.3.2.3. Editing a deployment by using the Developer perspective](#odc-editing-deployments_rolling-strategy) Copy linkLink copied to clipboard!

To change the strategy, images, environment variables, or advanced options for a deployment in OpenShift Container Platform, you can edit the deployment in the **Developer** perspective.

Open the application in the **Topology** view and use **Edit Deployment** to update settings such as rollouts and replicas.

**Prerequisites**

* You are in the **Developer** perspective of the web console.
* You have created an application.

**Procedure**

1. Navigate to the **Topology** view.
2. Click your application to see the **Details** panel.
3. In the **Actions** drop-down menu, select **Edit Deployment** to view the **Edit Deployment** page.
4. You can edit the following **Advanced options** for your deployment:

   1. Optional: You can pause rollouts by clicking **Pause rollouts**, and then selecting the **Pause rollouts for this deployment** checkbox.

      By pausing rollouts, you can make changes to your application without triggering a rollout. You can resume rollouts at any time.
   2. Optional: Click **Scaling** to change the number of instances of your image by modifying the number of **Replicas**.
5. Click **Save**.

##### [7.3.2.4. Starting a rolling deployment using the Developer perspective](#odc-starting-rolling-deployment_rolling-strategy) Copy linkLink copied to clipboard!

To upgrade an application with minimal downtime in OpenShift Container Platform, you can start a rolling deployment in the **Developer** perspective. From the **Topology** view, select **Start Rollout** to spin up the new version and then terminate the old pods.

**Prerequisites**

* You are in the **Developer** perspective of the web console.
* You have created an application.

**Procedure**

1. In the **Topology** view, click the application node to see the **Overview** tab in the side panel. Note that the **Update Strategy** is set to the default **Rolling** strategy.
2. In the **Actions** drop-down menu, select **Start Rollout** to start a rolling update. The rolling deployment spins up the new version of the application and then terminates the old one.

   **Figure 7.1. Rolling update**

#### [7.3.3. Recreate strategy](#deployments-recreate-strategy_rolling-strategy) Copy linkLink copied to clipboard!

To replace all previous pods before starting the new version in OpenShift Container Platform, you can use the recreate deployment strategy. Scale the old deployment to zero, then scale up the new one, optionally running `pre`, `mid`, and `post` lifecycle hooks.

**Example recreate strategy definition**

```
kind: Deployment
apiVersion: apps/v1
metadata:
  name: hello-openshift
# ...
spec:
# ...
  strategy:
    type: Recreate
    recreateParams:
      pre: {}
      mid: {}
      post: {}
```

* `spec.strategy.recreateParams` are optional.
* `spec.strategy.recreateParams.pre`, `spec.strategy.recreateParams.mid`, and `spec.strategy.recreateParams.post` are lifecycle hooks.

The recreate strategy:

1. Executes any `pre` lifecycle hook.
2. Scales down the previous deployment to zero.
3. Executes any `mid` lifecycle hook.
4. Scales up the new deployment.
5. Executes any `post` lifecycle hook.

Important

During scale up, if the replica count of the deployment is greater than one, the first replica of the deployment will be validated for readiness before fully scaling up the deployment. If the validation of the first replica fails, the deployment will be considered a failure.

**When to use a recreate deployment:**

* When you must run migrations or other data transformations before your new code starts.
* When you do not support having new and old versions of your application code running at the same time.
* When you want to use a RWO volume, which is not supported being shared between multiple replicas.

A recreate deployment incurs downtime because, for a brief period, no instances of your application are running. However, your old code and new code do not run at the same time.

##### [7.3.3.1. Editing a deployment by using the Developer perspective](#odc-editing-deployments_recreate-strategy) Copy linkLink copied to clipboard!

To change the strategy, images, environment variables, or advanced options for a deployment in OpenShift Container Platform, you can edit the deployment in the **Developer** perspective.

Open the application in the **Topology** view and use **Edit Deployment** to update settings such as rollouts and replicas.

**Prerequisites**

* You are in the **Developer** perspective of the web console.
* You have created an application.

**Procedure**

1. Navigate to the **Topology** view.
2. Click your application to see the **Details** panel.
3. In the **Actions** drop-down menu, select **Edit Deployment** to view the **Edit Deployment** page.
4. You can edit the following **Advanced options** for your deployment:

   1. Optional: You can pause rollouts by clicking **Pause rollouts**, and then selecting the **Pause rollouts for this deployment** checkbox.

      By pausing rollouts, you can make changes to your application without triggering a rollout. You can resume rollouts at any time.
   2. Optional: Click **Scaling** to change the number of instances of your image by modifying the number of **Replicas**.
5. Click **Save**.

##### [7.3.3.2. Starting a recreate deployment using the Developer perspective](#odc-starting-recreate-deployment_recreate-strategy) Copy linkLink copied to clipboard!

To switch from a rolling update to a recreate rollout in OpenShift Container Platform, you can change the deployment strategy in the **Developer** perspective. Set the strategy type to `Recreate` in the YAML editor, then start a rollout from the **Topology** view.

**Prerequisites**

* Ensure that you are in the **Developer** perspective of the web console.
* Ensure that you have created an application using the **Add** view and see it deployed in the **Topology** view.

**Procedure**

1. Click your application to see the **Details** panel.
2. In the **Actions** drop-down menu, select **Edit Deployment Config** to see the deployment configuration details of the application.
3. In the YAML editor, change the `spec.strategy.type` to `Recreate` and click **Save**.
4. In the **Topology** view, select the node to see the **Overview** tab in the side panel. The **Update Strategy** is now set to **Recreate**.
5. Use the **Actions** drop-down menu to select **Start Rollout** to start an update using the recreate strategy. The recreate strategy first terminates pods for the older version of the application and then spins up pods for the new version.

   **Figure 7.2. Recreate update**

#### [7.3.4. Custom strategy](#deployments-custom-strategy_recreate-strategy) Copy linkLink copied to clipboard!

To define your own rollout behavior in OpenShift Container Platform, you can use a custom deployment strategy. Provide a container image, command, and environment variables that control how the new deployment becomes active.

**Example custom strategy definition**

```
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  strategy:
    type: Custom
    customParams:
      image: organization/strategy
      command: [ "command", "arg1" ]
      environment:
        - name: ENV_1
          value: VALUE_1
```

In the above example, the `organization/strategy` container image provides the deployment behavior. The optional `command` array overrides any `CMD` directive specified in the image’s `Dockerfile`. The optional environment variables provided are added to the execution environment of the strategy process.

Additionally, OpenShift Container Platform provides the following environment variables to the deployment process:

Expand

| Environment variable | Description |
| --- | --- |
| `OPENSHIFT_DEPLOYMENT_NAME` | The name of the new deployment, a replication controller. |
| `OPENSHIFT_DEPLOYMENT_NAMESPACE` | The name space of the new deployment. |

Show more

The replica count of the new deployment will initially be zero. The responsibility of the strategy is to make the new deployment active using the logic that best serves the needs of the user.

Alternatively, use the `customParams` object to inject the custom deployment logic into the existing deployment strategies. Provide a custom shell script logic and call the `openshift-deploy` binary. Users do not have to supply their custom deployer container image; in this case, the default OpenShift Container Platform deployer image is used instead:

```
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  strategy:
    type: Rolling
    customParams:
      command:
      - /bin/sh
      - -c
      - |
        set -e
        openshift-deploy --until=50%
        echo Halfway there
        openshift-deploy
        echo Complete
```

This results in following deployment:

```
Started deployment #2
--> Scaling up custom-deployment-2 from 0 to 2, scaling down custom-deployment-1 from 2 to 0 (keep 2 pods available, don't exceed 3 pods)
    Scaling custom-deployment-2 up to 1
--> Reached 50% (currently 50%)
Halfway there
--> Scaling up custom-deployment-2 from 1 to 2, scaling down custom-deployment-1 from 2 to 0 (keep 2 pods available, don't exceed 3 pods)
    Scaling custom-deployment-1 down to 1
    Scaling custom-deployment-2 up to 2
    Scaling custom-deployment-1 down to 0
--> Success
Complete
```

If the custom deployment strategy process requires access to the OpenShift Container Platform API or the Kubernetes API the container that executes the strategy can use the service account token available inside the container for authentication.

##### [7.3.4.1. Editing a deployment by using the Developer perspective](#odc-editing-deployments_custom-strategy) Copy linkLink copied to clipboard!

To change the strategy, images, environment variables, or advanced options for a deployment in OpenShift Container Platform, you can edit the deployment in the **Developer** perspective.

Open the application in the **Topology** view and use **Edit Deployment** to update settings such as rollouts and replicas.

**Prerequisites**

* You are in the **Developer** perspective of the web console.
* You have created an application.

**Procedure**

1. Navigate to the **Topology** view.
2. Click your application to see the **Details** panel.
3. In the **Actions** drop-down menu, select **Edit Deployment** to view the **Edit Deployment** page.
4. You can edit the following **Advanced options** for your deployment:

   1. Optional: You can pause rollouts by clicking **Pause rollouts**, and then selecting the **Pause rollouts for this deployment** checkbox.

      By pausing rollouts, you can make changes to your application without triggering a rollout. You can resume rollouts at any time.
   2. Optional: Click **Scaling** to change the number of instances of your image by modifying the number of **Replicas**.
5. Click **Save**.

#### [7.3.5. Lifecycle hooks](#deployments-lifecycle-hooks_custom-strategy) Copy linkLink copied to clipboard!

To run custom logic at specific points during a rollout in OpenShift Container Platform, you can use lifecycle hooks with the rolling or recreate strategy. Configure hooks such as `pre` with a failure policy to abort, retry, or ignore when a hook fails.

The rolling and recreate strategies support *lifecycle hooks*, or deployment hooks, which allow behavior to be injected into the deployment process at predefined points within the strategy as shown in the following example:

```
pre:
  failurePolicy: Abort
  execNewPod: {}
```

`pre.execNewPod` is a pod-based lifecycle hook.

Every hook has a *failure policy*, which defines the action the strategy should take when a hook failure is encountered:

Expand

|  |  |
| --- | --- |
| `Abort` | The deployment process will be considered a failure if the hook fails. |
| `Retry` | The hook execution should be retried until it succeeds. |
| `Ignore` | Any hook failure should be ignored and the deployment should proceed. |

Show more

Hooks have a type-specific field that describes how to execute the hook. Currently, pod-based hooks are the only supported hook type, specified by the `execNewPod` field.

#### [7.3.6. Pod-based lifecycle hook](#deployments-lifecycle-hooks-pod-based_custom-strategy) Copy linkLink copied to clipboard!

Pod-based lifecycle hooks execute hook code in a new pod derived from the template in a `DeploymentConfig` object.

The following simplified example deployment uses the rolling strategy. Triggers and some other minor details are omitted for brevity:

```
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: frontend
spec:
  template:
    metadata:
      labels:
        name: frontend
    spec:
      containers:
        - name: helloworld
          image: openshift/origin-ruby-sample
  replicas: 5
  selector:
    name: frontendasciiditavale modules/creating-rolling-deployments-CLI.adoc

  strategy:
    type: Rolling
    rollingParams:
      pre:
        failurePolicy: Abort
        execNewPod:
          containerName: helloworld
          command: [ "/usr/bin/command", "arg1", "arg2" ]
          env:
            - name: CUSTOM_VAR1
              value: custom_value1
          volumes:
            - data
```

* `strategy.rollingParams.pre.execNewPod.containername.helloworld` refers to `spec.template.spec.containers[0].name`.
* `strategy.rollingParams.pre.execNewPod.command` overrides any `ENTRYPOINT` defined by the `openshift/origin-ruby-sample` image.
* `strategy.rollingParams.pre.execNewPod.env` is an optional set of environment variables for the hook container.
* `strategy.rollingParams.pre.execNewPod.volumes` is an optional set of volume references for the hook container.

In this example, the `pre` hook will be executed in a new pod using the `openshift/origin-ruby-sample` image from the `helloworld` container. The hook pod has the following properties:

* The hook command is `/usr/bin/command arg1 arg2`.
* The hook container has the `CUSTOM_VAR1=custom_value1` environment variable.
* The hook failure policy is `Abort`, meaning the deployment process fails if the hook fails.
* The hook pod inherits the `data` volume from the `DeploymentConfig` object pod.

#### [7.3.7. Setting lifecycle hooks](#deployments-setting-lifecycle-hooks_custom-strategy) Copy linkLink copied to clipboard!

You can set lifecycle hooks, or deployment hooks, for a deployment using the CLI.

**Procedure**

1. Use the `oc set deployment-hook` command to set the type of hook you want: `--pre`, `--mid`, or `--post`. For example, to set a pre-deployment hook:

   ```
   $ oc set deployment-hook dc/frontend \
       --pre -c helloworld -e CUSTOM_VAR1=custom_value1 \
       --volumes data --failure-policy=abort -- /usr/bin/command arg1 arg2
   ```

### [7.4. Using route-based deployment strategies](#route-based-deployment-strategies) Copy linkLink copied to clipboard!

To roll out application changes to selected traffic in OpenShift Container Platform, you can use route-based deployment strategies with the router and `Deployment` objects.

These advanced strategies, including blue-green, A/B, and canary, affect specific routes rather than every route that resolves to the application.

The most common route-based strategy is to use a *blue-green deployment*. The new version (the green version) is brought up for testing and evaluation, while the users still use the stable version (the blue version). When ready, the users are switched to the green version. If a problem arises, you can switch back to the blue version.

Alternatively, you can use an *A/B versions* strategy in which both versions are active at the same time. With this strategy, some users can use *version A*, and other users can use *version B*. You can use this strategy to experiment with user interface changes or other features in order to get user feedback. You can also use it to verify proper operation in a production context where problems impact a limited number of users.

A canary deployment tests the new version but when a problem is detected it quickly falls back to the previous version. This can be done with both of the above strategies.

The route-based deployment strategies do not scale the number of pods in the services. To maintain desired performance characteristics the deployment configurations might have to be scaled.

#### [7.4.1. Proxy shards and traffic splitting](#deployments-proxy-shard_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To precisely control how traffic reaches application shards in OpenShift Container Platform, you can use relative scale and proxy shards. A proxy shard forwards or splits incoming requests to other services so you can implement percentage-based traffic, comparison testing, or related patterns.

In the simplest configuration, the proxy forwards requests unchanged. In more complex setups, you can duplicate the incoming requests and send to both a separate cluster as well as to a local instance of the application, and compare the result. Other patterns include keeping the caches of a DR installation warm, or sampling incoming traffic for analysis purposes.

Any TCP (or UDP) proxy could be run under the desired shard. Use the `oc scale` command to alter the relative number of instances serving requests under the proxy shard. For more complex traffic management, consider customizing the OpenShift Container Platform router with proportional balancing capabilities.

#### [7.4.2. N-1 compatibility](#deployments-n1-compatibility_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To run old and new application code side by side during a rollout in OpenShift Container Platform, you need N-1 compatibility. Design your data and schemas so that values written by the new version can be read or safely ignored by the old version.

Applications that have new code and old code running at the same time must be careful to ensure that data written by the new code can be read and handled (or gracefully ignored) by the old version of the code. This is sometimes called *schema evolution* and is a complex problem.

This can take many forms: data stored on disk, in a database, in a temporary cache, or that is part of a user’s browser session. While most web applications can support rolling deployments, it is important to test and design your application to handle it.

For some applications, the period of time that old code and new code is running side by side is short, so bugs or some failed user transactions are acceptable. For others, the failure pattern may result in the entire application becoming non-functional.

One way to validate N-1 compatibility is to use an A/B deployment: run the old code and new code at the same time in a controlled way in a test environment, and verify that traffic that flows to the new deployment does not cause failures in the old deployment.

#### [7.4.3. Graceful termination](#deployments-graceful-termination_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To avoid dropping user connections when pods shut down in OpenShift Container Platform, you can rely on graceful termination. The platform sends a `TERM` signal so your application can stop accepting new traffic, close open connections, and exit before the grace period ends.

On shutdown, OpenShift Container Platform sends a `TERM` signal to the processes in the container. Application code, on receiving `SIGTERM`, stop accepting new connections. This ensures that load balancers route traffic to other active instances. The application code then waits until all open connections are closed, or gracefully terminate individual connections at the next opportunity, before exiting.

After the graceful termination period expires, a process that has not exited is sent the `KILL` signal, which immediately ends the process. The `terminationGracePeriodSeconds` attribute of a pod or pod template controls the graceful termination period (default 30 seconds) and can be customized per application as necessary.

#### [7.4.4. Setting up a blue-green deployment](#deployments-blue-green_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To switch users from a stable application version to a new one in OpenShift Container Platform, you can set up a blue-green deployment.

Run both versions at once, then point the production route at the new (green) service when you are ready, with the option to switch back to the blue version if needed.

Because many applications depend on persistent data, you must have an application that supports *N-1 compatibility*, which means it shares data and implements live migration between the database, store, or disk by creating two copies of the data layer.

Consider the data used in testing the new version. If it is the production data, a bug in the new version can break the production version.

Blue-green deployments use two `Deployment` objects. Both are running, and the one in production depends on the service the route specifies, with each `Deployment` object exposed to a different service.

Note

Routes are intended for web (HTTP and HTTPS) traffic, so this technique is best suited for web applications.

You can create a new route to the new version and test it. When ready, change the service in the production route to point to the new service and the new (green) version is live.

If necessary, you can roll back to the older (blue) version by switching the service back to the previous version.

**Procedure**

1. Create two independent application components.

   1. Create a copy of the example application running the `v1` image under the `example-blue` service:

      ```
      $ oc new-app openshift/deployment-example:v1 --name=example-blue
      ```
   2. Create a second copy that uses the `v2` image under the `example-green` service:

      ```
      $ oc new-app openshift/deployment-example:v2 --name=example-green
      ```
2. Create a route that points to the old service:

   ```
   $ oc expose svc/example-blue --name=bluegreen-example
   ```
3. Browse to the application at `bluegreen-example-<project>.<router_domain>` to verify you see the `v1` image.
4. Edit the route and change the service name to `example-green`:

   ```
   $ oc patch route/bluegreen-example -p '{"spec":{"to":{"name":"example-green"}}}'
   ```
5. To verify that the route has changed, refresh the browser until you see the `v2` image.

#### [7.4.5. A/B deployments](#deployments-ab-testing_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To test a new application version with a limited share of production traffic in OpenShift Container Platform, you can use an A/B deployment. You send most requests to the stable version, route a fraction to the new version, and increase that fraction as testing progresses.

Because you control the portion of requests to each version, as testing progresses you can increase the fraction of requests to the new version and ultimately stop using the previous version. As you adjust the request load on each version, the number of pods in each service might have to be scaled as well to provide the expected performance.

In addition to upgrading software, you can use this feature to experiment with versions of the user interface. Since some users get the old version and some the new, you can evaluate the user’s reaction to the different versions to inform design decisions.

For this to be effective, both the old and new versions must be similar enough that both can run at the same time. This is common with bug fix releases and when new features do not interfere with the old. The versions require N-1 compatibility to properly work together.

OpenShift Container Platform supports N-1 compatibility through the web console as well as the CLI.

#### [7.4.6. Load balancing for A/B testing](#deployments-ab-testing-lb_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To split production traffic between application versions for A/B testing in OpenShift Container Platform, you can configure a route with weighted services. Use the `oc set route-backends` command or edit the route to assign weights so the router sends a proportional share of requests to each version.

You set up a route with multiple services. Each service handles a version of the application.

Each service is assigned a `weight` and the portion of requests to each service is the `service_weight` divided by the `sum_of_weights`. The `weight` for each service is distributed to the service’s endpoints so that the sum of the endpoint `weights` is the service `weight`.

The route can have up to four services. The `weight` for the service can be between `0` and `256`. When the `weight` is `0`, the service does not participate in load balancing but continues to serve existing persistent connections. When the service `weight` is not `0`, each endpoint has a minimum `weight` of `1`. Because of this, a service with a lot of endpoints can end up with higher `weight` than intended. In this case, reduce the number of pods to get the expected load balance `weight`.

**Procedure**

1. Create the two applications and give them different names. Each creates a `Deployment` object. The applications are versions of the same program; one is usually the current production version and the other the proposed new version.

   1. Create the first application. The following example creates an application called `ab-example-a`:

      ```
      $ oc new-app openshift/deployment-example --name=ab-example-a
      ```
   2. Create the second application:

      ```
      $ oc new-app openshift/deployment-example:v2 --name=ab-example-b
      ```

      Both applications are deployed and services are created.
2. Make the application available externally via a route. At this point, you can expose either. It can be convenient to expose the current production version first and later modify the route to add the new version.

   ```
   $ oc expose svc/ab-example-a
   ```

   Browse to the application at `ab-example-a.<project>.<router_domain>` to verify that you see the expected version.
3. When you deploy the route, the router balances the traffic according to the `weights` specified for the services. At this point, there is a single service with default `weight=1` so all requests go to it. Adding the other service as an `alternateBackends` and adjusting the `weights` brings the A/B setup to life. This can be done by the `oc set route-backends` command or by editing the route.

   Note

   When using `alternateBackends`, also use the `roundrobin` load balancing strategy to ensure requests are distributed as expected to the services based on weight. `roundrobin` can be set for a route by using a route annotation. See the *Additional resources* section for more information about route annotations.

   Setting the `oc set route-backend` to `0` means the service does not participate in load balancing, but continues to serve existing persistent connections.

   Note

   Changes to the route just change the portion of traffic to the various services. You might have to scale the deployment to adjust the number of pods to handle the anticipated loads.

   To edit the route, run:

   ```
   $ oc edit route <route_name>
   ```

   **Example output**

   ```
   apiVersion: route.openshift.io/v1
   kind: Route
   metadata:
     name: route-alternate-service
     annotations:
       haproxy.router.openshift.io/balance: roundrobin
   # ...
   spec:
     host: ab-example.my-project.my-domain
     to:
       kind: Service
       name: ab-example-a
       weight: 10
     alternateBackends:
     - kind: Service
       name: ab-example-b
       weight: 15
   # ...
   ```

#### [7.4.7. Managing weights of an existing route by using the web console](#deployments-ab-testing-lb-web_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To split production traffic between application versions for A/B testing in OpenShift Container Platform, you can configure a route with weighted services. Use the `oc set route-backends` command or edit the route to assign weights so the router sends a proportional share of requests to each version.

**Procedure**

1. Navigate to the **Networking** → **Routes** page.
2. Click the Options menu
   next to the route you want to edit and select **Edit Route**.
3. Edit the YAML file. Update the `weight` to be an integer between `0` and `256` that specifies the relative weight of the target against other target reference objects. The value `0` suppresses requests to this back end. The default is `100`. Run `oc explain routes.spec.alternateBackends` for more information about the options.
4. Click **Save**.

#### [7.4.8. Managing weights of a new route by using the web console](#deployments-ab-testing-lb-web-new-route_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To set traffic weights when you create a new route for A/B testing in OpenShift Container Platform, you can use the web console. Create the route, add an alternate service, and assign relative weights so the router distributes requests between application versions.

**Procedure**

1. Navigate to the **Networking** → **Routes** page.
2. Click **Create Route**.
3. Enter the route **Name**.
4. Select the **Service**.
5. Click **Add Alternate Service**.
6. Enter a value for **Weight** and **Alternate Service Weight**. Enter a number between `0` and `255` that depicts relative weight compared with other targets. The default is `100`.
7. Select the **Target Port**.
8. Click **Create**.

#### [7.4.9. Managing weights using the CLI](#deployments-ab-testing-lb-cli_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To manage service traffic weights for A/B testing in OpenShift Container Platform, you can use the `oc set route-backends` command. Set or adjust weights on a route so the router sends a proportional share of requests to each service.

**Procedure**

1. To manage the services and corresponding weights load balanced by the route, use the `oc set route-backends` command:

   ```
   $ oc set route-backends ROUTENAME \
       [--zero|--equal] [--adjust] SERVICE=WEIGHT[%] [...] [options]
   ```

   For example, the following sets `ab-example-a` as the primary service with `weight=198` and `ab-example-b` as the first alternate service with a `weight=2`:

   ```
   $ oc set route-backends ab-example ab-example-a=198 ab-example-b=2
   ```

   This means 99% of traffic is sent to service `ab-example-a` and 1% to service `ab-example-b`.

   This command does not scale the deployment. You might be required to do so to have enough pods to handle the request load.
2. Run the command with no flags to verify the current configuration:

   ```
   $ oc set route-backends ab-example
   ```

   **Example output**

   ```
   NAME                    KIND     TO           WEIGHT
   routes/ab-example       Service  ab-example-a 198 (99%)
   routes/ab-example       Service  ab-example-b 2   (1%)
   ```
3. To override the default values for the load balancing algorithm, adjust the annotation on the route by setting the algorithm to `roundrobin`. For a route on OpenShift Container Platform, the default load balancing algorithm is set to `random` or `source` values.

   To set the algorithm to `roundrobin`, run the command:

   ```
   $ oc annotate routes/<route-name> haproxy.router.openshift.io/balance=roundrobin
   ```

   For Transport Layer Security (TLS) passthrough routes, the default value is `source`. For all other routes, the default is `random`.
4. To alter the weight of an individual service relative to itself or to the primary service, use the `--adjust` flag. Specifying a percentage adjusts the service relative to either the primary or the first alternate (if you specify the primary). If there are other backends, their weights are kept proportional to the changed.

   The following example alters the weight of `ab-example-a` and `ab-example-b` services:

   ```
   $ oc set route-backends ab-example --adjust ab-example-a=200 ab-example-b=10
   ```

   Alternatively, alter the weight of a service by specifying a percentage:

   ```
   $ oc set route-backends ab-example --adjust ab-example-b=5%
   ```

   By specifying `+` before the percentage declaration, you can adjust a weighting relative to the current setting. For example:

   ```
   $ oc set route-backends ab-example --adjust ab-example-b=+15%
   ```

   The `--equal` flag sets the `weight` of all services to `100`:

   ```
   $ oc set route-backends ab-example --equal
   ```

   The `--zero` flag sets the `weight` of all services to `0`. All requests then return with a 503 error.

   Note

   Not all routers support multiple or weighted backends.

#### [7.4.10. Create multiple Deployment objects that use one service](#deployments-ab-one-service-multi-dc_route-based-deployment-strategies) Copy linkLink copied to clipboard!

To serve multiple application versions through a single service in OpenShift Container Platform, you can create multiple `Deployment` objects that share a common label selector.

Expose one service for those pods so you can scale or update each shard independently while users reach them through the same route.

**Procedure**

1. Create a new application, adding a label `ab-example=true` that will be common to all shards:

   ```
   $ oc new-app openshift/deployment-example --name=ab-example-a --as-deployment-config=true --labels=ab-example=true --env=SUBTITLE\=shardA
   ```

   ```
   $ oc delete svc/ab-example-a
   ```

   The application is deployed and a service is created. This is the first shard.
2. Make the application available via a route, or use the service IP directly:

   ```
   $ oc expose deployment ab-example-a --name=ab-example --selector=ab-example\=true
   ```

   ```
   $ oc expose service ab-example
   ```
3. Browse to the application at `ab-example-<project_name>.<router_domain>` to verify you see the `v1` image.
4. Create a second shard based on the same source image and label as the first shard, but with a different tagged version and unique environment variables:

   ```
   $ oc new-app openshift/deployment-example:v2 \
       --name=ab-example-b --labels=ab-example=true \
       SUBTITLE="shard B" COLOR="red" --as-deployment-config=true
   ```

   ```
   $ oc delete svc/ab-example-b
   ```
5. At this point, both sets of pods are being served under the route. However, because both browsers (by leaving a connection open) and the router (by default, through a cookie) attempt to preserve your connection to a back-end server, you might not see both shards being returned to you.

   To force your browser to one or the other shard:

   1. Use the `oc scale` command to reduce replicas of `ab-example-a` to `0`.

      ```
      $ oc scale dc/ab-example-a --replicas=0
      ```

      Refresh your browser to show `v2` and `shard B` (in red).
   2. Scale `ab-example-a` to `1` replica and `ab-example-b` to `0`:

      ```
      $ oc scale dc/ab-example-a --replicas=1; oc scale dc/ab-example-b --replicas=0
      ```

      Refresh your browser to show `v1` and `shard A` (in blue).
6. If you trigger a deployment on either shard, only the pods in that shard are affected. You can trigger a deployment by changing the `SUBTITLE` environment variable in either `Deployment` object:

   ```
   $ oc edit dc/ab-example-a
   ```

   or

   ```
   $ oc edit dc/ab-example-b
   ```

## [Chapter 8. Quotas](#quotas) Copy linkLink copied to clipboard!

### [8.1. Resource quotas per project](#quotas-setting-per-project) Copy linkLink copied to clipboard!

A resource quota, defined by a `ResourceQuota` object, limits aggregate resource consumption per project. It limits the quantity of objects that you can create in a project by type, and the total amount of compute resources and storage consumed by the resources in that project.

This guide describes how resource quotas work, how cluster administrators can set and manage resource quotas on a per project basis, and how developers and cluster administrators can view them.

#### [8.1.1. Resources managed by quotas](#quotas-resources-managed_quotas-setting-per-project) Copy linkLink copied to clipboard!

Review the specific compute resources, storage resources, and object counts that you can manage with a project quota.

Note

A pod is in a terminal state if `status.phase in (Failed, Succeeded)` is true.

Expand

Table 8.1. Compute resources managed by quota

| Resource Name | Description |
| --- | --- |
| `cpu` | The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably. |
| `memory` | The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably. |
| `requests.cpu` | The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably. |
| `requests.memory` | The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably. |
| `limits.cpu` | The sum of CPU limits across all pods in a non-terminal state cannot exceed this value. |
| `limits.memory` | The sum of memory limits across all pods in a non-terminal state cannot exceed this value. |

Show more

Expand

Table 8.2. Storage resources managed by quota

| Resource Name | Description |
| --- | --- |
| `requests.storage` | The sum of storage requests across all persistent volume claims in any state cannot exceed this value. |
| `persistentvolumeclaims` | The total number of persistent volume claims that can exist in the project. |
| `<storage-class-name>.storageclass.storage.k8s.io/requests.storage` | The sum of storage requests across all persistent volume claims in any state that have a matching storage class, cannot exceed this value. |
| `<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` | The total number of persistent volume claims with a matching storage class that can exist in the project. |
| `ephemeral-storage` | The sum of local ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably. |
| `requests.ephemeral-storage` | The sum of ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably. |
| `limits.ephemeral-storage` | The sum of ephemeral storage limits across all pods in a non-terminal state cannot exceed this value. |

Show more

Expand

Table 8.3. Object counts managed by quota

| Resource Name | Description |
| --- | --- |
| `pods` | The total number of pods in a non-terminal state that can exist in the project. |
| `replicationcontrollers` | The total number of ReplicationControllers that can exist in the project. |
| `resourcequotas` | The total number of resource quotas that can exist in the project. |
| `services` | The total number of services that can exist in the project. |
| `services.loadbalancers` | The total number of services of type `LoadBalancer` that can exist in the project. |
| `services.nodeports` | The total number of services of type `NodePort` that can exist in the project. |
| `secrets` | The total number of secrets that can exist in the project. |
| `configmaps` | The total number of `ConfigMap` objects that can exist in the project. |
| `persistentvolumeclaims` | The total number of persistent volume claims that can exist in the project. |
| `openshift.io/imagestreams` | The total number of imagestreams that can exist in the project. |

Show more

#### [8.1.2. Quota scopes](#quotas-scopes_quotas-setting-per-project) Copy linkLink copied to clipboard!

Measure resource usage with a quota, and add scopes to restrict the allowed set of target resources to prevent validation errors.

Each quota can have an associated set of *scopes*. A quota only measures usage for a resource if it matches the intersection of enumerated scopes.

Expand

| Scope | Description |
| --- | --- |
| `BestEffort` | Match pods that have best effort quality of service for either `cpu` or `memory`. |
| `NotBestEffort` | Match pods that do not have best effort quality of service for `cpu` and `memory`. |

Show more

A `BestEffort` scope restricts a quota to limiting the following resources:

* `pods`

A `NotBestEffort` scope restricts a quota to tracking the following resources:

* `pods`
* `memory`
* `requests.memory`
* `limits.memory`
* `cpu`
* `requests.cpu`
* `limits.cpu`

#### [8.1.3. Quota enforcement](#quota-enforcement_quotas-setting-per-project) Copy linkLink copied to clipboard!

Track project resource usage, such as compute and storage, and automatically deny modifications that exceed defined limits to prevent quota violations.

After a resource quota for a project is first created, the project restricts the ability to create any new resources that may violate a quota constraint until it has calculated updated usage statistics.

After a quota is created and usage statistics are updated, the project accepts the creation of new content. When you create or modify resources, your quota usage is incremented immediately upon the request to create or modify the resource.

When you delete a resource, your quota use is decremented during the next full recalculation of quota statistics for the project. A configurable amount of time determines how long it takes to reduce quota usage statistics to their current observed system value.

If project modifications exceed a quota usage limit, the server denies the action, and an appropriate error message is returned to the user explaining the quota constraint violated, and what their currently observed usage statistics are in the system.

#### [8.1.4. Requests versus limits](#quotas-requests-vs-limits_quotas-setting-per-project) Copy linkLink copied to clipboard!

To manage cluster capacity, use a project quota to restrict container compute resources. When you configure CPU and memory quotas, incoming containers can explicitly request or limit resources to ensure stable performance.

If the quota has a value specified for `requests.cpu` or `requests.memory`, then it requires that every incoming container make an explicit request for those resources. If the quota has a value specified for `limits.cpu` or `limits.memory`, then it requires that every incoming container specify an explicit limit for those resources.

#### [8.1.5. Sample resource quota definitions](#quotas-sample-resource-quota-definitions_quotas-setting-per-project) Copy linkLink copied to clipboard!

View sample YAML definitions for resource quotas, including specifications for object counts, compute resources, QoS scopes, and storage classes, to configure custom quota manifests for your project.

**`core-object-counts.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: core-object-counts
spec:
  hard:
    configmaps: "10"
    persistentvolumeclaims: "4"
    replicationcontrollers: "20"
    secrets: "10"
    services: "10"
    services.loadbalancers: "2"
```

where:

`spec.hard.configmaps`
:   The total number of `ConfigMap` objects that can exist in the project.

`spec.hard.persistentvolumeclaims`
:   The total number of persistent volume claims (PVCs) that can exist in the project.

`spec.hard.replicationcontrollers`
:   The total number of replication controllers that can exist in the project.

`spec.hard.secrets`
:   The total number of secrets that can exist in the project.

`spec.hard.services`
:   The total number of services that can exist in the project.

`spec.hard.services.loadbalancers`
:   The total number of services of type `LoadBalancer` that can exist in the project.

**`openshift-object-counts.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: openshift-object-counts
spec:
  hard:
    openshift.io/imagestreams: "10"
```

where:

`spec.hard.openshift.io/imagestreams`
:   The total number of image streams that can exist in the project.

**`compute-resources.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    pods: "4"
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi
```

where:

`spec.hard.pods`
:   The total number of pods in a non-terminal state that can exist in the project.

`spec.hard.requests.cpu`
:   Across all pods in a non-terminal state, the sum of CPU requests cannot exceed 1 core.

`spec.hard.requests.memory`
:   Across all pods in a non-terminal state, the sum of memory requests cannot exceed 1Gi.

`spec.hard.limits.cpu`
:   Across all pods in a non-terminal state, the sum of CPU limits cannot exceed 2 cores.

`spec.hard.limits.memory`
:   Across all pods in a non-terminal state, the sum of memory limits cannot exceed 2Gi.

**`besteffort.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: besteffort
spec:
  hard:
    pods: "1"
  scopes:
  - BestEffort
```

where:

`spec.hard.pods`
:   The total number of pods in a non-terminal state with `BestEffort` quality of service that can exist in the project.

`spec.scopes`
:   Restricts the quota to only matching pods that have `BestEffort` quality of service for either memory or CPU.

**`compute-resources-long-running.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-long-running
spec:
  hard:
    pods: "4"
    limits.cpu: "4"
    limits.memory: "2Gi"
  scopes:
  - NotTerminating
```

where:

`spec.hard.pods`
:   The total number of pods in a non-terminal state.

`spec.hard.limits.cpu`
:   Across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value.

`spec.hard.limits.memory`
:   Across all pods in a non-terminal state, the sum of memory limits cannot exceed this value.

`spec.scopes`
:   Restricts the quota to only matching pods where `spec.activeDeadlineSeconds` is set to `nil`. Build pods fall under `NotTerminating` unless the `RestartNever` policy is applied.

**`compute-resources-time-bound.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-time-bound
spec:
  hard:
    pods: "2"
    limits.cpu: "1"
    limits.memory: "1Gi"
  scopes:
  - Terminating
```

where:

`spec.hard.pods`
:   The total number of pods in a terminating state.

`spec.hard.limits.cpu`
:   Across all pods in a terminating state, the sum of CPU limits cannot exceed this value.

`spec.hard.limits.memory`
:   Across all pods in a terminating state, the sum of memory limits cannot exceed this value.

`spec.scopes`
:   Restricts the quota to only matching pods where `spec.activeDeadlineSeconds >=0`. For example, this quota charges for build or deployer pods, but not long running pods like a web server or database.

**`storage-consumption.yaml`**

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: storage-consumption
spec:
  hard:
    persistentvolumeclaims: "10"
    requests.storage: "50Gi"
    gold.storageclass.storage.k8s.io/requests.storage: "10Gi"
    silver.storageclass.storage.k8s.io/requests.storage: "20Gi"
    silver.storageclass.storage.k8s.io/persistentvolumeclaims: "5"
    bronze.storageclass.storage.k8s.io/requests.storage: "0"
    bronze.storageclass.storage.k8s.io/persistentvolumeclaims: "0"
    requests.ephemeral-storage: 2Gi
    limits.ephemeral-storage: 4Gi
```

where:

`spec.hard.persistentvolumeclaims`
:   The total number of persistent volume claims in a project.

`spec.hard.requests.storage`
:   Across all persistent volume claims in a project, the sum of storage requested cannot exceed this value.

`spec.hard.gold.storageclass.storage.k8s.io/requests.storage`
:   Across all persistent volume claims in a project, the sum of storage requested in the gold storage class cannot exceed this value.

`spec.hard.silver.storageclass.storage.k8s.io/requests.storage`
:   Across all persistent volume claims in a project, the sum of storage requested in the silver storage class cannot exceed this value.

`spec.hard.silver.storageclass.storage.k8s.io/persistentvolumeclaims`
:   Across all persistent volume claims in a project, the total number of claims in the silver storage class cannot exceed this value.

`spec.hard.bronze.storageclass.storage.k8s.io/requests.storage`
:   Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, it means bronze storage class cannot request storage.

`spec.hard.bronze.storageclass.storage.k8s.io/persistentvolumeclaims`
:   Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, it means bronze storage class cannot create claims.

`spec.hard.requests.ephemeral-storage`
:   Across all pods in a non-terminal state, the sum of ephemeral storage requests cannot exceed 2Gi.

`spec.hard.limits.ephemeral-storage`
:   Across all pods in a non-terminal state, the sum of ephemeral storage limits cannot exceed 4Gi.

#### [8.1.6. Creating a quota](#quotas-creating-a-quota_quotas-setting-per-project) Copy linkLink copied to clipboard!

Create a defined quota in the project to limit resource consumption and object counts, preventing cluster resource exhaustion.

**Procedure**

1. Define the quota in a file.
2. Use the file to create the quota and apply it to a project:

   ```
   $ oc create -f <file> [-n <project_name>]
   ```

   For example:

   ```
   $ oc create -f core-object-counts.yaml -n demoproject
   ```

##### [8.1.6.1. Creating object count quotas](#quota-creating-object-count-quotas_quotas-setting-per-project) Copy linkLink copied to clipboard!

Restrict resource consumption and standard object creation in a project by creating an object count quota for standard namespaced resource types.

You can create an object count quota for all standard namespaced resource types on OpenShift Container Platform, such as `BuildConfig` and `DeploymentConfig` objects.

When using a resource quota, an object is charged against the quota upon creation. These types of quotas are useful to protect against exhaustion of resources. The quota can only be created if there are enough spare resources within the project.

**Procedure**

1. To configure an object count quota for a resource, run the following command:

   ```
   $ oc create quota <name> \
       --hard=count/<resource>.<group>=<quota>,count/<resource>.<group>=<quota>
   ```

   where:

   `<resource>`
   :   Specifies the name of the resource

   `<group>`
   :   Specifies the API group, if applicable. Use the `oc api-resources` command for a list of resources and their associated API groups.

   For example:

   ```
   $ oc create quota test \
       --hard=count/deployments.apps=2,count/replicasets.apps=4,count/pods=3,count/secrets=4
   ```

   The following is an example output:

   ```
   resourcequota "test" created
   ```

   This example limits the listed resources to the hard limit in each project in the cluster.
2. Verify that the quota was created:

   ```
   $ oc describe quota test
   ```

   **Example output**

   ```
   Name:                         test
   Namespace:                    quota
   Resource                      Used  Hard
   --------                      ----  ----
   count/deployments.apps        0     2
   count/pods                    0     3
   count/replicasets.apps        0     4
   count/secrets                 0     4
   ```

##### [8.1.6.2. Setting resource quota for extended resources](#setting-resource-quota-for-extended-resources_quotas-setting-per-project) Copy linkLink copied to clipboard!

Configure extended resources, such as GPUs, in a resource quota file and apply it to a project to enforce strict capacity limits and prevent pods from exceeding available capacity.

Overcommitment of resources is not allowed for extended resources, so you must specify `requests` and `limits` for the same extended resource in a quota. Currently, only quota items with the prefix `requests.` is allowed for extended resources. The following is an example scenario of how to set resource quota for the GPU resource `nvidia.com/gpu`.

**Procedure**

1. Determine how many GPUs are available on a node in your cluster. For example:

   ```
   # oc describe node ip-172-31-27-209.us-west-2.compute.internal | egrep 'Capacity|Allocatable|gpu'
   ```

   **Example output**

   ```
                       openshift.com/gpu-accelerator=true
   Capacity:
    nvidia.com/gpu:  2
   Allocatable:
    nvidia.com/gpu:  2
     nvidia.com/gpu  0           0
   ```

   In this example, 2 GPUs are available.
2. Create a `ResourceQuota` object to set a quota in the namespace `nvidia`. In this example, the quota is `1`:

   **Example output**

   ```
   apiVersion: v1
   kind: ResourceQuota
   metadata:
     name: gpu-quota
     namespace: nvidia
   spec:
     hard:
       requests.nvidia.com/gpu: 1
   ```
3. Create the quota:

   ```
   # oc create -f gpu-quota.yaml
   ```

   **Example output**

   ```
   resourcequota/gpu-quota created
   ```
4. Verify that the namespace has the correct quota set:

   ```
   # oc describe quota gpu-quota -n nvidia
   ```

   **Example output**

   ```
   Name:                    gpu-quota
   Namespace:               nvidia
   Resource                 Used  Hard
   --------                 ----  ----
   requests.nvidia.com/gpu  0     1
   ```
5. Define a pod that asks for a single GPU. The following example definition file is called `gpu-pod.yaml`:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     generateName: gpu-pod-
     namespace: nvidia
   spec:
     restartPolicy: OnFailure
     containers:
     - name: rhel7-gpu-pod
       image: rhel7
       env:
         - name: NVIDIA_VISIBLE_DEVICES
           value: all
         - name: NVIDIA_DRIVER_CAPABILITIES
           value: "compute,utility"
         - name: NVIDIA_REQUIRE_CUDA
           value: "cuda>=5.0"
       command: ["sleep"]
       args: ["infinity"]
       resources:
         limits:
           nvidia.com/gpu: 1
   ```
6. Create the pod:

   ```
   # oc create -f gpu-pod.yaml
   ```
7. Verify that the pod is running:

   ```
   # oc get pods
   ```

   **Example output**

   ```
   NAME              READY     STATUS      RESTARTS   AGE
   gpu-pod-s46h7     1/1       Running     0          1m
   ```
8. Verify that the quota `Used` counter is correct:

   ```
   # oc describe quota gpu-quota -n nvidia
   ```

   **Example output**

   ```
   Name:                    gpu-quota
   Namespace:               nvidia
   Resource                 Used  Hard
   --------                 ----  ----
   requests.nvidia.com/gpu  1     1
   ```
9. Attempt to create a second GPU pod in the `nvidia` namespace. This is technically available on the node because it has 2 GPUs:

   ```
   # oc create -f gpu-pod.yaml
   ```

   **Example output**

   ```
   Error from server (Forbidden): error when creating "gpu-pod.yaml": pods "gpu-pod-f7z2w" is forbidden: exceeded quota: gpu-quota, requested: requests.nvidia.com/gpu=1, used: requests.nvidia.com/gpu=1, limited: requests.nvidia.com/gpu=1
   ```

   This **Forbidden** error message is expected because you have a quota of 1 GPU and this pod tried to allocate a second GPU, which exceeds its quota.

#### [8.1.7. Viewing a quota](#quota-viewing-quotas_quotas-setting-per-project) Copy linkLink copied to clipboard!

View the usage statistics for the hard limits defined in a project quota to monitor resource consumption and plan cluster capacity.

You can view quota usage statistics on the project’s **Quota** page in the web console or by using the CLI.

**Procedure**

1. Get the list of quotas defined in the project. For example, for a project called `demoproject`:

   ```
   $ oc get quota -n demoproject
   ```

   **Example output**

   ```
   NAME                           AGE    REQUEST                                                                                                      LIMIT
   besteffort                     4s     pods: 1/2
   compute-resources-time-bound   10m    pods: 0/2                                                                                                    limits.cpu: 0/1, limits.memory: 0/1Gi
   core-object-counts             109s   configmaps: 2/10, persistentvolumeclaims: 1/4, replicationcontrollers: 1/20, secrets: 9/10, services: 2/10
   ```
2. Describe the quota you are interested in, for example the `core-object-counts` quota:

   ```
   $ oc describe quota core-object-counts -n demoproject
   ```

   **Example output**

   ```
   Name:			core-object-counts
   Namespace:		demoproject
   Resource		Used	Hard
   --------		----	----
   configmaps		3	10
   persistentvolumeclaims	0	4
   replicationcontrollers	3	20
   secrets			9	10
   services		2	10
   ```

#### [8.1.8. Configuring explicit resource quotas](#configuring-explicit-resource-quotas_quotas-setting-per-project) Copy linkLink copied to clipboard!

Configure explicit resource quotas in a project request template to apply specific resource quotas in new projects.

**Prerequisites**

* Access to the cluster as a user with the cluster-admin role.
* Install the OpenShift CLI (`oc`).

**Procedure**

1. Add a resource quota definition to a project request template:

   * If a project request template does not exist in a cluster:

     1. Create a bootstrap project template and output it to a file called `template.yaml`:

        ```
        $ oc adm create-bootstrap-project-template -o yaml > template.yaml
        ```
     2. Add a resource quota definition to `template.yaml`. The following example defines a resource quota named 'storage-consumption'. The definition must be added before the `parameters:` section in the template:

        ```
        - apiVersion: v1
          kind: ResourceQuota
          metadata:
            name: storage-consumption
            namespace: ${PROJECT_NAME}
          spec:
            hard:
              persistentvolumeclaims: "10"
              requests.storage: "50Gi"
              gold.storageclass.storage.k8s.io/requests.storage: "10Gi"
              silver.storageclass.storage.k8s.io/requests.storage: "20Gi"
              silver.storageclass.storage.k8s.io/persistentvolumeclaims: "5"
              bronze.storageclass.storage.k8s.io/requests.storage: "0"
              bronze.storageclass.storage.k8s.io/persistentvolumeclaims: "0"
        ```

        where:

        `spec.hard.persistentvolumeclaims`
        :   The total number of persistent volume claims in a project.

        `spec.hard.requests.storage`
        :   Across all persistent volume claims in a project, the sum of storage requested cannot exceed this value.

        `spec.hard.gold.storageclass.storage.k8s.io/requests.storage`
        :   Across all persistent volume claims in a project, the sum of storage requested in the gold storage class cannot exceed this value.

        `spec.hard.silver.storageclass.storage.k8s.io/requests.storage`
        :   Across all persistent volume claims in a project, the sum of storage requested in the silver storage class cannot exceed this value.

        `spec.hard.silver.storageclass.storage.k8s.io/persistentvolumeclaims`
        :   Across all persistent volume claims in a project, the total number of claims in the silver storage class cannot exceed this value.

        `spec.hard.bronze.storageclass.storage.k8s.io/requests.storage`
        :   Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this value is set to `0`, the bronze storage class cannot request storage.

        `spec.hard.bronze.storageclass.storage.k8s.io/persistentvolumeclaims`
        :   Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this value is set to `0`, the bronze storage class cannot create claims.
     3. Create a project request template from the modified `template.yaml` file in the `openshift-config` namespace:

        ```
        $ oc create -f template.yaml -n openshift-config
        ```

        Note

        To include the configuration as a `kubectl.kubernetes.io/last-applied-configuration` annotation, add the `--save-config` option to the `oc create` command.

        By default, the template is called `project-request`.
   * If a project request template already exists within a cluster:

     Note

     If you declaratively or imperatively manage objects within your cluster by using configuration files, edit the existing project request template through those files instead.

     1. List templates in the `openshift-config` namespace:

        ```
        $ oc get templates -n openshift-config
        ```
     2. Edit an existing project request template:

        ```
        $ oc edit template <project_request_template> -n openshift-config
        ```
     3. Add a resource quota definition, such as the preceding `storage-consumption` example, into the existing template. The definition must be added before the `parameters:` section in the template.
2. If you created a project request template, reference it in the cluster’s project configuration resource:

   1. Access the project configuration resource for editing:

      * By using the web console:

        1. Navigate to the **Administration** → **Cluster Settings** page.
        2. Click **Configuration** to view all configuration resources.
        3. Find the entry for **Project** and click **Edit YAML**.
      * By using the CLI:

        1. Edit the `project.config.openshift.io/cluster` resource:

           ```
           $ oc edit project.config.openshift.io/cluster
           ```
   2. Update the `spec` section of the project configuration resource to include the `projectRequestTemplate` and `name` parameters. The following example references the default project request template name `project-request`:

      ```
      apiVersion: config.openshift.io/v1
      kind: Project
      metadata:
      #  ...
      spec:
        projectRequestTemplate:
          name: project-request
      ```
3. Verify that the resource quota is applied when projects are created:

   1. Create a project:

      ```
      $ oc new-project <project_name>
      ```
   2. List the project’s resource quotas:

      ```
      $ oc get resourcequotas
      ```
   3. Describe the resource quota in detail:

      ```
      $ oc describe resourcequotas <resource_quota_name>
      ```

### [8.2. Resource quotas across multiple projects](#setting-quotas-across-multiple-projects) Copy linkLink copied to clipboard!

A multi-project quota, defined by a `ClusterResourceQuota` object, shares quotas across multiple projects. The system aggregates the resources used in each selected project and applies the aggregate limit across all selected projects.

This guide describes how cluster administrators can set and manage resource quotas across multiple projects.

Important

Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components.

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects.

#### [8.2.1. Selecting multiple projects during quota creation](#quotas-setting-projects_setting-quotas-across-multiple-projects) Copy linkLink copied to clipboard!

To aggregate resource usage and enforce consistent limits across multiple namespaces, you can select target projects by using annotation or label selectors when creating a `ClusterResourceQuota` object.

**Procedure**

1. To select projects based on annotations, run the following command:

   ```
   $ oc create clusterquota for-user \
        --project-annotation-selector openshift.io/requester=<user_name> \
        --hard pods=10 \
        --hard secrets=20
   ```

   This creates the following `ClusterResourceQuota` object:

   ```
   apiVersion: quota.openshift.io/v1
   kind: ClusterResourceQuota
   metadata:
     name: for-user
   spec:
     quota:
       hard:
         pods: "10"
         secrets: "20"
     selector:
       annotations:
         openshift.io/requester: <user_name>
       labels: null
   status:
     namespaces:
     - namespace: ns-one
       status:
         hard:
           pods: "10"
           secrets: "20"
         used:
           pods: "1"
           secrets: "9"
     total:
       hard:
         pods: "10"
         secrets: "20"
       used:
         pods: "1"
         secrets: "9"
   ```

   where:

   `spec.quota`
   :   The `ResourceQuotaSpec` object that will be enforced over the selected projects.

   `spec.selector.annotations`
   :   A simple key-value selector for annotations.

   `spec.selector.labels`
   :   A label selector that can be used to select projects.

   `status.namespaces`
   :   A per-namespace map that describes current quota usage in each selected project.

   `status.total`
   :   The aggregate usage across all selected projects.

       This multi-project quota document controls all projects requested by `<user_name>` using the default project request endpoint. You are limited to 10 pods and 20 secrets.
2. Similarly, to select projects based on labels, run this command:

   ```
   $  oc create clusterresourcequota for-name \
       --project-label-selector=name=frontend \
       --hard=pods=10 --hard=secrets=20
   ```

   where:

   `clusterresourcequota`
   :   Both `clusterresourcequota` and `clusterquota` are aliases of the same command. `for-name` is the name of the `ClusterResourceQuota` object.

   `--project-label-selector`
   :   To select projects by label, provide a key-value pair by using the format `--project-label-selector=key=value`.

   This creates the following `ClusterResourceQuota` object definition:

   ```
   apiVersion: quota.openshift.io/v1
   kind: ClusterResourceQuota
   metadata:
     creationTimestamp: null
     name: for-name
   spec:
     quota:
       hard:
         pods: "10"
         secrets: "20"
     selector:
       annotations: null
       labels:
         matchLabels:
           name: frontend
   ```

#### [8.2.2. Viewing applicable cluster resource quotas](#quotas-viewing-clusterresourcequotas_setting-quotas-across-multiple-projects) Copy linkLink copied to clipboard!

View the multi-project quota documents applied to your project by using the `AppliedClusterResourceQuota` resource. Although, as an administrator, you cannot create or modify multi-project quotas, you can monitor your project’s resource limits.

**Procedure**

* To view quotas applied to a project, run:

  ```
  $ oc describe AppliedClusterResourceQuota
  ```

  **Example output**

  ```
  Name:   for-user
  Namespace:  <none>
  Created:  19 hours ago
  Labels:   <none>
  Annotations:  <none>
  Label Selector: <null>
  AnnotationSelector: map[openshift.io/requester:<user-name>]
  Resource  Used  Hard
  --------  ----  ----
  pods        1     10
  secrets     9     20
  ```

#### [8.2.3. Selection granularity](#quotas-selection-granularity_setting-quotas-across-multiple-projects) Copy linkLink copied to clipboard!

When you create a multi-project quota, restrict the number of active projects to avoid degrading API server responsiveness.

When you configure a multi-project quota using a `ClusterResourceQuota` object, restrict the number of selected active projects to 100 or fewer. Because quota allocation claims require system locking, selecting more than 100 projects under a single multi-project quota can severely degrade API server responsiveness across those projects.

## [Chapter 9. Using config maps with applications](#config-maps) Copy linkLink copied to clipboard!

By using a config map, you can decouple configuration artifacts from image content to keep containerized applications portable.

The following sections define config maps, explain how to create and use them, and describe use cases for consuming `ConfigMap` objects in pods.

### [9.1. Understanding config maps](#nodes-pods-configmap-overview_config-maps) Copy linkLink copied to clipboard!

You can review the following sections to learn how to use config maps to make configuration values available to your pods separately from application code.

Many applications require configuration by using some combination of configuration files, command-line arguments, and environment variables. In OpenShift Container Platform, these configuration artifacts are decoupled from image content to keep containerized applications portable.

The `ConfigMap` object provides mechanisms to inject containers with configuration data while keeping containers agnostic of OpenShift Container Platform. A config map can be used to store fine-grained information like individual properties or coarse-grained information like entire configuration files or JSON blobs.

The `ConfigMap` object holds key-value pairs of configuration data that can be consumed in pods or used to store configuration data for system components such as controllers. For example:

**`ConfigMap` Object Definition**

```
kind: ConfigMap
apiVersion: v1
metadata:
  creationTimestamp: 2016-02-18T19:14:38Z
  name: example-config
  namespace: my-namespace
data:
  example.property.1: hello
  example.property.2: world
  example.property.file: |-
    property.1=value-1
    property.2=value-2
    property.3=value-3
binaryData:
  bar: L3Jvb3QvMTAw
```

where:

`data`
:   Specifies the configuration data.

`binaryData.bar`
:   Specifies a file that contains non-UTF8 data, for example, a binary Java keystore file. Enter the file data in Base 64.

Note

You can use the `binaryData` field when you create a config map from a binary file, such as an image.

Configuration data can be consumed in pods in a variety of ways. A config map can be used to:

* Populate environment variable values in containers
* Set command-line arguments in a container
* Populate configuration files in a volume

Users and system components can store configuration data in a config map.

A config map is similar to a secret, but designed to more conveniently support working with strings that do not contain sensitive information.

#### [9.1.1. Config map restrictions](#nodes-pods-configmap-overview-restrictions) Copy linkLink copied to clipboard!

**A config map must be created before its contents can be consumed in pods.**

Controllers can be written to tolerate missing configuration data. Consult individual components configured by using config maps on a case-by-case basis.

**`ConfigMap` objects reside in a project.**

They can only be referenced by pods in the same project.

**The Kubelet only supports the use of a config map for pods it gets from the API server.**

This includes any pods created by using the CLI, or indirectly from a replication controller. It does not include pods created by using the OpenShift Container Platform node’s `--manifest-url` flag, its `--config` flag, or its REST API because these are not common ways to create pods.

#### [9.1.2. Populating environment variables in containers by using config maps](#nodes-pods-configmaps-use-case-consuming-in-env-vars_config-maps) Copy linkLink copied to clipboard!

You can use config maps to populate individual environment variables in containers or to populate environment variables in containers from all keys that form valid environment variable names.

The following example `ConfigMap` custom resource (CR) contains two environment variables:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: special-config
  namespace: default
data:
  special.how: very
  special.type: charm
```

where:

`metadata.name`
:   Specifies the name of the config map.

`metadata.namespace`
:   Specifies the project in which the config map resides. Config maps can only be referenced by pods in the same project.

`data`
:   Specifies the environment variables to inject.

The following example `ConfigMap` (CR) contains one environment variable:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: env-config
  namespace: default
data:
  log_level: INFO
```

where:

`metadata.name`
:   Specifies the name of the config map.

`metadata.namespace`
:   Specifies the project in which the config map resides. Config maps can only be referenced by pods in the same project.

`data`
:   Specifies the environment variables to inject.

**Procedure**

* You can consume the keys of this `ConfigMap` in a pod using `configMapKeyRef` sections.

  **Sample `Pod` specification configured to inject specific environment variables**

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: dapi-test-pod
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
      - name: test-container
        image: gcr.io/google_containers/busybox
        command: [ "/bin/sh", "-c", "env" ]
        env:
          - name: SPECIAL_LEVEL_KEY
            valueFrom:
              configMapKeyRef:
                name: special-config
                key: special.how
          - name: SPECIAL_TYPE_KEY
            valueFrom:
              configMapKeyRef:
                name: special-config
                key: special.type
                optional: true
        envFrom:
          - configMapRef:
              name: env-config
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
    restartPolicy: Never
  ```

  where:

  `spec.containers.env`
  :   Specifies the environment variables to pull from a config map.

  `spec.containers.env.name`
  :   Specifies the name of a pod environment variable that you are injecting a key’s value into.

  `spec.containers.env.valueFrom.configMapKeyRef.name`
  :   Specifies the name of the config map to pull specific environment variables from.

  `spec.containers.env.valueFrom.configMapKeyRef.key`
  :   Specifies the environment variable to pull from the config map.

  `spec.containers.env.valueFrom.configMapKeyRef.optional`
  :   Specifies that the environment variable is optional. As optional, the pod will be started even if the specified config map and keys do not exist.

  `spec.containers.envFrom.configMapRef`
  :   Specifies the name of the config map to pull all environment variables from.

  When this pod is run, the pod logs will include the following output:

  ```
  SPECIAL_LEVEL_KEY=very
  log_level=INFO
  ```

  Note

  `SPECIAL_TYPE_KEY=charm` is not listed in the example output because `optional: true` is set.

#### [9.1.3. Setting command-line arguments for container commands with config maps](#nodes-pods-configmaps-use-case-setting-command-line-arguments_config-maps) Copy linkLink copied to clipboard!

You can use config maps to set the value of the commands or arguments in a container by using the Kubernetes substitution syntax `$(VAR_NAME)`.

As an example, consider the following config map:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: special-config
  namespace: default
data:
  special.how: very
  special.type: charm
```

**Procedure**

* To inject values into a command in a container, you must consume the keys you want to use as environment variables. Then you can refer to them in a container’s command using the `$(VAR_NAME)` syntax.

  **Sample pod specification configured to inject specific environment variables**

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: dapi-test-pod
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
      - name: test-container
        image: gcr.io/google_containers/busybox
        command: [ "/bin/sh", "-c", "echo $(SPECIAL_LEVEL_KEY) $(SPECIAL_TYPE_KEY)" ]
        env:
          - name: SPECIAL_LEVEL_KEY
            valueFrom:
              configMapKeyRef:
                name: special-config
                key: special.how
          - name: SPECIAL_TYPE_KEY
            valueFrom:
              configMapKeyRef:
                name: special-config
                key: special.type
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
    restartPolicy: Never
  ```

  where:

  `spec.containers.command`
  :   Specifies values to inject into a command in a container by using the keys you want to use as environment variables.

  When this pod is run, the output from the echo command run in the test-container container is as follows:

  ```
  very charm
  ```

#### [9.1.4. Injecting content into a volume by using config maps](#nodes-pods-configmaps-use-case-consuming-in-volumes_config-maps) Copy linkLink copied to clipboard!

You can use config maps to inject content into a volume.

The following example `ConfigMap` custom resource (CR) contains two environment variables:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: special-config
  namespace: default
data:
  special.how: very
  special.type: charm
```

The following procedure describes options for injecting content into a volume by using config maps.

**Procedure**

* The most basic way to inject content into a volume by using a config map is to populate the volume with files where the key is the file name and the content of the file is the value of the key:

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: dapi-test-pod
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
      - name: test-container
        image: gcr.io/google_containers/busybox
        command: [ "/bin/sh", "-c", "cat", "/etc/config/special.how" ]
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
    volumes:
      - name: config-volume
        configMap:
          name: special-config
    restartPolicy: Never
  ```

  where:

  `spec.volumes.configMap.name`
  :   Specifies a file containing key.

      When this pod is run, the output of the cat command will be:

      ```
      very
      ```
* You can also control the paths within the volume where config map keys are projected:

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: dapi-test-pod
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
      - name: test-container
        image: gcr.io/google_containers/busybox
        command: [ "/bin/sh", "-c", "cat", "/etc/config/path/to/special-key" ]
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
    volumes:
      - name: config-volume
        configMap:
          name: special-config
          items:
          - key: special.how
            path: path/to/special-key
    restartPolicy: Never
  ```

  where:

  `spec.volumes.configMap.items.path`
  :   Specifies the path to config map key.

  When this pod is run, the output of the cat command is `very`.

## [Chapter 10. Monitoring project and application metrics by using the Developer perspective](#odc-monitoring-project-and-application-metrics-using-developer-perspective_config-maps) Copy linkLink copied to clipboard!

The **Observe** view in the **Developer** perspective enables you to monitor project and application metrics to track performance, troubleshoot issues, and respond to alerts. For example, CPU, memory, and bandwidth usage, and network related information.

### [10.1. Prerequisites](#prerequisites_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

* You have created and deployed applications on OpenShift Container Platform.
* You have logged in to the web console.
* The **Developer** perspective is enabled and you have switched to it.

Important

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. The **Developer** perspective is no longer enabled by default.

All users can interact with all OpenShift Container Platform web console features. However, if you are not the cluster owner, you might need to request permission to access certain features from the cluster owner.

You can still enable the **Developer** perspective. On the **Getting Started** pane in the web console, you can take a tour of the console, find information on setting up your cluster, view a quick start for enabling the **Developer** perspective, and follow links to explore new features and capabilities.

See also, "Enabling the **Developer** perspective in the web console".

### [10.2. Enabling the Developer perspective in the web console](#enabling-developer-perspective_web-console_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

Enable the **Developer** perspective in the web console to give your developers tools to manage applications, visualize topology, and monitor projects as they develop and build them.

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. There is no longer a **Developer** perspective by default; however, cluster administrators can enable the **Developer** perspective for developers to use.

You can enable the **Developer** perspective with the following steps:

**Prerequisites**

* You have access to the web console as a user with `cluster-admin` privileges.

**Procedure**

1. Navigate to the **Cluster Settings** page by clicking Administration → Cluster Settings.
2. Select the **Configuration** tab.
3. Type `console` in the search field to locate the Console Operator resource and select `operator.openshift.io`.
4. On the **Cluster Details** page, click the **Actions** menu and select **Customize**.
5. In the **General** tab, locate the **Perspectives** section. You can enable or disable the **Developer** perspective as needed. Changes are automatically applied.
6. Optional: You can enable the **Developer** perspective by using the CLI with the following command:

   ```
   $ oc patch console.operator.openshift.io/cluster --type='merge' -p '{"spec":{"customization":{"perspectives":[{"id":"dev","visibility":{"state":"Enabled"}}]}}}'
   ```

   Note

   The change reflects in the web console after the console pod restarts successfully.

**Verification**

1. Locate the perspective switcher in the web console.
2. Verify that **Developer** is displayed as an available perspective option.

### [10.3. Monitoring capabilities from the Developer perspective](#monitoring-capabilities-in-the-developer-perspective_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

The **Observe** view in the **Developer** perspective shows monitoring tools filtered by your project access permissions to track performance, troubleshoot issues, and respond to alerts. You can monitor CPU, memory, bandwidth, and network metrics.

Important

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. The **Developer** perspective is no longer enabled by default.

All users can interact with all OpenShift Container Platform web console features. However, if you are not the cluster owner, you might need to request permission to access certain features from the cluster owner.

You can still enable the **Developer** perspective. On the **Getting Started** pane in the web console, you can take a tour of the console, find information on setting up your cluster, view a quick start for enabling the **Developer** perspective, and follow links to explore new features and capabilities.

See also, "Enabling the **Developer** perspective in the web console".

The **Observe** view in the **Developer** perspective uses the same monitoring components as the **Administrator** perspective, but displays only the projects you have permissions for. You can monitor your applications without seeing cluster-wide metrics you cannot access.

Note

A project represents a Kubernetes namespace with additional annotations. When you select a project in the **Developer** perspective, you view the topology and metrics for that namespace.

After selecting a project in the **Observe** view, the following tabs become available:

* **Events**: Cluster events filtered by the selected project
* **Alerting rules**: Configured alerting rules and their current state
* **Alerts**: Firing alerts for the selected project
* **Dashboards**: Pre-built visual dashboards showing resource consumption graphs including CPU usage, memory usage, bandwidth consumption, and network-related information
* **Metrics**: Prometheus query interface for analyzing specific metrics
* **Silences**: Create and manage alert silences to temporarily suppress alert notifications

The monitoring interface is the same as the **Administrator** perspective, with the key difference being project filtering based on your access permissions.

Note

In the **Administrator** perspective, the monitoring tabs are immediately available with a project dropdown for filtering. In the **Developer** perspective, you must select a project before the tabs are displayed. This scoping enables your developers to observe their applications by using the same monitoring tools as cluster administrators, focused only on their assigned projects.

### [10.4. Viewing project dashboards](#view-project-dashboards_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

View pre-built dashboards showing CPU usage, memory usage, bandwidth consumption, and network information across your project (namespace) topology to help you monitor application performance.

**Procedure**

1. In the **Developer** perspective navigation menu, select **Observe**.
2. Select a project from the **Project** list. After you select a project, the monitoring tabs are displayed.
3. Click the **Dashboards** tab.

   The **Dashboards** tab displays pre-built Kubernetes compute resources dashboards showing metrics such as CPU usage, memory usage, bandwidth consumption, and network-related information. The dashboard layout includes metric cards at the top showing current utilization percentages, and expandable graph sections below showing detailed resource usage trends over time.

### [10.5. Monitoring your application metrics](#odc-monitoring-your-application-metrics_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

Inspect alerts, metric charts, and health check status for individual application workloads to troubleshoot performance issues and monitor health directly from the topology view.

**Procedure**

1. In the **Developer** perspective, navigate to the **Topology** view.
2. Click the workload node to open the side panel.
3. Select the **Observe** tab to view workload-specific metrics:

   * Review active critical and warning alerts associated with the workload.
   * View CPU, memory, and bandwidth usage charts.
   * Click **View monitoring dashboard** to open the full metrics dashboard for the workload.

     Note

     Only critical and warning alerts in the **Firing** state are displayed in the **Topology** view. Alerts in the **Silenced**, **Pending** and **Not Firing** states are not displayed.

### [10.6. Image vulnerability metrics and severity levels](#odc-image-vulnerabilities-breakdown_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

Review container image security scan results on the project dashboard to identify and prioritize vulnerabilities for remediation.

In the **Developer** perspective, the project dashboard shows the **Image Vulnerabilities** link in the **Status** section. Using this link, you can view the **Image Vulnerabilities breakdown** window, which displays metrics such as the total count of vulnerable container images and fixable container images, organized by severity. The icon color indicates severity:

* Red: High severity. Fix immediately.
* Orange: Medium severity. Can be fixed after high-severity vulnerabilities.
* Yellow: Low severity. Can be fixed after high and medium-severity vulnerabilities.

Based on the severity level, you can prioritize vulnerabilities and fix them in an organized manner.

### [10.7. Monitoring your application and image vulnerabilities metrics](#odc-monitoring-your-application-image-vulnerabilities-metrics_odc-monitoring-project-and-application-metrics-using-developer-perspective) Copy linkLink copied to clipboard!

Analyze application dependency vulnerabilities across your cluster to identify and remediate security issues in container images.

After you create applications in your project and deploy them, use the **Developer** perspective in the web console to see the metrics for your application dependency vulnerabilities across your cluster. The metrics help you to analyze the following image vulnerabilities in detail:

* Total count of vulnerable images in a selected project
* Severity-based counts of all vulnerable images in a selected project
* Drill down into severity to obtain the details, such as count of vulnerabilities, count of fixable vulnerabilities, and number of affected pods for each vulnerable image

**Prerequisites**

* You have installed the Red Hat Quay Container Security Operator.

  Note

  The Red Hat Quay Container Security Operator detects vulnerabilities by scanning the images that are in the Red Hat Quay registry.

**Procedure**

1. In the **Developer** perspective, click **Project** to open the project dashboard.
2. For a detailed vulnerabilities overview, click the **Vulnerabilities** tab.

   1. To get more detail about an image, click its name.
   2. View the default graph with all types of vulnerabilities in the **Details** tab.
   3. Optional: Click the toggle button to view a specific type of vulnerability. For example, click **App dependency** to see vulnerabilities specific to application dependency.
   4. Optional: You can filter the list of vulnerabilities based on their **Severity** and **Type** or sort them by **Severity**, **Package**, **Type**, **Source**, **Current Version**, and **Fixed in Version**.
   5. Click a **Vulnerability** to get its associated details:

      * **Base image** vulnerabilities display information from a Red Hat Security Advisory (RHSA).
      * **App dependency** vulnerabilities display information from the Snyk security application.

## [Chapter 11. Monitoring application health by using health checks](#application-health) Copy linkLink copied to clipboard!

You can monitor application health on your OpenShift Container Platform cluster by configuring readiness, liveness, and startup probes for your application containers. You can also observe probe failure events so you can address issues before they affect users.

In software systems, components can become unhealthy due to transient issues such as temporary connectivity loss, configuration errors, or problems with external dependencies. OpenShift Container Platform applications have a number of options to detect and handle unhealthy containers.

### [11.1. Health checks](#application-health-about_application-health) Copy linkLink copied to clipboard!

You can configure health checks by understanding the differences between readiness, liveness, and startup probes.

A health check periodically performs diagnostics on a running container using any combination of the readiness, liveness, and startup health checks.

You can include one or more probes in the specification for the pod that contains the container which you want to perform the health checks.

Note

If you want to add or edit health checks in an existing pod, you must edit the pod `DeploymentConfig` object or use the web console. You cannot use the CLI to add or edit health checks for an existing pod.

Readiness probe
:   A *readiness probe* determines if a container is ready to accept service requests. If the readiness probe fails for a container, the kubelet removes the pod from the list of available service endpoints.

    After a failure, the probe continues to examine the pod. If the pod becomes available, the kubelet adds the pod to the list of available service endpoints.

Liveness health check
:   A *liveness probe* determines if a container is still running. If the liveness probe fails due to a condition such as a deadlock, the kubelet kills the container. The pod then responds based on the pod restart policy.

    For example, a liveness probe on a pod with a `restartPolicy` of `Always` or `OnFailure` kills and restarts the container.

Startup probe
:   A *startup probe* indicates whether the application within a container is started. All other probes are disabled until the startup succeeds. If the startup probe does not succeed within a specified time period, the kubelet kills the container, and the container is subject to the pod `restartPolicy`.

    Some applications can require additional startup time on their first initialization. You can use a startup probe with a liveness or readiness probe to delay that probe long enough to handle lengthy start-up time using the `failureThreshold` and `periodSeconds` parameters.

    For example, you can add a startup probe to a liveness probe. Use a `failureThreshold` of 30 failures and a `periodSeconds` of 10 seconds. This combination (30 × 10s = 300s) gives a maximum startup window of 5 minutes. After the startup probe succeeds the first time, the liveness probe takes over.

You can configure liveness, readiness, and startup probes with any of the following types of tests:

* HTTP `GET`: When using an HTTP `GET` test, the test determines the healthiness of the container by using a webhook. The test is successful if the HTTP response code is between `200` and `399`.

  You can use an HTTP `GET` test with applications that return HTTP status codes when completely initialized.
* Container Command: When using a container command test, the probe executes a command inside the container. The probe is successful if the test exits with a `0` status.
* Transmission Control Protocol (TCP) socket: When using a TCP socket test, the probe attempts to open a socket to the container. The container is considered healthy only if the probe can establish a connection. You can use a TCP socket test with applications that do not start listening until initialization is complete.

You can configure several fields to control the behavior of a probe:

* `initialDelaySeconds`: The time, in seconds, after the container starts before the probe can be scheduled. The default is 0.
* `periodSeconds`: The delay, in seconds, between performing probes. The default is `10`. This value must be greater than `timeoutSeconds`.
* `timeoutSeconds`: The number of seconds of inactivity after which the probe times out and the container is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.
* `successThreshold`: The number of times that the probe must report success after a failure to reset the container status to successful. The value must be `1` for a liveness probe. The default is `1`.
* `failureThreshold`: The number of times that the probe is allowed to fail. The default is 3. When the threshold is reached:

  + for a liveness probe, the container is restarted
  + for a readiness probe, the pod is marked `Unready`
  + for a startup probe, the container is killed and is subject to the `restartPolicy` of the pod

#### [11.1.1. Example probes](#application-health-examples_application-health) Copy linkLink copied to clipboard!

The following are samples of different probes as they appear in an object specification.

**Sample readiness probe with a container command readiness probe in a pod spec**

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app
    args:
    image: registry.k8s.io/goproxy:0.1
    readinessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
# ...
```

where:

`spec.containers.name`
:   Specifies the container name.

`spec.containers.image`
:   Specifies the container image to deploy.

`spec.containers.readinessProbe`
:   Specifies a readiness probe.

`spec.containers.readinessProbe.exec`
:   Specifies a container command test.

`spec.containers.readinessProbe.exec.command`
:   Specifies the commands to execute on the container.

**Sample container command startup probe and liveness probe with container command tests in a pod spec**

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app
    args:
    image: registry.k8s.io/goproxy:0.1
    livenessProbe:
      httpGet:
        scheme: HTTPS
        path: /healthz
        port: 8080
        httpHeaders:
        - name: X-Custom-Header
          value: Awesome
    startupProbe:
      httpGet:
        path: /healthz
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
# ...
```

where:

`spec.containers.name`
:   Specifies the container name.

`spec.containers.image`
:   Specifies the container image to deploy.

`spec.containers.livenessProbe`
:   Specifies a liveness probe.

`spec.containers.livenessProbe.httpGet`
:   Specifies an HTTP `GET` test.

`spec.containers.livenessProbe.httpGet.scheme`
:   Specifies the internet scheme: `HTTP` or `HTTPS`. The default value is `HTTP`.

`spec.containers.livenessProbe.httpGet.port`
:   Specifies the port on which the container is listening.

`spec.containers.startupProbe`
:   Specifies a startup probe.

`spec.containers.startupProbe.httpGet`
:   Specifies an HTTP `GET` test.

`spec.containers.startupProbe.httpGet.port`
:   Specifies the port on which the container is listening.

`spec.containers.startupProbe.failureThreshold`
:   Specifies the number of times to try the probe after a failure.

`spec.containers.startupProbe.periodSeconds`
:   Specifies the number of seconds to perform the probe.

**Sample liveness probe with a container command test that uses a timeout in a pod spec**

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app
    args:
    image: registry.k8s.io/goproxy:0.1
    livenessProbe:
      exec:
        command:
        - /bin/bash
        - '-c'
        - timeout 60 /opt/eap/bin/livenessProbe.sh
      periodSeconds: 10
      successThreshold: 1
      failureThreshold: 3
# ...
```

where:

`spec.containers.name`
:   Specifies the container name.

`spec.containers.image`
:   Specifies the container image to deploy.

`spec.containers.livenessProbe`
:   Specifies the liveness probe.

`spec.containers.livenessProbe.exec`
:   Specifies the type of probe, here a container command probe.

`spec.containers.livenessProbe.exec.command`
:   Specifies the command line to execute inside the container.

`spec.containers.livenessProbe.periodSeconds`
:   Specifies how often in seconds to perform the probe.

`spec.containers.livenessProbe.successThreshold`
:   Specifies the number of consecutive successes needed to show success after a failure.

`spec.containers.livenessProbe.failureThreshold`
:   Specifies the number of times to try the probe after a failure.

**Sample readiness probe and liveness probe with a TCP socket test in a deployment**

```
kind: Deployment
apiVersion: apps/v1
metadata:
  labels:
    test: health-check
  name: my-application
spec:
# ...
  template:
    spec:
      containers:
        - resources: {}
          readinessProbe:
            tcpSocket:
              port: 8080
            timeoutSeconds: 1
            periodSeconds: 10
            successThreshold: 1
            failureThreshold: 3
          terminationMessagePath: /dev/termination-log
          name: ruby-ex
          livenessProbe:
            tcpSocket:
              port: 8080
            initialDelaySeconds: 15
            timeoutSeconds: 1
            periodSeconds: 10
            successThreshold: 1
            failureThreshold: 3
# ...
```

where:

`spec.template.spec.containers.readinessProbe`
:   Specifies the readiness probe.

`spec.template.spec.containers.livenessProbe`
:   Specifies the liveness probe.

### [11.2. Configuring health checks using the CLI](#application-health-configuring_application-health) Copy linkLink copied to clipboard!

To configure readiness, liveness, and startup probes, add one or more probes to the specification for the pod that contains the container on which you want to perform the health checks. Probes let the cluster detect unhealthy containers and respond before failures affect application availability.

Note

If you want to add or edit health checks in an existing pod, you must edit the pod `DeploymentConfig` object or use the web console. You cannot use the CLI to add or edit health checks for an existing pod.

**Procedure**

1. Create a YAML file that defines a `Pod` object with one or more probes:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     labels:
       test: health-check
     name: my-application
   spec:
     containers:
     - name: my-container
       args:
       image: registry.k8s.io/goproxy:0.1
       livenessProbe:
         tcpSocket:
           port: 8080
         initialDelaySeconds: 15
         periodSeconds: 20
         timeoutSeconds: 10
       readinessProbe:
         httpGet:
           host: my-host
           scheme: HTTPS
           path: /healthz
           port: 8080
       startupProbe:
         exec:
           command:
           - cat
           - /tmp/healthy
         failureThreshold: 30
         periodSeconds: 20
         timeoutSeconds: 10
   ```

   Note

   Include only the probe types your application needs. The example shows liveness, readiness, and startup probes together for reference.

   where:

   `spec.containers.name`
   :   Specifies the container name.

   `spec.containers.image`
   :   Specifies the container image to deploy.

   `spec.containers.livenessProbe`
   :   Specifies a liveness probe. This value is optional.

   `spec.containers.livenessProbe.tcpSocket`
   :   Specifies a test to perform, here a Transmission Control Protocol (TCP) socket test.

   `spec.containers.livenessProbe.tcpSocket.port`
   :   Specifies the port on which the container is listening.

   `spec.containers.livenessProbe.initialDelaySeconds`
   :   Specifies the time, in seconds, after the container starts before the probe can be scheduled.

   `spec.containers.livenessProbe.periodSeconds`
   :   Specifies the number of seconds to perform the probe. The default is `10`. This value must be greater than `timeoutSeconds`.

   `spec.containers.livenessProbe.timeoutSeconds`
   :   Specifies the number of seconds of inactivity after which the probe is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.

   `spec.containers.readinessProbe`
   :   Specifies a readiness probe. This value is optional.

   `spec.containers.readinessProbe.httpGet`
   :   Specifies the type of test to perform, here an HTTP test.

   `spec.containers.readinessProbe.httpGet.host`
   :   Specifies a host IP address. When `host` is not defined, the `PodIP` is used.

   `spec.containers.readinessProbe.httpGet.scheme`
   :   Specifies `HTTP` or `HTTPS`. When `scheme` is not defined, the `HTTP` scheme is used.

   `spec.containers.readinessProbe.httpGet.port`
   :   Specifies the port on which the container is listening.

   `spec.containers.startupProbe`
   :   Specifies a startup probe. This value is optional.

   `spec.containers.startupProbe.exec`
   :   Specifies the type of test to perform, here a container execution probe.

   `spec.containers.startupProbe.exec.command`
   :   Specifies the commands to execute on the container.

   `spec.containers.startupProbe.failureThreshold`
   :   Specifies the number of times to try the probe after a failure.

   `spec.containers.startupProbe.periodSeconds`
   :   Specifies the number of seconds to perform the probe. The default is `10`. This value must be greater than `timeoutSeconds`.

   `spec.containers.startupProbe.timeoutSeconds`
   :   Specifies the number of seconds of inactivity after which the probe is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.

       Note

       If the `initialDelaySeconds` value is lower than the `periodSeconds` value, the first readiness probe occurs at some point between the two periods due to an issue with timers.

       The `timeoutSeconds` value must be lower than the `periodSeconds` value.
2. Apply the YAML file by running the following command:

   ```
   $ oc create -f <file-name>.yaml
   ```
3. Verify the state of the health check pod by running the following command:

   ```
   $ oc describe pod my-application
   ```

   **Example output**

   ```
   Events:
     Type    Reason     Age   From                                  Message
     ----    ------     ----  ----                                  -------
     Normal  Scheduled  9s    default-scheduler                     Successfully assigned openshift-logging/liveness-exec to ip-10-0-143-40.ec2.internal
     Normal  Pulling    2s    kubelet, ip-10-0-143-40.ec2.internal  pulling image "registry.k8s.io/liveness"
     Normal  Pulled     1s    kubelet, ip-10-0-143-40.ec2.internal  Successfully pulled image "registry.k8s.io/liveness"
     Normal  Created    1s    kubelet, ip-10-0-143-40.ec2.internal  Created container
     Normal  Started    1s    kubelet, ip-10-0-143-40.ec2.internal  Started container
   ```

   The following example shows output when a liveness probe fails and the container is restarted:

   ```
   ....

   Events:
     Type     Reason          Age                From                                               Message
     ----     ------          ----               ----                                               -------
     Normal   Scheduled       <unknown>                                                             Successfully assigned aaa/liveness-http to ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj
     Normal   AddedInterface  47s                multus                                             Add eth0 [10.129.2.11/23]
     Normal   Pulled          46s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 773.406244ms
     Normal   Pulled          28s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 233.328564ms
     Normal   Created         10s (x3 over 46s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Created container liveness
     Normal   Started         10s (x3 over 46s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Started container liveness
     Warning  Unhealthy       10s (x6 over 34s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Liveness probe failed: HTTP probe failed with statuscode: 500
     Normal   Killing         10s (x2 over 28s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Container liveness failed liveness probe, will be restarted
     Normal   Pulling         10s (x3 over 47s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Pulling image "registry.k8s.io/liveness"
     Normal   Pulled          10s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 244.116568ms
   ```

### [11.3. Application health monitoring by using the Developer perspective](#odc-monitoring-application-health-using-developer-perspective_application-health) Copy linkLink copied to clipboard!

You can monitor application health by adding readiness, liveness, and startup probes from the **Developer** perspective, either when you deploy an application or on a deployed application. Probes detect unhealthy containers and keep applications available before failures affect users.

You can use the **Developer** perspective to add three types of health probes to your container to ensure that your application is healthy:

* Use a readiness probe to check if the container is ready to handle requests.
* Use a liveness probe to check if the container is running.
* Use a startup probe to check if the application within the container has started.

You can add health checks either while creating and deploying an application, or after you have deployed an application.

### [11.4. Editing health checks using the Developer perspective](#odc-editing-health-checks_application-health) Copy linkLink copied to clipboard!

You can edit, remove, or add readiness, liveness, and startup probes on a deployed application from the **Topology** view in the **Developer** perspective. Use the **Edit Health Checks** page to update probe parameters, remove probes, or add new probe types.

**Prerequisites**

* You have switched to the **Developer** perspective in the web console.
* You have created and deployed an application on OpenShift Container Platform using the **Developer** perspective.
* You have added health checks to your application.

**Procedure**

1. In the **Topology** view, right-click your application and select **Edit Health Checks**. Alternatively, in the side panel, click the **Actions** drop-down list and select **Edit Health Checks**.
2. To remove a previously added health probe, click the **Remove** icon adjoining it.
3. To edit the parameters of an existing probe:

   1. Click the **Edit Probe** link next to a previously added probe to see the parameters for the probe.
   2. Modify the parameters as required, and click the check mark to save your changes.
4. To add a new health probe, click the add probe links. For example, to add a liveness probe that checks if your container is running:

   1. Click **Add Liveness Probe** to see a form containing the parameters for the probe.
   2. Edit the probe parameters as required.

      Note

      The `Timeout` value must be lower than the `Period` value. The `Timeout` default value is `1`. The `Period` default value is `10`.
   3. Click the check mark at the bottom of the form. The **Liveness Probe Added** message is displayed.
5. Click **Save** to save your modifications and add the additional probes to your container. You are redirected to the **Topology** view.

**Verification**

1. In the side panel, verify that the probes have been added by clicking on the deployed pod under the **Pods** section.
2. In the **Pod Details** page, click the listed container in the **Containers** section.
3. In the **Container Details** page, verify that the Liveness probe - `HTTP Get 10.129.4.65:8080/` has been added to the container, in addition to the earlier existing probes.

### [11.5. Monitoring health check failures using the Developer perspective](#odc-monitoring-health-checks_application-health) Copy linkLink copied to clipboard!

You can monitor health check failures for a deployed application from the **Topology** view in the **Developer** perspective. Use the **Observe** tab to view events that report probe failures and show when containers need attention before users are affected.

**Prerequisites**

* You have switched to the **Developer** perspective in the web console.
* You have created and deployed an application on OpenShift Container Platform using the **Developer** perspective.
* You have added health checks to your application.

**Procedure**

1. In the **Topology** view, click the application node to see the side panel.
2. Click the **Observe** tab to see health check failure events in the **Events (Warning)** section.
3. Click the down arrow adjoining **Events (Warning)** to see the details of the health check failure.

## [Chapter 12. Editing applications](#odc-editing-applications) Copy linkLink copied to clipboard!

You can edit the configuration and the source code of the application you create using the **Topology** view.

### [12.1. Prerequisites](#prerequisites-3) Copy linkLink copied to clipboard!

* You have the appropriate [roles and permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#default-roles_using-rbac) in a project to create and modify applications in OpenShift Container Platform.
* You have [created and deployed an application on OpenShift Container Platform using the **Developer** perspective](#odc-creating-applications-using-developer-perspective "3.2. Creating applications by using the Developer perspective").
* You have [logged in to the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#web-console) and have switched to [the **Developer** perspective](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#about-developer-perspective_web-console-overview).

### [12.2. Editing the source code of an application using the Developer perspective](#odc-editing-source-code-using-developer-perspective_odc-editing-applications) Copy linkLink copied to clipboard!

You can use the **Topology** view in the **Developer** perspective to edit the source code of your application.

**Procedure**

* In the **Topology** view, click the **Edit Source code** icon, displayed at the bottom-right of the deployed application, to access your source code and modify it.

  Note

  This feature is available only when you create applications using the **From Git**, **From Catalog**, and the **From Dockerfile** options.

  If the **Eclipse Che** Operator is installed in your cluster, a Che workspace (
  ) is created and you are directed to the workspace to edit your source code. If it is not installed, you will be directed to the Git repository (
  ) your source code is hosted in.

### [12.3. Editing the application configuration using the Developer perspective](#odc-editing-application-configuration-using-developer-perspective_odc-editing-applications) Copy linkLink copied to clipboard!

You can use the **Topology** view in the **Developer** perspective to edit the configuration of your application.

Note

Currently, only configurations of applications created by using the **From Git**, **Container Image**, **From Catalog**, or **From Dockerfile** options in the **Add** workflow of the **Developer** perspective can be edited. Configurations of applications created by using the CLI or the **YAML** option from the **Add** workflow cannot be edited.

**Prerequisites**

Ensure that you have created an application using the **From Git**, **Container Image**, **From Catalog**, or **From Dockerfile** options in the **Add** workflow.

**Procedure**

1. After you have created an application and it is displayed in the **Topology** view, right-click the application to see the edit options available.

   **Figure 12.1. Edit application**
2. Click **Edit *application-name*** to see the **Add** workflow you used to create the application. The form is pre-populated with the values you had added while creating the application.
3. Edit the necessary values for the application.

   Note

   You cannot edit the **Name** field in the **General** section, the CI/CD pipelines, or the **Create a route to the application** field in the **Advanced Options** section.
4. Click **Save** to restart the build and deploy a new image.

   **Figure 12.2. Edit and redeploy application**

## [Chapter 13. Pruning objects to reclaim resources](#pruning-objects) Copy linkLink copied to clipboard!

Reclaim cluster storage and optimize API server performance by pruning stale resources. You can run manual CLI commands or configure automated cron jobs to clean up obsolete deployment, build, image, and group records.

Over time, API objects created in OpenShift Container Platform can accumulate in the cluster’s etcd data store through normal user operations, such as when building and deploying applications.

Cluster administrators can periodically prune older versions of objects from the cluster that are no longer required. For example, by pruning images you can delete older images and layers that are no longer in use, but are still taking up disk space.

### [13.1. Basic pruning operations](#pruning-basic-operations_pruning-objects) Copy linkLink copied to clipboard!

Remove obsolete or unreferenced cluster objects to reclaim cluster storage and maintain optimal API server performance.

The CLI groups prune operations under a common parent command:

```
$ oc adm prune <object_type> <options>
```

This specifies:

* The `<object_type>` to perform the action on, such as `groups`, `builds`, `deployments`, or `images`.
* The `<options>` supported to prune that object type.

### [13.2. Pruning groups](#pruning-groups_pruning-objects) Copy linkLink copied to clipboard!

Remove stale user group records from external identity providers by using the group pruner. Pruning orphaned groups keeps user management data accurate, ensures cluster security, and prevents unauthorized access permissions.

To prune groups records from an external provider, administrators can run the following command:

```
$ oc adm prune groups \
    --sync-config=path/to/sync/config [<options>]
```

Expand

Table 13.1. oc adm prune groups flags

| Options | Description |
| --- | --- |
| `--confirm` | Indicate that pruning should occur, instead of performing a dry-run. |
| `--blacklist` | Path to the group blacklist file. |
| `--whitelist` | Path to the group whitelist file. |
| `--sync-config` | Path to the synchronization configuration file. |

Show more

**Procedure**

1. To see the groups that the prune command deletes, run the following command:

   ```
   $ oc adm prune groups --sync-config=ldap-sync-config.yaml
   ```
2. To perform the prune operation, add the `--confirm` flag:

   ```
   $ oc adm prune groups --sync-config=ldap-sync-config.yaml --confirm
   ```

### [13.3. Pruning deployment resources](#pruning-deployments_pruning-objects) Copy linkLink copied to clipboard!

Delete completed or failed deployment configurations and pod records to free up cluster storage, reduce database clutter, and speed up resource lookups.

You can prune resources associated with deployments that are no longer required by the system, due to age and status.

The following command prunes replication controllers associated with `DeploymentConfig` objects:

```
$ oc adm prune deployments [<options>]
```

Note

To also prune replica sets associated with `Deployment` objects, use the `--replica-sets` flag. This flag is currently a Technology Preview feature.

Expand

Table 13.2. oc adm prune deployments flags

| Option | Description |
| --- | --- |
| `--confirm` | Indicate that pruning should occur, instead of performing a dry-run. |
| `--keep-complete=<N>` | Per the `DeploymentConfig` object, keep the last `N` replication controllers that have a status of `Complete` and replica count of zero. The default is `5`. |
| `--keep-failed=<N>` | Per the `DeploymentConfig` object, keep the last `N` replication controllers that have a status of `Failed` and replica count of zero. The default is `1`. |
| `--keep-younger-than=<duration>` | Do not prune any replication controller that is younger than `<duration>` relative to the current time. Valid units of measurement include nanoseconds (`ns`), microseconds (`us`), milliseconds (`ms`), seconds (`s`), minutes (`m`), and hours (`h`). The default is `60m`. |
| `--orphans` | Prune all replication controllers that no longer have a `DeploymentConfig` object, has status of `Complete` or `Failed`, and has a replica count of zero. |
| `--replica-sets=true|false` | If `true`, replica sets are included in the pruning process. The default is `false`.  Important  This flag is a Technology Preview feature. |

Show more

**Procedure**

1. To see what a pruning operation would delete, run the following command:

   ```
   $ oc adm prune deployments --orphans --keep-complete=5 --keep-failed=1 \
       --keep-younger-than=60m
   ```
2. To actually perform the prune operation, add the `--confirm` flag:

   ```
   $ oc adm prune deployments --orphans --keep-complete=5 --keep-failed=1 \
       --keep-younger-than=60m --confirm
   ```

### [13.4. Pruning builds](#pruning-builds_pruning-objects) Copy linkLink copied to clipboard!

Prune obsolete build records and logs from your cluster to reclaim cluster storage and prevent API performance degradation.

To prune builds that are no longer required by the system due to age and status, administrators can run the following command:

```
$ oc adm prune builds [<options>]
```

Expand

Table 13.3. oc adm prune builds flags

| Option | Description |
| --- | --- |
| `--confirm` | Indicate that pruning should occur, instead of performing a dry-run. |
| `--orphans` | Prune all builds whose build configuration no longer exists, status is complete, failed, error, or canceled. |
| `--keep-complete=<N>` | Per build configuration, keep the last `N` builds whose status is complete. The default is `5`. |
| `--keep-failed=<N>` | Per build configuration, keep the last `N` builds whose status is failed, error, or canceled. The default is `1`. |
| `--keep-younger-than=<duration>` | Do not prune any object that is younger than `<duration>` relative to the current time. The default is `60m`. |

Show more

**Procedure**

1. To see what a pruning operation would delete, run the following command:

   ```
   $ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
       --keep-younger-than=60m
   ```
2. To actually perform the prune operation, add the `--confirm` flag:

   ```
   $ oc adm prune builds --orphans --keep-complete=5 --keep-failed=1 \
       --keep-younger-than=60m --confirm
   ```

   Note

   Developers can enable automatic build pruning by modifying their build configuration.

### [13.5. Automatically pruning images](#pruning-images_pruning-objects) Copy linkLink copied to clipboard!

To reclaim storage in the OpenShift image registry in OpenShift Container Platform and define image retention period, you can configure the automatic image pruner.

You set the schedule, suspension, and retention options on the pruning custom resource (CR).

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with cluster administrator permissions.
* Install the `oc` CLI.

Important

The behavior of the Image Registry Operator for managing the pruner is independent to the `managementState` specified on the `ClusterOperator` object of the Image Registry Operator. If the Image Registry Operator is not in the `Managed` state, the image pruner can still be configured and managed by the Pruning Custom Resource.

However, the `managementState` of the Image Registry Operator alters the behavior of the deployed image pruner job:

* `Managed`: the `--prune-registry` flag for the image pruner is set to `true`.
* `Removed`: the `--prune-registry` flag for the image pruner is set to `false`, meaning it only prunes image metadata in etcd.

**Procedure**

* Verify that the object named `imagepruners.imageregistry.operator.openshift.io/cluster` contains the following `spec` and `status` fields:

  ```
  spec:
    schedule: 0 0 * * *
    suspend: false
    keepTagRevisions: 3
    keepYoungerThanDuration: 60m
    keepYoungerThan: 3600000000000
    resources: {}
    affinity: {}
    nodeSelector: {}
    tolerations: []
    successfulJobsHistoryLimit: 3
    failedJobsHistoryLimit: 3
  status:
    observedGeneration: 2
    conditions:
    - type: Available
      status: "True"
      lastTransitionTime: 2019-10-09T03:13:45
      reason: Ready
      message: "Periodic image pruner has been created."
    - type: Scheduled
      status: "True"
      lastTransitionTime: 2019-10-09T03:13:45
      reason: Scheduled
      message: "Image pruner job has been scheduled."
    - type: Failed
      staus: "False"
      lastTransitionTime: 2019-10-09T03:13:45
      reason: Succeeded
      message: "Most recent image pruning job succeeded."
  ```

  where:

  `spec.schedule`
  :   `CronJob` formatted schedule. This is an optional field, default is daily at midnight.

  `spec.suspend`
  :   If set to `true`, the `CronJob` running pruning is suspended. This is an optional field, default is `false`. The initial value on new clusters is `false`.

  `spec.keepTagRevisions`
  :   The number of revisions per tag to keep. This is an optional field, default is `3`. The initial value is `3`.

  `spec.keepYoungerThanDuration`
  :   Retain images younger than this duration. This is an optional field. If a value is not specified, either `keepYoungerThan` or the default value `60m` (60 minutes) is used.

  `spec.keepYoungerThan`
  :   Deprecated. The same as `keepYoungerThanDuration`, but the duration is specified as an integer in nanoseconds. This is an optional field. When `keepYoungerThanDuration` is set, this field is ignored.

  `spec.resources`
  :   Standard pod resource requests and limits. This is an optional field.

  `spec.affinity`
  :   Standard pod affinity. This is an optional field.

  `nodeSelector`
  :   Standard pod node selector. This is an optional field.

  `spec.tolerations`
  :   Standard pod tolerations. This is an optional field.

  `spec.successfulJobsHistoryLimit`
  :   The maximum number of successful jobs to retain. Must be greater than or equal to `1` to ensure metrics are reported. This is an optional field, default is `3`. The initial value is `3`.

  `spec.failedJobsHistoryLimit`
  :   The maximum number of failed jobs to retain. Must be greater than or equal `1` to ensure metrics are reported. This is an optional field, default is `3`. The initial value is `3`.

  `status.observedGeneration`
  :   The generation observed by the Operator.

  `status.conditions`
  :   The standard condition objects with the following types:

      + `Available`: Indicates if the pruning job has been created. Reasons can be `Ready` or `Error`.
      + `Scheduled`: Indicates if the next pruning job has been scheduled. Reasons can be `Scheduled`, `Suspended`, or `Error`.
      + `Failed`: Indicates if the most recent pruning job failed.

### [13.6. Manually pruning images](#pruning-images-manual_pruning-objects) Copy linkLink copied to clipboard!

Manually remove orphaned image data from your integrated OpenShift image registry to reclaim storage capacity and prevent node disk exhaustion.

The pruning custom resource enables automatic image pruning for the images from the OpenShift image registry. Administrators can manually prune images with the `oc adm prune images <image_prune_option>` command.

For example:

```
$ oc adm prune images <image_prune_option>
```

For more information about available pruning options, see "Manual image pruning command options".

This command removes images that are no longer required by the system.

Depending on your needs, you can prune images based on their age and tag history, or prune images that cause a project to exceed its defined storage limits.

#### [13.6.1. Image pruning considerations](#pruning-images-considerations_pruning-objects) Copy linkLink copied to clipboard!

Review soft-delete conditions and registry caching behaviors before pruning images to prevent metadata corruption and protect active container deployment layers.

* Pruning with the `--namespace` flag does not remove images. It only removes image streams, because images are cluster-scoped resources. Limiting pruning to a particular namespace makes it impossible to calculate current usage.
* By default, the integrated registry caches metadata of blobs to reduce the number of requests to storage, and to increase request-processing speed. Pruning does not update the integrated registry cache. Images that still contain pruned layers after pruning will be broken because the pruned layers that have metadata in the cache will not be pushed. Therefore, you must redeploy the registry to clear the cache after pruning:

  ```
  $ oc rollout restart deployment/image-registry -n openshift-image-registry
  ```
* If the integrated registry uses a Redis cache, you must clean the database manually.
* If redeploying the registry after pruning is not an option, then you must permanently disable the cache.
* `oc adm prune images` operations require a route for your registry. Registry routes are not created by default.

#### [13.6.2. Image pruning limitations](#pruning-images-limitations_pruning-objects) Copy linkLink copied to clipboard!

Review image layer removal rules and external registry limitations before running prune operations to predict layer deletion and avoid unpruned image streams.

* Pruning images from external registries is unsupported.
* When an image is pruned, all references to the image are removed from all image streams that contain the image in `status.tags`.
* Image layers that are no longer referenced by any images are removed.

#### [13.6.3. Image prune conditions](#pruning-images-conditions_pruning-objects) Copy linkLink copied to clipboard!

Review the prerequisites, dependency checks, and soft-delete conditions required before removing registry images to safely prune image layers without breaking active pod deployments.

OpenShift Container Platform supports two methodologies for pruning images:

1. Pruning by age and tag
2. Pruning by size limit

These methodologies are mutually exclusive. You must choose whether to prune by age and tag, or by size limit. Regardless of the method that you choose, the image pruner checks to ensure that images in use are not removed.

An image is only pruned if it meets the primary condition **and** is not actively referenced by a system component.

Image pruning by age and tag
:   Pruning an image by age and tag is the default pruning strategy. It identifies images for removal by using the `--keep-younger-than` and `--keep-tag-revisions` flags. To prune an image by age and tag, the image must be older than the `--keep-younger-than` threshold, not one of the most recent tag revisions, and cannot be in use by an active workload.

    For an image to be pruned by age and tag, **all** of the following conditions must be met:

    1. The image is managed by OpenShift Container Platform or has the `openshift.io/image.managed` annotation.
    2. The image is older than the time specified by the `--keep-younger-than` flag.
    3. The image is not one of the most recent images for its tag, as specified by the `--keep-tag-revisions` flag.
    4. The image is **not** currently referenced by any of the following active or recent API objects:

       * Pods or image streams created more recently than the `--keep-younger-than` duration.
       * Running or pending pods
       * Deployments, replication controllers, replica sets, or stateful sets.
       * Builds, build configurations, jobs, or cronjobs.

         An image is only removed if it is old, not a recent tag revision, and is confirmed to have no active references by system components.

Image pruning by size limit
:   Pruning an image by size limit uses the `--prune-over-size-limit` flag. This method is used to bring a project back under its defined image storage limit.

    Note

    The `--prune-over-size-limit` flag cannot be combined with the `--keep-tag-revisions` flag nor the `--keep-younger-than` flags. Doing so returns information that this operation is not allowed.

    For an image to be pruned using this method, all of the following conditions must be true:

    1. The image is part of a project that is currently exceeding its smallest defined size limit.
    2. The image is selected by the pruner as a candidate for deletion to reduce the total size.
    3. The image is not currently referenced by any of the following active API objects:

       * Pods that are in a `running` or `pending` state.
       * Deployments, replication controllers, replica sets, or stateful sets.
       * Builds, build configurations, jobs, or cronjobs.

         With this method, the primary trigger is the project’s size, but the safety check to ensure that the image is not actively in use is still performed.

#### [13.6.4. Running image prune operations](#pruning-images-running-operation_pruning-objects) Copy linkLink copied to clipboard!

Securely remove unused container images from your registry to reclaim the cluster disk space and prevent registry storage exhaustion.

**Prerequisites**

* You must be logged into the CLI with an access token.
* You must have the `system:image-pruner` cluster role or greater (for example, `cluster-admin`).
* The image registry must be exposed.
* You have reviewed the "Considerations when manually pruning images" section of this document.

**Procedure**

1. Optional: To preview which images would be pruned, enter the following command. This command prints a list of the images, image streams, and pods that would be removed. Note that nothing is deleted until you add the `--confirm` flag.

   ```
   $ oc adm prune images <image_prune_option_one> <image_prune_option_two>
   ```

   For more information about available pruning options, see "Manual image pruning command options".
2. Review the output to confirm the list of images, image streams, and pods to be removed.
3. Run the `oc adm prune images` command with the appropriate options for your cluster. Add the `--confirm` flag to confirm deletion. For example:

   ```
   $ oc adm prune images <image_prune_option_one> <image_prune_option_two> --confirm
   ```

#### [13.6.5. Using secure or insecure connections](#pruning-images-secure-insecure_pruning-objects) Copy linkLink copied to clipboard!

Configure secure or insecure flags when pruning images to communicate with image registries. Setting custom CA certificates or bypassing HTTPS verification prevents connection failures during pruning.

The secure connection is the preferred and recommended approach. It is done over HTTPS protocol with a mandatory certificate verification. The `prune` command always attempts to use it if possible. If it is not possible, in some cases it can fall-back to insecure connection, which is dangerous. In this case, either certificate verification is skipped or plain HTTP protocol is used.

The fall-back to insecure connection is allowed in the following cases unless `--certificate-authority` is specified:

1. The `prune` command is run with the `--force-insecure` option.
2. The provided `registry-url` is prefixed with the `http://` scheme.
3. The provided `registry-url` is a local-link address or `localhost`.
4. The configuration of the current user allows for an insecure connection. This can be caused by the user either logging in using `--insecure-skip-tls-verify` or choosing the insecure connection when prompted.

Important

If the registry is secured by a certificate authority different from the one used by OpenShift Container Platform, it must be specified using the `--certificate-authority` flag. Otherwise, the `prune` command fails with an error.

#### [13.6.6. Image pruning CLI options](#pruning-images-options_pruning-objects) Copy linkLink copied to clipboard!

Review the CLI options for the `oc adm prune images` command to configure flags for age thresholds, tag references, and registry endpoints.

The following table describes the options you can use with the `oc adm prune images <image_prune_option>` command.

Expand

Table 13.4. Manual image pruning command options

| Option | Description |
| --- | --- |
| `--all` | Include images that were not pushed to the registry, but have been mirrored by pullthrough. This is on by default. To limit the pruning to images that were pushed to the integrated registry, pass `--all=false`. |
| `--certificate-authority` | The path to a certificate authority file to use when communicating with the OpenShift Container Platform-managed registries. Defaults to the certificate authority data from the current user’s configuration file. If provided, a secure connection is initiated. |
| `--confirm` | Indicate that pruning should occur, instead of performing a test-run. This requires a valid route to the integrated container image registry. If this command is run outside of the cluster network, the route must be provided using `--registry-url`. |
| `--force-insecure` | Use caution with this option. Allow an insecure connection to the container registry that is hosted via HTTP or has an invalid HTTPS certificate. |
| `--keep-tag-revisions=<N>` | For each imagestream, keep up to at most `N` image revisions per tag (default `3`). |
| `--keep-younger-than=<duration>` | Do not prune any image that is younger than `<duration>` relative to the current time. Alternately, do not prune any image that is referenced by any other object that is younger than `<duration>` relative to the current time (default `60m`). |
| `--prune-over-size-limit` | Prune each image that exceeds the smallest limit defined in the same project. This flag cannot be combined with `--keep-tag-revisions` nor `--keep-younger-than`. |
| `--registry-url` | The address to use when contacting the registry. The command attempts to use a cluster-internal URL determined from managed images and image streams. In case it fails (the registry cannot be resolved or reached), an alternative route that works needs to be provided using this flag. The registry hostname can be prefixed by `https://` or `http://`, which enforces particular connection protocol. |
| `--prune-registry` | In conjunction with the conditions stipulated by the other options, this option controls whether the data in the registry corresponding to the OpenShift Container Platform image API object is pruned. By default, image pruning processes both the image API objects and corresponding data in the registry.  This option is useful when you are only concerned with removing etcd content, to reduce the number of image objects but are not concerned with cleaning up registry storage, or if you intend to do that separately by hard pruning the registry during an appropriate maintenance window for the registry. |

Show more

Additional information about the `--prune-registry` flag
:   You can separate the removal of OpenShift Container Platform image API objects from the removal of image data in the registry by passing in the `--prune-registry=false` flag. For example, the following command prunes only the API objects, leaving the registry storage untouched:

    ```
    $ oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m --confirm --prune-registry=false
    ```

    Then, you can perform a hard prune of the registry to remove the associated image data. This approach can narrow the timing window for race conditions compared to pruning both in a single command.

    However, timing windows are not completely eliminated. For example, a pod might still be created that references an image while that image is being identified for pruning. You should track any API objects created during pruning to ensure that they do not reference deleted content.

    Re-running the pruning without the `--prune-registry` option, or with `--prune-registry=true`, does not remove the associated registry storage for images previously pruned with `--prune-registry=false`. Those images can only be removed from registry storage by performing a hard prune of the registry. For more information, see "Hard pruning the registry".

#### [13.6.7. Image pruning issues](#pruning-images-troubleshooting_pruning-objects) Copy linkLink copied to clipboard!

Identify the image pruning issues in your cluster to diagnose unpruned images, manage tag revision thresholds, and fix connection or certificate authority errors between the CLI client and registry.

Images not being pruned
:   If your images keep accumulating and the `prune` command removes just a small portion of what you expect, ensure that you understand the image prune conditions that must apply for an image to be considered a candidate for pruning.

    Ensure that images you want removed occur at higher positions in each tag history than your chosen tag revisions threshold. For example, consider an old and obsolete image named `sha256:abz`. By running the following command in your namespace, where the image is tagged, the image is tagged three times in a single image stream named `myapp`:

    ```
    $ oc get is -n <namespace> -o go-template='{{range $isi, $is := .items}}{{range $ti, $tag := $is.status.tags}}'\
    '{{range $ii, $item := $tag.items}}{{if eq $item.image "sha256:<hash>"}}{{$is.metadata.name}}:{{$tag.tag}} at position {{$ii}} out of {{len $tag.items}}\n'\
    '{{end}}{{end}}{{end}}{{end}}'
    ```

    **Example output**

    ```
    myapp:v2 at position 4 out of 5
    myapp:v2.1 at position 2 out of 2
    myapp:v2.1-may-2016 at position 0 out of 1
    ```

    When default options are used, the image is never pruned because it occurs at position `0` in a history of `myapp:v2.1-may-2016` tag. For an image to be considered for pruning, the administrator must either:

    * Specify `--keep-tag-revisions=0` with the `oc adm prune images` command.

      Warning

      This action removes all the tags from all the namespaces with underlying images, unless they are younger or they are referenced by objects younger than the specified threshold.
    * Delete all the `istags` where the position is below the revision threshold, which means `myapp:v2.1` and `myapp:v2.1-may-2016`.
    * Move the image further in the history, either by running new builds pushing to the same `istag`, or by tagging other image. This is not always desirable for old release tags.

      Tags having a date or time of a particular image’s build in their names should be avoided, unless the image must be preserved for an undefined amount of time. Such tags tend to have just one image in their history, which prevents them from ever being pruned.

Secure connection to an insecure registry
:   If you see a message similar to the following in the output of the `oc adm prune images` command, then your registry is not secured and the `oc adm prune images` client attempts to use a secure connection:

    ```
    error: error communicating with registry: Get https://172.30.30.30:5000/healthz: http: server gave HTTP response to HTTPS client
    ```

    * The recommended solution is to secure the registry. Otherwise, you can force the client to use an insecure connection by appending `--force-insecure` to the command; however, this is not recommended.

Insecure connection to a secured registry
:   If you see one of the following errors in the output of the `oc adm prune images` command, it means that your registry is secured using a certificate signed by a certificate authority other than the one used by `oc adm prune images` client for connection verification:

    ```
    error: error communicating with registry: Get http://172.30.30.30:5000/healthz: malformed HTTP response "\x15\x03\x01\x00\x02\x02"
    error: error communicating with registry: [Get https://172.30.30.30:5000/healthz: x509: certificate signed by unknown authority, Get http://172.30.30.30:5000/healthz: malformed HTTP response "\x15\x03\x01\x00\x02\x02"]
    ```

    By default, the certificate authority data stored in the user’s configuration files is used; the same is true for communication with the control plane API.

    Use the `--certificate-authority` option to provide the right certificate authority for the container image registry server.

Wrong certificate authority
:   The following error means that the certificate authority used to sign the certificate of the secured container image registry is different from the authority used by the client:

    ```
    error: error communicating with registry: Get https://172.30.30.30:5000/: x509: certificate signed by unknown authority
    ```

    Make sure to provide the right one with the flag `--certificate-authority`.

    As a workaround, the `--force-insecure` flag can be added instead. However, this is not recommended.

### [13.7. Hard pruning the registry](#pruning-hard-pruning-registry_pruning-objects) Copy linkLink copied to clipboard!

Hard prune the OpenShift image registry to remove orphaned image blobs that are not referenced in etcd and reclaim registry storage space when standard image pruning is insufficient.

The OpenShift image registry can accumulate blobs that are not referenced by the OpenShift Container Platform cluster’s etcd. The basic pruning images procedure, therefore, is unable to operate on them. These are called *orphaned blobs*.

Orphaned blobs can occur from the following scenarios:

* Manually deleting an image with `oc delete image <sha256:image-id>` command, which only removes the image from etcd, but not from the registry’s storage.
* Pushing to the registry initiated by daemon failures, which causes some blobs to get uploaded, but the image manifest (which is uploaded as the very last component) does not. All unique image blobs become orphans.
* OpenShift Container Platform refusing an image because of quota restrictions.
* The standard image pruner deleting an image manifest, but is interrupted before it deletes the related blobs.
* A bug in the registry pruner, which fails to remove the intended blobs, causing the image objects referencing them to be removed and the blobs becoming orphans.

*Hard pruning* the registry, a separate procedure from basic image pruning, allows cluster administrators to remove orphaned blobs. You should hard prune if you are running out of storage space in your OpenShift image registry and believe you have orphaned blobs.

This should be an infrequent operation and is necessary only when you have evidence that significant numbers of new orphans have been created. Otherwise, you can perform standard image pruning at regular intervals, for example, once a day (depending on the number of images being created).

**Procedure**

1. Log in.

   Log in to the cluster with the CLI as `kubeadmin` or another privileged user that has access to the `openshift-image-registry` namespace.
2. Run a basic image prune.

   Basic image pruning removes additional images that are no longer needed. The hard prune does not remove images on its own. It only removes blobs stored in the registry storage. Therefore, you should run this just before the hard prune.
3. Switch the registry to read-only mode.

   If the registry is not running in read-only mode, any pushes happening at the same time as the prune will either:

   * fail and cause new orphans, or
   * succeed although the images cannot be pulled (because some of the referenced blobs were deleted).

   Pushes will not succeed until the registry is switched back to read-write mode. Therefore, the hard prune must be carefully scheduled.

   To switch the registry to read-only mode:

   1. In `configs.imageregistry.operator.openshift.io/cluster`, set `spec.readOnly` to `true`:

      ```
      $ oc patch configs.imageregistry.operator.openshift.io/cluster -p '{"spec":{"readOnly":true}}' --type=merge
      ```
4. **Add the `system:image-pruner` role.**

   The service account used to run the registry instances requires additional permissions to list some resources.

   1. Get the service account name:

      ```
      $ service_account=$(oc get -n openshift-image-registry \
          -o jsonpath='{.spec.template.spec.serviceAccountName}' deploy/image-registry)
      ```
   2. Add the `system:image-pruner` cluster role to the service account:

      ```
      $ oc adm policy add-cluster-role-to-user \
          system:image-pruner -z \
          ${service_account} -n openshift-image-registry
      ```
5. **Optional: Run the pruner in dry-run mode.**

   To see how many blobs would be removed, run the hard pruner in dry-run mode. No changes are actually made. The following example references an image registry pod called `image-registry-3-vhndw`:

   ```
   $ oc -n openshift-image-registry exec pod/image-registry-3-vhndw -- /bin/sh -c '/usr/bin/dockerregistry -prune=check'
   ```

   Alternatively, to get the exact paths for the prune candidates, increase the logging level:

   ```
   $ oc -n openshift-image-registry exec pod/image-registry-3-vhndw -- /bin/sh -c 'REGISTRY_LOG_LEVEL=info /usr/bin/dockerregistry -prune=check'
   ```

   **Example output**

   ```
   time="2017-06-22T11:50:25.066156047Z" level=info msg="start prune (dry-run mode)" distribution_version="v2.4.1+unknown" kubernetes_version=v1.6.1+$Format:%h$ openshift_version=unknown
   time="2017-06-22T11:50:25.092257421Z" level=info msg="Would delete blob: sha256:00043a2a5e384f6b59ab17e2c3d3a3d0a7de01b2cabeb606243e468acc663fa5" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
   time="2017-06-22T11:50:25.092395621Z" level=info msg="Would delete blob: sha256:0022d49612807cb348cabc562c072ef34d756adfe0100a61952cbcb87ee6578a" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
   time="2017-06-22T11:50:25.092492183Z" level=info msg="Would delete blob: sha256:0029dd4228961086707e53b881e25eba0564fa80033fbbb2e27847a28d16a37c" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
   time="2017-06-22T11:50:26.673946639Z" level=info msg="Would delete blob: sha256:ff7664dfc213d6cc60fd5c5f5bb00a7bf4a687e18e1df12d349a1d07b2cf7663" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
   time="2017-06-22T11:50:26.674024531Z" level=info msg="Would delete blob: sha256:ff7a933178ccd931f4b5f40f9f19a65be5eeeec207e4fad2a5bafd28afbef57e" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
   time="2017-06-22T11:50:26.674675469Z" level=info msg="Would delete blob: sha256:ff9b8956794b426cc80bb49a604a0b24a1553aae96b930c6919a6675db3d5e06" go.version=go1.7.5 instance.id=b097121c-a864-4e0c-ad6c-cc25f8fdf5a6
   ...
   Would delete 13374 blobs
   Would free up 2.835 GiB of disk space
   Use -prune=delete to actually delete the data
   ```
6. Run the hard prune.

   Execute the following command inside one running instance of a `image-registry` pod to run the hard prune. The following example references an image registry pod called `image-registry-3-vhndw`:

   ```
   $ oc -n openshift-image-registry exec pod/image-registry-3-vhndw -- /bin/sh -c '/usr/bin/dockerregistry -prune=delete'
   ```

   **Example output**

   ```
   Deleted 13374 blobs
   Freed up 2.835 GiB of disk space
   ```
7. Switch the registry back to read-write mode.

   After the prune is finished, the registry can be switched back to read-write mode. In `configs.imageregistry.operator.openshift.io/cluster`, set `spec.readOnly` to `false`:

   ```
   $ oc patch configs.imageregistry.operator.openshift.io/cluster -p '{"spec":{"readOnly":false}}' --type=merge
   ```

### [13.8. Pruning cron jobs](#pruning-cronjobs_pruning-objects) Copy linkLink copied to clipboard!

Clean up completed and failed Kubernetes jobs manually to prevent resource exhaustion. You can restrict cron job access to authorized users and configure resource quotas to control job and pod creation.

Cron jobs can perform pruning of successful jobs, but might not properly handle failed jobs. Therefore, the cluster administrator should perform regular cleanup of jobs manually. They should also restrict the access to cron jobs to a small group of trusted users and set appropriate quota to prevent the cron job from creating too many jobs and pods.

## [Chapter 14. Reducing resource consumption with application idling](#idling-applications) Copy linkLink copied to clipboard!

As an administrator, you can reduce cluster resource consumption and lower public cloud costs by temporarily scaling inactive application resources to zero replicas.

If any scalable resources are not in use, OpenShift Container Platform discovers and idles them by scaling their replicas to `0`. The next time network traffic is directed to the resources, the resources are unidled by scaling up the replicas, and normal operation continues.

Applications are made of services, as well as other scalable resources, such as deployment configs. The action of idling an application involves idling all associated resources.

### [14.1. Application idling](#idle-idling-applications_idling-applications) Copy linkLink copied to clipboard!

Identify the scalable resources for one or more services, such as deployment configurations and replication controllers, and scale them down to zero replicas to optimize cluster capacity.

You can use the `oc idle` command to idle a single service, or use the `--resource-names-file` option to idle multiple services.

#### [14.1.1. Idling a single service](#idle-idling-applications-single_idling-applications) Copy linkLink copied to clipboard!

Scale down the scalable resources of a specific service to zero replicas to reduce cluster consumption.

**Procedure**

1. To idle a single service, run:

   ```
   $ oc idle <service>
   ```

#### [14.1.2. Idling multiple services](#idle-idling-applications-multiple_idling-applications) Copy linkLink copied to clipboard!

Scale multiple inactive services down to zero replicas to optimize cluster capacity.

Idling multiple services is helpful if an application spans across a set of services within a project, or when idling multiple services in conjunction with a script to idle multiple applications in bulk within the same project.

**Procedure**

1. Create a file containing a list of the services, each on their own line.
2. Idle the services using the `--resource-names-file` option:

   ```
   $ oc idle --resource-names-file <filename>
   ```

   Note

   The `idle` command is limited to a single project. For idling applications across a cluster, run the `idle` command for each project individually.

### [14.2. Unidling applications](#idle-unidling-applications_idling-applications) Copy linkLink copied to clipboard!

Restore normal application operations by scaling up the replicas when network traffic is directed back to the idled resources.

Application services become active again when they receive network traffic and are scaled back up to their previous state. This includes both traffic to the services and traffic passing through routes. Applications can also be manually unidled by scaling up the resources.

**Procedure**

* To scale up a DeploymentConfig, run:

  ```
  $ oc scale --replicas=1 dc <dc_name>
  ```

  Note

  Automatic unidling by a router is currently only supported by the default HAProxy router.

## [Chapter 15. Deleting applications](#odc-deleting-applications) Copy linkLink copied to clipboard!

You can delete applications created in your project.

### [15.1. Deleting applications using the Developer perspective](#odc-deleting-applications-using-developer-perspective_odc-deleting-applications) Copy linkLink copied to clipboard!

You can delete an application and all of its associated components using the **Topology** view in the **Developer** perspective:

1. Click the application you want to delete to see the side panel with the resource details of the application.
2. Click the **Actions** drop-down menu displayed on the upper right of the panel, and select **Delete Application** to see a confirmation dialog box.
3. Enter the name of the application and click **Delete** to delete it.

You can also right-click the application you want to delete and click **Delete Application** to delete it.

## [Legal Notice](#idm139966756849552) Copy linkLink copied to clipboard!

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
