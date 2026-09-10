## Why

The knowledge area has hand-authored Markdown documents but no reproducible
local corpus for OpenShift Container Platform 4.22. Acquiring the complete
official OCP 4.22 documentation set is needed to make later knowledge retrieval
cover the product rather than only one Architecture page.

## What Changes

- Add a Python command-line collector under `backend/app/knowledge/` that
  discovers the complete OCP 4.22 documentation set from the official Red Hat
  product/version directory, downloads each discovered `html-single` document,
  and converts its main content to Markdown.
- Create `backend/app/knowledge/docs/ocp-4.22/` as the managed corpus directory
  and emit one stable Markdown file per source document plus a JSON manifest.
- Restrict discovery and downloads to public `openshift_container_platform/4.22`
  URLs on `docs.redhat.com`; deduplicate documents and reject off-scope links.
- Make runs resumable and observable through per-document manifest status,
  source metadata, timeouts, response validation, safe writes, and a final
  partial-failure summary.
- Add fixture-based tests that validate discovery, conversion, manifests, and
  recovery without downloading live documentation.
- Add a shell downloader that first saves the OCP 4.22 catalog and every
  discovered canonical `html/<slug>` source page as raw HTML, allowing collection
  to use the normal `curl` path that the documentation service accepts.

## Capabilities

### New Capabilities
- `ocp-document-acquisition`: Discover, download, convert, and track the full
  public OCP 4.22 documentation corpus in local Markdown form.

### Modified Capabilities

None.

## Impact

- Adds collector and conversion modules, output-manifest support, tests, and
  small HTTP/HTML-to-Markdown dependencies under `backend/`.
- Produces a potentially large local corpus under `backend/app/knowledge/docs/`.
- Adds a raw HTML corpus beneath `backend/app/knowledge/docs/ocp-4.22/html/`
  and a shell-download manifest separate from Markdown conversion results.
- Adds a full-body `html-single/` corpus and matching manifest so converted
  Markdown contains document chapters instead of only multi-page entry-page
  abstracts.
- Does not alter Qdrant ingestion, call OpenShift/Kubernetes APIs, authenticate
  to Red Hat, or crawl any other product/version/site.
