from src.agents.math_agent import math_agent
from src.services.pretty_print import pretty_print_messages


if __name__ == "__main__":
    for chunk in math_agent.stream(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 7"}]}
    ):
        pretty_print_messages(chunk)