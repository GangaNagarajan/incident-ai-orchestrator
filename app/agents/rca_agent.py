from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class RCAAgent:


    def __init__(self):

        self.name = "RCA Agent"



    def process(self, context):

        print(
            "\n[RCA Agent] Analysing root cause..."
        )


        monitoring = context["agent_outputs"].get(
            "monitoring",
            {}
        )


        knowledge = context["agent_outputs"].get(
            "knowledge",
            {}
        )


        root_cause = "Unknown"



        if (
            monitoring.get("database_status") == "DOWN"
            and
            knowledge.get("similar_incident")
        ):

            root_cause = (
                "Database connection pool exhausted"
            )



        rca_result = {

            "root_cause": root_cause,

            "confidence": 0.95,

            "evidence": [

                "Database reported DOWN",

                f"Matched historical incident {knowledge.get('similar_incident')}"

            ]

        }



        print(
            f"[RCA Agent] Root Cause : {root_cause}"
        )


        print(
            "[RCA Agent] Confidence : 0.95"
        )



        if "agent_outputs" not in context:

            context["agent_outputs"] = {}



        context["agent_outputs"]["rca"] = rca_result



        return context