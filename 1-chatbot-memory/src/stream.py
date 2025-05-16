from src.graph import graph

config = {"configurable": {"thread_id": "1"}}


def stream_graph_updates(user_input: str):
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config,
        stream_mode="values",
    ):
        for value in event.values():
            # print(f"Assistant: {event["messages"][-1]["content"]}\n")
            event["messages"][-1].pretty_print()
