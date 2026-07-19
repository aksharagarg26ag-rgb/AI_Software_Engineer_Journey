from document import documents
from embedding import create_embedding
from vector_db import VectorDatabase

embeddings = create_embedding(documents)

print("Embeddings shape:", embeddings.shape)

dimension = embeddings.shape[1]

db= VectorDatabase(dimension)
db.add(embeddings)

query= input("Enter your query: ")
query_emb= create_embedding([query])


distances, indices= db.search(query_emb, k=3)
print("Retrieved Documents:")
for i in indices[0]:
    print(documents[i])