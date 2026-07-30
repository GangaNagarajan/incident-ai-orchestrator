from app.agents.base_agent import BaseAgent
from app.mcp.client.mcp_client import MCPClient


class MonitoringAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "Monitoring Agent"
        )

        self.mcp_client = MCPClient()



    def process(
        self,
        context
    ):


        print(
            f"\n[{self.name}] Checking application health..."
        )


        # Pydantic IncidentContext
        application_name = context.application



        health_result = (
            self.mcp_client.call_tool(
                "get_application_health",
                application_name=application_name
            )
        )


        # Ensure dictionary exists

        if context.agent_outputs is None:

            context.agent_outputs = {}



        context.agent_outputs["monitoring"] = (
            health_result
        )



        print(
            f"[{self.name}] Health check completed"
        )


        return context