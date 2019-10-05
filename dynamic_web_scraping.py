#Download the past 10 days files


from selenium import webdriver 
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from selenium import webdriver

# store the path of the chrome driver if the driver is not in the PATH. 
path='/Users/ms/Desktop/chromedriver'

driver = webdriver.Chrome(path)
driver.get("https://public.bitmex.com/?prefix=data/trade/")
time.sleep(10)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
reviews_selector = soup.find_all('a')

for i in range(7,len(reviews_selector)):
    if len(reviews_selector[i].text)==15 and datetime.strptime(reviews_selector[i].text.split('.')[0], '%Y%m%d') >datetime.now()-timedelta(days=10):
        urllib.request.urlretrieve(reviews_selector[i]['href'],reviews_selector[i].text) 
        time.sleep(2)