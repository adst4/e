from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = """Hello all, Welcome to Python Programming Academy. Python 
Programming Academy is a nice platform to learn new programming skills. It is difficult to get enrolled 
in this Academy."""

stopWords = set(stopwords.words("english"))

words = word_tokenize(text)
filtered_words =[]
for word in words:
    if word not in stopWords:
        filtered_words.append(word)
        
filtered_words