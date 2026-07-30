from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class ApprovalAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Approval Agent"
        )


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            f"\n[{self.name}] Validating approval requirement..."
        )


        recommendation = context.agent_outputs.get(
            "recommendation",
            {}
        )


        approval_required = recommendation.get(
            "requires_approval",
            True
        )


        approval_result = {


            "approval_required":

                approval_required,


            "approval_status":

                "PENDING_APPROVAL"
                if approval_required
                else "AUTO_APPROVED",


            "approved_by":

                None

        }



        context.agent_outputs["approval"] = approval_result



        print(
            f"[{self.name}] Approval status updated"
        )


        return context