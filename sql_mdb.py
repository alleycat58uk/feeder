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


def open_rw_connection() -> list:
	"""
	Open read write database connection

	:return: list containing connection and cursor objects
	:rtype: list
	"""
	conn = ctr.connect(user=cfg.rw_user, password=cfg.rw_pass, host=cfg.host, database=cfg.db_name)
	curr = conn.cursor()

	return [conn, curr]


def close_connection(conn):
	"""
	Close database connection

	:param conn: only database connection object
	"""
	if conn:
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
	close_connection(conn)

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
	close_connection(conn)

	return result


def get_org_ids_by_location(location: str) -> list:
	"""Get a list of organisation ids for a given location

	:param location: name of the location
	:return: list of all matching organisation ids
	"""

	ctx = open_ro_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('SELECT ORG.id FROM organisations ORG INNER JOIN locations LOC WHERE place = %s', location)

	result = []
	for id in curr:
		result.append(id)

	close_connection(conn)

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

	close_connection(conn)

	return result


# feed methods

def add_feed(name: str, url: str, org_id: int, location_id: int = None, feed_type: str = None, subject_id: int = None):
	"""Store details of a new feed to the database

	:param name: name of the feed
	:param url: url of the feed
	:param org_id: id of the organisation
	:param subject: list of subjects describing the feed
	:param location_id: string for the geographical location of the feed
	:param feed_type: code representing the type of feed ie news, video, blog etc.
	:return: true for success, false for failure
	:rtype: bool
	"""
	ctx = open_rw_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('INSERT INTO feeds (name, url, organisation_id, subject_id, location_id, type)'
	             'VALUES (%s, %s, %s, %s, %s, %s)', (name, url, org_id, subject_id, location_id, feed_type)
	)

	close_connection(conn)


def update_feed(feed_id: int, name: str = None, url: str = None, org_id: str = None, subject_id: list = None,
				location_id: str = None, feed_type: str = None):
	"""Update one or more details for a given feed id

	:param feed_id: id of organisation to update
	:param name: name of the feed
	:param url: url of the feed
	:param org_id: name of the organisation for the feed
	:param subject_id: list of subjects for the feed
	:param location_id: location of the feed
	:param feed_type: code representing the type of feed ie news, video, blog etc.
	# :return: true for success, false for failure
	# :rtype: bool
	"""

	ctx = open_rw_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('INSERT INTO feeds (name, url, organisation_id, subject_id, location_id, type)'
				 'VALUES (%s, %s, %s, %s, %s, %s)', (name, url, org_id, subject_id, location_id, feed_type)
	)

	close_connection(conn)


def get_all_feeds_by_org(org_id: int) -> list:
	"""Get all feed ids for a given organisation

	:param org_id: id for a given organisation
	:return: list of all feed ids
	:rtype: list
	"""

	ctx = open_ro_connection()
	conn = ctx[0]
	curr = ctx[1]

	curr.execute('SELECT id FROM feeds WHERE organisation_id = %s', org_id)

	result = []
	for id in curr:
		result.append(id[0])

	close_connection(conn)

	return result


# utility methods

def format_date(date):
	pass
