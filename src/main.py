from graph import graph


response = graph.invoke({"message": "Hello LangGraph!"})

print("\n===== FINAL STATE =====")
print(response)
