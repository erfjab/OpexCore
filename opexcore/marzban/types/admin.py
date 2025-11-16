from typing import Optional
from pydantic import BaseModel, Field


class MarzbanAdminCreate(BaseModel):
    """Schema for creating a new admin"""

    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    password: str = Field(..., title="Password")
    telegram_id: Optional[int] = Field(None, title="Telegram Id")
    discord_webhook: Optional[str] = Field(None, title="Discord Webhook")
    users_usage: Optional[int] = Field(None, title="Users Usage")


class MarzbanAdminModify(BaseModel):
    """Schema for modifying an existing admin"""

    password: Optional[str] = Field(None, title="Password")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: Optional[int] = Field(None, title="Telegram Id")
    discord_webhook: Optional[str] = Field(None, title="Discord Webhook")


class MarzbanAdmin(BaseModel):
    """Admin response schema"""

    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: Optional[int] = Field(None, title="Telegram Id")
    discord_webhook: Optional[str] = Field(None, title="Discord Webhook")
    users_usage: Optional[int] = Field(None, title="Users Usage")


class MarzbanToken(BaseModel):
    """Authentication token response"""

    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")
