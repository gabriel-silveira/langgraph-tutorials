from src.agents.research_agent import research_agent
from src.services.pretty_print import pretty_print_messages


if __name__ == "__main__":
    for chunk in research_agent.stream(
        {"messages": [{"role": "user", "content": "who is the mayor of NYC?"}]}
    ):
        pretty_print_messages(chunk)