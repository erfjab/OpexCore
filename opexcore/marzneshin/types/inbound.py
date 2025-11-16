from typing import Optional, List, Dict
from enum import Enum
from pydantic import BaseModel, Field


class MarzneshinProxyTypes(str, Enum):
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


class MarzneshinProxyHostALPN(str, Enum):
    """Proxy host ALPN enumeration"""

    NONE = "none"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H2_HTTP_1_1 = "h2,http/1.1"
    H3 = "h3"
    H3_H2 = "h3,h2"
    H3_H2_HTTP_1_1 = "h3,h2,http/1.1"


class MarzneshinProxyHostFingerprint(str, Enum):
    """Proxy host fingerprint enumeration"""

    EMPTY = ""
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    IOS = "ios"
    ANDROID = "android"
    EDGE = "edge"
    T360 = "360"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"


class MarzneshinInboundHostSecurity(str, Enum):
    """Inbound host security enumeration"""

    INBOUND_DEFAULT = "inbound_default"
    NONE = "none"
    TLS = "tls"


class MarzneshinFragmentSettings(BaseModel):
    """Fragment settings"""

    packets: str = Field(..., pattern=r"^(:?tlshello|[\d-]{1,32})$", title="Packets")
    length: str = Field(..., pattern=r"^[\d-]{1,32}$", title="Length")
    interval: str = Field(..., pattern=r"^[\d-]{1,32}$", title="Interval")


class MarzneshinXrayNoise(BaseModel):
    """Xray noise settings"""

    type: str = Field(..., pattern=r"^(:?rand|str|base64)$", title="Type")
    packet: str = Field(..., title="Packet")
    delay: str = Field(..., pattern=r"^\d{1,10}(-\d{1,10})?$", title="Delay")


class MarzneshinXMuxSettings(BaseModel):
    """XMux settings"""

    max_concurrency: Optional[str] = Field(
        None, pattern=r"^\d{1,10}(-\d{1,10})?$", title="Max Concurrency"
    )
    max_connections: Optional[str] = Field(
        None, pattern=r"^\d{1,10}(-\d{1,10})?$", title="Max Connections"
    )
    max_reuse_times: Optional[str] = Field(
        None, pattern=r"^\d{1,10}(-\d{1,10})?$", title="Max Reuse Times"
    )
    max_lifetime: Optional[str] = Field(
        None, pattern=r"^\d{1,10}(-\d{1,10})?$", title="Max Lifetime"
    )
    max_request_times: Optional[str] = Field(None, title="Max Request Times")
    keep_alive_period: Optional[int] = Field(None, title="Keep Alive Period")


class MarzneshinSplitHttpSettings(BaseModel):
    """Split HTTP settings"""

    mode: Optional[str] = Field(None, title="Mode")
    no_grpc_header: Optional[bool] = Field(None, title="No Grpc Header")
    padding_bytes: Optional[str] = Field(None, title="Padding Bytes")
    xmux: Optional[MarzneshinXMuxSettings] = Field(None, title="XMux")


class MarzneshinSingBoxMuxSettings(BaseModel):
    """Sing-Box mux settings"""

    max_connections: Optional[int] = Field(None, title="Max Connections")
    max_streams: Optional[int] = Field(None, title="Max Streams")
    min_streams: Optional[int] = Field(None, title="Min Streams")
    padding: Optional[bool] = Field(None, title="Padding")


class MarzneshinMuxCoolSettings(BaseModel):
    """Mux cool settings"""

    concurrency: Optional[int] = Field(None, title="Concurrency")
    xudp_concurrency: Optional[int] = Field(None, title="Xudp Concurrency")
    xudp_proxy_443: Optional[str] = Field(None, title="Xudp Proxy 443")


class MarzneshinMuxSettings(BaseModel):
    """Mux settings"""

    protocol: str = Field(..., title="Protocol")
    sing_box_mux_settings: Optional[MarzneshinSingBoxMuxSettings] = Field(
        None, title="Sing Box Mux Settings"
    )
    mux_cool_settings: Optional[MarzneshinMuxCoolSettings] = Field(
        None, title="Mux Cool Settings"
    )


class MarzneshinInboundHost(BaseModel):
    """Inbound host"""

    remark: str = Field(..., title="Remark")
    address: str = Field(..., title="Address")
    uuid: Optional[str] = Field(None, title="Uuid")
    password: Optional[str] = Field(None, title="Password")
    protocol: Optional[MarzneshinProxyTypes] = Field(None, title="Protocol")
    network: Optional[str] = Field(None, title="Network")
    port: Optional[int] = Field(None, title="Port")
    sni: Optional[str] = Field(None, title="Sni")
    host: Optional[str] = Field(None, title="Host")
    path: Optional[str] = Field(None, title="Path")
    security: MarzneshinInboundHostSecurity = Field(
        MarzneshinInboundHostSecurity.INBOUND_DEFAULT, title="Security"
    )
    alpn: MarzneshinProxyHostALPN = Field(MarzneshinProxyHostALPN.NONE, title="Alpn")
    fingerprint: MarzneshinProxyHostFingerprint = Field(
        MarzneshinProxyHostFingerprint.EMPTY, title="Fingerprint"
    )
    allowinsecure: Optional[bool] = Field(False, title="Allowinsecure")
    is_disabled: Optional[bool] = Field(False, title="Is Disabled")
    fragment: Optional[MarzneshinFragmentSettings] = Field(None, title="Fragment")
    noise: Optional[List[MarzneshinXrayNoise]] = Field(None, title="Noise")
    http_headers: Optional[Dict[str, str]] = Field(None, title="Http Headers")
    mtu: Optional[int] = Field(None, title="Mtu")
    dns_servers: Optional[str] = Field(None, title="Dns Servers")
    allowed_ips: Optional[str] = Field(None, title="Allowed Ips")
    header_type: Optional[str] = Field(None, title="Header Type")
    reality_public_key: Optional[str] = Field(None, title="Reality Public Key")
    reality_short_ids: Optional[List[str]] = Field(None, title="Reality Short Ids")
    flow: Optional[str] = Field(None, title="Flow")
    shadowtls_version: Optional[int] = Field(None, title="Shadowtls Version")
    shadowsocks_method: Optional[str] = Field(None, title="Shadowsocks Method")
    splithttp_settings: Optional[MarzneshinSplitHttpSettings] = Field(
        None, title="Splithttp Settings"
    )
    early_data: Optional[int] = Field(None, title="Early Data")
    mux_settings: Optional[MarzneshinMuxSettings] = Field(None, title="Mux Settings")
    universal: bool = Field(False, title="Universal")
    service_ids: List[int] = Field(default_factory=list, title="Service Ids")
    weight: int = Field(1, title="Weight")
    inbound_id: Optional[int] = Field(None, title="Inbound Id")
    chain_ids: List[int] = Field(default_factory=list, title="Chain Ids")


class MarzneshinInboundHostResponse(MarzneshinInboundHost):
    """Inbound host response"""

    id: int = Field(..., title="Id")


class MarzneshinNode(BaseModel):
    """Node information"""

    id: int = Field(..., title="Id")
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(53042, title="Port")
    connection_backend: str = Field("grpclib", title="Connection Backend")
    usage_coefficient: float = Field(1.0, title="Usage Coefficient")


class MarzneshinInbound(BaseModel):
    """Inbound"""

    id: int = Field(..., title="Id")
    tag: str = Field(..., title="Tag")
    protocol: MarzneshinProxyTypes = Field(..., title="Protocol")
    config: str = Field(..., title="Config")
    node: MarzneshinNode = Field(..., title="Node")
    service_ids: List[int] = Field(..., title="Service Ids")


class MarzneshinBackendConfigFormat(int, Enum):
    """Backend config format enumeration"""

    JSON = 0
    YAML = 1
    TOML = 2


class MarzneshinBackendConfig(BaseModel):
    """Backend config"""

    config: str = Field(..., title="Config")
    format: MarzneshinBackendConfigFormat = Field(..., title="Format")


class MarzneshinBackendStats(BaseModel):
    """Backend stats"""

    running: bool = Field(..., title="Running")
