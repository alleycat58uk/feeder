import requests
import json


def add_feed(name, url, region, subject, filter, dateformat):
    pass


def update_feed():
    pass


def get_all_feeds():
    url = "http://127.0.0.1:5984/feedr/_find"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    payload = json.dumps({
        "selector": {
            "feeds": {
                "$exists": True
            }
        },
        "fields": [
            "organisation",
            "feeds"
        ]
    })
    r = requests.post(url, headers=headers, data=payload)
    # TODO: handle an empty request
    return json.loads(r.text)['docs']


def get_feed_items(feedurl):
    data = None
    r = requests.get(feedurl)
    if r.status_code is 200:
        # process items
        data = r.text
    elif r.status_code is 301:
        data = 301
        # update feed url
    elif r.status_code is 404:
        data = 404
    return data


def check_item(date, url):
    pass


def format_date(dateformat):
    pass


def save_item(name, url, region, subject, filter, dateformat):
    pass
