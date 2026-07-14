# 📄 Resume Screening System

A Python-based Resume Screening System that compares multiple resumes with a job description using **Natural Language Processing (NLP)** and **TF-IDF Vectorization**. The system calculates similarity scores and extracts relevant technical skills to identify the most suitable candidates.

---

## 🚀 Features

- Clean and preprocess resume text
- Extract technical skills from resumes
- Convert text into TF-IDF vectors
- Calculate cosine similarity between resumes and job descriptions
- Rank resumes based on similarity score
- Modular and production-ready project structure

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- NLTK
- NumPy

---

## 📂 Project Structure

```
ResumeScreeningSystem/
│
├── data/
│   ├── job_description.txt
│   ├── resume1.txt
│   ├── resume2.txt
│   └── resume3.txt
│
├── models/
│
├── src/
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── similarity.py
│   └── skills.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aksharagarg26ag-rgb/ResumeScreeningSystem.git
```

### 2. Navigate to the project

```bash
cd ResumeScreeningSystem
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 🧠 How It Works

1. Load the job description and resumes.
2. Preprocess the text (lowercase, remove punctuation, remove stopwords).
3. Convert the text into TF-IDF vectors.
4. Compute cosine similarity between each resume and the job description.
5. Extract technical skills from resumes.
6. Display similarity scores and rank the resumes.

---

## 📊 Sample Output

```
Resume 1
Similarity Score : 82.45%

Matched Skills:
✔ Python
✔ SQL
✔ Machine Learning
✔ Pandas

-------------------------

Resume 2
Similarity Score : 68.17%

Matched Skills:
✔ Java
✔ MySQL
✔ Git

-------------------------

Best Matching Resume : Resume 1
```

---

## 📌 Modules

### preprocessing.py

- Clean text
- Remove punctuation
- Remove stopwords
- Normalize text

### vectorizer.py

- TF-IDF Vectorization
- Feature generation

### similarity.py

- Cosine similarity calculation
- Resume ranking

### skills.py

- Skill extraction
- Skill matching

### app.py

- Main application
- Integrates all modules

---

## 🔮 Future Improvements

- PDF and DOCX resume support
- Named Entity Recognition (NER)
- BERT/Sentence Transformers for semantic similarity
- Streamlit Web Interface
- FastAPI Backend
- Resume ranking dashboard
- Skill gap analysis
- Resume recommendations

---

## 📈 Learning Outcomes

This project demonstrates:

- Natural Language Processing (NLP)
- Text Preprocessing
- TF-IDF Vectorization
- Cosine Similarity
- Modular Python Programming
- Production-style Project Architecture

---

## 👩‍💻 Author

**Akshara Garg**

B.Tech Computer Science Engineering (Data Science)

Bennett University