from typing import Optional, Dict
from aiohttp import ClientSession, ClientTimeout


class RequestBase:
    @classmethod
    async def fetch(
        cls,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: int = 10,
    ) -> Dict:
        """
        Perform an HTTP request and return the result.
        :param method: HTTP method (GET, POST, etc.)
        :param url: URL to request
        :param params: Query parameters
        :param data: Request body data
        :param headers: Request headers
        :param timeout: Request timeout in seconds
        :return: Parsed JSON response
        """
        async with ClientSession(timeout=ClientTimeout(total=timeout)) as session:
            async with session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                headers=headers,
            ) as response:
                response.raise_for_status()
                return await response.json()

    @classmethod
    async def get(
        cls,
        url: str,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: int = 10,
    ) -> Dict:
        """
        Perform a GET request.
        :param url: URL to request
        :param params: Query parameters
        :param headers: Request headers
        :param timeout: Request timeout in seconds
        :return: Parsed JSON response
        """
        return await cls.fetch(
            method="GET",
            url=url,
            params=params,
            headers=headers,
            timeout=timeout,
        )

    @classmethod
    async def post(
        cls,
        url: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: int = 10,
    ) -> Dict:
        """
        Perform a POST request.
        :param url: URL to request
        :param data: Request body data
        :param headers: Request headers
        :param timeout: Request timeout in seconds
        :return: Parsed JSON response
        """
        return await cls.fetch(
            method="POST",
            url=url,
            data=data,
            params=params,
            headers=headers,
            timeout=timeout,
        )

    @classmethod
    async def delete(
        cls,
        url: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: int = 10,
    ) -> Dict:
        """
        Perform a DELETE request.
        :param url: URL to request
        :param headers: Request headers
        :param timeout: Request timeout in seconds
        :return: Parsed JSON response
        """
        return await cls.fetch(
            method="DELETE",
            url=url,
            data=data,
            params=params,
            headers=headers,
            timeout=timeout,
        )

    @classmethod
    async def put(
        cls,
        url: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: int = 10,
    ) -> Dict:
        """
        Perform a PUT request.
        :param url: URL to request
        :param data: Request body data
        :param headers: Request headers
        :param timeout: Request timeout in seconds
        :return: Parsed JSON response
        """
        return await cls.fetch(
            method="PUT",
            url=url,
            data=data,
            params=params,
            headers=headers,
            timeout=timeout,
        )
