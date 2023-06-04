import requests
from bs4 import BeautifulSoup

url = 'https://www.spiegel.de/panorama/missouri-mehrere-menschen-sterben-bei-tornado-in-bollinger-county-a-98db5b9b-a541-430d-a682-43e8b3996096'

# send a request to the webpage
response = requests.get(url)

# parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the main content of the page by class name
content = soup.find('div', class_='mw-parser-Korpus')

# remove the elements that are not needed
for tag in content.select('.align-middle", p, .RichText RichText--sans leading-loose lg:text-xl md:text-xl sm:text-l lg:mb-32 md:mb-32 sm:mb-24,'):
    tag.decompose()

# get the text from the remaining elements
text = content.get_text()

# save the extracted text to a txt file
with open('naturkatastrophe_spiegel.txt', 'w', encoding='utf-8') as file:
    file.write(text)
