from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)


from app.autogen_core.messages import IncidentMessage

from app.autogen_core.state import incident_state



class OrchestratorRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Incident Orchestrator"
        )



    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:


        print(
            "\n========== Incident Orchestrator =========="
        )


        incident_state.update_context(
            message.context
        )


        if incident_state.is_ready_for_rca():


            print(
                "Monitoring + Knowledge completed"
            )


            await self.send_message(

                IncidentMessage(
                    context=incident_state.get_context()
                ),

                AgentId(
                    "rca",
                    "default"
                )

            )

        else:

            print(
                "Waiting for remaining agents..."
            )