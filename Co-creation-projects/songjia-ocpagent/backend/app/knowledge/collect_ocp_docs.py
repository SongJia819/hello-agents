"""Collect the public OpenShift Container Platform 4.22 documentation corpus."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


CATALOG_URL = "https://docs.redhat.com/en/documentation/openshift_container_platform/4.22"
ALLOWED_HOST = "docs.redhat.com"
CATALOG_DOCUMENT_PATH = re.compile(
    r"^/en/documentation/openshift_container_platform/4\.22/html/([a-z0-9_-]+)/?(?:index)?/?$"
)
SINGLE_DOCUMENT_PATH = re.compile(
    r"^/en/documentation/openshift_container_platform/4\.22/html-single/([a-z0-9_-]+)/?(?:index)?/?$"
)
USER_AGENT = "ocp-agent-doc-collector/1.0 (+local knowledge corpus)"
REQUEST_TIMEOUT = (10, 60)
MAX_RESPONSE_BYTES = 50 * 1024 * 1024
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "docs" / "ocp-4.22"


class CollectionError(RuntimeError):
    """An expected collection failure that can be reported safely."""


@dataclass(frozen=True)
class DocumentSource:
    slug: str
    url: str


@dataclass(frozen=True)
class CollectionSummary:
    discovered: int
    completed: int
    skipped: int
    failed: int


def canonical_document_url(href: str, catalog_url: str = CATALOG_URL) -> DocumentSource | None:
    """Return the bounded html-single source represented by a catalog link."""

    parsed = urlsplit(urljoin(catalog_url, href))
    if parsed.scheme != "https" or parsed.netloc != ALLOWED_HOST:
        return None

    match = CATALOG_DOCUMENT_PATH.fullmatch(parsed.path)
    if match is None:
        match = SINGLE_DOCUMENT_PATH.fullmatch(parsed.path)
    if match is None:
        return None

    slug = match.group(1)
    return DocumentSource(
        slug=slug,
        url=(
            "https://docs.redhat.com/en/documentation/"
            f"openshift_container_platform/4.22/html-single/{slug}/index"
        ),
    )


def discover_documents(catalog_html: str, catalog_url: str = CATALOG_URL) -> list[DocumentSource]:
    soup = BeautifulSoup(catalog_html, "html.parser")
    documents = {
        document.url: document
        for anchor in soup.find_all("a", href=True)
        if (document := canonical_document_url(anchor["href"], catalog_url)) is not None
    }
    return [documents[url] for url in sorted(documents)]


def discover_local_documents(html_dir: Path) -> list[DocumentSource]:
    """Read validated raw-document sources from the shell downloader manifest."""

    path_patterns = {
        "html": CATALOG_DOCUMENT_PATH,
        "html-single": SINGLE_DOCUMENT_PATH,
    }
    document_format = html_dir.name
    path_pattern = path_patterns.get(document_format)
    if path_pattern is None:
        raise CollectionError("Raw HTML directory must be named html or html-single")

    manifest_path = html_dir.parent / f"{document_format}-manifest.tsv"
    try:
        with manifest_path.open(encoding="utf-8", newline="") as manifest_file:
            rows = list(csv.DictReader(manifest_file, delimiter="\t"))
    except OSError as error:
        raise CollectionError(f"Unable to read raw HTML manifest: {error}") from error

    documents: dict[str, DocumentSource] = {}
    for row in rows:
        source_url = row.get("url", "")
        parsed = urlsplit(source_url)
        match = path_pattern.fullmatch(parsed.path)
        if (
            parsed.scheme != "https"
            or parsed.netloc != ALLOWED_HOST
            or match is None
            or row.get("status") not in {"completed", "skipped"}
        ):
            continue

        slug = match.group(1)
        if row.get("slug") != slug or row.get("file") != f"{document_format}/{slug}.html":
            continue
        documents[source_url] = DocumentSource(slug=slug, url=source_url)

    if not documents:
        raise CollectionError(f"No completed raw OCP documents found in {manifest_path}")
    return [documents[url] for url in sorted(documents)]


def _validate_response(response: Any, url: str) -> str:
    if response.status_code < 200 or response.status_code >= 300:
        raise CollectionError(f"HTTP {response.status_code} while fetching {url}")

    content_type = response.headers.get("Content-Type", "").lower()
    if "text/html" not in content_type:
        raise CollectionError(f"Expected HTML content from {url}")

    content = response.content
    if len(content) > MAX_RESPONSE_BYTES:
        raise CollectionError(f"Response exceeded {MAX_RESPONSE_BYTES} bytes for {url}")
    return response.text


def fetch_html(session: requests.Session, url: str) -> str:
    try:
        response = session.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
        )
    except requests.RequestException as error:
        raise CollectionError(f"Request failed for {url}: {error}") from error
    return _validate_response(response, url)


def extract_markdown(html: str, source_url: str, retrieved_at: str | None = None) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("main article") or soup.select_one("main") or soup.select_one("article")
    if content is None:
        raise CollectionError(f"No main document content found in {source_url}")

    for element in content.select("nav, footer, header, script, style, noscript, aside"):
        element.decompose()

    heading = content.find("h1")
    page_title = heading.get_text(" ", strip=True) if heading else ""
    if not page_title and soup.title:
        page_title = soup.title.get_text(" ", strip=True)
    if not page_title:
        raise CollectionError(f"No document title found in {source_url}")

    body = markdownify(str(content), heading_style="ATX", strip=["img"])
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    if not body:
        raise CollectionError(f"Empty converted document for {source_url}")

    timestamp = retrieved_at or datetime.now(UTC).isoformat()
    markdown = (
        "---\n"
        f"title: {json.dumps(page_title, ensure_ascii=False)}\n"
        f"source_url: {source_url}\n"
        f"retrieved_at: {timestamp}\n"
        "---\n\n"
        f"{body}\n"
    )
    return page_title, markdown


def output_path_for(document: DocumentSource, output_dir: Path) -> Path:
    if not re.fullmatch(r"[a-z0-9_-]+", document.slug):
        raise CollectionError(f"Unsafe document slug: {document.slug}")
    root = output_dir.resolve()
    path = (root / f"{document.slug}.md").resolve()
    if path.parent != root:
        raise CollectionError("Document output path escaped the corpus root")
    return path


def local_html_path_for(document: DocumentSource, html_dir: Path) -> Path:
    root = html_dir.resolve()
    path = (root / f"{document.slug}.html").resolve()
    if path.parent != root:
        raise CollectionError("Raw HTML path escaped the corpus root")
    return path


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as temporary:
        temporary.write(content)
        temporary_path = Path(temporary.name)
    try:
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"documents": {}}
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CollectionError(f"Unable to read existing manifest: {error}") from error
    if not isinstance(manifest, dict) or not isinstance(manifest.get("documents"), dict):
        raise CollectionError("Existing manifest has an invalid structure")
    return manifest


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    atomic_write_text(path, json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def _convert_documents(
    documents: list[DocumentSource],
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    force: bool = False,
    load_document: Any = None,
    source_description: str = CATALOG_URL,
) -> CollectionSummary:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "manifest.json"
    manifest = load_manifest(manifest_path)
    entries: dict[str, dict[str, Any]] = manifest["documents"]
    manifest["catalog_url"] = source_description
    manifest["collected_at"] = datetime.now(UTC).isoformat()

    completed = skipped = failed = 0
    for document in documents:
        path = output_path_for(document, output_dir)
        previous = entries.get(document.url, {})
        if (
            not force
            and previous.get("status") == "completed"
            and path.is_file()
            and path.stat().st_size > 0
        ):
            skipped += 1
            continue

        try:
            title, markdown = extract_markdown(load_document(document), document.url)
            atomic_write_text(path, markdown)
            entries[document.url] = {
                "error": None,
                "output": path.name,
                "status": "completed",
                "title": title,
                "url": document.url,
            }
            completed += 1
        except CollectionError as error:
            entries[document.url] = {
                "error": str(error),
                "output": path.name,
                "status": "failed",
                "title": previous.get("title"),
                "url": document.url,
            }
            failed += 1
        write_manifest(manifest_path, manifest)

    return CollectionSummary(
        discovered=len(documents), completed=completed, skipped=skipped, failed=failed
    )


def collect(
    session: requests.Session,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    force: bool = False,
    limit: int | None = None,
) -> CollectionSummary:
    catalog_html = fetch_html(session, CATALOG_URL)
    documents = discover_documents(catalog_html)
    if not documents:
        raise CollectionError("The OCP 4.22 catalog did not contain any supported documents")
    if limit is not None:
        documents = documents[:limit]
    return _convert_documents(
        documents,
        output_dir,
        force,
        lambda document: fetch_html(session, document.url),
    )


def collect_local_html(
    html_dir: Path,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    force: bool = False,
    limit: int | None = None,
) -> CollectionSummary:
    html_dir = html_dir.resolve()
    documents = discover_local_documents(html_dir)
    if limit is not None:
        documents = documents[:limit]

    def load_document(document: DocumentSource) -> str:
        path = local_html_path_for(document, html_dir)
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as error:
            raise CollectionError(f"Unable to read raw HTML for {document.slug}: {error}") from error
        if not content.strip():
            raise CollectionError(f"Raw HTML for {document.slug} is empty")
        return content

    return _convert_documents(
        documents,
        output_dir,
        force,
        load_document,
        source_description=str(html_dir.parent / "html-manifest.tsv"),
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Refresh completed documents.")
    parser.add_argument(
        "--html-dir",
        type=Path,
        help="Convert downloaded raw HTML from this directory without network requests.",
    )
    parser.add_argument(
        "--limit", type=int, help="Collect at most this many documents for development."
    )
    arguments = parser.parse_args(argv)
    if arguments.limit is not None and arguments.limit < 1:
        parser.error("--limit must be at least 1")
    return arguments


def main(argv: list[str] | None = None) -> int:
    arguments = parse_args(argv)
    try:
        if arguments.html_dir is not None:
            summary = collect_local_html(
                arguments.html_dir, force=arguments.force, limit=arguments.limit
            )
        else:
            with requests.Session() as session:
                summary = collect(session, force=arguments.force, limit=arguments.limit)
    except CollectionError as error:
        print(f"Collection failed: {error}", file=sys.stderr)
        return 1

    print(
        "Collection complete: "
        f"discovered={summary.discovered} completed={summary.completed} "
        f"skipped={summary.skipped} failed={summary.failed}"
    )
    return 1 if summary.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
