from typing import Optional, List, Dict, Any
from datetime import datetime
from opexcore.core import RequestBase
from .types import (
    RustneshinToken,
    RustneshinAdminCreate,
    RustneshinAdminModify,
    RustneshinAdminResponse,
    RustneshinAdminsStats,
    RustneshinPageAdminResponse,
    RustneshinInbound,
    RustneshinInboundHost,
    RustneshinInboundHostResponse,
    RustneshinPageInbound,
    RustneshinPageInboundHostResponse,
    RustneshinNodeCreate,
    RustneshinNodeModify,
    RustneshinNodeResponse,
    RustneshinNodeSettings,
    RustneshinPageNodeResponse,
    RustneshinBackendConfig,
    RustneshinServiceCreate,
    RustneshinServiceModify,
    RustneshinServiceResponse,
    RustneshinPageServiceResponse,
    RustneshinUserCreate,
    RustneshinUserModify,
    RustneshinUserResponse,
    RustneshinPageUserResponse,
    RustneshinUserUsageSeriesResponse,
    RustneshinNodesStats,
    RustneshinUsersStats,
    RustneshinTrafficUsageSeries,
    RustneshinSubscriptionSettings,
    RustneshinTemplateSettings,
    RustneshinGranularity,
    RustneshinClientType,
    RustneshinCreateEndpointReq,
    RustneshinUpdateEndpointReq,
    RustneshinEndpointRes,
    RustneshinEndpointCreatedRes,
    RustneshinEndpointWithSubsRes,
)


class RustneshinManager(RequestBase):
    """Rustneshin API Manager with all endpoints"""

    @classmethod
    def _generate_headers(cls, token: Optional[str] = None) -> Dict[str, str]:
        """Generate headers for API requests"""
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    # ==================== Admin Endpoints ====================

    @classmethod
    async def admin_token(
        cls, host: str, username: str, password: str, timeout: int = 10
    ) -> RustneshinToken:
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
        return RustneshinToken(**response)

    @classmethod
    async def get_current_admin(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinAdminResponse:
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
        return RustneshinAdminResponse(**response)

    @classmethod
    async def get_admins(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinPageAdminResponse:
        """
        Fetch a list of admins.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Paginated admin response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageAdminResponse(**response)

    @classmethod
    async def create_admin(
        cls, host: str, token: str, admin_data: RustneshinAdminCreate, timeout: int = 10
    ) -> RustneshinAdminResponse:
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
            data=admin_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinAdminResponse(**response)

    @classmethod
    async def get_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinAdminResponse:
        """
        Retrieve a specific admin by username.

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
        return RustneshinAdminResponse(**response)

    @classmethod
    async def update_admin(
        cls,
        host: str,
        token: str,
        username: str,
        admin_data: RustneshinAdminModify,
        timeout: int = 10,
    ) -> RustneshinAdminResponse:
        """
        Update an existing admin's details.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param admin_data: Admin modification data
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/admins/{username}",
            data=admin_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinAdminResponse(**response)

    @classmethod
    async def delete_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete an admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/admins/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_admin_service_ids(
        cls, host: str, token: str, admin_id: str, timeout: int = 10
    ) -> List[int]:
        """
        Fetch service IDs for an admin.

        :param host: API host URL
        :param token: Authentication token
        :param admin_id: Admin ID
        :param timeout: Request timeout in seconds
        :return: List of service IDs
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{admin_id}/service_ids",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_admin_usage(
        cls,
        host: str,
        token: str,
        username: str,
        start: datetime,
        end: datetime,
        granularity: Optional[RustneshinGranularity] = None,
        timeout: int = 10,
    ) -> RustneshinTrafficUsageSeries:
        """
        Get traffic usage statistics for an admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param start: Start datetime
        :param end: End datetime
        :param granularity: Granularity level
        :param timeout: Request timeout in seconds
        :return: Traffic usage series
        """
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
        }
        if granularity:
            params["granularity"] = granularity.value

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{username}/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinTrafficUsageSeries(**response)

    # ==================== Inbound Endpoints ====================

    @classmethod
    async def get_inbounds(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinPageInbound:
        """
        Retrieve all inbounds.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Paginated inbound response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageInbound(**response)

    @classmethod
    async def get_inbound(
        cls, host: str, token: str, inbound_id: int, timeout: int = 10
    ) -> RustneshinInbound:
        """
        Retrieve a specific inbound by ID.

        :param host: API host URL
        :param token: Authentication token
        :param inbound_id: Inbound ID
        :param timeout: Request timeout in seconds
        :return: Inbound
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/{inbound_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinInbound(**response)

    @classmethod
    async def get_hosts(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinPageInboundHostResponse:
        """
        Retrieve all inbound hosts.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Paginated inbound host response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/hosts",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageInboundHostResponse(**response)

    @classmethod
    async def get_host(
        cls, host: str, token: str, host_id: int, timeout: int = 10
    ) -> RustneshinInboundHostResponse:
        """
        Retrieve a specific host by ID.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param timeout: Request timeout in seconds
        :return: Inbound host response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/hosts/{host_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinInboundHostResponse(**response)

    @classmethod
    async def update_host(
        cls,
        host: str,
        token: str,
        host_id: int,
        host_data: RustneshinInboundHost,
        timeout: int = 10,
    ) -> RustneshinInboundHostResponse:
        """
        Update a host by ID.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param host_data: Host data
        :param timeout: Request timeout in seconds
        :return: Inbound host response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/inbounds/hosts/{host_id}",
            data=host_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinInboundHostResponse(**response)

    @classmethod
    async def delete_host(
        cls, host: str, token: str, host_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a host by ID.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/inbounds/hosts/{host_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_inbound_hosts(
        cls, host: str, token: str, inbound_id: int, timeout: int = 10
    ) -> RustneshinPageInboundHostResponse:
        """
        Retrieve hosts for a specific inbound.

        :param host: API host URL
        :param token: Authentication token
        :param inbound_id: Inbound ID
        :param timeout: Request timeout in seconds
        :return: Paginated inbound host response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds/{inbound_id}/hosts",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageInboundHostResponse(**response)

    @classmethod
    async def create_host(
        cls,
        host: str,
        token: str,
        inbound_id: int,
        host_data: RustneshinInboundHost,
        timeout: int = 10,
    ) -> RustneshinInboundHostResponse:
        """
        Create a host for an inbound.

        :param host: API host URL
        :param token: Authentication token
        :param inbound_id: Inbound ID
        :param host_data: Host data
        :param timeout: Request timeout in seconds
        :return: Inbound host response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/inbounds/{inbound_id}/hosts",
            data=host_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinInboundHostResponse(**response)

    # ==================== Node Endpoints ====================

    @classmethod
    async def get_nodes(
        cls,
        host: str,
        token: str,
        name: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        timeout: int = 10,
    ) -> RustneshinPageNodeResponse:
        """
        Retrieve all nodes.

        :param host: API host URL
        :param token: Authentication token
        :param name: Filter by node name
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: Paginated node response
        """
        params = {}
        if name:
            params["name"] = name
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageNodeResponse(**response)

    @classmethod
    async def create_node(
        cls, host: str, token: str, node_data: RustneshinNodeCreate, timeout: int = 10
    ) -> RustneshinNodeResponse:
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
            data=node_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinNodeResponse(**response)

    @classmethod
    async def get_node_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinNodeSettings:
        """
        Retrieve node settings.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Node settings
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/settings",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinNodeSettings(**response)

    @classmethod
    async def get_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> RustneshinNodeResponse:
        """
        Retrieve a specific node by ID.

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
        return RustneshinNodeResponse(**response)

    @classmethod
    async def update_node(
        cls,
        host: str,
        token: str,
        node_id: int,
        node_data: RustneshinNodeModify,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Update an existing node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param node_data: Node modification data
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.put(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}",
            data=node_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def delete_node(
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
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_node_usage(
        cls,
        host: str,
        token: str,
        node_id: int,
        start: datetime,
        end: datetime,
        granularity: Optional[RustneshinGranularity] = None,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Get usage statistics for a node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param start: Start datetime
        :param end: End datetime
        :param granularity: Granularity level
        :param timeout: Request timeout in seconds
        :return: Usage data
        """
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
        }
        if granularity:
            params["granularity"] = granularity.value

        return await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_node_backend_config(
        cls, host: str, token: str, node_id: int, backend: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Get backend config for a node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param timeout: Request timeout in seconds
        :return: Backend config
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/config",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def update_node_backend_config(
        cls,
        host: str,
        token: str,
        node_id: int,
        backend: str,
        config: RustneshinBackendConfig,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Update backend config for a node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param config: Backend config
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.put(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/config",
            data=config.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_node_logs(
        cls, host: str, token: str, node_id: int, backend: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Get logs for a node backend.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param timeout: Request timeout in seconds
        :return: Logs
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/logs",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_node_backend_stats(
        cls, host: str, token: str, node_id: int, backend: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Get stats for a node backend.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param backend: Backend name
        :param timeout: Request timeout in seconds
        :return: Stats
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/{backend}/stats",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    # ==================== Service Endpoints ====================

    @classmethod
    async def get_services(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinPageServiceResponse:
        """
        Retrieve all services.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Paginated service response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/services",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageServiceResponse(**response)

    @classmethod
    async def create_service(
        cls,
        host: str,
        token: str,
        service_data: RustneshinServiceCreate,
        timeout: int = 10,
    ) -> RustneshinServiceResponse:
        """
        Create a new service.

        :param host: API host URL
        :param token: Authentication token
        :param service_data: Service creation data
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/services",
            data=service_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinServiceResponse(**response)

    @classmethod
    async def get_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> RustneshinServiceResponse:
        """
        Retrieve a specific service by ID.

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
        return RustneshinServiceResponse(**response)

    @classmethod
    async def update_service(
        cls,
        host: str,
        token: str,
        service_id: int,
        service_data: RustneshinServiceModify,
        timeout: int = 10,
    ) -> RustneshinServiceResponse:
        """
        Update an existing service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param service_data: Service modification data
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/services/{service_id}",
            data=service_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinServiceResponse(**response)

    @classmethod
    async def delete_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/services/{service_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_service_inbound_ids(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> List[int]:
        """
        Get inbound IDs for a service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param timeout: Request timeout in seconds
        :return: List of inbound IDs
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/services/{service_id}/inbound_ids",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def update_service_inbound_ids(
        cls,
        host: str,
        token: str,
        service_id: int,
        inbound_ids: List[int],
        timeout: int = 10,
    ) -> RustneshinServiceResponse:
        """
        Update inbound IDs for a service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param inbound_ids: List of inbound IDs
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        import json

        response = await cls.put(
            url=f"{host.rstrip('/')}/api/services/{service_id}/inbound_ids",
            data=json.dumps(inbound_ids),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinServiceResponse(**response)

    # ==================== Subscription Endpoints ====================

    @classmethod
    async def user_subscription(
        cls, host: str, username: str, key: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Get user subscription.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param timeout: Request timeout in seconds
        :return: Subscription data
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}",
            timeout=timeout,
        )

    @classmethod
    async def user_subscription_info(
        cls, host: str, username: str, key: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Get user subscription info.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param timeout: Request timeout in seconds
        :return: Subscription info
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}/info",
            timeout=timeout,
        )

    @classmethod
    async def user_subscription_usage(
        cls,
        host: str,
        username: str,
        key: str,
        start: datetime,
        end: datetime,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Get user subscription usage.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param start: Start datetime
        :param end: End datetime
        :param timeout: Request timeout in seconds
        :return: Usage data
        """
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
        }
        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}/usage",
            params=params,
            timeout=timeout,
        )

    @classmethod
    async def user_subscription_with_client_type(
        cls,
        host: str,
        username: str,
        key: str,
        client_type: RustneshinClientType,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Get user subscription with client type.

        :param host: API host URL
        :param username: Username
        :param key: Subscription key
        :param client_type: Client type
        :param timeout: Request timeout in seconds
        :return: Subscription data
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{username}/{key}/{client_type.value}",
            timeout=timeout,
        )

    # ==================== System Endpoints ====================

    @classmethod
    async def get_subscription_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinSubscriptionSettings:
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
        return RustneshinSubscriptionSettings(**response)

    @classmethod
    async def update_subscription_settings(
        cls,
        host: str,
        token: str,
        settings: RustneshinSubscriptionSettings,
        timeout: int = 10,
    ) -> RustneshinNodesStats:
        """
        Update subscription settings.

        :param host: API host URL
        :param token: Authentication token
        :param settings: Subscription settings
        :param timeout: Request timeout in seconds
        :return: Nodes stats
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/system/settings/subscription",
            data=settings.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinNodesStats(**response)

    @classmethod
    async def get_template(
        cls, host: str, token: str, template_name: str, timeout: int = 10
    ) -> RustneshinTemplateSettings:
        """
        Get template settings.

        :param host: API host URL
        :param token: Authentication token
        :param template_name: Template name
        :param timeout: Request timeout in seconds
        :return: Template settings
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/settings/subscription/templates/{template_name}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinTemplateSettings(**response)

    @classmethod
    async def update_template(
        cls,
        host: str,
        token: str,
        template_name: str,
        settings: RustneshinTemplateSettings,
        timeout: int = 10,
    ) -> RustneshinTemplateSettings:
        """
        Update template settings.

        :param host: API host URL
        :param token: Authentication token
        :param template_name: Template name
        :param settings: Template settings
        :param timeout: Request timeout in seconds
        :return: Template settings
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/system/settings/subscription/templates/{template_name}",
            data=settings.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinTemplateSettings(**response)

    @classmethod
    async def get_admins_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinAdminsStats:
        """
        Get admin statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Admin stats
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats/admins",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinAdminsStats(**response)

    @classmethod
    async def get_nodes_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinNodesStats:
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
        return RustneshinNodesStats(**response)

    @classmethod
    async def get_traffic_stats(
        cls,
        host: str,
        token: str,
        start: datetime,
        end: datetime,
        granularity: Optional[RustneshinGranularity] = None,
        timeout: int = 10,
    ) -> RustneshinTrafficUsageSeries:
        """
        Get traffic statistics.

        :param host: API host URL
        :param token: Authentication token
        :param start: Start datetime
        :param end: End datetime
        :param granularity: Granularity level
        :param timeout: Request timeout in seconds
        :return: Traffic usage series
        """
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
        }
        if granularity:
            params["granularity"] = granularity.value

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system/stats/traffic",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinTrafficUsageSeries(**response)

    @classmethod
    async def get_users_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> RustneshinUsersStats:
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
        return RustneshinUsersStats(**response)

    # ==================== User Endpoints ====================

    @classmethod
    async def get_users(
        cls,
        host: str,
        token: str,
        username: Optional[List[str]] = None,
        descending: Optional[bool] = None,
        is_active: Optional[bool] = None,
        activated: Optional[bool] = None,
        expired: Optional[bool] = None,
        data_limit_reached: Optional[bool] = None,
        enabled: Optional[bool] = None,
        owner_username: Optional[str] = None,
        order_by: Optional[str] = None,
        timeout: int = 10,
    ) -> RustneshinPageUserResponse:
        """
        Retrieve all users with optional filters.

        :param host: API host URL
        :param token: Authentication token
        :param username: Filter by usernames
        :param descending: Sort descending
        :param is_active: Filter by active status
        :param activated: Filter by activated status
        :param expired: Filter by expired status
        :param data_limit_reached: Filter by data limit reached
        :param enabled: Filter by enabled status
        :param owner_username: Filter by owner username
        :param order_by: Sort field
        :param timeout: Request timeout in seconds
        :return: Paginated user response
        """
        params = {}
        if username:
            params["username"] = username
        if descending is not None:
            params["descending"] = descending
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
        if order_by:
            params["order_by"] = order_by

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinPageUserResponse(**response)

    @classmethod
    async def create_user(
        cls, host: str, token: str, user_data: RustneshinUserCreate, timeout: int = 10
    ) -> RustneshinUserResponse:
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
            data=user_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinUserResponse(**response)

    @classmethod
    async def get_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinUserResponse:
        """
        Retrieve a specific user by username.

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
        return RustneshinUserResponse(**response)

    @classmethod
    async def update_user(
        cls,
        host: str,
        token: str,
        username: str,
        user_data: RustneshinUserModify,
        timeout: int = 10,
    ) -> RustneshinUserResponse:
        """
        Update an existing user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param user_data: User modification data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/users/{username}",
            data=user_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinUserResponse(**response)

    @classmethod
    async def delete_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinUserResponse:
        """
        Delete a user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/users/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinUserResponse(**response)

    @classmethod
    async def disable_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinUserResponse:
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
            data={},
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinUserResponse(**response)

    @classmethod
    async def enable_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinUserResponse:
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
            data={},
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinUserResponse(**response)

    @classmethod
    async def reset_user_data_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinUserResponse:
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
        return RustneshinUserResponse(**response)

    @classmethod
    async def revoke_user_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> RustneshinUserResponse:
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
        return RustneshinUserResponse(**response)

    @classmethod
    async def get_user_usage(
        cls,
        host: str,
        token: str,
        username: str,
        start: datetime,
        end: datetime,
        granularity: Optional[RustneshinGranularity] = None,
        timeout: int = 10,
    ) -> RustneshinUserUsageSeriesResponse:
        """
        Get user usage statistics.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param start: Start datetime
        :param end: End datetime
        :param granularity: Granularity level
        :param timeout: Request timeout in seconds
        :return: User usage series response
        """
        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
        }
        if granularity:
            params["granularity"] = granularity.value

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/{username}/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinUserUsageSeriesResponse(**response)

    # ==================== Webhook Endpoints ====================

    @classmethod
    async def list_webhook_endpoints(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[RustneshinEndpointRes]:
        """
        List all webhook endpoints.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of endpoints
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/webhook/endpoints",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [RustneshinEndpointRes(**item) for item in response]

    @classmethod
    async def create_webhook_endpoint(
        cls,
        host: str,
        token: str,
        endpoint_data: RustneshinCreateEndpointReq,
        timeout: int = 10,
    ) -> RustneshinEndpointCreatedRes:
        """
        Create a webhook endpoint.

        :param host: API host URL
        :param token: Authentication token
        :param endpoint_data: Endpoint creation data
        :param timeout: Request timeout in seconds
        :return: Created endpoint response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/webhook/endpoints",
            data=endpoint_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinEndpointCreatedRes(**response)

    @classmethod
    async def get_webhook_endpoint(
        cls, host: str, token: str, endpoint_id: int, timeout: int = 10
    ) -> RustneshinEndpointWithSubsRes:
        """
        Get a webhook endpoint with subscriptions.

        :param host: API host URL
        :param token: Authentication token
        :param endpoint_id: Endpoint ID
        :param timeout: Request timeout in seconds
        :return: Endpoint with subscriptions
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/webhook/endpoints/{endpoint_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinEndpointWithSubsRes(**response)

    @classmethod
    async def delete_webhook_endpoint(
        cls, host: str, token: str, endpoint_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a webhook endpoint.

        :param host: API host URL
        :param token: Authentication token
        :param endpoint_id: Endpoint ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/webhook/endpoints/{endpoint_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def update_webhook_endpoint(
        cls,
        host: str,
        token: str,
        endpoint_id: int,
        endpoint_data: RustneshinUpdateEndpointReq,
        timeout: int = 10,
    ) -> RustneshinEndpointWithSubsRes:
        """
        Update a webhook endpoint.

        :param host: API host URL
        :param token: Authentication token
        :param endpoint_id: Endpoint ID
        :param endpoint_data: Endpoint update data
        :param timeout: Request timeout in seconds
        :return: Updated endpoint with subscriptions
        """
        response = await cls.fetch(
            method="PATCH",
            url=f"{host.rstrip('/')}/api/webhook/endpoints/{endpoint_id}",
            data=endpoint_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return RustneshinEndpointWithSubsRes(**response)
