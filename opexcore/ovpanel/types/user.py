from typing import Optional, Any
from datetime import date
from pydantic import BaseModel, Field


class OVPanelCreateUser(BaseModel):
    """Schema for creating a new user"""

    name: str = Field(..., min_length=3, max_length=10, title="Name")
    expiry_date: date = Field(..., title="Expiry Date")


class OVPanelUpdateUser(BaseModel):
    """Schema for updating an existing user"""

    name: str = Field(..., title="Name")
    expiry_date: Optional[date] = Field(None, title="Expiry Date")
    status: bool = Field(True, title="Status")


class OVPanelUser(BaseModel):
    """User response schema"""

    name: str = Field(..., title="Name")
    expiry_date: date = Field(..., title="Expiry Date")
    status: bool = Field(..., title="Status")


class OVPanelResponseModel(BaseModel):
    """Generic response model"""

    success: bool = Field(..., title="Success")
    msg: str = Field(..., title="Message")
    data: Optional[Any] = Field(None, title="Data")
