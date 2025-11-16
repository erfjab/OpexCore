from typing import Optional, List, Dict, Any
from opexcore.core import RequestBase
from .types import (
    MarzneshinAdminCreate,
    MarzneshinAdminPartialModify,
    MarzneshinAdmin,
    MarzneshinAdminResponse,
    MarzneshinToken,
    MarzneshinNodeCreate,
    MarzneshinNodeModify,
    MarzneshinNodeResponse,
    MarzneshinNodeSettings,
    MarzneshinServiceCreate,
    MarzneshinServiceModify,
    MarzneshinServiceResponse,
    MarzneshinUserCreate,
    MarzneshinUserModify,
    MarzneshinUserResponse,
    MarzneshinUsersSortingOptions,
    MarzneshinUserUsageSeriesResponse,
    MarzneshinInboundHost,
    MarzneshinInboundHostResponse,
    MarzneshinInbound,
    MarzneshinBackendConfig,
    MarzneshinBackendStats,
    MarzneshinSubscriptionSettings,
    MarzneshinTelegramSettings,
    MarzneshinAdminsStats,
    MarzneshinNodesStats,
    MarzneshinUsersStats,
    MarzneshinTrafficUsageSeries,
)


class MarzneshinManager(RequestBase):
    """Marzneshin API Manager with all endpoints"""

    @classmethod
    def _generate_headers(cls, token: Optional[str] = None) -> Dict[str, str]:
        """Generate headers for API requests"""
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    @classmethod
    async def admin_token(
        cls, host: str, username: str, password: str, timeout: int = 10
    ) -> MarzneshinToken:
        """
        Authenticate an admin and issue a token.

        :param host: API host URL
        :param username: Admin username
        :param password: Admin password
        :param timeout: Request timeout in seconds
        :return: Token response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/token",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinToken(**data)

    @classmethod
    async def get_current_admin(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzneshinAdmin:
        """
        Retrieve the current authenticated admin.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/current",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdmin(**data)

    @classmethod
    async def get_admins(
        cls,
        host: str,
        token: str,
        username: Optional[str] = None,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinAdminResponse]:
        """
        Fetch a list of admins with optional filters.

        :param host: API host URL
        :param token: Authentication token
        :param username: Filter by username
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of admin responses
        """
        params = {"page": page, "size": size}
        if username:
            params["username"] = username

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinAdminResponse(**admin) for admin in data.get("items", [])]

    @classmethod
    async def create_admin(
        cls, host: str, token: str, admin_data: MarzneshinAdminCreate, timeout: int = 10
    ) -> MarzneshinAdmin:
        """
        Create a new admin.

        :param host: API host URL
        :param token: Authentication token
        :param admin_data: Admin creation data
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins",
            data=admin_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdmin(**data)

    @classmethod
    async def get_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinAdminResponse:
        """
        Get admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdminResponse(**data)

    @classmethod
    async def modify_admin(
        cls,
        host: str,
        token: str,
        username: str,
        admin_data: MarzneshinAdminPartialModify,
        timeout: int = 10,
    ) -> MarzneshinAdminResponse:
        """
        Modify an existing admin's details.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param admin_data: Admin modification data
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/admins/{username}",
            data=admin_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdminResponse(**data)

    @classmethod
    async def remove_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove an admin from the database.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/admins/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_admin_services(
        cls,
        host: str,
        token: str,
        username: str,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinServiceResponse]:
        """
        Get admin services.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of service responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{username}/services",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [
            MarzneshinServiceResponse(**service) for service in data.get("items", [])
        ]

    @classmethod
    async def get_admin_users(
        cls,
        host: str,
        token: str,
        username: str,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinUserResponse]:
        """
        Get admin users.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of user responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{username}/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinUserResponse(**user) for user in data.get("items", [])]

    @classmethod
    async def disable_admin_users(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinAdminResponse:
        """
        Disable all users of an admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/disable_users",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdminResponse(**data)

    @classmethod
    async def enable_admin_users(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinAdminResponse:
        """
        Enable all users of an admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/enable_users",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdminResponse(**data)

    @classmethod
    async def get_nodes(
        cls,
        host: str,
        token: str,
        status: Optional[List[str]] = None,
        name: Optional[str] = None,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinNodeResponse]:
        """
        Retrieve a list of all nodes.

        :param host: API host URL
        :param token: Authentication token
        :param status: Filter by status
        :param name: Filter by name
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of node responses
        """
        params = {"page": page, "size": size}
        if status:
            params["status"] = status
        if name:
            params["name"] = name

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinNodeResponse(**node) for node in data.get("items", [])]

    @classmethod
    async def add_node(
        cls, host: str, token: str, node_data: MarzneshinNodeCreate, timeout: int = 10
    ) -> MarzneshinNodeResponse:
        """
        Add a new node to the database.

        :param host: API host URL
        :param token: Authentication token
        :param node_data: Node creation data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes",
            data=node_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinNodeResponse(**data)

    @classmethod
    async def get_node_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzneshinNodeSettings:
        """
        Retrieve the current node settings.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Node settings response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/settings",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinNodeSettings(**data)

    @classmethod
    async def get_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> MarzneshinNodeResponse:
        """
        Retrieve details of a specific node by its ID.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinNodeResponse(**data)

    @classmethod
    async def modify_node(
        cls,
        host: str,
        token: str,
        node_id: int,
        node_data: MarzneshinNodeModify,
        timeout: int = 10,
    ) -> MarzneshinNodeResponse:
        """
        Update a node's details.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param node_data: Node modification data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}",
            data=node_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinNodeResponse(**data)

    @classmethod
    async def remove_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def reconnect_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Trigger a reconnection for the specified node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/resync",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_node_usage(
        cls,
        host: str,
        token: str,
        node_id: int,
        start: Optional[str] = None,
        end: Optional[str] = None,
        timeout: int = 10,
    ) -> MarzneshinTrafficUsageSeries:
        """
        Get node usage statistics.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param start: Start date
        :param end: End date
        :param timeout: Request timeout in seconds
        :return: Traffic usage series
        """
        params = {}
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinTrafficUsageSeries(**data)

    @classmethod
    async def get_backend_stats(
        cls, host: str, token: str, node_id: int, backend: str, timeout: int = 10
    ) -> MarzneshinBackendStats:
        """
        Get backend stats for a node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param timeout: Request timeout in seconds
        :return: Backend stats
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/stats",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinBackendStats(**data)

    @classmethod
    async def get_node_backend_config(
        cls, host: str, token: str, node_id: int, backend: str, timeout: int = 10
    ) -> MarzneshinBackendConfig:
        """
        Get node backend configuration.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param timeout: Request timeout in seconds
        :return: Backend config
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/config",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinBackendConfig(**data)

    @classmethod
    async def alter_node_backend_config(
        cls,
        host: str,
        token: str,
        node_id: int,
        backend: str,
        config_data: MarzneshinBackendConfig,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Alter node backend configuration.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param config_data: Backend config data
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/config",
            data=config_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_services(
        cls,
        host: str,
        token: str,
        name: Optional[str] = None,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinServiceResponse]:
        """
        Get all services with optional filters.

        :param host: API host URL
        :param token: Authentication token
        :param name: Filter by name
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of service responses
        """
        params = {"page": page, "size": size}
        if name:
            params["name"] = name

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/services",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [
            MarzneshinServiceResponse(**service) for service in data.get("items", [])
        ]

    @classmethod
    async def add_service(
        cls,
        host: str,
        token: str,
        service_data: MarzneshinServiceCreate,
        timeout: int = 10,
    ) -> MarzneshinServiceResponse:
        """
        Add a new service.

        :param host: API host URL
        :param token: Authentication token
        :param service_data: Service creation data
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/services",
            data=service_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinServiceResponse(**data)

    @classmethod
    async def get_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> MarzneshinServiceResponse:
        """
        Get service information by ID.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/services/{service_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinServiceResponse(**data)

    @classmethod
    async def modify_service(
        cls,
        host: str,
        token: str,
        service_id: int,
        service_data: MarzneshinServiceModify,
        timeout: int = 10,
    ) -> MarzneshinServiceResponse:
        """
        Modify a service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param service_data: Service modification data
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/services/{service_id}",
            data=service_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinServiceResponse(**data)

    @classmethod
    async def remove_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove a service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/services/{service_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_service_users(
        cls,
        host: str,
        token: str,
        service_id: int,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinUserResponse]:
        """
        Get service users.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of user responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/services/{service_id}/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinUserResponse(**user) for user in data.get("items", [])]

    @classmethod
    async def get_service_inbounds(
        cls,
        host: str,
        token: str,
        service_id: int,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinInbound]:
        """
        Get service inbounds.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of inbound responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/services/{service_id}/inbounds",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinInbound(**inbound) for inbound in data.get("items", [])]

    @classmethod
    async def get_inbounds(
        cls,
        host: str,
        token: str,
        tag: Optional[str] = None,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinInbound]:
        """
        Get all inbounds.

        :param host: API host URL
        :param token: Authentication token
        :param tag: Filter by tag
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of inbound responses
        """
        params = {"page": page, "size": size}
        if tag:
            params["tag"] = tag

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinInbound(**inbound) for inbound in data.get("items", [])]

    @classmethod
    async def get_inbound(
        cls, host: str, token: str, inbound_id: int, timeout: int = 10
    ) -> MarzneshinInbound:
        """
        Get a specific inbound.

        :param host: API host URL
        :param token: Authentication token
        :param inbound_id: Inbound ID
        :param timeout: Request timeout in seconds
        :return: Inbound response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/{inbound_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinInbound(**data)

    @classmethod
    async def get_hosts(
        cls, host: str, token: str, page: int = 1, size: int = 50, timeout: int = 10
    ) -> list[MarzneshinInboundHostResponse]:
        """
        Get all hosts.

        :param host: API host URL
        :param token: Authentication token
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of host responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/hosts",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinInboundHostResponse(**host) for host in data.get("items", [])]

    @classmethod
    async def create_unbound_host(
        cls,
        host: str,
        token: str,
        host_data: MarzneshinInboundHost,
        timeout: int = 10,
    ) -> MarzneshinInboundHostResponse:
        """
        Create a host without an inbound.

        :param host: API host URL
        :param token: Authentication token
        :param host_data: Host creation data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/inbounds/hosts",
            data=host_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinInboundHostResponse(**data)

    @classmethod
    async def get_host(
        cls, host: str, token: str, host_id: int, timeout: int = 10
    ) -> MarzneshinInboundHostResponse:
        """
        Get a host.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/hosts/{host_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinInboundHostResponse(**data)

    @classmethod
    async def update_host(
        cls,
        host: str,
        token: str,
        host_id: int,
        host_data: MarzneshinInboundHost,
        timeout: int = 10,
    ) -> MarzneshinInboundHostResponse:
        """
        Update a host.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param host_data: Host update data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/inbounds/hosts/{host_id}",
            data=host_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinInboundHostResponse(**data)

    @classmethod
    async def delete_host(
        cls, host: str, token: str, host_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a host.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/inbounds/hosts/{host_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_inbound_hosts(
        cls,
        host: str,
        token: str,
        inbound_id: int,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinInboundHostResponse]:
        """
        Get hosts of a specific inbound.

        :param host: API host URL
        :param token: Authentication token
        :param inbound_id: Inbound ID
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of host responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/{inbound_id}/hosts",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinInboundHostResponse(**host) for host in data.get("items", [])]

    @classmethod
    async def create_inbound_host(
        cls,
        host: str,
        token: str,
        inbound_id: int,
        host_data: MarzneshinInboundHost,
        timeout: int = 10,
    ) -> MarzneshinInboundHostResponse:
        """
        Add a host to an inbound.

        :param host: API host URL
        :param token: Authentication token
        :param inbound_id: Inbound ID
        :param host_data: Host creation data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/inbounds/{inbound_id}/hosts",
            data=host_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinInboundHostResponse(**data)

    @classmethod
    async def get_users(
        cls,
        host: str,
        token: str,
        username: Optional[List[str]] = None,
        order_by: Optional[MarzneshinUsersSortingOptions] = None,
        descending: bool = False,
        is_active: Optional[bool] = None,
        activated: Optional[bool] = None,
        expired: Optional[bool] = None,
        data_limit_reached: Optional[bool] = None,
        enabled: Optional[bool] = None,
        owner_username: Optional[str] = None,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinUserResponse]:
        """
        Get all users with optional filters.

        :param host: API host URL
        :param token: Authentication token
        :param username: Filter by usernames
        :param order_by: Sort field
        :param descending: Sort in descending order
        :param is_active: Filter by active status
        :param activated: Filter by activated status
        :param expired: Filter by expired status
        :param data_limit_reached: Filter by data limit reached status
        :param enabled: Filter by enabled status
        :param owner_username: Filter by owner username
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of user responses
        """
        params = {"page": page, "size": size, "descending": descending}
        if username:
            params["username"] = username
        if order_by:
            params["order_by"] = order_by.value
        if is_active is not None:
            params["is_active"] = is_active
        if activated is not None:
            params["activated"] = activated
        if expired is not None:
            params["expired"] = expired
        if data_limit_reached is not None:
            params["data_limit_reached"] = data_limit_reached
        if enabled is not None:
            params["enabled"] = enabled
        if owner_username:
            params["owner_username"] = owner_username

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [MarzneshinUserResponse(**user) for user in data.get("items", [])]

    @classmethod
    async def add_user(
        cls, host: str, token: str, user_data: MarzneshinUserCreate, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Add a new user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User creation data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users",
            data=user_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def reset_users_data_usage(
        cls, host: str, token: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Reset all users data usage.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def delete_expired_users(
        cls, host: str, token: str, passed_time: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete expired users.

        :param host: API host URL
        :param token: Authentication token
        :param passed_time: Number of days passed since expiration
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        params = {"passed_time": passed_time}
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/users/expired",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Get user information.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def modify_user(
        cls,
        host: str,
        token: str,
        username: str,
        user_data: MarzneshinUserModify,
        timeout: int = 10,
    ) -> MarzneshinUserResponse:
        """
        Modify an existing user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param user_data: User modification data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/users/{username}",
            data=user_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def remove_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove a user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/users/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_user_services(
        cls,
        host: str,
        token: str,
        username: str,
        page: int = 1,
        size: int = 50,
        timeout: int = 10,
    ) -> list[MarzneshinServiceResponse]:
        """
        Get user services.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of service responses
        """
        params = {"page": page, "size": size}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/{username}/services",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [
            MarzneshinServiceResponse(**service) for service in data.get("items", [])
        ]

    @classmethod
    async def reset_user_data_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Reset user data usage.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{username}/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def enable_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Enable a user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{username}/enable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def disable_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Disable a user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{username}/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def revoke_user_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Revoke user subscription.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/users/{username}/revoke_sub",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def get_user_usage(
        cls,
        host: str,
        token: str,
        username: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        timeout: int = 10,
    ) -> MarzneshinUserUsageSeriesResponse:
        """
        Get user usage statistics.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param start: Start date
        :param end: End date
        :param timeout: Request timeout in seconds
        :return: User usage series response
        """
        params = {}
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/{username}/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserUsageSeriesResponse(**data)

    @classmethod
    async def set_user_owner(
        cls,
        host: str,
        token: str,
        username: str,
        admin_username: str,
        timeout: int = 10,
    ) -> MarzneshinUserResponse:
        """
        Set user owner.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param admin_username: Admin username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        params = {"admin_username": admin_username}
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/users/{username}/set-owner",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def user_subscription(
        cls, host: str, username: str, key: str, user_agent: str = "", timeout: int = 10
    ) -> List[str]:
        """
        Get user subscription.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param user_agent: User agent header
        :param timeout: Request timeout in seconds
        :return: Subscription links
        """
        headers = {}
        if user_agent:
            headers["user-agent"] = user_agent

        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}",
            headers=headers,
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def user_subscription_info(
        cls, host: str, username: str, key: str, timeout: int = 10
    ) -> MarzneshinUserResponse:
        """
        Get user subscription info.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}/info",
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUserResponse(**data)

    @classmethod
    async def user_subscription_usage(
        cls,
        host: str,
        username: str,
        key: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        timeout: int = 10,
    ) -> MarzneshinTrafficUsageSeries:
        """
        Get user subscription usage.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param start: Start date
        :param end: End date
        :param timeout: Request timeout in seconds
        :return: Traffic usage series
        """
        params = {}
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}/usage",
            params=params,
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinTrafficUsageSeries(**data)

    @classmethod
    async def user_subscription_with_client_type(
        cls,
        host: str,
        username: str,
        key: str,
        client_type: str,
        timeout: int = 10,
    ) -> List[str]:
        """
        Get user subscription with specific client type.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param client_type: Client type (sing-box, clash-meta, clash, xray, v2ray, links, wireguard)
        :param timeout: Request timeout in seconds
        :return: Subscription links
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}/{client_type}",
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_subscription_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzneshinSubscriptionSettings:
        """
        Get subscription settings.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Subscription settings
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/settings/subscription",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinSubscriptionSettings(**data)

    @classmethod
    async def update_subscription_settings(
        cls,
        host: str,
        token: str,
        settings_data: MarzneshinSubscriptionSettings,
        timeout: int = 10,
    ) -> MarzneshinSubscriptionSettings:
        """
        Update subscription settings.

        :param host: API host URL
        :param token: Authentication token
        :param settings_data: Subscription settings data
        :param timeout: Request timeout in seconds
        :return: Updated subscription settings
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/system/settings/subscription",
            data=settings_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinSubscriptionSettings(**data)

    @classmethod
    async def get_telegram_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> Optional[MarzneshinTelegramSettings]:
        """
        Get Telegram settings.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Telegram settings or None
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/settings/telegram",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinTelegramSettings(**data) if data else None

    @classmethod
    async def update_telegram_settings(
        cls,
        host: str,
        token: str,
        settings_data: Optional[MarzneshinTelegramSettings],
        timeout: int = 10,
    ) -> Optional[MarzneshinTelegramSettings]:
        """
        Update Telegram settings.

        :param host: API host URL
        :param token: Authentication token
        :param settings_data: Telegram settings data or None to disable
        :param timeout: Request timeout in seconds
        :return: Updated Telegram settings or None
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/system/settings/telegram",
            data=settings_data.dict() if settings_data else None,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinTelegramSettings(**data) if data else None

    @classmethod
    async def get_admins_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzneshinAdminsStats:
        """
        Get admins statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Admins stats
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats/admins",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinAdminsStats(**data)

    @classmethod
    async def get_nodes_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzneshinNodesStats:
        """
        Get nodes statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Nodes stats
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats/nodes",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinNodesStats(**data)

    @classmethod
    async def get_total_traffic_stats(
        cls,
        host: str,
        token: str,
        start: Optional[str] = None,
        end: Optional[str] = None,
        timeout: int = 10,
    ) -> MarzneshinTrafficUsageSeries:
        """
        Get total traffic statistics.

        :param host: API host URL
        :param token: Authentication token
        :param start: Start date
        :param end: End date
        :param timeout: Request timeout in seconds
        :return: Traffic usage series
        """
        params = {}
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats/traffic",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinTrafficUsageSeries(**data)

    @classmethod
    async def get_users_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzneshinUsersStats:
        """
        Get users statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Users stats
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats/users",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return MarzneshinUsersStats(**data)
