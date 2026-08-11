from dotenv import load_dotenv

load_dotenv()

from app.llm.gemini_client import GeminiClient


client = GeminiClient()


context = {

    "incident_id": "INC1001",

    "title": "Database Connection Failure",

    "description": "Application cannot connect to database. Connection pool exhausted.",

    "application": "Payment Service",

    "environment": "Production",

    "status": "OPEN",

    "agent_outputs": {

        "monitoring": {

            "health": {

                "database_connections": "500/500",

                "cpu_usage": "92%",

                "memory_usage": "88%"

            },

            "logs": {

                "logs": [

                    "ERROR Connection pool exhausted",

                    "ERROR Database timeout"

                ]

            }

        }

    }

}


response = client.analyze(

    context

)


print(response)