from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def scrape_latest_news(stock_code):
    page_url = f"https://www.bnnbloomberg.ca/stock/{stock_code}#/News"
    
    #----------capture latest news post----------#
    page = urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')
    news = soup.find("li", {"class": "0 feed-item index-1"})

    #----------capture news content----------#
    article_content = news.find("div",{"class": "article-content"})
    title = article_content.find('h3').text
    url = article_content.a.get('href')

    #----------capture article date----------#
    date = news.find("div",{"class": "date"}).text.strip()

    #----------capture article category----------#
    article_category = news.find("li",{"class": "highlighted"})
    category = article_category.find('h4').text

    return date, title, url, category

def compare_tuple(t1,t2):
    return t1 == t2

def main():
    #load news file in csv
    df = pd.read_csv(f"{ROOT_DIR}/user/news.csv",sep='\|', engine='python')
    #iterate each row
    for index, row in df.iterrows():
        #----------scrape BNNBloomberg stock for latest news----------#
        stock = row['Stock']
        latest_news_tuple = scrape_latest_news(stock)
        latest_news_tuple = (stock,) + latest_news_tuple #add stock to tuple
        previous_news_tuple = tuple(row)
        
        #----------check if news has changed----------#
        if not compare_tuple(latest_news_tuple,previous_news_tuple):
            #TBD email
            #----------update news table data----------#
            df.loc[index]=latest_news_tuple
main()