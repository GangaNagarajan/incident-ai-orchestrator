import json
import os

from openai import OpenAI

from app.llm.prompt_builder import build_rca_prompt


class RCAOpenAIClient:

    def __init__(self):

        self.client = OpenAI(

            api_key=os.getenv("OPENAI_API_KEY")

        )

        self.model = os.getenv(
            "OPENAI_MODEL",
            "gpt-4.1-mini"
        )


    def analyze(
        self,
        context: dict
    ) -> dict:


        system_prompt, user_prompt = (
            build_rca_prompt(context)
        )


        response = self.client.chat.completions.create(

            model=self.model,

            temperature=0.1,

            response_format={
                "type": "json_object"
            },

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ]

        )


        return json.loads(

            response.choices[0].message.content

        )