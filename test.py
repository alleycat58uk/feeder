import sql_mdb as mdb
import nosql_cdb as cdb
# from urllib.parse import urlparse
# from urllib.parse import urljoin
# from urllib.parse import urlunparse
import urllib.parse as lp
import utilities as util
import config as cfg


# -------------------------------------------------

# test read only connection
# cnx = mdb.open_ro_connection()
#
# cur = cnx[1]
# con = cnx[0]
#
# cur.execute("SELECT * FROM organisations")
#
# for result in cur:
# 	print(result)
#
# mdb.close_connection(con, cur)

# -------------------------------------------------

# test read write connection
# cnx = mdb.open_rw_connection()
#
# cur = cnx[1]
# con = cnx[0]
#
# cur.execute("INSERT INTO locations (place, type) VALUES ('United Kingdom', 'Country')")
# cur.execute("INSERT INTO organisations (short_name, name, state_funded, location_id) \
# 			VALUES ('BBC', 'British Broadcasting Corporation', 'Y', 1)")
#
# con.commit()
#
# mdb.close_connection(con, cur)

# -------------------------------------------------

# url = '//www.bbc.co.uk/blogs/theeditors/rss.xml'
# fp_url = 'https://www.cbsnews.com/rss'
#
# parsed = lp.urlparse(url)
# print(parsed)
# if parsed.netloc == '':
# 	print(lp.urljoin(fp_url, url))
#
# if parsed.scheme != 'https':
# 	print(lp.urlunparse(parsed._replace(scheme='https')))

# -------------------------------------------------

# url = 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15837362'
# print(lp.urlparse(url))
# print(util.get_ext(url))

# -------------------------------------------------

print(cdb.get_guids())
