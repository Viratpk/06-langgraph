from langchain_core.messages import HumanMessage

from graph import graph


while True:
    question = input("\nAsk > ")

    if question.lower() == "exit":
        break

    response = graph.invoke({"messages": [HumanMessage(content=question)]})

    print("\n========== RESPONSE ==========\n")

    print(response["messages"][-1].content)
