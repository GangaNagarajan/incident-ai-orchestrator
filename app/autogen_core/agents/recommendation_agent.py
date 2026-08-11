from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
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


        #
        # Convert dictionary to IncidentContext
        #

        context = IncidentContext(
            **message.context
        )


        #
        # Execute Recommendation Agent
        #

        updated_context = self.business_agent.process(
            context
        )


        #
        # Convert back to dictionary
        #

        if hasattr(updated_context, "model_dump"):

            message.context = updated_context.model_dump()

        elif hasattr(updated_context, "__dict__"):

            message.context = updated_context.__dict__

        else:

            message.context = updated_context


        print(
            "[Recommendation Routed Agent] Completed"
        )

        print(
            "[Recommendation Routed Agent] Sending to Approval Agent..."
        )


        #
        # Send directly to Approval Agent
        #

        await self.send_message(

            IncidentMessage(
                context=message.context
            ),

            AgentId(
                "approval",
                "default"
            )

        )