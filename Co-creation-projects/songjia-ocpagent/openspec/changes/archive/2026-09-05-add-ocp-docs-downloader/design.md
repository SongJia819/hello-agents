## Context

`backend/app/knowledge/documents/` contains a small hand-authored set of
Markdown files. The revised request is for the complete public OpenShift
Container Platform 4.22 documentation collection, not only the Architecture
document. Red Hat exposes this collection through versioned product navigation
and individual `html` documents. Raw HTML must be preserved first through the
normal `curl` path, then can be converted by the existing Python collector in a
separate offline phase.

## Goals / Non-Goals

**Goals:**
- Discover every supported OCP 4.22 `html-single` document from the official
  product/version directory.
- Save every discovered OCP 4.22 `html/<slug>` source document as raw
  HTML before conversion.
- Convert each document's main body into readable Markdown and retain source
  provenance.
- Maintain an atomic manifest that records discovered, completed, skipped, and
  failed documents for a resumable corpus acquisition.
- Test discovery and conversion with fixtures and mocked HTTP only.

**Non-Goals:**
- Crawl linked pages beyond the discovered OCP 4.22 document set, including
  other Red Hat products, versions, external sites, images, or attachments.
- Bypass authentication, access controls, rate limits, or site restrictions.
- Index documents into Qdrant or change the existing ingestion workflow.
- Commit downloaded vendor documentation by default.

## Decisions

### Discover from one bounded catalog and validate every URL

The collector begins from the OCP 4.22 product/version directory URL and parses
its canonical OCP 4.22 `html/<slug>/index` document links. It validates the
host and product/version path, then normalizes each accepted slug to its
corresponding `html-single/<slug>/index` download URL. It removes fragments and
query strings, deduplicates by canonical download URL, and sorts the collection
before download. Links outside that bound are recorded as ignored and are never
fetched.

Using arbitrary user URLs or recursively following every document hyperlink was
rejected because either approach could silently expand collection scope beyond
the requested product/version corpus.

### Convert individual document bodies into one-file-per-document Markdown

For each accepted source, the collector fetches with explicit timeouts and a
descriptive user agent, requires a successful HTML response, parses with
BeautifulSoup, selects a semantic main/article body, removes navigation/footer
elements, and converts the remaining HTML with `markdownify`. Each Markdown
file begins with title, source URL, and retrieval timestamp.

The normalized source slug determines a stable filename under
`backend/app/knowledge/docs/ocp-4.22/`; no URL component can escape that root.
Whole-page conversion was rejected because documentation navigation substantially
pollutes knowledge retrieval.

### Download raw HTML with a portable shell collector first

`download_ocp_4_22_html.sh` fetches the catalog with ordinary `curl`, extracts
only OCP 4.22 `html/<slug>` targets from its document tiles, deduplicates slugs,
and downloads each canonical `html/<slug>` document into
`backend/app/knowledge/docs/ocp-4.22/html/<slug>.html`. It uses `curl --fail`,
temporary files, and atomic replacement so rejected or incomplete HTTP results
do not become corpus files. A TSV manifest records each URL, output filename,
and status; repeat runs skip non-empty completed files unless `--force` is
provided.

The shell script does not parse or convert document bodies. HTML parsing for
Markdown remains Python's responsibility, while simple route extraction from a
catalog is kept deliberately bounded to the known public URL pattern.

The Python collector accepts `--html-dir` for this offline phase. It reads only
the raw downloader manifest entries whose status is completed or skipped,
validates their public OCP 4.22 source URLs and `html/<slug>.html` paths, and
converts those local files without making HTTP requests.

### Download complete single-page documents for Markdown conversion

The multi-page `html/<slug>` entry pages contain only a document abstract; the
complete content is served by `html-single/<slug>/index`. The shell downloader
therefore offers `--single-page`, which reuses bounded catalog discovery and
downloads each single-page source into `html-single/<slug>.html` with a separate
manifest. The Python collector selects the manifest based on whether `--html-dir`
points to `html/` or `html-single/`, preserving the matching canonical source URL.
Downloads retain a stable `.part` file and use curl range continuation so a large
single-page document can resume after an interrupted execution window.

### Track progress in an atomic manifest and resume by default

`manifest.json` records catalog URL, collector timestamp, each canonical source
URL, title, output-relative path, status (`completed`, `failed`, or `skipped`),
and a safe error summary when applicable. The collector writes the manifest and
each Markdown file through temporary sibling files followed by atomic replace.

On a repeat run, a completed entry with an existing non-empty output is skipped;
failed/missing entries are retried. `--force` refreshes completed entries. The
final exit status is non-zero if catalog discovery fails or any document fails,
but successful documents and their manifest entries remain for a later resume.
This balances complete-corpus intent with transient web failures.

### Offer bounded execution controls without shrinking default scope

The default behavior processes every discovered in-scope document. `--limit`
is available only for development/testing runs and `--force` for refreshes;
neither changes the allowed URL boundary. The collector reports total,
completed, skipped, and failed counts, which makes a long manual execution
auditable without hiding partial results.

## Risks / Trade-offs

- [Catalog markup changes or omits document links] → Validate a non-empty
  discovery result, use semantic and route-based extraction, and fail without
  modifying existing corpus data when discovery is unusable.
- [A full corpus is large or slow] → Use per-request timeouts, resumable
  manifest entries, stable filenames, and progress output rather than a single
  all-or-nothing file.
- [Individual pages fail transiently] → Preserve completed files, record safe
  errors, return non-zero, and retry only incomplete entries on the next run.
- [Markdown conversion loses complex formatting] → Preserve titles, headings,
  prose, links, lists, tables where supported, and code; retain the source URL
  for authoritative verification.
- [Licensing or site terms restrict redistribution] → Keep the corpus local,
  retain attribution, do not commit generated vendor text by default, and honor
  server responses and access controls.

## Migration Plan

1. Add bounded catalog discovery, document conversion, manifest handling, and
   explicit dependencies.
2. Add fixture/mocked-HTTP tests, including partial failure and resume cases.
3. Run automated validation without network access.
4. After implementation approval, run the collector against the official OCP
   4.22 catalog and inspect manifest counts and representative Markdown files.
5. Roll back by removing the collector and generated `docs/ocp-4.22/` corpus;
   existing hand-authored documents and vector-store data are unchanged.

## Open Questions

- The generated corpus remains untracked unless the repository owner explicitly
  decides to version downloaded Red Hat documentation.
