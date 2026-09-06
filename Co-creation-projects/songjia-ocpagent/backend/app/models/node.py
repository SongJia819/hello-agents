from enum import Enum

from pydantic import BaseModel, Field


class NodeStatus(str, Enum):
    NEW = "new"
    ADDED = "added"
    REIMAGE = "reimage"
    REMOVED = "removed"


class Network(BaseModel):
    port: int
    ip: str
    netmask: str
    gateway: str

class Image(BaseModel):
    image_name: str
    image_path: str

class Firmware(BaseModel):
    firmware_name: str
    firmware_path: str

class Certificate(BaseModel):
    certificate_file_name: str
    certificate_file_path: str


class NetworkInterface(BaseModel):
    name: str
    mac_address: str
    ip: str
    netmask: str
    gateway: str
    speed_mbps: int
    is_primary: bool = False


class StorageDevice(BaseModel):
    device_name: str
    model: str
    capacity_gib: int
    storage_type: str
    serial_number: str


class Node(BaseModel):
    name: str
    network: Network
    username: str
    password: str
    domain: str
    image: Image
    firmware: Firmware
    certificate: Certificate
    cluster_id: str | None = None
    status: NodeStatus = NodeStatus.NEW
    idrac_ip: str | None = None
    network_interfaces: list[NetworkInterface] = Field(default_factory=list)
    storage_devices: list[StorageDevice] = Field(default_factory=list)
