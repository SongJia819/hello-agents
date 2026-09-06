"""Configuration for the local mock MCP SQLite store."""

from __future__ import annotations

import os
from pathlib import Path


def mock_cluster_database_path() -> Path:
    configured = os.getenv("OCP_MCP_SQLITE_PATH")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(__file__).resolve().parents[2] / "data" / "ocp_mock.sqlite3"
