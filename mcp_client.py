import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def fetch_transcript(yt_link: str):

    server =StdioServerParameters(
        command="python",
        args=["yt_mcp_server.py"]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "get_transcript", 
                {
                    "yt_url": yt_link
                }
            )
            return result.content[0].text
