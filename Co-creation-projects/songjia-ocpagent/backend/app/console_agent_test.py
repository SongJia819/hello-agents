"""Run the mock MCP server and Router Agent in an interactive local console.

Run with: ``PYTHONPATH=backend python -m app.console_agent_test``.
"""

from __future__ import annotations

import asyncio
import inspect
import json
import os
import signal
import sys
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Any

MCP_HOST = "127.0.0.1"
MCP_PORT = 8001
MCP_MODULE = "app.mcp.server"
STARTUP_TIMEOUT_SECONDS = 10.0
SHUTDOWN_TIMEOUT_SECONDS = 5.0
SENSITIVE_FIELDS = {"username", "password", "token", "api_key", "apikey", "secret"}


class MCPStartupError(RuntimeError):
    """The local mock MCP service could not be made ready."""


def find_existing_mcp_pids(proc_root: Path = Path("/proc")) -> list[int]:
    """Return only processes explicitly launched with ``app.mcp.server``."""

    pids: list[int] = []
    for entry in proc_root.iterdir():
        if not entry.name.isdigit():
            continue
        try:
            command = (entry / "cmdline").read_bytes().decode(errors="replace").split("\0")
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            continue
        if "-m" in command and MCP_MODULE in command:
            pids.append(int(entry.name))
    return pids


def _pid_is_running(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


async def stop_existing_mcp(pid: int, *, timeout: float = SHUTDOWN_TIMEOUT_SECONDS) -> None:
    """Gracefully stop one verified previous MCP server process."""

    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    deadline = asyncio.get_running_loop().time() + timeout
    while _pid_is_running(pid):
        if asyncio.get_running_loop().time() >= deadline:
            os.kill(pid, signal.SIGKILL)
            kill_deadline = asyncio.get_running_loop().time() + timeout
            while _pid_is_running(pid):
                if asyncio.get_running_loop().time() >= kill_deadline:
                    raise MCPStartupError(f"Previous MCP server process {pid} did not exit.")
                await asyncio.sleep(0.05)
            return
        await asyncio.sleep(0.05)


async def port_is_open(host: str = MCP_HOST, port: int = MCP_PORT) -> bool:
    try:
        _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=0.3)
    except (OSError, TimeoutError):
        return False
    writer.close()
    await writer.wait_closed()
    return True


async def wait_for_mcp_ready(*, timeout: float = STARTUP_TIMEOUT_SECONDS) -> None:
    deadline = asyncio.get_running_loop().time() + timeout
    while asyncio.get_running_loop().time() < deadline:
        if await port_is_open():
            return
        await asyncio.sleep(0.1)
    raise MCPStartupError(f"MCP server did not become ready on {MCP_HOST}:{MCP_PORT}.")


async def spawn_mcp_server() -> asyncio.subprocess.Process:
    return await asyncio.create_subprocess_exec(sys.executable, "-m", MCP_MODULE)


async def stop_managed_process(process: Any, *, timeout: float = SHUTDOWN_TIMEOUT_SECONDS) -> None:
    if process is None or process.returncode is not None:
        return
    process.terminate()
    try:
        await asyncio.wait_for(process.wait(), timeout=timeout)
    except TimeoutError:
        process.kill()
        await process.wait()


async def start_fresh_mcp_server(
    *,
    find_pids: Callable[[], list[int]] = find_existing_mcp_pids,
    stop_pid: Callable[[int], Awaitable[None]] = stop_existing_mcp,
    is_port_open: Callable[[], Awaitable[bool]] = port_is_open,
    spawn: Callable[[], Awaitable[Any]] = spawn_mcp_server,
    wait_ready: Callable[[], Awaitable[None]] = wait_for_mcp_ready,
) -> Any:
    """Replace a prior project MCP process, then start and verify a fresh one."""

    for pid in find_pids():
        await stop_pid(pid)
    if await is_port_open():
        raise MCPStartupError(
            f"Port {MCP_PORT} is occupied by a process other than {MCP_MODULE}; refusing to stop it."
        )
    process = await spawn()
    try:
        await wait_ready()
    except Exception:
        await stop_managed_process(process)
        raise
    return process


def _sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _sanitize(item) for key, item in value.items() if key.lower() not in SENSITIVE_FIELDS}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if hasattr(value, "model_dump"):
        return _sanitize(value.model_dump())
    return value


def format_state(state: Any) -> str:
    return json.dumps(_sanitize(state), ensure_ascii=False, indent=2, default=str)


def frontend_result(state: dict[str, Any]) -> dict[str, Any]:
    route_keys = ("agent", "action", "resource", "resource_name", "cluster_name")
    return _sanitize({
        "route": {key: state[key] for key in route_keys if key in state},
        "supported": state.get("supported"),
        "answer": state.get("answer"),
        "result": state.get("tool_result"),
    })


async def _read_line(input_fn: Callable[[str], Any], prompt: str) -> str:
    value = input_fn(prompt)
    if inspect.isawaitable(value):
        value = await value
    return str(value)


async def console_loop(router_agent: Any, *, input_fn: Callable[[str], Any] = input,
                       output: Callable[[str], None] = print) -> None:
    while True:
        try:
            request = (await _read_line(input_fn, "ocp> ")).strip()
        except EOFError:
            return
        if request.lower() in {"exit", "quit"}:
            return
        if not request:
            continue
        try:
            final_state = None
            async for event in router_agent.stream({"user_query": request}):
                if event.get("event") == "final_result":
                    final_state = event.get("payload", {})
                else:
                    output(format_state(event))
        except Exception as error:
            output(f"Request failed: {error}")
            continue
        if final_state is not None:
            output(format_state(frontend_result(final_state)))


async def run_console(
    *,
    container_factory: Callable[[], Any] | None = None,
    start_server: Callable[[], Awaitable[Any]] = start_fresh_mcp_server,
    stop_server: Callable[[Any], Awaitable[None]] = stop_managed_process,
    input_fn: Callable[[str], Any] = input,
    output: Callable[[str], None] = print,
) -> None:
    if container_factory is None:
        from app.config.container import Container
        container_factory = Container
    process = None
    try:
        process = await start_server()
        container = container_factory()
        await container.initialize()
        output("MCP server and Router Agent are ready. Type 'exit' to quit.")
        await console_loop(container.router_agent, input_fn=input_fn, output=output)
    except MCPStartupError as error:
        output(f"MCP startup failed: {error}")
    except KeyboardInterrupt:
        output("Console interrupted.")
    finally:
        await stop_server(process)


def main() -> int:
    try:
        asyncio.run(run_console())
    except KeyboardInterrupt:
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
