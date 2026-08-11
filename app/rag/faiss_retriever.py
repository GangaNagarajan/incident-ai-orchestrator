import pickle

import faiss
import numpy as np

from app.rag.embeddings import EmbeddingModel


class FAISSRetriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.index = faiss.read_index(
            "app/rag/vector.index"
        )

        with open(
            "app/rag/metadata.pkl",
            "rb"
        ) as f:

            self.documents = pickle.load(f)

    def retrieve(
        self,
        query,
        top_k=3
    ):

        embedding = self.embedding_model.generate_embedding(
            query
        )

        embedding = np.array(
            [embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for index in indices[0]:

            if index != -1:

                results.append(
                    self.documents[index]
                )

        return results