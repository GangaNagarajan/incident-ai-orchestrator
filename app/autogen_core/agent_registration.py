from app.autogen_core.runtime import runtime


from app.autogen_core.agents.ticket_agent import TicketRoutedAgent
from app.autogen_core.agents.triaging_agent import TriagingRoutedAgent
from app.autogen_core.agents.orchestrator_agent import (
    OrchestratorRoutedAgent
)
from app.autogen_core.agents.monitoring_agent import (
    MonitoringRoutedAgent
)
from app.autogen_core.agents.knowledge_agent import (
    KnowledgeRoutedAgent
)
from app.autogen_core.agents.rca_agent import (
    RCARoutedAgent
)
from app.autogen_core.agents.recommendation_agent import (
    RecommendationRoutedAgent
)
from app.autogen_core.agents.approval_agent import (
    ApprovalRoutedAgent
)
from app.autogen_core.agents.incident_update_agent import (
    IncidentUpdateRoutedAgent
)
from app.autogen_core.agents.scope_agent import (
    ScopeRoutedAgent
)


async def register_agents():

    await ScopeRoutedAgent.register(
    runtime,
    "scope",
    lambda: ScopeRoutedAgent()
    )

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


    await OrchestratorRoutedAgent.register(
        runtime,
        "orchestrator",
        lambda: OrchestratorRoutedAgent()
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

    


    runtime.start()