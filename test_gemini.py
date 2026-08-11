from dotenv import load_dotenv

load_dotenv()

from app.llm.gemini_client import GeminiClient


client = GeminiClient()


response = client.client.models.generate_content(

    model=client.model,

    contents="Say Hello in JSON only"

)


print(response.text)