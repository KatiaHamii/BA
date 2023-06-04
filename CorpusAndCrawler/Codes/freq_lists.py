import os
import re

import nltk
from nltk.corpus import stopwords
from string import punctuation
import csv

nltk.download('stopwords')

cwd = os.getcwd()
print("Current working directory:", cwd)
# Load the German stop words from NLTK and add some additional words to exclude

additional_stopwords = ['ab', 'ansonsten', 'außer', 'etwa', 'ganzen', 'irgend', 'irgendwo', 'je', 'jemals', 'jemand',
                        'manch', 'mindestens', 'sogar', 'sobald', 'solang', 'irgendwas', 'sogar', 'deren', 'dessen',
                        'selbst', 'kaum', 'meisten', 'insgesamt', 'anderen', 'einigermaßen', 'vollständig', 'notwendig',
                        'ausreichend', 'allerdings', 'nichtsdestotrotz', 'deshalb', 'dementsprechend', 'hiermit',
                        'erstens', 'zweitens', 'beispielsweise', 'unter anderem', 'kurzum', 'insofern', 'im Übrigen',
                        'folgendermaßen', 'nämlich', 'bekanntlich', 'darum', 'dannen', 'irgendwohin', 'ebenfalls',
                        'eher', 'allein', 'alleine', 'anderswo', 'übrigen', 'eigentlich', 'unbedingt', 'gegenüber',
                        'gewissermaßen', 'gleichsam', 'irgendjemand', 'irgendwie', 'jeglicher', 'jedweder', 'mindest',
                        'mehrerer', 'mithilfe', 'nachdem', 'nimmermehr', 'nur noch', 'obgleich', 'obschon', 'ohnehin',
                        'nochmals', 'respektive', 'sodass', 'soweit', 'teilweise', 'vor allem', 'vorerst', 'vormals',
                        'weshalb', 'wieviel', 'wiederum', 'währenddessen', 'wohlweislich', 'wozu', 'zudem', 'zumal',
                        'zurückhalten', 'zuzüglich', 'mehr', 'sei', 'seit', 'wurden', 'wurde', 'rund', 'seien', 'immer' ]

stop_words = set(stopwords.words('german') + additional_stopwords)
print((stopwords.words('german')))

with open('CorpusAndCrawler/BR24/Korpus/Subcorpora/whole_corpus.txt', 'r') as file:
    corpus = file.read().replace('\n', ' ').lower()

# Tokenize the corpus
words = nltk.word_tokenize(corpus)
# Exclude stop words, punctuation, and any word shorter than 3 characters
words = [word for word in words if word not in stop_words and word not in punctuation and len(word) > 2]

fdist = nltk.FreqDist(words)

text = ' '.join(words)
# Find all matches in the text
# matches = re.findall(pattern, text)

# Print the matches
# print(set(matches))
# print(len(matches))
with open('freq_dist_combined_text.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Word', 'Frequency'])
    for word, freq in fdist.most_common():
        csvwriter.writerow([word, freq])
# Print the number of unique words in the frequency distribution
print("Number of unique words:", len(fdist))
