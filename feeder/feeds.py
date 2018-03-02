import requests
import json


def addfeed(name,url,region,subject,filter,dateformat):
    pass


def getallfeeds():
    url = "http://127.0.0.1:5984/feeder/_find"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = json.dumps({
        "selector": {
            "type": {
                "$eq": "feed"
            }
        },
        "fields": [
            "name",
            "url",
            "region",
            "subject",
            "filter",
            "date-format"
        ]
    })
    r = requests.post(url, headers=headers, data=payload)
    return json.loads(r.text)['docs']


def getfeeditem(item,feedname,feedregion,feedsubject,feedfilter):
    # set tag name lists for parsing news items
    titletag = ['title']
    descriptiontag = ['description']
    linktag = ['link']
    subjecttag = ['subject', 'category']
    pubdatetag = ['date', 'pubDate']
    # extract required item details
    if item.find(titletag):
        itemtitle = item.find(titletag).contents[0]
    else:
        itemtitle = None
    if item.find(descriptiontag):
        itemdesc = item.find(descriptiontag).contents[0]
    else:
        itemdesc = None
    if item.find(linktag):
        itemlink = item.find(linktag).contents[0]
    else:
        itemlink = None
    if item.find(subjecttag):
        itemsubjects = []
        for subject in item.find_all(subjecttag):
            itemsubjects.append(subject.contents[0])
    else:
        itemsubjects = None
    if item.find(pubdatetag):
        itempubdate = item.find(pubdatetag).contents[0]
    else:
        itempubdate = None
    return json.dumps({'type': 'item',
                      'accessed': {
                          'first': 'today',
                          'last': 'today'
                      },
                      'feed': {'title': feedname,
                               'region': feedregion,
                               'subject': feedsubject,
                               'filter': feedfilter},
                      'item': {'title': itemtitle,
                               'description': itemdesc,
                               'link': itemlink,
                               'subjects': itemsubjects,
                               'pubDate': itempubdate}})


def checkitem(date,url):
    pass


def formatdate(date,dateformat):
    pass


def saveitem(name,url,region,subject,filter,dateformat):
    pass
