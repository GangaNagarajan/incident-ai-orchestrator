from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.approval_agent import ApprovalAgent



class ApprovalAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="ApprovalAgent",

            description="Validates whether human approval is required before production changes"

        )


        self.business_agent = ApprovalAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )