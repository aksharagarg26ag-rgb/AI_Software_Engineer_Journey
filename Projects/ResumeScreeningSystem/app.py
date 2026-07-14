from src.preprocessing import ResumeProcessor
from src.vectorizer import ResumeVectorizer
from src.similarity import SimilarityCalculator
from src.skills import SkillExtractor
from src.sentence_embedding import ResumeVectorizerSentenceEmbedding

# Read Resume
with open("Projects/resumeScreeningSystem/data/resume1.txt", "r") as file:
    resume = file.read()

# Read Job Description
with open("Projects/resumeScreeningSystem/data/job_description.txt", "r") as file:
    job_description = file.read()

# Create Objects
processor = ResumeProcessor()
vectorizer = ResumeVectorizer()
similarity = SimilarityCalculator()
skills = SkillExtractor()
sentence_vectorizer = ResumeVectorizerSentenceEmbedding()

# Clean Text
clean_resume = processor.clean_text(resume)
clean_job = processor.clean_text(job_description)

# Extract Skills
resume_skills = skills.extract_skills(clean_resume)
job_skills = skills.extract_skills(clean_job)

# Compare Skills
matched = skills.matched_skills(resume_skills, job_skills)
missing = skills.missing_skills(resume_skills, job_skills)

# ATS Score
score = skills.ats_score(matched, job_skills)

print("========== CLEAN RESUME ==========")
print(clean_resume)

print("========== CLEAN JOB DESCRIPTION ==========")
print(clean_job)

# Display Results
print("========== Resume Skills ==========")
print(resume_skills)

print("\n========== Job Skills ==========")
print(job_skills)

print("\n========== Matched Skills ==========")
for skill in matched:
    print(skill)

print("\n========== Missing Skills ==========")
for skill in missing:
    print(skill)

print("\n========== Recommendations ==========")
for skill in missing:
    print(skill)


# Vectorize
tfidf_matrix = vectorizer.vectorize(clean_resume, clean_job)
embeddings = sentence_vectorizer.vectorize(clean_resume, clean_job)

print()

print("========== VOCABULARY ==========")
print(vectorizer.get_vocabulary())

print()

print("========== TF-IDF MATRIX ==========")
print(vectorizer.get_matrix(tfidf_matrix))

# Similarity
score1 = similarity.calculate_similarity(tfidf_matrix)
score2 = similarity.calculate_similarity(embeddings)

print("Similarity (TF-IDF) :", score1)
print("Similarity (Sentence Embedding) :", score2)

print(f"Resume Match (TF-IDF) : {score1 * 100:.2f}%")
print(f"Resume Match (Sentence Embedding) : {score2 * 100:.2f}%")

print(f"\nATS Score (TF-IDF): {score1 * 100:.2f}%")
print(f"\nATS Score (Sentence Embedding): {score2 * 100:.2f}%")
