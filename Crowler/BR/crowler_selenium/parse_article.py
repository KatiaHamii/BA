from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def parse_article(driver, article_url):
    driver.get(article_url)

    article_content_selector = '#articlebody [class^="ArticleModuleText_content"]'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, article_content_selector)))
    time.sleep(2)
    article_page = BeautifulSoup(driver.page_source, 'html.parser')

    article_elements = article_page.select(article_content_selector)
    if len(article_elements) == 0:
        return ''

    article_element = article_elements[0]
    article_text = article_element.text

    return article_text
