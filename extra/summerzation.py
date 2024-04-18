from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize
import re
# Text preprocessing function
def preprocess_text(text):
    # Remove special characters and digits
    processed_text = re.sub(r'[^a-zA-Z\s]', '', text)
    processed_text = re.sub(r'\d+', '', processed_text)
    return processed_text

# Example text paragraph
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between 
computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. 
The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. 
The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves. 
Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.
"""

# Preprocess the text
formated_text = preprocess_text(text)

stopWords = set(stopwords.words("english"))
words = word_tokenize(formated_text)

wordfreq = {}
for word in words:
    if word in stopWords:
        continue
    if word in wordfreq:
        wordfreq[word]+=1
    else:
        wordfreq[word] =1

maximum_freq = max(wordfreq.values())

for word in wordfreq.keys():
    wordfreq[word] = (wordfreq[word]/maximum_freq)

sentences  = sent_tokenize(text)
sentencesValue = {}
for sentence in sentences:
    for word,frq in wordfreq.items():
        if word in sentence.lower():
            if sentence in sentencesValue:
                sentencesValue[sentence] += frq
            else:
                sentencesValue[sentence] = frq


import heapq 
summary = '' 
summary_sentence = heapq.nlargest(10,sentencesValue , key = sentencesValue.get)
summary = ' '.join(summary_sentence)
summary