from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class MonitoringAgent:

    def __init__(self):

        self.name = "Monitoring Agent"


    def process(self, context):

        print(
            "\n[Monitoring Agent] Checking application health..."
        )


        monitoring_result = {

            "health_status": "FAILED",

            "database_status": "DOWN",

            "error": "Database connection timeout"

        }


        print(
            "[Monitoring Agent] Health check completed"
        )


        if "agent_outputs" not in context:

            context["agent_outputs"] = {}


        context["agent_outputs"]["monitoring"] = monitoring_result


        return context