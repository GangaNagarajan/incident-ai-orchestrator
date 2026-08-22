import traceback

from autogen_core import AgentId

from app.autogen_core.runtime import runtime
from app.autogen_core.messages import IncidentMessage

from app.database.database import SessionLocal
from app.services.incident_service import IncidentService


class IncidentOrchestratorService:

    def __init__(self):

        self.incident_service = IncidentService()


    async def process_incident(
        self,
        incident
    ):

        incident_id = incident.incident_id

        db = SessionLocal()

        try:

            # -----------------------------------------
            # Mark workflow as RUNNING
            # -----------------------------------------

            self.incident_service.update_incident(
                db,
                incident_id,
                {
                    "analysis_status": "RUNNING",
                    "analysis_error": None,
                    "rejection_reason": None
                }
            )

            print(
                "\n========== STARTING AI WORKFLOW =========="
            )

            print(
                f"[Orchestrator Service] Sending "
                f"{incident_id} to Scope Agent"
            )

            # -----------------------------------------
            # Build Incident Context
            # -----------------------------------------

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

                "priority":
                    incident.priority,

                "category":
                    None,

                "next_agents":
                    [],

                "agent_outputs":
                    {}

            }

            # -----------------------------------------
            # Start workflow
            # -----------------------------------------

            await runtime.send_message(

                IncidentMessage(
                    context=context
                ),

                AgentId(
                    "scope",
                    "default"
                )
            )

            # -----------------------------------------
            # IMPORTANT
            #
            # Do NOT call runtime.stop_when_idle() here.
            #
            # The AutoGen runtime is a long-running application
            # runtime. The routed agents continue their workflow
            # after this message is delivered.
            #
            # The final IncidentUpdate agent is responsible for
            # persisting the final AI results.
            # -----------------------------------------

            print(
                f"[Orchestrator Service] "
                f"AI workflow dispatched for {incident_id}"
            )

            return {

                "incident_id":
                    incident_id,

                "analysis_status":
                    "RUNNING",

                "message":
                    "Incident AI workflow started"

            }

        except Exception as ex:

            # -----------------------------------------
            # Workflow dispatch failure
            # -----------------------------------------

            error_message = str(ex)

            print(
                f"[Orchestrator Service] "
                f"AI workflow FAILED: {error_message}"
            )

            traceback.print_exc()

            try:

                self.incident_service.update_incident(
                    db,
                    incident_id,
                    {
                        "analysis_status":
                            "FAILED",

                        "analysis_error":
                            error_message
                    }
                )

            except Exception as db_error:

                print(
                    "[Orchestrator Service] "
                    "Could not persist FAILED status: "
                    f"{db_error}"
                )

            return {

                "incident_id":
                    incident_id,

                "analysis_status":
                    "FAILED",

                "error":
                    error_message

            }

        finally:

            db.close()