import asyncio

from autogen_core import AgentId

from app.autogen_core.runtime import runtime

from app.autogen_core.messages import IncidentMessage

from app.autogen_core.agents.ticket_agent import TicketRoutedAgent
from app.autogen_core.agents.triaging_agent import TriagingRoutedAgent
from app.autogen_core.agents.monitoring_agent import MonitoringRoutedAgent
from app.autogen_core.agents.knowledge_agent import KnowledgeRoutedAgent
from app.autogen_core.agents.rca_agent import RCARoutedAgent
from app.autogen_core.agents.orchestrator_agent import OrchestratorRoutedAgent



async def main():



    await TicketRoutedAgent.register(

        runtime,

        "ticket",

        lambda: TicketRoutedAgent()

    )



    await TriagingRoutedAgent.register(

        runtime,

        "triaging",

        lambda: TriagingRoutedAgent()

    )

    await MonitoringRoutedAgent.register(
    runtime,
    "monitoring",
    lambda: MonitoringRoutedAgent()
)


    await KnowledgeRoutedAgent.register(
    runtime,
    "knowledge",
    lambda: KnowledgeRoutedAgent()
)

    await RCARoutedAgent.register(
    runtime,
    "rca",
    lambda: RCARoutedAgent()
)

    await OrchestratorRoutedAgent.register(
    runtime,
    "orchestrator",
    lambda: OrchestratorRoutedAgent()
)

    



    runtime.start()



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
        "OPEN"


    }



    await runtime.send_message(

        IncidentMessage(

            context=incident

        ),

        AgentId(

            "ticket",

            "default"

        )

    )



    await runtime.stop_when_idle()



if __name__ == "__main__":

    asyncio.run(main())