from mcp_client import fetch_description

async def test_mcp():
    url = "https://youtu.be/o4SSoURPODY?si=FWM8i7MayNYgyZd5"
    description = await fetch_description(url)

    assert description is not None