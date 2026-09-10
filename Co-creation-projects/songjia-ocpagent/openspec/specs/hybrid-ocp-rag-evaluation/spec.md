## Purpose

Provide a local, inspectable hybrid RAG evaluation workflow for versioned OCP
documentation stored in Qdrant.

## Requirements

### Requirement: Interactively accept versioned OCP questions
The system SHALL provide a standalone knowledge test script that repeatedly
accepts a user question and runs the fixed hybrid RAG pipeline for a selected
`document_version`. It SHALL default to version `4.22`, Qdrant endpoint
`http://localhost:6333`, and collection `ocp-documents`, while accepting
command-line overrides for those values and model names. The script SHALL allow
the user to exit cleanly without querying external services.

#### Scenario: A user asks an OCP question
- **WHEN** a non-empty question is entered for document version `4.22`
- **THEN** the script runs the fixed hybrid retrieval and answer pipeline using
  only points tagged with `document_version` `4.22`

#### Scenario: User exits the session
- **WHEN** the user enters an exit command or sends end-of-input
- **THEN** the script terminates without performing another retrieval or LLM
  request

### Requirement: Retrieve and fuse dense and sparse candidates
For every accepted question, the system SHALL encode a BGE-M3 dense query vector
and sparse lexical query vector, retrieve the top 30 version-filtered candidates
for each corresponding Qdrant named vector, and merge the two ranked lists with
reciprocal rank fusion. The system SHALL use a stable Qdrant point identifier to
deduplicate a chunk present in both lists and retain RRF provenance for output.

#### Scenario: Both retrieval modes return candidates
- **WHEN** dense and sparse retrieval each return 30 candidates
- **THEN** the fused order is determined by RRF across the two ranked lists and
  a duplicate point appears only once

#### Scenario: One retrieval mode returns no candidates
- **WHEN** one named-vector search returns no matching points while the other
  returns candidates
- **THEN** the system fuses and continues with the non-empty ranked list while
  reporting the dense and sparse result counts

### Requirement: Rerank a bounded fused candidate set
The system SHALL pass at most the first 20 RRF-ranked chunks and the original
question to a configurable BGE reranker, then retain the best 10 chunks for
generation. It SHALL preserve source path, heading path, document version, and
rerank score with every retained chunk.

#### Scenario: More than 20 chunks are fused
- **WHEN** RRF produces more than 20 candidate chunks
- **THEN** only its first 20 chunks are sent to the reranker and only its top
  10 reranked chunks are passed to answer generation

#### Scenario: No chunks are fused
- **WHEN** neither retrieval mode returns a version-matching chunk
- **THEN** the script reports that no supporting documentation was found and
  does not call the reranker or LLM

### Requirement: Log complete chunk provenance for every pipeline stage
The system SHALL write a log file named `hybrid_rag_test.log` beside the
standalone script. For every accepted question, it SHALL record the effective
configuration and all chunks reaching dense retrieval, sparse retrieval, RRF
fusion, the reranker input top 20, the reranked top 10, and the context sent to
the LLM. Each logged chunk SHALL include its stable point id, rank, stage score
when available, source path, heading path, document version, and content.

#### Scenario: A question completes the retrieval pipeline
- **WHEN** a question has dense, sparse, fused, and reranked candidates
- **THEN** the script-local log contains a distinct record for every stage's
  chunks and enough provenance to trace a generated answer back to a source

#### Scenario: A retrieval stage has no candidates
- **WHEN** dense or sparse retrieval returns an empty list
- **THEN** the log records that stage with an empty chunk list and retains the
  per-stage result counts for the question

### Requirement: Generate a grounded answer through local Ollama
The system SHALL use LangChain's Ollama chat integration to call local model
`qwen3.5:4b` through the native `http://localhost:11434/api/chat` service. It
SHALL send the original question and the 10 reranked chunks in a context-only
prompt, print the model answer, and print the chunk provenance used to support
it. Each context block SHALL be labeled as `[chunk:<point-id>]`, and the prompt
SHALL ask the model to identify its supporting chunks with those labels. The
system SHALL extract and log returned chunk labels but SHALL NOT reject an
otherwise successful answer based on the presence, format, or correspondence of
those labels. It SHALL report service or model failures without fabricating a
successful answer.

#### Scenario: Local model answers with retrieved context
- **WHEN** the reranker produces one or more retained chunks and Ollama is
  available
- **THEN** the model receives the question plus the retained chunks and the
  script prints its answer with supporting chunk metadata

#### Scenario: Ollama is unavailable
- **WHEN** the local Ollama chat request fails
- **THEN** the script reports the failure and retains the retrieval diagnostics
  without printing an answer as if generation succeeded

#### Scenario: Model omits or fabricates a chunk citation
- **WHEN** the model response has no chunk citation or cites an id absent from
  the supplied top-10 context
- **THEN** the script prints the answer and logs any returned chunk labels
