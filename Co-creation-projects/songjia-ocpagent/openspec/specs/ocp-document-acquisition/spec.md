# OCP Document Acquisition

## Purpose

Acquire and preserve the public OpenShift Container Platform 4.22 documentation
corpus as complete local Markdown with raw HTML provenance.

## Requirements

### Requirement: Preserve the complete OCP 4.22 source HTML corpus
The system SHALL provide `backend/app/knowledge/download_ocp_4_22_html.sh` to
download the configured OCP 4.22 catalog and every distinct in-scope
`html/<slug>` document it advertises. The script SHALL use normal `curl`
requests, accept only public `docs.redhat.com` OCP 4.22 URLs, and save each
successful document under `backend/app/knowledge/docs/ocp-4.22/html/` using a
safe slug-derived `.html` filename. It SHALL select only catalog document-tile
links so navigation routes are excluded.

#### Scenario: Catalog links produce raw HTML documents
- **WHEN** the OCP 4.22 catalog advertises distinct in-scope Architecture and
  Nodes document links
- **THEN** the shell downloader saves the catalog and one raw HTML file for
  each document under the managed corpus root

#### Scenario: Off-scope links are never downloaded
- **WHEN** the catalog includes a link to another product, another OCP version,
  or an external host
- **THEN** the shell downloader excludes that link from the raw HTML corpus

### Requirement: Resume raw HTML downloads safely
The shell downloader SHALL write a manifest with each source URL, output file,
and status. It SHALL preserve an existing non-empty successful HTML file on a
repeat run unless `--force` is supplied, and SHALL retain successful files when
one or more later downloads fail.

#### Scenario: Partial raw download can resume
- **WHEN** one raw HTML document download fails after others succeed
- **THEN** the manifest records the failure, successful HTML files remain, and
  the next run retries incomplete documents while skipping completed files

### Requirement: Discover the complete bounded OCP 4.22 document set
The system SHALL provide a Python command-line collector under
`backend/app/knowledge/` that starts from the configured public Red Hat OCP
4.22 product/version directory and discovers its canonical OCP 4.22
`html/<slug>/index` documentation links. It SHALL normalize each accepted slug
to the corresponding `html-single/<slug>/index` download URL, deduplicate URLs,
accept only `docs.redhat.com` URLs for `openshift_container_platform/4.22`, and
never fetch links outside that scope.

#### Scenario: Catalog discovery finds multiple OCP documents
- **WHEN** the official OCP 4.22 catalog contains links for Architecture and
  additional OCP 4.22 `html-single` documents
- **THEN** the collector records each distinct in-scope canonical document URL
  for collection

#### Scenario: Off-scope catalog links are ignored
- **WHEN** the catalog contains a link to another product, another version, or
  an external host
- **THEN** the collector does not download that link

#### Scenario: Empty or invalid catalog fails safely
- **WHEN** the catalog response is unsuccessful, non-HTML, or yields no
  in-scope document URLs
- **THEN** the collector exits non-zero without replacing the existing corpus
  manifest

### Requirement: Convert every discovered document to managed Markdown
The collector SHALL fetch every discovered in-scope document using explicit
timeouts and a user agent, reject unsuccessful or non-HTML responses, extract
the main/article content, and save one non-empty Markdown file per document
under `backend/app/knowledge/docs/ocp-4.22/`. Each file SHALL contain its title,
source URL, retrieval timestamp, and converted document body while excluding
navigation and footer content.

#### Scenario: Document content is converted cleanly
- **WHEN** a discovered document contains a main heading, paragraph, link,
  list, table, and code block
- **THEN** its Markdown file preserves the document content and excludes
  catalog navigation

#### Scenario: Managed output cannot escape the corpus root
- **WHEN** a discovered URL has an unexpected or unsafe path component
- **THEN** the collector rejects it rather than writing outside the OCP 4.22
corpus directory

#### Scenario: Downloaded raw HTML converts without network access
- **WHEN** the collector is run with `--html-dir` pointing at the raw HTML
  corpus and its downloader manifest
- **THEN** it converts every completed raw document to Markdown without making
  HTTP requests and records the raw document URL as source metadata

### Requirement: Preserve complete single-page document bodies
The shell downloader SHALL support `--single-page` to download every discovered
OCP 4.22 document from its canonical `html-single/<slug>/index` URL into an
`html-single/` corpus with a separate manifest. The collector SHALL convert this
corpus through `--html-dir` and preserve each single-page source URL.

#### Scenario: Single-page source produces substantive Markdown
- **WHEN** a complete `html-single` source contains document chapters
- **THEN** its generated Markdown contains the chapter content rather than only
  the multi-page entry-page abstract

### Requirement: Record resumable collection status
The collector SHALL maintain an atomically written
`backend/app/knowledge/docs/ocp-4.22/manifest.json` containing the catalog
source, collection timestamp, and one status record per discovered document.
Each record SHALL include canonical source URL, title when available,
output-relative path, status, and a safe error summary for failures. A repeat
run SHALL skip completed entries with a non-empty output, retry incomplete
entries, and refresh completed entries only when `--force` is supplied.

#### Scenario: Partial failure preserves successful documents
- **WHEN** one document fetch fails after other documents have converted
  successfully
- **THEN** the successful Markdown files and their completed manifest entries
  remain, the failed entry is recorded, and the collector exits non-zero

#### Scenario: Resume retries only incomplete documents
- **WHEN** a subsequent run finds completed manifest entries with non-empty
  output files and a prior failed entry
- **THEN** it skips completed documents and retries the failed document

#### Scenario: Forced collection refreshes completed documents
- **WHEN** `--force` is supplied for an existing complete entry
- **THEN** the collector replaces that document only after the refreshed
  download and conversion succeed

### Requirement: Report bounded collection outcomes
The collector SHALL report discovered, completed, skipped, and failed document
counts at completion. It SHALL process all discovered in-scope documents by
default; `--limit` MAY restrict processing only for development or testing.

#### Scenario: Default run covers the discovered corpus
- **WHEN** the collector runs without `--limit`
- **THEN** it attempts every discovered in-scope OCP 4.22 document
