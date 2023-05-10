import csv
import os
import nltk
import re
from string import punctuation

import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

cwd = os.getcwd()
print("Current working directory:", cwd)

lemmatizer = WordNetLemmatizer()

# Tokenize the corpus
with open('/Users/kateryna_hamii/Bachelorarbeit/university/WiSe2022-2023/Bachelorarbeit/Crowler/BR/output'
          '/corpus_lemmatized/lemmatized_corpus_Waldbrände.txt', 'r') as file:
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
unrelevant_words = ['br24', 'bearbeiten', 'quelltext', 'tippen', 'einfach', 'schlagwort', 'gibt', 'besonders', 'bisher',
                    'letzten', 'nächsten', 'festgestellt', 'gilt', 'viele', 'kurz', 'allenfalls',
                    'bereits', 'ganz', 'weitere', 'darüber', 'heute', 'gestern', 'schon', 'wäre', 'kam', 'laut',
                    'artikel',
                    'schlimm', 'groß', 'woche', 'nachlassen', 'früh', 'sogenannter', 'angewiesen', 'offenbar',
                    'darunter', 'deutlich',
                    'einzeln', 'prozent', 'klar', 'groß', 'bislang', 'fast', 'beispiel', 'podcast', 'vermeidbar',
                    'schwer', 'offenbar',
                    'aktuell', 'generell', 'offiziell', 'weit', 'letzter', 'deutlich', 'schwer', 'wegen', 'beiderseits',
                    'damalig', 'gut',
                    'zuständig', 'davon', 'leid', 'klein', 'rein', 'normal', 'übrig', 'wer', 'was', 'wohin', 'wem',
                    'wen', 'verheerend', 'stark', 'möchten', 'wollen', 'können', 'müssen', 'tante', 'weiterhin',
                    'mehrere', 'zuerst',
                    'vieler', 'tiktok', 'dabei', 'gar', 'pompompom', 'gerade', 'erneut', 'gleich', 'weniger', 'massiv',
                    'dicke', 'aktiv',
                    'hart', 'regelmäßig', 'neu', 'übrigallen', 'jung', 'bald', 'stetig', 'überall', 'mieterinn', 'per',
                    'wann',
                    'schnell', 'zuvor', 'irgendwann', 'sollen', 'niedrig', 'oben', 'dass', 'trotzdem', 'lediglich',
                    'mussen', 'knapp',
                    'effektiver', 'größ', 'lassen', 'jedoch', 'dankbar', 'dürfen', 'neben', 'dafür', 'gesamt',
                    'derzeit',
                    'täglich', 'seitdem', 'schwierig', 'dadurch', 'mehrfach', 'mäßig', 'langsam', 'spät', 'derartig',
                    'abend', 'morgen','heftig','wohl',
                    'umso', 'besser', 'desto', 'unten', 'oft', 'michael', 'vorab', 'möglich', 'lange', 'obwohl', 'während']

stop_words = set(stopwords.words('german') + additional_stopwords + unrelevant_words)
tokenized_text = nltk.word_tokenize(corpus)

corpus_text = nltk.Text(tokenized_text)

cleaned_words = nltk.Text(
    [word for word in corpus_text if word not in stop_words and word not in punctuation and len(word) > 2])

bigrm = nltk.bigrams(cleaned_words)
# print(list(bigrm))
# print(*map(' '.join, bigrm), sep=', ')

bigrm = [tuple(sorted(list(b))) for b in bigrm]

erd_bigrm = [b for b in bigrm if 'brände'in b[0] or 'brände' in b[1]]
fdist = nltk.FreqDist(erd_bigrm)

csv_header = ['Word', 'Frequency']

with open('../BR/output/lists_with_frequencies/freq_dict_lemmatized/freq_dist_combined_text_lemmatized_waldbrände.csv', 'w',
          encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(csv_header)
    for word, freq in fdist.most_common():
        csvwriter.writerow([word, freq])

print(list(fdist.most_common()))
