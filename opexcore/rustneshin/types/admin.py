from typing import Optional, List
from pydantic import BaseModel, Field


class RustneshinAdminCreate(BaseModel):
    """Schema for creating a new admin"""

    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    is_sudo: Optional[bool] = Field(None, title="Is Sudo")
    enabled: Optional[bool] = Field(None, title="Enabled")
    all_services_access: Optional[bool] = Field(None, title="All Services Access")
    modify_users_access: Optional[bool] = Field(None, title="Modify Users Access")
    service_ids: Optional[List[int]] = Field(None, title="Service IDs")
    subscription_url_prefix: Optional[str] = Field(
        None, title="Subscription URL Prefix"
    )


class RustneshinAdminModify(BaseModel):
    """Schema for modifying an existing admin"""

    username: Optional[str] = Field(None, title="Username")
    password: Optional[str] = Field(None, title="Password")
    is_sudo: Optional[bool] = Field(None, title="Is Sudo")
    enabled: Optional[bool] = Field(None, title="Enabled")
    all_services_access: Optional[bool] = Field(None, title="All Services Access")
    modify_users_access: Optional[bool] = Field(None, title="Modify Users Access")
    service_ids: Optional[List[int]] = Field(None, title="Service IDs")
    subscription_url_prefix: Optional[str] = Field(
        None, title="Subscription URL Prefix"
    )


class RustneshinAdminResponse(BaseModel):
    """Admin response schema"""

    id: int = Field(..., title="ID")
    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    enabled: bool = Field(..., title="Enabled")
    all_services_access: bool = Field(..., title="All Services Access")
    modify_users_access: bool = Field(..., title="Modify Users Access")
    service_ids: List[int] = Field(default_factory=list, title="Service IDs")
    subscription_url_prefix: str = Field(..., title="Subscription URL Prefix")
    users_data_usage: int = Field(..., title="Users Data Usage")
    subscription_count: int = Field(..., title="Subscription Count")
    lifetime_subscription_count: int = Field(..., title="Lifetime Subscription Count")


class RustneshinToken(BaseModel):
    """Authentication token response"""

    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")
    is_sudo: bool = Field(..., title="Is Sudo")


class RustneshinAdminsStats(BaseModel):
    """Admin statistics"""

    total: int = Field(..., title="Total")


class RustneshinPageAdminResponse(BaseModel):
    """Paginated admin response"""

    items: List[RustneshinAdminResponse] = Field(default_factory=list, title="Items")
    total: int = Field(..., title="Total")
    page: int = Field(..., title="Page")
    size: int = Field(..., title="Size")
    pages: int = Field(..., title="Pages")
