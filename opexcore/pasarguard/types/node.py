from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class PasarGuardNodeStatus(str, Enum):
    """Node status enumeration"""

    connected = "connected"
    connecting = "connecting"
    error = "error"
    disabled = "disabled"
    limited = "limited"


class PasarGuardNodeConnectionType(str, Enum):
    """Node connection type"""

    grpc = "grpc"
    rest = "rest"


class PasarGuardDataLimitResetStrategy(str, Enum):
    """Data limit reset strategy"""

    no_reset = "no_reset"
    day = "day"
    week = "week"
    month = "month"
    year = "year"


class PasarGuardNodeCreate(BaseModel):
    """Schema for creating a new node"""

    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient")
    connection_type: PasarGuardNodeConnectionType = Field(..., title="Connection Type")
    server_ca: str = Field(..., title="Server Ca")
    keep_alive: int = Field(..., title="Keep Alive")
    core_config_id: int = Field(..., title="Core Config Id")
    api_key: str = Field(..., title="Api Key")
    data_limit: int = Field(0, title="Data Limit")
    data_limit_reset_strategy: PasarGuardDataLimitResetStrategy = Field(
        PasarGuardDataLimitResetStrategy.no_reset, title="Data Limit Reset Strategy"
    )
    reset_time: int = Field(-1, title="Reset Time")


class PasarGuardNodeModify(BaseModel):
    """Schema for modifying an existing node"""

    name: Optional[str] = Field(None, title="Name")
    address: Optional[str] = Field(None, title="Address")
    port: Optional[int] = Field(None, title="Port")
    usage_coefficient: Optional[float] = Field(None, title="Usage Coefficient")
    connection_type: Optional[PasarGuardNodeConnectionType] = Field(
        None, title="Connection Type"
    )
    server_ca: Optional[str] = Field(None, title="Server Ca")
    keep_alive: Optional[int] = Field(None, title="Keep Alive")
    core_config_id: Optional[int] = Field(None, title="Core Config Id")
    api_key: Optional[str] = Field(None, title="Api Key")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[PasarGuardDataLimitResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    reset_time: Optional[int] = Field(None, title="Reset Time")
    status: Optional[PasarGuardNodeStatus] = Field(None, title="Status")


class PasarGuardNodeResponse(BaseModel):
    """Node response schema"""

    id: int = Field(..., title="Id")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient")
    connection_type: PasarGuardNodeConnectionType = Field(..., title="Connection Type")
    server_ca: str = Field(..., title="Server Ca")
    keep_alive: int = Field(..., title="Keep Alive")
    core_config_id: Optional[int] = Field(None, title="Core Config Id")
    api_key: Optional[str] = Field(None, title="Api Key")
    data_limit: int = Field(0, title="Data Limit")
    data_limit_reset_strategy: PasarGuardDataLimitResetStrategy = Field(
        PasarGuardDataLimitResetStrategy.no_reset, title="Data Limit Reset Strategy"
    )
    reset_time: int = Field(-1, title="Reset Time")
    xray_version: Optional[str] = Field(None, title="Xray Version")
    node_version: Optional[str] = Field(None, title="Node Version")
    status: PasarGuardNodeStatus = Field(..., title="Status")
    message: Optional[str] = Field(None, title="Message")
    uplink: int = Field(0, title="Uplink")
    downlink: int = Field(0, title="Downlink")
    lifetime_uplink: Optional[int] = Field(None, title="Lifetime Uplink")
    lifetime_downlink: Optional[int] = Field(None, title="Lifetime Downlink")


class PasarGuardNodeSettings(BaseModel):
    """Node settings response schema"""

    min_node_version: str = Field("v1.0.0", title="Min Node Version")
