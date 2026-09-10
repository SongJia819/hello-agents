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
        self.idrac_list_calls = []
        self.node_cluster_ids = []
        self.pod_cluster_ids = []

    async def _result(self, resource):
        self.active_calls += 1
        self.max_active_calls = max(self.max_active_calls, self.active_calls)
        await asyncio.sleep(0)
        self.active_calls -= 1
        return [{"resource": resource}]

    async def list_nodes(self, cluster_id):
        self.node_cluster_ids.append(cluster_id)
        return await self._result("node")

    async def list_pods(self, cluster_id):
        self.pod_cluster_ids.append(cluster_id)
        return await self._result("pod")

    async def list_idrac_nodes(self, selectors=None):
        self.idrac_list_calls.append(selectors)
        if not selectors:
            return await self._result("idrac")
        await self._result("idrac")
        records = {
            "DELLSN01": IdracNode.model_validate({
                "sn": "DELLSN01", "idrac_ip": "168.0.0.1", "system_information": {
                    "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                },
            }),
            "DELLSN02": IdracNode.model_validate({
                "sn": "DELLSN02", "idrac_ip": "168.0.0.2", "system_information": {
                    "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                },
            }),
        }
        by_selector = {
            "DELLSN01": records["DELLSN01"],
            "DELLSN02": records["DELLSN02"],
            "168.0.0.1": records["DELLSN01"],
            "168.0.0.2": records["DELLSN02"],
        }
        seen = set()
        return [
            node for selector in selectors if (node := by_selector.get(selector)) is not None
            and not (node.sn in seen or seen.add(node.sn))
        ]

    async def list_clusters(self):
        return [
            ClusterSummary(cluster_id="cluster-001", cluster_name="Cluster 1", cluster_ip="10.0.0.1", cluster_port=6443),
            ClusterSummary(cluster_id="cluster-002", cluster_name="Cluster 2", cluster_ip="10.0.0.2", cluster_port=6443),
        ]


class FakeAnswerLLM:
    async def ainvoke(self, _messages):
        return SimpleNamespace(content="mock query answer")


class FakeRouterLLM:
    async def ainvoke(self, _messages):
        return RouterResult(
            agent="query", action="list", resources=["idrac"],
            idrac_selectors=["DELLSN01", "168.0.0.2"],
        )


class FakeTargetRouterLLM:
    async def ainvoke(self, _messages):
        return RouterResult(
            agent="query", action="list", resources=["node"],
            current_work_cluster="Cluster 2", current_work_node="worker-02",
        )


class FakeMCPClient:
    def __init__(self):
        self.calls = []
        self.records = {
            "DELLSN01": IdracNode.model_validate({
                "sn": "DELLSN01", "idrac_ip": "168.0.0.1", "system_information": {
                    "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                },
            }),
            "DELLSN02": IdracNode.model_validate({
                "sn": "DELLSN02", "idrac_ip": "168.0.0.2", "system_information": {
                    "manufacturer": "Dell", "model": "PowerEdge R750", "operating_system": "Red Hat Enterprise Linux 8.0",
                },
            }),
        }

    async def call(self, tool_name, model, **kwargs):
        self.calls.append(("call", tool_name, model, kwargs))
        if tool_name == "list_idrac_nodes":
            return list(self.records.values())
        return []

    async def call_optional(self, tool_name, model, **kwargs):
        self.calls.append(("call_optional", tool_name, model, kwargs))
        selector = kwargs.get("sn") or kwargs.get("idrac_ip")
        return {
            "DELLSN01": self.records["DELLSN01"],
            "168.0.0.1": self.records["DELLSN01"],
            "DELLSN02": self.records["DELLSN02"],
            "168.0.0.2": self.records["DELLSN02"],
        }.get(selector)


class GeneralListTests(unittest.IsolatedAsyncioTestCase):
    async def test_cluster_list_returns_all_cluster_summaries(self):
        service = FakeClusterService()
        result = await QueryNodes(service).list(
            {
                "current_cluster": (await service.list_clusters())[0],
                "resources": ["cluster"],
            }
        )

        self.assertEqual(result["cluster_count"], 2)
        self.assertEqual(
            [cluster.model_dump() for cluster in result["tool_result"]["cluster"]],
            [
                {"cluster_id": "cluster-001", "cluster_name": "Cluster 1", "cluster_ip": "10.0.0.1", "cluster_port": 6443},
                {"cluster_id": "cluster-002", "cluster_name": "Cluster 2", "cluster_ip": "10.0.0.2", "cluster_port": 6443},
            ],
        )

    async def test_explicit_cluster_selector_is_used_for_node_and_pod_lists(self):
        service = FakeClusterService()
        nodes = QueryNodes(service)
        resolved = await nodes.resolve_cluster({"current_work_cluster": "Cluster 2"})
        result = await nodes.list({**resolved, "resources": ["node", "pod"]})

        self.assertEqual(resolved["current_cluster"].cluster_id, "cluster-002")
        self.assertEqual(set(result["tool_result"]), {"node", "pod"})
        self.assertEqual(service.node_cluster_ids, ["cluster-002"])
        self.assertEqual(service.pod_cluster_ids, ["cluster-002"])

    async def test_missing_cluster_selector_uses_first_cluster(self):
        service = FakeClusterService()
        nodes = QueryNodes(service)
        resolved = await nodes.resolve_cluster({})
        await nodes.list({**resolved, "resources": ["node"]})

        self.assertEqual(resolved["current_cluster"].cluster_id, "cluster-001")
        self.assertEqual(service.node_cluster_ids, ["cluster-001"])

    async def test_unmatched_cluster_selector_does_not_list_first_cluster(self):
        service = FakeClusterService()
        nodes = QueryNodes(service)
        resolved = await nodes.resolve_cluster({"current_work_cluster": "missing-cluster"})
        result = await nodes.list({**resolved, "resources": ["node", "pod"]})

        self.assertTrue(resolved["cluster_not_found"])
        self.assertEqual(result["tool_result"], {"node": [], "pod": []})
        self.assertEqual(service.node_cluster_ids, [])
        self.assertEqual(service.pod_cluster_ids, [])

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
        self.assertEqual(
            service.idrac_list_calls,
            [["168.0.0.2", "DELLSN01", "168.0.0.2", "UNKNOWN"]],
        )

    async def test_serial_only_idrac_nodes_use_one_batch_request(self):
        service = FakeClusterService()
        result = await QueryNodes(service).list(
            {
                "current_cluster": ClusterSummary(cluster_id="cluster-001", cluster_name="Cluster 1"),
                "resources": ["idrac"],
                "idrac_selectors": ["DELLSN02", "DELLSN01", "DELLSN02", "UNKNOWN"],
            }
        )

        self.assertEqual([node.sn for node in result["tool_result"]["idrac"]], ["DELLSN02", "DELLSN01"])
        self.assertEqual(service.idrac_list_calls, [["DELLSN02", "DELLSN01", "DELLSN02", "UNKNOWN"]])

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
    def test_route_preserves_cluster_and_node_selectors(self):
        route = asyncio.run(RouterNodes(FakeTargetRouterLLM()).route({"user_query": "list worker-02 in Cluster 2"}))

        self.assertEqual(route["current_work_cluster"], "Cluster 2")
        self.assertEqual(route["current_work_node"], "worker-02")

    def test_route_uses_empty_selectors_when_none_are_supplied(self):
        route = asyncio.run(RouterNodes(FakeRouterLLM()).route({"user_query": "list iDRAC nodes"}))

        self.assertEqual(route["current_work_cluster"], "")
        self.assertEqual(route["current_work_node"], "")

    def test_route_preserves_ordered_idrac_selectors(self):
        route = asyncio.run(RouterNodes(FakeRouterLLM()).route({"user_query": "list iDRAC nodes"}))

        self.assertEqual(route["resources"], ["idrac"])
        self.assertEqual(route["idrac_selectors"], ["DELLSN01", "168.0.0.2"])
        self.assertEqual(route["resource"], "idrac")

    def test_supported_list_action_and_resources(self):
        result = RouterNodes.capability_check(
            None,
            {"agent": "query", "action": "list", "resources": ["node", "pod", "idrac", "cluster"]},
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
    async def test_idrac_list_uses_full_inventory_when_selectors_are_missing_or_empty(self):
        client = FakeMCPClient()
        service = ClusterService(client)

        await service.list_idrac_nodes()
        await service.list_idrac_nodes([])

        self.assertEqual(client.calls[0][1], "list_idrac_nodes")
        self.assertEqual(client.calls[0][3], {})
        self.assertEqual(client.calls[1][1:], ("list_idrac_nodes", IdracNode, {}))

    async def test_idrac_list_uses_one_batch_request_for_serial_selectors(self):
        client = FakeMCPClient()
        service = ClusterService(client)

        result = await service.list_idrac_nodes(["DELLSN01", "DELLSN02"])

        self.assertEqual([node.sn for node in result], ["DELLSN01", "DELLSN02"])
        self.assertEqual(
            client.calls,
            [("call", "list_idrac_nodes", IdracNode, {"sn": ["DELLSN01", "DELLSN02"]})],
        )

    async def test_idrac_list_uses_single_lookup_for_ip_or_mixed_selectors(self):
        client = FakeMCPClient()
        service = ClusterService(client)

        result = await service.list_idrac_nodes(["168.0.0.2", "DELLSN01", "168.0.0.2", "UNKNOWN"])

        self.assertEqual([node.sn for node in result], ["DELLSN02", "DELLSN01"])
        self.assertEqual(
            client.calls,
            [
                ("call_optional", "get_idrac_node", IdracNode, {"idrac_ip": "168.0.0.2"}),
                ("call_optional", "get_idrac_node", IdracNode, {"sn": "DELLSN01"}),
                ("call_optional", "get_idrac_node", IdracNode, {"idrac_ip": "168.0.0.2"}),
                ("call_optional", "get_idrac_node", IdracNode, {"sn": "UNKNOWN"}),
            ],
        )


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
