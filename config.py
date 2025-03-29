# config.py
from dotenv import load_dotenv
import os
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai

# Load environment variables
load_dotenv()  # Looks for .env in current directory

# ================== API KEYS ==================
API_KEYS = {
    "ANTHROPIC": os.getenv("ANTHROPIC_API_KEY"),
    "GOOGLE": os.getenv("GOOGLE_API_KEY"),
    "OPENAI": os.getenv("OPENAI_API_KEY"),
    "DEEPSEEK": os.getenv("DEEPSEEK_API_KEY")
}

# ================== CLIENTS ==================
claude_client = Anthropic(api_key=API_KEYS["ANTHROPIC"])
openai_client = OpenAI(api_key=API_KEYS["OPENAI"])
genai.configure(api_key=API_KEYS["GOOGLE"])
deepseek_client = OpenAI(
    api_key=API_KEYS["DEEPSEEK"],
    base_url="https://api.deepseek.com/v1"
)

# Rest of your model config remains the same...
