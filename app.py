# from tools.youtube import get_transcript
import asyncio
from mcp_tools.mcp_client import fetch_transcript
from tools.embeddings import create_vectorstore
from graph.workflow import workflow
import streamlit as st

st.set_page_config(
    page_title="YouTube Learning Assistant",
    page_icon="🎥",
    layout="wide",
)

# Title and description
st.title("YouTube Learning Assistant")
st.write("Enter a English YouTube video URL here.")

# Input field for YouTube URL
url = st.text_input("YouTube Video URL:")

user_input = st.text_input(
    "What would you like to do?",
    placeholder="Example: Summarize this video?"
)

if st.button("Run"):
    # transcript = get_transcript(url)
    transcript = asyncio.run(
        fetch_transcript(url)
    )
    vector_store = create_vectorstore(transcript)

    state = {
        "yt_url": url,
        "transcript": transcript,
        "vector_store": vector_store,
        "request": user_input,
        "question": user_input,
        "result": ""
    }
    with st.spinner("Processing..."):
        result = asyncio.run(
            workflow.ainvoke(state)
        )

    st.write(result["result"])
    print(result["result"])