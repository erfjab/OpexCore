from typing import Optional, List, Dict
from enum import Enum
from pydantic import BaseModel, Field


class RustneshinProxyTypes(str, Enum):
    """Proxy types enumeration"""

    VMESS = "vmess"
    VLESS = "vless"
    TROJAN = "trojan"
    SHADOWSOCKS = "shadowsocks"
    SHADOWSOCKS2022 = "shadowsocks2022"
    HYSTERIA2 = "hysteria2"
    WIREGUARD = "wireguard"
    TUIC = "tuic"
    SHADOWTLS = "shadowtls"


class RustneshinInboundHostAlpn(str, Enum):
    """Inbound host ALPN options"""

    H2 = "h2"
    HTTP11 = "http/1.1"
    H2_HTTP11 = "h2,http/1.1"
    H3 = "h3"
    H3_H2 = "h3,h2"
    H3_H2_HTTP11 = "h3,h2,http/1.1"
    NONE = "none"


class RustneshinInboundHostFingerprint(str, Enum):
    """Inbound host fingerprint options"""

    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    IOS = "ios"
    ANDROID = "android"
    EDGE = "edge"
    QQ_360 = "360"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"
    NONE = "none"


class RustneshinInboundHostSecurity(str, Enum):
    """Inbound host security options"""

    INBOUND_DEFAULT = "inbound_default"
    NONE = "none"
    TLS = "tls"


class RustneshinFragmentSettings(BaseModel):
    """Fragment settings"""

    packets: str = Field(..., title="Packets")
    length: str = Field(..., title="Length")
    interval: str = Field(..., title="Interval")


class RustneshinMuxCoolSettings(BaseModel):
    """Mux cool settings"""

    concurrency: Optional[int] = Field(None, title="Concurrency")
    xudp_concurrency: Optional[int] = Field(None, title="XUDP Concurrency")
    xudp_proxy_443: Optional[str] = Field(None, title="XUDP Proxy 443")


class RustneshinSingBoxMuxSettings(BaseModel):
    """Sing-box mux settings"""

    max_connections: Optional[int] = Field(None, title="Max Connections")
    max_streams: Optional[int] = Field(None, title="Max Streams")
    min_streams: Optional[int] = Field(None, title="Min Streams")
    padding: Optional[bool] = Field(None, title="Padding")


class RustneshinMuxSettings(BaseModel):
    """Mux settings"""

    protocol: str = Field(..., title="Protocol")
    mux_cool_settings: Optional[RustneshinMuxCoolSettings] = Field(
        None, title="Mux Cool Settings"
    )
    sing_box_mux_settings: Optional[RustneshinSingBoxMuxSettings] = Field(
        None, title="Sing-box Mux Settings"
    )


class RustneshinXMuxSettings(BaseModel):
    """X-Mux settings"""

    keep_alive_period: Optional[int] = Field(None, title="Keep Alive Period")
    max_concurrency: Optional[str] = Field(None, title="Max Concurrency")
    max_connections: Optional[str] = Field(None, title="Max Connections")
    max_lifetime: Optional[str] = Field(None, title="Max Lifetime")
    max_request_times: Optional[str] = Field(None, title="Max Request Times")
    max_reuse_times: Optional[str] = Field(None, title="Max Reuse Times")


class RustneshinSplitHttpSettings(BaseModel):
    """Split HTTP settings"""

    mode: Optional[str] = Field(None, title="Mode")
    no_grpc_header: Optional[bool] = Field(None, title="No GRPC Header")
    padding_bytes: Optional[str] = Field(None, title="Padding Bytes")
    xmux: Optional[RustneshinXMuxSettings] = Field(None, title="X-Mux Settings")


class RustneshinXrayNoise(BaseModel):
    """Xray noise settings"""

    type: str = Field(..., title="Type")
    packet: str = Field(..., title="Packet")
    delay: str = Field(..., title="Delay")


class RustneshinNode(BaseModel):
    """Node base model"""

    id: Optional[int] = Field(None, title="ID")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient")
    connection_backend: Optional[str] = Field(None, title="Connection Backend")


class RustneshinInbound(BaseModel):
    """Inbound model"""

    id: int = Field(..., title="ID")
    tag: str = Field(..., title="Tag")
    protocol: RustneshinProxyTypes = Field(..., title="Protocol")
    config: str = Field(..., title="Config")
    node: RustneshinNode = Field(..., title="Node")
    service_ids: List[int] = Field(default_factory=list, title="Service IDs")


class RustneshinInboundHost(BaseModel):
    """Inbound host model"""

    remark: str = Field(..., title="Remark")
    address: str = Field(..., title="Address")
    inbound_id: Optional[int] = Field(None, title="Inbound ID")
    port: Optional[int] = Field(None, title="Port")
    sni: Optional[str] = Field(None, title="SNI")
    host: Optional[str] = Field(None, title="Host")
    path: Optional[str] = Field(None, title="Path")
    network: Optional[str] = Field(None, title="Network")
    security: Optional[RustneshinInboundHostSecurity] = Field(None, title="Security")
    alpn: Optional[RustneshinInboundHostAlpn] = Field(None, title="ALPN")
    fingerprint: Optional[RustneshinInboundHostFingerprint] = Field(
        None, title="Fingerprint"
    )
    allowinsecure: Optional[bool] = Field(None, title="Allow Insecure")
    is_disabled: Optional[bool] = Field(None, title="Is Disabled")
    weight: int = Field(1, title="Weight")
    protocol: Optional[RustneshinProxyTypes] = Field(None, title="Protocol")
    fragment: Optional[RustneshinFragmentSettings] = Field(None, title="Fragment")
    mux_settings: Optional[RustneshinMuxSettings] = Field(None, title="Mux Settings")
    splithttp_settings: Optional[RustneshinSplitHttpSettings] = Field(
        None, title="Split HTTP Settings"
    )
    noise: Optional[List[RustneshinXrayNoise]] = Field(None, title="Noise")
    http_headers: Dict[str, str] = Field(default_factory=dict, title="HTTP Headers")
    chain_ids: Optional[List[int]] = Field(None, title="Chain IDs")
    service_ids: Optional[List[int]] = Field(None, title="Service IDs")
    universal: Optional[bool] = Field(None, title="Universal")
    allowed_ips: Optional[str] = Field(None, title="Allowed IPs")
    dns_servers: Optional[str] = Field(None, title="DNS Servers")
    mtu: Optional[int] = Field(None, title="MTU")
    header_type: Optional[str] = Field(None, title="Header Type")
    flow: Optional[str] = Field(None, title="Flow")
    early_data: Optional[int] = Field(None, title="Early Data")
    reality_public_key: Optional[str] = Field(None, title="Reality Public Key")
    reality_short_ids: Optional[List[str]] = Field(None, title="Reality Short IDs")
    password: Optional[str] = Field(None, title="Password")
    uuid: Optional[str] = Field(None, title="UUID")
    shadowsocks_method: Optional[str] = Field(None, title="Shadowsocks Method")
    shadowtls_version: Optional[int] = Field(None, title="Shadow TLS Version")


class RustneshinInboundHostResponse(RustneshinInboundHost):
    """Inbound host response with ID"""

    id: int = Field(..., title="ID")


class RustneshinPageInbound(BaseModel):
    """Paginated inbound response"""

    items: List[RustneshinInbound] = Field(default_factory=list, title="Items")
    total: int = Field(..., title="Total")
    page: int = Field(..., title="Page")
    size: int = Field(..., title="Size")
    pages: int = Field(..., title="Pages")


class RustneshinPageInboundHostResponse(BaseModel):
    """Paginated inbound host response"""

    items: List[RustneshinInboundHostResponse] = Field(
        default_factory=list, title="Items"
    )
    total: int = Field(..., title="Total")
    page: int = Field(..., title="Page")
    size: int = Field(..., title="Size")
    pages: int = Field(..., title="Pages")
