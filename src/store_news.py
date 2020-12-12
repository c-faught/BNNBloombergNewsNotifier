import pandas
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_FILE = 'news.csv'
NEWS_FILE_TEMP = 'news_temp.csv'

def replace_news_csv(dataframe):
    dataframe.to_csv(f"{ROOT_DIR}/{NEWS_FILE}", index=False,sep='|')
    return True

