import aiohttp
from aiohttp import web

async def fetch_url():
    url = "http://gstatic.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Check HTTP status
            if response.status == 200:
                content = await response.text()
                print(f"Success! Response (first 100 chars): {content[:100]}")
                return content
            else:
                print(f"Request failed with status: {response.status}")

# Web application setup
app = web.Application()

# POST endpoint handler
async def handle_fetch(request):
    result = await fetch_url()
    return web.json_response(result)

# Configure routes
app.router.add_post('/fetch', handle_fetch)

# Run the server
if __name__ == "__main__":
    web.run_app(app, port=8080)
# Run the async function
#if __name__ == "__main__":
#    asyncio.run(fetch_url())