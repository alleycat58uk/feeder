import config as cfg
import json
import requests


def get_query_url(path: str = '') -> str:
    
    url = cfg.nosql_host + ':' + cfg.nosql_port + '/' + cfg.nosql_db_name + path

    return url


def get_guids() -> str:
    r = requests.get(get_query_url('/_design/test-guid/_view/vw-test-guid'), auth=(cfg.nossql_user, cfg.nosql_pass))
    
    return r.text
