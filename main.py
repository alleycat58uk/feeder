import requests
from bs4 import BeautifulSoup
from requests import RequestException
from feeder import feeds


# get feed urls
allfeeds = feeds.getallfeeds()

# fetch news items
for feed in allfeeds:
    try:
        r = requests.get(feed['url'])
    # TODO: include proper, inclusive exception handling
    except RequestException as e:
        print('Error fetching website')
    else:
        # parse document
        soup = BeautifulSoup(r.text, "xml")
        items = soup.find_all("item")
        for item in items:
            payload = feeds.getfeeditem(item,feed['name'],feed['region'],feed['subject'],feed['filter'],
                                        feed['date-format'])
            rt = requests.post('http://127.0.0.1:5984/feeder', data=payload, headers={'Content-Type': 'application/json'})
            print(rt)
