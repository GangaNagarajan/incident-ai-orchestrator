from datetime import datetime


class MonitoringMCPServer:


    def __init__(self):

        self.name = "Monitoring MCP Server"



    def get_application_health(
        self,
        application_name: str
    ):


        print(
            f"\n[MCP Monitoring Tool] Checking {application_name}"
        )


        return {


            "application":

                application_name,


            "status":

                "DEGRADED",


            "cpu_usage":

                "78%",


            "memory_usage":

                "82%",


            "database_connections":

                "500/500",


            "error_rate":

                "15%",


            "timestamp":

                str(datetime.now())

        }