import pytest
from aiohttp import web
import sut  # Replace 'your_module' with the name of your Python script (without .py)
from aiohttp.test_utils import TestClient, TestServer

@pytest.mark.asyncio
async def test_fetch_endpoint():
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
        assert 'null' in text.lower()[:20]  # gstatic.com returns HTML content