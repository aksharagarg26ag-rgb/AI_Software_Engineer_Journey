import config


class Retriever:

    def __init__(self, vector_database):
        self.vector_database = vector_database

    def retrieve(self,
                 query_embedding,
                 chunks):

        distances, indices = self.vector_database.search(
            query_embedding,
            config.TOP_K
        )

        retrieved_chunks = []

        for index in indices[0]:
            if index != -1 and index < len(chunks):
                retrieved_chunks.append(chunks[index])  

        return retrieved_chunks