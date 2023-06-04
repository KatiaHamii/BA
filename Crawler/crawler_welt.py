import requests
from bs4 import BeautifulSoup

url = "https://www.welt.de/vermischtes/katastrophen/article243119743/Indonesien-Schweres-Erdbeben-mit-einer-Staerke-von-7-6-bis-7-9.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

text_blocks = soup.select('.c-article-text p')
text = "\n".join([p.get_text() for p in text_blocks])

with open('all_wiki_articles_v2.txt', 'a', encoding='utf-8') as f:
    f.write(text)
