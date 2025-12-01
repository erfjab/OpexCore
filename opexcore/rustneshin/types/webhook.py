from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class RustneshinCreateSubReq(BaseModel):
    """Create subscription request"""

    is_enabled: Optional[bool] = Field(None, title="Is Enabled")
    subject_id: Optional[int] = Field(None, title="Subject ID")
    subject_type: Optional[str] = Field(None, title="Subject Type")
    topic: Optional[str] = Field(None, title="Topic")


class RustneshinCreateEndpointReq(BaseModel):
    """Create endpoint request"""

    url: str = Field(..., title="URL")
    is_active: Optional[bool] = Field(None, title="Is Active")
    owner_user_id: Optional[int] = Field(None, title="Owner User ID")
    secret: Optional[str] = Field(None, title="Secret")
    subscriptions: Optional[List[RustneshinCreateSubReq]] = Field(
        None, title="Subscriptions"
    )


class RustneshinSubscriptionRes(BaseModel):
    """Subscription response"""

    id: int = Field(..., title="ID")
    endpoint_id: int = Field(..., title="Endpoint ID")
    is_enabled: bool = Field(..., title="Is Enabled")
    created_at: datetime = Field(..., title="Created At")
    subject_id: Optional[int] = Field(None, title="Subject ID")
    subject_type: Optional[str] = Field(None, title="Subject Type")
    topic: Optional[str] = Field(None, title="Topic")


class RustneshinEndpointRes(BaseModel):
    """Endpoint response"""

    id: int = Field(..., title="ID")
    owner_user_id: int = Field(..., title="Owner User ID")
    url: str = Field(..., title="URL")
    is_active: bool = Field(..., title="Is Active")
    created_at: datetime = Field(..., title="Created At")


class RustneshinEndpointCreatedRes(RustneshinEndpointRes):
    """Endpoint created response with secret"""

    secret: str = Field(..., title="Secret")
    subscriptions: List[RustneshinSubscriptionRes] = Field(
        default_factory=list, title="Subscriptions"
    )


class RustneshinEndpointWithSubsRes(RustneshinEndpointRes):
    """Endpoint response with subscriptions"""

    subscriptions: List[RustneshinSubscriptionRes] = Field(
        default_factory=list, title="Subscriptions"
    )


class RustneshinSubUpsertReq(BaseModel):
    """Subscription upsert request"""

    id: Optional[int] = Field(None, title="ID")
    is_enabled: Optional[bool] = Field(None, title="Is Enabled")
    subject_id: Optional[int] = Field(None, title="Subject ID")
    subject_type: Optional[str] = Field(None, title="Subject Type")
    topic: Optional[str] = Field(None, title="Topic")


class RustneshinSubsUpdateReq(BaseModel):
    """Subscriptions update request"""

    items: List[RustneshinSubUpsertReq] = Field(..., title="Items")


class RustneshinUpdateEndpointReq(BaseModel):
    """Update endpoint request"""

    url: Optional[str] = Field(None, title="URL")
    is_active: Optional[bool] = Field(None, title="Is Active")
    secret: Optional[str] = Field(None, title="Secret")
    subscriptions: Optional[RustneshinSubsUpdateReq] = Field(
        None, title="Subscriptions"
    )
