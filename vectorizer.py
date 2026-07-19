# from sklearn.feature_extraction.text import TfidfVectorizer
# from preprocessing import ResumeProcessor
# processor = ResumeProcessor()
# with open("Projects/resumeScreeningSystem/data/resume1.txt","r") as file:
#     resume= file.read()

# with open("Projects/resumeScreeningSystem/data/job_description.txt","r") as file:
#     job_description= file.read()

# # Clean Text
# clean_resume = processor.clean_text(resume)
# clean_job = processor.clean_text(job_description)

# print("========== CLEAN RESUME ==========")
# print(clean_resume)

# print()

# print("========== CLEAN JOB DESCRIPTION ==========")
# print(clean_job)

# documents = [
#     clean_resume,
#     clean_job
# ]

# vectorizer = TfidfVectorizer()

# tfidf_matrix = vectorizer.fit_transform(documents)

# print()

# print("========== VOCABULARY ==========")
# print(vectorizer.get_feature_names_out())

# print()

# print("========== TF-IDF MATRIX ==========")
# print(tfidf_matrix.toarray())


from sklearn.feature_extraction.text import TfidfVectorizer


class ResumeVectorizer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def vectorize(self, clean_resume, clean_job):
        documents = [
            clean_resume,
            clean_job
        ]

        tfidf_matrix = self.vectorizer.fit_transform(documents)

        return tfidf_matrix

    def get_vocabulary(self):
        return self.vectorizer.get_feature_names_out()

    def get_matrix(self, tfidf_matrix):
        return tfidf_matrix.toarray()
    



    