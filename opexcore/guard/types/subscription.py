from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class GuardSubscriptionCreate(BaseModel):
    """Schema for creating a new subscription"""

    username: str = Field(..., title="Username")
    limit_usage: int = Field(..., title="Limit Usage")
    limit_expire: int = Field(..., title="Limit Expire")
    service_ids: List[int] = Field(..., title="Service Ids")
    access_key: Optional[str] = Field(None, title="Access Key")
    note: Optional[str] = Field(None, title="Note")


class GuardSubscriptionUpdate(BaseModel):
    """Schema for updating an existing subscription"""

    username: Optional[str] = Field(None, title="Username")
    limit_usage: Optional[int] = Field(None, title="Limit Usage")
    limit_expire: Optional[int] = Field(None, title="Limit Expire")
    service_ids: Optional[List[int]] = Field(None, title="Service Ids")
    note: Optional[str] = Field(None, title="Note")


class GuardSubscriptionResponse(BaseModel):
    """Subscription response schema"""

    id: int = Field(..., title="Id")
    username: str = Field(..., title="Username")
    owner_username: str = Field(..., title="Owner Username")
    access_key: str = Field(..., title="Access Key")
    enabled: bool = Field(..., title="Enabled")
    activated: bool = Field(..., title="Activated")
    reached: bool = Field(..., title="Reached")
    limited: bool = Field(..., title="Limited")
    expired: bool = Field(..., title="Expired")
    is_active: bool = Field(..., title="Is Active")
    is_online: bool = Field(..., title="Is Online")
    link: str = Field(..., title="Link")
    limit_usage: int = Field(..., title="Limit Usage")
    reset_usage: int = Field(..., title="Reset Usage")
    total_usage: int = Field(..., title="Total Usage")
    current_usage: int = Field(..., title="Current Usage")
    limit_expire: int = Field(..., title="Limit Expire")
    service_ids: List[int] = Field(..., title="Service Ids")
    note: Optional[str] = Field(None, title="Note")
    online_at: Optional[datetime] = Field(..., title="Online At")
    last_reset_at: Optional[datetime] = Field(..., title="Last Reset At")
    last_revoke_at: Optional[datetime] = Field(..., title="Last Revoke At")
    last_request_at: Optional[datetime] = Field(..., title="Last Request At")
    last_client_agent: Optional[str] = Field(..., title="Last Client Agent")
    created_at: datetime = Field(..., title="Created At")
    updated_at: datetime = Field(..., title="Updated At")


class GuardSubscriptionUsageLog(BaseModel):
    """Subscription usage log entry"""

    usage: int = Field(..., title="Usage")
    created_at: datetime = Field(..., title="Created At")


class GuardSubscriptionUsageLogsResponse(BaseModel):
    """Subscription usage logs response"""

    subscription: GuardSubscriptionResponse = Field(..., title="Subscription")
    usages: List[GuardSubscriptionUsageLog] = Field(..., title="Usages")


class GuardSubscriptionStatsResponse(BaseModel):
    """Subscription statistics response"""

    total: int = Field(..., title="Total")
    active: int = Field(..., title="Active")
    inactive: int = Field(..., title="Inactive")
    disabled: int = Field(..., title="Disabled")
    expired: int = Field(..., title="Expired")
    limited: int = Field(..., title="Limited")
    has_revoked: int = Field(..., title="Has Revoked")
    has_reseted: int = Field(..., title="Has Reseted")
    total_removed: int = Field(..., title="Total Removed")
    total_usage: int = Field(..., title="Total Usage")
