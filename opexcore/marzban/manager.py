from typing import Optional, List, Dict, Any
from datetime import datetime
from opexcore.core import RequestBase
from .types import (
    MarzbanAdmin,
    MarzbanAdminCreate,
    MarzbanAdminModify,
    MarzbanToken,
    MarzbanUserCreate,
    MarzbanUserModify,
    MarzbanUserResponse,
    MarzbanUsersResponse,
    MarzbanUserStatus,
    MarzbanUserUsagesResponse,
    MarzbanUsersUsagesResponse,
    MarzbanNodeCreate,
    MarzbanNodeModify,
    MarzbanNodeResponse,
    MarzbanNodeSettings,
    MarzbanNodesUsageResponse,
    MarzbanCoreStats,
    MarzbanSystemStats,
    MarzbanProxyInbound,
    MarzbanProxyHost,
    MarzbanSubscriptionUserResponse,
    MarzbanUserTemplateCreate,
    MarzbanUserTemplateModify,
    MarzbanUserTemplateResponse,
)


class MarzbanManager(RequestBase):
    """Marzban API Manager with all endpoints"""

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
    ) -> MarzbanToken:
        """
        Authenticate an admin and issue a token.

        :param host: API host URL
        :param username: Admin username
        :param password: Admin password
        :param timeout: Request timeout in seconds
        :return: Token response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admin/token",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=timeout,
        )
        return MarzbanToken(**response)

    @classmethod
    async def get_current_admin(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzbanAdmin:
        """
        Retrieve the current authenticated admin.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admin",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanAdmin(**response)

    @classmethod
    async def create_admin(
        cls, host: str, token: str, admin_data: MarzbanAdminCreate, timeout: int = 10
    ) -> MarzbanAdmin:
        """
        Create a new admin if the current admin has sudo privileges.

        :param host: API host URL
        :param token: Authentication token
        :param admin_data: Admin creation data
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admin",
            data=admin_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanAdmin(**response)

    @classmethod
    async def modify_admin(
        cls,
        host: str,
        token: str,
        username: str,
        admin_data: MarzbanAdminModify,
        timeout: int = 10,
    ) -> MarzbanAdmin:
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
            url=f"{host.rstrip('/')}/api/admin/{username}",
            data=admin_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanAdmin(**response)

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
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/admin/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_admins(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        username: Optional[str] = None,
        timeout: int = 10,
    ) -> List[MarzbanAdmin]:
        """
        Fetch a list of admins with optional filters for pagination and username.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param username: Filter by username
        :param timeout: Request timeout in seconds
        :return: List of admin responses
        """
        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if username is not None:
            params["username"] = username

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [MarzbanAdmin(**item) for item in response]

    @classmethod
    async def disable_all_active_users(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Disable all active users under a specific admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.post(
            url=f"{host.rstrip('/')}/api/admin/{username}/users/disable",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def activate_all_disabled_users(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Activate all disabled users under a specific admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.post(
            url=f"{host.rstrip('/')}/api/admin/{username}/users/activate",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def reset_admin_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzbanAdmin:
        """
        Resets usage of admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admin/usage/reset/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanAdmin(**response)

    @classmethod
    async def get_admin_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> int:
        """
        Retrieve the usage of given admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Usage amount
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/admin/usage/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_core_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzbanCoreStats:
        """
        Retrieve core statistics such as version and uptime.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Core stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/core",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanCoreStats(**response)

    @classmethod
    async def restart_core(
        cls, host: str, token: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Restart the core and all connected nodes.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.post(
            url=f"{host.rstrip('/')}/api/core/restart",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_core_config(
        cls, host: str, token: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Get the current core configuration.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Core configuration
        """
        return await cls.get(
            url=f"{host.rstrip('/')}/api/core/config",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def modify_core_config(
        cls, host: str, token: str, config: Dict[str, Any], timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Modify the core configuration and restart the core.

        :param host: API host URL
        :param token: Authentication token
        :param config: Core configuration data
        :param timeout: Request timeout in seconds
        :return: Updated core configuration
        """
        return await cls.put(
            url=f"{host.rstrip('/')}/api/core/config",
            data=config,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_node_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzbanNodeSettings:
        """
        Retrieve the current node settings, including TLS certificate.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Node settings response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/node/settings",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanNodeSettings(**response)

    @classmethod
    async def add_node(
        cls, host: str, token: str, node_data: MarzbanNodeCreate, timeout: int = 10
    ) -> MarzbanNodeResponse:
        """
        Add a new node to the database and optionally add it as a host.

        :param host: API host URL
        :param token: Authentication token
        :param node_data: Node creation data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/node",
            data=node_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanNodeResponse(**response)

    @classmethod
    async def get_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> MarzbanNodeResponse:
        """
        Retrieve details of a specific node by its ID.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/node/{node_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanNodeResponse(**response)

    @classmethod
    async def modify_node(
        cls,
        host: str,
        token: str,
        node_id: int,
        node_data: MarzbanNodeModify,
        timeout: int = 10,
    ) -> MarzbanNodeResponse:
        """
        Update a node's details. Only accessible to sudo admins.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param node_data: Node modification data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/node/{node_id}",
            data=node_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanNodeResponse(**response)

    @classmethod
    async def remove_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a node and remove it from xray in the background.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/node/{node_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_nodes(
        cls, host: str, token: str, timeout: int = 10
    ) -> List[MarzbanNodeResponse]:
        """
        Retrieve a list of all nodes. Accessible only to sudo admins.

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
        return [MarzbanNodeResponse(**item) for item in response]

    @classmethod
    async def reconnect_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Trigger a reconnection for the specified node. Only accessible to sudo admins.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.post(
            url=f"{host.rstrip('/')}/api/node/{node_id}/reconnect",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_nodes_usage(
        cls,
        host: str,
        token: str,
        start: str = "",
        end: str = "",
        timeout: int = 10,
    ) -> MarzbanNodesUsageResponse:
        """
        Retrieve usage statistics for nodes within a specified date range.

        :param host: API host URL
        :param token: Authentication token
        :param start: Start date (ISO format)
        :param end: End date (ISO format)
        :param timeout: Request timeout in seconds
        :return: Nodes usage response
        """
        params = {"start": start, "end": end}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanNodesUsageResponse(**response)

    @classmethod
    async def user_subscription(
        cls, host: str, token: str, user_agent: str = "", timeout: int = 10
    ) -> List[str]:
        """
        Provides a subscription link based on the user agent (Clash, V2Ray, etc.).

        :param host: API host URL
        :param token: Subscription token
        :param user_agent: User agent header
        :param timeout: Request timeout in seconds
        :return: Subscription links
        """
        headers = {}
        if user_agent:
            headers["user-agent"] = user_agent

        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{token}/",
            headers=headers,
            timeout=timeout,
        )

    @classmethod
    async def user_subscription_info(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzbanSubscriptionUserResponse:
        """
        Retrieves detailed information about the user's subscription.

        :param host: API host URL
        :param token: Subscription token
        :param timeout: Request timeout in seconds
        :return: Subscription user response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{token}/info",
            timeout=timeout,
        )
        return MarzbanSubscriptionUserResponse(**response)

    @classmethod
    async def user_get_usage(
        cls,
        host: str,
        token: str,
        start: str = "",
        end: str = "",
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Fetches the usage statistics for the user within a specified date range.

        :param host: API host URL
        :param token: Subscription token
        :param start: Start date
        :param end: End date
        :param timeout: Request timeout in seconds
        :return: Usage data
        """
        params = {"start": start, "end": end}
        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{token}/usage",
            params=params,
            timeout=timeout,
        )

    @classmethod
    async def user_subscription_with_client_type(
        cls,
        host: str,
        token: str,
        client_type: str,
        user_agent: str = "",
        timeout: int = 10,
    ) -> List[str]:
        """
        Provides a subscription link based on the specified client type (e.g., Clash, V2Ray).

        :param host: API host URL
        :param token: Subscription token
        :param client_type: Client type (sing-box, clash-meta, clash, outline, v2ray, v2ray-json)
        :param user_agent: User agent header
        :param timeout: Request timeout in seconds
        :return: Subscription links
        """
        headers = {}
        if user_agent:
            headers["user-agent"] = user_agent

        return await cls.get(
            url=f"{host.rstrip('/')}/sub/{token}/{client_type}",
            headers=headers,
            timeout=timeout,
        )

    @classmethod
    async def get_system_stats(
        cls, host: str, token: str, timeout: int = 10
    ) -> MarzbanSystemStats:
        """
        Fetch system stats including memory, CPU, and user metrics.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: System stats response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanSystemStats(**response)

    @classmethod
    async def get_inbounds(
        cls, host: str, token: str, timeout: int = 10
    ) -> Dict[str, List[MarzbanProxyInbound]]:
        """
        Retrieve inbound configurations grouped by protocol.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Dictionary of inbounds by protocol
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        result = {}
        for protocol, inbounds in response.items():
            result[protocol] = [MarzbanProxyInbound(**inbound) for inbound in inbounds]
        return result

    @classmethod
    async def get_hosts(
        cls, host: str, token: str, timeout: int = 10
    ) -> Dict[str, List[MarzbanProxyHost]]:
        """
        Get a list of proxy hosts grouped by inbound tag.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Dictionary of hosts by inbound tag
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/hosts",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        result = {}
        for tag, hosts in response.items():
            result[tag] = [MarzbanProxyHost(**host_data) for host_data in hosts]
        return result

    @classmethod
    async def modify_hosts(
        cls,
        host: str,
        token: str,
        modified_hosts: Dict[str, List[MarzbanProxyHost]],
        timeout: int = 10,
    ) -> Dict[str, List[MarzbanProxyHost]]:
        """
        Modify proxy hosts and update the configuration.

        :param host: API host URL
        :param token: Authentication token
        :param modified_hosts: Dictionary of modified hosts by inbound tag
        :param timeout: Request timeout in seconds
        :return: Updated dictionary of hosts
        """
        data = {}
        for tag, hosts in modified_hosts.items():
            data[tag] = [host_obj.dict() for host_obj in hosts]

        response = await cls.put(
            url=f"{host.rstrip('/')}/api/hosts",
            data=data,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        result = {}
        for tag, hosts in response.items():
            result[tag] = [MarzbanProxyHost(**host_data) for host_data in hosts]
        return result

    @classmethod
    async def add_user_template(
        cls,
        host: str,
        token: str,
        template_data: MarzbanUserTemplateCreate,
        timeout: int = 10,
    ) -> MarzbanUserTemplateResponse:
        """
        Add a new user template.

        :param host: API host URL
        :param token: Authentication token
        :param template_data: User template creation data
        :param timeout: Request timeout in seconds
        :return: User template response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user_template",
            data=template_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserTemplateResponse(**response)

    @classmethod
    async def get_user_templates(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: int = 10,
    ) -> List[MarzbanUserTemplateResponse]:
        """
        Get a list of User Templates with optional pagination.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param timeout: Request timeout in seconds
        :return: List of user template responses
        """
        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/user_template",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return [MarzbanUserTemplateResponse(**item) for item in response]

    @classmethod
    async def get_user_template(
        cls, host: str, token: str, template_id: int, timeout: int = 10
    ) -> MarzbanUserTemplateResponse:
        """
        Get User Template information by ID.

        :param host: API host URL
        :param token: Authentication token
        :param template_id: Template ID
        :param timeout: Request timeout in seconds
        :return: User template response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/user_template/{template_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserTemplateResponse(**response)

    @classmethod
    async def modify_user_template(
        cls,
        host: str,
        token: str,
        template_id: int,
        template_data: MarzbanUserTemplateModify,
        timeout: int = 10,
    ) -> MarzbanUserTemplateResponse:
        """
        Modify User Template.

        :param host: API host URL
        :param token: Authentication token
        :param template_id: Template ID
        :param template_data: User template modification data
        :param timeout: Request timeout in seconds
        :return: User template response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/user_template/{template_id}",
            data=template_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserTemplateResponse(**response)

    @classmethod
    async def remove_user_template(
        cls, host: str, token: str, template_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove a User Template by its ID.

        :param host: API host URL
        :param token: Authentication token
        :param template_id: Template ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/user_template/{template_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def add_user(
        cls, host: str, token: str, user_data: MarzbanUserCreate, timeout: int = 10
    ) -> MarzbanUserResponse:
        """
        Add a new user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User creation data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user",
            data=user_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

    @classmethod
    async def get_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzbanUserResponse:
        """
        Get user information.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/user/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

    @classmethod
    async def modify_user(
        cls,
        host: str,
        token: str,
        username: str,
        user_data: MarzbanUserModify,
        timeout: int = 10,
    ) -> MarzbanUserResponse:
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
            url=f"{host.rstrip('/')}/api/user/{username}",
            data=user_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

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
        return await cls.delete(
            url=f"{host.rstrip('/')}/api/user/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def reset_user_data_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzbanUserResponse:
        """
        Reset user data usage.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user/{username}/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

    @classmethod
    async def revoke_user_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzbanUserResponse:
        """
        Revoke users subscription (Subscription link and proxies).

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user/{username}/revoke_sub",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

    @classmethod
    async def get_users(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        username: Optional[List[str]] = None,
        search: Optional[str] = None,
        admin: Optional[List[str]] = None,
        status: Optional[MarzbanUserStatus] = None,
        sort: Optional[str] = None,
        timeout: int = 10,
    ) -> MarzbanUsersResponse:
        """
        Get all users with optional filters.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param username: Filter by usernames
        :param search: Search query
        :param admin: Filter by admin usernames
        :param status: Filter by status
        :param sort: Sort field
        :param timeout: Request timeout in seconds
        :return: Users response
        """
        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if username is not None:
            params["username"] = username
        if search is not None:
            params["search"] = search
        if admin is not None:
            params["admin"] = admin
        if status is not None:
            params["status"] = status.value
        if sort is not None:
            params["sort"] = sort

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUsersResponse(**response)

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
        return await cls.post(
            url=f"{host.rstrip('/')}/api/users/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )

    @classmethod
    async def get_user_usage(
        cls,
        host: str,
        token: str,
        username: str,
        start: str = "",
        end: str = "",
        timeout: int = 10,
    ) -> MarzbanUserUsagesResponse:
        """
        Get users usage.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param start: Start date
        :param end: End date
        :param timeout: Request timeout in seconds
        :return: User usages response
        """
        params = {"start": start, "end": end}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/user/{username}/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserUsagesResponse(**response)

    @classmethod
    async def active_next_plan(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> MarzbanUserResponse:
        """
        Reset user by next plan.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user/{username}/active-next",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

    @classmethod
    async def get_users_usage(
        cls,
        host: str,
        token: str,
        start: str = "",
        end: str = "",
        admin: Optional[List[str]] = None,
        timeout: int = 10,
    ) -> MarzbanUsersUsagesResponse:
        """
        Get all users usage.

        :param host: API host URL
        :param token: Authentication token
        :param start: Start date
        :param end: End date
        :param admin: Filter by admin usernames
        :param timeout: Request timeout in seconds
        :return: Users usages response
        """
        params = {"start": start, "end": end}
        if admin is not None:
            params["admin"] = admin

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/usage",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUsersUsagesResponse(**response)

    @classmethod
    async def set_owner(
        cls,
        host: str,
        token: str,
        username: str,
        admin_username: str,
        timeout: int = 10,
    ) -> MarzbanUserResponse:
        """
        Set a new owner (admin) for a user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param admin_username: Admin username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/user/{username}/set-owner",
            data={"admin_username": admin_username},
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return MarzbanUserResponse(**response)

    @classmethod
    async def get_expired_users(
        cls,
        host: str,
        token: str,
        expired_after: Optional[datetime] = None,
        expired_before: Optional[datetime] = None,
        timeout: int = 10,
    ) -> List[str]:
        """
        Get users who have expired within the specified date range.

        :param host: API host URL
        :param token: Authentication token
        :param expired_after: Expired after date
        :param expired_before: Expired before date
        :param timeout: Request timeout in seconds
        :return: List of usernames
        """
        params = {}
        if expired_after is not None:
            params["expired_after"] = expired_after.isoformat()
        if expired_before is not None:
            params["expired_before"] = expired_before.isoformat()

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users/expired",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def delete_expired_users(
        cls,
        host: str,
        token: str,
        expired_after: Optional[datetime] = None,
        expired_before: Optional[datetime] = None,
        timeout: int = 10,
    ) -> List[str]:
        """
        Delete users who have expired within the specified date range.

        :param host: API host URL
        :param token: Authentication token
        :param expired_after: Expired after date
        :param expired_before: Expired before date
        :param timeout: Request timeout in seconds
        :return: List of deleted usernames
        """
        params = {}
        if expired_after is not None:
            params["expired_after"] = expired_after.isoformat()
        if expired_before is not None:
            params["expired_before"] = expired_before.isoformat()

        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/users/expired",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response
