import collections
import os
from string import punctuation
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

cwd = os.getcwd()
print("Current working directory:", cwd)

lemmatizer = WordNetLemmatizer()

# Tokenize the corpus
with open('/Users/kateryna_hamii/Bachelorarbeit/university/WiSe2022-2023/Bachelorarbeit/Crowler/BR/output/corpus_lemmatized/lemmatized_corpus_erdbeben.txt', 'r') as file:
    corpus = file.read().replace('\n', ' ').lower()

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
unrelevant_words = ['br24', 'bearbeiten','quelltext', 'tippen','einfach', 'schlagwort', 'gibt', 'besonders', 'bisher',
                    'letzten', 'nächsten', 'festgestellt', 'gilt', 'viele', 'kurz', 'allenfalls',
                    'bereits', 'ganz', 'weitere', 'darüber', 'heute', 'gestern', 'schon', 'wäre', 'kam']

stop_words = set(stopwords.words('german') + additional_stopwords + unrelevant_words)
tokenized_text = nltk.word_tokenize(corpus)

corpus_text = nltk.Text(tokenized_text)

cleaned_words = nltk.Text([word for word in corpus_text if word not in stop_words and word not in punctuation and len(word) > 2])

word_freqs = collections.Counter(corpus.split())

# Print the 10 most frequent words
for word, count in word_freqs.most_common():
    print(word, count)
