import pickle

import faiss
import numpy as np

from app.rag.embeddings import EmbeddingModel


documents = [

    {
        "incident_id": "INC9654",
        "summary": "Database connection exhausted",
        "resolution": "Increase DB connection pool size"
    },

    {
        "incident_id": "INC9821",
        "summary": "Database timeout issue",
        "resolution": "Review timeout configuration"
    },

    {
        "incident_id": "INC7120",
        "summary": "CPU utilization high",
        "resolution": "Scale application instances"
    }

]


embedding_model = EmbeddingModel()


vectors = []

for doc in documents:

    embedding = embedding_model.generate_embedding(
        doc["summary"]
    )

    vectors.append(embedding)


vectors = np.array(
    vectors,
    dtype="float32"
)


dimension = vectors.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(vectors)

faiss.write_index(
    index,
    "app/rag/vector.index"
)

with open(
    "app/rag/metadata.pkl",
    "wb"
) as f:

    pickle.dump(
        documents,
        f
    )

print("Vector Store Created Successfully")