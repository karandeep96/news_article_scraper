import pandas as pd
import re
from utils import moneyScrapper, economicScrapper



def scraper(urls_df):
    '''
    scraper -> function scrapes the data from a given list of urls

    Arguments
        urls_df -> list of urls of websites to be extracted

    Variables
        money_control -> return a regular expression object for the sequence moneycontrol
        economic_times -> return a regular expression object for the sequence economictimes

        output_list -> output list of extracted data from the website
    
    Return
        returns the output_list

    '''
    

    money_control = re.compile(r'moneycontrol')
    economic_times = re.compile(r'economictimes')

    output_list = []

    
    for url in urls_df:

        #check if the given url is from money control
        if money_control.search(url):
            output_list.append(moneyScrapper(url))

        #check if the given url is from money control
        else:
            output_list.append(economicScrapper(url))

    return output_list




if __name__ == '__main__':

    # read the csv file with the given urls
    urls_df = pd.read_csv('/home/karandeep/Downloads/web_scraping/urls.csv')

    #convert the dataframe to list
    urls_df = list(urls_df['web_urls'])

    #extract the data in the form of a list
    output_list = scraper(urls_df)

    #create a dataframe of the extraceted data
    output_data = pd.DataFrame(output_list, columns=['heading', 'time_stamp', 'image_urls', 'article_content', 'source_url'])

    # save the extracted data to a csv file
    output_data.to_csv('scraped_data.csv')