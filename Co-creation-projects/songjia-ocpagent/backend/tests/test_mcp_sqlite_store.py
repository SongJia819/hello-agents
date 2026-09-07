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
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0], 5)
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
            self.assertEqual(statuses, {"new": 1, "reimage": 1, "removed": 1})
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute("UPDATE nodes SET cluster_id = NULL WHERE node_id = 'node-001'")
        self.assertEqual(self.store.list_nodes("unknown-cluster"), [])

    def test_cluster_relationships_keep_pods_isolated(self):
        cluster_one_pods = self.store.list_pods("cluster-001")
        cluster_two_pods = self.store.list_pods("cluster-002")
        self.assertEqual(len(cluster_one_pods), 2)
        self.assertEqual(len(cluster_two_pods), 2)
        self.assertTrue(all(pod.pod_name.startswith("cluster-001") for pod in cluster_one_pods))
        self.assertTrue(all(pod.pod_name.startswith("cluster-002") for pod in cluster_two_pods))


class SQLiteBackedMCPToolTests(unittest.TestCase):
    def test_tools_use_sqlite_store(self):
        with tempfile.TemporaryDirectory() as directory:
            store = MockClusterStore(Path(directory) / "ocp_mock.sqlite3")
            with patch.object(cluster_tools, "store", store):
                self.assertEqual(len(cluster_tools.list_clusters()), 2)
                self.assertEqual(cluster_tools.list_nodes("cluster-002")[0].cluster_id, "cluster-002")
                self.assertEqual(len(cluster_tools.list_pods("cluster-002")), 2)
                self.assertEqual(len(cluster_tools.list_idrac_nodes()), 10)
                self.assertEqual(cluster_tools.get_idrac_node(sn="DELLSN01").idrac_ip, "168.0.0.1")
                self.assertEqual(cluster_tools.get_idrac_node(idrac_ip="168.0.0.10").sn, "DELLSN10")
                self.assertIsNone(cluster_tools.get_idrac_node(sn="UNKNOWN"))
                with self.assertRaisesRegex(ValueError, "exactly one"):
                    cluster_tools.get_idrac_node()
                with self.assertRaisesRegex(ValueError, "exactly one"):
                    cluster_tools.get_idrac_node(sn="DELLSN01", idrac_ip="168.0.0.1")
                self.assertEqual(cluster_tools.health(), "OK")
