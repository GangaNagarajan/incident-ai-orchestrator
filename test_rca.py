from dotenv import load_dotenv

load_dotenv()

from app.agents.rca_agent import RCAAgent
from app.schemas.agent_context_schema import IncidentContext


context = IncidentContext(

    incident_id="INC1001",

    title="Database Connection Failure",

    description="Application cannot connect to database. Connection pool exhausted.",

    application="Payment Service",

    environment="Production",

    status="OPEN"

)

agent = RCAAgent()

result = agent.process(context)

print("\n========== RCA OUTPUT ==========\n")

print(result.agent_outputs["rca"])