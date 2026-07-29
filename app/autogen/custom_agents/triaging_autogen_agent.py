from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.triaging_agent import TriagingAgent



class TriagingAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="TriagingAgent",

            description="Analyses incident category, severity and priority"

        )


        self.business_agent = TriagingAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )