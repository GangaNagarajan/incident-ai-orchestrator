from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
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

        context = IncidentContext(
            **message.context
        )

        updated_context = self.business_agent.process(
            context
        )

        message.context = updated_context.model_dump()

        print(
            "[RCA Routed Agent] Completed"
        )

        print(
            "[RCA Routed Agent] Sending to Recommendation Agent..."
        )

        print(
    "[RCA Routed Agent] Sending to Recommendation Agent..."
)

        await self.send_message(

    IncidentMessage(
        context=message.context
    ),

    AgentId(
        "recommendation",
        "default"
    )
)