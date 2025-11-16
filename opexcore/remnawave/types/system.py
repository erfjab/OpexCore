from pydantic import BaseModel, Field


class RemnawaveUserStatistics(BaseModel):
    """User statistics"""

    active: int
    disabled: int
    limited: int
    expired: int

    class Config:
        populate_by_name = True


class RemnawaveOnlineStatistics(BaseModel):
    """Online statistics"""

    last_day: int = Field(..., alias="lastDay")
    last_week: int = Field(..., alias="lastWeek")
    never_online: int = Field(..., alias="neverOnline")
    online_now: int = Field(..., alias="onlineNow")

    class Config:
        populate_by_name = True


class RemnawaveNodeStatistics(BaseModel):
    """Node statistics"""

    total_online: int = Field(..., alias="totalOnline")

    class Config:
        populate_by_name = True


class RemnawaveSystemStats(BaseModel):
    """System statistics response"""

    user_stats: RemnawaveUserStatistics = Field(..., alias="userStats")
    online_stats: RemnawaveOnlineStatistics = Field(..., alias="onlineStats")
    nodes: RemnawaveNodeStatistics

    class Config:
        populate_by_name = True
