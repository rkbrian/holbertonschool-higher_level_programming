#!/usr/bin/python3
"""module for function save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """function to write an object to the given file name in JSON format"""

    import json
    with open(filename, mode="w") as BourneSupremacy:
        Jason = json.dumps(my_obj)
        BourneSupremacy.write(Jason)
