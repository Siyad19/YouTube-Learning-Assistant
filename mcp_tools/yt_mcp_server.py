from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
# import time
# from monitoring.activity import record_activity

mcp = FastMCP("YouTube Server")


def get_url(yt_url: str):
    yt_id = yt_url.split("https://youtu.be/")[1].split("?")[0]
    return yt_id


@mcp.tool()
def get_transcript(yt_url: str):
    """Get the YouTube video transcript."""
    
    yt_id = get_url(yt_url)
    yt_transcript = YouTubeTranscriptApi()

    transcript = yt_transcript.fetch(
        yt_id,
        languages=["en"]
    )
    text = " ".join(chunk.text for chunk in transcript)

    return text

@mcp.tool()
def video_description(yt_url : str) -> str:
    """Fetch the description of a YouTube video."""

    # configuration options for yt-dlp
    ydl_opts = {
        "quiet": True, # Don't print unnecessary information/logs to the terminal.
        "skip_download": True # Don't download the actual YouTube video.
    }

    # Creating the yt-dlp object
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         # fetches information about that video and store in 'info'.
        info = ydl.extract_info(yt_url, download=False) # Only extract the information. Don't download the video.

    return info.get("description", "No description found.")



# This code is for testing purpose another AIOps project.
# @mcp.tool()
# def get_transcript(yt_url: str, request_id: str = 'unknown'):

#     start_time = time.time()

#     try :
#         yt_id = get_url(yt_url)
#         yt_transcript = YouTubeTranscriptApi()
#         transcript = yt_transcript.fetch(
#             yt_id,
#             languages=["en"]
#         )
#         text = " ".join(chunk.text for chunk in transcript)

#         latency = (time.time() - start_time) * 1000
#         record_activity(
#             request_id=request_id,
#             activity_type="MCP_CALL",
#             component="youtube_transcript",
#             status="SUCCESS",
#             message="Transcript retrieved",
#             latency_ms=latency
#         )
#         print(record_activity)
#         return text

#     except Exception as e:
#         latency = (time.time() - start_time) * 1000
#         record_activity(
#             request_id=request_id,
#             activity_type="MCP_CALL",
#             component="youtube_transcript",
#             status="ERROR",
#             message=str(e),
#             latency_ms=latency
#         )

#         raise

           

if __name__ == "__main__":
    mcp.run()