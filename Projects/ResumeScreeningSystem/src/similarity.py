from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read files

with open("Projects/resumeScreeningSystem/data/resume1.txt","r") as file:
    resume= file.read()

with open("Projects/resumeScreeningSystem/data/job_description.txt","r") as file:
    job_description= file.read()


# Import your preprocessing function
from clean_text import clean_text

clean_resume = clean_text(resume)
clean_job = clean_text(job_description)

documents = [clean_resume, clean_job]

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Cosine Similarity
similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

print("Similarity:", similarity)

score = similarity[0][0] * 100

print(f"Resume Match: {score:.2f}%")