import asyncio
import json

from app.config.container import Container


async def main():

    container = Container()
    await container.initialize()

    state = {
        "user_query": "list node"
    }

    print("\n========== Query Agent ==========\n")

    async for event in container.query_agent.stream(state):
        print(json.dumps(event, indent=2, ensure_ascii=False, default=str))

    print("\n========== Finished ==========")


if __name__ == "__main__":
    asyncio.run(main())