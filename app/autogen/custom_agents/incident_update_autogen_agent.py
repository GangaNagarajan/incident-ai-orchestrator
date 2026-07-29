from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.incident_update_agent import IncidentUpdateAgent



class IncidentUpdateAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="IncidentUpdateAgent",

            description="Updates incident management tools like Jira and ServiceNow"

        )


        self.business_agent = IncidentUpdateAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )