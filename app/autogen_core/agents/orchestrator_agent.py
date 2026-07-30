from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    DefaultTopicId
)

from app.autogen_core.messages import IncidentMessage



class OrchestratorRoutedAgent(RoutedAgent):


    def __init__(self):

        super().__init__(
            "Incident Orchestrator"
        )


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



        #
        # First message initialization
        #
        if self.latest_context is None:

            self.latest_context = incoming_context



        else:


            #
            # Merge agent outputs
            #

            existing_outputs = (
                self.latest_context
                .get(
                    "agent_outputs",
                    {}
                )
            )


            incoming_outputs = (
                incoming_context
                .get(
                    "agent_outputs",
                    {}
                )
            )


            existing_outputs.update(
                incoming_outputs
            )


            self.latest_context[
                "agent_outputs"
            ] = existing_outputs



        agent_outputs = (
            self.latest_context
            .get(
                "agent_outputs",
                {}
            )
        )



        if "monitoring" in agent_outputs:

            self.monitoring_completed = True



        if "knowledge" in agent_outputs:

            self.knowledge_completed = True




        if not (

            self.monitoring_completed

            and

            self.knowledge_completed

        ):


            print(
                "Waiting for remaining agents..."
            )

            return




        print(
            "Monitoring + Knowledge completed"
        )



        print(
            "Sending evidence context to RCA Agent"
        )



        await self.publish_message(

            IncidentMessage(

                context=self.latest_context

            ),

            topic_id=DefaultTopicId(
                "rca"
            )

        )