import requests
from bs4 import BeautifulSoup
from requests import RequestException


# feed urls
# feed = "http://rss.dw.com/rdf/rss-en-all"
feed = "http://feeds.bbci.co.uk/news/rss.xml"
# fetch news items
try:
    r = requests.get(feed)
except RequestException as e:
    print('Error fetching website')
else:
    # set tag name lists for parsing news items
    titleTag = ['title']
    descriptionTag = ['description']
    linkTag = ['link']
    subjectTag = ['subject']
    pubDateTag = ['date', 'pubDate']
    # parse document
    soup = BeautifulSoup(r.text, "xml")
    print(soup.title.contents[0])
    items = soup.find_all("item")
    for item in items:
        if item.find(titleTag):
            itemTitle = item.find(titleTag).contents[0]
        else:
            itemTitle = None
        if item.find(descriptionTag):
            itemDesc = item.find(descriptionTag).contents[0]
        else:
            itemDesc = None
        if item.find(linkTag):
            itemLink = item.find(linkTag).contents[0]
        else:
            itemLink = None
        if item.find(subjectTag):
            itemSubject = item.find(subjectTag).contents[0]
        else:
            itemSubject = None
        if item.find(pubDateTag):
            itemPubDate = item.find(pubDateTag).contents[0]
        else:
            itemPubDate = None
        # print news item
        print(itemTitle)
        print(itemDesc)
        print(itemLink)
        print(itemSubject)
        print(itemPubDate, "\n")
