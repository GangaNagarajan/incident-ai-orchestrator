from app.mcp.server.monitoring_server import (
    MonitoringMCPServer
)



class MCPClient:


    def __init__(self):

        self.monitoring_server = MonitoringMCPServer()



    def call_tool(
        self,
        tool_name,
        **kwargs
    ):


        if tool_name == "get_application_health":

            return (
                self.monitoring_server
                .get_application_health(
                    **kwargs
                )
            )


        elif tool_name == "get_application_logs":

            return (
                self.monitoring_server
                .get_application_logs(
                    **kwargs
                )
            )


        elif tool_name == "get_recent_deployments":

            return (
                self.monitoring_server
                .get_recent_deployments(
                    **kwargs
                )
            )


        raise Exception(
            f"Unknown MCP tool {tool_name}"
        )