from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi

mcp = FastMCP("YouTube Server")


def get_url(yt_url: str):
    yt_id = yt_url.split("https://youtu.be/")[1].split("?")[0]
    return yt_id


@mcp.tool()
def get_transcript(yt_url: str):

    yt_id = get_url(yt_url)

    yt_transcript = YouTubeTranscriptApi()

    transcript = yt_transcript.fetch(
        yt_id,
        languages=["en"]
    )

    text = " ".join(chunk.text for chunk in transcript)

    return text


if __name__ == "__main__":
    mcp.run()