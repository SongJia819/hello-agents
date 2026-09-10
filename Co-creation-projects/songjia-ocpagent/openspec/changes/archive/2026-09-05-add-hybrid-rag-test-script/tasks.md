## 1. Query Pipeline Setup

- [x] 1.1 Add the LangChain Ollama and BGE reranker-compatible dependencies for
  the standalone local RAG test script.
- [x] 1.2 Create a separately named configurable interactive knowledge test
  command without modifying the ingestion command or legacy examples.
- [x] 1.3 Define typed LangChain document and result models that retain Qdrant
  point id, document version, provenance, and retrieval diagnostics.
- [x] 1.4 Configure structured `hybrid_rag_test.log` output beside the script,
  with a distinct question/run boundary and stage-specific chunk records.

## 2. Hybrid Retrieval And Fusion

- [x] 2.1 Reuse or extract the BGE-M3 query encoder to produce normalized dense
  and lexical sparse query vectors.
- [x] 2.2 Implement version-filtered LangChain retrievers for Qdrant `dense`
  and `sparse` named vectors, each returning exactly up to 30 candidates and
  log every candidate's provenance and content.
- [x] 2.3 Implement stable-id deduplication and LangChain RRF/ensemble fusion
  with observable dense, sparse, and fused ranks, logging each fused chunk.
- [x] 2.4 Report unavailable Qdrant services, incompatible schemas, malformed
  payloads, and empty candidate lists without calling later pipeline stages.

## 3. Reranking And Grounded Generation

- [x] 3.1 Implement a LangChain-compatible BGE reranker compressor that scores
  only the first 20 fused chunks, logging its input and output chunks with
  scores and provenance metadata.
- [x] 3.2 Retain the best 10 reranked chunks and construct a context-only
  LangChain prompt with the original user question and `[chunk:<point-id>]`
  labels, then log the exact context chunks.
- [x] 3.3 Invoke local Ollama model `qwen3.5:4b` through LangChain ChatOllama
  and log any chunk citations from its answer without rejecting the answer for
  citation mismatches.
- [x] 3.4 Implement a terminal question loop with clean exit behavior and clear
  diagnostics for embedding, reranking, and Ollama failures.

## 4. Verification

- [x] 4.1 Add offline tests with fake Qdrant, BGE, reranker, and chat model
  adapters for version filtering, 30-per-mode retrieval, RRF order,
  deduplication, 20-to-10 reranking, full stage logging, and grounded prompt
  citation validation.
- [x] 4.2 Run focused automated tests and
  `openspec validate add-hybrid-rag-test-script --strict`.
- [x] 4.3 With local Qdrant, BGE models, and Ollama available, ask a known OCP
  4.22 question and inspect the two retrieval lists, fused/reranked sources,
  script-local chunk log, and generated answer citations.
