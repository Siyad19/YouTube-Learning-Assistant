from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(yt_url):

    yt_id = yt_url.split("https://youtu.be/")[1].split("?")[0]  # Extract the video ID from the URL
    yt_transcript = YouTubeTranscriptApi()
    transcript = yt_transcript.fetch(yt_id, languages=["en"])

    text = " ".join(chunk.text for chunk in transcript)
    # print(text)

    return text # print(transcript)

