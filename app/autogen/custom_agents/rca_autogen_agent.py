from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.rca_agent import RCAAgent



class RCAAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="RCAAgent",

            description="Analyses incident evidence and determines root cause"

        )


        self.business_agent = RCAAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )