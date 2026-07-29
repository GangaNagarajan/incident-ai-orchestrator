from autogen_agentchat.teams import RoundRobinGroupChat

from app.autogen.agent_factory import AgentFactory



class IncidentTeam:


    def __init__(self):

        factory = AgentFactory()


        self.ticket_agent = (
            factory.create_ticket_agent()
        )


        self.triaging_agent = (
            factory.create_triaging_agent()
        )


        self.monitoring_agent = (
            factory.create_monitoring_agent()
        )


        self.knowledge_agent = (
            factory.create_knowledge_agent()
        )


        self.rca_agent = (
            factory.create_rca_agent()
        )


        self.recommendation_agent = (
            factory.create_recommendation_agent()
        )


        self.approval_agent = (
            factory.create_approval_agent()
        )


        self.incident_update_agent = (
            factory.create_incident_update_agent()
        )


        self.team = RoundRobinGroupChat(

        participants=[

        factory.create_ticket_agent().agent,

        factory.create_triaging_agent().agent,

        factory.create_monitoring_agent().agent,

        factory.create_knowledge_agent().agent,

        factory.create_rca_agent().agent,

        factory.create_recommendation_agent().agent,

        factory.create_approval_agent().agent,

        factory.create_incident_update_agent().agent

    ]

)