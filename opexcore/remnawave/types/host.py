from typing import Optional
from pydantic import BaseModel, Field


class RemnawaveHost(BaseModel):
    """Host response"""

    uuid: str
    remark: str
    address: str
    port: int
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[str] = None
    fingerprint: Optional[str] = None
    is_disabled: bool = Field(False, alias="isDisabled")
    is_hidden: bool = Field(False, alias="isHidden")
    tag: Optional[str] = None
    view_position: int = Field(..., alias="viewPosition")
    created_at: str = Field(..., alias="createdAt")
    updated_at: str = Field(..., alias="updatedAt")

    class Config:
        populate_by_name = True


class RemnawaveHostCreate(BaseModel):
    """Host creation data"""

    remark: str = Field(..., min_length=1, max_length=40)
    address: str
    port: int = Field(..., ge=1, le=65535)
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[str] = None
    fingerprint: Optional[str] = None
    is_hidden: bool = Field(False, alias="isHidden")
    tag: Optional[str] = Field(None, max_length=32)

    class Config:
        populate_by_name = True


class RemnawaveHostUpdate(BaseModel):
    """Host update data"""

    remark: Optional[str] = Field(None, max_length=40)
    address: Optional[str] = None
    port: Optional[int] = Field(None, ge=1, le=65535)
    path: Optional[str] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    alpn: Optional[str] = None
    fingerprint: Optional[str] = None
    is_hidden: Optional[bool] = Field(None, alias="isHidden")
    tag: Optional[str] = Field(None, max_length=32)

    class Config:
        populate_by_name = True
