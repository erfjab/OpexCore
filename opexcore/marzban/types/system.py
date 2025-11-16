from enum import Enum
from pydantic import BaseModel, Field


class MarzbanSystemStats(BaseModel):
    """System statistics schema"""

    version: str = Field(..., title="Version")
    mem_total: int = Field(..., title="Mem Total")
    mem_used: int = Field(..., title="Mem Used")
    cpu_cores: int = Field(..., title="Cpu Cores")
    cpu_usage: float = Field(..., title="Cpu Usage")
    total_user: int = Field(..., title="Total User")
    online_users: int = Field(..., title="Online Users")
    users_active: int = Field(..., title="Users Active")
    users_on_hold: int = Field(..., title="Users On Hold")
    users_disabled: int = Field(..., title="Users Disabled")
    users_expired: int = Field(..., title="Users Expired")
    users_limited: int = Field(..., title="Users Limited")
    incoming_bandwidth: int = Field(..., title="Incoming Bandwidth")
    outgoing_bandwidth: int = Field(..., title="Outgoing Bandwidth")
    incoming_bandwidth_speed: int = Field(..., title="Incoming Bandwidth Speed")
    outgoing_bandwidth_speed: int = Field(..., title="Outgoing Bandwidth Speed")


class MarzbanProxyTypes(str, Enum):
    """Proxy types enumeration"""

    VMESS = "vmess"
    VLESS = "vless"
    TROJAN = "trojan"
    SHADOWSOCKS = "shadowsocks"


class MarzbanProxyInbound(BaseModel):
    """Proxy inbound configuration schema"""

    tag: str = Field(..., title="Tag")
    protocol: MarzbanProxyTypes = Field(..., title="Protocol")
    network: str = Field(..., title="Network")
    tls: str = Field(..., title="Tls")
    port: int | str = Field(..., title="Port")


class MarzbanProxyHostSecurity(str, Enum):
    """Proxy host security types"""

    INBOUND_DEFAULT = "inbound_default"
    NONE = "none"
    TLS = "tls"


class MarzbanProxyHostALPN(str, Enum):
    """Proxy host ALPN types"""

    EMPTY = ""
    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H3_H2_HTTP_1_1 = "h3,h2,http/1.1"
    H3_H2 = "h3,h2"
    H2_HTTP_1_1 = "h2,http/1.1"


class MarzbanProxyHostFingerprint(str, Enum):
    """Proxy host fingerprint types"""

    EMPTY = ""
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    IOS = "ios"
    ANDROID = "android"
    EDGE = "edge"
    BROWSER_360 = "360"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"


class MarzbanProxyHost(BaseModel):
    """Proxy host configuration schema"""

    remark: str = Field(..., title="Remark")
    address: str = Field(..., title="Address")
    port: int | None = Field(None, title="Port")
    sni: str | None = Field(None, title="Sni")
    host: str | None = Field(None, title="Host")
    path: str | None = Field(None, title="Path")
    security: MarzbanProxyHostSecurity = Field(
        MarzbanProxyHostSecurity.INBOUND_DEFAULT, title="Security"
    )
    alpn: MarzbanProxyHostALPN = Field(MarzbanProxyHostALPN.EMPTY, title="Alpn")
    fingerprint: MarzbanProxyHostFingerprint = Field(
        MarzbanProxyHostFingerprint.EMPTY, title="Fingerprint"
    )
    allowinsecure: bool | None = Field(None, title="Allowinsecure")
    is_disabled: bool | None = Field(None, title="Is Disabled")
    mux_enable: bool | None = Field(None, title="Mux Enable")
    fragment_setting: str | None = Field(None, title="Fragment Setting")
    noise_setting: str | None = Field(None, title="Noise Setting")
    random_user_agent: bool | None = Field(None, title="Random User Agent")
    use_sni_as_host: bool | None = Field(None, title="Use Sni As Host")
