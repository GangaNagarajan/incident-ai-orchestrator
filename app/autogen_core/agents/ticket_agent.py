from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage
from app.agents.ticket_agent import TicketAgent
from app.schemas.agent_context_schema import IncidentContext


class TicketRoutedAgent(RoutedAgent):

    def __init__(self):

        super().__init__(
            "Ticket Routed Agent"
        )

        self.business_agent = TicketAgent()


    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:

        print(
            "\n========== Ticket Routed Agent ==========\n"
        )

        # -------------------------------------------------
        # Convert message context dict -> IncidentContext
        # -------------------------------------------------

        context = IncidentContext(
            **message.context
        )

        # -------------------------------------------------
        # Process using business agent
        # -------------------------------------------------

        updated_context = self.business_agent.process(
            context
        )

        # -------------------------------------------------
        # Convert IncidentContext -> dict
        # -------------------------------------------------

        message.context = (
            updated_context.model_dump()
        )

        print(
            "Sending incident to Triaging Agent..."
        )

        # -------------------------------------------------
        # Send to next agent
        # -------------------------------------------------

        await self.send_message(

            IncidentMessage(
                context=message.context
            ),

            AgentId(
                "triaging",
                "default"
            )
        )