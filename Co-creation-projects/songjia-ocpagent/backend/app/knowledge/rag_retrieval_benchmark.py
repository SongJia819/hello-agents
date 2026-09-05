"""Evaluate versioned OCP hybrid-retrieval quality against labeled chunks."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from langchain_core.documents import Document
from qdrant_client import QdrantClient

from app.knowledge.hybrid_rag_test import (
    DEFAULT_DOCUMENT_VERSION,
    DEFAULT_RERANKER_MODEL,
    RETRIEVAL_LIMIT,
    RRF_CONSTANT,
    BgeM3HybridEmbeddings,
    PipelineConfig,
    RetrievalError,
    create_reranker,
    fuse_documents,
    rerank_documents,
    retrieve_documents,
)
from app.knowledge.ingest_ocp_docs import COLLECTION_NAME, DEFAULT_MODEL_NAME, QDRANT_URL


DEFAULT_FIXTURE_PATH = Path(__file__).with_name("rag_retrieval_benchmark_cases.json")
DEFAULT_OUTPUT_DIRECTORY = Path(__file__).with_name("rag_benchmark_reports")
STAGE_NAMES = ("dense", "sparse", "rrf", "reranked")
METRIC_CUTOFFS = (10, 20, 30)
DEFAULT_RERANK_LIMIT = max(METRIC_CUTOFFS)


class BenchmarkError(RuntimeError):
    """A benchmark configuration or execution failure."""


class FixtureValidationError(BenchmarkError):
    """The configured expected chunk labels are invalid."""


@dataclass(frozen=True)
class BenchmarkCase:
    case_id: str
    question: str
    document_version: str
    expected_chunk_ids: tuple[str, ...]


@dataclass(frozen=True)
class BenchmarkFixture:
    fixture_version: int
    default_document_version: str
    cases: tuple[BenchmarkCase, ...]
    path: Path


@dataclass(frozen=True)
class BenchmarkConfig:
    fixture_path: Path = DEFAULT_FIXTURE_PATH
    document_version: str = DEFAULT_DOCUMENT_VERSION
    qdrant_url: str = QDRANT_URL
    collection_name: str = COLLECTION_NAME
    embedding_model: str = DEFAULT_MODEL_NAME
    reranker_model: str = DEFAULT_RERANKER_MODEL
    retrieval_limit: int = RETRIEVAL_LIMIT
    rerank_input_limit: int = DEFAULT_RERANK_LIMIT
    final_limit: int = DEFAULT_RERANK_LIMIT
    rrf_constant: int = RRF_CONSTANT
    output_directory: Path = DEFAULT_OUTPUT_DIRECTORY
    case_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class StageScore:
    retrieved_ids: tuple[str, ...]
    cutoff_scores: Mapping[int, "CutoffScore"]


@dataclass(frozen=True)
class CutoffScore:
    matched_ids: tuple[str, ...]
    missing_expected_ids: tuple[str, ...]
    precision: float
    recall: float


@dataclass(frozen=True)
class CaseResult:
    case: BenchmarkCase
    stages: Mapping[str, StageScore]
    error: str | None = None


def _require_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise FixtureValidationError(f"{path} must be a non-empty string")
    return value.strip()


def _parse_case(raw_case: Any, index: int) -> BenchmarkCase:
    if not isinstance(raw_case, dict):
        raise FixtureValidationError(f"cases[{index}] must be an object")
    case_id = _require_string(raw_case.get("id"), f"cases[{index}].id")
    question = _require_string(raw_case.get("question"), f"cases[{index}].question")
    document_version = _require_string(
        raw_case.get("document_version"), f"cases[{index}].document_version"
    )
    expected = raw_case.get("expected_chunk_ids")
    if not isinstance(expected, list) or not expected:
        raise FixtureValidationError(f"cases[{index}].expected_chunk_ids must be a non-empty list")
    expected_ids = tuple(_require_string(value, f"cases[{index}].expected_chunk_ids") for value in expected)
    if len(set(expected_ids)) != len(expected_ids):
        raise FixtureValidationError(f"cases[{index}].expected_chunk_ids must not contain duplicates")
    return BenchmarkCase(case_id, question, document_version, expected_ids)


def load_fixture(path: Path) -> BenchmarkFixture:
    """Load a strict, versioned benchmark fixture without contacting Qdrant."""

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise FixtureValidationError(f"Benchmark fixture does not exist: {path}") from error
    except json.JSONDecodeError as error:
        raise FixtureValidationError(f"Benchmark fixture is not valid JSON: {error}") from error
    if not isinstance(raw, dict):
        raise FixtureValidationError("Benchmark fixture root must be an object")
    if raw.get("fixture_version") != 1:
        raise FixtureValidationError("fixture_version must be 1")
    default_document_version = _require_string(
        raw.get("default_document_version"), "default_document_version"
    )
    raw_cases = raw.get("cases")
    if not isinstance(raw_cases, list) or not raw_cases:
        raise FixtureValidationError("cases must be a non-empty list")
    cases = tuple(_parse_case(raw_case, index) for index, raw_case in enumerate(raw_cases))
    case_ids = [case.case_id for case in cases]
    if len(set(case_ids)) != len(case_ids):
        raise FixtureValidationError("cases must have unique ids")
    if path.resolve() == DEFAULT_FIXTURE_PATH.resolve():
        if len(cases) != 250:
            raise FixtureValidationError("The default OCP 4.22 fixture must contain exactly 250 cases")
        if any(case.document_version != DEFAULT_DOCUMENT_VERSION for case in cases):
            raise FixtureValidationError("The default fixture cases must all use document version 4.22")
    return BenchmarkFixture(1, default_document_version, cases, path)


def select_cases(
    fixture: BenchmarkFixture, document_version: str, requested_case_ids: Iterable[str] = ()
) -> tuple[BenchmarkCase, ...]:
    requested = tuple(requested_case_ids)
    available = {case.case_id: case for case in fixture.cases if case.document_version == document_version}
    if requested:
        unknown = sorted(set(requested) - set(available))
        if unknown:
            raise FixtureValidationError(
                f"Selected case ids are not available for document version {document_version}: {', '.join(unknown)}"
            )
        return tuple(available[case_id] for case_id in requested)
    selected = tuple(available.values())
    if not selected:
        raise FixtureValidationError(f"Fixture has no cases for document version {document_version}")
    return selected


def validate_expected_chunks(client: Any, collection_name: str, cases: Sequence[BenchmarkCase]) -> None:
    """Ensure every expected point still belongs to the selected corpus version."""

    expected_versions: dict[str, str] = {}
    for case in cases:
        for point_id in case.expected_chunk_ids:
            previous_version = expected_versions.setdefault(point_id, case.document_version)
            if previous_version != case.document_version:
                raise FixtureValidationError(
                    f"Expected chunk {point_id} is assigned to more than one document version"
                )
    try:
        points = client.retrieve(
            collection_name=collection_name,
            ids=list(expected_versions),
            with_payload=["document_version"],
            with_vectors=False,
        )
    except Exception as error:
        raise FixtureValidationError(f"Could not validate expected chunks in Qdrant: {error}") from error
    found = {str(point.id): dict(point.payload or {}).get("document_version") for point in points}
    failures = []
    for point_id, expected_version in expected_versions.items():
        actual_version = found.get(point_id)
        if actual_version is None:
            failures.append(f"{point_id} is absent")
        elif actual_version != expected_version:
            failures.append(f"{point_id} has document_version {actual_version!r}, expected {expected_version!r}")
    if failures:
        raise FixtureValidationError("Invalid expected chunks: " + "; ".join(failures))


def unique_point_ids(documents: Sequence[Document]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for document in documents:
        point_id = document.metadata.get("point_id")
        if point_id is None:
            continue
        point_id = str(point_id)
        if point_id not in seen:
            seen.add(point_id)
            ordered.append(point_id)
    return tuple(ordered)


def score_documents(documents: Sequence[Document], expected_chunk_ids: Sequence[str]) -> StageScore:
    """Compute set-based precision and recall at all required ranking cutoffs."""

    retrieved_ids = unique_point_ids(documents)
    expected_ids = tuple(dict.fromkeys(str(point_id) for point_id in expected_chunk_ids))
    expected_set = set(expected_ids)
    cutoff_scores: dict[int, CutoffScore] = {}
    for cutoff in METRIC_CUTOFFS:
        top_ids = retrieved_ids[:cutoff]
        matched_ids = tuple(point_id for point_id in top_ids if point_id in expected_set)
        matched_set = set(matched_ids)
        missing_expected_ids = tuple(point_id for point_id in expected_ids if point_id not in matched_set)
        cutoff_scores[cutoff] = CutoffScore(
            matched_ids=matched_ids,
            missing_expected_ids=missing_expected_ids,
            precision=len(matched_ids) / len(top_ids) if top_ids else 0.0,
            recall=len(matched_ids) / len(expected_ids) if expected_ids else 0.0,
        )
    return StageScore(retrieved_ids=retrieved_ids, cutoff_scores=cutoff_scores)


def _pipeline_config(config: BenchmarkConfig) -> PipelineConfig:
    return PipelineConfig(
        document_version=config.document_version,
        qdrant_url=config.qdrant_url,
        collection_name=config.collection_name,
        embedding_model=config.embedding_model,
        reranker_model=config.reranker_model,
        retrieval_limit=config.retrieval_limit,
        rerank_input_limit=config.rerank_input_limit,
        context_limit=config.final_limit,
        rrf_constant=config.rrf_constant,
    )


def evaluate_case(
    case: BenchmarkCase,
    config: BenchmarkConfig,
    embeddings: BgeM3HybridEmbeddings,
    reranker: Any,
    client: Any,
) -> CaseResult:
    """Evaluate a single case without making an LLM request."""

    pipeline_config = _pipeline_config(config)
    try:
        dense, sparse = retrieve_documents(case.question, pipeline_config, embeddings, client)
        fused = fuse_documents(dense, sparse, pipeline_config)
        _rerank_input, reranked = rerank_documents(case.question, fused, reranker, pipeline_config)
        stages = {
            "dense": score_documents(dense, case.expected_chunk_ids),
            "sparse": score_documents(sparse, case.expected_chunk_ids),
            "rrf": score_documents(fused, case.expected_chunk_ids),
            "reranked": score_documents(reranked, case.expected_chunk_ids),
        }
        return CaseResult(case=case, stages=stages)
    except Exception as error:
        return CaseResult(case=case, stages={}, error=str(error))


def aggregate_stage_scores(results: Sequence[CaseResult]) -> dict[str, dict[str, dict[str, float | int]]]:
    aggregates: dict[str, dict[str, dict[str, float | int]]] = {}
    for stage_name in STAGE_NAMES:
        scores = [result.stages[stage_name] for result in results if stage_name in result.stages]
        stage_aggregates: dict[str, dict[str, float | int]] = {}
        for cutoff in METRIC_CUTOFFS:
            cutoff_scores = [score.cutoff_scores[cutoff] for score in scores]
            matched = sum(len(score.matched_ids) for score in cutoff_scores)
            retrieved = sum(min(len(score.retrieved_ids), cutoff) for score in scores)
            expected = sum(
                len(score.matched_ids) + len(score.missing_expected_ids) for score in cutoff_scores
            )
            stage_aggregates[f"top_{cutoff}"] = {
                "case_count": len(cutoff_scores),
                "macro_precision": (
                    sum(score.precision for score in cutoff_scores) / len(cutoff_scores)
                    if cutoff_scores
                    else 0.0
                ),
                "macro_recall": (
                    sum(score.recall for score in cutoff_scores) / len(cutoff_scores)
                    if cutoff_scores
                    else 0.0
                ),
                "micro_precision": matched / retrieved if retrieved else 0.0,
                "micro_recall": matched / expected if expected else 0.0,
                "matched_chunk_count": matched,
                "retrieved_chunk_count": retrieved,
                "expected_chunk_count": expected,
            }
        aggregates[stage_name] = stage_aggregates
    return aggregates


def _config_record(config: BenchmarkConfig) -> dict[str, Any]:
    record = asdict(config)
    record["fixture_path"] = str(config.fixture_path)
    record["output_directory"] = str(config.output_directory)
    record["case_ids"] = list(config.case_ids)
    return record


def report_record(
    fixture: BenchmarkFixture, config: BenchmarkConfig, results: Sequence[CaseResult], started_at: datetime
) -> dict[str, Any]:
    completed = [result for result in results if result.error is None]
    return {
        "created_at": datetime.now(UTC).isoformat(),
        "started_at": started_at.isoformat(),
        "fixture": {
            "path": str(fixture.path),
            "fixture_version": fixture.fixture_version,
            "default_document_version": fixture.default_document_version,
        },
        "configuration": _config_record(config),
        "selected_case_count": len(results),
        "completed_case_count": len(completed),
        "failed_case_count": len(results) - len(completed),
        "aggregate_metrics": aggregate_stage_scores(results),
        "cases": [
            {
                "id": result.case.case_id,
                "question": result.case.question,
                "document_version": result.case.document_version,
                "expected_chunk_ids": list(result.case.expected_chunk_ids),
                "error": result.error,
                "stages": {
                    stage_name: asdict(stage_score) for stage_name, stage_score in result.stages.items()
                },
            }
            for result in results
        ],
    }


def _markdown_report(record: Mapping[str, Any]) -> str:
    lines = [
        "# OCP RAG Retrieval Benchmark Report",
        "",
        f"- Created: {record['created_at']}",
        f"- Fixture: `{record['fixture']['path']}`",
        f"- Document version: `{record['configuration']['document_version']}`",
        f"- Cases: {record['completed_case_count']}/{record['selected_case_count']} completed",
        "",
        "## Aggregate Metrics",
        "",
        "| Stage | Cutoff | Cases | Macro precision | Macro recall | Micro precision | Micro recall |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for stage_name, cutoffs in record["aggregate_metrics"].items():
        for cutoff_name, metric in cutoffs.items():
            lines.append(
                "| {stage} | {cutoff} | {count} | {macro_p:.4f} | {macro_r:.4f} | {micro_p:.4f} | {micro_r:.4f} |".format(
                    stage=stage_name,
                    cutoff=cutoff_name.replace("top_", "top-"),
                    count=metric["case_count"],
                    macro_p=metric["macro_precision"],
                    macro_r=metric["macro_recall"],
                    micro_p=metric["micro_precision"],
                    micro_r=metric["micro_recall"],
                )
            )
    lines.extend(["", "## Case Results", ""])
    for case in record["cases"]:
        lines.extend([f"### {case['id']}", "", f"Question: {case['question']}", ""])
        if case["error"]:
            lines.extend([f"Error: `{case['error']}`", ""])
            continue
        lines.extend(
            [
                "| Stage | Cutoff | Precision | Recall | Matched IDs | Missing expected IDs |",
                "| --- | ---: | ---: | ---: | --- | --- |",
            ]
        )
        for stage_name, stage in case["stages"].items():
            for cutoff, score in stage["cutoff_scores"].items():
                lines.append(
                    "| {stage} | top-{cutoff} | {precision:.4f} | {recall:.4f} | {matched} | {missing} |".format(
                        stage=stage_name,
                        cutoff=cutoff,
                        precision=score["precision"],
                        recall=score["recall"],
                        matched=", ".join(score["matched_ids"]) or "-",
                        missing=", ".join(score["missing_expected_ids"]) or "-",
                    )
                )
        lines.append("")
    return "\n".join(lines)


def write_reports(record: Mapping[str, Any], output_directory: Path) -> tuple[Path, Path]:
    output_directory.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    json_path = output_directory / f"ocp-rag-retrieval-benchmark-{stamp}.json"
    markdown_path = output_directory / f"ocp-rag-retrieval-benchmark-{stamp}.md"
    json_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(_markdown_report(record) + "\n", encoding="utf-8")
    return json_path, markdown_path


def run_benchmark(
    config: BenchmarkConfig,
    *,
    client: Any | None = None,
    embeddings: BgeM3HybridEmbeddings | None = None,
    reranker: Any | None = None,
) -> tuple[dict[str, Any], tuple[Path, Path]]:
    fixture = load_fixture(config.fixture_path)
    selected_cases = select_cases(fixture, config.document_version, config.case_ids)
    client = client or QdrantClient(url=config.qdrant_url)
    validate_expected_chunks(client, config.collection_name, selected_cases)
    embeddings = embeddings or BgeM3HybridEmbeddings(config.embedding_model)
    reranker = reranker or create_reranker(config.reranker_model)
    started_at = datetime.now(UTC)
    results = [evaluate_case(case, config, embeddings, reranker, client) for case in selected_cases]
    record = report_record(fixture, config, results, started_at)
    return record, write_reports(record, config.output_directory)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE_PATH)
    parser.add_argument("--document-version", default=DEFAULT_DOCUMENT_VERSION)
    parser.add_argument("--qdrant-url", default=QDRANT_URL)
    parser.add_argument("--collection-name", default=COLLECTION_NAME)
    parser.add_argument("--embedding-model", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--reranker-model", default=DEFAULT_RERANKER_MODEL)
    parser.add_argument("--retrieval-limit", type=int, default=RETRIEVAL_LIMIT)
    parser.add_argument("--rerank-input-limit", type=int, default=DEFAULT_RERANK_LIMIT)
    parser.add_argument("--final-limit", type=int, default=DEFAULT_RERANK_LIMIT)
    parser.add_argument("--rrf-constant", type=int, default=RRF_CONSTANT)
    parser.add_argument("--output-directory", type=Path, default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--case", action="append", dest="case_ids", default=[])
    return parser.parse_args(argv)


def config_from_args(args: argparse.Namespace) -> BenchmarkConfig:
    if args.retrieval_limit < 1 or args.rerank_input_limit < 1 or args.final_limit < 1:
        raise BenchmarkError("retrieval and reranking limits must be positive")
    if args.rerank_input_limit > args.retrieval_limit * 2:
        raise BenchmarkError("rerank-input-limit cannot exceed the combined dense and sparse candidate depth")
    if args.final_limit > args.rerank_input_limit:
        raise BenchmarkError("final-limit cannot exceed rerank-input-limit")
    return BenchmarkConfig(
        fixture_path=args.fixture,
        document_version=args.document_version,
        qdrant_url=args.qdrant_url,
        collection_name=args.collection_name,
        embedding_model=args.embedding_model,
        reranker_model=args.reranker_model,
        retrieval_limit=args.retrieval_limit,
        rerank_input_limit=args.rerank_input_limit,
        final_limit=args.final_limit,
        rrf_constant=args.rrf_constant,
        output_directory=args.output_directory,
        case_ids=tuple(args.case_ids),
    )


def main(argv: Sequence[str] | None = None) -> int:
    try:
        config = config_from_args(parse_args(argv))
        record, paths = run_benchmark(config)
    except BenchmarkError as error:
        print(f"Benchmark failed: {error}", file=sys.stderr)
        return 2
    except RetrievalError as error:
        print(f"Benchmark failed: {error}", file=sys.stderr)
        return 2
    except Exception as error:
        print(f"Benchmark failed: {error}", file=sys.stderr)
        return 2
    print(f"JSON report: {paths[0]}")
    print(f"Markdown report: {paths[1]}")
    if record["failed_case_count"]:
        print(f"Completed with {record['failed_case_count']} failed case(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
