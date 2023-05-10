import os

import spacy
import csv
from collections import defaultdict

nlp = spacy.load("de_core_news_sm")


cwd = os.getcwd()
print("Current working directory:", cwd)

# Read the corpus from a file
with open("../BR/output/CorpusItself/combined_text.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

# Define a list of stop words to remove
stop_words = spacy.lang.de.stop_words.STOP_WORDS

# Define the chunk size
# This code splits the corpus into chunks of 100,000 characters
# and counts the word frequencies in each chunk separately using the spaCy language model.
chunk_size = 100000

# Split the corpus into chunks of 100,000 characters
chunks = [corpus[i:i+chunk_size] for i in range(0, len(corpus), chunk_size)]

# Count the frequencies of each word in each chunk
word_freq = defaultdict(int)
for chunk in chunks:
    doc = nlp(chunk)
    for token in doc:
        if token.text.lower() not in stop_words:
            word_freq[token.text.lower()] += 1

# Write the results to a CSV file
with open("../BR/output/word_freq.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word", "Frequency"])
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([word, freq])
