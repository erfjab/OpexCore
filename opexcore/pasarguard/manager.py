from typing import Optional, List, Dict, Any
from datetime import datetime
from opexcore.core import RequestBase
from .types import (
    PasarGuardAdminCreate,
    PasarGuardAdminModify,
    PasarGuardAdminDetails,
    PasarGuardToken,
    PasarGuardUserCreate,
    PasarGuardUserModify,
    PasarGuardUserResponse,
    PasarGuardUsersResponse,
    PasarGuardUserStatus,
    PasarGuardSubscriptionUserResponse,
    PasarGuardNodeCreate,
    PasarGuardNodeModify,
    PasarGuardNodeResponse,
    PasarGuardNodeSettings,
    PasarGuardNodeStatus,
    PasarGuardCoreCreate,
    PasarGuardCoreResponse,
    PasarGuardSystemStats,
    PasarGuardGroupCreate,
    PasarGuardGroupModify,
    PasarGuardGroupResponse,
    PasarGuardHostCreate,
    PasarGuardHostResponse,
    PasarGuardUserTemplateCreate,
    PasarGuardUserTemplateModify,
    PasarGuardUserTemplateResponse,
)


class PasarGuardManager(RequestBase):
    """PasarGuard API Manager with all endpoints"""

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
    ) -> PasarGuardToken:
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
        data = await response.json()
        return PasarGuardToken(**data)

    @classmethod
    async def get_current_admin(
        cls, host: str, token: str, timeout: int = 10
    ) -> PasarGuardAdminDetails:
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
        data = await response.json()
        return PasarGuardAdminDetails(**data)

    @classmethod
    async def create_admin(
        cls, host: str, token: str, admin_data: PasarGuardAdminCreate, timeout: int = 10
    ) -> PasarGuardAdminDetails:
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
        data = await response.json()
        return PasarGuardAdminDetails(**data)

    @classmethod
    async def modify_admin(
        cls,
        host: str,
        token: str,
        username: str,
        admin_data: PasarGuardAdminModify,
        timeout: int = 10,
    ) -> PasarGuardAdminDetails:
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
        data = await response.json()
        return PasarGuardAdminDetails(**data)

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
            url=f"{host.rstrip('/')}/api/admin/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_admins(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        username: Optional[str] = None,
        sort: Optional[str] = None,
        timeout: int = 10,
    ) -> List[PasarGuardAdminDetails]:
        """
        Fetch a list of admins with optional filters for pagination and username.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param username: Filter by username
        :param sort: Sort field
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
        if sort is not None:
            params["sort"] = sort

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admins",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [PasarGuardAdminDetails(**item) for item in data]

    @classmethod
    async def reset_admin_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> PasarGuardAdminDetails:
        """
        Resets usage of admin.

        :param host: API host URL
        :param token: Authentication token
        :param username: Admin username
        :param timeout: Request timeout in seconds
        :return: Admin response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/admin/{username}/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardAdminDetails(**data)

    @classmethod
    async def get_system_stats(
        cls,
        host: str,
        token: str,
        admin_username: Optional[str] = None,
        timeout: int = 10,
    ) -> PasarGuardSystemStats:
        """
        Fetch system stats including memory, CPU, and user metrics.

        :param host: API host URL
        :param token: Authentication token
        :param admin_username: Optional admin username filter
        :param timeout: Request timeout in seconds
        :return: System stats response
        """
        params = {}
        if admin_username:
            params["admin_username"] = admin_username

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/system",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardSystemStats(**data)

    @classmethod
    async def get_inbounds(cls, host: str, token: str, timeout: int = 10) -> List[str]:
        """
        Retrieve inbound configurations.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: List of inbound tags
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/inbounds",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def create_group(
        cls, host: str, token: str, group_data: PasarGuardGroupCreate, timeout: int = 10
    ) -> PasarGuardGroupResponse:
        """
        Create a new group.

        :param host: API host URL
        :param token: Authentication token
        :param group_data: Group creation data
        :param timeout: Request timeout in seconds
        :return: Group response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/group",
            data=group_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardGroupResponse(**data)

    @classmethod
    async def get_groups(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: int = 10,
    ) -> List[PasarGuardGroupResponse]:
        """
        List all groups.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param timeout: Request timeout in seconds
        :return: List of group responses
        """
        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/groups",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return (
            [PasarGuardGroupResponse(**item["groups"]) for item in [data]][0]
            if isinstance(data, dict)
            else [PasarGuardGroupResponse(**item) for item in data]
        )

    @classmethod
    async def get_group(
        cls, host: str, token: str, group_id: int, timeout: int = 10
    ) -> PasarGuardGroupResponse:
        """
        Get group details.

        :param host: API host URL
        :param token: Authentication token
        :param group_id: Group ID
        :param timeout: Request timeout in seconds
        :return: Group response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/group/{group_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardGroupResponse(**data)

    @classmethod
    async def modify_group(
        cls,
        host: str,
        token: str,
        group_id: int,
        group_data: PasarGuardGroupModify,
        timeout: int = 10,
    ) -> PasarGuardGroupResponse:
        """
        Modify group.

        :param host: API host URL
        :param token: Authentication token
        :param group_id: Group ID
        :param group_data: Group modification data
        :param timeout: Request timeout in seconds
        :return: Group response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/group/{group_id}",
            data=group_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardGroupResponse(**data)

    @classmethod
    async def remove_group(
        cls, host: str, token: str, group_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove group.

        :param host: API host URL
        :param token: Authentication token
        :param group_id: Group ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/group/{group_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def create_core(
        cls, host: str, token: str, core_data: PasarGuardCoreCreate, timeout: int = 10
    ) -> PasarGuardCoreResponse:
        """
        Create a new core configuration.

        :param host: API host URL
        :param token: Authentication token
        :param core_data: Core creation data
        :param timeout: Request timeout in seconds
        :return: Core response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/core",
            data=core_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardCoreResponse(**data)

    @classmethod
    async def get_core(
        cls, host: str, token: str, core_id: int, timeout: int = 10
    ) -> PasarGuardCoreResponse:
        """
        Get a core configuration by its ID.

        :param host: API host URL
        :param token: Authentication token
        :param core_id: Core ID
        :param timeout: Request timeout in seconds
        :return: Core response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/core/{core_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardCoreResponse(**data)

    @classmethod
    async def modify_core(
        cls,
        host: str,
        token: str,
        core_id: int,
        core_data: PasarGuardCoreCreate,
        restart_nodes: bool = False,
        timeout: int = 10,
    ) -> PasarGuardCoreResponse:
        """
        Update an existing core configuration.

        :param host: API host URL
        :param token: Authentication token
        :param core_id: Core ID
        :param core_data: Core modification data
        :param restart_nodes: Whether to restart nodes
        :param timeout: Request timeout in seconds
        :return: Core response
        """
        params = {"restart_nodes": restart_nodes}
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/core/{core_id}",
            params=params,
            data=core_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardCoreResponse(**data)

    @classmethod
    async def delete_core(
        cls,
        host: str,
        token: str,
        core_id: int,
        restart_nodes: bool = False,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Delete a core configuration.

        :param host: API host URL
        :param token: Authentication token
        :param core_id: Core ID
        :param restart_nodes: Whether to restart nodes
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        params = {"restart_nodes": restart_nodes}
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/core/{core_id}",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_cores(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: int = 10,
    ) -> List[PasarGuardCoreResponse]:
        """
        Get a list of all core configurations.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param timeout: Request timeout in seconds
        :return: List of core responses
        """
        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/cores",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        cores = data.get("cores", []) if isinstance(data, dict) else data
        return [PasarGuardCoreResponse(**item) for item in cores]

    @classmethod
    async def create_host(
        cls, host: str, token: str, host_data: PasarGuardHostCreate, timeout: int = 10
    ) -> PasarGuardHostResponse:
        """
        Create a new host.

        :param host: API host URL
        :param token: Authentication token
        :param host_data: Host creation data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/host/",
            data=host_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardHostResponse(**data)

    @classmethod
    async def get_host(
        cls, host: str, token: str, host_id: int, timeout: int = 10
    ) -> PasarGuardHostResponse:
        """
        Get host by ID.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/host/{host_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardHostResponse(**data)

    @classmethod
    async def modify_host(
        cls,
        host: str,
        token: str,
        host_id: int,
        host_data: PasarGuardHostCreate,
        timeout: int = 10,
    ) -> PasarGuardHostResponse:
        """
        Modify host by ID.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param host_data: Host modification data
        :param timeout: Request timeout in seconds
        :return: Host response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/host/{host_id}",
            data=host_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardHostResponse(**data)

    @classmethod
    async def remove_host(
        cls, host: str, token: str, host_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove host by ID.

        :param host: API host URL
        :param token: Authentication token
        :param host_id: Host ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/host/{host_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_hosts(
        cls,
        host: str,
        token: str,
        offset: int = 0,
        limit: int = 0,
        timeout: int = 10,
    ) -> List[PasarGuardHostResponse]:
        """
        Get proxy hosts.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param timeout: Request timeout in seconds
        :return: List of host responses
        """
        params = {"offset": offset, "limit": limit}
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/hosts",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [PasarGuardHostResponse(**item) for item in data]

    @classmethod
    async def get_node_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> PasarGuardNodeSettings:
        """
        Retrieve the current node settings.

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
        data = await response.json()
        return PasarGuardNodeSettings(**data)

    @classmethod
    async def get_nodes(
        cls,
        host: str,
        token: str,
        core_id: Optional[int] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        status: Optional[List[PasarGuardNodeStatus]] = None,
        enabled: bool = False,
        ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        timeout: int = 10,
    ) -> List[PasarGuardNodeResponse]:
        """
        Retrieve a list of all nodes.

        :param host: API host URL
        :param token: Authentication token
        :param core_id: Filter by core ID
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param status: Filter by status list
        :param enabled: Filter by enabled status
        :param ids: Filter by node IDs
        :param search: Search query
        :param timeout: Request timeout in seconds
        :return: List of node responses
        """
        params = {"enabled": enabled}
        if core_id is not None:
            params["core_id"] = core_id
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if status is not None:
            params["status"] = [s.value for s in status]
        if ids is not None:
            params["ids"] = ids
        if search is not None:
            params["search"] = search

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/nodes",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [PasarGuardNodeResponse(**item) for item in data]

    @classmethod
    async def create_node(
        cls, host: str, token: str, node_data: PasarGuardNodeCreate, timeout: int = 10
    ) -> PasarGuardNodeResponse:
        """
        Create a new node.

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
        data = await response.json()
        return PasarGuardNodeResponse(**data)

    @classmethod
    async def get_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> PasarGuardNodeResponse:
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
        data = await response.json()
        return PasarGuardNodeResponse(**data)

    @classmethod
    async def modify_node(
        cls,
        host: str,
        token: str,
        node_id: int,
        node_data: PasarGuardNodeModify,
        timeout: int = 10,
    ) -> PasarGuardNodeResponse:
        """
        Modify a node's details.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param node_data: Node modification data
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/node/{node_id}",
            data=node_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardNodeResponse(**data)

    @classmethod
    async def remove_node(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Remove a node.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/node/{node_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def reset_node_usage(
        cls, host: str, token: str, node_id: int, timeout: int = 10
    ) -> PasarGuardNodeResponse:
        """
        Reset node traffic usage.

        :param host: API host URL
        :param token: Authentication token
        :param node_id: Node ID
        :param timeout: Request timeout in seconds
        :return: Node response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/node/{node_id}/reset",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardNodeResponse(**data)

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
            url=f"{host.rstrip('/')}/api/node/{node_id}/reconnect",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def create_user_template(
        cls,
        host: str,
        token: str,
        template_data: PasarGuardUserTemplateCreate,
        timeout: int = 10,
    ) -> PasarGuardUserTemplateResponse:
        """
        Create a new user template.

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
        data = await response.json()
        return PasarGuardUserTemplateResponse(**data)

    @classmethod
    async def get_user_template(
        cls, host: str, token: str, template_id: int, timeout: int = 10
    ) -> PasarGuardUserTemplateResponse:
        """
        Get User Template information with id.

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
        data = await response.json()
        return PasarGuardUserTemplateResponse(**data)

    @classmethod
    async def modify_user_template(
        cls,
        host: str,
        token: str,
        template_id: int,
        template_data: PasarGuardUserTemplateModify,
        timeout: int = 10,
    ) -> PasarGuardUserTemplateResponse:
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
            data=template_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardUserTemplateResponse(**data)

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
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/user_template/{template_id}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def get_user_templates(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: int = 10,
    ) -> List[PasarGuardUserTemplateResponse]:
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
            url=f"{host.rstrip('/')}/api/user_templates",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return [PasarGuardUserTemplateResponse(**item) for item in data]

    @classmethod
    async def create_user(
        cls, host: str, token: str, user_data: PasarGuardUserCreate, timeout: int = 10
    ) -> PasarGuardUserResponse:
        """
        Create a new user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User creation data
        :param timeout: Request timeout in seconds
        :return: User response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user",
            data=user_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardUserResponse(**data)

    @classmethod
    async def get_user(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> PasarGuardUserResponse:
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
        data = await response.json()
        return PasarGuardUserResponse(**data)

    @classmethod
    async def modify_user(
        cls,
        host: str,
        token: str,
        username: str,
        user_data: PasarGuardUserModify,
        timeout: int = 10,
    ) -> PasarGuardUserResponse:
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
            data=user_data.dict(exclude_none=True),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardUserResponse(**data)

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
            url=f"{host.rstrip('/')}/api/user/{username}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def reset_user_data_usage(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> PasarGuardUserResponse:
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
        data = await response.json()
        return PasarGuardUserResponse(**data)

    @classmethod
    async def revoke_user_subscription(
        cls, host: str, token: str, username: str, timeout: int = 10
    ) -> PasarGuardUserResponse:
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
        data = await response.json()
        return PasarGuardUserResponse(**data)

    @classmethod
    async def get_users(
        cls,
        host: str,
        token: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        username: Optional[List[str]] = None,
        admin: Optional[List[str]] = None,
        group: Optional[List[int]] = None,
        search: Optional[str] = None,
        status: Optional[PasarGuardUserStatus] = None,
        sort: Optional[str] = None,
        proxy_id: Optional[str] = None,
        load_sub: bool = False,
        timeout: int = 10,
    ) -> PasarGuardUsersResponse:
        """
        Get all users.

        :param host: API host URL
        :param token: Authentication token
        :param offset: Offset for pagination
        :param limit: Limit for pagination
        :param username: Filter by usernames
        :param admin: Filter by admin usernames
        :param group: Filter by group IDs
        :param search: Search query
        :param status: Filter by status
        :param sort: Sort field
        :param proxy_id: Filter by proxy ID
        :param load_sub: Load subscription data
        :param timeout: Request timeout in seconds
        :return: Users response
        """
        params = {"load_sub": load_sub}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if username is not None:
            params["username"] = username
        if admin is not None:
            params["admin"] = admin
        if group is not None:
            params["group"] = group
        if search is not None:
            params["search"] = search
        if status is not None:
            params["status"] = status.value
        if sort is not None:
            params["sort"] = sort
        if proxy_id is not None:
            params["proxy_id"] = proxy_id

        response = await cls.get(
            url=f"{host.rstrip('/')}/api/users",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardUsersResponse(**data)

    @classmethod
    async def set_user_owner(
        cls,
        host: str,
        token: str,
        username: str,
        admin_username: str,
        timeout: int = 10,
    ) -> PasarGuardUserResponse:
        """
        Set a new owner (admin) for a user.

        :param host: API host URL
        :param token: Authentication token
        :param username: Username
        :param admin_username: Admin username
        :param timeout: Request timeout in seconds
        :return: User response
        """
        params = {"admin_username": admin_username}
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/user/{username}/set_owner",
            params=params,
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        data = await response.json()
        return PasarGuardUserResponse(**data)

    @classmethod
    async def get_expired_users(
        cls,
        host: str,
        token: str,
        admin_username: Optional[str] = None,
        expired_after: Optional[datetime] = None,
        expired_before: Optional[datetime] = None,
        timeout: int = 10,
    ) -> List[str]:
        """
        Get users who have expired within the specified date range.

        :param host: API host URL
        :param token: Authentication token
        :param admin_username: Filter by admin username
        :param expired_after: Expired after date
        :param expired_before: Expired before date
        :param timeout: Request timeout in seconds
        :return: List of usernames
        """
        params = {}
        if admin_username:
            params["admin_username"] = admin_username
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
        return await response.json()

    @classmethod
    async def delete_expired_users(
        cls,
        host: str,
        token: str,
        admin_username: Optional[str] = None,
        expired_after: Optional[datetime] = None,
        expired_before: Optional[datetime] = None,
        timeout: int = 10,
    ) -> Dict[str, Any]:
        """
        Delete users who have expired within the specified date range.

        :param host: API host URL
        :param token: Authentication token
        :param admin_username: Filter by admin username
        :param expired_after: Expired after date
        :param expired_before: Expired before date
        :param timeout: Request timeout in seconds
        :return: Response data with deleted users info
        """
        params = {}
        if admin_username:
            params["admin_username"] = admin_username
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
        return await response.json()

    @classmethod
    async def user_subscription(
        cls, host: str, token: str, user_agent: str = "", timeout: int = 10
    ) -> List[str]:
        """
        Provides a subscription link based on the user agent.

        :param host: API host URL
        :param token: Subscription token
        :param user_agent: User agent header
        :param timeout: Request timeout in seconds
        :return: Subscription links
        """
        headers = {}
        if user_agent:
            headers["user-agent"] = user_agent

        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{token}/",
            headers=headers,
            timeout=timeout,
        )
        return await response.json()

    @classmethod
    async def user_subscription_info(
        cls, host: str, token: str, timeout: int = 10
    ) -> PasarGuardSubscriptionUserResponse:
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
        data = await response.json()
        return PasarGuardSubscriptionUserResponse(**data)

    @classmethod
    async def user_subscription_with_client_type(
        cls,
        host: str,
        token: str,
        client_type: str,
        timeout: int = 10,
    ) -> List[str]:
        """
        Provides a subscription link based on the specified client type.

        :param host: API host URL
        :param token: Subscription token
        :param client_type: Client type (links, links_base64, xray, sing_box, clash, clash_meta, outline, block)
        :param timeout: Request timeout in seconds
        :return: Subscription links
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/sub/{token}/{client_type}",
            timeout=timeout,
        )
        return await response.json()
