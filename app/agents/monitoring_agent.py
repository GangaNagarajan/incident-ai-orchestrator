from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class MonitoringAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Monitoring Agent"
        )


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            f"\n[{self.name}] Checking application health..."
        )


        monitoring_result = {

            "application":
                context.application,

            "health_status":
                "DEGRADED",

            "services_checked":
                [
                    "Payment API",
                    "Database"
                ],

            "observations":
                [
                    "Database connection timeout detected",
                    "High connection pool utilization"
                ],

            "alerts":
                [
                    "DB_CONNECTION_TIMEOUT"
                ]

        }


        # Ensure agent_outputs exists

        if context.agent_outputs is None:
            context.agent_outputs = {}


        context.agent_outputs["monitoring"] = monitoring_result


        print(
            f"[{self.name}] Health check completed"
        )


        return context