from typing import Optional, Dict, List
from pydantic import BaseModel, Field, constr
from .user import MarzbanProxyTypes


class MarzbanUserTemplateCreate(BaseModel):
    """Schema for creating a user template"""

    name: Optional[str] = Field(None, title="Name")
    data_limit: Optional[int] = Field(
        None, title="Data Limit", description="In bytes, 0 or greater", ge=0
    )
    expire_duration: Optional[int] = Field(
        None, title="Expire Duration", description="In seconds, 0 or greater", ge=0
    )
    username_prefix: Optional[constr(min_length=1, max_length=20)] = Field(
        None, title="Username Prefix"
    )
    username_suffix: Optional[constr(min_length=1, max_length=20)] = Field(
        None, title="Username Suffix"
    )
    inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Inbounds"
    )


class MarzbanUserTemplateModify(BaseModel):
    """Schema for modifying a user template"""

    name: Optional[str] = Field(None, title="Name")
    data_limit: Optional[int] = Field(None, title="Data Limit", ge=0)
    expire_duration: Optional[int] = Field(None, title="Expire Duration", ge=0)
    username_prefix: Optional[constr(min_length=1, max_length=20)] = Field(
        None, title="Username Prefix"
    )
    username_suffix: Optional[constr(min_length=1, max_length=20)] = Field(
        None, title="Username Suffix"
    )
    inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Inbounds"
    )


class MarzbanUserTemplateResponse(BaseModel):
    """User template response schema"""

    id: int = Field(..., title="Id")
    name: Optional[str] = Field(None, title="Name")
    data_limit: Optional[int] = Field(None, title="Data Limit", ge=0)
    expire_duration: Optional[int] = Field(None, title="Expire Duration", ge=0)
    username_prefix: Optional[constr(min_length=1, max_length=20)] = Field(
        None, title="Username Prefix"
    )
    username_suffix: Optional[constr(min_length=1, max_length=20)] = Field(
        None, title="Username Suffix"
    )
    inbounds: Dict[MarzbanProxyTypes, List[str]] = Field(
        default_factory=dict, title="Inbounds"
    )
