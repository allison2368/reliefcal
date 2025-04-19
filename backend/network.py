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