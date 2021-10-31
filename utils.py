import requests
from bs4 import BeautifulSoup as bs
import re





def moneyScrapper(url):
    '''
    moneyScrapper -> function scraps data from the money control website

    Arguments
        url - input url to the webpage to be scraped

    Variables
        page -> GET request response
        soup -> BeautifulSoup object to get the HTML structure of the webpage

        heading -> heading of the extracted article
        time_stamp -> data and time of the posting of the article
        image_source -> url of the image posted along the article
        text -> extracted text of the article, from the <p> tags
        article_content -> string of all text from different <p> tags added together

    Return
        a list containing heading, time_stamp, image_source, article_content, url of webpage
    '''


    print('[NOTE] Scraping data from Money Control........')

    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    
    #article heading 
    heading = soup.h1.getText()
    
    #article posting data and time
    time_stamp = re.sub('/', ',', soup.find('div', {'class':'article_schedule'}).get_text())
    
    #article image url
    image_source = soup.find('div', {'class':'article_image'})
    image_source = image_source.find('img').get('data-src')
    
    #article content and text
    article_content = ''
    texts = soup.find_all('p')
    texts = texts[67:]
    for text in texts:
        article_content = article_content + (text.getText())

    # list of extracted information
    return [heading, time_stamp, image_source, article_content, url]





def economicScrapper(url):
    '''
    economicScrapper -> function scraps data from the economic times website

    Arguments
        url - input url to the webpage to be scraped

    Variables
        page -> GET request response
        soup -> BeautifulSoup object to get the HTML structure of the webpage

        heading -> heading of the extracted article
        time_stamp -> data and time of the posting of the article
        image_source -> url of the image posted along the article
        text -> extracted text of the article, from the <p> tags
        article_content -> string of all text from different <p> tags added together

    Return
        a list containing heading, time_stamp, image_source, article_content, url of webpage
    '''

    print('[NOTE] Scrapping data from Economic times......')

    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    #article heading
    heading = soup.h1.getText()

    #article posting date and time
    time_stamp = re.split(':', soup.find('time').get_text(), 1)
    time_stamp = time_stamp[1]
    time_stamp = re.sub('Oct', 'October', time_stamp)       #time_stamp modified in accordance with money control website time_stamp format
    
    #article image
    image_source = '_'                  #economics times articles had no images associated with them
    
    #article content and text
    article_content = soup.find('div', {'class':'artText'})
    article_content = article_content.get_text()

    #list of extracted data
    return [heading, time_stamp, image_source, article_content, url]