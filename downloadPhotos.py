import requests
from bs4 import BeautifulSoup

#define a founction that get text from a html page
def gettext(url, kv=None):
    try:
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failure")
        
#define a founction that scrapy a photo
def scrapy_photo(url,file_name):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        print(r.status_code)
        r.raise_for_status()
        with open(file_name,'wb') as f:
            f.write(r.content)
    except:
        print("error")
        
# get a html page
html = gettext('http://www.ugirls.com/Models/',kv = {'user-agent':'Mozilla/5.0'})
soup = BeautifulSoup(html, 'lxml')
a = soup.find_all('img')
link = []
#get all links 
for i in a:
   link.append(i.attrs['src'])

i = 1
for url in link:
    file_name = "pic{}.jfif".format(i)# name photos
    scrapy_photo(url,file_name)
    i = i + 1
