import json

from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext

from app.database.database import SessionLocal
from app.services.incident_service import IncidentService


class IncidentUpdateAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Incident Update Agent"
        )

        self.service = IncidentService()

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

        knowledge = context.agent_outputs.get(
            "knowledge",
            {}
        )

        approval = context.agent_outputs.get(
            "approval",
            {}
        )

        summary = f"""
Root Cause:
{rca.get("root_cause")}

Recommended Actions:
{recommendation.get("recommended_actions")}
"""

        db = SessionLocal()

        try:

            self.service.update_ai_result(

                db,

                context.incident_id,

                {

                    "status": "IN_PROGRESS",

                    "root_cause": rca.get(
                        "root_cause"
                    ),

                    "confidence": str(
                        rca.get(
                            "confidence"
                        )
                    ),

                    "knowledge": json.dumps(
                        knowledge
                    ),

                    "recommendations": json.dumps(
                        recommendation
                    ),

                    "approval_status": approval.get(
                        "approval_status"
                    ),

                    "incident_summary": summary

                }

            )

            print(
                "[Incident Update Agent] Database updated successfully"
            )

        finally:

            db.close()

        context.agent_outputs["incident_update"] = {

            "status": "IN_PROGRESS",

            "updated_by": "Incident AI Orchestrator"

        }

        return context