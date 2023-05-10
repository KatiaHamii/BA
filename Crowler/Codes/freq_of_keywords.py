import os

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

cwd = os.getcwd()
print("Current working directory:", cwd)

# Laden Sie den Korpus und extrahieren Sie den Text
with open("../BR/output/CorpusItself/combined_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenisieren des Textes und Entfernen von Stoppwörtern
tokens = word_tokenize(text.lower())

stop_words = set(stopwords.words("german"))
filtered_tokens = [token for token in tokens if token not in stop_words]

# Extrahieren von relevanten Begriffen zum Thema Naturkatastrophen
relevant_words = ["Erdbeben",
                    "Tsunami",
                    "Hurrikan",
                    "Tornado",
                    "Waldbrad",
                    "Überschwemmung",
                    "Dürre",
                    "Hagelstur",
                    "Schlammlawine",
                    "Lawine",
                    "Vulkanausbruch",
                    "Wirbelsturm",
                    "Sturmflut",
                    "Erdbebenwelle",
                    "Schneesturm",
                    "Blitzschlag",
                    "Eissturm",
                    "Küstenüberflutung",
                    "Staubsturm",
                    "Erdrutsch",
                  "Waldsterben",
                  "Erdbebenrisse",
                  "Schneelawine",
                  "Schneeverwehungen",
                  "Tornadowarnung",
                  "Hurrikanwarnung",
                  "Hagelschauer",
                  "Gewittersturm",
                  "Flutwelle",
                  "Starkregen",
                  "Sandsturm",
                  "Beben",
                  "Klimawandel",
                  "Schneeschmelze",
                  "Trockenheit",
                  "Hitzewelle",
                  "Frost",
                  "Eisregen",
                  "Eisbrocken",
                  "Hailstorm",
                  "Murenabgang",
                  "Schneeverwehung",
                  "Orkanböen",
                  "Sintflut",
                  "Gletscherabbruch",
                  "Schneedrift",
                  "Frostschäden",
                  "Sturmböen",
                  "Schneematsch",
                  "Überflutung"
                  ]

disaster_words = [word for word in filtered_tokens if word in relevant_words]

# Anzeigen der häufigsten Wörter und Begriffe
word_counts = Counter(disaster_words)
print(word_counts.most_common())
