from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler
)


from app.autogen_core.messages import IncidentMessage

from app.agents.monitoring_agent import MonitoringAgent

from app.autogen_core.state import incident_state

from autogen_core import AgentId


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
            "\n========== Monitoring Routed Agent =========="
        )


        updated_context = self.business_agent.process(
            message.context
        )


        incident_state.update_context(
            updated_context
        )


        incident_state.mark_completed(
            "monitoring"
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
            "[Monitoring Routed Agent] Completed"
        )

