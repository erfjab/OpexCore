from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from datetime import datetime


class PasarGuardCoreCreate(BaseModel):
    """Schema for creating a new core config"""

    name: Optional[str] = Field(None, title="Name")
    config: Dict[str, Any] = Field(..., title="Config")
    exclude_inbound_tags: Optional[List[str]] = Field(
        None, title="Exclude Inbound Tags"
    )
    fallbacks_inbound_tags: Optional[List[str]] = Field(
        None, title="Fallbacks Inbound Tags"
    )


class PasarGuardCoreResponse(BaseModel):
    """Core response schema"""

    id: int = Field(..., title="Id")
    name: str = Field(..., title="Name")
    config: Dict[str, Any] = Field(..., title="Config")
    exclude_inbound_tags: List[str] = Field(..., title="Exclude Inbound Tags")
    fallbacks_inbound_tags: List[str] = Field(..., title="Fallbacks Inbound Tags")
    created_at: datetime = Field(..., title="Created At")
