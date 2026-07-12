import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from tools import tools

load_dotenv()


llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

llm_with_tools = llm.bind_tools(tools)


def chatbot(state):

    return {"messages": [llm_with_tools.invoke(state["messages"])]}
