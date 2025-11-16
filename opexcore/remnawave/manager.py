from typing import Optional, List, Dict, Any
from opexcore.core import RequestBase
from .types import (
    RemnawaveToken,
    RemnawaveUser,
    RemnawaveUserCreate,
    RemnawaveUserUpdate,
    RemnawaveNode,
    RemnawaveNodeCreate,
    RemnawaveNodeUpdate,
    RemnawaveHost,
    RemnawaveHostCreate,
    RemnawaveHostUpdate,
    RemnawaveSubscription,
    RemnawaveSystemStats,
)


class RemnawaveManager(RequestBase):
    """Remnawave API Manager with all endpoints"""

    @classmethod
    def _generate_headers(cls, token: Optional[str] = None) -> Dict[str, str]:
        """Generate headers for API requests"""
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    @classmethod
    async def admin_login(
        cls, host: str, username: str, password: str, timeout: int = 10
    ) -> RemnawaveToken:
        """
        Login as admin and receive access token.

        :param host: API host URL
        :param username: Admin username
        :param password: Admin password
        :param timeout: Request timeout in seconds
        :return: Token response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/auth/login",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/json"},
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveToken(**data.get("response", data))

    @classmethod
    async def admin_register(
        cls, host: str, username: str, password: str, timeout: int = 10
    ) -> RemnawaveToken:
        """
        Register as superadmin.

        :param host: API host URL
        :param username: Admin username
        :param password: Admin password
        :param timeout: Request timeout in seconds
        :return: Token response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/auth/register",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/json"},
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveToken(**data.get("response", data))

    @classmethod
    async def create_user(
        cls, host: str, token: str, user_data: RemnawaveUserCreate, timeout: int = 10
    ) -> RemnawaveUser:
        """
        Create a new user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User creation data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users",
            data=user_data.dict(by_alias=True, exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def get_users(
        cls,
        host: str,
        token: str,
        size: int = 25,
        start: int = 0,
        sort: Optional[str] = None,
        timeout: int = 10,
    ) -> List[RemnawaveUser]:
        """
        Get all users with pagination.

        :param host: API host URL
        :param token: Authentication token
        :param size: Number of users to return
        :param start: Start index (offset)
        :param sort: Sort field
        :param timeout: Request timeout in seconds
        :return: List of users
        """
        params = {"size": size, "start": start}
        if sort:
            params["sort"] = sort

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        users_data = data.get("response", {}).get("users", [])
        return [RemnawaveUser(**user) for user in users_data]

    @classmethod
    async def get_user(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveUser:
        """
        Get user by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/{uuid}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def update_user(
        cls,
        host: str,
        token: str,
        uuid: str,
        user_data: RemnawaveUserUpdate,
        timeout: int = 10,
    ) -> RemnawaveUser:
        """
        Update user by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param user_data: User update data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/users/{uuid}",
            data=user_data.dict(by_alias=True, exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def delete_user(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete user by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/users/{uuid}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def disable_user(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveUser:
        """
        Disable a user.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{uuid}/actions/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def enable_user(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveUser:
        """
        Enable a user.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{uuid}/actions/enable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def reset_user_traffic(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveUser:
        """
        Reset user traffic.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{uuid}/actions/reset-traffic",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def revoke_user_subscription(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveUser:
        """
        Revoke user subscription.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: User UUID
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{uuid}/actions/revoke",
            headers=cls._generate_headers(token),
            timeout=timeout,
            data={},
        )
        data = await response.json()
        return RemnawaveUser(**data.get("response", data))

    @classmethod
    async def get_nodes(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[RemnawaveNode]:
        """
        Get all nodes.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of nodes
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        nodes_data = data.get("response", [])
        return [RemnawaveNode(**node) for node in nodes_data]

    @classmethod
    async def create_node(
        cls, host: str, token: str, node_data: RemnawaveNodeCreate, timeout: int = 10
    ) -> RemnawaveNode:
        """
        Create a new node.

        :param host: API host URL
        :param token: Authentication token
        :param node_data: Node creation data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes",
            data=node_data.dict(by_alias=True, exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveNode(**data.get("response", data))

    @classmethod
    async def get_node(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveNode:
        """
        Get node by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveNode(**data.get("response", data))

    @classmethod
    async def update_node(
        cls,
        host: str,
        token: str,
        uuid: str,
        node_data: RemnawaveNodeUpdate,
        timeout: int = 10,
    ) -> RemnawaveNode:
        """
        Update node by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param node_data: Node update data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}",
            data=node_data.dict(by_alias=True, exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveNode(**data.get("response", data))

    @classmethod
    async def delete_node(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a node.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def enable_node(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveNode:
        """
        Enable a node.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}/actions/enable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveNode(**data.get("response", data))

    @classmethod
    async def disable_node(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveNode:
        """
        Disable a node.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}/actions/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveNode(**data.get("response", data))

    @classmethod
    async def restart_node(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Restart node.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}/actions/restart",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def reset_node_traffic(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Reset node traffic.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Node UUID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{uuid}/actions/reset-traffic",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_hosts(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[RemnawaveHost]:
        """
        Get all hosts.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of hosts
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/hosts",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        hosts_data = data.get("response", [])
        return [RemnawaveHost(**host_data) for host_data in hosts_data]

    @classmethod
    async def create_host(
        cls, host: str, token: str, host_data: RemnawaveHostCreate, timeout: int = 10
    ) -> RemnawaveHost:
        """
        Create a new host.

        :param host: API host URL
        :param token: Authentication token
        :param host_data: Host creation data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/hosts",
            data=host_data.dict(by_alias=True, exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveHost(**data.get("response", data))

    @classmethod
    async def get_host(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> RemnawaveHost:
        """
        Get a host by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Host UUID
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/hosts/{uuid}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveHost(**data.get("response", data))

    @classmethod
    async def update_host(
        cls,
        host: str,
        token: str,
        uuid: str,
        host_data: RemnawaveHostUpdate,
        timeout: int = 10,
    ) -> RemnawaveHost:
        """
        Update a host by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Host UUID
        :param host_data: Host update data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/hosts/{uuid}",
            data=host_data.dict(by_alias=True, exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveHost(**data.get("response", data))

    @classmethod
    async def delete_host(
        cls, host: str, token: str, uuid: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a host by UUID.

        :param host: API host URL
        :param token: Authentication token
        :param uuid: Host UUID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/hosts/{uuid}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_subscription_info(
        cls, host: str, short_uuid: str, timeout: int = 10
    ) -> RemnawaveSubscription:
        """
        Get subscription info by short UUID (public endpoint).

        :param host: API host URL
        :param short_uuid: Short UUID of the user
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/sub/{short_uuid}/info",
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveSubscription(**data.get("response", data))

    @classmethod
    async def get_subscription_links(
        cls, host: str, short_uuid: str, client_type: str = "", timeout: int = 10
    ) -> str:
        """
        Get subscription links by short UUID and client type.

        :param host: API host URL
        :param short_uuid: Short UUID of the user
        :param client_type: Client type (stash, singbox, mihomo, json, v2ray-json, clash)
        :param timeout: Request timeout in seconds
        :return: Subscription content
        """
        if client_type:
            url = f"{host.rstrip('/')}/api/sub/{short_uuid}/{client_type}"
        else:
            url = f"{host.rstrip('/')}/api/sub/{short_uuid}"

        response = await cls.get(url=url, timeout=timeout)
        return await response.text()

    @classmethod
    async def get_system_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> RemnawaveSystemStats:
        """
        Get system statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: System stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return RemnawaveSystemStats(**data.get("response", data))
