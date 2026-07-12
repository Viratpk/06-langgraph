import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from tools import tools

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3-32b",
    api_key=os.getenv("GROQ_API_KEY"),
)

llm = llm.bind_tools(tools)


def chatbot(state):
    return {"messages": [llm.invoke(state["messages"])]}
