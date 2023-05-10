import csv
import nltk
from nltk.collocations import TrigramAssocMeasures, TrigramCollocationFinder
from nltk.corpus import stopwords


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

with open('/Users/kateryna_hamii/Bachelorarbeit/university/WiSe2022-2023/Bachelorarbeit/Crowler/BR/output'
          '/CorpusItself/Erdbeben.txt', 'r', encoding='utf-8') as file:
    corpus = file.read()

tokens = nltk.word_tokenize(corpus.lower())
filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

finder = TrigramCollocationFinder.from_words(filtered_tokens)
finder.apply_word_filter(lambda word: len(word) < 3)

finder.apply_freq_filter(3)
trigrams = finder.nbest(TrigramAssocMeasures().raw_freq, 50)

# create CSV file with trigrams
with open('11.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Trigram', 'Frequency'])
    for trigram in trigrams:
        if 'erdbeben' in trigram:
            frequency = finder.ngram_fd[trigram]
            writer.writerow([' '.join(trigram), frequency])
