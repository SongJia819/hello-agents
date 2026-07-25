import unittest

import httpx

from app.api.main import create_app


class FakeRouterAgent:
    def __init__(self, state):
        self.state = state
        self.calls = []

    async def invoke(self, state):
        self.calls.append(state)
        return self.state


class FakeContainer:
    def __init__(self, state):
        self.router_agent = FakeRouterAgent(state)
        self.initialize_calls = 0

    async def initialize(self):
        self.initialize_calls += 1


class ChatApiTests(unittest.IsolatedAsyncioTestCase):
    async def post_chat(self, app, payload):
        async with app.router.lifespan_context(app):
            transport = httpx.ASGITransport(app=app)
            async with httpx.AsyncClient(
                transport=transport, base_url="http://testserver"
            ) as client:
                return await client.post("/v1/chat", json=payload)

    async def test_chat_forwards_message_and_sanitizes_result(self):
        container = FakeContainer(
            {
                "agent": "query",
                "action": "list",
                "resource": "node",
                "resource_name": "",
                "cluster_name": "mock-cluster",
                "supported": True,
                "tool_result": [
                    {
                        "name": "mock-cluster-worker-01",
                        "username": "demo-user",
                        "password": "demo-password",
                        "network": {"ip": "10.0.0.10", "token": "hidden"},
                    }
                ],
            }
        )
        app = create_app(lambda: container)

        response = await self.post_chat(app, {"message": "list nodes"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(container.initialize_calls, 1)
        self.assertEqual(container.router_agent.calls, [{"user_query": "list nodes"}])
        self.assertEqual(
            response.json(),
            {
                "message": "list nodes",
                "route": {
                    "agent": "query",
                    "action": "list",
                    "resource": "node",
                    "resource_name": "",
                    "cluster_name": "mock-cluster",
                },
                "supported": True,
                "answer": None,
                "result": [
                    {
                        "name": "mock-cluster-worker-01",
                        "network": {"ip": "10.0.0.10"},
                    }
                ],
            },
        )

    async def test_chat_rejects_missing_message_without_invoking_router(self):
        container = FakeContainer({"supported": True})
        app = create_app(lambda: container)

        response = await self.post_chat(app, {})

        self.assertEqual(response.status_code, 422)
        self.assertEqual(container.router_agent.calls, [])

    async def test_chat_returns_unsupported_result_without_tool_data(self):
        container = FakeContainer(
            {
                "agent": "query",
                "action": "list",
                "resource": "pod",
                "supported": False,
                "answer": "当前版本暂不支持 'pod' 功能。",
            }
        )
        app = create_app(lambda: container)

        response = await self.post_chat(app, {"message": "list pods"})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["supported"])
        self.assertEqual(response.json()["answer"], "当前版本暂不支持 'pod' 功能。")
        self.assertIsNone(response.json()["result"])
