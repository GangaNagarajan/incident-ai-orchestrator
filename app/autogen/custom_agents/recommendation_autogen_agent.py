from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.recommendation_agent import RecommendationAgent



class RecommendationAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="RecommendationAgent",

            description="Creates resolution and remediation recommendations"

        )


        self.business_agent = RecommendationAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )