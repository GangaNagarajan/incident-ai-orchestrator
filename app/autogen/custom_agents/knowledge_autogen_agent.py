from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.knowledge_agent import KnowledgeAgent



class KnowledgeAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="KnowledgeAgent",

            description="Retrieves SOPs, runbooks, previous incidents and knowledge articles"

        )


        self.business_agent = KnowledgeAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )