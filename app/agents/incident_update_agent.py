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

        # -----------------------------------------
        # Read final agent outputs
        # -----------------------------------------

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

        # -----------------------------------------
        # Build final incident summary
        # -----------------------------------------

        summary = f"""
Root Cause:
{rca.get("root_cause")}

Recommended Actions:
{recommendation.get("recommended_actions")}
"""

        # -----------------------------------------
        # Persist final AI result
        # -----------------------------------------

        db = SessionLocal()

        try:

            result = self.service.update_ai_result(

                db,

                context.incident_id,

                {

                    # Incident business status
                    "status":
                        "IN_PROGRESS",

                    # AI workflow status
                    "analysis_status":
                        "COMPLETED",

                    # Clear any previous error
                    "analysis_error":
                        None,

                    # Clear rejection because workflow completed
                    "rejection_reason":
                        None,

                    # RCA
                    "root_cause":
                        rca.get(
                            "root_cause"
                        ),

                    "confidence":
                        str(
                            rca.get(
                                "confidence"
                            )
                        ),

                    # Knowledge
                    "knowledge":
                        json.dumps(
                            knowledge
                        ),

                    # Recommendations
                    "recommendations":
                        json.dumps(
                            recommendation
                        ),

                    # Approval
                    "approval_status":
                        approval.get(
                            "approval_status"
                        ),

                    # Human-readable summary
                    "incident_summary":
                        summary

                }

            )

            if result is None:

                raise RuntimeError(
                    f"Incident {context.incident_id} "
                    "was not found while saving AI results."
                )

            print(
                "[Incident Update Agent] "
                "Database updated successfully"
            )

            print(
                f"[Incident Update Agent] "
                f"Analysis status: {result.analysis_status}"
            )

            print(
                f"[Incident Update Agent] "
                f"Approval status: {result.approval_status}"
            )

        finally:

            db.close()

        # -----------------------------------------
        # Add final workflow result to context
        # -----------------------------------------

        context.agent_outputs["incident_update"] = {

            "status":
                "IN_PROGRESS",

            "analysis_status":
                "COMPLETED",

            "updated_by":
                "Incident AI Orchestrator"

        }

        return context