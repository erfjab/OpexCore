from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class GuardUsageDetailStats(BaseModel):
    """Usage detail statistics"""

    start: Optional[datetime] = Field(None, title="Start")
    end: Optional[datetime] = Field(None, title="End")
    remark: Optional[str] = Field(None, title="Remark")
    step: Optional[int] = Field(None, title="Step")
    usage: int = Field(..., title="Usage")


class GuardCountDetailStats(BaseModel):
    """Count detail statistics"""

    start: Optional[datetime] = Field(None, title="Start")
    end: Optional[datetime] = Field(None, title="End")
    count: int = Field(..., title="Count")


class GuardTopSubDetailStats(BaseModel):
    """Top subscription detail statistics"""

    username: str = Field(..., title="Username")
    is_active: bool = Field(..., title="Is Active")
    usage: int = Field(..., title="Usage")


class GuardExpireSubDetailStats(BaseModel):
    """Expire subscription detail statistics"""

    username: str = Field(..., title="Username")
    is_active: bool = Field(..., title="Is Active")
    expire: int = Field(..., title="Expire")


class GuardStatsResponse(BaseModel):
    """General statistics response"""

    total_subscriptions: int = Field(..., title="Total Subscriptions")
    active_subscriptions: int = Field(..., title="Active Subscriptions")
    inactive_subscriptions: int = Field(..., title="Inactive Subscriptions")
    online_subscriptions: int = Field(..., title="Online Subscriptions")
    most_usage_subscription: Optional[str] = Field(
        None, title="Most Usage Subscription"
    )
    most_usage_subscriptions: List[GuardUsageDetailStats] = Field(
        ..., title="Most Usage Subscriptions"
    )
    total_admins: int = Field(..., title="Total Admins")
    active_admins: int = Field(..., title="Active Admins")
    inactive_admins: int = Field(..., title="Inactive Admins")
    most_usage_admins: List[GuardUsageDetailStats] = Field(
        ..., title="Most Usage Admins"
    )
    total_nodes: int = Field(..., title="Total Nodes")
    active_nodes: int = Field(..., title="Active Nodes")
    inactive_nodes: int = Field(..., title="Inactive Nodes")
    most_usage_nodes: List[GuardUsageDetailStats] = Field(..., title="Most Usage Nodes")
    total_lifetime_usages: int = Field(..., title="Total Lifetime Usages")
    total_day_usages: int = Field(..., title="Total Day Usages")
    total_week_usages: int = Field(..., title="Total Week Usages")
    last_24h_usages: List[GuardUsageDetailStats] = Field(..., title="Last 24H Usages")
    last_7d_usages: List[GuardUsageDetailStats] = Field(..., title="Last 7D Usages")


class AdminStatsResponseNew(BaseModel):
    """Combined admin statistics response"""

    usage_limit: Optional[int] = Field(..., title="Usage Limit")
    current_usage: int = Field(..., title="Current Usage")
    left_usage: Optional[int] = Field(..., title="Left Usage")
    lifetime_usage: int = Field(..., title="Lifetime Usage")
    current_day_usage: int = Field(..., title="Current Day Usage")
    current_week_usage: int = Field(..., title="Current Week Usage")
    yesterday_usage: int = Field(..., title="Yesterday Usage")
    last_week_usage: int = Field(..., title="Last Week Usage")
    last_24h_usages: List[GuardUsageDetailStats] = Field(..., title="Last 24H Usages")
    last_7d_usages: List[GuardUsageDetailStats] = Field(..., title="Last 7D Usages")
    last_1m_usages: List[GuardUsageDetailStats] = Field(..., title="Last 1M Usages")
    last_3m_usages: List[GuardUsageDetailStats] = Field(..., title="Last 3M Usages")
    last_1y_usages: List[GuardUsageDetailStats] = Field(..., title="Last 1Y Usages")
    today_top_10_usage_subscriptions: List[GuardTopSubDetailStats] = Field(
        ..., title="Today Top 10 Usage Subscriptions"
    )
    week_top_10_usage_subscriptions: List[GuardTopSubDetailStats] = Field(
        ..., title="Week Top 10 Usage Subscriptions"
    )
    month_top_10_usage_subscriptions: List[GuardTopSubDetailStats] = Field(
        ..., title="Month Top 10 Usage Subscriptions"
    )
    last_24h_counts: List[GuardCountDetailStats] = Field(..., title="Last 24H Counts")
    last_7d_counts: List[GuardCountDetailStats] = Field(..., title="Last 7D Counts")
    last_1m_counts: List[GuardCountDetailStats] = Field(..., title="Last 1M Counts")
    last_3m_counts: List[GuardCountDetailStats] = Field(..., title="Last 3M Counts")
    last_1y_counts: List[GuardCountDetailStats] = Field(..., title="Last 1Y Counts")
    limit_count: int = Field(..., title="Limit Count")
    current_count: int = Field(..., title="Current Count")
    left_count: int = Field(..., title="Left Count")
    total_subscriptions: int = Field(..., title="Total Subscriptions")
    active_subscriptions: int = Field(..., title="Active Subscriptions")
    inactive_subscriptions: int = Field(..., title="Inactive Subscriptions")
    disabled_subscriptions: int = Field(..., title="Disabled Subscriptions")
    expired_subscriptions: int = Field(..., title="Expired Subscriptions")
    limited_subscriptions: int = Field(..., title="Limited Subscriptions")
    today_new_subscriptions: int = Field(..., title="Today New Subscriptions")
    yesterday_new_subscriptions: int = Field(..., title="Yesterday New Subscriptions")
    today_requested_subscriptions: int = Field(
        ..., title="Today Requested Subscriptions"
    )
    today_revoked_subscriptions: int = Field(..., title="Today Revoked Subscriptions")
    today_reseted_subscriptions: int = Field(..., title="Today Reseted Subscriptions")
    today_expire_soon_subscriptions: List[GuardExpireSubDetailStats] = Field(
        ..., title="Today Expire Soon Subscriptions"
    )
    week_expire_soon_subscriptions: List[GuardExpireSubDetailStats] = Field(
        ..., title="Week Expire Soon Subscriptions"
    )
    today_removed_subscriptions: int = Field(..., title="Today Removed Subscriptions")
    yesterday_removed_subscriptions: int = Field(
        ..., title="Yesterday Removed Subscriptions"
    )
    total_removed_subscriptions: int = Field(..., title="Total Removed Subscriptions")


class GuardSubscriptionStatusStatsResponse(BaseModel):
    """Subscription status statistics response"""

    total: int = Field(..., title="Total")
    active: int = Field(..., title="Active")
    disabled: int = Field(..., title="Disabled")
    expired: int = Field(..., title="Expired")
    limited: int = Field(..., title="Limited")
    pending: int = Field(..., title="Pending")
    available: int = Field(..., title="Available")
    unavailable: int = Field(..., title="Unavailable")
    online: int = Field(..., title="Online")
    offline: int = Field(..., title="Offline")


class GuardUsageSubscriptionDetail(BaseModel):
    """Usage subscription detail"""

    username: str = Field(..., title="Username")
    usage: int = Field(..., title="Usage")
    is_active: bool = Field(..., title="Is Active")


class GuardMostUsageSubscription(BaseModel):
    """Most usage subscription response"""

    subscriptions: List[GuardUsageSubscriptionDetail] = Field(..., title="Subscriptions")
    start_date: datetime = Field(..., title="Start Date")
    end_date: datetime = Field(..., title="End Date")


class GuardUsageDetail(BaseModel):
    """Usage detail"""

    start_date: datetime = Field(..., title="Start Date")
    end_date: datetime = Field(..., title="End Date")
    usage: int = Field(..., title="Usage")


class GuardUsageStatsResponse(BaseModel):
    """Usage statistics response"""

    total: int = Field(..., title="Total")
    usages: List[GuardUsageDetail] = Field(..., title="Usages")
    start_date: datetime = Field(..., title="Start Date")
    end_date: datetime = Field(..., title="End Date")


class GuardAgentStatsDetail(BaseModel):
    """Agent statistics detail"""

    category: str = Field(..., title="Category")
    count: int = Field(..., title="Count")


class GuardAgentStatsResponse(BaseModel):
    """Agent statistics response"""

    agents: List[GuardAgentStatsDetail] = Field(..., title="Agents")
