from typing import Optional
from pydantic import BaseModel, Field


class RemnawaveNode(BaseModel):
    """Node response"""

    uuid: str
    name: str
    address: str
    port: int
    is_connected: bool = Field(..., alias="isConnected")
    is_disabled: bool = Field(..., alias="isDisabled")
    is_node_online: bool = Field(..., alias="isNodeOnline")
    is_xray_running: bool = Field(..., alias="isXrayRunning")
    xray_version: Optional[str] = Field(None, alias="xrayVersion")
    node_version: Optional[str] = Field(None, alias="nodeVersion")
    users_online: Optional[int] = Field(None, alias="usersOnline")
    country_code: str = Field(..., alias="countryCode")
    consumption_multiplier: float = Field(..., alias="consumptionMultiplier")
    traffic_limit_bytes: Optional[int] = Field(None, alias="trafficLimitBytes")
    traffic_used_bytes: Optional[int] = Field(None, alias="trafficUsedBytes")
    created_at: str = Field(..., alias="createdAt")
    updated_at: str = Field(..., alias="updatedAt")

    class Config:
        populate_by_name = True


class RemnawaveNodeCreate(BaseModel):
    """Node creation data"""

    name: str = Field(..., min_length=3, max_length=30)
    address: str = Field(..., min_length=2)
    port: int = Field(..., ge=1, le=65535)
    country_code: str = Field("XX", alias="countryCode", max_length=2)
    consumption_multiplier: float = Field(1.0, alias="consumptionMultiplier", ge=0.1)
    traffic_limit_bytes: int = Field(0, alias="trafficLimitBytes", ge=0)
    is_traffic_tracking_active: bool = Field(False, alias="isTrafficTrackingActive")

    class Config:
        populate_by_name = True


class RemnawaveNodeUpdate(BaseModel):
    """Node update data"""

    name: Optional[str] = Field(None, min_length=3, max_length=30)
    address: Optional[str] = Field(None, min_length=2)
    port: Optional[int] = Field(None, ge=1, le=65535)
    country_code: Optional[str] = Field(None, alias="countryCode", max_length=2)
    consumption_multiplier: Optional[float] = Field(
        None, alias="consumptionMultiplier", ge=0.1
    )
    traffic_limit_bytes: Optional[int] = Field(None, alias="trafficLimitBytes", ge=0)
    is_traffic_tracking_active: Optional[bool] = Field(
        None, alias="isTrafficTrackingActive"
    )

    class Config:
        populate_by_name = True
