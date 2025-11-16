from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class PasarGuardUserTemplateCreate(BaseModel):
    """Schema for creating a new user template"""

    name: Optional[str] = Field(None, title="Name")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    expire_duration: Optional[int] = Field(None, title="Expire Duration")
    username_prefix: Optional[str] = Field(None, title="Username Prefix", max_length=20)
    username_suffix: Optional[str] = Field(None, title="Username Suffix", max_length=20)
    group_ids: List[int] = Field(..., title="Group Ids")
    extra_settings: Optional[Dict[str, Any]] = Field(None, title="Extra Settings")
    status: Optional[str] = Field(None, title="Status")
    reset_usages: Optional[bool] = Field(None, title="Reset Usages")
    on_hold_timeout: Optional[int] = Field(None, title="On Hold Timeout")
    data_limit_reset_strategy: str = Field(
        "no_reset", title="Data Limit Reset Strategy"
    )
    is_disabled: Optional[bool] = Field(None, title="Is Disabled")


class PasarGuardUserTemplateModify(BaseModel):
    """Schema for modifying an existing user template"""

    name: Optional[str] = Field(None, title="Name")
    data_limit: Optional[int] = Field(None, title="Data Limit")
    expire_duration: Optional[int] = Field(None, title="Expire Duration")
    username_prefix: Optional[str] = Field(None, title="Username Prefix", max_length=20)
    username_suffix: Optional[str] = Field(None, title="Username Suffix", max_length=20)
    group_ids: Optional[List[int]] = Field(None, title="Group Ids")
    extra_settings: Optional[Dict[str, Any]] = Field(None, title="Extra Settings")
    status: Optional[str] = Field(None, title="Status")
    reset_usages: Optional[bool] = Field(None, title="Reset Usages")
    on_hold_timeout: Optional[int] = Field(None, title="On Hold Timeout")
    data_limit_reset_strategy: str = Field(
        "no_reset", title="Data Limit Reset Strategy"
    )
    is_disabled: Optional[bool] = Field(None, title="Is Disabled")


class PasarGuardUserTemplateResponse(PasarGuardUserTemplateCreate):
    """User template response schema"""

    id: int = Field(..., title="Id")
