from datetime import datetime
import random

from duckduckgo_search import DDGS
from langchain_core.tools import tool

from rag import rag_search


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid expression."


@tool
def current_time() -> str:
    """
    Returns current system time.
    """
    return datetime.now().strftime("%I:%M:%S %p")


@tool
def current_date() -> str:
    """
    Returns today's date.
    """
    return datetime.now().strftime("%d %B %Y")


@tool
def random_number(start: int, end: int) -> str:
    """
    Returns a random number between start and end.
    """
    return str(random.randint(start, end))


@tool
def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """

    results = DDGS().text(query, max_results=5)

    output = []

    for result in results:
        output.append(
            f"""
Title: {result["title"]}
Body: {result["body"]}
Link: {result["href"]}
"""
        )

    return "\n\n".join(output)


tools = [
    calculator,
    current_time,
    current_date,
    random_number,
    web_search,
    rag_search,
]
