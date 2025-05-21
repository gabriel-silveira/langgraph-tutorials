from langgraph.prebuilt import create_react_agent
from src.llm import llm
from src.tools.tavily_tools import web_search
from src.prompts.agent_prompt import agent_prompt


research_agent = create_react_agent(
    model=llm,
    tools=[web_search],
    prompt=agent_prompt,
    name="research_agent",
)