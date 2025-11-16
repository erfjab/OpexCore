from typing import Optional, List
from pydantic import BaseModel, Field


class MarzneshinAdminCreate(BaseModel):
    """Schema for creating a new admin"""

    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    password: str = Field(..., title="Password")
    enabled: bool = Field(True, title="Enabled")
    all_services_access: bool = Field(False, title="All Services Access")
    modify_users_access: bool = Field(True, title="Modify Users Access")
    service_ids: List[int] = Field(default_factory=list, title="Service Ids")
    subscription_url_prefix: str = Field("", title="Subscription Url Prefix")


class MarzneshinAdminPartialModify(BaseModel):
    """Schema for modifying an existing admin"""

    username: Optional[str] = Field(None, title="Username")
    is_sudo: Optional[bool] = Field(None, title="Is Sudo")
    password: Optional[str] = Field(None, title="Password")
    enabled: Optional[bool] = Field(None, title="Enabled")
    all_services_access: Optional[bool] = Field(None, title="All Services Access")
    modify_users_access: Optional[bool] = Field(None, title="Modify Users Access")
    service_ids: Optional[List[int]] = Field(None, title="Service Ids")
    subscription_url_prefix: Optional[str] = Field(
        None, title="Subscription Url Prefix"
    )


class MarzneshinAdmin(BaseModel):
    """Admin response schema"""

    id: int = Field(..., title="Id")
    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    enabled: bool = Field(True, title="Enabled")
    all_services_access: bool = Field(False, title="All Services Access")
    modify_users_access: bool = Field(True, title="Modify Users Access")
    service_ids: List[int] = Field(default_factory=list, title="Service Ids")
    subscription_url_prefix: str = Field("", title="Subscription Url Prefix")


class MarzneshinAdminResponse(BaseModel):
    """Admin response with usage data"""

    id: int = Field(..., title="Id")
    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    enabled: bool = Field(True, title="Enabled")
    all_services_access: bool = Field(False, title="All Services Access")
    modify_users_access: bool = Field(True, title="Modify Users Access")
    service_ids: List[int] = Field(default_factory=list, title="Service Ids")
    subscription_url_prefix: str = Field("", title="Subscription Url Prefix")
    users_data_usage: int = Field(..., title="Users Data Usage")


class MarzneshinToken(BaseModel):
    """Authentication token response"""

    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")
