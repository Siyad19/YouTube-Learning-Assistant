from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.5
)

def give_answers(state):

    question = state["question"]
    vector_store = state["vector_store"]


    docs = vector_store.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an expert in answering questions based on the provided context.

    Context: 
    {context}

    Question: 
    {question}

    If the answer is not present in the context, respond with "I don't know."
    """
    response = llm.invoke(prompt)
    return {
        "result" : response.content 
    }