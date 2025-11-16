from typing import Optional, Dict, List, Any
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class MarzbanUserStatus(str, Enum):
    """User status enumeration"""

    ACTIVE = "active"
    DISABLED = "disabled"
    LIMITED = "limited"
    EXPIRED = "expired"
    ON_HOLD = "on_hold"


class MarzbanUserStatusCreate(str, Enum):
    """User status for creation"""

    ACTIVE = "active"
    ON_HOLD = "on_hold"


class MarzbanUserStatusModify(str, Enum):
    """User status for modification"""

    ACTIVE = "active"
    DISABLED = "disabled"
    ON_HOLD = "on_hold"


class MarzbanUserDataLimitResetStrategy(str, Enum):
    """Data limit reset strategy"""

    NO_RESET = "no_reset"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class MarzbanProxyTypes(str, Enum):
    """Proxy types enumeration"""

    VMESS = "vmess"
    VLESS = "vless"
    TROJAN = "trojan"
    SHADOWSOCKS = "shadowsocks"


class MarzbanNextPlanModel(BaseModel):
    """Next plan model for user"""

    data_limit: Optional[int] = Field(None, title="Data Limit")
    expire: Optional[int] = Field(None, title="Expire")
    add_remaining_traffic: bool = Field(False, title="Add Remaining Traffic")
    fire_on_either: bool = Field(True, title="Fire On Either")


class MarzbanUserCreate(BaseModel):
    """Schema for creating a new user"""

    username: str = Field(..., title="Username")
    status: Optional[MarzbanUserStatusCreate] = Field(None, title="Status")
    proxies: Dict[MarzbanProxyTypes, Dict[str, str]] = Field(
        default_factory=dict, title="Proxies"
    )
    expire: Optional[int] = Field(None, title="Expire", description="UTC timestamp")
    data_limit: Optional[int] = Field(
        None, title="Data Limit", description="In bytes, 0 means unlimited"
    )
    data_limit_reset_strategy: MarzbanUserDataLimitResetStrategy = Field(
        MarzbanUserDataLimitResetStrategy.NO_RESET, title="Data Limit Reset Strategy"
    )
    inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Inbounds"
    )
    note: Optional[str] = Field(None, title="Note")
    sub_updated_at: Optional[datetime] = Field(None, title="Sub Updated At")
    sub_last_user_agent: Optional[str] = Field(None, title="Sub Last User Agent")
    online_at: Optional[datetime] = Field(None, title="Online At")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[datetime] = Field(None, title="On Hold Timeout")
    auto_delete_in_days: Optional[int] = Field(None, title="Auto Delete In Days")
    next_plan: Optional[MarzbanNextPlanModel] = Field(None, title="Next Plan")


class MarzbanUserModify(BaseModel):
    """Schema for modifying an existing user"""

    status: Optional[MarzbanUserStatusModify] = Field(None, title="Status")
    proxies: Dict[MarzbanProxyTypes, Dict[str, str]] = Field(
        default_factory=dict, title="Proxies"
    )
    expire: Optional[int] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[MarzbanUserDataLimitResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Inbounds"
    )
    note: Optional[str] = Field(None, title="Note")
    sub_updated_at: Optional[datetime] = Field(None, title="Sub Updated At")
    sub_last_user_agent: Optional[str] = Field(None, title="Sub Last User Agent")
    online_at: Optional[datetime] = Field(None, title="Online At")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[datetime] = Field(None, title="On Hold Timeout")
    auto_delete_in_days: Optional[int] = Field(None, title="Auto Delete In Days")
    next_plan: Optional[MarzbanNextPlanModel] = Field(None, title="Next Plan")


class MarzbanUserResponse(BaseModel):
    """User response schema"""

    username: str = Field(..., title="Username")
    status: MarzbanUserStatus = Field(..., title="Status")
    proxies: Dict[str, Any] = Field(..., title="Proxies")
    expire: Optional[int] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: MarzbanUserDataLimitResetStrategy = Field(
        MarzbanUserDataLimitResetStrategy.NO_RESET, title="Data Limit Reset Strategy"
    )
    inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Inbounds"
    )
    note: Optional[str] = Field(None, title="Note")
    sub_updated_at: Optional[datetime] = Field(None, title="Sub Updated At")
    sub_last_user_agent: Optional[str] = Field(None, title="Sub Last User Agent")
    online_at: Optional[datetime] = Field(None, title="Online At")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[datetime] = Field(None, title="On Hold Timeout")
    auto_delete_in_days: Optional[int] = Field(None, title="Auto Delete In Days")
    next_plan: Optional[MarzbanNextPlanModel] = Field(None, title="Next Plan")
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(0, title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    links: List[str] = Field(default_factory=list, title="Links")
    subscription_url: str = Field("", title="Subscription Url")
    excluded_inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Excluded Inbounds"
    )
    admin: Optional[Any] = Field(None, title="Admin")


class MarzbanUsersResponse(BaseModel):
    """Multiple users response schema"""

    users: List[MarzbanUserResponse] = Field(..., title="Users")
    total: int = Field(..., title="Total")


class MarzbanUserUsageResponse(BaseModel):
    """User usage response schema"""

    node_id: Optional[int] = Field(None, title="Node Id")
    node_name: str = Field(..., title="Node Name")
    used_traffic: int = Field(..., title="Used Traffic")


class MarzbanUserUsagesResponse(BaseModel):
    """User usages response schema"""

    username: str = Field(..., title="Username")
    usages: List[MarzbanUserUsageResponse] = Field(..., title="Usages")


class MarzbanUsersUsagesResponse(BaseModel):
    """Multiple users usages response schema"""

    usages: List[MarzbanUserUsageResponse] = Field(..., title="Usages")
