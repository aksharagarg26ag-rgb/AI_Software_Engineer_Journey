#use sentence embedding insted of tf idf 
import config
from sentence_transformers import SentenceTransformer
import numpy as np


class SentenceEmbedding:

    def __init__(self):
        self.model = SentenceTransformer(config.EMBEDDING_MODEL)

    def generate_embeddings(self, documents: list[str]) -> np.ndarray:
       
        embeddings = self.model.encode(documents,convert_to_numpy=True)

        return embeddings.astype("float32")
