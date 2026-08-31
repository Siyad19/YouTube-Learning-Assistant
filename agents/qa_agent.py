from langchain_groq import ChatGroq
from dotenv import load_dotenv
from mcp_tools.mcp_client import fetch_description
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    # model="llama-3.1-8b-instant",
    model="openai/gpt-oss-20b",
    temperature=0.5
)

async def give_answers(state):

    question = state["question"]
    yt_url = state["yt_url"]
    vector_store = state["vector_store"]


    docs = vector_store.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    description = await fetch_description(yt_url)

    prompt = f"""
    You are an expert in answering questions based on the provided context.

    if user is asking for description of the video then provide the full description of the video.
    Video Description:
    {description}

    Context: 
    {context}

    Question: 
    {question}

    If the answer is not present in the context, respond with "I don't know."
    """
    response = await llm.ainvoke(prompt)

    return {
        "result" : response.content 
    }