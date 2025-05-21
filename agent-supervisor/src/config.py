from dotenv import load_dotenv
import os

# Carrega do .env forçando sobrescrita de variáveis existentes
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path, override=True)

# Pega as chaves do .env
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
#print(f"OPENAI_API_KEY do .env: {OPENAI_API_KEY}")

TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
#print(f"TAVILY_API_KEY do .env: {TAVILY_API_KEY}")
