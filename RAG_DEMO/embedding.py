from sentence_transformers import SentenceTransformer

model= SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(documents):
    embeddings= model.encode(documents, convert_to_numpy = True)

    return embeddings.astype("float32")