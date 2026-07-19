import faiss

class VectorDatabase:
    def __init__(self,dimension):
        self.index= faiss.IndexFlatL2(dimension)

    def add(self, embeddings):
        self.index.add(embeddings)

    def search(self, query_emb, k=3):
        distances,indices= self.index.search(query_emb, k)

        return distances, indices