from typing import Optional
from pydantic import BaseModel, Field


class RemnawaveToken(BaseModel):
    """Token response"""

    access_token: str = Field(..., alias="accessToken")

    class Config:
        populate_by_name = True


class RemnawaveAdmin(BaseModel):
    """Admin response"""

    uuid: str
    username: str
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    discord_webhook: Optional[str] = Field(None, alias="discordWebhook")
    is_sudo: bool = Field(..., alias="isSudo")
    created_at: str = Field(..., alias="createdAt")
    updated_at: str = Field(..., alias="updatedAt")

    class Config:
        populate_by_name = True


class RemnawaveAdminCreate(BaseModel):
    """Admin creation data"""

    username: str
    password: str
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    discord_webhook: Optional[str] = Field(None, alias="discordWebhook")
    is_sudo: bool = Field(False, alias="isSudo")

    class Config:
        populate_by_name = True


class RemnawaveAdminUpdate(BaseModel):
    """Admin update data"""

    password: Optional[str] = None
    telegram_id: Optional[int] = Field(None, alias="telegramId")
    discord_webhook: Optional[str] = Field(None, alias="discordWebhook")
    is_sudo: Optional[bool] = Field(None, alias="isSudo")

    class Config:
        populate_by_name = True
