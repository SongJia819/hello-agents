import asyncio
import json

from app.config.container import Container


async def test_query():
    container = Container()
    await container.initialize()

    state = {
        "user_query": "list node"
    }

    print("\n========== Router Agent ==========\n")

    async for event in container.router_agent.stream(state):
        print(json.dumps(event, indent=2, ensure_ascii=False, default=str))

    print("\n========== Finished ==========\n")

    result = await container.router_agent.invoke(state)

    print("Final State:")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))

async def test_not_supported():
    container = Container()
    await container.initialize()

    state = {
        "user_query": "list pod"
    }

    print("\n========== Router Agent ==========\n")

    async for event in container.router_agent.stream(state):
        print(json.dumps(event, indent=2, ensure_ascii=False, default=str))

    print("\n========== Finished ==========\n")

    result = await container.router_agent.invoke(state)

    print("Final State:")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))




async def main():
    await test_query()
    await test_not_supported()


if __name__ == "__main__":
    asyncio.run(main())