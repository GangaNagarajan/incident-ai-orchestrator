from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler
)


from app.autogen_core.messages import IncidentMessage

from app.agents.knowledge_agent import KnowledgeAgent

from app.autogen_core.state import incident_state

from autogen_core import AgentId

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
            "\n========== Knowledge Routed Agent =========="
        )


        updated_context = self.business_agent.process(
            message.context
        )


        incident_state.update_context(
            updated_context
        )


        incident_state.mark_completed(
            "knowledge"
        )

        await self.send_message(

    IncidentMessage(
        context=updated_context
    ),

    AgentId(
        "orchestrator",
        "default"
    )

)


        print(
            "[Knowledge Routed Agent] Completed"
        )