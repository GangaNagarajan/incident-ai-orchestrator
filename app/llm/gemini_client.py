import json
import os

from dotenv import load_dotenv
from google import genai

from app.llm.prompt_builder import build_rca_prompt
from app.llm.json_parser import JSONParser

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env", override=True)
#load_dotenv(".env", override=True)


class GeminiClient:


    def __init__(self):

        self.client = genai.Client(

            api_key=os.getenv("GEMINI_API_KEY")

        )

        self.model = os.getenv(

            "GEMINI_MODEL",

            "gemini-2.5-flash"

        )


    def analyze(
        self,
        context: dict
    ) -> dict:


        system_prompt, user_prompt = build_rca_prompt(
            context
        )


        response = self.client.models.generate_content(

            model=self.model,

            contents=f"""
{system_prompt}

{user_prompt}

Return ONLY JSON.
"""

        )


        return JSONParser.parse(
         response.text
        )


    def recommend(
        self,
        context: dict
    ) -> dict:


        prompt = f"""
You are an Incident Resolution Expert.

Incident Context:

{json.dumps(context, indent=2)}

Based on the RCA and monitoring evidence,
recommend resolution actions.

Return ONLY JSON.

{{
    "recommended_actions":[
        "...",
        "...",
        "..."
    ],
    "automation_possible": true,
    "requires_approval": true
}}
"""


        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt

        )


        return JSONParser.parse(
    response.text
)


    def knowledge(
        self,
        context: dict,
        documents: list
    ) -> dict:


        prompt = f"""
You are an Enterprise Incident Knowledge Agent.

Incident:

{json.dumps(context, indent=2)}

Retrieved Enterprise Incidents:

{json.dumps(documents, indent=2)}

Using ONLY the retrieved incidents,

identify

1. similar incidents

2. recommended resolutions

Return ONLY JSON.

{{
    "similar_incidents":[...],
    "recommended_resolutions":[...],
    "source":"Enterprise FAISS Knowledge Base"
}}
"""


        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt

        )


        return JSONParser.parse(
    response.text
)