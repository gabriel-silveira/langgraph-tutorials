from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY
)