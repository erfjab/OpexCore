from typing import Optional, Dict, Any
from aiohttp import ClientSession, ClientTimeout
from opexcore.core import RequestBase
from .types import (
    OVPanelToken,
    OVPanelCreateUser,
    OVPanelUpdateUser,
    OVPanelResponseModel,
    OVPanelNodeCreate,
    OVPanelNodeStatus,
    OVPanelSettings,
    OVPanelServerInfo,
)


class OVPanelManager(RequestBase):
    """OVPanel API Manager with all endpoints"""

    @classmethod
    def _generate_headers(cls, token: Optional[str] = None) -> Dict[str, str]:
        """Generate headers for API requests"""
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    @classmethod
    async def login(
        cls, host: str, username: str, password: str, timeout: int = 10
    ) -> OVPanelToken:
        """
        Authenticate and obtain an access token.

        :param host: API host URL
        :param username: Admin username
        :param password: Admin password
        :param timeout: Request timeout in seconds
        :return: Token response
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/login",
            data={"username": username, "password": password},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=timeout,
        )
        return OVPanelToken(**response)

    @classmethod
    async def get_all_users(
        cls, host: str, token: str, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        Get all users in the panel.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Response with list of users
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/user/all",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def create_user(
        cls, host: str, token: str, user_data: OVPanelCreateUser, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        Create a new user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User creation data
        :param timeout: Request timeout in seconds
        :return: Response with created user
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/user/create",
            data=user_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def update_user(
        cls, host: str, token: str, user_data: OVPanelUpdateUser, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Update an existing user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User update data
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/user/update",
            data=user_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def change_user_status(
        cls, host: str, token: str, user_data: OVPanelUpdateUser, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        Change the status of a user.

        :param host: API host URL
        :param token: Authentication token
        :param user_data: User update data with status
        :param timeout: Request timeout in seconds
        :return: Response with updated user
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/user/change-status",
            data=user_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def delete_user(
        cls, host: str, token: str, name: str, timeout: int = 10
    ) -> Dict[str, Any]:
        """
        Delete a user by name.

        :param host: API host URL
        :param token: Authentication token
        :param name: Username to delete
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/user/delete/{name}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return response

    @classmethod
    async def get_settings(
        cls, host: str, token: str, timeout: int = 10
    ) -> OVPanelSettings:
        """
        Get panel settings.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Panel settings
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/settings/",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelSettings(**response)

    @classmethod
    async def get_server_info(
        cls, host: str, token: str, timeout: int = 10
    ) -> OVPanelServerInfo:
        """
        Get server information (CPU, memory, etc.).

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Server information
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/settings/server/info",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelServerInfo(**response)

    @classmethod
    async def add_node(
        cls, host: str, token: str, node_data: OVPanelNodeCreate, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        Add a new node to the panel.

        :param host: API host URL
        :param token: Authentication token
        :param node_data: Node creation data
        :param timeout: Request timeout in seconds
        :return: Response with created node
        """
        response = await cls.post(
            url=f"{host.rstrip('/')}/api/node/add",
            data=node_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def update_node(
        cls,
        host: str,
        token: str,
        address: str,
        node_data: OVPanelNodeCreate,
        timeout: int = 10,
    ) -> OVPanelResponseModel:
        """
        Update an existing node.

        :param host: API host URL
        :param token: Authentication token
        :param address: Node address to update
        :param node_data: Node update data
        :param timeout: Request timeout in seconds
        :return: Response with updated node
        """
        response = await cls.put(
            url=f"{host.rstrip('/')}/api/node/update/{address}",
            data=node_data.dict(),
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def get_node_status(
        cls, host: str, token: str, address: str, timeout: int = 10
    ) -> OVPanelNodeStatus:
        """
        Get the status of a specific node.

        :param host: API host URL
        :param token: Authentication token
        :param address: Node address
        :param timeout: Request timeout in seconds
        :return: Node status response
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/node/status/{address}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelNodeStatus(**response)

    @classmethod
    async def list_nodes(
        cls, host: str, token: str, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        List all nodes in the panel.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Response with list of nodes
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/node/list",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def download_ovpn_client(
        cls, host: str, token: str, address: str, name: str, timeout: int = 10
    ) -> bytes:
        """
        Download OVPN client configuration from a node.

        :param host: API host URL
        :param token: Authentication token
        :param address: Node address
        :param name: Client name
        :param timeout: Request timeout in seconds
        :return: OVPN configuration file content
        """
        async with ClientSession(timeout=ClientTimeout(total=timeout)) as session:
            async with session.get(
                url=f"{host.rstrip('/')}/api/node/download/ovpn/{address}/{name}",
                headers=cls._generate_headers(token),
            ) as response:
                response.raise_for_status()
                return await response.read()

    @classmethod
    async def delete_node(
        cls, host: str, token: str, address: str, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        Delete a node by address.

        :param host: API host URL
        :param token: Authentication token
        :param address: Node address to delete
        :param timeout: Request timeout in seconds
        :return: Response data
        """
        response = await cls.delete(
            url=f"{host.rstrip('/')}/api/node/delete/{address}",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)

    @classmethod
    async def get_all_admins(
        cls, host: str, token: str, timeout: int = 10
    ) -> OVPanelResponseModel:
        """
        Get all admins in the panel.

        :param host: API host URL
        :param token: Authentication token
        :param timeout: Request timeout in seconds
        :return: Response with list of admins
        """
        response = await cls.get(
            url=f"{host.rstrip('/')}/api/admin/all",
            headers=cls._generate_headers(token),
            timeout=timeout,
        )
        return OVPanelResponseModel(**response)
