import re 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

with open("Projects/resumeScreeningSystem/data/resume1.txt","r") as file:
    resume= file.read()

with open("Projects/resumeScreeningSystem/data/job_description.txt","r") as file:
    job_description= file.read()

def clean_text(text):
    #lowercase
    text = text.lower()

    #Remove emails
    text=  re.sub(r"\S+@+\S","",text)

    #Remove numbers
    text=  re.sub(r"\d+","",text)

    #Remove special character
    text=  re.sub(r"[^a-zA-Z\s]","",text)

    #Tokenize
    tokens = word_tokenize(text)

    filtered_words = []

    for word in tokens:

        if word.isalpha():

            if word not in stop_words:

                filtered_words.append(
                    lemmatizer.lemmatize(word, pos="v")
                )

    return " ".join(filtered_words)

clean_resume= clean_text(resume)
clean_job= clean_text(job_description)

print("  ")
print("Cleaned Resume")
print("  ")
print(clean_resume)

print("  ")
print("Cleaned job Description")
print("  ")
print(clean_job)