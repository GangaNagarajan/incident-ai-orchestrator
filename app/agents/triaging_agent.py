from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class TriagingAgent:


    def __init__(self):

        self.name = "Triaging Agent"



    def process(self, context):

        print(
            "\n[Triaging Agent] Analysing incident..."
        )


        # AutoGen sends dictionary context
        description = context.get(
            "description",
            ""
        ).lower()



        # Incident classification rules

        if (
            "database" in description
            or "connection" in description
            or "timeout" in description
            or "sql" in description
        ):

            category = "Database Failure"
            priority = "P1"



        elif (
            "api" in description
            or "service" in description
            or "503" in description
            or "500" in description
        ):

            category = "Application Failure"
            priority = "P2"



        elif (
            "network" in description
            or "latency" in description
            or "connection refused" in description
        ):

            category = "Network Failure"
            priority = "P1"



        elif (
            "login" in description
            or "authentication" in description
            or "permission" in description
        ):

            category = "Security / Authentication Failure"
            priority = "P2"



        else:

            category = "Unknown"
            priority = "P3"



        print(
            f"[Triaging Agent] Category: {category}"
        )


        print(
            f"[Triaging Agent] Priority: {priority}"
        )



        # Update incident context

        context["category"] = category

        context["priority"] = priority



        # Maintain agent execution history

        if "next_agents" not in context:

            context["next_agents"] = []



        context["next_agents"] = [
            "Monitoring Agent",
            "Knowledge Agent"
        ]



        if "agent_outputs" not in context:

            context["agent_outputs"] = {}



        context["agent_outputs"]["triaging"] = {


            "category": category,


            "priority": priority,


            "decision":
            "Trigger Monitoring and Knowledge Agents"

        }



        return context