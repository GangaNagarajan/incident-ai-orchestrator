import json

from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore



class KnowledgeBase:


    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()



    def load(self,path):


        with open(path) as f:

            documents=json.load(f)



        texts=[]


        for doc in documents:

            texts.append(
                doc["description"]
            )


        embeddings = (
            self.embedding_model
            .generate_embeddings(texts)
        )


        self.vector_store.build(
            embeddings,
            documents
        )



    def retrieve(
        self,
        query
    ):


        embedding = (
            self.embedding_model
            .generate_embeddings(
                [query]
            )[0]
        )


        return self.vector_store.search(
            embedding
        )