## Context

`ocp-documents` already stores OCP chunks as named `dense` and `sparse`
vectors, with `document_version` in every point payload. The ingestion command
has no query-side companion: the legacy examples only use a single dense vector
store. Local Ollama exposes `qwen3.5:4b` through its native
`http://localhost:11434/api/chat` API.

## Goals / Non-Goals

**Goals:**
- Provide a terminal-driven, fixed hybrid RAG test path for a selected OCP
  documentation version.
- Retrieve 30 candidates independently from each named vector, fuse their
  rankings with RRF, rerank the first 20, and ground the answer in the top 10.
- Use LangChain interfaces for documents, retrievers, RRF, reranking, prompts,
  and Ollama chat integration wherever a compatible interface exists.
- Preserve the original question and retrieved chunk provenance in test output.

**Non-Goals:**
- Add an API, frontend, router integration, chat history, streaming, or
  autonomous tool-calling agent loop.
- Change the ingested corpus, Qdrant schema, or document ingestion command.
- Query a live OpenShift cluster.

## Decisions

### Use a fixed LangChain pipeline instead of an autonomous Agent

The script will deterministically execute dense retrieval, sparse retrieval,
RRF, BGE reranking, and generation once per question. It will use LangChain
`Document`, `BaseRetriever`, RRF/ensemble, compressor/reranker, prompt, and
chat-model boundaries but will not register a search tool for an LLM to decide
whether or how often to invoke.

An autonomous Agent was rejected because the requested retrieval depth and
reranking budget must be reproducible during local quality testing.

### Query Qdrant's named vectors separately and fuse by stable point id

The BGE-M3 adapter used for ingestion will encode the question into a normalized
dense vector and a lexical sparse vector. Two version-filtered retrievers will
each request 30 Qdrant points from `dense` and `sparse`; RRF will merge their
rankings using the point id as the deduplication key. The default RRF constant
will be 60 and may be exposed as an advanced script option.

A server-side hybrid query was rejected because the required behavior is two
independently inspectable top-30 result lists followed by explicit RRF.

### Compress the first 20 fused documents with BGE reranking

The pipeline will pass the first 20 RRF documents to a BGE reranker-backed
LangChain document compressor. It will retain the highest-scoring 10 documents
for generation and show their score and provenance. The default reranker model
will be `BAAI/bge-reranker-v2-m3`, with a command-line override.

Passing all fused documents to reranking was rejected because it makes local
latency and resource use unbounded; retaining only dense retrieval was rejected
because it discards lexical matches.

### Use LangChain ChatOllama for the native local Ollama service

The script will use `ChatOllama` configured with `base_url` of
`http://localhost:11434` and model `qwen3.5:4b`. ChatOllama sends requests to
Ollama's native `/api/chat` interface. A grounded prompt will include the
question and labeled top-10 context chunks, instruct the model to state when
the context does not support an answer.

`ChatOpenAI` was rejected for this script because it targets the OpenAI
compatibility endpoint rather than the requested native Ollama chat endpoint.

### Make every retrieval stage auditable and citations machine-checkable

The script will configure a `hybrid_rag_test.log` file in its own directory.
For each question, it will log the effective configuration and the full chunk
records for dense top-30, sparse top-30, RRF order, reranker input top-20,
reranked top-10, and the exact ten chunks supplied to Ollama. Each record will
contain stable point id, rank, source and heading provenance, stage-specific
score where available, and chunk content.

The generation prompt will label each context block as `[chunk:<point-id>]` and
ask the model to cite those labels for factual claims. The script will extract
and log any returned chunk labels, but will not reject an answer because a label
is absent, malformed, or does not match the supplied top-10 set.

Logging only aggregate counts was rejected because it cannot diagnose rank
fusion or reranking quality.

### Keep the script version-aware and fail before partial answers

Arguments will default to `ocp-documents`, `http://localhost:6333`, OCP `4.22`,
and the requested models. Every Qdrant retrieval will filter on
`document_version`; unavailable services, incompatible vector schema, no
matching documents, reranker errors, and Ollama errors will print a clear
message and return to the prompt without emitting an unsupported answer.

## Risks / Trade-offs

- [BGE-M3 and BGE reranker model initialization is slow] → Lazily initialize
  models once per process, expose model names, and keep candidate limits fixed.
- [A dense or sparse result list is empty] → Continue RRF with the non-empty
  list and show per-retriever counts; fail only when fusion has no documents.
- [Qdrant payload lacks a stable id or content] → Validate required payload
  fields before RRF and omit malformed points with a reported warning.
- [Ollama returns an ungrounded answer] → Use a context-only prompt and print
  the exact reranked sources alongside the answer for inspection.
- [Verbose chunk logs grow quickly] → Use structured per-question records in
  the script-local log and include an explicit run boundary for each question.

## Migration Plan

1. Add the script, LangChain Ollama integration dependency, and offline fakes.
2. Run focused tests without Qdrant, models, or Ollama.
3. Run the interactive script against the existing OCP 4.22 Qdrant collection
   and local Ollama deployment.
4. Roll back by removing the standalone test script and its dependencies; no
   stored Qdrant points are changed by querying.

## Open Questions

- None.
