from typing import Optional, List
from pydantic import BaseModel, Field


class MarzneshinAdminsStats(BaseModel):
    """Admins statistics"""

    total: int = Field(..., title="Total")


class MarzneshinNodesStats(BaseModel):
    """Nodes statistics"""

    total: int = Field(..., title="Total")
    healthy: int = Field(..., title="Healthy")
    unhealthy: int = Field(..., title="Unhealthy")


class MarzneshinUsersStats(BaseModel):
    """Users statistics"""

    total: int = Field(..., title="Total")
    active: int = Field(..., title="Active")
    on_hold: int = Field(..., title="On Hold")
    expired: int = Field(..., title="Expired")
    limited: int = Field(..., title="Limited")
    online: int = Field(..., title="Online")


class MarzneshinTrafficUsageSeries(BaseModel):
    """Traffic usage series"""

    step: int = Field(3600, title="Step")
    total: int = Field(0, title="Total")
    usages: List[List[int]] = Field(..., title="Usages")


class MarzneshinTelegramSettings(BaseModel):
    """Telegram settings"""

    token: str = Field(..., title="Token")
    admin_id: List[int] = Field(..., title="Admin Id")
    channel_id: Optional[int] = Field(None, title="Channel Id")
