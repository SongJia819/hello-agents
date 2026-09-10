## Context

The legacy `backend/app/knowledge/ingest.py` only ingests a fixed hand-authored
document directory into `ocp_knowledge` with a dense BGE-small model and
character-based splitting. It, `re-rank.py`, and `test_retrieval.py` will move
unchanged to `backend/app/knowledge/test/`. The acquired OCP corpus instead lives beneath versioned
`docs/ocp-<version>/` directories and needs release-aware hybrid retrieval.

## Goals / Non-Goals

**Goals:**
- Ingest one selected local OCP Markdown corpus into `ocp-documents` at
  `http://localhost:6333`.
- Preserve Markdown heading context and document provenance on every chunk.
- Produce BGE-M3 dense and sparse representations in one Qdrant point.
- Make document version, source location, endpoint, collection, model, and
  batch controls command-line configurable.
- Support repeatable replacement for one version without deleting other
  versions in the collection.

**Non-Goals:**
- Download or convert OCP documentation in this change.
- Change agent retrieval prompts or implement user-facing search.
- Contact a live OpenShift cluster.
- Commit downloaded vendor documents or model weights.
- Modify the legacy ingestion, reranking, or retrieval demonstration logic.

## Decisions

### Use a versioned corpus root with explicit command parameters

The command will accept `--document-version` and resolve the default input to
`backend/app/knowledge/docs/ocp-<version>/`. `--documents-root` can override
the parent root for later releases or test fixtures. `--qdrant-url`,
`--collection-name`, `--model-name`, `--batch-size`, and `--replace-version`
make the operational contract explicit while preserving defaults requested for
OCP 4.22, Qdrant, `ocp-documents`, and BGE-M3.

Hard-coding the current corpus directory was rejected because it would require
code changes whenever another OCP release is acquired.

### Isolate legacy knowledge demonstrations from the new command

The new command will be a separately named script, leaving the relocated legacy
scripts unchanged. Moving the three existing scripts to `knowledge/test/`
prevents new production-oriented ingestion behavior from being added to the
demo entry point while retaining those examples for reference.

### Split by Markdown headings before enforcing chunk size

`MarkdownHeaderTextSplitter` will establish heading metadata for H1 through H6.
Any heading section that exceeds the configured size will be split with a
`RecursiveCharacterTextSplitter`, carrying its heading metadata into each
child chunk. Each chunk will add stable `source_path`, source URL when present
in front matter, heading path, chunk ordinal, and `document_version` metadata.

Pure character splitting was rejected because it loses section boundaries that
are needed to explain retrieved operational guidance.

### Store BGE-M3 hybrid vectors as named Qdrant vectors

The collection will be created or validated with a named dense vector and a
named sparse vector. A BGE-M3 adapter will provide normalized dense embeddings
and lexical sparse token-weight mappings suitable for Qdrant sparse vectors;
the adapter will be used through LangChain-compatible document and vector-store
boundaries. Upserts will use deterministic point identifiers derived from the
document version, source, heading path, chunk ordinal, and content.

Using `HuggingFaceEmbeddings` alone was rejected because it exposes only dense
vectors and cannot satisfy the required BGE-M3 sparse-vector ingestion.

### Replace only the selected version when requested

Default ingestion upserts deterministic chunk ids, allowing retries without
duplicate points. `--replace-version` first deletes points filtered by
`document_version`, then writes the selected corpus. It never deletes points
for a different version or collection.

Dropping the complete collection was rejected because later versions share the
same collection and must remain queryable.

## Risks / Trade-offs

- [BGE-M3 model download or CPU inference is slow] → Make the model name and
  batch size configurable, report progress, and test adapters without loading
  model weights.
- [Qdrant is unavailable or collection schema conflicts] → Validate connection
  and named vector schema before upserts; fail with a clear error and avoid
  deleting data unless `--replace-version` was explicitly requested.
- [Heading sections are extremely large] → Apply bounded recursive splitting
  after header splitting and retain the complete heading metadata on children.
- [Source front matter is malformed] → Preserve the file path and version;
  omit optional source URL rather than failing unrelated documents.

## Migration Plan

1. Add the versioned hybrid ingestion command and dependencies.
2. Add offline tests with fake embeddings and a fake Qdrant client.
3. Run unit tests without a Qdrant server or model download.
4. Manually run ingestion against OCP 4.22 when Qdrant and BGE-M3 are available.
5. Roll back by deleting points filtered on the selected `document_version`;
   existing source Markdown remains unchanged.

## Open Questions

- None. The first implementation will use the documented defaults and expose
  all environment-specific controls as command-line parameters.
