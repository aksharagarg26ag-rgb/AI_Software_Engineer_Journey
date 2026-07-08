# from clean_text import clean_text

# with open("Projects/ResumeScreeningSystem/data/resume1.txt","r") as file:
#     resume= file.read()

# clean_resume= clean_text(resume)


# SKILLS = [

#     "python",
#     "java",
#     "sql",
#     "fastapi",
#     "docker",
#     "machine learning",
#     "deep learning",
#     "streamlit",
#     "scikit-learn",
#     "numpy",
#     "pandas",
#     "git",
#     "github"

# ]

# def extract_skills(text):

#     text = text.lower()

#     matched = []

#     for skill in SKILLS:

#         if skill in text:

#             matched.append(skill)

#     return matched
# print("Matched Skills:", extract_skills(clean_resume))

from clean_text import clean_text

with open("Projects/ResumeScreeningSystem/data/resume2.txt", "r") as file:
    resume = file.read()

with open("Projects/ResumeScreeningSystem/data/job_description.txt", "r") as file:
    job_description = file.read()

clean_resume = clean_text(resume)
clean_job = clean_text(job_description)

print("Clean Resume\n")
print(clean_resume)

print("Clean Job Description\n")
print(clean_job)

SKILLS = [

    "python",
    "java",
    "c++",
    "sql",
    "mysql",

    "machine learning",
    "deep learning",
    "artificial intelligence",

    "fastapi",
    "streamlit",
    "flask",

    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",

    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",

    "git",
    "github",
    "docker"

]


def extract_skills(text):

    text = text.lower()

    extracted = []

    for skill in SKILLS:

        if skill in text:

            extracted.append(skill)

    return extracted


resume_skills = extract_skills(clean_resume)

job_skills = extract_skills(clean_job)


matched_skills = [

    skill

    for skill in job_skills

    if skill in resume_skills

]


missing_skills = [

    skill

    for skill in job_skills

    if skill not in resume_skills

]


recommendations = missing_skills

# --------------------------------------------------
# Display Results
# --------------------------------------------------


print("Resume Skills")
print(resume_skills)



print("Job Skills")
print(job_skills)



print("Matched Skills")

for skill in matched_skills:

    print( skill)



print("Missing Skills")

for skill in missing_skills:

    print(skill)


print("Recommendations")

for skill in recommendations:

    print( skill)

#ats score
if(len(job_skills) > 0):
    ats_score = (len(matched_skills) / len(job_skills)) * 100
    print("ATS Score: ",ats_score,"%")