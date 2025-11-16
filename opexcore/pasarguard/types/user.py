from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class PasarGuardUserStatus(str, Enum):
    """User status enumeration"""

    active = "active"
    disabled = "disabled"
    limited = "limited"
    expired = "expired"
    on_hold = "on_hold"


class PasarGuardDataLimitResetStrategy(str, Enum):
    """Data limit reset strategy"""

    no_reset = "no_reset"
    day = "day"
    week = "week"
    month = "month"
    year = "year"


class PasarGuardUserCreate(BaseModel):
    """Schema for creating a new user"""

    username: str = Field(..., title="Username")
    proxy_settings: Optional[Dict[str, Any]] = Field(None, title="Proxy Settings")
    expire: Optional[Any] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[PasarGuardDataLimitResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, title="Note")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[Any] = Field(None, title="On Hold Timeout")
    group_ids: Optional[List[int]] = Field(None, title="Group Ids")
    auto_delete_in_days: Optional[int] = Field(None, title="Auto Delete In Days")
    status: Optional[str] = Field(None, title="Status")


class PasarGuardUserModify(BaseModel):
    """Schema for modifying an existing user"""

    proxy_settings: Optional[Dict[str, Any]] = Field(None, title="Proxy Settings")
    expire: Optional[Any] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[PasarGuardDataLimitResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, title="Note")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[Any] = Field(None, title="On Hold Timeout")
    group_ids: Optional[List[int]] = Field(None, title="Group Ids")
    auto_delete_in_days: Optional[int] = Field(None, title="Auto Delete In Days")
    status: Optional[str] = Field(None, title="Status")


class PasarGuardUserResponse(BaseModel):
    """User response schema"""

    id: int = Field(..., title="Id")
    username: str = Field(..., title="Username")
    status: PasarGuardUserStatus = Field(..., title="Status")
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(0, title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    proxy_settings: Optional[Dict[str, Any]] = Field(None, title="Proxy Settings")
    expire: Optional[Any] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[PasarGuardDataLimitResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, title="Note")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[Any] = Field(None, title="On Hold Timeout")
    group_ids: Optional[List[int]] = Field(None, title="Group Ids")
    auto_delete_in_days: Optional[int] = Field(None, title="Auto Delete In Days")
    edit_at: Optional[datetime] = Field(None, title="Edit At")
    online_at: Optional[datetime] = Field(None, title="Online At")
    subscription_url: str = Field("", title="Subscription Url")
    admin: Optional[Dict[str, Any]] = Field(None, title="Admin")


class PasarGuardUsersResponse(BaseModel):
    """Users list response schema"""

    users: List[PasarGuardUserResponse] = Field(..., title="Users")
    total: int = Field(..., title="Total")


class PasarGuardSubscriptionUserResponse(BaseModel):
    """Subscription user response schema"""

    id: int = Field(..., title="Id")
    username: str = Field(..., title="Username")
    status: PasarGuardUserStatus = Field(..., title="Status")
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(0, title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    proxy_settings: Optional[Dict[str, Any]] = Field(None, title="Proxy Settings")
    expire: Optional[Any] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[PasarGuardDataLimitResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[Any] = Field(None, title="On Hold Timeout")
    group_ids: Optional[List[int]] = Field(None, title="Group Ids")
    edit_at: Optional[datetime] = Field(None, title="Edit At")
    online_at: Optional[datetime] = Field(None, title="Online At")
