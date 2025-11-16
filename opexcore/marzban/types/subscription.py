from typing import Optional, Dict, List
from datetime import datetime
from pydantic import BaseModel, Field
from .user import (
    MarzbanProxyTypes,
    MarzbanUserStatus,
    MarzbanUserDataLimitResetStrategy,
    MarzbanNextPlanModel,
)


class MarzbanSubscriptionUserResponse(BaseModel):
    """Subscription user response schema"""

    username: str = Field(..., title="Username")
    status: MarzbanUserStatus = Field(..., title="Status")
    proxies: Dict[MarzbanProxyTypes, Dict[str, str]] = Field(
        default_factory=dict, title="Proxies"
    )
    expire: Optional[int] = Field(None, title="Expire")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    data_limit_reset_strategy: MarzbanUserDataLimitResetStrategy = Field(
        MarzbanUserDataLimitResetStrategy.NO_RESET, title="Data Limit Reset Strategy"
    )
    sub_updated_at: Optional[datetime] = Field(None, title="Sub Updated At")
    sub_last_user_agent: Optional[str] = Field(None, title="Sub Last User Agent")
    online_at: Optional[datetime] = Field(None, title="Online At")
    on_hold_expire_duration: Optional[int] = Field(
        None, title="On Hold Expire Duration"
    )
    on_hold_timeout: Optional[datetime] = Field(None, title="On Hold Timeout")
    next_plan: Optional[MarzbanNextPlanModel] = Field(None, title="Next Plan")
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(0, title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    links: List[str] = Field(default_factory=list, title="Links")
    subscription_url: str = Field("", title="Subscription Url")
