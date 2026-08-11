from autogen_core import AgentId

from app.autogen_core.runtime import runtime
from app.autogen_core.messages import IncidentMessage


class IncidentOrchestratorService:

    async def process_incident(
        self,
        incident
    ):

        context = {

            "incident_id":
                incident.incident_id,

            "title":
                incident.title,

            "description":
                incident.description,

            "application":
                incident.application,

            "environment":
                incident.environment,

            "status":
                incident.status,

            "agent_outputs":
                {}
        }

        print(
            "\n========== STARTING AI WORKFLOW =========="
        )

        print(
            f"[Orchestrator Service] Sending "
            f"{incident.incident_id} to Ticket Agent"
        )

        await runtime.send_message(

            IncidentMessage(
                context=context
            ),

            AgentId(
                "ticket",
                "default"
            )
        )

        await runtime.stop_when_idle()

        return context