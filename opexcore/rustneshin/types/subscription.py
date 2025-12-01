from enum import Enum


class RustneshinClientType(str, Enum):
    """Client type for subscription"""

    V2RAY = "v2ray"
    LINKS = "links"
    XRAY = "xray"
    SING_BOX = "sing-box"
    WIREGUARD = "wireguard"
    CLASH = "clash"
    CLASH_META = "clash-meta"
