import requests
from bs4 import BeautifulSoup
from requests import RequestException
import json


# feed urls
feed = ["http://www.france24.com/en/top-stories/rss",
        "http://rss.dw.com/rdf/rss-en-all",
        "http://feeds.bbci.co.uk/news/rss.xml",
        "https://feeds.feedburner.com/Torrentfreak"]
# fetch news items
try:
    r = requests.get(feed[0])
except RequestException as e:
    print('Error fetching website')
else:
    # set tag name lists for parsing news items
    titleTag = ['title']
    descriptionTag = ['description']
    linkTag = ['link']
    subjectTag = ['subject', 'category']
    pubDateTag = ['date', 'pubDate']
    # parse document
    soup = BeautifulSoup(r.text, "xml")
    feedTitle = soup.title.contents[0]
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
            itemSubjects = []
            for subject in item.find_all(subjectTag):
                itemSubjects.append(subject.contents[0])
        else:
            itemSubjects = None
        if item.find(pubDateTag):
            itemPubDate = item.find(pubDateTag).contents[0]
        else:
            itemPubDate = None
        # print news item
        # print(itemTitle)
        # print(itemDesc)
        # print(itemLink)
        # print(itemSubjects)
        # print(itemPubDate, "\n")
        payload = json.dumps({'feed': {'title': feedTitle},
                              'item': {'title': itemTitle,
                                       'description': itemDesc,
                                       'link': itemLink,
                                       'subjects': itemSubjects,
                                       'pubDate': itemPubDate}})
        rt = requests.post('http://127.0.0.1:5984/feeder', data=payload, headers={'Content-Type': 'application/json'})
        print(rt)
