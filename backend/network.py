"""Make a GET request to a URL"""
from typing import Any

import httpx

USER_AGENT = "team-moomoo-app/1.0"

async def make_request(url: str, headers: dict[str, Any] = {}) -> dict[str, Any] | None:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        **headers,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        
async def make_request_post(url: str, headers: dict[str, Any] = {}, data: dict[str, Any] = None) -> dict[str, Any] | None:
    """
    Makes an asynchronous POST request to the specified URL.

    Args:
        url: The URL to send the POST request to.
        headers: Optional dictionary of HTTP headers.
        data: Optional dictionary to be sent as the JSON body.

    Returns:
        The JSON response if successful, None otherwise.
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        **headers,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=data, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"HTTP error at {url}: {exc}")
            return None
        except httpx.RequestError as exc:
            print(f"Request error at {url}: {exc}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during POST request to {url}: {e}")
            return None