from app.agents.base_agent import BaseAgent


class TriagingAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "Triaging Agent"
        )


    def process(
        self,
        context: dict
    ) -> dict:


        print(
            "\n[Triaging Agent] Analysing incident..."
        )


        description = context.get(
            "description",
            ""
        ).lower()



        # Incident classification

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



        # Master Orchestrator will decide next agents

        context["next_agents"] = [
            "Master Orchestrator"
        ]



        if "agent_outputs" not in context:

            context["agent_outputs"] = {}



        context["agent_outputs"]["triaging"] = {


            "category":
                category,


            "priority":
                priority,


            "decision":
                "Send incident to Master Orchestrator for dynamic routing"

        }



        return context