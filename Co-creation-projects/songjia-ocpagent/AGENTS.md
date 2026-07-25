# Project Instructions

## Project Overview

Project Name: ocp-agent

This project is an enterprise AI Agent platform demo for OpenShift cluster management scenarios.

The primary goal is to demonstrate:

- AI agent orchestration
- LangGraph workflow design
- MCP tool integration
- Agent planning and execution
- Short-term and long-term memory
- Human interaction with AI agents

This project is a demo/reference implementation.

It is NOT a production OpenShift management platform.

Do not implement production-level infrastructure operations unless explicitly requested.


---

# Repository Structure

The repository is organized as follows:
ocp-agent/
├── AGENTS.md
│
├── openspec/
│ ├── specs/
│ └── changes/
│
├── backend/
│ ├── agents/
│ ├── api/
│ ├── mcp/
│ ├── memory/
│ ├── models/
│ ├── config/
│ └── tests/
│
└── frontend/
├── src/
└── tests/



## Directory Responsibilities


### backend/

The backend contains the AI Agent runtime and service APIs.

Responsibilities:

- Agent orchestration
- LangGraph workflows
- MCP client/server implementation
- Memory management
- REST API services
- Data models


### frontend/

The frontend provides the user interface.

Responsibilities:

- User interaction
- Agent conversation UI
- Workflow visualization
- Operation result display


### openspec/

OpenSpec is used for specification-driven development.

Contains:

- Project specifications
- Architecture documents
- Feature change proposals
- Design documents
- Implementation tasks

# OpenSpec Workflow

This project uses OpenSpec for feature development.

For new features, follow these phases:

1. Explore
   - Analyze requirements and existing architecture.
   - Do not modify code.

2. Propose
   - Create OpenSpec change proposal.
   - Wait for user review and approval.

3. Apply
   - Implement approved changes only after user confirmation.

4. Sync
   - Update specifications after implementation.

5. Archive
   - Archive completed changes after user confirmation.

Do not automatically skip phases.
Do not execute the next phase unless explicitly requested by the user.


---

# System Architecture


The overall architecture:
User
|
v
Frontend
|
v
Backend API
|
v
LangGraph Agent Runtime
|
+----------------+
| |
v v

Agent Nodes Memory

|
v

MCP Client

|
v

MCP Server

|
v

Mock Cluster Provider



Main components:

## Agent Layer

Implemented using LangGraph.

Responsibilities:

- User intent understanding
- Task planning
- Tool selection
- Workflow execution
- Result generation


Expected agents:

- Router Agent
- Query Agent
- Planner Agent
- Execution Agent
- Knowledge Agent
- Memory Agent


## MCP Layer

MCP provides tools for agent interaction.

Examples:

- list_nodes
- list_pods
- list_namespaces
- create_cluster
- delete_node
- drain_node


## Memory Layer

The system uses two types of memory:


### Short-term Memory

Managed by LangGraph checkpointing.

Purpose:

- Conversation state
- Workflow state
- Intermediate results


### Long-term Memory

Managed by Mem0.

Purpose:

- User preferences
- Historical operations
- Agent experiences


---

# MCP Development Rules


## Mock Data Requirement

All MCP Server tools MUST use mock data.

This project does NOT connect to real OpenShift clusters.


Do NOT:

- Call real Kubernetes APIs
- Call real OpenShift APIs
- Require cluster credentials
- Connect to external infrastructure
- Implement real cluster operations


MCP tools should:

- Return realistic mock responses
- Simulate normal scenarios
- Simulate failure scenarios
- Keep interfaces similar to production APIs


Example:


```python
def list_nodes():

    return [
        {
            "name": "worker-01",
            "status": "Ready",
            "cpu": "8",
            "memory": "32Gi"
        }
    ]