from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class GuardAdminRole(str, Enum):
    """Admin role types"""

    OWNER = "owner"
    SELLER = "seller"
    RESELLER = "reseller"


class GuardAdminPlaceHolderCategory(str, Enum):
    """Admin placeholder categories"""

    INFO = "info"
    LIMITED = "limited"
    EXPIRED = "expired"
    DISABLED = "disabled"


class GuardAdminPlaceHolder(BaseModel):
    """Admin placeholder configuration"""

    remark: str = Field(..., title="Remark")
    categories: List[GuardAdminPlaceHolderCategory] = Field(..., title="Categories")


class GuardAdminCreate(BaseModel):
    """Schema for creating a new admin"""

    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    role: GuardAdminRole = Field(..., title="Role")
    service_ids: List[int] = Field(..., title="Service Ids")
    create_access: Optional[bool] = Field(False, title="Create Access")
    update_access: Optional[bool] = Field(False, title="Update Access")
    remove_access: Optional[bool] = Field(False, title="Remove Access")
    count_limit: Optional[int] = Field(None, title="Count Limit")
    usage_limit: Optional[int] = Field(None, title="Usage Limit")
    access_prefix: Optional[str] = Field(None, title="Access Prefix")
    placeholders: Optional[List[GuardAdminPlaceHolder]] = Field(
        None, title="Placeholders"
    )
    max_links: Optional[int] = Field(None, title="Max Links")
    shuffle_links: Optional[bool] = Field(None, title="Shuffle Links")
    access_title: Optional[str] = Field(None, title="Access Title")
    access_description: Optional[str] = Field(None, title="Access Description")
    telegram_id: Optional[str] = Field(None, title="Telegram Id")
    telegram_token: Optional[str] = Field(None, title="Telegram Token")
    expire_warning_days: Optional[int] = Field(None, title="Expire Warning Days")
    usage_warning_percent: Optional[int] = Field(None, title="Usage Warning Percent")
    username_tag: Optional[bool] = Field(None, title="Username Tag")
    support_url: Optional[str] = Field(None, title="Support Url")
    update_interval: Optional[int] = Field(None, title="Update Interval")
    announce: Optional[str] = Field(None, title="Announce")
    announce_url: Optional[str] = Field(None, title="Announce Url")


class GuardAdminUpdate(BaseModel):
    """Schema for updating an existing admin"""

    password: Optional[str] = Field(None, title="Password")
    create_access: Optional[bool] = Field(None, title="Create Access")
    update_access: Optional[bool] = Field(None, title="Update Access")
    remove_access: Optional[bool] = Field(None, title="Remove Access")
    count_limit: Optional[int] = Field(None, title="Count Limit")
    usage_limit: Optional[int] = Field(None, title="Usage Limit")
    service_ids: Optional[List[int]] = Field(None, title="Service Ids")
    placeholders: Optional[List[GuardAdminPlaceHolder]] = Field(
        None, title="Placeholders"
    )
    max_links: Optional[int] = Field(None, title="Max Links")
    shuffle_links: Optional[bool] = Field(None, title="Shuffle Links")
    access_prefix: Optional[str] = Field(None, title="Access Prefix")
    access_title: Optional[str] = Field(None, title="Access Title")
    access_description: Optional[str] = Field(None, title="Access Description")
    telegram_id: Optional[str] = Field(None, title="Telegram Id")
    telegram_token: Optional[str] = Field(None, title="Telegram Token")
    expire_warning_days: Optional[int] = Field(None, title="Expire Warning Days")
    usage_warning_percent: Optional[int] = Field(None, title="Usage Warning Percent")
    username_tag: Optional[bool] = Field(None, title="Username Tag")
    support_url: Optional[str] = Field(None, title="Support Url")
    update_interval: Optional[int] = Field(None, title="Update Interval")
    announce: Optional[str] = Field(None, title="Announce")
    announce_url: Optional[str] = Field(None, title="Announce Url")


class GuardAdminCurrentUpdate(BaseModel):
    """Schema for updating current admin"""

    password: Optional[str] = Field(None, title="Password")
    placeholders: Optional[List[GuardAdminPlaceHolder]] = Field(
        None, title="Placeholders"
    )
    max_links: Optional[int] = Field(None, title="Max Links")
    shuffle_links: Optional[bool] = Field(None, title="Shuffle Links")
    access_title: Optional[str] = Field(None, title="Access Title")
    access_description: Optional[str] = Field(None, title="Access Description")
    telegram_id: Optional[str] = Field(None, title="Telegram Id")
    telegram_token: Optional[str] = Field(None, title="Telegram Token")
    expire_warning_days: Optional[int] = Field(None, title="Expire Warning Days")
    usage_warning_percent: Optional[int] = Field(None, title="Usage Warning Percent")
    username_tag: Optional[bool] = Field(None, title="Username Tag")
    support_url: Optional[str] = Field(None, title="Support Url")
    update_interval: Optional[int] = Field(None, title="Update Interval")
    announce: Optional[str] = Field(None, title="Announce")
    announce_url: Optional[str] = Field(None, title="Announce Url")


class GuardAdminResponse(BaseModel):
    """Admin response schema"""

    id: int = Field(..., title="Id")
    enabled: bool = Field(..., title="Enabled")
    username: str = Field(..., title="Username")
    role: GuardAdminRole = Field(..., title="Role")
    service_ids: List[int] = Field(..., title="Service Ids")
    create_access: Optional[bool] = Field(..., title="Create Access")
    update_access: Optional[bool] = Field(..., title="Update Access")
    remove_access: Optional[bool] = Field(..., title="Remove Access")
    count_limit: Optional[int] = Field(..., title="Count Limit")
    current_count: Optional[int] = Field(..., title="Current Count")
    left_count: Optional[int] = Field(..., title="Left Count")
    reached_count_limit: Optional[bool] = Field(..., title="Reached Count Limit")
    usage_limit: Optional[int] = Field(..., title="Usage Limit")
    current_usage: Optional[int] = Field(..., title="Current Usage")
    left_usage: Optional[int] = Field(..., title="Left Usage")
    reached_usage_limit: Optional[bool] = Field(..., title="Reached Usage Limit")
    placeholders: Optional[List[GuardAdminPlaceHolder]] = Field(
        ..., title="Placeholders"
    )
    max_links: Optional[int] = Field(..., title="Max Links")
    shuffle_links: Optional[bool] = Field(..., title="Shuffle Links")
    api_key: str = Field(..., title="Api Key")
    access_title: Optional[str] = Field(None, title="Access Title")
    access_description: Optional[str] = Field(None, title="Access Description")
    telegram_id: Optional[str] = Field(None, title="Telegram Id")
    telegram_token: Optional[str] = Field(None, title="Telegram Token")
    expire_warning_days: Optional[int] = Field(None, title="Expire Warning Days")
    usage_warning_percent: Optional[int] = Field(None, title="Usage Warning Percent")
    username_tag: Optional[bool] = Field(None, title="Username Tag")
    support_url: Optional[str] = Field(None, title="Support Url")
    update_interval: Optional[int] = Field(None, title="Update Interval")
    announce: Optional[str] = Field(None, title="Announce")
    announce_url: Optional[str] = Field(None, title="Announce Url")
    last_login_at: Optional[datetime] = Field(..., title="Last Login At")
    last_online_at: Optional[datetime] = Field(..., title="Last Online At")
    created_at: datetime = Field(..., title="Created At")
    updated_at: datetime = Field(..., title="Updated At")


class GuardAdminToken(BaseModel):
    """Admin authentication token"""

    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")


class GuardAdminUsageLog(BaseModel):
    """Admin usage log entry"""

    usage: int = Field(..., title="Usage")
    created_at: datetime = Field(..., title="Created At")


class GuardAdminUsageLogsResponse(BaseModel):
    """Admin usage logs response"""

    admin: GuardAdminResponse = Field(..., title="Admin")
    usages: List[GuardAdminUsageLog] = Field(..., title="Usages")
