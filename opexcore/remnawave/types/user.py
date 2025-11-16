from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field


class RemnawaveUserStatus(str, Enum):
    """User status enumeration"""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    LIMITED = "LIMITED"
    EXPIRED = "EXPIRED"


class RemnawaveTrafficLimitStrategy(str, Enum):
    """Traffic limit reset strategy"""

    NO_RESET = "NO_RESET"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"


class RemnawaveUser(BaseModel):
    """User response"""

    uuid: str
    short_uuid: str = Field(..., alias="shortUuid")
    username: str
    status: RemnawaveUserStatus
    used_traffic_bytes: int = Field(..., alias="usedTrafficBytes")
    lifetime_used_traffic_bytes: int = Field(..., alias="lifetimeUsedTrafficBytes")
    traffic_limit_bytes: int = Field(..., alias="trafficLimitBytes")
    traffic_limit_strategy: RemnawaveTrafficLimitStrategy = Field(
        ..., alias="trafficLimitStrategy"
    )
    expire_at: str = Field(..., alias="expireAt")
    online_at: Optional[str] = Field(None, alias="onlineAt")
    sub_revoked_at: Optional[str] = Field(None, alias="subRevokedAt")
    trojan_password: str = Field(..., alias="trojanPassword")
    vless_uuid: str = Field(..., alias="vlessUuid")
    ss_password: str = Field(..., alias="ssPassword")
    description: Optional[str] = None
    tag: Optional[str] = None
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    email: Optional[str] = None
    hwid_device_limit: Optional[int] = Field(None, alias="hwidDeviceLimit")
    created_at: str = Field(..., alias="createdAt")
    updated_at: str = Field(..., alias="updatedAt")
    subscription_url: str = Field(..., alias="subscriptionUrl")

    class Config:
        populate_by_name = True
        use_enum_values = True


class RemnawaveUserCreate(BaseModel):
    """User creation data"""

    username: str = Field(..., min_length=3, max_length=32)
    traffic_limit_bytes: int = Field(0, alias="trafficLimitBytes")
    traffic_limit_strategy: RemnawaveTrafficLimitStrategy = Field(
        RemnawaveTrafficLimitStrategy.NO_RESET, alias="trafficLimitStrategy"
    )
    expire_at: str = Field(..., alias="expireAt")
    description: Optional[str] = None
    tag: Optional[str] = None
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    email: Optional[str] = None
    hwid_device_limit: Optional[int] = Field(None, alias="hwidDeviceLimit")

    class Config:
        populate_by_name = True
        use_enum_values = True


class RemnawaveUserUpdate(BaseModel):
    """User update data"""

    traffic_limit_bytes: Optional[int] = Field(None, alias="trafficLimitBytes")
    traffic_limit_strategy: Optional[RemnawaveTrafficLimitStrategy] = Field(
        None, alias="trafficLimitStrategy"
    )
    expire_at: Optional[str] = Field(None, alias="expireAt")
    description: Optional[str] = None
    tag: Optional[str] = None
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    email: Optional[str] = None
    hwid_device_limit: Optional[int] = Field(None, alias="hwidDeviceLimit")

    class Config:
        populate_by_name = True
        use_enum_values = True
