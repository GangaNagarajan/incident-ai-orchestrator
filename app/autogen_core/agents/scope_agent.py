from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.scope_agent import ScopeAgent

from app.schemas.agent_context_schema import IncidentContext

from app.database.database import SessionLocal
from app.services.incident_service import IncidentService


class ScopeRoutedAgent(RoutedAgent):

    def __init__(self):

        super().__init__(
            "Scope Routed Agent"
        )

        self.business_agent = ScopeAgent()
        self.incident_service = IncidentService()


    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:

        print(
            "\n========== Scope Routed Agent ==========\n"
        )

        context = IncidentContext(
            **message.context
        )


        # -----------------------------------------
        # Run scope validation
        # -----------------------------------------

        updated_context = self.business_agent.process(
            context
        )

        message.context = (
            updated_context.model_dump()
        )


        # -----------------------------------------
        # Read scope result
        # -----------------------------------------

        scope = (
            message.context
            .get("agent_outputs", {})
            .get("scope", {})
        )

        is_incident = scope.get(
            "is_incident",
            True
        )

        reason = scope.get(
            "reason",
            "Request is not an enterprise IT incident."
        )


        # -----------------------------------------
        # Reject non-incident
        # -----------------------------------------

        if not is_incident:

            print(
                "[Scope Routed Agent] "
                "Non-incident request rejected"
            )

            print(
                f"[Scope Routed Agent] Reason: {reason}"
            )


            # -----------------------------------------
            # Persist REJECTED status
            # -----------------------------------------

            db = SessionLocal()

            try:

                self.incident_service.update_incident(
                    db,
                    context.incident_id,
                    {
                        "analysis_status": "REJECTED",
                        "rejection_reason": reason,
                        "analysis_error": None
                    }
                )

                db.commit()

            finally:

                db.close()


            # -----------------------------------------
            # Stop workflow
            # -----------------------------------------

            return


        # -----------------------------------------
        # Valid enterprise incident
        # -----------------------------------------

        print(
            "[Scope Routed Agent] "
            "Valid enterprise incident"
        )


        await self.send_message(
            IncidentMessage(
                context=message.context
            ),
            AgentId(
                "orchestrator",
                "default"
            )
        )