from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage


class OrchestratorRoutedAgent(RoutedAgent):

    def __init__(self):

        super().__init__(
            "Incident Orchestrator"
        )

        self.current_incident_id = None

        self.monitoring_completed = False

        self.knowledge_completed = False

        self.latest_context = None


    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:

        print(
            "\n========== Incident Orchestrator =========="
        )

        incoming_context = message.context

        incident_id = incoming_context.get("incident_id")


        #
        # New Incident
        #
        if self.current_incident_id != incident_id:

            self.current_incident_id = incident_id

            self.monitoring_completed = False

            self.knowledge_completed = False

            self.latest_context = incoming_context

            print(
                "[Master Orchestrator] New Incident Received"
            )

            print(
                "[Master Orchestrator] Dispatching Monitoring Agent..."
            )

            await self.send_message(

                IncidentMessage(
                    context=self.latest_context
                ),

                AgentId(
                    "monitoring",
                    "default"
                )

            )


            print(
                "[Master Orchestrator] Dispatching Knowledge Agent..."
            )

            await self.send_message(

                IncidentMessage(
                    context=self.latest_context
                ),

                AgentId(
                    "knowledge",
                    "default"
                )

            )

            return


        #
        # Merge returned context
        #
        existing_outputs = self.latest_context.setdefault(
            "agent_outputs",
            {}
        )

        incoming_outputs = incoming_context.get(
            "agent_outputs",
            {}
        )

        existing_outputs.update(
            incoming_outputs
        )

        self.latest_context.update(
            incoming_context
        )


        #
        # Track completed agents
        #
        if "monitoring" in incoming_outputs:

            self.monitoring_completed = True

            print(
                "[Master Orchestrator] Monitoring completed"
            )


        if "knowledge" in incoming_outputs:

            self.knowledge_completed = True

            print(
                "[Master Orchestrator] Knowledge completed"
            )


        #
        # Wait for both
        #
        if not (
            self.monitoring_completed
            and
            self.knowledge_completed
        ):

            print(
                "[Master Orchestrator] Waiting for remaining agents..."
            )

            return


        print(
            "[Master Orchestrator] Monitoring + Knowledge completed"
        )

        print(
            "[Master Orchestrator] Routing to RCA Agent..."
        )


        await self.send_message(

            IncidentMessage(
                context=self.latest_context
            ),

            AgentId(
                "rca",
                "default"
            )

        )


        #
        # Reset for next incident
        #
        self.current_incident_id = None

        self.monitoring_completed = False

        self.knowledge_completed = False

        self.latest_context = None