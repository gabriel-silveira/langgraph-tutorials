from langchain.chat_models import init_chat_model
from src.config import OPENAI_API_KEY
from src.model import State

llm = init_chat_model(
    model_provider="openai",
    model="gpt-4o-mini",
    temperature=0.7,
    openai_api_key=OPENAI_API_KEY,
)

# Modification: tell the LLM which tools it can call
# highlight-next-line
# llm_with_tools = llm.bind_tools([tavily_tool])


def chat_node(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [{"role": "assistant", "content": response.content}]}
