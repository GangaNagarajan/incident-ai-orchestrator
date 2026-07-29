from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class RecommendationAgent(BaseAgent):

    def __init__(self):
        super().__init__("Recommendation Agent")


    def process(
        self,
        context: IncidentContext
    ):

        print(
            f"\n[{self.name}] Generating resolution recommendations..."
        )


        rca_result = context.agent_outputs.get(
            "rca",
            {}
        )


        root_cause = rca_result.get(
            "root_cause",
            ""
        )


        recommendations = []

        automation_possible = False

        requires_approval = True



        if "Database connection pool exhausted" in root_cause:

            recommendations = [

                "Increase database connection pool size",

                "Restart application services after validation",

                "Monitor database connection utilization",

                "Review database timeout configurations"

            ]

            automation_possible = True



        elif "Application service unavailable" in root_cause:

            recommendations = [

                "Check application logs",

                "Restart application service",

                "Validate recent deployments"

            ]

            automation_possible = True



        else:

            recommendations = [

                "Perform detailed application analysis",

                "Check infrastructure health",

                "Review recent changes"

            ]



        context.agent_outputs["recommendation"] = {


            "root_cause_considered":
                root_cause,


            "recommended_actions":
                recommendations,


            "automation_possible":
                automation_possible,


            "requires_approval":
                requires_approval

        }


        print(
            f"[{self.name}] Recommendations generated"
        )


        return context