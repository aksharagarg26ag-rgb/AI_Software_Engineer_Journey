#use sentence embedding insted of tf idf 
from sentence_transformers import SentenceTransformer

class SentenceEmbedding:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def vectorize(self, clean_resume, clean_job):
        documents = [
            clean_resume,
            clean_job
        ]

        embeddings = self.model.encode(documents)

        return embeddings   
