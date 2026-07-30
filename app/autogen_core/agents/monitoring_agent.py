from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    DefaultTopicId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.monitoring_agent import MonitoringAgent

from app.schemas.agent_context_schema import IncidentContext



class MonitoringRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Monitoring Routed Agent"
        )

        self.business_agent = MonitoringAgent()



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== Monitoring Routed Agent ==========\n"
        )


        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        message.context = updated_context.model_dump()


        print(
            "[Monitoring Routed Agent] Completed"
        )


        # Send result back to orchestrator

        await self.publish_message(
            IncidentMessage(
                context=message.context
            ),
            topic_id=DefaultTopicId("orchestrator")
        )