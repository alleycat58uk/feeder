import requests
from bs4 import BeautifulSoup
from requests import RequestException


# feed urls
# feed = "http://rss.dw.com/atom/rss-en-all"
feed = "http://rss.dw.com/rdf/rss-en-all"
# fetch news items
try:
    r = requests.get(feed)
except RequestException as e:
    print('Error fetching website')
else:
    soup = BeautifulSoup(r.text, "xml")
    print(soup.title.contents[0])
    items = soup.find_all("item")
    for item in items:
        itemTitle = item.title.contents[0]
        itemDesc = item.description.contents[0]
        itemLink = item.link.contents[0]
        itemSubject = item.subject.contents[0]
        itemPubDate = item.date.contents[0]
        #
        print(itemTitle)
        print(itemDesc)
        print(itemLink)
        print(itemSubject)
        print(itemPubDate, "\n")
