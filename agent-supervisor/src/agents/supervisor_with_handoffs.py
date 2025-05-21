from langgraph.prebuilt import create_react_agent
from src.tools.handoff_tool import assign_to_research_agent, assign_to_math_agent
from src.prompts.supervisor_prompt import supervisor_prompt
from src.llm import llm


supervisor_agent = create_react_agent(
  model=llm,
  tools=[assign_to_research_agent, assign_to_math_agent],
  prompt=supervisor_prompt,
  name="supervisor",
)