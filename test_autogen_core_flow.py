import asyncio

from autogen_core import (
    AgentId,
    TypeSubscription
)

from app.autogen_core.runtime import runtime

from app.autogen_core.messages import IncidentMessage


# Routed Agents

from app.autogen_core.agents.ticket_agent import TicketRoutedAgent
from app.autogen_core.agents.triaging_agent import TriagingRoutedAgent
from app.autogen_core.agents.monitoring_agent import MonitoringRoutedAgent
from app.autogen_core.agents.knowledge_agent import KnowledgeRoutedAgent
from app.autogen_core.agents.rca_agent import RCARoutedAgent
from app.autogen_core.agents.orchestrator_agent import OrchestratorRoutedAgent
from app.autogen_core.agents.recommendation_agent import RecommendationRoutedAgent
from app.autogen_core.agents.approval_agent import ApprovalRoutedAgent
from app.autogen_core.agents.incident_update_agent import IncidentUpdateRoutedAgent



async def main():


    print(
        "\n========== INCIDENT AI AUTOGEN CORE FLOW ==========\n"
    )


    # =====================================================
    # Register Agents
    # =====================================================


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


    await RecommendationRoutedAgent.register(
        runtime,
        "recommendation",
        lambda: RecommendationRoutedAgent()
    )


    await ApprovalRoutedAgent.register(
        runtime,
        "approval",
        lambda: ApprovalRoutedAgent()
    )


    await IncidentUpdateRoutedAgent.register(
        runtime,
        "incident_update",
        lambda: IncidentUpdateRoutedAgent()
    )



    # =====================================================
    # Topic Subscriptions
    # =====================================================


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="monitoring",
            agent_type="monitoring"
        )
    )


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="knowledge",
            agent_type="knowledge"
        )
    )


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="rca",
            agent_type="rca"
        )
    )


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="recommendation",
            agent_type="recommendation"
        )
    )


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="approval",
            agent_type="approval"
        )
    )


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="incident_update",
            agent_type="incident_update"
        )
    )


    await runtime.add_subscription(
        TypeSubscription(
            topic_type="orchestrator",
            agent_type="orchestrator"
        )
    )



    # Start Runtime

    runtime.start()



    # =====================================================
    # Incident Input
    # =====================================================


    incident = {


        "incident_id":

            "INC1001",


        "title":

            "Payment API Failure",


        "description":

            "Payment API returning 503 errors due to database connection timeout",


        "application":

            "Payment Service",


        "environment":

            "PRODUCTION",


        "status":

            "OPEN",


        "priority":

            None,


        "category":

            None,


        "next_agents":

            [],


        "agent_outputs":

            {}

    }



    # =====================================================
    # Start Incident Processing
    # =====================================================


    await runtime.send_message(

        IncidentMessage(
            context=incident
        ),

        AgentId(
            "ticket",
            "default"
        )

    )


    # Wait until all agents complete

    await runtime.stop_when_idle()



    print(
        "\n========== INCIDENT AI FLOW COMPLETED ==========\n"
    )



if __name__ == "__main__":

    asyncio.run(main())