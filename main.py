import requests
from bs4 import BeautifulSoup
from requests import RequestException
import json
from feeder import feeds


# get feed urls
feeds = feeds.getallfeeds()

# fetch news items
for feed in feeds:
    try:
        r = requests.get(feed['url'])
    # TODO: include proper, inclusive exception handling
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

            # check if item already exists
            # - criteria: feed title, url, itemTitle
            # no - create record
            # yes - amend (inc. last date accessed)

            # store new item
            payload = json.dumps({'type': 'item',
                                  'accessed': {
                                      'first': 'today',
                                      'last': 'today'
                                  },
                                  'feed': {'title': feed['name'],
                                           'region': feed['region'],
                                           'subject': feed['subject'],
                                           'filter': feed['filter']},
                                  'item': {'title': itemTitle,
                                           'description': itemDesc,
                                           'link': itemLink,
                                           'subjects': itemSubjects,
                                           'pubDate': itemPubDate}})
            rt = requests.post('http://127.0.0.1:5984/feeder', data=payload, headers={'Content-Type': 'application/json'})
            print(rt)
