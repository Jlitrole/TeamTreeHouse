import requests
from bs4 import BeautifulSoup
import redis
from secrets import password
import datetime

class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://news.ycombinator.com/').text
        
