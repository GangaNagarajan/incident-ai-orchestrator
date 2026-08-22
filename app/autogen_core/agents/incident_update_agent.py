from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler
)

from app.autogen_core.messages import IncidentMessage

from app.agents.incident_update_agent import IncidentUpdateAgent

from app.schemas.agent_context_schema import IncidentContext


class IncidentUpdateRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Incident Update Routed Agent"
        )

        self.business_agent = IncidentUpdateAgent()


    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:

        print(
            "\n========== Incident Update Routed Agent ==========\n"
        )

        # -----------------------------------------
        # Convert incoming dictionary to context
        # -----------------------------------------

        if isinstance(
            message.context,
            IncidentContext
        ):

            context = message.context

        else:

            context = IncidentContext(
                **message.context
            )

        # -----------------------------------------
        # Execute final database update
        # -----------------------------------------

        updated_context = self.business_agent.process(
            context
        )

        # -----------------------------------------
        # Convert context back to dictionary
        # -----------------------------------------

        if hasattr(
            updated_context,
            "model_dump"
        ):

            message.context = (
                updated_context.model_dump()
            )

        elif isinstance(
            updated_context,
            dict
        ):

            message.context = (
                updated_context
            )

        elif hasattr(
            updated_context,
            "__dict__"
        ):

            message.context = (
                updated_context.__dict__
            )

        else:

            raise TypeError(
                "IncidentUpdateAgent returned "
                f"unsupported context type: "
                f"{type(updated_context)}"
            )

        # -----------------------------------------
        # Final logging
        # -----------------------------------------

        print(
            "[Incident Update Routed Agent] Completed"
        )

        print(
            "\n========== INCIDENT FINAL RESULT =========="
        )

        print(
            message.context
        )

        print(
            "\n========== FINAL AI RESULT =========="
        )

        import json

        print(
            json.dumps(
                message.context,
                indent=2,
                default=str
            )
        )