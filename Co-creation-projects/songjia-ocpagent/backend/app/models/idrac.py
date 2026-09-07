"""Typed mock iDRAC inventory responses."""

from pydantic import BaseModel, Field


class IdracSystemInformation(BaseModel):
    manufacturer: str
    model: str
    operating_system: str


class IdracNetworkInterface(BaseModel):
    name: str
    mac_address: str
    speed_mbps: int


class IdracStorageDevice(BaseModel):
    device_name: str
    model: str
    capacity_gib: int
    storage_type: str
    serial_number: str


class IdracNode(BaseModel):
    sn: str
    idrac_ip: str
    system_information: IdracSystemInformation
    network_interfaces: list[IdracNetworkInterface] = Field(default_factory=list)
    storage_devices: list[IdracStorageDevice] = Field(default_factory=list)
