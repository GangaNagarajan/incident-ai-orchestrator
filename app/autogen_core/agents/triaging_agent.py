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
            "\n========== Triaging Routed Agent ==========\n"
        )


        print(
            "[Triaging Agent] Analysing incident..."
        )


        updated_context = self.business_agent.process(
            message.context
        )


        # Ensure context remains dictionary
        if hasattr(updated_context, "model_dump"):

            updated_context = updated_context.model_dump()


        elif hasattr(updated_context, "__dict__"):

            updated_context = updated_context.__dict__



        message.context = updated_context



        print(
            f"[Triaging Agent] Category: {message.context.get('category')}"
        )


        print(
            f"[Triaging Agent] Priority: {message.context.get('priority')}"
        )


        print(
            "Sending incident to Master Orchestrator..."
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