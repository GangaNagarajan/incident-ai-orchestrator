from app.agents.ticket_agent import TicketAgent
from app.agents.triaging_agent import TriagingAgent
from app.agents.monitoring_agent import MonitoringAgent
from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.rca_agent import RCAAgent


ticket_agent = TicketAgent()
triaging_agent = TriagingAgent()
monitoring_agent = MonitoringAgent()
knowledge_agent = KnowledgeAgent()
rca_agent = RCAAgent()



def ticket_tool(incident: dict):

    return ticket_agent.process(
        incident
    )



def triaging_tool(context):

    return triaging_agent.process(
        context
    )



def monitoring_tool(context):

    return monitoring_agent.process(
        context
    )



def knowledge_tool(context):

    return knowledge_agent.process(
        context
    )



def rca_tool(context):

    return rca_agent.process(
        context
    )