from app.agents.base_agent import BaseAgent
from app.schemas.agent_context_schema import IncidentContext


class ApprovalAgent(BaseAgent):

    def __init__(self):

        super().__init__("Approval Agent")


    def process(
        self,
        context: IncidentContext
    ):

        print(
            f"\n[{self.name}] Checking approval requirements..."
        )


        recommendation = context.agent_outputs.get(
            "recommendation",
            {}
        )


        actions = recommendation.get(
            "recommended_actions",
            []
        )


        automation_possible = recommendation.get(
            "automation_possible",
            False
        )


        approval_status = "PENDING"


        approved_actions = []


        # Enterprise safety rule
        #
        # Production changes require human approval

        if (
            context.environment == "PRODUCTION"
            and automation_possible
        ):

            print(
                f"[{self.name}] Production change detected"
            )

            print(
                f"[{self.name}] Waiting for human approval"
            )


            approval_status = "PENDING"



        else:

            approval_status = "APPROVED"

            approved_actions = actions



        context.agent_outputs["approval"] = {


            "approval_status":
                approval_status,


            "requires_human_approval":
                approval_status == "PENDING",


            "approved_actions":
                approved_actions,


            "requested_actions":
                actions

        }


        return context