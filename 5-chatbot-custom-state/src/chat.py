from src.stream import stream_graph_updates


def chatbot():
    while True:
        try:
            user_input = input("\nUser: ")

            if user_input.lower() in ["exit", "quit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"

            print(f"\nUser: {user_input}")

            stream_graph_updates(user_input)

            break