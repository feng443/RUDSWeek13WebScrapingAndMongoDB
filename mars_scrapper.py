"""

<Chan Feng> 2018-05-04 Rutgers Data Science Boot Camp Assignment Week 13. Web scrapping, MongoDB and Flask

This file provide functions to retrieve information for the Flask App

"""

import time
import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
from splinter import Browser

def get_mars_news():
    url = 'https://mars.nasa.gov/news/'
    with Browser('chrome') as browser:
        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = bs4(html,'lxml')
        news_title = soup.find('div', class_='content_title').a.text.strip()
        news_p = soup.find('div', class_='article_teaser_body').text.strip()
    return (news_title, news_p)

def get_feature_image_url():
    base_url = 'https://www.jpl.nasa.gov/'
    url = f'{base_url}/spaceimages/?search=&category=Mars'
    with Browser('chrome') as browser:
        browser.visit(url)
        time.sleep(1)
        browser.click_link_by_id('full_image')
        time.sleep(1)
        browser.click_link_by_partial_text('more info')
        time.sleep(1)
        soup = bs4(browser.html, 'lxml')
        image_url = soup.find('figure', class_='lede').a['href']
    return base_url + image_url

def get_mars_weather():
    return bs4(
        requests.get(
            'https://twitter.com/marswxreport?lang=en'
        ).text, 'lxml').find('p', class_='TweetTextSize').text

def get_mars_fact_html():
    return pd.read_html(str(
        bs4(
        requests.get(
            'https://space-facts.com/mars/'
        ).text, 'lxml').find_all('table', class_='tablepress-id-mars')
    ))[0].rename(columns={0: 'Measure', 1: 'Value'}).to_html(index=False)


def get_mars_hemispheres():
    base_url = 'https://astrogeology.usgs.gov'
    url = f'{base_url}/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls = []
    with Browser('chrome') as browser:
        browser.visit(url)
        time.sleep(1)
        for item in bs4(browser.html, 'lxml').find_all('div', class_='item'):
            product_item = item.find('a', class_='product-item')
            title = product_item.img['alt'].replace(' Enhanced thumbnail', '')
            href = product_item['href']
            hemisphere_image_urls.append(dict(
                title=title,
                image_url=base_url + bs4(requests.get(
                    f'{base_url}{href}').text, 'lxml'
                                         ).find('img', class_='wide-image')['src']
            ))

    return hemisphere_image_urls

def get_mission_to_mars_info():
    (news_title, news_p) = get_mars_news()
    return dict(
        news_title=news_title,
        news_p=news_p,
        featured_image_url=get_feature_image_url(),
        mars_weather=get_mars_weather(),
        mars_fact_html=get_mars_fact_html(),
        hemisphere_image_urls=get_mars_hemispheres(),
    )