from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class GuardNodeCategory(str, Enum):
    """Node category types"""

    MARZBAN = "marzban"
    MARZNESHIN = "marzneshin"


class GuardNodeCreate(BaseModel):
    """Schema for creating a new node"""

    remark: str = Field(..., title="Remark")
    category: GuardNodeCategory = Field(..., title="Category")
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    host: str = Field(..., title="Host")
    offset_link: int = Field(0, title="Offset Link")
    batch_size: int = Field(1, title="Batch Size")
    usage_rate: float = Field(1.0, title="Usage Rate")


class GuardNodeUpdate(BaseModel):
    """Schema for updating an existing node"""

    remark: Optional[str] = Field(None, title="Remark")
    username: Optional[str] = Field(None, title="Username")
    password: Optional[str] = Field(None, title="Password")
    host: Optional[str] = Field(None, title="Host")
    offset_link: Optional[int] = Field(None, title="Offset Link")
    batch_size: Optional[int] = Field(None, title="Batch Size")
    usage_rate: Optional[float] = Field(None, title="Usage Rate")


class GuardNodeResponse(BaseModel):
    """Node response schema"""

    id: int = Field(..., title="Id")
    enabled: bool = Field(..., title="Enabled")
    remark: str = Field(..., title="Remark")
    category: GuardNodeCategory = Field(..., title="Category")
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    host: str = Field(..., title="Host")
    current_usage: int = Field(..., title="Current Usage")
    last_used_at: Optional[datetime] = Field(..., title="Last Used At")
    usage_rate: Optional[float] = Field(None, title="Usage Rate")
    offset_link: int = Field(..., title="Offset Link")
    batch_size: int = Field(..., title="Batch Size")
    created_at: datetime = Field(..., title="Created At")
    updated_at: datetime = Field(..., title="Updated At")


class GuardNodeStatsResponse(BaseModel):
    """Node statistics response"""

    total_nodes: int = Field(..., title="Total Nodes")
    active_nodes: int = Field(..., title="Active Nodes")
    inactive_nodes: int = Field(..., title="Inactive Nodes")
