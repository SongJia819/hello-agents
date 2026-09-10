import asyncio
import json
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from app.agents.query.prompts import QUERY_ANSWER_PROMPT
from app.config.llm import llm_settings, query_llm
from app.models.cluster import ClusterSummary
from app.observability import emit_progress, redact
from app.services.cluster_service import ClusterService
from app.services.llm_streaming import collect_streamed_answer


class QueryNodes:
    def __init__(self, cluster_service: ClusterService, answer_llm: Any = query_llm):
        self.cluster_service = cluster_service
        self.answer_llm = answer_llm

    async def resolve_cluster(self, state):
        emit_progress("query", "resolve_cluster", "cluster_resolution", "started", "正在确定集群。", state=state)
        clusters = await self.cluster_service.list_clusters()
        selector = state.get("current_work_cluster", "")
        cluster = next((item for item in clusters if selector and selector in {item.cluster_id, item.cluster_name}), None)
        if selector and cluster is None:
            emit_progress("query", "resolve_cluster", "cluster_resolution", "completed", "未找到指定集群。", state=state)
            return {"current_cluster": None, "cluster_not_found": True}
        cluster: ClusterSummary | None = cluster or (clusters[0] if clusters else None)
        emit_progress("query", "resolve_cluster", "cluster_resolution", "completed", "集群已确定。", state=state)
        return {"current_cluster": cluster}

    async def list(self, state):
        emit_progress("query", "list", "resource_listing", "started", "正在查询资源。", state=state)
        resources = state["resources"]
        if state.get("cluster_not_found"):
            return {"tool_result": {resource: [] for resource in resources}, "answer": "未找到指定集群。"}
        cluster_id = state["current_cluster"].cluster_id
        operations = {
            "node": lambda: self.cluster_service.list_nodes(cluster_id),
            "pod": lambda: self.cluster_service.list_pods(cluster_id),
            "idrac": lambda: self.cluster_service.list_idrac_nodes(state.get("idrac_selectors", [])),
            "cluster": self.cluster_service.list_clusters,
        }
        requests = [operations[resource]() for resource in resources]
        results = await asyncio.gather(*requests)
        emit_progress("query", "list", "resource_listing", "completed", "资源查询完成。", state=state)
        update = {"tool_result": dict(zip(resources, results, strict=True))}
        if "cluster" in resources:
            update["cluster_count"] = len(update["tool_result"]["cluster"])
        return update

    async def summarize_answer(self, state):
        result_json = json.dumps(redact(state["tool_result"]), ensure_ascii=False, default=self._json_default)
        cluster_count_context = ""
        if "cluster" in state.get("resources", []):
            cluster_count_context = f"\n\nCluster count: {state.get('cluster_count', 0)}"
        answer = await collect_streamed_answer(
            self.answer_llm,
            [SystemMessage(content=QUERY_ANSWER_PROMPT), HumanMessage(content=(
                f"Question:\n{state['user_query']}\n\nMock MCP query result (JSON):\n{result_json}{cluster_count_context}"))],
            agent="query", node="summarize_answer", state=state,
            attempts=llm_settings.empty_response_retry_limit,
            fallback="无法根据当前查询结果生成回答，请稍后重试。",
        )
        return {"answer": answer}

    @staticmethod
    def _json_default(value: Any) -> Any:
        return value.model_dump() if hasattr(value, "model_dump") else str(value)
