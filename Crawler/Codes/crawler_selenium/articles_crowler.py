import os

from selenium import webdriver
import json
from parse_article import parse_article

folder_path = '../../BR24/'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # run in headless mode
driver = webdriver.Chrome(options=options)
base_url = 'https://www.br.de'

# Iterate over all files in folder
for filename in os.listdir(folder_path):
    # Check if file has .json extension
    if filename.endswith('.json'):
        keyword = filename.split("-")[0]
        print(filename, keyword)

        # Do something with JSON file
        json_file_path = os.path.join(folder_path, filename)
        with open(json_file_path, 'r') as f:
            articles_urls = json.load(f)
            # Do something with JSON data
            for article_subpath in articles_urls:
                article_url = f'{base_url}{article_subpath}'
                try:
                    article_text = parse_article(driver, article_url)

                    with open(f'{keyword}.txt', 'a', encoding='utf-8') as output_file:
                        output_file.write(f'{article_text}\n')
                finally:
                    continue

