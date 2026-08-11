import json
import re


class JSONParser:


    @staticmethod
    def parse(text: str) -> dict:


        if not text:

            raise ValueError("Empty LLM response")


        text = text.strip()


        # Remove Markdown code fences

        text = re.sub(
            r"^```json",
            "",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"^```",
            "",
            text
        )

        text = re.sub(
            r"```$",
            "",
            text
        )


        text = text.strip()


        # Extract JSON object

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:

            raise ValueError("No JSON found in LLM response")


        json_text = text[start:end + 1]


        return json.loads(json_text)