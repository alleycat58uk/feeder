import urllib.parse as lp
from os.path import splitext


def get_absolute_url(url: str, fp_url: str) -> str:
    """
    Return a complete, absolute URL for a given URL converting relative urls and fixing a missing scheme

    :param: url feed url
    :param: fp_url feed page url

    :return: absolute url
    :rtype: str
    """
    absolute_url = url.replace(' ', '')
    parsed = lp.urlparse(absolute_url)

    if parsed.netloc == '':
        absolute_url = lp.urljoin(fp_url, url)

    if parsed.scheme in ('', 'http'):
        absolute_url = lp.urlunparse(parsed._replace(scheme='https'))

    return str(absolute_url)


def get_scheme(url: str) -> str:
    """
    Return the filename extension from url or https if not found

    :param url: url to parse

    :return: file extension minus the preceding .
    :rtype: str
    """
    parsed = lp.urlparse(url)
    schema = parsed.scheme if parsed.scheme != '' else 'https'

    return schema


def get_path(url: str) -> str:
    """
    Return the path from url or '' if not found

    :param url: url to parse

    :return: path
    :rtype: str
    """
    parsed = lp.urlparse(url)
    path = parsed.path

    return path


def get_ext(url: str) -> str:
    """
    Return the filename extension from url or '' if not found

    :param url: url to parse

    :return: file extension minus the preceding .
    :rtype: str
    """
    parsed = lp.urlparse(url)
    root, ext = splitext(parsed.path)
    # ext = ext if get_scheme(ext) == '//' else 'http://' + parsed.path[2:]

    return ext[1:]


def is_rss_path(url: str) -> bool:
    """
    Return the path from url or '' if not found

    :param url: url to parse

    :return: path
    :rtype: str
    """
    parsed = lp.urlparse(url)
    rss_path = 'rss' in parsed.path

    return rss_path
