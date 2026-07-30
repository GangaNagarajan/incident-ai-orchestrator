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
            f"\n[{self.name}] Collecting application evidence..."
        )


        application = context.application



        health = self.mcp_client.call_tool(
            "get_application_health",
            application_name=application
        )



        logs = self.mcp_client.call_tool(
            "get_application_logs",
            application_name=application
        )



        deployments = self.mcp_client.call_tool(
            "get_recent_deployments",
            application_name=application
        )



        if context.agent_outputs is None:

            context.agent_outputs = {}



        context.agent_outputs["monitoring"] = {


            "health":
                health,


            "logs":
                logs,


            "deployments":
                deployments

        }



        print(
            f"[{self.name}] Evidence collection completed"
        )


        return context