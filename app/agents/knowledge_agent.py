from app.agents.base_agent import BaseAgent
from app.schemas.incident_schema import IncidentCreate


class KnowledgeAgent:


    def __init__(self):

        self.name = "Knowledge Agent"



    def process(self, context):


        print(
            "\n[Knowledge Agent] Searching knowledge base..."
        )


        description = context["description"].lower()



        # Simulated knowledge retrieval

        if "database" in description or "connection" in description:

            knowledge_result = {

                "similar_incident": "INC8899",

                "recommended_resolution":
                    "Increase database connection pool size",

                "confidence": 0.93

            }


        else:

            knowledge_result = {

                "similar_incident": None,

                "recommended_resolution":
                    "No matching knowledge article found",

                "confidence": 0.50

            }



        print(
            "[Knowledge Agent] Knowledge retrieval completed"
        )



        # Ensure output container exists

        if "agent_outputs" not in context:

            context["agent_outputs"] = {}



        context["agent_outputs"]["knowledge"] = knowledge_result



        return context