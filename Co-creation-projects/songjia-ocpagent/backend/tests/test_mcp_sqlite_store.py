import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.mcp import cluster_tools
from app.mcp.cluster_store import MockClusterStore
from app.models.node import NodeStatus


class SQLiteMockClusterStoreTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.store = MockClusterStore(Path(self.tempdir.name) / "ocp_mock.sqlite3")

    def tearDown(self):
        self.tempdir.cleanup()

    def test_initialization_is_idempotent_and_seeds_two_clusters(self):
        self.store.initialize()
        self.store.initialize()
        self.assertEqual([cluster.cluster_id for cluster in self.store.list_clusters()], ["cluster-001", "cluster-002"])
        with self.store._connect() as connection:
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM clusters").fetchone()[0], 2)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0], 11)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM idrac_nodes").fetchone()[0], 10)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM idrac_network_interfaces").fetchone()[0], 10)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM idrac_storage_devices").fetchone()[0], 100)

    def test_idrac_inventory_has_prescribed_complete_mock_data(self):
        inventory = self.store.list_idrac_nodes()

        self.assertEqual([node.sn for node in inventory], [f"DELLSN{index:02d}" for index in range(1, 11)])
        self.assertEqual([node.idrac_ip for node in inventory], [f"168.0.0.{index}" for index in range(1, 11)])
        first = inventory[0]
        self.assertEqual(first.system_information.operating_system, "Red Hat Enterprise Linux 8.0")
        self.assertEqual(first.network_interfaces[0].speed_mbps, 20_000)
        self.assertEqual(len(first.storage_devices), 10)
        self.assertEqual(
            [device.serial_number for device in first.storage_devices],
            [f"DELLSN01storage{index:02d}" for index in range(1, 11)],
        )

    def test_idrac_inventory_can_be_selected_by_ordered_serial_number_array(self):
        self.assertEqual(len(self.store.list_idrac_nodes()), 10)
        self.assertEqual(len(self.store.list_idrac_nodes([])), 10)
        selected = self.store.list_idrac_nodes(["DELLSN02", "DELLSN01", "DELLSN02", "UNKNOWN"])

        self.assertEqual([node.sn for node in selected], ["DELLSN02", "DELLSN01"])

    def test_get_idrac_node_uses_either_supported_selector(self):
        by_sn = self.store.get_idrac_node(sn="DELLSN01")
        by_ip = self.store.get_idrac_node(idrac_ip="168.0.0.10")

        self.assertEqual(by_sn.idrac_ip, "168.0.0.1")
        self.assertEqual(by_ip.sn, "DELLSN10")
        self.assertIsNone(self.store.get_idrac_node(sn="UNKNOWN"))
        with self.assertRaisesRegex(ValueError, "exactly one"):
            self.store.get_idrac_node()
        with self.assertRaisesRegex(ValueError, "exactly one"):
            self.store.get_idrac_node(sn="DELLSN01", idrac_ip="168.0.0.1")

    def test_cluster_nodes_include_typed_hardware_inventory(self):
        node = self.store.list_nodes("cluster-001")[0]
        self.assertEqual(node.status, NodeStatus.ADDED)
        self.assertEqual(node.cluster_id, "cluster-001")
        self.assertEqual(node.idrac_ip, "192.168.1.101")
        self.assertTrue(node.network_interfaces[0].is_primary)
        self.assertEqual(node.storage_devices[0].storage_type, "nvme")

    def test_status_cluster_constraints_and_standalone_nodes(self):
        self.store.initialize()
        with self.store._connect() as connection:
            statuses = dict(connection.execute(
                "SELECT status, COUNT(*) FROM nodes WHERE cluster_id IS NULL GROUP BY status"
            ).fetchall())
            self.assertEqual(statuses, {"new": 3})
            cluster_counts = dict(connection.execute(
                "SELECT cluster_id, COUNT(*) FROM nodes WHERE status = 'added' GROUP BY cluster_id"
            ).fetchall())
            self.assertEqual(cluster_counts, {"cluster-001": 4, "cluster-002": 4})
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute("UPDATE nodes SET cluster_id = NULL WHERE name = 'cluster-001-worker-001'")
            self.assertEqual(self.store.list_nodes("unknown-cluster"), [])

    def test_reset_restores_all_fixture_rows_after_node_mutation(self):
        self.store.initialize()
        self.assertTrue(self.store.cordon_node("cluster-001", "cluster-001-worker-001").success)
        self.assertTrue(self.store.drain_node("cluster-001", "cluster-001-worker-001").success)
        self.assertTrue(self.store.delete_node("cluster-001", "cluster-001-worker-001").success)

        self.store.reset()

        with self.store._connect() as connection:
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM clusters").fetchone()[0], 2)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0], 11)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM nodes WHERE status = 'added'").fetchone()[0], 8)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM nodes WHERE status = 'new' AND cluster_id IS NULL").fetchone()[0], 3)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM idrac_nodes").fetchone()[0], 10)
        self.assertEqual(self.store.list_nodes("cluster-001")[0].status, NodeStatus.ADDED)

    def test_cluster_relationships_keep_pods_isolated(self):
        cluster_one_pods = self.store.list_pods("cluster-001")
        cluster_two_pods = self.store.list_pods("cluster-002")
        self.assertEqual(len(cluster_one_pods), 2)
        self.assertEqual(len(cluster_two_pods), 2)
        self.assertTrue(all(pod.pod_name.startswith("cluster-001") for pod in cluster_one_pods))
        self.assertTrue(all(pod.pod_name.startswith("cluster-002") for pod in cluster_two_pods))

    def test_node_delete_lifecycle_requires_cordon_then_drain_then_delete(self):
        cluster_id, node_name = "cluster-001", "cluster-001-worker-001"
        self.assertEqual(self.store.drain_node(cluster_id, node_name).error_code, "INVALID_STATE")
        self.assertEqual(self.store.cordon_node(cluster_id, node_name).status, NodeStatus.CORDONED)
        self.assertEqual(self.store.drain_node(cluster_id, node_name).status, NodeStatus.DRAINED)
        with self.store._connect() as connection:
            node_id = connection.execute("SELECT node_id FROM nodes WHERE name = ?", (node_name,)).fetchone()[0]
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM node_network_interfaces WHERE node_id = ?", (node_id,)).fetchone()[0], 1)
        self.assertTrue(self.store.delete_node(cluster_id, node_name).success)
        with self.store._connect() as connection:
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM nodes WHERE name = ?", (node_name,)).fetchone()[0], 0)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM node_network_interfaces WHERE node_id = ?", (node_id,)).fetchone()[0], 0)
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM node_storage_devices WHERE node_id = ?", (node_id,)).fetchone()[0], 0)

    def test_node_delete_operations_reject_unknown_or_mismatched_node(self):
        self.assertEqual(self.store.cordon_node("cluster-002", "cluster-001-worker-001").error_code, "NODE_NOT_FOUND")
        self.assertEqual(self.store.delete_node("cluster-001", "unknown").error_code, "NODE_NOT_FOUND")

    def test_legacy_nodes_status_constraint_is_migrated_without_losing_node(self):
        with self.store._connect() as connection:
            connection.executescript("""
                CREATE TABLE clusters (cluster_id TEXT PRIMARY KEY, cluster_name TEXT NOT NULL, cluster_ip TEXT NOT NULL, cluster_port INTEGER NOT NULL);
                INSERT INTO clusters VALUES ('legacy-cluster', 'Legacy', '127.0.0.1', 6443);
                CREATE TABLE nodes (
                    node_id TEXT PRIMARY KEY, cluster_id TEXT REFERENCES clusters(cluster_id), name TEXT NOT NULL UNIQUE,
                    status TEXT NOT NULL CHECK (status IN ('new', 'added', 'reimage', 'removed')),
                    idrac_ip TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, domain TEXT NOT NULL,
                    network_port INTEGER NOT NULL, network_ip TEXT NOT NULL, network_netmask TEXT NOT NULL, network_gateway TEXT NOT NULL,
                    image_name TEXT NOT NULL, image_path TEXT NOT NULL, firmware_name TEXT NOT NULL, firmware_path TEXT NOT NULL,
                    certificate_file_name TEXT NOT NULL, certificate_file_path TEXT NOT NULL,
                    CHECK ((status = 'added' AND cluster_id IS NOT NULL) OR (status != 'added' AND cluster_id IS NULL))
                );
                INSERT INTO nodes VALUES ('legacy-node', 'legacy-cluster', 'legacy-worker', 'added', '127.0.0.2', 'admin', 'secret', 'local', 1, '127.0.0.2', '255.255.255.0', '127.0.0.1', 'image', 'path', 'firmware', 'path', 'cert', 'path');
            """)
        self.store.initialize()
        self.assertEqual(self.store.cordon_node("legacy-cluster", "legacy-worker").status, NodeStatus.CORDONED)


class SQLiteBackedMCPToolTests(unittest.TestCase):
    def test_tools_use_sqlite_store(self):
        with tempfile.TemporaryDirectory() as directory:
            store = MockClusterStore(Path(directory) / "ocp_mock.sqlite3")
            with patch.object(cluster_tools, "store", store):
                self.assertEqual(len(cluster_tools.list_clusters()), 2)
                self.assertEqual(cluster_tools.list_nodes("cluster-002")[0].cluster_id, "cluster-002")
                self.assertEqual(len(cluster_tools.list_pods("cluster-002")), 2)
                self.assertEqual(len(cluster_tools.list_idrac_nodes()), 10)
                self.assertEqual(len(cluster_tools.list_idrac_nodes([])), 10)
                self.assertEqual(
                    [node.sn for node in cluster_tools.list_idrac_nodes(["DELLSN02", "DELLSN01", "DELLSN02", "UNKNOWN"])],
                    ["DELLSN02", "DELLSN01"],
                )
                self.assertEqual(cluster_tools.get_idrac_node(sn="DELLSN01").idrac_ip, "168.0.0.1")
                self.assertEqual(cluster_tools.get_idrac_node(idrac_ip="168.0.0.10").sn, "DELLSN10")
                self.assertIsNone(cluster_tools.get_idrac_node(sn="UNKNOWN"))
                with self.assertRaisesRegex(ValueError, "exactly one"):
                    cluster_tools.get_idrac_node()
                with self.assertRaisesRegex(ValueError, "exactly one"):
                    cluster_tools.get_idrac_node(sn="DELLSN01", idrac_ip="168.0.0.1")
                self.assertEqual(cluster_tools.health(), "OK")

    def test_node_delete_tools_delegate_to_sqlite_store(self):
        with tempfile.TemporaryDirectory() as directory:
            store = MockClusterStore(Path(directory) / "ocp_mock.sqlite3")
            with patch.object(cluster_tools, "store", store):
                self.assertEqual(cluster_tools.cordon_node("cluster-001", "cluster-001-worker-001").status, NodeStatus.CORDONED)
                self.assertEqual(cluster_tools.drain_node("cluster-001", "cluster-001-worker-001").status, NodeStatus.DRAINED)
                self.assertTrue(cluster_tools.delete_node("cluster-001", "cluster-001-worker-001").success)
