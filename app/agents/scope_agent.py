import json

from app.agents.base_agent import BaseAgent
from app.llm.llm_factory import LLMFactory


class ScopeAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Incident Scope Agent"
        )

        self.client = LLMFactory.get_client()


    def process(
        self,
        context
    ):

        print(
            f"\n[{self.name}] Validating incident scope..."
        )

        prompt = f"""
Determine whether this is a legitimate enterprise IT incident.

Title:
{context.title}

Description:
{context.description}

Application:
{context.application}

Environment:
{context.environment}

Return ONLY JSON.

Format:

{{
"is_incident": true,
"reason": "short explanation"
}}

Set is_incident to true for enterprise IT incidents such as:

- Application failures
- Authentication failures
- Password reset failures
- API failures
- Database issues
- Infrastructure issues
- Deployment failures
- Service degradation
- Performance issues
- Network issues
- Monitoring alerts

Set is_incident to false for unrelated requests such as:

- Shopping
- Clothes
- Restaurants
- Dining
- Travel
- Entertainment
- General questions
- Weather
- Personal requests
"""

        response = self.client.client.models.generate_content(
            model=self.client.model,
            contents=prompt
        )

        try:

            cleaned_response = (
                response.text
                .strip()
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            scope_result = json.loads(
                cleaned_response
            )

        except Exception as ex:

            print(
                f"[{self.name}] Scope parsing error: {ex}"
            )

            scope_result = {
                "is_incident": True,
                "reason": "Scope validation could not be parsed."
            }


        # -----------------------------------------
        # Store scope result in context
        # -----------------------------------------

        if context.agent_outputs is None:

            context.agent_outputs = {}

        context.agent_outputs["scope"] = scope_result


        print(
            f"[{self.name}] Result: {scope_result}"
        )


        # -----------------------------------------
        # Reject irrelevant requests
        # -----------------------------------------

        if scope_result.get("is_incident") is False:

            context.agent_outputs["scope_rejected"] = True

            context.agent_outputs["rejection_reason"] = (
                scope_result.get(
                    "reason",
                    "Request is not an enterprise IT incident."
                )
            )

        else:

            context.agent_outputs["scope_rejected"] = False


        return context