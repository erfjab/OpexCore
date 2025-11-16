from typing import Optional, List
from pydantic import BaseModel, Field


class PasarGuardGroupCreate(BaseModel):
    """Schema for creating a new group"""

    name: str = Field(..., title="Name", min_length=3, max_length=64)
    inbound_tags: List[str] = Field(..., title="Inbound Tags")
    is_disabled: bool = Field(False, title="Is Disabled")


class PasarGuardGroupModify(BaseModel):
    """Schema for modifying an existing group"""

    name: str = Field(..., title="Name", min_length=3, max_length=64)
    inbound_tags: Optional[List[str]] = Field([], title="Inbound Tags")
    is_disabled: bool = Field(False, title="Is Disabled")


class PasarGuardGroupResponse(BaseModel):
    """Group response schema"""

    id: int = Field(..., title="Id")
    name: str = Field(..., title="Name", min_length=3, max_length=64)
    inbound_tags: Optional[List[str]] = Field([], title="Inbound Tags")
    is_disabled: bool = Field(False, title="Is Disabled")
    total_users: int = Field(0, title="Total Users")
