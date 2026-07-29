from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler
)

from app.autogen_core.messages import IncidentMessage

from app.agents.rca_agent import RCAAgent



class RCARoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "RCA Routed Agent"
        )


        self.business_agent = RCAAgent()



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== RCA Routed Agent =========="
        )


        updated_context = self.business_agent.process(
            message.context
        )


        message.context = updated_context


        print(
            "[RCA Routed Agent] Completed"
        )