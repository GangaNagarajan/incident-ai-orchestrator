from dotenv import load_dotenv

load_dotenv()

from app.agents.knowledge_agent import KnowledgeAgent
from app.schemas.agent_context_schema import IncidentContext


context = IncidentContext(

    incident_id="INC1002",

    title="Database Timeout",

    description="Application cannot connect to database because connection pool exhausted",

    application="Payment Service",

    environment="Production",

    status="OPEN"

)

agent = KnowledgeAgent()

result = agent.process(context)

print("\n========== KNOWLEDGE OUTPUT ==========\n")

print(result.agent_outputs["knowledge"])