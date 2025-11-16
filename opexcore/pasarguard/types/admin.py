from typing import Optional
from pydantic import BaseModel, Field


class PasarGuardAdminCreate(BaseModel):
    """Schema for creating a new admin"""

    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: Optional[int] = Field(None, title="Telegram Id")
    discord_webhook: Optional[str] = Field(None, title="Discord Webhook")
    discord_id: Optional[int] = Field(None, title="Discord Id")
    is_disabled: Optional[bool] = Field(None, title="Is Disabled")
    sub_template: Optional[str] = Field(None, title="Sub Template")
    sub_domain: Optional[str] = Field(None, title="Sub Domain")
    profile_title: Optional[str] = Field(None, title="Profile Title")
    support_url: Optional[str] = Field(None, title="Support Url")


class PasarGuardAdminModify(BaseModel):
    """Schema for modifying an existing admin"""

    password: Optional[str] = Field(None, title="Password")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: Optional[int] = Field(None, title="Telegram Id")
    discord_webhook: Optional[str] = Field(None, title="Discord Webhook")
    discord_id: Optional[int] = Field(None, title="Discord Id")
    is_disabled: Optional[bool] = Field(None, title="Is Disabled")
    sub_template: Optional[str] = Field(None, title="Sub Template")
    sub_domain: Optional[str] = Field(None, title="Sub Domain")
    profile_title: Optional[str] = Field(None, title="Profile Title")
    support_url: Optional[str] = Field(None, title="Support Url")


class PasarGuardAdminDetails(BaseModel):
    """Admin response schema"""

    username: str = Field(..., title="Username")
    telegram_id: Optional[int] = Field(None, title="Telegram Id")
    discord_webhook: Optional[str] = Field(None, title="Discord Webhook")
    sub_domain: Optional[str] = Field(None, title="Sub Domain")
    profile_title: Optional[str] = Field(None, title="Profile Title")
    support_url: Optional[str] = Field(None, title="Support Url")
    id: Optional[int] = Field(None, title="Id")
    is_sudo: bool = Field(..., title="Is Sudo")
    total_users: int = Field(0, title="Total Users")
    used_traffic: int = Field(0, title="Used Traffic")
    is_disabled: bool = Field(False, title="Is Disabled")
    discord_id: Optional[int] = Field(None, title="Discord Id")
    sub_template: Optional[str] = Field(None, title="Sub Template")
    lifetime_used_traffic: Optional[int] = Field(None, title="Lifetime Used Traffic")


class PasarGuardToken(BaseModel):
    """Authentication token response"""

    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")
