from pydantic import BaseModel, Field


class OVPanelToken(BaseModel):
    """Authentication token response"""

    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")


class OVPanelAdmin(BaseModel):
    """Admin response schema"""

    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
