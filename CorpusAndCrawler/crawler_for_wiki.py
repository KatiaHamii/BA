import requests
from bs4 import BeautifulSoup

urls = ['https://de.wikipedia.org/wiki/Deich, '
        'https://de.wikipedia.org/wiki/Entwaldung',
        'https://de.wikipedia.org/wiki/%C3%9Cberweidung',
        'https://de.wikipedia.org/wiki/Bodenverfl%C3%BCssigung',
        'https://de.wikipedia.org/wiki/Vulkanausbruch',
        'https://de.wikipedia.org/wiki/Lava',
        'https://de.wikipedia.org/wiki/Vulkanische_Asche',
        'https://de.wikipedia.org/wiki/Pyroklastischer_Strom',
        'https://de.wikipedia.org/wiki/Supervulkan',
        'https://de.wikipedia.org/wiki/Vulkanischer_Winter',
        'https://de.wikipedia.org/wiki/Gletscherlauf',
        'https://de.wikipedia.org/wiki/Lahar',
        'https://de.wikipedia.org/wiki/Tsunami',
        'https://de.wikipedia.org/wiki/Massenbewegung_(Geologie)',
        'https://de.wikipedia.org/wiki/Steinschlag',
        'https://de.wikipedia.org/wiki/Erdrutsch',
        'https://de.wikipedia.org/wiki/Bergsturz',
        'https://de.wikipedia.org/wiki/Murgang',
        'https://de.wikipedia.org/wiki/Lawine',
        'https://de.wikipedia.org/wiki/Anomalie_(Meteorologie)',
        'https://de.wikipedia.org/wiki/Unwetter',
        'https://de.wikipedia.org/wiki/Sturmflut',
        'https://de.wikipedia.org/wiki/Hochwasser',
        'https://de.wikipedia.org/wiki/Orkan',
        'https://de.wikipedia.org/wiki/Sturm',
        'https://de.wikipedia.org/wiki/Trog_(Meteorologie)',
        'https://de.wikipedia.org/wiki/Tornado',
        'https://de.wikipedia.org/wiki/Hurrikan',
        'https://de.wikipedia.org/wiki/Schneeverwehung',
        'https://de.wikipedia.org/wiki/Regen#Starkregen',
        'https://de.wikipedia.org/wiki/Taifun',
        'https://de.wikipedia.org/wiki/Regen#Dauerregen_(Landregen)',
        'https://de.wikipedia.org/wiki/Hagel',
        'https://de.wikipedia.org/wiki/Schneelast',
        'https://de.wikipedia.org/wiki/Wintergl%C3%A4tte',
        'https://de.wikipedia.org/wiki/Regen#Unterk%C3%BChlter_Regen_(Klareis)',
        'https://de.wikipedia.org/wiki/Hitzewelle',
        'https://de.wikipedia.org/wiki/Jahrhundertsommer',
        'https://de.wikipedia.org/wiki/Tauwetter',
        'https://de.wikipedia.org/wiki/K%C3%A4ltewelle',
        'https://de.wikipedia.org/wiki/Gezeiten',
        'https://de.wikipedia.org/wiki/Smog',
        'https://de.wikipedia.org/wiki/Wanderheuschrecken',
        'https://de.wikipedia.org/wiki/Impakt',
        'https://de.wikipedia.org/wiki/Weltraumwetter',
        'https://de.wikipedia.org/wiki/Sonnenwind']

all_text = ""

# send a request to the webpage
for url in urls:
    # send a request to the webpage
    response = requests.get(url)

    # parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # find the main content of the page by class name
    content = soup.find('div', class_='mw-parser-Korpus')

    # check if content exists
    if content:
        # remove the elements that are not needed
        for tag in content.select(
                '.thumb.tright, #toc, .mw-headline, .references, #normdaten, .sisterproject, h2, [rel="nofollow"]'):
            tag.decompose()

        # get the text from the remaining elements
        text = content.get_text()
        all_text += text

    # save the extracted text to a txt file
with open('all_wiki_articles_v2.txt', 'a', encoding='utf-8') as file:
    file.write(all_text)
