from concurrent.futures import ThreadPoolExecutor

from app.registry.agent_registry import AgentRegistry



class IncidentOrchestrator:


    def __init__(self):

        self.registry = AgentRegistry()



    def process_incident(self, incident):


        print(
            "\n========== INCIDENT AI ORCHESTRATOR ==========\n"
        )


        # -----------------------------
        # Step 1
        # Ticket Agent
        # -----------------------------

        ticket_agent = self.registry.get_agent(
            "ticket"
        )


        context = ticket_agent.process(
            incident
        )



        # -----------------------------
        # Step 2
        # Triaging Agent
        # -----------------------------

        triaging_agent = self.registry.get_agent(
            "triaging"
        )


        context = triaging_agent.process(
            context
        )



        # -----------------------------
        # Step 3
        # Parallel Execution
        # Monitoring + Knowledge
        # -----------------------------


        monitoring_agent = self.registry.get_agent(
            "monitoring"
        )


        knowledge_agent = self.registry.get_agent(
            "knowledge"
        )


        with ThreadPoolExecutor(
            max_workers=2
        ) as executor:


            monitoring_task = executor.submit(

                monitoring_agent.process,

                context

            )


            knowledge_task = executor.submit(

                knowledge_agent.process,

                context

            )


            monitoring_task.result()

            knowledge_task.result()



        # -----------------------------
        # Step 4
        # RCA Agent
        # -----------------------------


        rca_agent = self.registry.get_agent(
            "rca"
        )


        context = rca_agent.process(
            context
        )


        recommendation_agent = self.registry.get_agent(
    "recommendation"
)


        context = recommendation_agent.process(
        context
)

        approval_agent = self.registry.get_agent(
    "approval"
)


        context = approval_agent.process(
                context
)

        incident_update_agent = self.registry.get_agent(
    "incident_update"
)


        context = incident_update_agent.process(
    context
)
        



        print(
            "\n========== INCIDENT PROCESSING COMPLETED ==========\n"
        )


        return context