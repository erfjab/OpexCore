from typing import Optional, List, Dict, Any
from opexcore.core import RequestBase
from .types import (
    AdminStatsResponseNew,
    GuardAdminCreate,
    GuardAdminCurrentUpdate,
    GuardAdminResponse,
    GuardAdminToken,
    GuardAdminUpdate,
    GuardAdminUsageLogsResponse,
    GuardNodeCreate,
    GuardNodeResponse,
    GuardNodeStatsResponse,
    GuardNodeUpdate,
    GuardServiceCreate,
    GuardServiceResponse,
    GuardServiceUpdate,
    GuardStatsResponse,
    GuardSubscriptionCreate,
    GuardSubscriptionResponse,
    GuardSubscriptionStatsResponse,
    GuardSubscriptionUpdate,
    GuardSubscriptionUsageLogsResponse,
    GuardSubscriptionStatusStatsResponse,
    GuardMostUsageSubscription,
    GuardUsageStatsResponse,
    GuardAgentStatsResponse,
)


class GuardManager(RequestBase):
    """GuardCore API Manager with all endpoints"""

    @classmethod
    def _generate_headers(cls, token: Optional[str] = None) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    @classmethod
    async def get_subscription_by_secret(
        cls, host: str, secret: str, timeout: int = 10
    ) -> List[str]:
        """
        Handle incoming subscription request from clients.

        :param host: API host URL
        :param secret: Subscription secret
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/guards/{secret}", timeout=timeout
        )
        return response

    @classmethod
    async def get_subscription_info_by_secret(
        cls, host: str, secret: str, timeout: int = 10
    ) -> GuardSubscriptionResponse:
        """
        Get subscription information by secret.

        :param host: API host URL
        :param secret: Subscription secret
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/guards/{secret}/info", timeout=timeout
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def get_subscription_usages_by_secret(
        cls, host: str, secret: str, timeout: int = 10
    ) -> GuardSubscriptionUsageLogsResponse:
        """
        Get subscription usage logs by secret.

        :param host: API host URL
        :param secret: Subscription secret
        :param timeout: Request timeout in seconds
        :return: Subscription usage logs response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/guards/{secret}/usages", timeout=timeout
        )
        return GuardSubscriptionUsageLogsResponse(**response)

    @classmethod
    async def get_subscription_status_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardSubscriptionStatusStatsResponse:
        """
        Get subscription status statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Subscription status stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/stats/subscriptions/status",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionStatusStatsResponse(**response)

    @classmethod
    async def get_most_usage_subscriptions(
        cls, host: str, token: str, start_date: str, end_date: str, timeout: int = 10
    ) -> GuardMostUsageSubscription:
        """
        Get most usage subscriptions.

        :param host: API host URL
        :param token: Authentication token
        :param start_date: Start date
        :param end_date: End date
        :param timeout: Request timeout in seconds
        :return: Most usage subscription response
        """
        params = {"start_date": start_date, "end_date": end_date}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/stats/subscriptions/most_usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardMostUsageSubscription(**response)

    @classmethod
    async def get_usage_stats(
        cls, host: str, token: str, start_date: str, end_date: str, timeout: int = 10
    ) -> GuardUsageStatsResponse:
        """
        Get usage statistics.

        :param host: API host URL
        :param token: Authentication token
        :param start_date: Start date
        :param end_date: End date
        :param timeout: Request timeout in seconds
        :return: Usage stats response
        """
        params = {"start_date": start_date, "end_date": end_date}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/stats/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardUsageStatsResponse(**response)

    @classmethod
    async def get_agent_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardAgentStatsResponse:
        """
        Get agent statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Agent stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/stats/agents",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAgentStatsResponse(**response)

    @classmethod
    async def get_nodes(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[GuardNodeResponse]:
        """
        Get a list of all nodes.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of node responses
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [GuardNodeResponse(**item) for item in response]

    @classmethod
    async def create_node(
        cls, host: str, token: str, node_data: GuardNodeCreate, timeout: int = 10
    ) -> GuardNodeResponse:
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
        return GuardNodeResponse(**response)

    @classmethod
    async def get_node_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardNodeStatsResponse:
        """
        Get statistics about nodes.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Node stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/stats",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardNodeStatsResponse(**response)

    @classmethod
    async def get_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> GuardNodeResponse:
        """
        Get a single node by ID.

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
        return GuardNodeResponse(**response)

    @classmethod
    async def update_node(
        cls,
        host: str,
        token: str,
        node_id: int,
        node_data: GuardNodeUpdate,
        timeout: int = 10,
    ) -> GuardNodeResponse:
        """
        Update an existing node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param node_data: Node update data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}",
            data=node_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardNodeResponse(**response)

    @classmethod
    async def delete_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a node by ID.

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
        return response

    @classmethod
    async def enable_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> GuardNodeResponse:
        """
        Enable a node by ID.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/enable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardNodeResponse(**response)

    @classmethod
    async def disable_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> GuardNodeResponse:
        """
        Disable a node by ID.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/nodes/{node_id}/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardNodeResponse(**response)

    @classmethod
    async def get_services(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[GuardServiceResponse]:
        """
        Get a list of all services.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of service responses
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/services",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [GuardServiceResponse(**item) for item in response]

    @classmethod
    async def create_service(
        cls, host: str, token: str, service_data: GuardServiceCreate, timeout: int = 10
    ) -> GuardServiceResponse:
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
        return GuardServiceResponse(**response)

    @classmethod
    async def get_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> GuardServiceResponse:
        """
        Get a single service by ID.

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
        return GuardServiceResponse(**response)

    @classmethod
    async def update_service(
        cls,
        host: str,
        token: str,
        service_id: int,
        service_data: GuardServiceUpdate,
        timeout: int = 10,
    ) -> GuardServiceResponse:
        """
        Update an existing service.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param service_data: Service update data
        :param timeout: Request timeout in seconds
        :return: Service response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/services/{service_id}",
            data=service_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardServiceResponse(**response)

    @classmethod
    async def delete_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a service by ID.

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
        return response

    @classmethod
    async def get_admins(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[GuardAdminResponse]:
        """
        Get a list of all admins.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of admin responses
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [GuardAdminResponse(**item) for item in response]

    @classmethod
    async def create_admin(
        cls, host: str, token: str, admin_data: GuardAdminCreate, timeout: int = 10
    ) -> GuardAdminResponse:
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
        return GuardAdminResponse(**response)

    @classmethod
    async def create_token(
        cls, host: str, username: str, password: str, timeout: int = 10
    ) -> GuardAdminToken:
        """
        Create authentication token for admin.

        :param host: API host URL
        :param username: Admin username
        :param password: Admin password
        :param timeout: Request timeout in seconds
        :return: Admin token
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/token",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=timeout,
        )
        return GuardAdminToken(**response)

    @classmethod
    async def get_current_admin(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardAdminResponse:
        """
        Get the current authenticated admin.

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
        return GuardAdminResponse(**response)

    @classmethod
    async def update_current_admin(
        cls,
        host: str,
        token: str,
        admin_data: GuardAdminCurrentUpdate,
        timeout: int = 10,
    ) -> GuardAdminResponse:
        """
        Update the current admin.

        :param host: API host URL
        :param token: Authentication token
        :param admin_data: Admin update data
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/admins/current",
            data=admin_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminResponse(**response)

    @classmethod
    async def get_current_admin_usages(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardAdminUsageLogsResponse:
        """
        Get usage logs for the current admin.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Admin usage logs response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/current/usages",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminUsageLogsResponse(**response)

    @classmethod
    async def revoke_current_admin_api_key(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardAdminResponse:
        """
        Revoke API key for the current admin.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/current/revoke",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminResponse(**response)

    @classmethod
    async def get_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardAdminResponse:
        """
        Get a single admin by username.

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
        return GuardAdminResponse(**response)

    @classmethod
    async def update_admin(
        cls,
        host: str,
        token: str,
        username: str,
        admin_data: GuardAdminUpdate,
        timeout: int = 10,
    ) -> GuardAdminResponse:
        """
        Update an existing admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param admin_data: Admin update data
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/admins/{username}",
            data=admin_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminResponse(**response)

    @classmethod
    async def delete_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete an admin by username.

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
        return response

    @classmethod
    async def get_admin_usages(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardAdminUsageLogsResponse:
        """
        Get usage logs for an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin usage logs response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{username}/usages",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminUsageLogsResponse(**response)

    @classmethod
    async def enable_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardAdminResponse:
        """
        Enable an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/enable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminResponse(**response)

    @classmethod
    async def disable_admin(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardAdminResponse:
        """
        Disable an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminResponse(**response)

    @classmethod
    async def revoke_admin_api_key(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardAdminResponse:
        """
        Revoke API key for an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/revoke",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardAdminResponse(**response)

    @classmethod
    async def get_admin_subscriptions(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> List[GuardSubscriptionResponse]:
        """
        Get subscriptions of an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: List of subscription responses
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins/{username}/subscriptions",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [GuardSubscriptionResponse(**item) for item in response]

    @classmethod
    async def delete_admin_subscriptions(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete subscriptions of an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/admins/{username}/subscriptions",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def activate_admin_subscriptions(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Activate subscriptions of an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/subscriptions/activate",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def deactivate_admin_subscriptions(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Deactivate subscriptions of an admin by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admins/{username}/subscriptions/deactivate",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def get_subscriptions(
        cls,
        host: str,
        token: str,
        limited: Optional[bool] = None,
        expired: Optional[bool] = None,
        is_active: Optional[bool] = None,
        enabled: Optional[bool] = None,
        search: Optional[str] = None,
        online: Optional[bool] = None,
        order_by: Optional[str] = None,
        page: int = 1,
        size: int = 10,
        timeout: int = 10,
    ) -> List[GuardSubscriptionResponse]:
        """
        Get a list of all subscriptions with optional filters.

        :param host: API host URL
        :param token: Authentication token
        :param limited: Filter by limited status
        :param expired: Filter by expired status
        :param is_active: Filter by active status
        :param enabled: Filter by enabled status
        :param search: Search query
        :param online: Filter by online status
        :param order_by: Order by field
        :param page: Page number
        :param size: Page size
        :param timeout: Request timeout in seconds
        :return: List of subscription responses
        """
        params = {"page": page, "size": size}
        if limited is not None:
            params["limited"] = limited
        if expired is not None:
            params["expired"] = expired
        if is_active is not None:
            params["is_active"] = is_active
        if enabled is not None:
            params["enabled"] = enabled
        if search is not None:
            params["search"] = search
        if online is not None:
            params["online"] = online
        if order_by is not None:
            params["order_by"] = order_by

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/subscriptions",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [GuardSubscriptionResponse(**item) for item in response]

    @classmethod
    async def create_subscriptions(
        cls,
        host: str,
        token: str,
        subscriptions_data: List[GuardSubscriptionCreate],
        timeout: int = 10,
    ) -> List[GuardSubscriptionResponse]:
        """
        Create bulk subscriptions.

        :param host: API host URL
        :param token: Authentication token
        :param subscriptions_data: List of subscription creation data
        :param timeout: Request timeout in seconds
        :return: List of subscription responses
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/subscriptions",
            data=[sub.model_dump_json(exclude_none=True) for sub in subscriptions_data],
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [GuardSubscriptionResponse(**item) for item in response]

    @classmethod
    async def get_subscription_count(
        cls,
        host: str,
        token: str,
        limited: Optional[bool] = None,
        expired: Optional[bool] = None,
        is_active: Optional[bool] = None,
        enabled: Optional[bool] = None,
        online: Optional[bool] = None,
        timeout: int = 10,
    ) -> int:
        """
        Get the count of subscriptions.

        :param host: API host URL
        :param token: Authentication token
        :param limited: Filter by limited status
        :param expired: Filter by expired status
        :param is_active: Filter by active status
        :param enabled: Filter by enabled status
        :param online: Filter by online status
        :param timeout: Request timeout in seconds
        :return: Subscription count
        """
        params = {}
        if limited is not None:
            params["limited"] = limited
        if expired is not None:
            params["expired"] = expired
        if is_active is not None:
            params["is_active"] = is_active
        if enabled is not None:
            params["enabled"] = enabled
        if online is not None:
            params["online"] = online

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/subscriptions/count",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def get_subscription_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> GuardSubscriptionStatsResponse:
        """
        Get subscription statistics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Subscription stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/subscriptions/stats",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionStatsResponse(**response)

    @classmethod
    async def get_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardSubscriptionResponse:
        """
        Get a single subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def update_subscription(
        cls,
        host: str,
        token: str,
        username: str,
        subscription_data: GuardSubscriptionUpdate,
        timeout: int = 10,
    ) -> GuardSubscriptionResponse:
        """
        Update an existing subscription.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param subscription_data: Subscription update data
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}",
            data=subscription_data.model_dump_json(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def delete_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def get_subscription_usages(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardSubscriptionUsageLogsResponse:
        """
        Get usage logs for a subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Subscription usage logs response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}/usages",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionUsageLogsResponse(**response)

    @classmethod
    async def enable_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardSubscriptionResponse:
        """
        Enable a subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}/enable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def disable_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardSubscriptionResponse:
        """
        Disable a subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def revoke_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardSubscriptionResponse:
        """
        Revoke a subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}/revoke",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def reset_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> GuardSubscriptionResponse:
        """
        Reset a subscription by username.

        :param host: API host URL
        :param token: Authentication token
        :param username: Subscription username
        :param timeout: Request timeout in seconds
        :return: Subscription response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/subscriptions/{username}/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return GuardSubscriptionResponse(**response)

    @classmethod
    async def bulk_add_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Add a service to all subscriptions of the current admin.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/subscriptions/services/{service_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def bulk_remove_service(
        cls, host: str, token: str, service_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove a service from all subscriptions of the current admin.

        :param host: API host URL
        :param token: Authentication token
        :param service_id: Service ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/subscriptions/services/{service_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response
