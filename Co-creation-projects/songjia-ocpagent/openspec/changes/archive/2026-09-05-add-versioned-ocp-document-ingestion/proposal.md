## Why

The downloaded OCP corpus is versioned Markdown, but the existing knowledge
ingester only targets hand-authored documents, uses fixed-size chunks, and
stores a single dense vector model. A version-aware hybrid ingestion command is
needed so retrieval can distinguish OCP releases and use both semantic and
lexical signals.

## What Changes

- Add a new knowledge ingestion command under `backend/app/knowledge/` that
  loads Markdown from a selected `docs/ocp-<version>/` corpus without changing
  the legacy `ingest.py` implementation.
- Move legacy knowledge scripts `ingest.py`, `re-rank.py`, and
  `test_retrieval.py` unchanged into `backend/app/knowledge/test/` to separate
  demonstrations from the new ingestion command.
- Split Markdown by heading hierarchy with LangChain text splitters, retaining
  document title, source URL, heading path, chunk ordinal, and selected OCP
  version as metadata.
- Generate BGE-M3 dense and sparse vectors and upsert them into Qdrant at
  `http://localhost:6333` in the `ocp-documents` collection.
- Expose command-line parameters for document root, OCP version, Qdrant URL,
  collection name, embedding model, batch size, and replacement behavior so
  later OCP versions can be ingested without code changes.
- Add offline tests for version discovery, heading-aware chunks, metadata, and
  Qdrant payload construction; live Qdrant/model verification remains manual.

## Capabilities

### New Capabilities
- `versioned-ocp-knowledge-ingestion`: Chunk versioned OCP Markdown by heading
  and ingest hybrid BGE-M3 vectors with provenance metadata into Qdrant.

### Modified Capabilities

None.

## Impact

- Adds a new executable ingestion module and focused tests under `backend/`;
  relocates legacy knowledge scripts without changing their behavior.
- Adds LangChain/Qdrant and BGE-M3-compatible embedding dependencies as needed.
- Requires a reachable Qdrant instance only when actually ingesting; does not
  alter agent routing, MCP tools, or live OpenShift cluster behavior.
