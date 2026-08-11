from pathlib import Path
from dotenv import load_dotenv
import os

from google import genai

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

for model in client.models.list():
    print(model.name)