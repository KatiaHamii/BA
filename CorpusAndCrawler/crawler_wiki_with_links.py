import requests
from bs4 import BeautifulSoup

url = 'https://de.wikipedia.org/wiki/Naturkatastrophe'

# send a request to the main web page
response = requests.get(url)

# parse the HTML content of the main page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all links with <a> tags that contain references to other pages
links = soup.select('a[href^="/wiki/"]')

# create an empty list to store the plain text and referenced text
texts = []

# loop through the links and extract the plain text and referenced text
for link in links:
    # extract the href attribute from the link
    href = link.get('href')
    # check if the href attribute is a reference to another page
    if ':' not in href and '#' not in href:
        # build the URL of the referenced page
        ref_url = 'https://de.wikipedia.org' + href
        # send a request to the referenced page
        ref_response = requests.get(ref_url)
        # parse the HTML content of the referenced page with BeautifulSoup
        ref_soup = BeautifulSoup(ref_response.content, 'html.parser')
        # extract the plain text from the referenced page
        ref_text = ref_soup.get_text()
        # append the referenced text to the list
        texts.append(ref_text)
    # extract the plain text from the main page
    text = link.get_text()
    # append the plain text to the list
    texts.append(text)

# extract the plain text from the main page
main_text = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ul', 'li'])
# loop through the extracted elements and add their text content to the 'texts' list
for element in main_text:
    texts.append(element.get_text())

# merge the text into a single string
text = '\n'.join(texts)

# save the extracted text to a txt file
with open('natkat_wiki_edited.txt', 'w', encoding='utf-8') as file:
    file.write(text)
