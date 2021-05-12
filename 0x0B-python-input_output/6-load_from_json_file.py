#!/usr/bin/python3
"""module for function load_from_json_file"""


def load_from_json_file(filename):
    """function to create an object from the given "JSON file"."""

    import json
    with open(filename) as BourneUltimatum:
        Jason = json.load(BourneUltimatum)
        return Jason
