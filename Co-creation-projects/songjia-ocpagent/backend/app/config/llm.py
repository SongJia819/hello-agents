from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="qwen3.5:4b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    temperature=0,
    max_tokens=11434,
)