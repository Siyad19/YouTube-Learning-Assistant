from typing import TypedDict

class State(TypedDict):
    transcript: str
    vector_store: object
    question: str
    request: str
    result: str