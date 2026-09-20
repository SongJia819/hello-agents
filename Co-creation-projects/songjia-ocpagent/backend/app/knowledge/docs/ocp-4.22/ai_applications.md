---
title: "AI applications"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ai_applications/index
retrieved_at: 2026-09-05T05:41:31.342970+00:00
---

# AI applications

---

OpenShift Container Platform 4.22

## Using AI applications on OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140358603826112)

**Abstract**

This document provides information about using an MCP server on an OpenShift Container Platform cluster.

---

## [Chapter 1. MCP server](#mcp-server) Copy linkLink copied to clipboard!

### [1.1. Inspect clusters with MCP server for Red Hat OpenShift](#mcp-server-overview) Copy linkLink copied to clipboard!

When problems occur on your OpenShift Container Platform cluster, you want to determine exactly what is happening, so that you can fix the issue as soon as possible. The MCP server for Red Hat OpenShift feature provides an AI tool to quickly and easily diagnose your OpenShift Container Platform cluster.

Important

MCP server for Red Hat OpenShift is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [1.1.1. AI safety](#ai-app-mcp-server-ai-safety_mcp-server-overview) Copy linkLink copied to clipboard!

Because MCP server for Red Hat OpenShift grants AI agents access to cluster resources, you must follow safety practices to protect your cluster from unauthorized actions, data exposure, and prompt injection risks.

Important

This feature uses AI technology. Do not include any personal information or other sensitive information in your input. Interactions may be used to improve Red Hat’s products or services. Always review AI-generated content before using it.

##### [1.1.1.1. Data ownership](#ai-app-mcp-server-ai-safety-data-ownership_mcp-server-overview) Copy linkLink copied to clipboard!

The MCP server for Red Hat OpenShift does not store any information or state of the cluster. If you opt in, there are several telemetry metrics that are collected to understand the overall usage levels of the MCP server for Red Hat OpenShift:

* Cluster:k8s\_mcp\_tool\_calls:sum:
* Total count of all Model Context Protocol (MCP) tool invocations across the cluster
* Cluster:k8s\_mcp\_tool\_errors:sum:
* Total count of all failed MCP tool invocations across the cluster
* Cluster:k8s\_mcp\_http\_requests:sum:
* Total count of all HTTP requests received by the MCP server

These metrics do not collect specific details of the calls, requests, or errors themselves; they only provide aggregate overall sums of the usage.

To opt in, edit TOML config:

```
[telemetry]
enabled = true
```

To opt out, edit TOML config:

```
[telemetry]
enabled = false
```

##### [1.1.1.2. Required verification workflow: Human in the loop (HITL) enforcement](#ai-app-mcp-server-ai-safety-hitl_mcp-server-overview) Copy linkLink copied to clipboard!

* It is recommended that you assess the AI agent’s proposed action in the MCP client.
* You should manually check suggested resource versions (for example, ensure the model is not suggesting deprecated APIs).
* It is recommended that you use a human approval mechanism in the AI client interface for "write" actions.

##### [1.1.1.3. Data privacy and redaction](#ai-app-mcp-server-ai-safety-privacy-redaction_mcp-server-overview) Copy linkLink copied to clipboard!

The MCP server for Red Hat OpenShift has no internal mechanisms for PII and data redaction. To ensure that cluster information within allowed Custom Resources (CRs) complies with data privacy standards, deploy TrustyAI to monitor and sanitize outgoing payloads. For how to scope and limit MCP access to specific CRs, see "Revoke access to Custom Resources".

##### [1.1.1.4. Audit trail recommendation](#ai-app-mcp-server-ai-safety-audit-trail_mcp-server-overview) Copy linkLink copied to clipboard!

The MCP server for Red Hat OpenShift is configured to append a user-agent string in audit logs to identify that requests were made by an AI agent through the MCP server. Ensure that authorization is enabled via OAuth or MCP gateway. For more information, see "Install MCP server for Red Hat OpenShift".

##### [1.1.1.5. Recommendations regarding 3rd-party MCP servers](#ai-app-mcp-server-ai-safety-mcp-servers-hitl_mcp-server-overview) Copy linkLink copied to clipboard!

For better security and control, it is recommended that third-party MCP hosts implement a HITL requirement to approve any "write" operations performed via the MCP server for Red Hat OpenShift.

##### [1.1.1.6. AI governance and guardrails](#ai-app-mcp-server-ai-safety-governance-guardrails_mcp-server-overview) Copy linkLink copied to clipboard!

MCP gateway acts as a centralized control point and enforces strict governance over agent-tool interactions through centralized authentication and identity management, using correctly scoped tokens and OAuth 2.0 to ensure agents only possess the specific permissions required for any given task. The MCP gateway further secures the environment using identity-based tool filtering, which removes unauthorized tools from the tools/list discovery process entirely, thus preventing agents from attempting to access forbidden capabilities.

To mitigate AI-specific risks, the gateway should be deployed with safety guardrails. Guardrails would include inspecting traffic payloads for prompt injections and safety violations by integrating with external engines like Trusty AI or NVIDIA Nemo. Additionally, the MCP gateway ensures operational stability and accountability by implementing rate limiting to prevent agent-driven denial-of-service attacks and providing comprehensive audit logging to track and analyze all tool usage.

##### [1.1.1.7. Emergency removal of AI agent access](#ai-app-mcp-server-ai-safety-governance-removal_mcp-server-overview) Copy linkLink copied to clipboard!

In an emergency, you can use any of the following possible actions to revoke access for the AI agent (via the MCP server):

* **Remove access to the offending tool** in `config.toml`.

  Only enable specific tools:

  ```
  enabled_tools = ["pods_list", "pods_get", "pods_log"]
  ```
* **Disable specific tools** from enabled toolsets.

  Disable destructive tool calls in `config.toml`.

  ```
  disabled_tools = ["resources_delete", "pods_delete"].
  ```
* **Create a production-safe configuration**.

  ```
  read_only = true
  ```
* **Allow writes, but prevent deletions**.

  ```
  disable_destructive = true
  ```
* **Uninstall the MCP server completely** by running the following command:

  ```
  $ helm uninstall openshift-mcp-server
  ```
* **RBAC revocation**:

  Remove the user’s rolebinding or clusterrolebinding. For more information, see "Install MCP server for Red Hat OpenShift".
* **Remove access through the MCP gateway**

  To remove access through the gateway, you can delete the MCPServerRegistration CR by running the following command:

  ```
  $ oc delete mcpsr <name of registration>
  ```

#### [1.1.2. Model Context Protocol overview](#ai-app-mcp-server-model-context-protocol-overview_mcp-server-overview) Copy linkLink copied to clipboard!

Model Context Protocol (MCP) is an open source standard that enables AI applications to securely connect to external data sources, tools, and workflows without custom integrations.

MCP is an open source standard for connecting AI applications to external systems.

Using MCP, AI applications, such as Claude Code or Cursor, can connect to the following items, enabling them to access key information and perform tasks:

* **Data sources**: for example, local files, databases
* **Tools**: for example, search engines, calculators
* **Workflows**: for example, specialized prompts

MCP works similarly to a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

#### [1.1.3. MCP server overview](#ai-app-mcp-server-mcp-server-overview_mcp-server-overview) Copy linkLink copied to clipboard!

A Model Context Protocol (MCP) server exposes cluster data and operations to AI models in a structured, secure way, so that AI agents can diagnose and act on your cluster without needing direct access to APIs or databases.

##### [1.1.3.1. The Goals of an MCP server](#ai-app-mcp-server-mcp-server-overview-goals_mcp-server-overview) Copy linkLink copied to clipboard!

The primary goal of an MCP server is to expose specific capabilities to an AI model in a structured, safe, and predictable way. Here are the key objectives an MCP server achieves:

* **Capability exposure**: The server defines exactly what the AI is allowed to do or see. It does this by exposing three specific things:

  + **Tools**: Executable functions that do things (for example, "Delete this file," "Post to Slack," or "Calculate mortgage").
  + **Resources**: Read-only data sources that provide context (for example, "Read the contents of README.md" or "Fetch the logs from the last hour").
  + **Prompts**: Predefined templates that guide the AI model’s behavior (for example, a "Code Reviewer" prompt that tells the AI exactly how to look for bugs in a specific language).
* **Abstraction of complexity**: An MCP server hides the complicated parts of an integration. The LLM does not need to know how to write a SQL query or use a specific GitHub API. The server handles the code, the formatting, and the technical unique complexities, giving the LLM a clean, standardized result.
* **Execution and action**: Unlike the MCP gateway, which just routes traffic, the server is where the logic lives. When an AI decides to use a tool, the MCP server is the component that actually executes using that tool. For example, runs a Python script, queries a database, or calls an external API.
* **Sandboxing and security**: The server provides a layer of isolation. By running as a separate process, it can be restricted to only accessing specific folders or specific API endpoints. If the AI model attempts to undesired or unintended action, for example, tries to delete your entire hard drive, the server can deny the behavior based on its internal rules.

#### [1.1.4. MCP gateway overview](#ai-app-mcp-server-mcp-gateway-overview_mcp-server-overview) Copy linkLink copied to clipboard!

The primary goal of a Model Context Protocol (MCP) gateway is to standardize and simplify how AI models interact with external data and tools. Without a gateway, an AI model would need a custom integration for every single database, API, or local file system it needs to access.

##### [1.1.4.1. Aggregation and orchestration](#ai-app-mcp-server-mcp-gateway-overview-agg-orch_mcp-server-overview) Copy linkLink copied to clipboard!

A gateway connects to multiple MCP servers simultaneously. Instead of the LLM (Large Language Model) managing ten different connections, it communicates only with the gateway. The gateway then routes the LLM’s request to the specific server that holds the relevant information (for example, fetching Jira tickets from one server and Google Drive docs from another).

##### [1.1.4.2. Security and access control](#ai-app-mcp-server-mcp-gateway-overview-security-access_mcp-server-overview) Copy linkLink copied to clipboard!

The gateway acts as a security perimeter.

It manages:

* **Authentication**: Holding the API keys or tokens required for various servers.
* **Permissions**: Ensuring the AI model only accesses the specific data or tools that the user authorized.
* **Privacy**: Stripping sensitive information before it is sent back to the model provider.

##### [1.1.4.3. Protocol translation](#ai-app-mcp-server-mcp-gateway-overview-protocol_mcp-server-overview) Copy linkLink copied to clipboard!

The gateway ensures that the communication between the AI model and the servers follows the MCP standard. It translates the high-level "intent" of the AI model into the specific JSON-RPC calls that the MCP servers understand.

##### [1.1.4.4. Scalability](#ai-app-mcp-server-mcp-gateway-overview-scale_mcp-server-overview) Copy linkLink copied to clipboard!

By decoupling the AI model from the data sources, you can add, remove, or update MCP servers without ever needing to change the core configuration of your AI application.

#### [1.1.5. MCP server for Red Hat OpenShift Prompting workflow](#ai-app-mcp-server-model-context-prompting-workflow_mcp-server-overview) Copy linkLink copied to clipboard!

By understanding the Model Context Protocol (MCP) prompting workflow you can better troubleshoot issues and optimize how your prompts reach cluster resources through the MCP server, gateway, and a Large Language Model (LLM).

When you prompt an LLM, the execution happens according to the following steps:

1. User types a prompt: "Are there any pods that keep restarting?".
2. MCP Host (for example, Claude Desktop): receives your prompt. It looks at its connected MCP servers and sees one has a tool called pods\_list.
3. MCP gateway (If used): If you are in an enterprise environment, the Host talks to the gateway first. The gateway checks "Is this user allowed to access the cluster?" and "Is the cluster currently online?"
4. MCP server: The gateway (or Host) sends the command to the server. The server runs the actual code (the API call to OpenShift), gets the data, and sends it back.
5. LLM: Receives that raw data, "reads" it, and gives you the final summary.

#### [1.1.6. Install MCP server for Red Hat OpenShift](#ai-mcp-server-install_mcp-server-overview) Copy linkLink copied to clipboard!

Install and configure the MCP server for Red Hat OpenShift to enable AI agents to securely diagnose and inspect your cluster.

To install the MCP server for Red Hat OpenShift feature, complete the following procedures.

**Prerequisites**

* Access to OpenShift console with admin rights.
* Installed MCP-compatible client, such as Claude Code, Visual Studio Code (VS Code), Cursor, or OpenShift LightSpeed (OLS).

**Procedure**

1. Install the MCP server for Red Hat OpenShift Helm chart.
2. Connect a compatible with Model Context Protocol (MCP) client, such as Claude Code, to the MCP server.
3. Install the MCP gateway.
4. Verify the MCP gateway deployment.
5. Configure the MCP gateway.
6. Configure RBAC enforcement.
7. Revoke access to Custom Resources.
8. Set up the MCP gateway authentication.
9. Set up MCP gateway authorization.

##### [1.1.6.1. Install the MCP server Helm chart](#ai-app-mcp-server-install-helm_mcp-server-overview) Copy linkLink copied to clipboard!

Install the Model Context Protocol (MCP) server Helm chart to deploy the MCP server for Red Hat OpenShift on your cluster, enabling AI agents to diagnose and inspect cluster resources.

**Prerequisites**

* Access to OpenShift console with admin rights.

**Procedure**

1. Install the MCP server for Red Hat OpenShift Helm chart by running one of the following commands:

   * For read-only access (recommended for most use cases):

     ```
     $ helm upgrade -i -n openshift-mcp-server --create-namespace openshift-mcp-server \
         openshift-helm-charts/redhat-openshift-mcp-server \
         --set config.toolsets=<toolset-names> \
         --set ingress.host=<hostname> \
         --set openshift=true \
         --set-json 'rbac.extraClusterRoleBindings=[{"name":"use-view-role","roleRef":{"name":"view","external":true}}]'
     ```
   * For full cluster access:

     ```
     $ helm upgrade -i -n openshift-mcp-server --create-namespace openshift-mcp-server \
         openshift-helm-charts/redhat-openshift-mcp-server \
         --set config.toolsets=<toolset-names> \
         --set ingress.host=<hostname> \
         --set openshift=true \
         --set-json 'rbac.extraClusterRoleBindings=[{"name":"admin-access","roleRef":{"name":"cluster-admin","external":true}}]'
     ```
   * `<hostname>` is a fully qualified domain name (FQDN) that serves as the entry point for the MCP server for Red Hat OpenShift. This host address is used by the Ingress controller to route external traffic to the MCP server service. This should be a URL such as `mcp-server.apps.cluster-name.domain.com`.
   * `<toolset-names>` can include toolsets from the following table.

     Expand

     Table 1.1. Available toolsets

     | Toolset | Description | Default | Status |
     | --- | --- | --- | --- |
     | `core` | Most common tools for Kubernetes management (Pods, Generic Resources, Events, etc.) | Yes | Technology Preview |
     | `config` | View and manage the current local Kubernetes configuration (kubeconfig) | Yes | Technology Preview |
     | `netedge` | NetEdge troubleshooting tools for OpenShift Container Platform | No | Technology Preview |
     | `helm` | Tools for managing Helm charts and releases | No | Technology Preview |
     | `metrics` | Toolset for querying Prometheus and Alertmanager endpoints in efficient ways | No | Technology Preview |
     | `ossm` | Most common tools for managing OSSM | No | Technology Preview |
     | `kubevirt` | KubeVirt virtual machine management tools | No | Developer Preview |
     | `tekton` | Tekton pipeline management tools for Pipelines, PipelineRuns, Tasks, and TaskRuns | No | Developer Preview |

     Show more

**Verification**

* Check that the command returns output similar to the following:

  **Example output**

  ```
  Release "openshift-mcp-server" does not exist. Installing it now.
  NAME: openshift-mcp-server
  LAST DEPLOYED: Mon Apr 20 09:28:13 2026
  NAMESPACE: openshift-mcp-server
  STATUS: deployed
  REVISION: 1
  TEST SUITE: None
  ```

##### [1.1.6.2. Connect a client to the MCP server](#ai-app-mcp-server-connect-client_mcp-server-overview) Copy linkLink copied to clipboard!

Connect a client that is compatible with the Model Context Protocol (MCP) to the MCP server so that an AI agent can interact with your cluster.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.

**Procedure**

1. Add the following lines to your client configuration file:

   * For Claude Desktop: `claude_desktop_config.json` file
   * For Claude Code (CLI): `.mcp.json` file

     ```
     {
       "mcpServers": {
         "openshift": {
           "type": "http",
           "url": "<url of the route created in the Helm chart>/mcp"
         }
       }
     }
     ```

     `<url of the route created in the Helm chart>` is the hostname you configured during Helm installation.
2. Accept the CA certificate when prompted by the client.

##### [1.1.6.3. Install the MCP gateway](#ai-app-mcp-server-install-gateway_mcp-server-overview) Copy linkLink copied to clipboard!

Install the Model Context Protocol (MCP) gateway to provide a secure, centralized entry point that enforces authentication, authorization, and rate limiting for all MCP server traffic.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.

**Procedure**

1. Install the MCP gateway.

   For information about how to install the MCP gateway, see "Install the MCP gateway (Red Hat Connectivity Link)".

   After installation, the controller automatically creates the HTTPRoute for gateway access. The MCP gateway acts as a reverse proxy that aggregates multiple MCP servers into a single endpoint and provides a layer for authentication and rate limiting.

##### [1.1.6.4. Verify the MCP gateway deployment](#ai-app-mcp-server-verify-deployment_mcp-server-overview) Copy linkLink copied to clipboard!

Verify that the Model Context Protocol (MCP) gateway is deployed and running correctly before configuring routing, authentication, and authorization.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed.

**Procedure**

1. Check the status of your deployment by running the following command:

   ```
   $ oc get pods -n mcp-system -l "app.kubernetes.io/instance=mcp-gateway"
   ```

   Note

   This example uses the namespace "mcp-system" for installing the gateway. If you install the gateway in a different namespace than "mcp-system", use that namespace instead throughout the procedure.

   **Example**

   ```
   NAME                                      READY   STATUS    RESTARTS   AGE
   mcp-gateway-controller-594b9649cf-zstfw   1/1     Running   0          22s
   ```
2. Ensure that the MCP gateway Extension exists by running the following command:

   ```
   $ oc get mcpgatewayextension -A
   ```

   **Example**

   ```
   NAMESPACE   NAME          READY   AGE
   mcp-system  mcp-gateway           105s
   ```
3. Verify the broker-router deployment by running the following command:

   ```
   $ oc logs -n mcp-system deployment/mcp-gateway-broker-router
   ```
4. Verify EnvoyFilter was created in the gateway namespace by running the following command:

   ```
   $ oc get envoyfilter -n mcp-system -l app.kubernetes.io/managed-by=mcp-gateway-controller
   ```

##### [1.1.6.5. Configure the MCP gateway](#ai-app-mcp-server-configure-gateway_mcp-server-overview) Copy linkLink copied to clipboard!

Configure the Model Context Protocol (MCP) gateway so that it can route client traffic to your MCP server and discover the tools the server exposes.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.

**Procedure**

1. Create the HTTPRoute for the MCP server by running the following command:

   ```
   $ oc apply -f - <<EOF
   apiVersion: gateway.networking.k8s.io/v1
   kind: HTTPRoute
   metadata:
     name: mcp-api-key-server-route
     namespace: openshift-mcp-server
   spec:
     parentRefs:
     - group: gateway.networking.k8s.io
       kind: Gateway
       name: mcp-gateway
       namespace: gateway-system
       sectionName: mcp
     hostnames:
     - ${MCP_SERVER_HOST}
     rules:
     - matches:
       - path:
           type: PathPrefix
           value: /mcp
       backendRefs:
       - name: openshift-mcp-server
         port: 8080
   EOF
   ```

   `${MCP_SERVER_HOST}` is the hostname you configured during Helm installation.

   This HTTPRoute enables the MCP gateway to route traffic to your MCP server instance and is referenced in the MCPServerRegistration resource.
2. Create an MCP server Registration Resource by running the following command:

   ```
   $ oc apply -f - <<EOF
   apiVersion: mcp.kuadrant.io/v1alpha1
   kind: MCPServerRegistration
   metadata:
     name: my-mcp-server-reg
     namespace: openshift-mcp-server
   spec:
     toolPrefix: "openshift_"
     targetRef:
       group: "gateway.networking.k8s.io"
       kind: "HTTPRoute"
       name: "mcp-api-key-server-route"
       namespace: openshift-mcp-server
   EOF
   ```

   * `metadata.name`: Provide a name for the MCP server registration object.
   * `metadata.namespace`: The namespace for the MCP server, which is `openshift-mcp-server`.
   * `spec.targetRef.name`: The name of your MCP server HTTPRoute. You can find this by running the command: `oc get httproute -n openshift-mcp-server`.
   * `spec.targetRef.namespace`: The namespace for the MCP server HTTPRoute, which is `openshift-mcp-server`.
3. Verify the registration status by running the following commands:

   ```
   $ oc wait --for=condition=Ready mcpsr/my-mcp-server-reg -n openshift-mcp-server --timeout=120s
   $ oc get mcpsr -A
   ```

   **Example output**

   ```
   NAMESPACE             NAME                PREFIX      TARGET                     PATH   READY   TOOLS   CREDENTIALS   AGE
   openshift-mcp-server  my-mcp-server-reg   myserver_   mcp-api-key-server-route   /mcp   True    4                     30s
   ```

   The **READY** column should display `True` and the **TOOLS** column should show the number of tools discovered.

   If the status is not ready, check the MCP server Registration conditions for details by running the following command:

   ```
   $ oc describe mcpsr my-mcp-server-reg -n openshift-mcp-server
   ```
4. Check the controller logs by running the following command:

   ```
   $ oc logs -n mcp-system deployment/mcp-gateway-controller
   ```
5. Check the broker logs for tool discovery by running the following command:

   ```
   $ oc logs -n mcp-system deployment/mcp-gateway-broker-router
   ```
6. Verify that your MCP server tools are available through the MCP gateway:

   1. Initialize the MCP session and capture session ID by using -D to dump headers to a file, and then reading the session ID by running the following command:

      ```
      $ curl -s -D /tmp/mcp_headers -X POST http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/mcp  \
        -H "Content-Type: application/json" \
        -d '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}'
      ```

      `<cluster-name>.<domain-name>` is the name and domain of your cluster.
   2. Extract the MCP session ID from response headers by running the following commands:

      ```
      $ SESSION_ID=$(grep -i "mcp-session-id:" /tmp/mcp_headers | cut -d' ' -f2 | tr -d '\r')

      $ echo "MCP Session ID: $SESSION_ID"
      ```
   3. List tools by using the session ID in the following command:

      ```
      $ curl -X POST http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/mcp \
        -H "Content-Type: application/json" \
        -H "mcp-session-id: $SESSION_ID" \
        -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'
      ```

      `<cluster-name>.<domain-name>` is the name and domain of your cluster.
   4. Clean up by running the following command:

      ```
      $ rm -f /tmp/mcp_headers
      ```

      You should now see your MCP server tools in the response, prefixed with your configured toolPrefix (for example, myserver\_).

##### [1.1.6.6. Configure RBAC enforcement](#ai-app-mcp-server-configure-rbac_mcp-server-overview) Copy linkLink copied to clipboard!

To control which cluster resources the Model Context Protocol (MCP) server can access, configure role-based access control (RBAC) so that AI agents are limited to only the resources they need.

By default, RBAC is enabled, and you can extend the ClusterRoles, ClusterRoleBindings, Roles, and Rolebindings.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* The MCP gateway is configured.

**Procedure**

1. Configure RBAC enforcement by extending ClusterRoles, ClusterRoleBindings, Roles, and Rolebindings.

   Use the following example RBAC YAML file to extend ClusterRoles, ClusterRoleBindings, Roles, and Rolebindings:

   **Example RBAC settings YAML file**

   ```
   extraClusterRoles:
     - name: acm-managed-clusters
       rules:
         # Required for discovering and watching managed clusters
         - apiGroups: ["cluster.open-cluster-management.io"]
           resources: ["managedclusters"]
           verbs: ["list", "watch"]

   # -- ClusterRoleBinding for the ACM managed clusters role
   extraClusterRoleBindings:
     - name: acm-managed-clusters
       roleRef:
         name: acm-managed-clusters

   # -- Role for accessing cluster-proxy-addon service in multicluster-engine namespace
   extraRoles:
     - name: acm-cluster-proxy-discovery
       namespace: multicluster-engine
       rules:
         # Required for auto-discovering cluster-proxy-addon service
         - apiGroups: [""]
           resources: ["services"]
           verbs: ["get"]

   # -- RoleBinding for the cluster-proxy-discovery role
   extraRoleBindings:
     - name: acm-cluster-proxy-discovery
       namespace: multicluster-engine
       roleRef:
         name: acm-cluster-proxy-discovery
   ```
2. Apply the RBAC configuration by saving the preceding example to a file (for example, `rbac-values.yaml`), and then run the following command:

   ```
   $ helm upgrade openshift-mcp-server openshift-helm-charts/redhat-openshift-mcp-server \
       -n openshift-mcp-server \
       -f rbac-values.yaml
   ```

##### [1.1.6.7. Revoke access to Custom Resources](#ai-app-mcp-server-revoke-cr-access_mcp-server-overview) Copy linkLink copied to clipboard!

To prevent AI agents from reading or exposing confidential cluster data, you can revoke Model Context Protocol (MCP) server access to sensitive Custom Resources (CRs), such as Secrets and ConfigMaps, .

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* The MCP gateway is configured.
* RBAC is configured.

**Procedure**

1. Configure denied resources to limit access to sensitive CRs.

   Use the following example file to revoke access to Secrets, ConfigMaps, and RBAC resources:

   **Example**

   ```
   # Deny access to Secrets
   [[denied_resources]]
   group = ""
   version = "v1"
   kind = "Secret"

   # Deny access to ConfigMaps
   [[denied_resources]]
   group = ""
   version = "v1"
   kind = "ConfigMap"

   # Deny access to RBAC resources for additional security
   [[denied_resources]]
   group = "rbac.authorization.k8s.io"
   version = "v1"
   kind = "Role"

   [[denied_resources]]
   group = "rbac.authorization.k8s.io"
   version = "v1"
   kind = "RoleBinding"

   [[denied_resources]]
   group = "rbac.authorization.k8s.io"
   version = "v1"
   kind = "ClusterRole"

   [[denied_resources]]
   group = "rbac.authorization.k8s.io"
   version = "v1"
   kind = "ClusterRoleBinding"
   ```
2. Apply this configuration by doing one of the following:

   * Save the configuration to a file (for example, `deny-resources.toml`) and pass it using a Helm values file:

     ```
     $ helm upgrade openshift-mcp-server openshift-helm-charts/redhat-openshift-mcp-server \
         -n openshift-mcp-server \
         --set-file config.deniedResources=deny-resources.toml
     ```
   * Or use `--set-json` to pass the configuration inline:

     ```
     $ helm upgrade openshift-mcp-server openshift-helm-charts/redhat-openshift-mcp-server \
         -n openshift-mcp-server \
         --set-json 'config.deniedResources=[{"group":"","version":"v1","kind":"Secret"},{"group":"","version":"v1","kind":"ConfigMap"}]'
     ```

##### [1.1.6.8. Set up MCP gateway authentication](#ai-app-mcp-server-setup-authentication_mcp-server-overview) Copy linkLink copied to clipboard!

To ensure that only verified users can access MCP server for Red Hat OpenShift tools and cluster resources, set up OAuth-based authentication for the Model Context Protocol (MCP) gateway.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* RBAC is configured.
* You have revoked access to specific Custom Resources (CRs) as needed.
* You have access to an Identity Provider (Entra ID).

**Procedure**

1. Configure OAuth metadata discovery by setting environment variables on the MCP gateway broker-router deployment by running the following command:

   ```
   $ oc set env deployment/mcp-gateway-broker-router -n mcp-system\
   OAUTH_RESOURCE_NAME="MCP Server" \
   OAUTH_RESOURCE="http://mcp.127-0-0-1.sslip.io:8001/mcp" \
   OAUTH_AUTHORIZATION_SERVERS="https://login.microsoftonline.com/<tenant-id>/v2.0" \
   OAUTH_BEARER_METHODS_SUPPORTED="header" \
   OAUTH_SCOPES_SUPPORTED="openid,mcp-server,offline_access"
   ```

   These environment variables enable the OAuth 2.0 Protected Resource Metadata endpoint that clients use for authentication discovery.
2. Create the HTTPRoute for OAuth discovery by running the following command:

   ```
   $ oc apply -f - <<EOF
   apiVersion: gateway.networking.k8s.io/v1
   kind: HTTPRoute
   metadata:
     name: mcp-gateway-oauth-metadata
     namespace: mcp-system
   spec:
     parentRefs:
     - group: gateway.networking.k8s.io
       kind: Gateway
       name: mcp-gateway
       namespace: gateway-system
       sectionName: mcp
     hostnames:
     - ${MCP_GATEWAY_HOST}
     rules:
     - matches:
       - path:
           type: PathPrefix
           value: /.well-known/oauth-protected-resource
       backendRefs:
       - name: mcp-gateway
         port: 8080
   EOF
   ```

   `${MCP_GATEWAY_HOST}` is the fully qualified domain name for your MCP gateway (for example, `mcp.127-0-0-1.sslip.io`).

   This route enables clients to discover OAuth metadata, which is required for the authentication flow. Without this route, clients receive a 404 error when attempting OAuth discovery.
3. Configure the Identity Provider (Entra ID) App Registration:

   1. In the Azure Portal or Entra admin center, go to your Entra ID App Registration.
   2. Under **Expose an API**, add a custom scope named `mcp-server`.
   3. Ensure that the following scopes are available: `openid`, `offline_access`, and `mcp-server`.
   4. If required by your organization, grant admin consent for these scopes.

      For more information about configuring Entra ID app registrations, see "Microsoft Entra ID".
4. Configure certificate trust for JWT validation by mounting the Entra ID CA certificate into the Authorino deployment by running the following commands:

   ```
   $ oc create configmap entra-ca --from-file=ca.crt=/path/to/entra-ca.crt -n kuadrant-system
   ```

   ```
   $ oc patch deployment authorino -n kuadrant-system --type=json -p='[
     {
       "op": "add",
       "path": "/spec/template/spec/volumes/-",
       "value": {"name": "entra-ca", "configMap": {"name": "entra-ca"}}
     },
     {
       "op": "add",
       "path": "/spec/template/spec/containers/0/volumeMounts/-",
       "value": {"name": "entra-ca", "mountPath": "/etc/ssl/certs/entra-ca.crt", "subPath": "ca.crt"}
     }
   ]'
   ```

   This ensures that Authorino can verify JWT token signatures from Microsoft Entra ID.
5. Configure the MCP gateway authentication by applying the authentication policy that validates JWT tokens by running the following command:

   ```
   $ oc apply -f - <<EOF
   apiVersion: kuadrant.io/v1
   kind: AuthPolicy
   metadata:
     name: mcp-auth-policy
     namespace: mcp-system
   spec:
     targetRef:
       group: gateway.networking.k8s.io
       kind: Gateway
       name: mcp-gateway
       sectionName: mcp
     defaults:
       when:

         - predicate: "!request.path.contains('/.well-known')"
       rules:
         authentication:
           'entra-id':
             jwt:
               issuerUrl: https://login.microsoftonline.com/<tenant-id>/v2.0
         response:
           unauthenticated:
             code: 401
             headers:
               'WWW-Authenticate':
                 value: Bearer resource_metadata=http://mcp.127-0-0-1.sslip.io:8001/.well-known/oauth-protected-resource/mcp
             body:
               value: |
                 {
                   "error": "Unauthorized",
                   "message": "Authentication required."
                 }
   EOF
   ```

**Verification**

1. Verify OAuth Discovery by testing that the broker now serves OAuth discovery information by running the following command:

   ```
   curl http://mcp.127-0-0-1.sslip.io:8001/.well-known/oauth-protected-resource
   ```

   The command should show OAuth 2.0 Protected Resource Metadata similar to the following:

   **Example**

   ```
   {
     "resource_name": "MCP Server",
     "resource": "http://mcp.127-0-0-1.sslip.io:8001/mcp",
     "authorization_servers": [
       "https://login.microsoftonline.com/<tenant-id>/v2.0"
     ],
     "bearer_methods_supported": [
       "header"
     ],
     "scopes_supported": [
       "openid",
       "mcp-server",
       "offline_access"
     ]
   }
   ```
2. Test that protected endpoints now require authentication by running the following command:

   ```
   $ curl -v http://mcp.127-0-0-1.sslip.io:8001/mcp \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'
   ```

   **Example**

   ```
   {
     "error": "Unauthorized",
     "message": "Authentication required."
   }
   ```

##### [1.1.6.9. Set up MCP gateway authorization](#ai-app-mcp-server-setup-authorization_mcp-server-overview) Copy linkLink copied to clipboard!

Set up tool-level authorization for the Model Context Protocol (MCP) gateway to control which users can access specific MCP server tools, ensuring that each user can only use the operations permitted by their role.

**Prerequisites**

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* RBAC is configured.
* You have revoked access to specific Custom Resources (CRs) as needed.
* MCP gateway authentication is configured.
* Your identity provider is configured to include group/role claims in JWT tokens.

**Procedure**

1. Ensure that your identity provider includes necessary group/role claims in the issued JWT tokens.

   The issued OAuth token should include claims similar to:

   **Example**

   ```
   {
     "resource_access": {
       "mcp-ns/openshift-mcp-server": {
         "roles": ["pods_list", "events_list", "nodes_list", "deployments_get"]
       },
       "mcp-ns/geometry-mcp-server": {
         "roles": ["pods_list", "events_list", "nodes_list", "deployments_get"]
       }
     }
   }
   ```

   * The namespace should match the namespace of the `MCPServerRegistration` CR.
   * The “roles” represent the allowed tools. In this example, pods\_list, events\_list, nodes\_list, deployments\_get.
2. Configure tool-level authorization by applying an AuthPolicy that enforces tool-level access control by running the following command:

   ```
   $ oc apply -f - <<EOF
   apiVersion: kuadrant.io/v1
   kind: AuthPolicy
   metadata:
     name: mcp-tool-auth-policy
     namespace: openshift-mcp-server
   spec:
     targetRef:
       group: gateway.networking.k8s.io
       kind: Gateway
       name: mcp-gateway
       sectionName: mcp
     rules:
       authentication:
         'sso-server':
           jwt:
             issuerUrl: https://login.microsoftonline.com/<tenant-id>/v2.0
       authorization:
         'tool-access-check':
           patternMatching:
             patterns:
               - predicate: |
                   request.headers['x-mcp-toolname'] in (has(auth.identity.resource_access) && auth.identity.resource_access.exists(p, p == request.headers['x-mcp-servername']) ? auth.identity.resource_access[request.headers['x-mcp-servername']].roles : [])
       response:
         unauthenticated:
           headers:
             'WWW-Authenticate':
               value: Bearer resource_metadata=http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/.well-known/oauth-protected-resource/mcp
           body:
             value: |
               {
                 "error": "Unauthorized",
                 "message": "MCP Tool Access denied: Authentication required."
               }
         unauthorized:
           body:
             value: |
               {
                 "error": "Forbidden",
                 "message": "MCP Tool Access denied: Insufficient permissions for this tool."
               }
   EOF
   ```

   * `spec.sectionName` targets the MCP server Listener.
   * `<cluster-name>.<domain-name>` is the name and domain of your cluster.

**Verification**

1. Test that authorization now controls tool access by setting up the MCP Inspector:

   1. Start MCP Inspector (requires Node.js/npm) by running the following command:

      ```
      $ npx @modelcontextprotocol/inspector@latest &
      INSPECTOR_PID=$!
      ```
   2. Wait for services to start by running the following command:

      ```
      $ sleep 3
      ```
   3. Open MCP Inspector by going to the following URL: <http://localhost:6274/?transport=streamable-http&serverUrl=http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/mcp>.

      `<cluster-name>.<domain-name>` is the name and domain of your cluster.
2. To stop the services later, run the following command:

   ```
   $ kill $INSPECTOR_PID
   ```
3. Authenticate using a user account configured with the required role claims in your identity provider.
4. Try the following allowed tools:

   * pods\_list
   * events\_list
   * nodes\_list
   * deployments\_get
5. Try this restricted tool: pods\_delete

   Since this tool is restricted, you should get a 403 Forbidden error.
6. Monitor authorization decisions:

   1. Check the AuthPolicy status by running the following command:

      ```
      $ oc get authpolicy -A
      ```
   2. View the authorization logs by running the following command:

      ```
      $ oc logs -n kuadrant-system -l authorino-resource=authorino
      ```

#### [1.1.7. MCP server for Red Hat OpenShift prompting](#ai-app-mcp-server-overview-prompting-instructions_mcp-server-overview) Copy linkLink copied to clipboard!

Use Model Context Protocol (MCP) server prompts to query a Large Language Model (LLM) to identify and diagnose issues across your OpenShift Container Platform cluster.

Note

To ensure that you get the best results when prompting be sure to:

* Specify the namespace.
* For Red Hat Advanced Cluster Management (ACM) for Kubernetes environments, specify the cluster.

##### [1.1.7.1. MCP prompts](#ai-app-mcp-server-overview-prompting-instructions-prompts_mcp-server-overview) Copy linkLink copied to clipboard!

MCP Prompts are predefined templates that guide AI assistants through specific workflows.

They combine:

* **Structured guidance**: Step-by-step instructions for common tasks
* **Parameterization**: Arguments that customize the prompt for specific contexts
* **Conversation templates**: Preformatted messages that guide the interaction

##### [1.1.7.2. Creating custom prompts](#ai-app-mcp-server-overview-prompting-instructions-custom_mcp-server-overview) Copy linkLink copied to clipboard!

Define custom prompts in your `config.toml` file. Code changes and recompilation are not needed.

**Example custom prompts**

```
[[prompts]]
name = "check-pod-logs"
title = "Check Pod Logs"
description = "Quick way to check pod logs"

[[prompts.arguments]]
name = "pod_name"
description = "Name of the pod"
required = true

[[prompts.arguments]]
name = "namespace"
description = "Namespace of the pod"
required = false

[[prompts.messages]]
role = "user"
content = "Show me the logs for pod {{pod_name}} in {{namespace}}"

[[prompts.messages]]
role = "assistant"
content = "I'll retrieve and analyze the logs for you."
```

Expand

Table 1.2. Configuration reference

| Prompt Fields | |
| --- | --- |
| name (required) | Unique identifier for the prompt |
| title (optional) | Human-readable display name |
| description (required) | Brief explanation of what the prompt does |
| arguments (optional) | List of parameters the prompt accepts |
| messages (required) | Conversation template with role/content pairs |
| Argument Fields | |
| name (required) | Argument identifier |
| description (optional) | Explanation of the argument’s purpose |
| required (optional) | Whether the argument must be provided (default: false) |
| Argument Substitution | |
| Use {{argument\_name}} placeholders in message content. The template engine replaces these with actual values when the prompt is called. If an optional argument is not provided, its placeholder is removed from the output. | |

Show more

##### [1.1.7.3. Built-in prompts](#ai-app-mcp-server-overview-prompting-instructions-built-in_mcp-server-overview) Copy linkLink copied to clipboard!

The MCP server for Red Hat OpenShift includes several built-in prompts that are always available:

`Cluster-health-check` performs a comprehensive health assessment of your OpenShift cluster.

Arguments:

* namespace (optional): Limit the health check to a specific namespace. Default: all namespaces.
* check\_events (optional): Include recent warning/error events in the analysis. Values: true or false. Default: true.

What it checks:

* **Nodes**: Status and conditions (for example, Ready, MemoryPressure, DiskPressure)
* **Cluster Operators**: Available and degraded status
* **Pods**: Phase, container statuses, restart counts, and common issues (for example, CrashLoopBackOff, ImagePullBackOff)
* **Workload Controllers**: Deployments, StatefulSets, and DaemonSets replica status
* **Persistent Volume Claims**: Binding status
* **Events**: Recent warning and error events from the last hour

Example usage:

```
Check the health of my cluster
```

Or with specific parameters:

```
Check the health of namespace production
```

You can also skip event checking for faster results:

```
Check the health of my cluster without events
```

The prompt gathers comprehensive diagnostic data and presents it to the LLM for analysis, which provides:

* Overall health status (Healthy, Warning, or Critical)
* Critical issues requiring immediate attention
* Warnings and recommendations
* Summary by component

##### [1.1.7.4. Configuration file location](#ai-app-mcp-server-overview-prompting-instructions-config-file_mcp-server-overview) Copy linkLink copied to clipboard!

Place your prompts in the `config.toml` file used by the MCP server. Specify the config file path by using the `--config flag` when starting the server.

##### [1.1.7.5. Toolset prompts](#ai-app-mcp-server-overview-prompting-instructions-toolset_mcp-server-overview) Copy linkLink copied to clipboard!

Some toolsets contain prompts and enabling the toolset enables the prompt(s).

##### [1.1.7.6. Prompt merging](#ai-app-mcp-server-overview-prompting-instructions-merging_mcp-server-overview) Copy linkLink copied to clipboard!

When both toolset and config prompts exist, config-defined prompts override toolset prompts with the same name. This allows administrators to customize built-in workflows. Prompts with unique names from both sources are available.

## [Legal Notice](#idm140358603826112) Copy linkLink copied to clipboard!

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
