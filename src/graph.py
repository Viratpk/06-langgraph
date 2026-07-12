from langgraph.graph import START
from langgraph.graph import StateGraph
from langgraph.graph import END

from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

from state import State
from chatbot import chatbot
from tools import tools


builder = StateGraph(State)

builder.add_node("chatbot", chatbot)

builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

builder.add_edge("tools", "chatbot")

graph = builder.compile()
