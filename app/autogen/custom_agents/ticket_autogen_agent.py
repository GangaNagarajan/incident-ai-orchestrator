from app.autogen.custom_agents.base_autogen_agent import BaseAutoGenAgent
from app.agents.ticket_agent import TicketAgent



class TicketAutoGenAgent(BaseAutoGenAgent):


    def __init__(self):

        super().__init__(

            name="TicketAgent",

            description="Processes incoming incident tickets and extracts incident details"

        )


        self.business_agent = TicketAgent()



    async def process(self, context):

        return self.business_agent.process(
            context
        )