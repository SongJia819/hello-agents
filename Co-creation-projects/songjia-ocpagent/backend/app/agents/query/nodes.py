import asyncio
import json
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from app.agents.query.prompts import QUERY_ANSWER_PROMPT
from app.config.llm import llm, llm_settings
from app.models.cluster import ClusterSummary
from app.observability import emit_progress, redact
from app.services.cluster_service import ClusterService
from app.services.llm_streaming import collect_streamed_answer


class QueryNodes:
    def __init__(self, cluster_service: ClusterService, answer_llm: Any = llm):
        self.cluster_service = cluster_service
        self.answer_llm = answer_llm

    async def resolve_cluster(self, state):
        emit_progress("query", "resolve_cluster", "cluster_resolution", "started", "正在确定集群。", state=state)
        clusters = await self.cluster_service.list_clusters()
        cluster: ClusterSummary = clusters[0]
        emit_progress("query", "resolve_cluster", "cluster_resolution", "completed", "集群已确定。", state=state)
        return {"current_cluster": cluster}

    async def list(self, state):
        emit_progress("query", "list", "resource_listing", "started", "正在查询资源。", state=state)
        cluster_id = state["current_cluster"].cluster_id
        resources = state["resources"]
        operations = {"node": self.cluster_service.list_nodes, "pod": self.cluster_service.list_pods}
        idrac_selectors = state.get("idrac_selectors", [])

        async def list_idrac_nodes():
            if not idrac_selectors:
                return await self.cluster_service.list_idrac_nodes()
            selected = await asyncio.gather(
                *(self.cluster_service.get_idrac_node(selector) for selector in idrac_selectors)
            )
            seen: set[str] = set()
            result = []
            for node in selected:
                if node is None or node.sn in seen:
                    continue
                seen.add(node.sn)
                result.append(node)
            return result

        requests = [
            list_idrac_nodes() if resource == "idrac" else operations[resource](cluster_id)
            for resource in resources
        ]
        results = await asyncio.gather(*requests)
        emit_progress("query", "list", "resource_listing", "completed", "资源查询完成。", state=state)
        return {"tool_result": dict(zip(resources, results, strict=True))}

    async def summarize_answer(self, state):
        result_json = json.dumps(redact(state["tool_result"]), ensure_ascii=False, default=self._json_default)
        answer = await collect_streamed_answer(
            self.answer_llm,
            [SystemMessage(content=QUERY_ANSWER_PROMPT), HumanMessage(content=(
                f"Question:\n{state['user_query']}\n\nMock MCP query result (JSON):\n{result_json}"))],
            agent="query", node="summarize_answer", state=state,
            attempts=llm_settings.empty_response_retry_limit,
            fallback="无法根据当前查询结果生成回答，请稍后重试。",
        )
        return {"answer": answer}

    @staticmethod
    def _json_default(value: Any) -> Any:
        return value.model_dump() if hasattr(value, "model_dump") else str(value)
