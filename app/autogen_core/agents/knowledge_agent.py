from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.knowledge_agent import KnowledgeAgent

from app.schemas.agent_context_schema import IncidentContext



class KnowledgeRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Knowledge Routed Agent"
        )

        self.business_agent = KnowledgeAgent()



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== Knowledge Routed Agent ==========\n"
        )


        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        message.context = updated_context.model_dump()


        print(
            "[Knowledge Routed Agent] Completed"
        )


        # Send result back to orchestrator

        await self.send_message(
            IncidentMessage(
                context=message.context
            ),
            AgentId(
                "orchestrator",
                "default"
            )
)