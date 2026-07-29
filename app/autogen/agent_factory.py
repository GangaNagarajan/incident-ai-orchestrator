from app.autogen.custom_agents.ticket_autogen_agent import TicketAutoGenAgent
from app.autogen.custom_agents.triaging_autogen_agent import TriagingAutoGenAgent
from app.autogen.custom_agents.monitoring_autogen_agent import MonitoringAutoGenAgent
from app.autogen.custom_agents.knowledge_autogen_agent import KnowledgeAutoGenAgent
from app.autogen.custom_agents.rca_autogen_agent import RCAAutoGenAgent
from app.autogen.custom_agents.recommendation_autogen_agent import RecommendationAutoGenAgent
from app.autogen.custom_agents.approval_autogen_agent import ApprovalAutoGenAgent
from app.autogen.custom_agents.incident_update_autogen_agent import IncidentUpdateAutoGenAgent



class AgentFactory:


    def create_ticket_agent(self):

        return TicketAutoGenAgent()



    def create_triaging_agent(self):

        return TriagingAutoGenAgent()



    def create_monitoring_agent(self):

        return MonitoringAutoGenAgent()



    def create_knowledge_agent(self):

        return KnowledgeAutoGenAgent()



    def create_rca_agent(self):

        return RCAAutoGenAgent()



    def create_recommendation_agent(self):

        return RecommendationAutoGenAgent()



    def create_approval_agent(self):

        return ApprovalAutoGenAgent()



    def create_incident_update_agent(self):

        return IncidentUpdateAutoGenAgent()