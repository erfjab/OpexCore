from typing import Optional, List
from pydantic import BaseModel, Field


class RustneshinServiceCreate(BaseModel):
    """Schema for creating a new service"""

    id: Optional[int] = Field(None, title="ID")
    name: Optional[str] = Field(None, title="Name")
    inbound_ids: List[int] = Field(default_factory=list, title="Inbound IDs")


class RustneshinServiceModify(BaseModel):
    """Schema for modifying an existing service"""

    id: Optional[int] = Field(None, title="ID")
    name: Optional[str] = Field(None, title="Name")
    inbound_ids: Optional[List[int]] = Field(None, title="Inbound IDs")


class RustneshinServiceResponse(BaseModel):
    """Service response schema"""

    id: int = Field(..., title="ID")
    name: Optional[str] = Field(None, title="Name")
    inbound_ids: List[int] = Field(default_factory=list, title="Inbound IDs")
    user_ids: List[int] = Field(default_factory=list, title="User IDs")
    inbound_count: int = Field(0, title="Inbound Count")
    user_count: int = Field(0, title="User Count")


class RustneshinPageServiceResponse(BaseModel):
    """Paginated service response"""

    items: List[RustneshinServiceResponse] = Field(default_factory=list, title="Items")
    total: int = Field(..., title="Total")
    page: int = Field(..., title="Page")
    size: int = Field(..., title="Size")
    pages: int = Field(..., title="Pages")
