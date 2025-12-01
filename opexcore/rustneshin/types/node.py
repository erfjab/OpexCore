from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field


class RustneshinNodeStatus(str, Enum):
    """Node status enumeration"""

    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DISABLED = "disabled"


class RustneshinNodeConnectionBackend(str, Enum):
    """Node connection backend"""

    GRPCIO = "grpcio"
    GRPCLIB = "grpclib"


class RustneshinBackendConfigFormat(str, Enum):
    """Backend config format"""

    PLAIN = "Plain"
    JSON = "Json"
    YAML = "Yaml"


class RustneshinBackend(BaseModel):
    """Backend model"""

    name: str = Field(..., title="Name")
    backend_type: str = Field(..., title="Backend Type")
    running: bool = Field(..., title="Running")
    version: Optional[str] = Field(None, title="Version")


class RustneshinBackendConfig(BaseModel):
    """Backend config model"""

    config: str = Field(..., title="Config")
    format: RustneshinBackendConfigFormat = Field(..., title="Format")


class RustneshinNodeCreate(BaseModel):
    """Schema for creating a new node"""

    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient")
    connection_backend: Optional[RustneshinNodeConnectionBackend] = Field(
        None, title="Connection Backend"
    )


class RustneshinNodeModify(BaseModel):
    """Schema for modifying an existing node"""

    name: Optional[str] = Field(None, title="Name")
    address: Optional[str] = Field(None, title="Address")
    port: Optional[int] = Field(None, title="Port")
    usage_coefficient: Optional[float] = Field(None, title="Usage Coefficient")
    connection_backend: Optional[RustneshinNodeConnectionBackend] = Field(
        None, title="Connection Backend"
    )


class RustneshinNodeResponse(BaseModel):
    """Node response schema"""

    id: Optional[int] = Field(None, title="ID")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient")
    connection_backend: Optional[RustneshinNodeConnectionBackend] = Field(
        None, title="Connection Backend"
    )
    status: RustneshinNodeStatus = Field(..., title="Status")
    backends: List[RustneshinBackend] = Field(default_factory=list, title="Backends")
    xray_version: Optional[str] = Field(None, title="Xray Version")
    message: Optional[str] = Field(None, title="Message")
    inbound_ids: Optional[List[int]] = Field(None, title="Inbound IDs")


class RustneshinNodeSettings(BaseModel):
    """Node settings schema"""

    certificate: str = Field(..., title="Certificate")
    min_node_version: str = Field("", title="Min Node Version")


class RustneshinPageNodeResponse(BaseModel):
    """Paginated node response"""

    items: List[RustneshinNodeResponse] = Field(default_factory=list, title="Items")
    total: int = Field(..., title="Total")
    page: int = Field(..., title="Page")
    size: int = Field(..., title="Size")
    pages: int = Field(..., title="Pages")
