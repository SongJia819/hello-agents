import asyncio
import json
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from app.agents.query.prompts import QUERY_ANSWER_PROMPT
from app.config.llm import llm
from app.services.cluster_service import ClusterService
from app.models.cluster import ClusterSummary
from app.observability import node_log, redact


class QueryNodes:

    def __init__(self, cluster_service: ClusterService, answer_llm: Any = llm):
        self.cluster_service = cluster_service
        self.answer_llm = answer_llm

    async def resolve_cluster(self, state):

        query = state["user_query"]

        clusters = await self.cluster_service.list_clusters()
        cluster: ClusterSummary = clusters[0]


        return {
            "current_cluster": cluster
        }

    async def list(self, state):
        cluster_id = state["current_cluster"].cluster_id
        resources = state["resources"]
        operations = {
            "node": self.cluster_service.list_nodes,
            "pod": self.cluster_service.list_pods,
        }

        results = await asyncio.gather(
            *(operations[resource](cluster_id) for resource in resources)
        )

        return {
            "tool_result": dict(zip(resources, results, strict=True))
        }

    async def summarize_answer(self, state):
        """Generate a user-facing answer without changing the MCP result."""

        try:
            result_json = json.dumps(
                redact(state["tool_result"]), ensure_ascii=False, default=self._json_default
            )
            response = await self.answer_llm.ainvoke(
                [
                    SystemMessage(content=QUERY_ANSWER_PROMPT),
                    HumanMessage(
                        content=(
                            f"Question:\n{state['user_query']}\n\n"
                            f"Mock MCP query result (JSON):\n{result_json}"
                        )
                    ),
                ]
            )
            return {"answer": str(response.content)}
        except Exception as error:
            node_log("query", "summarize_answer", "node_failed", state=state, error=error)
            return {"answer": "无法根据当前查询结果生成回答，请稍后重试。"}

    @staticmethod
    def _json_default(value: Any) -> Any:
        if hasattr(value, "model_dump"):
            return value.model_dump()
        return str(value)
