from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class PasarGuardHostCreate(BaseModel):
    """Schema for creating/modifying a host"""

    id: Optional[int] = Field(None, title="Id")
    remark: str = Field(..., title="Remark")
    address: List[str] = Field(..., title="Address")
    inbound_tag: Optional[str] = Field(None, title="Inbound Tag")
    port: Optional[int] = Field(None, title="Port")
    sni: Optional[List[str]] = Field(None, title="Sni")
    host: Optional[List[str]] = Field(None, title="Host")
    path: Optional[str] = Field(None, title="Path")
    security: str = Field("inbound_default", title="Security")
    alpn: Optional[List[str]] = Field(None, title="Alpn")
    fingerprint: str = Field("", title="Fingerprint")
    allowinsecure: Optional[bool] = Field(None, title="Allowinsecure")
    is_disabled: bool = Field(False, title="Is Disabled")
    http_headers: Optional[Dict[str, str]] = Field(None, title="Http Headers")
    transport_settings: Optional[Dict[str, Any]] = Field(
        None, title="Transport Settings"
    )
    mux_settings: Optional[Dict[str, Any]] = Field(None, title="Mux Settings")
    fragment_settings: Optional[Dict[str, Any]] = Field(None, title="Fragment Settings")
    noise_settings: Optional[Dict[str, Any]] = Field(None, title="Noise Settings")
    random_user_agent: bool = Field(False, title="Random User Agent")
    use_sni_as_host: bool = Field(False, title="Use Sni As Host")
    priority: int = Field(..., title="Priority")
    status: Optional[List[str]] = Field(None, title="Status")
    ech_config_list: Optional[str] = Field(None, title="Ech Config List")


class PasarGuardHostResponse(PasarGuardHostCreate):
    """Host response schema"""

    pass
