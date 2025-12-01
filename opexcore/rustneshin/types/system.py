from typing import Optional, List, Tuple
from enum import Enum
from pydantic import BaseModel, Field


class RustneshinGranularity(str, Enum):
    """Granularity for stats"""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class RustneshinConfigTypes(str, Enum):
    """Config types"""

    LINKS = "links"
    BASE64_LINKS = "base64-links"
    XRAY = "xray"
    SING_BOX = "sing-box"
    CLASH = "clash"
    CLASH_META = "clash-meta"
    WIREGUARD = "wireguard"
    TEMPLATE = "template"
    BLOCK = "block"


class RustneshinNodesStats(BaseModel):
    """Nodes statistics"""

    total: int = Field(..., title="Total")
    healthy: int = Field(..., title="Healthy")
    unhealthy: int = Field(..., title="Unhealthy")


class RustneshinUsersStats(BaseModel):
    """Users statistics"""

    total: int = Field(..., title="Total")
    active: int = Field(..., title="Active")
    on_hold: int = Field(..., title="On Hold")
    expired: int = Field(..., title="Expired")
    limited: int = Field(..., title="Limited")
    online: int = Field(..., title="Online")


class RustneshinTrafficUsageSeries(BaseModel):
    """Traffic usage series"""

    total: int = Field(..., title="Total")
    usages: List[Tuple[int, int]] = Field(default_factory=list, title="Usages")
    step: int = Field(3600, title="Step")


class RustneshinSubscriptionRule(BaseModel):
    """Subscription rule"""

    pattern: str = Field(..., title="Pattern")
    result: RustneshinConfigTypes = Field(..., title="Result")


class RustneshinSubscriptionSettings(BaseModel):
    """Subscription settings"""

    template_on_acceptance: bool = Field(..., title="Template On Acceptance")
    profile_title: str = Field(..., title="Profile Title")
    support_link: str = Field(..., title="Support Link")
    update_interval: int = Field(..., title="Update Interval")
    rules: List[RustneshinSubscriptionRule] = Field(default_factory=list, title="Rules")
    shuffle_configs: Optional[bool] = Field(None, title="Shuffle Configs")
    placeholder_if_disabled: Optional[bool] = Field(
        None, title="Placeholder If Disabled"
    )
    placeholder_remark: Optional[str] = Field(None, title="Placeholder Remark")


class RustneshinTemplateSettings(BaseModel):
    """Template settings"""

    value: Optional[str] = Field(None, title="Value")
