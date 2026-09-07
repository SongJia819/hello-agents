import asyncio
import json
import unittest
from types import SimpleNamespace

from app.config.container import Container
from app.agents.query.graph import QueryGraph
from app.agents.query.nodes import QueryNodes
from app.agents.router.nodes import RouterNodes
from app.models.cluster import ClusterSummary
from app.models.idrac import IdracNode
from app.models.router import RouterResult
from app.services.cluster_service import ClusterService


class FakeClusterService:
    def __init__(self):
        self.active_calls = 0
        self.max_active_calls = 0

    async def _result(self, resource):
        self.active_calls += 1
        self.max_active_calls = max(self.max_active_calls, self.active_calls)
        await asyncio.sleep(0)
        self.active_calls -= 1
        return [{"resource": resource}]

    async def list_nodes(self, cluster_id):
        return await self._result("node")

    async def list_pods(self, cluster_id):
        return await self._result("pod")

    async def list_idrac_nodes(self):
        return await self._result("idrac")

    async def get_idrac_node(self, selector):
        await self._result("idrac")
        records = {
            "DELLSN01": IdracNode.model_validate({
                "sn": "DELLSN01", "idrac_ip": "168.0.0.1", "system_information": {
                    "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                },
            }),
            "168.0.0.2": IdracNode.model_validate({
                "sn": "DELLSN02", "idrac_ip": "168.0.0.2", "system_information": {
                    "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                },
            }),
        }
        return records.get(selector)

    async def list_clusters(self):
        return [ClusterSummary(cluster_id="cluster-001", cluster_name="Cluster 1")]


class FakeAnswerLLM:
    async def ainvoke(self, _messages):
        return SimpleNamespace(content="mock query answer")


class FakeRouterLLM:
    async def ainvoke(self, _messages):
        return RouterResult(
            agent="query", action="list", resources=["idrac"],
            idrac_selectors=["DELLSN01", "168.0.0.2"],
        )


class FakeMCPClient:
    def __init__(self):
        self.calls = []

    async def call(self, tool_name, model, **kwargs):
        self.calls.append(("call", tool_name, model, kwargs))
        return []

    async def call_optional(self, tool_name, model, **kwargs):
        self.calls.append(("call_optional", tool_name, model, kwargs))
        return None


class GeneralListTests(unittest.IsolatedAsyncioTestCase):
    async def test_single_resource_list_returns_resource_keyed_result(self):
        for resource in ("node", "pod", "idrac"):
            with self.subTest(resource=resource):
                service = FakeClusterService()
                result = await QueryNodes(service).list(
                    {
                        "current_cluster": ClusterSummary(
                            cluster_id="cluster-001", cluster_name="Cluster 1"
                        ),
                        "resources": [resource],
                    }
                )

                self.assertEqual(
                    result["tool_result"], {resource: [{"resource": resource}]}
                )

    async def test_multiple_resources_are_listed_concurrently(self):
        service = FakeClusterService()
        result = await QueryGraph(QueryNodes(service, answer_llm=FakeAnswerLLM())).graph.ainvoke(
            {
                "user_query": "list node and pod",
                "resources": ["node", "pod"],
            }
        )

        self.assertEqual(set(result["tool_result"]), {"node", "pod"})
        self.assertGreaterEqual(service.max_active_calls, 2)

    async def test_selected_idrac_nodes_preserve_selector_order_and_deduplicate(self):
        service = FakeClusterService()
        result = await QueryNodes(service).list(
            {
                "current_cluster": ClusterSummary(cluster_id="cluster-001", cluster_name="Cluster 1"),
                "resources": ["idrac"],
                "idrac_selectors": ["168.0.0.2", "DELLSN01", "168.0.0.2", "UNKNOWN"],
            }
        )

        self.assertEqual(
            [node.model_dump() for node in result["tool_result"]["idrac"]],
            [
                {
                    "sn": "DELLSN02", "idrac_ip": "168.0.0.2", "system_information": {
                        "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                    }, "network_interfaces": [], "storage_devices": [],
                },
                {
                    "sn": "DELLSN01", "idrac_ip": "168.0.0.1", "system_information": {
                        "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                    }, "network_interfaces": [], "storage_devices": [],
                },
            ],
        )

    async def test_idrac_can_be_listed_with_cluster_resources(self):
        service = FakeClusterService()
        result = await QueryNodes(service).list(
            {
                "current_cluster": ClusterSummary(cluster_id="cluster-001", cluster_name="Cluster 1"),
                "resources": ["node", "pod", "idrac"],
            }
        )

        self.assertEqual(set(result["tool_result"]), {"node", "pod", "idrac"})
        self.assertGreaterEqual(service.max_active_calls, 3)


class RouterCapabilityTests(unittest.TestCase):
    def test_route_preserves_ordered_idrac_selectors(self):
        route = asyncio.run(RouterNodes(FakeRouterLLM()).route({"user_query": "list iDRAC nodes"}))

        self.assertEqual(route["resources"], ["idrac"])
        self.assertEqual(route["idrac_selectors"], ["DELLSN01", "168.0.0.2"])
        self.assertEqual(route["resource"], "idrac")

    def test_supported_list_action_and_resources(self):
        result = RouterNodes.capability_check(
            None,
            {"agent": "query", "action": "list", "resources": ["node", "pod", "idrac"]},
        )

        self.assertTrue(result["supported"])

    def test_unsupported_action_and_resource_are_rejected(self):
        action_result = RouterNodes.capability_check(
            None,
            {"agent": "query", "action": "delete", "resources": ["node"]},
        )
        resource_result = RouterNodes.capability_check(
            None,
            {"agent": "query", "action": "list", "resources": ["namespace"]},
        )

        self.assertFalse(action_result["supported"])
        self.assertFalse(resource_result["supported"])


class ClusterServiceIdracTests(unittest.IsolatedAsyncioTestCase):
    async def test_idrac_adapters_use_list_and_correct_selector_parameter(self):
        client = FakeMCPClient()
        service = ClusterService(client)

        await service.list_idrac_nodes()
        await service.get_idrac_node("DELLSN01")
        await service.get_idrac_node("168.0.0.2")

        self.assertEqual(client.calls[0][1], "list_idrac_nodes")
        self.assertEqual(client.calls[1][1:], ("get_idrac_node", IdracNode, {"sn": "DELLSN01"}))
        self.assertEqual(client.calls[2][1:], ("get_idrac_node", IdracNode, {"idrac_ip": "168.0.0.2"}))


async def main():
    container = Container()
    await container.initialize()

    for user_query in ("list node", "list pod", "list node and pod"):
        print("\n========== Router and Query Agent ==========\n")

        async for event in container.router_agent.stream({"user_query": user_query}):
            print(json.dumps(event, indent=2, ensure_ascii=False, default=str))

    print("\n========== Finished ==========")


if __name__ == "__main__":
    asyncio.run(main())
