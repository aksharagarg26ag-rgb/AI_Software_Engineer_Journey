import faiss
import numpy as np


class VectorDatabase:

    def __init__(self, dimension: int):
        """Create a FAISS index."""

        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings: np.ndarray):
        """
        Add embeddings to the FAISS index.
        """

        self.index.add(embeddings)

    def search(self, query_embedding: np.ndarray, top_k: int):
        """
        Search the nearest embeddings.
        """

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        return distances, indices