from typing import Optional, List
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class MarzneshinUserExpireStrategy(str, Enum):
    """User expire strategy enumeration"""

    NEVER = "never"
    FIXED_DATE = "fixed_date"
    START_ON_FIRST_USE = "start_on_first_use"


class MarzneshinUserDataUsageResetStrategy(str, Enum):
    """User data usage reset strategy enumeration"""

    NO_RESET = "no_reset"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class MarzneshinUsersSortingOptions(str, Enum):
    """Users sorting options enumeration"""

    USERNAME = "username"
    USED_TRAFFIC = "used_traffic"
    DATA_LIMIT = "data_limit"
    EXPIRE_DATE = "expire_date"
    CREATED_AT = "created_at"


class MarzneshinUserCreate(BaseModel):
    """Schema for creating a new user"""

    username: str = Field(..., pattern=r"^\w{3,32}$", title="Username")
    expire_strategy: MarzneshinUserExpireStrategy = Field(..., title="Expire Strategy")
    expire_date: Optional[datetime] = Field(None, title="Expire Date")
    usage_duration: Optional[int] = Field(None, title="Usage Duration")
    activation_deadline: Optional[datetime] = Field(None, title="Activation Deadline")
    data_limit: Optional[int] = Field(
        None, ge=0, title="Data Limit", description="data_limit can be 0 or greater"
    )
    data_limit_reset_strategy: MarzneshinUserDataUsageResetStrategy = Field(
        MarzneshinUserDataUsageResetStrategy.NO_RESET, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, max_length=500, title="Note")
    service_ids: List[int] = Field(default_factory=list, title="Service Ids")


class MarzneshinUserModify(BaseModel):
    """Schema for modifying an existing user"""

    username: str = Field(..., pattern=r"^\w{3,32}$", title="Username")
    expire_strategy: Optional[MarzneshinUserExpireStrategy] = Field(
        None, title="Expire Strategy"
    )
    expire_date: Optional[datetime] = Field(None, title="Expire Date")
    usage_duration: Optional[int] = Field(None, title="Usage Duration")
    activation_deadline: Optional[datetime] = Field(None, title="Activation Deadline")
    data_limit: Optional[int] = Field(
        None, ge=0, title="Data Limit", description="data_limit can be 0 or greater"
    )
    data_limit_reset_strategy: Optional[MarzneshinUserDataUsageResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, max_length=500, title="Note")
    service_ids: Optional[List[int]] = Field(None, title="Service Ids")


class MarzneshinUserResponse(BaseModel):
    """User response schema"""

    id: int = Field(..., title="Id")
    username: str = Field(..., pattern=r"^\w{3,32}$", title="Username")
    expire_strategy: MarzneshinUserExpireStrategy = Field(..., title="Expire Strategy")
    expire_date: Optional[datetime] = Field(None, title="Expire Date")
    usage_duration: Optional[int] = Field(None, title="Usage Duration")
    activation_deadline: Optional[datetime] = Field(None, title="Activation Deadline")
    key: str = Field(..., title="Key")
    data_limit: Optional[int] = Field(
        None, ge=0, title="Data Limit", description="data_limit can be 0 or greater"
    )
    data_limit_reset_strategy: MarzneshinUserDataUsageResetStrategy = Field(
        MarzneshinUserDataUsageResetStrategy.NO_RESET, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, max_length=500, title="Note")
    activated: bool = Field(..., title="Activated")
    is_active: bool = Field(..., title="Is Active")
    expired: bool = Field(..., title="Expired")
    data_limit_reached: bool = Field(..., title="Data Limit Reached")
    enabled: bool = Field(..., title="Enabled")
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(..., title="Lifetime Used Traffic")
    sub_revoked_at: Optional[datetime] = Field(None, title="Sub Revoked At")
    created_at: datetime = Field(..., title="Created At")
    service_ids: List[int] = Field(..., title="Service Ids")
    subscription_url: str = Field(..., title="Subscription Url")
    owner_username: Optional[str] = Field(None, title="Owner Username")
    traffic_reset_at: Optional[datetime] = Field(None, title="Traffic Reset At")
    sub_updated_at: Optional[datetime] = Field(None, title="Sub Updated At")
    sub_last_user_agent: Optional[str] = Field(None, title="Sub Last User Agent")
    online_at: Optional[datetime] = Field(None, title="Online At")


class MarzneshinUserNodeUsageSeries(BaseModel):
    """User node usage series"""

    node_id: Optional[int] = Field(None, title="Node Id")
    node_name: str = Field(..., title="Node Name")
    usages: List[List[int]] = Field(..., title="Usages")


class MarzneshinUserUsageSeriesResponse(BaseModel):
    """User usage series response"""

    username: str = Field(..., title="Username")
    node_usages: List[MarzneshinUserNodeUsageSeries] = Field(..., title="Node Usages")
    total: int = Field(..., title="Total")
