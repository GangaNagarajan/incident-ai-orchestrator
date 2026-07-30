from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    DefaultTopicId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.rca_agent import RCAAgent

from app.schemas.agent_context_schema import IncidentContext



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
            "\n========== RCA Routed Agent ==========\n"
        )


        # Convert dictionary -> IncidentContext

        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        # Convert IncidentContext -> dictionary

        message.context = updated_context.model_dump()


        print(
            "[RCA Routed Agent] Completed"
        )


        await self.publish_message(
            IncidentMessage(
                context=message.context
            ),
            topic_id=DefaultTopicId("recommendation")
        )