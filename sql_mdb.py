import config as cfg
import mysql.connector as ctr


def open_connection():
	cnx = ctr.connect(user=cfg.ro_user, password=cfg.ro_pass, host=cfg.host, database=cfg.db_name)
	return cnx


def close_connection(cnx):
	cnx.close()


def get_org_name_by_id(org_id: int) -> str:
	"""Get the name of an organisation by its id

	:param org_id: organisation id
	:return: name of the organisation name
	:rtype: str
	"""
	pass


def get_org_id_by_name(name: str) -> int:
	"""Get the id of an organisation by its name

	:return: id of the organisation name
	:rtype: int
	"""
	pass


def get_org_ids_by_location(location: str, place_type: str) -> list:
	"""Get a list of organisation ids for a given location

	:param location: name of the location
	:param place_type: continent, region, country or place
	:return: list of all matching organisation ids
	"""
	pass


def get_all_orgs() -> list:
	"""Get a list of all organisation ids

	:return: list of all organisation ids
	:rtype: list
	"""
	pass


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
