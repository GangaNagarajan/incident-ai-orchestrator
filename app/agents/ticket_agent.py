from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class TicketAgent(BaseAgent):

    def __init__(self):
        super().__init__("Ticket Agent")


    def process(self, incident):

        print(f"\n[{self.name}] Processing incident...")


        context = IncidentContext(

            incident_id=incident["incident_id"],

            title=incident["title"],

            description=incident["description"],

            application=incident["application"],

            environment=incident["environment"]

        )


        return context