import requests
from bs4 import BeautifulSoup

# specify the URL of the page
url = "https://www.munichre.com/de/unternehmen/media-relations/medieninformationen-und-unternehmensnachrichten/medieninformationen/2022/naturkatastrophen-bilanz-erstes-halbjahr-2022.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
richtext_element = soup.find("div", class_="richtext")
text = richtext_element.get_text().strip()

# append the text to the existing file
with open("all_wiki_articles_v2.txt", "a", encoding="utf-8") as file:
    file.write(text)
