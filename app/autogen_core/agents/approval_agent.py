from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    DefaultTopicId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.approval_agent import ApprovalAgent

from app.schemas.agent_context_schema import IncidentContext



class ApprovalRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Approval Routed Agent"
        )

        self.business_agent = ApprovalAgent()



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== Approval Routed Agent ==========\n"
        )


        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        message.context = updated_context.model_dump()


        print(
            "[Approval Routed Agent] Completed"
        )


        await self.publish_message(
            IncidentMessage(
                context=message.context
            ),
            topic_id=DefaultTopicId("incident_update")
        )