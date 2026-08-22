from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage
from app.agents.triaging_agent import TriagingAgent
from app.schemas.agent_context_schema import IncidentContext


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

        # -------------------------------------------------
        # Convert message context dict -> IncidentContext
        # -------------------------------------------------

        context = IncidentContext(
            **message.context
        )

        # -------------------------------------------------
        # Process using business agent
        # -------------------------------------------------

        updated_context = self.business_agent.process(
            context
        )

        # -------------------------------------------------
        # Convert IncidentContext -> dict
        # -------------------------------------------------

        message.context = (
            updated_context.model_dump()
        )

        print(
            f"[Triaging Agent] Category: "
            f"{message.context.get('category')}"
        )

        print(
            f"[Triaging Agent] Priority: "
            f"{message.context.get('priority')}"
        )

        print(
            "Sending incident to Master Orchestrator..."
        )

        # -------------------------------------------------
        # Send to Master Orchestrator
        # -------------------------------------------------

        await self.send_message(

            IncidentMessage(
                context=message.context
            ),

            AgentId(
                "orchestrator",
                "default"
            )
        )