# OCP RAG Retrieval Benchmark Report

- Created: 2026-09-05T14:38:23.179579+00:00
- Fixture: `/home/mystic/project/hello-agents/Co-creation-projects/songjia-ocpagent/backend/app/knowledge/rag_retrieval_benchmark_cases.json`
- Document version: `4.22`
- Cases: 250/250 completed

## Aggregate Metrics

| Stage | Cutoff | Cases | Macro precision | Macro recall | Micro precision | Micro recall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| dense | top-10 | 250 | 0.0868 | 0.8680 | 0.0868 | 0.8680 |
| dense | top-20 | 250 | 0.0450 | 0.9000 | 0.0450 | 0.9000 |
| dense | top-30 | 250 | 0.0309 | 0.9280 | 0.0309 | 0.9280 |
| sparse | top-10 | 250 | 0.0816 | 0.8160 | 0.0816 | 0.8160 |
| sparse | top-20 | 250 | 0.0432 | 0.8640 | 0.0432 | 0.8640 |
| sparse | top-30 | 250 | 0.0303 | 0.9080 | 0.0303 | 0.9080 |
| rrf | top-10 | 250 | 0.0884 | 0.8840 | 0.0884 | 0.8840 |
| rrf | top-20 | 250 | 0.0466 | 0.9320 | 0.0466 | 0.9320 |
| rrf | top-30 | 250 | 0.0315 | 0.9440 | 0.0315 | 0.9440 |
| reranked | top-10 | 250 | 0.0800 | 0.8000 | 0.0800 | 0.8000 |
| reranked | top-20 | 250 | 0.0458 | 0.9160 | 0.0458 | 0.9160 |
| reranked | top-30 | 250 | 0.0315 | 0.9440 | 0.0315 | 0.9440 |

## Case Results

### architecture-control-plane

Question: What components make up the OpenShift control plane?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| dense | top-20 | 0.0500 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| dense | top-30 | 0.0333 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | - |

### installation-cluster-type

Question: How do I choose an OpenShift cluster installation type?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| dense | top-20 | 0.0500 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| dense | top-30 | 0.0333 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace |
| sparse | top-20 | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace |
| sparse | top-30 | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace |
| rrf | top-10 | 0.1000 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| rrf | top-20 | 0.0500 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| rrf | top-30 | 0.0333 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| reranked | top-10 | 0.1000 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| reranked | top-20 | 0.0500 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |
| reranked | top-30 | 0.0333 | 1.0000 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | - |

### installation-capabilities

Question: How can cluster capabilities be enabled during installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| dense | top-20 | 0.0500 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| dense | top-30 | 0.0333 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 |
| sparse | top-30 | 0.0333 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | - |

### installation-fips

Question: What is required for an FIPS-capable OpenShift installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| dense | top-20 | 0.0500 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| dense | top-30 | 0.0333 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| sparse | top-10 | 0.1000 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| sparse | top-20 | 0.0500 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| sparse | top-30 | 0.0333 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| rrf | top-10 | 0.1000 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| rrf | top-20 | 0.0500 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| rrf | top-30 | 0.0333 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 3c7e49be-3b7a-5f27-a860-b95015f78d3d |
| reranked | top-20 | 0.0500 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |
| reranked | top-30 | 0.0333 | 1.0000 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | - |

### installation-butane

Question: How do I create a MachineConfig with Butane?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| dense | top-20 | 0.0500 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| dense | top-30 | 0.0333 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| reranked | top-20 | 0.0500 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | - |

### installation-firewall

Question: How should I configure the firewall for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| dense | top-20 | 0.0500 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| dense | top-30 | 0.0333 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| sparse | top-10 | 0.1000 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| sparse | top-20 | 0.0500 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| sparse | top-30 | 0.0333 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| rrf | top-10 | 0.1000 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| rrf | top-20 | 0.0500 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| rrf | top-30 | 0.0333 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| reranked | top-10 | 0.1000 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| reranked | top-20 | 0.0500 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |
| reranked | top-30 | 0.0333 | 1.0000 | c43ba670-454c-5725-8267-6aee4b080b53 | - |

### nodes-operations

Question: What node operations are available in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| dense | top-20 | 0.0500 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| dense | top-30 | 0.0333 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc |
| sparse | top-20 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc |
| sparse | top-30 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc |
| rrf | top-10 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc |
| rrf | top-20 | 0.0500 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| rrf | top-30 | 0.0333 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| reranked | top-10 | 0.1000 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| reranked | top-20 | 0.0500 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |
| reranked | top-30 | 0.0333 | 1.0000 | 14b97444-ffe1-5fb9-800a-290d53c6b9cc | - |

### nodes-hpa

Question: How do I automatically scale pods with the horizontal pod autoscaler?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| dense | top-20 | 0.0500 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| dense | top-30 | 0.0333 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| sparse | top-10 | 0.1000 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| sparse | top-20 | 0.0500 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| sparse | top-30 | 0.0333 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| rrf | top-10 | 0.1000 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| rrf | top-20 | 0.0500 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| rrf | top-30 | 0.0333 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| reranked | top-10 | 0.1000 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| reranked | top-20 | 0.0500 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |
| reranked | top-30 | 0.0333 | 1.0000 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | - |

### nodes-vpa

Question: How do I automatically adjust pod resources with the vertical pod autoscaler?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| dense | top-20 | 0.0500 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| dense | top-30 | 0.0333 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| sparse | top-10 | 0.1000 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| sparse | top-20 | 0.0500 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| sparse | top-30 | 0.0333 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| rrf | top-10 | 0.1000 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| rrf | top-20 | 0.0500 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| rrf | top-30 | 0.0333 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| reranked | top-10 | 0.1000 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| reranked | top-20 | 0.0500 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |
| reranked | top-30 | 0.0333 | 1.0000 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | - |

### network-core-layers

Question: What are the core network layers and components in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| dense | top-20 | 0.0500 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| dense | top-30 | 0.0333 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| sparse | top-10 | 0.1000 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| sparse | top-20 | 0.0500 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| sparse | top-30 | 0.0333 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | top-10 | 0.1000 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | top-20 | 0.0500 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |

### network-internal-traffic

Question: How is traffic managed within an OpenShift cluster?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 93f1a12d-b305-50fd-834d-1c48401a1838 |
| dense | top-20 | 0.0000 | 0.0000 | - | 93f1a12d-b305-50fd-834d-1c48401a1838 |
| dense | top-30 | 0.0333 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 93f1a12d-b305-50fd-834d-1c48401a1838 | - |

### network-service-cidr

Question: What is the service CIDR range in OpenShift networking?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| dense | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| dense | top-30 | 0.0333 | 1.0000 | c093be29-f9d2-5f4a-aea5-bc9303b70a99 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| sparse | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| sparse | top-30 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| rrf | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| rrf | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| rrf | top-30 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| reranked | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| reranked | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |
| reranked | top-30 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99 |

### network-pod-cidr

Question: What is the pod CIDR range in OpenShift networking?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| sparse | top-20 | 0.0500 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | - |

### storage-csi

Question: What is the Container Storage Interface in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| dense | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| dense | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| sparse | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| sparse | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| sparse | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| rrf | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| rrf | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| rrf | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| reranked | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| reranked | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |
| reranked | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658 |

### storage-dynamic-provisioning

Question: How does dynamic provisioning work for OpenShift storage?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| dense | top-20 | 0.0500 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |
| dense | top-30 | 0.0333 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| sparse | top-20 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| sparse | top-30 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | top-20 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | top-30 | 0.0333 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d |
| reranked | top-20 | 0.0500 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |
| reranked | top-30 | 0.0333 | 1.0000 | fbc8212e-0241-5fe4-984f-a044faba754d | - |

### storage-persistent-overview

Question: What is persistent storage in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314 |
| dense | top-20 | 0.0500 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| dense | top-30 | 0.0333 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314 |
| sparse | top-30 | 0.0333 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314 |
| rrf | top-20 | 0.0500 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 3b242797-c33e-52ef-9763-8625dfc47314 | - |

### storage-pvc

Question: How do persistent volume claims work in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| dense | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| dense | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27 |

### security-authentication

Question: How does authentication work in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| dense | top-20 | 0.0500 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| dense | top-30 | 0.0333 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| sparse | top-10 | 0.1000 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| sparse | top-20 | 0.0500 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| sparse | top-30 | 0.0333 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| rrf | top-10 | 0.1000 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| rrf | top-20 | 0.0500 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| rrf | top-30 | 0.0333 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| reranked | top-10 | 0.1000 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| reranked | top-20 | 0.0500 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |
| reranked | top-30 | 0.0333 | 1.0000 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | - |

### security-authorization

Question: How does authorization work in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| dense | top-20 | 0.0500 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| dense | top-30 | 0.0333 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| sparse | top-10 | 0.1000 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| sparse | top-20 | 0.0500 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| sparse | top-30 | 0.0333 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| rrf | top-10 | 0.1000 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| rrf | top-20 | 0.0500 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| rrf | top-30 | 0.0333 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| reranked | top-10 | 0.1000 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| reranked | top-20 | 0.0500 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |
| reranked | top-30 | 0.0333 | 1.0000 | 99cfd305-1539-52df-ba63-edaa17e8bced | - |

### security-users

Question: How are users represented in OpenShift authentication?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| dense | top-20 | 0.0500 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| dense | top-30 | 0.0333 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| sparse | top-20 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| sparse | top-30 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| rrf | top-10 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| rrf | top-20 | 0.0500 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| rrf | top-30 | 0.0333 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| reranked | top-20 | 0.0500 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| reranked | top-30 | 0.0333 | 1.0000 | d5b1462c-148d-5455-96ac-4e1765cacf4a | - |

### security-groups

Question: How are groups used in OpenShift authentication?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| dense | top-20 | 0.0500 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| dense | top-30 | 0.0333 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59 | - |

### security-oauth-flows

Question: What OAuth token request flows are supported by OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| dense | top-20 | 0.0500 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| dense | top-30 | 0.0333 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| sparse | top-10 | 0.1000 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| sparse | top-20 | 0.0500 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| sparse | top-30 | 0.0333 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| rrf | top-10 | 0.1000 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| rrf | top-20 | 0.0500 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| rrf | top-30 | 0.0333 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| reranked | top-10 | 0.1000 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| reranked | top-20 | 0.0500 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |
| reranked | top-30 | 0.0333 | 1.0000 | 94b4f452-edee-57d5-8300-0e0274173d7a | - |

### operators-overview

Question: What are Operators in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 |
| dense | top-20 | 0.0000 | 0.0000 | - | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 |
| dense | top-30 | 0.0333 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | - |

### operators-packaging

Question: What is the Operator Framework packaging format?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| dense | top-20 | 0.0500 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| dense | top-30 | 0.0333 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | - |

### operators-olm

Question: What is Operator Lifecycle Manager?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| dense | top-20 | 0.0500 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| dense | top-30 | 0.0333 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | d593c934-a567-594c-b380-da8a9681a07e |
| sparse | top-20 | 0.0500 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| sparse | top-30 | 0.0333 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| rrf | top-10 | 0.1000 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| rrf | top-20 | 0.0500 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| rrf | top-30 | 0.0333 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | d593c934-a567-594c-b380-da8a9681a07e |
| reranked | top-20 | 0.0000 | 0.0000 | - | d593c934-a567-594c-b380-da8a9681a07e |
| reranked | top-30 | 0.0333 | 1.0000 | d593c934-a567-594c-b380-da8a9681a07e | - |

### operators-crds

Question: What are custom resource definitions for Operators?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| dense | top-20 | 0.0500 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| dense | top-30 | 0.0333 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | - |

### operators-install-namespace

Question: How do I install an Operator in a namespace?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| dense | top-20 | 0.0500 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| dense | top-30 | 0.0333 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| sparse | top-10 | 0.1000 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| sparse | top-20 | 0.0500 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| sparse | top-30 | 0.0333 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| rrf | top-10 | 0.1000 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| rrf | top-20 | 0.0500 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| rrf | top-30 | 0.0333 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab |
| reranked | top-20 | 0.0500 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |
| reranked | top-30 | 0.0333 | 1.0000 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | - |

### observability-monitoring

Question: What monitoring is provided by OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| dense | top-20 | 0.0500 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| dense | top-30 | 0.0333 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083 | - |

### observability-logging

Question: What logging capabilities are available in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| dense | top-20 | 0.0500 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| dense | top-30 | 0.0333 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 4c532e18-b67c-5359-b034-a0907cd874a5 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 4c532e18-b67c-5359-b034-a0907cd874a5 |
| sparse | top-30 | 0.0333 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 4c532e18-b67c-5359-b034-a0907cd874a5 | - |

### backup-control-plane

Question: How do control plane backup and restore operations work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| dense | top-20 | 0.0500 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| dense | top-30 | 0.0333 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| sparse | top-20 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| sparse | top-30 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| rrf | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| rrf | top-20 | 0.0500 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| reranked | top-20 | 0.0500 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |

### backup-application

Question: How do application backup and restore operations work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6e591022-a8eb-596a-ab66-472d3f608957 |
| sparse | top-20 | 0.0500 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6e591022-a8eb-596a-ab66-472d3f608957 | - |

### backup-graceful-shutdown

Question: How do I shut down an OpenShift cluster gracefully?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| dense | top-20 | 0.0500 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| dense | top-30 | 0.0333 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b64f610a-7cef-5944-8e18-e72beb2abb51 | - |

### backup-oadp

Question: What is OpenShift API for Data Protection (OADP)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| dense | top-20 | 0.0500 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| dense | top-30 | 0.0333 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| sparse | top-10 | 0.1000 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| sparse | top-20 | 0.0500 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| reranked | top-10 | 0.1000 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| reranked | top-20 | 0.0500 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | eefde02b-0d2f-563a-995c-20564bda99d5 | - |

### updates-mechanics

Question: How do OpenShift cluster updates work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| dense | top-20 | 0.0500 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| dense | top-30 | 0.0333 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | - |

### updates-channels

Question: How do OpenShift update channels and releases work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| dense | top-20 | 0.0500 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| dense | top-30 | 0.0333 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b6bae24f-cff4-5f0e-8249-a6b115b56724 | - |

### updates-prepare-422

Question: How do I prepare a cluster to update to OpenShift 4.22?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| dense | top-20 | 0.0500 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| dense | top-30 | 0.0333 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6 |
| rrf | top-10 | 0.1000 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6 |
| reranked | top-20 | 0.0500 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0fc41488-7116-5d00-a951-27b610354fa6 | - |

### updates-cli

Question: How do I update an OpenShift cluster using the CLI?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6c6d609e-b380-5b0a-b640-640817748a47 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6c6d609e-b380-5b0a-b640-640817748a47 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 6c6d609e-b380-5b0a-b640-640817748a47 |
| rrf | top-10 | 0.1000 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6c6d609e-b380-5b0a-b640-640817748a47 | - |

### updates-disconnected

Question: How do I update an OpenShift cluster in a disconnected environment?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| dense | top-20 | 0.0500 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| dense | top-30 | 0.0333 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76 |
| sparse | top-20 | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76 |
| sparse | top-30 | 0.0333 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| rrf | top-10 | 0.1000 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| rrf | top-20 | 0.0500 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| rrf | top-30 | 0.0333 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76 |
| reranked | top-20 | 0.0500 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |
| reranked | top-30 | 0.0333 | 1.0000 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | - |

### machines-machine-api

Question: What is the Machine API in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| dense | top-20 | 0.0500 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| dense | top-30 | 0.0333 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| reranked | top-10 | 0.1000 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| reranked | top-20 | 0.0500 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |

### machines-autoscaling

Question: How does cluster autoscaling work for OpenShift machines?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| dense | top-20 | 0.0500 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| dense | top-30 | 0.0333 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 20755582-df24-52ee-85c8-309d77cdfad4 | - |

### machineset-aws

Question: How do I create a compute MachineSet on AWS?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| dense | top-20 | 0.0500 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| dense | top-30 | 0.0333 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f |
| sparse | top-30 | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f |
| rrf | top-10 | 0.1000 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | - |

### machineset-vsphere

Question: How do I create a compute MachineSet on vSphere?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| dense | top-20 | 0.0500 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| dense | top-30 | 0.0333 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | - |

### workloads-buildconfig

Question: What is the BuildConfig workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| dense | top-20 | 0.0500 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| dense | top-30 | 0.0333 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| sparse | top-10 | 0.1000 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| sparse | top-20 | 0.0500 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| sparse | top-30 | 0.0333 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| rrf | top-10 | 0.1000 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| rrf | top-20 | 0.0500 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| rrf | top-30 | 0.0333 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| reranked | top-10 | 0.1000 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| reranked | top-20 | 0.0500 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |
| reranked | top-30 | 0.0333 | 1.0000 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | - |

### workloads-cronjob

Question: What is the CronJob workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| dense | top-20 | 0.0500 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| dense | top-30 | 0.0333 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| sparse | top-10 | 0.1000 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| sparse | top-20 | 0.0500 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| sparse | top-30 | 0.0333 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 8b0c5464-b271-522e-9e44-32032ec320ef |
| reranked | top-20 | 0.0500 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8b0c5464-b271-522e-9e44-32032ec320ef | - |

### workloads-deployment

Question: What is the Deployment workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| dense | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| dense | top-30 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| sparse | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| sparse | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| sparse | top-30 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| rrf | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| rrf | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| rrf | top-30 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| reranked | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| reranked | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |
| reranked | top-30 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f |

### workloads-pod

Question: What is the Pod workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| rrf | top-20 | 0.0500 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1 |
| reranked | top-30 | 0.0333 | 1.0000 | 6986ef3f-df3e-554b-960e-8287587551b1 | - |

### ingress-basic-route

Question: How do I create a basic OpenShift route?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| dense | top-20 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| dense | top-30 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 9c12f617-eb4d-53eb-9566-20d859a99cd8 |

### ingress-secure-route

Question: How do I secure an OpenShift route?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| dense | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| dense | top-30 | 0.0333 | 1.0000 | 9e3d817c-a593-518e-8a11-f5af50b4316f | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| sparse | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| sparse | top-30 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| rrf | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| rrf | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| rrf | top-30 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| reranked | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |
| reranked | top-30 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f |

### ingress-external-ip

Question: How do I configure ExternalIPs for services?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| dense | top-20 | 0.0500 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| dense | top-30 | 0.0333 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| sparse | top-10 | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| sparse | top-20 | 0.0500 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| sparse | top-30 | 0.0333 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| rrf | top-10 | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| rrf | top-20 | 0.0500 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| rrf | top-30 | 0.0333 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| reranked | top-10 | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| reranked | top-20 | 0.0500 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |
| reranked | top-30 | 0.0333 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b | - |

### ingress-endpoint-strategy

Question: What Ingress Controller endpoint publishing strategies are available?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| dense | top-20 | 0.0500 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| dense | top-30 | 0.0333 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f98209c8-9f55-532e-b621-e251ba433bb4 | - |

### corpus-advanced-networking-2

Question: How does OpenShift Container Platform document Specialized and advanced networking topics in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | - |

### corpus-ai-applications-2

Question: How does OpenShift Container Platform document Using AI applications on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| dense | top-20 | 0.0500 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| dense | top-30 | 0.0333 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | - |

### corpus-ai-workloads-2

Question: How does OpenShift Container Platform document Running AI workloads on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| dense | top-20 | 0.0500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| dense | top-30 | 0.0333 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183 | - |

### corpus-api-overview-2

Question: How does OpenShift Container Platform document Overview content for the OpenShift Container Platform API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| dense | top-20 | 0.0500 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| dense | top-30 | 0.0333 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | - |

### corpus-architecture-2

Question: How does OpenShift Container Platform document An overview of the architecture for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| dense | top-20 | 0.0500 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| dense | top-30 | 0.0333 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| sparse | top-10 | 0.1000 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| sparse | top-20 | 0.0500 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| sparse | top-30 | 0.0333 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| rrf | top-10 | 0.1000 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| reranked | top-10 | 0.1000 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| reranked | top-20 | 0.0500 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5d6617ec-1789-5858-a380-aecc3c03aa2e | - |

### corpus-authentication-and-authorization-3

Question: How does OpenShift Container Platform document Chapter1.Overview of authentication and authorization?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| dense | top-20 | 0.0500 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| dense | top-30 | 0.0333 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| reranked | top-20 | 0.0500 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | - |

### corpus-authorization-apis-2

Question: How does OpenShift Container Platform document Reference guide for authorization APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| dense | top-20 | 0.0500 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| dense | top-30 | 0.0333 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |

### corpus-autoscale-apis-2

Question: How does OpenShift Container Platform document Reference guide for autoscale APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| dense | top-20 | 0.0500 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| dense | top-30 | 0.0333 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a1b8eb78-2362-55b1-a776-eec474282f15 | - |

### corpus-backup-and-restore-2

Question: How does OpenShift Container Platform document Backing up and restoring your OpenShift Container Platform cluster?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| dense | top-20 | 0.0500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| dense | top-30 | 0.0333 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| sparse | top-10 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| sparse | top-20 | 0.0500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| sparse | top-30 | 0.0333 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| rrf | top-10 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| rrf | top-20 | 0.0500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| rrf | top-30 | 0.0333 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| reranked | top-10 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| reranked | top-20 | 0.0500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |
| reranked | top-30 | 0.0333 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f | - |

### corpus-building-applications-2

Question: How does OpenShift Container Platform document Creating and managing applications on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| dense | top-20 | 0.0500 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| dense | top-30 | 0.0333 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | - |

### corpus-builds-using-buildconfig-3

Question: How does OpenShift Container Platform document 1.1.Builds?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| dense | top-20 | 0.0500 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| dense | top-30 | 0.0333 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| sparse | top-10 | 0.1000 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| sparse | top-20 | 0.0500 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| sparse | top-30 | 0.0333 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| rrf | top-10 | 0.1000 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| rrf | top-20 | 0.0500 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| rrf | top-30 | 0.0333 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| reranked | top-10 | 0.1000 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| reranked | top-20 | 0.0500 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | - |

### corpus-builds-using-shipwright-2

Question: How does OpenShift Container Platform document An extensible build framework to build container images on an OpenShift cluster?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| dense | top-20 | 0.0500 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| dense | top-30 | 0.0333 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | - |

### corpus-cicd-overview-2

Question: How does OpenShift Container Platform document Contains information about CI/CD for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| dense | top-20 | 0.0500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| dense | top-30 | 0.0333 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8 | - |

### corpus-cli-tools-2

Question: How does OpenShift Container Platform document Learning how to use the command-line tools for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |

### corpus-cluster-apis-2

Question: How does OpenShift Container Platform document Reference guide for cluster APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| dense | top-20 | 0.0500 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| dense | top-30 | 0.0333 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | - |

### corpus-cluster-observability-operator-2

Question: How does OpenShift Container Platform document Configuring and using the Cluster Observability Operator in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| dense | top-20 | 0.0500 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| dense | top-30 | 0.0333 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378 | - |

### corpus-common-object-reference-2

Question: How does OpenShift Container Platform document Reference guide common API objects?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| dense | top-20 | 0.0500 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| dense | top-30 | 0.0333 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| sparse | top-10 | 0.1000 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| sparse | top-20 | 0.0500 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| sparse | top-30 | 0.0333 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| rrf | top-10 | 0.1000 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| rrf | top-20 | 0.0500 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| rrf | top-30 | 0.0333 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| reranked | top-10 | 0.1000 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| reranked | top-20 | 0.0500 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |
| reranked | top-30 | 0.0333 | 1.0000 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | - |

### corpus-config-apis-2

Question: How does OpenShift Container Platform document Reference guide for config APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| dense | top-20 | 0.0500 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| dense | top-30 | 0.0333 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| sparse | top-10 | 0.1000 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| sparse | top-20 | 0.0500 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| sparse | top-30 | 0.0333 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| rrf | top-10 | 0.1000 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| rrf | top-20 | 0.0500 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| rrf | top-30 | 0.0333 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| reranked | top-10 | 0.1000 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| reranked | top-20 | 0.0500 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |
| reranked | top-30 | 0.0333 | 1.0000 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | - |

### corpus-configuring-network-settings-2

Question: How does OpenShift Container Platform document General networking configuration processes in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| dense | top-20 | 0.0500 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| dense | top-30 | 0.0333 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f741081f-2b5f-54db-9d54-dfb08627f439 | - |

### corpus-console-apis-2

Question: How does OpenShift Container Platform document Reference guide for console APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| dense | top-20 | 0.0500 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| dense | top-30 | 0.0333 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| sparse | top-10 | 0.1000 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| sparse | top-20 | 0.0500 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| sparse | top-30 | 0.0333 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| rrf | top-10 | 0.1000 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| rrf | top-20 | 0.0500 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| rrf | top-30 | 0.0333 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| reranked | top-10 | 0.1000 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| reranked | top-20 | 0.0500 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |
| reranked | top-30 | 0.0333 | 1.0000 | d34a1045-05a4-510b-a425-080bc74f6631 | - |

### corpus-disconnected-environments-2

Question: How does OpenShift Container Platform document Managing OpenShift Container Platform clusters in a disconnected environment?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| dense | top-20 | 0.0500 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| dense | top-30 | 0.0333 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| sparse | top-10 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| sparse | top-20 | 0.0500 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| sparse | top-30 | 0.0333 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| rrf | top-10 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| rrf | top-20 | 0.0500 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| rrf | top-30 | 0.0333 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| reranked | top-10 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| reranked | top-20 | 0.0500 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| reranked | top-30 | 0.0333 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |

### corpus-distributed-tracing-2

Question: How does OpenShift Container Platform document Configuring and using distributed tracing in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| dense | top-20 | 0.0500 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| dense | top-30 | 0.0333 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| sparse | top-10 | 0.1000 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| sparse | top-20 | 0.0500 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| sparse | top-30 | 0.0333 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| reranked | top-10 | 0.1000 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| reranked | top-20 | 0.0500 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c | - |

### corpus-edge-computing-2

Question: How does OpenShift Container Platform document Configure and deploy OpenShift Container Platform clusters at the network edge?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| dense | top-20 | 0.0500 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| dense | top-30 | 0.0333 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | - |

### corpus-etcd-2

Question: How does OpenShift Container Platform document Providing redundancy with etcd?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| dense | top-20 | 0.0500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| dense | top-30 | 0.0333 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| sparse | top-10 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| sparse | top-20 | 0.0500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| sparse | top-30 | 0.0333 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| rrf | top-10 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| rrf | top-20 | 0.0500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| rrf | top-30 | 0.0333 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| reranked | top-10 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| reranked | top-20 | 0.0500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| reranked | top-30 | 0.0333 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |

### corpus-extension-apis-2

Question: How does OpenShift Container Platform document Reference guide for extension APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| dense | top-20 | 0.0500 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| dense | top-30 | 0.0333 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | - |

### corpus-extensions-2

Question: How does OpenShift Container Platform document Working with extensions in OpenShift Container Platform using Operator Lifecycle Manager (OLM) v1.?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| dense | top-20 | 0.0500 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| dense | top-30 | 0.0333 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| sparse | top-10 | 0.1000 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| sparse | top-20 | 0.0500 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| sparse | top-30 | 0.0333 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| rrf | top-10 | 0.1000 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| rrf | top-20 | 0.0500 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| rrf | top-30 | 0.0333 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| reranked | top-10 | 0.1000 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| reranked | top-20 | 0.0500 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| reranked | top-30 | 0.0333 | 1.0000 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |

### corpus-gitops-2

Question: How does OpenShift Container Platform document A declarative way to implement continuous deployment for cloud native applications.?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| dense | top-20 | 0.0500 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| dense | top-30 | 0.0333 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | - |

### corpus-hardware-accelerators-2

Question: How does OpenShift Container Platform document Hardware accelerators?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| dense | top-20 | 0.0500 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| dense | top-30 | 0.0333 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| sparse | top-10 | 0.1000 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| sparse | top-20 | 0.0500 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| sparse | top-30 | 0.0333 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| rrf | top-10 | 0.1000 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| rrf | top-20 | 0.0500 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| rrf | top-30 | 0.0333 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| reranked | top-10 | 0.1000 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| reranked | top-20 | 0.0500 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |
| reranked | top-30 | 0.0333 | 1.0000 | efe72277-e863-5717-be18-3446659b193b | - |

### corpus-hardware-networks-2

Question: How does OpenShift Container Platform document Configuring hardware-specific networking features in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| dense | top-20 | 0.0500 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| dense | top-30 | 0.0333 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| sparse | top-10 | 0.1000 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| sparse | top-20 | 0.0500 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| sparse | top-30 | 0.0333 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| rrf | top-10 | 0.1000 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| rrf | top-20 | 0.0500 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| rrf | top-30 | 0.0333 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| reranked | top-10 | 0.1000 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| reranked | top-20 | 0.0500 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |
| reranked | top-30 | 0.0333 | 1.0000 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | - |

### corpus-hosted-control-planes-2

Question: How does OpenShift Container Platform document Using hosted control planes with OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| dense | top-20 | 0.0500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| dense | top-30 | 0.0333 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | - |

### corpus-image-apis-2

Question: How does OpenShift Container Platform document Reference guide for image APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| dense | top-20 | 0.0500 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| dense | top-30 | 0.0333 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| sparse | top-10 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| sparse | top-20 | 0.0500 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| sparse | top-30 | 0.0333 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| rrf | top-10 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| rrf | top-20 | 0.0500 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| rrf | top-30 | 0.0333 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| reranked | top-10 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| reranked | top-20 | 0.0500 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| reranked | top-30 | 0.0333 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |

### corpus-images-2

Question: How does OpenShift Container Platform document Creating and managing images and imagestreams in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2d37dd44-deed-5a47-bb08-772676b96949 | - |

### corpus-ingress-and-load-balancing-2

Question: How does OpenShift Container Platform document Exposing services and managing external traffic in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| dense | top-20 | 0.0500 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| dense | top-30 | 0.0333 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| sparse | top-10 | 0.1000 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| sparse | top-20 | 0.0500 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| sparse | top-30 | 0.0333 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| rrf | top-10 | 0.1000 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| rrf | top-20 | 0.0500 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| rrf | top-30 | 0.0333 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| reranked | top-10 | 0.1000 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| reranked | top-20 | 0.0500 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |
| reranked | top-30 | 0.0333 | 1.0000 | aeb316dd-8324-5466-96e7-b50216f67eba | - |

### corpus-installation-configuration-2

Question: How does OpenShift Container Platform document Cluster-wide configuration during installations?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| dense | top-20 | 0.0500 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| dense | top-30 | 0.0333 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e67a501e-c58e-56ac-b490-6080c3ff7167 | - |

### corpus-installation-overview-2

Question: How does OpenShift Container Platform document Overview content for installing OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| dense | top-20 | 0.0500 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| dense | top-30 | 0.0333 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 52c58389-178b-5c15-8ed0-c686feaea548 | - |

### corpus-installing-a-two-node-openshift-cluster-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on two nodes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| dense | top-20 | 0.0500 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| dense | top-30 | 0.0333 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| sparse | top-10 | 0.1000 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| sparse | top-20 | 0.0500 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| sparse | top-30 | 0.0333 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| rrf | top-10 | 0.1000 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| rrf | top-20 | 0.0500 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| rrf | top-30 | 0.0333 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| reranked | top-10 | 0.1000 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| reranked | top-20 | 0.0500 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| reranked | top-30 | 0.0333 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca | - |

### corpus-installing-an-on-premise-cluster-with-the-agent-based-installer-2

Question: How does OpenShift Container Platform document Installing an on-premise OpenShift Container Platform cluster with the Agent-based Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| dense | top-20 | 0.0500 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| dense | top-30 | 0.0333 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 |
| reranked | top-30 | 0.0333 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |

### corpus-installing-ibm-cloud-bare-metal-classic-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Cloud Bare Metal (Classic)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| dense | top-20 | 0.0500 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| dense | top-30 | 0.0333 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| sparse | top-10 | 0.1000 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| sparse | top-20 | 0.0500 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| sparse | top-30 | 0.0333 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| rrf | top-10 | 0.1000 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| rrf | top-20 | 0.0500 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| rrf | top-30 | 0.0333 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| reranked | top-10 | 0.1000 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| reranked | top-20 | 0.0500 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |
| reranked | top-30 | 0.0333 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d | - |

### corpus-installing-on-premise-with-assisted-installer-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on-premise with the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| dense | top-20 | 0.0500 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| dense | top-30 | 0.0333 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| sparse | top-10 | 0.1000 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| sparse | top-20 | 0.0500 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| sparse | top-30 | 0.0333 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| rrf | top-10 | 0.1000 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| rrf | top-20 | 0.0500 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| rrf | top-30 | 0.0333 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 94e34536-1d0e-53dc-bb09-e12da9c56b8f |
| reranked | top-20 | 0.0500 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |

### corpus-installing-on-a-single-node-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on a single node?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| dense | top-20 | 0.0500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| dense | top-30 | 0.0333 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | e775a89d-d659-5d00-8fb5-cb89d0977449 |
| reranked | top-20 | 0.0500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449 | - |

### corpus-installing-on-alibaba-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Alibaba Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| dense | top-20 | 0.0500 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| dense | top-30 | 0.0333 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| sparse | top-10 | 0.1000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| sparse | top-20 | 0.0500 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| sparse | top-30 | 0.0333 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| rrf | top-10 | 0.1000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| rrf | top-20 | 0.0500 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| rrf | top-30 | 0.0333 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| reranked | top-10 | 0.1000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| reranked | top-20 | 0.0500 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| reranked | top-30 | 0.0333 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd | - |

### corpus-installing-on-any-platform-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on any platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| dense | top-20 | 0.0500 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| dense | top-30 | 0.0333 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| sparse | top-10 | 0.1000 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| sparse | top-20 | 0.0500 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| sparse | top-30 | 0.0333 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| rrf | top-10 | 0.1000 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| rrf | top-20 | 0.0500 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| rrf | top-30 | 0.0333 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| reranked | top-10 | 0.1000 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| reranked | top-20 | 0.0500 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |
| reranked | top-30 | 0.0333 | 1.0000 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | - |

### corpus-installing-on-aws-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Amazon Web Services?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| dense | top-20 | 0.0500 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| dense | top-30 | 0.0333 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| sparse | top-10 | 0.1000 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| sparse | top-20 | 0.0500 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| sparse | top-30 | 0.0333 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| rrf | top-10 | 0.1000 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| rrf | top-20 | 0.0500 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| rrf | top-30 | 0.0333 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| reranked | top-10 | 0.1000 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| reranked | top-20 | 0.0500 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |
| reranked | top-30 | 0.0333 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | - |

### corpus-installing-on-azure-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Azure?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 2643250e-5baa-583b-b070-6fbe83bf5c77 |
| reranked | top-20 | 0.0500 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | - |

### corpus-installing-on-azure-stack-hub-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Azure Stack Hub?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| dense | top-20 | 0.0500 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| dense | top-30 | 0.0333 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| sparse | top-10 | 0.1000 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| sparse | top-20 | 0.0500 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| sparse | top-30 | 0.0333 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| rrf | top-10 | 0.1000 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| rrf | top-20 | 0.0500 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| rrf | top-30 | 0.0333 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba |
| reranked | top-20 | 0.0500 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |
| reranked | top-30 | 0.0333 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba | - |

### corpus-installing-on-bare-metal-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on bare metal?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| dense | top-20 | 0.0500 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| dense | top-30 | 0.0333 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |
| reranked | top-20 | 0.0500 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | - |

### corpus-installing-on-google-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Google Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| dense | top-20 | 0.0500 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| dense | top-30 | 0.0333 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 |
| reranked | top-20 | 0.0500 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | - |

### corpus-installing-on-ibm-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Cloud Bare Metal (Classic)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| dense | top-20 | 0.0500 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| dense | top-30 | 0.0333 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| sparse | top-10 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| sparse | top-20 | 0.0500 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| sparse | top-30 | 0.0333 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| rrf | top-10 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| rrf | top-20 | 0.0500 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| rrf | top-30 | 0.0333 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| reranked | top-10 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| reranked | top-20 | 0.0500 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |
| reranked | top-30 | 0.0333 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | - |

### corpus-installing-on-ibm-power-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Power?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| dense | top-20 | 0.0500 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| dense | top-30 | 0.0333 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 89389d95-495d-5611-ac71-fa2e7c985088 |
| reranked | top-20 | 0.0500 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088 | - |

### corpus-installing-on-ibm-power-virtual-server-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Power Virtual Server?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| dense | top-20 | 0.0500 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| dense | top-30 | 0.0333 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9b437025-830f-5e34-ab75-07ee52fc97a5 |
| reranked | top-20 | 0.0500 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |

### corpus-installing-on-ibm-powervc-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM PowerVC?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| dense | top-20 | 0.0500 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| dense | top-30 | 0.0333 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | ca4751a8-63fd-5016-a6f4-33c5e441c801 |
| reranked | top-20 | 0.0500 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |

### corpus-installing-on-ibm-z-and-ibm-linuxone-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Z and IBM LinuxONE?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| dense | top-20 | 0.0500 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| dense | top-30 | 0.0333 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| sparse | top-10 | 0.1000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| sparse | top-20 | 0.0500 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| sparse | top-30 | 0.0333 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| rrf | top-10 | 0.1000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| rrf | top-20 | 0.0500 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| rrf | top-30 | 0.0333 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | eef7ef3d-a263-5dd1-867f-ea331bde63ae |
| reranked | top-20 | 0.0500 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| reranked | top-30 | 0.0333 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |

### corpus-installing-on-nutanix-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Nutanix?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |

### corpus-installing-on-openstack-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on OpenStack?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| dense | top-20 | 0.0500 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| dense | top-30 | 0.0333 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789 | - |

### corpus-installing-on-oracle-database-appliance-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Installing on Oracle Database Appliance?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| dense | top-20 | 0.0500 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| dense | top-30 | 0.0333 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2a675940-64ff-5403-8209-990058797cea | - |

### corpus-installing-on-oracle-distributed-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Oracle Distributed Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| dense | top-20 | 0.0500 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| dense | top-30 | 0.0333 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| sparse | top-10 | 0.1000 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| sparse | top-20 | 0.0500 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | eac4261f-2460-503f-94f0-c5329f9018d5 |
| reranked | top-20 | 0.0500 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | eac4261f-2460-503f-94f0-c5329f9018d5 | - |

### corpus-installing-on-oracle-edge-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Oracle Edge Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| dense | top-20 | 0.0500 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| dense | top-30 | 0.0333 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | eb7235ff-a939-5bde-a133-635edbde7ae8 | - |

### corpus-installing-on-vmware-vsphere-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on vSphere?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| dense | top-20 | 0.0500 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| dense | top-30 | 0.0333 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| sparse | top-10 | 0.1000 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| sparse | top-20 | 0.0500 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| sparse | top-30 | 0.0333 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| rrf | top-10 | 0.1000 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| rrf | top-20 | 0.0500 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| rrf | top-30 | 0.0333 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | d97adff8-6154-56a2-bd9a-6416cd6093c2 |
| reranked | top-20 | 0.0000 | 0.0000 | - | d97adff8-6154-56a2-bd9a-6416cd6093c2 |
| reranked | top-30 | 0.0333 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |

### corpus-jenkins-3

Question: How does OpenShift Container Platform document Chapter1.Configuring Jenkins images?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| dense | top-20 | 0.0500 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| dense | top-30 | 0.0333 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | - |

### corpus-kubernetes-nmstate-2

Question: How does OpenShift Container Platform document Observing and updating node network state and configuration using Kubernetes NMState in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| dense | top-20 | 0.0500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| dense | top-30 | 0.0333 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| sparse | top-10 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| sparse | top-20 | 0.0500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| sparse | top-30 | 0.0333 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| rrf | top-10 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| rrf | top-20 | 0.0500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| rrf | top-30 | 0.0333 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| reranked | top-10 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| reranked | top-20 | 0.0500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |
| reranked | top-30 | 0.0333 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea | - |

### corpus-logging-2

Question: How does OpenShift Container Platform document Configuring and using logging in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| dense | top-20 | 0.0500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| dense | top-30 | 0.0333 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | - |

### corpus-machine-apis-2

Question: How does OpenShift Container Platform document Reference guide for machine APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| dense | top-20 | 0.0500 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| dense | top-30 | 0.0333 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 01feaa64-52d1-5311-be91-638189b9d982 | - |

### corpus-machine-configuration-2

Question: How does OpenShift Container Platform document Managing and applying configuration and updates of the base operating system and container runtimes in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| dense | top-20 | 0.0500 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| dense | top-30 | 0.0333 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2a23a7d9-4976-5501-86e4-669c9956d90f | - |

### corpus-machine-management-2

Question: How does OpenShift Container Platform document Adding and maintaining cluster machines?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| dense | top-20 | 0.0500 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| dense | top-30 | 0.0333 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| sparse | top-10 | 0.1000 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| sparse | top-20 | 0.0500 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| sparse | top-30 | 0.0333 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| rrf | top-10 | 0.1000 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| rrf | top-20 | 0.0500 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| rrf | top-30 | 0.0333 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| reranked | top-10 | 0.1000 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| reranked | top-20 | 0.0500 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |
| reranked | top-30 | 0.0333 | 1.0000 | bb43a1c4-4251-555f-9399-5f0283105079 | - |

### corpus-metadata-apis-2

Question: How does OpenShift Container Platform document Reference guide for metadata APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| dense | top-20 | 0.0500 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| dense | top-30 | 0.0333 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a4702c78-4647-5eb3-89df-60d31f85aba1 | - |

### corpus-migrating-from-version-3-to-4-2

Question: How does OpenShift Container Platform document Migrating to OpenShift Container Platform 4?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268 | - |

### corpus-monitoring-2

Question: How does OpenShift Container Platform document Configuring and using the monitoring stack in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| dense | top-20 | 0.0500 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| dense | top-30 | 0.0333 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 16289132-d267-551c-91d1-e388cbe1ce32 | - |

### corpus-monitoring-apis-2

Question: How does OpenShift Container Platform document Reference guide for monitoring APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| dense | top-20 | 0.0500 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| dense | top-30 | 0.0333 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a051b20f-a822-51f8-94eb-a7b71880f454 | - |

### corpus-multiple-networks-2

Question: How does OpenShift Container Platform document Configuring and managing multiple network interfaces and virtual routing in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| dense | top-20 | 0.0500 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| dense | top-30 | 0.0333 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| sparse | top-10 | 0.1000 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| sparse | top-20 | 0.0500 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| sparse | top-30 | 0.0333 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| rrf | top-10 | 0.1000 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| rrf | top-20 | 0.0500 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| rrf | top-30 | 0.0333 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| reranked | top-10 | 0.1000 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| reranked | top-20 | 0.0500 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |
| reranked | top-30 | 0.0333 | 1.0000 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | - |

### corpus-network-apis-2

Question: How does OpenShift Container Platform document Reference guide for network APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| dense | top-20 | 0.0500 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| dense | top-30 | 0.0333 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | - |

### corpus-network-observability-2

Question: How does OpenShift Container Platform document Configuring and using the Network Observability Operator in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| dense | top-20 | 0.0500 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| dense | top-30 | 0.0333 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | - |

### corpus-network-observability-operator-2

Question: How does OpenShift Container Platform document Network Observability Operator for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| dense | top-20 | 0.0500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| dense | top-30 | 0.0333 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| sparse | top-10 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| sparse | top-20 | 0.0500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| sparse | top-30 | 0.0333 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| rrf | top-10 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| rrf | top-20 | 0.0500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| rrf | top-30 | 0.0333 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| reranked | top-10 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| reranked | top-20 | 0.0500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| reranked | top-30 | 0.0333 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |

### corpus-network-security-2

Question: How does OpenShift Container Platform document Securing network traffic and enforcing network policies in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| dense | top-20 | 0.0500 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| dense | top-30 | 0.0333 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| sparse | top-10 | 0.1000 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| sparse | top-20 | 0.0500 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| sparse | top-30 | 0.0333 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| rrf | top-10 | 0.1000 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| rrf | top-20 | 0.0500 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| rrf | top-30 | 0.0333 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| reranked | top-10 | 0.1000 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| reranked | top-20 | 0.0500 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |
| reranked | top-30 | 0.0333 | 1.0000 | afecc12a-942c-509f-bdad-a987f4ee6d45 | - |

### corpus-networking-operators-2

Question: How does OpenShift Container Platform document Managing networking-specific Operators in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| dense | top-20 | 0.0500 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| dense | top-30 | 0.0333 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| sparse | top-10 | 0.1000 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| sparse | top-20 | 0.0500 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| sparse | top-30 | 0.0333 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| rrf | top-10 | 0.1000 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| rrf | top-20 | 0.0500 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| rrf | top-30 | 0.0333 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| reranked | top-10 | 0.1000 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| reranked | top-20 | 0.0500 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |
| reranked | top-30 | 0.0333 | 1.0000 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | - |

### corpus-networking-overview-2

Question: How does OpenShift Container Platform document Understanding fundamental networking concepts and general tasks in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| dense | top-20 | 0.0500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| dense | top-30 | 0.0333 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827 | - |

### corpus-node-apis-2

Question: How does OpenShift Container Platform document Reference guide for node APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| dense | top-20 | 0.0500 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| dense | top-30 | 0.0333 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| reranked | top-10 | 0.1000 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| reranked | top-20 | 0.0500 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | - |

### corpus-nodes-2

Question: How does OpenShift Container Platform document Configuring and managing nodes in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| dense | top-20 | 0.0500 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| dense | top-30 | 0.0333 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| sparse | top-10 | 0.1000 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| sparse | top-20 | 0.0500 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| sparse | top-30 | 0.0333 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| rrf | top-10 | 0.1000 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| rrf | top-20 | 0.0500 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| rrf | top-30 | 0.0333 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| reranked | top-10 | 0.1000 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| reranked | top-20 | 0.0500 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |
| reranked | top-30 | 0.0333 | 1.0000 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | - |

### corpus-oauth-apis-2

Question: How does OpenShift Container Platform document Reference guide for Oauth APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| dense | top-20 | 0.0500 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| dense | top-30 | 0.0333 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |

### corpus-observability-overview-2

Question: How does OpenShift Container Platform document Contains information about observability for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| dense | top-20 | 0.0500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| dense | top-30 | 0.0333 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| sparse | top-10 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| sparse | top-20 | 0.0500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| sparse | top-30 | 0.0333 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| rrf | top-10 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| rrf | top-20 | 0.0500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| rrf | top-30 | 0.0333 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| reranked | top-10 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| reranked | top-20 | 0.0500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |
| reranked | top-30 | 0.0333 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b | - |

### corpus-openshift-lightspeed-2

Question: How does OpenShift Container Platform document About OpenShift Lightspeed?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| dense | top-20 | 0.0500 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| dense | top-30 | 0.0333 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| sparse | top-10 | 0.1000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| sparse | top-20 | 0.0500 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| sparse | top-30 | 0.0333 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| reranked | top-10 | 0.1000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| reranked | top-20 | 0.0500 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | - |

### corpus-openshift-sandboxed-containers-2

Question: How does OpenShift Container Platform document OpenShift sandboxed containers guide?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| dense | top-20 | 0.0500 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| dense | top-30 | 0.0333 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| sparse | top-10 | 0.1000 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| sparse | top-20 | 0.0500 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| sparse | top-30 | 0.0333 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| rrf | top-10 | 0.1000 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| rrf | top-20 | 0.0500 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| rrf | top-30 | 0.0333 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| reranked | top-10 | 0.1000 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| reranked | top-20 | 0.0500 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |
| reranked | top-30 | 0.0333 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239 | - |

### corpus-operator-apis-2

Question: How does OpenShift Container Platform document Reference guide for Operator APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| dense | top-20 | 0.0500 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| dense | top-30 | 0.0333 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | - |

### corpus-operatorhub-apis-2

Question: How does OpenShift Container Platform document Reference guide for OperatorHub APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| dense | top-20 | 0.0500 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| dense | top-30 | 0.0333 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| sparse | top-10 | 0.1000 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| sparse | top-20 | 0.0500 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| sparse | top-30 | 0.0333 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| rrf | top-10 | 0.1000 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| rrf | top-20 | 0.0500 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| rrf | top-30 | 0.0333 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| reranked | top-10 | 0.1000 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| reranked | top-20 | 0.0500 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |
| reranked | top-30 | 0.0333 | 1.0000 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | - |

### corpus-operators-2

Question: How does OpenShift Container Platform document Working with Operators in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| dense | top-20 | 0.0500 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| dense | top-30 | 0.0333 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| sparse | top-10 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| sparse | top-20 | 0.0500 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| sparse | top-30 | 0.0333 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| rrf | top-10 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| rrf | top-20 | 0.0500 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| rrf | top-30 | 0.0333 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| reranked | top-10 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| reranked | top-20 | 0.0500 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |
| reranked | top-30 | 0.0333 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | - |

### corpus-overview-2

Question: How does OpenShift Container Platform document Introduction to OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | - |

### corpus-ovn-kubernetes-network-plugin-2

Question: How does OpenShift Container Platform document In-depth configuration and troubleshooting for the OVN-Kubernetes network plugin in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| dense | top-20 | 0.0500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| dense | top-30 | 0.0333 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8 | - |

### corpus-pipelines-2

Question: How does OpenShift Container Platform document Contains information about Pipelines for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| dense | top-20 | 0.0500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| dense | top-30 | 0.0333 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051 | - |

### corpus-policy-apis-2

Question: How does OpenShift Container Platform document Reference guide for policy APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| dense | top-20 | 0.0500 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| dense | top-30 | 0.0333 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | - |

### corpus-postinstallation-configuration-2

Question: How does OpenShift Container Platform document Day 2 operations for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| dense | top-20 | 0.0500 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| dense | top-30 | 0.0333 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| reranked | top-10 | 0.1000 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| reranked | top-20 | 0.0500 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | - |

### corpus-power-monitoring-2

Question: How does OpenShift Container Platform document Configuring and using power monitoring for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| dense | top-20 | 0.0500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| dense | top-30 | 0.0333 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| sparse | top-10 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| sparse | top-20 | 0.0500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| sparse | top-30 | 0.0333 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| rrf | top-10 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| reranked | top-10 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| reranked | top-20 | 0.0500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba | - |

### corpus-project-apis-2

Question: How does OpenShift Container Platform document Reference guide for project APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| dense | top-20 | 0.0500 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| dense | top-30 | 0.0333 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| sparse | top-10 | 0.1000 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| sparse | top-20 | 0.0500 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| sparse | top-30 | 0.0333 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| rrf | top-10 | 0.1000 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| rrf | top-20 | 0.0500 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| rrf | top-30 | 0.0333 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| reranked | top-10 | 0.1000 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| reranked | top-20 | 0.0500 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |
| reranked | top-30 | 0.0333 | 1.0000 | 12550d39-b552-5d17-99d7-383a5aabd41d | - |

### corpus-provisioning-apis-2

Question: How does OpenShift Container Platform document Reference guide for provisioning APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| dense | top-20 | 0.0500 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| dense | top-30 | 0.0333 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| sparse | top-10 | 0.1000 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| sparse | top-20 | 0.0500 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| sparse | top-30 | 0.0333 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| rrf | top-10 | 0.1000 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| rrf | top-20 | 0.0500 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| rrf | top-30 | 0.0333 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| reranked | top-10 | 0.1000 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| reranked | top-20 | 0.0500 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |
| reranked | top-30 | 0.0333 | 1.0000 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | - |

### corpus-rbac-apis-2

Question: How does OpenShift Container Platform document Reference guide for RBAC APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| dense | top-20 | 0.0500 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| dense | top-30 | 0.0333 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| sparse | top-10 | 0.1000 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| sparse | top-20 | 0.0500 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| sparse | top-30 | 0.0333 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| rrf | top-10 | 0.1000 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| rrf | top-20 | 0.0500 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| rrf | top-30 | 0.0333 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| reranked | top-10 | 0.1000 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| reranked | top-20 | 0.0500 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |
| reranked | top-30 | 0.0333 | 1.0000 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | - |

### corpus-red-hat-build-of-opentelemetry-2

Question: How does OpenShift Container Platform document Configuring and using the Red Hat build of OpenTelemetry in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | - |

### corpus-registry-2

Question: How does OpenShift Container Platform document Configuring registries for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| dense | top-20 | 0.0500 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| dense | top-30 | 0.0333 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606 | - |

### corpus-release-notes-2

Question: How does OpenShift Container Platform document Highlights of what is new and what has changed with this OpenShift Container Platform release?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| dense | top-20 | 0.0500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| dense | top-30 | 0.0333 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| sparse | top-10 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| sparse | top-20 | 0.0500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| sparse | top-30 | 0.0333 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| rrf | top-10 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| rrf | top-20 | 0.0500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| rrf | top-30 | 0.0333 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| reranked | top-10 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| reranked | top-20 | 0.0500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |
| reranked | top-30 | 0.0333 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db | - |

### corpus-role-apis-2

Question: How does OpenShift Container Platform document Reference guide for role APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| dense | top-20 | 0.0500 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| dense | top-30 | 0.0333 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| sparse | top-10 | 0.1000 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| rrf | top-10 | 0.1000 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| reranked | top-10 | 0.1000 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| reranked | top-20 | 0.0500 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | - |

### corpus-scalability-and-performance-2

Question: How does OpenShift Container Platform document Scaling your OpenShift Container Platform cluster and tuning performance in production environments?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| dense | top-20 | 0.0500 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| dense | top-30 | 0.0333 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473 | - |

### corpus-schedule-and-quota-apis-2

Question: How does OpenShift Container Platform document Reference guide for schedule and quota APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| dense | top-20 | 0.0500 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| dense | top-30 | 0.0333 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| sparse | top-10 | 0.1000 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| sparse | top-20 | 0.0500 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| sparse | top-30 | 0.0333 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| rrf | top-10 | 0.1000 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| rrf | top-20 | 0.0500 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| rrf | top-30 | 0.0333 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| reranked | top-10 | 0.1000 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| reranked | top-20 | 0.0500 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |
| reranked | top-30 | 0.0333 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | - |

### corpus-security-and-compliance-2

Question: How does OpenShift Container Platform document Learning about and managing security for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| dense | top-20 | 0.0500 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| dense | top-30 | 0.0333 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 405b6e83-7846-562b-b674-25124368f657 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 405b6e83-7846-562b-b674-25124368f657 |
| sparse | top-30 | 0.0333 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657 | - |

### corpus-security-apis-2

Question: How does OpenShift Container Platform document Reference guide for security APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| dense | top-20 | 0.0500 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| dense | top-30 | 0.0333 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| sparse | top-10 | 0.1000 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| sparse | top-20 | 0.0500 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | - |

### corpus-serverless-2

Question: How does OpenShift Container Platform document OpenShift Serverless installation, usage, and release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| dense | top-20 | 0.0500 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| dense | top-30 | 0.0333 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| reranked | top-10 | 0.1000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| reranked | top-20 | 0.0500 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489 | - |

### corpus-service-mesh-2

Question: How does OpenShift Container Platform document Service Mesh installation, usage, and release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| dense | top-20 | 0.0500 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| dense | top-30 | 0.0333 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | - |

### corpus-specialized-hardware-and-driver-enablement-2

Question: How does OpenShift Container Platform document Learn about hardware enablement on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| dense | top-20 | 0.0500 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| dense | top-30 | 0.0333 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223 | - |

### corpus-storage-2

Question: How does OpenShift Container Platform document Configuring and managing storage in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| dense | top-20 | 0.0500 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| dense | top-30 | 0.0333 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 332810e1-67f3-5288-a876-deb1168d67ba |
| sparse | top-20 | 0.0500 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| sparse | top-30 | 0.0333 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| rrf | top-10 | 0.1000 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| rrf | top-20 | 0.0500 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| rrf | top-30 | 0.0333 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| reranked | top-10 | 0.1000 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| reranked | top-20 | 0.0500 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |
| reranked | top-30 | 0.0333 | 1.0000 | 332810e1-67f3-5288-a876-deb1168d67ba | - |

### corpus-storage-apis-2

Question: How does OpenShift Container Platform document Reference guide for storage APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| dense | top-20 | 0.0500 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| dense | top-30 | 0.0333 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | - |

### corpus-support-2

Question: How does OpenShift Container Platform document Getting support for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | - |

### corpus-template-apis-2

Question: How does OpenShift Container Platform document Reference guide for template APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| dense | top-20 | 0.0500 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| dense | top-30 | 0.0333 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e310c8e9-6494-5ce9-8bd3-822283f11639 | - |

### corpus-tutorials-2

Question: How does OpenShift Container Platform document Getting started in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| dense | top-20 | 0.0500 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| dense | top-30 | 0.0333 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | - |

### corpus-updating-clusters-2

Question: How does OpenShift Container Platform document Updating OpenShift Container Platform clusters?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| dense | top-20 | 0.0500 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| dense | top-30 | 0.0333 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | - |

### corpus-user-and-group-apis-2

Question: How does OpenShift Container Platform document Reference guide for user and group APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| dense | top-20 | 0.0500 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| dense | top-30 | 0.0333 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | - |

### corpus-validation-and-troubleshooting-2

Question: How does OpenShift Container Platform document Validating and troubleshooting an OpenShift Container Platform installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| dense | top-20 | 0.0500 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| dense | top-30 | 0.0333 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |

### corpus-virtualization-2

Question: How does OpenShift Container Platform document OpenShift Virtualization installation, usage, and release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| dense | top-20 | 0.0500 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| dense | top-30 | 0.0333 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| sparse | top-10 | 0.1000 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| sparse | top-20 | 0.0500 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| sparse | top-30 | 0.0333 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| rrf | top-10 | 0.1000 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| rrf | top-20 | 0.0500 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| rrf | top-30 | 0.0333 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| reranked | top-10 | 0.1000 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| reranked | top-20 | 0.0500 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |
| reranked | top-30 | 0.0333 | 1.0000 | cac5e3ed-2125-5139-934f-4bba3b356e46 | - |

### corpus-virtualized-control-planes-2

Question: How does OpenShift Container Platform document Deploying OpenShift Container Platform clusters with virtualized control planes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| dense | top-20 | 0.0500 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| dense | top-30 | 0.0333 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707 | - |

### corpus-web-console-2

Question: How does OpenShift Container Platform document Getting started with the web console in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| dense | top-20 | 0.0500 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| dense | top-30 | 0.0333 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4 | - |

### corpus-windows-container-support-for-openshift-2

Question: How does OpenShift Container Platform document Red Hat OpenShift for Windows Containers Guide?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| dense | top-20 | 0.0500 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| dense | top-30 | 0.0333 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| sparse | top-10 | 0.1000 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| sparse | top-20 | 0.0500 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| sparse | top-30 | 0.0333 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| rrf | top-10 | 0.1000 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| rrf | top-20 | 0.0500 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| rrf | top-30 | 0.0333 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| reranked | top-10 | 0.1000 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| reranked | top-20 | 0.0500 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |
| reranked | top-30 | 0.0333 | 1.0000 | 7845e78c-66f1-5772-bacd-d813225b973b | - |

### corpus-workloads-apis-2

Question: How does OpenShift Container Platform document Reference guide for workloads APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| dense | top-20 | 0.0500 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| dense | top-30 | 0.0333 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 349797a4-9fc0-5591-91bf-abfe954f3860 | - |

### corpus-advanced-networking-3

Question: How does OpenShift Container Platform document Chapter1.Verifying connectivity to an endpoint?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| dense | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| dense | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645 |

### corpus-ai-applications-3

Question: How does OpenShift Container Platform document 1.1.Inspect clusters with MCP server for Red Hat OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| dense | top-20 | 0.0500 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| dense | top-30 | 0.0333 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| sparse | top-10 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| sparse | top-20 | 0.0500 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| sparse | top-30 | 0.0333 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| rrf | top-10 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| rrf | top-20 | 0.0500 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| rrf | top-30 | 0.0333 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| reranked | top-10 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| reranked | top-20 | 0.0500 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |
| reranked | top-30 | 0.0333 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e | - |

### corpus-ai-workloads-3

Question: How does OpenShift Container Platform document Chapter1.Overview of AI workloads on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| dense | top-20 | 0.0500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| dense | top-30 | 0.0333 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0 | - |

### corpus-api-overview-3

Question: How does OpenShift Container Platform document Chapter1.Understanding API tiers?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| dense | top-20 | 0.0500 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| dense | top-30 | 0.0333 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| sparse | top-10 | 0.1000 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| sparse | top-20 | 0.0500 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| sparse | top-30 | 0.0333 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| rrf | top-10 | 0.1000 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| rrf | top-20 | 0.0500 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| rrf | top-30 | 0.0333 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| reranked | top-10 | 0.1000 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| reranked | top-20 | 0.0500 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |
| reranked | top-30 | 0.0333 | 1.0000 | d144675a-71c4-573f-8cbf-a04b2f5c633c | - |

### corpus-architecture-3

Question: How does OpenShift Container Platform document Chapter1.Architecture overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| dense | top-20 | 0.0500 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| dense | top-30 | 0.0333 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| sparse | top-10 | 0.1000 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| sparse | top-20 | 0.0500 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| sparse | top-30 | 0.0333 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| rrf | top-10 | 0.1000 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| rrf | top-20 | 0.0500 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| rrf | top-30 | 0.0333 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| reranked | top-10 | 0.1000 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| reranked | top-20 | 0.0500 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |
| reranked | top-30 | 0.0333 | 1.0000 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | - |

### corpus-authentication-and-authorization-4

Question: How does OpenShift Container Platform document 1.1.Glossary of common terms for OpenShift Container Platform authentication and authorization?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| dense | top-20 | 0.0500 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| dense | top-30 | 0.0333 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| sparse | top-10 | 0.1000 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| sparse | top-20 | 0.0500 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| sparse | top-30 | 0.0333 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| rrf | top-10 | 0.1000 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| rrf | top-20 | 0.0500 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| rrf | top-30 | 0.0333 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| reranked | top-10 | 0.1000 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| reranked | top-20 | 0.0500 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |
| reranked | top-30 | 0.0333 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | - |

### corpus-authorization-apis-3

Question: How does OpenShift Container Platform document [1.1.LocalResourceAccessReview [authorization.openshift.io/v1]](#localresourceaccessreview-authorization-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| dense | top-20 | 0.0500 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| dense | top-30 | 0.0333 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | - |

### corpus-autoscale-apis-3

Question: How does OpenShift Container Platform document [1.1.ClusterAutoscaler [autoscaling.openshift.io/v1]](#clusterautoscaler-autoscaling-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| dense | top-20 | 0.0500 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| dense | top-30 | 0.0333 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| rrf | top-10 | 0.1000 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| reranked | top-20 | 0.0500 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | - |

### corpus-backup-and-restore-3

Question: How does OpenShift Container Platform document Chapter1.Backup and restore?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| dense | top-20 | 0.0500 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| dense | top-30 | 0.0333 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 987380f9-f164-5728-9141-559790cb7069 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 987380f9-f164-5728-9141-559790cb7069 |
| sparse | top-30 | 0.0333 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069 | - |

### corpus-building-applications-3

Question: How does OpenShift Container Platform document Chapter1.Building applications overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| dense | top-20 | 0.0500 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| dense | top-30 | 0.0333 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| sparse | top-10 | 0.1000 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| sparse | top-20 | 0.0500 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| sparse | top-30 | 0.0333 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| rrf | top-10 | 0.1000 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| rrf | top-20 | 0.0500 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| rrf | top-30 | 0.0333 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| reranked | top-10 | 0.1000 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| reranked | top-20 | 0.0500 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |
| reranked | top-30 | 0.0333 | 1.0000 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | - |

### corpus-builds-using-buildconfig-5

Question: How does OpenShift Container Platform document 1.1.1.Docker build?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2de9267a-6b39-545f-91ae-0e7833009f30 | - |

### corpus-builds-using-shipwright-3

Question: How does OpenShift Container Platform document Chapter1.Overview of Builds?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| dense | top-20 | 0.0500 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| dense | top-30 | 0.0333 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0e53378e-3fa4-5aba-833a-809b7c5772da | - |

### corpus-cicd-overview-3

Question: How does OpenShift Container Platform document Chapter1.About CI/CD?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| dense | top-20 | 0.0500 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| dense | top-30 | 0.0333 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |

### corpus-cli-tools-3

Question: How does OpenShift Container Platform document Chapter1.OpenShift Container Platform CLI tools overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| dense | top-20 | 0.0500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| dense | top-30 | 0.0333 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | - |

### corpus-cluster-apis-3

Question: How does OpenShift Container Platform document [1.1.IPAddress [ipam.cluster.x-k8s.io/v1beta1]](#ipaddress-ipam-cluster-x-k8s-iov1beta1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| dense | top-20 | 0.0500 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| dense | top-30 | 0.0333 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| reranked | top-20 | 0.0500 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | - |

### corpus-cluster-observability-operator-3

Question: How does OpenShift Container Platform document Chapter1.Cluster Observability Operator overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222 | - |

### corpus-common-object-reference-3

Question: How does OpenShift Container Platform document 1.1.com.coreos.monitoring.v1.AlertmanagerList schema?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| dense | top-20 | 0.0500 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| dense | top-30 | 0.0333 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| sparse | top-10 | 0.1000 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| sparse | top-20 | 0.0500 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| sparse | top-30 | 0.0333 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| rrf | top-10 | 0.1000 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| rrf | top-20 | 0.0500 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| rrf | top-30 | 0.0333 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| reranked | top-10 | 0.1000 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| reranked | top-20 | 0.0500 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |
| reranked | top-30 | 0.0333 | 1.0000 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | - |

### corpus-config-apis-3

Question: How does OpenShift Container Platform document [1.1.APIServer [config.openshift.io/v1]](#apiserver-config-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| dense | top-20 | 0.0500 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| dense | top-30 | 0.0333 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| sparse | top-10 | 0.1000 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| sparse | top-20 | 0.0500 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| sparse | top-30 | 0.0333 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| rrf | top-10 | 0.1000 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| rrf | top-20 | 0.0500 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| rrf | top-30 | 0.0333 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| reranked | top-10 | 0.1000 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| reranked | top-20 | 0.0500 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |
| reranked | top-30 | 0.0333 | 1.0000 | fcae96e9-3a23-518d-b191-69ebf26ea43e | - |

### corpus-configuring-network-settings-3

Question: How does OpenShift Container Platform document Chapter1.Configuring system controls and interface attributes using the tuning plugin?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| dense | top-20 | 0.0500 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| dense | top-30 | 0.0333 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| sparse | top-10 | 0.1000 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| sparse | top-20 | 0.0500 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| sparse | top-30 | 0.0333 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| rrf | top-10 | 0.1000 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| rrf | top-20 | 0.0500 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| rrf | top-30 | 0.0333 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| reranked | top-10 | 0.1000 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| reranked | top-20 | 0.0500 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |
| reranked | top-30 | 0.0333 | 1.0000 | aea45e71-8964-5bc3-92e7-e6557d60dc8d | - |

### corpus-console-apis-3

Question: How does OpenShift Container Platform document [1.1.ConsoleCLIDownload [console.openshift.io/v1]](#consoleclidownload-console-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| dense | top-20 | 0.0500 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| dense | top-30 | 0.0333 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| sparse | top-10 | 0.1000 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| sparse | top-20 | 0.0500 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| sparse | top-30 | 0.0333 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| rrf | top-10 | 0.1000 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| rrf | top-20 | 0.0500 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| rrf | top-30 | 0.0333 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| reranked | top-10 | 0.1000 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| reranked | top-20 | 0.0500 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |
| reranked | top-30 | 0.0333 | 1.0000 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | - |

### corpus-disconnected-environments-3

Question: How does OpenShift Container Platform document Chapter1.About disconnected environments?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| dense | top-20 | 0.0500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| dense | top-30 | 0.0333 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54 | - |

### corpus-distributed-tracing-3

Question: How does OpenShift Container Platform document Chapter1.About the Distributed Tracing Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| dense | top-20 | 0.0500 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| dense | top-30 | 0.0333 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| sparse | top-30 | 0.0333 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |

### corpus-edge-computing-3

Question: How does OpenShift Container Platform document Chapter1.Challenges of the network far edge?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| dense | top-20 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| dense | top-30 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-10 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-20 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-30 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-10 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-20 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-30 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-20 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-30 | 0.0000 | 0.0000 | - | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |

### corpus-etcd-3

Question: How does OpenShift Container Platform document Chapter1.Overview of etcd?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| dense | top-20 | 0.0500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| dense | top-30 | 0.0333 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| sparse | top-10 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| sparse | top-20 | 0.0500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| sparse | top-30 | 0.0333 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| rrf | top-10 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| rrf | top-20 | 0.0500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| rrf | top-30 | 0.0333 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| reranked | top-10 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| reranked | top-20 | 0.0500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| reranked | top-30 | 0.0333 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52 | - |

### corpus-extension-apis-3

Question: How does OpenShift Container Platform document [1.1.APIService [apiregistration.k8s.io/v1]](#apiservice-apiregistration-k8s-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| dense | top-20 | 0.0500 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| dense | top-30 | 0.0333 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| sparse | top-10 | 0.1000 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| sparse | top-20 | 0.0500 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| sparse | top-30 | 0.0333 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| rrf | top-10 | 0.1000 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| rrf | top-20 | 0.0500 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| rrf | top-30 | 0.0333 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 58322bfd-1625-56fe-a131-f476ab75678f |
| reranked | top-20 | 0.0500 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 58322bfd-1625-56fe-a131-f476ab75678f | - |

### corpus-extensions-3

Question: How does OpenShift Container Platform document Chapter1.Extensions overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 3e0957c9-d14c-5f36-b2f0-812bf71282af |
| dense | top-20 | 0.0500 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| dense | top-30 | 0.0333 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| sparse | top-10 | 0.1000 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| sparse | top-20 | 0.0500 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| sparse | top-30 | 0.0333 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| rrf | top-10 | 0.1000 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| rrf | top-20 | 0.0500 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| rrf | top-30 | 0.0333 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| reranked | top-10 | 0.1000 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| reranked | top-20 | 0.0500 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |
| reranked | top-30 | 0.0333 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | - |

### corpus-gitops-3

Question: How does OpenShift Container Platform document Chapter1.About RedHat OpenShift GitOps?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| dense | top-20 | 0.0500 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| dense | top-30 | 0.0333 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| sparse | top-10 | 0.1000 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| sparse | top-20 | 0.0500 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| sparse | top-30 | 0.0333 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| rrf | top-10 | 0.1000 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| rrf | top-20 | 0.0500 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| rrf | top-30 | 0.0333 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| reranked | top-10 | 0.1000 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| reranked | top-20 | 0.0500 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |
| reranked | top-30 | 0.0333 | 1.0000 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | - |

### corpus-hardware-accelerators-3

Question: How does OpenShift Container Platform document Chapter1.About hardware accelerators?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| dense | top-20 | 0.0500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| dense | top-30 | 0.0333 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| sparse | top-10 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| sparse | top-20 | 0.0500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| sparse | top-30 | 0.0333 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| rrf | top-10 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| rrf | top-20 | 0.0500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| rrf | top-30 | 0.0333 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| reranked | top-10 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| reranked | top-20 | 0.0500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |
| reranked | top-30 | 0.0333 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac | - |

### corpus-hardware-networks-3

Question: How does OpenShift Container Platform document Chapter1.About Single Root I/O Virtualization (SR-IOV) hardware networks?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| dense | top-20 | 0.0500 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| dense | top-30 | 0.0333 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | bdb22800-7a69-5c79-a968-d64045535da1 | - |

### corpus-hosted-control-planes-3

Question: How does OpenShift Container Platform document Chapter1.Hosted control planes release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| dense | top-20 | 0.0500 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| dense | top-30 | 0.0333 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |

### corpus-image-apis-3

Question: How does OpenShift Container Platform document [1.1.Image [image.openshift.io/v1]](#image-image-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| dense | top-20 | 0.0500 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| dense | top-30 | 0.0333 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 72451032-9898-5f5f-b16f-6b0d650284b7 |
| sparse | top-20 | 0.0500 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7 | - |

### corpus-images-3

Question: How does OpenShift Container Platform document Chapter1.Overview of images?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| dense | top-20 | 0.0500 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| dense | top-30 | 0.0333 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | e2fd35a2-190a-5d03-8956-91faa514385a |
| sparse | top-20 | 0.0000 | 0.0000 | - | e2fd35a2-190a-5d03-8956-91faa514385a |
| sparse | top-30 | 0.0333 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| rrf | top-10 | 0.1000 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| rrf | top-20 | 0.0500 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| rrf | top-30 | 0.0333 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| reranked | top-10 | 0.1000 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| reranked | top-20 | 0.0500 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |
| reranked | top-30 | 0.0333 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a | - |

### corpus-ingress-and-load-balancing-4

Question: How does OpenShift Container Platform document 1.1.1.Creating an HTTP-based route?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| dense | top-20 | 0.0500 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| dense | top-30 | 0.0333 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | - |

### corpus-installation-configuration-3

Question: How does OpenShift Container Platform document Chapter1.Customizing nodes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| dense | top-20 | 0.0500 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| dense | top-30 | 0.0333 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| sparse | top-10 | 0.1000 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| sparse | top-20 | 0.0500 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| sparse | top-30 | 0.0333 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| rrf | top-10 | 0.1000 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| rrf | top-20 | 0.0500 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| rrf | top-30 | 0.0333 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| reranked | top-10 | 0.1000 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| reranked | top-20 | 0.0500 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |
| reranked | top-30 | 0.0333 | 1.0000 | 694fea6c-6083-5316-af7e-9a63a535ad3b | - |

### corpus-installation-overview-3

Question: How does OpenShift Container Platform document Chapter1.OpenShift Container Platform installation overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| dense | top-20 | 0.0500 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| dense | top-30 | 0.0333 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| sparse | top-10 | 0.1000 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| sparse | top-20 | 0.0500 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| sparse | top-30 | 0.0333 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | f25095ff-907e-572c-81b5-94d064e72277 |
| reranked | top-20 | 0.0500 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |
| reranked | top-30 | 0.0333 | 1.0000 | f25095ff-907e-572c-81b5-94d064e72277 | - |

### corpus-installing-a-two-node-openshift-cluster-3

Question: How does OpenShift Container Platform document Chapter1.Two-Node with Arbiter?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| dense | top-20 | 0.0500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |

### corpus-installing-an-on-premise-cluster-with-the-agent-based-installer-3

Question: How does OpenShift Container Platform document Chapter1.Preparing to install with the Agent-based Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| dense | top-20 | 0.0500 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| dense | top-30 | 0.0333 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0da30e4c-ed47-5d04-8887-79303f4e629e | - |

### corpus-installing-ibm-cloud-bare-metal-classic-3

Question: How does OpenShift Container Platform document Chapter1.Prerequisites for installing a cluster on {ibm-cloud-bm}?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| dense | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| dense | top-30 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| sparse | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| sparse | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| sparse | top-30 | 0.0333 | 1.0000 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| rrf | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| rrf | top-30 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| reranked | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| reranked | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |
| reranked | top-30 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a |

### corpus-installing-on-premise-with-assisted-installer-3

Question: How does OpenShift Container Platform document Chapter1.Installing an on-premise cluster using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| dense | top-20 | 0.0500 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| dense | top-30 | 0.0333 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |

### corpus-installing-on-a-single-node-3

Question: How does OpenShift Container Platform document Chapter1.Preparing to install on a single node?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| dense | top-20 | 0.0500 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| dense | top-30 | 0.0333 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| sparse | top-10 | 0.1000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| sparse | top-20 | 0.0500 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| sparse | top-30 | 0.0333 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| rrf | top-10 | 0.1000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| rrf | top-20 | 0.0500 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| rrf | top-30 | 0.0333 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| reranked | top-10 | 0.1000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| reranked | top-20 | 0.0500 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| reranked | top-30 | 0.0333 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d | - |

### corpus-installing-on-alibaba-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Alibaba Cloud by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| dense | top-20 | 0.0500 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| dense | top-30 | 0.0333 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| reranked | top-10 | 0.1000 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| reranked | top-20 | 0.0500 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |

### corpus-installing-on-any-platform-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on any platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| dense | top-20 | 0.0500 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| dense | top-30 | 0.0333 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| sparse | top-10 | 0.1000 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| sparse | top-20 | 0.0500 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| sparse | top-30 | 0.0333 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| rrf | top-10 | 0.1000 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| rrf | top-20 | 0.0500 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| rrf | top-30 | 0.0333 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| reranked | top-10 | 0.1000 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| reranked | top-20 | 0.0500 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |
| reranked | top-30 | 0.0333 | 1.0000 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | - |

### corpus-installing-on-aws-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | cdd06c15-2087-5bf1-a723-bbafba10b2f8 |
| dense | top-20 | 0.0500 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| dense | top-30 | 0.0333 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| sparse | top-10 | 0.1000 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| sparse | top-20 | 0.0500 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| sparse | top-30 | 0.0333 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| rrf | top-10 | 0.1000 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| rrf | top-20 | 0.0500 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| rrf | top-30 | 0.0333 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| reranked | top-10 | 0.1000 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| reranked | top-20 | 0.0500 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |
| reranked | top-30 | 0.0333 | 1.0000 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | - |

### corpus-installing-on-azure-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| dense | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| dense | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006 |

### corpus-installing-on-azure-stack-hub-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f |
| dense | top-20 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f |
| dense | top-30 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f |
| sparse | top-10 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f |
| sparse | top-20 | 0.0500 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| sparse | top-30 | 0.0333 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f |
| rrf | top-20 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f |
| rrf | top-30 | 0.0333 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| reranked | top-10 | 0.1000 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| reranked | top-20 | 0.0500 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |

### corpus-installing-on-bare-metal-3

Question: How does OpenShift Container Platform document Chapter1.Preparing for bare-metal cluster installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| dense | top-20 | 0.0500 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| dense | top-30 | 0.0333 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| reranked | top-20 | 0.0000 | 0.0000 | - | 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| reranked | top-30 | 0.0333 | 1.0000 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |

### corpus-installing-on-google-cloud-3

Question: How does OpenShift Container Platform document 1.1.Prerequisites?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| dense | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| dense | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228 |

### corpus-installing-on-ibm-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| dense | top-20 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| dense | top-30 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| sparse | top-10 | 0.1000 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| sparse | top-20 | 0.0500 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| sparse | top-30 | 0.0333 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| rrf | top-20 | 0.0500 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| rrf | top-30 | 0.0333 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| reranked | top-10 | 0.1000 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| reranked | top-20 | 0.0500 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |
| reranked | top-30 | 0.0333 | 1.0000 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | - |

### corpus-installing-on-ibm-power-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| dense | top-20 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| dense | top-30 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| sparse | top-10 | 0.1000 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| rrf | top-20 | 0.0500 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| reranked | top-20 | 0.0500 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |

### corpus-installing-on-ibm-power-virtual-server-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| dense | top-20 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| dense | top-30 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| sparse | top-20 | 0.0500 | 1.0000 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| rrf | top-30 | 0.0333 | 1.0000 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| reranked | top-20 | 0.0500 | 1.0000 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |

### corpus-installing-on-ibm-powervc-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc |
| dense | top-20 | 0.0500 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| dense | top-30 | 0.0333 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc |
| sparse | top-20 | 0.0500 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| sparse | top-30 | 0.0333 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| rrf | top-10 | 0.1000 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| reranked | top-10 | 0.1000 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| reranked | top-20 | 0.0500 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |

### corpus-installing-on-ibm-z-and-ibm-linuxone-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa |
| dense | top-20 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa |
| dense | top-30 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa |
| sparse | top-10 | 0.1000 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| sparse | top-20 | 0.0500 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| sparse | top-30 | 0.0333 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa |
| rrf | top-20 | 0.0500 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| rrf | top-30 | 0.0333 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| reranked | top-10 | 0.1000 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| reranked | top-20 | 0.0500 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| reranked | top-30 | 0.0333 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |

### corpus-installing-on-nutanix-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 |
| dense | top-20 | 0.0000 | 0.0000 | - | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 |
| dense | top-30 | 0.0333 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |

### corpus-installing-on-openstack-3

Question: How does OpenShift Container Platform document Chapter1.Preparing to install on OpenStack?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| dense | top-20 | 0.0500 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| dense | top-30 | 0.0333 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| reranked | top-10 | 0.1000 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| reranked | top-20 | 0.0500 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |

### corpus-installing-on-oracle-database-appliance-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Oracle Database Appliance by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| dense | top-20 | 0.0500 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| dense | top-30 | 0.0333 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| sparse | top-20 | 0.0500 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| sparse | top-30 | 0.0333 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| rrf | top-10 | 0.1000 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| rrf | top-20 | 0.0500 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| rrf | top-30 | 0.0333 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| reranked | top-20 | 0.0000 | 0.0000 | - | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| reranked | top-30 | 0.0333 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | - |

### corpus-installing-on-oracle-distributed-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Oracle Distributed Cloud by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| dense | top-20 | 0.0500 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| dense | top-30 | 0.0333 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| sparse | top-20 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| sparse | top-30 | 0.0333 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| rrf | top-20 | 0.0500 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| rrf | top-30 | 0.0333 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| reranked | top-10 | 0.1000 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| reranked | top-20 | 0.0500 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |
| reranked | top-30 | 0.0333 | 1.0000 | dd93afd8-d8fb-5286-af72-7041a9f7857f | - |

### corpus-installing-on-oracle-edge-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Oracle Edge Cloud by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| dense | top-20 | 0.0500 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| dense | top-30 | 0.0333 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| sparse | top-20 | 0.0500 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| sparse | top-30 | 0.0333 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| rrf | top-20 | 0.0500 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| rrf | top-30 | 0.0333 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| reranked | top-10 | 0.1000 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| reranked | top-20 | 0.0500 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |
| reranked | top-30 | 0.0333 | 1.0000 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | - |

### corpus-installing-on-vmware-vsphere-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 2f6bf463-910c-536e-91b1-5621eeddf784 |
| dense | top-20 | 0.0500 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| dense | top-30 | 0.0333 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784 | - |

### corpus-jenkins-5

Question: How does OpenShift Container Platform document 1.1.Configuration and customization?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141 |
| dense | top-20 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141 |
| dense | top-30 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141 |
| sparse | top-10 | 0.1000 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| sparse | top-20 | 0.0500 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| sparse | top-30 | 0.0333 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141 |
| rrf | top-20 | 0.0500 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| rrf | top-30 | 0.0333 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| reranked | top-10 | 0.1000 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| reranked | top-20 | 0.0500 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |
| reranked | top-30 | 0.0333 | 1.0000 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | - |

### corpus-kubernetes-nmstate-3

Question: How does OpenShift Container Platform document Chapter1.Observing and updating the node network state and configuration?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| dense | top-20 | 0.0000 | 0.0000 | - | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| dense | top-30 | 0.0000 | 0.0000 | - | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| sparse | top-10 | 0.0000 | 0.0000 | - | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| sparse | top-20 | 0.0500 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| sparse | top-30 | 0.0333 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| rrf | top-10 | 0.0000 | 0.0000 | - | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| rrf | top-20 | 0.0500 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| rrf | top-30 | 0.0333 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| reranked | top-10 | 0.1000 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| reranked | top-20 | 0.0500 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| reranked | top-30 | 0.0333 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb | - |

### corpus-machine-apis-3

Question: How does OpenShift Container Platform document [1.1.ContainerRuntimeConfig [machineconfiguration.openshift.io/v1]](#containerruntimeconfig-machineconfiguration-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| dense | top-20 | 0.0500 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| dense | top-30 | 0.0333 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| sparse | top-10 | 0.1000 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| sparse | top-20 | 0.0500 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| sparse | top-30 | 0.0333 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| rrf | top-10 | 0.1000 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| rrf | top-20 | 0.0500 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| rrf | top-30 | 0.0333 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| reranked | top-10 | 0.1000 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| reranked | top-20 | 0.0500 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |
| reranked | top-30 | 0.0333 | 1.0000 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | - |

### corpus-machine-configuration-3

Question: How does OpenShift Container Platform document Chapter1.Machine configuration overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| dense | top-20 | 0.0000 | 0.0000 | - | d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| dense | top-30 | 0.0333 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| sparse | top-10 | 0.1000 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| sparse | top-20 | 0.0500 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| sparse | top-30 | 0.0333 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| rrf | top-10 | 0.1000 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| rrf | top-20 | 0.0500 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| rrf | top-30 | 0.0333 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| reranked | top-10 | 0.1000 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| reranked | top-20 | 0.0500 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |
| reranked | top-30 | 0.0333 | 1.0000 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | - |

### corpus-machine-management-3

Question: How does OpenShift Container Platform document Chapter1.Overview of machine management?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| dense | top-20 | 0.0500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| dense | top-30 | 0.0333 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| sparse | top-10 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| sparse | top-20 | 0.0500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| sparse | top-30 | 0.0333 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| rrf | top-10 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| rrf | top-20 | 0.0500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| rrf | top-30 | 0.0333 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| reranked | top-10 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| reranked | top-20 | 0.0500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |
| reranked | top-30 | 0.0333 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad | - |

### corpus-metadata-apis-3

Question: How does OpenShift Container Platform document [1.1.APIRequestCount [apiserver.openshift.io/v1]](#apirequestcount-apiserver-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| dense | top-20 | 0.0500 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| dense | top-30 | 0.0333 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b57bbb64-583c-523f-98c8-d52c147046c2 | - |

### corpus-migrating-from-version-3-to-4-3

Question: How does OpenShift Container Platform document Chapter1.Migration from OpenShift Container Platform 3 to 4 overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| dense | top-20 | 0.0500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| dense | top-30 | 0.0333 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| sparse | top-10 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| sparse | top-20 | 0.0500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| sparse | top-30 | 0.0333 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| rrf | top-10 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| rrf | top-20 | 0.0500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| rrf | top-30 | 0.0333 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| reranked | top-10 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| reranked | top-20 | 0.0500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| reranked | top-30 | 0.0333 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |

### corpus-monitoring-apis-3

Question: How does OpenShift Container Platform document [1.1.Alertmanager [monitoring.coreos.com/v1]](#alertmanager-monitoring-coreos-comv1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| dense | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| dense | top-30 | 0.0333 | 1.0000 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| sparse | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| sparse | top-30 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| rrf | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| rrf | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| rrf | top-30 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| reranked | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| reranked | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| reranked | top-30 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |

### corpus-multiple-networks-3

Question: How does OpenShift Container Platform document Chapter1.Understanding multiple networks?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| dense | top-20 | 0.0500 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| dense | top-30 | 0.0333 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| sparse | top-10 | 0.1000 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| sparse | top-20 | 0.0500 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| sparse | top-30 | 0.0333 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| rrf | top-10 | 0.1000 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| rrf | top-20 | 0.0500 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| rrf | top-30 | 0.0333 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| reranked | top-10 | 0.1000 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| reranked | top-20 | 0.0500 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |
| reranked | top-30 | 0.0333 | 1.0000 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 | - |

### corpus-network-apis-3

Question: How does OpenShift Container Platform document [1.1.ClusterUserDefinedNetwork [k8s.ovn.org/v1]](#clusteruserdefinednetwork-k8s-ovn-orgv1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| dense | top-20 | 0.0500 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| dense | top-30 | 0.0333 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| sparse | top-20 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| sparse | top-30 | 0.0333 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| rrf | top-10 | 0.1000 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| rrf | top-20 | 0.0500 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| rrf | top-30 | 0.0333 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| reranked | top-20 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| reranked | top-30 | 0.0333 | 1.0000 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | - |

### corpus-network-observability-3

Question: How does OpenShift Container Platform document Chapter1.Network Observability Operator release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| dense | top-20 | 0.0500 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| dense | top-30 | 0.0333 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| sparse | top-10 | 0.1000 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| sparse | top-20 | 0.0500 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| sparse | top-30 | 0.0333 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| rrf | top-10 | 0.1000 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| rrf | top-20 | 0.0500 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| rrf | top-30 | 0.0333 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| reranked | top-10 | 0.1000 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| reranked | top-20 | 0.0500 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |
| reranked | top-30 | 0.0333 | 1.0000 | ba916851-7def-53bc-bfc1-d9318d308c1c | - |

### corpus-network-observability-operator-3

Question: How does OpenShift Container Platform document Chapter1.Network Observability Operator?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| dense | top-20 | 0.0500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| dense | top-30 | 0.0333 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| sparse | top-10 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| sparse | top-20 | 0.0500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| sparse | top-30 | 0.0333 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| rrf | top-10 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| rrf | top-20 | 0.0500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| rrf | top-30 | 0.0333 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| reranked | top-10 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| reranked | top-20 | 0.0500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| reranked | top-30 | 0.0333 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |

### corpus-network-security-3

Question: How does OpenShift Container Platform document Chapter1.Understanding network policy APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| dense | top-20 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| dense | top-30 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| sparse | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| sparse | top-20 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| sparse | top-30 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| rrf | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| rrf | top-20 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| rrf | top-30 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| reranked | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| reranked | top-20 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| reranked | top-30 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd |

### corpus-networking-operators-3

Question: How does OpenShift Container Platform document Chapter1.Kubernetes NMState Operator?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| dense | top-20 | 0.0500 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| dense | top-30 | 0.0333 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| sparse | top-10 | 0.1000 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| sparse | top-20 | 0.0500 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| sparse | top-30 | 0.0333 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| rrf | top-10 | 0.1000 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| rrf | top-20 | 0.0500 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| rrf | top-30 | 0.0333 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| reranked | top-10 | 0.1000 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| reranked | top-20 | 0.0500 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |
| reranked | top-30 | 0.0333 | 1.0000 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | - |

### corpus-networking-overview-3

Question: How does OpenShift Container Platform document Chapter1.Understanding networking?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| dense | top-20 | 0.0500 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| dense | top-30 | 0.0333 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5 | - |

### corpus-node-apis-3

Question: How does OpenShift Container Platform document [1.1.Node [v1]](#node-v1-1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| dense | top-20 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| dense | top-30 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752 |

### corpus-nodes-3

Question: How does OpenShift Container Platform document Chapter1.Overview of nodes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| dense | top-20 | 0.0500 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| dense | top-30 | 0.0333 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| sparse | top-10 | 0.1000 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| sparse | top-20 | 0.0500 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| sparse | top-30 | 0.0333 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| rrf | top-10 | 0.1000 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| rrf | top-20 | 0.0500 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| rrf | top-30 | 0.0333 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| reranked | top-10 | 0.1000 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| reranked | top-20 | 0.0500 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |
| reranked | top-30 | 0.0333 | 1.0000 | e0b648b2-d5ac-505d-afda-96811d7b0926 | - |

### corpus-oauth-apis-3

Question: How does OpenShift Container Platform document [1.1.OAuthAccessToken [oauth.openshift.io/v1]](#oauthaccesstoken-oauth-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| dense | top-20 | 0.0500 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| dense | top-30 | 0.0333 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| sparse | top-10 | 0.1000 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| sparse | top-20 | 0.0500 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| sparse | top-30 | 0.0333 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| rrf | top-10 | 0.1000 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| rrf | top-20 | 0.0500 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| rrf | top-30 | 0.0333 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| reranked | top-10 | 0.1000 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| reranked | top-20 | 0.0500 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |
| reranked | top-30 | 0.0333 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | - |

### corpus-observability-overview-3

Question: How does OpenShift Container Platform document Chapter1.About Observability?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| dense | top-20 | 0.0500 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| dense | top-30 | 0.0333 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |

### corpus-openshift-lightspeed-3

Question: How does OpenShift Container Platform document 1.1.OpenShift Lightspeed overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| dense | top-20 | 0.0500 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| dense | top-30 | 0.0333 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| sparse | top-10 | 0.1000 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| sparse | top-20 | 0.0500 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| sparse | top-30 | 0.0333 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| rrf | top-10 | 0.1000 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| rrf | top-20 | 0.0500 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| rrf | top-30 | 0.0333 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| reranked | top-10 | 0.1000 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| reranked | top-20 | 0.0500 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| reranked | top-30 | 0.0333 | 1.0000 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |

### corpus-openshift-sandboxed-containers-3

Question: How does OpenShift Container Platform document Chapter1.About OpenShift sandboxed containers?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| dense | top-20 | 0.0500 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| dense | top-30 | 0.0333 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| sparse | top-10 | 0.1000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| sparse | top-20 | 0.0500 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| sparse | top-30 | 0.0333 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| rrf | top-10 | 0.1000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| rrf | top-20 | 0.0500 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| rrf | top-30 | 0.0333 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| reranked | top-10 | 0.1000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| reranked | top-20 | 0.0500 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |
| reranked | top-30 | 0.0333 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | - |

### corpus-operator-apis-3

Question: How does OpenShift Container Platform document [1.1.Authentication [operator.openshift.io/v1]](#authentication-operator-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| dense | top-20 | 0.0500 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| dense | top-30 | 0.0333 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| sparse | top-10 | 0.1000 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| sparse | top-20 | 0.0500 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| sparse | top-30 | 0.0333 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| rrf | top-10 | 0.1000 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| rrf | top-20 | 0.0500 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| rrf | top-30 | 0.0333 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| reranked | top-20 | 0.0500 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |
| reranked | top-30 | 0.0333 | 1.0000 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | - |

### corpus-operatorhub-apis-3

Question: How does OpenShift Container Platform document [1.1.CatalogSource [operators.coreos.com/v1alpha1]](#catalogsource-operators-coreos-comv1alpha1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| dense | top-20 | 0.0500 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| dense | top-30 | 0.0333 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| sparse | top-20 | 0.0500 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| sparse | top-30 | 0.0333 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| rrf | top-10 | 0.1000 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| rrf | top-20 | 0.0500 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| rrf | top-30 | 0.0333 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| reranked | top-20 | 0.0500 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |
| reranked | top-30 | 0.0333 | 1.0000 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | - |

### corpus-operators-3

Question: How does OpenShift Container Platform document Chapter1.Operators overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| dense | top-20 | 0.0500 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| dense | top-30 | 0.0333 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| sparse | top-10 | 0.1000 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| sparse | top-20 | 0.0500 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| sparse | top-30 | 0.0333 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| rrf | top-10 | 0.1000 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| rrf | top-20 | 0.0500 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| rrf | top-30 | 0.0333 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| reranked | top-10 | 0.1000 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| reranked | top-20 | 0.0500 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |
| reranked | top-30 | 0.0333 | 1.0000 | 753694b1-e529-5cac-8bf1-deb8de32cceb | - |

### corpus-overview-3

Question: How does OpenShift Container Platform document Chapter1.OpenShift Container Platform 4.22 Documentation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| dense | top-20 | 0.0500 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| dense | top-30 | 0.0333 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| sparse | top-10 | 0.1000 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| sparse | top-20 | 0.0500 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| sparse | top-30 | 0.0333 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| rrf | top-10 | 0.1000 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| rrf | top-20 | 0.0500 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| rrf | top-30 | 0.0333 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| reranked | top-10 | 0.1000 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| reranked | top-20 | 0.0500 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |
| reranked | top-30 | 0.0333 | 1.0000 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | - |

