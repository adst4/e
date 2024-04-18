from nltk.tokenize import word_tokenize ,sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt


text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between 
computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. 
The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. 
The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves. 
Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.
"""

stopWords = set(stopwords.words("english"))

# Tokenizing the paragraph
words = word_tokenize(text)

# removing stop word
wordfrq = {}
for word in words:
    if word in stopWords:
        continue
    if word in wordfrq:
        wordfrq[word]+=1 
    else:
        wordfrq[word] = 1

# plotting the frequencies
frequency_dist = FreqDist(wordfrq)
frequency_dist.plot(32 , cumulative=False)
plt.show()