# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd

def nasa_news_article_scrape(article):
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text
    return ( {"title":news_title, "description":news_p})

def astrogeology_scrape(browser, hemisphere):
    title = hemisphere.find("h3").text.replace('Enhanced', '')
    img_loc_url = "https://astrogeology.usgs.gov" + hemisphere.find('a')['href']
    browser.visit(img_loc_url)
    html = browser.html
    hem_soup = BeautifulSoup(html, 'html.parser')
    downloads = hem_soup.find_all("div", class_='downloads')
    img_url = [d.a['href'] for d in downloads]
    return ({'title': title, 'img_url': img_url[0]})

def nasa_news_scrape(browser):
    # NASA News : Scrape NASA Planet News Site for the latest News.
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all("div", class_='list_text')
    nasa_mars_news = [nasa_news_article_scrape(a) for a in articles]

    return(nasa_mars_news)

def jpl_images_scrape(browser):
    # JPL Mars Space Images 

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    background_image = soup.find("article", class_='carousel_item')['style']
    featured_image_url = "https://www.jpl.nasa.gov" + background_image.split('\'')[1]
    return( featured_image_url)

def planet_weather_tweet(browser):
    # Mars Weather tweet
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('div',class_='js-tweet-text-container').p.getText().strip()
    mars_weather = mars_weather.split("pic.twitter.com")[0]
    return(mars_weather)

def planet_facts_html():
    # Mars Facts
    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Planet Facts', 'Values']
    df.set_index('Planet Facts', inplace = True)
    mars_facts = df.to_html(header=False, index=True)
    return(mars_facts)

def planet_hemispheres(browser):
    # Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find("div", class_='collapsible results')
    hemispheres = results.find_all("div", class_='item')
    hemisphere_image_urls = [astrogeology_scrape(browser, h) for h in hemispheres]
    return( hemisphere_image_urls)


def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    data = {}
    data["nasa_news"] = nasa_news_scrape(browser)[0]
    data["jpl_image"] = jpl_images_scrape(browser)
    data['planet_weather_tweet'] = planet_weather_tweet(browser)
    data['planet_facts_html'] = planet_facts_html()
    data["planet_hemispheres"] = planet_hemispheres(browser)
    return(data)

# if __name__ == "__main__":
#     data = scrape()
#     print(data)

    