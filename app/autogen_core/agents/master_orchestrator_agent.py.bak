from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    DefaultTopicId
)

from app.autogen_core.messages import IncidentMessage

from app.schemas.agent_context_schema import IncidentContext

from app.agents.master_orchestrator_agent import (
    MasterOrchestratorAgent
)



class MasterOrchestratorRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Master Orchestrator Routed Agent"
        )


        self.business_agent = (
            MasterOrchestratorAgent()
        )



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    )-> None:


        print(
            "\n========== Master Orchestrator =========="
        )


        context = IncidentContext(
            **message.context
        )


        updated_context = (
            self.business_agent.process(
                context
            )
        )


        message.context = (
            updated_context.model_dump()
        )


        # send to monitoring

        await self.publish_message(
            IncidentMessage(
                context=message.context
            ),
            topic_id=DefaultTopicId(
                "monitoring"
            )
        )


        # send to knowledge

        await self.publish_message(
            IncidentMessage(
                context=message.context
            ),
            topic_id=DefaultTopicId(
                "knowledge"
            )
        )


        print(
            "[Master Orchestrator] Routing completed"
        )