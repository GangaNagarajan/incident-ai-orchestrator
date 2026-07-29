from typing import Dict, Any


class IncidentState:


    def __init__(self):

        self.context: Dict[str, Any] = {}

        self.completed_agents = set()



    def update_context(self, context):

        self.context = context



    def mark_completed(self, agent_name):

        self.completed_agents.add(agent_name)



    def is_ready_for_rca(self):

        required_agents = {

            "monitoring",

            "knowledge"

        }


        return required_agents.issubset(
            self.completed_agents
        )



    def get_context(self):

        return self.context