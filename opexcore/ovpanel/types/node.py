from typing import Optional
from pydantic import BaseModel, Field


class OVPanelNodeCreate(BaseModel):
    """Schema for creating a new node"""

    name: str = Field(..., max_length=10, title="Name")
    address: str = Field(..., title="Address")
    tunnel_address: Optional[str] = Field(None, title="Tunnel Address")
    protocol: str = Field("tcp", title="Protocol")
    ovpn_port: int = Field(1194, title="OVPN Port")
    port: int = Field(..., title="Port")
    key: str = Field(..., min_length=10, max_length=40, title="Key")
    status: bool = Field(True, title="Status")
    set_new_setting: bool = Field(False, title="Set New Setting")


class OVPanelNodeStatus(BaseModel):
    """Node status response schema"""

    success: bool = Field(..., title="Success")
    msg: str = Field(..., title="Message")
    data: Optional[dict] = Field(None, title="Data")


class OVPanelNode(BaseModel):
    """Node response schema"""

    id: int = Field(..., title="ID")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    tunnel_address: Optional[str] = Field(None, title="Tunnel Address")
    protocol: str = Field(..., title="Protocol")
    ovpn_port: int = Field(..., title="OVPN Port")
    port: int = Field(..., title="Port")
    key: str = Field(..., title="Key")
    status: bool = Field(..., title="Status")
