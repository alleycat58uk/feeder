import config as cfg
import mysql.connector as ctr


def open_ro_connection() -> list:
	"""
	Open read only database connection

	:return: list containing connection and cursor objects
	:rtype: list
	"""
	conn = ctr.connect(user=cfg.ro_user, password=cfg.ro_pass, host=cfg.host, database=cfg.db_name)
	curr = conn.cursor()

	return [conn, curr]


def close_ro_connection(conn):
	"""
	Close read only database connection

	:param conn: read only database connection object
	:return:
	"""
	conn.close()


def get_org_name_by_id(org_id: int) -> str:
	"""
	Get the name of an organisation by its id

	:param org_id: organisation id
	:return: name of the organisation name
	:rtype: str
	"""

	ctx = open_ro_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('SELECT name FROM organisations WHERE id = %s', [org_id])

	result = curr.fetchone()[0]
	close_ro_connection(conn)

	return result


def get_org_id_by_name(org_name: str) -> int:
	"""Get the id of an organisation by its name

	:param org_name: name of the organisation
	:return: id of the organisation
	:rtype: int
	"""

	ctx = open_ro_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('SELECT id FROM organisations WHERE name = %s', [org_name])

	result = curr.fetchone()[0]
	close_ro_connection(conn)

	return result


def get_org_ids_by_location(location: str) -> list:
	"""Get a list of organisation ids for a given location

	:param location: name of the location
	:return: list of all matching organisation ids
	"""

	ctx = open_ro_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('SELECT id FROM organisations WHERE')

	result = []
	for id in curr:
		result.append(id)

	close_ro_connection(conn)

	return result


def get_all_org_ids() -> list:
	"""Get a list of all organisation ids

	:return: list of all organisation ids
	:rtype: list
	"""

	ctx = open_ro_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('SELECT id FROM organisations')

	result = []
	for id in curr:
		result.append(id[0])

	close_ro_connection(conn)

	return result


# feed methods

def add_feed(name: str, url: str, organisation: str, location: str, feed_type: str, subject: list = None) -> bool:
	"""Store details of a new feed to the database

	:param name: name of the feed
	:param url: url of the feed
	:param organisation: name of the organisation
	:param subject: list of subjects describing the feed
	:param location: string for the geographical location of the feed
	:param feed_type: code representing the type of feed ie news, video, blog etc.
	:return: true for success, false for failure
	:rtype: bool
	"""
	pass


def update_feed(feed_id: int, name: str = None, url: str = None, organisation: str = None, subject: list = None,
                location: str = None, feed_type: str = None) -> bool:
	"""Update one or more details for a given feed id

	:param feed_id: id of organisation to update
	:param name: name of the feed
	:param url: url of the feed
	:param organisation: name of the organisation for the feed
	:param subject: list of subjects for the feed
	:param location: location of the feed
	:param feed_type: code representing the type of feed ie news, video, blog etc.
	:return: true for success, false for failure
	:rtype: bool
	"""
	pass


def get_all_feeds() -> list:
	"""Get all feed ids

	:return: list of all feed ids
	:rtype: list
	"""
	pass


def get_all_feeds_by_org(org_id: int) -> list:
	"""Get all feed ids for a given organisation

	:param org_id: id for a given organisation
	:return: list of all feed ids
	:rtype: list
	"""
	pass


# utility methods

def format_date(date):
	pass
