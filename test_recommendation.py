from dotenv import load_dotenv

load_dotenv()

from app.agents.recommendation_agent import RecommendationAgent
from app.schemas.agent_context_schema import IncidentContext


context = IncidentContext(

    incident_id="INC1003",

    title="Database Timeout",

    description="Database connection pool exhausted.",

    application="Payment Service",

    environment="Production",

    status="OPEN"

)

context.agent_outputs["rca"] = {

    "root_cause": "Database connection pool exhausted",

    "confidence": 0.95

}


agent = RecommendationAgent()

result = agent.process(context)

print(result.agent_outputs["recommendation"])