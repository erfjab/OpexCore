from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class MarzneshinConfigTypes(str, Enum):
    """Config types enumeration"""

    LINKS = "links"
    BASE64_LINKS = "base64-links"
    XRAY = "xray"
    SING_BOX = "sing-box"
    CLASH = "clash"
    CLASH_META = "clash-meta"
    TEMPLATE = "template"
    BLOCK = "block"


class MarzneshinSubscriptionRule(BaseModel):
    """Subscription rule"""

    pattern: str = Field(..., title="Pattern", format="regex")
    result: MarzneshinConfigTypes = Field(..., title="Result")


class MarzneshinSubscriptionSettings(BaseModel):
    """Subscription settings"""

    template_on_acceptance: bool = Field(..., title="Template On Acceptance")
    profile_title: str = Field(..., title="Profile Title")
    support_link: str = Field(..., title="Support Link")
    update_interval: int = Field(..., title="Update Interval")
    shuffle_configs: bool = Field(False, title="Shuffle Configs")
    placeholder_if_disabled: bool = Field(True, title="Placeholder If Disabled")
    placeholder_remark: str = Field("disabled", title="Placeholder Remark")
    rules: List[MarzneshinSubscriptionRule] = Field(..., title="Rules")
