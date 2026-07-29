from app.agents.ticket_agent import TicketAgent
from app.agents.triaging_agent import TriagingAgent
from app.agents.monitoring_agent import MonitoringAgent
from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.rca_agent import RCAAgent
from app.agents.recommendation_agent import RecommendationAgent
from app.agents.approval_agent import ApprovalAgent
from app.agents.incident_update_agent import IncidentUpdateAgent



class AgentRegistry:


    def __init__(self):

        self.agents = {


            "ticket":
                TicketAgent(),


            "triaging":
                TriagingAgent(),


            "monitoring":
                MonitoringAgent(),


            "knowledge":
                KnowledgeAgent(),


            "rca":
                RCAAgent(),


            "recommendation":
                RecommendationAgent(),

            "approval": 
                ApprovalAgent(),

            "incident_update": 
                IncidentUpdateAgent()

        }



    def get_agent(
        self,
        agent_name
    ):

        return self.agents.get(
            agent_name
        )



    def get_all_agents(self):

        return self.agents