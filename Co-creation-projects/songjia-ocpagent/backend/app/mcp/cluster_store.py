"""SQLite-backed, strictly local fixture data for mock OCP MCP tools."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from app.config.mcp import mock_cluster_database_path
from app.models.cluster import ClusterSummary, Pod
from app.models.node import Node, NodeStatus


class MockClusterStore:
    def __init__(self, database_path: Path | None = None):
        self.database_path = database_path or mock_cluster_database_path()

    def _connect(self) -> sqlite3.Connection:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS clusters (
                    cluster_id TEXT PRIMARY KEY,
                    cluster_name TEXT NOT NULL,
                    cluster_ip TEXT NOT NULL,
                    cluster_port INTEGER NOT NULL
                );
                CREATE TABLE IF NOT EXISTS nodes (
                    node_id TEXT PRIMARY KEY,
                    cluster_id TEXT REFERENCES clusters(cluster_id),
                    name TEXT NOT NULL UNIQUE,
                    status TEXT NOT NULL CHECK (status IN ('new', 'added', 'reimage', 'removed')),
                    idrac_ip TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    domain TEXT NOT NULL,
                    network_port INTEGER NOT NULL,
                    network_ip TEXT NOT NULL,
                    network_netmask TEXT NOT NULL,
                    network_gateway TEXT NOT NULL,
                    image_name TEXT NOT NULL,
                    image_path TEXT NOT NULL,
                    firmware_name TEXT NOT NULL,
                    firmware_path TEXT NOT NULL,
                    certificate_file_name TEXT NOT NULL,
                    certificate_file_path TEXT NOT NULL,
                    CHECK ((status = 'added' AND cluster_id IS NOT NULL) OR
                           (status != 'added' AND cluster_id IS NULL))
                );
                CREATE TABLE IF NOT EXISTS node_network_interfaces (
                    interface_id INTEGER PRIMARY KEY,
                    node_id TEXT NOT NULL REFERENCES nodes(node_id) ON DELETE CASCADE,
                    name TEXT NOT NULL,
                    mac_address TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    netmask TEXT NOT NULL,
                    gateway TEXT NOT NULL,
                    speed_mbps INTEGER NOT NULL,
                    is_primary INTEGER NOT NULL CHECK (is_primary IN (0, 1))
                );
                CREATE TABLE IF NOT EXISTS node_storage_devices (
                    storage_id INTEGER PRIMARY KEY,
                    node_id TEXT NOT NULL REFERENCES nodes(node_id) ON DELETE CASCADE,
                    device_name TEXT NOT NULL,
                    model TEXT NOT NULL,
                    capacity_gib INTEGER NOT NULL,
                    storage_type TEXT NOT NULL,
                    serial_number TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS namespaces (
                    namespace_id TEXT NOT NULL,
                    cluster_id TEXT NOT NULL REFERENCES clusters(cluster_id),
                    namespace_name TEXT NOT NULL,
                    PRIMARY KEY (namespace_id, cluster_id),
                    UNIQUE (cluster_id, namespace_name)
                );
                CREATE TABLE IF NOT EXISTS pods (
                    pod_name TEXT PRIMARY KEY,
                    cluster_id TEXT NOT NULL,
                    namespace_id TEXT NOT NULL,
                    pod_ip TEXT NOT NULL,
                    FOREIGN KEY (cluster_id) REFERENCES clusters(cluster_id),
                    FOREIGN KEY (namespace_id, cluster_id)
                        REFERENCES namespaces(namespace_id, cluster_id)
                );
                """
            )
            if connection.execute("SELECT 1 FROM clusters LIMIT 1").fetchone() is None:
                self._seed(connection)

    @staticmethod
    def _seed(connection: sqlite3.Connection) -> None:
        clusters = [
            ("cluster-001", "Cluster 1", "192.168.1.10", 6443),
            ("cluster-002", "Cluster 2", "192.168.2.10", 6443),
        ]
        connection.executemany("INSERT INTO clusters VALUES (?, ?, ?, ?)", clusters)
        nodes = [
            ("node-001", "cluster-001", "cluster-001-worker-001", "added", "192.168.1.101", "admin", "Admin@123456", "agent.local", 8080, "192.168.1.100", "255.255.255.0", "192.168.1.1", "ollama-qwen3-4b", "/opt/docker/images/qwen3-4b.tar", "device-fw-v2.3.1", "/data/firmware/v2.3.1.bin", "agent-cert.pem", "/etc/ssl/certs/agent-cert.pem"),
            ("node-002", "cluster-002", "cluster-002-worker-001", "added", "192.168.2.101", "admin", "Admin@123456", "agent.local", 8080, "192.168.2.100", "255.255.255.0", "192.168.2.1", "ollama-qwen3-4b", "/opt/docker/images/qwen3-4b.tar", "device-fw-v2.3.1", "/data/firmware/v2.3.1.bin", "agent-cert.pem", "/etc/ssl/certs/agent-cert.pem"),
            ("node-new-001", None, "new-worker-001", "new", "192.168.10.101", "admin", "Admin@123456", "agent.local", 8080, "192.168.10.100", "255.255.255.0", "192.168.10.1", "pending-image", "/opt/docker/images/pending.tar", "device-fw-v2.3.1", "/data/firmware/v2.3.1.bin", "agent-cert.pem", "/etc/ssl/certs/agent-cert.pem"),
            ("node-reimage-001", None, "reimage-worker-001", "reimage", "192.168.11.101", "admin", "Admin@123456", "agent.local", 8080, "192.168.11.100", "255.255.255.0", "192.168.11.1", "reimage-pending", "/opt/docker/images/reimage.tar", "device-fw-v2.3.1", "/data/firmware/v2.3.1.bin", "agent-cert.pem", "/etc/ssl/certs/agent-cert.pem"),
            ("node-removed-001", None, "removed-worker-001", "removed", "192.168.12.101", "admin", "Admin@123456", "agent.local", 8080, "192.168.12.100", "255.255.255.0", "192.168.12.1", "retired-image", "/opt/docker/images/retired.tar", "device-fw-v2.3.1", "/data/firmware/v2.3.1.bin", "agent-cert.pem", "/etc/ssl/certs/agent-cert.pem"),
        ]
        connection.executemany("INSERT INTO nodes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", nodes)
        interfaces = [
            (node_id, "eno1", f"00:25:90:00:00:{index:02x}", ip, "255.255.255.0", gateway, 10000, 1)
            for index, (node_id, _, _, _, _, _, _, _, _, ip, _, gateway, *_) in enumerate(nodes, 1)
        ]
        connection.executemany(
            "INSERT INTO node_network_interfaces (node_id, name, mac_address, ip, netmask, gateway, speed_mbps, is_primary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            interfaces,
        )
        storage = [
            (node_id, "/dev/sda", "Mock NVMe", 960, "nvme", f"MOCK-{index:04d}")
            for index, (node_id, *_) in enumerate(nodes, 1)
        ]
        connection.executemany(
            "INSERT INTO node_storage_devices (node_id, device_name, model, capacity_gib, storage_type, serial_number) VALUES (?, ?, ?, ?, ?, ?)",
            storage,
        )
        connection.executemany(
            "INSERT INTO namespaces VALUES (?, ?, ?)",
            [("ns-default-001", "cluster-001", "default"), ("ns-ocp-001", "cluster-001", "openshift-monitoring"),
             ("ns-default-002", "cluster-002", "default"), ("ns-ocp-002", "cluster-002", "openshift-monitoring")],
        )
        connection.executemany(
            "INSERT INTO pods VALUES (?, ?, ?, ?)",
            [("cluster-001-api-7d8f9c6b5d-xk2lm", "cluster-001", "ns-default-001", "10.128.0.21"),
             ("cluster-001-worker-6b7c8d9e4f-pq3rs", "cluster-001", "ns-ocp-001", "10.128.0.22"),
             ("cluster-002-api-7d8f9c6b5d-xk2lm", "cluster-002", "ns-default-002", "10.129.0.21"),
             ("cluster-002-worker-6b7c8d9e4f-pq3rs", "cluster-002", "ns-ocp-002", "10.129.0.22")],
        )

    def list_clusters(self) -> list[ClusterSummary]:
        self.initialize()
        with self._connect() as connection:
            rows = connection.execute("SELECT cluster_id, cluster_name FROM clusters ORDER BY cluster_id").fetchall()
        return [ClusterSummary.model_validate(dict(row)) for row in rows]

    def list_nodes(self, cluster_id: str) -> list[Node]:
        self.initialize()
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT * FROM nodes WHERE cluster_id = ? AND status = 'added' ORDER BY name", (cluster_id,)
            ).fetchall()
            return [self._node_from_row(connection, row) for row in rows]

    def _node_from_row(self, connection: sqlite3.Connection, row: sqlite3.Row) -> Node:
        interfaces = [dict(item) for item in connection.execute(
            "SELECT name, mac_address, ip, netmask, gateway, speed_mbps, is_primary FROM node_network_interfaces WHERE node_id = ? ORDER BY interface_id", (row["node_id"],)
        )]
        storage = [dict(item) for item in connection.execute(
            "SELECT device_name, model, capacity_gib, storage_type, serial_number FROM node_storage_devices WHERE node_id = ? ORDER BY storage_id", (row["node_id"],)
        )]
        return Node.model_validate({
            "name": row["name"], "cluster_id": row["cluster_id"], "status": NodeStatus(row["status"]), "idrac_ip": row["idrac_ip"],
            "username": row["username"], "password": row["password"], "domain": row["domain"],
            "network": {"port": row["network_port"], "ip": row["network_ip"], "netmask": row["network_netmask"], "gateway": row["network_gateway"]},
            "image": {"image_name": row["image_name"], "image_path": row["image_path"]},
            "firmware": {"firmware_name": row["firmware_name"], "firmware_path": row["firmware_path"]},
            "certificate": {"certificate_file_name": row["certificate_file_name"], "certificate_file_path": row["certificate_file_path"]},
            "network_interfaces": interfaces, "storage_devices": storage,
        })

    def list_pods(self, cluster_id: str) -> list[Pod]:
        self.initialize()
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT pod_name, pod_ip FROM pods WHERE cluster_id = ? ORDER BY pod_name", (cluster_id,)
            ).fetchall()
        return [Pod.model_validate(dict(row)) for row in rows]

    def health_check(self) -> bool:
        self.initialize()
        with self._connect() as connection:
            return connection.execute("SELECT 1").fetchone()[0] == 1
