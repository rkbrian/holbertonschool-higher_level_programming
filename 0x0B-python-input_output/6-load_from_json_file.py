#!/usr/bin/python3
"""module for function load_from_json_file"""


import json
def load_from_json_file(filename):
    """function to create an object from the given "JSON file"."""

    with open(filename) as BourneUltimatum:
        Jason = json.load(BourneUltimatum)
        return Jason
