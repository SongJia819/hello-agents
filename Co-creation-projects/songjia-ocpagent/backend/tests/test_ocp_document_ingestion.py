import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from app.knowledge.ingest_ocp_docs import (
    BgeM3HybridEmbeddings,
    COLLECTION_NAME,
    DENSE_VECTOR_NAME,
    SPARSE_VECTOR_NAME,
    IngestionError,
    corpus_path,
    delete_version,
    ensure_collection,
    hybrid_points,
    load_chunks,
    main,
    point_id,
)


class FakeModel:
    def encode(self, texts, **_kwargs):
        return {
            "dense_vecs": [[0.6, 0.8] for _ in texts],
            "lexical_weights": [{"10": 0.4, "20": 0.2} for _ in texts],
        }


class FakeClient:
    def __init__(self, exists=False, vectors=None, sparse_vectors=None):
        self.exists = exists
        self.created = None
        self.deleted = []
        self._vectors = vectors
        self._sparse_vectors = sparse_vectors

    def collection_exists(self, _name):
        return self.exists

    def create_collection(self, **kwargs):
        self.created = kwargs
        self.exists = True
        self._vectors = kwargs["vectors_config"]
        self._sparse_vectors = kwargs["sparse_vectors_config"]

    def get_collection(self, _name):
        return SimpleNamespace(
            config=SimpleNamespace(
                params=SimpleNamespace(vectors=self._vectors, sparse_vectors=self._sparse_vectors)
            )
        )

    def delete(self, **kwargs):
        self.deleted.append(kwargs)


class OcpDocumentIngestionTests(unittest.TestCase):
    def _corpus(self, root: Path, version="4.22"):
        corpus = root / f"ocp-{version}"
        corpus.mkdir()
        (corpus / "architecture.md").write_text(
            "---\nsource_url: https://example.test/architecture\n---\n\n"
            "# Architecture\n\nIntro text.\n\n## Control plane\n\n"
            "This section contains enough words to split into several bounded chunks. " * 8,
            encoding="utf-8",
        )
        return corpus

    def test_version_selection_rejects_missing_and_traversal_corpora(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._corpus(root, "4.23")
            self.assertEqual(corpus_path(root, "4.23"), root / "ocp-4.23")
            with self.assertRaises(IngestionError):
                corpus_path(root, "4.22")
            with self.assertRaises(IngestionError):
                corpus_path(root, "../4.23")

    def test_header_chunks_preserve_version_source_heading_and_ordinals(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            corpus = self._corpus(root)
            _corpus, chunks = load_chunks(root, "4.22", chunk_size=90, chunk_overlap=10)

            self.assertGreater(len(chunks), 1)
            self.assertTrue(all(chunk.metadata["document_version"] == "4.22" for chunk in chunks))
            self.assertTrue(all(chunk.metadata["source_path"] == "architecture.md" for chunk in chunks))
            self.assertTrue(all(chunk.metadata["source_url"] == "https://example.test/architecture" for chunk in chunks))
            self.assertTrue(all(chunk.metadata["document_title"] == "Architecture" for chunk in chunks))
            self.assertEqual([chunk.metadata["chunk_ordinal"] for chunk in chunks], list(range(len(chunks))))
            control_plane = [chunk for chunk in chunks if "Control plane" in chunk.metadata["heading_path"]]
            self.assertTrue(control_plane)
            self.assertEqual(corpus, root / "ocp-4.22")

    def test_point_ids_and_hybrid_payloads_are_deterministic(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._corpus(root)
            _corpus, chunks = load_chunks(root, "4.22", chunk_size=1000, chunk_overlap=10)
            adapter = BgeM3HybridEmbeddings(model=FakeModel())
            vectors = adapter.embed_hybrid([chunk.page_content for chunk in chunks])
            points = hybrid_points(chunks, vectors)

            self.assertEqual(point_id(chunks[0]), point_id(chunks[0]))
            self.assertIn(DENSE_VECTOR_NAME, points[0].vector)
            self.assertIn(SPARSE_VECTOR_NAME, points[0].vector)
            self.assertEqual(points[0].payload["document_version"], "4.22")
            self.assertEqual(points[0].vector[SPARSE_VECTOR_NAME].indices, [10, 20])
            self.assertAlmostEqual(sum(value * value for value in points[0].vector[DENSE_VECTOR_NAME]), 1.0)

    def test_collection_creation_and_incompatible_schema_validation(self):
        client = FakeClient()
        ensure_collection(client, COLLECTION_NAME, 2)
        self.assertIn(DENSE_VECTOR_NAME, client.created["vectors_config"])
        self.assertIn(SPARSE_VECTOR_NAME, client.created["sparse_vectors_config"])

        incompatible = FakeClient(exists=True, vectors={}, sparse_vectors={})
        with self.assertRaisesRegex(IngestionError, "named vectors"):
            ensure_collection(incompatible, COLLECTION_NAME, 2)

    def test_version_filtered_replacement_only_targets_selected_version(self):
        client = FakeClient()
        delete_version(client, COLLECTION_NAME, "4.22")
        condition = client.deleted[0]["points_selector"].filter.must[0]
        self.assertEqual(condition.key, "document_version")
        self.assertEqual(condition.match.value, "4.22")

    def test_command_returns_nonzero_for_a_loading_failure(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            self.assertEqual(
                main(["--document-version", "4.22", "--documents-root", temporary_directory]),
                1,
            )


if __name__ == "__main__":
    unittest.main()
