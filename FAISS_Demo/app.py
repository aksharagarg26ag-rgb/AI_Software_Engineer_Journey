import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

documents = [
    "Python is a programming language.",
    "Machine Learning uses data to learn patterns.",
    "Deep Learning is a subset of Machine Learning.",
    "FastAPI is used for building APIs.",
    "Football is a popular sport."
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)
embeddings = np.array(embeddings, dtype=np.float32)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

query = "Soccer game"

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding, dtype=np.float32)

distances, indices = index.search(query_embedding, k=3)

print("Top 3 Results:\n")

for rank, i in enumerate(indices[0], start=1):
    print(f"{rank}. {documents[i]}")