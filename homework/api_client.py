"""Minimal api_client placeholder for homework tests."""

import requests


def ping(url):
    try:
        r = requests.get(url)
        return r.status_code
    except Exception:
        return None
