from state import State


def chatbot(state: State):
    print("\n===== CHATBOT NODE =====")

    print("Input State:", state)

    return {"message": f"LangGraph says: {state['message']}"}
