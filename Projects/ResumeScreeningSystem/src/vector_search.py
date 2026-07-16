# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Read files

# with open("Projects/ResumeScreeningSystem/data/resume3.txt","r") as file:
#     resume= file.read()

# with open("Projects/ResumeScreeningSystem/data/job_description.txt","r") as file:
#     job_description= file.read()


# # Import your preprocessing function
# from preprocessing import clean_text

# clean_resume = clean_text(resume)
# clean_job = clean_text(job_description)

# documents = [clean_resume, clean_job]

# # TF-IDF
# vectorizer = TfidfVectorizer()
# tfidf_matrix = vectorizer.fit_transform(documents)

# # Cosine Similarity
# similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# print("Similarity:", similarity)

# score = similarity[0][0] * 100

# print(f"Resume Match: {score:.2f}%")


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SimilarityCalculator:

    def calculate_similarity(self, vectors):

        first = vectors[0]
        second = vectors[1]

        

        similarity = cosine_similarity(first, second)

        return similarity[0][0]

    def calculate_percentage(self, vectors):

        return self.calculate_similarity(vectors) * 100
        