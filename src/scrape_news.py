from bs4 import BeautifulSoup
from urllib.request import urlopen

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

print(scrape_latest_news('ESI:CT'))

