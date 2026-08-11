from autogen_core import (
    RoutedAgent,
    MessageContext,
    message_handler,
    AgentId
)

from app.autogen_core.messages import IncidentMessage

from app.agents.scope_agent import ScopeAgent

from app.schemas.agent_context_schema import IncidentContext


class ScopeRoutedAgent(RoutedAgent):

    def __init__(self):

        super().__init__(
            "Scope Routed Agent"
        )

        self.business_agent = ScopeAgent()


    @message_handler
    async def handle_incident(
        self,
        message: IncidentMessage,
        ctx: MessageContext
    ) -> None:

        print(
            "\n========== Scope Routed Agent ==========\n"
        )

        context = IncidentContext(
            **message.context
        )


        updated_context = self.business_agent.process(
            context
        )


        message.context = (
            updated_context.model_dump()
        )


        scope = (
            message.context
            .get("agent_outputs", {})
            .get("scope", {})
        )


        if not scope.get(
            "is_incident",
            True
        ):

            print(
                "[Scope Routed Agent] "
                "Non-incident request rejected"
            )

            return


        print(
            "[Scope Routed Agent] "
            "Valid enterprise incident"
        )


        await self.send_message(
            IncidentMessage(
                context=message.context
            ),
            AgentId(
                "orchestrator",
                "default"
            )
        )