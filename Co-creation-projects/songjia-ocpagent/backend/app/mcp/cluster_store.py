"""SQLite-backed, strictly local fixture data for mock OCP MCP tools."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from app.config.mcp import mock_cluster_database_path
from app.models.cluster import ClusterSummary, Pod
from app.models.idrac import IdracNode
from app.models.node import Node, NodeOperationResult, NodeStatus


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
                    status TEXT NOT NULL CHECK (status IN ('new', 'added', 'cordoned', 'drained', 'reimage', 'removed')),
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
                    CHECK ((status IN ('added', 'cordoned', 'drained') AND cluster_id IS NOT NULL) OR
                           (status NOT IN ('added', 'cordoned', 'drained') AND cluster_id IS NULL))
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
                CREATE TABLE IF NOT EXISTS idrac_nodes (
                    idrac_node_id TEXT PRIMARY KEY,
                    sn TEXT NOT NULL UNIQUE,
                    idrac_ip TEXT NOT NULL UNIQUE,
                    manufacturer TEXT NOT NULL,
                    model TEXT NOT NULL,
                    operating_system TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS idrac_network_interfaces (
                    interface_id INTEGER PRIMARY KEY,
                    idrac_node_id TEXT NOT NULL REFERENCES idrac_nodes(idrac_node_id)
                        ON DELETE CASCADE,
                    name TEXT NOT NULL,
                    mac_address TEXT NOT NULL,
                    speed_mbps INTEGER NOT NULL
                );
                CREATE TABLE IF NOT EXISTS idrac_storage_devices (
                    storage_id INTEGER PRIMARY KEY,
                    idrac_node_id TEXT NOT NULL REFERENCES idrac_nodes(idrac_node_id)
                        ON DELETE CASCADE,
                    device_name TEXT NOT NULL,
                    model TEXT NOT NULL,
                    capacity_gib INTEGER NOT NULL,
                    storage_type TEXT NOT NULL,
                    serial_number TEXT NOT NULL UNIQUE
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
            self._migrate_legacy_nodes(connection)
            if connection.execute("SELECT 1 FROM clusters LIMIT 1").fetchone() is None:
                self._seed(connection)
            if connection.execute("SELECT 1 FROM idrac_nodes LIMIT 1").fetchone() is None:
                self._seed_idrac_inventory(connection)

    @staticmethod
    def _migrate_legacy_nodes(connection: sqlite3.Connection) -> None:
        schema = connection.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'nodes'"
        ).fetchone()
        if schema is None or "'cordoned'" in schema["sql"]:
            return
        connection.commit()
        connection.execute("PRAGMA foreign_keys = OFF")
        try:
            connection.executescript(
                """
                BEGIN;
                CREATE TABLE nodes_replacement (
                    node_id TEXT PRIMARY KEY,
                    cluster_id TEXT REFERENCES clusters(cluster_id),
                    name TEXT NOT NULL UNIQUE,
                    status TEXT NOT NULL CHECK (status IN ('new', 'added', 'cordoned', 'drained', 'reimage', 'removed')),
                    idrac_ip TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, domain TEXT NOT NULL,
                    network_port INTEGER NOT NULL, network_ip TEXT NOT NULL, network_netmask TEXT NOT NULL, network_gateway TEXT NOT NULL,
                    image_name TEXT NOT NULL, image_path TEXT NOT NULL, firmware_name TEXT NOT NULL, firmware_path TEXT NOT NULL,
                    certificate_file_name TEXT NOT NULL, certificate_file_path TEXT NOT NULL,
                    CHECK ((status IN ('added', 'cordoned', 'drained') AND cluster_id IS NOT NULL) OR
                           (status NOT IN ('added', 'cordoned', 'drained') AND cluster_id IS NULL))
                );
                INSERT INTO nodes_replacement SELECT * FROM nodes;
                DROP TABLE nodes;
                ALTER TABLE nodes_replacement RENAME TO nodes;
                COMMIT;
                """
            )
        finally:
            connection.execute("PRAGMA foreign_keys = ON")

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

    @staticmethod
    def _seed_idrac_inventory(connection: sqlite3.Connection) -> None:
        nodes = [
            (f"idrac-{index:02d}", f"DELLSN{index:02d}", f"168.0.0.{index}", "Dell", "PowerEdge R750", "Red Hat Enterprise Linux 8.0")
            for index in range(1, 11)
        ]
        connection.executemany(
            "INSERT INTO idrac_nodes VALUES (?, ?, ?, ?, ?, ?)", nodes
        )
        interfaces = [
            (node_id, "NIC.Embedded.1-1", f"00:25:90:10:00:{index:02x}", 20_000)
            for index, (node_id, *_) in enumerate(nodes, 1)
        ]
        connection.executemany(
            "INSERT INTO idrac_network_interfaces (idrac_node_id, name, mac_address, speed_mbps) VALUES (?, ?, ?, ?)",
            interfaces,
        )
        storage = [
            (node_id, f"Disk.Bay.{disk}", "Mock SAS SSD", 960, "ssd", f"{sn}storage{disk:02d}")
            for node_id, sn, *_ in nodes
            for disk in range(1, 11)
        ]
        connection.executemany(
            "INSERT INTO idrac_storage_devices (idrac_node_id, device_name, model, capacity_gib, storage_type, serial_number) VALUES (?, ?, ?, ?, ?, ?)",
            storage,
        )

    def list_clusters(self) -> list[ClusterSummary]:
        self.initialize()
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT cluster_id, cluster_name, cluster_ip, cluster_port FROM clusters ORDER BY cluster_id"
            ).fetchall()
        return [ClusterSummary.model_validate(dict(row)) for row in rows]

    def list_nodes(self, cluster_id: str) -> list[Node]:
        self.initialize()
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT * FROM nodes WHERE cluster_id = ? AND status = 'added' ORDER BY name", (cluster_id,)
            ).fetchall()
        return [self._node_from_row(connection, row) for row in rows]

    @staticmethod
    def _failure(operation: str, cluster_id: str, node_name: str, error_code: str, message: str) -> NodeOperationResult:
        return NodeOperationResult(success=False, operation=operation, cluster_id=cluster_id, node_name=node_name, error_code=error_code, message=message)

    def _transition_node(self, operation: str, cluster_id: str, node_name: str, expected: NodeStatus, target: NodeStatus) -> NodeOperationResult:
        self.initialize()
        with self._connect() as connection:
            row = connection.execute("SELECT status FROM nodes WHERE cluster_id = ? AND name = ?", (cluster_id, node_name)).fetchone()
            if row is None:
                return self._failure(operation, cluster_id, node_name, "NODE_NOT_FOUND", "No matching mock node exists.")
            if row["status"] != expected.value:
                return self._failure(operation, cluster_id, node_name, "INVALID_STATE", f"Node must be {expected.value} before {operation}.")
            connection.execute("UPDATE nodes SET status = ? WHERE cluster_id = ? AND name = ?", (target.value, cluster_id, node_name))
        return NodeOperationResult(success=True, operation=operation, cluster_id=cluster_id, node_name=node_name, status=target, message=f"Node {node_name} is {target.value}.")

    def cordon_node(self, cluster_id: str, node_name: str) -> NodeOperationResult:
        return self._transition_node("node.cordon", cluster_id, node_name, NodeStatus.ADDED, NodeStatus.CORDONED)

    def drain_node(self, cluster_id: str, node_name: str) -> NodeOperationResult:
        return self._transition_node("node.drain", cluster_id, node_name, NodeStatus.CORDONED, NodeStatus.DRAINED)

    def delete_node(self, cluster_id: str, node_name: str) -> NodeOperationResult:
        self.initialize()
        with self._connect() as connection:
            row = connection.execute("SELECT node_id, status FROM nodes WHERE cluster_id = ? AND name = ?", (cluster_id, node_name)).fetchone()
            if row is None:
                return self._failure("node.delete", cluster_id, node_name, "NODE_NOT_FOUND", "No matching mock node exists.")
            if row["status"] != NodeStatus.DRAINED.value:
                return self._failure("node.delete", cluster_id, node_name, "INVALID_STATE", "Node must be drained before node.delete.")
            connection.execute("DELETE FROM nodes WHERE node_id = ?", (row["node_id"],))
        return NodeOperationResult(success=True, operation="node.delete", cluster_id=cluster_id, node_name=node_name, message=f"Node {node_name} was deleted.")

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

    def list_idrac_nodes(self, sn: list[str] | None = None) -> list[IdracNode]:
        self.initialize()
        with self._connect() as connection:
            if not sn:
                rows = connection.execute("SELECT * FROM idrac_nodes ORDER BY sn").fetchall()
                return [self._idrac_node_from_row(connection, row) for row in rows]

            requested_sns = list(dict.fromkeys(sn))
            placeholders = ", ".join("?" for _ in requested_sns)
            rows = connection.execute(
                f"SELECT * FROM idrac_nodes WHERE sn IN ({placeholders})", requested_sns
            ).fetchall()
            rows_by_sn = {row["sn"]: row for row in rows}
            return [
                self._idrac_node_from_row(connection, rows_by_sn[serial_number])
                for serial_number in requested_sns
                if serial_number in rows_by_sn
            ]

    def get_idrac_node(self, *, sn: str | None = None, idrac_ip: str | None = None) -> IdracNode | None:
        if (sn is None) == (idrac_ip is None):
            raise ValueError("Provide exactly one of sn or idrac_ip.")
        self.initialize()
        column, value = ("sn", sn) if sn is not None else ("idrac_ip", idrac_ip)
        with self._connect() as connection:
            row = connection.execute(
                f"SELECT * FROM idrac_nodes WHERE {column} = ?", (value,)
            ).fetchone()
            return self._idrac_node_from_row(connection, row) if row is not None else None

    @staticmethod
    def _idrac_node_from_row(connection: sqlite3.Connection, row: sqlite3.Row) -> IdracNode:
        interfaces = [dict(item) for item in connection.execute(
            "SELECT name, mac_address, speed_mbps FROM idrac_network_interfaces WHERE idrac_node_id = ? ORDER BY interface_id",
            (row["idrac_node_id"],),
        )]
        storage = [dict(item) for item in connection.execute(
            "SELECT device_name, model, capacity_gib, storage_type, serial_number FROM idrac_storage_devices WHERE idrac_node_id = ? ORDER BY storage_id",
            (row["idrac_node_id"],),
        )]
        return IdracNode.model_validate({
            "sn": row["sn"],
            "idrac_ip": row["idrac_ip"],
            "system_information": {
                "manufacturer": row["manufacturer"],
                "model": row["model"],
                "operating_system": row["operating_system"],
            },
            "network_interfaces": interfaces,
            "storage_devices": storage,
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
