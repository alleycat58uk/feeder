from itertools import count

import sql_mdb as mdb
import requests
from bs4 import BeautifulSoup
import utilities as util
import pandas as pd

fp_result = mdb.get_all_feed_pages()
all_links = []

for fp in fp_result:
	fp_id = fp[0]
	fp_url = fp[1]
	fp_org_id = fp[2]

	response = requests.get(fp_url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.content, "html.parser")
		links = soup.find_all("a")

		for link in links:
			if link.has_attr('href') and util.get_ext(link['href']) == 'xml':
				linkUrl = link['href'].strip()
				all_links.append([linkUrl, link.text.strip(), fp_id, fp_org_id])
			elif link.has_attr('href') and util.is_rss_path(link['href']):
				linkUrl = link['href'].strip()
				all_links.append([util.get_absolute_url(linkUrl, fp_url), link.text.strip(), fp_id, fp_org_id])

df_links = pd.DataFrame(all_links, columns=['feed_url', 'description', 'feed_page_id', 'organisation_id'])
df_links.drop_duplicates(subset=['feed_url'], inplace=True)

for row in df_links.itertuples(False, None):
	mdb.add_feed(url=row[0], text=row[1], feed_page_id=row[2], org_id=row[3])
	# print(row[0], row[1], row[2], row[3])

print(df_links.shape[0])
