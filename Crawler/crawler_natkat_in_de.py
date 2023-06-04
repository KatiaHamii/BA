import requests
from bs4 import  BeautifulSoup

url = "https://www.klimanavigator.eu/dossier/artikel/012154/index.php"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

content = soup.find('div', class_='gridColLeft')
for tag in content.select('h2, .impImgContainer, .moduleC9.clearfix'):
    tag.decompose()

text = content.get_text()

# save the extracted text to a txt file
with open('Naturkatastrophen_in_de.txt', 'w', encoding='utf-8') as file:
    file.write(text)