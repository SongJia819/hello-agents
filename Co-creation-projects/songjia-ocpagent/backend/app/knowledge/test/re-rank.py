from typing import List, TypedDict
from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from FlagEmbedding import FlagReranker

# --------------------------
# 1. 定义状态
# --------------------------
class RAGState(TypedDict):
    query: str
    raw_candidates: List[str]   # 粗召回出来的chunk列表
    reranked_docs: List[tuple]  # [(score, doc), ...]
    final_context: List[str]
    answer: str

# --------------------------
# 2. 加载reranker模型 (BGE‑Reranker‑v2‑m3)
# --------------------------
reranker = FlagReranker("BAAI/bge-reranker-v2-m3", use_fp16=True)
llm = ChatOpenAI(model="qwen3.5:4b", base_url="http://localhost:11434/v1", api_key="dummy")

# --------------------------
# 3. 定义graph节点
# --------------------------
def retrieve_node(state: RAGState) -> RAGState:
    """模拟粗召回，这里替换成真实向量库召回"""
    # 模拟从向量库拿到一批候选
    mock_chunks = [
        "Pod无法删除常见原因1：finalizer未清理",
        "Java开发环境安装步骤 jdk17",
        "Pod无法删除常见原因2：存储PV/PVC无法释放",
        "mysql主从部署教程",
        "Pod无法删除：节点失联导致资源僵死",
        "redis集群搭建文档",
    ]
    return {"raw_candidates": mock_chunks}


def rerank_node(state: RAGState) -> RAGState:
    """Cross‑Encoder重排节点"""
    query = state["query"]
    candidates = state["raw_candidates"]

    score_doc_pairs = []
    for doc in candidates:
        # reranker入参 (query, doc)
        score = reranker.compute_score([query, doc], normalize=True)
        score_doc_pairs.append((score, doc))

    # 分数降序排序
    score_doc_pairs.sort(key=lambda x: x[0], reverse=True)
    return {"reranked_docs": score_doc_pairs}


def build_context_node(state: RAGState) -> RAGState:
    """取top‑3作为上下文"""
    top_k = 3
    top_items = state["reranked_docs"][:top_k]
    context_texts = [doc for (score, doc) in top_items]
    return {"final_context": context_texts}


def generate_answer_node(state: RAGState) -> RAGState:
    prompt = f"""基于下面上下文回答用户问题。
上下文：
{"\n".join(state["final_context"])}

问题：{state["query"]}
"""
    resp = llm.invoke(prompt)
    return {"answer": resp.content}

# --------------------------
# 4. 组装LangGraph工作流
# --------------------------
builder = StateGraph(RAGState)
builder.add_node("retrieve", retrieve_node)
builder.add_node("rerank", rerank_node)
builder.add_node("build_context", build_context_node)
builder.add_node("generate", generate_answer_node)

builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "rerank")
builder.add_edge("rerank", "build_context")
builder.add_edge("build_context", "generate")
builder.set_finish_point("generate")

graph = builder.compile()

# --------------------------
# 5. 运行
# --------------------------
if __name__ == "__main__":
    result = graph.invoke({"query": "Pod为什么删不掉"})
    print("=== Answer ===")
    print(result["answer"])
    print("\n=== Rerank分数 ===")
    for s, d in result["reranked_docs"]:
        print(f"{s:.3f} | {d}")
