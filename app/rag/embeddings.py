import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")


class EmbeddingModel:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-embedding-001"

    def generate_embedding(
        self,
        text: str
    ):

        response = self.client.models.embed_content(
            model=self.model,
            contents=text
        )

        return response.embeddings[0].values