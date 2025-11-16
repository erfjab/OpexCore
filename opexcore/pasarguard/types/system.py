from typing import Optional
from pydantic import BaseModel, Field


class PasarGuardSystemStats(BaseModel):
    """System statistics response schema"""

    version: str = Field(..., title="Version")
    mem_total: Optional[int] = Field(None, title="Mem Total")
    mem_used: Optional[int] = Field(None, title="Mem Used")
    cpu_cores: Optional[int] = Field(None, title="Cpu Cores")
    cpu_usage: Optional[float] = Field(None, title="Cpu Usage")
    total_user: int = Field(..., title="Total User")
    online_users: int = Field(..., title="Online Users")
    active_users: int = Field(..., title="Active Users")
    on_hold_users: int = Field(..., title="On Hold Users")
    disabled_users: int = Field(..., title="Disabled Users")
    expired_users: int = Field(..., title="Expired Users")
    limited_users: int = Field(..., title="Limited Users")
    incoming_bandwidth: int = Field(..., title="Incoming Bandwidth")
    outgoing_bandwidth: int = Field(..., title="Outgoing Bandwidth")
