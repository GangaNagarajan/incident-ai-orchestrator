from app.llm.gemini_client import GeminiClient


class LLMFactory:


    @staticmethod
    def get_client():

        return GeminiClient()

        """ Later we change it to 
        if provider == "azure":
            return AzureOpenAIClient()

        if provider == "openai":
            return OpenAIClient()

        return GeminiClient() 
"""