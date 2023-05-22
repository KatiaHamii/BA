import csv
import os
from string import punctuation

import nltk
from nltk import WordNetLemmatizer, FreqDist, ngrams
from nltk import trigrams
from nltk.corpus import stopwords
nltk.download('stopwords')

cwd = os.getcwd()
print("Current working directory:", cwd)

lemmatizer = WordNetLemmatizer()

# Datei mit dem Korpus einlesen
with open('C:\\Users\\kater\\PycharmProjects\\Bachelorarbeit_v2_fromGIT\\Crowler\\BR\\output\\CorpusItself\\combined_text.txt', 'r', encoding='utf-8') as file:
    corpus = file.read().replace('\n', ' ').lower()

# Laden der deutschen Stopwörter


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
                    'artikel','schlimm', 'groß', 'woche', 'nachlassen', 'früh', 'sogenannter', 'angewiesen', 'offenbar',
                    'darunter', 'deutlich', 'einzeln', 'prozent', 'klar', 'groß', 'bislang', 'fast', 'beispiel', 'podcast', 'vermeidbar',
                    'schwer', 'offenbar','aktuell', 'generell', 'offiziell', 'weit', 'letzter', 'deutlich', 'schwer', 'wegen', 'beiderseits',
                    'damalig', 'gut','zuständig', 'davon', 'leid', 'klein', 'rein', 'normal', 'übrig', 'wer', 'was', 'wohin', 'wem',
                    'wen', 'verheerend', 'stark', 'möchten', 'wollen', 'können', 'müssen', 'tante', 'weiterhin',
                    'mehrere', 'zuerst','vieler', 'tiktok', 'dabei', 'gar', 'pompompom', 'gerade', 'erneut', 'gleich', 'weniger', 'massiv',
                    'dicke', 'aktiv','hart', 'regelmäßig', 'neu', 'übrigallen', 'jung', 'bald', 'stetig', 'überall', 'mieterinn', 'per',
                    'wann','schnell', 'zuvor', 'irgendwann', 'sollen', 'niedrig', 'oben', 'dass', 'trotzdem', 'lediglich',
                    'mussen', 'knapp','effektiver', 'größ', 'lassen', 'jedoch', 'dankbar', 'dürfen', 'neben', 'dafür', 'gesamt',
                    'derzeit','täglich', 'seitdem', 'schwierig', 'dadurch', 'mehrfach', 'mäßig', 'langsam', 'spät', 'derartig',
                    'abend', 'morgen','heftig','wohl','umso', 'besser', 'desto', 'unten', 'oft', 'michael', 'vorab', 'möglich', 'lange', 'obwohl', 'während',
                    'geben','frei','riesig', 'region', 'montag','dienstag', 'mittwoch', 'donnerstag', 'freitag', 'samstag', 'sonntag', 'jahr',
                    'hinweis','erfahrung', 'fit','vergleich', 'rechnen', 'tag', 'vermehrt', 'erwart', 'außerdem', 'ober', 'anfällig', 'absuchen', 'pass', 'gelegt',
                    'unklar', 'feststellen', 'geben', 'setzen', 'kommen', 'ermitteln',  'nacht',
                    'tag',  'worden', 'meter', 'hätte', 'news', 'gab', 'weiteres', 'peter', 'martin',
                    'häufig', 'denen', 'zweieinhalb', 'traf', 'lag', 'gemeldet', 'nähe', 'donnerstagmorgen', 'tagen'
                    , 'siehe', 'vergleichen', 'derweil', 'eingestellt', 'inzwischen','rundschau', 'angesichts', 'istdie',
                    'hat.insight',  'aufgezeichnet', 'aufgezeichnet', 'beschleunigen', 'lässt, durchforsteten', 'gegeben',
                    'betreibt', 'insight', 'sogenannte', 'wurden.', 'eingeschaltet.bergungsarbeiten', 'folge.das',
                    'fall.zum', 'sein.die', 'nicht-mitglieder.zum', 'seien.durch', 'aus.das', 'bohnhoff.zwar', 'mit.forscher',
                    'an.durch', 'verheerenden', 'stadt', 'veröffentlichte', 'mittelpunkt', 'beschlossen', 'regionale', 'stellen.für',
                    'ebenso',  'hrsg', 'bild', 'unterwegs', 'blidinje', 'zusätzlich','sichernunter', 'aufrichten', 'freilegen','außerorts'
                    'gemacht', 'zugleich', 'angestoßen', 'lobt', 'nimmt', 'richtig', 'allzu', 'wenige', 'nein', 'sowie',
                    'demnach', 'könnten', 'geschah', 'existenzielle', 'ist.so', 'befürchtendass', 'einzige', 'gebe', 'umgehend', 'zumindest',
                    'sei.warnung', 'gebietendie', 'bayreuth.ausuferungen', 'gewöhnt', 'sieht', 'bedroht',
                    'sturm', 'allgemeinen', 'verstehen', 'vorliegen', 'behauptet','ausgesetzt', 'uhr', 'möglicherweise', 'könne',
                    'raste', 'km/h','metern','erwarten', 'garantiert.das', 'urteil', 'infolge', 'erreicht', 'mhw', 'spricht', 'offizielle', 'möglich.am',
                    'geschlossenin', 'davor', 'besprach' , 'gehabt.züge', 'gepäck.morgen', 'möglichder', 'beschädigt.heftiger', 'piloten', 'schnell',
                    'wichtige','geleitet','vergangenen', 'technischem', 'ausreichende', 'ereignete', 'jahreszeit', 'bedeutet', 'schüsse', 'unterdessen',
                    'abc', 'unterdessen', 'bringen','frau','gelangen', 'dlrg', 'halb','dennoch', 'glaub', 'drauf', 'sollt'
                    ]

stop_words = set(stopwords.words('german') + additional_stopwords + unrelevant_words)
# Tokenisierung des Korpus in Wörter
tokenized_text = nltk.word_tokenize(corpus)

corpus_text = nltk.Text(tokenized_text)

cleaned_words = nltk.Text(
    [word for word in corpus_text if word not in stop_words and word not in punctuation and len(word) > 2])

trigram_list = list(trigrams(cleaned_words))
trigram = [tuple(sorted(list(b))) for b in trigram_list]

desired_word = "maßnahme" or "versicherung"

wordInTrigram = [b for b in trigram if desired_word in b[0] or desired_word in b[1] or  desired_word in b[2]]


# Berechnung der Wortfrequenzen
freq_dist = FreqDist(wordInTrigram)
csv_header = ['Word', 'Frequency']

with open(f"../BR/output/lists_with_frequencies/viergram_freq_dist_combined_text_{desired_word}.csv", "w",encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(csv_header)
    for word, freq in freq_dist.most_common():
        csvwriter.writerow([word, freq])

print(list(freq_dist.most_common()))

print(len(list(freq_dist.most_common())))