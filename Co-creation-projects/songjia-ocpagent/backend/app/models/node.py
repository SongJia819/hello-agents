from pydantic import BaseModel


class Node(BaseModel):
    name: str
    network: Network
    username: str
    password: str
    domain: str
    image: Image
    firmware: Firmware
    certificate: Certificate

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
