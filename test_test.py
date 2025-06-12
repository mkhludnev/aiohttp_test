from unittest.mock import AsyncMock, patch

import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer

@pytest.mark.asyncio
async def test_fetch_endpoint():
    # Mock response data
    mock_response_json = {"data": "mocked content"}

    # Create a mock for aiohttp.ClientSession.get
    mock_get = AsyncMock()
    mock_get.return_value.__aenter__.return_value.text = AsyncMock(return_value=str(mock_response_json))
    mock_get.return_value.__aenter__.return_value.status = 666

    # Patch aiohttp.ClientSession.get
    with patch("aiohttp.ClientSession.get", mock_get):
        import sut
        server = TestServer(sut.app)
        async with TestClient(server) as client:
            # Send POST request to /fetch
            resp = await client.post('/fetch')

            # Check response status
            assert resp.status == 200

            # Parse JSON response
            text = await resp.text()
            assert len(text) > 0  # Ensure we received some content

            # Optional: check if it looks like HTML
            assert '666' in text.lower()[:20]  # gstatic.com returns HTML content