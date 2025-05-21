from langgraph_supervisor import create_supervisor
from src.agents.math_agent import math_agent
from src.agents.research_agent import research_agent
from src.prompts.supervisor_prompt import supervisor_prompt
from src.llm import llm


supervisor = create_supervisor(
  model=llm,
  agents=[
    research_agent,
    math_agent,
  ],
  prompt=supervisor_prompt,
  add_handoff_back_messages=True,
  output_mode="full_history",
).compile()