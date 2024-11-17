import sql_mdb as mdb
import requests
from bs4 import BeautifulSoup
import utilities as util

fp_result = mdb.get_all_feed_pages()

for fp in fp_result:
	fp_id = fp[0]
	fp_url = fp[1]

	response = requests.get(fp_url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.content, "html.parser")
		print('\nTitle:', soup.title.string, fp_url)
		links = soup.find_all("a")

		urlSet = set()

		for link in links:
			if link.has_attr('href') and util.get_ext(link['href']) == 'xml':
				linkUrl = link['href'].strip()
				urlSet.add(util.get_absolute_url(linkUrl, fp_url))
			elif link.has_attr('href') and util.is_rss_path(link['href']):
				linkUrl = link['href'].strip()
				urlSet.add(util.get_absolute_url(linkUrl, fp_url))

		for url in urlSet:
			feed_response = requests.get(url)
			feed_soup = BeautifulSoup(feed_response.content, "xml")
			print(feed_soup.rss['version'])

		# print(urlSet)
