from langgraph.graph import START, END, StateGraph, MessagesState
from src.agents.supervisor_with_handoffs import supervisor_agent
from src.agents.research_agent import research_agent
from src.agents.math_agent import math_agent


# define the multi-agent supervisor graph
supervisor_graph = (
    StateGraph(MessagesState)
    # NOTE: `destinations` is only needed for visualization and doesn't affect runtime behavior
    .add_node(supervisor_agent, destinations=("research_agent", "math_agent", END))
    .add_node(research_agent)
    .add_node(math_agent)

    # start at the supervisor
    .add_edge(START, supervisor_agent.name)

    # always return back to the supervisor
    .add_edge(research_agent.name, supervisor_agent.name)
    .add_edge(math_agent.name, supervisor_agent.name)

    .compile()
)