#!/usr/bin/python3
""" Fetch json file from the given website """
import requests
import json
from time import gmtime, strftime
import os
import errno


def to_json(url=None):
    """ Fetches from the web and creates json file """
    if url is None:
        return None
    try:
        folder = "url_to_json"
        headers = {'User-Agent': 'PPP/0.0.1'}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            return None
        js = res.json()

        frmt = "%Y-%m-%d-%H-%M-%S"
        file = "{}.json".format(strftime(frmt, gmtime()))

        filename = "{}/{}".format(folder, file)
        print("\nDone.\nCreated at \"{}\"".format(filename))
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, 'w', encoding="utf-8") as a_files:
            a_files.write(json.dumps(js, indent=2))
    except Exception:
        return None


def is_url(args=None):
    """ Returns true if it is a url else false """
    headers = {'User-Agent': 'PPP/0.0.1'}
    if args is None:
        return None
    try:
        res = requests.get(args, headers=headers)
        if res.status_code == 200:
            return True
        return False
    except Exception:
        return False
