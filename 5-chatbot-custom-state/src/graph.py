from src.model import State
from langgraph.graph import StateGraph, START, END
from src.memory import memory
from src.tools.tavily_tool import tool_node, route_tools
from src.llm import chat_node

graph_builder = StateGraph(State)

# tavily search tool node
graph_builder.add_node("tools", tool_node)

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever the node is used.
graph_builder.add_node("chatbot", chat_node)
graph_builder.add_edge(START, "chatbot")

# The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "END" if
# it is fine directly responding. This conditional routing defines the main agent loop.
graph_builder.add_conditional_edges(
    "chatbot",
    route_tools,
    # The following dictionary lets you tell the graph to interpret the condition's outputs as a specific node
    # It defaults to the identity function, but if you
    # want to use a node named something else apart from "tools",
    # You can update the value of the dictionary to something else
    # e.g., "tools": "my_tools"
    {"tools": "tools", END: END},
)

# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge("tools", "chatbot")

graph = graph_builder.compile(checkpointer=memory)
