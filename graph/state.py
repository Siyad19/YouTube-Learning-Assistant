from typing import TypedDict

class State(TypedDict):
    yt_url: str
    transcript: str
    vector_store: object
    question: str
    request: str
    result: str