from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field


class MarzbanNodeStatus(str, Enum):
    """Node status enumeration"""

    CONNECTED = "connected"
    CONNECTING = "connecting"
    ERROR = "error"
    DISABLED = "disabled"


class MarzbanNodeCreate(BaseModel):
    """Schema for creating a new node"""

    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    api_port: int = Field(62051, title="Api Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient", gt=0.0)
    add_as_new_host: bool = Field(True, title="Add As New Host")


class MarzbanNodeModify(BaseModel):
    """Schema for modifying an existing node"""

    name: Optional[str] = Field(None, title="Name")
    address: Optional[str] = Field(None, title="Address")
    port: Optional[int] = Field(None, title="Port")
    api_port: Optional[int] = Field(None, title="Api Port")
    usage_coefficient: Optional[float] = Field(None, title="Usage Coefficient")
    status: Optional[MarzbanNodeStatus] = Field(None, title="Status")


class MarzbanNodeResponse(BaseModel):
    """Node response schema"""

    id: int = Field(..., title="Id")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    api_port: int = Field(62051, title="Api Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient", gt=0.0)
    xray_version: Optional[str] = Field(None, title="Xray Version")
    status: MarzbanNodeStatus = Field(..., title="Status")
    message: Optional[str] = Field(None, title="Message")


class MarzbanNodeSettings(BaseModel):
    """Node settings schema"""

    min_node_version: str = Field("v0.2.0", title="Min Node Version")
    certificate: str = Field(..., title="Certificate")


class MarzbanNodeUsageResponse(BaseModel):
    """Node usage response schema"""

    node_id: Optional[int] = Field(None, title="Node Id")
    node_name: str = Field(..., title="Node Name")
    uplink: int = Field(..., title="Uplink")
    downlink: int = Field(..., title="Downlink")


class MarzbanNodesUsageResponse(BaseModel):
    """Multiple nodes usage response schema"""

    usages: List[MarzbanNodeUsageResponse] = Field(..., title="Usages")
