from typing import Any, Dict

from autogen_agentchat.agents import AssistantAgent

from app.autogen.mock_model_client import MockModelClient



class BaseAutoGenAgent:
    """
    Base wrapper for AutoGen AgentChat agents.
    """


    def __init__(
        self,
        name: str,
        description: str
    ):

        self.name = name


        self.agent = AssistantAgent(

            name=name,

            description=description,

            model_client=MockModelClient()

        )



    async def process(
        self,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:

        return context