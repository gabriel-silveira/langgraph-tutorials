from src.model import State
from langgraph.graph import StateGraph, START
from langchain.chat_models import init_chat_model


graph_builder = StateGraph(State)

llm = init_chat_model(
    model_provider="openai",
    model="gpt-4o-mini",
    temperature=0.7,
)


def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [{"role": "assistant", "content": response.content}]}


# The first argument is the unique node name
# The second argument is the function or object that will be called whenever the node is used.
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile()
