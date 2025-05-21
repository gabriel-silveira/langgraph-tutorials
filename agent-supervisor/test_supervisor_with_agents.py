from src.agents.supervisor_with_agents import supervisor
from src.services.pretty_print import pretty_print_messages


if __name__ == "__main__":
  for chunk in supervisor.stream(
    {
      "messages": [
        {
            "role": "user",
            "content": "find US and New York state GDP in 2024. what % of US GDP was New York state?",
        }
      ]
    },
  ):
    pretty_print_messages(chunk, last_message=True)

  last_message = chunk["supervisor"]["messages"][-1].content

  print(f"Last message: {last_message}")