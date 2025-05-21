import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

web_search = TavilySearch(
    api_key=os.getenv('TAVILY_API_KEY'),
    max_results=3
)