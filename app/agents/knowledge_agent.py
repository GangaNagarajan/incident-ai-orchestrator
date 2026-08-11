from app.schemas.agent_context_schema import IncidentContext

from app.llm.llm_factory import LLMFactory

from app.rag.faiss_retriever import FAISSRetriever


class KnowledgeAgent:


    def __init__(self):

        self.retriever = FAISSRetriever()

        self.client = LLMFactory.get_client()


    def process(
        self,
        context: IncidentContext
    ) -> IncidentContext:


        print(
            "\n[Knowledge Agent] Searching Knowledge Base..."
        )


        query = f"""
        Incident:
        {context.description}

        Application:
        {context.application}

        Environment:
        {context.environment}
        """

        documents = self.retriever.retrieve(
            query,
            top_k=3
        )


        try:

            response = self.client.knowledge(

                context.model_dump(),

                documents

            )

        except Exception as ex:

            import traceback

            print(f"[Knowledge Agent] LLM Error : {ex}")

            traceback.print_exc()

            response = {

                "similar_incidents": [],

                "recommended_resolutions": [],

                "source": "Gemini Error"

            }


        context.agent_outputs["knowledge"] = response


        print(
            "[Knowledge Agent] RAG retrieval completed"
        )


        return context