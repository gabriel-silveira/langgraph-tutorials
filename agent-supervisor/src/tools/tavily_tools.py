from langchain_tavily import TavilySearch
from src.config import TAVILY_API_KEY


web_search = TavilySearch(
    api_key=TAVILY_API_KEY,
    max_results=3
)