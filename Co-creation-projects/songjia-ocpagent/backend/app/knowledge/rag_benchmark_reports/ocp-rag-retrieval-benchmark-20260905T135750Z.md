# OCP RAG Retrieval Benchmark Report

- Created: 2026-09-05T13:57:50.717856+00:00
- Fixture: `/home/mystic/project/hello-agents/Co-creation-projects/songjia-ocpagent/backend/app/knowledge/rag_retrieval_benchmark_cases.json`
- Document version: `4.22`
- Cases: 50/50 completed

## Aggregate Metrics

| Stage | Cases | Macro precision@k | Macro recall@k | Micro precision@k | Micro recall@k |
| --- | ---: | ---: | ---: | ---: | ---: |
| dense | 50 | 0.0307 | 0.9200 | 0.0307 | 0.9200 |
| sparse | 50 | 0.0233 | 0.7000 | 0.0233 | 0.7000 |
| rrf | 50 | 0.0191 | 0.9200 | 0.0187 | 0.9200 |
| reranked | 50 | 0.0680 | 0.6800 | 0.0680 | 0.6800 |

## Case Results

### architecture-control-plane

Question: What components make up the OpenShift control plane?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| sparse | 0.0333 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| rrf | 0.0208 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| reranked | 0.1000 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |

### installation-cluster-type

Question: How do I choose an OpenShift cluster installation type?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| sparse | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace |
| rrf | 0.0196 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| reranked | 0.1000 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |

### installation-capabilities

Question: How can cluster capabilities be enabled during installation?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| sparse | 0.0333 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| rrf | 0.0217 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| reranked | 0.1000 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |

### installation-fips

Question: What is required for an FIPS-capable OpenShift installation?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| sparse | 0.0333 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| rrf | 0.0256 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| reranked | 0.1000 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |

### installation-butane

Question: How do I create a MachineConfig with Butane?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| sparse | 0.0333 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| rrf | 0.0208 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| reranked | 0.0000 | 0.0000 | - | 28e9a156-fe5a-5426-b334-6dab60337bb4 |

### installation-firewall

Question: How should I configure the firewall for OpenShift Container Platform?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| sparse | 0.0333 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| rrf | 0.0192 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| reranked | 0.1000 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |

### nodes-operations

Question: What node operations are available in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| sparse | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc |
| rrf | 0.0182 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| reranked | 0.1000 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |

### nodes-hpa

Question: How do I automatically scale pods with the horizontal pod autoscaler?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| sparse | 0.0333 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| rrf | 0.0233 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| reranked | 0.1000 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |

### nodes-vpa

Question: How do I automatically adjust pod resources with the vertical pod autoscaler?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| sparse | 0.0333 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| rrf | 0.0227 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| reranked | 0.1000 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |

### network-core-layers

Question: What are the core network layers and components in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| sparse | 0.0333 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| rrf | 0.0169 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | 0.1000 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |

### network-internal-traffic

Question: How is traffic managed within an OpenShift cluster?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| sparse | 0.0333 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| rrf | 0.0172 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| reranked | 0.1000 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |

### network-service-cidr

Question: What is the service CIDR range in OpenShift networking?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | c093be29-f9d2-5f4a-aea5-bc9303b70a99 | - |
| sparse | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| rrf | 0.0185 | 1.0000 | c093be29-f9d2-5f4a-aea5-bc9303b70a99 | - |
| reranked | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |

### network-pod-cidr

Question: What is the pod CIDR range in OpenShift networking?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| sparse | 0.0333 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| rrf | 0.0189 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| reranked | 0.1000 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |

### storage-csi

Question: What is the Container Storage Interface in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| sparse | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| rrf | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| reranked | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |

### storage-dynamic-provisioning

Question: How does dynamic provisioning work for OpenShift storage?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |
| sparse | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | 0.0217 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |
| reranked | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |

### storage-persistent-overview

Question: What is persistent storage in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| sparse | 0.0333 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| rrf | 0.0244 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| reranked | 0.1000 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |

### storage-pvc

Question: How do persistent volume claims work in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| sparse | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| rrf | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| reranked | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |

### security-authentication

Question: How does authentication work in OpenShift Container Platform?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| sparse | 0.0333 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| rrf | 0.0217 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| reranked | 0.1000 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |

### security-authorization

Question: How does authorization work in OpenShift Container Platform?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| sparse | 0.0333 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| rrf | 0.0196 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| reranked | 0.1000 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |

### security-users

Question: How are users represented in OpenShift authentication?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| sparse | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| rrf | 0.0196 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| reranked | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |

### security-groups

Question: How are groups used in OpenShift authentication?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| sparse | 0.0333 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| rrf | 0.0179 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| reranked | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |

### security-oauth-flows

Question: What OAuth token request flows are supported by OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| sparse | 0.0333 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| rrf | 0.0213 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| reranked | 0.1000 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |

### operators-overview

Question: What are Operators in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| sparse | 0.0333 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| rrf | 0.0213 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| reranked | 0.1000 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |

### operators-packaging

Question: What is the Operator Framework packaging format?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| sparse | 0.0333 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| rrf | 0.0200 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| reranked | 0.1000 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |

### operators-olm

Question: What is Operator Lifecycle Manager?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| sparse | 0.0333 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| rrf | 0.0263 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| reranked | 0.0000 | 0.0000 | - | d593c934-a567-594c-b380-da8a9681a07e |

### operators-crds

Question: What are custom resource definitions for Operators?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| sparse | 0.0333 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| rrf | 0.0208 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| reranked | 0.1000 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |

### operators-install-namespace

Question: How do I install an Operator in a namespace?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| sparse | 0.0333 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| rrf | 0.0222 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| reranked | 0.0000 | 0.0000 | - | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab |

### observability-monitoring

Question: What monitoring is provided by OpenShift Container Platform?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| sparse | 0.0333 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| rrf | 0.0204 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| reranked | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |

### observability-logging

Question: What logging capabilities are available in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| sparse | 0.0333 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| rrf | 0.0175 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| reranked | 0.1000 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |

### backup-control-plane

Question: How do control plane backup and restore operations work?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| sparse | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| rrf | 0.0217 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| reranked | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |

### backup-application

Question: How do application backup and restore operations work?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| sparse | 0.0333 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| rrf | 0.0238 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| reranked | 0.1000 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |

### backup-graceful-shutdown

Question: How do I shut down an OpenShift cluster gracefully?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| sparse | 0.0333 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| rrf | 0.0182 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| reranked | 0.1000 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |

### backup-oadp

Question: What is OpenShift API for Data Protection (OADP)?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| sparse | 0.0333 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| rrf | 0.0244 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| reranked | 0.1000 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |

### updates-mechanics

Question: How do OpenShift cluster updates work?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| sparse | 0.0333 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| rrf | 0.0182 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| reranked | 0.1000 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |

### updates-channels

Question: How do OpenShift update channels and releases work?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| sparse | 0.0333 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| rrf | 0.0250 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| reranked | 0.1000 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |

### updates-prepare-422

Question: How do I prepare a cluster to update to OpenShift 4.22?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| sparse | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6 |
| rrf | 0.0167 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| reranked | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6 |

### updates-cli

Question: How do I update an OpenShift cluster using the CLI?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| sparse | 0.0000 | 0.0000 | - | 6c6d609e-b380-5b0a-b640-640817748a47 |
| rrf | 0.0189 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| reranked | 0.1000 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |

### updates-disconnected

Question: How do I update an OpenShift cluster in a disconnected environment?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| sparse | 0.0333 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| rrf | 0.0222 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| reranked | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76 |

### machines-machine-api

Question: What is the Machine API in OpenShift?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| sparse | 0.0333 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| rrf | 0.0196 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| reranked | 0.1000 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |

### machines-autoscaling

Question: How does cluster autoscaling work for OpenShift machines?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| sparse | 0.0333 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| rrf | 0.0200 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| reranked | 0.1000 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |

### machineset-aws

Question: How do I create a compute MachineSet on AWS?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| sparse | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f |
| rrf | 0.0189 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| reranked | 0.1000 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |

### machineset-vsphere

Question: How do I create a compute MachineSet on vSphere?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| sparse | 0.0333 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| rrf | 0.0217 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| reranked | 0.1000 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |

### workloads-buildconfig

Question: What is the BuildConfig workload API?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| sparse | 0.0333 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| rrf | 0.0189 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| reranked | 0.1000 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |

### workloads-cronjob

Question: What is the CronJob workload API?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| sparse | 0.0333 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| rrf | 0.0204 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| reranked | 0.0000 | 0.0000 | - | 8b0c5464-b271-522e-9e44-32032ec320ef |

### workloads-deployment

Question: What is the Deployment workload API?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| sparse | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| rrf | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| reranked | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |

### workloads-pod

Question: What is the Pod workload API?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| sparse | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| rrf | 0.0200 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| reranked | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |

### ingress-basic-route

Question: How do I create a basic OpenShift route?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |

### ingress-secure-route

Question: How do I secure an OpenShift route?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 9e3d817c-a593-518e-8a11-f5af50b4316f | - |
| sparse | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| rrf | 0.0196 | 1.0000 | 9e3d817c-a593-518e-8a11-f5af50b4316f | - |
| reranked | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |

### ingress-external-ip

Question: How do I configure ExternalIPs for services?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| sparse | 0.0333 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| rrf | 0.0227 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| reranked | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |

### ingress-endpoint-strategy

Question: What Ingress Controller endpoint publishing strategies are available?

| Stage | Precision@k | Recall@k | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | --- | --- |
| dense | 0.0333 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| sparse | 0.0333 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| rrf | 0.0233 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| reranked | 0.1000 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |

