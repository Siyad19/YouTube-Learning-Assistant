import pytest
from mcp_client import fetch_transcript

@pytest.mark.asyncio
async def test_fetch_transcript():
    yt_url = "https://youtu.be/oHYtLWbrwUo?si=9j-5hNY7id89CWZ-"
    transcript = await fetch_transcript(yt_url)

    assert transcript is not None
    assert len(transcript) > 0