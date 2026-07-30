from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext



class RCAAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            "RCA Agent"
        )



    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:



        print(
            f"\n[{self.name}] Analysing root cause..."
        )


        root_cause = "Unknown"

        confidence = 0.0


        evidence = []



        description = (
            context.description.lower()
        )



        # Get monitoring evidence

        monitoring_data = {}


        if (
            context.agent_outputs
            and
            "monitoring" in context.agent_outputs
        ):

            monitoring_data = (
                context.agent_outputs["monitoring"]
            )



        health = (
            monitoring_data.get(
                "health",
                {}
            )
        )


        logs = (
            monitoring_data.get(
                "logs",
                {}
            )
        )


        deployments = (
            monitoring_data.get(
                "deployments",
                {}
            )
        )



        log_entries = logs.get(
            "logs",
            []
        )



        # RCA Decision Logic


        if (

            "database" in description

            or

            "connection timeout" in description

            or

            "connection pool" in str(log_entries).lower()

        ):


            root_cause = (
                "Database connection pool exhausted"
            )


            confidence = 0.95



            evidence.append(
                "Incident indicates database connectivity issue"
            )



        if (

            "500/500"
            in
            health.get(
                "database_connections",
                ""
            )

        ):


            evidence.append(
                "Database connections reached maximum capacity"
            )


            confidence = 0.97



        if (

            "Connection pool exhausted"
            in
            str(log_entries)

        ):


            evidence.append(
                "Application logs show connection pool exhaustion"
            )


            confidence = 0.98



        if deployments:


            deployment_name = deployments.get(
                "latest_deployment"
            )


            deployment_time = deployments.get(
                "deployment_time"
            )


            if deployment_name:


                evidence.append(

                    f"Recent deployment detected: {deployment_name} ({deployment_time})"

                )



        if root_cause == "Unknown":


            if "503" in description:


                root_cause = (
                    "Application service unavailable"
                )


                confidence = 0.90



                evidence.append(
                    "HTTP 503 errors detected"
                )



        rca_result = {


            "root_cause":

                root_cause,


            "confidence":

                confidence,


            "evidence":

                evidence,


            "analysis":

                "Derived from incident details, monitoring signals, logs and deployment history"

        }



        if context.agent_outputs is None:

            context.agent_outputs = {}



        context.agent_outputs["rca"] = rca_result



        print(
            f"[{self.name}] Root Cause : {root_cause}"
        )


        print(
            f"[{self.name}] Confidence : {confidence}"
        )


        print(
            f"[{self.name}] Evidence : {evidence}"
        )



        return context