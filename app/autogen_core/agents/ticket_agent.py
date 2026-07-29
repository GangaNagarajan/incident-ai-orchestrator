from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage
from app.agents.ticket_agent import TicketAgent



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


        updated_context = self.business_agent.process(
            message.context
        )


        # Convert IncidentContext object to dict
        if hasattr(updated_context, "model_dump"):

            updated_context = updated_context.model_dump()


        elif hasattr(updated_context, "__dict__"):

            updated_context = updated_context.__dict__



        message.context = updated_context



        print(
            "Sending incident to Triaging Agent..."
        )


        await self.send_message(

            message,

            AgentId(
                "triaging",
                "default"
            )

        )