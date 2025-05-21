from src.graphs.multi_agent_supervisor_graph import supervisor_graph
from src.services.pretty_print import pretty_print_messages


if __name__ == "__main__":
  for chunk in supervisor_graph.stream(
    {
      "messages": [
      {
          "role": "user",
          "content": "find US and California state GDP in 2024. what % of US GDP was California state?",
      }
    ]
  }
  ):
    pretty_print_messages(chunk, last_message=True)

  final_message_history = chunk["supervisor"]["messages"]

  for message in final_message_history:
    message.pretty_print()