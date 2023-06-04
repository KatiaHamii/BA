import requests
from bs4 import BeautifulSoup

# list of URLs to crawl
urls = [
    'https://www.spiegel.de/panorama/missouri-mehrere-menschen-sterben-bei-tornado-in-bollinger-county-a-98db5b9b-a541-430d-a682-43e8b3996096',
    'https://www.spiegel.de/wirtschaft/naturkatastrophen-richteten-schaeden-in-hoehe-von-275-milliarden-dollar-an-a-b8cab468-7e57-47e5-a610-620a2d30e8a9',
    'https://www.manager-magazin.de/politik/naturkatastrophen-weltweiter-schaden-steigt-auf-275-milliarden-dollar-a-350c0236-b315-4697-8406-95929f2fddb3',
    'https://www.spiegel.de/wirtschaft/unternehmen/erdbeben-in-tuerkei-und-syrien-kostet-versicherer-bis-zu-vier-milliarden-dollar-a-9da4e904-f713-4a6b-bcb7-e250c6704f84',
    'https://www.spiegel.de/wirtschaft/service/naturkatastrophen-vorstoss-fuer-pflichtversicherung-gegen-elementarschaeden-a-3cc22c4b-61c3-46a3-92f9-271a59bd4624',
    'https://www.spiegel.de/ausland/erdbeben-in-tuerkei-und-syrien-katastrophe-trifft-viele-ohnehin-schon-schutzlose-syrer-a-a9108848-e304-4f9f-b8f1-485269a028dd',
    'https://www.spiegel.de/panorama/australien-hochwasser-hat-verheerende-auswirkungen-a-feecd03a-5bce-4d83-88c9-99977345dd58',
    'https://www.spiegel.de/panorama/tuerkei-erdbeben-erschuettert-nordwesten-des-landes-mehr-als-20-verletzte-a-a543dbd4-d673-4287-8db6-2ac997d2e80b',


]

# open the Korpus file for writing
with open('output.txt', 'w', encoding='utf-8') as outfile:

    # loop through the URLs
    for url in urls:

        # send a request to the webpage
        response = requests.get(url)

        # parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # select the elements to extract
        elements = soup.select('.align-middle, .RichText.RichText--sans.leading-loose.lg\\:text-xl.md\\:text-xl.sm\\:text-l.lg\\:mb-32.md\\:mb-32.sm\\:mb-24, p')

        # extract the text from the selected elements
        text = ''.join([e.get_text() for e in elements])

        # write the extracted text to the Korpus file
        outfile.write(text)

        # add a separator between pages
        outfile.write('\n\n')
