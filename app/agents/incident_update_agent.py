from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class IncidentUpdateAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Incident Update Agent"
        )


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            f"\n[{self.name}] Updating incident..."
        )


        rca = context.agent_outputs.get(
            "rca",
            {}
        )


        recommendation = context.agent_outputs.get(
            "recommendation",
            {}
        )


        update_payload = {


            "incident_id":

                context.incident_id,


            "status":

                "IN_PROGRESS",


            "summary":

                f"""
Root Cause:
{rca.get('root_cause')}

Recommended Actions:
{recommendation.get('recommended_actions')}
""",


            "updated_by":

                "Incident AI Orchestrator"

        }



        context.agent_outputs["incident_update"] = update_payload



        print(
            f"[{self.name}] Incident updated successfully"
        )


        return context