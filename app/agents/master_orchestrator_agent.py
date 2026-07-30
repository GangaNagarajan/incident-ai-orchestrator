from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class MasterOrchestratorAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Master Orchestrator Agent"
        )


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            f"\n[{self.name}] Deciding execution workflow..."
        )


        category = context.category


        next_agents = []


        if category == "Database Failure":

            next_agents = [

                "monitoring",
                "knowledge",
                "rca"

            ]


        elif category == "Security Issue":

            next_agents = [

                "security",
                "knowledge",
                "rca"

            ]


        else:

            next_agents = [

                "monitoring",
                "knowledge",
                "rca"

            ]


        context.next_agents = next_agents


        if context.agent_outputs is None:
            context.agent_outputs = {}


        context.agent_outputs["orchestrator"] = {


            "decision":

                "Dynamic workflow generated",


            "agents_triggered":

                next_agents

        }


        print(
            f"[{self.name}] Next Agents: {next_agents}"
        )


        return context