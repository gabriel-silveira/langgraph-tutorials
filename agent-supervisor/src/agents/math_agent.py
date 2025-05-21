from langgraph.prebuilt import create_react_agent
from src.tools.math_tools import add, multiply, divide
from src.llm import llm
from src.prompts.agent_prompt import agent_prompt


math_agent = create_react_agent(
    model=llm,
    tools=[add, multiply, divide],
    prompt=agent_prompt,
    name="math_agent",
)