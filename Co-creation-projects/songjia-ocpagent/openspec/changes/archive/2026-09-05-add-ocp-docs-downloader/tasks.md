## 1. Bounded Discovery And Conversion

- [x] 1.1 Add explicit HTTP, HTML parsing, and Markdown conversion dependencies
  required by the collector.
- [x] 1.2 Implement catalog discovery that normalizes and deduplicates only
  canonical public OCP 4.22 `html-single` URLs and rejects off-scope links.
- [x] 1.3 Implement document retrieval with timeouts, response validation, main
  content extraction, and Markdown conversion with source metadata.
- [x] 1.4 Derive safe stable output names under the managed OCP 4.22 corpus
  root and atomically write non-empty Markdown documents.

## 2. Resumable Corpus Collection

- [x] 2.1 Implement an atomically written manifest with per-document source,
  output path, title, status, and safe failure detail.
- [x] 2.2 Add default resume behavior, `--force` refresh behavior, `--limit`
  development control, progress reporting, and non-zero partial-failure status.

## 3. Test And Acquire

- [x] 3.1 Add fixture-based tests for in-scope discovery, off-scope rejection,
  clean Markdown conversion, safe paths, manifest updates, partial failure,
  resume, and forced refresh without live network access.
- [x] 3.2 Run the relevant automated tests and `openspec validate
  add-ocp-docs-downloader --strict`.
- [x] 3.3 Run the collector against the downloaded OCP 4.22 raw HTML corpus
  and inspect the manifest and representative Markdown files for complete/failed
  counts, source metadata, and non-empty content.

## 4. Raw HTML Corpus Acquisition

- [x] 4.1 Implement `download_ocp_4_22_html.sh` with bounded catalog route
  extraction, normal `curl` requests, safe output paths, and atomic writes.
- [x] 4.2 Add shell-level fixture tests for route filtering, resume behavior,
  forced refresh, and partial failure without live network access.
- [x] 4.3 Run the shell downloader against the official OCP 4.22 catalog and
  inspect its manifest and representative raw HTML files.

## 5. Complete Document Conversion

- [x] 5.1 Add resumable `--single-page` collection for bounded OCP 4.22
  `html-single` documents with a separate manifest.
- [x] 5.2 Update offline Markdown conversion to use the matching single-page
  manifest and add fixture coverage for complete-document sources.
- [x] 5.3 Download the complete single-page corpus, convert it to Markdown,
  and inspect manifest counts and representative document body content.
