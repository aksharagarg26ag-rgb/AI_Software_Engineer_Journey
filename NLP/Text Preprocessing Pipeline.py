import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

input = "Hello!! My name is Akshara. I am studying AI Software Engineering in 2026!!!"

stopword = set(stopwords.words("english"))
lemmatizor= WordNetLemmatizer()

def clean_text(input):
    #Lowercase
    input= input.lower()
    print(input)
 
    #Tokenize
    tokens = word_tokenize(input)
    print(tokens)

    filtered_words = []
    for word in tokens:
        if word.isalpha():
            if word not in stopword:
                filtered_words.append(lemmatizor.lemmatize(word, pos="v"))

    return " ".join(filtered_words)
print(clean_text(input))      




