from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class KnowledgeAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Knowledge Agent"
        )


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            f"\n[{self.name}] Searching knowledge base..."
        )


        knowledge_result = {

            "similar_incidents": [

                "INC9821 - Database timeout issue",
                "INC9732 - Payment API degradation"

            ],

            "matched_solution":

                "Increase DB connection pool and review timeout configuration",

            "knowledge_source":

                "Enterprise Knowledge Base"

        }


        if context.agent_outputs is None:
            context.agent_outputs = {}


        context.agent_outputs["knowledge"] = knowledge_result


        print(
            f"[{self.name}] Knowledge retrieval completed"
        )


        return context