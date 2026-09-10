## Why

The OCP knowledge corpus now stores BGE-M3 dense and sparse vectors, but there
is no interactive way to validate the complete hybrid retrieval and answer
generation path against the local Qdrant and Ollama services. A focused test
script is needed to make retrieval quality and grounded answers observable.

## What Changes

- Add an interactive knowledge test script that repeatedly accepts a user
  question and executes a fixed retrieval-to-answer pipeline.
- Retrieve 30 dense-vector and 30 sparse-vector candidates from the selected
  OCP document version, then merge the ranked lists with reciprocal rank
  fusion (RRF).
- Rerank the first 20 fused chunks with BGE Reranker and provide the best 10
  chunks plus the original question to local Ollama model `qwen3.5:4b`.
- Prefer LangChain retriever, RRF, reranker, document, prompt, and Ollama chat
  interfaces while retaining Qdrant's existing named hybrid-vector schema.
- Expose version, Qdrant endpoint, collection, model names, and result-count
  controls for repeatable local testing.
- Write every stage's chunks and ranks to a log file beside the script, and
  require generated answers to cite the stable identifiers of their supporting
  reranked chunks.

## Capabilities

### New Capabilities
- `hybrid-ocp-rag-evaluation`: Interactively retrieve, fuse, rerank, and answer
  OCP documentation questions from the versioned hybrid Qdrant corpus.

### Modified Capabilities

None.

## Impact

- Adds a new executable script and offline tests under `backend/app/knowledge/`
  and `backend/tests/`.
- Adds LangChain Ollama and BGE reranker-compatible dependencies as needed.
- Requires local Qdrant at `http://localhost:6333` and local Ollama at
  `http://localhost:11434` only when the interactive script is run.
