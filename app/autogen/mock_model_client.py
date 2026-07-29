from typing import Any, AsyncGenerator, Sequence

from autogen_core.models import (
    ChatCompletionClient,
    CreateResult,
    RequestUsage,
    UserMessage,
)



class MockModelClient(ChatCompletionClient):
    """
    Dummy LLM client for local AutoGen agent testing.

    Later this can be replaced with:
    - AzureOpenAIChatCompletionClient
    - OpenAIChatCompletionClient
    """



    @property
    def model_info(self):

        return {
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": "mock"
        }



    @property
    def capabilities(self):

        return {
            "vision": False,
            "function_calling": False,
            "json_output": False
        }



    async def create(
        self,
        messages,
        *,
        cancellation_token=None,
        **kwargs
    ):

        return CreateResult(

            finish_reason="stop",

            content="Mock response from AutoGen agent",

            usage=RequestUsage(
                prompt_tokens=10,
                completion_tokens=5
            )

        )



    async def create_stream(
        self,
        messages,
        *,
        cancellation_token=None,
        **kwargs
    ) -> AsyncGenerator[Any, None]:

        yield "Mock streaming response"



    def count_tokens(
        self,
        messages,
        **kwargs
    ):

        return 10



    def remaining_tokens(
        self,
        messages,
        **kwargs
    ):

        return 1000



    def total_usage(self):

        return RequestUsage(
            prompt_tokens=0,
            completion_tokens=0
        )



    def actual_usage(self):

        return RequestUsage(
            prompt_tokens=0,
            completion_tokens=0
        )



    async def close(self):

        pass