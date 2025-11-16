from typing import List, Optional
from pydantic import BaseModel, Field


class GuardServiceCreate(BaseModel):
    """Schema for creating a new service"""

    remark: str = Field(..., title="Remark")
    node_ids: List[int] = Field(..., title="Node Ids")


class GuardServiceUpdate(BaseModel):
    """Schema for updating an existing service"""

    remark: Optional[str] = Field(None, title="Remark")
    node_ids: Optional[List[int]] = Field(None, title="Node Ids")


class GuardServiceResponse(BaseModel):
    """Service response schema"""

    id: int = Field(..., title="Id")
    remark: str = Field(..., title="Remark")
    node_ids: List[int] = Field(..., title="Node Ids")
