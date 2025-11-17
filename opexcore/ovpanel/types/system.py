from typing import Optional, Any
from pydantic import BaseModel, Field


class OVPanelSettings(BaseModel):
    """Panel settings response schema"""

    success: bool = Field(..., title="Success")
    msg: str = Field(..., title="Message")
    data: Optional[Any] = Field(None, title="Data")


class OVPanelServerInfo(BaseModel):
    """Server information response schema"""

    success: bool = Field(..., title="Success")
    msg: str = Field(..., title="Message")
    data: Optional[dict] = Field(None, title="Data")
