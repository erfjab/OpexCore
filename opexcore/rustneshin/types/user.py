from typing import Optional, List, Tuple
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class RustneshinUserExpireStrategy(str, Enum):
    """User expire strategy"""

    NEVER = "never"
    FIXED_DATE = "fixed_date"
    START_ON_FIRST_USE = "start_on_first_use"


class RustneshinUserDataUsageResetStrategy(str, Enum):
    """Data limit reset strategy"""

    NO_RESET = "no_reset"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class RustneshinUsersSortingOptions(str, Enum):
    """Users sorting options"""

    USERNAME = "username"
    USED_TRAFFIC = "used_traffic"
    DATA_LIMIT = "data_limit"
    EXPIRE_DATE = "expire_date"
    CREATED_AT = "created_at"


class RustneshinUserCreate(BaseModel):
    """Schema for creating a new user"""

    username: str = Field(..., title="Username")
    expire_strategy: RustneshinUserExpireStrategy = Field(..., title="Expire Strategy")
    key: Optional[str] = Field(None, title="Key")
    expire_date: Optional[datetime] = Field(None, title="Expire Date")
    usage_duration: Optional[int] = Field(None, title="Usage Duration")
    activation_deadline: Optional[datetime] = Field(None, title="Activation Deadline")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[RustneshinUserDataUsageResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, title="Note")
    service_ids: List[int] = Field(default_factory=list, title="Service IDs")


class RustneshinUserModify(BaseModel):
    """Schema for modifying an existing user"""

    username: str = Field(..., title="Username")
    key: Optional[str] = Field(None, title="Key")
    expire_strategy: Optional[RustneshinUserExpireStrategy] = Field(
        None, title="Expire Strategy"
    )
    expire_date: Optional[datetime] = Field(None, title="Expire Date")
    usage_duration: Optional[int] = Field(None, title="Usage Duration")
    activation_deadline: Optional[datetime] = Field(None, title="Activation Deadline")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: Optional[RustneshinUserDataUsageResetStrategy] = Field(
        None, title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, title="Note")
    service_ids: Optional[List[int]] = Field(None, title="Service IDs")


class RustneshinUserResponse(BaseModel):
    """User response schema"""

    id: int = Field(..., title="ID")
    username: str = Field(..., title="Username")
    key: str = Field("", title="Key")
    expire_strategy: RustneshinUserExpireStrategy = Field(..., title="Expire Strategy")
    expire_date: Optional[datetime] = Field(None, title="Expire Date")
    usage_duration: Optional[int] = Field(None, title="Usage Duration")
    activation_deadline: Optional[datetime] = Field(None, title="Activation Deadline")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: RustneshinUserDataUsageResetStrategy = Field(
        ..., title="Data Limit Reset Strategy"
    )
    note: Optional[str] = Field(None, title="Note")
    activated: bool = Field(..., title="Activated")
    is_active: bool = Field(..., title="Is Active")
    expired: bool = Field(..., title="Expired")
    data_limit_reached: bool = Field(..., title="Data Limit Reached")
    enabled: bool = Field(..., title="Enabled")
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(..., title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    traffic_reset_at: Optional[datetime] = Field(None, title="Traffic Reset At")
    online_at: Optional[datetime] = Field(None, title="Online At")
    sub_updated_at: Optional[datetime] = Field(None, title="Subscription Updated At")
    sub_last_user_agent: Optional[str] = Field(
        None, title="Subscription Last User Agent"
    )
    sub_revoked_at: Optional[datetime] = Field(None, title="Subscription Revoked At")
    service_ids: List[int] = Field(default_factory=list, title="Service IDs")
    subscription_url: str = Field(..., title="Subscription URL")
    admin_id: Optional[int] = Field(None, title="Admin ID")
    owner_username: Optional[str] = Field(None, title="Owner Username")


class RustneshinPageUserResponse(BaseModel):
    """Paginated user response"""

    items: List[RustneshinUserResponse] = Field(default_factory=list, title="Items")
    total: int = Field(..., title="Total")
    page: int = Field(..., title="Page")
    size: int = Field(..., title="Size")
    pages: int = Field(..., title="Pages")


class RustneshinUserNodeUsageSeries(BaseModel):
    """User node usage series"""

    node_id: Optional[int] = Field(None, title="Node ID")
    node_name: str = Field(..., title="Node Name")
    usages: List[Tuple[int, int]] = Field(default_factory=list, title="Usages")


class RustneshinUserUsageSeriesResponse(BaseModel):
    """User usage series response"""

    username: str = Field(..., title="Username")
    node_usages: List[RustneshinUserNodeUsageSeries] = Field(
        default_factory=list, title="Node Usages"
    )
    total: int = Field(..., title="Total")
