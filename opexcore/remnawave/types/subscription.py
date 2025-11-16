from pydantic import BaseModel, Field


class RemnawaveSubscription(BaseModel):
    """Subscription response"""

    short_uuid: str = Field(..., alias="shortUuid")
    username: str
    days_left: int = Field(..., alias="daysLeft")
    traffic_used: str = Field(..., alias="trafficUsed")
    traffic_limit: str = Field(..., alias="trafficLimit")
    lifetime_traffic_used: str = Field(..., alias="lifetimeTrafficUsed")
    expires_at: str = Field(..., alias="expiresAt")
    is_active: bool = Field(..., alias="isActive")
    user_status: str = Field(..., alias="userStatus")
    subscription_url: str = Field(..., alias="subscriptionUrl")

    class Config:
        populate_by_name = True
