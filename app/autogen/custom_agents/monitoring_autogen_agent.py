from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.monitoring_agent import MonitoringAgent



class MonitoringAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="MonitoringAgent",

            description="Checks application health using monitoring platforms"

        )


        self.business_agent = MonitoringAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )