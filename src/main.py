from langchain_core.messages import HumanMessage

from graph import graph

config = {"configurable": {"thread_id": "virat"}}

while True:
    question = input("Ask > ")

    if question.lower() == "exit":
        break

    for event in graph.stream(
        {"messages": [HumanMessage(content=question)]},
        config=config,
    ):
        for value in event.values():
            if "messages" in value:
                print(value["messages"][-1].content)
