## ADDED Requirements

### Requirement: Select a versioned OCP Markdown corpus
The system SHALL provide a new knowledge ingestion command under
`backend/app/knowledge/` that accepts a required document version and loads
only Markdown files from the corresponding configurable `ocp-<version>` corpus
directory. It SHALL not modify the legacy `ingest.py` implementation. The
command SHALL default its Qdrant endpoint to
`http://localhost:6333` and collection name to `ocp-documents` while accepting
command-line overrides for document root, endpoint, collection, model, and
batch size.

#### Scenario: Default OCP 4.22 corpus selection
- **WHEN** the command is run with document version `4.22` and no document-root
  override
- **THEN** it selects Markdown files beneath the managed `ocp-4.22` corpus

#### Scenario: Later version uses the same command
- **WHEN** the command is run with document version `4.23` and a matching local
  corpus exists
- **THEN** it selects only the OCP 4.23 Markdown files without code changes

#### Scenario: Legacy scripts remain isolated
- **WHEN** the versioned ingestion command is added
- **THEN** legacy `ingest.py`, `re-rank.py`, and `test_retrieval.py` remain
  behaviorally unchanged under `backend/app/knowledge/test/`

### Requirement: Chunk Markdown with heading provenance
The command SHALL use LangChain Markdown header splitting before recursive size
splitting. Every produced chunk SHALL retain its source file path, selected
document version, heading hierarchy, and deterministic chunk ordinal. It SHALL
preserve source URL metadata when Markdown front matter provides one.

#### Scenario: Heading section stays identifiable after splitting
- **WHEN** a Markdown heading section exceeds the configured chunk size
- **THEN** every resulting chunk retains the same heading hierarchy and source
  metadata while receiving a distinct chunk ordinal

#### Scenario: Version metadata is stored on every chunk
- **WHEN** chunks are generated from an OCP 4.22 corpus
- **THEN** every chunk metadata payload contains `document_version` with value
  `4.22`

### Requirement: Ingest BGE-M3 dense and sparse vectors
The command SHALL use the configurable BGE-M3 model default to generate both
normalized dense embeddings and sparse lexical vectors for each chunk. It SHALL
create or validate Qdrant named dense and sparse vector fields and upsert both
vector forms with each chunk payload into the selected collection.

#### Scenario: Hybrid point contains both vector representations
- **WHEN** a Markdown chunk is ingested successfully
- **THEN** its Qdrant point contains a dense BGE-M3 vector, a sparse BGE-M3
  vector, and the chunk metadata payload

#### Scenario: Incompatible collection schema fails before writes
- **WHEN** the selected collection lacks the required dense or sparse named
  vector fields
- **THEN** the command exits with a clear schema error before upserting chunks

### Requirement: Support repeatable and version-scoped ingestion
The command SHALL use deterministic point identifiers so a retry does not
create duplicate chunks. It SHALL support an explicit replacement option that
deletes only points whose `document_version` equals the selected version before
upserting replacement chunks.

#### Scenario: Retry upserts stable point identifiers
- **WHEN** the command is run twice with the same corpus and options
- **THEN** the second run reuses the same point identifiers rather than adding
  duplicate points

#### Scenario: Replacement preserves another document version
- **WHEN** replacement is requested for OCP 4.22 while OCP 4.23 points exist
- **THEN** only points tagged with `document_version` `4.22` are deleted

### Requirement: Report ingestion outcome safely
The command SHALL report selected version, discovered document count, generated
chunk count, upserted chunk count, target collection, and any failures. It
SHALL return a non-zero status when loading, embedding, collection validation,
or upsert fails.

#### Scenario: Qdrant outage is reported without destructive replacement
- **WHEN** Qdrant is unreachable before ingestion begins
- **THEN** the command reports the connection failure and does not delete or
  upsert any points
