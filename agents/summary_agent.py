from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from tools.youtube import *

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=groq_api_key, 
    model="llama-3.1-8b-instant", 
    temperature=0.5
    )

def summarize(state):
    transcript = state["transcript"]

    prompt = f"""
    You are an expert summarizer,
    give me the summary of the following youtube transcript in a concise and clear manner as bullet points.
    Sumarize the following youtube transcript:

    {transcript}"""

    response = llm.invoke(prompt)

    return {
        "result": response.content
    }