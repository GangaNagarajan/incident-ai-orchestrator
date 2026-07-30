from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    DefaultTopicId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.recommendation_agent import RecommendationAgent

from app.schemas.agent_context_schema import IncidentContext



class RecommendationRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Recommendation Routed Agent"
        )

        self.business_agent = RecommendationAgent()



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== Recommendation Routed Agent ==========\n"
        )


        # Convert dict from AutoGen message
        # back to IncidentContext object

        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        # Convert Pydantic object back to dict
        # for next AutoGen message

        message.context = updated_context.model_dump()


        print(
            "[Recommendation Routed Agent] Completed"
        )


        await self.publish_message(
            IncidentMessage(
                context=message.context
            ),
            topic_id=DefaultTopicId("approval")
        )