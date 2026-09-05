from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from langchain_core.documents import Document

from app.knowledge.rag_retrieval_benchmark import (
    BenchmarkCase,
    BenchmarkConfig,
    CaseResult,
    CutoffScore,
    DEFAULT_FIXTURE_PATH,
    FixtureValidationError,
    StageScore,
    aggregate_stage_scores,
    evaluate_case,
    load_fixture,
    report_record,
    score_documents,
    select_cases,
    validate_expected_chunks,
    write_reports,
)


def document(point_id: str) -> Document:
    return Document(page_content=point_id, metadata={"point_id": point_id})


class FakePoint:
    def __init__(self, point_id: str, version: str) -> None:
        self.id = point_id
        self.payload = {"document_version": version}


class FakeClient:
    def __init__(self, points: list[FakePoint]) -> None:
        self.points = points

    def retrieve(self, **_kwargs: object) -> list[FakePoint]:
        return self.points


class RetrievalBenchmarkTests(unittest.TestCase):
    def write_fixture(self, payload: dict[str, object]) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "fixture.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_load_fixture_rejects_duplicate_case_ids(self) -> None:
        path = self.write_fixture(
            {
                "fixture_version": 1,
                "default_document_version": "4.22",
                "cases": [
                    {"id": "duplicate", "question": "one", "document_version": "4.22", "expected_chunk_ids": ["a"]},
                    {"id": "duplicate", "question": "two", "document_version": "4.22", "expected_chunk_ids": ["b"]},
                ],
            }
        )
        with self.assertRaisesRegex(FixtureValidationError, "unique ids"):
            load_fixture(path)

    def test_default_fixture_has_250_cases(self) -> None:
        fixture = load_fixture(DEFAULT_FIXTURE_PATH)
        self.assertEqual(len(fixture.cases), 250)
        self.assertEqual({case.document_version for case in fixture.cases}, {"4.22"})
        self.assertTrue(all(len(case.expected_chunk_ids) == 1 for case in fixture.cases))

    def test_select_cases_honors_version_and_requested_order(self) -> None:
        path = self.write_fixture(
            {
                "fixture_version": 1,
                "default_document_version": "4.22",
                "cases": [
                    {"id": "first", "question": "one", "document_version": "4.22", "expected_chunk_ids": ["a"]},
                    {"id": "other", "question": "two", "document_version": "4.21", "expected_chunk_ids": ["b"]},
                    {"id": "last", "question": "three", "document_version": "4.22", "expected_chunk_ids": ["c"]},
                ],
            }
        )
        fixture = load_fixture(path)
        selected = select_cases(fixture, "4.22", ["last", "first"])
        self.assertEqual([case.case_id for case in selected], ["last", "first"])

    def test_validate_expected_chunks_rejects_missing_or_wrong_version(self) -> None:
        cases = (BenchmarkCase("case", "question", "4.22", ("present", "missing")),)
        with self.assertRaisesRegex(FixtureValidationError, "missing is absent"):
            validate_expected_chunks(FakeClient([FakePoint("present", "4.21")]), "collection", cases)

    def test_score_documents_deduplicates_ids_and_calculates_metrics(self) -> None:
        documents = [document("a"), document("a")] + [document(f"id-{index}") for index in range(2, 31)]
        score = score_documents(documents, ["a", "id-15", "id-30"])
        self.assertEqual(score.retrieved_ids, ("a",) + tuple(f"id-{index}" for index in range(2, 31)))
        self.assertEqual(score.cutoff_scores[10].matched_ids, ("a",))
        self.assertEqual(score.cutoff_scores[10].recall, 1 / 3)
        self.assertEqual(score.cutoff_scores[20].matched_ids, ("a", "id-15"))
        self.assertEqual(score.cutoff_scores[20].precision, 0.1)
        self.assertEqual(score.cutoff_scores[30].matched_ids, ("a", "id-15", "id-30"))
        self.assertEqual(score.cutoff_scores[30].recall, 1.0)

    def test_evaluate_case_uses_dense_sparse_rrf_and_rerank_without_llm(self) -> None:
        case = BenchmarkCase("case", "question", "4.22", ("expected",))
        config = BenchmarkConfig()
        dense = [document("expected")]
        sparse = [document("sparse")]
        fused = [document("expected"), document("sparse")]
        reranked = [document("expected")]
        with patch("app.knowledge.rag_retrieval_benchmark.retrieve_documents", return_value=(dense, sparse)) as retrieve:
            with patch("app.knowledge.rag_retrieval_benchmark.fuse_documents", return_value=fused) as fuse:
                with patch("app.knowledge.rag_retrieval_benchmark.rerank_documents", return_value=(fused, reranked)) as rerank:
                    result = evaluate_case(case, config, object(), object(), object())
        self.assertIsNone(result.error)
        self.assertEqual(result.stages["reranked"].cutoff_scores[30].recall, 1.0)
        retrieve.assert_called_once()
        fuse.assert_called_once()
        rerank.assert_called_once()

    def test_reports_include_aggregate_metrics_and_case_diagnostics(self) -> None:
        case = BenchmarkCase("case", "question", "4.22", ("a",))
        stage = StageScore(
            ("a",),
            {
                cutoff: CutoffScore(("a",), (), 1.0, 1.0)
                for cutoff in (10, 20, 30)
            },
        )
        result = CaseResult(case, {stage_name: stage for stage_name in ("dense", "sparse", "rrf", "reranked")})
        aggregate = aggregate_stage_scores([result])
        self.assertEqual(aggregate["reranked"]["top_30"]["micro_recall"], 1.0)
        with tempfile.TemporaryDirectory() as directory:
            fixture = type("Fixture", (), {"path": Path("fixture.json"), "fixture_version": 1, "default_document_version": "4.22"})()
            record = report_record(fixture, BenchmarkConfig(output_directory=Path(directory)), [result], __import__("datetime").datetime.now(__import__("datetime").UTC))
            json_path, markdown_path = write_reports(record, Path(directory))
            self.assertIn("aggregate_metrics", json.loads(json_path.read_text(encoding="utf-8")))
            self.assertIn("### case", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
