from fastapi import FastAPI
from pydantic import BaseModel
from mcp_tools.mcp_client import fetch_transcript
from tools.embeddings import create_vectorstore
from graph.workflow import workflow
import asyncio

app = FastAPI()

# define and validate the structure of incoming data.
class Question(BaseModel):
    yt_url: str # youtube url
    question: str # user query

@app.get("/")
def hello():
    return {"youtube learning assistant API is running."}

@app.post("/ask")
def ask_question(data : Question):

    # yt video into transcript using the mcp tool
    transcript = asyncio.run(
        fetch_transcript(data.yt_url)
    )

    # stored inside the vector database
    vector_store = create_vectorstore(transcript)

    # state for LangGraph nodes
    state = {
        "yt_url": data.yt_url,
        "transcript": transcript,
        "vector_store": vector_store,
        "request": data.question,
        "question": data.question,
        "result": ""
    }

    # run LanGraph workflow
    result = workflow.invoke(state)

    return {
        "answer": result["result"]
    }