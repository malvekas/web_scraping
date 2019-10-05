import time 
import requests
import urllib.request
from bs4 import BeautifulSoup


page_source=requests.get("https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/sdn_data.aspx") #making a page request
soup=BeautifulSoup(page_source.text,'lxml') #Creating soup object
a=soup.find('table',{'class':"ms-rteTable-1"}) #Inspect the table from the webpage and find for the type and class of the table

# I want to download 4 files
for i in a.find_all('a'):
    if i.text in ("SDN.CSV","ADD.CSV","ALT.CSV","SDN_COMMENTS.CSV"):
        urllib.request.urlretrieve(i['href'],i.text)
        time.sleep(2)
      