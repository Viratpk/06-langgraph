from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """

    try:
        return str(eval(expression))
    except Exception:
        return "Invalid Expression"


tools = [calculator]
