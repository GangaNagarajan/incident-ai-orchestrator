from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.triaging_agent import TriagingAgent



class TriagingRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Triaging Routed Agent"
        )

        self.business_agent = TriagingAgent()



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== Triaging Routed Agent =========="
        )


        updated_context = self.business_agent.process(
            message.context
        )


        message.context = updated_context



        print(
            "Routing to Monitoring and Knowledge Agents..."
        )



        # Send to Monitoring Agent

        await self.send_message(

            IncidentMessage(
                context=message.context
            ),

            AgentId(
                "monitoring",
                "default"
            )

        )



        # Send to Knowledge Agent

        await self.send_message(

            IncidentMessage(
                context=message.context
            ),

            AgentId(
                "knowledge",
                "default"
            )

        )