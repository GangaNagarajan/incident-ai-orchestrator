import asyncio
import json

from autogen_agentchat.messages import TextMessage

from app.autogen.incident_team import IncidentTeam



async def main():

    print(
        "\n========== INCIDENT AI AUTOGEN ORCHESTRATOR ==========\n"
    )


    incident = {

        "incident_id": "INC1001",

        "title": "Payment API Failure",

        "description":
            "Payment API returning 503 errors due to database connection timeout",

        "application":
            "Payment Service",

        "environment":
            "PRODUCTION",

        "status":
            "OPEN",

        "priority":
            "P1"

    }



    team = IncidentTeam()



    task = TextMessage(

        content=str(incident),

        source="User"

    )



    result = await team.team.run(

        task=task

    )



    print(
        "\n========== AUTOGEN PROCESS COMPLETED ==========\n"
    )


    print(result)



if __name__ == "__main__":

    asyncio.run(main())