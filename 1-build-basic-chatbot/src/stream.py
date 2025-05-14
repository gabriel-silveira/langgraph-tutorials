from src.graph import graph


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print(f"\nAssistant:{value['messages'][-1]['content']}")