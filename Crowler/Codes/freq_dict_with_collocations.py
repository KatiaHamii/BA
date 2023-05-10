import os
import re

import nltk
import wn as wn
from nltk import BigramCollocationFinder, WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation
import csv

cwd = os.getcwd()
print("Current working directory:", cwd)

lemmatizer = WordNetLemmatizer()

# Tokenize the corpus
with open('/Users/kateryna_hamii/Bachelorarbeit/university/WiSe2022-2023/Bachelorarbeit/Crowler/BR/output/CorpusItself/combined_text.txt', 'r') as file:
    corpus = file.read().replace('\n', ' ').lower()
    words = nltk.word_tokenize(corpus, language='german')


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
                        'zurückhalten', 'zuzüglich', 'mehr', 'sei', 'seit', 'wurden', 'wurde', 'rund', 'seien', 'immer',
                        ]
unrelevant_words = ['br24', 'bearbeiten','quelltext', 'tippen','einfach', 'schlagwort', ]

stop_words = set(stopwords.words('german') + additional_stopwords)

words = [word for word in words if word not in stop_words and word not in punctuation and len(word) > 2]

# Create an NLTK Text object
text = nltk.Text(words)

print(text.collocation_list())