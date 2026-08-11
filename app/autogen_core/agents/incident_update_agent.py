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


        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        message.context = updated_context.model_dump()


        print(
            "[Incident Update Routed Agent] Completed"
        )


        print(
            "\n========== INCIDENT FINAL RESULT =========="
        )


        print(
            message.context
        )

        print("\n========== FINAL AI RESULT ==========")

        import json

        print(
    json.dumps(
        message.context,
        indent=2
    )
)