from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from parse_article import parse_article
import json


# set up the Selenium driver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # run in headless mode
driver = webdriver.Chrome(options=options)
base_url = 'https://www.br.de'
search_page_base_url = f'{base_url}/nachrichten/suche?param='

# define the list of keywords
keywords = [
    # 'Lawine',
    # 'Erdbeben',
    # 'Naturkatastrophen',
    # 'Hitze',
    # 'Flutkatastrophen',
    # 'Unwetter',
    # 'Gletscher',
    # 'Waldbrände',
    # 'Hochwasser',
    # 'Vulkan',
    # 'Tsunami',
    # 'Tornado'
]


def get_article_urls(search_results_page):
    article_urls = []
    search_results = search_results_page.select('[class^="ArticleItemResultsItem_wrapper"]')

    for search_result in search_results:
        result_link = search_result.select('a')
        if len(result_link) == 0:
            continue
        article_urls.append(result_link[0].get('href'))

    return article_urls


def load_all_articles(_driver):
    should_scroll_to_bottom = True
    loading_placeholder_selector = ':contains("Loading...")'

    while should_scroll_to_bottom:
        _driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        find_loading_text = lambda _driver: BeautifulSoup(_driver.page_source, 'html.parser').find_all(
            string='Loading...')
        loading_placeholder = find_loading_text(_driver)

        if len(loading_placeholder) == 0:
            should_scroll_to_bottom = False
        # wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, search_result_selector)) > initial_count)


for keyword in keywords:
    # construct the URL for the search query
    url = f'https://www.br.de/nachrichten/suche?param={keyword}'

    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class^="SearchResultsTable"]')))
    time.sleep(2)

    search_result_selector = '[class^="ArticleItemResultsItem_wrapper"]'
    search_results_page = BeautifulSoup(driver.page_source, 'html.parser')
    # search_results = search_results_page.select(search_result_selector)

    # uncomment after testing
    load_all_articles(driver)

    articles_urls = get_article_urls(BeautifulSoup(driver.page_source, 'html.parser'))

    with open(f'{keyword}-links.json', 'w', encoding='utf-8') as output_file:
        json.dump(articles_urls, output_file)

    # for article_subpath in articles_urls:
    #     article_url = f'{base_url}{article_subpath}'
    #     article_text = parse_article(driver, article_url)
    #
    #     with open(f'{keyword}.txt', 'a', encoding='utf-8') as output_file:
    #         output_file.write(f'{article_text}\n')


driver.quit()
