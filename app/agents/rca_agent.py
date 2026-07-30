from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class RCAAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "RCA Agent"
        )


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            f"\n[{self.name}] Analysing root cause..."
        )


        root_cause = "Unknown"


        confidence = 0.0



        description = context.description.lower()


        if (
            "database" in description
            or
            "connection timeout" in description
        ):

            root_cause = (
                "Database connection pool exhausted"
            )

            confidence = 0.95



        elif "503" in description:

            root_cause = (
                "Application service unavailable"
            )

            confidence = 0.90



        rca_result = {


            "root_cause":
                root_cause,


            "confidence":
                confidence,


            "analysis":

                "Derived from incident description and historical patterns"

        }



        if context.agent_outputs is None:
            context.agent_outputs = {}



        context.agent_outputs["rca"] = rca_result



        print(
            f"[{self.name}] Root Cause : {root_cause}"
        )

        print(
            f"[{self.name}] Confidence : {confidence}"
        )


        return context