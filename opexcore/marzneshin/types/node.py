from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field


class MarzneshinNodeStatus(str, Enum):
    """Node status enumeration"""

    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DISABLED = "disabled"


class MarzneshinNodeConnectionBackend(str, Enum):
    """Node connection backend enumeration"""

    GRPCIO = "grpcio"
    GRPCLIB = "grpclib"


class MarzneshinNodeCreate(BaseModel):
    """Schema for creating a new node"""

    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(53042, title="Port")
    connection_backend: MarzneshinNodeConnectionBackend = Field(
        MarzneshinNodeConnectionBackend.GRPCLIB, title="Connection Backend"
    )
    usage_coefficient: float = Field(1.0, ge=0.0, title="Usage Coefficient")


class MarzneshinNodeModify(BaseModel):
    """Schema for modifying an existing node"""

    name: Optional[str] = Field(None, title="Name")
    address: Optional[str] = Field(None, title="Address")
    port: Optional[int] = Field(None, title="Port")
    connection_backend: Optional[MarzneshinNodeConnectionBackend] = Field(
        None, title="Connection Backend"
    )
    usage_coefficient: Optional[float] = Field(None, ge=0.0, title="Usage Coefficient")
    status: Optional[MarzneshinNodeStatus] = Field(None, title="Status")


class MarzneshinBackend(BaseModel):
    """Backend information"""

    name: str = Field(..., title="Name")
    backend_type: str = Field(..., title="Backend Type")
    version: Optional[str] = Field(None, title="Version")
    running: bool = Field(..., title="Running")


class MarzneshinNodeResponse(BaseModel):
    """Node response schema"""

    id: int = Field(..., title="Id")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(53042, title="Port")
    connection_backend: MarzneshinNodeConnectionBackend = Field(
        MarzneshinNodeConnectionBackend.GRPCLIB, title="Connection Backend"
    )
    usage_coefficient: float = Field(1.0, ge=0.0, title="Usage Coefficient")
    xray_version: Optional[str] = Field(None, title="Xray Version")
    status: MarzneshinNodeStatus = Field(..., title="Status")
    message: Optional[str] = Field(None, title="Message")
    inbound_ids: Optional[List[int]] = Field(None, title="Inbound Ids")
    backends: List[MarzneshinBackend] = Field(..., title="Backends")


class MarzneshinNodeSettings(BaseModel):
    """Node settings response"""

    min_node_version: str = Field("v0.2.0", title="Min Node Version")
    certificate: str = Field(..., title="Certificate")
