import os
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from app.agents.knowledge.nodes import KnowledgeNodes
from app.agents.router.graph import RouterGraph
from app.agents.router.nodes import RouterNodes
from app.config.knowledge import KnowledgeSettings
from app.models.knowledge import KnowledgeChunk, KnowledgeRequest
from app.models.router import RouterResult
from app.services.knowledge_service import (
    KnowledgeAnswerService,
    QdrantRecallService,
    RRFFusionService,
    RerankService,
)


def chunk(point_id, content="content", **extra):
    return KnowledgeChunk(point_id=point_id, content=content, **extra)


class FakeEmbeddings:
    def embed_hybrid(self, _questions):
        return [([0.1, 0.2], {1: 0.3})]


class FakeQdrant:
    def __init__(self):
        self.calls = []

    def query_points(self, **kwargs):
        self.calls.append(kwargs)
        mode = kwargs["using"]
        points = [] if mode == "sparse" else [SimpleNamespace(
            id="point-1", score=0.8,
            payload={"content": "OCP evidence", "source_path": "docs/a.md", "heading_path": "A", "document_version": "4.22"},
        )]
        return SimpleNamespace(points=points)


class FakeReranker:
    def compute_score(self, pairs, normalize=True):
        self.pairs, self.normalize = pairs, normalize
        return [0.2 + index for index, _ in enumerate(pairs)]


class FakeChatModel:
    def __init__(self, answer="Use OADP [chunk:point-1]"):
        self.answer, self.messages = answer, []

    async def ainvoke(self, messages):
        self.messages = messages
        return SimpleNamespace(content=self.answer)


class FakeRouteLLM:
    async def ainvoke(self, _messages):
        return RouterResult(agent="knowledge", action="answer", resources=["documentation"])


class KnowledgeContractTests(unittest.TestCase):
    def test_configuration_defaults_and_environment_override(self):
        self.assertEqual(KnowledgeSettings().document_version, "4.22")
        with patch.dict(os.environ, {"OCP_KNOWLEDGE_DOCUMENT_VERSION": "4.23", "OCP_KNOWLEDGE_CONTEXT_LIMIT": "4"}, clear=False):
            settings = KnowledgeSettings.from_env()
        self.assertEqual(settings.document_version, "4.23")
        self.assertEqual(settings.context_limit, 4)

    def test_chunk_model_serializes_provenance(self):
        value = chunk("p", source_path="nodes.md", rrf_rank=1, rerank_score=0.9)
        self.assertEqual(value.model_dump()["source_path"], "nodes.md")
        self.assertEqual(value.rerank_score, 0.9)


class RetrievalServiceTests(unittest.TestCase):
    def test_recall_runs_dense_and_sparse_with_version_filter(self):
        client = FakeQdrant()
        dense, sparse = QdrantRecallService(KnowledgeSettings(), client, FakeEmbeddings()).recall(KnowledgeRequest(question="help"))
        self.assertEqual([item.point_id for item in dense], ["point-1"])
        self.assertEqual(sparse, [])
        self.assertEqual([call["using"] for call in client.calls], ["dense", "sparse"])
        self.assertEqual(client.calls[0]["query_filter"].must[0].match.value, "4.22")

    def test_rrf_deduplicates_and_supports_one_nonempty_ranking(self):
        fusion = RRFFusionService(60)
        result = fusion.fuse([chunk("same"), chunk("dense")], [chunk("same"), chunk("sparse")])
        self.assertEqual([item.point_id for item in result], ["same", "dense", "sparse"])
        self.assertEqual(result[0].rrf_rank, 1)
        self.assertEqual([item.point_id for item in fusion.fuse([], [chunk("only")])], ["only"])

    def test_reranker_limits_input_and_context(self):
        settings = KnowledgeSettings(rerank_input_limit=2, context_limit=1)
        reranker = FakeReranker()
        result = RerankService(settings, reranker).rerank("q", [chunk("a"), chunk("b"), chunk("c")])
        self.assertEqual(len(reranker.pairs), 2)
        self.assertEqual([item.point_id for item in result], ["b"])
        self.assertEqual(result[0].rerank_rank, 1)


class KnowledgeAnswerTests(unittest.IsolatedAsyncioTestCase):
    def _service(self, dense, sparse, reranked, chat_model=None):
        class Recall:
            def recall(self, _request):
                return dense, sparse

        class Rerank:
            def rerank(self, _question, _chunks):
                return reranked

        return KnowledgeAnswerService(
            recall_service=Recall(), rerank_service=Rerank(), chat_model=chat_model or FakeChatModel()
        )

    async def test_answer_uses_only_reranked_context_and_returns_citations(self):
        chat = FakeChatModel()
        result = await self._service([chunk("dense")], [], [chunk("point-1", "relevant")], chat).answer(KnowledgeRequest(question="What?"))
        self.assertTrue(result.successful)
        self.assertEqual(result.citations, ["point-1"])
        self.assertIn("[chunk:point-1]", chat.messages[1].content)
        self.assertNotIn("dense", chat.messages[1].content)

    async def test_no_evidence_does_not_call_llm(self):
        chat = FakeChatModel()
        result = await self._service([], [], [], chat).answer(KnowledgeRequest(question="What?"))
        self.assertEqual(result.failure_reason, "no_supporting_documentation")
        self.assertEqual(chat.messages, [])

    async def test_dependency_failure_returns_non_fabricated_fallback(self):
        class BrokenRecall:
            def recall(self, _request):
                raise RuntimeError("Qdrant down")

        result = await KnowledgeAnswerService(recall_service=BrokenRecall()).answer(KnowledgeRequest(question="What?"))
        self.assertIn("cannot retrieve", result.answer)
        self.assertIn("Qdrant down", result.failure_reason)

    async def test_knowledge_node_maps_result_to_state(self):
        result = await KnowledgeNodes(self._service([chunk("p")], [], [chunk("p")])).answer({"user_query": "help"})
        self.assertEqual(result["answer"], "Use OADP [chunk:point-1]")
        self.assertIsNotNone(result["knowledge_result"])


class KnowledgeRoutingTests(unittest.IsolatedAsyncioTestCase):
    async def test_structured_knowledge_intent_is_normalized_for_dispatch(self):
        result = await RouterNodes(router_llm=FakeRouteLLM()).route({"user_query": "How does OADP work?"})
        self.assertEqual(result["agent"], "knowledge")
        self.assertEqual(result["action"], "answer")
        self.assertEqual(result["resources"], ["documentation"])

    async def test_router_graph_registers_knowledge_terminal_node(self):
        class Agent:
            async def invoke(self, state):
                return state

        graph = RouterGraph(RouterNodes(router_llm=FakeRouteLLM()), Agent(), Agent(), Agent()).graph
        self.assertIn("knowledge", graph.get_graph().nodes)
