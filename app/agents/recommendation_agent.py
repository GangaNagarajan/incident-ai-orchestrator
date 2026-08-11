from app.schemas.agent_context_schema import IncidentContext

from app.llm.llm_factory import LLMFactory


class RecommendationAgent:


    def __init__(self):

        self.client = LLMFactory.get_client()


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            "\n[Recommendation Agent] Generating recommendations using Gemini..."
        )


        try:

            response = self.client.recommend(
                context.model_dump()
            )

        except Exception as ex:

            import traceback

            print(f"[Recommendation Agent] LLM Error : {ex}")
            traceback.print_exc()

            response = {

                "recommended_actions": [

                    "Review application logs",

                    "Investigate monitoring alerts",

                    "Validate infrastructure health"

                ],

                "automation_possible": False,

                "requires_approval": True

            }


        context.agent_outputs["recommendation"] = response


        print(
            "[Recommendation Agent] Completed"
        )


        return context