# OCP RAG Retrieval Benchmark Report

- Created: 2026-09-05T14:49:12.560781+00:00
- Fixture: `/home/mystic/project/hello-agents/Co-creation-projects/songjia-ocpagent/backend/app/knowledge/rag_retrieval_benchmark_cases.json`
- Document version: `4.22`
- Cases: 250/250 completed

## Aggregate Metrics

| Stage | Cutoff | Cases | Macro precision | Macro recall | Micro precision | Micro recall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| dense | top-10 | 250 | 0.1620 | 0.5400 | 0.1620 | 0.5400 |
| dense | top-20 | 250 | 0.0938 | 0.6253 | 0.0938 | 0.6253 |
| dense | top-30 | 250 | 0.0655 | 0.6547 | 0.0655 | 0.6547 |
| sparse | top-10 | 250 | 0.1152 | 0.3840 | 0.1152 | 0.3840 |
| sparse | top-20 | 250 | 0.0650 | 0.4333 | 0.0650 | 0.4333 |
| sparse | top-30 | 250 | 0.0473 | 0.4733 | 0.0473 | 0.4733 |
| rrf | top-10 | 250 | 0.1432 | 0.4773 | 0.1432 | 0.4773 |
| rrf | top-20 | 250 | 0.0872 | 0.5813 | 0.0872 | 0.5813 |
| rrf | top-30 | 250 | 0.0644 | 0.6440 | 0.0644 | 0.6440 |
| reranked | top-10 | 250 | 0.1352 | 0.4507 | 0.1352 | 0.4507 |
| reranked | top-20 | 250 | 0.0838 | 0.5587 | 0.0838 | 0.5587 |
| reranked | top-30 | 250 | 0.0644 | 0.6440 | 0.0644 | 0.6440 |

## Case Results

### architecture-control-plane

Question: What components make up the OpenShift control plane?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| dense | top-20 | 0.0500 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| dense | top-30 | 0.0333 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| sparse | top-10 | 0.1000 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| sparse | top-20 | 0.0500 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| sparse | top-30 | 0.0333 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| rrf | top-10 | 0.1000 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| rrf | top-20 | 0.0500 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| rrf | top-30 | 0.0333 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| reranked | top-10 | 0.1000 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| reranked | top-20 | 0.0500 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |
| reranked | top-30 | 0.0333 | 0.3333 | 13465663-d00d-5f6d-8c73-dc0c9eb9c770 | 20df2626-09e7-58af-845e-77e4d6b5d1bc, d6fed23f-94c0-5eb1-bbab-0bb347e89fd8 |

### installation-cluster-type

Question: How do I choose an OpenShift cluster installation type?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| dense | top-20 | 0.1000 | 0.6667 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace, 01895032-32c8-522e-bb5b-fa78f2bfaa3a | c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| dense | top-30 | 0.0667 | 0.6667 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace, 01895032-32c8-522e-bb5b-fa78f2bfaa3a | c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace, 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace, 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 26c55cd5-16a6-586c-9d1e-3b89f44cbace, 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| rrf | top-10 | 0.1000 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| rrf | top-20 | 0.0500 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| rrf | top-30 | 0.0333 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| reranked | top-10 | 0.1000 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| reranked | top-20 | 0.0500 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |
| reranked | top-30 | 0.0333 | 0.3333 | 26c55cd5-16a6-586c-9d1e-3b89f44cbace | 01895032-32c8-522e-bb5b-fa78f2bfaa3a, c79a1b4a-33ff-58af-a59c-c904851c9ec7 |

### installation-capabilities

Question: How can cluster capabilities be enabled during installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| dense | top-20 | 0.0500 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| dense | top-30 | 0.0333 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| sparse | top-10 | 0.0000 | 0.0000 | - | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085, d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| sparse | top-20 | 0.0000 | 0.0000 | - | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085, d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| sparse | top-30 | 0.0333 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| rrf | top-10 | 0.1000 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| rrf | top-20 | 0.0500 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| rrf | top-30 | 0.0333 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| reranked | top-10 | 0.1000 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| reranked | top-20 | 0.0500 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |
| reranked | top-30 | 0.0333 | 0.3333 | 8e7fe99d-e3b5-58d3-81bd-a8eccad2b085 | d7bb6127-da74-5d1e-97d7-ab5e6deefd7b, cb223188-9172-5817-a7d0-47a7095c7daa |

### installation-fips

Question: What is required for an FIPS-capable OpenShift installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| dense | top-20 | 0.0500 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| dense | top-30 | 0.0333 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| sparse | top-10 | 0.1000 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| sparse | top-20 | 0.0500 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| sparse | top-30 | 0.0333 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| rrf | top-10 | 0.1000 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| rrf | top-20 | 0.0500 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| rrf | top-30 | 0.0333 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| reranked | top-10 | 0.0000 | 0.0000 | - | 3c7e49be-3b7a-5f27-a860-b95015f78d3d, c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| reranked | top-20 | 0.0500 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |
| reranked | top-30 | 0.0333 | 0.3333 | 3c7e49be-3b7a-5f27-a860-b95015f78d3d | c39d901e-6e10-5e26-ad03-b4068cf6370e, 69029cba-0f8a-58d1-905f-230423031bbf |

### installation-butane

Question: How do I create a MachineConfig with Butane?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | 694fea6c-6083-5316-af7e-9a63a535ad3b, c0abaf37-57b2-526f-901d-60a7305704e2 |
| dense | top-20 | 0.1000 | 0.6667 | 28e9a156-fe5a-5426-b334-6dab60337bb4, c0abaf37-57b2-526f-901d-60a7305704e2 | 694fea6c-6083-5316-af7e-9a63a535ad3b |
| dense | top-30 | 0.0667 | 0.6667 | 28e9a156-fe5a-5426-b334-6dab60337bb4, c0abaf37-57b2-526f-901d-60a7305704e2 | 694fea6c-6083-5316-af7e-9a63a535ad3b |
| sparse | top-10 | 0.1000 | 0.3333 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | 694fea6c-6083-5316-af7e-9a63a535ad3b, c0abaf37-57b2-526f-901d-60a7305704e2 |
| sparse | top-20 | 0.0500 | 0.3333 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | 694fea6c-6083-5316-af7e-9a63a535ad3b, c0abaf37-57b2-526f-901d-60a7305704e2 |
| sparse | top-30 | 0.0667 | 0.6667 | 28e9a156-fe5a-5426-b334-6dab60337bb4, c0abaf37-57b2-526f-901d-60a7305704e2 | 694fea6c-6083-5316-af7e-9a63a535ad3b |
| rrf | top-10 | 0.1000 | 0.3333 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | 694fea6c-6083-5316-af7e-9a63a535ad3b, c0abaf37-57b2-526f-901d-60a7305704e2 |
| rrf | top-20 | 0.1000 | 0.6667 | 28e9a156-fe5a-5426-b334-6dab60337bb4, c0abaf37-57b2-526f-901d-60a7305704e2 | 694fea6c-6083-5316-af7e-9a63a535ad3b |
| rrf | top-30 | 0.0667 | 0.6667 | 28e9a156-fe5a-5426-b334-6dab60337bb4, c0abaf37-57b2-526f-901d-60a7305704e2 | 694fea6c-6083-5316-af7e-9a63a535ad3b |
| reranked | top-10 | 0.0000 | 0.0000 | - | 28e9a156-fe5a-5426-b334-6dab60337bb4, 694fea6c-6083-5316-af7e-9a63a535ad3b, c0abaf37-57b2-526f-901d-60a7305704e2 |
| reranked | top-20 | 0.0500 | 0.3333 | 28e9a156-fe5a-5426-b334-6dab60337bb4 | 694fea6c-6083-5316-af7e-9a63a535ad3b, c0abaf37-57b2-526f-901d-60a7305704e2 |
| reranked | top-30 | 0.0667 | 0.6667 | 28e9a156-fe5a-5426-b334-6dab60337bb4, c0abaf37-57b2-526f-901d-60a7305704e2 | 694fea6c-6083-5316-af7e-9a63a535ad3b |

### installation-firewall

Question: How should I configure the firewall for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| dense | top-20 | 0.0500 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| dense | top-30 | 0.0333 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| sparse | top-10 | 0.1000 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| sparse | top-20 | 0.0500 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| sparse | top-30 | 0.0333 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| rrf | top-10 | 0.1000 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| rrf | top-20 | 0.0500 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| rrf | top-30 | 0.0333 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| reranked | top-10 | 0.1000 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| reranked | top-20 | 0.0500 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |
| reranked | top-30 | 0.0333 | 0.3333 | c43ba670-454c-5725-8267-6aee4b080b53 | d22cf4f8-89bc-56b0-91b8-52bbd995e5a0, 9fd4354a-361f-58a3-ae36-e263bf60fc36 |

### nodes-operations

Question: What node operations are available in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| dense | top-20 | 0.1000 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| dense | top-30 | 0.0667 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc, 71da908f-3fdc-5898-8caa-b2e17cffb1b2, 9c24e546-b45b-5f6e-ba58-065bcb0f72ab |
| sparse | top-20 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc, 71da908f-3fdc-5898-8caa-b2e17cffb1b2, 9c24e546-b45b-5f6e-ba58-065bcb0f72ab |
| sparse | top-30 | 0.0000 | 0.0000 | - | 14b97444-ffe1-5fb9-800a-290d53c6b9cc, 71da908f-3fdc-5898-8caa-b2e17cffb1b2, 9c24e546-b45b-5f6e-ba58-065bcb0f72ab |
| rrf | top-10 | 0.1000 | 0.3333 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab | 14b97444-ffe1-5fb9-800a-290d53c6b9cc, 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| rrf | top-20 | 0.1000 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| rrf | top-30 | 0.0667 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| reranked | top-10 | 0.2000 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| reranked | top-20 | 0.1000 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |
| reranked | top-30 | 0.0667 | 0.6667 | 9c24e546-b45b-5f6e-ba58-065bcb0f72ab, 14b97444-ffe1-5fb9-800a-290d53c6b9cc | 71da908f-3fdc-5898-8caa-b2e17cffb1b2 |

### nodes-hpa

Question: How do I automatically scale pods with the horizontal pod autoscaler?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| dense | top-20 | 0.1000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| dense | top-30 | 0.0667 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| sparse | top-10 | 0.1000 | 0.3333 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3, 335de4ce-9687-5e01-9b11-5be5661cdfa1 |
| sparse | top-20 | 0.1000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| sparse | top-30 | 0.0667 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| rrf | top-10 | 0.2000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| rrf | top-20 | 0.1000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| rrf | top-30 | 0.0667 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| reranked | top-10 | 0.2000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| reranked | top-20 | 0.1000 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |
| reranked | top-30 | 0.0667 | 0.6667 | 08ac59bc-94f0-5121-a81e-bf8f2744f9de, 335de4ce-9687-5e01-9b11-5be5661cdfa1 | 1fea83bd-e2bf-57b0-9c5e-8bc0d36655f3 |

### nodes-vpa

Question: How do I automatically adjust pod resources with the vertical pod autoscaler?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| dense | top-20 | 0.1000 | 0.6667 | 10b3df4a-c34a-58ec-9840-0cbab2da69af, c04bf6a1-5859-5c84-9905-272b62fce187 | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02 |
| dense | top-30 | 0.0667 | 0.6667 | 10b3df4a-c34a-58ec-9840-0cbab2da69af, c04bf6a1-5859-5c84-9905-272b62fce187 | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02 |
| sparse | top-10 | 0.1000 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| sparse | top-20 | 0.0500 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| sparse | top-30 | 0.0333 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| rrf | top-10 | 0.1000 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| rrf | top-20 | 0.0500 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| rrf | top-30 | 0.0667 | 0.6667 | 10b3df4a-c34a-58ec-9840-0cbab2da69af, c04bf6a1-5859-5c84-9905-272b62fce187 | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02 |
| reranked | top-10 | 0.1000 | 0.3333 | 10b3df4a-c34a-58ec-9840-0cbab2da69af | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02, c04bf6a1-5859-5c84-9905-272b62fce187 |
| reranked | top-20 | 0.1000 | 0.6667 | 10b3df4a-c34a-58ec-9840-0cbab2da69af, c04bf6a1-5859-5c84-9905-272b62fce187 | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02 |
| reranked | top-30 | 0.0667 | 0.6667 | 10b3df4a-c34a-58ec-9840-0cbab2da69af, c04bf6a1-5859-5c84-9905-272b62fce187 | 3c58f5e0-ba4a-5fe9-a2fb-80548cff1f02 |

### network-core-layers

Question: What are the core network layers and components in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | cebd4679-a49a-5968-8c31-5eaafc9b225d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| dense | top-20 | 0.1000 | 0.6667 | 8a79346f-ccde-58d4-ac55-f222e37fa23c, 8136b814-2c0c-513f-a582-42551de5bed5 | cebd4679-a49a-5968-8c31-5eaafc9b225d |
| dense | top-30 | 0.0667 | 0.6667 | 8a79346f-ccde-58d4-ac55-f222e37fa23c, 8136b814-2c0c-513f-a582-42551de5bed5 | cebd4679-a49a-5968-8c31-5eaafc9b225d |
| sparse | top-10 | 0.1000 | 0.3333 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | cebd4679-a49a-5968-8c31-5eaafc9b225d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| sparse | top-20 | 0.0500 | 0.3333 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | cebd4679-a49a-5968-8c31-5eaafc9b225d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| sparse | top-30 | 0.0333 | 0.3333 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | cebd4679-a49a-5968-8c31-5eaafc9b225d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| rrf | top-10 | 0.1000 | 0.3333 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | cebd4679-a49a-5968-8c31-5eaafc9b225d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| rrf | top-20 | 0.0500 | 0.3333 | 8a79346f-ccde-58d4-ac55-f222e37fa23c | cebd4679-a49a-5968-8c31-5eaafc9b225d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| rrf | top-30 | 0.0667 | 0.6667 | 8a79346f-ccde-58d4-ac55-f222e37fa23c, 8136b814-2c0c-513f-a582-42551de5bed5 | cebd4679-a49a-5968-8c31-5eaafc9b225d |
| reranked | top-10 | 0.2000 | 0.6667 | 8a79346f-ccde-58d4-ac55-f222e37fa23c, 8136b814-2c0c-513f-a582-42551de5bed5 | cebd4679-a49a-5968-8c31-5eaafc9b225d |
| reranked | top-20 | 0.1000 | 0.6667 | 8a79346f-ccde-58d4-ac55-f222e37fa23c, 8136b814-2c0c-513f-a582-42551de5bed5 | cebd4679-a49a-5968-8c31-5eaafc9b225d |
| reranked | top-30 | 0.0667 | 0.6667 | 8a79346f-ccde-58d4-ac55-f222e37fa23c, 8136b814-2c0c-513f-a582-42551de5bed5 | cebd4679-a49a-5968-8c31-5eaafc9b225d |

### network-internal-traffic

Question: How is traffic managed within an OpenShift cluster?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 93f1a12d-b305-50fd-834d-1c48401a1838, 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| dense | top-20 | 0.0000 | 0.0000 | - | 93f1a12d-b305-50fd-834d-1c48401a1838, 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| dense | top-30 | 0.0333 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| sparse | top-10 | 0.1000 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| sparse | top-20 | 0.0500 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| sparse | top-30 | 0.0333 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| rrf | top-10 | 0.1000 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| rrf | top-20 | 0.0500 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| rrf | top-30 | 0.0333 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| reranked | top-10 | 0.1000 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| reranked | top-20 | 0.0500 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |
| reranked | top-30 | 0.0333 | 0.3333 | 93f1a12d-b305-50fd-834d-1c48401a1838 | 48f83337-b7f2-5fed-8a99-b87eb111a298, cebd4679-a49a-5968-8c31-5eaafc9b225d |

### network-service-cidr

Question: What is the service CIDR range in OpenShift networking?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| dense | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| dense | top-30 | 0.0333 | 0.3333 | c093be29-f9d2-5f4a-aea5-bc9303b70a99 | 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| sparse | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| sparse | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| sparse | top-30 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| rrf | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| rrf | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| rrf | top-30 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| reranked | top-10 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| reranked | top-20 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |
| reranked | top-30 | 0.0000 | 0.0000 | - | c093be29-f9d2-5f4a-aea5-bc9303b70a99, 1003c541-288a-5c36-ac03-25b93dc1737d, 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 |

### network-pod-cidr

Question: What is the pod CIDR range in OpenShift networking?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| dense | top-20 | 0.0500 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| dense | top-30 | 0.0333 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0, c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| sparse | top-20 | 0.0500 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| sparse | top-30 | 0.0333 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| rrf | top-10 | 0.1000 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| rrf | top-20 | 0.0500 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| rrf | top-30 | 0.0333 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| reranked | top-10 | 0.1000 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| reranked | top-20 | 0.0500 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |
| reranked | top-30 | 0.0333 | 0.3333 | 6bfe72ff-49c1-5492-b777-6bc05c6fa6f0 | c093be29-f9d2-5f4a-aea5-bc9303b70a99, e1fa8c04-0f45-5d8a-a985-a43aaa82c663 |

### storage-csi

Question: What is the Container Storage Interface in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| dense | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| dense | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| sparse | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| sparse | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| sparse | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| rrf | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| reranked | top-10 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| reranked | top-20 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |
| reranked | top-30 | 0.0000 | 0.0000 | - | fc08ac21-31ca-50cb-b649-334863afc658, fad762bc-c8bc-5033-b0b9-cde26082969c, fbc8212e-0241-5fe4-984f-a044faba754d |

### storage-dynamic-provisioning

Question: How does dynamic provisioning work for OpenShift storage?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| dense | top-20 | 0.0500 | 0.3333 | fbc8212e-0241-5fe4-984f-a044faba754d | fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| dense | top-30 | 0.0333 | 0.3333 | fbc8212e-0241-5fe4-984f-a044faba754d | fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| sparse | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| sparse | top-20 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| sparse | top-30 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| rrf | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| rrf | top-20 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| rrf | top-30 | 0.0333 | 0.3333 | fbc8212e-0241-5fe4-984f-a044faba754d | fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| reranked | top-10 | 0.0000 | 0.0000 | - | fbc8212e-0241-5fe4-984f-a044faba754d, fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| reranked | top-20 | 0.0500 | 0.3333 | fbc8212e-0241-5fe4-984f-a044faba754d | fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |
| reranked | top-30 | 0.0333 | 0.3333 | fbc8212e-0241-5fe4-984f-a044faba754d | fc08ac21-31ca-50cb-b649-334863afc658, bd7d8490-5fff-5b8b-bfbf-1efbcdee2e21 |

### storage-persistent-overview

Question: What is persistent storage in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314, b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| dense | top-20 | 0.0500 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| dense | top-30 | 0.0333 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| sparse | top-10 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314, b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| sparse | top-20 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314, b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| sparse | top-30 | 0.0333 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| rrf | top-10 | 0.0000 | 0.0000 | - | 3b242797-c33e-52ef-9763-8625dfc47314, b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| rrf | top-20 | 0.0500 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| rrf | top-30 | 0.0333 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| reranked | top-10 | 0.1000 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| reranked | top-20 | 0.0500 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |
| reranked | top-30 | 0.0333 | 0.3333 | 3b242797-c33e-52ef-9763-8625dfc47314 | b255c27f-3b3d-5d39-95ff-cc3f9f64fa4a, 7f65c7af-ed44-5989-b94d-edde4d7b3c3f |

### storage-pvc

Question: How do persistent volume claims work in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| dense | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| dense | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| sparse | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| sparse | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| sparse | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| rrf | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| rrf | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| rrf | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| reranked | top-10 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| reranked | top-20 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |
| reranked | top-30 | 0.0000 | 0.0000 | - | 8140fdf4-176b-5eca-808b-f0cb1e734f27, 3089f0dd-9582-5f8d-8731-e2d0b59a04e9, 5ccb787e-0c8a-5364-b9d0-6c529aa0495c |

### security-authentication

Question: How does authentication work in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | 5c716710-f8c0-5567-901c-ee624da28346, 045e7dc8-5596-54d1-a459-5140f7c69868 |
| dense | top-20 | 0.1000 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| dense | top-30 | 0.0667 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| sparse | top-10 | 0.1000 | 0.3333 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | 5c716710-f8c0-5567-901c-ee624da28346, 045e7dc8-5596-54d1-a459-5140f7c69868 |
| sparse | top-20 | 0.1000 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| sparse | top-30 | 0.0667 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| rrf | top-10 | 0.2000 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| rrf | top-20 | 0.1000 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| rrf | top-30 | 0.0667 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| reranked | top-10 | 0.1000 | 0.3333 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb | 5c716710-f8c0-5567-901c-ee624da28346, 045e7dc8-5596-54d1-a459-5140f7c69868 |
| reranked | top-20 | 0.1000 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |
| reranked | top-30 | 0.0667 | 0.6667 | 430ad4df-f1a1-5c7c-a317-6d9091d7b5fb, 5c716710-f8c0-5567-901c-ee624da28346 | 045e7dc8-5596-54d1-a459-5140f7c69868 |

### security-authorization

Question: How does authorization work in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| dense | top-20 | 0.1000 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| dense | top-30 | 0.0667 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| sparse | top-10 | 0.2000 | 0.6667 | f7396111-70b1-5175-8def-a2ca1746784e, 99cfd305-1539-52df-ba63-edaa17e8bced | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| sparse | top-20 | 0.1000 | 0.6667 | f7396111-70b1-5175-8def-a2ca1746784e, 99cfd305-1539-52df-ba63-edaa17e8bced | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| sparse | top-30 | 0.0667 | 0.6667 | f7396111-70b1-5175-8def-a2ca1746784e, 99cfd305-1539-52df-ba63-edaa17e8bced | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| rrf | top-10 | 0.2000 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| rrf | top-20 | 0.1000 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| rrf | top-30 | 0.0667 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| reranked | top-10 | 0.1000 | 0.3333 | 99cfd305-1539-52df-ba63-edaa17e8bced | f7396111-70b1-5175-8def-a2ca1746784e, 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| reranked | top-20 | 0.1000 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |
| reranked | top-30 | 0.0667 | 0.6667 | 99cfd305-1539-52df-ba63-edaa17e8bced, f7396111-70b1-5175-8def-a2ca1746784e | 728d9fc0-9866-5d62-9d84-089e46cb75fc |

### security-users

Question: How are users represented in OpenShift authentication?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| dense | top-20 | 0.0500 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| dense | top-30 | 0.0333 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| sparse | top-10 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a, ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| sparse | top-20 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a, ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| sparse | top-30 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a, ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| rrf | top-10 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a, ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| rrf | top-20 | 0.0500 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| rrf | top-30 | 0.0333 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| reranked | top-10 | 0.0000 | 0.0000 | - | d5b1462c-148d-5455-96ac-4e1765cacf4a, ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| reranked | top-20 | 0.0500 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |
| reranked | top-30 | 0.0333 | 0.3333 | d5b1462c-148d-5455-96ac-4e1765cacf4a | ee997644-2916-59d2-99db-675f0e309a46, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 |

### security-groups

Question: How are groups used in OpenShift authentication?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | f603bd9e-0235-5172-8fac-3797316a2d59 | a7762803-1bcc-572c-a37b-ff51adbe9d8c, 628b3d7c-561b-5ffa-9423-7339f5a97606 |
| dense | top-20 | 0.1500 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59, a7762803-1bcc-572c-a37b-ff51adbe9d8c, 628b3d7c-561b-5ffa-9423-7339f5a97606 | - |
| dense | top-30 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59, a7762803-1bcc-572c-a37b-ff51adbe9d8c, 628b3d7c-561b-5ffa-9423-7339f5a97606 | - |
| sparse | top-10 | 0.1000 | 0.3333 | f603bd9e-0235-5172-8fac-3797316a2d59 | a7762803-1bcc-572c-a37b-ff51adbe9d8c, 628b3d7c-561b-5ffa-9423-7339f5a97606 |
| sparse | top-20 | 0.1000 | 0.6667 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606 | a7762803-1bcc-572c-a37b-ff51adbe9d8c |
| sparse | top-30 | 0.0667 | 0.6667 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606 | a7762803-1bcc-572c-a37b-ff51adbe9d8c |
| rrf | top-10 | 0.2000 | 0.6667 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606 | a7762803-1bcc-572c-a37b-ff51adbe9d8c |
| rrf | top-20 | 0.1000 | 0.6667 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606 | a7762803-1bcc-572c-a37b-ff51adbe9d8c |
| rrf | top-30 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606, a7762803-1bcc-572c-a37b-ff51adbe9d8c | - |
| reranked | top-10 | 0.2000 | 0.6667 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606 | a7762803-1bcc-572c-a37b-ff51adbe9d8c |
| reranked | top-20 | 0.1000 | 0.6667 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606 | a7762803-1bcc-572c-a37b-ff51adbe9d8c |
| reranked | top-30 | 0.1000 | 1.0000 | f603bd9e-0235-5172-8fac-3797316a2d59, 628b3d7c-561b-5ffa-9423-7339f5a97606, a7762803-1bcc-572c-a37b-ff51adbe9d8c | - |

### security-oauth-flows

Question: What OAuth token request flows are supported by OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 94b4f452-edee-57d5-8300-0e0274173d7a | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e, 123541f6-5c09-5a02-8b7e-717606444523 |
| dense | top-20 | 0.1000 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| dense | top-30 | 0.0667 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| sparse | top-10 | 0.2000 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| sparse | top-20 | 0.1000 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| sparse | top-30 | 0.0667 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| rrf | top-10 | 0.2000 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| rrf | top-20 | 0.1000 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| rrf | top-30 | 0.0667 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| reranked | top-10 | 0.1000 | 0.3333 | 94b4f452-edee-57d5-8300-0e0274173d7a | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e, 123541f6-5c09-5a02-8b7e-717606444523 |
| reranked | top-20 | 0.1000 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |
| reranked | top-30 | 0.0667 | 0.6667 | 94b4f452-edee-57d5-8300-0e0274173d7a, 123541f6-5c09-5a02-8b7e-717606444523 | 5462fb43-d08a-57b4-87fc-e1f1436e5a5e |

### operators-overview

Question: What are Operators in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6, 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| dense | top-20 | 0.0000 | 0.0000 | - | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6, 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| dense | top-30 | 0.0333 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| sparse | top-10 | 0.1000 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| sparse | top-20 | 0.0500 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| sparse | top-30 | 0.0333 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| rrf | top-10 | 0.1000 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| rrf | top-20 | 0.0500 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| rrf | top-30 | 0.0333 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| reranked | top-10 | 0.1000 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| reranked | top-20 | 0.0500 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |
| reranked | top-30 | 0.0333 | 0.3333 | 8f3e0dd0-fb00-5e6d-ae95-91b41ea6fad6 | 0ae04d91-6119-51ec-b106-7e81343042f8, 6bb68fb5-8597-5ea7-a541-fbd11c57abf6 |

### operators-packaging

Question: What is the Operator Framework packaging format?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| dense | top-20 | 0.1000 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| dense | top-30 | 0.0667 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| sparse | top-10 | 0.2000 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| sparse | top-20 | 0.1000 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| sparse | top-30 | 0.0667 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| rrf | top-10 | 0.2000 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| rrf | top-20 | 0.1000 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| rrf | top-30 | 0.0667 | 0.6667 | a7e2bc8e-378c-5ca0-b119-2d39211b28e3, 7016589d-b32d-5275-b822-c584f6a8b608 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| reranked | top-10 | 0.2000 | 0.6667 | 7016589d-b32d-5275-b822-c584f6a8b608, a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| reranked | top-20 | 0.1000 | 0.6667 | 7016589d-b32d-5275-b822-c584f6a8b608, a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |
| reranked | top-30 | 0.0667 | 0.6667 | 7016589d-b32d-5275-b822-c584f6a8b608, a7e2bc8e-378c-5ca0-b119-2d39211b28e3 | 0e4c3171-bb23-5619-afeb-37bb1de2f2e4 |

### operators-olm

Question: What is Operator Lifecycle Manager?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | d593c934-a567-594c-b380-da8a9681a07e | a210b360-760e-50bf-87df-2eb06ba2e649, 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 |
| dense | top-20 | 0.0500 | 0.3333 | d593c934-a567-594c-b380-da8a9681a07e | a210b360-760e-50bf-87df-2eb06ba2e649, 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 |
| dense | top-30 | 0.0667 | 0.6667 | d593c934-a567-594c-b380-da8a9681a07e, 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | a210b360-760e-50bf-87df-2eb06ba2e649 |
| sparse | top-10 | 0.1000 | 0.3333 | 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | d593c934-a567-594c-b380-da8a9681a07e, a210b360-760e-50bf-87df-2eb06ba2e649 |
| sparse | top-20 | 0.1000 | 0.6667 | 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26, d593c934-a567-594c-b380-da8a9681a07e | a210b360-760e-50bf-87df-2eb06ba2e649 |
| sparse | top-30 | 0.0667 | 0.6667 | 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26, d593c934-a567-594c-b380-da8a9681a07e | a210b360-760e-50bf-87df-2eb06ba2e649 |
| rrf | top-10 | 0.2000 | 0.6667 | d593c934-a567-594c-b380-da8a9681a07e, 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | a210b360-760e-50bf-87df-2eb06ba2e649 |
| rrf | top-20 | 0.1000 | 0.6667 | d593c934-a567-594c-b380-da8a9681a07e, 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | a210b360-760e-50bf-87df-2eb06ba2e649 |
| rrf | top-30 | 0.0667 | 0.6667 | d593c934-a567-594c-b380-da8a9681a07e, 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | a210b360-760e-50bf-87df-2eb06ba2e649 |
| reranked | top-10 | 0.1000 | 0.3333 | 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | d593c934-a567-594c-b380-da8a9681a07e, a210b360-760e-50bf-87df-2eb06ba2e649 |
| reranked | top-20 | 0.0500 | 0.3333 | 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26 | d593c934-a567-594c-b380-da8a9681a07e, a210b360-760e-50bf-87df-2eb06ba2e649 |
| reranked | top-30 | 0.0667 | 0.6667 | 04074cc9-fe3b-59cf-a9a9-44a7d7ce6b26, d593c934-a567-594c-b380-da8a9681a07e | a210b360-760e-50bf-87df-2eb06ba2e649 |

### operators-crds

Question: What are custom resource definitions for Operators?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| dense | top-20 | 0.1000 | 0.6667 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d, c49f1470-0af4-5242-9cdf-3fdf870e2d21 | 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| dense | top-30 | 0.0667 | 0.6667 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d, c49f1470-0af4-5242-9cdf-3fdf870e2d21 | 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| sparse | top-10 | 0.1000 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| sparse | top-20 | 0.0500 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| sparse | top-30 | 0.0333 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| rrf | top-10 | 0.1000 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| rrf | top-20 | 0.0500 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| rrf | top-30 | 0.0667 | 0.6667 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d, c49f1470-0af4-5242-9cdf-3fdf870e2d21 | 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| reranked | top-10 | 0.1000 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| reranked | top-20 | 0.0500 | 0.3333 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d | c49f1470-0af4-5242-9cdf-3fdf870e2d21, 157e2f95-dc19-54b3-98ca-4d8b8e396891 |
| reranked | top-30 | 0.0667 | 0.6667 | 0951f16b-9db3-5bbf-bd72-f2f586d50e2d, c49f1470-0af4-5242-9cdf-3fdf870e2d21 | 157e2f95-dc19-54b3-98ca-4d8b8e396891 |

### operators-install-namespace

Question: How do I install an Operator in a namespace?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| dense | top-20 | 0.1000 | 0.6667 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab, f3d4a856-baf0-5163-97c6-020eb5f2af20 | d7e76c62-e2e9-50bd-9932-670bd8724c3b |
| dense | top-30 | 0.0667 | 0.6667 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab, f3d4a856-baf0-5163-97c6-020eb5f2af20 | d7e76c62-e2e9-50bd-9932-670bd8724c3b |
| sparse | top-10 | 0.1000 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| sparse | top-20 | 0.0500 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| sparse | top-30 | 0.0333 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| rrf | top-10 | 0.1000 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| rrf | top-20 | 0.0500 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| rrf | top-30 | 0.0667 | 0.6667 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab, f3d4a856-baf0-5163-97c6-020eb5f2af20 | d7e76c62-e2e9-50bd-9932-670bd8724c3b |
| reranked | top-10 | 0.0000 | 0.0000 | - | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab, d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| reranked | top-20 | 0.0500 | 0.3333 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab | d7e76c62-e2e9-50bd-9932-670bd8724c3b, f3d4a856-baf0-5163-97c6-020eb5f2af20 |
| reranked | top-30 | 0.0667 | 0.6667 | 83e1389c-3e95-5ec5-9182-a5e575b0e8ab, f3d4a856-baf0-5163-97c6-020eb5f2af20 | d7e76c62-e2e9-50bd-9932-670bd8724c3b |

### observability-monitoring

Question: What monitoring is provided by OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | f321f5cc-cbff-5600-b83f-f4899ec73083 | 16289132-d267-551c-91d1-e388cbe1ce32, 34a9330f-3546-5170-b523-f0bc38431851 |
| dense | top-20 | 0.1000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| dense | top-30 | 0.0667 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| sparse | top-10 | 0.1000 | 0.3333 | f321f5cc-cbff-5600-b83f-f4899ec73083 | 16289132-d267-551c-91d1-e388cbe1ce32, 34a9330f-3546-5170-b523-f0bc38431851 |
| sparse | top-20 | 0.0500 | 0.3333 | f321f5cc-cbff-5600-b83f-f4899ec73083 | 16289132-d267-551c-91d1-e388cbe1ce32, 34a9330f-3546-5170-b523-f0bc38431851 |
| sparse | top-30 | 0.0667 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| rrf | top-10 | 0.2000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| rrf | top-20 | 0.1000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| rrf | top-30 | 0.0667 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| reranked | top-10 | 0.2000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| reranked | top-20 | 0.1000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |
| reranked | top-30 | 0.0667 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 34a9330f-3546-5170-b523-f0bc38431851 |

### observability-logging

Question: What logging capabilities are available in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| dense | top-20 | 0.1000 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| dense | top-30 | 0.0667 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 4c532e18-b67c-5359-b034-a0907cd874a5, 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| sparse | top-20 | 0.0500 | 0.3333 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 4c532e18-b67c-5359-b034-a0907cd874a5, 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| sparse | top-30 | 0.0667 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| rrf | top-10 | 0.2000 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| rrf | top-20 | 0.1000 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| rrf | top-30 | 0.0667 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| reranked | top-10 | 0.2000 | 0.6667 | 4c532e18-b67c-5359-b034-a0907cd874a5, 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| reranked | top-20 | 0.1000 | 0.6667 | 4c532e18-b67c-5359-b034-a0907cd874a5, 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |
| reranked | top-30 | 0.0667 | 0.6667 | 4c532e18-b67c-5359-b034-a0907cd874a5, 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 2fc33bf2-d58f-5259-8c60-baafb8a68b11 |

### backup-control-plane

Question: How do control plane backup and restore operations work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| dense | top-20 | 0.0500 | 0.3333 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| dense | top-30 | 0.0667 | 0.6667 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 987380f9-f164-5728-9141-559790cb7069 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee |
| sparse | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| rrf | top-20 | 0.0500 | 0.3333 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| rrf | top-30 | 0.0333 | 0.3333 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| reranked | top-20 | 0.0500 | 0.3333 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |
| reranked | top-30 | 0.0333 | 0.3333 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, 987380f9-f164-5728-9141-559790cb7069 |

### backup-application

Question: How do application backup and restore operations work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| dense | top-20 | 0.0500 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| dense | top-30 | 0.0333 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6e591022-a8eb-596a-ab66-472d3f608957, 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| sparse | top-20 | 0.0500 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| sparse | top-30 | 0.0333 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| rrf | top-10 | 0.1000 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| rrf | top-20 | 0.0500 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| rrf | top-30 | 0.0333 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| reranked | top-10 | 0.1000 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| reranked | top-20 | 0.0500 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |
| reranked | top-30 | 0.0333 | 0.3333 | 6e591022-a8eb-596a-ab66-472d3f608957 | 7a61f3a4-42cc-5488-a4bb-09759dc087ee, b5311075-117e-5937-aea4-ae221661cf23 |

### backup-graceful-shutdown

Question: How do I shut down an OpenShift cluster gracefully?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| dense | top-20 | 0.1000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| dense | top-30 | 0.0667 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| sparse | top-10 | 0.2000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| sparse | top-20 | 0.1000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| sparse | top-30 | 0.0667 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| rrf | top-10 | 0.2000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| rrf | top-20 | 0.1000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| rrf | top-30 | 0.0667 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| reranked | top-10 | 0.2000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| reranked | top-20 | 0.1000 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |
| reranked | top-30 | 0.0667 | 0.6667 | e0986463-9433-51da-8f1e-d7939d201e95, b64f610a-7cef-5944-8e18-e72beb2abb51 | c3ba101f-39c4-567d-9938-00ab0dae2759 |

### backup-oadp

Question: What is OpenShift API for Data Protection (OADP)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |
| dense | top-20 | 0.1000 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |
| dense | top-30 | 0.0667 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |
| sparse | top-10 | 0.1000 | 0.3333 | eefde02b-0d2f-563a-995c-20564bda99d5 | 72f43458-4b8e-5de6-8885-61a543c652ad, f9ad5050-38cd-567b-8862-e070c563504e |
| sparse | top-20 | 0.0500 | 0.3333 | eefde02b-0d2f-563a-995c-20564bda99d5 | 72f43458-4b8e-5de6-8885-61a543c652ad, f9ad5050-38cd-567b-8862-e070c563504e |
| sparse | top-30 | 0.0333 | 0.3333 | eefde02b-0d2f-563a-995c-20564bda99d5 | 72f43458-4b8e-5de6-8885-61a543c652ad, f9ad5050-38cd-567b-8862-e070c563504e |
| rrf | top-10 | 0.1000 | 0.3333 | eefde02b-0d2f-563a-995c-20564bda99d5 | 72f43458-4b8e-5de6-8885-61a543c652ad, f9ad5050-38cd-567b-8862-e070c563504e |
| rrf | top-20 | 0.0500 | 0.3333 | eefde02b-0d2f-563a-995c-20564bda99d5 | 72f43458-4b8e-5de6-8885-61a543c652ad, f9ad5050-38cd-567b-8862-e070c563504e |
| rrf | top-30 | 0.0667 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |
| reranked | top-10 | 0.2000 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |
| reranked | top-20 | 0.1000 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |
| reranked | top-30 | 0.0667 | 0.6667 | eefde02b-0d2f-563a-995c-20564bda99d5, f9ad5050-38cd-567b-8862-e070c563504e | 72f43458-4b8e-5de6-8885-61a543c652ad |

### updates-mechanics

Question: How do OpenShift cluster updates work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b, 7e1f2517-f119-50d0-9991-4913eee2703b |
| dense | top-20 | 0.0500 | 0.3333 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b, 7e1f2517-f119-50d0-9991-4913eee2703b |
| dense | top-30 | 0.0667 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, 7e1f2517-f119-50d0-9991-4913eee2703b | f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b |
| sparse | top-10 | 0.1000 | 0.3333 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b, 7e1f2517-f119-50d0-9991-4913eee2703b |
| sparse | top-20 | 0.1000 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b | 7e1f2517-f119-50d0-9991-4913eee2703b |
| sparse | top-30 | 0.0667 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b | 7e1f2517-f119-50d0-9991-4913eee2703b |
| rrf | top-10 | 0.1000 | 0.3333 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b, 7e1f2517-f119-50d0-9991-4913eee2703b |
| rrf | top-20 | 0.1000 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b | 7e1f2517-f119-50d0-9991-4913eee2703b |
| rrf | top-30 | 0.0667 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b | 7e1f2517-f119-50d0-9991-4913eee2703b |
| reranked | top-10 | 0.1000 | 0.3333 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633 | f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b, 7e1f2517-f119-50d0-9991-4913eee2703b |
| reranked | top-20 | 0.1000 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b | 7e1f2517-f119-50d0-9991-4913eee2703b |
| reranked | top-30 | 0.0667 | 0.6667 | 1b6085a5-47d1-5156-8f3f-6d566f1e9633, f8d9c3e2-aee2-5d0d-84d6-e1f2ee27540b | 7e1f2517-f119-50d0-9991-4913eee2703b |

### updates-channels

Question: How do OpenShift update channels and releases work?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| dense | top-20 | 0.1000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| dense | top-30 | 0.0667 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| sparse | top-10 | 0.2000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| sparse | top-20 | 0.1000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| sparse | top-30 | 0.0667 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| rrf | top-10 | 0.2000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| rrf | top-20 | 0.1000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| rrf | top-30 | 0.0667 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| reranked | top-10 | 0.2000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| reranked | top-20 | 0.1000 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |
| reranked | top-30 | 0.0667 | 0.6667 | b6bae24f-cff4-5f0e-8249-a6b115b56724, 5e7dd74c-3ec6-54d8-a8ba-f02118a9fe51 | 5807161a-8430-50e8-9d0a-62580dee08bf |

### updates-prepare-422

Question: How do I prepare a cluster to update to OpenShift 4.22?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| dense | top-20 | 0.0500 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| dense | top-30 | 0.0333 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| sparse | top-10 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6, 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| sparse | top-20 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6, 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| sparse | top-30 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6, 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| rrf | top-10 | 0.1000 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| rrf | top-20 | 0.0500 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| rrf | top-30 | 0.0333 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| reranked | top-10 | 0.0000 | 0.0000 | - | 0fc41488-7116-5d00-a951-27b610354fa6, 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| reranked | top-20 | 0.0500 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |
| reranked | top-30 | 0.0333 | 0.3333 | 0fc41488-7116-5d00-a951-27b610354fa6 | 1c495ea0-0e46-5c19-9b99-3c6bbf079abe, 54afe987-7c00-559f-89c2-9e750a936dba |

### updates-cli

Question: How do I update an OpenShift cluster using the CLI?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c |
| dense | top-20 | 0.0500 | 0.3333 | 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c |
| dense | top-30 | 0.0333 | 0.3333 | 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6c6d609e-b380-5b0a-b640-640817748a47, 5be688d4-e80b-552e-87aa-bd9948c11f73, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c |
| sparse | top-20 | 0.0500 | 0.3333 | c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c | 6c6d609e-b380-5b0a-b640-640817748a47, 5be688d4-e80b-552e-87aa-bd9948c11f73 |
| sparse | top-30 | 0.0333 | 0.3333 | c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c | 6c6d609e-b380-5b0a-b640-640817748a47, 5be688d4-e80b-552e-87aa-bd9948c11f73 |
| rrf | top-10 | 0.1000 | 0.3333 | 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c |
| rrf | top-20 | 0.0500 | 0.3333 | 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c |
| rrf | top-30 | 0.0667 | 0.6667 | 6c6d609e-b380-5b0a-b640-640817748a47, c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c | 5be688d4-e80b-552e-87aa-bd9948c11f73 |
| reranked | top-10 | 0.2000 | 0.6667 | c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c, 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73 |
| reranked | top-20 | 0.1000 | 0.6667 | c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c, 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73 |
| reranked | top-30 | 0.0667 | 0.6667 | c2d36a1e-8db4-5edd-99b4-23b9f3f5ff5c, 6c6d609e-b380-5b0a-b640-640817748a47 | 5be688d4-e80b-552e-87aa-bd9948c11f73 |

### updates-disconnected

Question: How do I update an OpenShift cluster in a disconnected environment?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| dense | top-20 | 0.0500 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| dense | top-30 | 0.0333 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| sparse | top-10 | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76, 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| sparse | top-20 | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76, 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| sparse | top-30 | 0.0333 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| rrf | top-10 | 0.1000 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| rrf | top-20 | 0.0500 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| rrf | top-30 | 0.0333 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| reranked | top-10 | 0.0000 | 0.0000 | - | aebe89fe-63b9-5ce6-857c-c3a05365ff76, 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| reranked | top-20 | 0.0500 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |
| reranked | top-30 | 0.0333 | 0.3333 | aebe89fe-63b9-5ce6-857c-c3a05365ff76 | 964b9d85-bef1-5e90-bd5a-5950f5388b03, d9a345d3-eed8-5041-990e-ffc783cd3736 |

### machines-machine-api

Question: What is the Machine API in OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| dense | top-20 | 0.0500 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| dense | top-30 | 0.0333 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| sparse | top-10 | 0.1000 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| sparse | top-20 | 0.0500 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| sparse | top-30 | 0.0333 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| rrf | top-10 | 0.1000 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| rrf | top-20 | 0.0500 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| rrf | top-30 | 0.0333 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| reranked | top-10 | 0.1000 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| reranked | top-20 | 0.0500 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |
| reranked | top-30 | 0.0333 | 0.3333 | ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | b782a494-2be3-538e-b5a2-d2a1ce85d0e7, dd8f0f15-285e-5b7f-b51a-8b5e1d7da586 |

### machines-autoscaling

Question: How does cluster autoscaling work for OpenShift machines?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| dense | top-20 | 0.0500 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| dense | top-30 | 0.0333 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| sparse | top-10 | 0.1000 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| sparse | top-20 | 0.0500 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| sparse | top-30 | 0.0333 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| rrf | top-10 | 0.1000 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| rrf | top-20 | 0.0500 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| rrf | top-30 | 0.0333 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| reranked | top-10 | 0.1000 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| reranked | top-20 | 0.0500 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| reranked | top-30 | 0.0333 | 0.3333 | 20755582-df24-52ee-85c8-309d77cdfad4 | 6c5beadf-e69b-53cf-a70a-1ba7ef018c9d, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |

### machineset-aws

Question: How do I create a compute MachineSet on AWS?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| dense | top-20 | 0.0500 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| dense | top-30 | 0.0333 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f, 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f, 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f, 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| rrf | top-10 | 0.1000 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| rrf | top-20 | 0.0500 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| rrf | top-30 | 0.0333 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| reranked | top-10 | 0.1000 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| reranked | top-20 | 0.0500 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |
| reranked | top-30 | 0.0333 | 0.3333 | 6dd30eb2-e5f0-5762-82ab-e74de5c5d88f | 295bc48b-c6a5-5344-8a73-abd813f1e0dd, ff6d762b-c397-5b6a-927b-cf56a6277ae0 |

### machineset-vsphere

Question: How do I create a compute MachineSet on vSphere?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| dense | top-20 | 0.0500 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| dense | top-30 | 0.0333 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| sparse | top-10 | 0.1000 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| sparse | top-20 | 0.0500 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| sparse | top-30 | 0.0333 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| rrf | top-10 | 0.1000 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| rrf | top-20 | 0.0500 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| rrf | top-30 | 0.0333 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| reranked | top-10 | 0.1000 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| reranked | top-20 | 0.0500 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |
| reranked | top-30 | 0.0333 | 0.3333 | f12dc712-9366-511e-8546-c5a63c4fc1b1 | d98df362-9b23-508b-936f-be18d28911f3, 5243b310-1387-5974-a704-e2d42eda2f40 |

### workloads-buildconfig

Question: What is the BuildConfig workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| dense | top-20 | 0.0500 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| dense | top-30 | 0.0333 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| sparse | top-10 | 0.1000 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| sparse | top-20 | 0.0500 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| sparse | top-30 | 0.0667 | 0.6667 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc, 349797a4-9fc0-5591-91bf-abfe954f3860 | 84d857a3-f479-5659-b293-ccaa2ea258c0 |
| rrf | top-10 | 0.1000 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| rrf | top-20 | 0.0500 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| rrf | top-30 | 0.0333 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| reranked | top-10 | 0.1000 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| reranked | top-20 | 0.0500 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |
| reranked | top-30 | 0.0333 | 0.3333 | 578db6bc-f6df-539d-b7bb-1abb22c4abfc | 84d857a3-f479-5659-b293-ccaa2ea258c0, 349797a4-9fc0-5591-91bf-abfe954f3860 |

### workloads-cronjob

Question: What is the CronJob workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| dense | top-20 | 0.0500 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| dense | top-30 | 0.0333 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| sparse | top-10 | 0.1000 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| sparse | top-20 | 0.0500 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| sparse | top-30 | 0.0333 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| rrf | top-10 | 0.1000 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| rrf | top-20 | 0.0500 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| rrf | top-30 | 0.0333 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 8b0c5464-b271-522e-9e44-32032ec320ef, bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| reranked | top-20 | 0.0500 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| reranked | top-30 | 0.0333 | 0.3333 | 8b0c5464-b271-522e-9e44-32032ec320ef | bceaf071-855c-5ba3-99d1-bd87e1662510, 334dcb95-a5e1-5193-8211-d614fff108d2 |

### workloads-deployment

Question: What is the Deployment workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| dense | top-20 | 0.0500 | 0.3333 | c4a22229-e95a-5ac7-85c4-2651b543bacc | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| dense | top-30 | 0.0333 | 0.3333 | c4a22229-e95a-5ac7-85c4-2651b543bacc | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| sparse | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| sparse | top-30 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| rrf | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| rrf | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| rrf | top-30 | 0.0333 | 0.3333 | c4a22229-e95a-5ac7-85c4-2651b543bacc | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| reranked | top-20 | 0.0000 | 0.0000 | - | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2, c4a22229-e95a-5ac7-85c4-2651b543bacc |
| reranked | top-30 | 0.0333 | 0.3333 | c4a22229-e95a-5ac7-85c4-2651b543bacc | 39c6bbb9-de1f-57d0-b08f-81a9ab83e87f, 334dcb95-a5e1-5193-8211-d614fff108d2 |

### workloads-pod

Question: What is the Pod workload API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 6986ef3f-df3e-554b-960e-8287587551b1 | 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| dense | top-20 | 0.0500 | 0.3333 | 6986ef3f-df3e-554b-960e-8287587551b1 | 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| dense | top-30 | 0.0333 | 0.3333 | 6986ef3f-df3e-554b-960e-8287587551b1 | 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1, 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1, 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| sparse | top-30 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1, 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| rrf | top-10 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1, 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| rrf | top-20 | 0.0500 | 0.3333 | 6986ef3f-df3e-554b-960e-8287587551b1 | 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| rrf | top-30 | 0.0333 | 0.3333 | 6986ef3f-df3e-554b-960e-8287587551b1 | 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| reranked | top-10 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1, 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| reranked | top-20 | 0.0000 | 0.0000 | - | 6986ef3f-df3e-554b-960e-8287587551b1, 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |
| reranked | top-30 | 0.0333 | 0.3333 | 6986ef3f-df3e-554b-960e-8287587551b1 | 77b533f5-1eb8-5cf0-afc0-8d2368c0b917, eb79e80a-2055-5694-a715-1893d3eaddbc |

### ingress-basic-route

Question: How do I create a basic OpenShift route?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| dense | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| dense | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| sparse | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| sparse | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| sparse | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| rrf | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| rrf | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| rrf | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| reranked | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| reranked | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |
| reranked | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | 9c12f617-eb4d-53eb-9566-20d859a99cd8, aeb316dd-8324-5466-96e7-b50216f67eba |

### ingress-secure-route

Question: How do I secure an OpenShift route?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| dense | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| dense | top-30 | 0.0333 | 0.3333 | 9e3d817c-a593-518e-8a11-f5af50b4316f | 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 9e3d817c-a593-518e-8a11-f5af50b4316f, 850a18f1-1793-569d-8ea9-bec906bd3c2a, 60370dab-50a7-5bf7-ba64-644cdd3142a1 |

### ingress-external-ip

Question: How do I configure ExternalIPs for services?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833 | 9a63f960-34a7-5c67-85a4-271010d30564 |
| dense | top-20 | 0.1500 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 9a63f960-34a7-5c67-85a4-271010d30564 | - |
| dense | top-30 | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 9a63f960-34a7-5c67-85a4-271010d30564 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833 | 9a63f960-34a7-5c67-85a4-271010d30564 |
| sparse | top-20 | 0.1000 | 0.6667 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833 | 9a63f960-34a7-5c67-85a4-271010d30564 |
| sparse | top-30 | 0.0667 | 0.6667 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833 | 9a63f960-34a7-5c67-85a4-271010d30564 |
| rrf | top-10 | 0.2000 | 0.6667 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833 | 9a63f960-34a7-5c67-85a4-271010d30564 |
| rrf | top-20 | 0.1500 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 9a63f960-34a7-5c67-85a4-271010d30564 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 56393362-3718-563c-b0d1-362184d80e4b, 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 9a63f960-34a7-5c67-85a4-271010d30564 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 56393362-3718-563c-b0d1-362184d80e4b | 9a63f960-34a7-5c67-85a4-271010d30564 |
| reranked | top-20 | 0.1500 | 1.0000 | 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 56393362-3718-563c-b0d1-362184d80e4b, 9a63f960-34a7-5c67-85a4-271010d30564 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 8a7c92dd-ae37-51b4-8152-8d0f5e54e833, 56393362-3718-563c-b0d1-362184d80e4b, 9a63f960-34a7-5c67-85a4-271010d30564 | - |

### ingress-endpoint-strategy

Question: What Ingress Controller endpoint publishing strategies are available?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | f98209c8-9f55-532e-b621-e251ba433bb4, 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b | fd3a5345-414d-5840-a636-b33f15a43554 |
| dense | top-20 | 0.1000 | 0.6667 | f98209c8-9f55-532e-b621-e251ba433bb4, 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b | fd3a5345-414d-5840-a636-b33f15a43554 |
| dense | top-30 | 0.0667 | 0.6667 | f98209c8-9f55-532e-b621-e251ba433bb4, 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b | fd3a5345-414d-5840-a636-b33f15a43554 |
| sparse | top-10 | 0.2000 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| sparse | top-20 | 0.1000 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| sparse | top-30 | 0.0667 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| rrf | top-10 | 0.2000 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| rrf | top-20 | 0.1000 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| rrf | top-30 | 0.0667 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| reranked | top-10 | 0.2000 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| reranked | top-20 | 0.1000 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |
| reranked | top-30 | 0.0667 | 0.6667 | 19d12d86-d2e4-5ac0-9ae3-d8586beb6f2b, f98209c8-9f55-532e-b621-e251ba433bb4 | fd3a5345-414d-5840-a636-b33f15a43554 |

### corpus-advanced-networking-2

Question: How does OpenShift Container Platform document Specialized and advanced networking topics in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| dense | top-20 | 0.1000 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| dense | top-30 | 0.0667 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| sparse | top-10 | 0.1000 | 0.3333 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | 35903da6-dfce-5e52-b47d-6f614c4b4a40, 65b49d58-d7d6-52ff-acf0-481a962af645 |
| sparse | top-20 | 0.0500 | 0.3333 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | 35903da6-dfce-5e52-b47d-6f614c4b4a40, 65b49d58-d7d6-52ff-acf0-481a962af645 |
| sparse | top-30 | 0.0333 | 0.3333 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | 35903da6-dfce-5e52-b47d-6f614c4b4a40, 65b49d58-d7d6-52ff-acf0-481a962af645 |
| rrf | top-10 | 0.1000 | 0.3333 | 6d4c9a01-183d-5830-9f41-8f89f39755c9 | 35903da6-dfce-5e52-b47d-6f614c4b4a40, 65b49d58-d7d6-52ff-acf0-481a962af645 |
| rrf | top-20 | 0.1000 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| rrf | top-30 | 0.0667 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| reranked | top-10 | 0.2000 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| reranked | top-20 | 0.1000 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |
| reranked | top-30 | 0.0667 | 0.6667 | 6d4c9a01-183d-5830-9f41-8f89f39755c9, 35903da6-dfce-5e52-b47d-6f614c4b4a40 | 65b49d58-d7d6-52ff-acf0-481a962af645 |

### corpus-ai-applications-2

Question: How does OpenShift Container Platform document Using AI applications on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 0bf616bf-8839-5e90-8f9f-50547d7e82cc, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| dense | top-20 | 0.1000 | 0.6667 | 0bf616bf-8839-5e90-8f9f-50547d7e82cc, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| dense | top-30 | 0.0667 | 0.6667 | 0bf616bf-8839-5e90-8f9f-50547d7e82cc, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| sparse | top-10 | 0.1000 | 0.3333 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 0bf616bf-8839-5e90-8f9f-50547d7e82cc, c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| sparse | top-20 | 0.0500 | 0.3333 | e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 0bf616bf-8839-5e90-8f9f-50547d7e82cc, c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| sparse | top-30 | 0.0667 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| rrf | top-10 | 0.2000 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| rrf | top-20 | 0.1000 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| rrf | top-30 | 0.0667 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| reranked | top-10 | 0.2000 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| reranked | top-20 | 0.1000 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |
| reranked | top-30 | 0.0667 | 0.6667 | e726cde9-bf0d-5424-a75d-b17f6c9455a6, 0bf616bf-8839-5e90-8f9f-50547d7e82cc | c0c06e55-c972-5a13-8aab-c2f87a25ec8e |

### corpus-ai-workloads-2

Question: How does OpenShift Container Platform document Running AI workloads on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| dense | top-20 | 0.1500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| dense | top-30 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| sparse | top-10 | 0.2000 | 0.6667 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0 | 182724d3-a956-5535-acd0-c4ebdb9a455c |
| sparse | top-20 | 0.1500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| sparse | top-30 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| rrf | top-10 | 0.3000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| rrf | top-20 | 0.1500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| rrf | top-30 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| reranked | top-10 | 0.3000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| reranked | top-20 | 0.1500 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |
| reranked | top-30 | 0.1000 | 1.0000 | a797913b-3012-57a6-9136-972bda3f2183, 71d01548-21e2-522b-9121-1db05498f0d0, 182724d3-a956-5535-acd0-c4ebdb9a455c | - |

### corpus-api-overview-2

Question: How does OpenShift Container Platform document Overview content for the OpenShift Container Platform API?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| dense | top-20 | 0.1000 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| dense | top-30 | 0.0667 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| sparse | top-10 | 0.1000 | 0.3333 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | 6f342bd0-6a66-5c54-ac0b-b850e546a388, d144675a-71c4-573f-8cbf-a04b2f5c633c |
| sparse | top-20 | 0.0500 | 0.3333 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | 6f342bd0-6a66-5c54-ac0b-b850e546a388, d144675a-71c4-573f-8cbf-a04b2f5c633c |
| sparse | top-30 | 0.0333 | 0.3333 | e76f21b1-6e59-5d76-8010-bd5e01e02c92 | 6f342bd0-6a66-5c54-ac0b-b850e546a388, d144675a-71c4-573f-8cbf-a04b2f5c633c |
| rrf | top-10 | 0.2000 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| rrf | top-20 | 0.1000 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| rrf | top-30 | 0.0667 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| reranked | top-10 | 0.2000 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| reranked | top-20 | 0.1000 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |
| reranked | top-30 | 0.0667 | 0.6667 | e76f21b1-6e59-5d76-8010-bd5e01e02c92, 6f342bd0-6a66-5c54-ac0b-b850e546a388 | d144675a-71c4-573f-8cbf-a04b2f5c633c |

### corpus-architecture-2

Question: How does OpenShift Container Platform document An overview of the architecture for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | b8506aee-e798-5c77-aa09-d51fd783d670 |
| dense | top-20 | 0.1000 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | b8506aee-e798-5c77-aa09-d51fd783d670 |
| dense | top-30 | 0.0667 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | b8506aee-e798-5c77-aa09-d51fd783d670 |
| sparse | top-10 | 0.2000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | b8506aee-e798-5c77-aa09-d51fd783d670 |
| sparse | top-20 | 0.1000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | b8506aee-e798-5c77-aa09-d51fd783d670 |
| sparse | top-30 | 0.0667 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | b8506aee-e798-5c77-aa09-d51fd783d670 |
| rrf | top-10 | 0.2000 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | b8506aee-e798-5c77-aa09-d51fd783d670 |
| rrf | top-20 | 0.1000 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | b8506aee-e798-5c77-aa09-d51fd783d670 |
| rrf | top-30 | 0.0667 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | b8506aee-e798-5c77-aa09-d51fd783d670 |
| reranked | top-10 | 0.2000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | b8506aee-e798-5c77-aa09-d51fd783d670 |
| reranked | top-20 | 0.1000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | b8506aee-e798-5c77-aa09-d51fd783d670 |
| reranked | top-30 | 0.0667 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | b8506aee-e798-5c77-aa09-d51fd783d670 |

### corpus-authentication-and-authorization-3

Question: How does OpenShift Container Platform document Chapter1.Overview of authentication and authorization?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| dense | top-20 | 0.1500 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca, d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| dense | top-30 | 0.1000 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca, d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| sparse | top-10 | 0.2000 | 0.6667 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| sparse | top-20 | 0.1000 | 0.6667 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| sparse | top-30 | 0.0667 | 0.6667 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| rrf | top-10 | 0.2000 | 0.6667 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| rrf | top-20 | 0.1000 | 0.6667 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| rrf | top-30 | 0.1000 | 1.0000 | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca, d5b1462c-148d-5455-96ac-4e1765cacf4a | - |
| reranked | top-10 | 0.1000 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 483b7b09-0a84-5b6b-90df-c3a43bed4e93, d5b1462c-148d-5455-96ac-4e1765cacf4a |
| reranked | top-20 | 0.1000 | 0.6667 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca, 483b7b09-0a84-5b6b-90df-c3a43bed4e93 | d5b1462c-148d-5455-96ac-4e1765cacf4a |
| reranked | top-30 | 0.1000 | 1.0000 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca, 483b7b09-0a84-5b6b-90df-c3a43bed4e93, d5b1462c-148d-5455-96ac-4e1765cacf4a | - |

### corpus-authorization-apis-2

Question: How does OpenShift Container Platform document Reference guide for authorization APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab | 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| dense | top-20 | 0.1000 | 0.6667 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab | 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| dense | top-30 | 0.0667 | 0.6667 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab | 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| sparse | top-10 | 0.1000 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| sparse | top-20 | 0.0500 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| sparse | top-30 | 0.0333 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| rrf | top-10 | 0.1000 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| rrf | top-20 | 0.0500 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| rrf | top-30 | 0.0667 | 0.6667 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab | 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| reranked | top-10 | 0.1000 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| reranked | top-20 | 0.0500 | 0.3333 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab, 4c15a7b6-b2f2-5163-941e-24d988f561e2 |
| reranked | top-30 | 0.0667 | 0.6667 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 7d1ae6a1-256d-5cdc-b83a-4deb0d1a93ab | 4c15a7b6-b2f2-5163-941e-24d988f561e2 |

### corpus-autoscale-apis-2

Question: How does OpenShift Container Platform document Reference guide for autoscale APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | a1b8eb78-2362-55b1-a776-eec474282f15, 4fc0cde5-9b35-52ac-aecc-dbb887c9715d | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| dense | top-20 | 0.1000 | 0.6667 | a1b8eb78-2362-55b1-a776-eec474282f15, 4fc0cde5-9b35-52ac-aecc-dbb887c9715d | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| dense | top-30 | 0.0667 | 0.6667 | a1b8eb78-2362-55b1-a776-eec474282f15, 4fc0cde5-9b35-52ac-aecc-dbb887c9715d | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| sparse | top-10 | 0.1000 | 0.3333 | a1b8eb78-2362-55b1-a776-eec474282f15 | 4fc0cde5-9b35-52ac-aecc-dbb887c9715d, 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| sparse | top-20 | 0.0500 | 0.3333 | a1b8eb78-2362-55b1-a776-eec474282f15 | 4fc0cde5-9b35-52ac-aecc-dbb887c9715d, 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| sparse | top-30 | 0.0333 | 0.3333 | a1b8eb78-2362-55b1-a776-eec474282f15 | 4fc0cde5-9b35-52ac-aecc-dbb887c9715d, 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| rrf | top-10 | 0.1000 | 0.3333 | a1b8eb78-2362-55b1-a776-eec474282f15 | 4fc0cde5-9b35-52ac-aecc-dbb887c9715d, 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| rrf | top-20 | 0.1000 | 0.6667 | a1b8eb78-2362-55b1-a776-eec474282f15, 4fc0cde5-9b35-52ac-aecc-dbb887c9715d | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| rrf | top-30 | 0.0667 | 0.6667 | a1b8eb78-2362-55b1-a776-eec474282f15, 4fc0cde5-9b35-52ac-aecc-dbb887c9715d | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| reranked | top-10 | 0.1000 | 0.3333 | a1b8eb78-2362-55b1-a776-eec474282f15 | 4fc0cde5-9b35-52ac-aecc-dbb887c9715d, 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| reranked | top-20 | 0.0500 | 0.3333 | a1b8eb78-2362-55b1-a776-eec474282f15 | 4fc0cde5-9b35-52ac-aecc-dbb887c9715d, 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |
| reranked | top-30 | 0.0667 | 0.6667 | a1b8eb78-2362-55b1-a776-eec474282f15, 4fc0cde5-9b35-52ac-aecc-dbb887c9715d | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 |

### corpus-backup-and-restore-2

Question: How does OpenShift Container Platform document Backing up and restoring your OpenShift Container Platform cluster?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |
| dense | top-20 | 0.1500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |
| dense | top-30 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |
| sparse | top-10 | 0.1000 | 0.3333 | c681963c-27bb-5e4f-8461-bb49c966506f | 507563fc-e28d-50cb-afb0-4abfcef279cb, 987380f9-f164-5728-9141-559790cb7069 |
| sparse | top-20 | 0.0500 | 0.3333 | c681963c-27bb-5e4f-8461-bb49c966506f | 507563fc-e28d-50cb-afb0-4abfcef279cb, 987380f9-f164-5728-9141-559790cb7069 |
| sparse | top-30 | 0.0333 | 0.3333 | c681963c-27bb-5e4f-8461-bb49c966506f | 507563fc-e28d-50cb-afb0-4abfcef279cb, 987380f9-f164-5728-9141-559790cb7069 |
| rrf | top-10 | 0.2000 | 0.6667 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069 | 507563fc-e28d-50cb-afb0-4abfcef279cb |
| rrf | top-20 | 0.1500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |
| rrf | top-30 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |
| reranked | top-10 | 0.1000 | 0.3333 | c681963c-27bb-5e4f-8461-bb49c966506f | 507563fc-e28d-50cb-afb0-4abfcef279cb, 987380f9-f164-5728-9141-559790cb7069 |
| reranked | top-20 | 0.1500 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |
| reranked | top-30 | 0.1000 | 1.0000 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069, 507563fc-e28d-50cb-afb0-4abfcef279cb | - |

### corpus-building-applications-2

Question: How does OpenShift Container Platform document Creating and managing applications on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| dense | top-20 | 0.1000 | 0.6667 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, cd7122bd-4861-5907-8a1b-a5f318b19d8f | b50e6b58-bc9d-56bc-8816-1f6cb913b390 |
| dense | top-30 | 0.0667 | 0.6667 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, cd7122bd-4861-5907-8a1b-a5f318b19d8f | b50e6b58-bc9d-56bc-8816-1f6cb913b390 |
| sparse | top-10 | 0.1000 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| sparse | top-20 | 0.0500 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| sparse | top-30 | 0.0333 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| rrf | top-10 | 0.1000 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| rrf | top-20 | 0.0500 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| rrf | top-30 | 0.0333 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| reranked | top-10 | 0.1000 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| reranked | top-20 | 0.0500 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |
| reranked | top-30 | 0.0333 | 0.3333 | 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b50e6b58-bc9d-56bc-8816-1f6cb913b390, cd7122bd-4861-5907-8a1b-a5f318b19d8f |

### corpus-builds-using-buildconfig-3

Question: How does OpenShift Container Platform document 1.1.Builds?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| dense | top-20 | 0.1000 | 0.6667 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f, 999cf49f-74d5-501d-8ee6-9f67af2f95ee | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313 |
| dense | top-30 | 0.0667 | 0.6667 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f, 999cf49f-74d5-501d-8ee6-9f67af2f95ee | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313 |
| sparse | top-10 | 0.1000 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| sparse | top-20 | 0.0500 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| sparse | top-30 | 0.0333 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| rrf | top-10 | 0.1000 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| rrf | top-20 | 0.0500 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| rrf | top-30 | 0.0333 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| reranked | top-10 | 0.1000 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| reranked | top-20 | 0.0500 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |
| reranked | top-30 | 0.0333 | 0.3333 | 01be7a1d-3fa7-537a-8cec-003a3d7c189f | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 999cf49f-74d5-501d-8ee6-9f67af2f95ee |

### corpus-builds-using-shipwright-2

Question: How does OpenShift Container Platform document An extensible build framework to build container images on an OpenShift cluster?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9, 0e53378e-3fa4-5aba-833a-809b7c5772da | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| dense | top-20 | 0.1000 | 0.6667 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9, 0e53378e-3fa4-5aba-833a-809b7c5772da | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| dense | top-30 | 0.0667 | 0.6667 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9, 0e53378e-3fa4-5aba-833a-809b7c5772da | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| sparse | top-10 | 0.2000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| sparse | top-20 | 0.1000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| sparse | top-30 | 0.0667 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| rrf | top-10 | 0.2000 | 0.6667 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9, 0e53378e-3fa4-5aba-833a-809b7c5772da | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| rrf | top-20 | 0.1000 | 0.6667 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9, 0e53378e-3fa4-5aba-833a-809b7c5772da | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| rrf | top-30 | 0.0667 | 0.6667 | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9, 0e53378e-3fa4-5aba-833a-809b7c5772da | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| reranked | top-10 | 0.2000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| reranked | top-20 | 0.1000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |
| reranked | top-30 | 0.0667 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 | 7f5d35e0-f16d-563e-9630-01a57eb7bdee |

### corpus-cicd-overview-2

Question: How does OpenShift Container Platform document Contains information about CI/CD for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4bd50d21-1ed2-5603-ba5f-d6e848828b40, 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| dense | top-20 | 0.1500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4bd50d21-1ed2-5603-ba5f-d6e848828b40, 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| dense | top-30 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4bd50d21-1ed2-5603-ba5f-d6e848828b40, 4551cb38-96c0-57de-8031-43f7b29a54e7 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | 4bd50d21-1ed2-5603-ba5f-d6e848828b40 |
| sparse | top-20 | 0.1000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | 4bd50d21-1ed2-5603-ba5f-d6e848828b40 |
| sparse | top-30 | 0.0667 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | 4bd50d21-1ed2-5603-ba5f-d6e848828b40 |
| rrf | top-10 | 0.3000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7, 4bd50d21-1ed2-5603-ba5f-d6e848828b40 | - |
| rrf | top-20 | 0.1500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7, 4bd50d21-1ed2-5603-ba5f-d6e848828b40 | - |
| rrf | top-30 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7, 4bd50d21-1ed2-5603-ba5f-d6e848828b40 | - |
| reranked | top-10 | 0.3000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7, 4bd50d21-1ed2-5603-ba5f-d6e848828b40 | - |
| reranked | top-20 | 0.1500 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7, 4bd50d21-1ed2-5603-ba5f-d6e848828b40 | - |
| reranked | top-30 | 0.1000 | 1.0000 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7, 4bd50d21-1ed2-5603-ba5f-d6e848828b40 | - |

### corpus-cli-tools-2

Question: How does OpenShift Container Platform document Learning how to use the command-line tools for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| dense | top-20 | 0.1000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| dense | top-30 | 0.1000 | 1.0000 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977, af68bc01-d35b-5a6a-9db2-9cd785d70a2b | - |
| sparse | top-10 | 0.2000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| sparse | top-20 | 0.1000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| sparse | top-30 | 0.0667 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| rrf | top-10 | 0.2000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| rrf | top-20 | 0.1000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| rrf | top-30 | 0.0667 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| reranked | top-10 | 0.2000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| reranked | top-20 | 0.1000 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |
| reranked | top-30 | 0.0667 | 0.6667 | 2b2b0165-aa9f-52a9-a006-92c1706043a0, 9cfedc56-d40b-5d64-b436-39dc7dbcb977 | af68bc01-d35b-5a6a-9db2-9cd785d70a2b |

### corpus-cluster-apis-2

Question: How does OpenShift Container Platform document Reference guide for cluster APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e6c41450-0fe1-5753-9fb5-c60da524ab45, 1d63300a-6ce8-5a3c-8217-d205df309041 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| dense | top-20 | 0.1000 | 0.6667 | e6c41450-0fe1-5753-9fb5-c60da524ab45, 1d63300a-6ce8-5a3c-8217-d205df309041 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| dense | top-30 | 0.0667 | 0.6667 | e6c41450-0fe1-5753-9fb5-c60da524ab45, 1d63300a-6ce8-5a3c-8217-d205df309041 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| sparse | top-10 | 0.1000 | 0.3333 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | 1d63300a-6ce8-5a3c-8217-d205df309041, 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| sparse | top-20 | 0.0500 | 0.3333 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | 1d63300a-6ce8-5a3c-8217-d205df309041, 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| sparse | top-30 | 0.0333 | 0.3333 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | 1d63300a-6ce8-5a3c-8217-d205df309041, 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| rrf | top-10 | 0.1000 | 0.3333 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | 1d63300a-6ce8-5a3c-8217-d205df309041, 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| rrf | top-20 | 0.1000 | 0.6667 | e6c41450-0fe1-5753-9fb5-c60da524ab45, 1d63300a-6ce8-5a3c-8217-d205df309041 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| rrf | top-30 | 0.0667 | 0.6667 | e6c41450-0fe1-5753-9fb5-c60da524ab45, 1d63300a-6ce8-5a3c-8217-d205df309041 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| reranked | top-10 | 0.1000 | 0.3333 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | 1d63300a-6ce8-5a3c-8217-d205df309041, 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| reranked | top-20 | 0.0500 | 0.3333 | e6c41450-0fe1-5753-9fb5-c60da524ab45 | 1d63300a-6ce8-5a3c-8217-d205df309041, 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |
| reranked | top-30 | 0.0667 | 0.6667 | e6c41450-0fe1-5753-9fb5-c60da524ab45, 1d63300a-6ce8-5a3c-8217-d205df309041 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 |

### corpus-cluster-observability-operator-2

Question: How does OpenShift Container Platform document Configuring and using the Cluster Observability Operator in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b, 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| dense | top-20 | 0.1500 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b, 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| dense | top-30 | 0.1000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b, 6f68f926-1ee0-509b-bef1-5b795511d222 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 0a0f1a14-fa69-5e90-8ee5-f60648751b6b |
| sparse | top-20 | 0.1000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 0a0f1a14-fa69-5e90-8ee5-f60648751b6b |
| sparse | top-30 | 0.0667 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 0a0f1a14-fa69-5e90-8ee5-f60648751b6b |
| rrf | top-10 | 0.2000 | 0.6667 | f1dec798-b76b-5158-95fe-8da4a66f6378, 6f68f926-1ee0-509b-bef1-5b795511d222 | 0a0f1a14-fa69-5e90-8ee5-f60648751b6b |
| rrf | top-20 | 0.1500 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378, 6f68f926-1ee0-509b-bef1-5b795511d222, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b | - |
| rrf | top-30 | 0.1000 | 1.0000 | f1dec798-b76b-5158-95fe-8da4a66f6378, 6f68f926-1ee0-509b-bef1-5b795511d222, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b | - |
| reranked | top-10 | 0.2000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 0a0f1a14-fa69-5e90-8ee5-f60648751b6b |
| reranked | top-20 | 0.1500 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b | - |
| reranked | top-30 | 0.1000 | 1.0000 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378, 0a0f1a14-fa69-5e90-8ee5-f60648751b6b | - |

### corpus-common-object-reference-2

Question: How does OpenShift Container Platform document Reference guide common API objects?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 86ba90a3-3c45-5acd-a02f-47a7d8c895e4 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| dense | top-20 | 0.1000 | 0.6667 | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 86ba90a3-3c45-5acd-a02f-47a7d8c895e4 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| dense | top-30 | 0.0667 | 0.6667 | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 86ba90a3-3c45-5acd-a02f-47a7d8c895e4 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| sparse | top-10 | 0.1000 | 0.3333 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | 86ba90a3-3c45-5acd-a02f-47a7d8c895e4, ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| sparse | top-20 | 0.0500 | 0.3333 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | 86ba90a3-3c45-5acd-a02f-47a7d8c895e4, ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| sparse | top-30 | 0.0333 | 0.3333 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | 86ba90a3-3c45-5acd-a02f-47a7d8c895e4, ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| rrf | top-10 | 0.1000 | 0.3333 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | 86ba90a3-3c45-5acd-a02f-47a7d8c895e4, ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| rrf | top-20 | 0.0500 | 0.3333 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | 86ba90a3-3c45-5acd-a02f-47a7d8c895e4, ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| rrf | top-30 | 0.0667 | 0.6667 | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 86ba90a3-3c45-5acd-a02f-47a7d8c895e4 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| reranked | top-10 | 0.1000 | 0.3333 | 63aec8a6-33ce-57c7-8afb-06b3c690600e | 86ba90a3-3c45-5acd-a02f-47a7d8c895e4, ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| reranked | top-20 | 0.1000 | 0.6667 | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 86ba90a3-3c45-5acd-a02f-47a7d8c895e4 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc |
| reranked | top-30 | 0.0667 | 0.6667 | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 86ba90a3-3c45-5acd-a02f-47a7d8c895e4 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc |

### corpus-config-apis-2

Question: How does OpenShift Container Platform document Reference guide for config APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e | fcae96e9-3a23-518d-b191-69ebf26ea43e |
| dense | top-20 | 0.1000 | 0.6667 | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e | fcae96e9-3a23-518d-b191-69ebf26ea43e |
| dense | top-30 | 0.0667 | 0.6667 | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e | fcae96e9-3a23-518d-b191-69ebf26ea43e |
| sparse | top-10 | 0.1000 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| sparse | top-20 | 0.0500 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| sparse | top-30 | 0.0333 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| rrf | top-10 | 0.1000 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| rrf | top-20 | 0.0500 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| rrf | top-30 | 0.0667 | 0.6667 | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e | fcae96e9-3a23-518d-b191-69ebf26ea43e |
| reranked | top-10 | 0.1000 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| reranked | top-20 | 0.0500 | 0.3333 | d1ae4432-c7b0-5506-9f50-c7c205b96dba | 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e, fcae96e9-3a23-518d-b191-69ebf26ea43e |
| reranked | top-30 | 0.0667 | 0.6667 | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 37c68e6b-ff22-5e29-be6c-7cdcdaf49c2e | fcae96e9-3a23-518d-b191-69ebf26ea43e |

### corpus-configuring-network-settings-2

Question: How does OpenShift Container Platform document General networking configuration processes in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| dense | top-20 | 0.1000 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| dense | top-30 | 0.0667 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| sparse | top-10 | 0.1000 | 0.3333 | f741081f-2b5f-54db-9d54-dfb08627f439 | ec4c0210-25d7-50f0-a169-6f8084d50a59, aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| sparse | top-20 | 0.0500 | 0.3333 | f741081f-2b5f-54db-9d54-dfb08627f439 | ec4c0210-25d7-50f0-a169-6f8084d50a59, aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| sparse | top-30 | 0.0333 | 0.3333 | f741081f-2b5f-54db-9d54-dfb08627f439 | ec4c0210-25d7-50f0-a169-6f8084d50a59, aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| rrf | top-10 | 0.1000 | 0.3333 | f741081f-2b5f-54db-9d54-dfb08627f439 | ec4c0210-25d7-50f0-a169-6f8084d50a59, aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| rrf | top-20 | 0.1000 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| rrf | top-30 | 0.0667 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| reranked | top-10 | 0.1000 | 0.3333 | f741081f-2b5f-54db-9d54-dfb08627f439 | ec4c0210-25d7-50f0-a169-6f8084d50a59, aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| reranked | top-20 | 0.1000 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |
| reranked | top-30 | 0.0667 | 0.6667 | f741081f-2b5f-54db-9d54-dfb08627f439, ec4c0210-25d7-50f0-a169-6f8084d50a59 | aea45e71-8964-5bc3-92e7-e6557d60dc8d |

### corpus-console-apis-2

Question: How does OpenShift Container Platform document Reference guide for console APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | d34a1045-05a4-510b-a425-080bc74f6631, 3ffbd292-14b3-53a5-9bc2-b0542347d889 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| dense | top-20 | 0.1000 | 0.6667 | d34a1045-05a4-510b-a425-080bc74f6631, 3ffbd292-14b3-53a5-9bc2-b0542347d889 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| dense | top-30 | 0.0667 | 0.6667 | d34a1045-05a4-510b-a425-080bc74f6631, 3ffbd292-14b3-53a5-9bc2-b0542347d889 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| sparse | top-10 | 0.1000 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| sparse | top-20 | 0.0500 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| sparse | top-30 | 0.0333 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| rrf | top-10 | 0.1000 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| rrf | top-20 | 0.0500 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| rrf | top-30 | 0.0667 | 0.6667 | d34a1045-05a4-510b-a425-080bc74f6631, 3ffbd292-14b3-53a5-9bc2-b0542347d889 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| reranked | top-10 | 0.1000 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| reranked | top-20 | 0.0500 | 0.3333 | d34a1045-05a4-510b-a425-080bc74f6631 | 3ffbd292-14b3-53a5-9bc2-b0542347d889, c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |
| reranked | top-30 | 0.0667 | 0.6667 | d34a1045-05a4-510b-a425-080bc74f6631, 3ffbd292-14b3-53a5-9bc2-b0542347d889 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 |

### corpus-disconnected-environments-2

Question: How does OpenShift Container Platform document Managing OpenShift Container Platform clusters in a disconnected environment?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69, 68515748-db0c-5456-9cf2-961351082f54 | - |
| dense | top-20 | 0.1500 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69, 68515748-db0c-5456-9cf2-961351082f54 | - |
| dense | top-30 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69, 68515748-db0c-5456-9cf2-961351082f54 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 68515748-db0c-5456-9cf2-961351082f54, 7e211c51-03f5-54f6-8607-ac63e70aabcf | 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 |
| sparse | top-20 | 0.1000 | 0.6667 | 68515748-db0c-5456-9cf2-961351082f54, 7e211c51-03f5-54f6-8607-ac63e70aabcf | 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 |
| sparse | top-30 | 0.0667 | 0.6667 | 68515748-db0c-5456-9cf2-961351082f54, 7e211c51-03f5-54f6-8607-ac63e70aabcf | 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 |
| rrf | top-10 | 0.3000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 68515748-db0c-5456-9cf2-961351082f54, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 68515748-db0c-5456-9cf2-961351082f54, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 68515748-db0c-5456-9cf2-961351082f54, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 68515748-db0c-5456-9cf2-961351082f54 | 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 |
| reranked | top-20 | 0.1000 | 0.6667 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 68515748-db0c-5456-9cf2-961351082f54 | 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 |
| reranked | top-30 | 0.1000 | 1.0000 | 7e211c51-03f5-54f6-8607-ac63e70aabcf, 68515748-db0c-5456-9cf2-961351082f54, 0fa77f6f-d7fc-5077-ae2d-80f6edb54e69 | - |

### corpus-distributed-tracing-2

Question: How does OpenShift Container Platform document Configuring and using distributed tracing in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| dense | top-20 | 0.1000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| dense | top-30 | 0.1000 | 1.0000 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 8da37ae7-1013-5b0f-ae45-6e805645052c | 27ded506-73eb-5808-ad9a-e2508009fafe, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| sparse | top-20 | 0.0500 | 0.3333 | 8da37ae7-1013-5b0f-ae45-6e805645052c | 27ded506-73eb-5808-ad9a-e2508009fafe, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| sparse | top-30 | 0.0333 | 0.3333 | 8da37ae7-1013-5b0f-ae45-6e805645052c | 27ded506-73eb-5808-ad9a-e2508009fafe, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| rrf | top-10 | 0.1000 | 0.3333 | 8da37ae7-1013-5b0f-ae45-6e805645052c | 27ded506-73eb-5808-ad9a-e2508009fafe, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| rrf | top-20 | 0.1000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| rrf | top-30 | 0.0667 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| reranked | top-10 | 0.2000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| reranked | top-20 | 0.1000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |
| reranked | top-30 | 0.0667 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 27ded506-73eb-5808-ad9a-e2508009fafe | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 |

### corpus-edge-computing-2

Question: How does OpenShift Container Platform document Configure and deploy OpenShift Container Platform clusters at the network edge?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| dense | top-20 | 0.0500 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| dense | top-30 | 0.0333 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-10 | 0.1000 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-20 | 0.0500 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-30 | 0.0333 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-10 | 0.1000 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-20 | 0.0500 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-30 | 0.0333 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-10 | 0.1000 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-20 | 0.0500 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-30 | 0.0333 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 087a52dc-5677-59b1-a18a-2f74d6839b40, 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |

### corpus-etcd-2

Question: How does OpenShift Container Platform document Providing redundancy with etcd?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, a36589f2-de69-5cdc-abe0-505c126036da, cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| dense | top-20 | 0.1500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, a36589f2-de69-5cdc-abe0-505c126036da, cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| dense | top-30 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, a36589f2-de69-5cdc-abe0-505c126036da, cb07bd4f-f6dd-5575-813a-757a481cef52 | - |
| sparse | top-10 | 0.2000 | 0.6667 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52 | a36589f2-de69-5cdc-abe0-505c126036da |
| sparse | top-20 | 0.1000 | 0.6667 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52 | a36589f2-de69-5cdc-abe0-505c126036da |
| sparse | top-30 | 0.0667 | 0.6667 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52 | a36589f2-de69-5cdc-abe0-505c126036da |
| rrf | top-10 | 0.3000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52, a36589f2-de69-5cdc-abe0-505c126036da | - |
| rrf | top-20 | 0.1500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52, a36589f2-de69-5cdc-abe0-505c126036da | - |
| rrf | top-30 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52, a36589f2-de69-5cdc-abe0-505c126036da | - |
| reranked | top-10 | 0.2000 | 0.6667 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52 | a36589f2-de69-5cdc-abe0-505c126036da |
| reranked | top-20 | 0.1500 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52, a36589f2-de69-5cdc-abe0-505c126036da | - |
| reranked | top-30 | 0.1000 | 1.0000 | fb807836-6f26-5dfd-9d71-c283e2cfa024, cb07bd4f-f6dd-5575-813a-757a481cef52, a36589f2-de69-5cdc-abe0-505c126036da | - |

### corpus-extension-apis-2

Question: How does OpenShift Container Platform document Reference guide for extension APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 978f893b-5621-5d79-8180-2cc42fa26fd9 | 58322bfd-1625-56fe-a131-f476ab75678f |
| dense | top-20 | 0.1000 | 0.6667 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 978f893b-5621-5d79-8180-2cc42fa26fd9 | 58322bfd-1625-56fe-a131-f476ab75678f |
| dense | top-30 | 0.0667 | 0.6667 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 978f893b-5621-5d79-8180-2cc42fa26fd9 | 58322bfd-1625-56fe-a131-f476ab75678f |
| sparse | top-10 | 0.1000 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| sparse | top-20 | 0.0500 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| sparse | top-30 | 0.0333 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| rrf | top-10 | 0.1000 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| rrf | top-20 | 0.0500 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| rrf | top-30 | 0.0667 | 0.6667 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 978f893b-5621-5d79-8180-2cc42fa26fd9 | 58322bfd-1625-56fe-a131-f476ab75678f |
| reranked | top-10 | 0.1000 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| reranked | top-20 | 0.0500 | 0.3333 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3 | 978f893b-5621-5d79-8180-2cc42fa26fd9, 58322bfd-1625-56fe-a131-f476ab75678f |
| reranked | top-30 | 0.0667 | 0.6667 | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 978f893b-5621-5d79-8180-2cc42fa26fd9 | 58322bfd-1625-56fe-a131-f476ab75678f |

### corpus-extensions-2

Question: How does OpenShift Container Platform document Working with extensions in OpenShift Container Platform using Operator Lifecycle Manager (OLM) v1.?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| dense | top-20 | 0.1000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| dense | top-30 | 0.0667 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| sparse | top-10 | 0.2000 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| sparse | top-20 | 0.1000 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| sparse | top-30 | 0.0667 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| rrf | top-10 | 0.2000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| rrf | top-20 | 0.1000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| rrf | top-30 | 0.0667 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| reranked | top-10 | 0.2000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| reranked | top-20 | 0.1000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |
| reranked | top-30 | 0.0667 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | ed78bb8e-a80c-59fc-ad29-d03fddd67d8e |

### corpus-gitops-2

Question: How does OpenShift Container Platform document A declarative way to implement continuous deployment for cloud native applications.?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| dense | top-20 | 0.0500 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| dense | top-30 | 0.0333 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| sparse | top-10 | 0.1000 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| sparse | top-20 | 0.0500 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| sparse | top-30 | 0.0333 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| rrf | top-10 | 0.1000 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| rrf | top-20 | 0.0500 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| rrf | top-30 | 0.0333 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| reranked | top-10 | 0.1000 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| reranked | top-20 | 0.0500 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |
| reranked | top-30 | 0.0333 | 0.3333 | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4 | 48ada4c6-13a6-58ec-b684-4e43169b6582, 18955a40-b23d-5dcc-8425-a7b36e22dcac |

### corpus-hardware-accelerators-2

Question: How does OpenShift Container Platform document Hardware accelerators?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, efe72277-e863-5717-be18-3446659b193b | - |
| dense | top-20 | 0.1500 | 1.0000 | e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, efe72277-e863-5717-be18-3446659b193b | - |
| dense | top-30 | 0.1000 | 1.0000 | e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, efe72277-e863-5717-be18-3446659b193b | - |
| sparse | top-10 | 0.3000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| sparse | top-20 | 0.1500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| sparse | top-30 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| rrf | top-10 | 0.3000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| rrf | top-20 | 0.1500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| rrf | top-30 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| reranked | top-10 | 0.3000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| reranked | top-20 | 0.1500 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |
| reranked | top-30 | 0.1000 | 1.0000 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, e1df6a0c-d0a2-5f25-9261-d9bc7aad8780, efe72277-e863-5717-be18-3446659b193b | - |

### corpus-hardware-networks-2

Question: How does OpenShift Container Platform document Configuring hardware-specific networking features in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| dense | top-20 | 0.0500 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| dense | top-30 | 0.0333 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| sparse | top-10 | 0.1000 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| sparse | top-20 | 0.0500 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| sparse | top-30 | 0.0333 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| rrf | top-10 | 0.1000 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| rrf | top-20 | 0.0500 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| rrf | top-30 | 0.0333 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| reranked | top-10 | 0.1000 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| reranked | top-20 | 0.0500 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |
| reranked | top-30 | 0.0333 | 0.3333 | b3ae06b7-503a-5b8a-a9de-190f25bf1e8e | 72442901-3cb3-5c0d-a9b0-d598c80a2a55, bdb22800-7a69-5c79-a968-d64045535da1 |

### corpus-hosted-control-planes-2

Question: How does OpenShift Container Platform document Using hosted control planes with OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 |
| dense | top-20 | 0.1500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| dense | top-30 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 97f14b7e-6fb9-5af9-8482-baa185da9db8 | 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 |
| sparse | top-20 | 0.1000 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 |
| sparse | top-30 | 0.0667 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 |
| rrf | top-10 | 0.2000 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 |
| rrf | top-20 | 0.1500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 |
| reranked | top-20 | 0.1500 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 09cb2c81-5eed-510b-8fa9-14fe0ac0ffc0 | - |

### corpus-image-apis-2

Question: How does OpenShift Container Platform document Reference guide for image APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, c878dbc8-95e0-5f3e-8b79-6bceacd8466a | 72451032-9898-5f5f-b16f-6b0d650284b7 |
| dense | top-20 | 0.1500 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| dense | top-30 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 |
| sparse | top-20 | 0.0500 | 0.3333 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 |
| sparse | top-30 | 0.0333 | 0.3333 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 |
| rrf | top-10 | 0.1000 | 0.3333 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 |
| rrf | top-20 | 0.1000 | 0.6667 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, c878dbc8-95e0-5f3e-8b79-6bceacd8466a | 72451032-9898-5f5f-b16f-6b0d650284b7 |
| rrf | top-30 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 | - |
| reranked | top-10 | 0.1000 | 0.3333 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 |
| reranked | top-20 | 0.0500 | 0.3333 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf | c878dbc8-95e0-5f3e-8b79-6bceacd8466a, 72451032-9898-5f5f-b16f-6b0d650284b7 |
| reranked | top-30 | 0.1000 | 1.0000 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 72451032-9898-5f5f-b16f-6b0d650284b7, c878dbc8-95e0-5f3e-8b79-6bceacd8466a | - |

### corpus-images-2

Question: How does OpenShift Container Platform document Creating and managing images and imagestreams in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| dense | top-20 | 0.1000 | 0.6667 | 2d37dd44-deed-5a47-bb08-772676b96949, e2fd35a2-190a-5d03-8956-91faa514385a | ee2ec254-9792-5c41-8387-204fce1eba50 |
| dense | top-30 | 0.0667 | 0.6667 | 2d37dd44-deed-5a47-bb08-772676b96949, e2fd35a2-190a-5d03-8956-91faa514385a | ee2ec254-9792-5c41-8387-204fce1eba50 |
| sparse | top-10 | 0.1000 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| sparse | top-20 | 0.0500 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| sparse | top-30 | 0.0333 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| rrf | top-10 | 0.1000 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| rrf | top-20 | 0.0500 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| rrf | top-30 | 0.0667 | 0.6667 | 2d37dd44-deed-5a47-bb08-772676b96949, e2fd35a2-190a-5d03-8956-91faa514385a | ee2ec254-9792-5c41-8387-204fce1eba50 |
| reranked | top-10 | 0.1000 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| reranked | top-20 | 0.0500 | 0.3333 | 2d37dd44-deed-5a47-bb08-772676b96949 | ee2ec254-9792-5c41-8387-204fce1eba50, e2fd35a2-190a-5d03-8956-91faa514385a |
| reranked | top-30 | 0.0667 | 0.6667 | 2d37dd44-deed-5a47-bb08-772676b96949, e2fd35a2-190a-5d03-8956-91faa514385a | ee2ec254-9792-5c41-8387-204fce1eba50 |

### corpus-ingress-and-load-balancing-2

Question: How does OpenShift Container Platform document Exposing services and managing external traffic in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| dense | top-20 | 0.0500 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| dense | top-30 | 0.0333 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | top-10 | 0.1000 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | top-20 | 0.0500 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| sparse | top-30 | 0.0333 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | top-10 | 0.1000 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | top-20 | 0.0500 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| rrf | top-30 | 0.0333 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | top-10 | 0.1000 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | top-20 | 0.0500 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |
| reranked | top-30 | 0.0333 | 0.3333 | aeb316dd-8324-5466-96e7-b50216f67eba | d90b9cc5-a64e-5915-954b-491b32b23191, 9c12f617-eb4d-53eb-9566-20d859a99cd8 |

### corpus-installation-configuration-2

Question: How does OpenShift Container Platform document Cluster-wide configuration during installations?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| dense | top-20 | 0.0500 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| dense | top-30 | 0.0333 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| sparse | top-10 | 0.1000 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| sparse | top-20 | 0.0500 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| sparse | top-30 | 0.0333 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| rrf | top-10 | 0.1000 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| rrf | top-20 | 0.0500 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| rrf | top-30 | 0.0333 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| reranked | top-10 | 0.1000 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| reranked | top-20 | 0.0500 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |
| reranked | top-30 | 0.0333 | 0.3333 | e67a501e-c58e-56ac-b490-6080c3ff7167 | 5ded38d2-e130-51a9-a537-a8d1f72cbb86, 694fea6c-6083-5316-af7e-9a63a535ad3b |

### corpus-installation-overview-2

Question: How does OpenShift Container Platform document Overview content for installing OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| dense | top-20 | 0.1000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| dense | top-30 | 0.0667 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| sparse | top-10 | 0.1000 | 0.3333 | 52c58389-178b-5c15-8ed0-c686feaea548 | 02ffe48b-2487-5709-a690-d0dc7badd71f, f25095ff-907e-572c-81b5-94d064e72277 |
| sparse | top-20 | 0.0500 | 0.3333 | 52c58389-178b-5c15-8ed0-c686feaea548 | 02ffe48b-2487-5709-a690-d0dc7badd71f, f25095ff-907e-572c-81b5-94d064e72277 |
| sparse | top-30 | 0.0333 | 0.3333 | 52c58389-178b-5c15-8ed0-c686feaea548 | 02ffe48b-2487-5709-a690-d0dc7badd71f, f25095ff-907e-572c-81b5-94d064e72277 |
| rrf | top-10 | 0.2000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| rrf | top-20 | 0.1000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| rrf | top-30 | 0.0667 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| reranked | top-10 | 0.2000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| reranked | top-20 | 0.1000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |
| reranked | top-30 | 0.0667 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, 02ffe48b-2487-5709-a690-d0dc7badd71f | f25095ff-907e-572c-81b5-94d064e72277 |

### corpus-installing-a-two-node-openshift-cluster-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on two nodes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 |
| dense | top-20 | 0.1500 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| dense | top-30 | 0.1000 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 984e6e13-c15d-5118-a037-381cffd2fcca | e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 |
| sparse | top-20 | 0.0500 | 0.3333 | 984e6e13-c15d-5118-a037-381cffd2fcca | e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 |
| sparse | top-30 | 0.0333 | 0.3333 | 984e6e13-c15d-5118-a037-381cffd2fcca | e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 |
| rrf | top-10 | 0.1000 | 0.3333 | 984e6e13-c15d-5118-a037-381cffd2fcca | e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 |
| rrf | top-20 | 0.1000 | 0.6667 | 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 |
| rrf | top-30 | 0.1000 | 1.0000 | 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7, 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, 984e6e13-c15d-5118-a037-381cffd2fcca, e7b429f8-68f1-5cf7-947b-977501b896c7 | - |

### corpus-installing-an-on-premise-cluster-with-the-agent-based-installer-2

Question: How does OpenShift Container Platform document Installing an on-premise OpenShift Container Platform cluster with the Agent-based Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, e1861532-b1e8-58d5-a2ba-aead485235bd | 0da30e4c-ed47-5d04-8887-79303f4e629e |
| dense | top-20 | 0.1000 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, e1861532-b1e8-58d5-a2ba-aead485235bd | 0da30e4c-ed47-5d04-8887-79303f4e629e |
| dense | top-30 | 0.1000 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, e1861532-b1e8-58d5-a2ba-aead485235bd, 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| sparse | top-10 | 0.1000 | 0.3333 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | e1861532-b1e8-58d5-a2ba-aead485235bd, 0da30e4c-ed47-5d04-8887-79303f4e629e |
| sparse | top-20 | 0.1000 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, 0da30e4c-ed47-5d04-8887-79303f4e629e | e1861532-b1e8-58d5-a2ba-aead485235bd |
| sparse | top-30 | 0.1000 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, 0da30e4c-ed47-5d04-8887-79303f4e629e, e1861532-b1e8-58d5-a2ba-aead485235bd | - |
| rrf | top-10 | 0.2000 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, e1861532-b1e8-58d5-a2ba-aead485235bd | 0da30e4c-ed47-5d04-8887-79303f4e629e |
| rrf | top-20 | 0.1500 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, e1861532-b1e8-58d5-a2ba-aead485235bd, 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| rrf | top-30 | 0.1000 | 1.0000 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, e1861532-b1e8-58d5-a2ba-aead485235bd, 0da30e4c-ed47-5d04-8887-79303f4e629e | - |
| reranked | top-10 | 0.1000 | 0.3333 | e1861532-b1e8-58d5-a2ba-aead485235bd | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, 0da30e4c-ed47-5d04-8887-79303f4e629e |
| reranked | top-20 | 0.1000 | 0.6667 | e1861532-b1e8-58d5-a2ba-aead485235bd, 0da30e4c-ed47-5d04-8887-79303f4e629e | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 |
| reranked | top-30 | 0.1000 | 1.0000 | e1861532-b1e8-58d5-a2ba-aead485235bd, 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | - |

### corpus-installing-ibm-cloud-bare-metal-classic-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Cloud Bare Metal (Classic)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 5ac8f40d-cfe0-5255-afa9-315235578099, 7222659b-8d19-526d-abe5-58d02df8e46d, 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a | - |
| dense | top-20 | 0.1500 | 1.0000 | 5ac8f40d-cfe0-5255-afa9-315235578099, 7222659b-8d19-526d-abe5-58d02df8e46d, 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a | - |
| dense | top-30 | 0.1000 | 1.0000 | 5ac8f40d-cfe0-5255-afa9-315235578099, 7222659b-8d19-526d-abe5-58d02df8e46d, 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a | - |
| sparse | top-10 | 0.2000 | 0.6667 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d | 5ac8f40d-cfe0-5255-afa9-315235578099 |
| sparse | top-20 | 0.1500 | 1.0000 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |
| sparse | top-30 | 0.1000 | 1.0000 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |
| rrf | top-10 | 0.3000 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d, 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d, 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 7222659b-8d19-526d-abe5-58d02df8e46d, 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d | 5ac8f40d-cfe0-5255-afa9-315235578099 |
| reranked | top-20 | 0.1500 | 1.0000 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 5ac8f40d-cfe0-5255-afa9-315235578099 | - |

### corpus-installing-on-premise-with-assisted-installer-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on-premise with the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 67aeef97-4b27-542a-b4c4-a662978dbe0d, 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| dense | top-20 | 0.1500 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 67aeef97-4b27-542a-b4c4-a662978dbe0d, 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| dense | top-30 | 0.1000 | 1.0000 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 67aeef97-4b27-542a-b4c4-a662978dbe0d, 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 67aeef97-4b27-542a-b4c4-a662978dbe0d |
| sparse | top-20 | 0.1000 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 67aeef97-4b27-542a-b4c4-a662978dbe0d |
| sparse | top-30 | 0.0667 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 67aeef97-4b27-542a-b4c4-a662978dbe0d |
| rrf | top-10 | 0.2000 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 67aeef97-4b27-542a-b4c4-a662978dbe0d |
| rrf | top-20 | 0.1500 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 67aeef97-4b27-542a-b4c4-a662978dbe0d | - |
| rrf | top-30 | 0.1000 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 67aeef97-4b27-542a-b4c4-a662978dbe0d | - |
| reranked | top-10 | 0.1000 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 67aeef97-4b27-542a-b4c4-a662978dbe0d |
| reranked | top-20 | 0.1500 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 67aeef97-4b27-542a-b4c4-a662978dbe0d, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |
| reranked | top-30 | 0.1000 | 1.0000 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 67aeef97-4b27-542a-b4c4-a662978dbe0d, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | - |

### corpus-installing-on-a-single-node-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on a single node?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| dense | top-20 | 0.1500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| dense | top-30 | 0.1000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| sparse | top-10 | 0.1000 | 0.3333 | e775a89d-d659-5d00-8fb5-cb89d0977449 | 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d |
| sparse | top-20 | 0.0500 | 0.3333 | e775a89d-d659-5d00-8fb5-cb89d0977449 | 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d |
| sparse | top-30 | 0.0333 | 0.3333 | e775a89d-d659-5d00-8fb5-cb89d0977449 | 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d |
| rrf | top-10 | 0.1000 | 0.3333 | e775a89d-d659-5d00-8fb5-cb89d0977449 | 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d |
| rrf | top-20 | 0.1500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| rrf | top-30 | 0.1000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d | - |
| reranked | top-10 | 0.1000 | 0.3333 | 7da09197-3dc7-50f8-8edd-e7ab91faa701 | e775a89d-d659-5d00-8fb5-cb89d0977449, d697f502-f12d-5b17-8a1e-9c2b9666366d |
| reranked | top-20 | 0.1500 | 1.0000 | 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 7da09197-3dc7-50f8-8edd-e7ab91faa701, d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449 | - |

### corpus-installing-on-alibaba-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Alibaba Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | b75b40a3-f0e6-552b-94e6-18193a3898bd, 8dee03a8-4615-5c95-be33-53da96babd6b | ef050325-ff43-581b-9a9f-29a1fa167bf3 |
| dense | top-20 | 0.1500 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd, 8dee03a8-4615-5c95-be33-53da96babd6b, ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| dense | top-30 | 0.1000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd, 8dee03a8-4615-5c95-be33-53da96babd6b, ef050325-ff43-581b-9a9f-29a1fa167bf3 | - |
| sparse | top-10 | 0.2000 | 0.6667 | b75b40a3-f0e6-552b-94e6-18193a3898bd, ef050325-ff43-581b-9a9f-29a1fa167bf3 | 8dee03a8-4615-5c95-be33-53da96babd6b |
| sparse | top-20 | 0.1000 | 0.6667 | b75b40a3-f0e6-552b-94e6-18193a3898bd, ef050325-ff43-581b-9a9f-29a1fa167bf3 | 8dee03a8-4615-5c95-be33-53da96babd6b |
| sparse | top-30 | 0.0667 | 0.6667 | b75b40a3-f0e6-552b-94e6-18193a3898bd, ef050325-ff43-581b-9a9f-29a1fa167bf3 | 8dee03a8-4615-5c95-be33-53da96babd6b |
| rrf | top-10 | 0.3000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd, ef050325-ff43-581b-9a9f-29a1fa167bf3, 8dee03a8-4615-5c95-be33-53da96babd6b | - |
| rrf | top-20 | 0.1500 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd, ef050325-ff43-581b-9a9f-29a1fa167bf3, 8dee03a8-4615-5c95-be33-53da96babd6b | - |
| rrf | top-30 | 0.1000 | 1.0000 | b75b40a3-f0e6-552b-94e6-18193a3898bd, ef050325-ff43-581b-9a9f-29a1fa167bf3, 8dee03a8-4615-5c95-be33-53da96babd6b | - |
| reranked | top-10 | 0.3000 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd, 8dee03a8-4615-5c95-be33-53da96babd6b | - |
| reranked | top-20 | 0.1500 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd, 8dee03a8-4615-5c95-be33-53da96babd6b | - |
| reranked | top-30 | 0.1000 | 1.0000 | ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd, 8dee03a8-4615-5c95-be33-53da96babd6b | - |

### corpus-installing-on-any-platform-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on any platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| dense | top-20 | 0.1000 | 0.6667 | c2d086c3-ce90-500e-bfb2-a923a1c5b019, 21d69eae-01d5-5514-8b0e-5a9f9a965509 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| dense | top-30 | 0.0667 | 0.6667 | c2d086c3-ce90-500e-bfb2-a923a1c5b019, 21d69eae-01d5-5514-8b0e-5a9f9a965509 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| sparse | top-10 | 0.1000 | 0.3333 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| sparse | top-20 | 0.0500 | 0.3333 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| sparse | top-30 | 0.0333 | 0.3333 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| rrf | top-10 | 0.1000 | 0.3333 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| rrf | top-20 | 0.0500 | 0.3333 | c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| rrf | top-30 | 0.0667 | 0.6667 | c2d086c3-ce90-500e-bfb2-a923a1c5b019, 21d69eae-01d5-5514-8b0e-5a9f9a965509 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| reranked | top-10 | 0.2000 | 0.6667 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| reranked | top-20 | 0.1000 | 0.6667 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |
| reranked | top-30 | 0.0667 | 0.6667 | 21d69eae-01d5-5514-8b0e-5a9f9a965509, c2d086c3-ce90-500e-bfb2-a923a1c5b019 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec |

### corpus-installing-on-aws-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Amazon Web Services?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| dense | top-20 | 0.1000 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| dense | top-30 | 0.1000 | 1.0000 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8, a3f30643-1344-5295-85d3-e62869475681 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| sparse | top-20 | 0.1000 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| sparse | top-30 | 0.0667 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| rrf | top-10 | 0.2000 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| rrf | top-20 | 0.1000 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| rrf | top-30 | 0.0667 | 0.6667 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, cdd06c15-2087-5bf1-a723-bbafba10b2f8 | a3f30643-1344-5295-85d3-e62869475681 |
| reranked | top-10 | 0.2000 | 0.6667 | cdd06c15-2087-5bf1-a723-bbafba10b2f8, 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | a3f30643-1344-5295-85d3-e62869475681 |
| reranked | top-20 | 0.1000 | 0.6667 | cdd06c15-2087-5bf1-a723-bbafba10b2f8, 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | a3f30643-1344-5295-85d3-e62869475681 |
| reranked | top-30 | 0.0667 | 0.6667 | cdd06c15-2087-5bf1-a723-bbafba10b2f8, 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd | a3f30643-1344-5295-85d3-e62869475681 |

### corpus-installing-on-azure-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Azure?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| dense | top-20 | 0.1000 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| dense | top-30 | 0.0667 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| sparse | top-10 | 0.1000 | 0.3333 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | 1363c764-5b3c-5712-a7f0-8b54884ae146, 5a476753-384f-577f-98c3-89f8bfe1d006 |
| sparse | top-20 | 0.0500 | 0.3333 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | 1363c764-5b3c-5712-a7f0-8b54884ae146, 5a476753-384f-577f-98c3-89f8bfe1d006 |
| sparse | top-30 | 0.0333 | 0.3333 | 2643250e-5baa-583b-b070-6fbe83bf5c77 | 1363c764-5b3c-5712-a7f0-8b54884ae146, 5a476753-384f-577f-98c3-89f8bfe1d006 |
| rrf | top-10 | 0.2000 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| rrf | top-20 | 0.1000 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| rrf | top-30 | 0.0667 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146, 5a476753-384f-577f-98c3-89f8bfe1d006 |
| reranked | top-20 | 0.1000 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |
| reranked | top-30 | 0.0667 | 0.6667 | 2643250e-5baa-583b-b070-6fbe83bf5c77, 1363c764-5b3c-5712-a7f0-8b54884ae146 | 5a476753-384f-577f-98c3-89f8bfe1d006 |

### corpus-installing-on-azure-stack-hub-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Azure Stack Hub?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| dense | top-20 | 0.1500 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| dense | top-30 | 0.1000 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | - |
| sparse | top-10 | 0.2000 | 0.6667 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 |
| sparse | top-20 | 0.1000 | 0.6667 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 |
| sparse | top-30 | 0.0667 | 0.6667 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 |
| rrf | top-10 | 0.2000 | 0.6667 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 44d40f32-aa8e-5999-b5a6-8995b9f8415f | 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 |
| rrf | top-20 | 0.1500 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 44d40f32-aa8e-5999-b5a6-8995b9f8415f, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 | - |
| rrf | top-30 | 0.1000 | 1.0000 | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 44d40f32-aa8e-5999-b5a6-8995b9f8415f, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 | - |
| reranked | top-10 | 0.1000 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 |
| reranked | top-20 | 0.1500 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 3a08d8ac-aa46-5c5f-a333-ec9087dc9902 | - |

### corpus-installing-on-bare-metal-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on bare metal?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| dense | top-20 | 0.1500 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| dense | top-30 | 0.1000 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| sparse | top-10 | 0.1000 | 0.3333 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| sparse | top-20 | 0.0500 | 0.3333 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| sparse | top-30 | 0.0333 | 0.3333 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 | 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| rrf | top-10 | 0.2000 | 0.6667 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 9e4cfb21-94cd-5177-8716-f3d6f625f842 | 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| rrf | top-20 | 0.1500 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| rrf | top-30 | 0.1000 | 1.0000 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 9e4cfb21-94cd-5177-8716-f3d6f625f842, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| reranked | top-10 | 0.1000 | 0.3333 | 9e4cfb21-94cd-5177-8716-f3d6f625f842 | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 2e809890-9346-5378-8a47-d5f9d85bb1dd |
| reranked | top-20 | 0.1500 | 1.0000 | 9e4cfb21-94cd-5177-8716-f3d6f625f842, 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |
| reranked | top-30 | 0.1000 | 1.0000 | 9e4cfb21-94cd-5177-8716-f3d6f625f842, 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 2e809890-9346-5378-8a47-d5f9d85bb1dd | - |

### corpus-installing-on-google-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Google Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |
| dense | top-20 | 0.1000 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |
| dense | top-30 | 0.0667 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |
| sparse | top-10 | 0.1000 | 0.3333 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | 085eb9b8-f5e5-5c75-913b-9895eaea1c6d, 221be235-a22a-579d-b8e2-5140ceafc228 |
| sparse | top-20 | 0.0500 | 0.3333 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | 085eb9b8-f5e5-5c75-913b-9895eaea1c6d, 221be235-a22a-579d-b8e2-5140ceafc228 |
| sparse | top-30 | 0.0333 | 0.3333 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | 085eb9b8-f5e5-5c75-913b-9895eaea1c6d, 221be235-a22a-579d-b8e2-5140ceafc228 |
| rrf | top-10 | 0.1000 | 0.3333 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35 | 085eb9b8-f5e5-5c75-913b-9895eaea1c6d, 221be235-a22a-579d-b8e2-5140ceafc228 |
| rrf | top-20 | 0.1000 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |
| rrf | top-30 | 0.0667 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d, 221be235-a22a-579d-b8e2-5140ceafc228 |
| reranked | top-20 | 0.1000 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |
| reranked | top-30 | 0.0667 | 0.6667 | 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 085eb9b8-f5e5-5c75-913b-9895eaea1c6d | 221be235-a22a-579d-b8e2-5140ceafc228 |

### corpus-installing-on-ibm-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Cloud Bare Metal (Classic)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | b115ffcb-bf06-533e-bee8-f225988e4dff, 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| dense | top-20 | 0.1500 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a, b115ffcb-bf06-533e-bee8-f225988e4dff | - |
| dense | top-30 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a, b115ffcb-bf06-533e-bee8-f225988e4dff | - |
| sparse | top-10 | 0.1000 | 0.3333 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | b115ffcb-bf06-533e-bee8-f225988e4dff, 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| sparse | top-20 | 0.1000 | 0.6667 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a | b115ffcb-bf06-533e-bee8-f225988e4dff |
| sparse | top-30 | 0.0667 | 0.6667 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a | b115ffcb-bf06-533e-bee8-f225988e4dff |
| rrf | top-10 | 0.2000 | 0.6667 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a | b115ffcb-bf06-533e-bee8-f225988e4dff |
| rrf | top-20 | 0.1000 | 0.6667 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a | b115ffcb-bf06-533e-bee8-f225988e4dff |
| rrf | top-30 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a, b115ffcb-bf06-533e-bee8-f225988e4dff | - |
| reranked | top-10 | 0.1000 | 0.3333 | fe4dd2ac-a393-59d3-9125-fb75933b0529 | b115ffcb-bf06-533e-bee8-f225988e4dff, 93d21363-b5e1-5b4a-8283-1b069bd0608a |
| reranked | top-20 | 0.1000 | 0.6667 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a | b115ffcb-bf06-533e-bee8-f225988e4dff |
| reranked | top-30 | 0.1000 | 1.0000 | fe4dd2ac-a393-59d3-9125-fb75933b0529, 93d21363-b5e1-5b4a-8283-1b069bd0608a, b115ffcb-bf06-533e-bee8-f225988e4dff | - |

### corpus-installing-on-ibm-power-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Power?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088, d45a492a-1a5a-5908-b270-32a75da1da87, 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| dense | top-20 | 0.1500 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088, d45a492a-1a5a-5908-b270-32a75da1da87, 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| dense | top-30 | 0.1000 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088, d45a492a-1a5a-5908-b270-32a75da1da87, 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 89389d95-495d-5611-ac71-fa2e7c985088 | d45a492a-1a5a-5908-b270-32a75da1da87, 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| sparse | top-20 | 0.1000 | 0.6667 | 89389d95-495d-5611-ac71-fa2e7c985088, 855a9eb7-d25c-5335-9fab-bda066a607d6 | d45a492a-1a5a-5908-b270-32a75da1da87 |
| sparse | top-30 | 0.0667 | 0.6667 | 89389d95-495d-5611-ac71-fa2e7c985088, 855a9eb7-d25c-5335-9fab-bda066a607d6 | d45a492a-1a5a-5908-b270-32a75da1da87 |
| rrf | top-10 | 0.2000 | 0.6667 | 89389d95-495d-5611-ac71-fa2e7c985088, 855a9eb7-d25c-5335-9fab-bda066a607d6 | d45a492a-1a5a-5908-b270-32a75da1da87 |
| rrf | top-20 | 0.1500 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088, 855a9eb7-d25c-5335-9fab-bda066a607d6, d45a492a-1a5a-5908-b270-32a75da1da87 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 89389d95-495d-5611-ac71-fa2e7c985088, 855a9eb7-d25c-5335-9fab-bda066a607d6, d45a492a-1a5a-5908-b270-32a75da1da87 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 89389d95-495d-5611-ac71-fa2e7c985088, d45a492a-1a5a-5908-b270-32a75da1da87, 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| reranked | top-20 | 0.1000 | 0.6667 | d45a492a-1a5a-5908-b270-32a75da1da87, 89389d95-495d-5611-ac71-fa2e7c985088 | 855a9eb7-d25c-5335-9fab-bda066a607d6 |
| reranked | top-30 | 0.1000 | 1.0000 | d45a492a-1a5a-5908-b270-32a75da1da87, 89389d95-495d-5611-ac71-fa2e7c985088, 855a9eb7-d25c-5335-9fab-bda066a607d6 | - |

### corpus-installing-on-ibm-power-virtual-server-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Power Virtual Server?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5, b48bd3be-6c60-50da-926a-bce97e978663, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| dense | top-20 | 0.1500 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5, b48bd3be-6c60-50da-926a-bce97e978663, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| dense | top-30 | 0.1000 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5, b48bd3be-6c60-50da-926a-bce97e978663, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | b48bd3be-6c60-50da-926a-bce97e978663 |
| sparse | top-20 | 0.1000 | 0.6667 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | b48bd3be-6c60-50da-926a-bce97e978663 |
| sparse | top-30 | 0.0667 | 0.6667 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | b48bd3be-6c60-50da-926a-bce97e978663 |
| rrf | top-10 | 0.2000 | 0.6667 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 318433bf-ebf4-5d86-8751-0bbcd63045b5 | b48bd3be-6c60-50da-926a-bce97e978663 |
| rrf | top-20 | 0.1500 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 318433bf-ebf4-5d86-8751-0bbcd63045b5, b48bd3be-6c60-50da-926a-bce97e978663 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 318433bf-ebf4-5d86-8751-0bbcd63045b5, b48bd3be-6c60-50da-926a-bce97e978663 | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 9b437025-830f-5e34-ab75-07ee52fc97a5, b48bd3be-6c60-50da-926a-bce97e978663, 318433bf-ebf4-5d86-8751-0bbcd63045b5 |
| reranked | top-20 | 0.1500 | 1.0000 | b48bd3be-6c60-50da-926a-bce97e978663, 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |
| reranked | top-30 | 0.1000 | 1.0000 | b48bd3be-6c60-50da-926a-bce97e978663, 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5 | - |

### corpus-installing-on-ibm-powervc-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM PowerVC?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, c75f1568-cc44-5448-8dbf-e4e58b88369e, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| dense | top-20 | 0.1500 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, c75f1568-cc44-5448-8dbf-e4e58b88369e, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| dense | top-30 | 0.1000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, c75f1568-cc44-5448-8dbf-e4e58b88369e, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | - |
| sparse | top-10 | 0.2000 | 0.6667 | ca4751a8-63fd-5016-a6f4-33c5e441c801, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | c75f1568-cc44-5448-8dbf-e4e58b88369e |
| sparse | top-20 | 0.1000 | 0.6667 | ca4751a8-63fd-5016-a6f4-33c5e441c801, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | c75f1568-cc44-5448-8dbf-e4e58b88369e |
| sparse | top-30 | 0.1000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e | - |
| rrf | top-10 | 0.3000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e | - |
| rrf | top-20 | 0.1500 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e | - |
| rrf | top-30 | 0.1000 | 1.0000 | ca4751a8-63fd-5016-a6f4-33c5e441c801, 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e | - |
| reranked | top-10 | 0.2000 | 0.6667 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e | ca4751a8-63fd-5016-a6f4-33c5e441c801 |
| reranked | top-20 | 0.1500 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e, ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, c75f1568-cc44-5448-8dbf-e4e58b88369e, ca4751a8-63fd-5016-a6f4-33c5e441c801 | - |

### corpus-installing-on-ibm-z-and-ibm-linuxone-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on IBM Z and IBM LinuxONE?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 458e7ebc-5512-5b2c-b00c-6a4576a9c322, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| dense | top-20 | 0.1500 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 458e7ebc-5512-5b2c-b00c-6a4576a9c322, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| dense | top-30 | 0.1000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 458e7ebc-5512-5b2c-b00c-6a4576a9c322, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | - |
| sparse | top-10 | 0.2000 | 0.6667 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | 458e7ebc-5512-5b2c-b00c-6a4576a9c322 |
| sparse | top-20 | 0.1000 | 0.6667 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | 458e7ebc-5512-5b2c-b00c-6a4576a9c322 |
| sparse | top-30 | 0.1000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, 458e7ebc-5512-5b2c-b00c-6a4576a9c322 | - |
| rrf | top-10 | 0.3000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, 458e7ebc-5512-5b2c-b00c-6a4576a9c322 | - |
| rrf | top-20 | 0.1500 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, 458e7ebc-5512-5b2c-b00c-6a4576a9c322 | - |
| rrf | top-30 | 0.1000 | 1.0000 | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, 458e7ebc-5512-5b2c-b00c-6a4576a9c322 | - |
| reranked | top-10 | 0.1000 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 458e7ebc-5512-5b2c-b00c-6a4576a9c322 |
| reranked | top-20 | 0.1500 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, 458e7ebc-5512-5b2c-b00c-6a4576a9c322, eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |
| reranked | top-30 | 0.1000 | 1.0000 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, 458e7ebc-5512-5b2c-b00c-6a4576a9c322, eef7ef3d-a263-5dd1-867f-ea331bde63ae | - |

### corpus-installing-on-nutanix-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Nutanix?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, f43c8144-a09a-59a6-ba9a-695a6b123ad5, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| dense | top-20 | 0.1500 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, f43c8144-a09a-59a6-ba9a-695a6b123ad5, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| dense | top-30 | 0.1000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, f43c8144-a09a-59a6-ba9a-695a6b123ad5, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | f43c8144-a09a-59a6-ba9a-695a6b123ad5 |
| sparse | top-20 | 0.1000 | 0.6667 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | f43c8144-a09a-59a6-ba9a-695a6b123ad5 |
| sparse | top-30 | 0.0667 | 0.6667 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | f43c8144-a09a-59a6-ba9a-695a6b123ad5 |
| rrf | top-10 | 0.2000 | 0.6667 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | f43c8144-a09a-59a6-ba9a-695a6b123ad5 |
| rrf | top-20 | 0.1500 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 5020cbc5-a226-53ff-8b09-d8a11cd599b1, f43c8144-a09a-59a6-ba9a-695a6b123ad5 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 5020cbc5-a226-53ff-8b09-d8a11cd599b1, f43c8144-a09a-59a6-ba9a-695a6b123ad5 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1, f43c8144-a09a-59a6-ba9a-695a6b123ad5, 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1, f43c8144-a09a-59a6-ba9a-695a6b123ad5, 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1, f43c8144-a09a-59a6-ba9a-695a6b123ad5, 2533d4a8-bc15-5a1e-9b85-f8b0e326f359 | - |

### corpus-installing-on-openstack-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on OpenStack?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 272cb21a-fc44-56d2-9de6-095e5a736789, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 | ee550e8d-5fe2-50a6-bfa1-f50619443688 |
| dense | top-20 | 0.1500 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0, ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| dense | top-30 | 0.1000 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0, ee550e8d-5fe2-50a6-bfa1-f50619443688 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 272cb21a-fc44-56d2-9de6-095e5a736789, ee550e8d-5fe2-50a6-bfa1-f50619443688 | e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 |
| sparse | top-20 | 0.1000 | 0.6667 | 272cb21a-fc44-56d2-9de6-095e5a736789, ee550e8d-5fe2-50a6-bfa1-f50619443688 | e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 |
| sparse | top-30 | 0.0667 | 0.6667 | 272cb21a-fc44-56d2-9de6-095e5a736789, ee550e8d-5fe2-50a6-bfa1-f50619443688 | e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 |
| rrf | top-10 | 0.2000 | 0.6667 | 272cb21a-fc44-56d2-9de6-095e5a736789, ee550e8d-5fe2-50a6-bfa1-f50619443688 | e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 |
| rrf | top-20 | 0.1500 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789, ee550e8d-5fe2-50a6-bfa1-f50619443688, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 272cb21a-fc44-56d2-9de6-095e5a736789, ee550e8d-5fe2-50a6-bfa1-f50619443688, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 | - |
| reranked | top-10 | 0.3000 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688, 272cb21a-fc44-56d2-9de6-095e5a736789, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 | - |
| reranked | top-20 | 0.1500 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688, 272cb21a-fc44-56d2-9de6-095e5a736789, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 | - |
| reranked | top-30 | 0.1000 | 1.0000 | ee550e8d-5fe2-50a6-bfa1-f50619443688, 272cb21a-fc44-56d2-9de6-095e5a736789, e0c76d6e-043f-5aa1-b480-c7f3cbac0cf0 | - |

### corpus-installing-on-oracle-database-appliance-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Installing on Oracle Database Appliance?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| dense | top-20 | 0.1000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| dense | top-30 | 0.0667 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| sparse | top-10 | 0.2000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| sparse | top-20 | 0.1000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| sparse | top-30 | 0.0667 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| rrf | top-10 | 0.2000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| rrf | top-20 | 0.1000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| rrf | top-30 | 0.0667 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| reranked | top-10 | 0.2000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| reranked | top-20 | 0.1000 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |
| reranked | top-30 | 0.0667 | 0.6667 | 2a675940-64ff-5403-8209-990058797cea, f698539a-b4f8-58dc-8117-545f15c69f0d | 63cd6e35-62b0-5fe1-b47e-e58063ea799a |

### corpus-installing-on-oracle-distributed-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Oracle Distributed Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| dense | top-20 | 0.1000 | 0.6667 | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| dense | top-30 | 0.0667 | 0.6667 | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| sparse | top-10 | 0.1000 | 0.3333 | eac4261f-2460-503f-94f0-c5329f9018d5 | 605112f9-e304-523e-8aae-171471e87194, dd93afd8-d8fb-5286-af72-7041a9f7857f |
| sparse | top-20 | 0.0500 | 0.3333 | eac4261f-2460-503f-94f0-c5329f9018d5 | 605112f9-e304-523e-8aae-171471e87194, dd93afd8-d8fb-5286-af72-7041a9f7857f |
| sparse | top-30 | 0.0667 | 0.6667 | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| rrf | top-10 | 0.1000 | 0.3333 | eac4261f-2460-503f-94f0-c5329f9018d5 | 605112f9-e304-523e-8aae-171471e87194, dd93afd8-d8fb-5286-af72-7041a9f7857f |
| rrf | top-20 | 0.1000 | 0.6667 | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| rrf | top-30 | 0.0667 | 0.6667 | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| reranked | top-10 | 0.0000 | 0.0000 | - | eac4261f-2460-503f-94f0-c5329f9018d5, 605112f9-e304-523e-8aae-171471e87194, dd93afd8-d8fb-5286-af72-7041a9f7857f |
| reranked | top-20 | 0.1000 | 0.6667 | 605112f9-e304-523e-8aae-171471e87194, eac4261f-2460-503f-94f0-c5329f9018d5 | dd93afd8-d8fb-5286-af72-7041a9f7857f |
| reranked | top-30 | 0.0667 | 0.6667 | 605112f9-e304-523e-8aae-171471e87194, eac4261f-2460-503f-94f0-c5329f9018d5 | dd93afd8-d8fb-5286-af72-7041a9f7857f |

### corpus-installing-on-oracle-edge-cloud-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on Oracle Edge Cloud?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | eb7235ff-a939-5bde-a133-635edbde7ae8, 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| dense | top-20 | 0.1000 | 0.6667 | eb7235ff-a939-5bde-a133-635edbde7ae8, 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| dense | top-30 | 0.0667 | 0.6667 | eb7235ff-a939-5bde-a133-635edbde7ae8, 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| sparse | top-10 | 0.1000 | 0.3333 | eb7235ff-a939-5bde-a133-635edbde7ae8 | 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e, dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| sparse | top-20 | 0.0500 | 0.3333 | eb7235ff-a939-5bde-a133-635edbde7ae8 | 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e, dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| sparse | top-30 | 0.0333 | 0.3333 | eb7235ff-a939-5bde-a133-635edbde7ae8 | 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e, dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| rrf | top-10 | 0.2000 | 0.6667 | eb7235ff-a939-5bde-a133-635edbde7ae8, 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| rrf | top-20 | 0.1000 | 0.6667 | eb7235ff-a939-5bde-a133-635edbde7ae8, 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| rrf | top-30 | 0.0667 | 0.6667 | eb7235ff-a939-5bde-a133-635edbde7ae8, 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| reranked | top-10 | 0.2000 | 0.6667 | 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e, eb7235ff-a939-5bde-a133-635edbde7ae8 | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| reranked | top-20 | 0.1000 | 0.6667 | 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e, eb7235ff-a939-5bde-a133-635edbde7ae8 | dd42bc83-bc17-5a12-acfc-16792b39fbcc |
| reranked | top-30 | 0.0667 | 0.6667 | 73ff0ee9-490a-5bd3-a4ce-8c4f65067f1e, eb7235ff-a939-5bde-a133-635edbde7ae8 | dd42bc83-bc17-5a12-acfc-16792b39fbcc |

### corpus-installing-on-vmware-vsphere-2

Question: How does OpenShift Container Platform document Installing OpenShift Container Platform on vSphere?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 0375f425-bed0-5aaa-88ae-b33a3989c60d, 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| dense | top-20 | 0.1500 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 0375f425-bed0-5aaa-88ae-b33a3989c60d, 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| dense | top-30 | 0.1000 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 0375f425-bed0-5aaa-88ae-b33a3989c60d, 2f6bf463-910c-536e-91b1-5621eeddf784 | - |
| sparse | top-10 | 0.2000 | 0.6667 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 2f6bf463-910c-536e-91b1-5621eeddf784 | 0375f425-bed0-5aaa-88ae-b33a3989c60d |
| sparse | top-20 | 0.1000 | 0.6667 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 2f6bf463-910c-536e-91b1-5621eeddf784 | 0375f425-bed0-5aaa-88ae-b33a3989c60d |
| sparse | top-30 | 0.0667 | 0.6667 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 2f6bf463-910c-536e-91b1-5621eeddf784 | 0375f425-bed0-5aaa-88ae-b33a3989c60d |
| rrf | top-10 | 0.2000 | 0.6667 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 2f6bf463-910c-536e-91b1-5621eeddf784 | 0375f425-bed0-5aaa-88ae-b33a3989c60d |
| rrf | top-20 | 0.1500 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 2f6bf463-910c-536e-91b1-5621eeddf784, 0375f425-bed0-5aaa-88ae-b33a3989c60d | - |
| rrf | top-30 | 0.1000 | 1.0000 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 2f6bf463-910c-536e-91b1-5621eeddf784, 0375f425-bed0-5aaa-88ae-b33a3989c60d | - |
| reranked | top-10 | 0.1000 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 0375f425-bed0-5aaa-88ae-b33a3989c60d |
| reranked | top-20 | 0.1000 | 0.6667 | 2f6bf463-910c-536e-91b1-5621eeddf784, 0375f425-bed0-5aaa-88ae-b33a3989c60d | d97adff8-6154-56a2-bd9a-6416cd6093c2 |
| reranked | top-30 | 0.1000 | 1.0000 | 2f6bf463-910c-536e-91b1-5621eeddf784, 0375f425-bed0-5aaa-88ae-b33a3989c60d, d97adff8-6154-56a2-bd9a-6416cd6093c2 | - |

### corpus-jenkins-3

Question: How does OpenShift Container Platform document Chapter1.Configuring Jenkins images?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| dense | top-20 | 0.1000 | 0.6667 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c | c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| dense | top-30 | 0.0667 | 0.6667 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c | c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| sparse | top-10 | 0.1000 | 0.3333 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| sparse | top-20 | 0.0500 | 0.3333 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| sparse | top-30 | 0.0667 | 0.6667 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c | c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| rrf | top-10 | 0.1000 | 0.3333 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| rrf | top-20 | 0.1000 | 0.6667 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c | c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| rrf | top-30 | 0.0667 | 0.6667 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c | c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| reranked | top-10 | 0.1000 | 0.3333 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| reranked | top-20 | 0.0500 | 0.3333 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, c13f0c9c-6589-5fe1-bd01-713f9840d391 |
| reranked | top-30 | 0.0667 | 0.6667 | 852c9e50-4c3f-55fc-a2c2-7de02ab95469, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c | c13f0c9c-6589-5fe1-bd01-713f9840d391 |

### corpus-kubernetes-nmstate-2

Question: How does OpenShift Container Platform document Observing and updating node network state and configuration using Kubernetes NMState in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, b19721c2-7852-556a-8c4a-bc6cc06be719, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| dense | top-20 | 0.1500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, b19721c2-7852-556a-8c4a-bc6cc06be719, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| dense | top-30 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, b19721c2-7852-556a-8c4a-bc6cc06be719, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| sparse | top-10 | 0.2000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb | b19721c2-7852-556a-8c4a-bc6cc06be719 |
| sparse | top-20 | 0.1000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb | b19721c2-7852-556a-8c4a-bc6cc06be719 |
| sparse | top-30 | 0.0667 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb | b19721c2-7852-556a-8c4a-bc6cc06be719 |
| rrf | top-10 | 0.3000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb, b19721c2-7852-556a-8c4a-bc6cc06be719 | - |
| rrf | top-20 | 0.1500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb, b19721c2-7852-556a-8c4a-bc6cc06be719 | - |
| rrf | top-30 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb, b19721c2-7852-556a-8c4a-bc6cc06be719 | - |
| reranked | top-10 | 0.2000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb | b19721c2-7852-556a-8c4a-bc6cc06be719 |
| reranked | top-20 | 0.1000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb | b19721c2-7852-556a-8c4a-bc6cc06be719 |
| reranked | top-30 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, f16dd82a-b19f-5758-86a3-91e469d47cdb, b19721c2-7852-556a-8c4a-bc6cc06be719 | - |

### corpus-logging-2

Question: How does OpenShift Container Platform document Configuring and using logging in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| dense | top-20 | 0.1500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| dense | top-30 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 |
| sparse | top-20 | 0.0500 | 0.3333 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 |
| sparse | top-30 | 0.0333 | 0.3333 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742 | 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 |
| rrf | top-10 | 0.3000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15, 4c532e18-b67c-5359-b034-a0907cd874a5 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5 | 442d1deb-ebeb-5271-9ea9-270d2b2c8e15 |
| reranked | top-20 | 0.1500 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 03572e96-a6e1-54d9-be9c-5bdd1cc28742, 4c532e18-b67c-5359-b034-a0907cd874a5, 442d1deb-ebeb-5271-9ea9-270d2b2c8e15 | - |

### corpus-machine-apis-2

Question: How does OpenShift Container Platform document Reference guide for machine APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 01feaa64-52d1-5311-be91-638189b9d982, 9f466fba-b29a-5160-ab49-df4ff91b96dd | c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| dense | top-20 | 0.1000 | 0.6667 | 01feaa64-52d1-5311-be91-638189b9d982, 9f466fba-b29a-5160-ab49-df4ff91b96dd | c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| dense | top-30 | 0.0667 | 0.6667 | 01feaa64-52d1-5311-be91-638189b9d982, 9f466fba-b29a-5160-ab49-df4ff91b96dd | c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| sparse | top-10 | 0.1000 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| sparse | top-20 | 0.0500 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| sparse | top-30 | 0.0333 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| rrf | top-10 | 0.1000 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| rrf | top-20 | 0.0500 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| rrf | top-30 | 0.0667 | 0.6667 | 01feaa64-52d1-5311-be91-638189b9d982, 9f466fba-b29a-5160-ab49-df4ff91b96dd | c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| reranked | top-10 | 0.1000 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| reranked | top-20 | 0.0500 | 0.3333 | 01feaa64-52d1-5311-be91-638189b9d982 | 9f466fba-b29a-5160-ab49-df4ff91b96dd, c3eb6302-eeb1-57bb-b5b7-dc3161066592 |
| reranked | top-30 | 0.0667 | 0.6667 | 01feaa64-52d1-5311-be91-638189b9d982, 9f466fba-b29a-5160-ab49-df4ff91b96dd | c3eb6302-eeb1-57bb-b5b7-dc3161066592 |

### corpus-machine-configuration-2

Question: How does OpenShift Container Platform document Managing and applying configuration and updates of the base operating system and container runtimes in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| dense | top-20 | 0.0500 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| dense | top-30 | 0.0667 | 0.6667 | 2a23a7d9-4976-5501-86e4-669c9956d90f, d0866a16-62e9-59d5-b1fb-0cd89da842fd | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5 |
| sparse | top-10 | 0.1000 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| sparse | top-20 | 0.0500 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| sparse | top-30 | 0.0333 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| rrf | top-10 | 0.1000 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| rrf | top-20 | 0.0500 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| rrf | top-30 | 0.0333 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| reranked | top-10 | 0.1000 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| reranked | top-20 | 0.0500 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |
| reranked | top-30 | 0.0333 | 0.3333 | 2a23a7d9-4976-5501-86e4-669c9956d90f | dbf4a4e1-3f85-57d5-8c49-fe9b84e0d8b5, d0866a16-62e9-59d5-b1fb-0cd89da842fd |

### corpus-machine-management-2

Question: How does OpenShift Container Platform document Adding and maintaining cluster machines?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| dense | top-20 | 0.0500 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| dense | top-30 | 0.0333 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| sparse | top-10 | 0.1000 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| sparse | top-20 | 0.0500 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| sparse | top-30 | 0.0333 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| rrf | top-10 | 0.1000 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| rrf | top-20 | 0.0500 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| rrf | top-30 | 0.0333 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| reranked | top-10 | 0.1000 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| reranked | top-20 | 0.0500 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |
| reranked | top-30 | 0.0333 | 0.3333 | bb43a1c4-4251-555f-9399-5f0283105079 | 38eb0d11-5de5-5cdd-ad14-e1bb8d8e73d8, 21a45103-4e63-51ed-b725-04a975efd8ad |

### corpus-metadata-apis-2

Question: How does OpenShift Container Platform document Reference guide for metadata APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | a4702c78-4647-5eb3-89df-60d31f85aba1, ad144812-88b9-5e32-8b99-4e94e6efc8e9 | b57bbb64-583c-523f-98c8-d52c147046c2 |
| dense | top-20 | 0.1000 | 0.6667 | a4702c78-4647-5eb3-89df-60d31f85aba1, ad144812-88b9-5e32-8b99-4e94e6efc8e9 | b57bbb64-583c-523f-98c8-d52c147046c2 |
| dense | top-30 | 0.0667 | 0.6667 | a4702c78-4647-5eb3-89df-60d31f85aba1, ad144812-88b9-5e32-8b99-4e94e6efc8e9 | b57bbb64-583c-523f-98c8-d52c147046c2 |
| sparse | top-10 | 0.1000 | 0.3333 | a4702c78-4647-5eb3-89df-60d31f85aba1 | ad144812-88b9-5e32-8b99-4e94e6efc8e9, b57bbb64-583c-523f-98c8-d52c147046c2 |
| sparse | top-20 | 0.0500 | 0.3333 | a4702c78-4647-5eb3-89df-60d31f85aba1 | ad144812-88b9-5e32-8b99-4e94e6efc8e9, b57bbb64-583c-523f-98c8-d52c147046c2 |
| sparse | top-30 | 0.0333 | 0.3333 | a4702c78-4647-5eb3-89df-60d31f85aba1 | ad144812-88b9-5e32-8b99-4e94e6efc8e9, b57bbb64-583c-523f-98c8-d52c147046c2 |
| rrf | top-10 | 0.1000 | 0.3333 | a4702c78-4647-5eb3-89df-60d31f85aba1 | ad144812-88b9-5e32-8b99-4e94e6efc8e9, b57bbb64-583c-523f-98c8-d52c147046c2 |
| rrf | top-20 | 0.1000 | 0.6667 | a4702c78-4647-5eb3-89df-60d31f85aba1, ad144812-88b9-5e32-8b99-4e94e6efc8e9 | b57bbb64-583c-523f-98c8-d52c147046c2 |
| rrf | top-30 | 0.0667 | 0.6667 | a4702c78-4647-5eb3-89df-60d31f85aba1, ad144812-88b9-5e32-8b99-4e94e6efc8e9 | b57bbb64-583c-523f-98c8-d52c147046c2 |
| reranked | top-10 | 0.1000 | 0.3333 | a4702c78-4647-5eb3-89df-60d31f85aba1 | ad144812-88b9-5e32-8b99-4e94e6efc8e9, b57bbb64-583c-523f-98c8-d52c147046c2 |
| reranked | top-20 | 0.0500 | 0.3333 | a4702c78-4647-5eb3-89df-60d31f85aba1 | ad144812-88b9-5e32-8b99-4e94e6efc8e9, b57bbb64-583c-523f-98c8-d52c147046c2 |
| reranked | top-30 | 0.0667 | 0.6667 | a4702c78-4647-5eb3-89df-60d31f85aba1, ad144812-88b9-5e32-8b99-4e94e6efc8e9 | b57bbb64-583c-523f-98c8-d52c147046c2 |

### corpus-migrating-from-version-3-to-4-2

Question: How does OpenShift Container Platform document Migrating to OpenShift Container Platform 4?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 0f24ff25-67e0-544f-be54-2f38faf87438, 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| dense | top-20 | 0.1500 | 1.0000 | 0f24ff25-67e0-544f-be54-2f38faf87438, 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| dense | top-30 | 0.1000 | 1.0000 | 0f24ff25-67e0-544f-be54-2f38faf87438, 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| sparse | top-10 | 0.2000 | 0.6667 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | 0f24ff25-67e0-544f-be54-2f38faf87438 |
| sparse | top-20 | 0.1000 | 0.6667 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | 0f24ff25-67e0-544f-be54-2f38faf87438 |
| sparse | top-30 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |
| rrf | top-10 | 0.3000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 0f24ff25-67e0-544f-be54-2f38faf87438 | - |

### corpus-monitoring-2

Question: How does OpenShift Container Platform document Configuring and using the monitoring stack in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 049b021d-ee67-5b87-9573-0c59027f28be |
| dense | top-20 | 0.1500 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32, 049b021d-ee67-5b87-9573-0c59027f28be | - |
| dense | top-30 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32, 049b021d-ee67-5b87-9573-0c59027f28be | - |
| sparse | top-10 | 0.2000 | 0.6667 | 16289132-d267-551c-91d1-e388cbe1ce32, f321f5cc-cbff-5600-b83f-f4899ec73083 | 049b021d-ee67-5b87-9573-0c59027f28be |
| sparse | top-20 | 0.1000 | 0.6667 | 16289132-d267-551c-91d1-e388cbe1ce32, f321f5cc-cbff-5600-b83f-f4899ec73083 | 049b021d-ee67-5b87-9573-0c59027f28be |
| sparse | top-30 | 0.0667 | 0.6667 | 16289132-d267-551c-91d1-e388cbe1ce32, f321f5cc-cbff-5600-b83f-f4899ec73083 | 049b021d-ee67-5b87-9573-0c59027f28be |
| rrf | top-10 | 0.2000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 049b021d-ee67-5b87-9573-0c59027f28be |
| rrf | top-20 | 0.1000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 049b021d-ee67-5b87-9573-0c59027f28be |
| rrf | top-30 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32, 049b021d-ee67-5b87-9573-0c59027f28be | - |
| reranked | top-10 | 0.2000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 049b021d-ee67-5b87-9573-0c59027f28be |
| reranked | top-20 | 0.1000 | 0.6667 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32 | 049b021d-ee67-5b87-9573-0c59027f28be |
| reranked | top-30 | 0.1000 | 1.0000 | f321f5cc-cbff-5600-b83f-f4899ec73083, 16289132-d267-551c-91d1-e388cbe1ce32, 049b021d-ee67-5b87-9573-0c59027f28be | - |

### corpus-monitoring-apis-2

Question: How does OpenShift Container Platform document Reference guide for monitoring APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | a051b20f-a822-51f8-94eb-a7b71880f454, 9e142b9c-bb9d-5399-acd6-5012f85c0947 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| dense | top-20 | 0.1000 | 0.6667 | a051b20f-a822-51f8-94eb-a7b71880f454, 9e142b9c-bb9d-5399-acd6-5012f85c0947 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| dense | top-30 | 0.0667 | 0.6667 | a051b20f-a822-51f8-94eb-a7b71880f454, 9e142b9c-bb9d-5399-acd6-5012f85c0947 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| sparse | top-10 | 0.1000 | 0.3333 | a051b20f-a822-51f8-94eb-a7b71880f454 | 9e142b9c-bb9d-5399-acd6-5012f85c0947, ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| sparse | top-20 | 0.0500 | 0.3333 | a051b20f-a822-51f8-94eb-a7b71880f454 | 9e142b9c-bb9d-5399-acd6-5012f85c0947, ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| sparse | top-30 | 0.0333 | 0.3333 | a051b20f-a822-51f8-94eb-a7b71880f454 | 9e142b9c-bb9d-5399-acd6-5012f85c0947, ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| rrf | top-10 | 0.1000 | 0.3333 | a051b20f-a822-51f8-94eb-a7b71880f454 | 9e142b9c-bb9d-5399-acd6-5012f85c0947, ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| rrf | top-20 | 0.1000 | 0.6667 | a051b20f-a822-51f8-94eb-a7b71880f454, 9e142b9c-bb9d-5399-acd6-5012f85c0947 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| rrf | top-30 | 0.0667 | 0.6667 | a051b20f-a822-51f8-94eb-a7b71880f454, 9e142b9c-bb9d-5399-acd6-5012f85c0947 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| reranked | top-10 | 0.1000 | 0.3333 | a051b20f-a822-51f8-94eb-a7b71880f454 | 9e142b9c-bb9d-5399-acd6-5012f85c0947, ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| reranked | top-20 | 0.0500 | 0.3333 | a051b20f-a822-51f8-94eb-a7b71880f454 | 9e142b9c-bb9d-5399-acd6-5012f85c0947, ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |
| reranked | top-30 | 0.0667 | 0.6667 | a051b20f-a822-51f8-94eb-a7b71880f454, 9e142b9c-bb9d-5399-acd6-5012f85c0947 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 |

### corpus-multiple-networks-2

Question: How does OpenShift Container Platform document Configuring and managing multiple network interfaces and virtual routing in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| dense | top-20 | 0.0500 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| dense | top-30 | 0.0333 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| sparse | top-10 | 0.1000 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| sparse | top-20 | 0.0500 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| sparse | top-30 | 0.0333 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| rrf | top-10 | 0.1000 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| rrf | top-20 | 0.0500 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| rrf | top-30 | 0.0333 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| reranked | top-10 | 0.1000 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| reranked | top-20 | 0.0500 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |
| reranked | top-30 | 0.0333 | 0.3333 | 4e19c74c-61b0-513e-8814-a5c41cecbe5e | b2e6a49d-b2ce-5c9b-82c1-3d1e58e01f02, ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3 |

### corpus-network-apis-2

Question: How does OpenShift Container Platform document Reference guide for network APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| dense | top-20 | 0.1000 | 0.6667 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, 966fa1fd-9306-5930-9555-9bb080491a8c | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| dense | top-30 | 0.0667 | 0.6667 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, 966fa1fd-9306-5930-9555-9bb080491a8c | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| sparse | top-10 | 0.1000 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| sparse | top-20 | 0.0500 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| sparse | top-30 | 0.0333 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| rrf | top-10 | 0.1000 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| rrf | top-20 | 0.0500 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| rrf | top-30 | 0.0667 | 0.6667 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, 966fa1fd-9306-5930-9555-9bb080491a8c | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| reranked | top-10 | 0.1000 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| reranked | top-20 | 0.0500 | 0.3333 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87 | 966fa1fd-9306-5930-9555-9bb080491a8c, f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |
| reranked | top-30 | 0.0667 | 0.6667 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, 966fa1fd-9306-5930-9555-9bb080491a8c | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 |

### corpus-network-observability-2

Question: How does OpenShift Container Platform document Configuring and using the Network Observability Operator in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c | 32aec05f-260f-5810-8529-6915fdb5c630 |
| dense | top-20 | 0.1500 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c, 32aec05f-260f-5810-8529-6915fdb5c630 | - |
| dense | top-30 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c, 32aec05f-260f-5810-8529-6915fdb5c630 | - |
| sparse | top-10 | 0.1000 | 0.3333 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 32aec05f-260f-5810-8529-6915fdb5c630, ba916851-7def-53bc-bfc1-d9318d308c1c |
| sparse | top-20 | 0.1000 | 0.6667 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c | 32aec05f-260f-5810-8529-6915fdb5c630 |
| sparse | top-30 | 0.0667 | 0.6667 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c | 32aec05f-260f-5810-8529-6915fdb5c630 |
| rrf | top-10 | 0.1000 | 0.3333 | e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 32aec05f-260f-5810-8529-6915fdb5c630, ba916851-7def-53bc-bfc1-d9318d308c1c |
| rrf | top-20 | 0.1000 | 0.6667 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c | 32aec05f-260f-5810-8529-6915fdb5c630 |
| rrf | top-30 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c, 32aec05f-260f-5810-8529-6915fdb5c630 | - |
| reranked | top-10 | 0.2000 | 0.6667 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c | 32aec05f-260f-5810-8529-6915fdb5c630 |
| reranked | top-20 | 0.1000 | 0.6667 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c | 32aec05f-260f-5810-8529-6915fdb5c630 |
| reranked | top-30 | 0.1000 | 1.0000 | e4fd75c8-5748-51f6-bce1-321e66d5dae7, ba916851-7def-53bc-bfc1-d9318d308c1c, 32aec05f-260f-5810-8529-6915fdb5c630 | - |

### corpus-network-observability-operator-2

Question: How does OpenShift Container Platform document Network Observability Operator for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b1213697-8b36-5042-8415-f4e5552eed90, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| dense | top-20 | 0.1500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b1213697-8b36-5042-8415-f4e5552eed90, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| dense | top-30 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b1213697-8b36-5042-8415-f4e5552eed90, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | - |
| sparse | top-10 | 0.2000 | 0.6667 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | b1213697-8b36-5042-8415-f4e5552eed90 |
| sparse | top-20 | 0.1000 | 0.6667 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | b1213697-8b36-5042-8415-f4e5552eed90 |
| sparse | top-30 | 0.0667 | 0.6667 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | b1213697-8b36-5042-8415-f4e5552eed90 |
| rrf | top-10 | 0.2000 | 0.6667 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | b1213697-8b36-5042-8415-f4e5552eed90 |
| rrf | top-20 | 0.1500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, b1213697-8b36-5042-8415-f4e5552eed90 | - |
| rrf | top-30 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, b1213697-8b36-5042-8415-f4e5552eed90 | - |
| reranked | top-10 | 0.2000 | 0.6667 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | b1213697-8b36-5042-8415-f4e5552eed90 |
| reranked | top-20 | 0.1500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, b1213697-8b36-5042-8415-f4e5552eed90 | - |
| reranked | top-30 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, b1213697-8b36-5042-8415-f4e5552eed90 | - |

### corpus-network-security-2

Question: How does OpenShift Container Platform document Securing network traffic and enforcing network policies in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| dense | top-20 | 0.0500 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| dense | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| sparse | top-10 | 0.1000 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| sparse | top-20 | 0.0500 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| sparse | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| rrf | top-10 | 0.1000 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| rrf | top-20 | 0.0500 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| rrf | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| reranked | top-10 | 0.1000 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| reranked | top-20 | 0.0500 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |
| reranked | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | 2d712e80-d722-5910-aabf-002713e9d4bd, c6859b69-7e60-5eb6-9add-d514eb66b5dd |

### corpus-networking-operators-2

Question: How does OpenShift Container Platform document Managing networking-specific Operators in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| dense | top-20 | 0.1000 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| dense | top-30 | 0.0667 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| sparse | top-10 | 0.1000 | 0.3333 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | 4c739f6a-d162-57c9-a453-a211a1a2a0c0, 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| sparse | top-20 | 0.0500 | 0.3333 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | 4c739f6a-d162-57c9-a453-a211a1a2a0c0, 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| sparse | top-30 | 0.0333 | 0.3333 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | 4c739f6a-d162-57c9-a453-a211a1a2a0c0, 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| rrf | top-10 | 0.1000 | 0.3333 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c | 4c739f6a-d162-57c9-a453-a211a1a2a0c0, 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| rrf | top-20 | 0.1000 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| rrf | top-30 | 0.0667 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| reranked | top-10 | 0.2000 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| reranked | top-20 | 0.1000 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |
| reranked | top-30 | 0.0667 | 0.6667 | 7ffe0602-12ca-5010-8a3e-fd74e30c981c, 4c739f6a-d162-57c9-a453-a211a1a2a0c0 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f |

### corpus-networking-overview-2

Question: How does OpenShift Container Platform document Understanding fundamental networking concepts and general tasks in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| dense | top-20 | 0.1500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| dense | top-30 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 507af079-dae6-536f-865c-4d6c11e29827 | cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| sparse | top-20 | 0.0500 | 0.3333 | 507af079-dae6-536f-865c-4d6c11e29827 | cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| sparse | top-30 | 0.0333 | 0.3333 | 507af079-dae6-536f-865c-4d6c11e29827 | cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 |
| rrf | top-10 | 0.2000 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, cb8246b6-f83a-5894-a7a6-23e479f9ea9d | 8136b814-2c0c-513f-a582-42551de5bed5 |
| rrf | top-20 | 0.1500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, cb8246b6-f83a-5894-a7a6-23e479f9ea9d, 8136b814-2c0c-513f-a582-42551de5bed5 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5 | cb8246b6-f83a-5894-a7a6-23e479f9ea9d |
| reranked | top-20 | 0.1500 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5, cb8246b6-f83a-5894-a7a6-23e479f9ea9d | - |
| reranked | top-30 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5, cb8246b6-f83a-5894-a7a6-23e479f9ea9d | - |

### corpus-node-apis-2

Question: How does OpenShift Container Platform document Reference guide for node APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 415e5a9d-371f-5a51-b350-689e04f516f6 | 264b374e-491d-50e1-af1c-0d651499c752 |
| dense | top-20 | 0.1000 | 0.6667 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 415e5a9d-371f-5a51-b350-689e04f516f6 | 264b374e-491d-50e1-af1c-0d651499c752 |
| dense | top-30 | 0.0667 | 0.6667 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 415e5a9d-371f-5a51-b350-689e04f516f6 | 264b374e-491d-50e1-af1c-0d651499c752 |
| sparse | top-10 | 0.1000 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| sparse | top-20 | 0.0500 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| sparse | top-30 | 0.0333 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| rrf | top-10 | 0.1000 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| rrf | top-20 | 0.0500 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| rrf | top-30 | 0.0667 | 0.6667 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 415e5a9d-371f-5a51-b350-689e04f516f6 | 264b374e-491d-50e1-af1c-0d651499c752 |
| reranked | top-10 | 0.1000 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| reranked | top-20 | 0.0500 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 415e5a9d-371f-5a51-b350-689e04f516f6, 264b374e-491d-50e1-af1c-0d651499c752 |
| reranked | top-30 | 0.0667 | 0.6667 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 415e5a9d-371f-5a51-b350-689e04f516f6 | 264b374e-491d-50e1-af1c-0d651499c752 |

### corpus-nodes-2

Question: How does OpenShift Container Platform document Configuring and managing nodes in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| dense | top-20 | 0.0500 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| dense | top-30 | 0.0667 | 0.6667 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60, e0b648b2-d5ac-505d-afda-96811d7b0926 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd |
| sparse | top-10 | 0.1000 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| sparse | top-20 | 0.0500 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| sparse | top-30 | 0.0333 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| rrf | top-10 | 0.1000 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| rrf | top-20 | 0.0500 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| rrf | top-30 | 0.0333 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| reranked | top-10 | 0.1000 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| reranked | top-20 | 0.0500 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |
| reranked | top-30 | 0.0333 | 0.3333 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 | 9d386825-74d5-5b8d-9e00-4b9692c6a9fd, e0b648b2-d5ac-505d-afda-96811d7b0926 |

### corpus-oauth-apis-2

Question: How does OpenShift Container Platform document Reference guide for Oauth APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| dense | top-20 | 0.1000 | 0.6667 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| dense | top-30 | 0.0667 | 0.6667 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| sparse | top-10 | 0.1000 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| sparse | top-20 | 0.0500 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| sparse | top-30 | 0.0333 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| rrf | top-10 | 0.1000 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| rrf | top-20 | 0.0500 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| rrf | top-30 | 0.0667 | 0.6667 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| reranked | top-10 | 0.1000 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| reranked | top-20 | 0.0500 | 0.3333 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38, b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |
| reranked | top-30 | 0.0667 | 0.6667 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, 7e00d5e1-5c3a-5191-8be6-d7ca680b9b38 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 |

### corpus-observability-overview-2

Question: How does OpenShift Container Platform document Contains information about observability for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | c0c361db-58e4-5716-9078-c721b0265a6e, a870e122-fffd-5cbe-8ac3-048137f48f3b | 13c74613-fe59-5a3c-9556-2cd617e013c6 |
| dense | top-20 | 0.1500 | 1.0000 | c0c361db-58e4-5716-9078-c721b0265a6e, a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| dense | top-30 | 0.1000 | 1.0000 | c0c361db-58e4-5716-9078-c721b0265a6e, a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | c0c361db-58e4-5716-9078-c721b0265a6e |
| sparse | top-20 | 0.1000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | c0c361db-58e4-5716-9078-c721b0265a6e |
| sparse | top-30 | 0.0667 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | c0c361db-58e4-5716-9078-c721b0265a6e |
| rrf | top-10 | 0.3000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, c0c361db-58e4-5716-9078-c721b0265a6e | - |
| rrf | top-20 | 0.1500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, c0c361db-58e4-5716-9078-c721b0265a6e | - |
| rrf | top-30 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, c0c361db-58e4-5716-9078-c721b0265a6e | - |
| reranked | top-10 | 0.2000 | 0.6667 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6 | c0c361db-58e4-5716-9078-c721b0265a6e |
| reranked | top-20 | 0.1500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, c0c361db-58e4-5716-9078-c721b0265a6e | - |
| reranked | top-30 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, c0c361db-58e4-5716-9078-c721b0265a6e | - |

### corpus-openshift-lightspeed-2

Question: How does OpenShift Container Platform document About OpenShift Lightspeed?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 3d995eb3-3de5-526f-b228-ac703e11c7e3, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| dense | top-20 | 0.1500 | 1.0000 | 3d995eb3-3de5-526f-b228-ac703e11c7e3, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| dense | top-30 | 0.1000 | 1.0000 | 3d995eb3-3de5-526f-b228-ac703e11c7e3, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | 3d995eb3-3de5-526f-b228-ac703e11c7e3 |
| sparse | top-20 | 0.1000 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | 3d995eb3-3de5-526f-b228-ac703e11c7e3 |
| sparse | top-30 | 0.0667 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | 3d995eb3-3de5-526f-b228-ac703e11c7e3 |
| rrf | top-10 | 0.3000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 3d995eb3-3de5-526f-b228-ac703e11c7e3 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 3d995eb3-3de5-526f-b228-ac703e11c7e3 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 3d995eb3-3de5-526f-b228-ac703e11c7e3 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 3d995eb3-3de5-526f-b228-ac703e11c7e3 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 3d995eb3-3de5-526f-b228-ac703e11c7e3 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 3d995eb3-3de5-526f-b228-ac703e11c7e3 | - |

### corpus-openshift-sandboxed-containers-2

Question: How does OpenShift Container Platform document OpenShift sandboxed containers guide?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| dense | top-20 | 0.1500 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| dense | top-30 | 0.1000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | 346c7282-d910-5bf9-a047-edffc561f2d5 |
| sparse | top-20 | 0.1000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | 346c7282-d910-5bf9-a047-edffc561f2d5 |
| sparse | top-30 | 0.0667 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | 346c7282-d910-5bf9-a047-edffc561f2d5 |
| rrf | top-10 | 0.3000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| reranked | top-10 | 0.3000 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239, 857b4fd4-6b84-504e-b8ec-f2b569435c9e, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| reranked | top-20 | 0.1500 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239, 857b4fd4-6b84-504e-b8ec-f2b569435c9e, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |
| reranked | top-30 | 0.1000 | 1.0000 | cd442f4e-9ba3-523f-920b-f8dc7fe24239, 857b4fd4-6b84-504e-b8ec-f2b569435c9e, 346c7282-d910-5bf9-a047-edffc561f2d5 | - |

### corpus-operator-apis-2

Question: How does OpenShift Container Platform document Reference guide for Operator APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 0cc80091-c566-5d0b-9fd8-b61af93751a1, fc7c95ff-b38a-57f7-952d-74a68f12f3d2 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| dense | top-20 | 0.1000 | 0.6667 | 0cc80091-c566-5d0b-9fd8-b61af93751a1, fc7c95ff-b38a-57f7-952d-74a68f12f3d2 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| dense | top-30 | 0.0667 | 0.6667 | 0cc80091-c566-5d0b-9fd8-b61af93751a1, fc7c95ff-b38a-57f7-952d-74a68f12f3d2 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| sparse | top-10 | 0.1000 | 0.3333 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | fc7c95ff-b38a-57f7-952d-74a68f12f3d2, c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| sparse | top-20 | 0.0500 | 0.3333 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | fc7c95ff-b38a-57f7-952d-74a68f12f3d2, c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| sparse | top-30 | 0.0333 | 0.3333 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | fc7c95ff-b38a-57f7-952d-74a68f12f3d2, c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| rrf | top-10 | 0.1000 | 0.3333 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | fc7c95ff-b38a-57f7-952d-74a68f12f3d2, c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| rrf | top-20 | 0.1000 | 0.6667 | 0cc80091-c566-5d0b-9fd8-b61af93751a1, fc7c95ff-b38a-57f7-952d-74a68f12f3d2 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| rrf | top-30 | 0.0667 | 0.6667 | 0cc80091-c566-5d0b-9fd8-b61af93751a1, fc7c95ff-b38a-57f7-952d-74a68f12f3d2 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| reranked | top-10 | 0.1000 | 0.3333 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | fc7c95ff-b38a-57f7-952d-74a68f12f3d2, c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| reranked | top-20 | 0.0500 | 0.3333 | 0cc80091-c566-5d0b-9fd8-b61af93751a1 | fc7c95ff-b38a-57f7-952d-74a68f12f3d2, c43d7ed0-4449-5cc3-be7f-51d912ed93ce |
| reranked | top-30 | 0.0667 | 0.6667 | 0cc80091-c566-5d0b-9fd8-b61af93751a1, fc7c95ff-b38a-57f7-952d-74a68f12f3d2 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce |

### corpus-operatorhub-apis-2

Question: How does OpenShift Container Platform document Reference guide for OperatorHub APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | d39bbe45-3314-5da3-b701-a2d87f88fb68, a4c7605d-ba55-5b87-982c-80b4962f0138 | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| dense | top-20 | 0.1000 | 0.6667 | d39bbe45-3314-5da3-b701-a2d87f88fb68, a4c7605d-ba55-5b87-982c-80b4962f0138 | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| dense | top-30 | 0.0667 | 0.6667 | d39bbe45-3314-5da3-b701-a2d87f88fb68, a4c7605d-ba55-5b87-982c-80b4962f0138 | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| sparse | top-10 | 0.1000 | 0.3333 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | a4c7605d-ba55-5b87-982c-80b4962f0138, d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| sparse | top-20 | 0.0500 | 0.3333 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | a4c7605d-ba55-5b87-982c-80b4962f0138, d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| sparse | top-30 | 0.0333 | 0.3333 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | a4c7605d-ba55-5b87-982c-80b4962f0138, d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| rrf | top-10 | 0.1000 | 0.3333 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | a4c7605d-ba55-5b87-982c-80b4962f0138, d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| rrf | top-20 | 0.1000 | 0.6667 | d39bbe45-3314-5da3-b701-a2d87f88fb68, a4c7605d-ba55-5b87-982c-80b4962f0138 | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| rrf | top-30 | 0.0667 | 0.6667 | d39bbe45-3314-5da3-b701-a2d87f88fb68, a4c7605d-ba55-5b87-982c-80b4962f0138 | d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| reranked | top-10 | 0.1000 | 0.3333 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | a4c7605d-ba55-5b87-982c-80b4962f0138, d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| reranked | top-20 | 0.0500 | 0.3333 | d39bbe45-3314-5da3-b701-a2d87f88fb68 | a4c7605d-ba55-5b87-982c-80b4962f0138, d418ddd9-5b85-54e8-8cff-19aa944395b5 |
| reranked | top-30 | 0.0667 | 0.6667 | d39bbe45-3314-5da3-b701-a2d87f88fb68, a4c7605d-ba55-5b87-982c-80b4962f0138 | d418ddd9-5b85-54e8-8cff-19aa944395b5 |

### corpus-operators-2

Question: How does OpenShift Container Platform document Working with Operators in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| dense | top-20 | 0.1500 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb, 2c1634db-7f79-56ea-89f1-e6dd14a18196 | - |
| dense | top-30 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb, 2c1634db-7f79-56ea-89f1-e6dd14a18196 | - |
| sparse | top-10 | 0.2000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| sparse | top-20 | 0.1000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| sparse | top-30 | 0.0667 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| rrf | top-10 | 0.2000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| rrf | top-20 | 0.1000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| rrf | top-30 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb, 2c1634db-7f79-56ea-89f1-e6dd14a18196 | - |
| reranked | top-10 | 0.2000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| reranked | top-20 | 0.1000 | 0.6667 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb | 2c1634db-7f79-56ea-89f1-e6dd14a18196 |
| reranked | top-30 | 0.1000 | 1.0000 | dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f, 753694b1-e529-5cac-8bf1-deb8de32cceb, 2c1634db-7f79-56ea-89f1-e6dd14a18196 | - |

### corpus-overview-2

Question: How does OpenShift Container Platform document Introduction to OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 2b3cfb52-0315-5200-bb8b-d6447317f904, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |
| dense | top-20 | 0.1500 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d, 5b6e54a9-5b42-50dc-996a-573be925d8a6 | - |
| dense | top-30 | 0.1000 | 1.0000 | 2b3cfb52-0315-5200-bb8b-d6447317f904, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d, 5b6e54a9-5b42-50dc-996a-573be925d8a6 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | 5b6e54a9-5b42-50dc-996a-573be925d8a6, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d |
| sparse | top-20 | 0.0500 | 0.3333 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | 5b6e54a9-5b42-50dc-996a-573be925d8a6, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d |
| sparse | top-30 | 0.0333 | 0.3333 | 2b3cfb52-0315-5200-bb8b-d6447317f904 | 5b6e54a9-5b42-50dc-996a-573be925d8a6, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d |
| rrf | top-10 | 0.2000 | 0.6667 | 2b3cfb52-0315-5200-bb8b-d6447317f904, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |
| rrf | top-20 | 0.1000 | 0.6667 | 2b3cfb52-0315-5200-bb8b-d6447317f904, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |
| rrf | top-30 | 0.0667 | 0.6667 | 2b3cfb52-0315-5200-bb8b-d6447317f904, 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |
| reranked | top-10 | 0.2000 | 0.6667 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d, 2b3cfb52-0315-5200-bb8b-d6447317f904 | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |
| reranked | top-20 | 0.1000 | 0.6667 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d, 2b3cfb52-0315-5200-bb8b-d6447317f904 | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |
| reranked | top-30 | 0.0667 | 0.6667 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d, 2b3cfb52-0315-5200-bb8b-d6447317f904 | 5b6e54a9-5b42-50dc-996a-573be925d8a6 |

### corpus-ovn-kubernetes-network-plugin-2

Question: How does OpenShift Container Platform document In-depth configuration and troubleshooting for the OVN-Kubernetes network plugin in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | - |
| dense | top-20 | 0.1500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | - |
| dense | top-30 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | - |
| sparse | top-10 | 0.2000 | 0.6667 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d |
| sparse | top-20 | 0.1000 | 0.6667 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d |
| sparse | top-30 | 0.0667 | 0.6667 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d |
| rrf | top-10 | 0.3000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d | - |
| rrf | top-20 | 0.1500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d | - |
| rrf | top-30 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d | - |
| reranked | top-10 | 0.2000 | 0.6667 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0 | 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d |
| reranked | top-20 | 0.1500 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d | - |
| reranked | top-30 | 0.1000 | 1.0000 | a75c6431-1926-5aaa-aba2-0f305b584bb8, ccebb28a-193d-5aaf-958f-e0e5e21ad2c0, 0bfcea40-5efe-5bc0-b9be-a3f1e8e5d03d | - |

### corpus-pipelines-2

Question: How does OpenShift Container Platform document Contains information about Pipelines for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, e2bbd59d-6319-5d41-874e-b8f0f83bea1c, 16e77789-7cdc-58f5-94dc-11537a511482 | - |
| dense | top-20 | 0.1500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, e2bbd59d-6319-5d41-874e-b8f0f83bea1c, 16e77789-7cdc-58f5-94dc-11537a511482 | - |
| dense | top-30 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, e2bbd59d-6319-5d41-874e-b8f0f83bea1c, 16e77789-7cdc-58f5-94dc-11537a511482 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482 | e2bbd59d-6319-5d41-874e-b8f0f83bea1c |
| sparse | top-20 | 0.1000 | 0.6667 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482 | e2bbd59d-6319-5d41-874e-b8f0f83bea1c |
| sparse | top-30 | 0.0667 | 0.6667 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482 | e2bbd59d-6319-5d41-874e-b8f0f83bea1c |
| rrf | top-10 | 0.2000 | 0.6667 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482 | e2bbd59d-6319-5d41-874e-b8f0f83bea1c |
| rrf | top-20 | 0.1500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482, e2bbd59d-6319-5d41-874e-b8f0f83bea1c | - |
| rrf | top-30 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482, e2bbd59d-6319-5d41-874e-b8f0f83bea1c | - |
| reranked | top-10 | 0.3000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482, e2bbd59d-6319-5d41-874e-b8f0f83bea1c | - |
| reranked | top-20 | 0.1500 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482, e2bbd59d-6319-5d41-874e-b8f0f83bea1c | - |
| reranked | top-30 | 0.1000 | 1.0000 | 876f7381-d6d4-5a73-b4f3-a31473484051, 16e77789-7cdc-58f5-94dc-11537a511482, e2bbd59d-6319-5d41-874e-b8f0f83bea1c | - |

### corpus-policy-apis-2

Question: How does OpenShift Container Platform document Reference guide for policy APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 0e8941cf-e232-5549-8072-50ffa5f139c1, 41fb59dd-3c1a-5622-ad2a-950c32bd4eac | 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| dense | top-20 | 0.1000 | 0.6667 | 0e8941cf-e232-5549-8072-50ffa5f139c1, 41fb59dd-3c1a-5622-ad2a-950c32bd4eac | 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| dense | top-30 | 0.0667 | 0.6667 | 0e8941cf-e232-5549-8072-50ffa5f139c1, 41fb59dd-3c1a-5622-ad2a-950c32bd4eac | 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| sparse | top-10 | 0.1000 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| sparse | top-20 | 0.0500 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| sparse | top-30 | 0.0333 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| rrf | top-10 | 0.1000 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| rrf | top-20 | 0.0500 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| rrf | top-30 | 0.0667 | 0.6667 | 0e8941cf-e232-5549-8072-50ffa5f139c1, 41fb59dd-3c1a-5622-ad2a-950c32bd4eac | 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| reranked | top-10 | 0.1000 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| reranked | top-20 | 0.0500 | 0.3333 | 0e8941cf-e232-5549-8072-50ffa5f139c1 | 41fb59dd-3c1a-5622-ad2a-950c32bd4eac, 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |
| reranked | top-30 | 0.0667 | 0.6667 | 0e8941cf-e232-5549-8072-50ffa5f139c1, 41fb59dd-3c1a-5622-ad2a-950c32bd4eac | 652b0ef7-0c84-55ec-8d06-22d66c0d7674 |

### corpus-postinstallation-configuration-2

Question: How does OpenShift Container Platform document Day 2 operations for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| dense | top-20 | 0.0500 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| dense | top-30 | 0.0333 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| sparse | top-10 | 0.1000 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| sparse | top-20 | 0.0500 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| sparse | top-30 | 0.0333 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| rrf | top-10 | 0.1000 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| rrf | top-20 | 0.0500 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| rrf | top-30 | 0.0333 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| reranked | top-10 | 0.1000 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| reranked | top-20 | 0.0500 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |
| reranked | top-30 | 0.0333 | 0.3333 | ac5e2d25-4578-52ea-b981-335ad30eaa15 | ff4cd1c7-3c9e-5a1f-ac4f-b1c4a24f7d6e, f0f80516-0861-5a35-bf5e-ba4513c74672 |

### corpus-power-monitoring-2

Question: How does OpenShift Container Platform document Configuring and using power monitoring for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, 02c920d1-86bc-5a4b-9400-1fffc7715882, a9e0a742-2d11-536e-aec5-1c238504f27b | - |
| dense | top-20 | 0.1500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, 02c920d1-86bc-5a4b-9400-1fffc7715882, a9e0a742-2d11-536e-aec5-1c238504f27b | - |
| dense | top-30 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, 02c920d1-86bc-5a4b-9400-1fffc7715882, a9e0a742-2d11-536e-aec5-1c238504f27b | - |
| sparse | top-10 | 0.2000 | 0.6667 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b | 02c920d1-86bc-5a4b-9400-1fffc7715882 |
| sparse | top-20 | 0.1000 | 0.6667 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b | 02c920d1-86bc-5a4b-9400-1fffc7715882 |
| sparse | top-30 | 0.0667 | 0.6667 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b | 02c920d1-86bc-5a4b-9400-1fffc7715882 |
| rrf | top-10 | 0.2000 | 0.6667 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b | 02c920d1-86bc-5a4b-9400-1fffc7715882 |
| rrf | top-20 | 0.1500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b, 02c920d1-86bc-5a4b-9400-1fffc7715882 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b, 02c920d1-86bc-5a4b-9400-1fffc7715882 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b, 02c920d1-86bc-5a4b-9400-1fffc7715882 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b, 02c920d1-86bc-5a4b-9400-1fffc7715882 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 5dae9f97-8693-5df1-ada2-911eb036dbba, a9e0a742-2d11-536e-aec5-1c238504f27b, 02c920d1-86bc-5a4b-9400-1fffc7715882 | - |

### corpus-project-apis-2

Question: How does OpenShift Container Platform document Reference guide for project APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| dense | top-20 | 0.1000 | 0.6667 | 12550d39-b552-5d17-99d7-383a5aabd41d, 70135bd3-160f-583a-9434-00e9ebf6d5fa | 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| dense | top-30 | 0.0667 | 0.6667 | 12550d39-b552-5d17-99d7-383a5aabd41d, 70135bd3-160f-583a-9434-00e9ebf6d5fa | 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| sparse | top-10 | 0.1000 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| sparse | top-20 | 0.0500 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| sparse | top-30 | 0.0333 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| rrf | top-10 | 0.1000 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| rrf | top-20 | 0.0500 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| rrf | top-30 | 0.0667 | 0.6667 | 12550d39-b552-5d17-99d7-383a5aabd41d, 70135bd3-160f-583a-9434-00e9ebf6d5fa | 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| reranked | top-10 | 0.1000 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| reranked | top-20 | 0.0500 | 0.3333 | 12550d39-b552-5d17-99d7-383a5aabd41d | 70135bd3-160f-583a-9434-00e9ebf6d5fa, 2b50dc76-33d3-5708-9556-e39efd39fac8 |
| reranked | top-30 | 0.0667 | 0.6667 | 12550d39-b552-5d17-99d7-383a5aabd41d, 70135bd3-160f-583a-9434-00e9ebf6d5fa | 2b50dc76-33d3-5708-9556-e39efd39fac8 |

### corpus-provisioning-apis-2

Question: How does OpenShift Container Platform document Reference guide for provisioning APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| dense | top-20 | 0.1000 | 0.6667 | f0a0f102-9a49-50be-9bc9-b20ee886b55f, 99bf927c-7499-5f24-9c69-e6c8ead41e77 | e675d384-daf8-57c9-bbb5-44d955e498fd |
| dense | top-30 | 0.0667 | 0.6667 | f0a0f102-9a49-50be-9bc9-b20ee886b55f, 99bf927c-7499-5f24-9c69-e6c8ead41e77 | e675d384-daf8-57c9-bbb5-44d955e498fd |
| sparse | top-10 | 0.1000 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| sparse | top-20 | 0.0500 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| sparse | top-30 | 0.0333 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| rrf | top-10 | 0.1000 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| rrf | top-20 | 0.0500 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| rrf | top-30 | 0.0667 | 0.6667 | f0a0f102-9a49-50be-9bc9-b20ee886b55f, 99bf927c-7499-5f24-9c69-e6c8ead41e77 | e675d384-daf8-57c9-bbb5-44d955e498fd |
| reranked | top-10 | 0.1000 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| reranked | top-20 | 0.0500 | 0.3333 | f0a0f102-9a49-50be-9bc9-b20ee886b55f | 99bf927c-7499-5f24-9c69-e6c8ead41e77, e675d384-daf8-57c9-bbb5-44d955e498fd |
| reranked | top-30 | 0.0667 | 0.6667 | f0a0f102-9a49-50be-9bc9-b20ee886b55f, 99bf927c-7499-5f24-9c69-e6c8ead41e77 | e675d384-daf8-57c9-bbb5-44d955e498fd |

### corpus-rbac-apis-2

Question: How does OpenShift Container Platform document Reference guide for RBAC APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | d55aea3c-7bcb-5711-b83d-224d2f0086d2, 39e1aee8-5c9f-5a78-8779-3219e76a6b88 | 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| dense | top-20 | 0.1000 | 0.6667 | d55aea3c-7bcb-5711-b83d-224d2f0086d2, 39e1aee8-5c9f-5a78-8779-3219e76a6b88 | 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| dense | top-30 | 0.0667 | 0.6667 | d55aea3c-7bcb-5711-b83d-224d2f0086d2, 39e1aee8-5c9f-5a78-8779-3219e76a6b88 | 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| sparse | top-10 | 0.1000 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| sparse | top-20 | 0.0500 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| sparse | top-30 | 0.0333 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| rrf | top-10 | 0.1000 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| rrf | top-20 | 0.0500 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| rrf | top-30 | 0.0667 | 0.6667 | d55aea3c-7bcb-5711-b83d-224d2f0086d2, 39e1aee8-5c9f-5a78-8779-3219e76a6b88 | 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| reranked | top-10 | 0.1000 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| reranked | top-20 | 0.0500 | 0.3333 | d55aea3c-7bcb-5711-b83d-224d2f0086d2 | 39e1aee8-5c9f-5a78-8779-3219e76a6b88, 4c4707f9-7c67-551a-91cc-122524fd2c56 |
| reranked | top-30 | 0.0667 | 0.6667 | d55aea3c-7bcb-5711-b83d-224d2f0086d2, 39e1aee8-5c9f-5a78-8779-3219e76a6b88 | 4c4707f9-7c67-551a-91cc-122524fd2c56 |

### corpus-red-hat-build-of-opentelemetry-2

Question: How does OpenShift Container Platform document Configuring and using the Red Hat build of OpenTelemetry in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| dense | top-20 | 0.1000 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| dense | top-30 | 0.0667 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| sparse | top-10 | 0.1000 | 0.3333 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | c7ee85b7-e719-5d56-992c-90e3c56cf715, 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| sparse | top-20 | 0.0500 | 0.3333 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | c7ee85b7-e719-5d56-992c-90e3c56cf715, 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| sparse | top-30 | 0.0333 | 0.3333 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8 | c7ee85b7-e719-5d56-992c-90e3c56cf715, 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| rrf | top-10 | 0.2000 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| rrf | top-20 | 0.1000 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| rrf | top-30 | 0.0667 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| reranked | top-10 | 0.2000 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| reranked | top-20 | 0.1000 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |
| reranked | top-30 | 0.0667 | 0.6667 | 2e5e1929-3c24-5b44-840d-7eb0b94199f8, c7ee85b7-e719-5d56-992c-90e3c56cf715 | 2818fb27-2ba6-5524-b889-4b73aa4cc605 |

### corpus-registry-2

Question: How does OpenShift Container Platform document Configuring registries for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 0138e0c2-2571-55bf-b15a-134e16846413, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | - |
| dense | top-20 | 0.1500 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 0138e0c2-2571-55bf-b15a-134e16846413, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | - |
| dense | top-30 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 0138e0c2-2571-55bf-b15a-134e16846413, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | - |
| sparse | top-10 | 0.2000 | 0.6667 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | 0138e0c2-2571-55bf-b15a-134e16846413 |
| sparse | top-20 | 0.1000 | 0.6667 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | 0138e0c2-2571-55bf-b15a-134e16846413 |
| sparse | top-30 | 0.0667 | 0.6667 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | 0138e0c2-2571-55bf-b15a-134e16846413 |
| rrf | top-10 | 0.3000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce, 0138e0c2-2571-55bf-b15a-134e16846413 | - |
| rrf | top-20 | 0.1500 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce, 0138e0c2-2571-55bf-b15a-134e16846413 | - |
| rrf | top-30 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce, 0138e0c2-2571-55bf-b15a-134e16846413 | - |
| reranked | top-10 | 0.2000 | 0.6667 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | 0138e0c2-2571-55bf-b15a-134e16846413 |
| reranked | top-20 | 0.1000 | 0.6667 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce | 0138e0c2-2571-55bf-b15a-134e16846413 |
| reranked | top-30 | 0.1000 | 1.0000 | b3362800-7d34-5ff0-8aa5-0fa777bdf606, 087d0fe7-aaa1-5add-96a5-bf0c426140ce, 0138e0c2-2571-55bf-b15a-134e16846413 | - |

### corpus-release-notes-2

Question: How does OpenShift Container Platform document Highlights of what is new and what has changed with this OpenShift Container Platform release?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 73522633-2cff-595c-969f-b8e58d027d43 | 28223c57-e6fe-5460-aeb1-424b59d58e1a |
| dense | top-20 | 0.1500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 73522633-2cff-595c-969f-b8e58d027d43, 28223c57-e6fe-5460-aeb1-424b59d58e1a | - |
| dense | top-30 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 73522633-2cff-595c-969f-b8e58d027d43, 28223c57-e6fe-5460-aeb1-424b59d58e1a | - |
| sparse | top-10 | 0.2000 | 0.6667 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a | 73522633-2cff-595c-969f-b8e58d027d43 |
| sparse | top-20 | 0.1000 | 0.6667 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a | 73522633-2cff-595c-969f-b8e58d027d43 |
| sparse | top-30 | 0.0667 | 0.6667 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a | 73522633-2cff-595c-969f-b8e58d027d43 |
| rrf | top-10 | 0.2000 | 0.6667 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a | 73522633-2cff-595c-969f-b8e58d027d43 |
| rrf | top-20 | 0.1500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a, 73522633-2cff-595c-969f-b8e58d027d43 | - |
| rrf | top-30 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a, 73522633-2cff-595c-969f-b8e58d027d43 | - |
| reranked | top-10 | 0.2000 | 0.6667 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a | 73522633-2cff-595c-969f-b8e58d027d43 |
| reranked | top-20 | 0.1500 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a, 73522633-2cff-595c-969f-b8e58d027d43 | - |
| reranked | top-30 | 0.1000 | 1.0000 | e58987e6-abbd-5169-8fbc-52fae6e0e3db, 28223c57-e6fe-5460-aeb1-424b59d58e1a, 73522633-2cff-595c-969f-b8e58d027d43 | - |

### corpus-role-apis-2

Question: How does OpenShift Container Platform document Reference guide for role APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | a5484249-da59-5e7b-b31b-e0c4a670b6f6, e4e8b645-3db1-5586-86b8-b58b62f5221f | 51762ff9-210f-501f-8ef9-3afc58adf617 |
| dense | top-20 | 0.1000 | 0.6667 | a5484249-da59-5e7b-b31b-e0c4a670b6f6, e4e8b645-3db1-5586-86b8-b58b62f5221f | 51762ff9-210f-501f-8ef9-3afc58adf617 |
| dense | top-30 | 0.0667 | 0.6667 | a5484249-da59-5e7b-b31b-e0c4a670b6f6, e4e8b645-3db1-5586-86b8-b58b62f5221f | 51762ff9-210f-501f-8ef9-3afc58adf617 |
| sparse | top-10 | 0.1000 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| sparse | top-20 | 0.0500 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| sparse | top-30 | 0.0333 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| rrf | top-10 | 0.1000 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| rrf | top-20 | 0.0500 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| rrf | top-30 | 0.0667 | 0.6667 | a5484249-da59-5e7b-b31b-e0c4a670b6f6, e4e8b645-3db1-5586-86b8-b58b62f5221f | 51762ff9-210f-501f-8ef9-3afc58adf617 |
| reranked | top-10 | 0.1000 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| reranked | top-20 | 0.0500 | 0.3333 | a5484249-da59-5e7b-b31b-e0c4a670b6f6 | e4e8b645-3db1-5586-86b8-b58b62f5221f, 51762ff9-210f-501f-8ef9-3afc58adf617 |
| reranked | top-30 | 0.0667 | 0.6667 | a5484249-da59-5e7b-b31b-e0c4a670b6f6, e4e8b645-3db1-5586-86b8-b58b62f5221f | 51762ff9-210f-501f-8ef9-3afc58adf617 |

### corpus-scalability-and-performance-2

Question: How does OpenShift Container Platform document Scaling your OpenShift Container Platform cluster and tuning performance in production environments?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| dense | top-20 | 0.1500 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| dense | top-30 | 0.1000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50 | 2f43abe0-3f66-5761-b85e-8663d4b06ac1 |
| sparse | top-20 | 0.1000 | 0.6667 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50 | 2f43abe0-3f66-5761-b85e-8663d4b06ac1 |
| sparse | top-30 | 0.0667 | 0.6667 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50 | 2f43abe0-3f66-5761-b85e-8663d4b06ac1 |
| rrf | top-10 | 0.3000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 67b4fcc0-9697-5b43-885b-d7f37a632473, ec131af4-f328-59c6-8baa-ad9242703b50, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| reranked | top-10 | 0.2000 | 0.6667 | ec131af4-f328-59c6-8baa-ad9242703b50, 67b4fcc0-9697-5b43-885b-d7f37a632473 | 2f43abe0-3f66-5761-b85e-8663d4b06ac1 |
| reranked | top-20 | 0.1500 | 1.0000 | ec131af4-f328-59c6-8baa-ad9242703b50, 67b4fcc0-9697-5b43-885b-d7f37a632473, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |
| reranked | top-30 | 0.1000 | 1.0000 | ec131af4-f328-59c6-8baa-ad9242703b50, 67b4fcc0-9697-5b43-885b-d7f37a632473, 2f43abe0-3f66-5761-b85e-8663d4b06ac1 | - |

### corpus-schedule-and-quota-apis-2

Question: How does OpenShift Container Platform document Reference guide for schedule and quota APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99 | 796196b9-51e5-5eef-a570-3b4501f62f44 |
| dense | top-20 | 0.1000 | 0.6667 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99 | 796196b9-51e5-5eef-a570-3b4501f62f44 |
| dense | top-30 | 0.1000 | 1.0000 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99, 796196b9-51e5-5eef-a570-3b4501f62f44 | - |
| sparse | top-10 | 0.1000 | 0.3333 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99, 796196b9-51e5-5eef-a570-3b4501f62f44 |
| sparse | top-20 | 0.0500 | 0.3333 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99, 796196b9-51e5-5eef-a570-3b4501f62f44 |
| sparse | top-30 | 0.0333 | 0.3333 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99, 796196b9-51e5-5eef-a570-3b4501f62f44 |
| rrf | top-10 | 0.1000 | 0.3333 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99, 796196b9-51e5-5eef-a570-3b4501f62f44 |
| rrf | top-20 | 0.0500 | 0.3333 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a | 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99, 796196b9-51e5-5eef-a570-3b4501f62f44 |
| rrf | top-30 | 0.0667 | 0.6667 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99 | 796196b9-51e5-5eef-a570-3b4501f62f44 |
| reranked | top-10 | 0.2000 | 0.6667 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99 | 796196b9-51e5-5eef-a570-3b4501f62f44 |
| reranked | top-20 | 0.1000 | 0.6667 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99 | 796196b9-51e5-5eef-a570-3b4501f62f44 |
| reranked | top-30 | 0.0667 | 0.6667 | 7025d13a-ebfd-5b0e-a5fe-acf61b05762a, 1d6a8c5f-fcbd-5afc-96a4-b4e3687c7d99 | 796196b9-51e5-5eef-a570-3b4501f62f44 |

### corpus-security-and-compliance-2

Question: How does OpenShift Container Platform document Learning about and managing security for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 341b1dff-ee04-55b0-bf33-139a2dc855e7, 405b6e83-7846-562b-b674-25124368f657, 1601a64e-21e5-57e9-b21d-124ed1353bd3 | - |
| dense | top-20 | 0.1500 | 1.0000 | 341b1dff-ee04-55b0-bf33-139a2dc855e7, 405b6e83-7846-562b-b674-25124368f657, 1601a64e-21e5-57e9-b21d-124ed1353bd3 | - |
| dense | top-30 | 0.1000 | 1.0000 | 341b1dff-ee04-55b0-bf33-139a2dc855e7, 405b6e83-7846-562b-b674-25124368f657, 1601a64e-21e5-57e9-b21d-124ed1353bd3 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 405b6e83-7846-562b-b674-25124368f657, 1601a64e-21e5-57e9-b21d-124ed1353bd3, 341b1dff-ee04-55b0-bf33-139a2dc855e7 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 405b6e83-7846-562b-b674-25124368f657, 1601a64e-21e5-57e9-b21d-124ed1353bd3, 341b1dff-ee04-55b0-bf33-139a2dc855e7 |
| sparse | top-30 | 0.0333 | 0.3333 | 405b6e83-7846-562b-b674-25124368f657 | 1601a64e-21e5-57e9-b21d-124ed1353bd3, 341b1dff-ee04-55b0-bf33-139a2dc855e7 |
| rrf | top-10 | 0.1000 | 0.3333 | 405b6e83-7846-562b-b674-25124368f657 | 1601a64e-21e5-57e9-b21d-124ed1353bd3, 341b1dff-ee04-55b0-bf33-139a2dc855e7 |
| rrf | top-20 | 0.1500 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657, 341b1dff-ee04-55b0-bf33-139a2dc855e7, 1601a64e-21e5-57e9-b21d-124ed1353bd3 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657, 341b1dff-ee04-55b0-bf33-139a2dc855e7, 1601a64e-21e5-57e9-b21d-124ed1353bd3 | - |
| reranked | top-10 | 0.1000 | 0.3333 | 405b6e83-7846-562b-b674-25124368f657 | 1601a64e-21e5-57e9-b21d-124ed1353bd3, 341b1dff-ee04-55b0-bf33-139a2dc855e7 |
| reranked | top-20 | 0.1000 | 0.6667 | 405b6e83-7846-562b-b674-25124368f657, 341b1dff-ee04-55b0-bf33-139a2dc855e7 | 1601a64e-21e5-57e9-b21d-124ed1353bd3 |
| reranked | top-30 | 0.1000 | 1.0000 | 405b6e83-7846-562b-b674-25124368f657, 341b1dff-ee04-55b0-bf33-139a2dc855e7, 1601a64e-21e5-57e9-b21d-124ed1353bd3 | - |

### corpus-security-apis-2

Question: How does OpenShift Container Platform document Reference guide for security APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 6c9e547f-2c6f-590a-8930-f5483c93e59b, 68147300-895c-5567-b5b4-6bba4872fe48 | e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| dense | top-20 | 0.1000 | 0.6667 | 6c9e547f-2c6f-590a-8930-f5483c93e59b, 68147300-895c-5567-b5b4-6bba4872fe48 | e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| dense | top-30 | 0.0667 | 0.6667 | 6c9e547f-2c6f-590a-8930-f5483c93e59b, 68147300-895c-5567-b5b4-6bba4872fe48 | e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| sparse | top-10 | 0.1000 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| sparse | top-20 | 0.0500 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| sparse | top-30 | 0.0333 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| rrf | top-10 | 0.1000 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| rrf | top-20 | 0.0500 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| rrf | top-30 | 0.0667 | 0.6667 | 6c9e547f-2c6f-590a-8930-f5483c93e59b, 68147300-895c-5567-b5b4-6bba4872fe48 | e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| reranked | top-10 | 0.1000 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| reranked | top-20 | 0.0500 | 0.3333 | 6c9e547f-2c6f-590a-8930-f5483c93e59b | 68147300-895c-5567-b5b4-6bba4872fe48, e937fc39-032f-5a57-8d3f-d9fe28ebb32f |
| reranked | top-30 | 0.0667 | 0.6667 | 6c9e547f-2c6f-590a-8930-f5483c93e59b, 68147300-895c-5567-b5b4-6bba4872fe48 | e937fc39-032f-5a57-8d3f-d9fe28ebb32f |

### corpus-serverless-2

Question: How does OpenShift Container Platform document OpenShift Serverless installation, usage, and release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489, 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| dense | top-20 | 0.1500 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489, 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| dense | top-30 | 0.1000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489, 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, ea6ea31d-b74e-58b5-ba8e-a1336615a489 | a986c392-c7bc-5f2e-972d-14e64151c737 |
| sparse | top-20 | 0.1000 | 0.6667 | 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, ea6ea31d-b74e-58b5-ba8e-a1336615a489 | a986c392-c7bc-5f2e-972d-14e64151c737 |
| sparse | top-30 | 0.0667 | 0.6667 | 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, ea6ea31d-b74e-58b5-ba8e-a1336615a489 | a986c392-c7bc-5f2e-972d-14e64151c737 |
| rrf | top-10 | 0.3000 | 1.0000 | 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, ea6ea31d-b74e-58b5-ba8e-a1336615a489, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, ea6ea31d-b74e-58b5-ba8e-a1336615a489, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, ea6ea31d-b74e-58b5-ba8e-a1336615a489, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| reranked | top-10 | 0.2000 | 0.6667 | ea6ea31d-b74e-58b5-ba8e-a1336615a489, 2b8f8b01-1650-5f4b-8627-03ed47a39dd4 | a986c392-c7bc-5f2e-972d-14e64151c737 |
| reranked | top-20 | 0.1500 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489, 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, a986c392-c7bc-5f2e-972d-14e64151c737 | - |
| reranked | top-30 | 0.1000 | 1.0000 | ea6ea31d-b74e-58b5-ba8e-a1336615a489, 2b8f8b01-1650-5f4b-8627-03ed47a39dd4, a986c392-c7bc-5f2e-972d-14e64151c737 | - |

### corpus-service-mesh-2

Question: How does OpenShift Container Platform document Service Mesh installation, usage, and release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| dense | top-20 | 0.1000 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| dense | top-30 | 0.0667 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| sparse | top-10 | 0.1000 | 0.3333 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | 547eab84-f5a1-57fa-8c74-cf637ab6f999, 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| sparse | top-20 | 0.0500 | 0.3333 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | 547eab84-f5a1-57fa-8c74-cf637ab6f999, 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| sparse | top-30 | 0.0667 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 5fe9db05-9565-56c4-a582-0ae1f6a681d4 | 547eab84-f5a1-57fa-8c74-cf637ab6f999 |
| rrf | top-10 | 0.1000 | 0.3333 | b41aa73d-88f3-5c09-9db7-d58ac4002e06 | 547eab84-f5a1-57fa-8c74-cf637ab6f999, 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| rrf | top-20 | 0.1000 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| rrf | top-30 | 0.0667 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| reranked | top-10 | 0.2000 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| reranked | top-20 | 0.1000 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |
| reranked | top-30 | 0.0667 | 0.6667 | b41aa73d-88f3-5c09-9db7-d58ac4002e06, 547eab84-f5a1-57fa-8c74-cf637ab6f999 | 5fe9db05-9565-56c4-a582-0ae1f6a681d4 |

### corpus-specialized-hardware-and-driver-enablement-2

Question: How does OpenShift Container Platform document Learn about hardware enablement on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 96d1589b-966b-59b9-8929-c23e5b51ec0d | 624c4370-6936-5332-ad40-dcc87d346f62 |
| dense | top-20 | 0.1000 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 96d1589b-966b-59b9-8929-c23e5b51ec0d | 624c4370-6936-5332-ad40-dcc87d346f62 |
| dense | top-30 | 0.0667 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 96d1589b-966b-59b9-8929-c23e5b51ec0d | 624c4370-6936-5332-ad40-dcc87d346f62 |
| sparse | top-10 | 0.1000 | 0.3333 | 472c788d-674c-572c-b7ba-43470151b223 | 96d1589b-966b-59b9-8929-c23e5b51ec0d, 624c4370-6936-5332-ad40-dcc87d346f62 |
| sparse | top-20 | 0.1000 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 624c4370-6936-5332-ad40-dcc87d346f62 | 96d1589b-966b-59b9-8929-c23e5b51ec0d |
| sparse | top-30 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223, 624c4370-6936-5332-ad40-dcc87d346f62, 96d1589b-966b-59b9-8929-c23e5b51ec0d | - |
| rrf | top-10 | 0.2000 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 96d1589b-966b-59b9-8929-c23e5b51ec0d | 624c4370-6936-5332-ad40-dcc87d346f62 |
| rrf | top-20 | 0.1000 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 96d1589b-966b-59b9-8929-c23e5b51ec0d | 624c4370-6936-5332-ad40-dcc87d346f62 |
| rrf | top-30 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223, 96d1589b-966b-59b9-8929-c23e5b51ec0d, 624c4370-6936-5332-ad40-dcc87d346f62 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 472c788d-674c-572c-b7ba-43470151b223, 624c4370-6936-5332-ad40-dcc87d346f62 | 96d1589b-966b-59b9-8929-c23e5b51ec0d |
| reranked | top-20 | 0.1500 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223, 624c4370-6936-5332-ad40-dcc87d346f62, 96d1589b-966b-59b9-8929-c23e5b51ec0d | - |
| reranked | top-30 | 0.1000 | 1.0000 | 472c788d-674c-572c-b7ba-43470151b223, 624c4370-6936-5332-ad40-dcc87d346f62, 96d1589b-966b-59b9-8929-c23e5b51ec0d | - |

### corpus-storage-2

Question: How does OpenShift Container Platform document Configuring and managing storage in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| dense | top-20 | 0.1000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| dense | top-30 | 0.0667 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| sparse | top-10 | 0.0000 | 0.0000 | - | 332810e1-67f3-5288-a876-deb1168d67ba, 6787b054-eb98-5291-b2ba-793d821cdbfa, b2a2f9eb-4161-50be-8287-7bafe4d47818 |
| sparse | top-20 | 0.1000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| sparse | top-30 | 0.0667 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| rrf | top-10 | 0.2000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| rrf | top-20 | 0.1000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| rrf | top-30 | 0.0667 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| reranked | top-10 | 0.2000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| reranked | top-20 | 0.1000 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |
| reranked | top-30 | 0.0667 | 0.6667 | 332810e1-67f3-5288-a876-deb1168d67ba, b2a2f9eb-4161-50be-8287-7bafe4d47818 | 6787b054-eb98-5291-b2ba-793d821cdbfa |

### corpus-storage-apis-2

Question: How does OpenShift Container Platform document Reference guide for storage APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 0db9c415-f766-591b-9084-0c3a6a6839b8, f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa | 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| dense | top-20 | 0.1000 | 0.6667 | 0db9c415-f766-591b-9084-0c3a6a6839b8, f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa | 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| dense | top-30 | 0.0667 | 0.6667 | 0db9c415-f766-591b-9084-0c3a6a6839b8, f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa | 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| sparse | top-10 | 0.1000 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| sparse | top-20 | 0.0500 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| sparse | top-30 | 0.0333 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| rrf | top-10 | 0.1000 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| rrf | top-20 | 0.0500 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| rrf | top-30 | 0.0667 | 0.6667 | 0db9c415-f766-591b-9084-0c3a6a6839b8, f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa | 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| reranked | top-10 | 0.1000 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| reranked | top-20 | 0.0500 | 0.3333 | 0db9c415-f766-591b-9084-0c3a6a6839b8 | f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa, 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |
| reranked | top-30 | 0.0667 | 0.6667 | 0db9c415-f766-591b-9084-0c3a6a6839b8, f0ddb3fd-d1fa-5226-9f40-eb781fbfe7fa | 52f722c7-3baf-5d93-9b47-bb9ba156bff5 |

### corpus-support-2

Question: How does OpenShift Container Platform document Getting support for OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 8708db3b-7b15-5904-9442-b4d3fe793729, 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| dense | top-20 | 0.1000 | 0.6667 | 8708db3b-7b15-5904-9442-b4d3fe793729, 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| dense | top-30 | 0.0667 | 0.6667 | 8708db3b-7b15-5904-9442-b4d3fe793729, 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| sparse | top-10 | 0.1000 | 0.3333 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | 8708db3b-7b15-5904-9442-b4d3fe793729, c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| sparse | top-20 | 0.0500 | 0.3333 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | 8708db3b-7b15-5904-9442-b4d3fe793729, c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| sparse | top-30 | 0.0333 | 0.3333 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | 8708db3b-7b15-5904-9442-b4d3fe793729, c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| rrf | top-10 | 0.1000 | 0.3333 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | 8708db3b-7b15-5904-9442-b4d3fe793729, c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| rrf | top-20 | 0.1000 | 0.6667 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95, 8708db3b-7b15-5904-9442-b4d3fe793729 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| rrf | top-30 | 0.0667 | 0.6667 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95, 8708db3b-7b15-5904-9442-b4d3fe793729 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| reranked | top-10 | 0.1000 | 0.3333 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95 | 8708db3b-7b15-5904-9442-b4d3fe793729, c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| reranked | top-20 | 0.1000 | 0.6667 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95, 8708db3b-7b15-5904-9442-b4d3fe793729 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |
| reranked | top-30 | 0.0667 | 0.6667 | 6d46e700-7b17-516e-a9bd-3ad44a28ef95, 8708db3b-7b15-5904-9442-b4d3fe793729 | c38b5bb6-c848-592e-b6d4-ca7d77d54dac |

### corpus-template-apis-2

Question: How does OpenShift Container Platform document Reference guide for template APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e310c8e9-6494-5ce9-8bd3-822283f11639, af14dc93-1526-5953-9b39-39c81087d313 | 33ebaa43-142f-5a3e-a942-1044688e29dc |
| dense | top-20 | 0.1000 | 0.6667 | e310c8e9-6494-5ce9-8bd3-822283f11639, af14dc93-1526-5953-9b39-39c81087d313 | 33ebaa43-142f-5a3e-a942-1044688e29dc |
| dense | top-30 | 0.0667 | 0.6667 | e310c8e9-6494-5ce9-8bd3-822283f11639, af14dc93-1526-5953-9b39-39c81087d313 | 33ebaa43-142f-5a3e-a942-1044688e29dc |
| sparse | top-10 | 0.1000 | 0.3333 | e310c8e9-6494-5ce9-8bd3-822283f11639 | af14dc93-1526-5953-9b39-39c81087d313, 33ebaa43-142f-5a3e-a942-1044688e29dc |
| sparse | top-20 | 0.0500 | 0.3333 | e310c8e9-6494-5ce9-8bd3-822283f11639 | af14dc93-1526-5953-9b39-39c81087d313, 33ebaa43-142f-5a3e-a942-1044688e29dc |
| sparse | top-30 | 0.0333 | 0.3333 | e310c8e9-6494-5ce9-8bd3-822283f11639 | af14dc93-1526-5953-9b39-39c81087d313, 33ebaa43-142f-5a3e-a942-1044688e29dc |
| rrf | top-10 | 0.1000 | 0.3333 | e310c8e9-6494-5ce9-8bd3-822283f11639 | af14dc93-1526-5953-9b39-39c81087d313, 33ebaa43-142f-5a3e-a942-1044688e29dc |
| rrf | top-20 | 0.1000 | 0.6667 | e310c8e9-6494-5ce9-8bd3-822283f11639, af14dc93-1526-5953-9b39-39c81087d313 | 33ebaa43-142f-5a3e-a942-1044688e29dc |
| rrf | top-30 | 0.0667 | 0.6667 | e310c8e9-6494-5ce9-8bd3-822283f11639, af14dc93-1526-5953-9b39-39c81087d313 | 33ebaa43-142f-5a3e-a942-1044688e29dc |
| reranked | top-10 | 0.1000 | 0.3333 | e310c8e9-6494-5ce9-8bd3-822283f11639 | af14dc93-1526-5953-9b39-39c81087d313, 33ebaa43-142f-5a3e-a942-1044688e29dc |
| reranked | top-20 | 0.0500 | 0.3333 | e310c8e9-6494-5ce9-8bd3-822283f11639 | af14dc93-1526-5953-9b39-39c81087d313, 33ebaa43-142f-5a3e-a942-1044688e29dc |
| reranked | top-30 | 0.0667 | 0.6667 | e310c8e9-6494-5ce9-8bd3-822283f11639, af14dc93-1526-5953-9b39-39c81087d313 | 33ebaa43-142f-5a3e-a942-1044688e29dc |

### corpus-tutorials-2

Question: How does OpenShift Container Platform document Getting started in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5, 6dd2da10-27e9-56f1-b3d1-653bef13909b | e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| dense | top-20 | 0.1000 | 0.6667 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5, 6dd2da10-27e9-56f1-b3d1-653bef13909b | e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| dense | top-30 | 0.0667 | 0.6667 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5, 6dd2da10-27e9-56f1-b3d1-653bef13909b | e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| sparse | top-10 | 0.1000 | 0.3333 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | 6dd2da10-27e9-56f1-b3d1-653bef13909b, e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| sparse | top-20 | 0.0500 | 0.3333 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | 6dd2da10-27e9-56f1-b3d1-653bef13909b, e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| sparse | top-30 | 0.0333 | 0.3333 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | 6dd2da10-27e9-56f1-b3d1-653bef13909b, e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| rrf | top-10 | 0.1000 | 0.3333 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | 6dd2da10-27e9-56f1-b3d1-653bef13909b, e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| rrf | top-20 | 0.1000 | 0.6667 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5, 6dd2da10-27e9-56f1-b3d1-653bef13909b | e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| rrf | top-30 | 0.0667 | 0.6667 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5, 6dd2da10-27e9-56f1-b3d1-653bef13909b | e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| reranked | top-10 | 0.1000 | 0.3333 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | 6dd2da10-27e9-56f1-b3d1-653bef13909b, e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| reranked | top-20 | 0.0500 | 0.3333 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5 | 6dd2da10-27e9-56f1-b3d1-653bef13909b, e59386b3-f3c6-5304-bc7c-712bfc002fdb |
| reranked | top-30 | 0.0667 | 0.6667 | 33cf6a4d-a0a7-5125-a9be-2899877f87b5, 6dd2da10-27e9-56f1-b3d1-653bef13909b | e59386b3-f3c6-5304-bc7c-712bfc002fdb |

### corpus-updating-clusters-2

Question: How does OpenShift Container Platform document Updating OpenShift Container Platform clusters?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | c220690a-f28c-5de3-8d65-879478616e14, 79af0c06-4004-54f6-833b-3e9aa1c61905 | d82698f5-1053-5d05-8a23-d2039e43a98d |
| dense | top-20 | 0.1500 | 1.0000 | c220690a-f28c-5de3-8d65-879478616e14, 79af0c06-4004-54f6-833b-3e9aa1c61905, d82698f5-1053-5d05-8a23-d2039e43a98d | - |
| dense | top-30 | 0.1000 | 1.0000 | c220690a-f28c-5de3-8d65-879478616e14, 79af0c06-4004-54f6-833b-3e9aa1c61905, d82698f5-1053-5d05-8a23-d2039e43a98d | - |
| sparse | top-10 | 0.1000 | 0.3333 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | c220690a-f28c-5de3-8d65-879478616e14, d82698f5-1053-5d05-8a23-d2039e43a98d |
| sparse | top-20 | 0.0500 | 0.3333 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | c220690a-f28c-5de3-8d65-879478616e14, d82698f5-1053-5d05-8a23-d2039e43a98d |
| sparse | top-30 | 0.0333 | 0.3333 | 79af0c06-4004-54f6-833b-3e9aa1c61905 | c220690a-f28c-5de3-8d65-879478616e14, d82698f5-1053-5d05-8a23-d2039e43a98d |
| rrf | top-10 | 0.2000 | 0.6667 | 79af0c06-4004-54f6-833b-3e9aa1c61905, c220690a-f28c-5de3-8d65-879478616e14 | d82698f5-1053-5d05-8a23-d2039e43a98d |
| rrf | top-20 | 0.1000 | 0.6667 | 79af0c06-4004-54f6-833b-3e9aa1c61905, c220690a-f28c-5de3-8d65-879478616e14 | d82698f5-1053-5d05-8a23-d2039e43a98d |
| rrf | top-30 | 0.1000 | 1.0000 | 79af0c06-4004-54f6-833b-3e9aa1c61905, c220690a-f28c-5de3-8d65-879478616e14, d82698f5-1053-5d05-8a23-d2039e43a98d | - |
| reranked | top-10 | 0.3000 | 1.0000 | d82698f5-1053-5d05-8a23-d2039e43a98d, 79af0c06-4004-54f6-833b-3e9aa1c61905, c220690a-f28c-5de3-8d65-879478616e14 | - |
| reranked | top-20 | 0.1500 | 1.0000 | d82698f5-1053-5d05-8a23-d2039e43a98d, 79af0c06-4004-54f6-833b-3e9aa1c61905, c220690a-f28c-5de3-8d65-879478616e14 | - |
| reranked | top-30 | 0.1000 | 1.0000 | d82698f5-1053-5d05-8a23-d2039e43a98d, 79af0c06-4004-54f6-833b-3e9aa1c61905, c220690a-f28c-5de3-8d65-879478616e14 | - |

### corpus-user-and-group-apis-2

Question: How does OpenShift Container Platform document Reference guide for user and group APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8, 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c | 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| dense | top-20 | 0.1000 | 0.6667 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8, 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c | 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| dense | top-30 | 0.0667 | 0.6667 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8, 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c | 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| sparse | top-10 | 0.1000 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| sparse | top-20 | 0.0500 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| sparse | top-30 | 0.0333 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| rrf | top-10 | 0.1000 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| rrf | top-20 | 0.0500 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| rrf | top-30 | 0.0667 | 0.6667 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8, 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c | 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| reranked | top-10 | 0.1000 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| reranked | top-20 | 0.0500 | 0.3333 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8 | 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c, 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |
| reranked | top-30 | 0.0667 | 0.6667 | c797f5eb-f966-5e34-b0dd-48f295bf7ea8, 7dc3c3ae-48e8-5dba-8a54-5eb676110e8c | 8c1bc9b6-4f4d-5cc7-a174-8b7d82693751 |

### corpus-validation-and-troubleshooting-2

Question: How does OpenShift Container Platform document Validating and troubleshooting an OpenShift Container Platform installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d, 8f9ebdd4-18de-56ae-8f3d-53456048e084 | - |
| dense | top-20 | 0.1500 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d, 8f9ebdd4-18de-56ae-8f3d-53456048e084 | - |
| dense | top-30 | 0.1000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d, 8f9ebdd4-18de-56ae-8f3d-53456048e084 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 8f9ebdd4-18de-56ae-8f3d-53456048e084 | 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d |
| sparse | top-20 | 0.1000 | 0.6667 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 8f9ebdd4-18de-56ae-8f3d-53456048e084 | 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d |
| sparse | top-30 | 0.0667 | 0.6667 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 8f9ebdd4-18de-56ae-8f3d-53456048e084 | 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d |
| rrf | top-10 | 0.3000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 8f9ebdd4-18de-56ae-8f3d-53456048e084, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d | - |
| rrf | top-20 | 0.1500 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 8f9ebdd4-18de-56ae-8f3d-53456048e084, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d | - |
| rrf | top-30 | 0.1000 | 1.0000 | 753a60db-8f0e-5d7a-9c4e-be68dfa84b51, 8f9ebdd4-18de-56ae-8f3d-53456048e084, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d | - |
| reranked | top-10 | 0.3000 | 1.0000 | 8f9ebdd4-18de-56ae-8f3d-53456048e084, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d, 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 8f9ebdd4-18de-56ae-8f3d-53456048e084, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d, 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 8f9ebdd4-18de-56ae-8f3d-53456048e084, 3c51d5e3-f129-5d01-a3be-a986fa3f8b2d, 753a60db-8f0e-5d7a-9c4e-be68dfa84b51 | - |

### corpus-virtualization-2

Question: How does OpenShift Container Platform document OpenShift Virtualization installation, usage, and release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| dense | top-20 | 0.0500 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| dense | top-30 | 0.0667 | 0.6667 | cac5e3ed-2125-5139-934f-4bba3b356e46, 453aa827-a901-563f-9dca-31bfe2c833a9 | 5d089bf7-2918-5133-86d9-141ef94679c9 |
| sparse | top-10 | 0.1000 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| sparse | top-20 | 0.1000 | 0.6667 | cac5e3ed-2125-5139-934f-4bba3b356e46, 5d089bf7-2918-5133-86d9-141ef94679c9 | 453aa827-a901-563f-9dca-31bfe2c833a9 |
| sparse | top-30 | 0.0667 | 0.6667 | cac5e3ed-2125-5139-934f-4bba3b356e46, 5d089bf7-2918-5133-86d9-141ef94679c9 | 453aa827-a901-563f-9dca-31bfe2c833a9 |
| rrf | top-10 | 0.1000 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| rrf | top-20 | 0.0500 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| rrf | top-30 | 0.0333 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| reranked | top-10 | 0.1000 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| reranked | top-20 | 0.0500 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |
| reranked | top-30 | 0.0333 | 0.3333 | cac5e3ed-2125-5139-934f-4bba3b356e46 | 453aa827-a901-563f-9dca-31bfe2c833a9, 5d089bf7-2918-5133-86d9-141ef94679c9 |

### corpus-virtualized-control-planes-2

Question: How does OpenShift Container Platform document Deploying OpenShift Container Platform clusters with virtualized control planes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09, 0a5c3513-6d4e-550f-91c3-9834ca62a046 | - |
| dense | top-20 | 0.1500 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09, 0a5c3513-6d4e-550f-91c3-9834ca62a046 | - |
| dense | top-30 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09, 0a5c3513-6d4e-550f-91c3-9834ca62a046 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 2b465229-4b29-59b8-affe-0073dff77f09, 5bd237dc-fe60-5300-8216-a9a657738707 | 0a5c3513-6d4e-550f-91c3-9834ca62a046 |
| sparse | top-20 | 0.1000 | 0.6667 | 2b465229-4b29-59b8-affe-0073dff77f09, 5bd237dc-fe60-5300-8216-a9a657738707 | 0a5c3513-6d4e-550f-91c3-9834ca62a046 |
| sparse | top-30 | 0.0667 | 0.6667 | 2b465229-4b29-59b8-affe-0073dff77f09, 5bd237dc-fe60-5300-8216-a9a657738707 | 0a5c3513-6d4e-550f-91c3-9834ca62a046 |
| rrf | top-10 | 0.2000 | 0.6667 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09 | 0a5c3513-6d4e-550f-91c3-9834ca62a046 |
| rrf | top-20 | 0.1500 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09, 0a5c3513-6d4e-550f-91c3-9834ca62a046 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09, 0a5c3513-6d4e-550f-91c3-9834ca62a046 | - |
| reranked | top-10 | 0.1000 | 0.3333 | 5bd237dc-fe60-5300-8216-a9a657738707 | 0a5c3513-6d4e-550f-91c3-9834ca62a046, 2b465229-4b29-59b8-affe-0073dff77f09 |
| reranked | top-20 | 0.1000 | 0.6667 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09 | 0a5c3513-6d4e-550f-91c3-9834ca62a046 |
| reranked | top-30 | 0.1000 | 1.0000 | 5bd237dc-fe60-5300-8216-a9a657738707, 2b465229-4b29-59b8-affe-0073dff77f09, 0a5c3513-6d4e-550f-91c3-9834ca62a046 | - |

### corpus-web-console-2

Question: How does OpenShift Container Platform document Getting started with the web console in OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 61c47b02-2d02-5f64-aed7-a59ce58b4c85, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | - |
| dense | top-20 | 0.1500 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 61c47b02-2d02-5f64-aed7-a59ce58b4c85, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | - |
| dense | top-30 | 0.1000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 61c47b02-2d02-5f64-aed7-a59ce58b4c85, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | - |
| sparse | top-10 | 0.2000 | 0.6667 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | 61c47b02-2d02-5f64-aed7-a59ce58b4c85 |
| sparse | top-20 | 0.1000 | 0.6667 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | 61c47b02-2d02-5f64-aed7-a59ce58b4c85 |
| sparse | top-30 | 0.0667 | 0.6667 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | 61c47b02-2d02-5f64-aed7-a59ce58b4c85 |
| rrf | top-10 | 0.2000 | 0.6667 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d | 61c47b02-2d02-5f64-aed7-a59ce58b4c85 |
| rrf | top-20 | 0.1500 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d, 61c47b02-2d02-5f64-aed7-a59ce58b4c85 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 9453b745-0975-5a6d-bba5-7de3b6b530d4, 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d, 61c47b02-2d02-5f64-aed7-a59ce58b4c85 | - |
| reranked | top-10 | 0.2000 | 0.6667 | 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d, 9453b745-0975-5a6d-bba5-7de3b6b530d4 | 61c47b02-2d02-5f64-aed7-a59ce58b4c85 |
| reranked | top-20 | 0.1000 | 0.6667 | 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d, 9453b745-0975-5a6d-bba5-7de3b6b530d4 | 61c47b02-2d02-5f64-aed7-a59ce58b4c85 |
| reranked | top-30 | 0.1000 | 1.0000 | 96a7cdfd-f40e-53bb-b5f2-cf1c81f0667d, 9453b745-0975-5a6d-bba5-7de3b6b530d4, 61c47b02-2d02-5f64-aed7-a59ce58b4c85 | - |

### corpus-windows-container-support-for-openshift-2

Question: How does OpenShift Container Platform document Red Hat OpenShift for Windows Containers Guide?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 7845e78c-66f1-5772-bacd-d813225b973b | e802bfc7-17f8-5333-8720-04b5eeeb8862, 123d0737-1813-5091-aa42-4c5ca522d515 |
| dense | top-20 | 0.1000 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| dense | top-30 | 0.0667 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| sparse | top-10 | 0.2000 | 0.6667 | 123d0737-1813-5091-aa42-4c5ca522d515, 7845e78c-66f1-5772-bacd-d813225b973b | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| sparse | top-20 | 0.1000 | 0.6667 | 123d0737-1813-5091-aa42-4c5ca522d515, 7845e78c-66f1-5772-bacd-d813225b973b | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| sparse | top-30 | 0.0667 | 0.6667 | 123d0737-1813-5091-aa42-4c5ca522d515, 7845e78c-66f1-5772-bacd-d813225b973b | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| rrf | top-10 | 0.2000 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| rrf | top-20 | 0.1000 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| rrf | top-30 | 0.0667 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| reranked | top-10 | 0.2000 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| reranked | top-20 | 0.1000 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |
| reranked | top-30 | 0.0667 | 0.6667 | 7845e78c-66f1-5772-bacd-d813225b973b, 123d0737-1813-5091-aa42-4c5ca522d515 | e802bfc7-17f8-5333-8720-04b5eeeb8862 |

### corpus-workloads-apis-2

Question: How does OpenShift Container Platform document Reference guide for workloads APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 349797a4-9fc0-5591-91bf-abfe954f3860, 8379d840-ce07-521a-b604-4134fbda1f6a | 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| dense | top-20 | 0.1000 | 0.6667 | 349797a4-9fc0-5591-91bf-abfe954f3860, 8379d840-ce07-521a-b604-4134fbda1f6a | 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| dense | top-30 | 0.0667 | 0.6667 | 349797a4-9fc0-5591-91bf-abfe954f3860, 8379d840-ce07-521a-b604-4134fbda1f6a | 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| sparse | top-10 | 0.1000 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| sparse | top-20 | 0.0500 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| sparse | top-30 | 0.0333 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| rrf | top-10 | 0.1000 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| rrf | top-20 | 0.0500 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| rrf | top-30 | 0.0667 | 0.6667 | 349797a4-9fc0-5591-91bf-abfe954f3860, 8379d840-ce07-521a-b604-4134fbda1f6a | 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| reranked | top-10 | 0.1000 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| reranked | top-20 | 0.0500 | 0.3333 | 349797a4-9fc0-5591-91bf-abfe954f3860 | 8379d840-ce07-521a-b604-4134fbda1f6a, 578db6bc-f6df-539d-b7bb-1abb22c4abfc |
| reranked | top-30 | 0.0667 | 0.6667 | 349797a4-9fc0-5591-91bf-abfe954f3860, 8379d840-ce07-521a-b604-4134fbda1f6a | 578db6bc-f6df-539d-b7bb-1abb22c4abfc |

### corpus-advanced-networking-3

Question: How does OpenShift Container Platform document Chapter1.Verifying connectivity to an endpoint?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| dense | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| dense | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 65b49d58-d7d6-52ff-acf0-481a962af645, 6d4c9a01-183d-5830-9f41-8f89f39755c9, f4594041-dbf1-50e6-b3ed-d45403416702 |

### corpus-ai-applications-3

Question: How does OpenShift Container Platform document 1.1.Inspect clusters with MCP server for Red Hat OpenShift?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 3482d303-ebe2-53e4-8802-d2a48390c159 |
| dense | top-20 | 0.1000 | 0.6667 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 3482d303-ebe2-53e4-8802-d2a48390c159 |
| dense | top-30 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |
| sparse | top-10 | 0.2000 | 0.6667 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 3482d303-ebe2-53e4-8802-d2a48390c159 |
| sparse | top-20 | 0.1000 | 0.6667 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 3482d303-ebe2-53e4-8802-d2a48390c159 |
| sparse | top-30 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |
| rrf | top-10 | 0.3000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |
| rrf | top-20 | 0.1500 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |
| rrf | top-30 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |
| reranked | top-10 | 0.2000 | 0.6667 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6 | 3482d303-ebe2-53e4-8802-d2a48390c159 |
| reranked | top-20 | 0.1500 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |
| reranked | top-30 | 0.1000 | 1.0000 | c0c06e55-c972-5a13-8aab-c2f87a25ec8e, e726cde9-bf0d-5424-a75d-b17f6c9455a6, 3482d303-ebe2-53e4-8802-d2a48390c159 | - |

### corpus-ai-workloads-3

Question: How does OpenShift Container Platform document Chapter1.Overview of AI workloads on OpenShift Container Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183 | d3a0d023-0e40-5957-b72f-1ea9ddafe953 |
| dense | top-20 | 0.1500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| dense | top-30 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| sparse | top-10 | 0.3000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| sparse | top-20 | 0.1500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| sparse | top-30 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| rrf | top-10 | 0.3000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 71d01548-21e2-522b-9121-1db05498f0d0, a797913b-3012-57a6-9136-972bda3f2183, d3a0d023-0e40-5957-b72f-1ea9ddafe953 | - |

### corpus-api-overview-3

Question: How does OpenShift Container Platform document Chapter1.Understanding API tiers?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | d144675a-71c4-573f-8cbf-a04b2f5c633c | cf634e33-3687-583b-89b6-cb69edce0a6b, e76f21b1-6e59-5d76-8010-bd5e01e02c92 |
| dense | top-20 | 0.0500 | 0.3333 | d144675a-71c4-573f-8cbf-a04b2f5c633c | cf634e33-3687-583b-89b6-cb69edce0a6b, e76f21b1-6e59-5d76-8010-bd5e01e02c92 |
| dense | top-30 | 0.0333 | 0.3333 | d144675a-71c4-573f-8cbf-a04b2f5c633c | cf634e33-3687-583b-89b6-cb69edce0a6b, e76f21b1-6e59-5d76-8010-bd5e01e02c92 |
| sparse | top-10 | 0.2000 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |
| sparse | top-20 | 0.1000 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |
| sparse | top-30 | 0.0667 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |
| rrf | top-10 | 0.1000 | 0.3333 | d144675a-71c4-573f-8cbf-a04b2f5c633c | cf634e33-3687-583b-89b6-cb69edce0a6b, e76f21b1-6e59-5d76-8010-bd5e01e02c92 |
| rrf | top-20 | 0.1000 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |
| rrf | top-30 | 0.0667 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |
| reranked | top-10 | 0.1000 | 0.3333 | d144675a-71c4-573f-8cbf-a04b2f5c633c | cf634e33-3687-583b-89b6-cb69edce0a6b, e76f21b1-6e59-5d76-8010-bd5e01e02c92 |
| reranked | top-20 | 0.1000 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |
| reranked | top-30 | 0.0667 | 0.6667 | d144675a-71c4-573f-8cbf-a04b2f5c633c, e76f21b1-6e59-5d76-8010-bd5e01e02c92 | cf634e33-3687-583b-89b6-cb69edce0a6b |

### corpus-architecture-3

Question: How does OpenShift Container Platform document Chapter1.Architecture overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| dense | top-20 | 0.1000 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| dense | top-30 | 0.0667 | 0.6667 | 5d6617ec-1789-5858-a380-aecc3c03aa2e, ab01e557-0ca7-5d92-9d50-15aa69408e1f | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| sparse | top-10 | 0.1000 | 0.3333 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | 5d6617ec-1789-5858-a380-aecc3c03aa2e, c48a6cb8-61de-5a70-ba35-dee71a47116d |
| sparse | top-20 | 0.0500 | 0.3333 | ab01e557-0ca7-5d92-9d50-15aa69408e1f | 5d6617ec-1789-5858-a380-aecc3c03aa2e, c48a6cb8-61de-5a70-ba35-dee71a47116d |
| sparse | top-30 | 0.0667 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| rrf | top-10 | 0.2000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| rrf | top-20 | 0.1000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| rrf | top-30 | 0.0667 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| reranked | top-10 | 0.2000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| reranked | top-20 | 0.1000 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |
| reranked | top-30 | 0.0667 | 0.6667 | ab01e557-0ca7-5d92-9d50-15aa69408e1f, 5d6617ec-1789-5858-a380-aecc3c03aa2e | c48a6cb8-61de-5a70-ba35-dee71a47116d |

### corpus-authentication-and-authorization-4

Question: How does OpenShift Container Platform document 1.1.Glossary of common terms for OpenShift Container Platform authentication and authorization?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| dense | top-20 | 0.0500 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| dense | top-30 | 0.0333 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| sparse | top-10 | 0.1000 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| sparse | top-20 | 0.0500 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| sparse | top-30 | 0.0333 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| rrf | top-10 | 0.1000 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| rrf | top-20 | 0.0500 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| rrf | top-30 | 0.0333 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| reranked | top-10 | 0.1000 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| reranked | top-20 | 0.0500 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |
| reranked | top-30 | 0.0333 | 0.3333 | 9ad4c260-fa42-59b8-80f6-a5d2eec5d3ca | 23e28d3f-dcaf-5ec1-a386-006cc026e538, 3f27d3a6-7915-51df-835b-9313d993f74a |

### corpus-authorization-apis-3

Question: How does OpenShift Container Platform document [1.1.LocalResourceAccessReview [authorization.openshift.io/v1]](#localresourceaccessreview-authorization-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 |
| dense | top-20 | 0.1500 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3, 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| dense | top-30 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3, 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| sparse | top-10 | 0.2000 | 0.6667 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 |
| sparse | top-20 | 0.1000 | 0.6667 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 |
| sparse | top-30 | 0.0667 | 0.6667 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 |
| rrf | top-10 | 0.2000 | 0.6667 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 |
| rrf | top-20 | 0.1500 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3, 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 6c2cca11-915e-54e6-8c61-ff468f462dc3, 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | - |
| reranked | top-10 | 0.1000 | 0.3333 | 4c15a7b6-b2f2-5163-941e-24d988f561e2 | 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 6c2cca11-915e-54e6-8c61-ff468f462dc3 |
| reranked | top-20 | 0.1000 | 0.6667 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 44a57bdf-2c38-5345-94ec-ac2bd9739fc6 | 6c2cca11-915e-54e6-8c61-ff468f462dc3 |
| reranked | top-30 | 0.1000 | 1.0000 | 4c15a7b6-b2f2-5163-941e-24d988f561e2, 44a57bdf-2c38-5345-94ec-ac2bd9739fc6, 6c2cca11-915e-54e6-8c61-ff468f462dc3 | - |

### corpus-autoscale-apis-3

Question: How does OpenShift Container Platform document [1.1.ClusterAutoscaler [autoscaling.openshift.io/v1]](#clusterautoscaler-autoscaling-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15 | 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| dense | top-20 | 0.1500 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 | - |
| dense | top-30 | 0.1000 | 1.0000 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| rrf | top-10 | 0.1000 | 0.3333 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6 | a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| rrf | top-20 | 0.1000 | 0.6667 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15 | 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| rrf | top-30 | 0.0667 | 0.6667 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15 | 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15, 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| reranked | top-20 | 0.1000 | 0.6667 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15 | 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |
| reranked | top-30 | 0.0667 | 0.6667 | 5762542d-ea9f-5f5f-8ebb-318cfd47dec6, a1b8eb78-2362-55b1-a776-eec474282f15 | 9963b6ee-1579-5b4a-9d5e-4ae5b0971f25 |

### corpus-backup-and-restore-3

Question: How does OpenShift Container Platform document Chapter1.Backup and restore?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| dense | top-20 | 0.1000 | 0.6667 | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| dense | top-30 | 0.1000 | 1.0000 | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f, 0a3cad35-252c-5dc6-b5a4-a15e82baf07a | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f, 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| sparse | top-20 | 0.0000 | 0.0000 | - | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f, 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| sparse | top-30 | 0.0333 | 0.3333 | 987380f9-f164-5728-9141-559790cb7069 | c681963c-27bb-5e4f-8461-bb49c966506f, 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| rrf | top-10 | 0.2000 | 0.6667 | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| rrf | top-20 | 0.1000 | 0.6667 | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| rrf | top-30 | 0.0667 | 0.6667 | 987380f9-f164-5728-9141-559790cb7069, c681963c-27bb-5e4f-8461-bb49c966506f | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| reranked | top-10 | 0.2000 | 0.6667 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| reranked | top-20 | 0.1000 | 0.6667 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |
| reranked | top-30 | 0.0667 | 0.6667 | c681963c-27bb-5e4f-8461-bb49c966506f, 987380f9-f164-5728-9141-559790cb7069 | 0a3cad35-252c-5dc6-b5a4-a15e82baf07a |

### corpus-building-applications-3

Question: How does OpenShift Container Platform document Chapter1.Building applications overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| dense | top-20 | 0.1000 | 0.6667 | cd7122bd-4861-5907-8a1b-a5f318b19d8f, 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| dense | top-30 | 0.0667 | 0.6667 | cd7122bd-4861-5907-8a1b-a5f318b19d8f, 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| sparse | top-10 | 0.1000 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| sparse | top-20 | 0.0500 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| sparse | top-30 | 0.0333 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| rrf | top-10 | 0.1000 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| rrf | top-20 | 0.0500 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| rrf | top-30 | 0.0667 | 0.6667 | cd7122bd-4861-5907-8a1b-a5f318b19d8f, 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| reranked | top-10 | 0.1000 | 0.3333 | cd7122bd-4861-5907-8a1b-a5f318b19d8f | 46ed4ef1-971b-508b-93fd-17193a7ca6a9, b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| reranked | top-20 | 0.1000 | 0.6667 | cd7122bd-4861-5907-8a1b-a5f318b19d8f, 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |
| reranked | top-30 | 0.0667 | 0.6667 | cd7122bd-4861-5907-8a1b-a5f318b19d8f, 46ed4ef1-971b-508b-93fd-17193a7ca6a9 | b5edd600-4beb-5d7b-9da8-5da3aa1ce057 |

### corpus-builds-using-buildconfig-5

Question: How does OpenShift Container Platform document 1.1.1.Docker build?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| dense | top-20 | 0.0500 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| dense | top-30 | 0.0333 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| sparse | top-10 | 0.1000 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| sparse | top-20 | 0.0500 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| sparse | top-30 | 0.0333 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| rrf | top-10 | 0.1000 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| rrf | top-20 | 0.0500 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| rrf | top-30 | 0.0333 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| reranked | top-10 | 0.1000 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| reranked | top-20 | 0.0500 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |
| reranked | top-30 | 0.0333 | 0.3333 | 2de9267a-6b39-545f-91ae-0e7833009f30 | bbc0c4e4-7ab9-5f16-931b-2c5c0aee9313, 2eba68ef-50e3-58ce-9a5a-db00f45447d4 |

### corpus-builds-using-shipwright-3

Question: How does OpenShift Container Platform document Chapter1.Overview of Builds?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 46a7a803-992a-5640-a45a-7b08981d6c6f, 0e53378e-3fa4-5aba-833a-809b7c5772da | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| dense | top-20 | 0.1000 | 0.6667 | 46a7a803-992a-5640-a45a-7b08981d6c6f, 0e53378e-3fa4-5aba-833a-809b7c5772da | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| dense | top-30 | 0.0667 | 0.6667 | 46a7a803-992a-5640-a45a-7b08981d6c6f, 0e53378e-3fa4-5aba-833a-809b7c5772da | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| sparse | top-10 | 0.1000 | 0.3333 | 0e53378e-3fa4-5aba-833a-809b7c5772da | 46a7a803-992a-5640-a45a-7b08981d6c6f, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| sparse | top-20 | 0.0500 | 0.3333 | 0e53378e-3fa4-5aba-833a-809b7c5772da | 46a7a803-992a-5640-a45a-7b08981d6c6f, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| sparse | top-30 | 0.0333 | 0.3333 | 0e53378e-3fa4-5aba-833a-809b7c5772da | 46a7a803-992a-5640-a45a-7b08981d6c6f, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| rrf | top-10 | 0.1000 | 0.3333 | 0e53378e-3fa4-5aba-833a-809b7c5772da | 46a7a803-992a-5640-a45a-7b08981d6c6f, 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| rrf | top-20 | 0.1000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 46a7a803-992a-5640-a45a-7b08981d6c6f | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| rrf | top-30 | 0.0667 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 46a7a803-992a-5640-a45a-7b08981d6c6f | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| reranked | top-10 | 0.2000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 46a7a803-992a-5640-a45a-7b08981d6c6f | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| reranked | top-20 | 0.1000 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 46a7a803-992a-5640-a45a-7b08981d6c6f | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |
| reranked | top-30 | 0.0667 | 0.6667 | 0e53378e-3fa4-5aba-833a-809b7c5772da, 46a7a803-992a-5640-a45a-7b08981d6c6f | 651ddd99-c2f9-5793-9e46-b15f6c2bd6b9 |

### corpus-cicd-overview-3

Question: How does OpenShift Container Platform document Chapter1.About CI/CD?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| dense | top-20 | 0.1000 | 0.6667 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| dense | top-30 | 0.0667 | 0.6667 | dcc1119a-ff32-555e-b9ef-23a471e4add8, 4551cb38-96c0-57de-8031-43f7b29a54e7 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| sparse | top-10 | 0.2000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| sparse | top-20 | 0.1000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| sparse | top-30 | 0.0667 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| rrf | top-10 | 0.2000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| rrf | top-20 | 0.1000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| rrf | top-30 | 0.0667 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| reranked | top-10 | 0.2000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| reranked | top-20 | 0.1000 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |
| reranked | top-30 | 0.0667 | 0.6667 | 4551cb38-96c0-57de-8031-43f7b29a54e7, dcc1119a-ff32-555e-b9ef-23a471e4add8 | cd644686-d565-53fb-9cf6-582e140e1b42 |

### corpus-cli-tools-3

Question: How does OpenShift Container Platform document Chapter1.OpenShift Container Platform CLI tools overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | ea5aedb2-9bff-52f6-9547-a16547811b9a |
| dense | top-20 | 0.1500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, 2b2b0165-aa9f-52a9-a006-92c1706043a0, ea5aedb2-9bff-52f6-9547-a16547811b9a | - |
| dense | top-30 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, 2b2b0165-aa9f-52a9-a006-92c1706043a0, ea5aedb2-9bff-52f6-9547-a16547811b9a | - |
| sparse | top-10 | 0.3000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, ea5aedb2-9bff-52f6-9547-a16547811b9a, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| sparse | top-20 | 0.1500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, ea5aedb2-9bff-52f6-9547-a16547811b9a, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| sparse | top-30 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, ea5aedb2-9bff-52f6-9547-a16547811b9a, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| rrf | top-10 | 0.3000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, 2b2b0165-aa9f-52a9-a006-92c1706043a0, ea5aedb2-9bff-52f6-9547-a16547811b9a | - |
| rrf | top-20 | 0.1500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, 2b2b0165-aa9f-52a9-a006-92c1706043a0, ea5aedb2-9bff-52f6-9547-a16547811b9a | - |
| rrf | top-30 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, 2b2b0165-aa9f-52a9-a006-92c1706043a0, ea5aedb2-9bff-52f6-9547-a16547811b9a | - |
| reranked | top-10 | 0.3000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, ea5aedb2-9bff-52f6-9547-a16547811b9a, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, ea5aedb2-9bff-52f6-9547-a16547811b9a, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 9cfedc56-d40b-5d64-b436-39dc7dbcb977, ea5aedb2-9bff-52f6-9547-a16547811b9a, 2b2b0165-aa9f-52a9-a006-92c1706043a0 | - |

### corpus-cluster-apis-3

Question: How does OpenShift Container Platform document [1.1.IPAddress [ipam.cluster.x-k8s.io/v1beta1]](#ipaddress-ipam-cluster-x-k8s-iov1beta1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| dense | top-20 | 0.1000 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| dense | top-30 | 0.0667 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| sparse | top-10 | 0.2000 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| sparse | top-20 | 0.1000 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| sparse | top-30 | 0.0667 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| rrf | top-10 | 0.2000 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| rrf | top-20 | 0.1000 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| rrf | top-30 | 0.0667 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, e6c41450-0fe1-5753-9fb5-c60da524ab45, d33123c6-06eb-5b06-b74f-cfd1fd84a44b |
| reranked | top-20 | 0.0500 | 0.3333 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3 | e6c41450-0fe1-5753-9fb5-c60da524ab45, d33123c6-06eb-5b06-b74f-cfd1fd84a44b |
| reranked | top-30 | 0.0667 | 0.6667 | 23b5ad5e-68c7-5fd3-b68a-907302c8ecd3, d33123c6-06eb-5b06-b74f-cfd1fd84a44b | e6c41450-0fe1-5753-9fb5-c60da524ab45 |

### corpus-cluster-observability-operator-3

Question: How does OpenShift Container Platform document Chapter1.Cluster Observability Operator overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| dense | top-20 | 0.1000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| dense | top-30 | 0.0667 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| sparse | top-10 | 0.1000 | 0.3333 | 6f68f926-1ee0-509b-bef1-5b795511d222 | f1dec798-b76b-5158-95fe-8da4a66f6378, 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| sparse | top-20 | 0.0500 | 0.3333 | 6f68f926-1ee0-509b-bef1-5b795511d222 | f1dec798-b76b-5158-95fe-8da4a66f6378, 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| sparse | top-30 | 0.0667 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| rrf | top-10 | 0.2000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| rrf | top-20 | 0.1000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| rrf | top-30 | 0.0667 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| reranked | top-10 | 0.2000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| reranked | top-20 | 0.1000 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |
| reranked | top-30 | 0.0667 | 0.6667 | 6f68f926-1ee0-509b-bef1-5b795511d222, f1dec798-b76b-5158-95fe-8da4a66f6378 | 6eac6b90-b21a-5756-b7fb-84f200568bb2 |

### corpus-common-object-reference-3

Question: How does OpenShift Container Platform document 1.1.com.coreos.monitoring.v1.AlertmanagerList schema?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 62ca7e8e-a532-595a-b048-bb0a9347c11b |
| dense | top-20 | 0.0500 | 0.3333 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 62ca7e8e-a532-595a-b048-bb0a9347c11b |
| dense | top-30 | 0.0333 | 0.3333 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 62ca7e8e-a532-595a-b048-bb0a9347c11b |
| sparse | top-10 | 0.2000 | 0.6667 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc, 62ca7e8e-a532-595a-b048-bb0a9347c11b | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| sparse | top-20 | 0.1000 | 0.6667 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc, 62ca7e8e-a532-595a-b048-bb0a9347c11b | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| sparse | top-30 | 0.0667 | 0.6667 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc, 62ca7e8e-a532-595a-b048-bb0a9347c11b | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| rrf | top-10 | 0.1000 | 0.3333 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e, 62ca7e8e-a532-595a-b048-bb0a9347c11b |
| rrf | top-20 | 0.1000 | 0.6667 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc, 62ca7e8e-a532-595a-b048-bb0a9347c11b | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| rrf | top-30 | 0.0667 | 0.6667 | ed9f6bcc-46f1-502b-acc1-56687d16b3fc, 62ca7e8e-a532-595a-b048-bb0a9347c11b | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| reranked | top-10 | 0.2000 | 0.6667 | 62ca7e8e-a532-595a-b048-bb0a9347c11b, ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| reranked | top-20 | 0.1000 | 0.6667 | 62ca7e8e-a532-595a-b048-bb0a9347c11b, ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e |
| reranked | top-30 | 0.0667 | 0.6667 | 62ca7e8e-a532-595a-b048-bb0a9347c11b, ed9f6bcc-46f1-502b-acc1-56687d16b3fc | 63aec8a6-33ce-57c7-8afb-06b3c690600e |

### corpus-config-apis-3

Question: How does OpenShift Container Platform document [1.1.APIServer [config.openshift.io/v1]](#apiserver-config-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| dense | top-20 | 0.1000 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| dense | top-30 | 0.0667 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| sparse | top-10 | 0.1000 | 0.3333 | fcae96e9-3a23-518d-b191-69ebf26ea43e | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| sparse | top-20 | 0.0500 | 0.3333 | fcae96e9-3a23-518d-b191-69ebf26ea43e | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| sparse | top-30 | 0.0333 | 0.3333 | fcae96e9-3a23-518d-b191-69ebf26ea43e | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| rrf | top-10 | 0.2000 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| rrf | top-20 | 0.1000 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| rrf | top-30 | 0.0667 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| reranked | top-10 | 0.1000 | 0.3333 | fcae96e9-3a23-518d-b191-69ebf26ea43e | d1ae4432-c7b0-5506-9f50-c7c205b96dba, 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| reranked | top-20 | 0.1000 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |
| reranked | top-30 | 0.0667 | 0.6667 | fcae96e9-3a23-518d-b191-69ebf26ea43e, d1ae4432-c7b0-5506-9f50-c7c205b96dba | 892e87cf-fb30-5b78-a296-bd5e7dc6ee01 |

### corpus-configuring-network-settings-3

Question: How does OpenShift Container Platform document Chapter1.Configuring system controls and interface attributes using the tuning plugin?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| dense | top-20 | 0.1000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| dense | top-30 | 0.0667 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| sparse | top-10 | 0.2000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| sparse | top-20 | 0.1000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| sparse | top-30 | 0.0667 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| rrf | top-10 | 0.2000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| rrf | top-20 | 0.1000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| rrf | top-30 | 0.0667 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| reranked | top-10 | 0.2000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| reranked | top-20 | 0.1000 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |
| reranked | top-30 | 0.0667 | 0.6667 | aea45e71-8964-5bc3-92e7-e6557d60dc8d, 43204b30-bbef-5bcf-bcc3-69e410794ecb | f741081f-2b5f-54db-9d54-dfb08627f439 |

### corpus-console-apis-3

Question: How does OpenShift Container Platform document [1.1.ConsoleCLIDownload [console.openshift.io/v1]](#consoleclidownload-console-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| dense | top-20 | 0.0500 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| dense | top-30 | 0.0333 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| sparse | top-10 | 0.1000 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| sparse | top-20 | 0.0500 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| sparse | top-30 | 0.0333 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| rrf | top-10 | 0.1000 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| rrf | top-20 | 0.0500 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| rrf | top-30 | 0.0333 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| reranked | top-10 | 0.1000 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| reranked | top-20 | 0.0500 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |
| reranked | top-30 | 0.0333 | 0.3333 | c0e865ae-7f68-5a5c-bc65-bdab3d323a40 | d34a1045-05a4-510b-a425-080bc74f6631, 1a2e2aa8-459a-51f6-bae3-6540ef3f83e6 |

### corpus-disconnected-environments-3

Question: How does OpenShift Container Platform document Chapter1.About disconnected environments?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| dense | top-20 | 0.1500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| dense | top-30 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| sparse | top-10 | 0.2000 | 0.6667 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4 | 7e211c51-03f5-54f6-8607-ac63e70aabcf |
| sparse | top-20 | 0.1000 | 0.6667 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4 | 7e211c51-03f5-54f6-8607-ac63e70aabcf |
| sparse | top-30 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| rrf | top-10 | 0.3000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| rrf | top-20 | 0.1500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| rrf | top-30 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| reranked | top-10 | 0.3000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| reranked | top-20 | 0.1500 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |
| reranked | top-30 | 0.1000 | 1.0000 | 68515748-db0c-5456-9cf2-961351082f54, 1f6fa27c-2a73-5b45-a355-1cfdd0c4b3b4, 7e211c51-03f5-54f6-8607-ac63e70aabcf | - |

### corpus-distributed-tracing-3

Question: How does OpenShift Container Platform document Chapter1.About the Distributed Tracing Platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| dense | top-20 | 0.1000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| dense | top-30 | 0.0667 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 6e4201b7-d7fe-5df7-af44-c33f9721fd38, 8da37ae7-1013-5b0f-ae45-6e805645052c, 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 6e4201b7-d7fe-5df7-af44-c33f9721fd38, 8da37ae7-1013-5b0f-ae45-6e805645052c, 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| sparse | top-30 | 0.0333 | 0.3333 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| rrf | top-10 | 0.1000 | 0.3333 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| rrf | top-20 | 0.1000 | 0.6667 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38, 8da37ae7-1013-5b0f-ae45-6e805645052c | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| rrf | top-30 | 0.0667 | 0.6667 | 6e4201b7-d7fe-5df7-af44-c33f9721fd38, 8da37ae7-1013-5b0f-ae45-6e805645052c | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| reranked | top-10 | 0.2000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| reranked | top-20 | 0.1000 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |
| reranked | top-30 | 0.0667 | 0.6667 | 8da37ae7-1013-5b0f-ae45-6e805645052c, 6e4201b7-d7fe-5df7-af44-c33f9721fd38 | 5f4bda0f-7180-56cd-ba4b-0629e4d54f50 |

### corpus-edge-computing-3

Question: How does OpenShift Container Platform document Chapter1.Challenges of the network far edge?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d, bcf031a4-3bc3-588f-8991-a5ff425f8b21 |
| dense | top-20 | 0.0500 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d, bcf031a4-3bc3-588f-8991-a5ff425f8b21 |
| dense | top-30 | 0.0333 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d, bcf031a4-3bc3-588f-8991-a5ff425f8b21 |
| sparse | top-10 | 0.2000 | 0.6667 | e97055d6-6c2e-5b45-91e5-756f86b959d4, bcf031a4-3bc3-588f-8991-a5ff425f8b21 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-20 | 0.1000 | 0.6667 | e97055d6-6c2e-5b45-91e5-756f86b959d4, bcf031a4-3bc3-588f-8991-a5ff425f8b21 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| sparse | top-30 | 0.0667 | 0.6667 | e97055d6-6c2e-5b45-91e5-756f86b959d4, bcf031a4-3bc3-588f-8991-a5ff425f8b21 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-10 | 0.1000 | 0.3333 | e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d, bcf031a4-3bc3-588f-8991-a5ff425f8b21 |
| rrf | top-20 | 0.1000 | 0.6667 | e97055d6-6c2e-5b45-91e5-756f86b959d4, bcf031a4-3bc3-588f-8991-a5ff425f8b21 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| rrf | top-30 | 0.0667 | 0.6667 | e97055d6-6c2e-5b45-91e5-756f86b959d4, bcf031a4-3bc3-588f-8991-a5ff425f8b21 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-10 | 0.2000 | 0.6667 | bcf031a4-3bc3-588f-8991-a5ff425f8b21, e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-20 | 0.1000 | 0.6667 | bcf031a4-3bc3-588f-8991-a5ff425f8b21, e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |
| reranked | top-30 | 0.0667 | 0.6667 | bcf031a4-3bc3-588f-8991-a5ff425f8b21, e97055d6-6c2e-5b45-91e5-756f86b959d4 | 9308a0d4-28b9-54a9-9d9f-5ff368a8de2d |

### corpus-etcd-3

Question: How does OpenShift Container Platform document Chapter1.Overview of etcd?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024 | a784dac3-035e-5dc1-a4b8-157f99fdd246 |
| dense | top-20 | 0.1500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 | - |
| dense | top-30 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 | - |
| sparse | top-10 | 0.1000 | 0.3333 | cb07bd4f-f6dd-5575-813a-757a481cef52 | fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 |
| sparse | top-20 | 0.1000 | 0.6667 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024 | a784dac3-035e-5dc1-a4b8-157f99fdd246 |
| sparse | top-30 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 | - |
| rrf | top-10 | 0.3000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 | - |
| rrf | top-20 | 0.1500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 | - |
| rrf | top-30 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, fb807836-6f26-5dfd-9d71-c283e2cfa024, a784dac3-035e-5dc1-a4b8-157f99fdd246 | - |
| reranked | top-10 | 0.3000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, a784dac3-035e-5dc1-a4b8-157f99fdd246, fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| reranked | top-20 | 0.1500 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, a784dac3-035e-5dc1-a4b8-157f99fdd246, fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |
| reranked | top-30 | 0.1000 | 1.0000 | cb07bd4f-f6dd-5575-813a-757a481cef52, a784dac3-035e-5dc1-a4b8-157f99fdd246, fb807836-6f26-5dfd-9d71-c283e2cfa024 | - |

### corpus-extension-apis-3

Question: How does OpenShift Container Platform document [1.1.APIService [apiregistration.k8s.io/v1]](#apiservice-apiregistration-k8s-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| dense | top-20 | 0.0500 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| dense | top-30 | 0.0333 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| sparse | top-10 | 0.1000 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| sparse | top-20 | 0.0500 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| sparse | top-30 | 0.0333 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| rrf | top-10 | 0.1000 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| rrf | top-20 | 0.0500 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| rrf | top-30 | 0.0333 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 58322bfd-1625-56fe-a131-f476ab75678f, 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| reranked | top-20 | 0.0500 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |
| reranked | top-30 | 0.0333 | 0.3333 | 58322bfd-1625-56fe-a131-f476ab75678f | 449b3edc-5522-55e3-a06b-5a1fb60fd2f3, 73fa8995-338c-5591-a992-1f5a49b15893 |

### corpus-extensions-3

Question: How does OpenShift Container Platform document Chapter1.Extensions overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 3e0957c9-d14c-5f36-b2f0-812bf71282af, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 5378e601-dcdd-52ca-b420-1cfccba0d77b |
| dense | top-20 | 0.1000 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | 5378e601-dcdd-52ca-b420-1cfccba0d77b |
| dense | top-30 | 0.0667 | 0.6667 | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 3e0957c9-d14c-5f36-b2f0-812bf71282af | 5378e601-dcdd-52ca-b420-1cfccba0d77b |
| sparse | top-10 | 0.1000 | 0.3333 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 5378e601-dcdd-52ca-b420-1cfccba0d77b |
| sparse | top-20 | 0.1000 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e |
| sparse | top-30 | 0.0667 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e |
| rrf | top-10 | 0.1000 | 0.3333 | 3e0957c9-d14c-5f36-b2f0-812bf71282af | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e, 5378e601-dcdd-52ca-b420-1cfccba0d77b |
| rrf | top-20 | 0.1000 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e |
| rrf | top-30 | 0.1000 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| reranked | top-10 | 0.2000 | 0.6667 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b | f7817d29-59cb-5e7e-8c38-3b93eadbaa9e |
| reranked | top-20 | 0.1500 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |
| reranked | top-30 | 0.1000 | 1.0000 | 3e0957c9-d14c-5f36-b2f0-812bf71282af, 5378e601-dcdd-52ca-b420-1cfccba0d77b, f7817d29-59cb-5e7e-8c38-3b93eadbaa9e | - |

### corpus-gitops-3

Question: How does OpenShift Container Platform document Chapter1.About RedHat OpenShift GitOps?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| dense | top-20 | 0.0500 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| dense | top-30 | 0.0333 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| sparse | top-10 | 0.1000 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| sparse | top-20 | 0.0500 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| sparse | top-30 | 0.0333 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| rrf | top-10 | 0.1000 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| rrf | top-20 | 0.0500 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| rrf | top-30 | 0.0333 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| reranked | top-10 | 0.1000 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| reranked | top-20 | 0.0500 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |
| reranked | top-30 | 0.0333 | 0.3333 | 18955a40-b23d-5dcc-8425-a7b36e22dcac | 7439a5de-4091-5974-bb6e-d2e28ecfe3c4, 1f899c2d-8cf2-5362-8f48-20e2eac67922 |

### corpus-hardware-accelerators-3

Question: How does OpenShift Container Platform document Chapter1.About hardware accelerators?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| dense | top-20 | 0.1000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| dense | top-30 | 0.0667 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| sparse | top-10 | 0.2000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| sparse | top-20 | 0.1000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| sparse | top-30 | 0.0667 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| rrf | top-10 | 0.2000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| rrf | top-20 | 0.1000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| rrf | top-30 | 0.0667 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| reranked | top-10 | 0.2000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| reranked | top-20 | 0.1000 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |
| reranked | top-30 | 0.0667 | 0.6667 | d6f5f6ff-5877-5a34-bb11-076d08ecf7ac, ec5ca1c4-aab7-5482-b3c6-e9f6574b67e3 | f5862fe3-fcfe-5b90-b2c5-8a306721abf3 |

### corpus-hardware-networks-3

Question: How does OpenShift Container Platform document Chapter1.About Single Root I/O Virtualization (SR-IOV) hardware networks?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | bdb22800-7a69-5c79-a968-d64045535da1 | b8e05d8e-8e34-5fdb-96c4-e9066114bee2, 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| dense | top-20 | 0.1000 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| dense | top-30 | 0.0667 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| sparse | top-10 | 0.1000 | 0.3333 | bdb22800-7a69-5c79-a968-d64045535da1 | b8e05d8e-8e34-5fdb-96c4-e9066114bee2, 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| sparse | top-20 | 0.1000 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| sparse | top-30 | 0.0667 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| rrf | top-10 | 0.1000 | 0.3333 | bdb22800-7a69-5c79-a968-d64045535da1 | b8e05d8e-8e34-5fdb-96c4-e9066114bee2, 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| rrf | top-20 | 0.1000 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| rrf | top-30 | 0.0667 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| reranked | top-10 | 0.1000 | 0.3333 | bdb22800-7a69-5c79-a968-d64045535da1 | b8e05d8e-8e34-5fdb-96c4-e9066114bee2, 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| reranked | top-20 | 0.0500 | 0.3333 | bdb22800-7a69-5c79-a968-d64045535da1 | b8e05d8e-8e34-5fdb-96c4-e9066114bee2, 0cd55560-0e37-522e-93c1-6df2473fa5c8 |
| reranked | top-30 | 0.0667 | 0.6667 | bdb22800-7a69-5c79-a968-d64045535da1, b8e05d8e-8e34-5fdb-96c4-e9066114bee2 | 0cd55560-0e37-522e-93c1-6df2473fa5c8 |

### corpus-hosted-control-planes-3

Question: How does OpenShift Container Platform document Chapter1.Hosted control planes release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| dense | top-20 | 0.1000 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| dense | top-30 | 0.0667 | 0.6667 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| sparse | top-10 | 0.1000 | 0.3333 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| sparse | top-20 | 0.0500 | 0.3333 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| sparse | top-30 | 0.0333 | 0.3333 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| rrf | top-10 | 0.1000 | 0.3333 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1 | 97f14b7e-6fb9-5af9-8482-baa185da9db8, 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| rrf | top-20 | 0.1000 | 0.6667 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 97f14b7e-6fb9-5af9-8482-baa185da9db8 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| rrf | top-30 | 0.0667 | 0.6667 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 97f14b7e-6fb9-5af9-8482-baa185da9db8 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| reranked | top-10 | 0.2000 | 0.6667 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 97f14b7e-6fb9-5af9-8482-baa185da9db8 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| reranked | top-20 | 0.1000 | 0.6667 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 97f14b7e-6fb9-5af9-8482-baa185da9db8 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |
| reranked | top-30 | 0.0667 | 0.6667 | 80f9e716-60f8-5b7e-9aea-0fc5ff201ae1, 97f14b7e-6fb9-5af9-8482-baa185da9db8 | 99151ff3-4779-59ca-9a72-0b68a3827ecb |

### corpus-image-apis-3

Question: How does OpenShift Container Platform document [1.1.Image [image.openshift.io/v1]](#image-image-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| dense | top-20 | 0.1000 | 0.6667 | 72451032-9898-5f5f-b16f-6b0d650284b7, 208c1b5c-e26e-577e-9169-0a3f600a3b20 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf |
| dense | top-30 | 0.1000 | 1.0000 | 72451032-9898-5f5f-b16f-6b0d650284b7, 208c1b5c-e26e-577e-9169-0a3f600a3b20, 01378752-bcba-5b40-bbb5-a9e4f21f26cf | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 72451032-9898-5f5f-b16f-6b0d650284b7, 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| sparse | top-20 | 0.0500 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| sparse | top-30 | 0.0333 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| rrf | top-10 | 0.1000 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| rrf | top-20 | 0.0500 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| rrf | top-30 | 0.0333 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| reranked | top-10 | 0.1000 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| reranked | top-20 | 0.0500 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |
| reranked | top-30 | 0.0333 | 0.3333 | 72451032-9898-5f5f-b16f-6b0d650284b7 | 01378752-bcba-5b40-bbb5-a9e4f21f26cf, 208c1b5c-e26e-577e-9169-0a3f600a3b20 |

### corpus-images-3

Question: How does OpenShift Container Platform document Chapter1.Overview of images?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | e2fd35a2-190a-5d03-8956-91faa514385a, af708316-1315-5b66-8fb8-0ed4138a5aa9 | 2d37dd44-deed-5a47-bb08-772676b96949 |
| dense | top-20 | 0.1500 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a, af708316-1315-5b66-8fb8-0ed4138a5aa9, 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| dense | top-30 | 0.1000 | 1.0000 | e2fd35a2-190a-5d03-8956-91faa514385a, af708316-1315-5b66-8fb8-0ed4138a5aa9, 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| sparse | top-10 | 0.1000 | 0.3333 | af708316-1315-5b66-8fb8-0ed4138a5aa9 | e2fd35a2-190a-5d03-8956-91faa514385a, 2d37dd44-deed-5a47-bb08-772676b96949 |
| sparse | top-20 | 0.0500 | 0.3333 | af708316-1315-5b66-8fb8-0ed4138a5aa9 | e2fd35a2-190a-5d03-8956-91faa514385a, 2d37dd44-deed-5a47-bb08-772676b96949 |
| sparse | top-30 | 0.0667 | 0.6667 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a | 2d37dd44-deed-5a47-bb08-772676b96949 |
| rrf | top-10 | 0.2000 | 0.6667 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a | 2d37dd44-deed-5a47-bb08-772676b96949 |
| rrf | top-20 | 0.1000 | 0.6667 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a | 2d37dd44-deed-5a47-bb08-772676b96949 |
| rrf | top-30 | 0.1000 | 1.0000 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a, 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| reranked | top-10 | 0.2000 | 0.6667 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a | 2d37dd44-deed-5a47-bb08-772676b96949 |
| reranked | top-20 | 0.1500 | 1.0000 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a, 2d37dd44-deed-5a47-bb08-772676b96949 | - |
| reranked | top-30 | 0.1000 | 1.0000 | af708316-1315-5b66-8fb8-0ed4138a5aa9, e2fd35a2-190a-5d03-8956-91faa514385a, 2d37dd44-deed-5a47-bb08-772676b96949 | - |

### corpus-ingress-and-load-balancing-4

Question: How does OpenShift Container Platform document 1.1.1.Creating an HTTP-based route?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| dense | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| dense | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| sparse | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| sparse | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| sparse | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| rrf | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| rrf | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| rrf | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| reranked | top-10 | 0.1000 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| reranked | top-20 | 0.0500 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |
| reranked | top-30 | 0.0333 | 0.3333 | b074fe5e-bace-5d0f-a5ad-e118ce361ea6 | d41fc628-126f-531c-bf39-087e82a256c4, aa60d887-7e83-5a12-81b8-408f7f0ce5c8 |

### corpus-installation-configuration-3

Question: How does OpenShift Container Platform document Chapter1.Customizing nodes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| dense | top-20 | 0.0500 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| dense | top-30 | 0.0333 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| sparse | top-10 | 0.1000 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| sparse | top-20 | 0.0500 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| sparse | top-30 | 0.0333 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| rrf | top-10 | 0.1000 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| rrf | top-20 | 0.0500 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| rrf | top-30 | 0.0333 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| reranked | top-10 | 0.1000 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| reranked | top-20 | 0.0500 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |
| reranked | top-30 | 0.0333 | 0.3333 | 694fea6c-6083-5316-af7e-9a63a535ad3b | e67a501e-c58e-56ac-b490-6080c3ff7167, 28e9a156-fe5a-5426-b334-6dab60337bb4 |

### corpus-installation-overview-3

Question: How does OpenShift Container Platform document Chapter1.OpenShift Container Platform installation overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, f25095ff-907e-572c-81b5-94d064e72277 | ebe67615-643a-582e-bb23-9394781fae67 |
| dense | top-20 | 0.1000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, f25095ff-907e-572c-81b5-94d064e72277 | ebe67615-643a-582e-bb23-9394781fae67 |
| dense | top-30 | 0.0667 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, f25095ff-907e-572c-81b5-94d064e72277 | ebe67615-643a-582e-bb23-9394781fae67 |
| sparse | top-10 | 0.1000 | 0.3333 | f25095ff-907e-572c-81b5-94d064e72277 | 52c58389-178b-5c15-8ed0-c686feaea548, ebe67615-643a-582e-bb23-9394781fae67 |
| sparse | top-20 | 0.1000 | 0.6667 | f25095ff-907e-572c-81b5-94d064e72277, ebe67615-643a-582e-bb23-9394781fae67 | 52c58389-178b-5c15-8ed0-c686feaea548 |
| sparse | top-30 | 0.0667 | 0.6667 | f25095ff-907e-572c-81b5-94d064e72277, ebe67615-643a-582e-bb23-9394781fae67 | 52c58389-178b-5c15-8ed0-c686feaea548 |
| rrf | top-10 | 0.2000 | 0.6667 | f25095ff-907e-572c-81b5-94d064e72277, 52c58389-178b-5c15-8ed0-c686feaea548 | ebe67615-643a-582e-bb23-9394781fae67 |
| rrf | top-20 | 0.1000 | 0.6667 | f25095ff-907e-572c-81b5-94d064e72277, 52c58389-178b-5c15-8ed0-c686feaea548 | ebe67615-643a-582e-bb23-9394781fae67 |
| rrf | top-30 | 0.0667 | 0.6667 | f25095ff-907e-572c-81b5-94d064e72277, 52c58389-178b-5c15-8ed0-c686feaea548 | ebe67615-643a-582e-bb23-9394781fae67 |
| reranked | top-10 | 0.0000 | 0.0000 | - | f25095ff-907e-572c-81b5-94d064e72277, 52c58389-178b-5c15-8ed0-c686feaea548, ebe67615-643a-582e-bb23-9394781fae67 |
| reranked | top-20 | 0.1000 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, f25095ff-907e-572c-81b5-94d064e72277 | ebe67615-643a-582e-bb23-9394781fae67 |
| reranked | top-30 | 0.0667 | 0.6667 | 52c58389-178b-5c15-8ed0-c686feaea548, f25095ff-907e-572c-81b5-94d064e72277 | ebe67615-643a-582e-bb23-9394781fae67 |

### corpus-installing-a-two-node-openshift-cluster-3

Question: How does OpenShift Container Platform document Chapter1.Two-Node with Arbiter?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| dense | top-20 | 0.1500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| dense | top-30 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| sparse | top-10 | 0.1000 | 0.3333 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca |
| sparse | top-20 | 0.0500 | 0.3333 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca |
| sparse | top-30 | 0.0333 | 0.3333 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3 | eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca |
| rrf | top-10 | 0.2000 | 0.6667 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0 | 984e6e13-c15d-5118-a037-381cffd2fcca |
| rrf | top-20 | 0.1500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| rrf | top-30 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| reranked | top-10 | 0.3000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| reranked | top-20 | 0.1500 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |
| reranked | top-30 | 0.1000 | 1.0000 | 2c740ac8-9970-57a5-8ab7-124daa7a6ec3, eda93ea1-8d38-5358-b74f-b070d0165df0, 984e6e13-c15d-5118-a037-381cffd2fcca | - |

### corpus-installing-an-on-premise-cluster-with-the-agent-based-installer-3

Question: How does OpenShift Container Platform document Chapter1.Preparing to install with the Agent-based Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, 0da30e4c-ed47-5d04-8887-79303f4e629e | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| dense | top-20 | 0.1000 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, 0da30e4c-ed47-5d04-8887-79303f4e629e | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| dense | top-30 | 0.0667 | 0.6667 | 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3, 0da30e4c-ed47-5d04-8887-79303f4e629e | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| sparse | top-10 | 0.1000 | 0.3333 | 0da30e4c-ed47-5d04-8887-79303f4e629e | 917de59b-ec15-54ca-94c7-0d96f7fc2a86, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 |
| sparse | top-20 | 0.1000 | 0.6667 | 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| sparse | top-30 | 0.0667 | 0.6667 | 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| rrf | top-10 | 0.2000 | 0.6667 | 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| rrf | top-20 | 0.1000 | 0.6667 | 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| rrf | top-30 | 0.0667 | 0.6667 | 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |
| reranked | top-10 | 0.1000 | 0.3333 | 0da30e4c-ed47-5d04-8887-79303f4e629e | 917de59b-ec15-54ca-94c7-0d96f7fc2a86, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 |
| reranked | top-20 | 0.0500 | 0.3333 | 0da30e4c-ed47-5d04-8887-79303f4e629e | 917de59b-ec15-54ca-94c7-0d96f7fc2a86, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 |
| reranked | top-30 | 0.0667 | 0.6667 | 0da30e4c-ed47-5d04-8887-79303f4e629e, 9877efbc-dcd2-55d3-9f04-44fbdf59f7d3 | 917de59b-ec15-54ca-94c7-0d96f7fc2a86 |

### corpus-installing-ibm-cloud-bare-metal-classic-3

Question: How does OpenShift Container Platform document Chapter1.Prerequisites for installing a cluster on {ibm-cloud-bm}?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| dense | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| dense | top-30 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| sparse | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| sparse | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| sparse | top-30 | 0.0333 | 0.3333 | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a | 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| rrf | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| rrf | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| rrf | top-30 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| reranked | top-10 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| reranked | top-20 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |
| reranked | top-30 | 0.0000 | 0.0000 | - | 68ed5fdb-625e-5cd7-bb68-feb8bfc6177a, 7222659b-8d19-526d-abe5-58d02df8e46d, 29ffde42-190c-5594-bae9-53432df2d31f |

### corpus-installing-on-premise-with-assisted-installer-3

Question: How does OpenShift Container Platform document Chapter1.Installing an on-premise cluster using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 23322e73-afdf-5785-8297-448fe0629f29 |
| dense | top-20 | 0.1000 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 23322e73-afdf-5785-8297-448fe0629f29 |
| dense | top-30 | 0.0667 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 23322e73-afdf-5785-8297-448fe0629f29 |
| sparse | top-10 | 0.1000 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 23322e73-afdf-5785-8297-448fe0629f29 |
| sparse | top-20 | 0.0500 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 23322e73-afdf-5785-8297-448fe0629f29 |
| sparse | top-30 | 0.0333 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 23322e73-afdf-5785-8297-448fe0629f29 |
| rrf | top-10 | 0.1000 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 23322e73-afdf-5785-8297-448fe0629f29 |
| rrf | top-20 | 0.1000 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 23322e73-afdf-5785-8297-448fe0629f29 |
| rrf | top-30 | 0.0667 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 23322e73-afdf-5785-8297-448fe0629f29 |
| reranked | top-10 | 0.1000 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 23322e73-afdf-5785-8297-448fe0629f29 |
| reranked | top-20 | 0.0500 | 0.3333 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72 | 94e34536-1d0e-53dc-bb09-e12da9c56b8f, 23322e73-afdf-5785-8297-448fe0629f29 |
| reranked | top-30 | 0.0667 | 0.6667 | 47f3c4a4-4ea8-50de-b15f-14ed9fc0bb72, 94e34536-1d0e-53dc-bb09-e12da9c56b8f | 23322e73-afdf-5785-8297-448fe0629f29 |

### corpus-installing-on-a-single-node-3

Question: How does OpenShift Container Platform document Chapter1.Preparing to install on a single node?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449 | f71a4180-296d-5fd1-acbe-f55c8de1994a |
| dense | top-20 | 0.1500 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| dense | top-30 | 0.1000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| sparse | top-10 | 0.3000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, d697f502-f12d-5b17-8a1e-9c2b9666366d, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| sparse | top-20 | 0.1500 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, d697f502-f12d-5b17-8a1e-9c2b9666366d, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| sparse | top-30 | 0.1000 | 1.0000 | e775a89d-d659-5d00-8fb5-cb89d0977449, d697f502-f12d-5b17-8a1e-9c2b9666366d, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| rrf | top-10 | 0.3000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| rrf | top-20 | 0.1500 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| rrf | top-30 | 0.1000 | 1.0000 | d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449, f71a4180-296d-5fd1-acbe-f55c8de1994a | - |
| reranked | top-10 | 0.2000 | 0.6667 | f71a4180-296d-5fd1-acbe-f55c8de1994a, d697f502-f12d-5b17-8a1e-9c2b9666366d | e775a89d-d659-5d00-8fb5-cb89d0977449 |
| reranked | top-20 | 0.1500 | 1.0000 | f71a4180-296d-5fd1-acbe-f55c8de1994a, d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449 | - |
| reranked | top-30 | 0.1000 | 1.0000 | f71a4180-296d-5fd1-acbe-f55c8de1994a, d697f502-f12d-5b17-8a1e-9c2b9666366d, e775a89d-d659-5d00-8fb5-cb89d0977449 | - |

### corpus-installing-on-alibaba-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Alibaba Cloud by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| dense | top-20 | 0.1500 | 1.0000 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| dense | top-30 | 0.1000 | 1.0000 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| sparse | top-10 | 0.2000 | 0.6667 | ef050325-ff43-581b-9a9f-29a1fa167bf3, 40d6e161-726b-5d9b-8ac1-8b3b721d516f | b75b40a3-f0e6-552b-94e6-18193a3898bd |
| sparse | top-20 | 0.1000 | 0.6667 | ef050325-ff43-581b-9a9f-29a1fa167bf3, 40d6e161-726b-5d9b-8ac1-8b3b721d516f | b75b40a3-f0e6-552b-94e6-18193a3898bd |
| sparse | top-30 | 0.0667 | 0.6667 | ef050325-ff43-581b-9a9f-29a1fa167bf3, 40d6e161-726b-5d9b-8ac1-8b3b721d516f | b75b40a3-f0e6-552b-94e6-18193a3898bd |
| rrf | top-10 | 0.2000 | 0.6667 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3 | b75b40a3-f0e6-552b-94e6-18193a3898bd |
| rrf | top-20 | 0.1500 | 1.0000 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| rrf | top-30 | 0.1000 | 1.0000 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd | - |
| reranked | top-10 | 0.2000 | 0.6667 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3 | b75b40a3-f0e6-552b-94e6-18193a3898bd |
| reranked | top-20 | 0.1000 | 0.6667 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3 | b75b40a3-f0e6-552b-94e6-18193a3898bd |
| reranked | top-30 | 0.1000 | 1.0000 | 40d6e161-726b-5d9b-8ac1-8b3b721d516f, ef050325-ff43-581b-9a9f-29a1fa167bf3, b75b40a3-f0e6-552b-94e6-18193a3898bd | - |

### corpus-installing-on-any-platform-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on any platform?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| dense | top-20 | 0.0500 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| dense | top-30 | 0.0333 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| sparse | top-10 | 0.1000 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| sparse | top-20 | 0.0500 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| sparse | top-30 | 0.0333 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| rrf | top-10 | 0.1000 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| rrf | top-20 | 0.0500 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| rrf | top-30 | 0.0333 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| reranked | top-10 | 0.1000 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| reranked | top-20 | 0.0500 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |
| reranked | top-30 | 0.0333 | 0.3333 | 3b9f8aab-e120-5039-8ea5-06c2b5ab7eec | c2d086c3-ce90-500e-bfb2-a923a1c5b019, daa63ce8-c073-5cb3-a5e7-d6ae8d9cacf9 |

### corpus-installing-on-aws-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | cdd06c15-2087-5bf1-a723-bbafba10b2f8, 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| dense | top-20 | 0.0500 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| dense | top-30 | 0.0333 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| sparse | top-10 | 0.1000 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| sparse | top-20 | 0.0500 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| sparse | top-30 | 0.0333 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| rrf | top-10 | 0.1000 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| rrf | top-20 | 0.0500 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| rrf | top-30 | 0.0333 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| reranked | top-10 | 0.1000 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| reranked | top-20 | 0.0500 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |
| reranked | top-30 | 0.0333 | 0.3333 | cdd06c15-2087-5bf1-a723-bbafba10b2f8 | 507a0cd1-1fa1-5bdf-9ec5-7d371d4d13fd, feaf506e-38eb-5c0d-b5f7-0ce8626c972a |

### corpus-installing-on-azure-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| dense | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| dense | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 5a476753-384f-577f-98c3-89f8bfe1d006, 2643250e-5baa-583b-b070-6fbe83bf5c77, 95eb37ef-48d5-5c8a-b927-c2e38a78d891 |

### corpus-installing-on-azure-stack-hub-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| dense | top-20 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| dense | top-30 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| sparse | top-20 | 0.0500 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| sparse | top-30 | 0.0333 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 44d40f32-aa8e-5999-b5a6-8995b9f8415f, f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| rrf | top-30 | 0.0333 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| reranked | top-10 | 0.1000 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| reranked | top-20 | 0.0500 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |
| reranked | top-30 | 0.0333 | 0.3333 | 44d40f32-aa8e-5999-b5a6-8995b9f8415f | f19ddb55-a1a0-5c6c-8844-70ecf3acc9ba, 63e5f6e1-dfff-5997-b6b6-d024dff01cb7 |

### corpus-installing-on-bare-metal-3

Question: How does OpenShift Container Platform document Chapter1.Preparing for bare-metal cluster installation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 23c55559-abed-5bdd-93fd-23a5a9b53c3b | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |
| dense | top-20 | 0.1000 | 0.6667 | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 23c55559-abed-5bdd-93fd-23a5a9b53c3b | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |
| dense | top-30 | 0.0667 | 0.6667 | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 23c55559-abed-5bdd-93fd-23a5a9b53c3b | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |
| sparse | top-10 | 0.1000 | 0.3333 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 23c55559-abed-5bdd-93fd-23a5a9b53c3b |
| sparse | top-20 | 0.0500 | 0.3333 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 23c55559-abed-5bdd-93fd-23a5a9b53c3b |
| sparse | top-30 | 0.0333 | 0.3333 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 23c55559-abed-5bdd-93fd-23a5a9b53c3b |
| rrf | top-10 | 0.1000 | 0.3333 | 2e809890-9346-5378-8a47-d5f9d85bb1dd | 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 23c55559-abed-5bdd-93fd-23a5a9b53c3b |
| rrf | top-20 | 0.1000 | 0.6667 | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 23c55559-abed-5bdd-93fd-23a5a9b53c3b | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |
| rrf | top-30 | 0.0667 | 0.6667 | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 23c55559-abed-5bdd-93fd-23a5a9b53c3b | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 23c55559-abed-5bdd-93fd-23a5a9b53c3b |
| reranked | top-20 | 0.0000 | 0.0000 | - | 2e809890-9346-5378-8a47-d5f9d85bb1dd, 12efa61a-ddd3-50c2-93d2-cce8e35c8298, 23c55559-abed-5bdd-93fd-23a5a9b53c3b |
| reranked | top-30 | 0.0667 | 0.6667 | 23c55559-abed-5bdd-93fd-23a5a9b53c3b, 2e809890-9346-5378-8a47-d5f9d85bb1dd | 12efa61a-ddd3-50c2-93d2-cce8e35c8298 |

### corpus-installing-on-google-cloud-3

Question: How does OpenShift Container Platform document 1.1.Prerequisites?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| dense | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| dense | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| rrf | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| rrf | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| reranked | top-20 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |
| reranked | top-30 | 0.0000 | 0.0000 | - | 221be235-a22a-579d-b8e2-5140ceafc228, 5449a7b3-1311-50aa-8c3b-a00cc0529a35, 4a2592fb-71ba-5f82-8144-4492f227e788 |

### corpus-installing-on-ibm-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a, fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| dense | top-20 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a, fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| dense | top-30 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a, fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| sparse | top-10 | 0.1000 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| sparse | top-20 | 0.0500 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| sparse | top-30 | 0.0333 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| rrf | top-10 | 0.0000 | 0.0000 | - | 93d21363-b5e1-5b4a-8283-1b069bd0608a, fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| rrf | top-20 | 0.0500 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| rrf | top-30 | 0.0333 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| reranked | top-10 | 0.1000 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| reranked | top-20 | 0.0500 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |
| reranked | top-30 | 0.0333 | 0.3333 | 93d21363-b5e1-5b4a-8283-1b069bd0608a | fe4dd2ac-a393-59d3-9125-fb75933b0529, b19c67ab-c3f6-56d5-bd3b-07b9b7b4d35e |

### corpus-installing-on-ibm-power-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6, 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| dense | top-20 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6, 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| dense | top-30 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6, 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| sparse | top-10 | 0.1000 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| sparse | top-20 | 0.0500 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| sparse | top-30 | 0.0333 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6, 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| rrf | top-20 | 0.0500 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| rrf | top-30 | 0.0333 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 855a9eb7-d25c-5335-9fab-bda066a607d6, 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| reranked | top-20 | 0.0500 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |
| reranked | top-30 | 0.0333 | 0.3333 | 855a9eb7-d25c-5335-9fab-bda066a607d6 | 89389d95-495d-5611-ac71-fa2e7c985088, 478aa08f-e001-591c-a229-9896cf98a352 |

### corpus-installing-on-ibm-power-virtual-server-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| dense | top-20 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| dense | top-30 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| sparse | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| sparse | top-20 | 0.0500 | 0.3333 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| sparse | top-30 | 0.0333 | 0.3333 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| rrf | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| rrf | top-20 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| rrf | top-30 | 0.0333 | 0.3333 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| reranked | top-10 | 0.0000 | 0.0000 | - | 318433bf-ebf4-5d86-8751-0bbcd63045b5, 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| reranked | top-20 | 0.0500 | 0.3333 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |
| reranked | top-30 | 0.0333 | 0.3333 | 318433bf-ebf4-5d86-8751-0bbcd63045b5 | 9b437025-830f-5e34-ab75-07ee52fc97a5, 0999827d-1438-5453-83f5-30c69e0c02ec |

### corpus-installing-on-ibm-powervc-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| dense | top-20 | 0.0500 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| dense | top-30 | 0.0333 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| sparse | top-10 | 0.0000 | 0.0000 | - | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc, ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| sparse | top-20 | 0.0500 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| sparse | top-30 | 0.0333 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| rrf | top-10 | 0.1000 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| rrf | top-20 | 0.0500 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| rrf | top-30 | 0.0333 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| reranked | top-10 | 0.1000 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| reranked | top-20 | 0.0500 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |
| reranked | top-30 | 0.0333 | 0.3333 | 5767b9cc-2db5-5b3a-b0c3-85513b5e22bc | ca4751a8-63fd-5016-a6f4-33c5e441c801, 39535c1e-8b7c-5570-b700-3d8b5ea5914b |

### corpus-installing-on-ibm-z-and-ibm-linuxone-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| dense | top-20 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| dense | top-30 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| sparse | top-10 | 0.1000 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| sparse | top-20 | 0.0500 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| sparse | top-30 | 0.0333 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa, eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| rrf | top-20 | 0.0500 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| rrf | top-30 | 0.0333 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| reranked | top-10 | 0.1000 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| reranked | top-20 | 0.0500 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |
| reranked | top-30 | 0.0333 | 0.3333 | 6272dd32-74a9-5c18-9e3f-3003bbfe8daa | eef7ef3d-a263-5dd1-867f-ea331bde63ae, 69814657-ddec-5119-9a56-b929ff7dd499 |

### corpus-installing-on-nutanix-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 5020cbc5-a226-53ff-8b09-d8a11cd599b1, 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| dense | top-20 | 0.0000 | 0.0000 | - | 5020cbc5-a226-53ff-8b09-d8a11cd599b1, 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| dense | top-30 | 0.0333 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| sparse | top-10 | 0.1000 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| sparse | top-20 | 0.0500 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| sparse | top-30 | 0.0333 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| rrf | top-10 | 0.1000 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| rrf | top-20 | 0.0500 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| rrf | top-30 | 0.0333 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| reranked | top-10 | 0.1000 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| reranked | top-20 | 0.0500 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |
| reranked | top-30 | 0.0333 | 0.3333 | 5020cbc5-a226-53ff-8b09-d8a11cd599b1 | 2533d4a8-bc15-5a1e-9b85-f8b0e326f359, 52877c53-56be-5d4b-993c-8a172eca4d89 |

### corpus-installing-on-openstack-3

Question: How does OpenShift Container Platform document Chapter1.Preparing to install on OpenStack?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| dense | top-20 | 0.0500 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| dense | top-30 | 0.0333 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| sparse | top-10 | 0.1000 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| sparse | top-20 | 0.0500 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| sparse | top-30 | 0.0333 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| rrf | top-10 | 0.1000 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| rrf | top-20 | 0.0500 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| rrf | top-30 | 0.0333 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| reranked | top-10 | 0.1000 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| reranked | top-20 | 0.0500 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |
| reranked | top-30 | 0.0333 | 0.3333 | ee550e8d-5fe2-50a6-bfa1-f50619443688 | 69610e64-389d-5b6f-b8a5-8b57ba91644c, 9a792a90-51b9-5c8b-80f5-a9d94e4eea9b |

### corpus-installing-on-oracle-database-appliance-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Oracle Database Appliance by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | 2a675940-64ff-5403-8209-990058797cea, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 |
| dense | top-20 | 0.1500 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 | - |
| dense | top-30 | 0.1000 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 | - |
| sparse | top-10 | 0.0000 | 0.0000 | - | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 |
| sparse | top-20 | 0.1000 | 0.6667 | a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0, 63cd6e35-62b0-5fe1-b47e-e58063ea799a | 2a675940-64ff-5403-8209-990058797cea |
| sparse | top-30 | 0.1000 | 1.0000 | a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0, 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea | - |
| rrf | top-10 | 0.1000 | 0.3333 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a | 2a675940-64ff-5403-8209-990058797cea, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 |
| rrf | top-20 | 0.1500 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0, 2a675940-64ff-5403-8209-990058797cea | - |
| rrf | top-30 | 0.1000 | 1.0000 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0, 2a675940-64ff-5403-8209-990058797cea | - |
| reranked | top-10 | 0.0000 | 0.0000 | - | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea, a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 |
| reranked | top-20 | 0.0500 | 0.3333 | a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0 | 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea |
| reranked | top-30 | 0.1000 | 1.0000 | a17fc2a0-1dbf-5e89-8fe3-3a4cce3708f0, 63cd6e35-62b0-5fe1-b47e-e58063ea799a, 2a675940-64ff-5403-8209-990058797cea | - |

### corpus-installing-on-oracle-distributed-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Oracle Distributed Cloud by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f, eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| dense | top-20 | 0.0500 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| dense | top-30 | 0.0667 | 0.6667 | dd93afd8-d8fb-5286-af72-7041a9f7857f, eac4261f-2460-503f-94f0-c5329f9018d5 | 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| sparse | top-10 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f, eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| sparse | top-20 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f, eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| sparse | top-30 | 0.0333 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| rrf | top-10 | 0.0000 | 0.0000 | - | dd93afd8-d8fb-5286-af72-7041a9f7857f, eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| rrf | top-20 | 0.0500 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| rrf | top-30 | 0.0333 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| reranked | top-10 | 0.1000 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| reranked | top-20 | 0.0500 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |
| reranked | top-30 | 0.0333 | 0.3333 | dd93afd8-d8fb-5286-af72-7041a9f7857f | eac4261f-2460-503f-94f0-c5329f9018d5, 31e78566-4b14-53ab-965a-2534ffbdfb64 |

### corpus-installing-on-oracle-edge-cloud-3

Question: How does OpenShift Container Platform document Chapter1.Installing a cluster on Oracle Edge Cloud by using the Assisted Installer?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| dense | top-20 | 0.1000 | 0.6667 | dd42bc83-bc17-5a12-acfc-16792b39fbcc, eb7235ff-a939-5bde-a133-635edbde7ae8 | 871cf665-ef46-504f-99f6-9a366af22a22 |
| dense | top-30 | 0.0667 | 0.6667 | dd42bc83-bc17-5a12-acfc-16792b39fbcc, eb7235ff-a939-5bde-a133-635edbde7ae8 | 871cf665-ef46-504f-99f6-9a366af22a22 |
| sparse | top-10 | 0.0000 | 0.0000 | - | dd42bc83-bc17-5a12-acfc-16792b39fbcc, eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| sparse | top-20 | 0.0500 | 0.3333 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| sparse | top-30 | 0.0333 | 0.3333 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| rrf | top-10 | 0.0000 | 0.0000 | - | dd42bc83-bc17-5a12-acfc-16792b39fbcc, eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| rrf | top-20 | 0.0500 | 0.3333 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| rrf | top-30 | 0.0667 | 0.6667 | dd42bc83-bc17-5a12-acfc-16792b39fbcc, eb7235ff-a939-5bde-a133-635edbde7ae8 | 871cf665-ef46-504f-99f6-9a366af22a22 |
| reranked | top-10 | 0.1000 | 0.3333 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| reranked | top-20 | 0.0500 | 0.3333 | dd42bc83-bc17-5a12-acfc-16792b39fbcc | eb7235ff-a939-5bde-a133-635edbde7ae8, 871cf665-ef46-504f-99f6-9a366af22a22 |
| reranked | top-30 | 0.0667 | 0.6667 | dd42bc83-bc17-5a12-acfc-16792b39fbcc, eb7235ff-a939-5bde-a133-635edbde7ae8 | 871cf665-ef46-504f-99f6-9a366af22a22 |

### corpus-installing-on-vmware-vsphere-3

Question: How does OpenShift Container Platform document Chapter1.Installation methods?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | 2f6bf463-910c-536e-91b1-5621eeddf784, d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| dense | top-20 | 0.0500 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| dense | top-30 | 0.0333 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| sparse | top-10 | 0.1000 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| sparse | top-20 | 0.0500 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| sparse | top-30 | 0.0333 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| rrf | top-10 | 0.1000 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| rrf | top-20 | 0.0500 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| rrf | top-30 | 0.0333 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| reranked | top-10 | 0.1000 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| reranked | top-20 | 0.0500 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |
| reranked | top-30 | 0.0333 | 0.3333 | 2f6bf463-910c-536e-91b1-5621eeddf784 | d97adff8-6154-56a2-bd9a-6416cd6093c2, 728b671f-4610-547d-82a2-f3ad620bd6d8 |

### corpus-jenkins-5

Question: How does OpenShift Container Platform document 1.1.Configuration and customization?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| dense | top-20 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| dense | top-30 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| sparse | top-10 | 0.1000 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| sparse | top-20 | 0.0500 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| sparse | top-30 | 0.0333 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| rrf | top-10 | 0.0000 | 0.0000 | - | fe77d5c3-56c5-58ea-88d8-167700a7c141, b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| rrf | top-20 | 0.0500 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| rrf | top-30 | 0.0333 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| reranked | top-10 | 0.1000 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| reranked | top-20 | 0.0500 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |
| reranked | top-30 | 0.0333 | 0.3333 | fe77d5c3-56c5-58ea-88d8-167700a7c141 | b9f5fb74-4e9d-5c99-86ea-cc33e442d34c, 3408668c-cfdb-5ee1-bce4-614a5e9ba182 |

### corpus-kubernetes-nmstate-3

Question: How does OpenShift Container Platform document Chapter1.Observing and updating the node network state and configuration?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| dense | top-20 | 0.1000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| dense | top-30 | 0.0667 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| sparse | top-10 | 0.2000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| sparse | top-20 | 0.1500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| sparse | top-30 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| rrf | top-10 | 0.2000 | 0.6667 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | f16dd82a-b19f-5758-86a3-91e469d47cdb |
| rrf | top-20 | 0.1500 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| rrf | top-30 | 0.1000 | 1.0000 | f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d, f16dd82a-b19f-5758-86a3-91e469d47cdb | - |
| reranked | top-10 | 0.3000 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb, f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | - |
| reranked | top-20 | 0.1500 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb, f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | - |
| reranked | top-30 | 0.1000 | 1.0000 | f16dd82a-b19f-5758-86a3-91e469d47cdb, f0e90a67-5732-5da5-9ae3-00e25a5b5dea, 4af04738-33bc-5e62-90aa-94b02859d93d | - |

### corpus-machine-apis-3

Question: How does OpenShift Container Platform document [1.1.ContainerRuntimeConfig [machineconfiguration.openshift.io/v1]](#containerruntimeconfig-machineconfiguration-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | c3eb6302-eeb1-57bb-b5b7-dc3161066592, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 | 01feaa64-52d1-5311-be91-638189b9d982 |
| dense | top-20 | 0.1000 | 0.6667 | c3eb6302-eeb1-57bb-b5b7-dc3161066592, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 | 01feaa64-52d1-5311-be91-638189b9d982 |
| dense | top-30 | 0.0667 | 0.6667 | c3eb6302-eeb1-57bb-b5b7-dc3161066592, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 | 01feaa64-52d1-5311-be91-638189b9d982 |
| sparse | top-10 | 0.1000 | 0.3333 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | 01feaa64-52d1-5311-be91-638189b9d982, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 |
| sparse | top-20 | 0.0500 | 0.3333 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | 01feaa64-52d1-5311-be91-638189b9d982, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 |
| sparse | top-30 | 0.0333 | 0.3333 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | 01feaa64-52d1-5311-be91-638189b9d982, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 |
| rrf | top-10 | 0.1000 | 0.3333 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | 01feaa64-52d1-5311-be91-638189b9d982, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 |
| rrf | top-20 | 0.1000 | 0.6667 | c3eb6302-eeb1-57bb-b5b7-dc3161066592, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 | 01feaa64-52d1-5311-be91-638189b9d982 |
| rrf | top-30 | 0.0667 | 0.6667 | c3eb6302-eeb1-57bb-b5b7-dc3161066592, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 | 01feaa64-52d1-5311-be91-638189b9d982 |
| reranked | top-10 | 0.1000 | 0.3333 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | 01feaa64-52d1-5311-be91-638189b9d982, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 |
| reranked | top-20 | 0.0500 | 0.3333 | c3eb6302-eeb1-57bb-b5b7-dc3161066592 | 01feaa64-52d1-5311-be91-638189b9d982, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 |
| reranked | top-30 | 0.0667 | 0.6667 | c3eb6302-eeb1-57bb-b5b7-dc3161066592, ab8d8e8e-a0fe-5930-a411-1d88a1765ef0 | 01feaa64-52d1-5311-be91-638189b9d982 |

### corpus-machine-configuration-3

Question: How does OpenShift Container Platform document Chapter1.Machine configuration overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | d0866a16-62e9-59d5-b1fb-0cd89da842fd, 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| dense | top-20 | 0.0000 | 0.0000 | - | d0866a16-62e9-59d5-b1fb-0cd89da842fd, 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| dense | top-30 | 0.0333 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| sparse | top-10 | 0.1000 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| sparse | top-20 | 0.0500 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| sparse | top-30 | 0.0333 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| rrf | top-10 | 0.1000 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| rrf | top-20 | 0.0500 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| rrf | top-30 | 0.0333 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| reranked | top-10 | 0.1000 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| reranked | top-20 | 0.0500 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |
| reranked | top-30 | 0.0333 | 0.3333 | d0866a16-62e9-59d5-b1fb-0cd89da842fd | 2a23a7d9-4976-5501-86e4-669c9956d90f, 140a2387-00a8-537a-a097-f8e85c4a721f |

### corpus-machine-management-3

Question: How does OpenShift Container Platform document Chapter1.Overview of machine management?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, bb43a1c4-4251-555f-9399-5f0283105079, ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| dense | top-20 | 0.1500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, bb43a1c4-4251-555f-9399-5f0283105079, ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| dense | top-30 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, bb43a1c4-4251-555f-9399-5f0283105079, ffe555a9-46cb-5f45-ad79-ab0a63998fd3 | - |
| sparse | top-10 | 0.3000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| sparse | top-20 | 0.1500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| sparse | top-30 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| rrf | top-10 | 0.3000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| reranked | top-20 | 0.1500 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |
| reranked | top-30 | 0.1000 | 1.0000 | 21a45103-4e63-51ed-b725-04a975efd8ad, ffe555a9-46cb-5f45-ad79-ab0a63998fd3, bb43a1c4-4251-555f-9399-5f0283105079 | - |

### corpus-metadata-apis-3

Question: How does OpenShift Container Platform document [1.1.APIRequestCount [apiserver.openshift.io/v1]](#apirequestcount-apiserver-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| dense | top-20 | 0.0500 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| dense | top-30 | 0.0333 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| sparse | top-10 | 0.1000 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| sparse | top-20 | 0.0500 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| sparse | top-30 | 0.0333 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| rrf | top-10 | 0.1000 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| rrf | top-20 | 0.0500 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| rrf | top-30 | 0.0333 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| reranked | top-10 | 0.1000 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| reranked | top-20 | 0.0500 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |
| reranked | top-30 | 0.0333 | 0.3333 | b57bbb64-583c-523f-98c8-d52c147046c2 | a4702c78-4647-5eb3-89df-60d31f85aba1, b1b9be77-70ff-51f0-827e-ebbc778e6f43 |

### corpus-migrating-from-version-3-to-4-3

Question: How does OpenShift Container Platform document Chapter1.Migration from OpenShift Container Platform 3 to 4 overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.3000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| dense | top-20 | 0.1500 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| dense | top-30 | 0.1000 | 1.0000 | 6f70c094-6de6-5835-a27a-0e7d656db268, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 12b75083-e43b-55ca-84cf-1fa6ecddeeed | - |
| sparse | top-10 | 0.2000 | 0.6667 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e | 6f70c094-6de6-5835-a27a-0e7d656db268 |
| sparse | top-20 | 0.1500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| sparse | top-30 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| rrf | top-10 | 0.3000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| rrf | top-20 | 0.1500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| rrf | top-30 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e, 6f70c094-6de6-5835-a27a-0e7d656db268 | - |
| reranked | top-10 | 0.3000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 6f70c094-6de6-5835-a27a-0e7d656db268, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e | - |
| reranked | top-20 | 0.1500 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 6f70c094-6de6-5835-a27a-0e7d656db268, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e | - |
| reranked | top-30 | 0.1000 | 1.0000 | 12b75083-e43b-55ca-84cf-1fa6ecddeeed, 6f70c094-6de6-5835-a27a-0e7d656db268, 2f0ac88b-f287-566d-abd0-65a6bbbdd98e | - |

### corpus-monitoring-apis-3

Question: How does OpenShift Container Platform document [1.1.Alertmanager [monitoring.coreos.com/v1]](#alertmanager-monitoring-coreos-comv1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| dense | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| dense | top-30 | 0.0333 | 0.3333 | ae4dba2d-fe47-57aa-8c1e-011fa09e4269 | a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| sparse | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| sparse | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| sparse | top-30 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| rrf | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| rrf | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| rrf | top-30 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| reranked | top-10 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| reranked | top-20 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |
| reranked | top-30 | 0.0000 | 0.0000 | - | ae4dba2d-fe47-57aa-8c1e-011fa09e4269, a051b20f-a822-51f8-94eb-a7b71880f454, 0f83c687-c22d-5c42-b418-c9050a9f5471 |

### corpus-multiple-networks-3

Question: How does OpenShift Container Platform document Chapter1.Understanding multiple networks?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| dense | top-20 | 0.1000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| dense | top-30 | 0.0667 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| sparse | top-10 | 0.2000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| sparse | top-20 | 0.1000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| sparse | top-30 | 0.0667 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| rrf | top-10 | 0.2000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| rrf | top-20 | 0.1000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| rrf | top-30 | 0.0667 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| reranked | top-10 | 0.2000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| reranked | top-20 | 0.1000 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |
| reranked | top-30 | 0.0667 | 0.6667 | ef7b37e1-fea4-5d93-83ba-bdcebb5f48c3, 4e19c74c-61b0-513e-8814-a5c41cecbe5e | fdc74aa4-a520-5e16-97f9-ea53e24df99b |

### corpus-network-apis-3

Question: How does OpenShift Container Platform document [1.1.ClusterUserDefinedNetwork [k8s.ovn.org/v1]](#clusteruserdefinednetwork-k8s-ovn-orgv1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| dense | top-20 | 0.0500 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| dense | top-30 | 0.0333 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| sparse | top-10 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440, 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| sparse | top-20 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440, 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| sparse | top-30 | 0.0333 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| rrf | top-10 | 0.1000 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| rrf | top-20 | 0.0500 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| rrf | top-30 | 0.0333 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| reranked | top-10 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440, 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| reranked | top-20 | 0.0000 | 0.0000 | - | f5488bd0-fba5-53ce-ad21-2f4d7ab29440, 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |
| reranked | top-30 | 0.0333 | 0.3333 | f5488bd0-fba5-53ce-ad21-2f4d7ab29440 | 0647b25d-1ebd-567f-8b73-0c1daa0afd87, d894c6f9-9c93-54f8-8a8c-a635b67c6d6d |

### corpus-network-observability-3

Question: How does OpenShift Container Platform document Chapter1.Network Observability Operator release notes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| dense | top-20 | 0.1000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| dense | top-30 | 0.0667 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| sparse | top-10 | 0.1000 | 0.3333 | ba916851-7def-53bc-bfc1-d9318d308c1c | e4fd75c8-5748-51f6-bce1-321e66d5dae7, 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| sparse | top-20 | 0.1000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| sparse | top-30 | 0.0667 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| rrf | top-10 | 0.2000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| rrf | top-20 | 0.1000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| rrf | top-30 | 0.0667 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| reranked | top-10 | 0.2000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| reranked | top-20 | 0.1000 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |
| reranked | top-30 | 0.0667 | 0.6667 | ba916851-7def-53bc-bfc1-d9318d308c1c, e4fd75c8-5748-51f6-bce1-321e66d5dae7 | 160db3d6-c2d0-5a76-aae1-b0aa875a0de0 |

### corpus-network-observability-operator-3

Question: How does OpenShift Container Platform document Chapter1.Network Observability Operator?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc | 27d41601-2b71-54f6-a377-4f7ae5b9be4a |
| dense | top-20 | 0.1500 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a | - |
| dense | top-30 | 0.1000 | 1.0000 | eba32b63-c941-5c61-a7fd-ab1e65cc81fd, b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a | - |
| sparse | top-10 | 0.3000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| sparse | top-20 | 0.1500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| sparse | top-30 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| rrf | top-10 | 0.3000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, eba32b63-c941-5c61-a7fd-ab1e65cc81fd, 27d41601-2b71-54f6-a377-4f7ae5b9be4a | - |
| rrf | top-20 | 0.1500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, eba32b63-c941-5c61-a7fd-ab1e65cc81fd, 27d41601-2b71-54f6-a377-4f7ae5b9be4a | - |
| rrf | top-30 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, eba32b63-c941-5c61-a7fd-ab1e65cc81fd, 27d41601-2b71-54f6-a377-4f7ae5b9be4a | - |
| reranked | top-10 | 0.3000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| reranked | top-20 | 0.1500 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |
| reranked | top-30 | 0.1000 | 1.0000 | b44c6b07-f819-5b89-a065-0cb5e3bbf4bc, 27d41601-2b71-54f6-a377-4f7ae5b9be4a, eba32b63-c941-5c61-a7fd-ab1e65cc81fd | - |

### corpus-network-security-3

Question: How does OpenShift Container Platform document Chapter1.Understanding network policy APIs?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd, afecc12a-942c-509f-bdad-a987f4ee6d45, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| dense | top-20 | 0.0500 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | c6859b69-7e60-5eb6-9add-d514eb66b5dd, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| dense | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | c6859b69-7e60-5eb6-9add-d514eb66b5dd, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| sparse | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd, afecc12a-942c-509f-bdad-a987f4ee6d45, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| sparse | top-20 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd, afecc12a-942c-509f-bdad-a987f4ee6d45, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| sparse | top-30 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd, afecc12a-942c-509f-bdad-a987f4ee6d45, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| rrf | top-10 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd, afecc12a-942c-509f-bdad-a987f4ee6d45, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| rrf | top-20 | 0.0000 | 0.0000 | - | c6859b69-7e60-5eb6-9add-d514eb66b5dd, afecc12a-942c-509f-bdad-a987f4ee6d45, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| rrf | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | c6859b69-7e60-5eb6-9add-d514eb66b5dd, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| reranked | top-10 | 0.1000 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | c6859b69-7e60-5eb6-9add-d514eb66b5dd, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| reranked | top-20 | 0.0500 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | c6859b69-7e60-5eb6-9add-d514eb66b5dd, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |
| reranked | top-30 | 0.0333 | 0.3333 | afecc12a-942c-509f-bdad-a987f4ee6d45 | c6859b69-7e60-5eb6-9add-d514eb66b5dd, 83e6fe3b-de22-55a4-8c83-13bdc186d9cb |

### corpus-networking-operators-3

Question: How does OpenShift Container Platform document Chapter1.Kubernetes NMState Operator?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| dense | top-20 | 0.0500 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| dense | top-30 | 0.0333 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| sparse | top-10 | 0.1000 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| sparse | top-20 | 0.0500 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| sparse | top-30 | 0.0333 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| rrf | top-10 | 0.1000 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| rrf | top-20 | 0.0500 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| rrf | top-30 | 0.0333 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| reranked | top-10 | 0.1000 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| reranked | top-20 | 0.0500 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |
| reranked | top-30 | 0.0333 | 0.3333 | 0cf7881a-1e32-54fe-a90b-7b0d04b6932f | 40b2c631-e035-5c5f-b82d-a6de29e896b6, a73fc23d-f8dd-5752-a969-f72eb8f696a7 |

### corpus-networking-overview-3

Question: How does OpenShift Container Platform document Chapter1.Understanding networking?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 8136b814-2c0c-513f-a582-42551de5bed5, 507af079-dae6-536f-865c-4d6c11e29827 | 8a79346f-ccde-58d4-ac55-f222e37fa23c |
| dense | top-20 | 0.1500 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5, 507af079-dae6-536f-865c-4d6c11e29827, 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| dense | top-30 | 0.1000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5, 507af079-dae6-536f-865c-4d6c11e29827, 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| sparse | top-10 | 0.2000 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5 | 8a79346f-ccde-58d4-ac55-f222e37fa23c |
| sparse | top-20 | 0.1000 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5 | 8a79346f-ccde-58d4-ac55-f222e37fa23c |
| sparse | top-30 | 0.0667 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5 | 8a79346f-ccde-58d4-ac55-f222e37fa23c |
| rrf | top-10 | 0.2000 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5 | 8a79346f-ccde-58d4-ac55-f222e37fa23c |
| rrf | top-20 | 0.1000 | 0.6667 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5 | 8a79346f-ccde-58d4-ac55-f222e37fa23c |
| rrf | top-30 | 0.1000 | 1.0000 | 507af079-dae6-536f-865c-4d6c11e29827, 8136b814-2c0c-513f-a582-42551de5bed5, 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | top-10 | 0.3000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5, 507af079-dae6-536f-865c-4d6c11e29827, 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | top-20 | 0.1500 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5, 507af079-dae6-536f-865c-4d6c11e29827, 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |
| reranked | top-30 | 0.1000 | 1.0000 | 8136b814-2c0c-513f-a582-42551de5bed5, 507af079-dae6-536f-865c-4d6c11e29827, 8a79346f-ccde-58d4-ac55-f222e37fa23c | - |

### corpus-node-apis-3

Question: How does OpenShift Container Platform document [1.1.Node [v1]](#node-v1-1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| dense | top-20 | 0.0500 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| dense | top-30 | 0.0333 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| sparse | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752, f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| sparse | top-20 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752, f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| sparse | top-30 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752, f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| rrf | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752, f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| rrf | top-20 | 0.0500 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| rrf | top-30 | 0.0333 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| reranked | top-10 | 0.0000 | 0.0000 | - | 264b374e-491d-50e1-af1c-0d651499c752, f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| reranked | top-20 | 0.0500 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |
| reranked | top-30 | 0.0333 | 0.3333 | f50ac9a4-94d4-5c7d-91e9-bc8d41a3aae2 | 264b374e-491d-50e1-af1c-0d651499c752, 56db0895-0c6e-5f79-87ba-d32f2410c060 |

### corpus-nodes-3

Question: How does OpenShift Container Platform document Chapter1.Overview of nodes?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 |
| dense | top-20 | 0.0500 | 0.3333 | e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 |
| dense | top-30 | 0.0333 | 0.3333 | e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 |
| sparse | top-10 | 0.2000 | 0.6667 | b32c3dff-3465-5c54-b2ee-9ac10f6fef05, e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| sparse | top-20 | 0.1000 | 0.6667 | b32c3dff-3465-5c54-b2ee-9ac10f6fef05, e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| sparse | top-30 | 0.0667 | 0.6667 | b32c3dff-3465-5c54-b2ee-9ac10f6fef05, e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| rrf | top-10 | 0.1000 | 0.3333 | e0b648b2-d5ac-505d-afda-96811d7b0926 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 |
| rrf | top-20 | 0.1000 | 0.6667 | e0b648b2-d5ac-505d-afda-96811d7b0926, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| rrf | top-30 | 0.0667 | 0.6667 | e0b648b2-d5ac-505d-afda-96811d7b0926, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| reranked | top-10 | 0.2000 | 0.6667 | e0b648b2-d5ac-505d-afda-96811d7b0926, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| reranked | top-20 | 0.1000 | 0.6667 | e0b648b2-d5ac-505d-afda-96811d7b0926, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |
| reranked | top-30 | 0.0667 | 0.6667 | e0b648b2-d5ac-505d-afda-96811d7b0926, b32c3dff-3465-5c54-b2ee-9ac10f6fef05 | aa6a0fa3-8411-5c5b-8142-54e94fe8fb60 |

### corpus-oauth-apis-3

Question: How does OpenShift Container Platform document [1.1.OAuthAccessToken [oauth.openshift.io/v1]](#oauthaccesstoken-oauth-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| dense | top-20 | 0.1500 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0, 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| dense | top-30 | 0.1000 | 1.0000 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0, 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 | - |
| sparse | top-10 | 0.2000 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| sparse | top-20 | 0.1000 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| sparse | top-30 | 0.0667 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| rrf | top-10 | 0.2000 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| rrf | top-20 | 0.1000 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| rrf | top-30 | 0.0667 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |
| reranked | top-10 | 0.1000 | 0.3333 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, a6acea40-a44c-592a-b6a9-9016a7ae84c0 |
| reranked | top-20 | 0.0500 | 0.3333 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0, a6acea40-a44c-592a-b6a9-9016a7ae84c0 |
| reranked | top-30 | 0.0667 | 0.6667 | b073171f-31ca-55cd-ae6e-f26e97ec6bd1, a6acea40-a44c-592a-b6a9-9016a7ae84c0 | 45e421e4-0f5a-507f-b183-ffc06d9a0ec0 |

### corpus-observability-overview-3

Question: How does OpenShift Container Platform document Chapter1.About Observability?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6 | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| dense | top-20 | 0.1500 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, a1916eee-1aa4-5da0-b8b2-3566af39efed | - |
| dense | top-30 | 0.1000 | 1.0000 | a870e122-fffd-5cbe-8ac3-048137f48f3b, 13c74613-fe59-5a3c-9556-2cd617e013c6, a1916eee-1aa4-5da0-b8b2-3566af39efed | - |
| sparse | top-10 | 0.2000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| sparse | top-20 | 0.1000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| sparse | top-30 | 0.0667 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| rrf | top-10 | 0.2000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| rrf | top-20 | 0.1000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| rrf | top-30 | 0.0667 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| reranked | top-10 | 0.2000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| reranked | top-20 | 0.1000 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |
| reranked | top-30 | 0.0667 | 0.6667 | 13c74613-fe59-5a3c-9556-2cd617e013c6, a870e122-fffd-5cbe-8ac3-048137f48f3b | a1916eee-1aa4-5da0-b8b2-3566af39efed |

### corpus-openshift-lightspeed-3

Question: How does OpenShift Container Platform document 1.1.OpenShift Lightspeed overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| dense | top-20 | 0.1000 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| dense | top-30 | 0.0667 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| sparse | top-10 | 0.2000 | 0.6667 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| sparse | top-20 | 0.1000 | 0.6667 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| sparse | top-30 | 0.0667 | 0.6667 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| rrf | top-10 | 0.2000 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| rrf | top-20 | 0.1000 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| rrf | top-30 | 0.0667 | 0.6667 | 8e399fa6-8f37-5ee7-ba8e-301f23154d2d, 3fb1e8c7-2e5c-5909-a41b-9d823469b231 | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| reranked | top-10 | 0.2000 | 0.6667 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| reranked | top-20 | 0.1000 | 0.6667 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | f668d1bb-a773-5ad7-9af8-327463e28dd4 |
| reranked | top-30 | 0.0667 | 0.6667 | 3fb1e8c7-2e5c-5909-a41b-9d823469b231, 8e399fa6-8f37-5ee7-ba8e-301f23154d2d | f668d1bb-a773-5ad7-9af8-327463e28dd4 |

### corpus-openshift-sandboxed-containers-3

Question: How does OpenShift Container Platform document Chapter1.About OpenShift sandboxed containers?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| dense | top-20 | 0.1000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| dense | top-30 | 0.0667 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| sparse | top-10 | 0.1000 | 0.3333 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e | cd442f4e-9ba3-523f-920b-f8dc7fe24239, f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| sparse | top-20 | 0.1000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| sparse | top-30 | 0.0667 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| rrf | top-10 | 0.2000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| rrf | top-20 | 0.1000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| rrf | top-30 | 0.0667 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| reranked | top-10 | 0.2000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| reranked | top-20 | 0.1000 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |
| reranked | top-30 | 0.0667 | 0.6667 | 857b4fd4-6b84-504e-b8ec-f2b569435c9e, cd442f4e-9ba3-523f-920b-f8dc7fe24239 | f1f66a92-c347-54c1-aa5d-d1cab64d5f26 |

### corpus-operator-apis-3

Question: How does OpenShift Container Platform document [1.1.Authentication [operator.openshift.io/v1]](#authentication-operator-openshift-iov1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| dense | top-20 | 0.0500 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| dense | top-30 | 0.0333 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| sparse | top-10 | 0.1000 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| sparse | top-20 | 0.0500 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| sparse | top-30 | 0.0333 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| rrf | top-10 | 0.1000 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| rrf | top-20 | 0.0500 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| rrf | top-30 | 0.0333 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| reranked | top-10 | 0.0000 | 0.0000 | - | c43d7ed0-4449-5cc3-be7f-51d912ed93ce, 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| reranked | top-20 | 0.0500 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |
| reranked | top-30 | 0.0333 | 0.3333 | c43d7ed0-4449-5cc3-be7f-51d912ed93ce | 0cc80091-c566-5d0b-9fd8-b61af93751a1, 538a2c98-bb74-5b5b-872a-fc9d0a9fdf9e |

### corpus-operatorhub-apis-3

Question: How does OpenShift Container Platform document [1.1.CatalogSource [operators.coreos.com/v1alpha1]](#catalogsource-operators-coreos-comv1alpha1)?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| dense | top-20 | 0.0500 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| dense | top-30 | 0.0333 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| sparse | top-10 | 0.0000 | 0.0000 | - | d418ddd9-5b85-54e8-8cff-19aa944395b5, d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| sparse | top-20 | 0.0500 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| sparse | top-30 | 0.0333 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| rrf | top-10 | 0.1000 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| rrf | top-20 | 0.0500 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| rrf | top-30 | 0.0333 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| reranked | top-10 | 0.0000 | 0.0000 | - | d418ddd9-5b85-54e8-8cff-19aa944395b5, d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| reranked | top-20 | 0.0500 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |
| reranked | top-30 | 0.0333 | 0.3333 | d418ddd9-5b85-54e8-8cff-19aa944395b5 | d39bbe45-3314-5da3-b701-a2d87f88fb68, 008ff30c-f68a-551b-9088-22f924a6ce95 |

### corpus-operators-3

Question: How does OpenShift Container Platform document Chapter1.Operators overview?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.2000 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| dense | top-20 | 0.1000 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| dense | top-30 | 0.0667 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| sparse | top-10 | 0.1000 | 0.3333 | 753694b1-e529-5cac-8bf1-deb8de32cceb | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f |
| sparse | top-20 | 0.0500 | 0.3333 | 753694b1-e529-5cac-8bf1-deb8de32cceb | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f |
| sparse | top-30 | 0.0333 | 0.3333 | 753694b1-e529-5cac-8bf1-deb8de32cceb | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f |
| rrf | top-10 | 0.1000 | 0.3333 | 753694b1-e529-5cac-8bf1-deb8de32cceb | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f |
| rrf | top-20 | 0.1000 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| rrf | top-30 | 0.0667 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| reranked | top-10 | 0.2000 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| reranked | top-20 | 0.1000 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |
| reranked | top-30 | 0.0667 | 0.6667 | 753694b1-e529-5cac-8bf1-deb8de32cceb, dfed1bf6-6e52-5a6e-a5a1-1abfdc3e5e1f | 4a7bcc74-1a42-5f6b-83bc-f2b077a542aa |

### corpus-overview-3

Question: How does OpenShift Container Platform document Chapter1.OpenShift Container Platform 4.22 Documentation?

| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |
| --- | ---: | ---: | ---: | --- | --- |
| dense | top-10 | 0.1000 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| dense | top-20 | 0.0500 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| dense | top-30 | 0.0333 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| sparse | top-10 | 0.1000 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| sparse | top-20 | 0.0500 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| sparse | top-30 | 0.0667 | 0.6667 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d, 2b3cfb52-0315-5200-bb8b-d6447317f904 | 134c2873-709a-51e3-9b33-9b627ae9615e |
| rrf | top-10 | 0.1000 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| rrf | top-20 | 0.0500 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| rrf | top-30 | 0.0333 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| reranked | top-10 | 0.1000 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| reranked | top-20 | 0.0500 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |
| reranked | top-30 | 0.0333 | 0.3333 | 9c0176e0-ef5d-595f-ad1c-ce9852dbee2d | 2b3cfb52-0315-5200-bb8b-d6447317f904, 134c2873-709a-51e3-9b33-9b627ae9615e |

