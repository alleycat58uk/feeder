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


def getfeeditems(feed):
    pass


def checkitem(date,url):
    pass


def formatdate(dateformat):
    pass


def saveitem(name,url,region,subject,filter,dateformat):
    pass
