# # from gensim.models import Word2Vec

# # sentences = [
# #     ["dog", "likes", "milk"],
# #     ["puppy", "likes", "milk"],
# #     ["dog", "eats", "meat"],
# #     ["cat", "drinks", "milk"],
# #     ["car", "runs", "fast"]
# # ]

# # model = Word2Vec(
# #     sentences,
# #     vector_size=10,
# #     window=2,
# #     min_count=1,
# #     workers=1
# # )

# # print(model.wv['dog'])
# # print(model.wv.similarity(
# #     "dog",
# #     "car"
# # ))
# # print(model.wv.similarity(
# #     "dog",
# #     "puppy"
# # ))
# # print(model.wv.similarity(
# #     "dog",
# #     "cat"
# # ))

# # print(model.wv.most_similar(
# #     positive=["king","woman"],
# #     negative=["man"]
# # ))


# from gensim.models import Word2Vec

# sentences = [
#     ["dog", "likes", "milk"],
#     ["puppy", "likes", "milk"],
#     ["dog", "eats", "meat"],
#     ["cat", "drinks", "milk"],
#     ["car", "runs", "fast"]
# ]

# model = Word2Vec(
#     sentences,
#     vector_size=10,
#     window=2,
#     min_count=1,
#     workers=1
# )

# print("Dog Embedding:")
# print(model.wv["dog"])

# print()

# print("Similar Words:")
# print(model.wv.most_similar("dog"))

# print()

# print("Similarity:")
# print(model.wv.similarity("dog","puppy"))


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentence1 = "Dog likes milk."
sentence2 = "Puppy drinks milk."

emb1 = model.encode(sentence1)
emb2 = model.encode(sentence2)

print("Shape:", emb1.shape)

similarity = cosine_similarity(
    [emb1],
    [emb2]
)

print("Similarity:", similarity)