from typing import Optional, List
from pydantic import BaseModel, Field


class MarzneshinServiceCreate(BaseModel):
    """Schema for creating a new service"""

    name: Optional[str] = Field(None, title="Name")
    inbound_ids: List[int] = Field(default_factory=list, title="Inbound Ids")


class MarzneshinServiceModify(BaseModel):
    """Schema for modifying an existing service"""

    name: Optional[str] = Field(None, title="Name")
    inbound_ids: Optional[List[int]] = Field(None, title="Inbound Ids")


class MarzneshinServiceResponse(BaseModel):
    """Service response schema"""

    id: int = Field(..., title="Id")
    name: Optional[str] = Field(None, title="Name")
    inbound_ids: List[int] = Field(..., title="Inbound Ids")
    user_ids: List[int] = Field(..., title="User Ids")
