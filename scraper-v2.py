from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json
# import urllib

import requests # python -m pip install requests

DEBUG = True

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


def getWebsiteInfoBotlike(domain: str):
    url = f'https://www.similarweb.com/website/{domain}/#overview'
    if DEBUG:
        print(url)
    # page = urllib.request.urlopen(url)
    page = requests.get(url)
    if DEBUG:
        print(page.text)
        # <dd class="data-company-info__list-item data-company-info__list-item--value">United States, California, San Bruno</dd>
        # <dd class="data-company-info__list-item data-company-info__list-item--value"><a class="data-company-info__link" href="/top-websites/category/arts-and-entertainment/tv-movies-and-streaming/">Arts &amp; Entertainment &gt; TV Movies and Streaming</a></dd>
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.prettify())

def getWebsiteInfoChromelike(domain: str):
    url = f'https://www.similarweb.com/website/{domain}/#overview'
    if DEBUG:
        print(url)
    driver.get(url)
    if DEBUG:
        print(driver.page_source)
        # <dd class="data-company-info__list-item data-company-info__list-item--value">United States, California, San Bruno</dd>
        # <dd class="data-company-info__list-item data-company-info__list-item--value"><a class="data-company-info__link" href="/top-websites/category/arts-and-entertainment/tv-movies-and-streaming/">Arts &amp; Entertainment &gt; TV Movies and Streaming</a></dd>
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())



getWebsiteInfo('youtube.com')


# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
# driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
#     name = a.find('div', attrs={'class':'_3wU53n'})
#     price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
#     rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
#     products.append(name.text)
#     prices.append(price.text)
#     ratings.append(rating.text)

# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')
