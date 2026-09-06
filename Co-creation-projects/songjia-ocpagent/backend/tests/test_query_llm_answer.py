import unittest
from types import SimpleNamespace

from app.agents.query.graph import QueryGraph
from app.agents.query.nodes import QueryNodes
from app.models.cluster import ClusterSummary


class FakeClusterService:
    async def list_clusters(self):
        return [ClusterSummary(cluster_id="cluster-001", cluster_name="Cluster 1")]

    async def list_nodes(self, _cluster_id):
        return [{"name": "worker-01", "status": "Ready"}]

    async def list_pods(self, _cluster_id):
        return [{"name": "console", "status": "Running"}]


class FakeLLM:
    def __init__(self, answer="The mock result contains one ready worker."):
        self.answer = answer
        self.messages = []

    async def ainvoke(self, messages):
        self.messages = messages
        return SimpleNamespace(content=self.answer)


class FailingLLM:
    async def ainvoke(self, _messages):
        raise RuntimeError("LLM unavailable")


class QueryLLMAnswerTests(unittest.IsolatedAsyncioTestCase):
    async def test_single_resource_answer_receives_question_and_json_result(self):
        chat = FakeLLM("节点查询完成。")
        graph = QueryGraph(QueryNodes(FakeClusterService(), answer_llm=chat)).graph

        result = await graph.ainvoke({"user_query": "有哪些节点？", "resources": ["node"]})

        self.assertEqual(result["answer"], "节点查询完成。")
        self.assertEqual(result["tool_result"]["node"][0]["name"], "worker-01")
        self.assertIn("有哪些节点？", chat.messages[1].content)
        self.assertIn('"worker-01"', chat.messages[1].content)

    async def test_multiple_resource_answer_retains_all_tool_results(self):
        chat = FakeLLM("节点和 Pod 查询完成。")
        graph = QueryGraph(QueryNodes(FakeClusterService(), answer_llm=chat)).graph

        result = await graph.ainvoke(
            {"user_query": "列出节点和 Pod", "resources": ["node", "pod"]}
        )

        self.assertEqual(result["answer"], "节点和 Pod 查询完成。")
        self.assertEqual(set(result["tool_result"]), {"node", "pod"})
        self.assertIn('"node"', chat.messages[1].content)
        self.assertIn('"pod"', chat.messages[1].content)

    async def test_llm_failure_keeps_tool_result_and_returns_honest_fallback(self):
        graph = QueryGraph(QueryNodes(FakeClusterService(), answer_llm=FailingLLM())).graph

        result = await graph.ainvoke({"user_query": "list node", "resources": ["node"]})

        self.assertEqual(result["tool_result"]["node"][0]["status"], "Ready")
        self.assertEqual(result["answer"], "无法根据当前查询结果生成回答，请稍后重试。")

    async def test_sensitive_mcp_fields_are_redacted_before_prompting_llm(self):
        chat = FakeLLM()
        nodes = QueryNodes(FakeClusterService(), answer_llm=chat)

        await nodes.summarize_answer(
            {
                "user_query": "list node",
                "tool_result": {"node": [{"name": "worker-01", "password": "secret"}]},
            }
        )

        self.assertIn('"password": "***"', chat.messages[1].content)
        self.assertNotIn("secret", chat.messages[1].content)
