import os

import spacy


cwd = os.getcwd()
print("Current working directory:", cwd)

# load the German language model
nlp = spacy.load('de_core_news_sm')

# read in corpus from file
with open('/Users/kateryna_hamii/Bachelorarbeit/university/WiSe2022-2023/Bachelorarbeit/CorpusAndCrawler/BR24/Korpus'
          '/Subcorpora/Flutkatastrophen.txt', 'r', encoding='utf-8') as file:
    corpus = file.read()

# tokenize the corpus
doc = nlp(corpus)

# lemmatize each token and join back into string
lemmatized_corpus = ' '.join([token.lemma_ for token in doc])

# save lemmatized corpus to file
with open('../BR24/Korpus/corpus_lemmatized/lemmatized_corpus_Flutkatastrophen_lg.txt', 'w', encoding='utf-8') as file:
    file.write(lemmatized_corpus)
