from app.schemas.agent_context_schema import IncidentContext

from app.llm.llm_factory import LLMFactory
from app.llm.response_parser import RCAResponseParser


class RCAAgent:

    def __init__(self):

        self.client = LLMFactory.get_client()

    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:

        print(
            "\n[RCA Agent] Analysing root cause using Gemini..."
        )

        try:

            response = self.client.analyze(
                context.model_dump()
            )

            rca = RCAResponseParser.parse(
                response
            )

        except Exception as ex:

            import traceback

            print(f"[RCA Agent] LLM Error : {ex}")
            traceback.print_exc()

            rca = {

                "root_cause":
                    "Unable to determine root cause",

                "confidence":
                    0.0,

                "business_impact":
                    "Unknown",

                "evidence":
                    [],

                "immediate_actions":
                    [],

                "permanent_actions":
                    [],

                "risk":
                    "Unknown",

                "affected_component":
                    "Unknown"

            }

        context.agent_outputs["rca"] = rca

        print(
            "[RCA Agent] Root Cause :",
            rca["root_cause"]
        )

        print(
            "[RCA Agent] Confidence :",
            rca["confidence"]
        )

        print(
            "[RCA Agent] Evidence :",
            rca["evidence"]
        )

        return context